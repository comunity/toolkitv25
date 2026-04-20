#!/usr/bin/env python3
"""
ComUnity Toolkit Docs Extractor
================================

Walks a GitBook-style markdown repo (ComUnity Toolkit) and emits three
LLM-friendly artifacts under `dist/`:

  1. toolkit.jsonl  — one JSON record per markdown doc, with cleaned content,
                      headings, resolved links, and images.
  2. links.json     — citation map keyed by doc id: {title, source_path,
                      public_url}. Includes images/assets too.
  3. toolkit.txt    — concatenated corpus with <doc ...> delimiters, suitable
                      for simple context-stuffing.

Design goals:
  * Python stdlib only (works on any GitHub Actions runner out of the box).
  * Deterministic output (sorted keys, stable ids) so diffs are meaningful.
  * No mutation of the source repo.

Usage:
  python3 scripts/extract/extract.py \
      --root "." \
      --out  "scripts/extract/dist" \
      --base-url "https://comunity.gitbook.io/learning.comunityplatform/25.x"

All flags have sensible defaults assuming the script is run from the repo root.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse, quote

# ---------------------------------------------------------------------------
# Config / constants
# ---------------------------------------------------------------------------

DEFAULT_BASE_URL = "https://comunity.gitbook.io/learning.comunityplatform/25.x"

# File extensions we classify as "assets" (vs markdown docs).
ASSET_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".avif", ".mov",
              ".mp4", ".webp", ".pdf", ".docx", ".xlsx", ".pptx"}

MARKDOWN_EXT = ".md"

# Regexes
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
MD_LINK_RE = re.compile(r"(?<!\!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_IMG_SRC_RE = re.compile(r"<img\s+[^>]*src=\"([^\"]+)\"", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<[^>]+>")
# GitBook escape: &#x20; (non-breaking space-ish), backslash line breaks, etc.
GITBOOK_NBSP_RE = re.compile(r"&#x20;")
BACKSLASH_EOL_RE = re.compile(r"\\(\s*\n)")
MULTI_BLANK_RE = re.compile(r"\n{3,}")


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class LinkRef:
    text: str
    href: str                      # as written in the markdown
    target_path: Optional[str]     # repo-relative path if internal, else None
    target_doc_id: Optional[str]   # doc id if resolves to a known doc
    public_url: Optional[str]      # absolute URL (gitbook or external)
    kind: str                      # 'internal-doc' | 'internal-asset' | 'external' | 'anchor' | 'unresolved'


@dataclass
class DocRecord:
    id: str
    title: str
    section: Optional[str]
    path: str                      # repo-relative source path
    public_url: str
    headings: List[Dict[str, object]] = field(default_factory=list)
    content: str = ""
    links: List[Dict] = field(default_factory=list)
    images: List[Dict] = field(default_factory=list)
    frontmatter: Dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def rel_posix(p: Path, root: Path) -> str:
    """Return POSIX-style repo-relative path."""
    return p.relative_to(root).as_posix()


def doc_id_from_path(rel: str) -> str:
    """Stable id: strip .md, collapse trailing /README to folder name."""
    if rel.endswith("/README.md"):
        rel = rel[: -len("/README.md")]
    elif rel == "README.md":
        return "index"
    elif rel.endswith(MARKDOWN_EXT):
        rel = rel[: -len(MARKDOWN_EXT)]
    return rel


def public_url_for(rel: str, base_url: str) -> str:
    """Map repo path to GitBook public URL.

    GitBook URL convention (standard sites):
      README.md                   -> <base>/
      foo/README.md               -> <base>/foo
      foo/bar.md                  -> <base>/foo/bar
      assets under .gitbook/...   -> <base>/<path> (left as-is; GitBook serves
                                     them via the same host, though the exact
                                     asset URL can differ between sites. We
                                     keep this as a best-effort reference.)
    """
    base = base_url.rstrip("/")
    if rel == "README.md":
        return base + "/"
    if rel.endswith("/README.md"):
        slug = rel[: -len("/README.md")]
    elif rel.endswith(MARKDOWN_EXT):
        slug = rel[: -len(MARKDOWN_EXT)]
    else:
        slug = rel
    # URL-encode each path segment but keep '/'
    parts = [quote(seg, safe="") for seg in slug.split("/")]
    return base + "/" + "/".join(parts)


def is_external(href: str) -> bool:
    if href.startswith(("http://", "https://", "mailto:", "tel:")):
        return True
    parsed = urlparse(href)
    return bool(parsed.scheme and parsed.scheme not in ("",))


def normalize_internal(src_path: Path, root: Path, href: str) -> Optional[str]:
    """Resolve a relative href from src_path to a repo-relative POSIX path.
    Returns None if it escapes the repo or is not resolvable.

    Folder-style hrefs (e.g. `foo/bar/` or `../observability/`) are resolved
    to `<folder>/README.md` when that file exists — this is how GitBook
    links from one section to another's index page.
    """
    if not href or href.startswith("#"):
        return None
    # Strip fragment/query for file resolution (fragment preserved by caller).
    path_part = href.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return None
    # Resolve relative to the directory of src_path
    src_dir = src_path.parent
    try:
        resolved = (src_dir / path_part).resolve()
    except Exception:
        return None
    try:
        rel = resolved.relative_to(root.resolve())
    except ValueError:
        return None
    # If the target is a directory (or the href ends with `/`), try its README.md
    if resolved.is_dir() or href.rstrip().endswith("/"):
        readme = resolved / "README.md"
        if readme.exists():
            try:
                return readme.relative_to(root.resolve()).as_posix()
            except ValueError:
                return None
    return rel.as_posix()


def split_frontmatter(text: str) -> Tuple[Dict, str]:
    """Pull off a YAML-ish frontmatter block. We do a minimal key: value parse
    instead of depending on PyYAML (stdlib-only goal).
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    block = m.group(1)
    body = text[m.end():]
    meta: Dict[str, object] = {}
    # Very small parser: top-level `key: value` lines. Nested structures are
    # preserved as raw strings. This is good enough for GitBook's cover/coverY.
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body


