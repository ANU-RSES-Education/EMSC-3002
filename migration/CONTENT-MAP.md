# EMSC-3002 — Content Map & Overlap Analysis

A cross-module map of what is taught where, built to plan **consolidation of
overlapping material** (primary focus: Modules 1–3) and to decide **where new
material should go**. Slide-level detail for Modules 1–3; topic-level for 4–5.

Legend for role codes: **●** taught in depth (canonical) · **P** previewed /
tasted · **A** applied without deriving · **R** re-taught from scratch · **—** absent.

Format status (target = authored reveal markdown: text + KaTeX math + referenced
images). **Author = format**: the *bolded* name in each deck's credit slide is its
author — Moresi & Beucher wrote native markdown; Jiang wrote in PowerPoint.

| Module | Author (bold credit) | Format | Notes |
|---|---|---|---|
| i | Louis Moresi | ✅ native | text markdown |
| ii | Louis Moresi | ✅ native | text markdown; some full-bleed figure slides |
| iii | Chengxin Jiang | ✅ converted | was PowerPoint; converted, equations recovered |
| iv | Chengxin Jiang | ✅ converted (draft) | 4 pptx (Lectures 4–7) → draft decks, 46 equations recovered; old image decks 4.0–4.4 still present |
| v | Romain Beucher | ✅ native | text markdown; many `data-background` geological photos (not lost text) |

**All modules now text-native.** Module iv converted 2026-07-23 from the 4 source
pptx into `Module-iv-lecture{4,5,6,7}-*-draft.reveal.md` (Brittle deformation /
Joints & faults / Faults & fault zones / Tohoku). The pre-existing image-only
`Module-iv-lecture{0-4}` decks (the 4.0–4.4 split) remain until you reconcile the
draft decks against that structure.

---

## 1. Course structure & teaching order

Delivery order is **i → ii → iii → (mid-term) → iv → v** — descriptive first,
formalise in the middle, apply at the end (a spiral curriculum). The order is
sound; the issue is that **each module was authored standalone**, so shared
theory is *duplicated* rather than *cross-referenced*.

| # | Module | Decks | Role |
|---|--------|-------|------|
| i | Global Tectonics | 3 (`Module-i-GlobalTectonics-{1,2,3}`) | Descriptive tectonics + an early theory taster (deck 3) |
| ii | Structural Geology & Crustal Deformation | 4 (intro, Contractional, Extensional, Strike-Slip) | Descriptive deformation regimes; fault geometry |
| iii | Theory | 3 (Stress, Strain, Rheology) | **The theory home** (just converted, equations recovered) |
| iv | Brittle Deformation | 5 (lecture 0–4) | Fracture, joints/veins, faults, earthquakes — *image-only* |
| v | Ductile Deformation | 5 (fold geometry, mechanisms, associated structures ×2, shear zones) | Folds & shear zones |

---

## 2. Concept × Module overlap matrix

| Concept | i | ii | iii | iv | v |
|---|:--:|:--:|:--:|:--:|:--:|
| Stress tensor / principal stress | ● | A | ● | A | A |
| Mohr circle | — | — | ● | R | — |
| Coulomb–Mohr failure criterion | A¹ | — | ● | R | — |
| Anderson faulting (stress → fault type) | P | A | ● | A | — |
| Fault geometry (normal/reverse/thrust/strike-slip) | A | ● | A | ● | — |
| Strain / strain tensor / strain ellipse | ● | A | ● | — | R |
| Pure vs simple shear; coaxial/non-coaxial | — | A | ● | — | R |
| Kinematic vorticity Wₖ | — | ● | A | — | R |
| Strain rate | ● | — | ● | — | A |
| Rheology (elastic / viscous / plastic) | ● | A | ● | A | R |
| Brittle–ductile transition | ● | A | ● | A | R |
| Focal mechanisms / moment tensor | ● | — | A | A | — |
| Deformation mechanisms (creep, crystal defects) | A | — | A | ● | R |

¹ Module i gives the fault-angle/friction relation algebraically (tan 2θ = ∓1/μ)
but never names the Mohr circle.

---

## 3. Modules 1–3: slide-level concordance (the consolidation core)

**Module i deck 3 ("Stress, Strain & Strength", 30 slides) ≈ a compressed
Module iii.** But they are two *different treatments*:

