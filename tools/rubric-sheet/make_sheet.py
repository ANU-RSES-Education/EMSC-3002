"""Printable marking sheet from a Canvas rubric export: one page per presenter.

Lays the rubric out as the Canvas "traditional" grid (criteria down the side,
one cell per rating level with its descriptor and points, a points box and a
comment line for each criterion, an overall comment and a score box), sized to
fit a single A4 landscape page. Print one per presenter, or pass a class list
with --names to get one page per student with the name already filled in.

Input is a Canvas rubric-export CSV (Rubrics -> Export): columns Rubric Name,
Criteria Name, Criteria Description, Criteria Enable Range, then a
(Rating Name, Rating Description, Rating Points) triplet per level. Canvas
exports can carry entities escaped several times over (Q&amp;amp;amp;A), and a
comma that was not quoted on import shifts every later field along; both are
handled or reported.

The page is rendered by Chrome's print-to-PDF. chrome-headless-shell is used
when it can be found (decktape/puppeteer keep one in ~/.cache/puppeteer): a full
Chrome 151 run with --headless never exits after printing. Set CHROME to point
at a specific executable.

Run:  pixi run python tools/rubric-sheet/make_sheet.py \\
          Jupyterbook/Exercises/Rubrics/AustralianPlatePresentation.csv
      (writes ...-marking-sheet.pdf beside the CSV; -o to choose the output,
       --names class.txt for one pre-named page per line of class.txt)
"""
import argparse
import csv
import glob
import html
import itertools
import os
import re
import shutil
import subprocess
import sys
import tempfile


def unescape(s):
    prev = None
    while prev != s:
        prev, s = s, html.unescape(s)
    return s.strip()


