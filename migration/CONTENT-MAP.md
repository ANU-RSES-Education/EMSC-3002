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

## 0. Course direction (stated 2026-07, Moresi)

**Where the course has come from and where it is going.** The material has
evolved from *structural-geology-heavy* content towards **more tectonics with a
broader structural focus** — e.g. *structures found in the Australian Plate* —
and the trajectory is to add **more Australian examples, geophysical-imaging
content, and applications**. The course is already *titled* "Structure and
Tectonic Evolution of the Australian Plate"; the content needs to catch up with
the title (see §9: outside Module i, Australian examples are nearly absent).

**Pedagogy:** repetition is fine *per se* (spiral curriculum), but every revisit
after the first full treatment must be **shorter** and must **acknowledge where
the concept was originally taught** (module + link). See §6.

**Learning outcomes style:** module openers say **"What you will learn in this
module"** — plain language, not formal ILO boilerplate.

### This year's priorities (2026 delivery, starts 28 July)
1. **More viscous flow** — not just brittle structures. Anchors exist (iii-3
   Couette/inclined-plane/Maxwell; v-2 Biot wavelength); see §11 for the
   specific attach-points and gaps.
2. **Cut the brittle repetition** — the worst duplication in the course is in
   brittle content (Mohr/failure criteria/Anderson across iii-1, iv-4, iv-6;
   see §10).
3. **Australian examples across the board** — every module should carry them,
   not just Module i (see §9 for the per-deck gap list).

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

## 6. Consolidation model — *one full treatment + shorter, linked revisits*

**Design principle (Moresi):** repetition is not bad *per se* — a spiral
curriculum wants concepts revisited. But **every revisit after the first full
treatment must be (a) shorter and (b) explicitly acknowledge where the concept
was originally taught** (module name + link where possible). So we are *not*
deleting overlap; we are demoting revisits to recaps and wiring the links.

Directional by teaching order (**i → ii → iii → iv → v**):
- **Preview → Full**: a concept may be *introduced* briefly before its full
  treatment (i-deck3 previews the theory owned by iii). The preview stays short
  and **forward-links** ("detailed in Module 3"); the full treatment
  **back-links** ("first met in Module 1.3").
- **Full → Application**: once the home module has taught it, later uses are
  **recaps** that **back-link** to the home.

| Concept cluster | Full-treatment home | Revisits (shorten + link) |
|---|---|---|
| Stress, strain, strain-rate, rheology, Mohr circle, failure criteria | **iii** | i-deck3 (preview, fwd-link); ii/iv/v (recap, back-link) |
| Tensor/geodynamics extras (invariants, vorticity, Kostrov, deformation maps) | **fold into iii** (from i-deck3) | i keeps the conceptual hook only |
| Fault geometry (normal/reverse/thrust/strike-slip) | **ii** | i/iii/iv recap + link |
| Kinematic vorticity Wₖ | **ii-L4** (derived there) or **iii** | v recap + back-link |
| Deformation micro-mechanisms (creep, defects) | **iv** (lecture 4) | i/iii link |
| Focal mechanisms | **i** (deck 2) | iii recap + back-link |

### Concrete 1–3 action list (the focus)

| # | Action | Where | Type | Risk |
|---|--------|-------|------|------|
| A1 | Add forward-link "full treatment → Module 3" on the preview slides | i-deck3 (Stress/Strain/Rheology intro slides) | link | low |
| A2 | Add back-link "first introduced in Module 1.3" on the opening slides | iii deck1/2/3 | link | low |
| A3 | Move unique material into iii (tensor invariants, velocity-gradient/vorticity, Kostrov summation, Byerlee deformation maps) | i-deck3 → iii | move | med |
| A4 | Shorten i-deck3's tensor/strain/rheology mechanics to conceptual level once iii owns them | i-deck3 | trim | **needs Louis** |
| A5 | ii-L3 principal-stress→fault-type: add forward-link "stress theory in Module 3" | ii-L3 | link | low |
| A6 | iii Anderson-faulting slide: back/forward-link to ii fault-geometry | iii deck1 | link | low |

