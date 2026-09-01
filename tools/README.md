# tools

Maintenance scripts for the course site. **None of these run during
`pixi run build`** — they are things you invoke by hand, occasionally.

| Directory | What it does | When to run it |
|---|---|---|
| [`pptx2reveal/`](pptx2reveal/) | Imports a PowerPoint deck as a reveal.js deck: recovers equation-editor maths as LaTeX, applies pptx image crops, sizes images from their slide geometry, keeps a `<!-- source: … slide N -->` trail. | Only when bringing in a **new** deck. The already-converted Module 3 and 4 decks are hand-maintained now — see the warning in that README. |
| [`glossary-index/`](glossary-index/) | Rebuilds the *Slides:* cross-references in `Jupyterbook/Glossary.md`, deep-linking each glossary term to the slide(s) that teach it. Run `build_index.py` then `inject_index.py`. | After substantial deck edits — slide coordinates shift when slides are added or removed. |
| [`figures/`](figures/) | Scripts that generate course figures from public data. `australia_deposits.py` plots major ore deposits on the Wikimedia craton base map (the georeferencing and its verification are documented in the script). | When a figure's content changes; the outputs are committed, so only on edit. |
| [`dropped-text.py`](dropped-text.py) | Compares each converted deck against its source pptx and reports slides whose body text the converter discarded outright — the loss that leaves nothing behind to notice. `pixi run python tools/dropped-text.py Lectures/*-draft.reveal.md` | After any pptx conversion, alongside `label-soup.py`. |
| [`label-soup.py`](label-soup.py) | Lists converted slides where a pptx diagram's labels were shredded into the body text, so they can be screenshotted and replaced in one pass. `pixi run python tools/label-soup.py Lectures/*-draft.reveal.md` | After any pptx conversion, and before presenting a converted deck. |
| [`../build_pdfs.sh`](../build_pdfs.sh) | Renders every built deck to PDF with decktape (`pixi run pdfs`). | When you want fresh PDFs; takes ~10–15 min for the full set. |

Build and deploy itself is documented in [`../BUILD.md`](../BUILD.md); the
operational gotchas are collected in `.claude/skills/emsc3002-site/SKILL.md`.
