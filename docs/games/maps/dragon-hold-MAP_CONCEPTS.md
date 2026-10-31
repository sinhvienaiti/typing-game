# Dragonhold · Map Concepts (draft for review, 01/11/2026)

**What this is.** One concept per map, written before any map is built, for the owner to review and to paste into ChatGPT (normal chat, high reasoning, not the work mode) for critique and a concept painting. A map is built only after its painting is accepted; the build is then judged against that painting, side by side.

**Why.** Owner, 01/11/2026: the maps of all three games are "not acceptable". For Dragonhold the trees, rocks, water and ground look like toys even at Ultra. The bar (AGENTS.md, `ART_DIRECTION_2026-10-28.md` §1.3): commercial fantasy game art, epic, majestic, cinematic light, judged against the owner's reference `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (score 9). Accept at 8. Everything the player reads is English. Nothing the player sees is a code-drawn stand-in; shaders that meet the VFX standard are fine.

**Read for this draft.** `docs/games/dragon-lane/00`, `02` (§1.1, §2.1, §4.3, §6.1), `04` (whole), `05` (§1.2, §2, §3); `ART_DIRECTION_2026-10-28.md` (§1, §3 Dragonhold bible, §5.2, §7); `MAP1_PRODUCTION.md` §1; `PATH_QUALITY.md`; `MODEL_QUALITY.md` §1; `NAMES_EN.md`; tickets 119, 120, 124, 155, 251 and their reports; game source `src/content/data/{stages,maps,waves}.ts`, `src/view/{stage,camera,scatter,paint,water,impostor}.ts`, `src/view/maps/{scene.ts,L2-cau.map.json}`; captures `games/dragon-hold/tmp/diag-0111/` (Ultra, 1920×1080, 01/11, play build and dev).

**What exists today.** One playable map: **Stage 1 · Bridge and Brook** (`m0-l2-cau`, layout `L2-cau`, 10 waves, chapter-2 strength). The campaign in `04-stages-maps-progression.md` plans 520 stages (26 chapters × 20), 8 region kits plus the Black Mist layer and the Mist Rift. No other map is built.

**What this document covers.**
- Section 3: Map 1 as played today (Bridge and Brook), in full.
- Section 4: Chapter 1, all 20 stages, in full.
- Section 5: Chapters 2–26, one paragraph each.
- Section 6: why the current maps fail.
- Section 7: what needs the owner.

---

## 0. How to review a map (paste this block into ChatGPT with each map)

```text
You are an art director for a commercial fantasy strategy game. Review the map concept below for
Dragonhold, a 3D lane-defence typing game seen from a high strategy camera (55 degrees down, no sky).
1. Gameplay: can a new player read the lanes, the enemy gates and the defended Dragon Platform at a
   glance at 1280x720? Does anything tall stand between the camera and a lane?
2. Scale: is there ONE hero landmark at least ten times a soldier's height that makes the player feel
   small, and does it stay out of the play area?
3. Depth and light: foreground frame, playfield, wings, far band; one light direction; a clear
   colour script (pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight).
4. Is it different enough from the other maps of the chapter? Is anything cute, cozy or toy-like?
Give a score out of 10 against games like Kingdom Rush Vengeance, Call of Dragons, Diablo IV and
Warcraft III Reforged, the three biggest problems, and concrete fixes. If you would change the
concept, rewrite the image prompt. Then paint the image from the prompt.
Reject and repaint if: it looks like a miniature, diorama or floating island; the lane is not the
clearest ground; a tall object hides a lane; two landmarks compete for the eye; bright red, orange,
gold or turquoise covers large areas; there is any text, number or interface; the view is not the
high 55-degree game camera.
```

---

## 1. The game camera and what it can show (every map)

Numbers come from the code (`src/view/stage.ts`: perspective camera, 30° vertical field of view; `src/view/camera.ts`: limits; `src/content/data/maps.ts`: L2-cau camera) and from projecting world points onto a 1280×720 frame.

**The default view.**
- Pitch 55°, distance 95 m, 30° vertical field of view; the camera looks 4 m past the platform toward the main gate.
- The camera stands about 78 m up and 55 m back. The player can tilt 40–75°, zoom 0.6–1.3× and rotate freely; the overview is 75° at 1.22×.
- Ground in frame: from about 42 m ahead of the platform (top edge) to about 22 m behind it (bottom edge). Width: ±38 m at the bottom edge, ±56 m at the top edge.
- The 32 m play circle fills the frame. The Dragon Platform sits at screen (640, 412).

**What it can never show.**
- At every allowed tilt the horizon and the sky are out of frame.
- Mountains, sky and the painted backdrop ring (ticket 120) show only on the title camera, the results camera, and as reflections in water.
- So the epic part of every map has to be built inside the roughly 100 × 64 m patch of ground the camera sees.
- Tall things lean outward in this view. On the wings they lean toward the frame edges.
- In the top band anything taller than 6–8 m leaves the frame.
- Drops below ground (gorges, cloud seas) show only toward the camera side: the lower corners and the wings.

**Landmark slots** (world metres: x east, z south, platform at the origin, default yaw 0 = camera looks north):

| Slot | World position | Height budget | Screen at 1280×720 | Use |
|---|---|---|---|---|
| Left wing | x −34…−38, z −14…0 (35–39 m out, outside the 32 m play circle) | 20–24 m whole in frame; taller is cropped on purpose | base ≈ (140, 340) → top ≈ (25, 120) | Hero colossi, carved cliffs, towers |
| Right wing | mirror of the left | same | base ≈ (1135, 320) → top ≈ (1250, 100) | Hero; the debut card (≈ 1030–1280 × 80–195) covers its top for a few seconds |
| Top band | z −30…−42 | 6–8 m | y 0–120 | Enemy gates, arches, muster ground, forest wall |
| Bottom band | z +18…+24 | walls ≤ 10 m; towers ≤ 18 m only at x ≥ ±14 | y 520–720, mostly under the HUD | Foreground frame (ramparts, dark crowns) |
| Lower corners (drops) | x ±36, 40 m down | — | ≈ (256, 643) and (1024, 643) | Cloud seas, gorges; under the HUD panels, mood only |

A 10 m wall at z +20 stays below the south house pads at every tilt (screen y ≥ 517 at 40°), so a rampart there never hides play.

**HUD-safe zones** (from the 01/11 capture, scaled to 1280×720):
- top-left status panel 0–310 × 0–60;
- top-right buttons 1080–1280 × 0–50;
- bottom-left dragon panel 0–350 × 590–720;
- typing bar about 450–830 × 630–705;
- bottom-right carry strip 940–1280 × 640–720.

**Readability rules** (05 §2.2, §3; `PATH_QUALITY.md`; art-pipeline §5):
- Lane core luma ≥ grass + 0.15.
- Ground under the word-tag band ≤ 0.6 luma: no snowfields, pale quarry floors or sunlit water behind tags.
- Red `#FF4A4A`, orange `#FFB020`, gold `#FFC83A` and turquoise `#7FF5E0` are signals: never large fields on the map. The blight's yellow-green `#C8D24A` lives only in foe eyes and cracks.
- Anything between the camera and a lane or a word tag dithers to 35 %.
- Lanes are 24–40 m long; two lanes stay ≥ 8 m apart except where they merge.
- Gates sit inside the default frame. Trap, block and house slots show only once the stage has unlocked them (04 §6.1, 00 §5).
- Scale: characters are drawn 1.4× against the scenery. At 1080p a swarm is ≥ 26 px, a foe 32–44 px and Hỏa Long 80–100 px. A hero landmark is at least ten times a Moss Grunt's height (1.8 m → ≥ 18 m).

---

## 2. The Pass Kit: what every map is built from

### 2.1 Already in the repo

| Piece | Path | State |
|---|---|---|
| Hỏa Long, Inferno form, Bạch Long | `public/assets/dragon-hold/models/heroes/draconis-v2`, `heroes/draconis-v3`, `guides/draconis-v4` | In game |
| Foes of chapters 1–4 | `models/m0b/enemies/{moss-grunt, moss-archer, blight-wolf, tusk-boar, thorn-wasp, thorn-ant}`; general `moss-banner` (Moss Bannerman) | In game (meshes cut by about 58 %, maps stripped: `MODEL_QUALITY.md` §1) |
| Our side | `models/m0b/units/moss-warden` (Grove Warden), `m0b/props/herb-hut`, traps `spikes`, `pine-bomb`, `net-launcher` | In game |
| Six landmark source images (ticket 124) | `art-src/landmarks/{hold-gate, hold-wall, watchtower, dragon-statue, ruined-arch, brazier}.png`; scale sheet `art-src/_review/124-scale.jpg` (gate 16 m, wall 10 m, tower 14 m, statue 12 m, arch 8 m, brazier 3 m) | Images done (self-score M 8–8.5); **Tripo not made yet** |
| Backdrop ring: dawn sky, near, mid and far mountain layers (ticket 120) | `art-src/backdrops/pass-epic/sky-dawn-{a,b,c,d}.png`, `layer-near-{a,b,c,d}.v2(.alpha).png`, `layer-mid.v2`, `layer-mid-2.v2`, `layer-far.v2`, `layer-far-2.v2` | Delivered, not accepted, not wired; title and results camera only |
| Granite road art (ticket 155) | `art-src/ground-v3/road/{road-flagstone, road-verge}.png` and decal sheet | Delivered, awaiting judging |
| Key art, world reference (ticket 119; 251 redo running) | `art-src/ui/title-epic/keyart.png` | Provisional |
| Fire for braziers and beacons | fire C flipbooks and Kenney CC0 particles (`docs/games/THIRD_PARTY.md`) | In game |

### 2.2 New Tripo models (the owner makes them on the Tripo web; Codex draws the source picture first, as in ticket 124)

Order by first use. About 30 credits each, plus retries (`ART_DIRECTION` §7.2).

| ID | Model | Size | First map | Priority |
|---|---|---|---|---|
| T1 | **Dragon Platform**: octagonal granite bastion, 8 m across, 1.2 m high, four dragon-claw corner posts, stairs on three sides, two brazier sockets | 8 × 8 × 1.2 m | every map | P0 |
| T2 | **Old stone arch bridge**: one span about 8 m, deck 3.4 m, parapets 0.9 m, two dragon-head keystones, one cracked parapet | 9 × 4 × 4 m | Map 1 | P0 |
| T3 | **Warden colossus**: the 124 `dragon-statue` made as a half relief growing out of a granite cliff block (or the 124 model scaled 1.8–2× and sunk into a cliff mesh in Blender, if that reads well) | 22–26 m | Map 1, S1 | P0 |
| T4 | Beacon tower with an iron fire basket | 20 m | S5 | P1 |
| T5 | Watermill with a 10 m wheel (wheel as a separate part, so it can turn) | 14 m | S7 | P1 |
| T6 | Dragon pillar (one model, used six times) | 8 m | S8 | P1 |
| T7 | Quarry set: timber crane, cut blocks (3 sizes), a dragon head left half-carved in rock | crane 12 m, head 20 m | S3 | P1 |
| T8 | Blight ant mound (violet-grey crust, glowing cracks) | 4–6 m | S4 | P1 |
| T9 | Fallen giant pine with an upright root plate | trunk 60 m, plate 12 m | S4 | P1 |
| T10 | Blighted wasp hive under an overhang | 12 m | S12 | P2 |
| T11 | Signal mast with a net winch | 20 m | S13 | P2 |
| T12 | Dam with three dragon-head spillways (one segment, repeated) | 14 m | S14 | P2 |
| T13 | Low five-arch causeway bridge | 30 × 4 m | S14 | P2 |
| T14 | Elder Bones: dragon skull, rib arch, vertebra stone | skull 10 m, rib 15 m | S15 | P2 |
| T15 | Aqueduct span (whole and broken) | 18 m | S16 | P2 |
| T16 | Granary (round, slate cone roof) and the Hold's inner keep | 9 m, 30 m | S17 | P2 |
| T17 | Palisade of whole pine trunks: straight, gate, broken | 8 m | S19, S20 | P2 |

Garrison and workers on the maps reuse the Grove Warden model: the Hold is kept by the moss folk who fight on our side, so no new character model is needed in chapter 1.

### 2.3 Free, commercial-safe packs (kinds only; the asset researcher picks names)

**Licence rule.**
- Allowed: CC0 first; then MIT, BSD or Apache; CC-BY only with a credit line in `docs/games/THIRD_PARTY.md`.
- Never: non-commercial (NC), no-derivatives (ND), editorial or personal-use terms, engine-locked marketplace licences, or any licence that forbids shipping the raw files. A web build exposes every texture and model to the public.

