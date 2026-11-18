# Dragonhold · Map Concepts (v1.2, 01/11/2026)

**Version.** v1.2, 01/11/2026: map 1 folds in ChatGPT's art-director review (8.1/10, `dragon-hold-CHATGPT_REVIEW.md`) and carries its image prompt; chapter 1 and the later chapters take its notes. Layout and camera unchanged.

**What this is.** One concept per map, written before any map is built, for the owner to review and to send to ChatGPT (normal chat, High reasoning, not the work mode) for critique and a concept painting. A map is built only after its painting is accepted; the build is then judged against that painting, side by side at 1280×720.

**Why.** Owner, 01/11/2026: the maps of all three games are "not acceptable". For Dragonhold the trees, rocks, water and ground look like toys even at Ultra (today's honest score: 4/10, `QUALITY_RESCUE_2026-11-01.md` §1). The bar (`AGENTS.md`): commercial fantasy game art, epic, majestic, cinematic light, judged against the owner's reference `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`. **Acceptance is 8.5**, from two blind judges. Everything the player reads is English. Nothing the player sees is a code-drawn stand-in; shaders that meet the VFX standard are fine.

**What exists today.** One playable map: **Stage 1 · Bridge and Brook** (`m0-l2-cau`, layout `L2-cau`, 10 waves, chapter-2 strength). The campaign in `dragon-lane/04-stages-maps-progression.md` plans 520 stages (26 chapters × 20), 8 region kits, the Black Mist layer and the Mist Rift. No other map is built.

**What this document covers.**
- Section 1: the camera, measured with one projection script; the sky decision; HUD zones.
- Section 2: the kit (repo, Tripo, free packs, systems, creatures).
- Section 3: Map 1 in full, with its base image and its concept painting prompt.
- Section 4: Chapter 1 (20 stages), short.
- Section 5: Chapters 2–26, one line each.
- Sections 6–7: why the current maps fail; what needs the owner.

## Changes in v1.1 (revision 2, 01/11, after the critic)

- **Owner decisions of 01/11** (`docs/OWNER_QUEUE.md`):
  - Painterly-realistic replaces the "painted toy diorama" (O1).
  - Camera trial O3 (pitch 50°, zoom 0.85): every map 1 position is given for both cameras.
  - Only the six landmarks of ticket 124 go to Tripo for now; their sources failed the 8.5 gate and are being redone with Firefly (`TRIPO_TODO.md`).
  - Trees and rocks come from free packs first.
  - Reuse monsters from `MONSTER_MODEL_INVENTORY.md` before making new ones.
  - Free, commercial-safe assets only, verified (`FREE_ASSET_SOURCES.md`).
  - Acceptance bar 8.5.
- **Critic's fixes.**
  1. ChatGPT paints over a base image taken from the real game camera (section 3.8). The prompt covers only light, materials, mood and scale.
  2. Every screen coordinate comes from one script (section 1). No sky and no horizon in play: the image shows none.
  3. The doc follows the owner decisions above.
  4. Life first: muster grounds at both gates, defenders where the player looks, the dragons. Animals with no verified source are removed (crows, hawk, fox, deer, ducks, heron, ibex and others).
  5. The Tripo list is ordered by measured share of the battle frame.
- **Map 1 changes.** The positions moved where the measurements required it:
  - The West Warden moves from (−37, −7) to (−33, −8), so it reads at both cameras.
  - The gatehouse leaves the map 1 frame: at 16 m it would reach screen y 503 and cover both south house pads.
  - The rampart drops to 8 m at z +18…+20, so it clears the south pads even at 40° tilt.
  - One watchtower, at the rampart's east end.
  - The braziers move to flank the north stair.
  - The north muster stands beside the arch, not behind it.
  - HUD zones are remeasured from the DOM.
- **Shorter.** Chapter 1 and chapters 2–26 lose their ASCII maps, per-stage prompts and hand-estimated screen points. Each stage gets a base image and a prompt when its grey box exists.

---

## 0. How ChatGPT reviews a map

1. Lay the map out in the game (grey box is enough).
2. Capture it at 1280×720 from the battle camera on the play host, canvas only (word tags and HUD hidden).
3. `make-base.mjs` draws each planned piece as a flat translucent block at its projected position and height, and greys the HUD.
4. Write a legend mapping colours to pieces.
5. ChatGPT reviews the concept as a senior art director and writes the image prompt. The painting is made **over** the base image (ChatGPT image in Chat mode with High effort, or Adobe Firefly Image 5 with the base image as composition reference): same layout, same camera, HUD zones grey, no text. The prompt locks the layout and changes only the look.
6. Two blind judges score the painting against the commercial board. It needs 8.5.

Reject and repaint if:
- it looks like a miniature, diorama or floating island;
- a lane is not the clearest ground;
- a tall object hides a lane;
- two landmarks compete for the eye;
- red, orange, gold or turquoise covers large areas;
- there is any text, number or interface;
- a horizon or sky shows;
- the layout or camera moved off the base image.

Map 1's paste-ready message is `docs/games/maps/dragon-hold-CHATGPT_MESSAGE.md`; its review is `docs/games/maps/dragon-hold-CHATGPT_REVIEW.md` (8.1/10), folded into section 3 in v1.2.

---

## 1. The game camera and what it can show (every map)

**One script.** `games/dragon-hold/tmp/map-concepts/project.mjs` (not tracked) reproduces the rig of `src/view/camera.ts` and `src/view/stage.ts`:
- perspective camera, 30° vertical field of view;
- position = look point + (sin yaw·cos pitch·d, 0.6 + sin pitch·d, cos yaw·cos pitch·d);
- `lookAt` the look point at 0.6 m (the dais top).

It was checked against the game's own `__dh.project()` on the play host (`?debug=1`, 01/11) at 9 world points in both cameras below: every point matched to the pixel. Run `node project.mjs [--cam=default|o3|tilt40|overview] [--pt=x,y,z]`. World metres: x east, z south, y up, platform at the origin.

**The two cameras.**

| | Default (shipping) | O3 trial |
|---|---|---|
| View | yaw 0, pitch 55°, 95 m, look (0, −4) | pitch 50°, zoom 0.85 (80.75 m), same look |
| Camera position | (0, 78.4, 50.5) | (0, 62.5, 47.9) |
| Ground at the top edge | z −43, x ±56 | z −41.3, x ±50 |
| Ground at mid-height | z −4.4, x ±45.6 | z −4.5, x ±38.8 |
| Ground at the bottom edge | z +21.9, x ±38.4 | z +18.8, x ±31.7 |
| Platform centre | (640, 412) | (640, 419) |

The player can tilt 40–75°, zoom 0.6–1.3× and rotate freely; the overview is 75° at 1.22× (`CAMERA_LIMITS`).

**Sky: never in play.** The horizon sits far above the top edge at every allowed tilt and zoom:
- y −767 at 40°;
- y −1241 at O3;
- y −1559 at the default.

So the battle image shows **no sky and no horizon**. Land runs past every edge. Mountains, sky and the painted backdrop ring (ticket 120) are for the title and results cameras only, and appear in play only as reflections in water.

**What it means for the epic.**
- The epic has to be built inside the roughly 100 × 65 m patch of ground the camera sees.
- Tall things lean outward and up: on the wings toward the frame edges, in the bottom band up toward the play.
- In the top band, a piece at z −36 shows whole only up to 5.9 m (3.8 m at O3); an 8 m arch at z −30.5 just fits at the default (top at y 25) and crops 5 px at O3.
- Drops below ground show only toward the camera: the lower corners, which sit under the HUD panels.

**HUD zones at 1280×720** (measured from the DOM on the play host, 01/11; prep and wave layouts):

| Zone | Box (x, y) | When |
|---|---|---|
| Status bar | 13–304 × 11–59 | always |
| System buttons | 1083–1268 × 11–56 | always |
| Dragon panel | 13–358 × 600–708 | always |
| Typing bar | 448–832 × 637–707 | always |
| Loadout strip | 840–1267 × 614–709 (prep and breaks); 947–1267 × 664–709 (waves) | always |
| Wave card | 13–341 × 67–293 at wave 1 (smaller later). It tries the top left, then the top right, then the top centre, and never covers a lane or a slot (`screen-zones.ts`) | prep and breaks |
| New-foe card | 1027–1267 × 80–192 | a few seconds when a new foe enters |

**Landmark slots** (recomputed with the script):

| Slot | World | Height budget | Default: base → top | O3: base → top | Notes |
|---|---|---|---|---|---|
| Left wing | x −31…−35, z −14…0 (outside the 32 m play circle) | 22 m whole at the default | (−33, −8): (187, 320) → 22 m (84, 98) | (111, 317) → 17 m (70, 102); higher parts crop at the left edge | Under the wave card in breaks; keep the key read (a face) below y 100 |
| Right wing | mirror, x 31…35 | same | (33, −8): (1093, 320) | (1169, 317) | Clear in breaks. With a sky lane, nothing over 10 m south of the lane's entry |
| Top band | z −30…−40 | ≤ 6 m at z −36; 8 m at z −30.5 | (8.8, −30.5): (747, 101) → 8 m (754, 25) | (760, 88) → 8 m (768, −5) | Gates, arches, musters, the forest edge |
| Bottom band | z +18…+20 | walls ≤ 8 m | wall top (0, 8, 17.75) at y 598 | y 622 | 8 m clears the south pads at every tilt (40°: wall top y 512, pads y 487). A 16 m gatehouse reaches y 503 at the default and covers the pads |
| Lower corners | x ±30, z +15…+22 | — | under the dragon panel and the loadout strip | same | Mood only |

**Readability rules** (05 §2.2, §3; `PATH_QUALITY.md`):
- Lane core luma ≥ grass + 0.15.
- Ground under the word-tag band ≤ 0.6 luma: no snowfields, pale quarry floors or sunlit water behind tags.
- Red `#FF4A4A`, orange `#FFB020`, gold `#FFC83A` and turquoise `#7FF5E0` are signals: never large fields on the map. The blight's yellow-green `#C8D24A` lives only in foe eyes and cracks.
- Anything between the camera and a lane or a word tag dithers to 35 %.
- Lanes are 24–40 m long; two lanes stay ≥ 8 m apart except where they merge.
- Gates sit inside the default frame. Trap, block and house slots show only once the stage has unlocked them (04 §6.1).
- Scale: characters are drawn 1.4× against the scenery. A hero landmark is at least ten times a Moss Grunt as drawn (1.56 m × 1.4 ≈ 2.2 m → ≥ 22 m).

---

## 2. The Pass Kit: what every map is built from

### 2.1 Already in the repo

| Piece | Path | State |
|---|---|---|
| Hỏa Long, Inferno form, Bạch Long | `public/assets/dragon-hold/models/heroes/draconis-v2` (rigged, 25 bones), `heroes/draconis-v3`, `guides/draconis-v4` | In game |
| Foes of chapter 1 | `models/m0b/enemies/{moss-grunt, moss-archer, blight-wolf, tusk-boar, thorn-wasp, thorn-ant}`; general `moss-banner` (Moss Bannerman, G01) | In game. The shipped files are cut (1,707–4,325 triangles, no normal maps). Any rebuild starts from the Tripo originals in `art-src/3d/` (inventory §3) |
| Our side | `models/m0b/units/moss-warden` (Grove Warden), `m0b/props/herb-hut`, traps `spikes`, `pine-bomb`, `net-launcher` | In game |
| Six landmark source images (ticket 124) | `art-src/landmarks/{hold-gate, hold-wall, watchtower, dragon-statue, ruined-arch, brazier}.png`; heights gate 16 m, wall 10 m, tower 14 m, statue 12 m, arch 8 m, brazier 3 m | **Failed the 8.5 gate** (M 5–7.5, judges J and K, 01/11); being redone with Firefly in the painterly-realistic style; no credits spent |
| Backdrop ring (ticket 120) | `art-src/backdrops/pass-epic/` | Title and results camera only; never in the battle frame |
| Granite road art (ticket 155) | `art-src/ground-v3/road/` | Awaiting judging |
| Fire for braziers | fire C flipbooks and Kenney CC0 particles (`THIRD_PARTY.md`) | In game |

### 2.2 Tripo, ordered by what the battle frame shows

**Frame share** = pixels of the piece's projected box in the 1280×720 battle frame that are not under the HUD. It is measured by `make-base.mjs` on map 1 and is a proxy for "how much the player sees". The order is the same at O3.

**Now: the six landmarks of ticket 124.** The owner builds them on the Tripo web once the redone sources pass 8.5 (`TRIPO_TODO.md` rows 1–6, 40 credits each).

| Rank | Model | Map 1 use | Frame share: default (O3) | Note |
|---|---|---|---|---|
| 1 | `dragon-statue` | The West Warden, scaled ×1.8 (≈22 m), crouched on a cliff ledge | 74,920 px, 8.1 % (65,824 px) | The hero. The new source must be colossal: a big head, wings with depth, weathered granite, rooted in broken rock so it can grow out of the cliff (3.2) |
| 2 | `hold-wall` | The Hold's north rampart, 8 m, along the bottom band | 25,560 px, 2.8 % (20,852 px) | Only the battlements and wall walk show above the HUD; the wall face matters little in this map. The source carries the Hold's masonry language (3.4) |
| 3 | `watchtower` | Rampart east end, (29, 15) | 23,764 px, 2.6 % (18,412 px) | Same masonry language as the wall (3.4) |
| 4 | `ruined-arch` | North gate, the Bridge Lane comes out under it | 10,556 px, 1.1 % (11,968 px) | Also the hero of S10 at ×2 |
| 5 | `brazier` | Two flank the platform's north stair; four on the wall walk | 4,280 px, 0.5 % (4,492 px) | Small but the brightest points after the dragon; at the centre of play |
| 6 | `hold-gate` | Not in the map 1 frame | 0 | First needed in S1 (the Hold's East Gate, left wing) and S17 |

**Not asked** (the owner allows only the six for now). They are listed by frame need, so the next ask is ready:

| Rank | Model | Why | Until then |
|---|---|---|---|
| N1 | Dragon Platform: octagonal cream-granite bastion in the Hold's masonry language (3.4), 8 m across, three stairs, two brazier sockets | At the centre of every map (≈ 8,800 px) | The current terrain dais with PBR granite (ambientCG) |
| N2 | Old single-arch granite bridge, damp and mossy, about 8 m span, deck 3.4 m | Map 1's choke point at the top centre (6,588 px); also C2 | The plank bridge stays; it is on the retire list once the stone bridge exists |
| Later | One hero piece per chapter-1 stage (section 4: beacon basket, mill, dragon pillars, hive, mast, dam, causeway, Elder Bones, aqueduct, keep and granary, palisade) | Each is measured with its own stage's base image before it is asked | — |

### 2.3 Free, commercial-safe sources (verified on the source page, `FREE_ASSET_SOURCES.md`)

**Licence rule** (owner, 01/11; `SHARED_SYSTEMS_BAR.md` §5):
- Allowed: CC0, the Quaternius Asset License, MIT, BSD, ISC, Apache-2.0, MPL-2.0, Zlib. CC-BY only with a credit line.
- Never: NC, ND or GPL; Mixamo, Fab or Sketchfab Standard; anything tagged NoAI; models taken through the Poly Pizza service into AI tools; code-built trees (ez-tree).
- Each download is recorded in `THIRD_PARTY.md` with its date and version.

| ID | Kind | Source (licence) | Use |
|---|---|---|---|
| P1 | PBR textures: granite and cliff, forest floor, river gravel, moss, mud, snow, travertine, ash | ambientCG (CC0), Poly Haven textures (CC0), cgbookcase (CC0) | Terrain splat and triplanar cliffs, regraded to the colour script |
| P2 | Rocks, cliff faces, boulders, river stones; conifers | Poly Haven models (CC0): rock faces such as Rock Face 01 (20 k triangles), the Pine Forest collection, checked per asset. Quaternius Stylized Nature MegaKit (QAL) only if it holds up next to scans | Cliff walls, scree, boulders, forest walls and groves (they replace the round-crown props) |
| P3 | HDRI | Poly Haven HDRIs (CC0) | Lighting and reflections (they replace `RoomEnvironment`); never shown as sky |
| P4 | ~~Animated birds and animals~~ | **None verified** | No ambient animals until a verified source exists |
| P5 | Particles and flipbooks: spray, steam, dust, embers, smoke, fire | Kenney (CC0, in use), Unity Labs flipbooks (CC0), JangaFX VDBs (CC0, rendered in Blender) | Cascade spray, mist, embers, brazier and beacon fire |
| P6 | Code | three r170 add-ons (MIT): `Water2`, `CSM`, `GTAOPass`, `SMAAPass`, `LUTPass`, `GodRaysShader`, `GroundedSkybox`. `three-custom-shader-material` (MIT); Quick_Grass (MIT, code only); pmndrs `postprocessing` (Zlib, owner 01/11) | Systems in 2.4 |
| P7 | Ambience: river, waterfall, wind in pines, horns | Real files through `AUDIO_PIPELINE.md` (the owner makes SFX in Firefly) | Map ambience |

### 2.4 Systems Claude builds (shaders and code, no drawn stand-ins)

- **Painterly-realistic look (O1).** Move scenery from `MeshLambertMaterial` with a 3-step ramp to physically based materials with normal, roughness and AO maps. The painterly feel lives in the grade, not in the shading.
- **Light.** Poly Haven HDRI for image-based light; cascaded shadows for long dawn shadows; GTAO contact shadows; SMAA; a filmic tone map and one colour lookup per map and hour. Bloom only on fire and magic.
- **Terrain.** Real cliffs from the height field with triplanar granite (P1), up to 30 m. Retire the "cliff blocks widened into a face".
- **Water.**
  - Rivers: flow-map shader (`Water2`) with depth colour, Fresnel, sun specular, foam from speed and around rocks and piers, rapids on drops. A per-map foam mask limits where foam shows (map 1: piers, cascade and stepping stones only, 3.4).
  - Waterfalls: a mesh with scrolling foam, spray particles and mist cards.
- **Atmosphere.** Height fog pooled in river beds and hollows; light shafts at dawn and dusk; cloud shadows crossing the map every 10–15 s.
- **Wind.** One wind field for pines, grass, banners (cloth vertex shader) and pennants.
- **Grass.** 40–60 k instanced tufts (Quick_Grass method), kept 1.5 m off lanes and slots.
- **Blight.** An animated, low violet haze at the gates (thin and see-through on map 1, 3.4), Black Mist volumes, and grass that withers along a lane after a wave passes.
- **Muster ground (view only).** During the build phase and the wave warning, the next wave's first groups stand at their gate: idle foes in the shade with glowing eyes. They walk onto the lane when the sim spawns them. The sim never reads it; the golden hashes stay the same.
- **Occluder dither** (05 §3) for anything between the camera and a lane or a tag.

### 2.5 Retire from the new maps (the files stay; the 29/10 rule keeps existing models)

- `props/pine-river-pine-round` (round crowns), `tree-violet` near lanes, `bush-blossom`.
- The "warm crowns" rule (red-to-rust crowns, `scatter.ts` V7).
- `kit3` `cliff-rock-a/b` as cliff builders.
- `wooden-jetty`, `rail-fence`, `lantern-post` as park furniture.
- `bridge-old` (plank footbridge), once the stone bridge exists.
- The pond with lily pads.
- The pilot meadow palette `PILOT_GROUND` (`paint.ts`).
- Placeholder stepping stones in `water.ts`.

### 2.6 Creatures: only what has a source

- **In the game now:** Hỏa Long, Bạch Long, Moss Grunt, Moss Archer, Blight Wolf, Tusk Boar, Thorn Wasp, Thorn Ant, Moss Bannerman, and the Grove Warden on our side. The Grove Warden is also the Hold's garrison and workers in chapter 1.
- **Reuse before new** (`MONSTER_MODEL_INVENTORY.md` §6.2). Examples:
  - `troll` (Wordwoven, rigged) → Forest Ogre and Drum Ogre.
  - `thuong-luong` → River Eel and boss B15.
  - `lieutenant-nature` → B13.
  - the Space `shadow` family → the mist foes.
  - `moc-tinh` → B11.
  - `tusk-boar` scaled → B01 Tuskfather.
- **No source yet** (inventory §7): bats, moths, toads, stags, bears, spiders, crabs, centipedes, the canyon colossus, the raven sage, the ghost horse. Concepts may name these bosses, but they are open requests, not props.
- **No ambient animals** (birds, deer, fish and the like) until a verified free source exists. Life comes from foes, defenders, the dragons, fire, water, wind, banners and smoke. Fireflies and embers are particles, not creatures.

---

## 3. Map 1 (playable today) · Bridge and Brook · `L2-cau`

**Story beat.** The blight comes down the valley to the Hold's north face. Hỏa Long holds the river crossings below the West Warden, the stone dragon that has watched this pass for a thousand years. The picture is a dialogue between the two: living fire on the platform, dead stone on the cliff.

**What v1.2 changes.** Only the look (sections 3.2–3.6 and 3.8); the layout of 3.1 and the camera stay. Where ChatGPT's review and v1.1 disagreed, the review wins unless it would move gameplay or readability; each case is marked in one italic line.

### 3.1 Gameplay layout (sim unchanged: lanes, slots, river path and golden hashes stay)

- **Defended point:** the Dragon Platform at (0, 0), radius 4 m.
  - Hỏa Long hovers 2.5 m above it.
  - Bạch Long stands at the south-west edge (−2.6, 2.0).
  - The word zone is the 26 m ring.
- **Bridge Lane** (main lane in waves 1–3 and 7–8).
  - From the north gate (8.5, −29), 3 m wide, down to the platform's north stair.
  - Crosses the river on the bridge, 10.5–18.4 m along the lane, deck 3.4 m: the choke point.
  - Four trap slots, one on the deck; two block points.
- **Brook Lane** (main lane in waves 4–6 and 9–10).
  - From the west gate (−30, 7), 2.6 m wide.
  - Wades the stream at the ford, 6.9–14 m along the lane: 30 % slower, Wet for 4 s.
  - Three trap slots, none in the ford; two block points.
- **Sky Lane.** From (30.5, −8.5) at 3 m altitude, over the east meadow. Thorn Wasps from wave 2.
- **River.** Enters from the north-east 8 m wide, crosses the upper third at z ≈ −15, bends south-west past the ford and leaves the lower left as a 4 m stream.
- **House pads:** four on the inner ring (NW, NE, SE, SW at 7–9 m) and two outer pads by the crossings, (9.5, −11) and (−14, 6.5).
- **Camera:** unchanged (section 1).

**Screen positions at 1280×720** (`project.mjs`):

| Feature | World | Default | O3 |
|---|---|---|---|
| Platform centre | (0, 0) | (640, 412) | (640, 419) |
| Hỏa Long | (0, 2.5, 0) | (640, 392) | (640, 392) |
| Bạch Long | (−2.6, 0.6, 2) | (602, 432) | (595, 440) |
| North gate (lane start) | (8.5, −29) | (744, 114) | (757, 101) |
| Bridge centre | (2.7, −15.8) | (676, 237) | (681, 229) |
| Bridge Lane end (north stair) | (0.4, −6) | (646, 342) | (647, 341) |
| West gate (lane start) | (−30, 7) | (188, 501) | (96, 520) |
| Ford centre | (−20.7, 2.4) | (337, 442) | (279, 452) |
| Sky Lane entry, 3 m up | (30.5, −8.5) | (1069, 289) | (1141, 278) |
| River entry (NE) | (38, −25) | (1115, 149) | (1179, 137) |
| South house pads | (−5, 6.5), (5.5, 6) | (565, 494), (722, 488) | (550, 512), (739, 505) |
| Stream exit | (−38, 22) | below the frame, under the dragon panel | off frame |

Both gates, both crossings and the platform sit in the clear middle of the HUD at both cameras. At O3 the west gate moves to x 96, close to the left edge.

### 3.2 Hero landmark: the West Warden

- **What it is.** A colossal stone dragon that grows out of the west granite wall: the 124 `dragon-statue` scaled ×1.8 (≈22 m to the folded wing tops, head at ≈17 m). It crouches on a ledge with its wings folded and its head turned east, toward the bridge and the platform.
  - It is carved from the mountain, not set on it: the wing roots sink into the rock, the talons merge with cracked ledges, and the cliff's erosion lines run on across the sculpture.
  - Its two eyes are iron fire basins, dead and black until the map is won, so the living fire dragon keeps the strongest fire.
  - With Hỏa Long it carries the map's main visual dialogue (3.3).
- **Where it sits.** Centre (−33, −8), 34 m from the platform, outside the play circle, 15 m north of the Brook Lane's start and 18 m west of the river.
  - Default: base (187, 320), head (159, 157), wing tops (84, 98), all below the status bar.
  - O3: base (111, 317), head (70, 102); the wing tops crop at the left edge on purpose.
  - Dawn gold falls only on its east planes (brow, muzzle, shoulder, the leading edge of the folded wing); the rest stays cool granite in shade. It leans outward, away from the play.
  - Behind it the **west granite wall** (terrain with CC0 rock scans): 25–30 m, x −46…−37, z −34…+3, with three ledges and scree fans, running off the top-left corner. Fractured cool grey granite with oversized fractures (5–10 m long), not the Hold's cream blocks (3.4).
- **Scale cues.** Only young pines, 4–8 m, at its feet and on its ledges, so they read very small against it; the 14–24 m forest wall stays north of it and off its silhouette. The two lookouts on its shoulder ledge (3.5) give the human measure.
- **Build notes.**
  - Sink the Tripo statue 2–3 m into the cliff terrain; sculpt the height field's ledges up to its talons and wing roots.
  - One world-space triplanar granite (P1, cool grey) on both statue and cliff, so erosion lines, lichen and moss streaks run across the seam; GTAO and a scree-and-moss blend hide what is left of it.
  - The redone 124 `dragon-statue` source shows the statue rooted in broken rock, so Tripo gives a base that can merge (`TRIPO_TODO.md` row 1).
  - Eye basins: no emissive and no fire until victory.
- **Break-time conflict.** In prep and breaks the wave card prefers the top left and covers the Warden's head (13–341 × 67–293 at wave 1). Request to the UI lane: add the Warden's screen box to the wave card's keep-out zones (`screen-zones.ts`), so on this map the card goes to the top right or top centre. In waves the left wing is clear.
- **Supporting pieces.** They frame the hero and never compete with it. The north gate, the watchtower and the cascade sit 15–25 % below the Warden in contrast and detail: in shade, with flatter texture contrast and fewer small details.
  - **North gate.** The 124 `ruined-arch`, 8 m, at (8.8, −30.5); the Bridge Lane comes out under it. Screen: base (747, 101), top (754, 25). It stands in pine shadow; a low, thin violet haze seeps out under it (3.4).
  - **The Hold's north rampart.** 124 `hold-wall` segments, 8 m, at z +18…+20 from x −28 to +28.
    - It frames the foreground as a heavy dark band along the bottom: shadow side, slightly oversized battlements (fewer, larger merlons), dark pine crowns beyond both ends in the lower corners.
    - The battlements grow in proportion only; the wall top stays at 8 m (y 598) so the south pads stay clear at every tilt. *The review's "oversized" does not raise the wall (gameplay).*
    - Its battlements and wall walk show as a strip at y ≈ 590–637 above the typing bar; the face is under the HUD.
    - The road from the platform's south stair runs to a gate passage behind the typing bar. The gatehouse itself is out of frame.
  - **Watchtower.** 124 `watchtower`, 14 m, at the rampart's east end (29, 15): base (1101, 613), top (1173, 505). At O3 its top crops at the right edge. Mostly in its own shade, lit along one edge only.
  - **Braziers.** 124 `brazier`, 3 m:
    - two on the platform at (±2.9, −2.9), flanking the north stair where the main lane arrives, clear of Bạch Long and the Sky Lane's end (747, 366);
    - four on the wall walk, burning low with no bloom, so the foreground band stays dark (3.3).
  - **The cascade.** The river drops twice (3 m and 2 m) at x 36…46, z −29…−23: screen 1080–1235 × 87–168. A pale vertical rhythm, partly hidden by pines in front of it (all outside the play circle, none over the Sky Lane); foam and spray only at its two drops. No extra structures there. The new-foe card covers it for a few seconds when it shows. *v1.1 made it a white-water eye-catcher; the review wins.*
  - **The bridge.** An old single-arch granite bridge (not asked yet, 2.2 N2) replaces the plank bridge, same place and length: screen 633–718 × 169–285. Older and wetter than the Hold: darker damp stone, moss on the arch ring and spandrels, wet stains under the deck line. Dawn gold only on the parapet crowns; foam only at the piers.

### 3.3 Depth layers, focal order, light and colour

| Layer | Content |
|---|---|
| Foreground frame (bottom band, mostly under the HUD) | A heavy dark band: rampart with slightly oversized battlements, the east watchtower, four braziers, banners; dark pine crowns in both lower corners. Shadow side, 25–35 % darker than the playfield |
| Playfield (≤ 32 m) | Subdued olive meadow, no gold patches; low granite outcrops. The river in a real bed: gravel bars, boulders, foam only at the bridge piers and the ford's stepping stones. The two lanes, each in its own material (3.4), are the clearest and brightest ground. Within 2–4 m of a lane edge or the platform the ground stays simple: short grass, a few low stones and puddles |
| Wings (32–46 m) | West: the fractured grey wall, its ledges, the Warden with young pines at its feet, two scree fans. East: a forested ridge with the cascade half hidden in pines, and a blighted dead pine at the Sky Lane's entry where the wasps gather |
| Far band (top, z −32…−43) | The pine forest wall climbing north, darker and softer than the playfield (lower contrast, no fine detail). A low, thin violet haze at the north gate. The muster ground, half lost in pine shadow |
| Sky | Never in frame (section 1). Present only as river reflections (cool slate blue with narrow warm highlights, never a gold sheet: the light budget below), cloud shadows every 10–15 s and faint light shafts through the river mist |

**Depth.** The platform and the lanes are crisp. A slight mist lies in the river bed in the middle distance (0–3 m deep). The top pine wall reads farther because it is darker and softer, not because of fog. No uniform fog over the map.

**Focal order** (what the eye reads, in this order):
1. Hỏa Long over the platform and the West Warden: the main dialogue, living fire against dead stone, the Warden's head turned to the dragon.
2. The platform and the two lanes: the crispest and brightest ground.
3. The bridge (the choke point) and the ford.
4. The north gate and its muster: shadow and tiny eyes.
5. The rampart, the watchtower and the cascade: the frame, never the subject.

**Light budget and value hierarchy.**
- **Time:** dawn. **Sun:** bearing 70° (east-north-east), elevation 24°: dawn gold from the upper right, long deep pine-green shadows falling west-south-west toward the lower left.
- **Brightest:** Hỏa Long's fire and the two platform braziers. Only they bloom.
- **Dawn gold lands on four things only:** the Warden's east planes, the bridge's parapet crowns, the platform rim and selected grass edges. The Warden's east planes are the largest lit mass and stay under 0.75 luma.
- **Lanes:** core luma ≥ meadow + 0.15, and ≤ 0.6 under the word-tag band (section 1).
- **Meadow:** subdued olive; with the lane rule it stays at about 0.45 luma or below. *v1.1 had gold sun patches on the meadow; the review wins.*
- **Supporting landmarks:** watchtower, cascade, north gate 15–25 % below the Warden in contrast and detail.
- **Top band:** the pine wall darker and softer than the playfield.
- **Foreground band:** 25–35 % darker than the playfield.
- **Weather:** clear, light breeze. Mist 0–3 m deep in the river bed; spray at the cascade; light shafts stay faint, never a gold field.

**Colour reservations.**
- Shadows: deep pine green and slate blue.
- Dawn gold: only the four places above.
- Granite: four families (3.4): cream blocks for the Hold, cool grey for the cliff and the Warden, dark damp stone for the bridge, worn polished flags on the Bridge Lane.
- River: dark slate-teal; white only at the piers, the cascade and the stepping stones; never turquoise.
- Ember orange and red: only Hỏa Long and the braziers. The banners are a dark, weathered ember cloth in shade, well below the signal orange.
- Violet: only the thin haze at the two gates and the Moss Bannerman's banner.
- Yellow-green `#C8D24A`: only foe eyes and blight cracks.

**Style.** Painterly-realistic (O1). Real material response (wet stone, lichen, bark, needles) with a painterly grade, never toy plastic.

### 3.4 Materials and set dressing

**Materials** (each family keeps one language, so granite, grass and pine do not repeat):

| Family | Look | Build note |
|---|---|---|
| The Hold (rampart, watchtower, platform) | Huge fitted cream granite blocks in large courses (1–1.5 m), dark iron cramps, worn chamfers, drainage grooves, lichen in sheltered joints, patches of repaired masonry. Narrow wall stairs (about 1 m). The rampart is the heaviest piece | The redone 124 `hold-wall` and `watchtower` sources and the N1 platform ask carry this language, so Tripo bakes it; decals add the repairs and joint lichen |
| Cliff and the Warden | Fractured cool grey granite, oversized fractures 5–10 m long, lichen and moss streaks, scree at the foot | Triplanar P1 granite on terrain and statue (3.2); P2 rock scans for the faces |
| The bridge | Older and wetter than the Hold: darker damp stone, moss, wet stains, one arch | N2 ask; until it exists the plank bridge stays |
| Bridge Lane | Engineered: granite flags with wheel wear and polished worn edges, gravel shoulders | Road art (155) with a wheel-wear and edge-polish mask (lower roughness on worn edges) |
| Brook Lane | Primitive: packed earth, gravel, damp footprints; stepping stones at the ford | Splat of P1 earth and gravel. A footprint decal needs a verified CC0 source logged in `THIRD_PARTY.md`; until then damp patches only |
| River | Dark slate-teal water, gravel seen in the shallows and on the bars, narrow highlights only, never a turquoise stripe | `Water2` flow map with depth colour; foam mask limited to piers, cascade and stepping stones |
| Meadow | Subdued olive grass, a few sun-catching edges | P1 ground under the grass instances |

Both lanes stay brighter than the grass (section 1). *v1.1 gave the Brook Lane a stone edge and wheel ruts; the review moves wheel wear to the Bridge Lane.*

**Set dressing.**
- **Conifers** (P2):
  - 160–220 tall pines and spruces, 14–24 m, in the forest walls (north, the north-east ridge, beyond the rampart ends), never inside the Warden's silhouette;
  - three inner stands of 6–9 pines: the north-west wedge across the river, by the SE pad, south of the ford; each stand stays 4 m or more from a lane edge and the platform;
  - 40 young pines, 4–8 m, at the margins and at the Warden's feet and ledges;
  - a few pines in front of the cascade, partly hiding it (3.2).
  - No round broadleaf crowns, no red crowns.
- **Granite** (terrain with P1, scans from P2):
  - the west wall, 25–30 m high, about 60 m long, three ledges, oversized fractures, lichen and moss streaks;
  - two scree fans;
  - 14 boulders, 2–5 m, along the river; 30–40 river stones;
  - six flat, low outcrops, 4–8 m, on the meadow, 4 m or more from the lanes.
- **River.** A 6–8 m channel, 1.2 m deep; the cascade's two drops; two boulder islands; gravel bars on the inside of bends. Foam only at the bridge piers, the cascade and the ford's stepping stones; boulders and islands get a dark wake, not foam.
- **Ford.** Nine flat stepping stones beside a sunken causeway visible under 20 cm of water; two broken causeway posts with iron rings. Foes still wade beside the stones (3.1).
- **Platform.** An octagonal cream-granite bastion (N1; until then the terrain dais in the same granite), two lit braziers by the north stair, stairs north, west and south; dawn gold on its rim.
- **The Hold.** About five wall segments with oversized battlements, one watchtower, four braziers on the wall walk, six hanging banners (dark weathered ember cloth, dark iron dragon sigil, no letters).
- **Ground cover.** 40–60 k grass tufts on the meadow; 300 ferns at the forest edges; moss on north faces. Within 2–4 m of a lane edge and the platform the vegetation thins: short grass only, from none at 1.5 m to full density at 4 m; no ferns, tall tufts or young pines there. *v1.1 put roadside tufts every 2–6 m; the review wins.*
- **Blight.** A low, thin violet haze (knee height, see-through) reaching 8–10 m out from both gates; three dead blighted pines at each gate; withered grass along a lane after a wave. *v1.1 had a thick creep; the review wins.*

**Not on this map.** Gold patches on the meadow; turquoise water; foam outside the piers, the cascade and the stepping stones; uniform fog; extra structures (none at the cascade, nothing the lists above do not name); extra creatures; tall vegetation near the lanes and the platform; lit Warden eyes before victory; sky or horizon.

### 3.5 Life on the map

- **The dragons.** Hỏa Long hovers on the platform at (640, 392) and turns toward the lane that lights on the wave card. Bạch Long waits at the south-west edge (602, 432).
- **Foes before the wave (muster ground, view only).** The next wave's first groups wait at their gate during the build phase and the wave warning:
  - **North:** two groups flank the ruined arch in the forest shade, at (−2…4, −31…−37) and (13.5…19.5, −31…−36). Screen 615–690 × 31–94 and 800–880 × 35–98.
  - **West:** in the cleft behind the Brook Lane's gate, (−39…−33, 4…10). Screen 28–153 × 445–541.
  - What stands there is the wave's real mix:
    - Moss Grunts thumping their stone knives;
    - Thorn Ant swarms boiling in a hollow;
    - Moss Archers from wave 2, Tusk Boars pawing from wave 3, a Blight Wolf line pacing from wave 7.
  - They half fade into the pine shadow and the thin haze: no rim light, bodies in shade, only their eyes show as tiny yellow-green points (`#C8D24A`).
  - In waves 5 and 10 the Moss Bannerman's tattered violet banner rises over the west cleft before he steps out.
- **Wasps.** From wave 2, Thorn Wasps circle the blighted dead pine at the Sky Lane's entry (1069, 289).
- **Defenders (Grove Wardens).** On structures only, never near a lane, so they are not mistaken for placed blockers:
  - two guard the platform's south stair, at (613, 447–465) and (667, 447–465);
  - two lookouts on the Warden's shoulder ledge (≈ (160, 215–275));
  - six on the rampart's wall walk, just above the typing bar;
  - two on the watchtower.
  - When a wave starts, they raise shields, the braziers flare and a horn sounds from the wall (a real audio file).
  - On victory the Warden's eye basins ignite and stay lit for the results camera.
  - *The review asks for tiny defenders; the 1.4× character scale (section 1) stays for readability, so the scale reads from the large masonry courses, the narrow stairs and the cliff fractures instead.*
- **Ambient (no animals).** Mist drifts down the river; spray at the cascade; pines, grass and banners move in one wind; cloud shadows pass; embers and sparks rise from the braziers; chimney smoke rises from behind the rampart; dust puffs under marching foes on the Brook Lane's earth (none in the ford, little on the Bridge Lane's flags; P5 particles at foot contacts, view only).
- **Removed:** the two crows and the hawk of the first draft (no verified animated source).

### 3.6 Where every piece comes from

| Source | Pieces |
|---|---|
| Repo | Dragons; foes rebuilt from their Tripo originals; Grove Warden; traps; Herb Hut; road art (155) for the Bridge Lane flags, with a wheel-wear and edge-polish mask; fire C for the braziers |
| Tripo now (owner, after the redone 124 sources pass 8.5) | `dragon-statue`, `hold-wall`, `watchtower`, `ruined-arch`, `brazier` (`hold-gate` is not in this frame) |
| Not asked | Dragon Platform (N1), stone bridge (N2); until then the terrain dais and the plank bridge stay |
| Free sources | P1 granite (cream and cool grey), forest floor, meadow, packed earth, river gravel; P2 pines, rock faces, boulders; P3 dawn HDRI for light; P5 spray, mist, embers, sparks, dust; P6 water, shadows, AO, grade, grass code; P7 river and wind ambience. Footprint decals: no verified source yet |
| Shaders | Flow-map river with a limited foam mask, cascade; river-bed mist and faint light shafts; cloud shadows; wind; thin blight haze; muster crowd; physically based scenery, triplanar cliff-and-Warden granite and the dawn grade |

### 3.7 What is wrong with today's version (Ultra and High, 01/11, `tmp/diag-0111/`)

1. **It is a park, not a mountain pass.** Football-pitch green meadow, beige sand paths, a round pond with lily pads, a jetty, lantern posts and rail fences. Nothing says "Hold", "dragon" or "pass".
2. **The shipped build has no ground textures:** `paint.ts` loads them in dev only. D1 (the `map-pilot` merge, on branch `dh-wave1`) brings them to the play build.
3. **Toy materials by construction.** Lambert with a 3-step ramp, flat-shaded rocks, sphere-normal crowns. Tree and rock models lost 84–91 % of their triangles and all their normal and roughness maps.
4. **No landmark, no scale.** The tallest scenery is a 9 m cliff of widened blocks that read as sugar cubes. Nothing is ten times a soldier; the six 124 landmarks were never built in 3D.
5. **Wrong colour script.** Saturated green grass, a bright blue river, up to six red-to-rust "warm crowns", a violet ground bounce.
6. **Flat light.** Sun at 50°, hemisphere fill 2.7, mist only past 47 m, no shafts, no cloud shadows, no AO.
7. **The water is a canal:** a uniform blue ribbon with cartoon specks; no depth colour, rapids, rocks or foam; placeholder stepping stones.
8. **The choke point has no presence:** a plank footbridge with rail fences.
9. **Paths are smears:** even-width sand ribbons, the "finger smear" `PATH_QUALITY.md` bans.
10. **The map is empty between waves:** no garrison, no muster, no banners, no smoke. Foes appear from nowhere at the lane end.

### 3.8 Concept painting: base image and prompt

- **Base image to attach:** `games/dragon-hold/art-src/_review/maps/map1-base-1280x720.png`. It is the real battle-camera capture (wave 1, canvas only, desaturated) with translucent blocks for the planned pieces and grey HUD boxes. No text.
- **Tool:** ChatGPT image in Chat mode with High effort, with the base image attached; or Adobe Firefly Image 5 with the base image as the composition reference. Claude's browser could not attach the image on 01/11, so the owner attaches it.
- **Legend:** `games/dragon-hold/art-src/_review/maps/map1-base-legend.md`.
- **Made by:** `games/dragon-hold/tmp/map-concepts/{scenario-base.mjs, map1-plan.mjs, make-base.mjs}`.
- **The message:** `docs/games/maps/dragon-hold-CHATGPT_MESSAGE.md` (review brief, constraints, this concept condensed, the other maps in one paragraph).
- **The review:** `docs/games/maps/dragon-hold-CHATGPT_REVIEW.md`: 8.1/10, with 8.7–9.0 expected once sections 3.2–3.5 are carried out.
- **Acceptance:** two blind judges, both 8.5 or higher, against the commercial board and the owner's reference; then the reject list of section 0.

**Concept painting prompt** (ChatGPT, verbatim; the layout comes from the base image):

```text
Use the supplied base capture as an exact composition reference. Preserve the identical high strategy camera, 55° downward angle, 30° vertical FOV, framing, terrain boundaries and every gameplay position. Do not move the two lanes, river, ford, bridge, central platform, dragons, foes, gates or HUD zones. Replace placeholder scenery with a painterly-realistic ancient mountain fortress environment at dawn. Transform the central dais into an octagonal cream-granite bastion with north, west and south stairs. Keep the red-orange fire dragon hovering above it and the pearl-white dragon at the southwest edge. Build the colossal weathered West Warden stone dragon into the left cliff, its folded wings and ledges merging naturally with 25–30 m fractured granite. Replace the plank bridge with a damp mossy single-arch granite bridge. Create dark pine forest around the ruined north arch, localized muted-violet blight mist and shadowed enemy muster groups. Make Bridge Lane worn granite flags and Brook Lane packed earth with stepping-stone ford, both clearly readable. Add slate-teal river water, gravel bars, restrained white foam, cascade spray and low river mist. Add the Hold rampart, watchtower, braziers, Grove Wardens, banners and smoke. Dawn gold comes from upper right; deep pine-green shadows fall lower left. Keep HUD areas plain dark grey and empty. No text, sky, horizon, extra creatures or new structures.
```

---

## 4. Chapter 1 · The Hold Awakens (stages 1–20, Pine River kit, spring)

**Arc.** The Black Mist rises in the high forest. Blighted moss folk, ants and wasps come down on the Hold. The old wardens built **Dragon Platforms** all around the pass; each holds the blight back while its fire burns. Hỏa Long relights them one by one: at the Hold's gate and fields, up the valley, onto the high ground (where Bạch Long joins him), and finally at the den of the Tuskfather, the blighted boar lord at the head of the valley.

**Chapter-wide rules.**
- One lane per stage (04 §3.2); a sky lane from S12.
- Spring: fresh olive and pine greens, snowmelt, small white and pale-yellow flowers away from the lanes; no candy colours.
- Light moves dawn → morning → noon → golden hour → dusk → blue hour; no full night.
- A system that is not yet open has no slot on the map: trap slots from S2, block points from S6, house pads from S16 (04 §6.1).
- Camera as map 1 unless noted. Wing heroes use the slots of section 1: centre at |x| 31–35, z −14…0.
- **One unmistakable dominant silhouette per stage** (ChatGPT review). Grass, pine, granite and river repeat across the chapter, so each stage is remembered by one shape: its hero landmark, at least 22 m (section 1), alone on its wing, with a ground and stone that set it apart from its neighbours.
  - The benchmarks: S3 (the dragon-head quarry), S11 (the granite needle above the cloud sea), S14 (the dragon-head spillway dam), S15 (the elder-dragon fossil), S18 (the hanging glacier), S20 (the boar lord's den).
  - The weakest were the mill (S7), the herb terraces (S16) and the granary (S17); v1.2 gives each a bigger silhouette below.
  - A stage whose hero is under 22 m, or shares its silhouette with another stage, is redesigned before its prompt is written.
- **Map 1's look rules apply** (3.3–3.4): one focal dialogue, a light budget, separate stone families, lanes as the clearest ground, thin vegetation near the lanes.
- **Life in every stage:** a muster ground at each gate (the stage's own foes), Grove Wardens on structures, the dragons. No ambient animals.
- **Before a stage is built:** grey-box it, capture its base image, measure its frame shares, then write its prompt (light, materials, mood, scale) and send it to ChatGPT.

| # | Name | Site | Layout | Teaches (04 §6.1) | Hero landmark · source | Light |
|---|---|---|---|---|---|---|
| 1 | First Fire | The Hold's east gate | L1-thang | Type → fire; Moss Grunt | The Hold's East Gate, left wing · 124 `hold-gate`, `hold-wall`, `watchtower` (Tripo now) | Dawn |
| 2 | The Spike Line | The Hold's terrace fields | L1-s | Build, Spikes | The Broken Tower, right wing · 124 `watchtower` ×1.6, top fallen (Tripo now) | Morning haze |
| 3 | Breath of Fire | The old quarry | L1-thang | Fire Breath | The Unfinished Warden, left wing · 124 `dragon-statue` sunk to the shoulders in rough-cut rock (reuse) | Noon, broken cloud |
| 4 | The Ant Hills | A burned logging slope | L1-s | Thorn Ant swarms | The Fallen King pine, right wing · P2 pine scan laid down plus a root plate (not asked) | Golden morning |
| 5 | The Bannerman | Signal Hill | L1-thang | General, aura, Seal Break | The Beacon of the Pass, left wing · 124 `watchtower` ×1.4 crowned with `brazier` ×3 (reuse) | Late afternoon |
| 6 | Wardens of the Grove | The Elder Grove | L1-s | Grove Warden | The Elder Pine, right wing · P2 giant conifer plus terrain roots | Morning shafts |
| 7 | The Mill Race | The Hold's mill | L1-thang | Small Potion | The Mill Tower and its trestle flume, right wing · not asked | Misty morning |
| 8 | Horns at Noon | The Long Stair | L1-s | Call waves early | The Long Stair, left wing · terrain stair; dragon pillars not asked | Noon |
| 9 | The Warm Springs | Hot spring terraces | L1-thang (short) | Review | The Steam Falls, top right · terrain, travertine (P1), shaders | Soft morning |
| 10 | The Captain's Gate | The old outer wall | L1-s | Mini-boss: Moss Bannerman at W 16 | The Broken Gate, right wing · 124 `ruined-arch` ×2 and `hold-wall` stubs (Tripo now) | Dusk |
| 11 | Two Dragons | The White Eyrie | L1-xoan | Bạch Long, Feather Shield | The Eyrie Needle, left wing · terrain pinnacle with P2 rock faces | Dawn over a cloud sea |
| 12 | Wings over the Pass | The Hive Cliff | L1-thang + sky | Thorn Wasp | The Hive, right wing · not asked | Windy morning |
| 13 | Nets and Wind | The Windgap | L1-s + sky | Net Launcher | The Windgap Mast, left wing · not asked | Breaking overcast |
| 14 | The Flood Bridge | Below the Upper Dam | L1 with bridge and ford | Pine Bomb; flood | The Upper Dam, right wing · not asked (dam, causeway) | Bright morning, spray |
| 15 | Dragon's Rage | The Elder Bones | L1-thang | Dragon Rage, Inferno | The Elder Bones, left wing · not asked | Afternoon gold |
| 16 | The Herb Terraces | Healers' terraces | L1-s | Herb Hut | The Great Aqueduct, two tiers, right wing · not asked | Morning |
| 17 | Hold the Granary | The Hold's bailey | L1-thang | Dragon Heart, Hard Scale; Granary objective | The Inner Keep and the fresh breach, left wing · 124 `hold-wall`, `watchtower`, `hold-gate` kit; keep and granary not asked | Harvest gold |
| 18 | The Roar | The Echo Cirque | L1-s | Urgent word, Dragon Roar | The Hanging Glacier, left wing and top · terrain and ice shader | Cold bright morning |
| 19 | Campfire | The last camp | L1-thang (short) | Review; boss preview | The Tusk Wall palisade, top band · not asked | Blue hour, campfire |
| 20 | Tuskfather | The Den | L1-thang (long charges) | Boss B01 | The broken Tusk Wall and the lair mound · palisade not asked; boss = `tusk-boar` scaled | Violet haze → sunburst |

**The stages in short** (world positions are plans; screen positions come from `project.mjs` once each stage is laid out):

- **S1 First Fire.**
  - Gate in the north-east forest at (20, −24); one straight lane, 27 m, across a meadow to the platform's north-east stair.
  - The Hold's East Gate (`hold-gate` facing east, `hold-wall` running north–south, a `watchtower` at the north end) fills the left wing, more than 30 m from the lane. A ceremonial granite road runs from the gate to the platform.
  - Life: Grunts muster 4–6 at a time at the gate; Grove Wardens on the wall; chimney smoke from behind it.
  - Risk: with today's kit, a gate model dropped on bright grass.
- **S2 The Spike Line.**
  - Gate at the top centre; an S-lane, 38 m, between drystone field walls (≥ 2.5 m from the lane); four trap slots at the bends and straights.
  - The Broken Tower on a granite knoll at the right wing, its fallen top lying across the field in 3–4 m blocks that stop short of the lane. Young barley as instanced cards.
- **S3 Breath of Fire.**
  - Straight lane, 30 m, in a cut channel 6 m wide, so the Fire Breath cone fills it and reads.
  - The Unfinished Warden, half carved out of the west face. The quarry floor is dark crushed granite (≤ 0.6 luma under the tags); pale cut faces only on the walls.
  - Risk: pale stone behind white tags.
- **S4 The Ant Hills.**
  - Three blight ant mounds at the gate pour Thorn Ant swarms down an S-lane, 36 m, on a burned slope.
  - The Fallen King's root plate (12 m) on the right wing; the trunk runs off the edge over a ravine.
  - Keep the lane core one step brighter than the ash.
- **S5 The Bannerman.**
  - Straight lane up a granite dome. The beacon is cold until the general falls, then burns (fire C plus embers) for the rest of the stage.
  - The Moss Bannerman plants banners on the verge (G01).
  - Heather stays small and away from the tags.
- **S6 Wardens of the Grove.**
  - Gate on the left wing; an S-lane through a chain of clearings, never under canopy.
  - The Elder Pine (trunk 4.5 m, 45 m tall, crown cropped by the frame edge) on the right wing; giant trunks only on the wings and the far band.
  - Grove Wardens step out of the root hollows when placed.
- **S7 The Mill Race.**
  - Straight lane crossing the mill race on a low culvert (no slowdown).
  - The Mill Tower: a 24 m granite mill tower on a cliff spur at the right wing, its 16 m overshot wheel fed by a timber flume on tall trestles that comes down the wing from the north; the race falls white off the wheel into the gorge. The silhouette is the wheel and the trestle line against dark pines. *v1.1's three-storey mill with a 10 m wheel was under the 22 m hero rule and lacked drama (review).*
  - Keep it massive and cool, never a cozy village.
- **S8 Horns at Noon.**
  - An S-lane switching back down a terraced slope.
  - The Long Stair climbs the left-wing cliff between dragon pillars, with two war horns that Grove Wardens blow when the player calls a wave early.
  - Cloud shadows and stair relief carry the noon light.
- **S9 The Warm Springs.**
  - Short lane along pool rims (pools ≥ 3 m from it).
  - A 15 m travertine waterfall with milky jade-grey water (not turquoise) on the right; steam drifting.
  - Few foes; calm.
- **S10 The Captain's Gate.**
  - The lane enters through the ruined arch (×2, 16 m) on the right wing and runs along the old wall line.
  - The strong Moss Bannerman (W 16) enters alone after the second peak.
  - Dusk: orange stays in the light, not in the ground.
- **S11 Two Dragons.**
  - A half-spiral (L1-xoan) around the platform on a tableland.
  - A 45 m granite needle on the left wing, cropped so it reads as endless. A cloud sea fills the right side and the lower right; the spiral's last stretch runs over dark ledge stone, never in front of the bright clouds.
  - Bạch Long flies in from the cloud sea.
- **S12 Wings over the Pass.**
  - Ground lane plus a sky lane from the hive on the right wing (nothing tall south of the sky lane's entry).
  - Wasps orbit the hive before each wave. Keep the sky lane over plain meadow.
- **S13 Nets and Wind.**
  - S-lane across a saddle that falls away at both lower corners; a sky lane along the gap.
  - A guyed timber-and-iron signal mast with a net winch on the left wing.
- **S14 The Flood Bridge.**
  - The lane crosses a fast river on a low five-arch causeway; a ford detour downstream opens while the bridge floods.
  - The dam's three dragon-head spillways on the right wing: eyes glow, a horn sounds, and 3 s later the surge.
  - Needs a river surge state in the water shader.
- **S15 Dragon's Rage.**
  - Straight lane down a scorched slope.
  - The stone-fossil skeleton of an elder dragon on the left wing: a 10 m skull and ribs of 12–15 m. Embers glow in the skull as Rage fills. Stone and moss, never gore.
- **S16 The Herb Terraces.**
  - S-lane down terraces; house pads appear.
  - The Great Aqueduct: two tiers of granite arches, 30 m, striding across a gorge on the right wing and running off the frame edge so it reads endless; one upper span is broken and pours a white ribbon fall. *v1.1's three 18 m arches lacked drama (review).*
  - The terraces are held by massive granite retaining walls, 4–6 m, stepping down the slope, so it reads as a mountain stair, not a garden.
  - Herb beds in sage, silver and white; no lavender (it reads as blight).
- **S17 Hold the Granary.**
  - Straight lane through a fresh breach in the outer wall: a rubble fan that stops 2 m short of the lane, broken timber hoardings, smoke from a fire on the wall walk.
  - The granary (objective) at (−9, 7), 11.4 m from the platform, kept low so it never covers the platform or a pad.
  - The Inner Keep is the stage's one silhouette: a 32 m square granite keep on the left wing, top cropped, timber hoardings on its crown, a 12 m dragon-sigil war banner (no letters) down its face, harvest light raking it. *v1.1's keep and granary lacked drama (review).*
- **S18 The Roar.**
  - S-lane over dark wet scree.
  - The glacier and its snow stay on the left wing and the top-left band only, never behind the tags. Dragon Roar shakes snow off the glacier lip.
- **S19 Campfire.**
  - Short lane from the palisade gate.
  - The campfire on the platform's south edge is the warm key light. Two glowing eyes move behind the palisade gaps (the boss preview).
  - Foes get rim light from the fire and the violet back-glow.
- **S20 Tuskfather.**
  - Long straight lane with an 8 m trampled charge apron, so the red charge line reads on clean ground; four ant mounds at the flanks.
  - The boar lord bursts through the palisade. On victory the violet haze burns off into gold: the grade change is the reward.

---

## 5. Chapters 2–26 (one line each)

Each chapter is 20 stages in one region (04 §2.1). Stages 1, 10 and 20 are hand-built and get their own concept page, base image and prompt before production. Kits keep their signature mechanic (04); each chapter gets one hero set piece. No temples, shrines or worship objects. The boss source follows `MONSTER_MODEL_INVENTORY.md` §6.2 and §7.

**Review notes (ChatGPT, 01/11).** The direction holds because each chapter changes scale, material, vegetation and atmosphere; keep that. The weakest idea is a Black Mist chapter that only recolours an earlier one: each Mist version changes silhouettes, damage, particles and materials. The floating-granite rift stays for the very end (C26): no floating islands or levitating rock before it.

| Ch | Region, mood · title | Signature and hero set piece | Boss · model source |
|---|---|---|---|
| C2 | Pine River, summer · The Hold Besieged | Two lanes; opens on Map 1. Thunderheads at dusk; the Hold's gatehouse from the inner court for S20 | B02 Moss Chieftain · `tyrant-g04` or `warden-nature` (ST); totem from `nature-oppressor` |
| C3 | Violet Glade, day · The Lanternwood | Colossal blue-indigo trees, 40–70 m; mushrooms that put foes to sleep glow cool white. Hero: the Hollow Giant | B03 Thorn Queen · `thorn-wasp` scaled |
| C4 | Hill Meadow · The High Downs | Hill pads +25 % range, wind changes every wave. Granite tors 25–40 m with a ruined hill fort | B04 Twin Wolves · `blight-wolf` scaled and recoloured (not in the inventory table; to confirm) |
| C5 | Mire, mist · The Drowned Causeway | Foes rise from the water by the pads. A dragon statue sunk to its brow, 30 m across | B05 Bog Toad King · **no source** |
| C6 | Rainforest, rain · The Vine Gorge | Vines open and close lanes. A 60 m waterfall curtain and an overgrown aqueduct | B06 Web Matriarch · **no source** |
| C7 | Red Canyon, noon · The Red Gates | Rockfall on a typed cliff. Two 40 m carved dragon pillars; the closest chapter to the owner's reference | B07 Canyon Colossus · **no source** (troll, `tyrant-g04` weak) |
| C8 | Rock Coast, sunset · The Tide Cliffs | Tidal flats flood on a 40 s rhythm. Sea stacks, a sea arch, a giant wreck's ribs | B08 Tide Crab · **no source** |
| C9 | Violet Glade, night · The Moonwood | Foe bodies show only near light; words stay clear | B09 Night Bat Lord · **no source** |
| C10 | Volcano, ash · The Ember Throne | Lava vents every 20 s. A dragon maw carved into the crater wall | B10 Magma Salamander · **no source** |
| C11 | Pine River, autumn · The Turning Year | Muted ochre larches away from the lanes; the Elder Grove | B11 Rotwood Ancient · `moc-tinh` (WW) |
| C12 | Mire, firefly night · The Lantern Marsh | Firefly particles; the sunken statue lit from below | B12 Spore Mother · `nuppeppo` (WW) |
| C13 | Hill Meadow, storm · The Thunder Downs | Strongest wind hazard; lightning silhouettes the tors | B13 Storm Beetle · `lieutenant-nature` (ST) |
| C14 | Rainforest, night · The Dark Gorge | The waterfall glowing with moonlight | B14 Mist Knight · Space shadow bosses; the horse has **no source** |
| C15 | Rock Coast, storm · The Breakers | Storm waves; the estuary river floods | B15 River Serpent · `thuong-luong` (WW) |
| C16 | Red Canyon, night · The Mirror City | Polished-stone mirrors in the cliff city | B16 Raven Sage · **no source** |
| C17 | Pine River, winter · The Frozen Hold | Deep snow; lanes swept dark for the tags; the Warden capped with snow | B17 Frost Stag · **no source** |
| C18 | Violet Glade, bloom · The Flowering Wood | Pale blossom drifts | B18 Deep Centipede · **no source** |
| C19 | Volcano, eruption · The Burning Sky | Lava lake, ash fall; red in the light, not the ground | B19 Black Wyrm · `draconis-v3` re-materialled |
| C20–25 | The Black Mist (Act III) | Earlier regions under the Mist layer, with each chapter's rule (02 §4.4). Each one changes silhouettes (landmarks broken, collapsed or overgrown), damage, particles and materials, never only the colour. In C25 the Hold is in ruins: the Warden broken, the bridge fallen | Twin bosses from above |
| C26 | The Mist Rift · Heart of the Mist | A chasm with floating granite islands, the only floating rock in the campaign; three lanes on bridges; the drop shows at the wings and lower corners | B20 Mist Mother · Space shadow bosses (inventory D16) |

---

## 6. Why the current maps fail (Dragonhold)

1. **We built a system, not places.** One map dressed by rule (forest bays, groves with sand rings, warm crowns, a pond). There is no landmark a player would remember. Commercial maps are hand-composed around one set piece.
2. **We judged ourselves on our own scale.** The pilot moved toward an old cozy reference and scored 7.1 on our scale; on the market scale the map is 4.
3. **We made the epic for cameras the player does not use.** At 55° from 78 m the sky never shows (horizon at y −1559). The dawn sky, the mountains and the title art live on the title screen, while the playfield stayed a lawn. The epic has to live in the ~100 × 65 m patch: colossi on the wings, a rampart along the bottom, gates and musters in the top band.
4. **Everything is at human scale.** Cliffs of 8–9 m read as a 1:100 diorama; nothing is ten times a soldier.
5. **Toy rendering by construction.** Lambert with a ramp, flat-shaded rocks, sphere-normal crowns, meshes cut by 84–91 % and stripped of their maps. Ultra cannot fix this.
6. **Light and colour are flat and off-script.** High sun, strong fill, a violet bounce; saturated green, bright blue and red crowns.
7. **Water, paths and the bridge, the things the player looks at most, are the weakest.**
8. **The shipped build differed from dev** (ground tiles loaded in dev only), and nobody judged the play build.
9. **No life.** No garrison, no muster, no banners, no smoke.
10. **No target before code.** We tuned knobs without a picture of "done". The fix is this document's process: base image, ChatGPT critique and painting, an accepted painting, then a build matched to it side by side at 1280×720, judged blind against the owner's reference.

---

## 7. What needs the owner

- **Map 1 concept painting.** Attach the base image and paste the prompt of 3.8 in ChatGPT (Chat mode, High effort), or run them in Firefly Image 5; then two blind judges at 8.5.
- **Tripo, now.** The six 124 landmarks, after their Firefly sources pass 8.5 (`TRIPO_TODO.md` rows 1–6). For map 1 the order is `dragon-statue`, `hold-wall`, `watchtower`, `ruined-arch`, `brazier`, then `hold-gate` (first needed in S1).
- **Tripo, later (not asked).** N1 Dragon Platform, then N2 stone bridge. Then one hero piece per stage, each measured on its own base image first.
- **Camera O3.** Map 1 works at both cameras: the Warden's head and the arch stay in frame. The owner picks after Claude's camera trial images. If O3 becomes the default, the base image is recaptured with `--cam=o3`.
- **Old scenery models.** Leave the files, stop using them in new maps, and replace them with P2 conifers and rocks.
- **Backdrop ring (120).** Title and results cameras only; its painted gate must face south, where the 3D Hold stands, or be painted out.

**Dependency, not an owner decision.** Map 1 needs the wave card to treat the Warden's screen box as a keep-out zone (`screen-zones.ts`, UI lane).
