#!/usr/bin/env python3
"""Convert extracted pptx manifest slides -> reveal markdown using templates + roles.
Usage: convert_deck.py <manifest.json> <img_relpath_prefix> <first> <last> <out.reveal.md> [title]"""
import sys, json, re, pathlib

SMALL = {"and","or","the","of","in","on","a","to","via","for","with","from","as","at","by"}
KEEP_UPPER = {"3D","2D","1D","ANU","ETH","USGS","GPS","NB","2P","P","S"}
BARE_URL = re.compile(r"^\s*(https?://|www\.)?[\w.-]+\.(com|org|edu|au|net|gov)(/\S*)?\s*$", re.I)

def recase(t):
    letters = [c for c in t if c.isalpha()]
    if not letters or sum(c.isupper() for c in letters) / len(letters) < 0.8:
        return t
    out = []
    for i, w in enumerate(t.split()):
        bare = re.sub(r"[^A-Za-z0-9]", "", w)
        if bare.upper() in KEEP_UPPER or any(ch.isdigit() for ch in w):
            out.append(w)
        elif i > 0 and bare.lower() in SMALL:
            out.append(w.lower())
        else:
            out.append(w.capitalize())
    return " ".join(out)

def is_caps(t):
    letters = [c for c in t if c.isalpha()]
    return letters and sum(c.isupper() for c in letters) / len(letters) >= 0.85

def img(prefix, im, extra=""):
    return f'![]({prefix}/{im["file"]}){extra}'

def img_sized(prefix, im, container_pct):
    """Image sized from its pptx display geometry: im['w'] is % of slide width;
    container_pct is the container's approximate % of slide width. Emits a width
    style only when meaningfully smaller than the container (fixes e.g. a tiny
    icon rendering at full column width)."""
    w = im.get("w") or 0
    rel = round(min(100.0, w / container_pct * 100)) if w else 100
    if rel >= 95:
        return img(prefix, im)
    return img(prefix, im, f' <!-- .element style="width:{rel}%;" -->')

def img_block(prefix, imgs, container_pct):
    """Emit images preserving pptx rows: images that sat side-by-side (similar y)
    go into a nested flex row instead of stacking."""
    rows = []
    for im in sorted(imgs, key=lambda i: (i["y"], i["x"])):
        if rows and abs(im["y"] - rows[-1][0]["y"]) < 8:
            rows[-1].append(im)
        else:
            rows.append([im])
    out = []
    for row in rows:
        row.sort(key=lambda i: i["x"])
        if len(row) == 1:
            out.append(img_sized(prefix, row[0], container_pct))
        else:
            out.append('<div class="cols">')
            for im in row:
                out += ['', img(prefix, im), '']
            out.append('</div>')
        out.append("")
    return "\n".join(out).strip()

def caption_block(caps):
    caps = [c for c in caps if not BARE_URL.match(c)]          # drop bare-URL noise
    if not caps:
        return []
    return [f'<p class="caption">{" · ".join(caps)}</p>']

def order(items):
    return sorted(items, key=lambda t: (round(t["y"]), round(t["x"])))

def pick_title(s):
    titles = [t for t in s["texts"] if t["role"] == "title"]
    body = [t for t in s["texts"] if t["role"] == "body"]
    if titles:
        return titles[0]["text"].replace("\n", " ").strip(), body
    # else: promote a short, top, large-font body text
    cands = [t for t in body if len(t["text"].split()) <= 12 and "\n" not in t["text"].strip()]
    if cands:
        cands.sort(key=lambda t: (-(t["font"] or 0), t["y"]))
        top = cands[0]
        if (top["font"] or 0) >= 18 or is_caps(top["text"]):
            return top["text"].strip(), [t for t in body if t is not top]
    return "", body

def tidy(s):
    return s.replace(" -> ", " → ").replace("->", "→")

def text_md(bodies):
    out = []
    for t in order(bodies):
        t = {**t, "lines": [tidy(l) for l in t["lines"]]}
        if t["bullets"]:
            for ln in t["lines"]:
                out.append(f"- {ln}")
        else:
            for ln in t["lines"]:
                out.append(f"**{ln}**" if is_caps(ln) and len(ln.split()) <= 8 else ln)
        out.append("")
    return "\n".join(out).strip()

def find_text(s, needle):
    for t in s["texts"]:
        if needle in t["text"].lower():
            return t
    return None

def title_slide(s, course, module):
    out = [f'<!-- source: {s["source_ref"]} · template: T-title -->',
           f"# {course}", "", f"## {module}", ""]
    credits = find_text(s, "convenor") or find_text(s, "(lecturer)")
    if credits:
        for ln in credits["lines"]:
            out.append(f"  - {ln}")
        out.append("")
    out += ["Australian National University", ""]
    lic = find_text(s, "creative commons") or find_text(s, "nb:")
    if lic:
        txt = re.sub(r"^\s*NB:\s*", "", lic["text"].replace("\n", " ").strip(), flags=re.I)
        out.append(f"_**NB:** {txt}_")
    return "\n".join(out)

