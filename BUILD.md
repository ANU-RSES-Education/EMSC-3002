# EMSC-3002 — build & deploy

The site is a **Jupyter Book 2 (MyST)** book plus **MkSlides** (reveal.js) slide
decks, built together into one static site. Cutover from the legacy Jupyter
Book 1 build: 2026-07-27 (the old system remains in gh-pages branch history;
its config lives untouched under `Jupyterbook/_config.yml` / `_toc.yml`).

## What builds the site

| Piece | Tool | Source | Output |
|---|---|---|---|
| Book pages | `mystmd` (Jupyter Book 2 engine) | `myst.yml` (repo root) + `Jupyterbook/`, `Lectures/*.md`, `Notebooks/` | `_build/html/` |
| Slide decks | `mkslides` (reveal.js 5) | `Lectures/*.reveal.md` + `Lectures/mkslides.yml` + `Lectures/css/anu.css` | `_build/html/slideshows/` |
| Lecture PDFs | copied | `Lectures/static_pdfs/PDFs/` | `_build/html/PDFs/` |

Everything is orchestrated by `build.sh`; the toolchain is managed by **pixi**
(`pixi.toml` — mystmd from conda-forge, mkslides from PyPI, plus python-pptx /
lxml / pillow / pymupdf for the slide-conversion pipeline).

## Build locally

```bash
pixi run build     # full site -> _build/html
pixi run book      # MyST book only
pixi run serve     # live preview of the book (myst start)
pixi run pdfs      # decktape PDF of every built deck -> _build/html/pdfs
                   #   (or: bash build_pdfs.sh 'Module-i-*' for a subset)
```

Slide separators: `<--o-->` (horizontal) and `<--v-->` (vertical); speaker
notes start at a `Note:` line. Maths is KaTeX (`$…$`, `$$…$$`), enabled by
default in mkslides.

## Deploy (CI)

| Workflow | Trigger | Deploys to |
|---|---|---|
| `deploy_site.yml` | push to `master` | gh-pages **root** → https://anu-rses-education.github.io/EMSC-3002/ |
| `deploy_myst_staging.yml` | push to `migrate-jb2` (or manual) | gh-pages `staging/` → …/EMSC-3002/staging/ |
| `test_build.yml` | pull requests | build check only, no deploy |

Both deploys build with the matching `BASE_URL` (`/EMSC-3002` or
`/EMSC-3002/staging`) — the MyST site is an SPA and needs the base path baked
in. The root deploy uses `keep_files: false`, so **a master push wipes
`/staging`**; push the staging branch again to recreate the preview.

## Gotchas

- **Per-deck `revealOptions:` front matter is ignored** — mkslides only reads
  the global `Lectures/mkslides.yml` (all decks render 1200×800).
- Bare `![](…)` directly inside a block-level `<div>` is left unrendered by
  reveal's markdown pass — wrap images in their own `<div>` with blank lines
  (the templates do this).
- Two or more `$…$` spans with subscripts in one paragraph: write subscript
  underscores space-padded (`{\sigma} _ {1}`) or markdown will pair the `_`s
  as emphasis and break the math (the conversion pipeline does this
  automatically).
- `build.sh` stages every `Lectures/Module-*/` **directory** as slide assets —
  a new deck's images belong in such a directory (e.g. `Module-x-…-extracted/`).
- Source PowerPoints live in `migration/PPTs/` (gitignored, large). The
  pptx→reveal conversion pipeline and its docs: `migration/module3/pipeline/`.
  Regenerating a converted deck must go through the 3-way-merge protocol
  described there so hand edits are preserved.

## Content map / planning

`migration/CONTENT-MAP.md` — course direction, per-module inventories, overlap
analysis and the consolidation model.
