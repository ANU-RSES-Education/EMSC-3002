# Label-soup worklist

Label soup in Module 3 is cleared. What is left is a DIFFERENT failure:
figures drawn with native PowerPoint shapes, which the converter never
extracted at all, because it only pulls out embedded pictures. The slide
kept the diagram's text boxes and lost the diagram.

Regenerate with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```


## Figures that never converted — 4 in Module 3

Screenshot the pptx slide; the labels listed are all that survived.

| Deck | pptx slide | goes to | Slide title | What the diagram showed |
|---|---:|---|---|---|
| 3.2 | **16** | `#/15` | Quantify Strain with Displacement | `(Advanced)` · `= $\frac{u1(B)-u1(A)}{AB}$` · `Before stretching` · `AA’ = $u1(A)$` · `BB’ = $u1\left( B \right)$` |
| 3.2 | **17** | `#/16` | Quantify Strain with Displacement | `$\Delta x$` · `$\phi$` · `$y$` · `Simple shear` · `Sub-simple shear` · `$x2$` · +10 |
| 3.2 | **41** | `#/36/5` | Pure Shear and Simple Shear | `$x_2$` · `$x_2$` · `y` · `y` · `Before` · `Before` · +14 |
| 3.3 | **22** | `#/19` | Strain Hardening and Softening | `` · `Yield point` · `Strain hardening` · `Yield stress` · `Perfect plastic` · `Elastic` · +3 |

`3.2 #/36/5` sits after the deck's final Summary and is already flagged
PARKED, so it may not be worth a screenshot until that slide has a home.


## Across the repo

Fifteen slides in all show this pattern; four are in Module 3. The rest
are in Modules 4 and 5 and have not been looked at.


## Module 3 label soup — done

| Deck | pptx | What happened |
|---|---|---|
| 3.1 | 19, 31 | a sentence rejoined, an equation un-split |
| 3.2 | 12, 13, 15, 22, 23, 24, 29, 32 | figures replaced, strays cleared; 13 split into three |
| 3.3 | 7, 11–16, 21, 24, 25, 26, 28, 29 | figures replaced, strays cleared; 11/12 made a build |
| 3.3 | 23 | checked — already complete, no action |
