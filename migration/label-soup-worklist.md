# Label-soup worklist

**All of Module 3 is clear** as of 2026-08-29 — 3.1, 3.2 and 3.3 all report
zero. Regenerate for any deck with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```

**The number that matters is the PowerPoint slide.** The `#/n` code is where
the fix goes back in the reveal deck; the two do not match.


## What was done

| Deck | pptx | What happened |
|---|---|---|
| 3.1 | 19, 31 | a sentence rejoined and an equation that had split into two inline spans |
| 3.2 | 12, 15, 22, 23, 24, 29, 32 | figures replaced, strays cleared |
| 3.2 | 13 | split into three — Longitudinal / Angular / Volumetric |
| 3.2 | 9, 10 | checked clean; one caption reunited with its photo |
| 3.3 | 7, 13, 14, 15, 16, 21, 24, 25, 26, 29 | figures replaced, strays cleared |
| 3.3 | 11, 12 | pseudo-animation — parent slide plus a vertical child |
| 3.3 | 28 | Griggs wet/dry quartz and Fossen pore pressure restored |
| 3.3 | 23 | checked — extracted figure was already complete, no action |

## Next, when wanted

Module 4.4 reports 13 and Module 5 has its own; neither has been touched.


## What the detector learned

Two rounds of false alarms shaped it, and both are worth knowing:

- It could not see inside `<p class="caption">`, where the converter had
  swept loose text boxes joined by middots. Now mines captions carrying
  three or more fragments — a damaged one has many, a written one has a
  description and a credit.

- Then it over-fired on Module 3.1, a heavily hand-worked deck, calling
  `Assumptions:`, `and`, and whole sentences 'strays'. A label is now a
  short noun phrase: no terminal punctuation, at most five words, not a
  connective. Bare maths counts only if it is a SYMBOL — a relation is a
  step of a derivation someone chose not to centre.

