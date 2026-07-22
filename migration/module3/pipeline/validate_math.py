import re, sys, pathlib
files = sys.argv[1:]
span = re.compile(r'\$\$(.+?)\$\$|\$([^$\n]+?)\$', re.S)
total = 0
issues = []
for fp in files:
    txt = pathlib.Path(fp).read_text()
    name = pathlib.Path(fp).name
    for m in span.finditer(txt):
        s = (m.group(1) or m.group(2))
        total += 1
        # brace balance
        depth = 0; ok = True
        for c in s:
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth < 0: ok = False; break
        if not ok or depth != 0:
            issues.append((name, 'brace-imbalance', s[:80]))
        if not s.strip():
            issues.append((name, 'empty', ''))
        if s.count(r'\begin{matrix}') != s.count(r'\end{matrix}'):
            issues.append((name, 'matrix-mismatch', s[:80]))
        if '\\\\' in s:
            issues.append((name, 'double-backslash', s[:80]))
    # markdown-risky escaped punctuation delimiters
    for pat in (r'\\\{', r'\\\}', r'\\\|', r'\\\[', r'\\\]'):
        c = len(re.findall(pat, txt))
        if c:
            issues.append((name, f'risky {pat}', str(c)))
print(f'total math spans: {total}')
print(f'issues: {len(issues)}')
from collections import Counter
for (nm, kind, ex) in issues[:40]:
    print(f'  [{nm}] {kind}: {ex}')
print('summary:', dict(Counter(k for _, k, _ in issues)))
