import re

with open('theory/unit2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<!-- Q5 & Numericals: PI/IPR + Gilbert Curves -->')
end_idx = content.find('<!-- Q5: Wellbore', idx)

if idx != -1 and end_idx != -1:
    new_num_section = '''<!-- Numericals Section -->
<div class="qcard" style="border-color: #8b5cf6; background: rgba(139, 92, 246, 0.05);">
    <div class="qhead"><span class="qbadge" style="background: linear-gradient(135deg, #8b5cf6, #d946ef);">Numericals</span><span class="qtitle">PI / IPR / AOF Numericals (15 Marks each)</span></div>
    
    <div class="qquote">
        <strong>Numerical 1:</strong> "A productivity test was conducted on a well. The test results indicate that the well is capable of producing at a stabilized flow rate of 110 STB/day and a bottom-hole flowing pressure of 900 psi. After shutting the well for 24 hours, the bottom-hole pressure reached a static value of 1300 psi. Calculate: PI, AOF, Flow rate if Pwf is reduced to 600 psi, Pwf required to produce 250 STB/day."<br><br>
        <strong>Numerical 2:</strong> "A well is produced from a saturated oil reservoir with average reservoir pressure of 2500 psig. Stabilized production rate is 500 STB/day and flowing bottom-hole pressure is 1950 psig. Find: Flow rate at Pwf=1950, PI, AOF, Plot IPR."
    </div>
    <div class="answer-section">
        <div class="kp">📂 These numericals have detailed step-wise solutions in the Numericals section. Refer to:
            <br>→ <a href="../../numericals/pre_midsem_ppt/index.html" style="color:#a78bfa">Pre Midsem PPT Numericals</a> (Problem 1 & 2)
            <br>→ <a href="../../numericals/pre_midsem_self/index.html" style="color:#a78bfa">Pre Midsem Self Numericals</a> (Problem 1 & 2)
        </div>
        <div class="bluff" style="border-color: rgba(139, 92, 246, 0.3); background: rgba(139, 92, 246, 0.1);">
            <h5 style="color: #c4b5fd;">✨ Exam Alert</h5>
            <p style="color: #ddd6fe;">The professor explicitly noted: <em>"Values will be changed in the exam"</em>. Do the self questions first as they have detailed stepwise solutions unlike the PPT ones!</p>
        </div>
    </div>
</div>

<div class="qcard" style="border-color: #ec4899; background: rgba(236, 72, 153, 0.05);">
    <div class="qhead"><span class="qbadge" style="background: linear-gradient(135deg, #ec4899, #f43f5e);">Numericals</span><span class="qtitle">Tubing Performance (Gilbert Curves) (15 Marks each)</span></div>
    <div class="qquote">
        <strong>Numerical 3:</strong> "Find the flowing pressure at the foot of 13000 ft of 2-3/8 in. tubing when the well is flowing at a rate of 1000 bbl/day with a GLR of 200 mcf/bbl and a tubing pressure of 300 psi."<br><br>
        <strong>Numerical 4:</strong> "What is the tubing pressure (THP) of well completed with 8000 ft of 2-3/8 in. tubing, flowing 1000 bbl/day with a GLR of 200 mcf/bbl and a bottom-hole flowing pressure (BHP) of 2000 psi?"<br><br>
        <strong>Numerical 5:</strong> "It is hoped to flow a well having a PI of 0.4 bbl/day/psi, and a static pressure of 3000 psi, at a rate of 400 bbl/day with a GLR of 400 mcf/bbl, through 8000 ft of 2-3/8 in. tubing against a tubing pressure of 200 psi. Will the well flow at the desired rate?"
    </div>
    <div class="answer-section">
        <div class="kp">📂 These numericals have detailed step-wise solutions in the Numericals section. Refer to:
            <br>→ <a href="../../numericals/post_midsem_ppt/index.html" style="color:#f472b6">Post Midsem PPT Numericals</a> (Problems 1, 2 & 3)
            <br>→ <a href="../../numericals/post_midsem_self/index.html" style="color:#f472b6">Post Midsem Self Numericals</a>
        </div>
        <div class="twocol">
            <div class="imgbox"><img src="images/gilbert_curves.png" alt="Gilbert Curves"><div class="imgcap">Fig 6: Gilbert's Nomogram/Curves</div></div>
            <div class="imgbox"><img src="images/gilbert_example.png" alt="Gilbert Example"><div class="imgcap">Fig 7: How to read the Gilbert Curves</div></div>
        </div>
        <div class="bluff" style="border-color: rgba(236, 72, 153, 0.3); background: rgba(236, 72, 153, 0.1);">
            <h5 style="color: #fbcfe8;">✨ Exam Alert</h5>
            <p style="color: #fce7f3;">The professor explicitly noted: <em>"Values will be changed in the exam"</em>. Do the self questions first as they have detailed stepwise solutions unlike the PPT ones!</p>
        </div>
    </div>
</div>
'''
    new_content = content[:idx] + new_num_section + content[end_idx:]
    with open('theory/unit2/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Numericals section updated with exact wording!")
else:
    print("Could not find sections to replace.")
