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

Each hit reports the SOURCE pptx and slide number, taken from the converter's
own provenance comment, because the fix starts in PowerPoint and hunting for
the matching original is most of the work.

Run:  pixi run python tools/label-soup.py Lectures/Module-iii-*-draft.reveal.md
      pixi run python tools/label-soup.py --table Lectures/*.reveal.md
"""
import pathlib
import re
import sys

SKIP = ("#", "<", "-", "*", "!", "|", "Note:", "$$", "1.", "2.", "3.")
# a credit names a source: a site, a year, or "Someone, Somewhere"
CREDIT = re.compile(r"(wikipedia|usgs|www\.|https?:|\b\d{4}\b"
                    r"|,\s*[A-Z][\w.']*(\s+[A-Z][\w.']*)*\s*$)", re.I | re.M)
SOURCE = re.compile(r"<!--\s*source:\s*(\S+?\.pptx)\s+slide\s+(\d+)", re.I)
# A bare RELATION that lost its $$ block is an equation, not a loose label:
# fix it in text. A bare SYMBOL ("$\phi$", "$y$") is a diagram label and does
# need the screenshot -- hence the "=" test as well as the maths test.
EQUATION = re.compile(r"^\$[^$]*=[^$]*\$$")
MATHY = re.compile(r"^\$[^$]*\$$")
# the converter also turned soft-wrapped prose into separate bullets, which
# is a third defect with a third fix: rejoin them, no screenshot needed
FRAGMENT = re.compile(r"^-\s+(and|or|where|which|but|the|a|to|for|with|of|in)\b|^-\s+[a-z]")


def orphans(block):
    """Short standalone lines: what a shredded text box leaves behind."""
    # a multi-line $$...$$ block is one equation, not a stack of strays,
    # and a multi-line HTML comment is not content at all
    block = re.sub(r"\$\$.*?\$\$", " ", block, flags=re.S)
    block = re.sub(r"<!--.*?-->", " ", block, flags=re.S)
    # The converter also swept loose text boxes INTO the caption, joined with
    # middots -- "Jaeger and Cook, 1979 · Brittle failure · Plastic flow ·
    # Fossen, 2011 · Marble". Those are diagram labels too, and they were
    # invisible here because caption lines start with "<". Pull them out.
    caps = re.findall(r'<p class="caption">(.*?)</p>', block, flags=re.S)
    block = re.sub(r'<p class="caption">.*?</p>', " ", block, flags=re.S)
    for cap in caps:
        parts = re.split(r"\u00b7|&middot;", cap)
        # The converter swept several loose text boxes into one caption, so a
        # damaged caption has MANY fragments. A caption written by hand has a
        # description and a credit -- two. Only mine the crowded ones.
        if len(parts) < 3:
            continue
        for part in parts:
            part = part.strip()
            # a credit belongs in a caption; so does a descriptive sentence I
            # wrote. Only a SHORT bare noun -- "Granite", "Brittle failure",
            # "State 0" -- is a diagram label that lost its diagram.
            if not part or len(part) > 26 or "<" in part or CREDIT.search(part):
                continue
            block += "\n" + part
    out = []
    for ln in block.split("\n"):
        t = ln.strip()
        if not t or t.startswith(SKIP) or t.startswith("<--"):
            continue
        bare = re.sub(r"[*_`$\\]|&[a-z]+;|&#\d+;", "", t).strip()
        if not bare:
            continue
        # A label is short. A CAPTION can be long but is still a noun phrase:
        # no terminal full stop, and not many words. Prose has both.
        if len(bare) > 34 and not (len(bare.split()) <= 12
                                   and not bare.endswith((".", "!", "?"))):
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
            if not o or "![" not in vb:
                continue
            m = re.search(r"^#{1,4} (.+)$", vb, re.M)
            title = re.sub(r"&#?\w+;", "", m.group(1)).strip() if m else "(untitled)"
            src = SOURCE.search(vb)
            src = f"{src.group(1)} s{src.group(2)}" if src else "—"
            real = [x for x in o if not CREDIT.search(x)]
            kind = ("equation" if real and all(EQUATION.match(x) for x in real)
                    else "screenshot")
            frags = sum(1 for ln in vb.split("\n") if FRAGMENT.match(ln.strip()))
            if frags >= 2 and kind == "screenshot" and not any(
                    MATHY.match(x) and len(x) < 12 for x in real):
                kind = "rewrap"
            # Count is a poor guide -- a graph can lose exactly one label.
            # Sort by WHAT the strays are: a bare noun ("Granite", "State 0")
            # is a diagram label and needs the picture; a credit belongs in a
            # caption; a relation is an equation that lost its $$.
            labels = [x for x in real
                      if not MATHY.match(x) and not EQUATION.match(x)]
            if kind == "screenshot" and not labels:
                kind = "caption" if not real else "equation"
            elif kind == "screenshot" and real and not labels:
                kind = "caption"
            hits.append((f"#/{h}" + (f"/{v}" if v else ""), title, src, kind,
                         o, frags))
    return hits


args = sys.argv[1:]
as_table = "--table" in args
paths = [a for a in args if a != "--table"]

if as_table:
    print("| Deck | Slide | Title | Screenshot from | Fix | Strays |")
    print("|---|---|---|---|---|---|")
for path in paths:
    hits = scan(path)
    name = pathlib.Path(path).name.replace(".reveal.md", "")
    if as_table:
        for coord, title, src, kind, o, frags in hits:
            strays = " · ".join(f"`{x}`" for x in o[:6])
            if len(o) > 6:
                strays += f" · +{len(o) - 6}"
            print(f"| {name} | `{coord}` | {title} | {src} | {kind} | {strays} |")
        continue
    print(f"\n=== {name}  ({len(hits)} slides)")
    for coord, title, src, kind, o, frags in hits:
        print(f"  {coord:<9} {len(o):>2}  {kind:<10} {src:<34} {title[:44]}")
        for x in o[:10]:
            tag = "  (credit?)" if CREDIT.search(x) else ""
            print(f"             · {x[:58]}{tag}")