| ID | Kind | Use |
|---|---|---|
| P1 | PBR texture sets (albedo, normal, roughness, AO; 2K): granite cliff with lichen, granite slabs, forest floor with pine needles, alpine meadow, river gravel and wet stones, mud, moss, snow, travertine, ash and charcoal | Terrain and cliffs, regraded to the bible palette |
| P2 | Stylized-realistic conifers (pine, spruce, larch) with LODs and alpha needle cards; ferns, grass tufts, alpine shrubs, rock and boulder scans | Forest walls, groves, edges (replaces the round-crown props) |
| P3 | HDRI skies (dawn, overcast, dusk) | Lighting and reflections only, never shown |
| P4 | Animated birds (crow, raven, hawk, eagle, heron), deer, fish | Ambient life |
| P5 | Particle textures (spray, steam, dust, embers, leaves) | Waterfalls, mist, embers; Kenney CC0 is already in use |
| P6 | Shader code under MIT (three.js examples and similar): flow-map water, light shafts, height fog, instanced grass, wind | Systems in 2.4 |
| P7 | Ambience recordings (river, waterfall, wind in pines, birds) | Map ambience, through `AUDIO_PIPELINE.md` |

### 2.4 Systems Claude builds (shaders and code, no drawn stand-ins)

- **Scenery materials.** Move scenery from `MeshLambertMaterial` with a 3-step ramp (`scatter.ts`, `terrain.ts paintMaterial`) to physically based materials with normal, roughness and AO maps. Keep the painterly feel in the grade, not in the shading.
- **Grade.** A filmic tone map plus one colour lookup per map and hour (dawn, noon, golden, dusk, blue hour). Bloom only on fire and magic.
- **Terrain.** Real cliffs from the height field with triplanar granite (P1), up to 30 m. Retire the "cliff blocks widened into a face".
- **Water.**
  - Rivers: flow-map shader with depth colour, foam from speed, rocks and piers, and rapids on drops.
  - Waterfalls: mesh with scrolling foam, spray particles and mist cards.
  - Sky colour and the sun reflected in the water.
- **Atmosphere.** Height fog pooled in river beds and hollows; light shafts at dawn and dusk; cloud shadows crossing the map every 10–15 s.
- **Wind.** One wind field for pines, grass, banners (cloth vertex shader) and pennants.
- **Grass.** 40–60 k instanced tufts with P1/P2 textures, kept 1.5 m off lanes and slots.
- **Blight.** An animated violet creep at the gates, Black Mist volumes, and grass that withers along the lane after a wave passes.
- **Muster ground (view only).** During the build phase and the wave card, the next wave stands at its gate: idle foes in the forest shade, with eyes glowing. They step onto the lane when the sim spawns them. The sim never reads it, and the golden hashes stay the same.
- **Snow and ice shader** (S18, C17). Occluder dither already exists as a rule (05 §3).

### 2.5 Retire from the new maps (the files stay; the owner decides on old models, see section 7)

- `props/pine-river-pine-round` (round lollipop crowns).
- `tree-violet` near lanes.
- `bush-blossom`.
- The "warm crowns" rule (red to rust crowns, up to six, `scatter.ts` V7).
- `kit3` `cliff-rock-a/b` as cliff builders.
- `wooden-jetty`, `rail-fence` and `lantern-post` as park furniture.
- `bridge-old` (plank footbridge).
- The pond with lily pads.
- The pilot meadow palette `PILOT_GROUND` (`paint.ts`: bright meadow green `#6b9e49`, sand dirt `#c9a77c`).
- Placeholder stepping stones in `water.ts`.

---

## 3. Map 1 (playable today) · Bridge and Brook · `L2-cau`

**Name and story beat.** *Bridge and Brook.* The blight comes down the valley to the Hold's north face; Hỏa Long holds the river crossings below the West Warden, the stone dragon that has watched this pass for a thousand years.

### 3.1 Gameplay layout (sim unchanged: lanes, slots, river path and golden hashes stay as they are)

- **Defended point:** the Dragon Platform at (0, 0), radius 4 m.
  - Hỏa Long hovers 2.5 m above it.
  - Bạch Long stands at the south-west edge (−2.6, 2.0).
  - The word zone is the 26 m ring.
- **Bridge Lane** (main lane in waves 1–3 and 7–8).
  - Starts at the north gate (8.5, −29) and runs 3 m wide down to the platform's north stair.
  - Crosses the river on the bridge, 10.5–18.4 m along the lane, deck 3.4 m: the choke point.
  - Four trap slots, one of them on the deck; two block points.
- **Brook Lane** (main lane in waves 4–6 and 9–10).
  - Starts at the west gate (−30, 7) and runs 2.6 m wide.
  - Wades the stream at the ford, 6.9–14 m along the lane: 30 % slower, Wet for 4 s.
  - Three trap slots, none in the ford; two block points.
- **Sky Lane.** Starts at (30.5, −8.5) at 3 m altitude and comes in over the east meadow. Thorn Wasps.
- **River.**
  - Enters from the north-east 8 m wide and crosses the upper third at z ≈ −15.
  - Bends south-west past the ford and leaves the lower-left as a 4 m stream.
- **House pads:** four on the inner ring (NW, NE, SE, SW at 7–9 m) and two outer pads by the crossings (9.5, −11) and (−14, 6.5).

**Camera:** yaw 0, pitch 55°, 95 m, look (0, −4). Unchanged.

**Screen positions at 1280×720:**

| Feature | Screen (x, y) |
|---|---|
| Platform | (640, 412) |
| Bridge | (664, 256) |
| North gate | (744, 114) |
| Ford | (349, 431) |
| West gate | (188, 501) |
| Sky Lane entry | (1069, 289) |
| Stream exit | (164, 613) |

Both gates and both crossings sit in the clear middle of the HUD.

```text
 top of screen = north                                       x −48 ............ +48
 z −42  AAAAAAAAAAAAAAAAAAAAAAA ::[N]:: AAAAAAAAAAAAAAAAA  ≈≈≈ AAAA   [N] north gate under the ruined arch
 z −34  ^^^^AAAAAAAAAAAAAAAAAA    ║     AAAAAAAAAAA   ≈≈≈≈≈ cascade (two drops)
 z −26  ^^^^^AA              T    ║                ≈≈≈≈≈
 z −18  ^^^^^^         ≈≈≈≈≈≈≈≈≈[B=B]≈≈≈≈≈≈≈≈≈≈≈             * blighted snag (wasps)
 z −10  ^^WW^^     ≈≈≈≈     H T   ║   H   H                <······ Sky Lane
 z  −2  ^^WW^^   ≈≈              ║
 z  +6  ^^[W]=T==≈ford≈==T==W=( D )   H                       D  Dragon Platform
 z +12  ^^^^     ≈≈≈        H           H                       WW the West Warden (colossus)
 z +18  ^^^     ≈≈                                              ^  granite wall 25–30 m
 z +24  ##[TT]######### [ HOLD GATEHOUSE ] ##########[TT]##     #  the Hold's north rampart (under the HUD)
 legend: ║ = Bridge Lane, = Brook Lane, T trap slot, W block point, H house pad, ≈ water, A pines
```

### 3.2 Hero landmark: the West Warden

- **What it is.** A 22 m dragon colossus carved out of the west granite wall. It crouches with its wings folded and its head turned east down the valley. Its forefoot grips the cleft the Brook Lane comes out of. Its two eyes are iron fire basins, dark until the map is won.
- **Where it sits.** At (−37, −7), outside the 32 m play circle. On screen it rises from about (135, 330) to its head at about (20, 110).
  - Left wing, above the west gate (188, 501) and below the status panel.
  - It is lit gold by the dawn sun and leans outward, away from the play.
  - At 40° tilt the head stays in frame; zoomed in, it leaves the frame on purpose.
- **Supporting pieces (they frame the hero, they do not compete with it):**
  - **The Hold's north rampart** across the bottom edge at z +20…+24: six 12 m wall segments up to 10 m high, the gatehouse (16 m) at (0, +22) with its gate open, and a granite road up to the platform's south stair. Two watchtowers (14 m) at (±24, +20) show beside the HUD panels at about (200, 590) and (1080, 590). The rest sits under the HUD.
  - **The cascade**: the river drops twice (3 m and 2 m) at (36…46, −24…−28) in the top-right, (1090–1200, 95–160): white water that moves in the corner of the eye.
  - **The north gate**: the 8 m ruined arch at (9, −31), top at (749, 21). The blight pours out under it.

### 3.3 Depth layers, light, colour

| Layer | Content |
|---|---|
| Foreground frame (bottom band, mostly under the HUD) | Rampart battlements, two watchtowers, four braziers, eight banners. Dark pine crowns beyond the wall ends. Shadow side, 25–35 % darker than the playfield |
| Playfield (≤ 32 m) | Olive meadow with gold sun patches; granite outcrops. The river in a real bed (gravel bars, boulders, foam at the bridge). Bridge Lane in worn granite flags with gravel shoulders. Brook Lane in packed earth with a stone edge and wheel ruts. Roadside stones, tufts and puddles every 2–6 m |
| Wings (32–45 m) | West: the 25–30 m granite wall, three ledges, the Warden, two scree fans. East: a forested ridge with the cascade and a blighted dead pine where the wasps nest |
| Far band (top, z −32…−42) | The dark pine forest wall climbing north. Violet Black Mist pooling at both gates. The muster ground |
| Sky | Never in frame at 55°. It is present as river reflections (dawn gold to cool blue), cloud shadows every 10–15 s, and light shafts through the river mist. The title and results cameras show the 120 backdrop ring; its painted gate must face south, where the 3D Hold stands, or be painted out |

- **Time:** dawn.
- **Sun:** bearing 70° (east-north-east), elevation 24°.
  - Long shadows fall west-south-west across the meadow.
  - The Warden's east face takes the warm light; it is the largest lit mass but stays under 0.75 luma.
  - The brightest points are the dragon's fire and the braziers.
- **Weather:** clear with a light breeze. Mist lies 0–3 m deep in the river bed. Spray hangs at the cascade.
- **Colour script.**
  - Shadows: deep pine green and slate blue.
  - Light: dawn gold on granite and grass tips.
  - Granite: cream. River: slate-teal with white foam (not turquoise).
  - Blight: muted violet at the gates only.
  - Ember orange only on braziers and the dragon.

### 3.4 Set dressing

- **Conifers.**
  - 160–220 tall pines and spruces, 14–24 m, in the forest walls (north, the north-east ridge, beyond the rampart ends).
  - Three inner stands of 6–9 pines: the north-west wedge across the river, by the south-east pad, and south of the ford.
  - 40 young pines, 4–8 m, at the margins.
  - No round broadleaf crowns, no red crowns.
- **Granite.**
  - The west wall: 25–30 m high, about 60 m long, three ledges, lichen and moss streaks, dark crevices.
  - 2 scree fans.
  - 14 boulders, 2–5 m, along the river.
  - 30–40 river stones.
  - 6 flat outcrops, 4–8 m, on the meadow, 3 m or more from the lanes.
- **River.**
  - 6–8 m channel, 1.2 m deep.
  - Rapids over two ledges, 2 boulder islands.
  - Gravel bars on the inside of bends, foam lines at the bridge piers.
- **Bridge (T2).** Single stone arch spanning about 8 m. Moss on the keystones, one cracked parapet stone.
- **Ford.** 9 flat stepping stones beside a sunken causeway visible under 20 cm of water; 2 broken causeway posts with iron rings.
- **Dragon Platform (T1).** Octagonal, two lit braziers, stairs north, west and south.
- **The Hold.**
  - 6 wall segments, 1 gatehouse, 2 watchtowers.
  - 4 braziers on the wall walk.
  - 8 hanging banners: ember cloth, dark iron dragon sigil, no letters.
- **Ground cover.** 40–60 k grass tufts on the meadow; 300 ferns at the forest edges; moss on north faces.
- **Blight.**
  - Animated violet creep 8–10 m deep at both gates.
  - 3 dead blighted pines at each gate.
  - Withered grass along a lane after a wave.

### 3.5 Life on the map

- **Hỏa Long** idles on the platform and turns toward the next gate when the wave card shows. **Bạch Long** waits at the south-west edge.
- **Foes from the start of a wave.** The muster ground shows the next wave's first groups:
  - in the forest shade behind the north gate, about (780, 40);
  - in the west cleft, about (30, 528).
  - Grunts thump their weapons, wolves pace and eyes glow `#C8D24A`.
  - In waves 5 and 10 the Moss Bannerman's banner rises above the tree line before he steps out.
- **Wasps** circle the blighted snag on the east ridge from wave 2.
- **Defenders.**
  - 6–10 Grove Wardens stand on the rampart.
  - The braziers flare and a horn sounds from the gatehouse when a wave starts.
  - On victory the Warden's eye basins ignite and stay lit for the results camera.
- **Ambient.**
  - Two crows circle the Warden's head; a hawk rides the updraft over the cliff.
  - Mist drifts down the river; spray at the cascade.
  - Pines, grass and banners move in one wind; cloud shadows pass.
  - Embers rise from the braziers.

### 3.6 Where every piece comes from

| Source | Pieces |
|---|---|
| Repo | Dragons, foes, Grove Warden, traps, Herb Hut (2.1); `hold-wall`, `hold-gate`, `watchtower`, `ruined-arch`, `brazier` images (124) → Tripo; road art (155) for the Bridge Lane core and verge; fire C for braziers |
| Tripo (owner) | T1 Dragon Platform, T2 stone arch bridge, T3 Warden colossus |
| Free packs | P1 granite cliff, forest floor, meadow, river gravel; P2 conifers, ferns, tufts, boulders; P3 dawn HDRI for lighting; P4 crows and a hawk; P5 spray and embers; P7 river and wind ambience |
| Shaders | Flow-map river, cascade and foam; height fog and light shafts; cloud shadows; wind; blight creep; muster crowd; physically based scenery materials and the dawn grade |

