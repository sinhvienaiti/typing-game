# Last Line: map concepts, stage by stage (01/11/2026, v1.2)

> **For:** the owner, ChatGPT (art-director review, then one concept painting over a base image), the map lane.
> **Game:** Last Line (`games/typing-survival`). Typed words load guns that hold one straight lane on a space station against the Black Hole Horde.
> **Status:** concepts only. No code changed. Rules, sim and camera stay as they are; only what the player sees changes.
> **v1.2 (01/11/2026, after ChatGPT's art-director review, 8.0/10):** map 1 takes every fix of `typing-survival-CHATGPT_REVIEW.md` (ivory not gold, one light budget, a darker lower abyss, a thick fractured Ring, ChatGPT's painting prompt), stages 3 and 6 take its notes; a critic pass then aligned the trial and stages 4, 5, 7, 8 and 9 with the same colour reservations and light budget; layout and camera unchanged.
> **v1.1 (revision 2, 01/11, after the critic's five fixes):** every screen coordinate is recomputed with one projection script; the battle frame shows **no sky and no horizon**; the gun cards sit at variant A (owner O7); the hero is the woman gunner with a support drone (owner); the Horde is purple (owner O5); life first, and creatures without a source are gone; the Tripo list follows what the battle frame shows; only verified free commercial-safe sources. **Map 1** (Chapter 1, stage 1, "First Shift") is complete and has a base image; the other maps are short.
> **Sources read:** `docs/SURVIVAL_MODE_PLAN.md`, `docs/BUILD_S1.md` (§6 foes, §7 hazards and boss, §8 chapter table), `docs/FEEL_PASS_S1.md`, `src/content/{chapter-1,stage-s0,rules,foes}.ts`, `src/view/{scene,hud,probes}.ts`, the variant-A layout on branch `ts-wave1` (`hud.ts` `CARDS`), parent `docs/OWNER_QUEUE.md` (01/11), `docs/games/QUALITY_RESCUE_2026-11-01.md` (§3 L4, L7, §4), `docs/games/MONSTER_MODEL_INVENTORY.md` (§5, §6.1), `docs/games/FREE_ASSET_SOURCES.md` (§0, §9, §11), `docs/games/TRIPO_TODO.md`, `docs/games/ART_DIRECTION_2026-10-28.md` §1 and §4, `docs/games/MAP1_PRODUCTION.md` §3, `docs/games/VFX_STANDARD.md`, the arena kit report `docs/codex-queue/125-report.md`, a play-host capture of `c1-s1` at 1280 × 720 (01/11); for v1.2, ChatGPT's review `docs/games/maps/typing-survival-CHATGPT_REVIEW.md`.
> **Projection script:** `games/typing-survival/tmp/map-concepts/project.mjs` (not tracked). It copies the camera of `src/view/scene.ts` and prints every projected table in §1 and §4.2 (`node project.mjs`); `--json --mvg` writes the base image's draw files; `place.mjs` beside it places the other maps' landmarks (§6); `capture.mjs` takes the frame on the play host and `build-base.sh` rebuilds the base image from it (the raw frames were pruned after use, so capture again first). Checked against the game's own projection: the foes reported by `__survival.foes()` land on the script's rows to 1–2 px.
> **Art bar:** the owner's reference `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (a hero seen from behind, something colossal, deep space falling away, warm low light) and the board of commercial references (ART_DIRECTION §1.3). Acceptance is **8.5** for everything the player sees (AGENTS.md; "chấm C" in QUALITY_RESCUE: two blind independent judges both ≥ 8.5, in game at 1280 × 720 and 1920 × 1080, High and Ultra, beside commercial references). Everything the player reads is English. No code-drawn stand-ins for art.

---

## 0. How to use this file with ChatGPT

1. **Review: done.** ChatGPT (Chat mode, High) reviewed map 1 as a senior art director on 01/11 at about 07:00: **8.0/10**, 8.7–9.0 expected after its fixes (`docs/games/maps/typing-survival-CHATGPT_REVIEW.md`; its input was the paste-ready message `typing-survival-CHATGPT_MESSAGE.md`). v1.2 folds every fix into §1.5–§1.7, §2.1, §4 and §5, and its notes on the other maps into §6.2 and §6.5.
2. **Next: the concept painting.** Paint with the prompt in §4.10 **over the base image** `games/typing-survival/art-src/_review/maps/map1-base-1280x720.png` (legend `map1-base-legend.md` in the same folder), in ChatGPT image (Chat mode, High effort) or in Adobe Firefly Image 5 with the base image as the composition reference. The base fixes the camera, the lane, the gate band, the Line, the heroine and drone, the landmark blocks and the grey HUD zones. The painting decides only light, materials, mood and scale.
3. Optional second attachment, for identity only: `games/typing-survival/art-src/ui/screens-epic/results-lose-bg.png` (the heroine and her drone with the cyan eye; their white-gold is painted as ivory ceramic here, §1.7).
4. Reject and ask again when the painting:
   - moves the lane, the gate sill, the Line, the heroine or a grey zone;
   - shows a horizon, a sky band, a skyline or a white glow at the top centre;
   - draws the heroine bigger than her block (68 px at 720p);
   - puts anything bright behind a grey zone, under the word line or right behind the lane;
   - has anything brighter than the Ring's lit face, or puts the Ring's whitest part behind the foe lane;
   - draws the Ring as a thin, smooth lit U instead of a thick, fractured, hazed arc (§4.3);
   - paints the Ring, the heroine or the drone gold instead of ivory;
   - paints bright cyan falls in the lower half, a cyan glyph run down the bridge or fine high-frequency orange filaments (§4.6, "Kept out");
   - lights the heroine's basin or the lower side areas (y 372–720) with rich orange;
   - draws the black hole as two clean circles or as a black sky;
   - paints foes that are not black glass with purple veins, or purple pools on the deck;
   - uses red anywhere except a foe attack;
   - shows any text, number, logo or UI.

   At most three tries per painting, then keep the best and write down what is missing.

---

## 1. Fixed rules for every map

### 1.1 The field (the sim does not change)

- One straight lane, **24 m wide, 40 m long** (`FIELD` in `src/content/rules.ts`). x runs across (−12 … +12), z runs away from the heroine, y is up.
- **Foes enter over the gate at z 40**, across the full width, in packs of 4–12 (block, wedge or line). Packs wait in a queue up to z 52. Five vanguard packs (6–8 foes) stand at z 18, 26, 34, 42 and 50 when a fight starts.
- **The defended point is the Line at z 2.4.** A foe that reaches it costs armour. From z 14 in (chapter stages) every foe bleeds armour; the near zone is z ≤ 7.
- **The heroine stands at z 0**, centre. Bay 1's gun is in her hands, bay 2's gun is on her drone (§1.7).
- Hazards and objectives that need room on the map:
  - **Rift**: a crack opens at the foot of the left or right wall (seeded), z 9–13, 2.5 s of warning, then 8 foes pour out.
  - **Gravity well**: centred at x ±4 (seeded), z 18, radius 8 m.
  - **Ion storm**: numbs one bay for 6 s after 2.5 s of warning.
  - **Nests**: crawling hives that appear at z 30–36 and crawl to z 10.
  - **Pack Leaders**: big foes with a gold beacon column.
  - **Boss**: stands at z 22, then 15, then 8.

### 1.2 The camera at 1280 × 720 (recomputed)

The fight camera stays as it is (`src/view/scene.ts`): pitch 36° below the horizon, vertical FOV 42° (horizontal 68.6°), **19.8 m up and 17.75 m behind the heroine**.

**Decision: no sky in battle.** Every view ray points down: 15.0° below horizontal at the top centre, 12.6° at the top corners, 36° at the centre, 57° at the bottom. The horizon never enters the frame, so **no battle painting shows a horizon, a sky band or a skyline**. Beyond the deck's far end the frame shows only what lies below the causeway: the abyss, the accretion disk, the black hole's shadow ahead and below, and structures rising from far below. The sky belongs to the title, the stage card and the 2.5 s intro sweep (§2).

The deck plane leaves the top edge at z 56.2. At the gate (z 40) the top edge is only **4.3 m** above the deck, and at z 30 only 7.0 m: anything taller there leaves the frame.

| Depth z | What | Screen y | Deck x (lane ±12) | Wall posts x (±12.73) |
|---:|---|---:|---|---|
| 56.2 | top edge | 0 | 482–798 | 473–807 |
| 52 | queue end | 16 | 475–805 | 465–815 |
| 40 | gate | 72 | 447–833 | 435–845 |
| 30 | | 135 | 416–864 | 403–877 |
| 22 | boss P1 | 203 | 383–897 | 367–913 |
| 18 | well | 245 | 363–917 | 346–934 |
| 13 | rift top | 307 | 332–948 | 313–967 |
| 9 | rift foot | 368 | 302–978 | 281–999 |
| 7 | near zone | 404 | 285–995 | 263–1017 |
| 4.4 | word line, near end | 455 | 259–1021 | 236–1044 |
| 2.4 | the Line | 500 | 237–1043 | 213–1067 |
| 0 | heroine's feet | 562 | 207–1073 | 181–1099 |
| −4.9 | bottom edge | 720 | 130–1150 | 98–1182 |

Heights on screen, standing on the lane's centre line:

| What | Screen y | Height |
|---|---|---:|
| the heroine, 2.6 m, at z 0 | 494–562 | 68 px |
| a 1.8 m person at z 0 | 515–562 | 46 px |
| a wall lamp post, 1.82 m, at the Line | 454–500 | 46 px |
| a 2 m foe at the gate | 40–72 | 32 px |
| a 2 m foe at the queue end | −13–16 | 29 px |
| the boss, 6 m, at z 22 | 76–203 | 127 px |

**The frame covers little ground beside the lane.** At deck level it reaches about ±15 m from the centre at the bottom edge and ±49 m at the top edge. Lower down the view widens, so a landmark must be far and low:

| Ground point (x, z) | Anything higher than this leaves the frame top | Screen x there |
|---|---:|---|
| −200, 300 | −65 m | 29 |
| −600, 900 | −226 m | 6 |
| 700, 1,250 | −320 m | 1,176 |
| −2,289, 5,424 | −1,438 m | 232 |
| 300, 100 | (outside the frame at any height) | 3,112 |
| 300, 400 | (outside the frame at any height) | 1,337 |

So a landmark is **seen from above**: its crown sits well below the causeway, or its arms leave the frame top. Revision 1's landmarks "300 m to the side, 400 m tall, filling the upper corner" are outside the frame.

**Tall things at the deck edge lean outward on screen, into the gun cards.** A 10 m mast at x 14, z 2 runs from (1115, 510) to (1244, 201), across gun card 2. A 6 m pylon at x 14, z 12 runs from (1008, 322) to (1048, 176). So nothing along the lane stands taller than the parapet's lamp posts (1.82 m) from z −5 to z 30.

### 1.3 HUD and gun cards (variant A, owner O7)

The gun cards moved up beside the lane, outside both walls (branch `ts-wave1`, `hud.ts` `CARDS`): bays 1–2 from 30 % of the height, bays 3–4 from 47 %, 2.5 % in from the screen's edge. A card is 230 × 100 px at 720p, a sealed bay's chip 132 × 34 px. The top HUD was measured on the play host.

| Zone | x | y |
|---|---|---|
| Armour (HULL) bar | 14–376 | 12–58 |
| Stage clock | 386–543 | 12–58 |
| Kill counter | 1028–1178 | 12–80 |
| Settings gear and Sound speaker | 1188–1268 | 12–48 |
| Word line (word and meaning), over the deck | about 500–780 (the width follows the word; at its widest the game protects 372–908) | 352–458 |
| Gun card 1 (bay 1, the heroine's gun), its tab above | 32–262 (tab 44–86) | 216–316 (tab 176–216) |
| Gun card 2 (bay 2, the drone's gun), its tab above | 1018–1248 (tab 1194–1236) | 216–316 (tab 176–216) |
| Bay 3 chip (a full card from stage 5) | 32–164 | 338–372 |
| Bay 4 chip | 1116–1248 | 338–372 |

**Free zones for a landmark's bright part:**
- the upper-left band, x 0–440, y 58–176;
- the upper-right band, x 840–1280, y 80–176.

**Other areas:**
- The strips between a card and the deck edge are narrow (40–100 px).
- The lower side areas below the chips (y 372–720) sit next to the player's eye: keep them dark and slow.

### 1.4 Screen map at 1280 × 720 (map 1)

```text
y   0 +[HULL 14-376][CLOCK 386-543]   muster ground z 40-56   [KILLS 1028-1178][gear 1188-1268]+
      |  Broken Ring arc  shadow lobe  \  x 448-832, y 0-70   / shadow lobe       shuttles      |
y  72 |  x 0-470,         x 192-470     \== gate sill z 40 ==/  x 810-1088        x 1109-1178   |
      |  y 0-172                         \ deck x 447-833    /                    y 110-136     |
y 176 | [tab1]                            \                 /                          [tab2]  |
y 216 | [GUN CARD 1 32-262, 216-316]       \ boss z 22 y 203/      [GUN CARD 2 1018-1248, 216-316]|
y 307 |                                     \ rift z 9-13   /                                    |
y 338 | [CHIP 3 32-164]   outriggers   [WORD LINE 500-780, 352-458]   outriggers   [CHIP 4]       |
y 404 |   disk far below                    near zone z 7                 disk, cross-span     |
y 500 |   ------------------- THE LINE  z 2.4, x 235-1045, y 495-504 -------------------          |
y 562 |                  HEROINE x 623-657, y 484-571 | DRONE x 668-704, y 486-518               |
y 720 +---------------------------------------------------------------------------------------+
```

### 1.5 Rules that follow

- **The landmark's brightest region lives in a free band (§1.3)**, never behind a card, never right behind the lane, never in the lower side areas.
- **The deck under and round the word line stays dark** (z 4.4–10, y 340–456): at most +0.02 luma over today (FEEL_PASS_S1 §4.1). Light pools from the guns are the only bright things there.
- Light from the abyss must not wash the horde out (the `f8` grade: ≤ 10 %).
- **One light budget per map:** one brightest region (the landmark's lit part, in a free band); the heroine's basin and the lower side areas stay the darkest large regions; the black hole's shadow reads as a void in the abyss below the camera, never as a black sky (map 1: §4.5).
- No mast, pylon or tower taller than 1.82 m along the lane from z −5 to z 30 (§1.2). Tall structures live far out and far below.
- The heroine stands from y 494 to 562 (68 px). The drone sits at her right shoulder (x 668–704, y 486–518). The deck round her stays dark and quiet except her own glyph ring.
- Budgets:
  - ≤ 60 draw calls for the whole frame on High (MAP1_PRODUCTION TS-M1-08);
  - models seen up close ≥ 2,000 triangles (`MODEL_QUALITY.md`);
  - the heroine ≥ 20,000 triangles at High (QUALITY_RESCUE §4.3).

### 1.6 Colours reserved for signals

| Colour | Means | Rule |
|---|---|---|
| Purple, violet | the Horde: foe veins, nests, the foes inside a rift, glints in the queue (owner O5) | no other purple near the lane; no purple pools on the deck; a rift's body stays near-black, only the foes in it carry violet |
| Red | a foe attack only (the boss's slam lane) | today's red Line goes cyan-white; the Mortar's ring goes pale orange with a white rim (VFX_STANDARD §3.6.3) |
| Gold | Pack Leaders: beacon column, lane mark, crest | other gold stays low near the lane; the Ring, the heroine and the drone are ivory, not gold |
| Ivory, pale stone | lit structure and the hero group's armour: the Ring's face, the stone bands, the heroine, the drone | the only near-white values; one brightest region per frame, in a free band |
| Cyan | the heroine, her drone, the Line, the Pulse Gun, friendly lamps | sparse: thin cores with a few px of bloom; no glyph run down the bridge; no bright cyan in the lower half except the Line and the hero group |
| Orange | the Heat Beam | the disk's orange-gold lives only in the abyss, never on the deck; strongest in the upper left, dark in the lower side areas, no fine filaments |
| Blue | Shield Guards' shields | — |
| White-blue / amber / vermilion | Rail Gun / Scatter Gun / Star Mortar | — |

Today's orange-and-black hazard stripes on both walls break this table (they are the loudest pixels and match the foes' cracks). They go.

### 1.7 The hero group (owner, 01/11)

- **The heroine** (working name Lightbearer) is a woman gunner in **ivory ceramic armour over graphite** (not metallic gold: gold is the Leaders', ChatGPT review), with very thin cyan seams, a dark helmet, a cyan visor slit and a mostly navy-black three-panel cape with dim ivory filigree.
  - Heroic scale 2.6 m: 68 px at 720p, 100 px at 1080p.
  - Seen from behind and about 46° above, so her cyan visor faces the foes and the player never sees it. The cape, the cyan seams down her back and the helmet's crest fins carry her read.
  - She **holds bay 1's gun** (the left card) and fires it.
- **Five hand-held guns** (QUALITY_RESCUE §4.4 prompts): Pulse Gun, Heat Beam, Scatter Gun, Rail Gun, Star Mortar.
- **The support drone** (0.9–1.0 m) floats at her **right shoulder**: a sharp white-ceramic teardrop with one narrow cyan aperture, not a glowing sphere.
  - It **fires bay 2's gun** (the right card) from its own emitter.
  - It also does her support work: her work light, the repair pod.
- **View only:** the sim, the trial's golden trace and the chapter hashes do not change.
- **Who builds them:** the owner makes **7 Tripo models** on the Tripo web (heroine, drone, 5 guns; `TRIPO_TODO.md` rows 7–13). The heroine's and the drone's source prompts (QUALITY_RESCUE §4.4) change to ivory ceramic before their source images are made.
- **Open (not decided):** from stage 5, bays 3 and 4 open, and nothing shoots them yet. All bays fire on the same tick, so one pair of hands cannot hold two guns. Choices for the owner: (a) a second drone at her left shoulder, (b) a shoulder-mounted launcher. This file does not paint bays 3–4.

### 1.8 The Horde (owner O5; reuse before new)

- **Look:** black glass and dark chitin with glowing **purple-violet veins**, which replace the orange cracks (QUALITY_RESCUE L7).
- **Each kind keeps its read:**
  - Swarm: small.
  - Scout: winged.
  - Brute: broad.
  - Shield Guard: a large faceted blue shield.
  - Splitter: round, with seams.
  - Pack Leader: 1.25 × a Brute, gold crest and beacon.
- **Models** (`MONSTER_MODEL_INVENTORY.md` §6.1):
  - The main horde is Space's `cosmic` family: 14 models in void purple, work S. Their gold trim is toned down by the shader, except on Leaders.
  - Machine foes: Space's unused `drone`, `lock-on` and `bomb`.
  - Boss candidates for the Warden: `tyrant-g05` or `warden-shadow`.
  - Until then, today's five `rainbow-*` copies, tinted.
- **No new Tripo foe for Chapter 1.**

---

## 2. One idea for all of Chapter 1: a causeway over the disk

Chapter 1 (in game "CHAPTER 1 · VC-7 CORRIDOR") is drawn as the **VC-7 causeway**: a 4 km bridge of graphite steel and pale ancient stone. It runs from the station's citadel (behind the camera) out over the accretion disk toward the black hole, which lies **ahead and below** the causeway's far end. The Horde crawls out of the black hole's shadow and walks the causeway toward the citadel.

- **In battle the player looks down past the deck edges into the abyss.** Far below, a sea of orange-gold plasma spirals. The black hole's shadow shows ahead and below, on both sides of the gate band. Station structures rise out of the depth: rings, monoliths, lower spans.
  - This is how a camera that looks down gets "epic" (ART_DIRECTION §1.2: the field stands high and its edge is a drop).
  - There is no sky in this frame (§1.2).
- **Each stage is a different span of VC-7**, one step farther from the citadel. This is presentation only; the sim field is the same. The disk grows, the ruins break more and the light warms from stage 1 to stage 10.
- **Stage intro sweep** (view only, during the stage card): 2.5 s from a low camera over her shoulder, aimed at the stage's landmark, then down into the fight view.
  - This is where the sky, the black hole's full disc and the landmark's crown are seen.
  - The title camera blend in `scene.ts` already does this move. Any key skips it; reduced motion cuts straight.

### 2.1 Shared kit for Chapter 1 (K-numbers below)

Only sources that are ours or verified free for commercial use (`FREE_ASSET_SOURCES.md` §0, §9):
- Quaternius kits use a custom licence (QAL) and wait for the owner to accept it.
- Kenney and KayKit are grey-box only.
- Sketchfab and Fab are not used.

| Id | Piece | Seen in the battle frame | Source |
|---|---|---|---|
| K1 | **Deck**: graphite plates in 2–3 large families (length, tone, wear) with crisp inset seams, a few huge full-width pale-stone cross bands, restrained wear toward the centre, sparse cyan inlays (never a run down the bridge), almost no glow; 24 × 60 m in frame; the 6 × 1.5 m plate must not read as a repeated tile | always, the frame's centre | Our own Blender mesh. Albedo: ticket 125's `art-src/arena-v2/deck-tile.png` (ours; not judged yet). Normal and roughness: ambientCG metal plates and painted metal (CC0). Anisotropy 8–16× so the far deck stays sharp |
| K2 | **Decals**: scorches, black glass shards with purple veins, stone cracks, her glyph ring | 12–20 a stage, none under the word line | Ticket 125's `deck-decals-alpha-v3.png` (ours), shard veins re-tinted to purple |
| K3 | **Parapet**: 1 m stone wall capped with steel, lamp posts 1.82 m (as today) with dim heads, a cyan running light that is dark at rest and pulses toward the heroine on a surge warning | both edges, the whole length | Our own Blender mesh with ambientCG materials (CC0). Ticket 125's `deck-edge-alpha-v3.png` is a look reference. The light is an emissive strip |
| K4 | **Span gate**: a raised sill across the deck at z 40 (0.6 m) and two squat bastions outside the parapets (2.5 m; they would leave the frame if taller). Authority from mass and width: broad foundations, giant blocks, recessed joints, deep contact shadows | always, the top band | Blender + ambientCG. A Tripo bastion only if this misses 8.5 at its 90 px size |
| K5 | **Bastion dais**: dark stone under the heroine, z −8 … 2.4; **the Line is its front lip** (a thin cyan-white light); her glyph ring inlaid | always, the bottom third | Part of K1. Glyph ring from `deck-decals-alpha-v3.png` |
| K6 | **Outriggers**: buttresses under the deck edge every 12 m (x ±13.2…±16.5, 0.4–6 m down), big dark silhouettes that lose contrast with distance (the perspective ruler of the causeway); two pour very narrow cyan coolant falls into the abyss that fade into haze before y 372. The camera cannot see the deck's underside or side faces from above the lane; the outriggers carry the read of a deep structure | always, both sides | Blender + ambientCG. Falls: a flow shader to VFX_STANDARD, Kenney Smoke Particles (CC0, already in `THIRD_PARTY.md`) for spray |
| K7 | **Midground structures**: rings, monoliths, lower spans 0.7–6 km out and 0.3–2 km below the deck | one landmark + 1–2 pieces a stage | Painted alpha cards from ChatGPT (our generated art), 2–3 layers for the intro sweep's parallax. Ticket 125's `far-ring-alpha-v3.png`, `wall-left/right-alpha-v3.png` are candidates |
| K8 | **The black hole's shadow**: ahead and below the far end, 24° in radius, its middle hidden by the deck: an irregular near-black occlusion inside the abyss with a razor-thin, distorted warm rim. It reads as a void below the camera, never as a black sky or two clean circles | always, two lobes beside the gate band | Shader (three.js, MIT) to VFX_STANDARD; ticket 125's `sky-disk.png` as the colour target |
| K9 | **Accretion disk**: a world-space ring mesh far below (plasma streams in kilometre-scale bands, not noisy flames or fine filaments; the Doppler-bright side on the left, inner glow). Strongest near the stage's landmark; dark in the lower side areas | always, every side area | Shader. No starfield in battle |
| K10 | **Atmosphere**: height fog in the abyss, dust motes in the disk light, broad rising particle columns and faint volume strata (not many thin god rays), heat shimmer at the gate; the lane stays clean | per stage | Kenney Particle Pack and Smoke Particles (CC0, in `THIRD_PARTY.md`); Unity Labs flipbooks (CC0); three.js examples (MIT) for the volume light; fog is a shader |
| K11 | **Muster ground**: the deck past the gate sill where the queue waits (z 40–56 is all the frame shows) | always, the top centre | The sim's queued packs. No impostor reservoir beyond z 56 in battle (it is out of frame); the reservoir belongs to the intro sweep |
| K12 | **The hero group** (§1.7) | always, the bottom centre | 7 Tripo models by the owner. Clips: Mesh2Motion (CC0, already on disk) first. Quaternius UAL is QAL and waits for the owner |
| K13 | **Life beside the fight**: evacuation shuttles fleeing toward the citadel; coolant falls; lamps pulsing on surge warnings | per stage | Shuttles: Space's own ship models (ours, `space-typing/art-src/3d/ships/`), recoloured dark with very small neutral or cool glints |
| K14 | **Light rig**: key = the disk, **from below and ahead** (warm up-light and back light); fill = navy from above; the heroine's cyan; image-based light from our own PMREM of the abyss shader so every model gets a rim; one shadow-casting light on the near deck (High and Ultra); bloom only a few px on the Line and the cyan (QUALITY_RESCUE L1) | — | three.js (MIT): DirectionalLight, PMREMGenerator; today's gun light pools stay |

Dropped from revision 1:
- **Edge pylons and the two bastion towers:** they lean into the gun cards (§1.2).
- **The impostor reservoir beyond z 56:** out of frame.
- **The starfield in the top corners:** there is no sky.
- **Void mantas and Horde climbers:** they had no source.

Quality tiers:
- Medium drops shadows, the fog layers and K13.
- Low keeps K1–K6, K8, K9 and one card layer.

---

## 3. Trial (`s0`, outside the chapter): "The Proving Span" (short)

- **Beat.** Before her first watch, the heroine proves herself on the citadel's outer span while the Horde tests the gate.
- **Gameplay.** Hold 180 s. No hazard. Five vanguard packs at z 18–50, two surges (55 s, 145 s), scouts from 12 s.
- **Set.** **Map 1's set at "cold watch" light**, so the frame needs no new assets:
  - the disk dim amber, navy fill;
  - the Broken Ring unlit, a dark arc in the upper-left band;
  - fewer decals, a clean deck.
- **Landmark.** The citadel's Lantern, recomputed:
  - A beacon tower beside the citadel is outside the frame at any height (a point 300 m to the side at z 100 is at screen x 3,112).
  - So in battle only its **beam** shows: a slow, dim cyan sweep across the abyss haze every 8 s, below the deck and in the upper side bands, never across the deck and never in the lower side areas (y 372–720 stay dark, §1.5; no bright cyan in the lower half, §1.6).
  - The tower itself is in the intro sweep.
- **Life.** The vanguard packs, the queue at the sill, the shuttles leaving as tiny dark shapes with small neutral glints (as map 1, §4.6).
- **Sources.** Map 1's. The beam is a light shader (VFX_STANDARD). The tower for the intro sweep is a painted card.

---

## 4. Map 1: Chapter 1 · VC-7 Corridor, stage 1 (`c1-s1`): "First Shift"

**v1.2.** This section is the current concept: it takes every fix of ChatGPT's art-director review (`typing-survival-CHATGPT_REVIEW.md`, 8.0/10, 8.7–9.0 expected after the fixes). The gameplay layout and the camera are unchanged (lane, Line, dais, gate, positions and HUD zones as in §1.2–§1.4). Where the review and revision 2 disagreed, the review wins; none of its changes moves gameplay, the camera or a HUD zone, so none was set aside.

### 4.1 Story and gameplay

- **Story beat.** The first real watch on Span One: the Horde comes over the gate in earnest, and the first Brutes push through the swarm.
- **Gameplay.**
  - Hold 150 s. No hazard. Armour drain ×2.
  - Calm rate 4.4 a second, surges at 50 s and 115 s, scouts from 12 s.
  - Brute packs (a Brute and 5 swarm behind it) from 80 s.
  - Two bays, default guns: Pulse Gun on bay 1 (in her hands), Heat Beam on bay 2 (the drone).

### 4.2 The battle frame and its base image

**Base image** (fix 1 of the critic): `games/typing-survival/art-src/_review/maps/map1-base-1280x720.png`, legend `map1-base-legend.md` beside it.

**How the base was made:**
- It is the real `c1-s1` frame on the play host (main `bb9d1d7`, seed 3, High, 1.4 s in, held clock, every DOM layer hidden).
- Today's ship was taken out.
- Flat translucent blocks mark each planned element at its projected place and height. Blocks below the deck are hidden by it, as the camera would hide them.
- Grey boxes mark the HUD and the variant-A gun cards.
- It has no text.

| Element | World (m) | Screen at 1280 × 720 (px) | Base colour |
|---|---|---|---|
| The heroine, 2.6 m, holding bay 1's gun | x 0, z 0 | x 623–657, y 484–571 | cyan |
| Support drone, 0.9 m, fires bay 2's gun | x +1.2, z 0, 2.0–2.6 m up | x 668–704, y 486–518 | white |
| The Line, front lip of the dais | z 2.4 | x 235–1045, y 495–504 | pale cyan-white |
| Vanguard packs (gameplay, kept from the capture) | z 18–34 | y 120–270 | — |
| Span gate: the sill | z 40, 0.6 m high | x 445–835, y 61–74 | lime |
| Span gate: two squat bastions, 2.5 m | x ±13.2…±17.5, z 38.5–41.5 | x 345–432 (mostly behind the clock) and 848–935, y 24–80 | lime |
| Muster ground: the queue past the gate | z 40–56 | x 448–832, y 0–70 | violet |
| Outriggers, every 12 m | x ±13.2…±16.5, 0.4–6 m below the deck, z 6–54 | both sides along the deck edge | blue |
| **The Broken Ring** (hero landmark) | centre x −2,289, z 5,424, 958 m below the deck; radius 1,210 m; nearly upright | lower arc x 0–472, y 0–172; brightest x 150–330, y 110–172 | pale gold |
| Black hole shadow | straight ahead, 14° below horizontal, radius 24° | lobes x 192–470 and 810–1088, y 0–≈240 | near-black |
| Accretion disk far below | km below the deck | every side area no other block covers | orange |
| Lower cross-span | from x 100, z 500 to x 1,500, z 900, 700 m below | x 1100–1280, y 515–600 | lavender |
| Evacuation shuttles (3) | x 650–760, z 1,100–1,400, 420–560 m below | x 1109–1178, y 110–136 | pink |

The base colours are labels, not paint: the Ring's pale-gold block is painted ivory stone, the heroine's cyan block ivory ceramic and graphite (§4.5); the violet queue block is the foes' black glass with purple veins only; the lavender cross-span is almost all atmospheric dark; the pink shuttles are tiny dark shapes with neutral or cool glints (§4.6).

### 4.3 Hero landmark: the Broken Ring of VC-7

- **What it is.** A colossal station ring, **2.4 km across**, standing nearly upright **6 km out on the left**, its centre about 1 km below the deck. It is broken at its top.
- **In the battle frame** only its lower arc shows: a U that drops from the top edge at x 7 to its lowest point near (230, 141), then rises back to the top edge at x 426.
  - Its broken top lies above the frame, behind the hull bar and the clock.
  - Its inner face is **the brightest region of the frame**, at about x 150–330, y 110–172: ivory stone and steel heated by the disk's orange up-light, not gold. This is the free band above gun card 1. Its whitest part never sits behind the foe lane.
- **It must read as 2.4 km, not a few hundred metres.** At its distance 100 m is about 16 px at 720p, so a smooth lit U reads small. The arc carries its own scale:
  - **Thickness:** a section about 200 m deep (≈ 32 px), so the inner face, the outer rim and the broken ends all show mass.
  - **Giant structure:** segment joints every 250–350 m (40–55 px) with giant ribs between them.
  - **Asymmetric damage:** heavily fractured, with missing chunks, exposed inner layers (decks, conduits, frame) and deep dark cavities; heavier on the left arm, so the lit bottom of the U stays readable.
  - **Hidden sections:** stretches of the arc lost in the shadow lobe or the haze, so the eye completes it.
  - **Atmospheric falloff** (x 0–350, y 0–170): the rear ribs dissolve into warm haze; only the nearest lit edge stays crisp.
- **Behind it** the black hole's left shadow lobe gives the lit arc a near-black backdrop, so the Ring stands as a silhouette against it. Below it the disk is at its strongest orange (§4.5).
- **Match.** It matches the accepted stage card `art-src/ui/stages-v2/c1-s1.png` (Broken Ring upper left). The intro sweep shows its whole broken circle against the sky.

### 4.4 Depth layers (all inside the battle frame)

- **Foreground:**
  - The bastion dais of dark stone with her glyph ring, dim.
  - The Line as its front lip: a thin cyan-white core with small segmented hardware in the lip.
  - The heroine and her drone; the parapet and its lamp posts.
- **Playfield:**
  - The deck K1 in large graphite plate families, with two or three huge pale-stone cross bands and restrained wear toward the centre.
  - About 12 decals beyond z 9, none under the word line.
  - The vanguard packs.
- **Gate band (y 0–80):**
  - The sill and the two squat bastions: broad foundations, giant blocks, deep contact shadows.
  - Past them, the muster ground with the queued packs.
- **Midground below the deck edge:**
  - The outriggers: big dark silhouettes every 12 m that lose contrast with distance, the ruler of the causeway's length.
  - Two very narrow cyan coolant falls (left z 18, right z 30) that fade into haze before y 372.
- **Far:**
  - The Broken Ring, its rear ribs in warm haze.
  - The lower cross-span (a service bridge) off the right edge, almost all in atmospheric dark.
  - The shuttle convoy in the upper-right band, tiny dark shapes.
- **Abyss:**
  - The accretion disk in kilometre-scale bands: strongest orange in the upper left under the Ring, much darker for y 372–720.
  - The black hole's shadow: an irregular near-black occlusion inside the abyss on both sides of the gate band, with a razor-thin distorted warm rim. It reads as a void below the camera, not as black sky and not as two clean circles.
  - Broad rising particle columns and faint volume strata round the Ring.
  - No sky, no horizon.

### 4.5 Light, value and colour: "First light"

- **Key:** the disk, from below and ahead-left, a warm orange up-light. It heats the Ring's inner face, rims the foes on their left and touches the parapet's outer rim. The lane itself gets almost none.
- **Fill:** cool navy from above; it rims the foes' other side.
- **The heroine:** a cyan rim and her thin seams.
- **Bloom:** a few pixels on the Line and the cyan only (QUALITY_RESCUE L1); nothing blooms over the deck.

**Light budget.** One bright region; everything else steps down.

| Rank | What | Where | Rule |
|---:|---|---|---|
| 1 | The Ring's lit inner face, ivory heated by orange | x 150–330, y 110–172 | the only near-white mass in the frame |
| 2 | The Line | y 495–504 | a thin cyan-white core, a few px of bloom |
| 3 | Gun light pools and shots | the near deck, while firing | short-lived; the only bright things round the word line |
| 4 | The heroine's seams, the drone's aperture | x 623–704, y 484–571 | thin lines and one narrow point |
| 5 | Foe veins (purple); Leader gold (none in stage 1) | the lane and the queue | small; no purple pools on the deck |
| 6 | The disk | the abyss | bright only in the upper left; dark below y 372 |
| 7 | Support lights: the two falls, the sparse inlays, the photon rim, shuttle glints, the service bridge's edges | §4.6 | low contrast; the parapet's running light and the outriggers' lamps are dark at rest and pulse only on a surge warning |

**Value plan by region:**
- **The heroine's focus basin** (x 500–780, y 352–720): the darkest large region, one to two values darker than the mid lane, with little reflected orange. The word-line limit (+0.02 luma, §1.5) still holds.
- **The lower side areas** (y 372–720): dark atmosphere over a dim disk.
- **The main lane** (x 448–832, y 75–495): mid-dark graphite, almost no glow.
- **The shadow lobes:** near-black, the Ring's backdrop.
- **The upper-left abyss and the Ring:** the light end of the frame, peaking on the Ring's face.

**Read order in play:**
1. The foes on the lane and in the queue: near-black silhouettes, a warm rim on their left and navy on their right, against the mid graphite lane.
2. The heroine and the Line: the only cool accents in the dark basin.
3. The Broken Ring: the brightest mass, held in the upper-left free band so it frames the fight and never sits behind the foe lane.
4. The gate's mass at the head of the lane.
5. Everything else, as support at low contrast.

**Colour script** (orange cut from 30 %, so the deck no longer floats as a silhouette over a glowing carpet):

| Share | Colour | Where |
|---:|---|---|
| ≈ 60 % | graphite and navy | the deck, the buttresses, the gate, the heroine's basin, the lower side areas |
| ≈ 15 % | near-black | the shadow occlusion, the dark lower abyss |
| ≈ 15 % | orange-gold plasma | the abyss, strongest in the upper left; never on the deck |
| ≈ 6 % | ivory and pale stone | the Ring's face, the stone cross bands, the heroine's armour, the drone |
| ≈ 3 % | cyan | the Line, her seams, the drone's aperture, the dais's glyph ring, the two falls |
| ≈ 1 % | purple | foe veins only |

**Colour reservations in this frame** (§1.6):
- **Gold:** Pack Leaders only (none in stage 1). The Ring, the heroine and the drone are ivory, pale stone and ceramic lit warm by the disk, never metallic gold.
- **Purple:** foe veins only; no purple pools on the deck and none in the world.
- **Red:** none in stage 1 (no boss); today's red Line goes.
- **Blue:** Shield Guards' shields only (none in stage 1).
- **Cyan:** the friendly side, kept sparse (§1.6).

### 4.6 Look by screen region (layout and camera unchanged)

| Area | Where (1280 × 720) | Look |
|---|---|---|
| The heroine's focus basin | x 500–780, y 352–720 | the darkest large region, 1–2 values darker than the mid lane; little reflected orange |
| The Line | y 495–504 | a thin cyan-white core with a few px of bloom and small segmented hardware in its lip; no red |
| The heroine | x 623–657, y 484–571 | same size; ivory ceramic and graphite, not metallic gold; very thin cyan seams; a mostly navy-black cape |
| The drone | x 668–704, y 486–518 | a sharper white-ceramic teardrop with one narrow cyan aperture, not a big glowing sphere |
| The main lane | x 448–832, y 75–495 | large graphite plate families, a few huge pale-stone cross bands (none from z 4 to z 10), wear toward the centre, almost no glow; sparse cyan inlays |
| Foes | y 120–270; the queue y 0–70 | near-black glass and chitin with small purple veins; a warm rim on one side, navy on the other; no purple pools |
| The gate | sill y 61–74; bastions x 345–432 and 848–935 | broad foundations, recessed joints, giant blocks, deep contact shadows; no taller |
| The Broken Ring | x 0–472, y 0–172 | thick, asymmetric, heavily fractured: giant ribs, exposed inner layers, missing chunks, deep cavities; brightest at x 150–330, y 110–172 as ivory heated by orange light |
| Ring depth | x 0–350, y 0–170 | the rear ribs dissolve into warm haze; the nearest lit edge stays crisp |
| Black-hole shadow | x 192–470 and 810–1088, y 0–240 | an irregular near-black occlusion inside the abyss, a razor-thin distorted warm rim; below the camera, not a sky; not two clean circles |
| Accretion disk | every abyss area | kilometre-scale bands, not noisy flames; strongest orange in the upper left under the Ring (x 0–440, y 58–176), dimmer behind gun card 1, much darker for y 372–720 |
| Buttresses (outriggers) | both deck edges | big dark silhouettes every 12 m, losing contrast with distance: a perspective ruler for the 4 km |
| Coolant falls | under the deck edges, left z 18, right z 30 | only two, very narrow, cyan, fading into haze before y 372 |
| Service bridge (lower cross-span) | x 1100–1280, y 515–600 | almost all in atmospheric dark, shown by its silhouette and tiny orange edges |
| Shuttles | x 1109–1178, y 110–136 | tiny dark shapes with very small neutral or cool glints |
| Atmosphere | the upper-left abyss, round the Ring | broad rising particle columns and faint volume strata, not many thin god rays; the lane stays clean |

**Kept out of the frame** (each one breaks the read):
- bright cyan falls in the lower half (they would read as beams or objectives);
- cyan glyphs repeated down the whole bridge (they weaken the Line);
- the Ring's whitest area behind the central foe lane;
- rich orange plasma in the lower corners;
- small high-frequency orange filaments;
- a white glow at the top centre (it suggests a horizon or a sun);
- gold on the Ring, the heroine or the drone;
- today's red Line, its red-brown glow and the orange-and-black wall stripes (§1.6).

### 4.7 Life (where the player looks)

- **Foes first.**
  - On the first frame the vanguard packs stand at z 18, 26 and 34 (y 120–270).
  - The muster ground past the sill (y 0–70) holds 2–3 queued packs at z 42–52, purple veins glinting, shuffling.
  - On a surge warning the queue thickens and presses against the sill. Brutes show there before they cross.
- **The defenders.**
  - The heroine stands in a combat stance, her cape stirring, her gun raised as each word loads it.
  - The drone bobs at her right shoulder. Its narrow aperture glints as it tracks a target; it throws no light pool on the near deck at rest. It fires on bay 2's loads.
- **Beside the fight.**
  - A convoy of 3 shuttles, tiny dark shapes with small neutral or cool glints, crosses the upper-right band every 30–40 s, fleeing toward the citadel.
  - The two narrow coolant falls pour.
  - The outriggers' lamps and the parapet's running light are dark at rest and pulse once on each surge warning.
- **Removed:**
  - The void manta (no source).
  - The banners on the bastion towers (the towers are gone).

### 4.8 Sources and build notes (licences checked)

| Element | Source | Licence | State |
|---|---|---|---|
| Heroine, drone, 5 guns | Tripo by the owner from our source pictures (`art-src/models-src/lightbearer-*`, QUALITY_RESCUE §4.4) | ours | to make (7 models); the heroine's and drone's prompts go ivory ceramic first |
| Foes | Space's `cosmic` family through `pnpm models:prepare --import`; today's `rainbow-*` meanwhile | ours | reuse, work S |
| Deck, parapet, gate sill and bastions, outriggers | Claude in Blender; ambientCG materials; ticket 125 deck tile | CC0 / ours | to make |
| The Broken Ring | ChatGPT painted alpha cards, 2 layers: the near lit arc, the rear ribs in haze (`far-ring-alpha-v3.png` is a candidate) | ours | to paint after this concept |
| Black hole shadow, disk, coolant falls | shaders to VFX_STANDARD | three.js MIT | to write |
| Lower cross-span | painted alpha card, mostly dark | ours | to paint |
| Shuttles | Space ship models, recoloured dark | ours | reuse |
| Dust, spray, smoke | Kenney Particle Pack and Smoke Particles; Unity Labs flipbooks | CC0 | Kenney in use; Unity Labs to record in `THIRD_PARTY.md` before use |
| Not used | Quaternius (QAL, waits for the owner), Kenney and KayKit models (grey-box only), Sketchfab and Fab (licence) | — | — |

**Build notes:**
- **Hero group (K12):** the heroine and the drone are ivory ceramic, not gold. Change their Tripo prompts in `QUALITY_RESCUE_2026-11-01.md` §4.4 before the source images are made (that doc is not changed here).
- **Bloom (K14):** the QUALITY_RESCUE L1 bloom change fits this concept: the Line and the cyan get only a few pixels of bloom.
- **Deck rhythm (K1):** 2–3 plate families (length, tone, wear) on one trim sheet, laid so the seam layout does not repeat inside the frame; a world-space macro mask (about 60 m) varies tone and wear; the pale-stone cross bands are their own mesh strips, two or three in frame, none from z 4 to z 10.
- **Gate (K4):** wider foundations broken into giant blocks with recessed joints; deep contact shadows from the near-deck shadow light or baked AO; the bastions stay 2.5 m.
- **Ring (K7):** two card layers for parallax: the near lit arc with its crisp edge, and the rear ribs already faded into haze. The brightest pixels stay inside x 150–330, y 110–172.
- **Black hole (K8) and disk (K9):** the shadow is an irregular, lensed occlusion inside the disk shader, not a drawn circle. The disk's brightness falls from the upper left to dark below y 372 (a world-angle mask in the shader); bands are kilometre-scale, with no fine filament noise.
- **Falls (K6):** the projection puts y 372 only 7 m (left, z 18) to 16 m (right, z 30) below the deck edge, so the flow shader fades each fall into fog within that drop.
- **Atmosphere (K10):** broad particle columns and a few soft volume strata in the upper-left abyss; no particles over the lane.
- **Signal lights (K3, K6):** the parapet's running light and the outriggers' lamps sit at zero emission at rest and pulse on the surge-warning event; the drone casts no light pool at rest.

### 4.9 What is wrong today

- The lane is a code-drawn steel corridor with orange-and-black hazard stripes on both walls and a red line over a red-brown glow: a loading dock, not a mythic causeway.
- The black hole is a poster disc behind the timer and a thin torus arch. Its white glow sits right behind the queue and washes it out.
- About 37 % of the screen (the side areas) is a flat poster with a swirl. Nothing lies below the deck, so the corridor floats on wallpaper.
- The hero is a 100 × 80 px faceless ship.
- The accepted stage card shows the Broken Ring, the heroine and a causeway. The fight then shows none of them.

### 4.10 Concept painting prompt

- **Attach:** the base image `games/typing-survival/art-src/_review/maps/map1-base-1280x720.png` (legend `map1-base-legend.md` beside it). Optional, for identity only: `results-lose-bg.png` (§0).
- **Tool:** ChatGPT image in Chat mode with High effort, or Adobe Firefly Image 5 with the base image as the composition reference.
- **Prompt:** ChatGPT's own words from the review, verbatim. It replaces revision 2's compact prompt, which still asked for white-gold armour and a pale-gold ring. Judge the result with the reject list in §0.

```text
Use the supplied base capture as an exact composition reference. Preserve the locked camera, framing, heroine size, straight 24 m lane, gate, deck walls, posts, enemy positions, HUD zones and all gameplay geometry exactly. Repaint only the art. Make the VC-7 causeway premium painterly-realistic sci-fi: dark graphite steel plates, pale ancient-stone bands, crisp seams, restrained wear, and sparse cyan friendly inlays. Keep the heroine at x623–657 y484–571, seen from behind, in ivory ceramic and graphite armour with thin cyan seams; drone at x668–704 y486–518, white ceramic with one cyan eye. Make the Line a thin controlled cyan edge at y495–504.

At left, create the colossal broken VC-7 station ring from x0–472 y0–172: thick, damaged, asymmetrical ivory stone-and-steel architecture, its lower inner face strongly warmed by orange plasma light from below, silhouetted against near-black black-hole shadow. Keep this bright focal area away from the lane. Fill all visible abyss with layered orange-gold accretion plasma far below, darkest near the deck and lower side areas. Add deep atmospheric depth, sparse dust shafts, tiny right-side evacuation shuttles, a dim lower service bridge, and heavy buttresses beneath both deck edges. Foes remain black glass and dark chitin with purple veins; only shields may be blue. No red, no text, no logos, no sky, no horizon. HUD and card zones remain plain dark grey.
```

---

## 5. What map 1 needs, ordered by "seen in the battle frame"

Only what the frame needs (fix 5). No Tripo request beyond the owner's 7 hero-group models.

| Rank | Item | Seen | Size at 720p | Source | Tripo |
|---:|---|---|---|---|---|
| 1 | The heroine | always, bottom centre | 68 px tall | Tripo by the owner (`TRIPO_TODO` row 7); ivory ceramic prompt (§4.8) | yes |
| 2 | Support drone | always, at her right shoulder | ≈ 36 × 32 px | Tripo (row 8); white ceramic, one narrow cyan aperture | yes |
| 3 | Pulse Gun in her hands (stage 1's bay 1), then Heat Beam, Scatter Gun, Rail Gun, Star Mortar | always | 15–25 px | Tripo (rows 9–13) | yes |
| 4 | Foes: vanguard packs and the queue | always | 25–60 px | Space `cosmic` family (reuse) | no |
| 5 | Deck, dais, parapet and lamp posts | always, the frame's centre | half the frame | Blender + ambientCG (CC0) + ticket 125 tile | no |
| 6 | Gate sill and bastions | always, top band | ≈ 90 × 56 px each bastion | Blender + ambientCG | only if it misses 8.5 |
| 7 | Outriggers and two narrow coolant falls (gone by y 372) | always, both sides | 60–150 px | Blender + ambientCG; flow shader | no |
| 8 | The Broken Ring | always, upper left | 470 × 172 px arc | ChatGPT painted cards, 2 layers (near lit arc, rear ribs in haze) | no |
| 9 | Black hole shadow and disk | always | side areas | shaders (irregular occlusion; disk dark below y 372) | no |
| 10 | Shuttles | every 30–40 s | 13–16 px | Space ship models, recoloured dark | no |
| 11 | Lower cross-span | always, lower-right corner | ≈ 180 × 85 px | painted card, mostly in atmospheric dark | no |

Dropped from revision 1:
- **The ring's base pylon** (Tripo): behind the deck from this camera.
- **The two right monoliths** (Tripo): outside the frame.
- **Bastion towers and edge pylons** (Tripo): they cross the gun cards.

---

## 6. The other maps (short; placements recomputed with `place.mjs`)

Each landmark below is placed for this camera:
- far out and well below the deck;
- its bright part in a free band (§1.3);
- anything the frame cannot show moves to the intro sweep.

Prompts for these maps are written after map 1's painting is agreed. ChatGPT's notes on them (review, 01/11) are folded in: stage 6's violet storm was the weakest idea and is replaced (§6.5); stage 3 keeps its rift's body dark (§6.2). Every stage follows map 1's colour reservations and light budget (§1.5, §1.6): gold only on Leaders or what a Leader triggers, violet only on the Horde, the lower side areas dark.

### 6.1 Stage 2 (`c1-s2`): "Leader Hunt"

- **Gameplay.** Hunt 3 of 5 Pack Leaders (20, 58, 96, 134, 172 s), cap 240 s. Each Leader walks behind 8 swarm. One surge at 70 s. Brutes from 30 s.
- **Landmark: the Herald Monolith.** A tilted 700 m monolith of dark stone in steel gantries, rising from the abyss on the right and leaning toward the lane.
  - Its crown is 1.6 km out at about x 700, z 1,300, 540 m below the deck. It shows at (1110, 140) in the upper-right band, where 100 m is 67 px.
  - Its horn-like antenna crown glows gold when a Leader arrives. Gold is the Leaders' colour; the world's other gold stays low.
- **Light.** "Beacon gold": the disk brighter on the right.
- **Life.** The queue at the sill parts when a Leader comes up, 2 s before it crosses z 40. When the hunt is won, the queue scatters back.
- **Sources.** Painted cards for the monolith; the antenna glow is a shader.

### 6.2 Stage 3 (`c1-s3`): "Rift Wall"

- **Gameplay.** Hold 165 s. A rift every 30 s from 25 s (wall foot, z 9–13, y 307–368).
- **Landmark: the Torn Span.** A tear in space about 400 m below the causeway, wide on the left, narrow on the right.
  - It fills the lower-left side area (x 0–260, y 380–720) and a thin strip at the lower right. It never crosses the deck.
  - **Its body stays almost black**, edged by a thin warm rim where the disk's light bends round it. Only the Horde coming out of it carries the violet: the vein glints of foes climbing inside the tear.
  - When a rift warns, the glints thicken on that side and the tear's edge stirs; the body stays dark. The world gives the warning a source without a violet wash.
  - The deck rifts at the wall foot follow the same rule: a near-black crack, violet only on the foes that pour out.
- **Light.** "Torn dark": the disk dims round the tear; violet stays on the foes, the Horde's colour.
- **Life.** Slabs of the causeway's underside float up beside the outriggers; dust drifts upward.
- **Sources.** A tear shader on a world-space mesh (five phases: edge stir, open, crawl, burst, embers; the body stays near-black) and a painted interior card, dark. The slabs use our K1/K3 meshes, broken.

### 6.3 Stage 4 (`c1-s4`): "Shining Shields"

- **Gameplay.** Hold 165 s. Shield Guard packs from 20 s; Missing-letters rule.
- **Landmark: the Aegis Array.** Three shield-emitter pylons rising from the abyss on the right.
  - Their crowns are 1.5–1.9 km out and 510–590 m below the deck, at (1000, 130) and (1150, 110) in the upper-right band.
  - They hold a cracked hexagonal curtain of blue light across the right side area, brightest in the upper-right band and only a dim shimmer below y 372 (§1.5). The Shield Guards' walls are pieces of it.
  - The Void Leviathan's shadow rises faintly inside the right shadow lobe on each surge.
- **Light.** "Aegis blue": cold blue from the right, the disk's warm orange from the left.
- **Sources.**
  - Emitters: painted cards.
  - Curtain: the Shield Guard wall shader at landmark scale.
  - Leviathan shadow: ticket 125's `void-leviathan-alpha-v3.png` (ours), dim.

### 6.4 Stage 5 (`c1-s5`, planned, checkpoint): "Buried Nests"

- **Gameplay.** Destroy 2 Nests, cap 300 s. Winning lights the checkpoint and opens bay 3 (see the open item in §1.7).
- **Landmark: the Hive Hulk.** A capsized freighter whose bow crashed onto the causeway's left edge past the gate. Its stern hangs into the abyss.
  - In frame: its pulsing belly glows at (250, 120) in the upper-left band, 900 m out and 290 m below the deck, where 100 m is 116 px.
  - Its bow on the causeway (z 44–56) is in the top band beside the muster ground, mostly behind the hull bar and the clock.
- **Light.** "Ember brood", in purple-violet instead of orange, since the brood is the Horde's. The violet stays on the hive's belly, its cracks and the brood; no violet wash over the deck or the abyss, no purple pools (as stage 3, §6.2).
- **Life.** Swarm drop from the hull's cracks onto the muster ground. The belly pulses with the nests' spawn timer. On victory the checkpoint light runs down both parapets.
- **Sources.** Painted cards in 3 layers; resin decals (a new ChatGPT decal sheet).

### 6.5 Stage 6 (`c1-s6`, planned): "Ion Storm"

- **Gameplay.** Hold 165 s. The ion storm numbs one bay at a time.
- **Landmark: the Storm Conductor.** A broken antenna spire rising from a near-black cyclone on the right.
  - Its forked crown is at (1150, 120), 1.5 km out and 470 m below the deck.
  - It is the hazard's source: sparse neutral-white electric fractures crawl up the spire as the storm charges, then a thin neutral-white bolt arcs across the abyss to the warned bay's shooter (bay 1: the heroine's gun, bay 2: the drone).
  - The bolt crosses the deck for 2–3 frames only.
  - The numbed bay shows as local static round its weapon (her gun or the drone's emitter) for its 6 s; nothing washes the screen.
- **Light.** "Black cyclone": a near-black gravitational particle cyclone turns slowly below the bridge in both side areas; the disk shows dimly through its gaps. No violet clouds: seen steeply from above they became a noisy purple overlay and clashed with the Horde's purple (the review's weakest idea).
- **Sources.**
  - Spire: painted cards.
  - Cyclone: instanced particles on a flow field (three.js, MIT) with Kenney or Unity Labs smoke sprites (CC0), darkened; JangaFX Cloud Pack VDBs (CC0) rendered dark to cards only if the body looks thin.
  - Fractures, bolt and static: to VFX_STANDARD.

### 6.6 Stage 7 (`c1-s7`, planned): "Splitter Swarm"

- **Gameplay.** Hunt 4 of 6 Leaders; rifts; splitters.
- **Landmark: the Shattered Twin.** A parallel causeway broken into a dozen drifting segments, falling away on the left.
  - The nearest segment is 260–420 m out and 140–260 m below the deck, in the lower-left side area under chip 3 (x 60–300, y 400–600). There 100 m is 250–380 px.
  - Farther segments step up into the upper-left band (x 60–300, y 90–170), 0.8–1.4 km out.
  - The Broken Ring from map 1 reappears far behind (same card).
- **Light.** "Shatter": strong side light from the disk's bright left; every segment edge rim-lit. The brightest rims are on the far segments in the upper-left band; the near segment in the lower-left side area stays a dark body with thin rims (§1.5).
- **Sources.** Our K1/K3 meshes as broken sections (no new art); the ring card reused.

### 6.7 Stage 8 (`c1-s8`, planned): "Black Well"

- **Gameplay.** Destroy 3 Nests. A gravity well at x ±4, z 18 (y 245).
- **Landmark: the Sink.** The station's collapsed core, a pale cracked sphere 200–300 m across, 1.1 km out and 690 m below the deck, under the well's side.
  - Its centre is near (150–220, 500) in the lower side area, about 190–280 px across. Its inner edge is hidden by the deck.
  - A slow spiral of debris rises from it to the upper band.
  - On the deck, plates lift a few centimetres round the well (view only).
- **Light.** "Sink": desaturated toward the well; the core glows a dim cold white from inside its cracks, not violet (violet is the Horde's, §1.6). It sits in a lower side area, so it stays dim; the stage's brightest region is the debris spiral's top in the upper-left band (§1.5).
- **Sources.** A sphere shader with a ChatGPT texture; debris from our K-meshes, instanced.

### 6.8 Stage 9 (`c1-s9`, planned): "Voice of the Station"

- **Gameplay.** Hold 180 s. Meaning rule. Rifts.
- **Landmark: the Archive Spire.** A slender spire of pale stone and ivory ceramic on the left (not gold: gold is the Leaders', §1.6), ringed by three slow-turning rings of abstract glyphs (shapes, never letters).
  - The rings are seen from above as ellipses at (210, 120) in the upper-left band, 1.4 km out and 450 m below the deck.
  - They brighten with each finished word, but never past the deck limit near the word line.
- **Light.** "Choir dawn": warm ivory from the rings, the disk's orange-gold from below (it stays in the abyss, §1.6).
- **Sources.** Painted cards. The rings are shader rings with a glyph texture in the style of ticket 125's glyph ring.

### 6.9 Stage 10 (`c1-s10`, planned, boss): "The Warden"

- **Gameplay.** The boss in three phases at z 22, 15 and 8. A slam lane in red (the only red).
- **Landmarks.**
  - **The Breach Gate** at z 60–80 is **out of the battle frame**: the deck leaves the top edge at z 56, and at the gate only 4.3 m shows. It appears only in the intro sweep. In battle, its chains hang into the abyss beside the gate band.
  - **The Void Leviathan** coils up out of the black hole on the right. Its head is at (1090, 130) in the upper-right band, 2 km out and 670 m below the deck, where 100 m is 53 px. It looks **up** at the Line and roars, a head lift with a purple flare, on each phase change.
- **The Warden.** Space's `tyrant-g05` or `warden-shadow` (inventory L4), animated by us.
- **Sources.** The Leviathan uses ticket 125's `void-leviathan-alpha-v3.png` and `art-src/ui/boss/boss-void-leviathan.png` as looks. In game it is painted cards with a flow shader on the veins.

---

## 7. Later chapters (planned in `SURVIVAL_MODE_PLAN.md` §4.0, not in code)

Each chapter is one map with one foe family and one boss. The same camera rules apply (§1.2–1.5): no sky in battle, landmarks far out and below, bright parts in the free bands.

| Chapter | Hazard | Setting |
|---|---|---|
| 2 · Ashfall Belt | meteor rain | a moon's split half far below on the left; meteor streaks fall through the side areas and strike marked circles on the deck |
| 3 · Nebula Locks | nebula fog | lock gates; a dry dock with a dead capital ship below on the right; fog rolls over the far half of the deck only |
| 4 · Sunward Array | glare pulses | mirror panels; a ring of giant mirrors below that catch a blue companion star (in the intro sweep) |
| 5 · The Cargo Maze | minefield, moving walls | a stacked container city below both sides, cranes rising from the depth |
| 6 · The Twin Spans | two lanes swap | a central pylon below that rotates to swap the spans |

Chapters 7–60 reuse these kits with new foe families, light scripts and one new landmark each.

---

## 8. Why the current maps fail (Last Line, 01/11/2026)

1. **The map is a code-drawn stand-in, not art.**
   - Every surface in `src/view/scene.ts` is made in code: the deck is a fragment shader, the parapets are grey boxes, the far arch is a squashed torus.
   - AGENTS.md forbids code-drawn scenery. Shaders are fine for light and VFX, not as the painting of the world.
2. **It is the wrong world.**
   - The owner chose direction B (the heroine on a causeway at the edge of a black hole) on 29/10. The menus, the stage cards and the logo show that world.
   - The fight still shows the old industrial corridor: orange-and-black stripes, a red line, a red-brown glow.
3. **The landmark is hidden, and the camera cannot see the sky.**
   - The black hole is a poster disc under the timer.
   - Revision 1 of this file placed landmarks where this camera cannot look. Revision 2 places them far out and below.
4. **More than a third of the screen is wallpaper.** The side areas look down past the deck edge, and today they show a camera-facing poster. There is no abyss, no structure, no fog, no parallax.
5. **No depth layers, no light direction.** Uniform warm wash, no shadows, no image-based light, no rim.
6. **The loudest colours are in the wrong place.** The wall stripes are orange like the foes' cracks.
7. **The hero is a small faceless ship.**
   - Owner, 01/11: the woman gunner with a support drone replaces it.
   - Seven Tripo models are to make.
8. **Every stage looks the same.** No stage has its own landmark, light or weather.
9. **No life outside the fight.**
10. **It looks soft.**
    - No texel detail on the deck.
    - Bloom spreads over the deck (QUALITY_RESCUE L1).
    - No MSAA on High and Ultra (L2).
11. **Good art exists but sits unused.** Ticket 125's arena kit, never judged or wired.

**What fixes it, in order:**
1. Agree map 1's concept and painting with ChatGPT over the base image.
2. Build the hero group (owner's Tripo models) and the K-kit:
   - the deck, parapet, gate and outriggers in Blender with CC0 materials;
   - the abyss, disk and black hole as shaders.
3. Paint the landmark cards per stage.
4. Score every stage in game with "chấm C" at 1280 and 1920 against the owner's reference and the agreed painting:
   - acceptance 8.5;
   - the word-line luma limit kept;
   - horde wash-out ≤ 10 %;
   - ≤ 60 draw calls on High.
