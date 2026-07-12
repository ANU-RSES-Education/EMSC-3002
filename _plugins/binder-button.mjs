// Reusable {binder} directive — renders a "Launch on Binder" button.
//
// Usage (raw course environment, opens a notebook):
//   :::{binder}
//   :path: Notebooks/Example1.ipynb
//   :::
//
// Underworld3-specific container (uses the uw3-binder-launcher cache):
//   :::{binder} Launch Underworld3
//   :preset: uw3
//   :::
//
// Any other repo/branch:
//   :::{binder}
//   :repo: myorg/myrepo
//   :ref: main
//   :path: intro.ipynb
//   :::

const PRESETS = {
  course: { repo: 'ANU-RSES-Education/EMSC-3002', ref: 'master' },
  uw3: { repo: 'underworldcode/uw3-binder-launcher', ref: 'main' },
};

const binderDirective = {
  name: 'binder',
  doc: 'Render a Launch-on-Binder button for a notebook or environment.',
  arg: { type: String, doc: 'Button label (default "Launch on Binder")' },
  options: {
    preset: { type: String, doc: 'Named environment: "course" (default) or "uw3"' },
    repo: { type: String, doc: 'GitHub org/repo for the Binder image (overrides preset)' },
    ref: { type: String, doc: 'Git branch/ref (overrides preset)' },
    path: { type: String, doc: 'File to open in JupyterLab (labpath)' },
    binderhub: { type: String, doc: 'BinderHub base URL (default https://mybinder.org)' },
  },
  run(data) {
    const o = data.options || {};
    const preset = PRESETS[o.preset || 'course'] || PRESETS.course;
    const repo = o.repo || preset.repo;
    const ref = o.ref || preset.ref;
    const hub = (o.binderhub || 'https://mybinder.org').replace(/\/+$/, '');
    const label = data.arg || 'Launch on Binder';
    let url = `${hub}/v2/gh/${repo}/${ref}`;
    if (o.path) url += `?labpath=${encodeURIComponent(o.path)}`;
    const style = [
      'display:inline-block',
      'padding:0.4em 0.9em',
      'margin:0.3em 0',
      'background:#C58812', // ANU honey
      'color:#fff',
      'border-radius:6px',
      'text-decoration:none',
      'font-weight:600',
    ].join(';');
    const html =
      `<a class="binder-launch-button" style="${style}" ` +
      `href="${url}" target="_blank" rel="noopener">\u{1F680} ${label}</a>`;
    return [{ type: 'html', value: html }];
  },
};

const plugin = { name: 'Binder launch button', directives: [binderDirective] };
export default plugin;