### 3.7 What is wrong with today's version (Ultra, 1920×1080, 01/11, `tmp/diag-0111/`)

1. **It is a park, not a mountain pass.** Football-pitch green meadow, beige sand paths, a round pond with lily pads, a jetty, lantern posts and rail fences. Nothing says "Hold", "dragon" or "pass". The independent score of the A2 layout was 6–6.5 on the market scale (`ART_DIRECTION` §5.2); the map pilot's 7.125 was on our own scale.
2. **The shipped build has no ground textures.** The play build loads none (`"ground": []` in `numbers.json`), because `paint.ts` loads the ground tiles and decals from `/art-src` in dev only (`buildGroundPaint`, "MF-C24 not done"). Players see a flat procedural green.
3. **Toy materials by construction.**
   - Scenery props use `MeshLambertMaterial` with a 3-step ramp; rocks are flat-shaded and crowns get sphere normals (`scatter.ts` 416–419, 561).
   - The tree and rock models lost 84–91 % of their triangles and all their normal and roughness maps in processing (`MODEL_QUALITY.md` §1).
   - Result: vinyl toys, whatever the quality tier.
4. **No landmark, no scale.**
   - The tallest scenery is the 9 m west cliff and 7.8 m south-west cliff, built from widened `cliff-rock` blocks. They read as white sugar cubes.
   - Nothing on the map is ten times a soldier, and the dragon is a red smear.
   - The six landmarks of ticket 124 have never been built in 3D.
5. **Wrong colour script.**
   - Saturated green grass and a bright blue river.
   - Up to six red-to-rust "warm crowns" placed by rule, which breaks the bible's ban on red and orange fields.
   - A violet ground bounce in the light.
   - None of the bible's pine green, slate blue, cream granite and dawn gold.
6. **Flat light.**
   - Sun from the east at 50° elevation (`L2-cau.map.json`), so the shadows are short.
   - Hemisphere fill at 2.7 flattens every form.
   - Mist only from 47 m.
   - No light shafts, no cloud shadows; the scene background is a mist colour. The bible asks for a low dawn sun, 25–35°, raking along the valley.
7. **The water is a canal.**
   - A ribbon of uniform blue with cartoon specks and "stepped sparkles".
   - No depth colour, no rapids, no rocks in the stream, no foam at the bridge.
   - The ford's stepping stones are placeholders (`water.ts`).
   - The bible's "fast mountain river" reads as a garden ditch.
8. **The choke point has no presence.** The bridge is a small plank footbridge with rail fences. The bible and the key art call for an old stone bridge.
9. **Paths are smears.** Even-width sand ribbons with soft edges and the same colour as the dirt rings around every grove (the "finger smear" `PATH_QUALITY.md` bans). Footpaths lead to a pond and a scree for no reason.
10. **The map is empty between waves.** No garrison, no muster, no birds, no banners, no smoke. Foes appear at the lane end with nothing before them.

### 3.8 ChatGPT image prompt

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A mountain valley at dawn: a fast river with white rapids crosses the upper third under an old single-arch stone bridge, then bends down the left past a ford of stepping stones. A granite-flagstone road over the bridge and an earth track through the ford lead to an octagonal granite platform in the centre, where a large red-orange fire dragon hovers. Small moss creatures and grey wolves with violet rags walk both roads out of a dark pine forest edged with violet mist. On the left, a colossal dragon statue carved into a granite cliff, ten times their height, crouches over the ford in low sun. Fortress battlements with braziers along the bottom edge. Long shadows, river mist. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

---

## 4. Chapter 1 · The Hold Awakens (stages 1–20, Pine River kit, spring)

**Arc.** The Black Mist rises in the high forest. Blighted moss folk, ants and wasps come down on the Hold. The old wardens built **Dragon Platforms** all around the pass; each holds the blight back while its fire burns. Hỏa Long relights them one by one:
- first at the Hold's own gate and fields;
- then up the valley;
- then onto the high ground, where Bạch Long joins him;
- and finally to the den of the Tuskfather, the blighted boar lord at the head of the valley.

Every won stage lights its platform on the Journey screen. The chapter is built from one kit (2.1–2.4); each stage gets its own hero composition.

**Chapter-wide rules.**
- One lane in every stage (04 §3.2). A sky lane is added from S12.
- Spring: fresh olive and pine greens, snowmelt, small white and pale-yellow flowers away from the lanes; no candy colours.
- Light moves through the chapter: dawn → morning → noon → golden hour → dusk → blue hour. There is no full night (night is a later variant).
- Teaching and unlocks come from 04 §6.1. A system that is not open has no slot on the map: trap slots appear from S2, block points from S6, house pads from S16.

| # | Name | Site | Layout | Teaches (04 §6.1) | Hero landmark | Light |
|---|---|---|---|---|---|---|
| 1 | First Fire | The Hold's east gate | L1-thang | Type → fire; Moss Grunt | The Hold's East Gate (left wing) | Dawn |
| 2 | The Spike Line | The Hold's terrace fields | L1-s | Build, Spikes | The Broken Tower (right) | Morning haze |
| 3 | Breath of Fire | The old quarry | L1-thang | Fire Breath | The Unfinished Warden (left) | Noon, broken cloud |
| 4 | The Ant Hills | A burned logging slope | L1-s | Thorn Ant swarms | The Fallen King pine (right) | Golden morning |
| 5 | The Bannerman | Signal Hill | L1-thang | General, aura, Seal Break | The Beacon of the Pass (left) | Late afternoon |
| 6 | Wardens of the Grove | The Elder Grove | L1-s | Grove Warden | The Elder Pine (right) | Morning shafts |
| 7 | The Mill Race | The Hold's mill | L1-thang | Small Potion | The Great Mill (right) | Misty morning |
| 8 | Horns at Noon | The Long Stair | L1-s | Call waves early | The Long Stair (left) | Noon |
| 9 | The Warm Springs | Hot spring terraces | L1-thang (short) | Review stage | The Steam Falls (top right) | Soft morning |
| 10 | The Captain's Gate | The old outer wall | L1-s | Mini-boss captain | The Broken Gate (right) | Dusk |
| 11 | Two Dragons | The White Eyrie | L1-xoan | Bạch Long, Feather Shield | The Eyrie Needle (left) | Dawn over a cloud sea |
| 12 | Wings over the Pass | The Hive Cliff | L1-thang + sky | Thorn Wasp | The Hive (right) | Windy morning |
| 13 | Nets and Wind | The Windgap | L1-s + sky | Net Launcher | The Windgap Mast (left) | Breaking overcast |
| 14 | The Flood Bridge | Below the Upper Dam | L1 with bridge and ford | Pine Bomb; bridge and stream; flood | The Upper Dam (right) | Bright morning, spray |
| 15 | Dragon's Rage | The Elder Bones | L1-thang | Dragon Rage, Inferno | The Elder Bones (left) | Afternoon gold |
| 16 | The Herb Terraces | Healers' terraces | L1-s | Herb Hut | The Aqueduct (right) | Morning |
| 17 | Hold the Granary | The Hold's bailey | L1-thang | Dragon Heart, Hard Scale; Granary objective | The Inner Keep (left) and the granary | Harvest gold |
| 18 | The Roar | The Echo Cirque | L1-s | Urgent word, Dragon Roar | The Hanging Glacier (left, top) | Cold bright morning |
| 19 | Campfire | The last camp | L1-thang (short) | Review; boss preview | The Tusk Wall (top band) | Blue hour, campfire |
| 20 | Tuskfather | The Den | L1-thang (long charges) | Boss B01 | The broken Tusk Wall and the lair mound | Violet haze → sunburst |

The prompts below share one opening and one closing so that the paintings match. The middle of each prompt is the map.

### 4.1 Stage 1 · First Fire

- **Story beat.** The first blighted scouts come down the valley road to the Hold's east gate; Hỏa Long wakes on the gate platform and learns that a true name, typed, becomes fire.
- **Teaches.** Typing a word makes Hỏa Long attack; the learning frame; Moss Grunt. Hand-built stage. No slots.
- **Gameplay layout.**
  - Gate in the north-east forest at (20, −24), screen (891, 159).
  - One straight lane (`L1-thang`), 3 m wide and 27 m long, across a meadow to the platform's north-east stair.
  - The platform stands on the paved forecourt in front of the Hold's gate.
- **Camera.** Yaw 0, pitch 55°, look (+3, −4). The lane runs from the upper right toward the centre; the left third holds the Hold.

```text
 z −42  ^^^^##AAAAAAAAAAAAAAAAAAAAAAAAAAAA[G]AAAAAAAA     [G] gate in the forest, violet mist
 z −30  ^^[TW]AA                         //               TW watchtower at the wall's north end
 z −18  ^^##                         //
 z  −6  ^^##   :::::::::::        //                      ::: granite forecourt road
 z   0  ^[GATE]::::::::::::::( D )                        [GATE] the Hold's East Gate, facing east
 z  +8  ^^##        AA   AA                               ## the Hold's wall running north–south
 z +16  ^^[WG]≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈            [WG] water gate: the river flows under the wall
```

- **Hero landmark: the Hold's East Gate.**
  - The gatehouse (124 `hold-gate`, 16 m) stands at (−35, 0), facing east, with its portcullis half raised.
  - Wall segments (124 `hold-wall`) run north and south along x ≈ −36. A watchtower (14 m) closes the north end at (−36, −26).
  - On screen it fills the left wing from about (135, 412) up to (53, 267), with the wall running up to the top-left.
  - It stays more than 30 m from the lane.
  - A ceremonial granite road, 8 m wide, runs from the gate to the platform. Foes never use it.
- **Depth, light, colour.**
  - Foreground: the river along the bottom edge, entering the water gate under the wall; dark pines at the lower right.
  - Playfield: meadow and forecourt.
  - Wings: the Hold (left), the forest slope (right).
  - Far band: the forest wall and the gate's violet mist.
  - Dawn, sun at bearing 75°, elevation 20°: the gate's east face is gold, pine shadows stripe the lane, mist lies on the river.
- **Set dressing.**
  - 120 pines, 14–22 m, in the north and north-east forest; 20 young pines.
  - 2 meadow outcrops, 8 boulders on the river bank, 2 gravel bars.
  - The Hold: 1 gatehouse, 4 wall segments, 1 watchtower, 6 braziers, 6 banners.
  - Forecourt: 2 granite milestones, a horse trough, 3 crates.
  - 30 k grass tufts.
- **Life.**
  - Grunts muster 4–6 at a time in the forest shade at the gate.
  - Grove Wardens stand on the wall; chimney smoke drifts in from behind the wall at the left edge.
  - A hawk; banners in the wind.
  - On victory, the gate's braziers flare.
- **Sources.**
  - Repo: 124 `hold-gate`, `hold-wall`, `watchtower`, `brazier` (via Tripo); Moss Grunt; Grove Warden.
  - Tripo: T1.
  - Packs: P1, P2, P4, P5.
  - Shaders: river, height fog, wind, muster.
- **Today.** No map exists. Built with today's kit, it would be the Map 1 park with a gate model dropped on bright grass.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. Dawn at the east gate of an ancient granite fortress: the gatehouse and its curtain wall run along the left side of the frame, half-raised portcullis, braziers and ember banners, a watchtower at the top-left. A wide granite road runs from the gate to an octagonal granite platform in the centre, where a large red-orange fire dragon hovers. One worn earth lane comes out of a dark pine forest at the upper right, edged with violet mist, and small moss creatures with violet rags walk it toward the dragon. A river runs along the bottom edge into a water gate under the wall. Low gold sun from the right, long pine shadows across the lane, mist on the water. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.2 Stage 2 · The Spike Line

- **Story beat.** The Hold's terrace fields lie empty; the farmers fled behind the walls. Hỏa Long sets the first spikes where the field track bends.
- **Teaches.** Placing traps; Spikes. Four trap slots, at the two bends and the two straights.
- **Gameplay layout.**
  - Gate at the top centre (0, −31), screen (640, 96).
  - An S-lane (`L1-s`), 38 m long, bends right at (8, −22) and left at (−7, −12) between drystone field walls, then reaches the platform's north stair.
  - The field walls (0.8–1.2 m) stay 2.5 m or more from the lane.
- **Camera.** Yaw 0, pitch 55°, look (0, −4).

```text
 z −42  AAAAAAAAAAAAAAAAAAAA[G]AAAAAAAAAAAAAAAAAAAAA
 z −30  ===== field wall ===  ╲   ===== field wall =====       ╲ ╱ the S-lane
 z −22  barley        T        ╲T         barley     ^^[BT]^   [BT] the Broken Tower on its knoll
 z −14  ===== field wall ===  ╱             ▪ ▪ ▪  ^^^^         ▪ fallen tower stones
 z  −6  barley      T╱  T                              ^^^
 z   0  ===== field wall ==( D )===== field wall =====
```

