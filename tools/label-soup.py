"""Find slides where a pptx diagram's labels were shredded into the body text.

When the pptx converter met a picture with text boxes floating on top of it,
the picture came across but every label became its own paragraph. The result
renders as a diagram followed by a scatter of stray words and half-equations,
and it is the single most common conversion casualty in this repo.

These are cheap to fix by hand -- screenshot the original slide and drop the
image in whole -- but only if you know which slides to screenshot. That is
what this prints.

The signature it looks for: a slide that contains an image AND three or more
"orphan" lines -- short, standalone, not bullets, headings, HTML or speaker
notes. Bare maths counts, since axis labels and inline formulae are what
usually break loose.

Two kinds of hit, and they want different fixes:

  * scattered DIAGRAM LABELS ("Past", "Today", "ln(X/Y)", "$\\phi$") --
    screenshot the original slide, replace the image, delete the strays;
  * a DISPLAY EQUATION that lost its $$ block and is now a bare line --
    no screenshot needed, just wrap it.

Likely figure credits are tagged so they do not read as damage.

Run:  pixi run python tools/label-soup.py Lectures/Module-iii-*-draft.reveal.md
"""
import pathlib
import re
import sys

SKIP = ("#", "<", "-", "*", "!", "|", "Note:", "$$", "1.", "2.", "3.")
CREDIT = re.compile(r"(wikipedia|usgs|,\s*(u\w*|the )?\w*(univ|usyd|uc |gji|\d{4}))",
                    re.I)


def orphans(block):
    """Short standalone lines: what a shredded text box leaves behind."""
    out = []
    for ln in block.split("\n"):
        t = ln.strip()
        if not t or t.startswith(SKIP) or t.startswith("<--"):
            continue
        bare = re.sub(r"[*_`$\\]|&[a-z]+;|&#\d+;", "", t).strip()
        if not bare or len(bare) > 34:
            continue
        # a short line that is still a whole sentence is prose, not a label
        if bare.endswith((".", ":", "?", "!")) and len(bare.split()) > 4:
            continue
        out.append(t)
    return out


def scan(path):
    txt = pathlib.Path(path).read_text()
    txt = re.sub(r"^---\n.*?\n---\n", "", txt, flags=re.S)          # front matter
    txt = re.sub(r"Note:\n.*?(?=\n<--|\Z)", "", txt, flags=re.S)    # speaker notes
    hits = []
    h = -1
    for hblock in re.split(r"\n<--o-->\n", txt):
        h += 1
        for v, vb in enumerate(re.split(r"\n<--v-->\n", hblock)):
            o = orphans(vb)
            if len(o) < 3 or "![" not in vb:
                continue
            m = re.search(r"^#{1,4} (.+)$", vb, re.M)
            title = re.sub(r"&#?\w+;", "", m.group(1)).strip() if m else "(untitled)"
            hits.append((f"#/{h}" + (f"/{v}" if v else ""), title, o))
    return hits


total = 0
for path in sys.argv[1:]:
    hits = scan(path)
    total += len(hits)
    print(f"\n=== {pathlib.Path(path).name}  ({len(hits)} slides)")
    for coord, title, o in hits:
        print(f"  {coord:<9} {len(o):>2}  {title[:52]}")
        for x in o[:10]:
            tag = "  (credit?)" if CREDIT.search(x) else ""
            print(f"             · {x[:58]}{tag}")
print(f"\n{total} slides to screenshot" if total else "\nnothing to screenshot")
