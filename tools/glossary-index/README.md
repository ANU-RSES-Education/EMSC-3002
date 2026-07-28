# Glossary → slide index

Regenerates the *Slides:* cross-references under each glossary entry, turning the
glossary into an index **into** the lecture material: look a term up, and the
entry tells you which decks teach it and links straight to the slide.

```bash
pixi run python tools/glossary-index/build_index.py     # analyse + write /tmp/term_index.json
```

then re-inject (see the commit that introduced this for the injection snippet), or
simply re-run the whole thing when slides have moved.

## How references are chosen

Each deck is parsed into slides with their reveal coordinates (`#/h` or `#/h/v`).
For every glossary term the script scores each slide:

| where the term appears | score |
|---|---|
| slide **title** | 3 + how much of the title the term accounts for |
| **bold** text on the slide | 2 |
| body text only | 1 — *discarded* |

Bare body mentions are deliberately thrown away: for an index, a wrong link is
worse than a missing one. Up to three references are kept per term, best first,
at most one per deck — so a concept taught twice (the Mohr circle in 3.1 and
again in 4.1) shows both, which is exactly what you want from an index.

Matching folds curly quotes and dashes (decks and glossary punctuate
differently), strips maths and parentheticals, and falls back to the distinctive
leading words so "Coulomb–Mohr failure criterion" still finds a slide titled
"Coulomb-Mohr Failure Criteria".

## Maintenance

Slide coordinates shift if slides are inserted or removed, so **re-run this after
substantial deck edits**. The link text carries the slide title as well as the
number, so a drifted link still tells the reader what to look for. The script
self-checks: every emitted reference is verified to resolve to the slide title it
claims.

Coverage is currently 173 of 307 terms. Raising it means accepting weaker
(body-mention) matches — a deliberate trade-off, changed by keeping `score >= 1`
in `find()`.
