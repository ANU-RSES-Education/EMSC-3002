# Building & deploying EMSC-3002

This repo publishes to **https://anu-rses-education.github.io/EMSC-3002/** via GitHub Pages
(the `gh-pages` branch). This note describes the **current** pipeline. A migration to
Jupyter Book 2 + MkSlides is planned — see `archive/README.md` and the migration plan.

## What builds the site

The live site is a **Jupyter Book 1.x** book (Sphinx + `sphinx-book-theme` + MyST-NB) with
**reveal.js slide decks** (built by `reveal-md`) folded in.

| Piece | Source | Output |
|---|---|---|
| The book (notes, lecture pages, exercises) | `Jupyterbook/` (`_config.yml`, `_toc.yml`) | `Jupyterbook/_build/html` |
| Slide decks | `Lectures/*.reveal.md` | `Lectures/static_slides/slideshows` → copied to `_build/html/slideshows` |

`Jupyterbook/Lectures` and `Jupyterbook/Notebooks` are **symlinks** to the repo-root
`Lectures/` and `Notebooks/`. Build outputs (`_build`, `static_slides`) are gitignored and
regenerated on every build.

## Build locally

Requires `jupyter-book` (1.x), Node/`reveal-md`, and the packages in
`.github/workflows/envs/build_jb.yml`.

```bash
cd Jupyterbook
source build_book.sh   # builds slides (reveal-md) → builds book → copies slides/PDFs/movies in
```

`build_book.sh` runs, in order:
1. `Lectures/build_slides.sh` — `reveal-md` renders every `**/*.reveal.md` to static HTML.
2. `Lectures/build_pdfs.sh` — a stub (the one PDF, `pt_rules`, is committed under
   `Lectures/static_pdfs/`).
3. `jupyter-book build .` → `_build/html`.
4. Copies slideshows, PDFs, `Figures/Movies`, `Exercises/Resources` into `_build/html`.

Open `Jupyterbook/_build/html/index.html` to preview.

## Deploy (CI)

- **`.github/workflows/deploy_to_gh_pages.yml`** (`deploy-book`) — on push to `master`
  (or manual). Builds via `build_book.sh` and publishes `Jupyterbook/_build/html` to the
  **root** of `gh-pages` with `peaceiris/actions-gh-pages`. This is the **only** workflow
  that writes to `gh-pages`.
- **`.github/workflows/build_dont_deploy_to_gh_pages.yml`** (`test-build-jupyter-book`) —
  **PR-only**. Builds the book to check it compiles; does not deploy.

To deploy by hand: Actions tab → *deploy-book* → **Run workflow** (or just merge to master).

## Pinned versions (do not loosen without testing)

- `jupyter-book>=1.0,<2` — **critical.** Jupyter Book 2 is a MyST-engine rewrite that does
  **not** read the classic `_toc.yml`/`_config.yml`; an unpinned install can pull it and
  break the build.
- `nodejs=18` and `reveal-md@6.1.4` — `reveal-md` is unmaintained; the pin keeps slide
  generation stable.

Pins live in `.github/workflows/envs/build_jb.yml` (book) and `Lectures/build_slides.sh`
(slides).

## Gotchas

- **Single gh-pages pusher.** Only `deploy-book` may push to `gh-pages`. A second pusher
  (the old Quarto revision workflow) previously caused the deploy to fail with a push race —
  that workflow has been retired.
- **Slide theme is fetched from the live site.** `build_slides.sh` pulls `anu.css` from
  `https://anu-rses-education.github.io/EMSC-3002/slideshows/css/anu.css`. If `gh-pages` is
  ever wiped, slides lose styling until the site is republished. (The JB2/MkSlides migration
  will switch this to a local theme file.)
- **`archive/`** holds the retired Quarto revision book — not built, not deployed; kept for
  content migration.
- CI warns that `actions/checkout@v3` / `setup-micromamba@v2` use the deprecated Node-20
  runner; bump to `@v4` when convenient (non-blocking).
