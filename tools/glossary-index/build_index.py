#!/usr/bin/env python3
"""Build a glossary term -> slide index.

For every glossary term, find the slide(s) where the course actually TEACHES it,
and emit a deep link (deck#/h/v). Ranking: a hit in the slide title beats a bold
hit, which beats a plain mention; ties break towards the earlier deck in teaching
order, so the primary reference is where the idea is introduced.
"""
import re, json, pathlib, unicodedata

LECT = pathlib.Path('Lectures')

# teaching order -> (file stem, human label)
DECKS = [
    ("Lecture-1-Introduction", "Introduction"),
    ("Module-i-GlobalTectonics-1", "1.1 Global Deformation Patterns"),
    ("Module-i-GlobalTectonics-1a", "1.1a The Australian Plate"),
    ("Module-i-GlobalTectonics-2", "1.2 Plate Boundaries"),
    ("Module-i-GlobalTectonics-3", "1.3 Stress, Strain and Strength"),
    ("Module-ii-Lecture-1-Structural-Geology-And-Crustal-Deformation", "2.1 Structural Geology"),
    ("Module-ii-Lecture-2-Contractional_Regimes", "2.2 Contractional Regimes"),
    ("Module-ii-Lecture-3-Extensional_Regimes", "2.3 Extensional Regimes"),
    ("Module-ii-Lecture-4-Strike-Slip-Transtention-Transpression", "2.4 Strike-Slip, Transtension & Transpression"),
    ("Module-iii-lecture1-Theory", "3.1 Stress"),
    ("Module-iii-lecture2-Theory", "3.2 Strain and Strain Rate"),
    ("Module-iii-lecture3-Theory", "3.3 Rheology"),
    # Module 4 still points at the -draft decks. The book serves the image
    # decks for now, but those carry no text to index, so the glossary is the
    # only searchable route into this module's content.
    ("Module-iv-lecture4-Brittle-deformation-draft", "4.1 Brittle Deformation"),
    ("Module-iv-lecture5-Joints-Faults-draft", "4.2 Joints and Faults"),
    ("Module-iv-lecture6-Faults-Fault-Zones-draft", "4.3 Faults and Fault Zones"),
    ("Module-iv-lecture7-Tohoku-EQ-draft", "4.4 The Tohoku Earthquake"),
    ("Module-v-lecture1-Fold-Geometry", "5.1 Fold Geometry"),
    ("Module-v-lecture2-Folds-and-Folding-Mechanisms", "5.2 Folds and Folding Mechanisms"),
    ("Module-v-lecture3-Structures-Associated-with-Folding-1", "5.3 Structures Associated with Folding (1)"),
    ("Module-v-lecture3-Structures-Associated-with-Folding-2", "5.4 Structures Associated with Folding (2)"),
    ("Module-v-lecture4-Shear-Zones", "5.5 Shear Zones"),
]

def parse_deck(path):
    """-> list of dicts: {h, v, title, text, bold}"""
    txt = path.read_text()
    txt = re.sub(r'^---\n.*?\n---\n', '', txt, flags=re.S)      # front matter
    slides, h = [], -1
    for hblock in re.split(r'\n<--o-->\n', txt):
        h += 1
        for v, vblock in enumerate(re.split(r'\n<--v-->\n', hblock)):
            m = re.search(r'^#{1,4} (.+)$', vblock, re.M)
            title = m.group(1).strip() if m else ''
            bold = ' '.join(re.findall(r'\*\*(.+?)\*\*', vblock))
            body = re.sub(r'<!--.*?-->', ' ', vblock, flags=re.S)
            body = re.sub(r'<[^>]+>', ' ', body)
            slides.append({'h': h, 'v': v, 'title': norm(title),
                           'bold': norm(bold), 'text': norm(body)})
    return slides

def norm(s):
    """Fold curly quotes and dashes so deck text and glossary terms match."""
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u2013', '-'),
                 ('\u2014', '-'), ('\u2212', '-')):
        s = s.replace(a, b)
    return s

