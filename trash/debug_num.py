import re

with open('theory/unit2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the numericals section to show exact question wordings from PDF
old_num = '<!-- Q5 & Numericals: PI/IPR + Gilbert Curves -->'
idx = content.find(old_num)
if idx == -1:
    # try alternate marker
    old_num = '<!-- Q5b & Tubing Performance / Gilbert -->'
    idx = content.find(old_num)

print("Numericals block found at idx:", idx)

# find the end of numerical section
end_markers = ['<!-- Q5: Wellbore', '<!-- Q6:']
for m in end_markers:
    end_idx = content.find(m, idx+10 if idx != -1 else 0)
    if end_idx != -1:
        print(f"End marker '{m}' found at {end_idx}")
        break

# Show what's in that section currently
if idx != -1 and end_idx != -1:
    print("\nCurrent numericals section:")
    print(content[idx:idx+200])
