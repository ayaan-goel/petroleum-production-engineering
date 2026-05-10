import re

files = [
    'theory/unit2/index.html',
    'theory/unit4/index.html',
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Remove all replacement characters and broken sequences
    content = content.replace('\ufffd', '')
    
    # Fix broken dash sequences like â€" 
    content = re.sub(r'[â][€][""–—]', '-', content)
    content = re.sub(r'[â][€][˜™]', "'", content)
    
    # Remove broken emoji fragments (sequences of garbled chars before HTML tags or words)
    # Pattern: garbled prefix like dY"c, dYOS, etc.
    content = re.sub(r'd[YX]["\'\x60\xc2-\xff][^\s<]*\s*', '', content)
    content = re.sub(r'[^\x00-\x7F\u00A0-\u024F\u2000-\u206F\u20A0-\u20CF\u2100-\u214F\u2190-\u21FF\u2200-\u22FF]+', '', content)
    content = re.sub(r'\?\"\s*', '- ', content)
    content = re.sub(r'\?\'', '-', content)
    content = re.sub(r'\?O\s*', '', content)
    content = re.sub(r'\?[a-z.]\s*', '', content)
    
    # Clean up multiple spaces
    content = re.sub(r'  +', ' ', content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed: {fpath}')