def variants(term):
    """Search strings for a glossary term."""
    t = norm(term)
    t = re.sub(r'\$[^$]*\$', ' ', t)              # drop math
    t = re.sub(r'\([^)]*\)', ' ', t)              # drop parentheticals
    t = t.replace('—', ' ').replace('–', ' ')
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'\s+', ' ', t).strip(' ,:')
    out = set()
    if len(t) >= 4:
        out.add(t.lower())
    # "Fold, chevron" -> also "chevron fold" and "chevron"
    if ',' in t:
        head, tail = [x.strip() for x in t.split(',', 1)]
        if len(tail) >= 4:
            out.add(tail.lower())
            out.add(f'{tail.lower()} {head.lower()}')
    # "X and Y" -> both halves
    if ' and ' in t.lower():
        for half in re.split(r'\s+and\s+', t, flags=re.I):
            if len(half.strip()) >= 5:
                out.add(half.strip().lower())
    # fallback: the distinctive leading word(s), so "Coulomb-Mohr failure
    # criterion" still finds a slide titled "Coulomb-Mohr Failure Criteria"
    GENERIC = {'law','laws','method','criterion','criteria','stress','strain',
               'fault','fold','zone','plate','rock','analysis','theory','number'}
    words = t.split()
    if words:
        w0 = words[0].lower().strip(',')
        if len(w0) >= 6 and w0 not in GENERIC:
            out.add(w0)
        if len(words) >= 2:
            two = ' '.join(words[:2]).lower().strip(',')
            if len(two) >= 8:
                out.add(two)
    return {v for v in out if len(v) >= 4}

def find(term, decks_parsed):
    """Return up to 3 references, best first. A title hit where the term is most
    of the title is the strongest signal that this is where the idea is taught."""
    hits = []
    for order, (stem, label) in enumerate(DECKS):
        for s in decks_parsed.get(stem, []):
            if s['h'] == 0:            # deck title slide: never a useful reference
                continue
            score = 0
            for v in variants(term):
                pat = re.compile(r'\b' + re.escape(v) + r'\b', re.I)
                if pat.search(s['title']):
                    # reward the term being a large fraction of the title
                    ratio = len(v) / max(len(s['title']), 1)
                    score = max(score, 3 + min(ratio, 1.0))
                elif pat.search(s['bold']):
                    score = max(score, 2)
                elif pat.search(s['text']):
                    score = max(score, 1)
            if score:
                hits.append((score, -order, stem, label, s))
    if not hits:
        return []
    hits.sort(key=lambda x: (-x[0], -x[1]))
    hits = [h for h in hits if h[0] >= 2]
    if not hits:
        return []
    out, seen = [], set()
    for score, negorder, stem, label, s in hits:
        if stem in seen:               # at most one reference per deck
            continue
        seen.add(stem)
        out.append({'deck': stem, 'label': label, 'h': s['h'], 'v': s['v'],
                    'slide': s['title'], 'score': round(score, 2)})
        if len(out) == 3:
            break
    return out

def main():
    parsed = {}
    for stem, _ in DECKS:
        p = LECT / f'{stem}.reveal.md'
        if p.exists():
            parsed[stem] = parse_deck(p)

    gl = pathlib.Path('Jupyterbook/Glossary.md').read_text()
    body = gl.split('```{glossary}\n', 1)[1].rsplit('```', 1)[0]
    terms = [l for l in body.split('\n') if l and not l.startswith(':') and not l.startswith(' ')]

    index, misses = {}, []
    for t in terms:
        refs = find(t, parsed)
        if refs:
            index[t] = refs
        else:
            misses.append(t)

    pathlib.Path('/tmp/term_index.json').write_text(json.dumps(index, indent=1))
    print(f'terms: {len(terms)}   located: {len(index)}   not found: {len(misses)}')
    from collections import Counter
    print('refs per term:', dict(Counter(len(v) for v in index.values())))
    print('strong (title) primaries:', sum(1 for v in index.values() if v[0]['score'] >= 3))
    print('\nspot-check previously-wrong terms:')
    for t in ('Fabric','Foliation','Lineation','Fracture','Fault','Fold, inclined',
              'Mohr circle','Cleavage','Boudinage','Vergence','Mylonite'):
        if t in index:
            print(f'  {t:16s} ' + ' | '.join(f'{r["label"]} #{r["h"]}/{r["v"]} "{r["slide"][:34]}"' for r in index[t]))
    print('\nnot found (' + str(len(misses)) + '):', ', '.join(misses[:30]))

main()
