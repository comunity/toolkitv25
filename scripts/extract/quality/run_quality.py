#!/usr/bin/env python3
"""
Extraction Quality Runner
=========================

Orchestrates the quality tiers, computes a weighted overall score, and writes
both a JSON and Markdown report.

Usage (from repo root):
    python3 scripts/extract/quality/run_quality.py
    python3 scripts/extract/quality/run_quality.py --strict   # exit 1 on FAIL/WARN

Reads:
    scripts/extract/dist/toolkit.jsonl
    scripts/extract/dist/links.json

Writes:
    scripts/extract/dist/quality-report.json
    scripts/extract/dist/quality-report.md

Exit codes:
    0  — PASS (or WARN, unless --strict)
    1  — FAIL (or WARN with --strict)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running as a module OR as a script
try:
    from .framework import (
        load_context, run_tier, assemble_report,
        write_json_report, write_markdown_report,
        VERDICT_PASS, VERDICT_WARN, VERDICT_FAIL,
    )
    from .tiers import ACTIVE_TIERS
except ImportError:
    # Script invocation: add parent to path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))
    from scripts.extract.quality.framework import (  # type: ignore
        load_context, run_tier, assemble_report,
        write_json_report, write_markdown_report,
        VERDICT_PASS, VERDICT_WARN, VERDICT_FAIL,
    )
    from scripts.extract.quality.tiers import ACTIVE_TIERS  # type: ignore


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run extraction quality tiers and emit a report.")
    ap.add_argument("--root", default=".", help="Repo root (default: cwd)")
    ap.add_argument("--dist", default="scripts/extract/dist",
                    help="Directory containing toolkit.jsonl and links.json")
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1 on WARN as well as FAIL")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    dist = (root / args.dist).resolve() if not Path(args.dist).is_absolute() else Path(args.dist)

    ctx = load_context(root, dist)
    print(f"[quality] loaded {len(ctx.records)} records, {len(ctx.links_map)} link entries", file=sys.stderr)

    tier_results = [run_tier(cls(ctx)) for cls in ACTIVE_TIERS]
    report = assemble_report(tier_results)

    json_path = dist / "quality-report.json"
    md_path = dist / "quality-report.md"
    write_json_report(report, json_path)
    write_markdown_report(report, md_path)

    print(f"[quality] overall {report.overall_score:.1f}/100  verdict={report.verdict}", file=sys.stderr)
    print(f"[quality] report → {md_path.relative_to(root)}", file=sys.stderr)
    for t in report.tiers:
        if t.skipped:
            print(f"  - {t.name}: skipped ({t.skip_reason})", file=sys.stderr)
        else:
            print(f"  - {t.name}: {t.score:.1f}/100", file=sys.stderr)

    if report.verdict == VERDICT_FAIL:
        return 1
    if report.verdict == VERDICT_WARN and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