- **Hero landmark: the Broken Tower.**
  - The 124 `watchtower` scaled 1.6× (22 m) on a granite knoll at the right wing (36, −8).
  - Its top third has fallen. A line of 3–4 m stones runs from its foot into the field, stopping 2.5 m short of the lane.
  - Screen: from (1135, 330) up to about (1250, 110).
- **Depth, light, colour.**
  - Foreground: a field wall and an overturned cart at the bottom edge.
  - Playfield: terraces of young barley (olive to pale gold) cut by grey walls.
  - Wings: the knoll and tower (right); a hedge of pines and a scree (left).
  - Far band: forest wall with mist at the gate.
  - Morning at 9 am, sun at bearing 110°, elevation 28°; light haze; cloud shadows cross the terraces.
- **Set dressing.**
  - 9 terrace walls, 20–40 m long.
  - 2 overturned carts, 3 abandoned ploughs, 1 stone field barn with a slate roof (no thatch).
  - 4 granite boundary stones.
  - 70 pines.
  - Barley as instanced cards (25 k).
- **Life.**
  - Crows rise from the furrows when foes pass.
  - A fox crosses the field before wave 1.
  - The Hold's horn sounds far off; grunts muster at the gate.
- **Sources.**
  - Repo: 124 `watchtower`; Spikes.
  - Tripo: T1, plus a drystone wall segment (or a P2 pack wall if one fits).
  - Packs: P1 soil, P2, P4.
  - Shaders: wind on the barley, cloud shadows, muster.
- **Today.** No map. Risk with today's kit: green carpet with beige S-smear and round trees.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. Abandoned terraced fields below a mountain fortress on a hazy spring morning: young barley in olive and pale gold, long grey drystone walls, an overturned cart. One earth lane snakes in an S from a dark pine forest at the top, with violet mist at its edge, down to an octagonal granite platform where a large red-orange fire dragon hovers. Small moss creatures with violet rags walk the lane; iron spike traps wait at its bends. On the right, a colossal ruined stone watchtower on a granite knoll, its fallen top lying across the field in huge blocks. Crows rising, cloud shadows on the terraces. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.3 Stage 3 · Breath of Fire

- **Story beat.** The blight takes the old quarry where the wardens once carved their dragons. Hỏa Long learns to breathe a cone of fire down its cut channel.
- **Teaches.** Fire Breath (Alt + 1, skill word); the Claw slot. Four trap slots.
- **Gameplay layout.**
  - Gate north-west (−18, −26), screen (416, 140).
  - A straight lane (`L1-thang`), 30 m long, in a cut channel 6 m wide between walls of cut blocks, so the Fire Breath cone fills the channel and reads clearly.
  - The channel opens onto the platform's ledge.
- **Camera.** Yaw 0, pitch 55°, look (−3, −4).

```text
 z −42  ^^^AA[G]AAAAAAAAAAAAAAA^^^^^^^^^^^^^^^^^^^^^^^^      quarry rim with pines
 z −30  ^HEAD ▓▓╲▓▓      ▓▓ blocks ▓▓          crane ┼        ▓ cut blocks 2–5 m
 z −20  ^HEAD^  ▓╲▓T  ▓▓▓      ▓▓              ┼            HEAD the Unfinished Warden
 z −10  ^^^^^    ▓╲▓ T   ▓▓          spoil                      in the west face
 z   0  ^^^^^      ( D )   ▓▓ ▓▓  heap
```

- **Hero landmark: the Unfinished Warden.**
  - A 20 m dragon head and shoulders, half carved out of the quarry's west face at (−36, −14), on the left wing.
  - One eye finished, the jaw still rough block. Timber scaffolding climbs its cheek.
  - A 12 m timber crane with a hanging block stands on the rim at the top right.
- **Depth, light, colour.**
  - Foreground: spoil heap and a sledge.
  - Playfield: a dark crushed-granite floor (luma ≤ 0.6 under the tags); pale cut faces only on the walls.
  - Wings: the carved face (left), the crane and block stacks (right).
  - Far band: pines on the quarry rim.
  - Noon, sun at bearing 160°, elevation 55°; broken cloud gives moving sun and shade; dust motes hang in the light.
- **Set dressing.** 24 cut blocks, 2–5 m; 3 block stacks; 2 sledges; ropes and pulleys; 1 crane; 1 scaffold; 2 spoil heaps; 40 pines on the rim; dust decals.
- **Life.**
  - Dust trickles from the face when Fire Breath hits.
  - The rope and block sway in the wind; swifts nest in the face.
  - Grunts muster among the blocks at the gate.
- **Sources.**
  - Tripo: T7 (crane, blocks, head), T1.
  - Packs: P1 granite and gravel, P2 rim pines, P5 dust.
  - Shaders: grade, light, wind on ropes.
- **Today.** No map. Risk: pale stone floor behind white word tags (luma rule), and toy flat-shaded blocks.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. An ancient granite quarry at noon under broken clouds: a straight lane of dark crushed stone runs from the upper left through a channel between huge cut blocks to an octagonal granite platform where a large red-orange fire dragon breathes a cone of flame down the channel at small moss creatures with violet rags. On the left, the quarry wall holds a colossal dragon head half carved from the rock, one eye finished, timber scaffolding on its cheek. A tall timber crane with a hanging block on the right rim, pines along the rim, dust in the sunlight. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.4 Stage 4 · The Ant Hills

- **Story beat.** On the burned logging slope the blight has raised ant mounds that boil with thorn ants; one word burns a whole swarm.
- **Teaches.** Swarm clusters (one word for the cluster). Four trap slots.
- **Gameplay layout.**
  - Gate at the top band (22, −31), where three blight ant mounds sit at (18…30, −32…−38).
  - An S-lane, 36 m long, comes down the burned slope to the platform.
  - A ravine runs north–south on the right side, outside the play circle.
- **Camera.** Yaw 0, pitch 55°, look (+2, −4).

```text
 z −42  ‡‡‡ snags ‡‡‡   AAAA   (M)(M)[G](M)  ‡‡‡  ‖ravine‖    (M) blight ant mound 4–6 m
 z −30   ‡    ‡           T  ╱╱              ‖      ‖        ‡  charred snag
 z −18     stumps     ╱╱  T            ROOT▐‖      ‖        ROOT the Fallen King's root plate
 z  −8   ‡      T ╲╲             ════trunk═════════‖══▶      trunk crosses the ravine
 z   0          T  ( D )      ferns
```

- **Hero landmark: the Fallen King.**
  - A giant pine, 60 m long and 4 m thick, has fallen across the ravine.
  - Its root plate stands 12 m tall at (34, −8) on the right wing; the trunk runs off the right edge over the ravine and its broken crown is lost in the far forest.
  - Screen: root plate from (1120, 330) to about (1200, 200). The lane passes 6 m from the root plate.
- **Depth, light, colour.**
  - Foreground: charred stumps and bracken at the bottom edge.
  - Playfield: black-and-ochre burned ground healing with fresh green bracken.
  - Wings: dead snags (left); the root plate and ravine (right).
  - Far band: the mounds glowing violet-grey and the forest wall.
  - Golden morning, sun at bearing 120°, elevation 25°: the trunk's long shadow crosses the slope.
- **Set dressing.** 40 charred stumps; 25 black snags, 8–14 m; 60 young pines, 2–4 m; 300 bracken ferns; ash decals; 3 mounds; a ravine 12 m deep with a white stream at its bottom (seen at the right edge).
- **Life.**
  - Ant clusters pour from the mounds.
  - Ash drifts; a woodpecker drums (sound); the mounds pulse.
- **Sources.**
  - Tripo: T8 mounds, T9 fallen pine, T1.
  - Repo: Thorn Ant.
  - Packs: P1 ash and soil, P2 snags (or new Tripo), P5 ash.
  - Shaders: blight pulse, wind.
- **Today.** No map. Risk: ants (26 px) lost on busy black ground. Keep the lane core one step brighter than the ash.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A burned logging slope in golden morning light: charred stumps, black dead pines, fresh green bracken. At the top, three large blighted ant mounds with violet-grey crusts and glowing cracks pour swarms of small thorn ants down one winding earth lane to an octagonal granite platform where a large red-orange fire dragon hovers. On the right, a colossal fallen pine lies across a deep ravine, its upright root plate taller than a house, its long shadow across the slope. Ash drifting in the light. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.5 Stage 5 · The Bannerman

- **Story beat.** A Moss Bannerman climbs Signal Hill to plant the blight's banners under the cold beacon; when he falls, the beacon of the pass burns again.
- **Teaches.** General stage: Moss Bannerman, aura, Seal Break. Four trap slots.
- **Gameplay layout.**
  - Gate at the top (−4, −31).
  - A straight lane, 28 m long, up the granite dome to the platform on its crown.
  - The Bannerman plants banners on the lane's verge (G01).
- **Camera.** Yaw 0, pitch 55°, look (−1, −4).

```text
 z −42  AAAAAAAAAAAAAAAA[G]AAAAAAAAAAAAAAAAAAAA
 z −30  ^^^ heather       ║  T        heather   boulders
 z −18  [BEACON]^         ║ T   ⚑ planted banner
 z  −6  [BEACON]^^      T ║                      cairn
 z   0  ^^^^^       T ( D )        granite dome
```

- **Hero landmark: the Beacon of the Pass.**
  - A 20 m granite beacon tower with a great iron fire basket at (−36, −6), on the left wing; screen (140, 342) up to (25, 122).
  - It is cold at the start. On the general's death it ignites (fire C plus embers) and stays lit.
  - Its fire is the only big warm light in the map.
- **Depth, light, colour.**
  - Foreground: heather and granite slabs.
  - Playfield: the bare dome with dark heather and lichen.
  - Wings: the beacon (left), boulders and a cairn (right).
  - Far band: pines below the dome edge.
  - Late afternoon, sun at bearing 250°, elevation 18°, from the left behind the beacon: rim light on the tower, long shadows to the east.
- **Set dressing.** Granite dome; heather (muted plum-brown, small patches, never near tags); 6 boulders; 2 trail cairns (markers, not shrines); 1 ruined signal hut; 30 pines below the edges; wind-flattened grass.
- **Life.**
  - The Bannerman's horn and planted banners flapping.
  - Hawks; grass waves.
  - On victory the beacon roars up, and a second beacon answers far away (title and results camera).
- **Sources.**
  - Tripo: T4, T1.
  - Repo: Moss Bannerman and its banner; fire C.
  - Packs: P1 granite and heather, P2.
  - Shaders: wind, grade.
- **Today.** No map. Risk: a bald green hill with nothing to look at.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A bare granite hilltop in late afternoon light, dark heather and lichen on the stone. On the left, a colossal stone beacon tower crowned with a huge iron fire basket, cold and dark, rim-lit by the low sun behind it. One straight earth lane climbs from a dark pine forest at the top, edged with violet mist, to an octagonal granite platform where a large red-orange fire dragon hovers. A moss creature carrying a tall tattered violet banner leads small moss creatures up the lane, planting banners on its verge. Long shadows across the hill, wind-flattened grass. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.6 Stage 6 · Wardens of the Grove

- **Story beat.** In the Elder Grove the moss folk who keep the Hold step out of the roots to stand on the road beside the dragon.
- **Teaches.** Grove Warden (blocker). Four trap slots and two block points.
- **Gameplay layout.**
  - Gate on the left wing (−30, −4), screen (218, 365).
  - An S-lane, 36 m long, winds between boulders and giant trunks to the platform in a fern clearing.
  - No canopy over the lane: the lane runs through a chain of clearings.
- **Camera.** Yaw 0, pitch 55°, look (+2, −4).

```text
 z −42  AAAAA ⬤ AAAAAAAA ⬤ AAAAAAAAAA ⬤ AAAAA        ⬤ giant trunk 3–4 m
 z −28  AA   clearing    ⬤     clearing    AAA [ELDER]
 z −16  AA ⬤    ╱‾‾‾T‾‾‾╲        ⬤       AA [ELDER]  roots arch 8 m
 z  −4  [G]═══╱  W        ╲T  W             [ELDER]
 z  +6  AA ⬤   ferns       ( D )   ferns    AAAA
```

- **Hero landmark: the Elder Pine.**
  - Trunk 4.5 m thick, 45 m tall, at (35, −10) on the right wing.
  - Its roots arch 8 m high over mossy boulders. Its crown is cut off by the top of the frame, so the eye reads a tree too big to fit.
  - Grove Wardens step out of the root hollows when placed.
- **Depth, light, colour.**
  - Foreground: ferns and a fallen log.
  - Playfield: clearings of moss and needles.
  - Wings: giant trunks (left); the Elder Pine (right).
  - Far band: the forest's dark column wall.
  - Morning, sun at bearing 90°, elevation 30°; light shafts slant through the canopy into the clearings; motes; deep green shade.
- **Set dressing.** 18 giant pines, 30–45 m (wings and far band only, never between the camera and the lane); 40 pines; 200 ferns; 12 mossy boulders, 2–4 m; 6 fallen logs; small muted mushrooms.
- **Life.**
  - Grove Wardens idle in the roots; squirrels.
  - A red deer at the clearing edge bolts when the wave card shows.
  - Motes drift in the shafts.
