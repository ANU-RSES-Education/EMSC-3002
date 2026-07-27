# Module 3 → reveal: standard slide templates

A small, fixed set of slide templates, derived from the existing authored decks
(`Lectures/Module-ii-Lecture-2-Contractional_Regimes.reveal.md`). Each converted Module 3
slide is assigned **one** template. The extractor auto-guesses a template from the
PowerPoint layout (image count + text + image positions); you override with
"slide N should be **Tx**".

Every converted slide is stamped with its origin, e.g.:
`<!-- source: Lecture1_Stress.pptx slide 5 · template: T3 -->`

Slide canvas is 16:9 (matches the pptx). Images keep the ANU theme; sizing/positioning is
the main hand-tuning step and is seeded from the PowerPoint coordinates.

---

## T0 — Section / title divider
Heading only (optionally a subtitle + one bold lead line). Use for topic breaks.
```markdown
## Stress in the Earth
### A brief introduction
```

## T1 — Prose (no image)
Title + a bold lead sentence + short paragraphs. Definitions, framing.
```markdown
## Deformation and stress

**Structural geology is concerned with permanent deformation** that produces structures
such as folds and faults in rocks.

If a rock fails by fracturing and loses cohesion it is *brittle*; if it deforms without
losing cohesion it is *ductile*.
```

## T2 — Bullets (one column)
Title + bold lead + bullet list. Learning outcomes, lists of factors.
```markdown
## Why the stress state matters

**Knowing the stress state helps us:**

- Assess earthquake hazard
- Design tunnels and slopes
- Predict where and how rock will fail
```

## T3 — Text + image (two column)   ← most common
Text/bullets on one side, a single figure on the other. Side & width come from the
PowerPoint position (image at x>50% → float right; else left).
```markdown
## Importance of knowing the stress state

<div>
<div style="width:52%; float:left">

- Geotechnical engineering (tunnels, highways)
- Earthquake hazard

</div>
<div style="width:44%; float:right; margin-left:40px;">

![](Figures-Theory1/slide006_img2.jpg) <!-- .element width="100%" -->
*Image: M. S. Paterson*

</div>
</div>
```

## T4 — Full-bleed figure (image only)
A figure that fills the slide, no prose. (This is what *every* current Module 3 slide is.)
```markdown
<!-- .slide: data-background="Figures-Theory1/slide012_img1.png" -->
```

## T5 — Figure focus (title + large centred figure)
Title (+ optional subtitle) over one large centred image and an optional caption.
```markdown
## The Mohr circle
![](Figures-Theory1/slide020_img1.png) <!-- .element width="80%" -->

*After Fossen (2010)*
```

## T6 — Two-image comparison
Title + two figures side by side (≈50% each), optional caption. Before/after, folds/faults.
```markdown
## Faults and folds

![](Figures-Theory1/slide004_img2.png) <!-- .element style="float:left" width="49%" -->
![](Figures-Theory1/slide004_img1.jpg) <!-- .element style="float:right" width="49%" -->
```

---

## Speaker notes
The pptx speaker notes (53 slides have them) are carried in as reveal presenter notes —
shown in the speaker view, hidden from students:
```markdown
Note:
The stress tensor has nine components but is symmetric, so only six are independent...
```

## Conventions
- Figures live in `Lectures/Module-iii-Theory/Figures-Theory{1,2,3}/` (extracted per lecture).
- Slide separators `<--o-->` (horizontal) and `<--v-->` (vertical, for sub-topics).
- Emphasis: **bold** for key terms, *italic* for captions/attributions.