def resources_slide(s):
    out = [f'<!-- source: {s["source_ref"]} · template: T-resources -->', "## Resources", ""]
    refs = []
    for t in s["texts"]:
        refs += [l for l in t["lines"] if len(l) > 15]
    for r in refs:
        out.append(f"1. {r}")
    return "\n".join(out)

def convert_slide(s, prefix, course="EMSC 3002", module="Module 3", plain=False):
    # plain mode (research talks): no course title/resources/ILO scaffolding —
    # every slide goes through the ordinary templates.
    if not plain:
        if s["n"] == 1:
            return title_slide(s, course, module)
        if s["n"] == 2:
            return resources_slide(s)
    tmpl = s["template_guess"]
    title, bodies = pick_title(s)
    caps = [t["text"].replace("\n", " ").strip() for t in s["texts"] if t["role"] == "caption"]
    imgs = [im for im in s["images"] if im.get("file")]
    out = [f'<!-- source: {s["source_ref"]} · template: {tmpl} -->']
    H = f"## {recase(title)}" if title else ""

    if tmpl == "T4-full-figure" and imgs:
        big = max(imgs, key=lambda i: i["w"] * i["h"])
        out.append(f'<!-- .slide: data-background="{prefix}/{big["file"]}" -->')

    elif tmpl == "T6-two-image" and len(imgs) >= 2:
        if H: out.append(H)
        a, b = sorted(imgs, key=lambda i: i["x"])[:2]
        # each image wrapped in its own <div> with surrounding blank lines, so
        # reveal's markdown pass parses the ![](...) (bare images directly inside
        # a block-level <div> are treated as raw HTML and left unrendered).
        out.append('<div class="cols">')
        for im in (a, b):
            out += ['<div>', '', img_sized(prefix, im, 48), '', '</div>']
        out.append('</div>')
        out += caption_block(caps)

    elif tmpl == "T5-figure-focus" and imgs:
        if H: out.append(H)
        big = max(imgs, key=lambda i: i["w"] * i["h"])
        out.append(img(prefix, big, ' <!-- .element class="r-stretch" -->'))
        out += caption_block(caps)

    elif tmpl == "T3-text-and-image" and imgs:
        if H: out.append(H)
        tb = text_md(bodies) or "&nbsp;"
        imgblock = img_block(prefix, imgs, 37)   # image column ~37% of slide (flex 1 vs 1.7)
        col_img = ['<div>', "", imgblock] + (["", *caption_block(caps)] if caps else []) + ["", '</div>']
        col_txt = ['<div class="wide">', "", tb, "", '</div>']
        out.append('<div class="cols">')
        out += (col_txt + col_img) if imgs[0]["x"] >= 45 else (col_img + col_txt)
        out.append('</div>')

    elif tmpl == "T2-bullets":
        if H: out.append(H)
        out.append(text_md(bodies))
        out += caption_block(caps)

    else:  # T1-prose / T0
        if H: out.append(H)
        if bodies: out.append(text_md(bodies))
        if imgs: out.append(img_block(prefix, imgs, 100))
        out += caption_block(caps)

    if s["notes"]:
        out += ["", "Note:", s["notes"]]
    return "\n".join(x for x in out if x is not None)

def main():
    plain = "--plain" in sys.argv
    argv = [a for a in sys.argv if a != "--plain"]
    man = json.loads(pathlib.Path(argv[1]).read_text())
    prefix, first, last, outpath = argv[2], int(argv[3]), int(argv[4]), argv[5]
    title = argv[6] if len(argv) > 6 else "Theory (draft)"
    module = argv[7] if len(argv) > 7 else "Module 3"
    fm = ("---\n" f"title: {title}\n"
          "separator: '<--o-->'\nverticalSeparator: '<--v-->'\n"
          "revealOptions:\n    transition: 'fade'\n    slideNumber: true\n"
          "    width: 1200\n    height: 800\n    margin: 0.07\n---\n")
    slides = [s for s in man["slides"] if first <= s["n"] <= last]
    parts = [convert_slide(s, prefix, "EMSC 3002", module, plain=plain) for s in slides]
    # course decks: insert the what-you-will-learn placeholder after Resources.
    idxs = [] if plain else [i for i, s in enumerate(slides) if s["n"] == 2]
    if idxs:
        ilo = ("<!-- ILO placeholder — not in the pptx; fill in -->\n"
               "## What you will learn in this module\n\n"
               "<!-- TODO: add what you will learn in this module -->")
        parts.insert(idxs[0] + 1, ilo)
    body = "\n\n<--o-->\n\n".join(parts)
    pathlib.Path(outpath).write_text(fm + "\n" + body + "\n")
    print(f"wrote {outpath}: {len(slides)} slides")

if __name__ == "__main__":
    main()
