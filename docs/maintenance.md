# Maintenance

## Source of truth

`data/use-cases.json` is the public curated case dataset. `README.md` is the English editorial presentation; the ten localized READMEs must match its case identities, order, source links, authors, metadata, media and exact Prompt blocks. `data/use-cases.csv` exposes the same 83 cases for sorting in spreadsheet tools. `data/use-cases.md` is the compact source index.

The initial [collection scope](collection-scope.md) records search windows, gaps and inclusion rules. Research snapshots and execution evidence stay outside the public repository. Public verification must work without private snapshots, credentials, local downloads or access to the original collector's filesystem.

## Case format

Use a stable `case-N` HTML anchor immediately before the third-level linked case heading, followed by a bold reader-action takeaway, source-grounded notes, a linked R2 poster and optional exact public Prompt blocks. End with the canonical `Type: ... | Date: YYYY-MM-DD` line and a separator. Metadata dates are source UTC dates, not a claimed date of creation of the media.

Types are `Demo`, `Tutorial`, `Evaluation`, `Integration`, `Benchmark` or `Limit`. Missing prompts are omitted. Preserve source text and Prompt hashes; do not infer a prompt from a video. Keep posting-account attribution separate from original authorship, and retain author-reply conversation relationships in structured source records.

## Update checklist

1. Freeze the collection timestamp and requested search window, preserve raw source evidence privately, and record gaps and API coverage limits
2. Review every candidate, deduplicate source URLs and media, and resolve category, title, type, date, takeaway, attribution and Prompt boundary before editing
3. Freeze a source-fidelity manifest and expected visual set, including every selected attachment; verify the handoff before changing READMEs
4. Host original playback and derived posters on R2, preserve source URLs and hashes, and confirm complete bytes and content types
5. Update English README and structured data first, run the English gate, then update all ten translations without changing Prompt/code blocks
6. Refresh the CSV and compact index, retaining the same case order and captured engagement timestamps
7. Run the portable checker, canonical pipeline gates, complete public-link audit and GitHub rendered-media audit; fix findings and rerun affected checks
8. Commit, push and read back the exact public commit, README, media, About fields and branch before describing an update as published

Never run a new model generation without an approved credit budget. A source video does not prove API availability. A first-publication or later update must explicitly document any owner-approved exception to a required pipeline gate.

## Validation

From a clean checkout with Python 3.10 or newer:

```bash
python3 scripts/verify_repo.py --english-only
python3 scripts/verify_repo.py
git diff --check
```

The portable checker compares every public case to the dataset, verifies exact Prompt hashes, CSV equality, localized identities and media sets, and checks local Markdown links. It is a local consistency check: it does not prove network availability, translation nuance, real model execution, GitHub rendering or publication.

Release operators also run the `model-repo-pipeline` canonical handoff, English, localization, media/link, public-surface and completion gates. Record those versioned tool paths and command results in private run evidence, rather than introducing a dependency on one maintainer's absolute paths here.

## Hosting and links

Case posters link to playable R2 MP4s. Original X media URLs are provenance in structured data, not display fallbacks. Keep all case visuals across languages equal to the frozen expected set. Public EvoLink links use `utm_source=github`, campaign `awesome-kling-4-usecases` and placement/locale attribution. GitHub About homepage is exempt. Source and third-party media links must not receive EvoLink UTM parameters.

Recheck model/API/skill availability before changing Quick Start. Star History must remain absent below ten live GitHub stars; add it only after reading the live count, then keep it as the final README element.
