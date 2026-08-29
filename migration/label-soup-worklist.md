# Label-soup worklist — Module 3

Regenerate with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```

**The number that matters is the PowerPoint slide.** The `#/n` code is where
the fix goes back in the reveal deck; the two do not match.


## Screenshot these — 10

| Deck | pptx slide | goes to | Slide title | Labels that came loose |
|---|---:|---|---|---|
| 3.2 | **22** | `#/21` | Uniaxial Strain – Compaction | `Fluids` · `Compaction` |
| 3.3 | **7** | `#/6` | Elastic Deformation | `Source: Taryn Lausch` · `State 0` · `State 1` · `State 2` |
| 3.3 | **14** | `#/12` | Strain Calculations | `X` · `Y` · `Z` |
| 3.3 | **15** | `#/13` | Elastic Tensor | `$\sigma_{ij} = C_{ijkl} \cdot \epsilon_{kl}$` · `A hexagonal prism` |
| 3.3 | **16** | `#/14` | Viscous Deformation | `Wikipedia` · `$\sigma_n=\eta \dot{e}$` · `$\sigma_s=\eta \dot{\gamma}$` · `Newtonian` · `Power-law` |
| 3.3 | **21** | `#/18` | Elastic Vs. Viscous Deformation | `Elastic deformation` · `$tM=\frac{\eta}{E}$` |
| 3.3 | **24** | `#/21` | Combined Models (advanced) | `Mechanical analog` · `Strain history curves` |
| 3.3 | **25** | `#/22` | Deformation Controlling Factors | `Granite` · `Brittle failure` · `Plastic flow` · `Marble` |
| 3.3 | **26** | `#/23` | Effect of Confining Pressure | `Marble` · `Strain hardening` · `Strain softening` |
| 3.3 | **29** | `#/26` | Effects of Foliation and Crystal Fabric | `Olivine` |

## Text fixes — 5, no PowerPoint needed

Mine to do. `equation` = a display equation that lost its `$$`;
`caption` = a credit adrift from its figure.


| Deck | pptx slide | goes to | Slide title | Kind |
|---|---:|---|---|---|
| 3.3 | 8 | `#/7` | Young’s Modulus | equation |
| 3.3 | 10 | `#/9` | Poisson’s Ratio | caption |
| 3.3 | 19 | `#/16` | Couette Flow (advanced) | equation |
| 3.3 | 20 | `#/17` | Flow Down An Inclined Plane (advanced) | equation |
| 3.3 | 37 | `#/29/6` | Summary of Deformation Controling Factors | caption |

## Already done

| Deck | pptx | What happened |
|---|---|---|
| 3.2 | 12, 15, 23, 24, 29, 32 | figures replaced, strays cleared |
| 3.2 | 13 | split into three — Longitudinal / Angular / Volumetric |
| 3.2 | 9, 10 | checked clean; one caption reunited with its photo |
| 3.3 | 11, 12 | pseudo-animation — parent slide plus a vertical child |
| 3.3 | 28 | Griggs wet/dry quartz and Fossen pore pressure restored |

## A note on the detector

Until 2026-08-29 it could not see inside `<p class="caption">`, and the
converter had swept loose text boxes in there joined by middots. It now
mines captions carrying three or more fragments, and sorts hits by WHAT
the strays are rather than how many: a bare noun needs the picture, a
relation is an equation, a source is a credit.