A1/A2/A5/A6 (links) are additive and reversible — safe to do now. A3 (move) is
low-risk content relocation. **A4 (trimming Louis's slides) needs his slide-level
judgment** and is deliberately held back.

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

### New-material register (2026)

Material Louis has identified for inclusion, with placement per the rules above:

| # | Material | Source | Placement | Notes |
|---|----------|--------|-----------|-------|
| N1 | **Continental accretion** — research presentation (2025 delivery), follows the subduction story; Australian component | `RSES-Collisions.pptx` -> `Module-i-Accretion-draft.reveal.md` (converted 2026-07-23) | **Module i**, directly after deck 2's subduction/convergent-boundary sequence — natural narrative continuation ("what subduction builds") | Feeds the Australian-assembly thread (N3); candidate new deck (numbering free now that the Australian-structure deck is 1.1a) or extension of deck 2 |
| N2 | **Modelling faults for hydrogen exploration** — research presentation (2025 delivery); Australian component | `Curtin-May2025-PPT.pptx` -> `Module-iv-HydrogenFaults-draft.reveal.md` (converted 2026-07-23, 43 equations) | **Module iv**, as an *applications* lecture after Faults & Fault Zones (iv-6) | Exactly the "applications" direction of §0; ties to pore-pressure/effective-stress (iii-1) and fault-zone architecture (iv-6) with back-links, plus seal/reactivation concepts |
| N3 | **Interpreting Australian structure** — a *capability thread*, not just a deck: (a) where Australia sat in plate reconstructions through geological time; (b) when the pieces came together (craton assembly, Proterozoic orogens, Tasmanides); (c) what the datasets are (Moho depth, sediment thickness, LAB depth, …); (d) the names of things (province/orogen nomenclature) | To be authored | **Home in Module i as deck 1.1a** (renumbered from 1.4, 2026-07-24: introduces the Indo-Australian plate + boundaries, then the structure-interpretation reference) (it already has LAB-thickness maps, Australian stress, and the GPlates link on the book page) as an "Australian lithospheric architecture" deck/page; then *every* module's Australian examples (§9) reference back to it | This is the geophysical-imaging thread of §0 made concrete. Dataset candidates: AusMoho / AuSREM (Moho), AusLAMP (LAB), OZ SEEBASE (sediment thickness), GA seismic lines, WSM-Australia, GPlates/EarthByte reconstructions. Doubles as the shared base layer the §9 gap-filling examples hang off |

Sequencing note: N3 is the connective tissue — N1 (accretion) supplies its
"when did the pieces come together" narrative, and the §9 per-module examples
give students repeated practice *using* it. Suggested build order: N3 skeleton
(nomenclature + datasets) → N1 conversion → N2 conversion.

---

## 9. Australian-examples inventory (gap: everywhere except Module i)

Full sweep of decks, book pages and exercises (2026-07-23). Concrete Australian
geological examples per unit:

| Unit | Count | What's there |
|---|---|---|
| Module i | ~5 | Australian stress map ×2 (i-1); Mount Waverley collapse, WA M5.6 2023 quake (i-3) — the only well-integrated module |
| Module ii | 1 | Australia TMI magnetic-anomaly grid (ii-1); **ii-2/3/4 have zero** |
| Module iii (drafts) | 2 | Olympic Dam borehole stress; Lake George fault (exercise figures) — deck 1 only; **decks 2/3 zero** |
| Module iv (drafts) | 4 | Kangaroo Island joints (iv-5); Canberra Camp Hill normal faults + Lake George Fault Zone (iv-6); Earthquakes-in-Australia + Mansfield 2021 (iv-7, one slide) |
| Module v | 1 | Ruby Gap quartzite mylonite (v-4); **v-1/2/3 zero** |
| Exercises | 1 strong | Lake George stress/Mohr exercise (built around RSES/GA 2020 drilling) |

**Gaps to fill** (decks with zero): ii-Contractional, ii-Extensional,
ii-Strike-Slip, iii-Strain, iii-Rheology, v-Folds (1/2/3). Natural candidates to
consider: Flinders/Adelaide fold belt (v folds — perfect fit), Mt Isa / Broken
Hill shear zones (v-4), Petermann/Alice Springs orogens (ii contraction),
Otway/Gippsland rift margins (ii extension), seismic reflection lines across
Australian basins (the geophysical-imaging thread, §0).

Note: the Mansfield 2021 case study is *named* in iv-7 and the book page but has
no developed body — an easy win to expand with GA material.

---

## 10. Brittle repetition — slide-level (the worst duplication in the course)

Ranked by number of independent FULL treatments (2026-07-23 sweep of ii-2/3/4,
iii-1, iv-4/5/6/7 drafts):

1. **Coulomb–Mohr / failure criteria — WORST.** Full in iii-1 (criterion +
   "Will the Fault Fail?" worked example) AND iv-4 (near-verbatim criterion
   slide + Mohr envelope + Griffith + composite envelope). Also re-summarised
   3× within iii-1 itself.
2. **Mohr circle.** Fully derived in iii-1 (4 slides) and **re-derived** in
   iv-4 ("Revisiting the Mohr Circle" ×2 — same σₙ=σcos²θ derivation).
3. **Anderson / fault classification.** FULL ×3+: iii-1, iv-4 (verbatim
   "Implication to Normal/reverse Faulting"), iv-6 (twice!). Fault-type
   definitions also full in ii-2, ii-4, iv-6.
4. **Earthquake phenomenology.** iv-6 ↔ iv-7 duplicate whole slides
   ("Different Types of Eq Magnitude"; Omori/Gutenberg-Richter/Båth aftershock
   laws appear verbatim in both).
5. **Pore pressure / effective stress.** Full in iii-1 (×2 + hydraulic
   fracturing) and iv-4 (repeats the effective-stress text), third take in
   iv-5 (beer-can experiment).
6. Within-deck duplicate: iv-6 has "Fault Vs. Fault Zone" twice (slides 16 & 59).

Near-verbatim slide pairs to resolve first: Coulomb–Mohr criterion (iii-1↔iv-4),
"Implication to Normal/reverse Faulting" (iii-1↔iv-4), Eq-magnitude and
aftershock-laws slides (iv-6↔iv-7).

**Treatment under the §6 model:** iii-1 keeps the full Mohr/failure/Anderson
treatment (pre-midterm theory home). iv-4's re-derivations become *short recaps
with back-links* — but iv-4 legitimately *extends* the theory (Griffith,
composite envelope, friction/Byerlee): keep those as the module's new content.
iv-6's Anderson slides → recap + link. iv-6/iv-7 shared earthquake slides →
keep in one deck, link from the other. Low-priority: ii's fault-geometry
treatments are regime-specific and mostly non-redundant.

---

## 11. Viscous flow — inventory & growth plan (this-year priority #1)

**Existing anchors** (all quantitative): iii-3 Viscous Deformation (σ=ηε̇,
Newtonian vs power-law) · Couette flow · inclined-plane gravity flow · Maxwell
time (t_M=η/E, mantle ~1000 yr) · viscosity table (ice → mantle) · i-3 power-law
η=K·II_D^(n−1) + plasticity-as-viscosity · v-2 **Biot dominant wavelength**
λ=2πH·∛(μ₁/6μ₂) (the only flow-instability equation in the course) · v-4
shear-zone kinematics (ISA, velocity profiles) · iii-2 strain-rate tensor.

**Missing for a coherent viscous thread:** Stokes/buoyancy-driven flow;
Rayleigh–Taylor / diapir growth; post-glacial rebound → mantle-viscosity
estimation; channel (Poiseuille) / lower-crustal flow; folding growth-*rate*
theory (Biot slide gives wavelength only); boudinage as the dual extensional
instability; creep-law microphysics (ε̇=Aσⁿexp(−Q/RT), grain size); glacier /
lava / salt as worked analogues; corner flow; shear heating; **any notebook /
computational flow exercise** (the computational track
`Theory_Computational_Exercises.md` is commented out of the toc).

**Attach-points (grow from existing slides, minimal restructuring):**
| Anchor (existing) | Add |
|---|---|
| iii-3 Couette flow | Channel/Poiseuille companion → lower-crustal channel flow |
| iii-3 Inclined plane | Name it as the glacier/lava/salt equation + photos (it already *is* the glacier equation) |
| iii-3 viscosity table (mantle 10¹⁸–10²⁴) | Post-glacial rebound: relaxation time → η estimate (closes the loop on the quoted numbers) |
| iii-3 power-law / i-3 power-law | Creep-law microphysics (Arrhenius, n, diffusion vs dislocation) |
| iii-3 Maxwell time | Stokes / Rayleigh–Taylor timescale of diapiric rise |
| v-2 Biot wavelength | Growth-rate curve (amplification vs λ) + boudinage dual instability |
| v-4 creep-mechanisms slide (names only) | The flow-law equations it currently only names |
| Notebooks/Exercises (empty of flow) | First computational flow exercise (inclined-plane or Biot λ vs μ-contrast); re-enable the computational-exercises page; promote the syrup/oil diapir project idea to a practical |

Australian tie-ins for the new flow content (§9 synergy): salt structures
(Amadeus/Canning basins), lower-crustal flow in Proterozoic orogens,
post-glacial signals, Flinders folding for the Biot instability.

---

## 12. Provenance

Built 2026-07-22 from a parallel read of all five modules' decks + book pages;
§§9–11 added 2026-07-23 from three targeted inventory sweeps (Australian
examples, brittle repetition, viscous flow). Modules 1–3 verified at slide-title
granularity; iv at draft-deck level. Companion to the conversion pipeline in
`migration/module3/`.
