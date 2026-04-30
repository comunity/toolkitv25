# Toolkit Docs Extractor

Walks this GitBook-style repo and emits LLM-ready artifacts you can drop into a
knowledge base (RAG index, context-stuffed prompt, etc.), plus a citation map
so the LLM can cite back to the public docs site.

## Outputs (under `dist/`)

| File            | What it is                                                                 |
| --------------- | -------------------------------------------------------------------------- |
| `toolkit.jsonl` | One JSON record per markdown doc: id, title, section, path, public_url, headings, cleaned content, links, images, frontmatter. |
| `links.json`    | Citation map keyed by doc id (and `asset::<path>` for referenced assets). Each entry has `{title, source_path, public_url, kind}`. |
| `toolkit.txt`   | Whole corpus concatenated with `<doc id=... url=...>` delimiters. Useful for quick context-stuffing / eyeballing. |

Doc ids are derived from the repo path: `toolkit-guides/screens/README.md` →
`toolkit-guides/screens`, root `README.md` → `index`.

## Run it locally

```sh
# From repo root:
python3 scripts/extract/extract.py

# Or with explicit flags:
python3 scripts/extract/extract.py \
  --root . \
  --out  scripts/extract/dist \
  --base-url https://comunity.gitbook.io/learning.comunityplatform/25.x
```

No dependencies — Python 3.9+ stdlib only.

## Run it in GitHub Actions

See `.github/workflows/extract-toolkit.yml`. It runs on push to `main` and on
manual dispatch, uploading the three files as a build artifact. You can swap
the artifact step for a publish step (S3, release, commit-back, etc.) when you
wire it into a real pipeline.

## How citations work

For every doc and referenced asset we compute a `public_url` under
`https://comunity.gitbook.io/learning.comunityplatform/25.x`. Feed `links.json`
to your LLM system-prompt as a lookup table: when the model answers, it cites
by doc id, and you resolve the id to `{title, public_url}` for the user-facing
citation.

## Quality framework

After extraction, run the quality tiers to get a weighted completeness score:

```sh
python3 scripts/extract/quality/run_quality.py
# → scripts/extract/dist/quality-report.{json,md}
```

Currently active tiers (no network, no extra dependencies):

| Tier | Weight | Checks |
| --- | ---: | --- |
| structural        | 20% | doc-count parity, required fields, empty content, section assignment |
| content_fidelity  | 25% | char retention, heading / code-fence / table preservation |
| link_integrity    | 20% | internal-doc resolution, image resolution, unresolved-link rate, citation-map coverage |

Verdict thresholds: **PASS** ≥ 90 with no tier < 75; **FAIL** if overall < 75
or any tier < 50; otherwise **WARN**. CI fails the job only on FAIL — warnings
are surfaced in the report and on the run summary.

Tiers 4 (citation liveness — HEAD every public_url) and 5 (QA answerability
against curated questions) are scaffolded in `scripts/extract/quality/tiers.py`
and will be enabled once we decide CI cadence and seed the question set.

## Gotchas

- GitBook asset URLs may not 1:1 match the repo path on every GitBook site.
  The script assumes the standard scheme; verify a few asset links after
  publishing and adjust `public_url_for()` if your site uses a CDN path.
- Frontmatter is parsed with a minimal key/value reader (no PyYAML dep). Rich
  nested YAML is preserved as raw strings.
- `clean_content()` strips `<figure>` and other HTML wrappers so the LLM sees
  prose, not GitBook chrome. Images are still captured separately under
  `record.images` for citation.