def read_rubric(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [r for r in csv.reader(f) if any(c.strip() for c in r)]
    head = [h.strip().lower() for h in rows[0]]
    if head[:2] != ["rubric name", "criteria name"]:
        sys.exit(f"{path}: not a Canvas rubric export (expected 'Rubric Name, Criteria Name, ...').")
    first = head.index("rating name") if "rating name" in head else 4
    criteria, shifted = [], []
    for r in rows[1:]:
        ratings = []
        for i in range(first, len(r) - 2, 3):
            name, desc, pts = unescape(r[i]), unescape(r[i + 1]), r[i + 2].strip()
            if not (name or desc or pts):
                continue
            try:
                points = float(pts)
            except ValueError:
                points = None
            ratings.append((name, desc, points))
        # an unquoted comma shifts every later field: descriptors turn up as
        # rating names and point values as descriptors
        if any(p is None or re.fullmatch(r"\d+(\.\d+)?", d) or len(n) > 60 for n, d, p in ratings):
            shifted.append(unescape(r[1]))
        if ratings:
            criteria.append({"name": unescape(r[1]), "desc": unescape(r[2]), "ratings": ratings,
                             "max": max(p or 0 for _, _, p in ratings)})
    return unescape(rows[1][0]), criteria, shifted


def fmt(x):
    return f"{x:g}"


CSS = """
@page { size: A4 landscape; margin: 5mm 7mm; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { font: 6.2pt/1.18 "Helvetica Neue", Helvetica, Arial, sans-serif; color: #1d2125;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
/* min-height, not height: a sheet that is too long spills onto a second page,
   which main() detects, instead of being silently clipped */
.sheet { min-height: 199mm; display: flex; flex-direction: column; break-after: page; }
.sheet:last-child { break-after: auto; }

header { display: flex; align-items: flex-end; gap: 6mm; margin-bottom: 1.5mm; }
header h1 { font-size: 10pt; margin: 0 0 .6mm; white-space: nowrap; }
.field { flex: 1; color: #5d6670; font-size: 6.5pt; }
.field .line { border-bottom: .3mm solid #1d2125; height: 5.5mm; color: #1d2125; font-size: 10pt;
  padding: 0 1mm; display: flex; align-items: flex-end; }
.score { display: flex; border: .3mm solid #cfd4da; border-radius: 1.6mm; overflow: hidden; }
.score span { background: #f3f4f5; padding: 1.4mm 3mm; font-weight: 600; font-size: 9pt; }
.score b { background: #2b7a3d; color: #fff; padding: 1.4mm 3mm; font-size: 10pt; min-width: 26mm; text-align: right; }

table { width: 100%; border-collapse: collapse; border: .3mm solid #cfd4da; table-layout: fixed; }
col.crit { width: 34mm; } col.pts { width: 15mm; }
thead th { background: #f3f4f5; text-align: left; padding: .8mm 2mm; font-size: 7pt; border-bottom: .3mm solid #cfd4da; }
tr.crit > * { border-top: .3mm solid #cfd4da; vertical-align: top; }
th.name { padding: 1mm 1.8mm; text-align: left; font-size: 7pt; }
.c-num { display: block; color: #5d6670; font-size: 5.4pt; font-weight: 400; text-transform: uppercase; letter-spacing: .04em; }
.c-desc { display: block; color: #5d6670; font-weight: 400; font-size: 5.8pt; margin-top: .6mm; }
/* height: 1px lets the grid take 100% of the cell, so the rules between levels
   run the full height of the row even when the criteria column is the taller */
td.ratings { padding: 0; height: 1px; border-left: .3mm solid #cfd4da; border-right: .3mm solid #cfd4da; }
.grid { display: grid; height: 100%; }
.rating { border-left: .3mm solid #cfd4da; padding: .9mm 1.4mm 1.1mm; }
.rating:first-child { border-left: 0; }
.r-head { display: flex; align-items: baseline; margin-bottom: .5mm; }
.r-name { flex: 1; font-weight: 700; text-align: center; font-size: 6.8pt; white-space: nowrap; }
.r-pts { font-weight: 700; font-size: 6.6pt; white-space: nowrap; margin-left: 1mm; }
td.points { text-align: center; vertical-align: middle; font-size: 8pt; white-space: nowrap; }
.box { display: inline-block; width: 8mm; height: 6mm; border: .3mm solid #9aa4ae; border-radius: 1mm; vertical-align: middle; }
.of { color: #5d6670; }
tr.comment td { padding: .3mm 1.8mm .9mm; }
.write { border: .3mm solid #cfd4da; border-radius: 1mm; height: 5mm; padding: .3mm 1.3mm; color: #9aa4ae; font-size: 5.6pt; }
.overall { flex: 1; min-height: 9mm; margin-top: 1.5mm; border: .3mm solid #cfd4da; border-radius: 1mm;
  padding: .8mm 2mm; color: #5d6670; font-size: 7pt; font-weight: 600; }
"""


def column_template(criteria):
    """Grid columns shared by every row, sized to make the rows as short as possible.

    A row is as tall as its longest descriptor relative to that column's width,
    so equal columns waste most of the short "No Evidence" cells. Search a
    coarse grid of relative widths for the one that minimises the summed row
    heights. Rubrics whose criteria have different numbers of levels (or more
    than six) fall back to equal columns."""
    counts = {len(c["ratings"]) for c in criteria}
    if len(counts) != 1 or max(counts) > 6:
        return None
    n = counts.pop()
    # +40 characters stands in for the level-name line every cell carries
    lengths = [[len(c["ratings"][j][1]) + 40 for j in range(n)] for c in criteria]
    best = min(itertools.product((0.5, 0.6, 0.7, 0.8, 0.9, 1.0), repeat=n),
               key=lambda w: sum(max(L[j] * sum(w) / w[j] for j in range(n)) for L in lengths))
    return " ".join(f"{x:g}fr" for x in best)


def sheet_html(title, criteria, presenter=""):
    e = html.escape
    total = sum(c["max"] for c in criteria)
    shared = column_template(criteria)
    rows = []
    for i, c in enumerate(criteria, 1):
        cells = "".join(
            f'<div class="rating"><div class="r-head"><span class="r-name">{e(n)}</span>'
            f'<span class="r-pts">{fmt(p or 0)} pts</span></div>{e(d)}</div>' for n, d, p in c["ratings"])
        columns = shared or f"repeat({len(c['ratings'])},1fr)"
        rows.append(
            f'<tr class="crit"><th class="name"><span class="c-num">Criterion {i}</span>{e(c["name"])}'
            f'<span class="c-desc">{e(c["desc"])}</span></th>'
            f'<td class="ratings"><div class="grid" style="grid-template-columns:{columns}">{cells}</div></td>'
            f'<td class="points"><span class="box"></span> <span class="of">/{fmt(c["max"])}</span></td></tr>'
            f'<tr class="comment"><td colspan="3"><div class="write">Comment</div></td></tr>')
    return f"""<section class="sheet">
<header><h1>{e(title)}</h1>
<div class="field">Presenter<div class="line">{e(presenter)}</div></div>
<div class="field">Topic<div class="line"></div></div>
<div class="score"><span>Score</span><b>/ {fmt(total)}</b></div></header>
<table><colgroup><col class="crit"><col><col class="pts"></colgroup>
<thead><tr><th>Criteria</th><th>Ratings</th><th>Points</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>
<div class="overall">Overall comment</div>
</section>"""


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    shells = sorted(glob.glob(os.path.expanduser(
        "~/.cache/puppeteer/chrome-headless-shell/*/chrome-headless-shell-*/chrome-headless-shell")))
    if shutil.which("chrome-headless-shell"):
        return shutil.which("chrome-headless-shell")
    if shells:
        return shells[-1]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        if shutil.which(name):
            return shutil.which(name)
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        *sorted(glob.glob(os.path.expanduser(
            "~/.cache/puppeteer/chrome/*/chrome-mac*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing")), reverse=True),
        *sorted(glob.glob(os.path.expanduser("~/.cache/puppeteer/chrome/*/chrome-linux*/chrome")), reverse=True),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    sys.exit("Chrome/Chromium not found: set CHROME to its executable.")


def page_count(pdf):
    try:
        import fitz
        with fitz.open(pdf) as doc:
            return doc.page_count
    except ImportError:
        return len(re.findall(rb"/Type\s*/Page[^s]", open(pdf, "rb").read()))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("csv", help="Canvas rubric-export CSV")
    ap.add_argument("-o", "--output", help="PDF to write (default: <csv>-marking-sheet.pdf)")
    ap.add_argument("--names", help="text file, one presenter per line: one pre-named page each")
    args = ap.parse_args()

    title, criteria, shifted = read_rubric(args.csv)
    if shifted:
        print("warning: these criteria look column-shifted (an unquoted comma in the CSV?): "
              + "; ".join(shifted), file=sys.stderr)
    names = [""]
    if args.names:
        names = [n.strip() for n in open(args.names, encoding="utf-8") if n.strip()]
    out = os.path.abspath(args.output or os.path.splitext(args.csv)[0] + "-marking-sheet.pdf")

    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
           f"<style>{CSS}</style></head><body>" + "".join(sheet_html(title, criteria, n) for n in names)
           + "</body></html>")
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "sheet.html")
        open(page, "w", encoding="utf-8").write(doc)
        # --use-mock-keychain: without it macOS Chrome can block on a keychain prompt nobody sees
        subprocess.run([find_chrome(), "--headless", "--disable-gpu", "--use-mock-keychain",
                        "--no-first-run", "--no-default-browser-check", f"--user-data-dir={tmp}/profile",
                        "--no-pdf-header-footer", f"--print-to-pdf={out}", "file://" + page],
                       check=True, capture_output=True, timeout=120)
    pages = page_count(out)
    print(f"{out}: {pages} page(s) for {len(names)} presenter(s)")
    if pages != len(names):
        sys.exit("error: a sheet overflowed its page; shorten the descriptors or reduce the font size in CSS.")


if __name__ == "__main__":
    main()