- **i-deck3** — Louis's modern **tensor / geodynamics** voice. Unique to it:
  tensor invariants framing, velocity-gradient/vorticity (advanced), **Kostrov
  summation** (seismicity ↔ strain-rate), **Byerlee rock-deformation maps**.
- **iii** — the classical **structural-geology (Fossen)** treatment. Unique to
  it: full **Mohr-circle derivation**, worked **trig examples**, **Flinn
  diagram**, **strain-measurement methods** (Fry, Rf/φ…), **Maxwell time**,
  spring–dashpot analogues, stress-measurement methods in depth.

i-deck3 self-flags the overlap: *"covers concepts we will deal with in
considerable detail in Module 3… a brief introduction; we will return to details
once you've completed Module 2."*

| Concept | i deck 3 (tensor/geodynamics) | iii (classical/Fossen) | ii usage |
|---|---|---|---|
| Stress: motivation & definition | "What is Stress?" ×4 (tunnel/collapse) | Deformation & stress; Stress = F/A + units; Body vs surface forces | — |
| Stress tensor | "The Stress Tensor" ×3 (traction, symmetry, dev/volumetric) | Stress state 2D/3D; Stress on a plane via tensor; traction example | — |
| Principal stress | "Principal Stresses" (diagonalisation) | Principal stress & ellipsoid; Deviatoric & mean stress | — |
| Principal stress → tectonic regimes | "Principal Stresses & Tectonics" ×2 (free surface, tan 2θ, friction) | Anderson's faulting; normal/reverse implication; free-surface effects | L3 "Principal stresses & extension" (A) |
| **Mohr circle** | — (tan 2θ only) | **Deriving the Mohr circle; The Mohr circle; Mohr & angle θ; 3D Mohr** | — |
| **Failure criterion** | (implicit via friction) | **Coulomb–Mohr failure; "Will the fault fail?"** | — |
| Global / Australian stress | "Global Stress Revisited"; "Australian Stress Field" (also deck 1) | Global stress map; S. California; How we measure stress | — |
| Strain: definition | "What is Strain?" | Strain (non-rigid); deformation types; homogeneous/heterogeneous | finite vs incremental (L1, A) |
| Strain tensor | "Strain Tensor"; Symmetry; Volumetric strain & incompressibility; **Invariants** | Strain tensor; quantify strain; principal strain/ellipsoid; volume change | — |
| Pure vs simple shear | (within strain) | **Pure shear & simple shear; Flinn diagram** | L2/L3 pure/simple shear (A) |
| Strain rate | "What is Strain-Rate?"; **Advanced: velocity gradient/vorticity**; **Kostrov summation** | Strain rate; strain-rate tensor; strain rates at plate boundaries | — |
| Rheology | "Rheology"; Elasticity ×2; Viscosity ×3; Plasticity | Entire Rheology deck (Young's, Poisson, Hooke 3D, Maxwell, viscosity, yield…) | brittle/ductile qualitative (A) |
| Deformation map / B–D transition | **"Rock Deformation Map" ×2; "Brittle–Ductile Transition" ×2 (Byerlee)** | Rheology of the lithosphere (brittle–plastic transition) | — |

**Module ii's theory touchpoints** (all *applied*, none derived): principal-stress
orientation → fault type (L3); finite vs incremental & pure/simple shear (L1–L3);
**kinematic vorticity Wₖ derived in full** (L4 strike-slip) — this is ii's one
piece of *canonical* theory, later re-taught in v.

---

## 4. Modules 4–5: topic-level map

**Module iv (Brittle) — image-only, ILO-level:**
- lecture 0 — deformation mechanisms (crystal structure, slip systems, defects, creep) → **canonical** home for micro-mechanisms
- lecture 1 — fundamentals of brittle deformation; four fracture modes; **Mohr failure envelope + composite criterion** (re-teaches failure) ; frictional sliding
- lecture 2 — joints & veins (plumose, arrays, origins)
- lecture 3 — faults, fault zones & earthquakes; fault types (re-covers ii geometry); faulting↔stress
- lecture 4 — two earthquakes (Mansfield 2021, Tohoku 2011)

**Module v (Ductile) — native markdown** (Romain Beucher; the image slides are
full-bleed geological photographs, not lost text):
- Deck 1 — fold geometry (morphology, classification, styles, attitude)
- Deck 2 — folding mechanisms (buckling/viscosity contrast, passive, bending, kink/chevron, superposed, sheath)
- Deck 3a — foliations/cleavage (fabric, cleavage, S₁/D₁, bedding–cleavage, cleavage–strain)
- Deck 3b — lineations & boudinage (mullions, lineation–strain, boudinage)
- Deck 4 — shear zones (brittle→ductile, mylonites, ideal plastic/simple/pure/sub-simple shear, **ISA**, **vorticity/Wₖ**, kinematic indicators)

v **re-teaches** all shared theory inline with **no cross-references**: strain
ellipse, pure/simple shear, coaxial/non-coaxial, vorticity, brittle-vs-ductile,
viscosity/competence. Only stress (σ₁) and strain rate are merely *applied*.

---

## 5. Overlap hotspots (ranked)

1. **i-deck3 ↔ iii — two parallel theory passes.** The biggest 1–3 item. Not
   pure duplication: complementary voices. Decision is *how to reconcile*, not
   *which to delete*.
2. **Failure criteria re-taught in iv-lecture1** despite iii owning Mohr–Coulomb
   (iii even says failure criteria "will be introduced in brittle deformation").
3. **Fault classification smeared across i, ii, iii, iv** — Anderson (i P, iii ●,
   ii/iv A) and fault geometry (ii ●, iv ●).
4. **Vorticity/Wₖ taught twice** — ii-L4 (● derived) and v-deck4 (R).
5. **v re-teaches strain/shear/rheology** from scratch with no links to iii.

---

## 6. Proposed consolidation model — *one canonical home + light cross-links*

| Concept cluster | Canonical home | Everyone else |
|---|---|---|
| Stress, strain, strain-rate, rheology, Mohr circle, failure criteria | **iii** | i previews; ii/iv/v recap + link |
| Tensor/geodynamics extras (invariants, vorticity, Kostrov, deformation maps) | **fold into iii** (from i-deck3) | i keeps the conceptual hook |
| Fault geometry (normal/reverse/thrust/strike-slip descriptive) | **ii** | i/iii/iv link |
| Kinematic vorticity Wₖ | **iii** (with the strain-rate tensor) | ii/v apply + link |
| Deformation micro-mechanisms (creep, defects) | **iv-lecture0** | i/iii link |
| Focal mechanisms | **i** (deck 2) | iii applies + links |

### Concrete moves for 1–3 (the focus)
- **Thin i-deck3 to a genuine preview**: keep the motivation ("What is Stress?"
  tunnel story), the tectonic-regime payoff, and the global/Aus stress maps.
  **Move the unique tensor material** (invariants, velocity-gradient/vorticity,
  Kostrov summation, Byerlee deformation maps) **into iii** so nothing is lost —
  iii currently lacks these.
- **iii becomes the single derivation home** for the stress/strain/rheology
  spine; i links forward, ii links back instead of re-deriving.
- **Reconcile the two voices**: decide whether iii adopts the tensor notation
  from i-deck3 or keeps Fossen-classical (a style decision, see §7).

---

## 7. Open decisions & "where does new material go?"

Decisions to make (feed the next planning step):

1. **i-deck3**: thin to preview (recommended) vs keep as full early pass?
2. **Notation/voice**: unify on the tensor/geodynamics treatment, the classical
   Fossen treatment, or a deliberate two-pass (intuitive first, formal in iii)?
3. **iv failure criteria**: recap-and-link to iii, or keep self-contained until
   iv is converted?
4. **v shear/strain**: add back-links to iii, or leave self-contained?

**Guidance for placing NEW material** (use the homes in §6):
- New *theory/derivation* (any stress/strain/rheology/failure) → **iii**.
- New *tectonic-setting or regional* content → **i** (global) or **ii** (regime).
- New *fault-geometry* detail → **ii**.
- New *brittle/fracture* content → **iv**; new *fold/shear* content → **v**.
- New *worked examples / exercises* → the theory home (iii) or the Practical
  Exercises section, cross-linked from the relevant lecture.
- If new material spans two homes, put the derivation in the canonical home and a
  short applied recap (with a link) in the other — never a second derivation.

---

## 8. Provenance

Built 2026-07-22 from a parallel read of all five modules' decks + book pages.
Modules 1–3 verified at slide-title granularity; 4–5 at topic/ILO level (iv is
image-only). Companion to the Module-3 conversion work in `migration/module3/`.