def extract_title(frontmatter: Dict, body: str, fallback: str) -> str:
    if isinstance(frontmatter.get("title"), str) and frontmatter["title"]:
        return frontmatter["title"]  # type: ignore[return-value]
    m = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    if m:
        # Strip trailing HTML anchor junk like `<a href="#..." id="..."></a>`
        return HTML_TAG_RE.sub("", m.group(1)).strip()
    return fallback


def extract_headings(body: str) -> List[Dict[str, object]]:
    out = []
    for m in HEADING_RE.finditer(body):
        level = len(m.group(1))
        text = HTML_TAG_RE.sub("", m.group(2)).strip()
        if text:
            out.append({"level": level, "text": text})
    return out


def clean_content(body: str) -> str:
    """Produce LLM-friendly plaintext-ish markdown.

    * Strip HTML tags (they're mostly <figure>/<div> wrappers around images
      that we already capture separately).
    * Collapse GitBook artefacts like `&#x20;` and escaped line breaks.
    * Squash excess blank lines.
    """
    text = body
    # Drop <figure>...</figure> blocks entirely — alt text is captured via
    # image extraction, and leaving the HTML in confuses LLMs.
    text = re.sub(r"<figure>.*?</figure>", "", text, flags=re.DOTALL)
    text = re.sub(r"<div[^>]*>|</div>", "", text, flags=re.IGNORECASE)
    # Generic HTML tags → drop
    text = HTML_TAG_RE.sub("", text)
    text = GITBOOK_NBSP_RE.sub(" ", text)
    text = BACKSLASH_EOL_RE.sub(r"\1", text)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# SUMMARY.md parser (for section hierarchy)
# ---------------------------------------------------------------------------

SECTION_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
SUMMARY_LINK_RE = re.compile(r"^(\s*)\*\s+\[([^\]]+)\]\(([^)]+)\)\s*$")

def parse_summary(summary_path: Path) -> Dict[str, Dict[str, str]]:
    """Return map: rel_path -> {title, section}."""
    result: Dict[str, Dict[str, str]] = {}
    if not summary_path.exists():
        return result
    current_section: Optional[str] = None
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        sh = SECTION_HEADING_RE.match(line)
        if sh:
            current_section = sh.group(1).strip()
            continue
        m = SUMMARY_LINK_RE.match(line)
        if not m:
            continue
        _indent, title, href = m.groups()
        # Ignore external links in SUMMARY (rare, but possible)
        if is_external(href):
            continue
        # Normalize '.' segments
        href = href.split("#", 1)[0].split("?", 1)[0]
        result[href] = {"title": title.strip(), "section": current_section or ""}
    return result


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------

