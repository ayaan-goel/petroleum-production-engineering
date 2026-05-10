import re

# Read all files and check/fix encoding
files = {
    'theory/unit1/index.html': None,
    'theory/unit2/index.html': None,
    'theory/unit3/index.html': None,
    'theory/unit4/index.html': None,
}

broken_pattern = re.compile(r'[dD][YX]["\'\x60\xc2-\xff][^\s<]*|[\ufffd]+|\?["\'\x60O][^\s<]*')

for path in files:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    broken = broken_pattern.findall(content)
    files[path] = broken
    print(f"\n{path}: {len(broken)} broken sequences")
    for b in broken[:5]:
        print(f"  -> {repr(b)}")
