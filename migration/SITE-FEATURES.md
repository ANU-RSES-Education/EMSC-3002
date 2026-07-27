# JB1 → JB2 site features: port / drop decisions

Tracking the site-level features from the old `_config.yml` and how they carry to the new
MyST site.

| JB1 feature | Decision | Notes |
|---|---|---|
| Font-switcher / font-scaler buttons (`extra_navbar` JS) | **Drop** | Superseded by book-theme's own typography controls. Not carried into `myst.yml`. |
| hypothes.is comments | **Drop (for now)** | Can be re-added later if wanted. |
| Binder / launch buttons | **Port** — reusable `{binder}` directive | See below. |
| Repository button | Kept | `project.github` in `myst.yml`. |
| MathJax / math | Native | dollarmath renders natively in MyST. |

## The `{binder}` directive

A reusable launch-button directive lives in `_plugins/binder-button.mjs` and is registered
under `project.plugins` in `myst.yml`. It gives per-page control over which container a
button launches — the "raw course env" vs an "underworld3-specific" container.

**Raw course environment** (launches this repo via its `binder/` env), optionally opening a file:
```markdown
:::{binder} Launch the course notebooks
:path: Notebooks/Index.md
:::
```

**Underworld3-specific container** (uses the `uw3-binder-launcher` mybinder cache):
```markdown
:::{binder} Launch Underworld3
:preset: uw3
:::
```

**Any repo/branch:**
```markdown
:::{binder}
:repo: myorg/myrepo
:ref: main
:path: intro.ipynb
:::
```

Options: `preset` (`course` default | `uw3`), `repo`, `ref`, `path` (labpath), `binderhub`
(default `https://mybinder.org`). The directive argument is the button label.

A live example is on the **Exercises** page.

> Future: the `uw3` preset points at `underworldcode/uw3-binder-launcher`. If more named
> environments are needed, extend the `PRESETS` map in `_plugins/binder-button.mjs`.
