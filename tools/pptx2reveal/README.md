# pptx → reveal.js converter

A general-purpose tool for importing a PowerPoint deck into this course as a
reveal.js slide deck (`Lectures/<name>.reveal.md` + an images directory).

> ## ⚠️ This is NOT part of the site build
>
> Nothing in the build (`pixi run build`) runs these scripts. They are a
> **one-shot import tool**, used by hand when you want to bring a *new* pptx
> into the course.
>
> **The decks already converted — Module 3 (Theory ×3) and Module 4 (×4) — are
> now hand-maintained content.** They have been edited since conversion
> (worked examples, cross-links, replacement figures, layout fixes). Do **not**
> re-run the converter over them: it would overwrite that work. Each of those
> decks carries a `DO NOT REGENERATE` marker in its first line.
>
> If a genuine re-import of an already-converted deck is ever needed, see
> *Re-importing* at the bottom — it requires a 3-way merge and is a deliberate,
> careful operation, not a routine one.

## Why the tool exists

`python-pptx` alone loses a lot: equation-editor maths is wrapped in
`mc:AlternateContent > mc:Choice` (which `slide.shapes` skips, exposing only a
garbled `mc:Fallback`), image crops live on the *use* of an image rather than
the file, and display geometry is discarded. This tool recovers all of that.

## Files

| file | role |
|------|------|
| `extract_pptx2.py` | XML-level extractor → `manifest.json`. Descends into `mc:Choice`, converts OMML maths to LaTeX, interleaves it with text as `$…$` / `$$…$$`, maps text super/subscripts to `<sup>`/`<sub>`, applies pptx crops (`srcRect`), optimises images (≤1600 px, TIFF→web, opaque-RGBA→JPEG, smaller of JPEG/PNG), and records each image's slide position/size. |
| `omml2tex.py` | OMML → LaTeX: fractions, sub/superscripts, radicals, delimiters, n-ary (∑/∫), matrices, accents, functions; folds math-italic Unicode, maps Greek to commands, wraps prose typed inside equations in `\text{}`, and emits markdown-proof subscripts (`{\sigma} _ {1}` — see BUILD.md gotchas). Matrix rows use `\cr`. |
| `convert_deck.py` | `manifest.json` → `.reveal.md` using the T0–T6 templates (`TEMPLATES.md`). Sizes images from their pptx geometry and preserves side-by-side rows. `--plain` omits the course title/resources/learning-outcomes scaffolding (for research talks). |
| `validate_math.py` | static check of generated maths: brace balance, empty spans, matrix pairing. |
| `katex_check.mjs` | parses every `$…$` span with KaTeX itself (`npm i katex` first). |

Dependencies are already in `pixi.toml`: `python-pptx`, `lxml`, `pillow`
(plus `pymupdf`, used for rendering slides from a PDF export — see below).

## Importing a new deck

```bash
PPTX=migration/PPTs/MyTalk.pptx        # source (keep large pptx out of git)
OUT=/tmp/import                        # scratch

# 1. extract text, maths and images
pixi run python tools/pptx2reveal/extract_pptx2.py "$PPTX" "$OUT"

# 2. convert to reveal markdown
#    args: manifest  image-path-prefix  first  last  output  [title] [subtitle]
#    add --plain for a talk that should not get course title/resources slides
pixi run python tools/pptx2reveal/convert_deck.py \
  "$OUT/MyTalk/manifest.json" "Module-x-MyTalk-extracted" 1 40 \
  Lectures/Module-x-MyTalk.reveal.md "EMSC 3002 - My Talk"

# 3. put the images where the build will find them
#    (build.sh stages every Lectures/Module-*/ directory)
mkdir -p Lectures/Module-x-MyTalk-extracted
cp "$OUT/MyTalk/images/"* Lectures/Module-x-MyTalk-extracted/

# 4. check the maths, then build
node tools/pptx2reveal/katex_check.mjs Lectures/Module-x-MyTalk.reveal.md
pixi run build
```

Then **edit the result by hand** — the conversion is a starting point, roughly
90–97 % of the way there. From that point on the markdown is the source of
truth and the pptx is only provenance (each slide keeps a
`<!-- source: … slide N -->` comment).

## Known limits

- **Shape-drawn diagrams** (arrows, axes, freehand drawn in PowerPoint) are not
  extractable — only their text labels survive. Fix by rendering the slide from
  a PDF export of the deck and using it as a full-slide image:
  ```python
  import fitz  # pymupdf
  doc = fitz.open("deck.pdf")
  doc[page-1].get_pixmap(matrix=fitz.Matrix(2, 2)).save("slideNNN_full.png")
  ```
  Note a PDF exported with animation builds has more pages than slides — match
  by the slide number printed in the page footer, not by index.
- **Keynote sources** must be exported to .pptx first; Keynote turns equations
  into images on export, so they arrive as pictures rather than live maths.
- Speaker notes convert; slide transitions/animations do not.

## Re-importing an already-converted deck (rare)

Only if the source pptx has genuinely changed and the change is worth the risk.
Never overwrite the deck directly — 3-way merge so hand edits survive:

```bash
# base = the last PURE-GENERATED version of the deck (regenerate it from the
#        commit where it was created, NOT a later hand-edited or merged commit)
# ours = the current, hand-edited file in Lectures/
# theirs = the freshly generated file
git merge-file --marker-size=7 Lectures/<deck>.reveal.md base.md theirs.md
```

Getting the base wrong silently reverts hand edits — verify a known hand edit
is still present afterwards before committing.
