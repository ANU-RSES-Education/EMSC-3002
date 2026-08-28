# Label-soup worklist — Module 3

**All screenshot work is done.** 3.2 was cleared on 2026-08-28; 3.3's three
shredded figures went in the same day. What is left is text fixes only, and
they need no PowerPoint.

Regenerate with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```


## Text fixes — 11 slides in 3.3

`caption` = a caption or credit adrift from its figure; `equation` = a display
equation that lost its `$$`.


| pptx slide | goes to | Slide title | Kind | Strays |
|---:|---|---|---|---|
| 8 | `#/7` | Young’s Modulus | equation | `$E= \frac{\sigma_n}{\epsilon_n}$` |
| 10 | `#/9` | Poisson’s Ratio | caption | `Magali Billen, UC Davis` |
| 15 | `#/13` | Elastic Tensor | caption | `$\sigma_{ij} = C_{ijkl} \cdot \epsilon_{kl}$` · `A hexagonal prism` |
| 16 | `#/14` | Viscous Deformation | equation | `Wikipedia` · `$\sigma_n=\eta \dot{e}$` · `$\sigma_s=\eta \dot{\gamma}$` |
| 19 | `#/16` | Couette Flow (advanced) | equation | `$u=u0 (1-\frac{y}{h})$` · `$\dot{\epsilon}=\frac{du}{dy}=-\frac{u0}{h}$` · `Magali Billen, UC Davis` · `$\sigma =\eta \dot{\epsilon}=-\frac{\eta u0}{h}$` |
| 20 | `#/17` | Flow Down An Inclined Plane (advanced) | equation | `$u=\frac{\rho g\sin \alpha}{\eta}(h2-y2)$` |
| 21 | `#/18` | Elastic Vs. Viscous Deformation | caption | `Elastic deformation` · `$tM=\frac{\eta}{E}$` |
| 24 | `#/21` | Combined Models (advanced) | caption | `Mechanical analog` · `Strain history curves` |
| 25 | `#/22` | Deformation Controlling Factors | caption | `Granite` |
| 29 | `#/26` | Effects of Foliation and Crystal Fabric | caption | `Olivine` |
| 37 | `#/29/6` | Summary of Deformation Controling Factors | caption | `Roderick Brown, U Glasgow` |

## Screenshots done

Images live in `Lectures/Module-iii-Theory/Lecture2-restored/` and
`Lecture3-restored/`.


| Deck | pptx | What happened |
|---|---|---|
| 3.2 | 12, 15, 23, 24, 29, 32 | figures replaced, strays cleared |
| 3.2 | 13 | split into three slides — Longitudinal / Angular / Volumetric |
| 3.2 | 9, 10 | checked, already clean (one caption reunited with its photo) |
| 3.3 | 11, 12 | pseudo-animation — now a parent slide and a vertical child |
| 3.3 | 28 | two figures restored: Griggs wet/dry quartz, Fossen pore pressure |