- **Sources.**
  - Repo: Grove Warden.
  - Packs: P2 giant conifers (or Tripo at full detail), P1 forest floor and moss, P4 deer.
  - Shaders: light shafts, occluder dither, wind.
  - Tripo: T1.
- **Today.** No map. Risk: today's round crowns would bury the lane; tag readability breaks under canopy.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. An ancient pine grove in the morning: shafts of sunlight slant through the canopy into a chain of mossy clearings. One earth lane winds in an S from the left between giant trunks and boulders to an octagonal granite platform in a fern clearing, where a large red-orange fire dragon hovers. Small moss creatures with violet rags walk the lane; sturdy moss guardians with bark shields block it. On the right, a colossal elder pine, its trunk wider than the lane and its roots arching over boulders, too tall to fit in the frame. Deep green shade, motes in the light. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.7 Stage 7 · The Mill Race

- **Story beat.** The blight comes for the Hold's great mill; the miller's healing draughts become Hỏa Long's first potions.
- **Teaches.** Small Potion (Alt + 7). Four trap slots and two block points.
- **Gameplay layout.**
  - Gate north-west (−20, −24).
  - A straight lane, 30 m long, to the platform. It crosses the mill race on a low stone culvert at mid-lane (no slowdown).
  - The millpond is at the top right, the mill on the right wing.
- **Camera.** Yaw 0, pitch 55°, look (+2, −4).

```text
 z −42  AAAA[G]AAAAAAAAAAAAAAAAAA   ≈≈≈≈ millpond ≈≈≈≈ AAA
 z −30  AA    ╲    T                 ≈≈≈≈≈≈≈≈≈≈≈≈ weir
 z −18  AA     ╲T  W               ════ race ════[MILL]◎   ◎ 10 m wheel
 z  −8  ═══════culvert═══race══════════════════ [MILL]
 z   0  alders    T╲  W  ( D )    sacks, carts
```

- **Hero landmark: the Great Mill.**
  - A three-storey granite-and-timber mill (14 m) at (34, −12) on the right wing.
  - Its 10 m wheel turns in the race and throws spray; a weir spills from the millpond above it.
  - Screen: from (1150, 300) up to about (1210, 160).
- **Depth, light, colour.**
  - Foreground: the race running out along the bottom-left; alders.
  - Playfield: meadow, flagged yard, sacks.
  - Wings: alders and the race (left); the mill (right).
  - Far band: millpond mist and the forest.
  - Morning, sun at bearing 80°, elevation 25°: mist lifts off the pond; the wheel's spray catches the light.
- **Set dressing.** 1 mill and wheel; 40 m stone race channel; millpond 20 m; weir; sluice gate; 3 spare millstones; 12 grain sacks; 2 carts; 30 pines; 12 alders (dark, not round lollipops); reeds.
- **Life.**
  - The wheel turns and the race flows; ducks on the pond; smoke from the mill.
  - A Grove Warden carries sacks inside when the wave card shows.
- **Sources.**
  - Tripo: T5, T1.
  - Packs: P1, P2 (alders, reeds), P4 ducks, P5 spray.
  - Shaders: flow-map race and pond, height fog, wheel rotation.
- **Today.** No map. Risk: cozy village look (mill plus ducks); keep the mill massive and granite, the colours cool.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A misty spring morning at a massive granite-and-timber watermill on the right side of the frame, its great wheel turning in a stone mill race and throwing bright spray, a millpond with lifting mist above it. One straight earth lane comes from a dark pine forest at the upper left, edged with violet mist, crosses the mill race on a low stone culvert and reaches an octagonal granite platform where a large red-orange fire dragon hovers. Small moss creatures with violet rags walk the lane; grain sacks and carts in the yard; dark alders along the water. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.8 Stage 8 · Horns at Noon

- **Story beat.** At the foot of the Long Stair the Hold's great horns hang between dragon pillars; sound them and the next wave comes early, for a richer reward.
- **Teaches.** Calling a wave early (Shift + Enter). Four trap slots and two block points.
- **Gameplay layout.**
  - Gate high on the slope at the top (6, −31).
  - An S-lane, 40 m long, switches back down a terraced slope to the platform on a terrace.
  - Retaining walls lie between the switchbacks, ≥ 8 m apart.
- **Camera.** Yaw 0, pitch 55°, look (0, −5).

```text
 z −42  AAAAAAAAAAAAAAA[G]AAAAAAAAAAAAAAAAA
 z −32  ▮PILLAR▮        ╲════════╗ T            retaining wall
 z −22  ▮ STAIR▮   T ╔══════════╝   W           (switchbacks)
 z −12  ▮PILLAR▮     ╚═══════╗ T
 z  −2  ▮ STAIR▮  W        ( D )    terrace
```

- **Hero landmark: the Long Stair.**
  - An 8 m wide granite stair climbs the left-wing cliff toward the Hold's upper bastion, which is out of frame.
  - Six dragon pillars (8 m) flank it; two great bronze-and-iron horns hang between the top pair.
  - Screen: the stair runs from about (150, 380) to the top-left corner.
- **Depth, light, colour.**
  - Foreground: the lowest retaining wall.
  - Playfield: terraces of turf and gravel.
  - Wings: the stair and pillars (left); boulders and pines (right).
  - Far band: the forest above the slope.
  - Noon, sun at bearing 170°, elevation 62°: crisp, short shadows. Racing cloud shadows give the contrast; bright and clean.
- **Set dressing.** The stair (terrain cut with P1 slab textures); 6 pillars; 2 horn frames; 5 retaining walls; 50 pines; 12 boulders; alpine flowers (white, pale yellow) on the terraces away from the lane.
- **Life.**
  - Grove Wardens stand by the horns and blow them when the player calls a wave (the horn sound and a ring of dust).
  - Swallows; cloud shadows.
- **Sources.** Tripo: T6, T1. Packs: P1, P2, P4. Shaders: cloud shadows, grade.
- **Today.** No map. Risk: noon light flattens forms; the cloud shadows and stair relief must carry it.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A terraced mountain slope at bright noon, racing cloud shadows on the grass. On the left, a monumental granite stairway climbs the cliff, flanked by six tall carved dragon pillars, with two great bronze war horns hanging between the top pair. One earth lane switches back down the slope between stone retaining walls, from a dark pine forest at the top edged with violet mist to an octagonal granite platform on a terrace, where a large red-orange fire dragon hovers. Small moss creatures with violet rags walk the switchbacks. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.9 Stage 9 · The Warm Springs

- **Story beat.** A quiet stage at the hot springs: the dragons rest and go over the words they learned. Few foes, no hazard.
- **Teaches.** First review stage: learn ahead, review card. Four trap slots and two block points (already unlocked).
- **Gameplay layout.**
  - Gate on the right wing (30, −8).
  - A short straight lane, 26 m long, along the pool rims to the platform.
  - The pools sit ≥ 3 m from the lane.
- **Camera.** Yaw 0, pitch 55°, look (+3, −4).

```text
 z −42  AAAAAAAAAAAAAAAAAAAAAAAA ░STEAM FALLS░ AAAA      ░ stepped travertine falls 15 m
 z −30  AAA   ◌pool   ◌pool        ░░░░░░░░ ◌            ◌ warm pool in granite
 z −18  AA  ◌pool    ◌         ◌pool   ░░░░
 z  −8  AA      ◌      ═══════T═══W═══════[G]
 z   0  AAA   ◌pool  ( D )  ◌pool   AAA
```

- **Hero landmark: the Steam Falls.**
  - A 15 m stepped travertine waterfall: cream and pale ochre terraces with milky jade-grey water (not turquoise, 05 §2.2).
  - It runs from the top band down the right side, around (30…44, −20…−34).
  - Columns of steam rise and drift over the map.
- **Depth, light, colour.**
  - Foreground: steam pools at the bottom edge.
  - Playfield: granite terraces with pools.
  - Wings: pines (left); the falls (right).
  - Far band: steam veiling the forest.
  - Soft morning, sun at bearing 100°, elevation 22°, diffused by the steam; low contrast, calm palette.
- **Set dressing.** The falls (travertine terrain with P1 travertine); 12 pools, 3–8 m; 6 steam vents; 30 pines; 10 boulders; moss rims.
- **Life.** A grey heron in a pool; steam drifting; birds; only a few foes.
- **Sources.** Tripo: T1. Packs: P1 travertine and granite, P2, P4 heron, P5 steam. Shaders: water (calm), steam volumes, height fog.
- **Today.** No map. Risk: pale travertine behind word tags; keep the lane band on dark granite.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. Hot springs in a granite valley on a soft spring morning: on the right, a tall stepped waterfall over cream travertine terraces, milky jade-grey water, columns of steam drifting across the scene. Warm pools in granite basins around an octagonal granite platform where a large red-orange fire dragon rests. One short earth lane comes in from the right along the pool rims; only a few small moss creatures with violet rags walk it. A grey heron in a pool, pines on the left. Calm, quiet, low contrast. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.10 Stage 10 · The Captain's Gate

- **Story beat.** At dusk a blighted captain marches through the broken gate of the old outer wall, the line the Hold lost long ago.
- **Teaches.** Mini-boss: a strong captain (W 16, 02 §4.4). Four trap slots and two block points.
- **Gameplay layout.**
  - Gate on the right wing, through the arch at (30, −6), screen (1057, 342).
  - An S-lane, 36 m long, runs along the ruined wall line, then turns to the platform.
  - The captain enters alone after the second peak.
- **Camera.** Yaw 0, pitch 55°, look (+3, −4).

```text
 z −42  AAAAAAAAAAAAAA ▪▪ wall stub ▪▪ AAAAAAAAAAAA
 z −30  AA  burned wagon      ▪   ╱‾‾‾‾‾T‾‾‾‾‾‾‾╲
 z −18  AA             ▪▪▪  ╱  W             ▪  ╲
 z  −6  AA  T  ╲______________╱       ▪▪   [ARCH]═[G]       [ARCH] ruined outer gate, 16 m
 z  +4  AA    W  ( D )    fallen stones
```

- **Hero landmark: the Broken Gate.**
  - The 124 `ruined-arch` at 2× (16 m) standing over the lane's entrance on the right wing.
  - Broken `hold-wall` stubs run from it across the far band.
  - Blight banners hang from the arch; the captain's horn sounds from behind it.
- **Depth, light, colour.**
  - Foreground: fallen stones.
  - Playfield: rough grass over old paving.
  - Wings: pines (left); the arch (right).
  - Far band: wall stubs and the darkening forest.
  - Dusk, sun at bearing 265°, elevation 8°, from the left: red-gold rim on the arch, very long shadows toward the gate, violet haze rising from the ground.
- **Set dressing.** 1 arch (2×); 5 broken wall segments; 30 fallen stones; 2 burned wagons; 6 blighted snags; 40 pines; old paving patches.
- **Life.** Blight banners flap; ravens on the arch; the muster growls in the arch's shadow; the captain's horn.
- **Sources.** Repo: 124 `ruined-arch`, `hold-wall` (via Tripo). Tripo: T1. Packs: P1, P2, P4. Shaders: dusk grade, blight haze.
- **Today.** No map. Risk: dusk turns everything orange; keep the orange in the light only, not in the ground.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. Dusk at the ruins of an ancient outer wall: on the right, a colossal broken stone gate arch with tattered violet blight banners, red-gold rim light from the setting sun at the left, very long shadows. Broken wall stubs run across the top of the frame. One earth lane enters through the arch and winds along the old wall line to an octagonal granite platform where a large red-orange fire dragon hovers. A large armoured moss captain with a horn leads small moss creatures through the gate. Burned wagons, fallen stones, violet haze rising. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.11 Stage 11 · Two Dragons

- **Story beat.** High on the White Eyrie, above a sea of cloud, Bạch Long wakes in her old nest and flies down to fight beside Hỏa Long.
- **Teaches.** Bạch Long joins; Feather Shield (Alt + 3). First half-spiral layout. Four trap slots and two block points.
- **Gameplay layout.**
  - Gate at the top band (−6, −31).
  - The lane (`L1-xoan`) comes down to the platform's north side, then wraps half a turn around it clockwise on a ledge 9–12 m out, and enters from the south-east. The foes spend longer in the word zone.
  - The ledge is ≥ 8 m from its own earlier stretch.
- **Camera.** Yaw 0, pitch 55°, look (0, −3).

```text
 z −42  AAAAAAAAAAA[G]AAAAAA  krummholz pines
 z −30  ▲▲            ╲   T
 z −18  ▲NEEDLE▲        ╲______
 z  −6  ▲NEEDLE▲   T          ╲   W        ░░░ cloud sea
 z  +4  ▲▲▲         ( D )      │ T       ░░░░░░░░
 z +14  ▲▲    W  ╲_____________╱      ░░░░░░░░░░░   (drop on the right and lower right)
```

