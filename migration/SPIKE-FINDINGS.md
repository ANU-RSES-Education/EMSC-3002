# JB2 + MkSlides migration — spike findings

Branch: `migrate-jb2`. Date: 2026-07-09. Tooling via **pixi** (`pixi.toml`):
mystmd **1.10.1** (conda-forge) + mkslides (pypi). Goal: prove the two halves of the
migration end-to-end and give a go/no-go for a **28 July** cutover.

## Verdict: **GO** ✅

Both halves work against the *real* EMSC-3002 content with only mechanical fixes. The
existing course markdown is substantially JB2/MyST-compatible, and MkSlides is a genuine
drop-in for reveal-md.

---

## MkSlides (reveal-md successor) — works

- `Lectures/mkslides.yml` reproduces the old `build_slides.sh` reveal-md flags: custom
  separators (`separator: "<--o-->"`, `separator_vertical: "<--v-->"`), local ANU theme
  (`theme: css/anu.css` — **fixes the old circular live-URL theme dependency**),
  `highlight_theme: github`, and reveal options (`width/height/margin/transition/slideNumber`).
- Built `Module-i-GlobalTectonics-1.reveal.md` to a working reveal.js deck.
- **Asset handling = `--static-dirs` replacement:** a **directory** build mirrors the whole
  source tree (verified `css/anu.css` and `images/…` copied to output). A **single-file**
  build does NOT copy siblings — so decks must be built as a directory.

**Required restructure (small):** MkSlides has no include/exclude filter, so it converts
*every* `.md` in the target dir. The `Lectures/` folder mixes slide decks (`*.reveal.md`)
with book pages (`*.md`). Move the decks + their figure folders into a dedicated slides
source dir (e.g. `Slides/`) so only decks are processed. Then copy the built output into the
site at `/slideshows/` (same as the old `cp` step).

**Open:** per-deck reveal-md frontmatter (`revealOptions`, `separator`) is ignored by
MkSlides (it reads only `slides`/`revealjs`/`plugins` keys) — global `mkslides.yml` covers
it. PDF export path (old "build your own PDF" `?print-pdf`) not yet verified.

## Jupyter Book 2 / MyST — works

- Hand-authored a `myst.yml` (`project.toc`, `bibliography`, `site.template: book-theme`)
  and built an isolated 3-page subset (FrontPage, Introductory_Remarks,
  Module-i-GlobalTectonics) with `myst build --html` → static site under `_build/html/`.
- **Content parity is high.** These all parsed/rendered natively on book-theme:
  `{grid}` / `{grid-item-card}` (sphinx-design), `{figure}`, `{cite}` + `.bib` bibliography,
  `{glossary}`, `$$` math, and raw `<iframe>` slide embeds.
- Only trivial issues: one `unexpected option "gutter"` warning on a grid (mechanical), and
  a missing image (expected — assets dir not staged in the isolated spike).

**Auto-migration note:** `myst init` detects the legacy Jupyter Book and offers to migrate
`_config.yml`/`_toc.yml` → `myst.yml` (plus glossary/admonition upgrades). It is interactive
and does not drive from a pipe; run it in a real terminal, or hand-author `myst.yml` (done
here). The classic build is unaffected on `master`.

**Parity work remaining (site-level, not content — reproduce or consciously drop):**
- Custom font-switcher buttons (`extra_navbar` HTML in `_config.yml`).
- hypothes.is comments.
- Launch / Binder buttons (mystmd has its own launch/thebe integration to wire).
- Sphinx `html_extra_path` slide copy → replace with a build step that copies MkSlides
  output into the MyST site's static output.

## Next steps (Phase C proper)

1. Restructure slide decks into a dedicated source dir; finalise `mkslides.yml`; build all
   decks and confirm parity with the current live slideshows.
2. Author the full `myst.yml` from `_config.yml`/`_toc.yml`; build the whole book; fix
   directive-option warnings; decide on font-switcher / hypothes.is / launch buttons.
3. Add `linux-64` to `pixi.toml` platforms; write ONE pixi-based deploy workflow that builds
   MyST + MkSlides and pushes `gh-pages` once (single pusher). Deploy to a `staging/` dir
   first for side-by-side comparison with the JB1 fallback.
4. Cut over to root when at parity (target 28 July); JB1 stays live until then.
