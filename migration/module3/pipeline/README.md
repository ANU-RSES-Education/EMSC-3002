# Module 3 pptx → reveal pipeline

Converts the original PowerPoint theory decks (Stress / Strain / Rheology) into
`*.reveal.md` decks, **recovering the equations**.

## Why this exists

The equation-bearing shapes in the pptx are wrapped in
`<mc:AlternateContent><mc:Choice>` (the real OMML math) + `<mc:Fallback>`
(a flattened, garbled text copy). `python-pptx`'s `slide.shapes` skips the
`Choice` and exposes only the `Fallback`, so a naive text extraction **drops or
scrambles every equation**. This pipeline walks the slide XML directly, takes the
`Choice`, and converts the OMML to LaTeX (rendered by reveal.js's bundled KaTeX).

## Files

| file | role |
|------|------|
| `omml2tex.py`     | OMML (`<m:oMath>`) → LaTeX. Handles fractions, sub/superscripts, radicals, delimiters, n-ary (∑/∫), matrices, accents (vec/hat/dot/bar), functions; NFKC-folds math-italic Unicode and maps Greek → `\command`. Matrix rows use `\cr` (not `\\`, which reveal's markdown pass mangles). |
| `extract_pptx2.py`| XML-level extractor. Descends into `mc:Choice`, interleaves text runs with inline `$…$` / display `$$…$$`, converts text super/subscripts to `<sup>`/`<sub>`, extracts + **optimizes** images (downscale to ≤1600 px, TIFF→web, opaque RGBA→JPEG, pick smaller of JPEG/PNG). Emits `manifest.json`. |
| `convert_deck.py` | manifest → `*.reveal.md` using the T0–T6 templates (see `../TEMPLATES.md`). |
| `validate_math.py`| static check: brace balance, empty spans, matrix pairing. |
| `katex_check.mjs` | parses every `$…$`/`$$…$$` span with KaTeX (needs `npm i katex`). |

## Run (from repo root, via pixi)

```bash
SRC=OneDrive_1_16-07-2026            # source pptx (git-ignored)
for f in Lecture1_Stress Lecture2_Strain_StrainRate Lecture3_Rheology; do
  pixi run python migration/module3/pipeline/extract_pptx2.py "$SRC/$f.pptx" /tmp/m3
done
pixi run python migration/module3/pipeline/convert_deck.py \
  /tmp/m3/Lecture1_Stress/manifest.json "Module-iii-Theory/Lecture1-extracted" \
  1 52 Lectures/Module-iii-lecture1-Theory-draft.reveal.md \
  "Theory 1 (draft — reveal conversion)" "Module3.1 - Stress"
# … Lecture2 (1 41, Module3.2 - Strain and Strain rate) and Lecture3 (1 37, Module3.3 - Rheology)
# then copy /tmp/m3/<deck>/images/* into Lectures/Module-iii-Theory/Lecture{1,2,3}-extracted/
```

Deps (already in `pixi.toml`): `python-pptx`, `lxml`, `pillow`.

## Known remaining gap

Slides whose figure was **drawn with PowerPoint autoshapes** (arrows, axes,
freehand — e.g. the traction-vector construction and the exercise figures) have
no extractable raster image, so they show scattered labels instead of the
diagram. These need the source slide exported as an image (from PowerPoint, or a
LibreOffice/soffice render) — the OMML recovery does not address them.