- **Hero landmark: the Eyrie Needle.**
  - A 45 m granite pinnacle at (−36, −8) on the left wing. Its lower 20 m is in frame, (140, 342) to about (46, 122); the rest is cropped, so it reads as endless.
  - White feathers drift down from the hidden nest.
  - The right side of the tableland drops into a cloud sea, seen on the right wing and in the lower-right corner.
- **Depth, light, colour.**
  - Foreground: the cloud sea at the lower right.
  - Playfield: a granite tableland with alpine turf.
  - Wings: the Needle (left); the cliff edge and cloud sea (right).
  - Far band: wind-bent pines.
  - Dawn, sun at bearing 95°, elevation 10°, just above the cloud sea: pink-gold light, long blue shadows. The Needle catches the first light.
  - The cloud sea is bright, so the spiral's last stretch must run over dark ledge stone, never in front of the clouds.
- **Set dressing.** Needle (terrain plus P1 granite); 20 wind-bent pines, 6–10 m; 8 boulders; a ruined ring wall around the platform; alpine turf; 3 drifting feather particle emitters.
- **Life.**
  - Bạch Long flies in from the cloud sea at the start, circles the Needle and lands.
  - Alpine choughs; the cloud sea moves slowly.
- **Sources.**
  - Repo: Bạch Long `guides/draconis-v4`.
  - Tripo: T1.
  - Packs: P1, P2 krummholz, P4 choughs.
  - Shaders: cloud sea (layered noise cards, MIT shader code), dawn grade, wind.
- **Today.** No map. Risk: a bright cloud sea fighting the word tags for attention.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A granite tableland at dawn above a sea of pink-gold cloud that fills the right side and lower right. On the left, a colossal granite pinnacle rises out of the top of the frame, white feathers drifting down from a hidden nest, its face lit by the first sun. One earth lane comes from wind-bent pines at the top and spirals half around an octagonal granite platform, where a large red-orange fire dragon hovers and a pearl-white dragon lands beside it. Small moss creatures with violet rags walk the spiral. Long blue shadows. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.12 Stage 12 · Wings over the Pass

- **Story beat.** A blighted hive hangs under the cliff, and the first thorn wasps take to the air.
- **Teaches.** First flyer: Thorn Wasp on a sky lane. Four trap slots and two block points.
- **Gameplay layout.**
  - Ground gate at the top (0, −31); a straight ground lane, 28 m long.
  - Sky lane from the hive at (34, −14), altitude 3 m, across the east meadow to the platform.
  - The two lanes meet only at the platform.
- **Camera.** Yaw 0, pitch 55°, look (+2, −4).

```text
 z −42  AAAAAAAAAAAAAA[G]AAAAAAAAAAAAAAA ^^^^^^^
 z −30  AAA   meadow   ║  T             ^^[HIVE]^   [HIVE] 12 m blighted hive under an overhang
 z −18  AA          T  ║  W         ·····^^^^^       ····· sky lane, 3 m up
 z  −6  AA     T       ║      ·····      ^^^
 z   0  AAA          ( D )·····    wind-waved grass
```

- **Hero landmark: the Hive.**
  - A 12 m blighted wasp hive of violet-grey paper layers under a granite overhang at (34, −14), on the right wing; screen about (1149, 122)–(1135, 300).
  - Its openings glow `#C8D24A` in small points only.
  - The 25 m right-wing cliff carries it.
- **Depth, light, colour.**
  - Foreground: tall grass.
  - Playfield: windy meadow.
  - Wings: pines (left); the hive cliff (right).
  - Far band: the forest bending in the wind.
  - Bright windy morning, sun at bearing 120°, elevation 30°; fast clouds; strong grass waves.
- **Set dressing.** The hive (T10); a 25 m cliff with an overhang; 2 dead snags with small hives; 60 pines; 10 boulders; 50 k grass tufts.
- **Life.**
  - Wasps orbit the hive before each wave. A flyer leaving the hive trails violet dust.
  - Swallows keep away from the hive.
  - Pines bend in the gusts.
- **Sources.** Tripo: T10, T1. Repo: Thorn Wasp. Packs: P1, P2, P4. Shaders: wind field, grass, blight glow.
- **Today.** No map. Risk: wasps (small flyers) lost against busy cliff texture; keep the sky lane over the plain meadow.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A windy mountain meadow on a bright morning, grass rippling in waves. On the right, a huge blighted wasp hive of violet-grey paper hangs under a granite overhang, its openings glowing faintly yellow-green; thorn wasps stream out of it and fly low over the meadow toward the centre. One straight earth lane comes from a dark pine forest at the top, edged with violet mist, to an octagonal granite platform where a large red-orange fire dragon hovers. Small moss creatures with violet rags walk the lane. Pines bending in the wind. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.13 Stage 13 · Nets and Wind

- **Story beat.** At the Windgap the wardens' old signal mast still carries its net winch: Hỏa Long learns to drag the wasps out of the gale.
- **Teaches.** Net Launcher. Four trap slots, two block points, sky lane.
- **Gameplay layout.**
  - Ground gate at the top (8, −31); an S-lane, 36 m long, across the saddle.
  - Sky lane from the right edge (31, −4) along the gap.
  - The saddle falls away on both sides; both drops are visible in the lower corners.
- **Camera.** Yaw 0, pitch 55°, look (0, −4).

```text
 z −42  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾[G]‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   saddle crest, wind-bent pines
 z −30  [MAST]       T ╱╱        cairn
 z −18  [MAST]     ╱╱  W                   ·········· sky lane
 z  −6  [MAST]  T ╲╲         ·········
 z  +6  ░drop░      ( D )                    ░drop░
```

- **Hero landmark: the Windgap Mast.**
  - A 20 m timber-and-iron signal mast at (−36, −8), guyed with chains, with tattered ember pennants as a small accent and an old net winch and net racks at its foot.
  - Left wing; it leans in the gale with the wind field.
- **Depth, light, colour.**
  - Foreground: the drops at the lower corners, with mist.
  - Playfield: saddle grassland and granite.
  - Wings: the mast (left); a stone shelter and boulders (right).
  - Far band: the crest line.
  - Breaking overcast, sun at bearing 200°, elevation 35°, in moving patches; fast cloud shadows; cool palette.
- **Set dressing.** Mast (T11); 2 stone shelters; 3 trail cairns; 25 wind-bent pines; 8 boulders; net racks; grass.
- **Life.**
  - Pennants snap; grass waves; an eagle hangs in the wind.
  - Wasps fight the gusts (sky lane wobble in the view only).
- **Sources.** Tripo: T11, T1. Repo: Net Launcher, Thorn Wasp. Packs: P1, P2, P4 eagle. Shaders: wind, cloud shadows, drop mist.
- **Today.** No map. Risk: a bare grassy saddle with nothing to look at; the mast and the drops must carry it.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A high windswept mountain saddle under breaking overcast, patches of sun racing over the grass, the ground falling into misty drops at both lower corners. On the left, a tall ancient timber-and-iron signal mast held by chains, tattered ember pennants snapping in the gale, a net winch at its foot. One earth lane crosses the saddle in an S from the top to an octagonal granite platform where a large red-orange fire dragon hovers; a net trap fires a net over thorn wasps flying low along the gap. Small moss creatures with violet rags on the lane. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.14 Stage 14 · The Flood Bridge

- **Story beat.** Below the wardens' Upper Dam the river runs fast. The blight crosses on the low causeway bridge until the dragon mouths of the dam roar open and flood it.
- **Teaches.** Pine Bomb; the kit's signature mechanic (bridge and stream, 04 §2.1); the Flood hazard (the bridge floods for 10 s, warned 3 s ahead). Four trap slots and two block points.
- **Gameplay layout.**
  - Gate at the top (−4, −31).
  - One lane crosses the river (flowing east → west across the middle, z ≈ −14) on the low causeway bridge, the choke point.
  - A detour branch wades the ford 14 m downstream (30 % slower, Wet) and rejoins before the platform. Foes take it only while the bridge is flooded.
- **Camera.** Yaw 0, pitch 55°, look (0, −4).

```text
 z −42  AAAAAAAAAAAAAAA[G]AAAAAAAAAAAAAAAAAAAA  ^^^^^^
 z −30  AAA      T       ║                     [DAM]≋≋     ≋ dragon-head spillways
 z −14  ≈≈≈≈ford≈≈≈≈≈≈≈≈[=CAUSEWAY=]≈≈≈≈≈≈≈≈≈≈≈≈[DAM]≋≋     river flows right → left
 z  −6  AA  ╲╲ detour   W║  T                   [DAM]
 z   0  AA    ╲╲════════( D )   cone-laden pines
```

- **Hero landmark: the Upper Dam.**
  - An ancient granite dam (14 m) across the river's gorge on the right wing, (34…44, −24…−8).
  - Three dragon heads pour the river from their jaws.
  - The flood warning: the dragon eyes glow, a horn sounds, and 3 s later the jaws open wide and a surge runs down the river over the causeway.
- **Depth, light, colour.**
  - Foreground: the river's lower bank.
  - Playfield: both banks, the causeway, the ford.
  - Wings: cone-laden pines (left); the dam (right).
  - Far band: forest.
  - Bright morning, sun at bearing 100°, elevation 30°: spray glitters at the dam (kept off the tag band), cool water, gold rims on wet stone.
- **Set dressing.** Dam with 3 spillways (T12); a low 5-arch causeway, 30 m (T13); a ford with 9 stepping stones; 20 boulders; 80 pines with large cones (the Pine Bomb source); 2 sluice wheels; a flood-gauge pillar with carved notches (no numbers).
- **Life.**
  - Spray; rapids; trout leaping below the dam; a heron.
  - The dam horn; surge foam during the flood.
- **Sources.** Tripo: T12, T13, T1. Repo: Pine Bomb. Packs: P1, P2, P4, P5. Shaders: flow-map river with a surge state, spray, foam, wet-stone sheen.
- **Today.** No map. Today's river shader has no surge and no foam; the flood would read as nothing.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A fast mountain river crosses the middle of the frame from right to left. On the right, an ancient granite dam across the gorge pours the river out of three huge carved dragon heads, white spray in bright morning light. One earth lane comes from a dark pine forest at the top, edged with violet mist, and crosses the river on a low stone causeway bridge of five arches; a side track wades a ford downstream. Small moss creatures with violet rags cross toward an octagonal granite platform where a large red-orange fire dragon hovers; a pine-cone bomb bursts on the bridge. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.15 Stage 15 · Dragon's Rage

- **Story beat.** Where an elder dragon died long ago, its bones still hold heat. Fighting beside them, Hỏa Long's rage fills, and for the first time he takes the Inferno form.
- **Teaches.** General stage; Dragon Rage; Inferno (Alt + 5); the Fire Orb slot. Four trap slots and two block points.
- **Gameplay layout.**
  - Gate at the top right (14, −29).
  - A straight lane, 30 m long, down an old scorched slope to the platform.
  - The general enters in the last wave.
- **Camera.** Yaw 0, pitch 55°, look (+1, −4).

```text
 z −42  ‿‿vertebrae‿‿‿  AAAAAAAAAAA[G]AAAAAAA
 z −30  )))RIBS)))          T  ╱
 z −18  )))RIBS)))      T  ╱  W        scorched ground
 z  −6  [SKULL]      T ╱                  obsidian shards
 z  +4  [SKULL]   W ( D )        boulders
```

- **Hero landmark: the Elder Bones.**
  - The stone-fossil skeleton of an ancient dragon in the hillside on the left wing.
  - A 10 m skull, half buried, at (−34, 0).
  - Five ribs arch 12–15 m over the slope; vertebrae run off the top-left.
  - Embers glow in the eye socket as Rage fills; when Inferno fires, the bones answer with a pulse of light.
- **Depth, light, colour.**
  - Foreground: obsidian shards and scorched turf.
  - Playfield: an old burn healed to dark olive grass.
  - Wings: the bones (left); boulders and pines (right).
  - Far band: forest.
  - Afternoon gold turning amber by the last wave, sun at bearing 240°, elevation 22°. The warm colour comes from the light, not from painted ground.
- **Set dressing.** Skull, 5 ribs, 30 vertebra stones (T14); scorched decals; obsidian shards (small); 50 pines; 15 boulders.
- **Life.** Heat shimmer over the skull; embers rising when Rage fills; ravens on the ribs; the general's horn.
- **Sources.** Tripo: T14, T1. Repo: `draconis-v3` for Inferno, fire C. Packs: P1, P2, P4, P5 embers. Shaders: heat shimmer, ember glow, grade shift.
- **Today.** No map. Risk: bones read as a graveyard. Keep them stone and moss, ancient and majestic, never gory (the game has no blood).
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A mountainside in afternoon gold light. On the left, the colossal stone-fossil skeleton of an ancient dragon lies in the hill, mossy and weathered: a huge half-buried skull with embers glowing in its eye socket, great ribs arching higher than the trees. One straight earth lane comes from a dark pine forest at the upper right, edged with violet mist, to an octagonal granite platform where a large red-orange fire dragon blazes with rising power. A big moss general and small moss creatures with violet rags walk the lane. Heat shimmer, embers rising. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.16 Stage 16 · The Herb Terraces

