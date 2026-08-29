# Label-soup worklist — Module 3

**3.2 and 3.3 are done** (2026-08-29): every shredded figure replaced, every
stray label cleared, both decks report zero. What follows is 3.1, which the
improved detector can now see into.

Regenerate with:

```
pixi run python tools/label-soup.py --table Lectures/*.reveal.md
```

**The number that matters is the PowerPoint slide.** The `#/n` code is where
the fix goes back in the reveal deck; the two do not match.


## 3.1 Stress — screenshot these (11)

`Lecture1_Stress.pptx`

| pptx slide | goes to | Slide title | Labels that came loose |
|---:|---|---|---|
| **13** | `#/12` | Stress on a Plane via Stress Tensor | `The stress components acting on the faces of a small cube` |
| **16** | `#/13/1` | Example: Computing Traction Vector | `The formula to find the traction vector is $\vec{T}_i=\sigma \cdot \vec{n}$` · `Perform matrix multiplication:` |
| **14** | `#/13/3` | Aside — Review of matrix multiplication. | `or` |
| **19** | `#/16` | Scalar, Vector & Tensor | `Right Temperature field is a scalar (above); Temperature _gradient_ field is` · `a vector (below)` |
| **27** | `#/21` | Deriving the Mohr Circle | `Two formulae:` · `$\sigma_n =  \sigma (\cos 2\theta + 1)/2 \\;\\;$` · `and` · `$\\; \\; \sigma_s = \frac{\sigma \sin 2\theta}{2}$` · `$\cos 2\theta = 2(\sigma_n - \sigma/2)/\sigma \\;\\;$` · `and` · +2 |
| **31** | `#/25` | The Coulomb-mohr Failure Criterion | `$\sigma_{s}=C+\sigma_{n}\tan \phi =C+$ $\sigma_{n}\mu$` |
| **33** | `#/26/1` | Example: Will the Fault Fail? | `Example:` |
| **34** | `#/27` | Anderson’s Theory of Faulting (1905) | `Assumptions:` |
| **39** | `#/33` | Summary | `We derived the Mohr circle for a uniaxial compression case and` · `general form of Mohr circle for biaxial compression / triaxial` · `The Coulomb-Mohr failure criterion:` · `Concepts of lithostatic stress/pressure and hydrostatic stress,` |
| **40** | `#/34` | How We Measure Stress | `A 3D image of the borehole and cross-section` |
| **42** | `#/36` | How We Measure Stress | `Hydraulic fracturing:` |

## 3.1 — text fixes (1)

| pptx slide | goes to | Slide title | Kind |
|---:|---|---|---|
| 25 | `#/19` | Deriving (Some) Stress Relationships | equation |

## Done

| Deck | pptx | What happened |
|---|---|---|
| 3.2 | 12, 15, 23, 24, 29, 32 | figures replaced, strays cleared |
| 3.2 | 13 | split into three — Longitudinal / Angular / Volumetric |
| 3.2 | 22 | compaction figure restored |
| 3.2 | 9, 10 | checked clean; one caption reunited with its photo |
| 3.3 | 7, 13, 14, 15, 16, 21, 24, 25, 26, 29 | figures replaced, strays cleared |
| 3.3 | 11, 12 | pseudo-animation — parent slide plus a vertical child |
| 3.3 | 28 | Griggs wet/dry quartz and Fossen pore pressure restored |
| 3.3 | 23 | checked — extracted figure was already complete, no action |
