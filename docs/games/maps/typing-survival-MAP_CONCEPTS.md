# Last Line: map concepts, stage by stage (01/11/2026)

> **For:** the owner, ChatGPT (review, then concept paintings), the map lane.
> **Game:** Last Line (`games/typing-survival`). Typed words load guns that hold one straight lane on a space station against the Black Hole Horde.
> **Status:** concepts only. No code changed. Rules, sim and camera stay as they are; only what the player sees changes.
> **Sources read:** `docs/SURVIVAL_MODE_PLAN.md`, `docs/BUILD_S1.md` (§6 foes, §7 hazards and boss, §8 chapter table), `docs/FEEL_PASS_S1.md`, `src/content/{chapter-1,stage-s0,rules,foes}.ts`, `src/view/scene.ts`, `src/view/models.ts`, the model manifest, parent `docs/games/ART_DIRECTION_2026-10-28.md` §1 and §4 (Lightbearer bible), `docs/games/MAP1_PRODUCTION.md` §3, `docs/games/PATH_QUALITY.md`, `docs/games/THIRD_PARTY.md`, the arena kit report `docs/codex-queue/125-report.md`, today's captures in `games/typing-survival/tmp/diag-0111/`.
> **Art bar:** the owner's reference `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (a hero seen from behind, a colossal creature in the sky, a deep land running far away, warm low light). Every painting and every in-game capture is scored M (market scale, ART_DIRECTION §1.3) and Q; accepted at **M ≥ 8 and Q ≥ 8**. Everything the player reads is English. No code-drawn stand-ins for art.

---

## 0. How to use this file with ChatGPT

1. Paste §1 (fixed rules) and one stage section at a time. Ask: "Review this map concept as a senior art director of a commercial sci-fi action game. Keep the gameplay layout and camera. Is the landmark strong enough? Does anything hide play? Propose a better idea if you have one."
2. When the concept is agreed, ask for the painting with the stage's prompt. Attach `games/typing-survival/art-src/concepts/b-lightbearer-fight.png` with the line "Use the attached image only to keep the same heroine, sentinels, foes, materials and colours."
3. Reject and ask again when: the deck is not a straight lane from bottom centre to a gate near the top; the heroine is big (more than about 12% of image height); the landmark sits over the deck; the deck just ahead of the heroine is bright; any text, number, logo or UI appears; the foes are not black glass with orange cracks. At most three tries a painting, then keep the best and write down what is missing.

---

## 1. Fixed rules for every map (the sim and the camera do not change)

### 1.1 The field

- One straight lane, **24 m wide, 40 m long** (`FIELD` in `src/content/rules.ts`). x runs across (−12 … +12), z runs away from the heroine.
- **Foes enter over the gate at z 40**, across the full width, in packs of 4–12 (block, wedge or line). Packs wait in a queue up to z 52. Five vanguard packs (6–8 foes) already stand at z 18, 26, 34, 42 and 50 when a fight starts.
- **The defended point is the Line at z 2.4.** A foe that reaches it costs armour. From z 14 in (chapter stages) every foe bleeds armour; the near zone is z ≤ 7.
- **The heroine stands at z 0**, centre. Her guns are the sentinels beside her; each bay (a DOM panel) feeds one sentinel.
- Hazards and objectives that need room on the map:
  - **Rift**: a crack opens at the foot of the left or right wall (seeded), z 9–13, 2.5 s of warning, then 8 foes pour out.
  - **Gravity well**: centred at x ±4 (seeded), z 18, radius 8 m.
  - **Ion storm**: numbs one bay for 6 s after 2.5 s of warning.
  - **Nests**: crawling hives that appear at z 30–36 and crawl to z 10.
  - **Pack Leaders**: big foes with a gold beacon column.
  - **Boss**: stands at z 22, then 15, then 8.

### 1.2 The camera and the screen at 1280 × 720

The fight camera stays: pitch 36° below the horizon, vertical FOV 42°, about 20 m up and 18 m behind the heroine (`src/view/scene.ts`). The horizon is 15° **above** the top edge of the screen. Everything beside the lane is therefore seen looking **down**: the side areas show what lies below and beside the causeway, from deck level near the lane down to kilometres of depth.

Measured from the current camera:

