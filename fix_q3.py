import os

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacement for the list items in Step 2
    old_list = '''<ol>
                    <li>Start at \( P_{wh} = 200 \text{ psi} \) on the top axis (marked as ①).</li>
                    <li>Drop vertically to the \( GLR = 0.2 \text{ mcf/bbl} \) curve (marked as ②).</li>
                    <li>Read the equivalent wellhead depth on the left axis: \( 7,500 \text{ ft} \) (marked as ③).</li>
                    <li>Add the tubing length (\( 4,000 \text{ ft} \)) to find the bottom equivalent depth: <br>
                    <div class="equation-box">\( L_{eq, bottom} = 7,500 \text{ ft} + 4,000 \text{ ft} = \mathbf{11,500 \text{ ft}} \)</div> (marked as ④).
                    </li>
                    <li>Move right from \( 11,500 \text{ ft} \) to intersect the \( 0.2 \) GLR curve (marked as ⑤) and read the Required Bottomhole Pressure: <br>
                    <div class="equation-box">\( P_{wf, required} \approx \mathbf{800 \text{ psi}} \)</div>
                    </li>
                </ol>'''

    new_list = '''<ol>
                    <li>Start at \( P_{wh} = 200 \text{ psi} \) on the top axis (marked as ①).</li>
                    <li>Drop vertically to the \( GLR = 0.2 \text{ mcf/bbl} \) curve (marked as ②).</li>
                    <li>Read the equivalent wellhead depth on the left axis: \( 3,500 \text{ ft} \) (marked as ③).</li>
                    <li>Add the tubing length (\( 4,000 \text{ ft} \)) to find the bottom equivalent depth: <br>
                    <div class="equation-box">\( L_{eq, bottom} = 3,500 \text{ ft} + 4,000 \text{ ft} = \mathbf{7,500 \text{ ft}} \)</div> (marked as ④).
                    </li>
                    <li>Move right from \( 7,500 \text{ ft} \) to intersect the \( 0.2 \) GLR curve (marked as ⑤) and read the Required Bottomhole Pressure: <br>
                    <div class="equation-box">\( P_{wf, required} \approx \mathbf{500 \text{ psi}} \)</div>
                    </li>
                </ol>'''

    # Replacement for Step 3
    old_step3 = '''<p><strong>Step 3: Compare Available vs Required Pressure</strong></p>
                <div class="math-block">
                    <ul>
                        <li>Available Pressure (\( P_{wf, available} \)) = \( 500 \text{ psi} \)</li>
                        <li>Required Pressure (\( P_{wf, required} \)) = \( 800 \text{ psi} \)</li>
                    </ul>
                </div>
                <p><strong>Conclusion:</strong> Since \( 500 \text{ psi} < 800 \text{ psi} \), the reservoir pressure is <strong>not sufficient</strong> to overcome the tubing losses at the desired rate. The well <strong>will not flow</strong> at \( 400 \text{ bbl/day} \).</p>'''

    new_step3 = '''<p><strong>Step 3: Compare Available vs Required Pressure</strong></p>
                <div class="math-block">
                    <ul>
                        <li>Available Pressure (\( P_{wf, available} \)) = \( 500 \text{ psi} \)</li>
                        <li>Required Pressure (\( P_{wf, required} \)) \approx \( 500 \text{ psi} \)</li>
                    </ul>
                </div>
                <p><strong>Conclusion:</strong> Since \( P_{wf, available} \approx P_{wf, required} \), the well is at a <strong>borderline/equilibrium condition</strong>. The reservoir pressure is just barely sufficient to maintain the flow, and the well <strong>can flow</strong> (at equilibrium) at \( 400 \text{ bbl/day} \) under these assumed conditions.</p>'''

    content = content.replace(old_list, new_list)
    content = content.replace(old_step3, new_step3)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

paths = ['numericals/post_midsem_ppt/index.html', 'numericals/post_midsem_self/index.html']
for p in paths:
    update_file(p)
