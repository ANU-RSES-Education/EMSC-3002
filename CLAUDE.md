# EMSC-3002 — repo notes

Course site for *Structure and Tectonic Evolution of the Australian Plate* (ANU).
Jupyter Book 2 (MyST) book + MkSlides reveal.js decks, built together by
`pixi run build`.

**Before doing anything here, read `.claude/skills/emsc3002-site/SKILL.md`** — it
has the build/deploy commands, the maintenance tools, and a list of silent-failure
traps (MyST rewriting relative links, front-matter placement, image staging) that
are easy to hit and hard to notice.

Key points:

- **`master` is the live branch.** Pushing rebuilds and publishes the public site.
- **The converted Module 3 and 4 decks are hand-authored content now**, not build
  artefacts. They carry `DO NOT REGENERATE` markers. Do not re-run the pptx
  converter over them without the 3-way-merge protocol.
- `pixi run build` must pass before committing.
- Course direction, module inventories and the overlap analysis:
  `migration/CONTENT-MAP.md`.
- Build/deploy detail: `BUILD.md`. Maintenance scripts: `tools/README.md`.
