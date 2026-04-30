"""
Quality framework primitives: Tier base class, Check/TierResult dataclasses,
weighted scoring, and a markdown/JSON reporter.

A Tier runs one or more Checks. Each Check returns a score 0-100 and optional
findings. The Tier score is the weighted average of its checks (or simple
mean if weights aren't set). The overall report score is the weighted average
of tier scores.

Designed so Tiers 4 (URL liveness) and 5 (QA answerability) can be added
later by subclassing Tier and registering with the runner — no changes
required to the framework itself.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional


# ---------------------------------------------------------------------------
# Severity / verdict constants
# ---------------------------------------------------------------------------

INFO = "info"
WARN = "warn"
FAIL = "fail"

VERDICT_PASS = "PASS"
VERDICT_WARN = "WARN"
VERDICT_FAIL = "FAIL"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    severity: str        # 'info' | 'warn' | 'fail'
    tier: str
    check: str
    message: str
    doc_id: Optional[str] = None
    detail: Optional[Dict] = None


@dataclass
class CheckResult:
    name: str
    score: float                       # 0-100
    weight: float = 1.0
    summary: str = ""
    findings: List[Finding] = field(default_factory=list)


@dataclass
class TierResult:
    name: str
    weight: float
    score: float
    checks: List[CheckResult] = field(default_factory=list)
    skipped: bool = False
    skip_reason: Optional[str] = None


@dataclass
class QualityReport:
    overall_score: float
    verdict: str
    generated_at: str
    tiers: List[TierResult]
    findings: List[Finding]


# ---------------------------------------------------------------------------
# Tier base class
# ---------------------------------------------------------------------------

class Tier:
    """Base class. Subclass and implement `run()` returning a list of CheckResults."""

    name: str = "unnamed"
    weight: float = 1.0

    def __init__(self, ctx: "QualityContext"):
        self.ctx = ctx

    # Override
    def run(self) -> List[CheckResult]:
        raise NotImplementedError

    # Convenience: build a CheckResult from a numerator/denominator
    @staticmethod
    def ratio_check(name: str, ok: int, total: int, *, weight: float = 1.0,
                    summary_fmt: str = "{ok}/{total} ({pct:.1f}%)",
                    findings: Optional[List[Finding]] = None) -> CheckResult:
        if total == 0:
            score = 100.0
            summary = f"{name}: nothing to check (n=0)"
        else:
            score = (ok / total) * 100.0
            summary = summary_fmt.format(ok=ok, total=total, pct=score)
        return CheckResult(name=name, score=score, weight=weight,
                           summary=summary, findings=findings or [])


# ---------------------------------------------------------------------------
# Context shared by tiers (parsed inputs)
# ---------------------------------------------------------------------------

@dataclass
class QualityContext:
    repo_root: Path
    dist_dir: Path
    records: List[Dict]                       # parsed jsonl
    links_map: Dict[str, Dict]                # parsed links.json
    raw_md_files: List[Path]                  # source markdown (for fidelity checks)


def load_context(repo_root: Path, dist_dir: Path) -> QualityContext:
    jsonl = dist_dir / "toolkit.jsonl"
    links = dist_dir / "links.json"
    if not jsonl.exists():
        raise FileNotFoundError(f"Missing {jsonl}. Run extract.py first.")
    if not links.exists():
        raise FileNotFoundError(f"Missing {links}. Run extract.py first.")

    # NOTE: read line-by-line via the file iterator (which only splits on '\n')
    # rather than str.splitlines(), which also splits on U+2028/U+2029 — those
    # can legally appear inside JSON string values and would corrupt the parse.
    records = []
    with jsonl.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.strip():
                records.append(json.loads(line))
    links_map = json.loads(links.read_text(encoding="utf-8"))

    # Source markdown files — same exclusion rules as the extractor
    raw_files: List[Path] = []
    for md in repo_root.rglob("*.md"):
        parts = md.relative_to(repo_root).parts
        if any(p.startswith(".") for p in parts):
            continue
        if parts and parts[0] == "scripts":
            continue
        if parts == ("SUMMARY.md",):
            continue
        raw_files.append(md)
    raw_files.sort()

    return QualityContext(
        repo_root=repo_root,
        dist_dir=dist_dir,
        records=records,
        links_map=links_map,
        raw_md_files=raw_files,
    )


# ---------------------------------------------------------------------------
# Runner + scoring
# ---------------------------------------------------------------------------

def run_tier(tier: Tier) -> TierResult:
    try:
        checks = tier.run()
    except Exception as e:  # never let one tier crash the report
        return TierResult(
            name=tier.name, weight=tier.weight, score=0.0, checks=[],
            skipped=True, skip_reason=f"crashed: {e!r}",
        )

    if not checks:
        return TierResult(name=tier.name, weight=tier.weight, score=100.0, checks=[])

    total_w = sum(c.weight for c in checks) or 1.0
    score = sum(c.score * c.weight for c in checks) / total_w
    return TierResult(name=tier.name, weight=tier.weight, score=score, checks=checks)


def assemble_report(tier_results: List[TierResult]) -> QualityReport:
    # Overall: weighted by tier weight, ignoring skipped tiers
    active = [t for t in tier_results if not t.skipped]
    if active:
        total_w = sum(t.weight for t in active) or 1.0
        overall = sum(t.score * t.weight for t in active) / total_w
    else:
        overall = 0.0

    # Verdict thresholds
    if overall >= 90 and all(t.score >= 75 for t in active):
        verdict = VERDICT_PASS
    elif overall < 75 or any(t.score < 50 for t in active):
        verdict = VERDICT_FAIL
    else:
        verdict = VERDICT_WARN

    findings: List[Finding] = []
    for t in tier_results:
        for c in t.checks:
            findings.extend(c.findings)

    return QualityReport(
        overall_score=round(overall, 1),
        verdict=verdict,
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        tiers=tier_results,
        findings=findings,
    )


# ---------------------------------------------------------------------------
# Reporters
# ---------------------------------------------------------------------------

def write_json_report(report: QualityReport, path: Path) -> None:
    def _ser(obj):
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        raise TypeError(f"not serialisable: {type(obj)}")
    path.write_text(
        json.dumps(asdict(report), default=_ser, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_markdown_report(report: QualityReport, path: Path) -> None:
    lines: List[str] = []
    lines.append(f"# Toolkit Extraction Quality Report")
    lines.append("")
    lines.append(f"**Overall score:** {report.overall_score:.1f}/100  ")
    lines.append(f"**Verdict:** `{report.verdict}`  ")
    lines.append(f"**Generated:** {report.generated_at}")
    lines.append("")
    lines.append("## Tier scores")
    lines.append("")
    lines.append("| Tier | Weight | Score | Status |")
    lines.append("| --- | ---: | ---: | --- |")
    for t in report.tiers:
        if t.skipped:
            lines.append(f"| {t.name} | {t.weight:.0%} | — | skipped ({t.skip_reason}) |")
        else:
            status = "✅" if t.score >= 90 else ("⚠️" if t.score >= 75 else "❌")
            lines.append(f"| {t.name} | {t.weight:.0%} | {t.score:.1f} | {status} |")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for t in report.tiers:
        if t.skipped:
            continue
        lines.append(f"### {t.name}  *(score {t.score:.1f})*")
        lines.append("")
        for c in t.checks:
            lines.append(f"- **{c.name}** — {c.score:.1f}/100 — {c.summary}")
        lines.append("")
    if report.findings:
        warn = [f for f in report.findings if f.severity == WARN]
        fail = [f for f in report.findings if f.severity == FAIL]
        if fail:
            lines.append("## ❌ Failures")
            lines.append("")
            for f in fail[:50]:
                tail = f" *(doc: `{f.doc_id}`)*" if f.doc_id else ""
                lines.append(f"- [{f.tier}/{f.check}] {f.message}{tail}")
            if len(fail) > 50:
                lines.append(f"- …and {len(fail) - 50} more")
            lines.append("")
        if warn:
            lines.append("## ⚠️ Warnings")
            lines.append("")
            for f in warn[:50]:
                tail = f" *(doc: `{f.doc_id}`)*" if f.doc_id else ""
                lines.append(f"- [{f.tier}/{f.check}] {f.message}{tail}")
            if len(warn) > 50:
                lines.append(f"- …and {len(warn) - 50} more")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
