# tools

Maintenance scripts for the course site. **None of these run during
`pixi run build`** — they are things you invoke by hand, occasionally.

| Directory | What it does | When to run it |
|---|---|---|
| [`pptx2reveal/`](pptx2reveal/) | Imports a PowerPoint deck as a reveal.js deck: recovers equation-editor maths as LaTeX, applies pptx image crops, sizes images from their slide geometry, keeps a `<!-- source: … slide N -->` trail. | Only when bringing in a **new** deck. The already-converted Module 3 and 4 decks are hand-maintained now — see the warning in that README. |
| [`glossary-index/`](glossary-index/) | Rebuilds the *Slides:* cross-references in `Jupyterbook/Glossary.md`, deep-linking each glossary term to the slide(s) that teach it. | After substantial deck edits — slide coordinates shift when slides are added or removed. |
| [`../build_pdfs.sh`](../build_pdfs.sh) | Renders every built deck to PDF with decktape (`pixi run pdfs`). | When you want fresh PDFs; takes ~10–15 min for the full set. |

Build and deploy itself is documented in [`../BUILD.md`](../BUILD.md); the
operational gotchas are collected in `.claude/skills/emsc3002-site/SKILL.md`.
