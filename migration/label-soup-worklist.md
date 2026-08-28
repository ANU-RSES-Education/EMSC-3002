# Label-soup worklist — Module 3.2 and 3.3

Slides where the pptx converter kept the picture but scattered its labels
into the body text. Regenerate at any time with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```

**The number that matters is the PowerPoint slide.** The `#/n` code is where
the fix goes back in the reveal deck; the two do not match.


## Screenshot these — 4 left


### 3.2 Strain and Strain Rate — `Lecture2_Strain_StrainRate.pptx`

| pptx slide | goes to | Slide title | Stray labels to delete |
|---:|---|---|---|
| **13** | `#/10` | Quantify Strain | `$\Delta x$` · `$\phi$` · `$y$` · `$\gamma =\tan \phi = \frac{\Delta x}{y}$` |

### 3.3 Rheology — `Lecture3_Rheology.pptx`

| pptx slide | goes to | Slide title | Stray labels to delete |
|---:|---|---|---|
| **11** | `#/10` | Elastic Deformation in 3D | `$E= \frac{\sigma_n}{\epsilon_n}$` · `Normal strain from $\sigma_{zz}$:  $\sigma_{zz}=E \cdot (\epsilon_{zz}-\epsilon_{zz}'-\epsilon_{zz}'')$` · `Young’s modulus` · `Poisson’s ratio` |
| **12** | `#/11` | Elastic Deformation in 3D | `$E= \frac{\sigma_n}{\epsilon_n}$` · `Young’s modulus` · `Poisson’s ratio` |
| **28** | `#/26` | Presence of Fluids | `950 °C, Dry Quartz` · `20` · `Stress kbars` · `10` · `950 °C, Wet Quartz` · `Griggs, GJI. 1967` · +4 |

## Done — screenshots dropped in 2026-08-28

Images live in `Lectures/Module-iii-Theory/Lecture2-restored/`.


| pptx slide | goes to | Slide title |
|---:|---|---|
| **12** | `#/9` | Summary — stress behind us, strain ahead |
| **15** | `#/12` | Example: Quantify Strain in a Rock |
| **23** | `#/20` | Pure Shear and Simple Shear |
| **24** | `#/21` | Flinn Diagram |
| **29** | `#/26` | Summary — strain, measured from displacement |
| **32** | `#/29` | Strain Rate |

## Text fixes — 19 slides, no PowerPoint needed

Mine to do. `caption` = a caption or credit adrift from its figure;
`equation` = a display equation that lost its `$$`; `rewrap` = prose the
converter split into fragment bullets mid-sentence.


| Deck | pptx slide | goes to | Slide title | Kind |
|---|---:|---|---|---|
| 3.2 | 11 | `#/8` | Homogeneous & Heterogeneous Strain | caption |
| 3.2 | 14 | `#/11` | Example: Quantify Strain in a Rock | caption |
| 3.2 | 19 | `#/16` | Principal Strain: Strain Ellipsoid | caption |
| 3.2 | 21 | `#/18` | Volume Change | caption |
| 3.2 | 22 | `#/19` | Uniaxial Strain – Compaction | caption |
| 3.2 | 26 | `#/23` | The Fry Method for Strain Analysis | caption |
| 3.2 | 28 | `#/25` | Stress Vs. Strain | caption |
| 3.2 | 31 | `#/28` | Example: Strain from a Seismic Wave | rewrap |
| 3.3 | 8 | `#/7` | Young’s Modulus | equation |
| 3.3 | 10 | `#/9` | Poisson’s Ratio | caption |
| 3.3 | 15 | `#/14` | Elastic Tensor | caption |
| 3.3 | 16 | `#/15` | Viscous Deformation | equation |
| 3.3 | 19 | `#/17` | Couette Flow (advanced) | equation |
| 3.3 | 20 | `#/18` | Flow Down An Inclined Plane (advanced) | equation |
| 3.3 | 21 | `#/19` | Elastic Vs. Viscous Deformation | caption |
| 3.3 | 24 | `#/22` | Combined Models (advanced) | caption |
| 3.3 | 25 | `#/23` | Deformation Controlling Factors | caption |
| 3.3 | 29 | `#/27` | Effects of Foliation and Crystal Fabric | caption |
| 3.3 | 37 | `#/30/6` | Summary of Deformation Controling Factors | caption |

## Checked and clean

- **pptx 9**, *Displacement Vector* — both figures came across whole.
- **pptx 10**, *Strain* — one caption line had drifted; fixed 2026-08-28.