def classify_link(href: str, src_path: Path, root: Path) -> Tuple[str, Optional[str]]:
    """Return (kind, target_rel_path_or_None)."""
    if href.startswith("#"):
        return "anchor", None
    if is_external(href):
        return "external", None
    target = normalize_internal(src_path, root, href)
    if target is None:
        return "unresolved", None
    ext = Path(target).suffix.lower()
    if ext == MARKDOWN_EXT:
        return "internal-doc", target
    if ext in ASSET_EXTS:
        return "internal-asset", target
    # Folders or other — treat as asset-ish / unresolved
    return "unresolved", target


def extract_links_and_images(
    body: str,
    src_path: Path,
    root: Path,
    base_url: str,
    all_doc_ids: Dict[str, str],  # rel_path -> doc_id
) -> Tuple[List[LinkRef], List[LinkRef]]:
    links: List[LinkRef] = []
    images: List[LinkRef] = []

    # Markdown images
    for m in MD_IMAGE_RE.finditer(body):
        alt, href = m.group(1), m.group(2)
        kind, target = classify_link(href, src_path, root)
        public = None
        if is_external(href):
            public = href
        elif target:
            public = public_url_for(target, base_url)
        images.append(LinkRef(
            text=alt.strip(), href=href,
            target_path=target,
            target_doc_id=all_doc_ids.get(target) if target else None,
            public_url=public,
            kind="internal-asset" if (target and kind != "external") else kind,
        ))

    # HTML <img src="..."> (GitBook sprinkles these inside <figure>)
    for m in HTML_IMG_SRC_RE.finditer(body):
        href = m.group(1)
        kind, target = classify_link(href, src_path, root)
        public = href if is_external(href) else (public_url_for(target, base_url) if target else None)
        images.append(LinkRef(
            text="", href=href, target_path=target,
            target_doc_id=all_doc_ids.get(target) if target else None,
            public_url=public,
            kind="internal-asset" if (target and kind != "external") else kind,
        ))

    # Markdown links (non-image)
    for m in MD_LINK_RE.finditer(body):
        text, href = m.group(1), m.group(2)
        kind, target = classify_link(href, src_path, root)
        if is_external(href):
            public = href
        elif target:
            public = public_url_for(target, base_url)
            # Preserve fragment if present
            if "#" in href:
                public = public + "#" + href.split("#", 1)[1]
        else:
            public = None
        links.append(LinkRef(
            text=HTML_TAG_RE.sub("", text).strip(),
            href=href,
            target_path=target,
            target_doc_id=all_doc_ids.get(target) if target else None,
            public_url=public,
            kind=kind,
        ))

    return links, images


def build_all_doc_ids(root: Path) -> Dict[str, str]:
    """rel_path -> doc_id for every markdown file in the repo."""
    ids: Dict[str, str] = {}
    for md in root.rglob("*.md"):
        rel = rel_posix(md, root)
        ids[rel] = doc_id_from_path(rel)
    return ids


def iter_markdown_files(root: Path) -> List[Path]:
    """Walk docs-only markdown files.

    Exclusions:
      * Any path under a dot-folder (.github, .gitbook, etc.)
      * Anything under `scripts/` (the extractor's own README/dist is not docs)
      * `SUMMARY.md` at the repo root (it's a TOC, not content — we already
        used it to build the section map)
    """
    files = []
    for md in root.rglob("*.md"):
        parts = md.relative_to(root).parts
        if any(p.startswith(".") for p in parts):
            continue
        if parts and parts[0] == "scripts":
            continue
        if parts == ("SUMMARY.md",):
            continue
        files.append(md)
    files.sort()
    return files


def process_doc(
    md_path: Path,
    root: Path,
    base_url: str,
    summary_map: Dict[str, Dict[str, str]],
    all_doc_ids: Dict[str, str],
) -> DocRecord:
    rel = rel_posix(md_path, root)
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    fm, body = split_frontmatter(raw)

    summary_info = summary_map.get(rel, {})
    fallback_title = summary_info.get("title") or md_path.stem.replace("-", " ").title()
    title = extract_title(fm, body, fallback_title)
    section = summary_info.get("section") or None

    headings = extract_headings(body)
    links, images = extract_links_and_images(body, md_path, root, base_url, all_doc_ids)
    cleaned = clean_content(body)

    return DocRecord(
        id=doc_id_from_path(rel),
        title=title,
        section=section,
        path=rel,
        public_url=public_url_for(rel, base_url),
        headings=headings,
        content=cleaned,
        links=[asdict(l) for l in links],
        images=[asdict(i) for i in images],
        frontmatter=fm,
    )


