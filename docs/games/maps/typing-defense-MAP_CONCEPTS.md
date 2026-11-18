# Wordwoven: map concepts for every stage (v1.2, 01/11/2026)

Game: **Wordwoven** (repo id `typing-defense`, folder `games/typing-defense`). Written by the map designer after the owner's note of 01/11/2026: the maps of all three games are unacceptable; write one concept per map, have ChatGPT review and paint it, redo whatever falls short, and use only free resources that allow commercial use.

**v1.2 (01/11/2026): the ChatGPT art-director review of map 1 (7.9/10, [`typing-defense-CHATGPT_REVIEW.md`](typing-defense-CHATGPT_REVIEW.md)) is folded into section 3 (read order, materials, light budget, value hierarchy, colour reservations, removals, buildability, its verbatim painting prompt in 3.10) and its idea notes into section 4; layout and camera unchanged.**

**v1.1 (01/11/2026, after the critic's review; this file called it "v2").** What changed from v1:

- **The camera is the real one.** v1 designed for a 50° / 76 m "Battle view" nobody picked. v2 uses the battle camera being built on branch `td-units-3d`: 42° tilt, 46 m, 42° lens (owner 01/11: an oblique 40–45° view). Every on-screen number comes from one projection script, checked against the engine (section 1.3).
- **No sky in the battle frame.** The owner's 01/11 line asks for an oblique 40–45° view *with a sky band*. With a 42° lens that cannot happen: the top edge looks 21° below the horizon. The concept paints no horizon. Decision D1 in 3.2.
- **Layout v2 is withdrawn.** It was drawn for the 50° / 76 m frame. Map 1 keeps today's sim layout; nothing in `slice-1a.ts` changes.
- **ChatGPT paints over a base image** captured from that camera: `games/typing-defense/art-src/_review/maps/map1-base-1280x720.png`, with its legend beside it. The prompt covers light, materials, mood and scale only.
- **Owner decisions of 01/11 applied:**
  - Draconis is Dragonhold's `draconis-v2` (Hỏa Long, rigged).
  - The current houses stay until this concept is approved; no rebuild ticket now.
  - Foes come from the existing models first ([MONSTER_MODEL_INVENTORY](../MONSTER_MODEL_INVENTORY.md)).
  - Only free, commercial-safe assets, licence checked ([FREE_ASSET_SOURCES](../FREE_ASSET_SOURCES.md)).
  - Acceptance bar 8.5.
- **Life first; creatures with no source are removed.** Egrets, swifts, gulls, fish, dragonflies, crabs and butterflies are gone; so is everything the battle frame cannot see.
- **The Tripo list is ordered by "seen in the battle frame".** For map 1 it is empty (3.8).
- **Map 1 stays complete; maps 2–7 are shortened.** They keep their ideas; their screen numbers are removed until each layout is checked with the script.

The paste-ready message for ChatGPT is [`typing-defense-CHATGPT_MESSAGE.md`](typing-defense-CHATGPT_MESSAGE.md). This file is the full design behind it. ChatGPT's answer is [`typing-defense-CHATGPT_REVIEW.md`](typing-defense-CHATGPT_REVIEW.md).

---

## 0. For the reviewer (ChatGPT): what to do with this file

**Status (v1.2).** Steps 1 and 4 are done for map 1 (ChatGPT, Chat mode, High, 01/11: 7.9/10, 8.8–9.0 expected after the changes now in section 3). Next is step 2, with the prompt and the base image in 3.10, then step 3.

1. **Review map 1** as a senior art director of a commercial top-down game, against the bar in 1.2. Score it 0–10, list the gaps, and propose concrete improvements that keep the gameplay layout and the camera.
2. **Paint one concept image over the attached base image.** Keep the exact layout, camera and grey HUD boxes. Replace the coloured placement blocks with what the legend names, as section 3 now describes it (3.10). No text, no sky, no horizon.
3. **Score your own painting** against 1.2. 8.5 is the acceptance bar. Below it, say what is missing and paint again (at most three tries).
4. Give the other maps (section 4) a quick idea review: one or two lines each.

---

## 1. Shared context for every map

### 1.1 The game in five lines

- Wordwoven is a typing tower defence in a painted East Asian fantasy realm inspired by northern Vietnam: limestone karst, silver waterfalls, rice terraces, jade rivers, lanterns.
- **By day** the player builds and runs the village: places towers and farms, sends villagers to chop trees and work fields, and answers the "calls" that appear as word cards above houses.
- **By night** creatures come out of a **Rift** (an ink-black tear in the world) and walk a fixed road to the **Fort**. Towers shoot on their own; typing the words on the cards powers them up.
- **Our side:**
  - **Draconis**: Dragonhold's `draconis-v2` model, Hỏa Long, an ember-red winged dragon. He flies at 4–6 m and perches on roofs; about 3.5 m long with a 6 m wingspan at Wordwoven's scale.
  - Three owlet **Helpers** (1.1–1.3 m, walk).
  - Villagers (1.2–1.4 m).
  - Barracks Spearmen (2.2 m).
- **Foes on map 1** (all with a model, section 3.5): Hopping Zombie and Zombie Leader, Split Blob, Raccoon Dog, River Serpent, Ghost Flame (a VFX wisp), and the boss **Mộc Tinh**, an ancient banyan spirit (7–10 m).

### 1.2 The bar

- **Commercial-game level**, judged against a board of commercial references, never against our own style guide:
  - the owner's reference `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`: a colossal flying beast over a canyon, a cloaked hero, cinematic light, huge scale contrast;
  - our accepted title painting `games/typing-defense/art-src/ui/title-epic/title-backdrop.v2.png`: karst towers in mist, silver falls, a jade river with lanterns, terraces, a sky turtle carrying ruins.
- Keywords: **epic, majestic, cinematic light, deep atmosphere, painterly-realistic, bold readable shapes**.
- **Acceptance: 8.5**, scored in the game's battle frame at its real size, by two independent judges ([QUALITY_RESCUE_2026-11-01](../QUALITY_RESCUE_2026-11-01.md), "chấm C"). 9 is the owner's reference.
- The chibi-chunky models (Fort, towers, foes) stay as they are; **the world around them** must reach the bar.

### 1.3 Camera and frame (the battle camera of record)

**Camera.** Home view of `src/view/3d/camera.ts` on branch `td-units-3d` (worktree `games/.wt-td-units`, uncommitted on 01/11):

| Setting | Value |
|---|---|
| Tilt | 42° (`CAMERA.views.home`) |
| Distance | 46 m |
| Lens | 42° vertical field of view, 16:9 |
| Heading | north, yaw 0 |
| Look point | halfway between the road's fork (6, −34) and the Fort (0, 40): (3, 3) |
| Camera position | (3, 30.8, 37.2) |

The rig's other views:
- PageDown, a close view: 30° at 26 m;
- End, the overview: 60° at 122 m;
- tilt range 22–85°, zoom 22–140 m.

**One script for every number:** `games/typing-defense/tmp/map-concepts/project.mjs` (not tracked; it mirrors `CameraRig.update`, no dependencies).
- Next to it:
  - `map1-layout.json`: the sim layout and the planned blocks;
  - `budget.mjs`: the height budget;
  - `capture-base.mjs`: the capture scenario;
  - `draw-base.py`: the base image.
- Check against the engine: 0 px error on the four bridge ends the engine reports (`node project.mjs --check raw/capture.json`). The engine's two junction plazas sit 0.6–1 m from the route vertices, because the ground rounds the curves.

**The frame at 1280 × 720** (1920 × 1080 is the same frame at 1.5×):

| Screen y | Ground z | Visible x | px per metre | A 2 m foe |
|---|---|---|---|---|
| 0 (top) | −43.0 | −51.7 … 57.7 | 11.7 | 24 px |
| 90 | −26.1 | −43.1 … 49.1 | 13.9 | 26 px |
| 180 | −13.8 | −36.9 … 42.9 | 16.0 | 29 px |
| 360 | 3.0 | −28.4 … 34.4 | 20.4 | 31 px |
| 540 | 13.9 | −22.9 … 28.9 | 24.7 | 32 px |
| 720 (bottom) | 21.5 | −19.0 … 25.0 | 29.1 | 30 px |

**What a standing thing can show** (its height before the top edge cuts it; the same for every column):

| Screen y of its foot | 0 | 20 | 45 | 70 | 90 | 135 | 180 | 270 | 360 | 540 | 719 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Height in frame (m) | 0 | 1.6 | 3.5 | 5.2 | 6.5 | 9.0 | 11.2 | 14.8 | 17.7 | 21.8 | 24.7 |

This table drives every landmark decision:
- **The top band (y < 70) shows almost no height.** A tree there shows its trunk only; its crown overhangs from beyond the top edge.
- **A standing giant can only show in the lower half**, where it would hide the play. So in this frame the scale comes from:
  - things lying on the ground;
  - things cropped by the top edge;
  - water, light and shadow;
  - life.

**Sky: none in play.**

| View | Top edge below the horizon |
|---|---|
| Home | 21° |
| PageDown | 9° |
| End | 39° |
| The rig's lowest tilt, 22° | 1°: the horizon only touches the top edge |

- A sky band of 12 % of the frame needs a 16.5° tilt.
- So the battle frame and the concept painting show **no horizon, no sky and no far mountains above the ground**.
- The sky, the Silverfall cliff and the far karst rings belong to the title painting and to a low tilt the player chooses. This concept does not paint them.

**HUD at 720p** (story mode; the sandbox panel is a dev tool):

| Box | Pixels | Ground it hides at Home |
|---|---|---|
| Run panel, top left | 12–296 × 12–198 | x −49 … −18, z −40 … −12: the north bridge, the north cascade, 7 trees of the west-bank grove |
| Settings gear and Sound speaker | 1196–1268 × 12–44 | the world-edge window |
| Team bar, bottom left | 12–296 × 598–708 | meadow west of the S bend |
| Typing strip | 308–668 × 668–712 | the road toward the Fort |
| Action bar, bottom right | 878–1268 × 666–708 | meadow |
| Teaching rows, top right, tutorial beats only | 964–1268 × 80–260 | x 21 … 49, z −28 … −5 |
| Boss bar, top centre, night 5 only | 430–850 × 10–84 | the muster ground at the fork |

**Readability.**
- The brightest things on screen are word cards, typed letters and shots.
- Ground under a word card stays below luma 0.6.
- A grey, blurred screenshot must still show lanes, foes, our units and health bars.

### 1.4 Rules every map follows

- **English** for everything the player reads. Proper names stay: Draconis, Mộc Tinh, Chấm, Phẩy, Gạch.
- **Banned** (art bible, design rule 22.1):
  - thatched huts, bamboo walls, wooden country shacks;
  - windmills, tea hills, rainbows, striped lighthouses;
  - cartoon daisies, strawberry bushes, ink-outlined clip-art, candy-floss trees.
  - The current thatched houses stay until this concept is approved (owner, 01/11). The review chose **dark fired-tile roofs** on the same silhouettes for the painting (3.6).
- **No religious buildings or objects:** no pagodas, temples, shrines, torii, altars, incense, Buddha or deity statues.
  - Secular forms are fine: tiered stone watchtowers, gatehouses, granaries.
  - Allowed motifs: Dong Son sun-star rings, cranes as carvings, cloud scrolls, Ly-dynasty dragon balustrades.
- **Colour script:**
  - jade and teal shadows (never black), warm gold light, silver water and mist, limestone white;
  - small cinnabar-red and lantern-amber accents;
  - grass jade-teal (hue 80–150°, median saturation ≤ 0.55);
  - roads at least 0.15 luma brighter than grass.
- **Colours reserved for signals:**
  - word-card ivory and gold, typed-letter glow, shot and hit flashes (warm white-gold);
  - Ghost Flame cold cyan;
  - the Rift's indigo-black with a cold rim (a blue-leaning near-black, never violet).
  - The world never uses saturated versions of these. No bright pink, magenta or purple (keying colours).
- **Light:**
  - Day: one sun from the south-west (lower left of the frame), 40° high, long sharp shadows toward the upper right, drifting cloud shadows. This is the stage's `SUN` vector.
  - Night: a low cold moon from the north-east (upper right; the stage's `MOON`), amber lamps, thicker mist.
- **No code-drawn stand-ins** for art. Shaders and VFX that meet the [layered VFX standard](../VFX_STANDARD.md) are allowed: water, fog, wind, the Rift, shadows.
- **Sources:**
  - Our own accepted art.
  - Free assets whose licence allows commercial use and shipping the raw files in a web build: CC0 first (Poly Haven, ambientCG, cgbookcase); CC-BY with credit in `docs/games/THIRD_PARTY.md`; MIT, BSD or ISC code (three r170 add-ons, Quick_Grass, `three-custom-shader-material`, `@pmndrs/vanilla`).
  - Need the owner's yes: Quaternius (its site licence is QAL v1.0, outside the list) and pmndrs `postprocessing` (Zlib).
  - Grey-box only: Kenney and KayKit (the toy look).
  - Sketchfab: only CC0 or CC-BY models, one by one, never NoAI, never fed to AI tools.
  - Licences are checked on the source page and recorded in `THIRD_PARTY.md` at download.
  - Not allowed: NC, ND, "editorial", "personal use", unclear packs, engine-locked store licences.
- **Budgets per map** (High / Medium):
  - ≤ 150 / 100 draw calls, ≤ 1.5 / 0.7 million triangles, media ≤ 16 / 9 MB.
  - Models a player sees up close keep at least 2,000 triangles and their normal and roughness maps ([MODEL_QUALITY](../MODEL_QUALITY.md)).

### 1.5 The campaign

| # | Map | Status | Waves | Boss | Section |
|---|---|---|---|---|---|
| W1-1 | **Silverfall Meadow** (`w1-silverfall`) | Built: 5 days, 5 nights; 3D in progress (foes and soldiers on `td-units-3d`) | 5 nights | Mộc Tinh, retreats at 50 % | 3 (full) |
| W1-2 | **Whitestone Bay** (`w1-whitestone`) | Planned | 10 | Storm Eagle | 4.1 |
| W1-3 | **Old Rootwood** (`w1-rootwood`) | Planned | 12 | Mộc Tinh, full | 4.2 |
| W1-S | **Goldstair Terraces** (side map, was "Tea Hills") | Planned | 8 | none | 4.3 |
| W1-N | **Starsea Rift** (bonus, Neon style pack) | Planned | 8 | Rift Warden (proposal) | 4.4 |
| W2–W5 | Amber Dunes, Frostsong North, Starsea Isles, Emberstone Highlands | After the MVP | — | — | 4.5 |

The sandbox (`?sandbox=1`) plays on map 1's field.

---

## 2. One method for every map

1. **Lock the layout in the real battle frame.** Run `project.mjs` on the layout; compute the height budget; mark the HUD boxes. Fix any lane, crossing or resource under the HUD.
2. **Base image.** Capture the real camera at 1280 × 720 and draw translucent blocks for every planned landmark and key figure at its projected position and height, with grey HUD boxes and a legend.
3. **Concept painting over the base** (ChatGPT image, or Adobe Firefly Image 5 with the base as composition reference). Accepted at 8.5 or more against 1.2, with lanes, foes and our units readable in a half-size grey copy.
4. **Life before polish.** Foes, Draconis, Helpers, villagers, Spearmen and the choppable trees on screen before more ground polish.
5. **Ground, water and light**, then the cropped landmarks, then dressing.
6. **Judge in-game screenshots** in the battle frame at both sizes (day, night, boss) beside the painting and the reference board, by two independent judges ("chấm C").

---

## 3. W1-1 Silverfall Meadow (`w1-silverfall`): full concept

Where v1.1 and the ChatGPT review disagreed, the review wins, because none of its changes moves gameplay (roads, plazas, houses, trees, HUD and camera stay; uneven tree spacing is done without moving the 36 sim trees): the Commons stops being a focal point, the spur loses its glowing gold, the world edge becomes a cropped karst wall instead of a pinnacle, flower drifts become sparse muted colonies, rocks are clustered, roofs are dark fired tile, and Draconis drops to the third or fourth read.

### 3.1 Name and story beat

**Silverfall Meadow.** A high meadow on the brink of the Silverfall gorge, where the Silver Brook runs to the falls. At dusk the Rift tears open at the meadow's north edge and its ink runs down the old road. The valley's first Fort must hold five nights, until the nameless banyan, Mộc Tinh, rises and is driven back.

### 3.2 Gameplay layout (today's sim, unchanged) and the frame

Layout from `src/content/slice-1a.ts` (identical on `main` and `td-units-3d`, 01/11):

| Element | World (m) | Screen at 720p (Home) | In frame |
|---|---|---|---|
| Gate (the Rift) | (−10, −46) | (492, −13) | no: 3 m beyond the top edge |
| Shared road | (−10, −46) → (−4, −40) → (6, −34) | enters the top edge at x ≈ 480–560 | yes, from the edge |
| Fork plaza | (6, −34) | (678, 44) | yes |
| West branch | (−12, −20) → (−10, 0) → merge | bend (417, 131) | yes |
| East branch | (16, −20) → (12, 2) → merge | bend (833, 131) | yes |
| Merge plaza | (0, 12) | (568, 504) | yes |
| S toward the Fort | (−6, 20) → (6, 30) → (0, 40) | leaves the bottom edge at (387, 680) | partly |
| Fort | (0, 40) | (488, 1615) | no: 18 m below the bottom edge |
| Flight line (Ghost Flames, 3 m up) | gate → (20, −20) → Fort | bend (901, 89) | yes |
| Silver Brook, 3 m | x −25.5 … −22.5, full length | left third, leaves the left edge at y ≈ 500 | yes |
| Bridges (walkers) | (−24, −14), (−24, 26) | (208, 178) under the run panel; the south one out | — |
| Ore ★★★ with the Gold Mine | (26, −30) | (946, 66) | yes |
| Ore ★★, ore ★ | (−34, 8), (−12, 32) | out (left; below) | no |
| Choppable trees | 36 in five groves | 29 in frame, all above y 165 | the gate and north-east groves: trunks only |
| Preset Archer, Cannon, Barracks | (−8, 12), (7, 12), (3, 18) | (378, 504), (735, 504), (640, 630) | yes |

**What the player sees:** the middle of the fight. The road comes in at the top edge, splits at the fork plaza, runs round the meadow loop and meets again at the merge plaza, where the defence stands. About 60 % of the frame is build ground.

**Decisions for the owner** (each one is computed with the script):

- **D1. Sky.** A 40–45° view with a 42° lens has no sky; its top edge is 19–24° below the horizon. Recommended: keep 42°, no sky in the battle frame. If the owner wants a sky view on demand, lower the rig's tilt limit from 22° to 16° (a 12 % sky band at 16.5°); at that tilt a 2 m foe is 15 px at the far road and 82 px at the near edge, so it is a different game camera and never the default.
- **D2. The Rift and its muster ground.** At this Home view the Rift stands 3 m beyond the top edge, so a standing 14 m tear does not show at all.
  - Recommended (view only, no sim change):
    - draw the Rift as a ground-level wound whose ink spills down the shared road to the fork plaza;
    - at dusk the night's first pack musters in the ink at the fork plaza (5, −35), where a 2 m foe fits whole (3.1 m of height in frame);
    - when the wave starts, that preview pack sinks into the ink, and the sim's members walk in from the top edge 1–3 s later.
  - Alternative: move the Home look point 3.7 m north (`homeShare` 0.5 → 0.45). The gate then sits on the top edge and whole foes stand at the first bend (−4, −40); the Barracks leaves the bottom edge.
- **D3. HUD over play.**
  - The run panel hides the north bridge, the north cascade and 7 choppable trees.
  - The teaching rows hide part of the east meadow.
  - The boss bar hides the muster ground on night 5.
  - Recommended (UI lane): by night the run panel shows only its top block (y ≤ 110), and the early-night call moves into the action bar. That frees the bridge (y 133–193).
  - Moving the camera does not solve it: at look x −4 the bridge's centre clears the panel, but the whole frame shifts 5 m west and the Gold Mine (then at x 1039) crowds the corner icons and the teaching rows.
- **D4. Layout v2 is withdrawn.** No golden, balance or scenario change.

### 3.3 Read order and what carries the scale

**Read order.** The concept is edited, not redesigned: it was held back by hierarchy, not asset quality, because every idea tried to be memorable at once. The frame reads in this order, and nothing lower may outshine anything higher:

1. **The Rift and the invasion** (top centre): the ink and the muster pack.
2. **The roads and the defensive line**: the flagstone road and the three Spearmen at the merge, the second story point.
3. **The huge meadow and the gorge**: the jade-teal field, the brook, the world edge, the cloud shadows.
4. **The secondary life**: Draconis (third or fourth, never second), the owlets, the villagers, the lanterns.

The forest edge, the gold spur and the Sun-Star Commons are support. They give depth and texture and are never a focal point of their own.

**What carries the scale.** At 42° nothing tall can stand in the top half without being cut, and nothing tall may stand in the lower half without hiding play (rule: nothing over 3 m south of a lane or build ground). So:

1. **The Rift's ink tide: the main focal point (x 429–758, y 0–66).** The ink lies on the ground, so it reads from above.
   - A near-black indigo mass (value 8–15 %) runs from the top edge down the shared road to the fork plaza. Two or three big curled edges, like scorched paper, not many tendrils.
   - A narrow cold rim where the ink meets the grass, well below the brightness of the Ghost Flame cyan. No strong glow.
   - The grass within 1–2 m of the ink turns charcoal grey.
   - Thin smoke rises and leaves the frame at once; it never hangs over the road.
2. **The muster pack (fork plaza).** 5–7 Hopping Zombies in earth-grey robes (in game a muted robe tint, the model unchanged), staggered so they read as one silhouette in the ink. It is the view-only preview of D2, so its size does not touch the sim. The night-5 boss bar may cover this spot, so the story cannot depend on small details here.
3. **The forest edge (top band).** The 29 choppable trees in frame all stand above y 165; in the gate and north-east groves only their trunks and lowest boughs fit.
   - Paint only trunks, low boughs and crowns overhanging from beyond the top edge, at uneven spacing, with dark gaps between trunks and warm sun shafts through them. No flat wall of canopy.
   - Keep a clear visual channel over the road where it enters at x 480–560: the crowns of the two nearest trees, (−14.5, −42.5) west and (−1.5, −44) east, lean away from it.
   - The north-east grove is softer: lower contrast, in the gorge mist.
   - The 36 sim positions stay. The unevenness comes from crown size, species, lean and non-choppable trees beyond the top edge.
4. **The gold spur (top right, behind the Gold Mine).** 9 m tall, rising out of the top edge; only its lowest 3 m are in frame. Pale limestone strata with muted ochre mineral seams. No glowing gold.
5. **The Silver Brook (left third).** An irregular limestone cleft, never a straight line: jade-silver water, then dark wet stone, then reeds. Underwater stones break the line. Foam only at the two 0.8 m drops. It carries the light into a frame with no sky.
6. **The world edge (top-right corner, x 1161–1280, y 0–117, partly under the corner icons).** East of x 48: the meadow lip, a limestone fracture, a mist-filled void and a huge karst wall cropped by the right edge. Not a small free-standing karst pinnacle. Atmosphere only.
7. **Giant shadows.** One or two huge cloud shadows drift across the field, never mottled patches. On Day 3 the sky turtle's shadow, about 60 m long, crosses the meadow in about 20 s. Draconis' large shadow on the road carries his height (3.5).
8. **Life** (3.5): the muster pack, the walking packs, the Spearmen's line at the merge, Draconis' shadow sweeping the road.

**The Sun-Star Commons (frame centre): a quiet floor, not a focal point.** A 16 m Dong Son sun-star ring of worn limestone stays inlaid in the turf inside the road loop, flush with it.
- Only 10–15 % lighter than the turf, with 15–20 % of it hidden under moss, dirt and wear; a low-contrast engraving.
- Archaeological, not mystical: no glow, no crisp lines. It must not show in the grey blur test.
- It is flat, so houses may stand on it. It still foreshadows the Seal Dais of later maps.

The Silverfall cliff and the Guardian statue of v1 stood outside this frame and are dropped from the battle concept.

### 3.4 Planned elements in the frame (the base image's blocks)

| Element | World position and size | Screen box at 720p | Source |
|---|---|---|---|
| Rift ink spill | gate (−10, −46) to the fork plaza (6, −34), 6–10 m wide, ground level; two or three big curled edges, a narrow cold rim, charcoal-grey grass 1–2 m around it | x 429–758, y 0–66 | Shader and VFX on our own art: `art-src/vfx/ink-smoke.png`, `ink-splat.png`, `paper-scraps.png`, plus Unity Labs CC0 smoke flipbooks; five phases per the VFX standard |
| Muster pack | (5, −35), 8 × 3.5 m; 5–7 Hopping Zombies, staggered, one silhouette | x 614–719, y 5–48 | Existing foe models (3.5) |
| Gold spur | (31, −35), 9 × 6 m, 9 m tall; lowest 3 m in frame | x 928–1102, y 0–55 | CC0 modular limestone rock or cliff mesh with a pale-strata material and muted ochre seams, no emissive |
| Sun-Star Commons | centre (2, −10), radius 6.3–8 m, flat; 10–15 % lighter than the turf, 15–20 % covered | x 488–758, y 146–297 | A decal or a displaced mesh: a painted decal (new small 2D ticket) or an ambientCG CC0 paving material through a ring mask, vertex-blended into the turf |
| Silver Brook cleft | x −26.5 … −21.5; irregular banks, underwater stones | left third | three r170 `Water2` (MIT) with flow maps and CC0 normal maps; CC0 limestone material on the banks, dark and wet at the waterline |
| Cascades | (−24, −31), (−24, −3), 0.8 m; the only foam on the brook | (246–320, 47–64) under the run panel; (81–189, 267–292) | Water shader, `art-src/vfx/waterfall-foam.png`, `water-splash.png` |
| Stone arch bridge | (−24, −14), 8 × 3.5 m | x 120–280, y 133–193, under the run panel | Keep `3d/props/cau-go.glb`, relit, until D3 frees the spot |
| World-edge window | east of x 48, z −44 … −22; meadow lip, limestone fracture, mist void, karst wall | x 1161–1280, y 0–117 | Terrain lip and fracture beyond the field (code), fog and mist shader, one CC0 rock-wall mesh scaled up and cropped by the right edge |
| Choppable trees | 36 sim positions, 8–14 m; varied crowns, a road channel at x 480–560 | 29 in the top band | Free modular 3D trees first (Poly Haven CC0; Quaternius Stylized Nature MegaKit only if the owner accepts QAL); the accepted 116 billboards as the fallback |

### 3.5 Life in the frame (first, before any polish)

**Foes** (every one has a model; [MONSTER_MODEL_INVENTORY](../MONSTER_MODEL_INVENTORY.md) §4):

| Foe (nights) | Model | State |
|---|---|---|
| Hopping Zombie (1–5), Zombie Leader (sandbox) | `enemies/cuong-thi` + `attachments/cuong-thi-lead-hat` | Shipped, 28 bones, 5 clips |
| Split Blob (3) | `enemies/nuppeppo` | Shipped, with a split death clip |
| Raccoon Dog (4) | `enemies/tanuki` | Shipped, drum Skill clip |
| River Serpent (4–5) | `enemies/thuong-luong` | Shipped, 20 tail segments |
| Ghost Flame (2–5) | none: a cold-cyan VFX wisp on the flight line | VFX standard; Space Typing's `shadow-mine` as its core (inventory W4) |
| Sapling (boss phase 2), Troll (sandbox) | `enemies/mam-go`, `enemies/troll` | Shipped |
| Mộc Tinh (boss, night 5) | `art-src/3d/bosses/moc-tinh.glb`, 29,177 triangles | Tripo original, not rigged: one rig for Wordwoven and Dragonhold's B11 `rotwood-ancient` |

On `td-units-3d` the foes and Spearmen are drawn in 3D (the base image shows nine foes and three Spearmen). On `main` the 3D view still draws none.

**Where the player sees them:**
- **Dusk:** the ink spills down the shared road, and the first pack musters at the fork plaza (D2): 5–7 Hopping Zombies in earth-grey robes, staggered into one silhouette.
- **Night:** packs walk in from the top edge and split at the fork. Ghost Flames follow the flight line at 3 m over the east meadow, a faint ink trail behind them, the only cold-cyan lights in the frame.
- **The merge plaza is the killing ground.** Arrows and cannon shots cross it, and the Spearmen hold the line.

**Our side** (in read order: the Spearmen second, after the Rift; Draconis third or fourth; the rest after him):
- **Spearmen** (`units/linh-giao`, rigged, 8 clips) hold the merge: the frame's second story point. A warm rim on shoulders and spear tips, long shadows to the upper right, no showy VFX.
- **Draconis** (`games/dragon-hold/public/assets/dragon-hold/models/heroes/draconis-v2/`, 22,000 triangles, 25 bones, Fly, Idle_Hover, Boost, Attack, Cast clips). He glides at 5–6.5 m over the west branch and perches on the roof of the house he powers.
  - Banked steeply, so his body reads compact and his wings follow the road.
  - Deep ember red, never bright red. In game this is a darker tint on Wordwoven's instance; the model itself stays as it is.
  - His large shadow on the road carries his height. He is noticed third or fourth, never second.
- **Three owlet Helpers** (`art-src/models/helpers/helper-owlet.glb`, rigged, 13 clips, wing-band attachments) work beside the crew at the Cannon Tower.
  - Natural brown, grey and cream plumage; the shipped model's brief already asks for grey-brown down, a beige face and a cream cap.
  - Working poses: carrying, pulling, inspecting.
- **Villagers** (`art-src/3d/workers/worker-base.glb` + 24 kit items): a small group at the west-bank grove (−16.5, −25), beside the west branch, never on the road, with fresh logs and wood chips around them (axe swings; a tree falls only when it is empty). They are Tripo originals and are not rigged yet: rig them with the Mesh2Motion human rig (CC0), or with Quaternius UAL if the owner accepts QAL.

**Ambient (VFX and shaders only):**
- mist from the gorge and the brook;
- fireflies along the brook at night (`@pmndrs/vanilla` `Sparkles`, MIT): dim, sparse cool-green points, never gold or cyan, so they never read as typed letters, shots or Ghost Flames;
- paper lanterns drifting north on night 3: small amber cores like the tower lanterns, never in front of a word card;
- one or two huge cloud shadows (never mottled patches), and the sky turtle's shadow (our accepted `sky-beast-top.png`, 114, as a shadow cookie);
- wind in grass and boughs; pennants on the towers, and lanterns with small amber cores.

**Removed (no source, or out of frame):** egrets, swifts, fish, dragonflies, water buffalo (`trau.glb` exists, unrigged, and its west-bank spot is under the run panel), Alicanto (not in map 1's waves).

### 3.6 Depth, light, weather, colour

| Layer (battle frame) | What |
|---|---|
| Top border | The forest edge (trunks, low boughs, overhanging crowns at uneven spacing, dark gaps, warm shafts), the Rift's ink and smoke, the spur's lowest 3 m, the world-edge mist and cropped karst wall at the top right. It steps back in values (dark trunks and gaps, warm shafts, the softer misted north-east grove), so it never reads as one flat wall |
| Playfield | Deep jade-teal meadow in broad bands; the wet limestone flag road; the Sun-Star Commons, low-contrast; the brook cleft; the merge plaza |
| Bottom edge | The road leaving toward the Fort (out of frame); at night a faint warm spill from the Fort's lamps along the bottom edge, inside the road's value band, not a pool of light |

**Materials.**

| Surface | Look |
|---|---|
| Road | Wet fitted limestone flags with worn centres, broken moss lines, puddles and darker damp joints. One clear value step above the meadow. Near the top edge the detail resolves into large masses |
| Meadow | Deep jade-teal in broad bands: short grass, damp grass, moss, trampled ground. Sparse flower colonies in muted tones. Never mint; no flower decals |
| House pads | Quiet ground around each house, under 60 % brightness |
| Houses | **Dark fired-tile roofs** instead of thatch, on today's silhouettes (the rebuild waits for the owner's approval of the painting) |
| Silver Brook | Jade-silver water, then dark wet stone, then reeds, in an irregular limestone cleft; underwater stones; foam only at the two drops |
| Sun-Star Commons | Worn limestone 10–15 % lighter than the turf, 15–20 % under moss, dirt and wear |
| Gold spur | Pale limestone strata with muted ochre seams |
| World edge | Meadow lip, limestone fracture, mist in the void, a huge karst wall cropped by the right edge |

**Light budget.**
- One source: a golden sun from the south-west (lower left), low at dusk, long shadows to the upper right.
- One or two huge cloud shadows, not mottled patches.
- Shadows jade-teal, never black.
- Lanterns are small amber cores, not pools of light.
- The Rift gives only a narrow cold edge and lights nothing else.
- Speculars on wet flags and water stay inside their surface's band in the value table; nothing in the world reaches the word cards.

**Value hierarchy for gameplay** (grey value, 0 % black to 100 % white):

| Element | Value |
|---|---|
| Rift interior | 8–15 % |
| Deep vegetation and shadow | 20–30 % |
| Meadow | 30–42 % |
| House pads | 35–50 % |
| Road | 48–58 % |
| Sunlit limestone | 55–65 % |
| Word cards and VFX | above all of these |

The shared rules of 1.3–1.4 still hold on top: ground under a word card below luma 0.6, the road at least 0.15 luma above the grass beside it.

**Colour reservations on this map.**
- Bright gold: only the signals of 1.4 (word cards, typed letters, shots). The spur's seams are muted ochre and the mine's gold does not glow.
- Red: Draconis is deep ember red, never bright red; cinnabar stays a small accent.
- The Rift: indigo-black (blue-leaning, never violet) with a narrow cold rim, dimmer than the Ghost Flame cyan, which is the only cyan light.
- No pink, magenta or purple (keying colours).

**Remove:** flower decals; glowing gold; strong Rift glow; evenly spaced trees; scattered small rocks; detail inside the word-card zones; high-contrast ring engraving; bright red on Draconis.

**One beat per day and night** (the sun stays south-west; height, colour and weather change):

| Beat | What happens | Light, weather, colour |
|---|---|---|
| Day 1 | Fort, Archer Tower, villagers chop | Morning after rain, wet flags with speculars kept inside the road's value band, mist lifting off the brook; jade and soft gold light |
| Night 1 | 10 Hopping Zombies; the Rift opens for the first time | Clear; low cold moon from the upper right; the ink's narrow cold rim at the top edge, no glow; small amber lantern cores on the towers |
| Day 2 | Barracks | High thin cloud, wind in the grass |
| Night 2 | Zombies and the first Ghost Flames | Ground mist along the brook; the Ghost Flames are the only cyan lights |
| Day 3 | Gold Mine, Cannon Tower, Fort level 2 | Clear high summer sun, warm but never the word cards' gold, one or two huge cumulus shadows; the sky turtle's shadow crosses the field |
| Night 3 | Split Blobs | Lantern night: paper lanterns drift north over the field, small amber cores, not pools of light |
| Day 4 | Upgrades | Warm haze, dust motes in the sun shafts under the boughs |
| Night 4 | Raccoon Dogs (drums), a River Serpent, packs | Fog banks roll in from the gorge; foes appear out of the fog |
| Day 5 | Fort level 3 | A storm front darkens the top edge; low light breaks under it; wind bends the boughs |
| Night 5 | River Serpents, then **Mộc Tinh rises** on the road | Thunderstorm, rain, lightning off frame (a short cold lift in the mist, below the word cards); the ink tide reaches the fork; the mist shifts 20 % toward the boss's amber-moss; root cracks spread across the road; when it retreats the rain stops |

### 3.7 Set dressing (only what the frame shows)

| Item | Count and scale |
|---|---|
| Road | Wet fitted limestone flags, lane 3.8 m wide (±15 %), worn centres, broken moss lines, darker damp joints, worn verge 0.5 m; junction plazas at the fork and the merge; a dressing item every 2–6 m (kerb stones in the flags' own grey, grass tufts, broken slabs, puddles); in the top band the detail merges into large masses; 4 roadside lantern posts (2.5 m) at the two plazas, small amber cores |
| Sun-Star Commons | 1 ring, 16 m across, flush with the turf, 10–15 % lighter than it, moss and dirt over 15–20 % of it, low-contrast grooves |
| Silver Brook | 3 m of water in an irregular cleft, 1 m banks of dark wet stone, 2 cascades (the only foam), 30 reed clumps (1.5–2.5 m), 20 river stones, some under water to break the line |
| Gold spur and node | 1 spur (9 m, lowest 3 m in frame) of pale limestone strata with muted ochre seams; gold piles and the mine cart (existing `3d/props/gold-mine-cart.glb`, `gold-pile-1…4.glb`), not glowing |
| Trees | 36 choppable trees (sea-almond, mountain pine, 8–14 m) at their sim positions, varied in crown size, species and lean; non-choppable trees beyond the top edge fill the overhang at uneven spacing (view only, not in `slice-1a.ts`, never on the shared road or the gate); stumps regrow at dawn |
| Understory | Ferns and shrubs (1–2 m) only at grove edges; sparse flower colonies in muted tones, no decals; grass blades 1,600 (Medium) to 4,000 (High) |
| Rocks | Up to 40 limestone boulders (0.6–2.5 m), only in clusters (grove edges, brook banks, the world-edge lip); no scattered small rocks; never on a lane or a build spot the player uses often |
| Houses | Today's silhouettes with dark fired-tile roofs (concept); quiet pads under 60 % brightness; no detail inside the word-card zones above them |
| World-edge window | Meadow lip, a limestone fracture, mist in the void, one huge karst wall cropped by the right edge |

### 3.8 Sources and the Tripo list

| Piece | Source | Status |
|---|---|---|
| Fort, towers, mine, kits | `art-src/3d/buildings/*.glb`, `3d/kits/*` | Keep (owner 01/11) until the owner approves the painting; relight; then dark fired-tile roofs on the same silhouettes |
| Bridge, kerb stones | `3d/props/cau-go.glb`, `3d/props/da-ke.glb` | Keep, relight |
| Ground: meadow, moss, road, verge | Tiling ambientCG and Poly Haven CC0 PBR ground sets (mossy grass, wet earth, gravel, flagstone), vertex-blended into the meadow's bands, with our painted decals on top (no flower decals); Quick_Grass (MIT) for blades | Asset download with the licence recorded |
| Trees and rocks | Free modular packs first, as for Dragonhold (owner 01/11): Poly Haven CC0 trees and CC0 modular limestone rocks; Quaternius only after the owner accepts QAL; the accepted 116 billboards as the fallback | To try |
| Water, mist, gorge edge | three r170 `Water2` (MIT) + CC0 normal and flow maps; our foam and splash art; mist and fog shaders; the gorge edge is terrain, fog and one cropped CC0 rock wall | Code |
| Rift, Ghost Flames | Our ink art + Unity Labs CC0 flipbooks, five-phase VFX | Art exists |
| Sun-Star Commons | A decal or a displaced mesh: new small 2D decal ticket (Codex) or a CC0 paving material through a mask | New |
| Light | Poly Haven CC0 HDRI for image-based light (no visible sky); r170 `GodRaysShader` (MIT) for the shafts; cloud-shadow shader with CC0 noise | Code |
| Characters | All listed in 3.5 | Exist; rigs needed for villagers and Mộc Tinh |

**No bespoke environment model is needed** (review): CC0 limestone and modular rocks, tiling ground materials, a decal or displaced mesh for the ring, vertex blending, water and mist shaders, VFX and modular trees cover the frame.

**Tripo, ordered by "seen in the battle frame": none for map 1.** Everything the frame shows exists or comes from free packs and shaders. Not requested now:
- the Guardian statue (out of frame);
- the dragon stairway and the bronze-drum terrace (the knoll is gone; the flat sun-star ring replaces the terrace);
- ruined watchtowers, hamlet houses and the cliff wall (out of frame);
- the stone arch bridge (under the run panel until D3);
- the houses (dark fired-tile roofs on the same silhouettes, after the owner approves the painting).

### 3.9 What is wrong with today's version

Evidence: the Home capture on `td-units-3d`, High, 1280 × 720, day 1 with the sandbox preset (the base image is made from it). Night not captured this round.

1. **The threat's origin is off-screen.** The Rift is 3 m above the top edge and the Fort 18 m below the bottom edge. Foes slide in from the edge with nothing to announce them.
2. **Half the life is missing.** Foes and Spearmen are drawn on `td-units-3d` (none on `main`), but Draconis, the Helpers and the villagers are not, and **the 36 choppable trees are not drawn at all**. The yellow-green blobs are flat flower decals.
3. **Ground like a football pitch.** One flat mint green, a beige road, white kerb specks; the ★★★ node is a beige disc.
4. **The brook is a concrete gutter**: a straight grey strip with a plank bridge, and half of it sits under the run panel.
5. **No scale.** The top band is bare lawn: nothing is cropped by the edge, nothing rises, no edge of the world. Nothing stands taller than the Archer Tower.
6. **The centre is empty.** The road loop encloses about a sixth of the frame, all plain lawn.
7. **Off-bible thatched houses** (kept until the owner approves the concept, which paints dark fired-tile roofs).
8. **HUD over play**: the bridge, the north cascade and 7 trees under the run panel (D3).

### 3.10 The base image and the concept painting prompt

- **Base image to attach:** `games/typing-defense/art-src/_review/maps/map1-base-1280x720.png`.
- **Legend:** `map1-base-legend.md` beside it. It lists every colour, world position and screen box. The coloured blocks are placement codes, not colours to paint. Its words for the gold spur ("gold-veined") and the world edge ("a karst pinnacle") are v1.1; where they differ, this section and the prompt win. Its purple (Rift), pink (owlets), cyan (cascades, bridge) and yellow (spur) blocks are codes only: the painting has no purple or pink, no cyan light and no glowing gold.
- **Tool:** ChatGPT image in Chat mode with High effort, or Adobe Firefly Image 5 with the base image as composition reference.
- **Acceptance:** 8.5 or more from two blind judges against 1.2; lanes, foes and our units readable in a half-size grey copy, and the Commons gone in the grey blur test. ChatGPT expects 8.8–9.0 for a painting that follows this section.

**Concept painting prompt** (ChatGPT, verbatim, 01/11/2026):

```text
Use the supplied Wordwoven gameplay capture as the exact composition reference. Preserve the 42° battle camera, framing, roads, stream, plazas, four house silhouettes, soldiers, foes and gameplay spacing. Upgrade only the world into a painterly-realistic commercial fantasy key frame at dusk. At the north edge, show indigo-black Rift ink entering from off-screen, curling like scorched paper over the shared road, with a restrained cold rim, grey-withered grass and thin smoke cropped by the frame. Keep a small readable zombie pack in the fork. Build a cropped forest edge across the top: sea-almond and mountain-pine trunks, low boughs and overhanging crowns, warm sun shafts, no visible sky. Add the low limestone spur behind the mine with muted ochre mineral seams, not glowing gold. Inside the loop, inlay a worn 16 m radial limestone sun-star ring flush with turf, mossy and low-contrast. Render the Silver Brook as silver-jade water in a limestone cleft with reeds, stones and two small cascades. At right, show the meadow lip, gorge mist and a cropped karst wall. Keep Draconis banked and readable, emphasizing his long shadow. Add owlet workers, villagers chopping, amber tower lanterns, wet flagstones, jade-teal shadows and drifting cloud shadows. Replace thatch with dark fired-tile roofs. Keep HUD and word-card zones flat dark grey. No text, sky, horizon, religious objects, pink, magenta or purple.
```

The v1.1 prompt is superseded; git history keeps it.

---

## 4. Other maps (shortened; screen numbers removed until each layout is checked with the script)

Rules each of these must meet in the 42° battle frame (from 1.3):
- the giant reads from above (lying, flat or cropped by the top edge), or stands outside the frame;
- a standing Rift sits at least 180 px below the top edge (11 m of height in frame), or is a ground-level wound;
- the muster ground sits at least 45 px below the top edge (3.5 m in frame);
- no lane, crossing or resource under a HUD box.

ChatGPT's idea review (01/11, with map 1) is applied in each entry below:

| Map | Idea score | Verdict |
|---|---|---|
| Whitestone Bay | 8.6 | Strong for this camera |
| Old Rootwood | 8.8 | The strongest for this camera |
| Goldstair Terraces | 8.2 | Beautiful but risky: gold and the festival can overpower roads and cards |
| Starsea Rift | 7.3 | The weakest: its premise needs sky and a vertical drop |

### 4.1 W1-2 Whitestone Bay (`w1-whitestone`)

- **Story.** The Storm Eagle has seized the Stone Otters' boats and gold. Two Rifts open on the beach while the tide turns; winning back the bay returns the feather that carries half of the banyan's lost name.
- **Layout (to re-check).**
  - Sea in the north; two Rifts on the sand; two causeways around the White Stone Terrace, merging before the Fort.
  - The Boat Cove (fish ponds) in the west; the rich headland in the east under the flight line.
  - The Tide changes every two waves: low tide favours the west Rift and pays the ponds ×1.5; high tide the reverse.
- **Scale in the 42° frame.**
  - Review (8.6): strong for this camera. The surf lines, the wet tide flats and the sea gate's huge shadow carry the scale.
  - The surf line and wet sand are the top band; seen from above, waves roll in through the arches of a colossal three-arched sea gate whose feet stand in the surf and whose roofs leave the frame. Keep the arches mostly cropped; the gate's huge shadow across the tide flats shows its size.
  - The tide visibly moves the waterline ±6 m (a shader uniform, wet-sand darkening).
  - A stone lantern tower on the headland replaces the old striped lighthouse.
  - The sea pillars are seen only on the title.
- **Life.**
  - Foes, all Tripo originals: Bifang (`tat-phuong`), Alicanto, Kamaitachi; Troll and Hopping Zombie are rigged. The originals need rigs.
  - Boss: Storm Eagle (`dai-bang-tinh`, 34,927 triangles, unrigged), whose shadow sweeps the beach.
  - Defenders: villagers from `worker-base` as fishers.
  - Gulls and crabs removed (no source).
- **Needs.**
  - Tripo only for what the frame will show: the sea gate (source `art-src/landmarks-epic/stone-gate.png`) and the lantern tower (`lantern-tower.png`), after the layout check.
  - Stilt houses with tile roofs (the existing `nha-rai-da.glb` is thatched).

### 4.2 W1-3 Old Rootwood (`w1-rootwood`)

- **Story.** Following the banyan's roots into the old rainforest, the heroes reach the hollow tree where Mộc Tinh sleeps. Read its true name aloud and the spirit becomes a tree again.
- **Layout (to re-check).**
  - Two Rifts at the side edges and two separate trails that meet just before the Fort.
  - The Root River divides the map, with three crossings: stepping stones (only Lam can jump them), Tre's bridging point and the Red Bridge.
  - Walkers off the trails move 30 % slower. The Canopy rule: three or more trees near a house cut ranged damage by 40 %.
- **Scale in the 42° frame.** Review (8.8): the strongest idea for this camera. The giant roots cropped by the top edge and the central sinkhole give real depth; **the roots must never hide the trails**.
  - giant aerial roots arch across the top band like the vaults of a hall, cropped by the edge;
  - root walls 2–3 m high snake across the ground, never across a trail and never just south of one, where they would hide it;
  - a 10 m sinkhole with a waterfall pouring into darkness sits at the centre and reads from above;
  - dapple light through the canopy.
  - The banyan's trunk itself is never in frame.
- **Life.**
  - Foes: Oni, Dokkaebi, Ma Da (Water Wraith), Kamaitachi (Tripo originals, rigs needed); Raccoon Dog rigged.
  - Boss: Mộc Tinh tears out of the roots.
  - Heroes: Lam (rigged, shipped); Tre (Tripo original, unrigged).
  - Butterflies and birds removed.
- **Needs.** The existing landmark models `re-vom.glb`, `thac-ho-sut.glb`, `cau-do.glb`, `da-ke.glb` first, relit and checked for scale. Tripo for root arches only if the existing ones fail at real size.

### 4.3 W1-S Goldstair Terraces (side map)

- **Story.** The harvest festival in the terraces above the valley. Golden Hours and runaway Golden Piggies test the economy; no boss.
- **Layout (to re-check).**
  - One Rift on the highest terrace.
  - One stair-road zigzags down four terrace levels (2–3 m drops with retaining walls).
  - Houses on a higher ledge get +10 % range.
- **Scale in the 42° frame.** Review (8.2): beautiful but risky, because gold reflections and the festival can overpower the roads and the word cards. So:
  - The terraces themselves are the giant: flooded paddies stepping toward the camera as muted mirrors, darker than the stair-road, with no gold glint next to a lane or under a card zone. Gold stays the word cards' colour.
  - The festival lives at the frame's edges and in small amber lantern cores, never on the stair-road or around houses.
  - Thin silver falls spill between levels.
  - An ancient aqueduct's arches are cropped by the top edge.
- **Life.**
  - Farmers from `worker-base`.
  - Golden Piggy (`piggy.glb`, flagged cute: rebuild as a gilded bronze piggy spirit, muted gilt that never glows).
  - Water buffalo (`trau.glb`, needs a rig).
  - Cranes removed (no source).
- **Needs.** Retaining walls and paddies from CC0 materials and terrain. Tripo only for the aqueduct piece the frame shows, after the layout check.

### 4.4 W1-N Starsea Rift (bonus, Neon style pack)

- **Story.** The mountaintop where Draconis fell through a tear in the sky; the stolen constellation's name still burns in the crater.
- **Layout (to re-check).**
  - Floating rock islands over a cloud sea, joined by bridges that switch on and off by wave (a lane detours 20 m when one is off).
  - Two Rifts; the Fort island at the south.
- **Scale in the 42° frame.** Review (7.3): the weakest idea, because its premise needs sky and a vertical drop, and light bridges clash with the signal colours. Rework it this way before its layout check:
  - The depth comes from dark voids between the islands and the islands' undersides (hanging rock and roots) seen from above; the cloud sea lies far down and dim. No sky.
  - The bridges keep their on/off rule but use no reserved signal colour (word-card ivory and gold, typed-letter glow, Ghost Flame cyan, the Rift's cold rim): for example stone spans that rise and sink.
  - The Neon material, the star-touched seams and the tear light keep off those signal colours too, and off pink, magenta and purple (1.4).
  - The star-fall from the sky tear shows only as light in the top band; the tear itself stays out of frame.
- **Life.**
  - Foes: the World 1 models with a star-touched glow at their seams.
  - Rift Warden boss: no model yet. Candidates: Space Typing's `warden-*` bosses (inventory §6.3, style change needed).
- **Needs.** CC0 rock and crystal meshes with the Neon material; Tripo only for the crash crater; shaders for the tear light, bridges and cloud sea.

### 4.5 Later worlds (one line each)

- **W2 Amber Dunes:** sandstone canyons seen from above, with a half-buried colossal guardian lying in the sand.
- **W3 Frostsong North:** a frozen lake harbour; the frozen-falls wall is cropped at the top edge, and the ice makes foes slide.
- **W4 Starsea Isles:** floating islands over the cloud sea, reusing the Starsea Rift kit.
- **W5 Emberstone Highlands:** lava channels in terraces that open and close lanes, with a basalt dam glowing through its cracks along the top band.

---

## 5. Why the current maps fail

Only map 1 exists. These reasons would repeat on every later map if the method stayed.

1. **We built from rule rectangles, not from a picture.** Road polylines became masks, the water rectangle a strip, nodes beige disks. No one painted the map as a shot from the game camera, so there was no target.
2. **The field and the camera were never designed together.** The 96 m square field was made for the old square 2D view. At 42° / 46 m the frame sees 64 m of depth, so the Rift and the Fort are both outside it.
3. **The epic was put where the camera cannot look.** The cliff, the Guardian, the far karst and the sky sit beyond the top edge. At 42° the top band shows 0–4 m of height. v1 repeated this mistake with an invented camera; v2 computes the frame first.
4. **The 3D work was ordered so the stage was empty.** Ground, houses and word cards shipped before foes, heroes and trees. The 36 choppable trees, a gameplay object, are still invisible.
5. **The ground, the largest thing on screen, was left at score 3**, with no free CC0 fallback while the painted tiles waited.
6. **No verticals and no edges**, so the light has nothing to act on.
7. **Day and night were the same picture.** `td-units-3d` adds a night light (moon, blue mist, the Fort's lamps), not judged yet.
8. **Water treated as a rectangle.**
9. **Off-direction models** (thatch), now parked until the owner approves the painting (dark fired-tile roofs, 3.6).
10. **We scored ourselves** against our own earlier screens.

**What changes now:**
- the layout is locked in the real frame with the script;
- a base image is captured from the game;
- the concept is painted over it and accepted at 8.5;
- the grey-box is matched to the painting;
- life comes before polish;
- only in-game shots are judged, beside the painting and the reference board.
