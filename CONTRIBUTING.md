# Contributing

Submit a concrete public Kling 4 workflow, demonstration, evaluation, integration, benchmark or practical limitation through an issue or pull request.

Include the original source URL, posting account, source date, a short title, what a reader can inspect or reproduce, and the media or methodological evidence. Disclose platform sponsorship, reused footage, comparison settings and any uncertainty that affects interpretation. Claims about price, generation length or performance need their own evidence.

Only include a generation Prompt when its exact text is public or supplied with permission. Link author replies and image transcriptions to their original source. Do not reconstruct instructions from an output. A workflow explanation and a generation Prompt are different artifacts.

Before submitting a case change:

- Follow the stable case format in [maintenance](docs/maintenance.md)
- Update the English README, case data, CSV and source index together
- Synchronize all ten translations, preserving identifiers, media, source URLs and exact Prompt/code blocks
- Use R2-hosted posters linked to R2-hosted videos, with accurate input/output labels
- Run `python3 scripts/verify_repo.py` and `git diff --check`

Editorial contributions use CC BY 4.0. Contributing a link or reproduction does not transfer ownership of third-party media or prompts. For corrections, rights concerns or removal requests, open an issue with the affected source and case number; no new generation is required.

API installers, npm packages and runnable model API examples belong in separate repositories. This repository may link to a verified adjacent surface, but does not maintain that surface's release state.
