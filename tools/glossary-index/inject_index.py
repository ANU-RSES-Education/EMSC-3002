"""Write the term index from build_index.py back into Glossary.md.

`build_index.py` analyses the decks and emits /tmp/term_index.json; this
puts the resulting `*Slides: …*` lines into the glossary. Splitting the
two means the index can be inspected before it is committed.

Usage (from the repo root, after build_index.py):

    pixi run python tools/glossary-index/inject_index.py

Every term gets at most one `*Slides:*` line, immediately after its
definition block. Existing lines are REPLACED, so re-running after a
deck edit refreshes drifted coordinates rather than accumulating.
"""
import json
import pathlib
import re
import sys

GLOSSARY = pathlib.Path("Jupyterbook/Glossary.md")
INDEX = pathlib.Path("/tmp/term_index.json")
SLIDES_RE = re.compile(r"^\s*\*Slides: .*\*\s*$")


def ref_link(r):
    frag = f"#/{r['h']}" + (f"/{r['v']}" if r.get("v") else "")
    return (f"[{r['label']} — {r['slide']}]"
            f"(/slideshows/{r['deck']}.reveal.html{frag})")


def main():
    if not INDEX.exists():
        sys.exit("run build_index.py first — /tmp/term_index.json missing")
    index = json.loads(INDEX.read_text())
    text = GLOSSARY.read_text()
    head, rest = text.split("```{glossary}\n", 1)
    body, tail = rest.rsplit("```", 1)

    lines = body.split("\n")
    out, i, n_written, n_cleared = [], 0, 0, 0
    while i < len(lines):
        line = lines[i]
        # a term is a non-indented, non-definition, non-blank line
        is_term = bool(line) and not line.startswith((":", " ", "\t"))
        out.append(line)
        i += 1
        if not is_term:
            continue
        # copy the definition block, dropping any existing Slides line
        while i < len(lines):
            nxt = lines[i]
            if nxt and not nxt.startswith((":", " ", "\t")):
                break                       # next term
            if SLIDES_RE.match(nxt):
                n_cleared += 1
                i += 1
                # swallow a blank line that belonged to the old entry
                if i < len(lines) and not lines[i].strip():
                    i += 1
                continue
            out.append(nxt)
            i += 1
        refs = index.get(line)
        if refs:
            while out and not out[-1].strip():
                out.pop()
            out.append("")
            out.append("  *Slides: "
                       + " · ".join(ref_link(r) for r in refs) + "*")
            out.append("")
            n_written += 1

    GLOSSARY.write_text(head + "```{glossary}\n"
                        + "\n".join(out) + "```" + tail)
    print(f"cleared {n_cleared} old Slides lines, wrote {n_written} "
          f"({len(index)} terms in the index)")


if __name__ == "__main__":
    main()