- **Story beat.** The Hold's healers grow their herbs on terraces watered by an old aqueduct; the first Herb Hut is raised to tend the defenders.
- **Teaches.** Herb Hut (first magic house); house pads appear: two inner (7–9 m) and two outer (14–18 m), 2–6 m from the lane. Four trap slots and two block points.
- **Gameplay layout.**
  - Gate at the top left (−14, −29).
  - An S-lane, 38 m long, down through the terraces to the platform.
  - The terraces step down toward the camera, with retaining walls ≤ 1.2 m.
- **Camera.** Yaw 0, pitch 55°, look (0, −4).

```text
 z −42  AAAA[G]AAAAAAAAAAAAAAAAAAAAAAAAA   ⌒⌒AQUEDUCT⌒⌒
 z −30  ═══terrace══╲═══════H═══════════  ⌒⌒ ║broken span → ribbon fall
 z −18  ═══terrace═══╲T══W═════════════   ⌒⌒ pool
 z  −6  ═══terrace══H═╲═══T═══channels═══ ⌒⌒
 z  +4  ════════════════( D )═══H═══════
```

- **Hero landmark: the Aqueduct.**
  - Three 18 m granite arches cross the right wing at (34…40, −24…+2).
  - One span is broken: the water falls as a white ribbon into a pool that feeds stone channels running down the terraces.
  - Screen: from about (1180, 120) to (1120, 420).
- **Depth, light, colour.**
  - Foreground: the lowest terrace wall.
  - Playfield: herb beds in sage, silver and white yarrow with pale yellow. No lavender: it reads as blight violet.
  - Wings: pines (left); the aqueduct (right).
  - Far band: forest.
  - Morning, sun at bearing 70°, elevation 35°; water glints in the channels.
- **Set dressing.** 3 aqueduct spans (T15); 6 terraces with drystone walls; herb beds (instanced cards); stone channels, 80 m; 1 stone drying house with a slate roof; 40 pines; 2 water barrels.
- **Life.** Water running in the channels; pale butterflies; steam from the Herb Hut's brew; Grove Wardens tending the beds.
- **Sources.** Tripo: T15, T1. Repo: Herb Hut (fix its colour per the bible §3.5). Packs: P1, P2 herbs, P4, P5. Shaders: channel water, wind.
- **Today.** No map. Risk: a cozy cottage garden. Scale and granite must win over prettiness.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. Herb terraces on a mountain slope in morning light: beds of sage-green, silver and white herbs between low drystone walls, stone water channels glinting. On the right, a colossal ancient granite aqueduct of three tall arches, one span broken, a white ribbon of water falling into a pool. One earth lane winds in an S from a dark pine forest at the top left, edged with violet mist, down the terraces to an octagonal granite platform where a large red-orange fire dragon hovers, beside a small herb hut with a leaf roof on a stone base. Small moss creatures with violet rags on the lane. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.17 Stage 17 · Hold the Granary

- **Story beat.** The blight breaks through the Hold's outer bailey wall to reach the winter grain. If the granary falls, the Hold starves.
- **Teaches.** Dragon Heart and Hard Scale (buying health and armour); the Scale Armour slot; objective "Hold the Granary" (04 §5.2: granary 8–12 m from the platform; lose it, lose the stage); the first challenge mark. Four trap slots, two block points, four house pads.
- **Gameplay layout.**
  - Gate through a breach in the outer wall at the top band (6, −31).
  - A straight lane, 28 m long, to the platform.
  - The granary stands at (−9, +7), 11.4 m from the platform. Its top (9 m) reaches screen y ≈ 420, beside the platform and never over it.
  - Foes that reach the platform's ring turn on the granary.
- **Camera.** Yaw 0, pitch 55°, look (0, −3).

```text
 z −42  ######[BREACH]##########  outer bailey wall (dark pines beyond)
 z −30  [KEEP]          ║  T
 z −18  [KEEP]       T  ║  W        wagons
 z  −6  [KEEP]   H      ║        H
 z  +6  [KEEP]   (GRANARY) ( D )  H      threshing floor, well
```

- **Hero landmark: the Inner Keep.**
  - A 30 m square granite keep at (−36, −4) on the left wing: its lower 15 m in frame, (140, 360) up to about (59, 227), and its top cropped.
  - Sentinel braziers burn on its walk.
  - The granary is the gameplay landmark: round, granite, a slate cone roof and a big iron-banded door. It is kept low and solid so its health bar reads.
- **Depth, light, colour.**
  - Foreground: grain wagons and sacks at the bottom edge.
  - Playfield: the bailey's packed earth and flags.
  - Wings: the keep (left); stables and the bailey wall (right).
  - Far band: the breached outer wall.
  - Harvest-gold afternoon, sun at bearing 230°, elevation 25°; grain dust in the light.
- **Set dressing.** Keep and granary (T16); 3 outer wall segments with a breach (124 `hold-wall`); 2 wagons; 20 sacks; 6 barrels; a threshing floor; a well; 1 stable block; 30 pines outside the wall.
- **Life.** Grove Wardens carry sacks into the granary until the wave card shows, then shut its door; sparrows on the roof; banners on the keep.
- **Sources.** Repo: 124 `hold-wall`, `brazier`. Tripo: T16, T1. Packs: P1, P2, P4, P5 dust. Shaders: grade, dust.
- **Today.** No map. Risk: the granary hides a pad or the platform from tilted views; the occluder dither covers it.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. The outer bailey of a mountain fortress in harvest-gold afternoon light, grain dust in the air. On the left, a colossal square granite keep rises out of the top of the frame, braziers on its walls. Beside the centre, a sturdy round granite granary with a slate cone roof and an iron-banded door. One straight earth lane comes through a breach in the outer wall at the top to an octagonal granite platform where a large red-orange fire dragon hovers. Small moss creatures with violet rags pour through the breach; wagons and grain sacks in the yard. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.18 Stage 18 · The Roar

- **Story beat.** In the Echo Cirque under the hanging glacier, Hỏa Long's roar rolls off the ice walls and drives the blight back.
- **Teaches.** Urgent word; Dragon Roar. Four trap slots, two block points, four house pads.
- **Gameplay layout.**
  - Gate on the right wing (30, −8), screen (1052, 320).
  - An S-lane, 36 m long, across dark wet scree and alpine turf to the platform.
  - Snow and ice stay on the left wing and the top-left band only, never behind the tag band (≤ 0.6 luma).
- **Camera.** Yaw 0, pitch 55°, look (+2, −4).

```text
 z −42  ❄❄❄[GLACIER]❄❄❄❄❄  moraine   ‾‾‾‾‾‾‾‾‾‾
 z −30  ❄[GLACIER]❄ |falls|     ○tarn○        stunted pines
 z −18  ❄❄❄  |falls|   T╱‾‾‾‾‾‾‾‾‾╲  W
 z  −6  ❄❄  scree     ╱  H         ╲═T══[G]
 z  +4  ❄  moraine  ( D )  H   T    scree
```

- **Hero landmark: the Hanging Glacier.**
  - A 30 m wall of blue ice on the left wing and the top-left band, (−30…−44, −10…−40).
  - Three meltwater falls; a dark tarn below it.
  - Dragon Roar shakes snow off its lip (VFX: slough and powder); cracks boom.
- **Depth, light, colour.**
  - Foreground: moraine boulders.
  - Playfield: dark wet scree and turf.
  - Wings: the glacier (left); a scree slope and the gate (right).
  - Far band: moraine ridge.
  - Cold bright morning, sun at bearing 130°, elevation 30°: blue shadows, cold white ice, gold only on the turf tips.
- **Set dressing.** Glacier (terrain plus ice shader); 3 waterfalls; 1 tarn, 25 m; 30 moraine boulders; 15 stunted pines; snow patches on the left only.
- **Life.** Meltwater; snow sloughs; two ibex on a ledge; choughs; the roar's echo.
- **Sources.** Tripo: T1. Packs: P1 snow, ice, scree; P2; P4 ibex. Shaders: ice (refraction-lite, blue depth), snow, waterfalls, slough VFX.
- **Today.** No map. Risk: snow glare under word tags; the lane placement above solves it.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A glacial cirque on a cold bright morning. On the left and across the top left, a colossal wall of blue glacier ice with three meltwater falls into a dark mountain lake, snow on its ledges. One earth lane enters from the right and crosses dark wet scree and alpine turf in an S to an octagonal granite platform where a large red-orange fire dragon roars, a ring of wind and dust bursting outward and snow falling from the glacier lip. Small moss creatures with violet rags stagger back. Blue shadows, moraine boulders. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.19 Stage 19 · Campfire

