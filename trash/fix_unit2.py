import re

# Read current unit2 file
with open('theory/unit2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where Q6-Q10 block starts (the combined wax removal card) and replace with separated versions
old_q6_10_start = '<!-- Q6-Q10: Wax Removal Methods -->'

q6_to_10_replacement = '''<!-- Q6: All Wax Removal Methods -->
<div class="qcard">
    <div class="qhead"><span class="qbadge">Q6</span><span class="qtitle">Wax Removal Methods for Paraffin & Asphaltene</span><span class="mbadge">15 Marks</span></div>
    <div class="qquote">"Illustrate all the Wax Removal Methods available for paraffin and asphaltene removal oil and gas industry."</div>
    <div class="answer-section">
        <h4>Scale Deposition (Background)</h4>
        <p>Scale forms due to crystallization/precipitation of minerals from water (pressure drop, temperature change, or mixing incompatible waters). Removed mechanically (string shot, drilling, reaming) or chemically:</p>
        <ul>
            <li><strong>Water-soluble scale (NaCl)</strong> - dissolve with fresh water</li>
            <li><strong>Acid-soluble scale (CaCO3)</strong> - HCl or Acetic Acid</li>
            <li><strong>Acid-insoluble (BaSO4, SrSO4)</strong> - mechanical methods only</li>
        </ul>
        <h4>Four Wax Removal Methods</h4>
        <p><strong>1. Mechanical (Scraping)</strong> - Scraper attached to wireline scrapes inner tubing walls; done in winter; automatic timing devices used in gas lift wells</p>
        <p><strong>2. Thermal (Hot Oiling/Steaming)</strong> - Hot oil or water injected to melt/soften paraffin; reverse circulation method used (steam through casing-tubing annulus, recovered through tubing)</p>
        <p><strong>3. Solvent</strong> - Solvents like kerosene, xylene dissolve paraffin. CS2 = universal solvent but extremely flammable and toxic. CCl4 effective but not used in USA (damages refinery catalysts)</p>
        <p><strong>4. Dispersant</strong> - Water-soluble dispersants (e.g., Halliburton's Parasperse) disperse paraffin particles (does NOT dissolve). Effective at 120 deg F. 90-98% water so non-flammable and cheap.</p>
        <div class="bluff"><h5>Bluff Tip</h5><p>Present as a table: Method | Mechanism | Suitable For | Limitations. Conclude: "Choice depends on wax characteristics, well conditions, and economics."</p></div>
    </div>
</div>

<!-- Q7: Mechanical Scrapping Case Study -->
<div class="qcard">
    <div class="qhead"><span class="qbadge">Q7</span><span class="qtitle">Mechanical Scrapping - Cambay Basin Case Study</span><span class="mbadge">15 Marks</span></div>
    <div class="qquote">"Discuss the operational steps for mechanical scrapping through a case study of Cambay Basin."</div>
    <div class="answer-section">
        <h4>Case Study Setup</h4>
        <ul>
            <li>A Dummy-mounted Butterfly Scraping tool connected above crown valve</li>
            <li>Lowered to depth of 800m via slick line; dummy attached below for automatic downward pull</li>
            <li>Depth measured using odometer on the line</li>
            <li>During upward movement, scraping tool removes paraffin from inner tubing walls</li>
            <li>Operations done in winter (paraffin deposits more in cold weather)</li>
        </ul>
        <h4>Operational Steps</h4>
        <ol>
            <li>Fit lubricator on top of crown valve of Xmas tree</li>
            <li>Remove lubricator cap; lower scraper assembly inside lubricator while crown valve is closed</li>
            <li>Fit stuffing box firmly on lubricator; open crown valve; lower assembly slowly</li>
            <li>If obstruction felt, move up/down for soft hammering effect; if still stuck, use smaller scraper</li>
            <li>Wire must always be in tension while lowering to avoid twisting</li>
            <li>After reaching desired depth, pull out slowly using power of scrapping winch</li>
            <li>Monitor tentiometer, weight indicators, and depth meter continuously</li>
            <li>After reaching top inside lubricator, close crown valve; release trapped pressure via cock valve</li>
            <li>Unscrew cap after pressure release; remove scraper</li>
            <li>Lubricator length must always be more than scraper assembly length</li>
        </ol>
        <h4>Safety Rules</h4>
        <ul>
            <li>Well must be in flowing condition during scrapping; increase bean size for severe deposition</li>
            <li>Assembly must be made by experienced operator only</li>
            <li>Bean/choke must be checked before and after (paraffin cuttings may plug bean)</li>
            <li>Scrapping NOT to be done on non-flowing wells or during night</li>
        </ul>
        <div class="bluff"><h5>Bluff Tip</h5><p>Mention: "This method is the most commonly used in India (Cambay Basin, OIL fields) due to its low cost and effectiveness for medium-severity deposits."</p></div>
    </div>
</div>

<!-- Q8: Thermal Treatment WITH packer -->
<div class="qcard">
    <div class="qhead"><span class="qbadge">Q8</span><span class="qtitle">Thermal Treatment WITH Packer (CTU Method)</span><span class="mbadge">15 Marks</span></div>
    <div class="qquote">"Discuss with diagram the operational steps for thermal treatment (with packer) for paraffin and asphaltene removal."</div>
    <div class="answer-section">
        <h4>Method: Coiled Tubing Unit (CTU)</h4>
        <p>When the annulus is isolated with a packer, direct steaming through the annulus is NOT possible. The <strong>Coiled Tubing Unit (CTU)</strong> is used with hot oil or hot water.</p>
        <h4>Operational Steps</h4>
        <ol>
            <li>Install and test Tubing BOP (Blow-Out Preventer) prior to starting the job</li>
            <li>Hot oil or hot water is pumped through coiled tubing (CT)</li>
            <li>Fluid is recovered through the annulus between CT and production tubing</li>
            <li>Oil temperature maintained at 60 to 70 deg C</li>
            <li>Lower CTU and circulate hot oil simultaneously</li>
            <li>Circulate at maximum possible rate; lower CTU slowly to avoid stuck pipe</li>
            <li>Maintain circulation for at least 2 hours after reaching desired depth (normally 100m below paraffin deposition zone)</li>
            <li>Exercise extreme care while handling hot oil; keep fire-fighting equipment on standby</li>
        </ol>
        <div class="bluff"><h5>Bluff Tip</h5><p>Key differentiator from Q9: "When a packer is present, annulus is sealed - hence CTU is the ONLY viable thermal method. The hot fluid travels down the CT and returns through the CT-tubing annulus, melting paraffin deposits along the way."</p></div>
    </div>
</div>

<!-- Q9: Thermal Treatment WITHOUT packer -->
<div class="qcard">
    <div class="qhead"><span class="qbadge">Q9</span><span class="qtitle">Thermal Treatment WITHOUT Packer (Annulus Steam/Hot Oil)</span><span class="mbadge">15 Marks</span></div>
    <div class="qquote">"Discuss with diagram the operational steps for thermal treatment (without packer) for paraffin and asphaltene removal."</div>
    <div class="answer-section">
        <h4>Method: Steam/Hot Oil via Annulus</h4>
        <p>Applicable ONLY for wells where annulus is NOT packed off. Steam applied through casing-tubing annulus; heats outer surface of tubing; heat conducted inward to soften paraffin.</p>
        <h4>Case Study (Reverse Circulation with Steam)</h4>
        <ul>
            <li>Steam injected through casing-tubing annulus at high pressure (~40 kgf/cm2) for 1 hour</li>
            <li>After 1 hour, crude oil (at 10-12 kgf/cm2) mixed with steam and pumped through annulus</li>
            <li>During reverse circulation, paraffin melts and comes out through tubing along with well production</li>
        </ul>
        <h4>Operational Steps (Pipeline Steaming)</h4>
        <ol>
            <li>Record ABP (After Bean Pressure) of well before starting</li>
            <li>Keep mobile steam unit at safe distance; lay steam line with NRV (Non-Return Valve)</li>
            <li>Test steam line at pressure higher than tested pressure of flowline</li>
            <li>Do NOT close the well while steaming flowline</li>
            <li>For longer flowlines, inject steam at more than one point</li>
            <li>Always follow steaming with oil flushing to remove molten paraffin</li>
            <li>For multiple points: start from installation side, move toward well side in stages</li>
            <li>Do NOT steam lines with severe deposition (risk of line rupture)</li>
        </ol>
        <h4>Key Precautions (No-Packer Wells)</h4>
        <ul>
            <li>Record annulus pressure; if higher than boiler working pressure, bleed off annulus gas first</li>
            <li>NRV on steaming line set at higher pressure than max working pressure of boiler</li>
            <li>Open annulus valve ONLY when steam line pressure exceeds annulus pressure</li>
            <li>Steam continuously without interruption; follow with oil circulation and scrapping if needed</li>
        </ul>
        <div class="bluff"><h5>Bluff Tip</h5><p>Key differentiator from Q8: "Without packer, annulus is accessible. Steam heats tubing from OUTSIDE (conduction). With packer (CTU), hot fluid circulates INSIDE CT string directly to paraffin zone."</p></div>
    </div>
</div>

<!-- Q10: Dispersant Treatment -->
<div class="qcard">
    <div class="qhead"><span class="qbadge">Q10</span><span class="qtitle">Dispersant Treatment for Pour Point Depression (Well to GGS)</span><span class="mbadge">15 Marks</span></div>
    <div class="qquote">"Discuss with diagram the operational steps for dispersant treatment for lowering pour point while transporting crude oil from Well to GGS."</div>
    <div class="answer-section">
        <h4>What is Pour Point Depressant (PPD)?</h4>
        <p>A chemical additive that lowers the pour point of crude oil, preventing it from solidifying/crystallizing during pipeline transportation in cold conditions. Does NOT remove wax - it prevents wax crystal formation by modifying crystal structure.</p>
        <h4>Case Study: Operational Steps</h4>
        <ol>
            <li>PPD first heated in a heater to prevent it from crystallizing itself (cold weather precaution)</li>
            <li>Sent to PPD tank where solvent (diesel) added in 1:1 ratio</li>
            <li>Solution continuously agitated in tank</li>
            <li>The PPD-diesel solution is then compressed/pressurized</li>
            <li>Crude oil from well is first sent to heater treater for basic separation</li>
            <li>Pneumatic pump injects the compressed PPD solution at rate of 7 L/hour into crude oil coming out from bath heater</li>
            <li>PPD solution depresses pour point of crude, preventing crystallization</li>
            <li>Treated crude stored in storage tank (capacity: 170 m3)</li>
            <li>Crude then transmitted via pipeline to Group Gathering Station (GGS) 22 km away</li>
        </ol>
        <div class="bluff"><h5>Bluff Tip</h5><p>Mention: "PPD is especially critical for waxy crude oils in cold climates or offshore pipelines where temperature drops significantly below pour point. The PPD modifies wax crystal morphology rather than dissolving wax - this is key."</p></div>
    </div>
</div>'''

# Find and replace the Q6-Q10 block
# First find the start of the old combined block
idx = content.find('<!-- Q6-Q10: Wax Removal Methods -->')
if idx == -1:
    print("Q6-Q10 block not found - checking what's there")
    # Find last qcard closing
    import re
    blocks = list(re.finditer(r'<!-- Q\d', content))
    for b in blocks:
        print(b.group(), 'at', b.start())
else:
    # Find end of this block (next script tag or container close)
    end_marker = '\n</div>\n<script'
    end_idx = content.find(end_marker, idx)
    if end_idx == -1:
        print("End not found")
    else:
        new_content = content[:idx] + q6_to_10_replacement + content[end_idx:]
        with open('theory/unit2/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("SUCCESS: Q6-Q10 replaced with separated questions")
