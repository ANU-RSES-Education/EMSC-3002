#!/usr/bin/env bash
# Generate PDF versions of the reveal.js decks with decktape (mkslides has no
# built-in PDF export; decktape prints any reveal deck, KaTeX included).
#
# Usage:
#   pixi run pdfs                 # all decks -> _build/html/pdfs/
#   bash build_pdfs.sh <pattern>  # only decks matching the glob pattern,
#                                 #   e.g. bash build_pdfs.sh 'Module-i-*'
#
# Requires: the site already built (pixi run build), node/npx on PATH.
# decktape downloads its own headless Chromium on first run.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
SLIDES="$ROOT/_build/html/slideshows"
PDFOUT="$ROOT/_build/html/pdfs"
PATTERN="${1:-*}"
PORT=8123

[ -d "$SLIDES" ] || { echo "No built slides at $SLIDES — run 'pixi run build' first."; exit 1; }
mkdir -p "$PDFOUT"

# serve the built slideshows (decktape needs http, not file://)
( cd "$SLIDES" && python3 -m http.server $PORT >/dev/null 2>&1 ) &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null || true' EXIT
sleep 1

shopt -s nullglob
for f in "$SLIDES"/$PATTERN.reveal.html; do
  name="$(basename "$f" .html)"
  # use the deck's own reveal size if present (Louis's decks 1100x750, converted 1200x800)
  if grep -q '"width": 1100' "$f" || grep -q 'width: 1100' "$f"; then
    SIZE=1100x750
  else
    SIZE=1200x800
  fi
  echo "==> $name  ($SIZE)"
  npx -y decktape@3 reveal "http://localhost:$PORT/$name.html" "$PDFOUT/$name.pdf" \
      --size "$SIZE" --pause 500 2>&1 | tail -1
done

echo "==> PDFs in $PDFOUT"