- **Story beat.** The last camp before the Den: around the fire the dragons go over the hardest words of the chapter, while behind the palisade something huge paces and grunts.
- **Teaches.** Review stage; Campfire (preview of the boss's attacks, phases and typing rules). Few foes. All slots open.
- **Gameplay layout.**
  - Gate at the palisade gate at the top band (0, −32).
  - A short straight lane, 26 m long, to the platform.
  - The campfire sits on the platform's south edge.
- **Camera.** Yaw 0, pitch 55°, look (0, −4).

```text
 z −42  ‖‖‖‖‖‖‖‖‖‖‖‖‖[ GATE ]‖‖‖‖‖‖‖‖‖‖‖‖‖     ‖ palisade of pine trunks, 8 m
 z −30  AA  tents      ║   T                   tents
 z −18  AA      T      ║   W      weapon rack
 z  −6  AA   H         ║        H
 z  +4  AA        ( D )🔥 campfire     H
```

- **Hero landmark: the Tusk Wall.**
  - The boar's palisade of whole pine trunks, 8 m, along the top band. Its top is cropped by the frame edge, so it reads as taller than it is.
  - Tusk gouges and blight vines on the trunks; a great barred gate in the middle.
  - Two glowing eyes move behind the gaps.
  - On a timer the gate shudders and dust falls (the boss preview).
- **Depth, light, colour.**
  - Foreground: tents and the fire glow.
  - Playfield: the trampled camp clearing.
  - Wings: pines and tents.
  - Far band: the palisade, lit violet-green from behind.
  - Blue hour, with a deep blue sky reflected in puddles. The campfire is the warm key light (radius 10 m); braziers on the platform.
- **Set dressing.** Palisade with gate (T17); 4 canvas tents in muted ochre and grey; 2 weapon racks; campfire; 2 cooking stands; 30 pines; 8 boulders.
- **Life.** Fireflies (first in the chapter); sparks from the fire; growls; Grove Wardens around the fire; an owl.
- **Sources.** Tripo: T17, T1. Repo: fire C for the campfire. Packs: P1, P2, P4 owl, P5 sparks. Shaders: blue-hour grade, firelight, fireflies.
- **Today.** No map. Risk: dark scene hides foes; keep rim light on foes from the fire and the violet back-glow.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A forest camp at blue hour. Across the top of the frame, a towering palisade of whole pine trunks gouged by huge tusks and wrapped in blight vines, a great barred gate in its middle, violet-green light and two glowing eyes behind the gaps. A short earth lane runs from the gate to an octagonal granite platform where a large red-orange fire dragon rests beside a big campfire, its warm light on canvas tents, weapon racks and sturdy moss guardians. A few small moss creatures with violet rags slip out of the gate. Fireflies, sparks, deep blue shadows. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

### 4.20 Stage 20 · Tuskfather

- **Story beat.** The Tuskfather, the blighted boar lord, smashes through his palisade and charges the dragons; when he falls, the violet haze over the valley head burns away.
- **Boss.** B01 `tuskfather` (02 §4.3, §4.5).
  - Phase 1: charges in straight lines (red line warning 1.5 s; after a charge he is stunned 2 s and takes ×1.5).
  - Phase 2 (60 %): two tusks, two words each.
  - He calls 4 ant clusters.
  - Final phase: the chapter's word exam (04 §7.3).
- **Gameplay layout.**
  - Gate at the palisade gate at the top band (0, −32).
  - One long straight lane, 32 m, with a wide charge apron (8 m) of trampled earth, so the red charge line reads on clean ground.
  - Four ant mounds at the lane's flanks feed the swarms.
  - All slots open.
- **Camera.** Yaw 0, pitch 55°, look (0, −5). The boss is 140–220 px tall at 1080p.

```text
 z −42  ‖‖‖‖‖‖‖‖‖‖╳╳BROKEN╳╳‖‖‖‖‖‖‖‖‖‖‖‖    ╳ smashed gate, splinters
 z −30  (M)  AA     ┃▓▓▓▓▓┃   T    [LAIR MOUND]   (M) ant mound
 z −18  ‡‡     T    ┃charge┃  W    [LAIR MOUND]   ▓ trampled charge apron
 z  −6  (M)   H     ┃apron ┃     H    (M)
 z  +4  ‡‡        ( D )        H      ‡ blighted snags
```

- **Hero landmark: the Den.**
  - The broken Tusk Wall across the top band: the gate bursts at the start of the fight (splinters, dust, VFX).
  - The lair mound on the right wing: a 10 m heap of uprooted pines and earth at (34, −14), with the boss's wallow.
  - The Tuskfather himself is the living landmark.
- **Depth, light, colour.**
  - Foreground: trampled earth and snags.
  - Playfield: the clearing and its charge apron.
  - Wings: snags and an ant mound (left); the lair mound (right).
  - Far band: the broken palisade.
  - Mid-morning under a low violet blight haze (grey-violet grade, flat light). On victory the haze burns off and the sun breaks through at bearing 110°, elevation 30°: gold light floods the valley head. The grade change is the reward.
- **Set dressing.** Broken palisade and gate debris (T17); lair mound (T9 trunks plus terrain); 4 ant mounds (T8); 40 pines; 20 blighted snags; tusk-gouged earth decals.
- **Life.** The boss pawing and snorting during the intro; swarms; crows; after victory, birdsong returns and the blight creep withers.
- **Sources.** Tripo: T8, T9, T17, T1; the boss model is a new Tripo (02 §7.2: B01 is "new"). Repo: Thorn Ant, Tusk Boar as the proportions reference. Packs: P1, P2, P4. Shaders: blight haze, grade transition, charge-line telegraph.
- **Today.** No map, no boss model. Risk: the red charge line on busy ground; the apron solves it.
- **ChatGPT prompt.**

```text
Concept painting of one battle map for Dragonhold, a fantasy lane-defence game, seen from its high strategy camera looking 55 degrees down, 16:9, no horizon or sky, land continuing past every frame edge, not a diorama. A blighted forest clearing under a low violet haze. A gigantic moss-covered boar lord with cracked grey tusks and glowing yellow-green eyes smashes through a towering palisade of pine trunks at the top, splinters flying, and charges down a wide trampled earth lane toward an octagonal granite platform where a large red-orange fire dragon rears to meet it. Blight ant mounds at the flanks pour small thorn ants; on the right, a huge lair mound of uprooted pines. The first beam of gold sunlight breaks through the haze. Stylized painterly-realistic, top commercial fantasy strategy quality; pine-green and slate-blue shadows, warm gold light, cream granite, muted violet blight. No text, letters, UI or watermark.
```

---

## 5. Chapters 2–26 (one paragraph each)

Each chapter is 20 stages in one region (04 §2.1, 02 §6.1). Stages 1, 10 and 20 are hand-built and get their own concept page before production; the others reuse the chapter's sites with new layouts, seeds, hours and weather. Kits from 04 keep their signature mechanic; the concept lifts each one to the epic bar with one hero set piece. In every region: no temples, shrines or worship objects (04 §2.1, TD 22.1); forts, bridges, mills and monuments are fine.

**C2 · Pine River, summer · "The Hold Besieged"** (two lanes from here).
- Sites: the Hold's north face (Map 1, Bridge and Brook, opens the chapter), the river meadows, the Upper Dam with two lanes, and both sides of the West Warden.
- Summer: deeper greens, haze, thunderheads building at dusk (cloud shadows, warm-cold contrast).
- Boss: B02 Moss Chieftain marches behind his carved totem pole and steps through the Hold's north gate road (02 §4.5). Hero for S20: the Hold's gatehouse seen from the inside court.

**C3 · Violet Glade, day · "The Lanternwood".**
- A forest of colossal blue-indigo trees, 40–70 m, with sequoia girth; their roots make bridges over pools.
- Signature: glowing mushrooms (type the word on one to put nearby foes to sleep). The mushrooms glow cool white-cyan.
- The glade's colour must lean blue-indigo, never the dull violet-grey of the blight.
- Hero: the Hollow Giant, a dead colossal tree hollowed into a natural hall at the wing.
- Boss: B03 Thorn Queen bursts out of a 20 m golden-grey hive in its crown.

**C4 · Hill Meadow, summer · "The High Downs".**
- Rolling downs above a cloud sea. Signature: hill pads give +25 % range, and the wind changes every wave.
- Hero: the Windwalls, a chain of granite tors 25–40 m tall with a ruined hill fort on one of them; enormous cloud shadows race over the grass.
- Boss: B04 Twin Wolves of Wind and Shadow leap out of two gates at once.

**C5 · Mire, early mist · "The Drowned Causeway".**
- A sunken causeway of the old wardens crosses a misty marsh.
- Signature: foes rise from the water near the pads (bubbles warn 3 s).
- Hero: a colossal dragon statue sunk to its brow, only the horns and eyes above the water, 30 m across.
- Boss: B05 Bog Toad King rises out of the mud beside it.

**C6 · Rainforest, rain · "The Vine Gorge".**
- A jungle gorge in steady rain with a waterfall curtain 60 m wide. Signature: vines open and close lanes, shown on the wave card.
- Hero: an overgrown stone aqueduct spanning the gorge.
- Boss: B06 Web Matriarch drops on silk strung between the gorge walls.

**C7 · Red Canyon, noon · "The Red Gates".**
- The chapter closest to the owner's reference: towering red sandstone walls, wind-cut spires and a cliff city carved with dragon reliefs.
- Signature: rockfall (type the word on the cliff to drop rocks across a lane for 15 s).
- Hero: the canyon gate, two 40 m carved dragon pillars at the wings.
- Boss: B07 Canyon Colossus walks out of a landslide.

**C8 · Rock Coast, sunset · "The Tide Cliffs".**
- Sea stacks and a colossal sea arch. Signature: the tidal flats flood on a 40 s rhythm.
- The wreck of a giant ship lies on the rocks; its ribs are the wing landmark.
- Boss: B08 Tide Crab rises from the surf; the river-side lane slows.

**C9 · Violet Glade, night · "The Moonwood".**
- The Lanternwood under a full moon. Night hazard: foe bodies show only near light; words stay clear. Mushrooms and Firefly Lamps are the lights.
- Hero: the Hollow Giant again, now moonlit.
- Boss: B09 Night Bat Lord eclipses the moon.

**C10 · Volcano, ash · "The Ember Throne".**
- Black basalt fields and ash rain. Signature: lava vents erupt every 20 s and burn both sides.
- Hero: the caldera gate, a dragon maw carved into the crater wall, glowing from inside.
- Boss: B10 Magma Salamander dives into one vent and surfaces at another gate. End of Act I.

**C11 · Pine River, autumn · "The Turning Year".**
- Act II returns to the Hold. Muted ochre larches (kept away from the lanes, since gold is a signal colour) and grey skies.
- Hero: the Elder Grove.
- Boss: B11 Rotwood Ancient is the Elder Pine of S6 itself, blighted, tearing its roots out of the ground.

**C12 · Mire, firefly night · "The Lantern Marsh".**
- The Drowned Causeway at night: thousands of fireflies, the sunken statue lit from below by glowing water.
- Boss: B12 Spore Mother swells out of the reeds.

**C13 · Hill Meadow, storm · "The Thunder Downs".**
- Rain bands and lightning silhouetting the tors; the wind hazard is strongest here.
- Boss: B13 Storm Beetle chains lightning between our magic houses.

**C14 · Rainforest, night · "The Dark Gorge".**
- The Vine Gorge at night, the waterfall glowing with moonlight.
- Boss: B14 Mist Knight rides a ghost horse straight through the curtain.

**C15 · Rock Coast, storm · "The Breakers".**
- Storm waves explode over the sea stacks; the estuary river floods.
- Boss: B15 River Serpent surfaces in two stretches of the river.

**C16 · Red Canyon, night · "The Mirror City".**
- The cliff city by moonlight with mirrors of polished stone in its windows.
- Boss: B16 Raven Sage steps out of the mirrors and copies himself.

**C17 · Pine River, winter · "The Frozen Hold".**
- The Hold under deep snow: the cascade and the Upper Dam's dragon mouths frozen into ice, the West Warden capped with snow.
- Lanes are swept dark so word tags stay readable.
- Boss: B17 Frost Stag spreads ice down the lanes.

**C18 · Violet Glade, bloom · "The Flowering Wood".**
- The Lanternwood in bloom: pale blossom drifts in the light.
- Boss: B18 Deep Centipede bursts up from under the roots in a ring of cracked earth.

**C19 · Volcano, eruption · "The Burning Sky".**
- The volcano erupting: a lava lake, ash fall, the sky light red-black (light only, not red ground).
- Boss: B19 Black Wyrm fights Hỏa Long dragon to dragon over the lava.

**C20–C25 · The Black Mist (Act III).**
- Each earlier region returns under the Black Mist layer: a grey-violet grade, withered props, mist volumes and the chapter's Black Mist rule (04 §2.2).
- The chapters:

| Chapter | Region | Mist rule | Twin bosses |
|---|---|---|---|
| C20 | The Red Gates | Mist spreads | B07 + B11 |
| C21 | The Drowned Causeway | Dead foes leave healing pools | B05 + B12 |
| C22 | The Lanternwood | Generals rise once | B09 + B16 |
| C23 | The Tide Cliffs | The tide moves lanes | B08 + B15 |
| C24 | The Ember Throne | Ash puts out traps | B10 + B13 |
| C25 | The Hold in ruins | — | B14 + B19 |

- In C25 the West Warden is broken, the stone bridge has fallen and the rampart is breached: the most moving map of the game, because the player knows this place.

**C26 · The Mist Rift · "Heart of the Mist".**
- The source of the blight: a colossal chasm in the world with floating granite islands, violet mist pouring upward, and three lanes on bridges between the islands.
- Boss: B20 Mist Mother, with three hearts on three lanes. Each phase turns the mist a new colour.
- Hero: the rift itself, seen as depth below the islands (the lower corners and wings show the drop).

---

## 6. Why the current maps fail (Dragonhold)

1. **We built a system, not places.**
   - The plan makes 520 maps from 16 layout templates × region kits × seeds (04 §3.1, §11). The only built map was dressed by rule: forest bays every 60–90°, groves with sand rings, warm crowns, footpaths to a pond.
   - Rules produce a generic meadow. There is no place, no story and no landmark a player would remember or screenshot.
   - Commercial games hand-compose every map around one set piece.
2. **We tuned to the wrong reference and judged ourselves.**
   - The map pilot moved the palette "toward the reference's soft light green" (`paint.ts` `PILOT_GROUND`), which is the old cozy village reference, not the 28/10 epic bar.
   - We scored 7.1 on our own scale; on the market scale the map is 6–6.5, and the owner calls it toys.
3. **The camera hides everything epic, and we made the epic parts for cameras the player does not use.**
   - At 55° from 78 m the sky, the horizon and the mountains never show.
   - The dawn sky and mountain ring (120) and the title art (119) show only on the title screen. The playfield, which the player looks at 95 % of the time, stayed a lawn.
   - Epic has to live inside the 100 × 64 m patch: colossi on the wings, a rampart along the bottom, drops at the corners, gates and musters in the top band (section 1).
4. **Everything is at human scale under a 95 m camera.**
   - Cliffs of 7.8–9 m and trees of similar size read as a 1:100 diorama.
   - Nothing on the map is ten times a soldier. The six landmarks drawn for this (ticket 124) were never made into 3D models.
5. **Toy rendering by construction.**
   - Lambert materials with a 3-step ramp, flat-shaded rocks, sphere-normal crowns and no normal or roughness response.
   - Tree and rock meshes cut by 84–91 % and stripped of their maps.
   - Ultra cannot fix this: the look is in the materials and the processing, not the quality tier.
6. **Light and colour are flat and off-script.**
   - Sun at 50° from the east; hemisphere fill 2.7; a violet ground bounce; mist only past 47 m.
   - Saturated green grass, bright blue water and red crowns, where the bible asks for pine green, slate blue, cream granite and a low gold dawn.
7. **Water, paths and the bridge, the three things the player looks at most, are the weakest.**
   - The river is a uniform ribbon with cartoon specks.
   - The paths are the smears `PATH_QUALITY.md` bans.
   - The choke point is a plank footbridge.
8. **The shipped build is worse than dev.** The play host loads no ground textures at all (`buildGroundPaint`, dev-only tiles). The owner judged a flat green that we never looked at.
9. **No life.** No garrison, no muster, no birds, no smoke, no banners. Foes appear from nowhere at the lane end. An epic map needs things that move and a threat you can see coming.
10. **The process skipped the target.** No map had an approved concept painting before code. We iterated on knobs (bays, groves, tints) without a picture of what "done" looks like.
    - The fix is in this document: concept first, ChatGPT critique, an accepted painting, then a build matched to it side by side at 1280×720, judged blind by two judges against the owner's reference.

---

## 7. What needs the owner

- **Tripo models.** Make T1–T3 first (Platform, stone bridge, Warden colossus), then the six landmarks of ticket 124, then T4–T17 as chapter 1 is built. That is about 23 models, roughly 690 credits before retries, out of the ~4,000 web credits.
- **Old scenery models** (pine-round, tree-violet, bushes, rocks, cliff blocks). The owner's 29/10 rule keeps existing models until he asks. Recommendation: leave the files, stop using them in the new maps, and replace them with P2 pack conifers and rocks or fresh Tripo at full detail (`MODEL_QUALITY.md` §2).
- **Garrison.** Reuse the Grove Warden as the Hold's garrison and workers in chapter 1, instead of new human models. Recommended.
- **Backdrop ring (120).** Its painted gate must sit at the south bearing of Map 1, where the 3D Hold stands, or be painted out, so the title camera and the play camera show one world.
