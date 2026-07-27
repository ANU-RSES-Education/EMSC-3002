import katex from './node_modules/katex/dist/katex.mjs';
import fs from 'fs';

const files = process.argv.slice(2);
const spanRe = /\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g;
let total = 0, fails = [];
for (const fp of files) {
  const txt = fs.readFileSync(fp, 'utf8');
  const name = fp.split('/').pop();
  let m;
  while ((m = spanRe.exec(txt)) !== null) {
    const disp = m[1] !== undefined;
    const s = (m[1] ?? m[2]);
    total++;
    try {
      katex.renderToString(s, { displayMode: disp, throwOnError: true, strict: false });
    } catch (e) {
      fails.push({ name, s: s.slice(0, 90), err: e.message.split('\n')[0].slice(0, 90) });
    }
  }
}
console.log(`checked ${total} spans; ${fails.length} failed KaTeX parse`);
for (const f of fails.slice(0, 50)) console.log(`  [${f.name}] ${f.err}\n     :: ${f.s}`);
