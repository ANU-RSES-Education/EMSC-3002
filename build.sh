#!/usr/bin/env bash
# Build the EMSC-3002 site: Jupyter Book 2 (MyST) book + MkSlides reveal.js decks.
# Output: _build/html  (deployable static site; slideshows under _build/html/slideshows).
#
# Run inside the pixi environment:  pixi run build   (or:  pixi run bash build.sh)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

OUT="$ROOT/_build/html"
SLIDES_OUT="$OUT/slideshows"
STAGE="$ROOT/_slides_src"

echo "==> 1/3  Building the MyST book"
myst build --html

echo "==> 2/3  Building reveal.js decks with MkSlides"
# MkSlides has no file filter, so stage only the *.reveal.md decks + their assets,
# then build the directory (a directory build mirrors referenced assets == old --static-dirs).
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp Lectures/*.reveal.md "$STAGE/"
cp Lectures/mkslides.yml "$STAGE/"
cp -R Lectures/css Lectures/data Lectures/images Lectures/movies "$STAGE/" 2>/dev/null || true
# every Module-* asset DIRECTORY (figures, extracted images, ...) — directories only,
# so book-page .md files are not swept in and built as bogus slideshows
for d in Lectures/Module-*/; do
  cp -R "${d%/}" "$STAGE/" 2>/dev/null || true   # strip trailing slash: BSD cp -R dir/ copies contents, not dir
done
( cd "$STAGE" && mkslides build . -f mkslides.yml -d "$SLIDES_OUT" )
rm -rf "$STAGE"

echo "==> 3/3  Copying lecture PDFs into the site"
if [ -d Lectures/static_pdfs/PDFs ]; then
  mkdir -p "$OUT/PDFs"
  cp -R Lectures/static_pdfs/PDFs/. "$OUT/PDFs/" || true
fi

echo "==> Done. Site at: $OUT"
