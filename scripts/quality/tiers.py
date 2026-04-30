"""
Tier implementations.

Tier 1 — Structural        : coverage, field completeness, empty docs
Tier 2 — Content fidelity  : char retention, heading/code/table preservation
Tier 3 — Link integrity    : internal link & image resolution rates

Tier 4 (URL liveness) and Tier 5 (QA answerability) are scaffolded as TODOs at
the bottom of this file.
"""

from __future__ import annotations

import re
from typing import List

from .framework import (
    Tier, CheckResult, Finding, INFO, WARN, FAIL,
)

# Regexes for content fidelity (kept here so each tier file is self-contained
# from a reading perspective).
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
FENCE_RE = re.compile(r"^```", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def _strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


# ---------------------------------------------------------------------------
# Tier 1 — Structural
# ---------------------------------------------------------------------------

class StructuralTier(Tier):
    name = "structural"
    weight = 0.20

    def run(self) -> List[CheckResult]:
        ctx = self.ctx
        checks: List[CheckResult] = []

        # 1a. Doc count parity (record count == raw md count)
        raw_n = len(ctx.raw_md_files)
        rec_n = len(ctx.records)
        coverage_score = 100.0 if raw_n == rec_n else max(0.0, (min(raw_n, rec_n) / max(raw_n, rec_n)) * 100)
        checks.append(CheckResult(
            name="doc_count_parity",
            score=coverage_score,
            weight=2.0,
            summary=f"records={rec_n} vs source .md files={raw_n}",
            findings=[] if raw_n == rec_n else [Finding(
                severity=FAIL, tier=self.name, check="doc_count_parity",
                message=f"Mismatch: {rec_n} records but {raw_n} source files",
            )],
        ))

        # 1b. Required fields populated
        required = ["id", "title", "path", "public_url"]
        missing = []
        for r in ctx.records:
            for f in required:
                if not r.get(f):
                    missing.append(Finding(
                        severity=FAIL, tier=self.name, check="required_fields",
                        message=f"Missing required field '{f}'",
                        doc_id=r.get("id") or r.get("path"),
                    ))
        ok = len(ctx.records) - len({f.doc_id for f in missing})
        checks.append(self.ratio_check(
            "required_fields", ok, len(ctx.records),
            weight=2.0,
            summary_fmt="{ok}/{total} docs have all required fields ({pct:.1f}%)",
            findings=missing,
        ))

        # 1c. Empty / near-empty content (warn-only — some source docs are stubs)
        TINY = 40
        tiny_docs = [r for r in ctx.records if len((r.get("content") or "").strip()) < TINY]
        findings = [Finding(
            severity=WARN, tier=self.name, check="empty_content",
            message=f"Content is {len(r['content'].strip())} chars (<{TINY})",
            doc_id=r["id"],
        ) for r in tiny_docs]
        ok = len(ctx.records) - len(tiny_docs)
        checks.append(self.ratio_check(
            "empty_content", ok, len(ctx.records),
            weight=1.0,
            summary_fmt="{ok}/{total} docs have non-trivial content ({pct:.1f}%)",
            findings=findings,
        ))

        # 1d. Section assignment (every doc should ideally be inside a SUMMARY section)
        sectioned = sum(1 for r in ctx.records if r.get("section"))
        checks.append(self.ratio_check(
            "section_assigned", sectioned, len(ctx.records),
            weight=1.0,
            summary_fmt="{ok}/{total} docs assigned to a section ({pct:.1f}%)",
        ))

        return checks


# ---------------------------------------------------------------------------
# Tier 2 — Content fidelity
# ---------------------------------------------------------------------------

class ContentFidelityTier(Tier):
    name = "content_fidelity"
    weight = 0.25

    def run(self) -> List[CheckResult]:
        ctx = self.ctx
        checks: List[CheckResult] = []

        # Build: rel_path -> raw text (frontmatter stripped)
        raw_by_path = {
            p.relative_to(ctx.repo_root).as_posix():
                _strip_frontmatter(p.read_text(encoding="utf-8", errors="replace"))
            for p in ctx.raw_md_files
        }

        # 2a. Char retention (extracted/raw, capped at 100). HTML stripping
        # reasonably costs ~10%, so we score as-is and warn under 70%.
        per_doc_retention = []
        retention_findings: List[Finding] = []
        for r in ctx.records:
            raw = raw_by_path.get(r["path"], "")
            extracted = r.get("content") or ""
            if len(raw) < 50:
                continue  # skip stubs
            ratio = min(len(extracted) / len(raw), 1.0) if len(raw) else 1.0
            per_doc_retention.append(ratio)
            if ratio < 0.70:
                retention_findings.append(Finding(
                    severity=WARN, tier=self.name, check="char_retention",
                    message=f"Retention {ratio*100:.0f}% (extracted={len(extracted)} / raw={len(raw)})",
                    doc_id=r["id"],
                ))
        avg_retention = (sum(per_doc_retention) / len(per_doc_retention) * 100) if per_doc_retention else 100.0
        checks.append(CheckResult(
            name="char_retention",
            score=min(100.0, avg_retention),
            weight=1.0,
            summary=f"avg retention {avg_retention:.1f}% across {len(per_doc_retention)} docs",
            findings=retention_findings,
        ))

        # 2b. Heading preservation (count of #...###### should match raw)
        heading_findings: List[Finding] = []
        ok = 0
        total = 0
        for r in ctx.records:
            raw = raw_by_path.get(r["path"], "")
            if not raw:
                continue
            total += 1
            raw_count = len(HEADING_RE.findall(raw))
            ext_count = len(r.get("headings") or [])
            # Allow ±1 slack for edge cases (heading inside a code fence, etc.)
            if abs(raw_count - ext_count) <= 1:
                ok += 1
            else:
                heading_findings.append(Finding(
                    severity=WARN, tier=self.name, check="heading_preservation",
                    message=f"Headings raw={raw_count} extracted={ext_count}",
                    doc_id=r["id"],
                ))
        checks.append(self.ratio_check(
            "heading_preservation", ok, total,
            weight=1.5,
            summary_fmt="{ok}/{total} docs preserve heading count ({pct:.1f}%)",
            findings=heading_findings,
        ))

        # 2c. Code fence preservation (count of ``` lines should match raw)
        fence_findings: List[Finding] = []
        ok = 0
        total = 0
        for r in ctx.records:
            raw = raw_by_path.get(r["path"], "")
            if not raw:
                continue
            raw_fences = len(FENCE_RE.findall(raw))
            if raw_fences == 0:
                continue  # nothing to check
            total += 1
            ext_fences = len(FENCE_RE.findall(r.get("content") or ""))
            if raw_fences == ext_fences:
                ok += 1
            else:
                fence_findings.append(Finding(
                    severity=WARN, tier=self.name, check="code_fence_preservation",
                    message=f"Code fences raw={raw_fences} extracted={ext_fences}",
                    doc_id=r["id"],
                ))
        checks.append(self.ratio_check(
            "code_fence_preservation", ok, total,
            weight=1.0,
            summary_fmt="{ok}/{total} docs preserve code fences ({pct:.1f}%)",
            findings=fence_findings,
        ))

        # 2d. Markdown table preservation
        table_findings: List[Finding] = []
        ok = 0
        total = 0
        for r in ctx.records:
            raw = raw_by_path.get(r["path"], "")
            if not raw:
                continue
            raw_rows = len(TABLE_ROW_RE.findall(raw))
            if raw_rows == 0:
                continue
            total += 1
            ext_rows = len(TABLE_ROW_RE.findall(r.get("content") or ""))
            # Tables can lose ±2 lines via cleanup; tolerate small drift
            if ext_rows >= raw_rows - 2:
                ok += 1
            else:
                table_findings.append(Finding(
                    severity=WARN, tier=self.name, check="table_preservation",
                    message=f"Table rows raw={raw_rows} extracted={ext_rows}",
                    doc_id=r["id"],
                ))
        checks.append(self.ratio_check(
            "table_preservation", ok, total,
            weight=1.0,
            summary_fmt="{ok}/{total} docs with tables preserve them ({pct:.1f}%)",
            findings=table_findings,
        ))

        return checks


# ---------------------------------------------------------------------------
# Tier 3 — Link integrity
# ---------------------------------------------------------------------------

class LinkIntegrityTier(Tier):
    name = "link_integrity"
    weight = 0.20

    def run(self) -> List[CheckResult]:
        ctx = self.ctx
        checks: List[CheckResult] = []

        # 3a. Internal-doc link resolution (target_doc_id present)
        internal = [(r, l) for r in ctx.records for l in r.get("links", [])
                    if l.get("kind") == "internal-doc"]
        ok = sum(1 for _, l in internal if l.get("target_doc_id"))
        dangling = [Finding(
            severity=FAIL, tier=self.name, check="internal_doc_resolution",
            message=f"Unresolved internal-doc link: {l['href']}",
            doc_id=r["id"],
        ) for r, l in internal if not l.get("target_doc_id")]
        checks.append(self.ratio_check(
            "internal_doc_resolution", ok, len(internal),
            weight=2.0,
            summary_fmt="{ok}/{total} internal-doc links resolve ({pct:.1f}%)",
            findings=dangling,
        ))

        # 3b. Internal-asset image resolution (target_path present)
        imgs = [(r, i) for r in ctx.records for i in r.get("images", [])
                if i.get("kind") == "internal-asset"]
        ok = sum(1 for _, i in imgs if i.get("target_path"))
        bad_imgs = [Finding(
            severity=WARN, tier=self.name, check="internal_image_resolution",
            message=f"Unresolved image: {i['href']}",
            doc_id=r["id"],
        ) for r, i in imgs if not i.get("target_path")]
        checks.append(self.ratio_check(
            "internal_image_resolution", ok, len(imgs),
            weight=1.0,
            summary_fmt="{ok}/{total} image references resolve ({pct:.1f}%)",
            findings=bad_imgs,
        ))

        # 3c. Total unresolved-kind links — should be near zero
        unresolved = [(r, l) for r in ctx.records
                      for l in (r.get("links", []) + r.get("images", []))
                      if l.get("kind") == "unresolved"]
        total_links = sum(len(r.get("links", [])) + len(r.get("images", []))
                          for r in ctx.records)
        ok = total_links - len(unresolved)
        unres_findings = [Finding(
            severity=WARN, tier=self.name, check="unresolved_links",
            message=f"Unresolved link/image: {l['href']}",
            doc_id=r["id"],
        ) for r, l in unresolved[:30]]
        checks.append(self.ratio_check(
            "unresolved_links", ok, total_links,
            weight=1.5,
            summary_fmt="{ok}/{total} links/images classified non-unresolved ({pct:.1f}%)",
            findings=unres_findings,
        ))

        # 3d. Citation coverage — every doc has a links.json entry
        in_map = sum(1 for r in ctx.records if r["id"] in ctx.links_map)
        checks.append(self.ratio_check(
            "citation_map_coverage", in_map, len(ctx.records),
            weight=1.0,
            summary_fmt="{ok}/{total} docs present in links.json ({pct:.1f}%)",
        ))

        return checks


# ---------------------------------------------------------------------------
# Future tiers (scaffold)
# ---------------------------------------------------------------------------

class CitationLivenessTier(Tier):
    """Tier 4 — opt-in. HEADs every public_url to verify it returns 200.
    Not implemented yet; will be added once we decide whether to run it in CI.
    """
    name = "citation_liveness"
    weight = 0.15

    def run(self) -> List[CheckResult]:
        return []  # TODO


class QAAnswerabilityTier(Tier):
    """Tier 5 — needs a curated questions.yaml file. Not implemented yet."""
    name = "qa_answerability"
    weight = 0.20

    def run(self) -> List[CheckResult]:
        return []  # TODO


ACTIVE_TIERS = [StructuralTier, ContentFidelityTier, LinkIntegrityTier]
