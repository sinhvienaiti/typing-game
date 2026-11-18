# Burst audit (16/11/2026)

Source QA gate: `.agents/skills/game-video-vfx-usage/SKILL.md`. Method: 9 frames spread over each atlas, looked at by one agent (needs a second independent check before any `contentCheck: pass`), plus edge metrics (outer 5% max RGB, per clip in `metrics.json`). Sheets: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-audit/`.

Clips audited: 59. PASS 44, FAIL 15. Not audited: `boss-charge-impact-r2`, `thunder-five-impact-burst-wg` (not in scope). Missing: `metal-impact`, `fire-impact`, `fire-big-burst` (named `fire-burst`).
Every clip fades out to near zero at its last frame; all are one-shot (loop false). The angle column is the angle each can serve.

| clip | result | reason | angle | look | look reason |
| --- | --- | --- | --- | --- | --- |
| blood-big-burst | PASS | spans about 92% of the cell at peak, tight margin | radial burst; reads as a camera-facing card at any angle (rosette) | C | glossy plastic/gummy spiky blob, toy-like |
| blood-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| blood-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| blood-ring-burst | PASS | clean black, margin ok, fades out to 0 | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| dark-big-burst | PASS | sparse red sparks, low energy; shape reads as a faint burst only | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| dark-big-burst-v2 | PASS | starts at full energy, small; engine fade-in needed | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| dark-big-burst-white | FAIL | grey smoke fills the cell and is cut off by the square cell edges (frames 15-27) | radial burst; reads as a camera-facing card at any angle (rosette) | C | flat grey clay spiky blob, no light, smoke card |
| dark-ground-impact | FAIL | baked cobblestone paving scenery at frames 0-8 (and a rim of stone left at the end) | ground; top-down only | C | baked cartoon cobblestone, flat outline ring |
| dark-ground-impact-v2 | PASS | ring starts at full energy; engine fade-in needed | ground; top-down only | B | clean but plain; fine as support layer |
| dark-ground-impact-white | FAIL | same grey smoke clipped by the cell edges; reads as a smoke card, not a ground mark | ground; top-down only | C | flat grey clay spiky blob, no light, smoke card |
| dark-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| dark-impact-white | FAIL | same grey smoke clipped by the cell edges | radial impact; camera-facing card | C | flat grey clay spiky blob, no light, smoke card |
| dark-ring-burst | FAIL | ring touches the left/right/top/bottom cell edges (margin under 2%) | ring; top-down only (flat ring, collapses to a line at a low camera) | C | thin flat single-line ring, generic |
| earth-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | A | volumetric, layered detail, rich light |
| earth-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| earth-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | A | volumetric, layered detail, rich light |
| earth-ring-burst | FAIL | baked solid rock boulder (an object, not a ring) static for about 20 frames, then glows; wrong role | ring; top-down only (flat ring, collapses to a line at a low camera) | C | static clip-art boulder with painted cracks |
| fire-burst | FAIL | flame column anchored at the bottom edge and cut off there (edge pixel 215); fixed side view only; white-hot base clips | side view only (fixed camera); not usable from above | C | flat cartoon clip-art flames, solid fills, blown white base |
| fire-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| fire-ring-burst | PASS | clean black, margin ok, fades out to 0 | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| ice-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | A | volumetric, layered detail, rich light |
| ice-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| ice-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | A | volumetric, layered detail, rich light |
| ice-ring-burst | PASS | spikes about 96% of the cell, tight margin | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| light-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| light-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| light-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| light-ring-burst | PASS | clean black, margin ok, fades out to 0 | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| metal-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | C | flat grey clay spiky blob, no light, smoke card |
| metal-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| metal-ring-burst | PASS | spikes about 96% of the cell, tight margin | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| poison-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | C | flat cartoon green/purple blobs, sticker look |
| poison-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| poison-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | C | flat cartoon green/purple blobs, sticker look |
| poison-ring-burst | FAIL | ring touches the cell edges (edge 31); also baked gold glyph marks that read as text | ring; top-down only (flat ring, collapses to a line at a low camera) | C | flat green outline disc with doodle glyphs |
| star-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| star-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | A | volumetric, layered detail, rich light |
| star-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | A | volumetric, layered detail, rich light |
| star-ring-burst | PASS | trails about 96% of the cell, tight margin | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| thunder-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | A | volumetric, layered detail, rich light |
| thunder-ground-impact | FAIL | bolt tips reach the cell edge in frames 0-8 (edge pixel 82) | ground; top-down only | B | clean but plain; fine as support layer |
| thunder-impact | FAIL | bolts run to the cell edges from frame 0 (cut off at left/right/top/bottom) | radial impact; camera-facing card | A | volumetric, layered detail, rich light |
| thunder-ring-burst | PASS | clean black, margin ok, fades out to 0 | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |
| void-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| void-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | C | flat outlined wireframe squares, vector look |
| void-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| void-ring-burst | FAIL | ring touches the cell edges (edge pixel 255, clipped) | ring; top-down only (flat ring, collapses to a line at a low camera) | C | thin flat single-line ring, generic |
| water-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| water-ground-impact | PASS | clean black, margin ok, fades out to 0 | ground; top-down only | B | clean but plain; fine as support layer |
| water-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| water-ring-burst | FAIL | ring touches/cuts at the cell edges (edge 98); starts at full energy at frame 0 (no fade-in); filled blue disc | ring; top-down only (flat ring, collapses to a line at a low camera) | C | flat blue disc with outline, no depth |
| wind-big-burst | PASS | starts strong at frame 0 (engine fade-in needed) | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| wind-ground-impact | FAIL | hard-edged solid grey disc appears at the centre in frames 23-31 (stray object) | ground; top-down only | B | clean but plain; fine as support layer |
| wind-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| wind-ring-burst | FAIL | concentric HUD-like rings touch the cell edges (edge 156); frame 0 already full energy | ring; top-down only (flat ring, collapses to a line at a low camera) | C | flat HUD/sci-fi concentric circles, not xianxia |
| wood-big-burst | PASS | clean black, margin ok, fades out to 0 | radial burst; reads as a camera-facing card at any angle (rosette) | B | clean but plain; fine as support layer |
| wood-ground-impact | PASS | orange swirl, clean; reads as a ground swirl | ground; top-down only | B | clean but plain; fine as support layer |
| wood-impact | PASS | clean black, margin ok, fades out to 0 | radial impact; camera-facing card | B | clean but plain; fine as support layer |
| wood-ring-burst | FAIL | ring and dark foliage clutter reach the cell edges (edge 83); little fade-in | ring; top-down only (flat ring, collapses to a line at a low camera) | B | clean but plain; fine as support layer |


Look grades (16/11, one blind judge from contact sheets): A 8, B 35, C 16. C clips must be remade; montage `ugly-C.jpg` in the sheets folder.
## Gộp hai giám khảo (16/11)
- **Cả hai chấm C → làm lại (10):** dark-ring-burst, void-ring-burst, water-ring-burst, wind-ring-burst, earth-ring-burst, fire-burst, poison-big-burst, poison-ring-burst, void-ground-impact, dark-ground-impact.
- **Một giám khảo chấm C (10), làm lại sau nhóm trên:** blood-big-burst, dark-big-burst-white, dark-ground-impact-white, dark-impact-white, metal-big-burst, poison-impact (giám khảo 1); ice-ring-burst, wood-big-burst, dark-big-burst, void-big-burst (giám khảo 2).
- **Cả hai chấm A (3):** earth-big-burst, earth-impact, thunder-big-burst — mẫu phong cách khi tạo lại. (Giám khảo 1 thêm: ice-big-burst, ice-impact, star-ground-impact, star-impact, thunder-impact; giám khảo 2 thêm: blood-impact, ice-ground-impact, light-impact, light-ring-burst, star-big-burst.)