# ---------------------------------------------------------------------------
# Emitters
# ---------------------------------------------------------------------------

def write_jsonl(records: List[DocRecord], out_path: Path) -> None:
    with out_path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(asdict(r), ensure_ascii=False, sort_keys=True))
            f.write("\n")


def write_links_map(records: List[DocRecord], root: Path, base_url: str, out_path: Path) -> None:
    """links.json: citation map for both docs and referenced assets."""
    out: Dict[str, Dict[str, str]] = {}

    # Docs
    for r in records:
        out[r.id] = {
            "title": r.title,
            "source_path": r.path,
            "public_url": r.public_url,
            "kind": "doc",
        }

    # Asset files referenced by any doc (collect union of internal-asset refs)
    asset_paths: Dict[str, str] = {}  # rel_path -> title (best-effort)
    for r in records:
        for img in r.images:
            tp = img.get("target_path")
            if tp and img.get("kind") == "internal-asset":
                asset_paths.setdefault(tp, img.get("text") or Path(tp).name)
        for ln in r.links:
            tp = ln.get("target_path")
            if tp and ln.get("kind") == "internal-asset":
                asset_paths.setdefault(tp, ln.get("text") or Path(tp).name)

    # Also include every asset that physically exists under .gitbook/assets,
    # even if unreferenced — useful for a complete citation surface.
    gitbook_assets = root / ".gitbook" / "assets"
    if gitbook_assets.exists():
        for f in gitbook_assets.rglob("*"):
            if f.is_file() and f.suffix.lower() in ASSET_EXTS:
                rel = rel_posix(f, root)
                asset_paths.setdefault(rel, f.name)

    for rel_path, title in sorted(asset_paths.items()):
        asset_id = "asset::" + rel_path
        out[asset_id] = {
            "title": title or Path(rel_path).name,
            "source_path": rel_path,
            "public_url": public_url_for(rel_path, base_url),
            "kind": "asset",
        }

    out_path.write_text(
        json.dumps(dict(sorted(out.items())), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_corpus_txt(records: List[DocRecord], out_path: Path) -> None:
    with out_path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(f'<doc id="{r.id}" title="{r.title}" url="{r.public_url}" path="{r.path}">\n')
            if r.section:
                f.write(f"[section: {r.section}]\n\n")
            f.write(r.content.rstrip() + "\n")
            f.write("</doc>\n\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="Docs repo root (default: current dir)")
    ap.add_argument("--out", default="scripts/extract/dist", help="Output directory")
    ap.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Public docs base URL for citations")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = (root / out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if not (root / "SUMMARY.md").exists():
        print(f"[warn] No SUMMARY.md found at {root}; section hierarchy will be empty.", file=sys.stderr)

    summary_map = parse_summary(root / "SUMMARY.md")
    all_doc_ids = build_all_doc_ids(root)

    md_files = iter_markdown_files(root)
    print(f"[info] Found {len(md_files)} markdown files under {root}", file=sys.stderr)

    records: List[DocRecord] = []
    for md in md_files:
        try:
            records.append(process_doc(md, root, args.base_url, summary_map, all_doc_ids))
        except Exception as e:
            print(f"[error] Failed on {md}: {e}", file=sys.stderr)
            raise

    # Deterministic ordering by doc id
    records.sort(key=lambda r: r.id)

    jsonl_path = out_dir / "toolkit.jsonl"
    links_path = out_dir / "links.json"
    corpus_path = out_dir / "toolkit.txt"

    write_jsonl(records, jsonl_path)
    write_links_map(records, root, args.base_url, links_path)
    write_corpus_txt(records, corpus_path)

    # Small summary stats
    total_links = sum(len(r.links) for r in records)
    total_images = sum(len(r.images) for r in records)
    print(f"[ok] Wrote {jsonl_path.name}: {len(records)} docs", file=sys.stderr)
    print(f"[ok] Wrote {links_path.name}: {json.loads(links_path.read_text())and len(json.loads(links_path.read_text()))} entries", file=sys.stderr)
    print(f"[ok] Wrote {corpus_path.name}: ~{corpus_path.stat().st_size // 1024} KB", file=sys.stderr)
    print(f"[stats] links={total_links} images={total_images}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
