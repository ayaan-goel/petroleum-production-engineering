import re, sys

files = [
    'theory/unit1/index.html',
    'theory/unit2/index.html',
    'theory/unit3/index.html',
    'theory/unit4/index.html',
]

for path in files:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Find broken sequences - chars that are not standard ASCII, latin extended, or known emoji/unicode blocks
    bad = re.findall(r'[^\x09\x0a\x0d\x20-\x7e\u00a0-\u024f\u2000-\u27ff\u2e00-\u2e7f\ufe00-\ufe0f\U0001F000-\U0001FAFF]', content)
    unique_bad = set(bad)
    
    result = f"{path}: {len(bad)} suspect chars"
    if unique_bad:
        safe = [repr(c) for c in list(unique_bad)[:8]]
        result += f" {safe}"
    else:
        result += " CLEAN"
    
    sys.stdout.buffer.write((result + "\n").encode('utf-8'))