| Depth z | Screen y | Deck spans x |
|---|---:|---|
| 52 (queue end) | 16 | 475–805 |
| 40 (gate) | 72 | 447–833 |
| 30 | 135 | 416–864 |
| 22 (boss P1) | 203 | 383–897 |
| 18 (well) | 245 | 363–917 |
| 13 (rift top) | 307 | 332–948 |
| 7 (near zone) | 404 | 285–995 |
| 2.4 (the Line) | 500 | 237–1043 |
| 0 (heroine's feet) | 561 | 207–1073 |
| −4.9 (bottom edge) | 720 | 129–1151 |

```text
y   0 +-[hull bar 15-375][timer 388-545]--(free sky 545-1020)--[kills 1020-1175][gear]-+
      |                     \  horde queue + black hole shadow  /                     |
y  72 |   LEFT WEDGE         \======= gate (z 40), 386 px =====/        RIGHT WEDGE    |
      |   landmark box        \                                /     landmark box     |
      |   x 0-400, y 80-330    \        boss z 22 (y 203)     /   x 880-1280, y 80-330|
y 245 |                         \       well z 18 (y 245)    /                        |
y 307 |   rift side ->           \     rift z 9-13          /          <- rift side   |
y 400 |                           \ [ word line 400-456 ]  /                          |
y 500 |   ------------------- THE LINE (z 2.4, x 237-1043) -------------------        |
y 561 | [locked 40-200][bay 1 235-465]   HEROINE   [bay 2 815-1045][locked 1080-1240] |
y 720 +------------------------------------------------------------------------------+
```

Rules that follow from this:
- **The landmark lives in a side wedge** (upper-left or upper-right box) or in the free sky strip above the gate. Nothing big ever stands on the deck.
- Tall things at the deck edge lean **outward** on screen (they cannot cover the lane). A 10 m tower at x 14, z 2 runs from (1116, 509) to (1244, 201); a 30 m pylon at z 20 rises from (951, 245) up and out of the top right of the frame.
- **The deck under the word line (y 400–456, z 4.4–7) stays dark**: at most +0.02 luma over today (FEEL_PASS_S1 §4.1). Light pools from guns are the only bright things there.
- Light from the sky must not wash the horde out (the `f8` grade: ≤ 10 %). The brightest region of each map is in a wedge, never behind the lane.
- The heroine at 2.8 m stands from y 487 to y 561 (74 px). Her sentinels at 1.6 m height, ±1.5 m, sit near (584/696, 520). Keep the deck round her dark and quiet except her own glyph ring.
- Map budget: ≤ 60 draw calls for the whole frame on High (MAP1_PRODUCTION TS-M1-08); models seen up close ≥ 2,000 triangles (`MODEL_QUALITY.md`).

### 1.3 One idea for all of Chapter 1: a causeway over the disk

Chapter 1 (in game "CHAPTER 1 · VC-7 CORRIDOR") is drawn as the **VC-7 causeway**: a 4 km bridge of graphite steel and pale ancient stone that runs from the station's citadel out over the accretion disk toward the black hole. The Horde crawls out of the black hole's shadow and walks the causeway toward the citadel.

- **Looking down past the deck edge you see the disk below**: a sea of orange-gold plasma spiralling far beneath the bridge, lit from below, crossed by the station's lower decks, pylons and other causeways falling away into haze. This is how a top-down camera gets "epic" (ART_DIRECTION §1.2: the field stands on a high plateau and its edge is a cliff). Today that space is a flat poster.
- **Each stage is a different span of VC-7**, one step farther from the citadel (presentation only; the sim field is the same). The heroine pushes the Line out span by span to the Breach where the Warden holds the gate open. So the disk grows, the ruins break more and the light warms from stage 1 to stage 10, and no two stages look alike.
- **Stage intro sweep** (view only, during the stage card): 2.5 s from a low camera over her shoulder, aimed at the stage's landmark, then down into the fight view. The title camera blend in `scene.ts` already does this move. Any key skips; reduced motion cuts straight.

### 1.4 Shared kit for Chapter 1 (referred to by K-numbers below)

| Id | Piece | Size and count | Comes from |
|---|---|---|---|
| K1 | **Deck surface**: long graphite plates and pale stone bands running along the lane, inset seams, worn centre, dim cyan glyph inlays | 24 × 46 m, plates 6 × 1.5 m along z | `art-src/arena-v2/deck-tile.png` (ticket 125, self-scored 8, **not judged, not wired**) as albedo, plus a free CC0 PBR stone and worn-metal set for normal and roughness detail; trim-sheet strips along the edges. Anisotropic filtering 8–16× so the far deck stays sharp |
| K2 | **Deck decals**: scorch with orange cracks, black glass shards, glyph ring, stone crack | 12–20 a stage, seeded, none inside the word-line box | `art-src/arena-v2/deck-decals-alpha-v3.png` (125) |
| K3 | **Parapet**: 1 m stone wall capped with steel, a cyan running light that pulses toward the heroine | both sides, 46 m | real mesh from a free CC0 PBR sci-fi modular kit (wall, cap, post); `deck-edge-alpha-v3.png` (125) as look reference; the running light is an emissive strip (today's conduit shader on a real mesh) |
| K4 | **Edge pylons**: slim stone-and-steel pylons outside the parapet, leaning out, a cyan lamp and a light banner each | 10 a side, every 4–5 m, 6–9 m tall | one Tripo model by the owner (or a CC0 kit assembly), instanced; banner is a cloth-like light shader |
| K5 | **Bastion dais** (foreground): semicircular stone dais under the heroine, radius 10 m, her glyph ring inlaid; two bastion towers at x ±14, z 1–3, 10–12 m tall, leaning out of the bottom corners | 1 dais, 2 towers | towers: Tripo by the owner (seen up close, ≥ 2,000 triangles); glyph ring from `deck-decals-alpha-v3.png` |
| K6 | **Underside**: the causeway's truss, 6–10 m deep, visible at the inner edge of the wedges; cyan coolant falls pouring off broken edges into the void | truss along both edges; 2–4 falls a stage | CC0 kit girders, instanced; falls are a flow shader (VFX standard) |
| K7 | **Midground structures**: monoliths, pylons and station-ring bases rising out of the abyss 150–600 m beside the causeway | 4–6 a stage | near ones (≤ 300 m): Tripo or CC0 kit composites; farther ones: painted alpha cards from ChatGPT, 2–3 layers each for parallax; `wall-left-alpha-v3.png`, `wall-right-alpha-v3.png` (125) are candidates |
| K8 | **Far layer**: titanic broken rings and other causeways spiralling down toward the disk, 1–5 km away | 1–2 cards a stage | `art-src/arena-v2/far-ring-alpha-v3.png` (125) plus new ChatGPT cards per stage |
| K9 | **Sky and abyss**: black hole shadow beyond the gate, lensed photon ring, accretion disk as a **world-space ring mesh below and ahead of the causeway** (plasma streams, Doppler-bright side, inner glow), starfield only in the top corners | 1 | shaders (allowed when they meet `VFX_STANDARD.md`); today's `SKY_FRAGMENT` is the start; `art-src/arena-v2/sky-disk.png` (125) is the colour target; starfield cubemap from a free tool whose output we own, or a CC0 one |
| K10 | **Atmosphere**: height fog layers in the abyss, dust motes in the light, light shafts from the disk, heat shimmer at the gate | per stage | Kenney Particle Pack and Smoke Particles (CC0, already in `THIRD_PARTY.md`) for motes and smoke; three.js examples (MIT) for god rays and lens flare; fog is a shader |
| K11 | **Horde reservoir**: the Horde massing on the causeway beyond the gate in the black hole's shadow, orange crack glints | 150–300 silhouettes, z 40–80 | impostor cards rendered from the five rainbow models in `public/assets/typing-survival/models/` (or instanced lowest LOD), one draw call |
| K12 | **Heroine group**: the Lightbearer (woman gunner, white-and-gold ceramic armour over graphite, cyan visor, navy cape with gold seams), one sentinel gun-drone per bay at her shoulders (Pulse cyan, Heat Beam orange, Scatter amber, Rail white-blue, Star Mortar vermilion), and **a small support drone** above her right shoulder that carries her work light and delivers the repair pod | 2.6–2.8 m heroic scale (65–74 px at 720p) | Tripo by the owner from `art-src/models-src/lightbearer-{front,back,left}.png` and `sentinel-*.png` (ticket 156; not built yet); support drone needs a new source picture; clips from the CC0 libraries already proposed in `THIRD_PARTY.md` (Quaternius UAL, Mesh2Motion; waiting for the owner's OK) |
| K13 | **Ambient life**: void mantas gliding far below, debris shoals, evacuation shuttles (tiny lights) crossing the top corners, maintenance drones on the parapets | 2–3 mantas, 1 shoal (instanced), 3–6 shuttles, 2–4 drones | mantas: painted cards or one Tripo model; rocks: CC0 instanced; shuttles: light sprites |
| K14 | **Light rig**: key = the disk, low and **from ahead and below** (back light and up light, warm); fill = navy from above; the heroine's cyan; image-based light from the sky so every model gets rim light; one shadow-casting light on the near deck (High and Ultra) | 1 | three.js (MIT): DirectionalLight, PMREM from the sky; today's light pools stay |

Quality tiers: Medium drops shadows, fog layers and K13; Low keeps K1–K5, K9 and one card layer.

---

## 2. Trial (`s0`, outside the chapter): "The Proving Span"

**Story beat.** Before her first watch, the Lightbearer proves herself on the outer span of the citadel while the Horde tests the gate.

**Gameplay layout.** Hold 180 s. No hazard. Five vanguard packs at z 18–50, two surges (55 s, 145 s), scouts from 12 s. The lane, gate, Line and bays as §1.

```text
 z                x=-12                       x=+12
 52   . . . . . [ horde reservoir, thin ] . . . . .
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 34        |  . vanguard pack (8)          |
 26        |       . vanguard pack (7)     |   (R) LANTERN TOWER
 18        |  . vanguard pack (6)          |       400 m out, right
  7        |. . . . near zone . . . . . . .|
  2.4      |=========== THE LINE ==========|
  0        |       S1   HEROINE   S2       |
 -3        \_______ bastion dais __________/
```

**Hero landmark.** **The Lantern of VC-7**: the citadel's beacon tower, about 400 m tall, standing on a pier 300 m to the right and rising out of the abyss. Its crown holds a slow sweeping cyan lamp. In frame it fills the upper-right box (x 900–1280, y 80–330); its beam sweeps across the free sky strip every 8 s, never across the deck.

**Depth layers.**
- Foreground frame: K5 dais and bastion towers, dark, rim-lit in cyan.
- Playfield: K1 deck, new and clean (few decals), K3 parapets, K4 pylons.
- Midground: the Lantern tower; two low station blocks on the left at 200 m.
- Far background: the citadel's outer ring curving away on the left, lit windows.
- Sky: the black hole small and distant (shadow radius 0.12 of view height), disk a thin gold ellipse far below; mostly navy and stars.
- Time and light: "cold watch". The disk is dim amber, low ahead; cool navy fill; the Lantern is the only strong cyan. No weather; slow dust.
- Colour script: navy and graphite 70 %, cyan 15 %, amber 15 %.

**Set dressing.** Dais 1; bastion towers 2 (10 m); edge pylons 20 (7 m); light banners 6 (white-gold, the Lightbearer order's crest as an abstract shape); station blocks 2 (60–90 m); Lantern tower 1 (400 m); citadel ring card 1; coolant falls 2.

**Life on the map.** The vanguard packs walking in; a thin reservoir (about 100 silhouettes) beyond the gate; 4 shuttles leaving the citadel with tiny white lights; 2 maintenance drones gliding along the left parapet; the Lantern's beam.

**Sources.** K1–K14; Lantern tower: lower 60 m as one Tripo model (seen at 300 m, medium detail), the rest a two-layer ChatGPT alpha card; citadel ring: ChatGPT card.

**What is wrong today.** The trial uses the same scene as every stage: the industrial corridor of §9. Nothing tells the player this is a practice span at the citadel.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, seen exactly from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel plates and pale stone bands that runs from the bottom centre to a far gate near the top. The heroine stands small at bottom centre: a woman gunner in white-and-gold ceramic armour, cyan visor, long navy cape, two floating white-gold sentinel gun drones at her shoulders and a small support drone above. A thin white-gold barrier line crosses the deck just ahead of her; the deck right ahead of her stays dark and calm. Small packs of black glass creatures with glowing orange cracks walk in from the gate. To the upper right, a 400 metre beacon tower rises out of a deep abyss beside the causeway, its cyan lamp sweeping. Far below, a dim amber accretion disk; the black hole small and distant. Cold navy light, cyan rim light. Painterly-realistic, crisp big shapes. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 3. Chapter 1 · VC-7 Corridor, stage 1 (`c1-s1`): "First Shift"

**Story beat.** The first real watch on Span One: the Horde comes over the gate in earnest, and the first Brutes push through the swarm.

**Gameplay layout.** Hold 150 s. No hazard. Calm rate 4.4 a second, surges at 50 s and 115 s, scouts from 12 s, Brute packs (a Brute and 5 swarm behind it) from 80 s. Armour drain ×2. Two bays.

```text
 z                x=-12                       x=+12
 52   . . . . [ horde reservoir, dense ] . . . . .
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 36  (L) BROKEN RING  |  packs 4-12 (block, wedge, line)|
 30   base pylon at   |                          |
 22   x -60, z 30     |      Brute + 5 (from 80 s)|
 14        |. . . . . armour drain from here . . . |
  7        |. . . . near zone . . . . . . . . . . .|
  2.4      |============== THE LINE ===============|
  0        |  [bay 1] S1  HEROINE  S2 [bay 2]      |
 -3        \__________ bastion dais ______________/
```

**Hero landmark.** **The Broken Ring of VC-7**: a colossal station ring, about 2 km across, standing on edge to the left of the causeway and broken at its top. Its base pylon rises out of the abyss 60 m left of the lane at z 30; the ring's pale inner face blazes in the disk light. In frame: the lower arc fills the upper-left box (x 0–420, y 80–330) and leaves the top edge; the brightest region of the map is the lit inner face near (150, 180). This matches the accepted stage card `art-src/ui/stages-v2/c1-s1.png`.

**Depth layers.**
- Foreground frame: K5, the two bastion towers, banners stirring.
- Playfield: K1 with light wear, 12 decals (scorches far up the lane, none near the Line).
- Midground: the ring's base pylon (300 m tall, its lower half in frame), gantries linking it to the causeway's underside; two monoliths on the right at 250 m and 450 m.
- Far background: the ring's far arc and floating ring fragments; a second causeway 1 km below on the right.
- Sky: the black hole shadow centred above the top edge, its lower rim visible in the free sky strip; the disk's near side a vast gold band below both wedges; the photon ring brightest on the left (the side turning toward us).
- Time and light: "first light". The disk low ahead-left, warm gold; long shadows from pylons point toward the heroine; cyan fill on her; light dust shafts slanting from the upper left.
- Colour script: graphite and navy 60 %, orange-gold 30 % (left), cyan 10 %.

**Set dressing.** Dais 1; bastion towers 2 (11 m); edge pylons 20 (6–9 m); banners 6; ring base pylon 1 (300 m); ring arc card 1 (2 km); right monoliths 2 (180 m, 260 m); ring fragments 8–12 (20–80 m, instanced); coolant falls 3 (left two, right one); debris shoal 1 (40 rocks).

**Life on the map.**
- Vanguard packs at z 18–50 on the first frame; a dense reservoir (250 silhouettes) beyond the gate, glints shifting.
- One void manta (wingspan 150 m) gliding slowly below the right wedge, crossing in 40 s.
- Shuttles fleeing toward the citadel at the top corners.
- Light banners and the pylons' lamps pulse once on each surge warning.

**Sources.** K1–K14. Ring base pylon: Tripo by the owner (one model, used again in stage 7); ring arc and fragments: ChatGPT alpha cards in two layers; right monoliths: `wall-right-alpha-v3.png` (125) as a far card, one Tripo monolith as the near one (used again in stage 2); manta: ChatGPT card with a flap shader, or Tripo.

**What is wrong today.**
- The lane is a code-drawn steel corridor with orange-and-black hazard stripes on both walls and a red-brown glow over the lower deck: it reads as a loading dock, not a mythic causeway.
- The only landmark, the black hole, is a 116 px disc at y 50, behind the timer and a thin torus arch: in play it is almost invisible.
- About 37 % of the screen (the side wedges) is a flat poster with a swirl. Nothing lies below the deck, so the corridor floats on wallpaper.
- The hero is a 100 × 80 px faceless ship.
- The accepted stage card shows the Broken Ring, the heroine and a causeway; the fight then shows none of them.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone that runs from the bottom centre to a far gate near the top. The heroine stands small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, two white-gold sentinel gun drones at her shoulders, firing a cyan pulse stream and an orange heat beam, a small support drone above. The deck just ahead of her stays dark. A swarm of black glass creatures with orange cracks pours over the gate, one heavy brute among them. To the upper left a colossal broken station ring rises out of the abyss beside the causeway, its pale inner face blazing gold. Below both sides of the causeway, a vast orange-gold accretion disk spirals in haze; the black hole's shadow sits beyond the gate. Low warm back light, cyan rim light, dust shafts. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 4. Stage 2 (`c1-s2`): "Leader Hunt"

**Story beat.** On Span Two the Horde sends Pack Leaders; bring down three of five and the swarm breaks and flees.

**Gameplay layout.** Hunt 3 of 5 Pack Leaders (arrive at 20, 58, 96, 134, 172 s), cap 240 s. Each Leader walks behind 8 swarm. One surge at 70 s. Brute packs from 30 s. A Leader is read by its size (1.25 × a Brute), gold veins, a gold beacon column and a lane mark on the deck.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 36        |   escort 8 swarm                 |  (R) HERALD MONOLITH
 30        |      [L] Pack Leader + beacon    |   tilted, 500 m,
 22        |   Brute + 5                       |   x +80, z 60
 14        |. . . . . armour drain . . . . . . |
  7        |. . . . near zone . . . . . . . . .|
  2.4      |============== THE LINE ===========|
  0        |  [bay 1] S1  HEROINE  S2 [bay 2]  |
 -3        \__________ bastion dais __________/
  lane mark: a gold strip runs down the deck under each live Leader
```

**Hero landmark.** **The Herald Monolith**: a gigantic tilted monolith of dark stone wrapped in steel gantries, about 500 m tall, standing in the abyss 80 m right of the causeway, leaning toward the lane. Its broad pale face catches the strongest disk light. A horn-like antenna array crowns it; when a Leader arrives the array glows gold (the Leader's horn sound has a source in the world). In frame: upper-right box, brightest region near (1120, 160). Matches `art-src/ui/stages-v2/c1-s2.png`.

**Depth layers.**
- Foreground frame: K5; the right bastion tower damaged (cracked crown).
- Playfield: K1, more scorches, fallen stone blocks against the parapets (outside the lane).
- Midground: the monolith; three smaller leaning pylons on the left at 150–300 m.
- Far background: Span One and the Broken Ring behind and left, half lost in haze (seen only in the intro sweep).
- Sky: black hole shadow above the top edge; the disk bigger than stage 1; the Doppler-bright side on the right this time.
- Time and light: "beacon gold". The disk ahead-right, warmer and higher; gold dust; long shadows of the pylons fall leftward across the void (not over the deck).
- Colour script: graphite 55 %, gold 35 %, cyan 10 %. Gold is the language of Leaders: keep other gold accents low so beacons read.

**Set dressing.** Dais 1; bastion towers 2; edge pylons 20; banners 4 (two torn); fallen stone blocks 6–8 (2–4 m) outside the lane; left pylons 3 (120–220 m); Herald Monolith 1 (500 m); antenna array crown 1; coolant falls 2; debris shoal 1.

**Life on the map.**
- Reservoir beyond the gate parts like a crowd when a Leader comes through, so the player sees it coming 2 s before it crosses z 40.
- The monolith's crown glows gold on each Leader arrival; shuttles avoid it.
- Two mantas far below on the left.
- When the hunt is won, the reservoir visibly scatters back into the black hole's shadow.

**Sources.** K1–K14. Herald Monolith: near part (base and gantries, 150 m of it in frame) as Tripo by the owner (reused from stage 1's monolith with a new texture), upper part a ChatGPT card; antenna glow is a shader; fallen blocks: CC0 rock or ruin kit.

**What is wrong today.** Identical to First Shift. The Leader's beacon is the only new visual; the map says nothing about a hunt. The beacon column and the gold lane mark fight with the orange hazard stripes on the walls.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, two white-gold sentinel gun drones at her shoulders, a small support drone above. The deck just ahead of her stays dark. Mid-lane, a huge black glass Pack Leader with a golden crest walks behind a wedge of smaller cracked creatures, a thin gold beacon of light rising from it. To the upper right a gigantic tilted monolith rises out of the abyss beside the causeway, its pale face blazing gold, a crown of antennas glowing. Far below, a vast accretion disk spirals in haze. Warm gold back light from ahead right, long shadows, cyan rim light. Painterly-realistic, big readable shapes. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 5. Stage 3 (`c1-s3`): "Rift Wall"

**Story beat.** Span Three crosses a wound in space: the void tears open under the bridge and the Horde climbs out of the cracks beside the Line.

**Gameplay layout.** Hold 165 s. **Rift** every 30 s from 25 s: a crack at the foot of the left or right wall (seeded), z 9–13, warns 2.5 s (it glows orange), then 8 foes pour out within gun range. Surges at 55 s and 140 s.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 30        |                                  |
 22  (L) THE TEAR: a 600 m crack in space under the bridge, wide on the left,
 18        |                                  |   narrow on the right
 13    /// |rift L (seeded)      rift R (seeded)| \\\
  9    /// |   8 foes pour out here            | \\\
  7        |. . . . near zone . . . . . . . . .|
  2.4      |============== THE LINE ===========|
  0        |  [bay 1] S1  HEROINE  S2 [bay 2]  |
 floating slabs drift up beside both parapets at z 8-20
```

**Hero landmark.** **The Torn Span**: a vast tear in space running **under** the causeway, wide and blazing on the left, narrowing on the right. Its edges burn orange and violet; inside is a deep black with faint stars of another place. Slabs of the causeway's underside have broken loose and float up beside the parapets. The rifts on the deck are where this tear reaches up through the wall: when a rift warns, the tear below brightens on that side. In frame: the wide end fills the left wedge (x 0–330, y 150–420), the narrow end the lower-right wedge. **The tear never crosses the deck** (the accepted stage card draws it across the lane; in the fight that would hide play).

**Depth layers.**
- Foreground frame: K5; the left bastion tower tilted, one of its stones floating.
- Playfield: K1 with cracks running in from both walls at z 9–13 (decals, dark until a rift warns).
- Midground: floating slabs (8–14, 3–12 m) rising slowly beside the parapets; the torn underside truss.
- Far background: the disk seen through the tear's edges; ring fragments.
- Sky: black hole high; its light partly hidden by drifting station debris so the tear is the brightest thing.
- Time and light: "torn violet". The tear lights the deck edges from below; the disk is a softer gold behind. Weather: slow upward drift of dust and small slabs (gravity broken here); heat shimmer over the tear.
- Colour script: graphite 50 %, orange 25 %, violet 15 % (only at the tear), cyan 10 %.

**Set dressing.** Dais 1; bastion towers 2 (left tilted); edge pylons 16 (4 broken stubs); floating slabs 8–14 (3–12 m); tear 1 (600 m long); cracked wall segments at z 9–13 both sides (4); coolant falls 2, bending sideways into the tear; debris shoal 2.

**Life on the map.**
- Small Horde climbers crawl along the tear's edges far below, always moving toward the bridge (cheap cards).
- Slabs turn slowly; one breaks off and rises every 20 s.
- The cracked wall segment on the warned side glows hotter through the 2.5 s warning, matching the sound.
- Reservoir beyond the gate as usual.

**Sources.** K1–K14. Tear: a shader on a world-space mesh under the bridge (meets the VFX standard: charge = glow, release = open, travel = foes crawl, impact = burst, aftermath = embers), plus a ChatGPT card for its deep interior; floating slabs: CC0 rock or ruin kit pieces in the deck's materials, instanced; cracked wall: K3 variant mesh.

**What is wrong today.** The rift is a crack drawn in a shader at the wall's foot of the same industrial corridor. There is no tear, no broken bridge, no reason in the world for foes to appear there. The wall stripes make the warning glow hard to see.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape blown back, two white-gold sentinel gun drones, a small support drone. The deck just ahead of her stays dark. Under the causeway a vast tear in space runs across the abyss, wide and blazing orange and violet on the left, narrow on the right; broken slabs of the bridge float upward beside both walls. On the left wall, one glowing crack lets black glass creatures with orange cracks climb onto the deck. The tear never crosses the deck. Far behind, the black hole and a softer gold accretion disk. Light from below, violet edges, rising dust. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 6. Stage 4 (`c1-s4`): "Shining Shields"

**Story beat.** Span Four runs past the station's old shield array: the Horde has stolen its light and walks behind walls of blue.

**Gameplay layout.** Hold 165 s. No hazard. Learning rule "missing letters". Shield Guard packs (a Shield Guard and a wedge of 6) from 20 s; the shield is a 2.6 m blue energy wall 0.8 m in front of its bearer, facing the heroine. A surge turns violent 25 % of the time. One bay starts at level 2.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 30        |    ( ) ( )  Shield Guards in wedges |  (R) AEGIS ARRAY
 22        |      )   (    blue walls face her   |   three emitter pylons,
 14        |. . . . . armour drain . . . . . . . |   a cracked hex curtain
  7        |. . . . near zone . . . . . . . . . .|   across the void
  2.4      |============== THE LINE ==============|
  0        |  [bay 1] S1  HEROINE  S2 [bay 2]     |
 -3        \__________ bastion dais _____________/
```

**Hero landmark.** **The Aegis Array**: three colossal shield-emitter pylons (250–350 m) standing in the abyss to the right, still projecting a vast cracked hexagonal curtain of blue light that hangs across the void, flickering, with holes burned through it. The Shield Guards' blue walls are pieces of this light. Far behind, inside the black hole, the Void Leviathan's shadow rises for the first time. In frame: pylons and curtain in the upper-right box; the curtain's brightest cells near (1050, 220); the Leviathan shadow only in the free sky strip, low contrast.

**Depth layers.**
- Foreground frame: K5; two dead shield emitters (small, 3 m) on the bastion, sparking.
- Playfield: K1; hex-shaped scorch decals where shields broke.
- Midground: the three emitter pylons and the curtain; one fallen emitter dish in the left wedge (80 m).
- Far background: the Leviathan's dark head and horns inside the black hole's shadow.
- Sky: the disk partly hidden by the curtain on the right, blazing on the left.
- Time and light: "aegis blue". Two lights fight: cold blue from the right (curtain), warm gold from ahead-left (disk). Weather: ion sparks falling from the curtain like snow.
- Colour script: graphite 50 %, blue-cyan 25 % (right), gold 20 % (left), violet 5 % (Leviathan).

**Set dressing.** Dais 1; bastion towers 2; dead small emitters 2; edge pylons 20; emitter pylons 3 (250–350 m); hex curtain 1 (1.2 km wide); fallen dish 1 (80 m); hex scorch decals 6; ion spark particles; coolant falls 2.

**Life on the map.**
- The curtain's cells flicker and die one by one through the stage; a hole opens on each surge.
- Ion sparks drift down past the right parapet.
- The Leviathan's shadow lifts slightly at each surge (ART_DIRECTION §8.3: "the void beast rises in the black hole on a surge").
- Reservoir with blue glints (Shield Guards waiting).

**Sources.** K1–K14. Emitter pylons: one Tripo model by the owner, instanced three times with different scale; curtain: a hex energy shader (reuse the Shield Guard wall shader in `src/view/hazard-fx.ts` at landmark scale); Leviathan shadow: `art-src/arena-v2/void-leviathan-alpha-v3.png` (125) as a dim card; fallen dish: CC0 kit or Tripo.

**What is wrong today.** Same corridor. The blue shield walls are the only blue in a frame that is otherwise orange and black; nothing in the world explains where shields come from. Orange stripes on the walls compete with the shield flashes.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, two white-gold sentinel gun drones firing at the lane, a small support drone above. The deck just ahead of her stays dark. Mid-lane, black glass creatures with orange cracks advance behind floating faceted walls of blue light. To the upper right, three colossal shield emitter pylons rise out of the abyss, projecting a vast cracked hexagonal curtain of blue light across the void. Far beyond the gate, inside the black hole, the faint shadow of a gigantic horned creature rises. Cold blue light from the right, warm gold from the accretion disk on the left, falling sparks. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 7. Stage 5 (`c1-s5`, planned, checkpoint): "Buried Nests"

**Story beat.** Span Five passes a capsized freighter fused to the bridge; the Horde has nested inside it. Burn both nests and the span becomes the checkpoint.

**Gameplay layout.** Destroy 2 Nests, cap 300 s. Nests appear at z 30–36 and crawl to z 10, spawning 6 swarm every 7 s (down to 3.5 s). A nest guard (a Brute and 2 Shield Guards) at 40 s. Low calm rate (1.6 a second). Winning lights the checkpoint and opens bay 3.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 36  (L) HIVE HULK  | [N1] nest appears          |
 30   capsized      |              [N2]          |
 22   freighter,    |  nests crawl toward z 10   |
 14   bow on the    |. . . . armour drain . . . .|
 10   parapet       |  nests stop here           |
  2.4      |============== THE LINE ===========|
  0        |  [bay 1] S1  HEROINE  S2 [bay 2]  |   checkpoint beacon on the
 -3        \__________ bastion dais __________/   right bastion tower
```

**Hero landmark.** **The Hive Hulk**: a capsized freighter, about 400 m long, its bow crashed onto the causeway's left side beyond the gate and its stern hanging into the abyss. Its belly is cracked open and pulses with orange egg-light; ropes of black glass resin run from the cracks onto the bridge. In frame: the hull fills the upper-left box and the top-left corner; its pulsing belly glows near (200, 140). The nests on the deck read as pieces broken off it.

**Depth layers.**
- Foreground frame: K5; the right bastion tower carries the dark checkpoint beacon that ignites white-gold on victory.
- Playfield: K1 with resin stains (dark glossy decals with orange veins) from the gate down to z 10.
- Midground: the Hulk; its torn cargo containers hanging below on chains.
- Far background: the disk, larger; Span Four's curtain faint behind.
- Sky: black hole shadow; the disk's glow dimmed by the Hulk's smoke on the left.
- Time and light: "ember brood". Deep red-orange inner light from the Hulk; smoke drifting right over the void; the checkpoint beacon is the one cool light.
- Colour script: graphite 55 %, deep orange-red 30 %, cyan 10 %, white-gold 5 % (beacon).

**Set dressing.** Dais 1; bastion towers 2 (beacon on the right); edge pylons 18; Hulk 1 (400 m); hanging containers 6–8 (12 m); resin decals 10–14; smoke plume 1 (slow, out over the void); coolant falls 1; debris 1 shoal.

**Life on the map.**
- The Hulk's belly pulses in step with the nests' spawn timer (a 2 s brighter pulse before each brood).
- Swarm crawl out of the Hulk's cracks far up and drop onto the bridge beyond the gate (reservoir feeding).
- On victory: the checkpoint beacon lights, its light runs down both parapets to the gate, the Hulk's glow dies.

**Sources.** K1–K14. Hulk: ChatGPT painted cards in three layers (it is 150 m+ away) plus one Tripo bow section where it touches the causeway; containers: CC0 sci-fi kit; resin decals: new ChatGPT decal sheet; checkpoint beacon: part of the bastion tower model, emissive.

**What is wrong today.** The stage does not exist yet (R2). If it shipped on today's scene, the nests would crawl out of nowhere on the same striped corridor.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, two white-gold sentinel gun drones, a small support drone above. The deck just ahead of her stays dark. Two pulsing hive nests of black glass and orange light crawl down the lane, small creatures spilling from them. To the upper left, a huge capsized freighter has crashed onto the far end of the causeway, its cracked belly glowing deep orange, its stern hanging into the abyss, dark smoke drifting over the void. Far below, the accretion disk. Deep red-orange light from the wreck, a cool white-gold beacon on a tower beside her. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 8. Stage 6 (`c1-s6`, planned): "Ion Storm"

**Story beat.** Past the checkpoint, Span Six runs into an ion storm boiling up from the disk; lightning numbs her sentinels one at a time.

**Gameplay layout.** Hold 165 s. **Ion storm** every 30 s from 20 s: one bay (seeded, never the same twice) flashes blue for 2.5 s, then its sentinel stops firing for 6 s; typing still loads it. Three bays (bay 3 open). Shield Guards and Brutes.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 30        |                                  |  (R) STORM CONDUCTOR
 22        |   Brutes, Shield Guards           |   broken antenna spire,
 14        |. . . . armour drain . . . . . . . |   lightning to the clouds
  2.4      |============== THE LINE ===========|
  0        | [bay 1] S1  S3 HEROINE  S2 [bay 2]|  <- a bolt from the storm
 -3        \__________ bastion dais __________/     hits the warned sentinel
 storm clouds boil below both wedges
```

**Hero landmark.** **The Storm Conductor**: a broken antenna spire, about 450 m, on the right, its top shattered into forked prongs that drink lightning from the storm clouds below. Its lightning is the hazard's source: the warning is a charge running up the spire, the strike is a bolt that arcs across the void to the warned sentinel. In frame: upper-right box; bolts travel from (1150, 120) toward the sentinel at the bottom, outside the deck where possible (they cross the near deck for 2–3 frames only).

**Depth layers.**
- Foreground frame: K5; banners whipping; rain of sparks.
- Playfield: K1, wet-looking only where lightning hits (small, quick).
- Midground: the spire; storm clouds of violet-blue plasma boiling up from below in both wedges, hiding the disk.
- Far background: lightning flashes inside clouds; the disk seen through gaps.
- Sky: black hole dim behind the storm.
- Time and light: "storm". The disk's gold is muted to patches; cold blue-white flashes light the scene for 2–4 frames; between flashes it is the darkest stage.
- Colour script: navy-violet 60 %, blue-white 20 % (flashes), gold 15 %, cyan 5 %.

**Set dressing.** Dais 1; bastion towers 2; edge pylons 20 (lamps flickering); storm spire 1 (450 m); cloud banks 3 layers (shader volumes or cards); lightning bolts (VFX); spark rain; coolant falls 0 (frozen).

**Life on the map.** Clouds roll; distant lightning every 3–6 s (dim, never during a surge's first seconds); the spire's charge runs up during each warning; one manta fleeing through the clouds.

**Sources.** K1–K14. Spire: ChatGPT cards in two layers plus a Tripo base section if it comes closer than 300 m; clouds: three.js volume-cloud example (MIT) or layered cards with a flow shader; lightning: VFX standard five phases (charge on the spire, release, travel to the sentinel, impact on the bay's sentinel, aftermath sparks).

**What is wrong today.** Not built (R2). The planned warning is a blue flash on the DOM bay only: the world gives no cause.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape whipping, three white-gold sentinel gun drones around her, a small support drone above. The deck just ahead of her stays dark. Black glass creatures with orange cracks advance, some behind blue shield walls. To the upper right a broken antenna spire rises from the abyss, a bolt of blue-white lightning leaping from its forked crown toward one of her sentinels. Violet-blue storm clouds boil up from below on both sides, hiding most of the accretion disk. Dark stormy light, cold flashes, warm gaps. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 9. Stage 7 (`c1-s7`, planned): "Splitter Swarm"

**Story beat.** Span Seven runs beside its twin, which has shattered and drifts apart; the Horde here shatters too, each body breaking into shards.

**Gameplay layout.** Hunt 4 of 6 Pack Leaders (every 25 s from 20 s), cap 240 s. Rift (every 35 s). Splitters (break into 3 shards on death) 14 % of foes.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 36  (L) THE SHATTERED |  [L] leader + escort       |
 30   TWIN: a parallel |   splitters (break in 3)   |
 22   causeway broken  |                            |
 13   into drifting  //|rift (seeded)  rift (seeded)|\\
  9   segments       //|                            |\\
  2.4      |============== THE LINE ===============|
  0        |  [bay 1] S1  S3  HEROINE  S2 [bay 2]  |
```

**Hero landmark.** **The Shattered Twin**: a second causeway, parallel to VC-7, 120 m to the left and 40 m lower, broken into a dozen great segments drifting apart, each still carrying its parapets, pylons and dead lamps; one segment tilts almost vertical. In frame: the segments step away from the lane through the left wedge from (300, 400) up to (0, 80); the Broken Ring base from stage 1 reappears far behind (same model, new place).

**Depth layers.**
- Foreground frame: K5.
- Playfield: K1 with glass shard decals everywhere (the splitters' remains), but none under the word line.
- Midground: the twin's segments (40–120 m each).
- Far background: ring base pylon (reused), fragments.
- Sky: the disk now fills the lower half of both wedges; the black hole bigger.
- Time and light: "shatter". Strong side light from the disk's bright left side; every segment's edge rim-lit; glass glints.
- Colour script: graphite 50 %, orange-gold 35 %, cyan 10 %, white glints 5 %.

**Set dressing.** Twin segments 10–12 (40–120 m, instanced variants of one kit causeway section); dead lamps on them; shard decals 16; ring base pylon 1 (reused); edge pylons 14 (several leaning); debris shoals 2.

**Life on the map.** Segments drift and rotate very slowly; one grinds against another every 30 s with sparks; shard glints on the deck flash when a gun light passes.

**Sources.** K1–K14; twin segments: the K1 and K3 meshes reused as a broken section (no new art); ring base pylon from stage 1 (Tripo).

**What is wrong today.** Not built (R2).

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, three white-gold sentinel gun drones, a small support drone above. The deck just ahead of her stays dark. Round black glass creatures with orange seams burst into shards under her fire; a huge Pack Leader with a golden crest walks behind them. On the left, a second parallel causeway lies broken into great drifting segments stepping away into the abyss, one tilted almost upright, all rim-lit. Below both sides a vast blazing accretion disk; the black hole beyond the gate. Strong golden side light, glinting glass. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 10. Stage 8 (`c1-s8`, planned): "Black Well"

**Story beat.** Span Eight crosses the station's collapsed core; its gravity bleeds up through the deck and drags the Horde (and her shots) into a knot.

**Gameplay layout.** Destroy 3 Nests, cap 300 s. **Gravity well** at x ±4 (seeded), z 18, radius 8 m: pulls foes toward its centre and bends Pulse rounds and Scatter pellets; Rail and Heat Beam fly straight; Star Mortar shells drift 1 m toward it.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 36        | [N1]          [N3]               |
 26        |     .---- well r 8 m ----.       |
 18        |    (  W at x -4 or +4     )      |   THE SINK below the bridge:
 10        |     '---- (seeded) -----'  [N2]  |   a collapsed core sphere,
  2.4      |============== THE LINE ===========|   debris spiralling into it
  0        |  [bay 1] S1  S3 HEROINE  S2 [bay 2]|
```

**Hero landmark.** **The Sink**: the station's collapsed core, a pale sphere about 300 m across, 200 m below the causeway, wrapped in a slow spiral of debris, plates and chains being drawn into it. It sits under the well's side (left or right, seeded) and shows in that wedge; its debris spiral reaches across both wedges. The well on the deck is where the core's pull comes through: plates around it lift a few centimetres and glow faintly at the seams. In frame: the core in the lower half of the well's wedge (y 250–450), its spiral rising to the top corners.

**Depth layers.**
- Foreground frame: K5; chains from the bastion towers pulled taut toward the core.
- Playfield: K1 with a ring of lifted plates round the well (a view-only displacement on the deck mesh, ≤ 6 cm, no dark overlay over foes).
- Midground: the core and the debris spiral; bent pylons leaning toward it.
- Far background: the disk bending (lensing ripple) around the core's edge.
- Sky: the black hole large; the disk fills most of both wedges.
- Time and light: "sink". The scene is desaturated toward the well; the core glows pale white-violet from within; light bends.
- Colour script: graphite 55 %, pale white-violet 15 %, gold 25 %, cyan 5 %.

**Set dressing.** Core sphere 1 (300 m); debris spiral (60–120 instanced pieces, 1–20 m); taut chains 4; bent edge pylons 8; lifted-plate ring 1; nests 3 (gameplay).

**Life on the map.** The spiral turns once a minute; small debris streak past the well's side of the deck; the well's ring of plates breathes with the pull.

**Sources.** K1–K14; core: a shader sphere with a ChatGPT texture (cracked pale shell); debris: CC0 rocks and kit pieces, instanced; lensing ripple: screen-space distortion limited to the wedge.

**What is wrong today.** Not built (R2).

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, three white-gold sentinel gun drones, a small support drone above. The deck just ahead of her stays dark. Left of the lane's middle, a circle of deck plates lifts slightly and bends the light, dragging black glass creatures with orange cracks into a tight knot; crawling hive nests approach. Below the left side of the causeway, a pale cracked sphere hangs in the abyss, a slow spiral of debris and chains falling into it. The accretion disk bends around it. Desaturated light, pale violet glow from below, gold rims. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 11. Stage 9 (`c1-s9`, planned): "Voice of the Station"

**Story beat.** On Span Nine the station's archive spire still speaks; it shows the meanings and she must answer with the words, while the void keeps tearing.

**Gameplay layout.** Hold 180 s. Learning rule "meaning" (the bay shows the Vietnamese meaning; she types the English word). Rift every 30 s. Three surges (55, 120, 160 s). Brutes, splitters, Shield Guards.

```text
 z                x=-12                       x=+12
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 36  (L) ARCHIVE SPIRE |                         |
 30   rings of light   |  mixed packs            |
 22   turning slowly   |                         |
 13              /// |rift (seeded)  rift (seeded)| \\\
  2.4      |============== THE LINE ===========|
  0        |  [bay 1] S1  S3 HEROINE  S2 [bay 2]|
```

**Hero landmark.** **The Archive Spire**: a slender white stone and gold spire, about 600 m, on the left, ringed by three slow-turning rings of abstract glyphs (shapes, never readable letters) that brighten each time she completes a word. It is the calmest, most sacred place of the chapter, the last thing the station built. In frame: upper-left box, rings brightest near (180, 200).

**Depth layers.**
- Foreground frame: K5 with fresh white-gold banners (the order's colours).
- Playfield: K1, cleaner; the glyph inlays in the stone bands glow faintly white-gold.
- Midground: the spire; two smaller lectern towers on the right (150 m).
- Far background: the disk and the black hole now huge; the Breach visible as a dark notch at the far end in the intro sweep.
- Sky: the brightest stage overall, but the brightness lives in the left wedge.
- Time and light: "choir dawn". White-gold light from the spire's rings plus the disk's gold; soft, reverent; few particles.
- Colour script: graphite 50 %, white-gold 30 %, orange 15 %, cyan 5 %.

**Set dressing.** Spire 1 (600 m); glyph rings 3 (80–160 m across); lectern towers 2; banners 6 (white-gold); edge pylons 20; rift-cracked wall segments 4.

**Life on the map.** Rings turn and pulse with her finished words (view-only, read from the word event, never brighter than the deck limit near the word line); glowing motes rise from the spire; rifts tear as in stage 3, but their violet is the only dark note.

**Sources.** K1–K14; spire: ChatGPT cards in two layers; glyph rings: shader rings with an abstract glyph texture from ChatGPT (`deck-decals-alpha-v3.png`'s glyph ring as the style match); lectern towers: Tripo or CC0 kit.

**What is wrong today.** Not built (R2).

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight causeway of graphite steel and pale stone from the bottom centre to a far gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, three white-gold sentinel gun drones, a small support drone above. The deck just ahead of her stays dark. Mixed black glass creatures with orange cracks advance; a violet crack opens at the foot of the right wall. To the upper left, a slender white stone and gold spire rises out of the abyss, ringed by three slow turning rings of glowing abstract glyphs, never letters. Below, a vast golden accretion disk; the black hole looms large beyond the gate. Soft white-gold light, reverent and calm, gold rims. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 12. Stage 10 (`c1-s10`, planned, boss): "The Warden"

**Story beat.** At the Breach, the end of VC-7 at the edge of the event horizon, the Warden holds the gate open for the Horde, and behind it the Void Leviathan rises from the black hole.

**Gameplay layout.** Boss, 5,000 HP, three phases. Steps through the gate at 20 s; stands at z 22 (P1, max 50 s), z 15 (P2, max 50 s), z 8 (P3). Escorts: 6 swarm every 8 s from beside it (P1), Shield Guard packs (P2), splitters (P3). **Slam**: a red lane with warning stripes from the boss to the Line, plus a block word; type it in time to block.

```text
 z                x=-12                       x=+12
 52   . . . . THE BREACH GATE (ring gate, torn open) . . . .
 40  ABYSS =========== GATE (spawn) ===========  ABYSS
 22        |        [WARDEN]  P1              |  (R) VOID LEVIATHAN rising
 15        |        [WARDEN]  P2              |   out of the black hole,
  8        |        [WARDEN]  P3              |   coiling up the right side
           |        ||| slam lane |||          |
  2.4      |============== THE LINE ===========|
  0        |  [bay 1] S1  S3 HEROINE  S2 [bay 2]|
```

**Hero landmark.** Two pieces, one on each side of the gate so they never cover the lane:
- **The Breach Gate**: a ring gate 300 m tall at the causeway's end (z 60–80), its frame torn open, chains hanging; the black hole's shadow fills it. In frame its lower half crowns the free sky strip and both upper corners.
- **The Void Leviathan**: a colossal serpent of black glass with orange cracks and a crown of spines, coiling up out of the black hole on the right. In frame: its body rises through the upper-right box, its head near (1080, 110) looking down at the Line. It roars (a head lift and an orange flare) on each phase change.

**Depth layers.**
- Foreground frame: K5; the bastion towers' banners burning; the heroine's dais glyph ring at full light.
- Playfield: K1 heavily scarred, scorched, cracked; red slam lanes as a VFX on top.
- Midground: the Breach Gate and its chains; the Warden on the deck (the boss model).
- Far background: the Leviathan's coils and the event horizon; the disk fills both wedges edge to edge.
- Sky: the black hole's shadow huge beyond the gate; the photon ring arcs over the top of the frame.
- Time and light: "event horizon". Molten gold everywhere except the black shadow; violet in the Leviathan's cracks; red only for the slam. Weather: embers and ash streaming toward the black hole (the pull), heat shimmer.
- Colour script: black 35 %, molten gold 40 %, violet 10 %, cyan 10 % (her), red 5 % (slam only).

**Set dressing.** Breach Gate 1 (300 m); chains 6 (100 m); Leviathan 1 (2 km long); broken edge pylons 12; burning banners 4; scorch and crack decals 20 (none under the word line); ember stream particles.

**Life on the map.** The Leviathan breathes and shifts its coils; the Horde reservoir pours out of the gate's shadow at every escort call; the gate's chains swing when the Warden roars; on the boss's death the Leviathan sinks back with a long flare (the chapter's ending shot, and a tease for the next chapter).

**Sources.** K1–K14. Warden: today's `warden-rainbow` boss model is not in this game's manifest; the owner makes it in Tripo (or it is imported from Space's library through `pnpm models:prepare --import`), animated by us (procedural motion and VFX are ours). Breach Gate: ChatGPT cards plus one Tripo section of the gate's foot. Leviathan: `art-src/arena-v2/void-leviathan-alpha-v3.png` and `art-src/ui/boss/boss-void-leviathan.png` as source looks; in game a set of painted alpha cards (head, coils) with a slow flow shader on the cracks; a Tripo model only if the intro sweep needs real parallax.

**What is wrong today.** Not built (R3). The boss has no arena, no Breach and no Leviathan in the game; only a splash image exists.

**ChatGPT prompt.**
```text
Gameplay concept painting for Last Line, a premium sci-fi typing survival game, from the game camera: high behind and above a lone heroine, looking down about 36 degrees along a straight, scarred causeway of graphite steel and pale stone from the bottom centre to a torn ring gate near the top. The heroine is small at bottom centre: a woman gunner in white-and-gold armour, cyan visor, navy cape, three white-gold sentinel gun drones, a small support drone above. Mid-lane stands a towering armoured warden of black glass and orange cracks, a red warning lane on the deck leading from it to her. Beyond the gate, the black hole's shadow fills a colossal broken ring gate hung with chains. On the upper right a gigantic void serpent of black glass with orange cracks and a crown of spines coils up out of the black hole, looking down at her. A molten gold accretion disk fills the abyss on both sides. Embers stream toward the gate. Painterly-realistic. Landscape 16:9. No text, UI, letters or numbers.
```

---

## 13. Later chapters (planned in `SURVIVAL_MODE_PLAN.md` §4.0, not in code)

The plan has 60 chapters of 10 stages; each chapter is **one map** with one foe family and one boss, and the plan names nebulae, asteroid belts and broken stations as settings. The sim field stays 24 × 40 m in every chapter. Short concepts for the chapters that teach the remaining hazards:

- **Chapter 2 · Ashfall Belt** (hazard: meteor rain). The causeway threads a debris ring of a shattered moon. Landmark: the moon's split half on the upper left, a 10 km cliff of rock and old mining scaffolds; meteor streaks fall across the wedges and strike marked circles on the deck (the warning). Colour: rust and grey with cyan. Sources: CC0 rock sets instanced, ChatGPT cards for the moon, a meteor VFX by the standard.
- **Chapter 3 · Nebula Locks** (hazard: nebula fog that hides the far lane). A causeway of lock gates through a violet-teal nebula. Landmark: a dry dock holding a dead capital ship on the right. The fog rolls in from the wedges and over the far half of the deck as a shader, never over the near zone. Colour: violet, teal, white-gold.
- **Chapter 4 · Sunward Array** (hazard: horizon glare in pulses). A bridge of mirror panels facing a blue companion star that rises over the gate. Landmark: a ring of giant mirrors swinging toward the star; each glare pulse is a mirror catching it. Colour: blue-white and gold.
- **Chapter 5 · The Cargo Maze** (hazards: minefield, moving walls). A docking causeway where cargo blocks slide across the lane on rails (moving walls) and drifting mines tumble. Landmark: a stacked container city on both sides, cranes the size of towers. Colour: graphite, signal amber, cyan.
- **Chapter 6 · The Twin Spans** (hazard: two lanes swap). Two parallel causeways side by side with crossover bridges; the heroine's lane is lit, the other dark until the swap. Landmark: a central pylon that rotates to swap them. Colour: navy, cyan, gold.

Chapters 7–60 reuse these biome kits with new foe families, light scripts and one new landmark each.

---

## 14. Why the current maps fail (Last Line, 01/11/2026)

**1. The map is a code-drawn stand-in, not art.** Every surface in `src/view/scene.ts` is made in code: the deck's plates, rivets, lane dashes and chevrons are a fragment shader; the parapets and posts are grey boxes with amber box lamps; the far arch is a squashed torus; the "conduits" are 14 cm boxes. AGENTS.md now forbids code-drawn scenery. Shaders are fine for light and VFX, not as the painting of the world.

**2. It is the wrong world.** The owner chose direction B (Lightbearer, a causeway of graphite steel and pale ancient stone at the edge of a black hole) on 29/10. The menus, the stage cards and the logo already show that world (tickets 121, 126, accepted). The fight still shows the old direction A corridor: orange-and-black hazard stripes on both walls, a red line, a red-brown glow over the lower deck. Going from the stage card to the fight is a downgrade the player sees every time.

**3. The landmark is hidden.** The black hole is the game's whole promise ("Last Line before the black hole"). In the fight view it is a 116 px disc centred at y 50 of 720, under the timer panel and behind the thin arch. Nothing in the frame is ten or a hundred times bigger than the hero (ART_DIRECTION §1.1, "something that makes the player small").

**4. More than a third of the screen is wallpaper.** The camera looks down 36°, so the side areas beside the deck (about 37 % of the frame, nearly half with the strip above the gate) look down past the deck edge. Today they show a camera-facing plane with a swirl and a few stars. There is nothing below or beside the causeway: no abyss, no structures, no fog, no parallax. The corridor reads as a flat strip floating on a poster.

**5. No depth layers, no light direction.** There is no foreground frame, no midground, no far layer; just deck and backdrop. Light is a uniform warm wash plus three directional lights; no shadows, no image-based light, no rim on the foes or the hero. The "danger glow" turns the whole near deck red-brown.

**6. The loudest colours are in the wrong place.** Orange-black stripes on both walls are the most saturated pixels in the frame, and they are orange like the foes' cracks: the eye goes to the walls, and the horde blends into them at the edges.

**7. The hero is a small faceless ship.** The Vanguard ship is about 100 × 80 px at the bottom. The Lightbearer, her sentinels and a support drone have source pictures (ticket 156) but no model in the game.

**8. Every stage looks the same.** First Shift, Leader Hunt, Rift Wall and Shining Shields, and the Trial, share one scene. Only the foes and the hazard effects change; no stage has its own landmark, light or weather.

**9. No life outside the fight.** Apart from the foes and the conduit pulses, nothing moves: no creatures, no ships, no banners, no horde massing beyond the gate before it enters.

**10. It looks soft.** The deck has no texel detail (it is a noise shader), the bloom halo spreads over it, and High renders at a pixel ratio of 1.5. Even with sharp foes the frame reads blurry, which matches the owner's note that Last Line's shots are blurry.

**11. Good art exists but sits unused.** The arena kit v2 (`art-src/arena-v2/`, ticket 125: deck tile, causeway edge, two walls, far rings, black hole sky, Leviathan, decals) was made on 29/10, self-scored 8, and was never judged or wired. Even used, it is a set of flat cards: on its own it cannot give the depth below the deck that this camera needs.

**What fixes it, in order:**
1. Build the K-kit (§1.4) as real 3D: a textured deck, parapets, pylons and the bastion from free CC0 PBR kits and the 125 textures, and the heroine group from the owner's Tripo models.
2. Put the abyss under the causeway: the disk as a world-space mesh below the bridge, midground structures rising from it, fog layers, painted cards only beyond 300 m.
3. Give each stage its landmark in a side wedge, its light script and its weather, all from data.
4. Score every stage in game at 1280 and 1920 against the owner's reference and the stage's agreed concept painting: M ≥ 8, the word-line luma limit kept, horde wash-out ≤ 10 %, ≤ 60 draw calls on High.
