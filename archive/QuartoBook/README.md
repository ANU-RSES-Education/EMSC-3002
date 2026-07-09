# EMSC 3002 Quarto Book - Revision Notes

This directory contains Quarto-based revision materials for EMSC 3002.

## Contents

### Chapter Files
- `index.qmd` - Front page/welcome
- `01-introduction.qmd` - How to use these revision notes
- `02-module1-global-tectonics.qmd` - Module I: Global Tectonics
- `03-module2-structural-geology.qmd` - Module II: Structural Geology
- `04-module3-theory.qmd` - Module III: Theoretical Underpinnings
- `05-module4-brittle.qmd` - Module IV: Brittle Deformation
- `06-module5-ductile.qmd` - Module V: Ductile Deformation
- `07-cross-cutting-themes.qmd` - Cross-Cutting Themes
- `08-practical-resources.qmd` - Practical Resources
- `09-exam-preparation.qmd` - Exam Preparation

### Configuration
- `_quarto.yml` - Quarto configuration
- `custom.scss` - Custom styling
- `references.bib` - Bibliography

## Building the Book

### Prerequisites

You need Quarto installed. Download from: https://quarto.org/docs/get-started/

### Build Commands

To preview the book locally:
```bash
cd QuartoBook
quarto preview
```

To render the book:
```bash
cd QuartoBook
quarto render
```

The rendered HTML will be in the `_book/` directory.

### Automated Deployment

The revision notes are automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the `master` branch.

**Workflow:** `.github/workflows/deploy_quarto_revision.yml`

**Published URL:** https://anu-rses-education.github.io/EMSC-3002/revision/

The deployment:
- Triggers on pushes to `master` that modify files in `QuartoBook/`
- Can also be manually triggered via workflow_dispatch
- Publishes to the `/revision` subdirectory to coexist with the main Jupyterbook
- Uses `keep_files: true` to preserve other content in gh-pages

### Manual Publishing

You can also publish manually using:
```bash
quarto publish gh-pages
```

Note: Manual publishing will deploy to the root, not the `/revision` subdirectory.

## Structure

The revision notes are organized into:

1. **Module I: Global Tectonics** - Plate boundaries, motions, and large-scale deformation
2. **Module II: Structural Geology** - Contractional, extensional, and strike-slip regimes
3. **Module III: Theory** - Stress, strain, and rheology fundamentals
4. **Module IV: Brittle Deformation** - Fractures, faults, and earthquakes
5. **Module V: Ductile Deformation** - Folds, shear zones, and flow
6. **Cross-Cutting Themes** - Integrative concepts across modules
7. **Important Locations** - Case studies and real-world examples
8. **Terminology Checklist** - Essential definitions
9. **Quantitative Skills** - Calculations and graphical methods
10. **Integration Questions** - Synthesis scenarios
11. **Common Mistakes** - Pitfalls to avoid
12. **Exam Strategies** - How to prepare effectively

## Features

- Self-test questions to check understanding
- Cross-references between related topics
- Callout boxes for tips, warnings, and notes
- Checklists for exam preparation
- Integration scenarios requiring synthesis across modules
- Real-world examples and case studies

## Future Expansion

This Quarto book can be expanded to include:
- Full lecture notes converted from Jupyterbook
- Interactive exercises
- Additional practice problems
- Videos and animations
- Field trip guides

## Notes

This is a supplement to the main course materials in the Jupyterbook. For the complete course content, see: https://anu-rses-education.github.io/EMSC-3002/
