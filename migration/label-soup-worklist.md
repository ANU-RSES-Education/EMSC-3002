# Label-soup worklist — Module 3.3

**Module 3.2 is done** — every shredded diagram replaced and every stray
label cleared, 2026-08-28. What follows is 3.3 only.

Regenerate with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```

**The number that matters is the PowerPoint slide.** The `#/n` code is where
the fix goes back in the reveal deck; the two do not match.


## Screenshot these — 3

### 3.3 Rheology — `Lecture3_Rheology.pptx`

| pptx slide | goes to | Slide title | Stray labels to delete |
|---:|---|---|---|
| **11** | `#/10` | Elastic Deformation in 3D | `$E= \frac{\sigma_n}{\epsilon_n}$` · `Normal strain from $\sigma_{zz}$:  $\sigma_{zz}=E \cdot (\epsilon_{zz}-\epsilon_{zz}'-\epsilon_{zz}'')$` · `Young’s modulus` · `Poisson’s ratio` |
| **12** | `#/11` | Elastic Deformation in 3D | `$E= \frac{\sigma_n}{\epsilon_n}$` · `Young’s modulus` · `Poisson’s ratio` |
| **28** | `#/26` | Presence of Fluids | `950 °C, Dry Quartz` · `20` · `Stress kbars` · `10` · `950 °C, Wet Quartz` · `Griggs, GJI. 1967` · +4 |

On the two *Elastic Deformation in 3D* slides the loose bits are figure
annotations, but the three `Effective strain from …` lines beneath them are
real derivation. Screenshot the figure; the working stays as text.


## Text fixes — 11, no PowerPoint needed

Mine to do. `caption` = a caption or credit adrift from its figure;
`equation` = a display equation that lost its `$$`.


| pptx slide | goes to | Slide title | Kind |
|---:|---|---|---|
| 8 | `#/7` | Young’s Modulus | equation |
| 10 | `#/9` | Poisson’s Ratio | caption |
| 15 | `#/14` | Elastic Tensor | caption |
| 16 | `#/15` | Viscous Deformation | equation |
| 19 | `#/17` | Couette Flow (advanced) | equation |
| 20 | `#/18` | Flow Down An Inclined Plane (advanced) | equation |
| 21 | `#/19` | Elastic Vs. Viscous Deformation | caption |
| 24 | `#/22` | Combined Models (advanced) | caption |
| 25 | `#/23` | Deformation Controlling Factors | caption |
| 29 | `#/27` | Effects of Foliation and Crystal Fabric | caption |
| 37 | `#/30/6` | Summary of Deformation Controling Factors | caption |

## Module 3.2 — cleared 2026-08-28

Screenshots dropped in for pptx 12, 15, 23, 24, 29, 32; pptx 13 split into
three slides (Longitudinal / Angular / Volumetric); eight text fixes applied.
Images in `Lectures/Module-iii-Theory/Lecture2-restored/`.

