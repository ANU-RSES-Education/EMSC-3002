---
name: emsc3002-site
description: Build, deploy and maintain the EMSC-3002 course site (Jupyter Book 2 / MyST + MkSlides reveal decks). Use for ANY work in this repo - editing lecture decks or book pages, deploying, importing PowerPoint, regenerating the glossary slide-index, or making PDFs. Encodes the traps that are easy to hit and hard to spot.
---

# EMSC-3002 course site

Jupyter Book 2 (MyST) book + MkSlides (reveal.js) decks, built together into one
static site. Toolchain is **pixi**. Full detail in `BUILD.md`; tool index in
`tools/README.md`.

## Everyday commands

```bash
pixi run build     # whole site -> _build/html   (ALWAYS run before committing)
pixi run serve     # live preview of the book
pixi run pdfs      # decktape PDFs of every deck (slow; local only, not in CI)
```

## Deploy

**`master` is the live branch.** Pushing to it rebuilds and publishes to
<https://anu-rses-education.github.io/EMSC-3002/> via `deploy_site.yml`
(~4 min build, then up to ~10 min of GitHub CDN cache).

- Branch `migrate-jb2` deploys to `/staging/` for preview.
- The public URL lags the deploy. To check whether a deploy *actually* worked,
  fetch the `gh-pages` branch directly — that bypasses the CDN:
  `https://raw.githubusercontent.com/ANU-RSES-Education/EMSC-3002/gh-pages/<path>`

## Rule: converted decks are hand-maintained content

Module 3 (×3) and Module 4 (×4) decks were converted from PowerPoint and have
since been **edited by Louis**. Each carries a `DO NOT REGENERATE` marker.
Never re-run the converter over them casually — it destroys hand edits.

If a genuine re-import is unavoidable, use a **3-way merge** where the base is
the last *pure-generated* version of the deck (regenerate it from the commit
where it was created — **not** a later hand-edited or merged commit; getting
this wrong silently reverts Louis's work). Then verify a known hand edit
survived before committing. See `tools/pptx2reveal/README.md`.

## Tools (none of these run during the build)

| Task | Tool |
|---|---|
| Import a **new** pptx as a deck | `tools/pptx2reveal/` |
| Rebuild the glossary → slide index | `tools/glossary-index/` |
| PDF of every deck | `build_pdfs.sh` (`pixi run pdfs`) |

**Re-run `tools/glossary-index/` after substantial deck edits** — the glossary
deep-links to slides by reveal coordinate (`#/h/v`), and inserting or removing
slides shifts them.

## Traps (all of these have bitten; all are silent failures)

- **MyST mangles relative `<a href>`.** It concatenates BASE_URL with the path
  verbatim, so `../slideshows/x.html` becomes `/EMSC-3002../slideshows/x.html`.
  Use **root-relative** hrefs (`/slideshows/x.html`) — those get the base
  prepended correctly and still work locally. Note `<iframe src>` is *not*
  rewritten, so iframes must stay relative (`../slideshows/…`). This is why
  embeds can work while the links beside them 404.
- **reveal `<!-- .element … -->` comments do nothing in MyST.** On book pages use
  a MyST `{image}` directive with `:width:`; the reveal comment only works inside
  `*.reveal.md`.
- **Never put anything above a deck's YAML front matter** — even a comment. It
  silently breaks front-matter parsing and dumps `separator:` etc. onto slide 1.
- **Two or more `$…$` spans with subscripts in one paragraph**: markdown pairs the
  `_`s as emphasis and breaks the maths. Write subscripts space-padded
  (`{\sigma} _ {1}`). The converter does this automatically.
- **Bare `![](…)` directly inside a block-level `<div>`** is left unrendered by
  reveal's markdown pass. Wrap each image in its own `<div>` with blank lines.
- **`build.sh` stages every `Lectures/Module-*/` directory** as slide assets. A
  new deck's images must live in such a directory or they 404 in the built site.
- **Per-deck `revealOptions:` front matter is ignored** by mkslides (only the
  global `Lectures/mkslides.yml` applies), and mkslides emits **no `<title>`**,
  so front-matter `title:` only shows on the slideshows index page.
- **Don't hotlink images.** Wikimedia blocks `/thumb/` URLs, which silently broke
  several slides. Fetch the original, optimise it into `Lectures/images/`, and
  reference it locally.
- **KaTeX is vendored, not fetched.** The reveal math plugin defaults to a CDN
  (`katex@latest`) *at presentation time* — fatal in a lecture theatre. It now
  loads from `Lectures/katex/` via `katex.local` in `mkslides.yml`, staged into
  `slideshows/katex/` by `build.sh`. The plugin needs **four** things under
  `dist/`: `katex.min.js`, `katex.min.css`, `fonts/` **and**
  `contrib/auto-render.min.js` — miss the last and no maths renders at all.
  Miss only the `KaTeX_Size*` fonts and the failure is subtler: everything looks
  right except large delimiters, which silently shrink to normal-height
  brackets. Verify with Chromium's
  `--host-resolver-rules="MAP * 127.0.0.1:9, EXCLUDE localhost"`.

## Content planning

`migration/CONTENT-MAP.md` — course direction, per-module inventories, the
overlap/repetition analysis and the consolidation model (one full treatment +
shorter, linked revisits). Read it before restructuring anything.
