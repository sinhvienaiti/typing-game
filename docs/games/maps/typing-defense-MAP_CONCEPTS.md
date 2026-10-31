# Wordwoven: map concepts for every stage (v1, 01/11/2026)

Game: **Wordwoven** (repo id `typing-defense`, folder `games/typing-defense`). Written by the map designer after the owner's note of 01/11/2026: the maps of all three games are unacceptable; first write one concept per map, have ChatGPT review it and paint it, redo whatever falls short, and use only free resources that allow commercial use.

This file is written to be pasted into ChatGPT (normal chat, high reasoning). Paste **section 0 and section 1** together with **one map section** at a time.

---

## 0. For the reviewer (ChatGPT): what to do with this file

1. **Review the concept** of the map you are given, as a senior level designer and art director of a commercial top-down game:
   - Can a player read the lanes, the enemy entry, the build ground and the defended Fort at 1280 × 720 in the camera described in 1.3?
   - Does it feel epic and majestic next to the reference board in 1.2, or still cosy, toy-like and small?
   - Does it break a rule in 1.4 (culture, banned motifs, English only)?
   - Can it be built with the sources listed (our own art, free assets that allow commercial use, a few Tripo models, shaders)?
   - Say what you would change, and why. Be blunt. Propose better ideas when you have them.
2. **Paint the concept** with the prompt at the end of the map's section, improved by your review. One image, 16:9, seen from the game camera, no text in the image.
3. **Score your own painting** 0–10 against the bar in 1.2: 9 = the owner's reference; 8 = shippable (big landmark, at least three depth layers, directional cinematic light, colour script, finished detail, gameplay readable). Below 8: say what is missing and paint it again (at most three tries).

---

## 1. Shared context for every map

### 1.1 The game in five lines

- Wordwoven is a typing tower defence in a painted East Asian fantasy realm inspired by northern Vietnam (limestone karst towers, silver waterfalls, rice terraces, jade rivers, lanterns).
- **By day** the player builds and runs the village: places towers and farms, sends villagers to chop trees and work fields, answers the "calls" that appear as word cards above houses.
- **By night** creatures come out of a **Rift** (an ink-black tear in the world) and walk a fixed road to the **Fort**. Towers shoot on their own; typing the words on the cards powers them up.
- Heroes and helpers: **Draconis** (a white-and-gold feathered phoenix-dragon, 3.5 m body, 6 m wingspan, flies at 4–6 m and perches on roofs); three owlet **Helpers** (1.1–1.3 m, walk); villagers and workers (1.2–1.4 m); Barracks soldiers (1.7–2.0 m).
- Foes in World 1: Hopping Zombie and Zombie Leader (1.6–2.2 m, packs), Ghost Flame (wisps flying low at 3 m), Split Blob and Little Blob, River Serpent (heavy, armoured), Raccoon Dog (drums to heal its pack), Troll (stone dome), Alicanto (gold-thief bird), Sapling; later Oni, Bifang, Water Wraith, Dokkaebi, Sickle Weasel. Bosses: **Mộc Tinh** (an ancient banyan spirit, 7–10 m) and the **Storm Eagle** (12 m wingspan).

### 1.2 The bar

- **Commercial-game level**, judged against a board of commercial references, not against our own style guide:
  - the owner's reference (`games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`): a colossal flying beast over a canyon, a cloaked hero, cinematic light, huge scale contrast;
  - our accepted title painting `games/typing-defense/art-src/ui/title-epic/title-backdrop.v2.png`: sheer karst towers in mist, silver falls, a jade river with lanterns, terraces, a sky turtle carrying ruins.
- Keywords: **epic, majestic, cinematic light, deep atmosphere, one giant landmark, painterly-realistic, bold readable shapes**.
- Players' chibi-chunky models (Fort, towers, foes) stay as they are; **the world around them** must reach the bar.

### 1.3 Camera, frame and scale (the gameplay frame every map is designed for)

Today's default camera looks 55° down from 58 m. At 16:9 it shows only a band about 52 m deep, so on map 1 the Rift and the whole northern half are never on screen (see 3.8). Every concept below is designed for a new default **Battle view** that shows the whole fight:

| View | Pitch | Distance | What it is for |
|---|---|---|---|
| **Battle view** (default, day and night) | 50° | 76 m, looking at (0, 5) | the whole lane from Rift to Fort in one frame |
| Close view (zoom or PageDown) | 40–55° | 30–58 m | placing and reading houses |
| Vista (map opening fly-in 4 s, dawn and dusk transitions, results) | 18–25° | 60–90 m | sky, far karst rings, sky beast; never during a wave |

**The Battle view frame** (vertical FOV 38°, 1280 × 720; coordinates in metres, +x east, +z south, the Fort at the south):

| Ground row z | Screen y (720p) | Visible x | Pixels per metre (720p / 1080p) |
|---|---|---|---|
| −42 | 0 (top edge) | ±58 | 10 / 15 |
| −26 | 100 | ±53 | 10.9 / 16 |
| 0 | 309 | ±43 | 13.2 / 20 |
| +26 (Fort row) | 629 | ±34 | 16.7 / 25 |
| +32 | 720 (bottom edge) | ±31 | 18 / 27 |

- A 2 m Hopping Zombie is 22 px tall at the Rift and 33 px at the Fort (720p); 1.5× at 1080p. That matches today's close camera, so nothing gets smaller.
- At 50° the top of the frame is still 31° below the horizon: **no sky in the Battle view**. A landmark shows in play only if its foot stands in the top band (z −42 to −34) or at a side edge; its upper part rises out of frame. Its full height is seen in the Vista.
- **HUD keep-outs at 720p:** top-left panel x < 240, y < 150; bottom bars y > 650. No Rift, lane or build ground under them.
- **Frame template for every map:** wide things in the top band (Rifts, landmark foot, rich resources); the lane funnels down; the Fort stands at bottom centre (0, 26). Nothing taller than 3 m stands **south of** (in front of, lower on screen than) a lane or build ground; tall things live behind play (north) or outside the side edges.

### 1.4 Rules every map follows

- **English** for everything the player reads. Proper names stay: Draconis, Mộc Tinh, Chấm, Phẩy, Gạch.
- **Banned (art bible and design rule 22.1):** thatched huts, bamboo walls, wooden country shacks, windmills, tea hills, rainbows, red-and-white striped lighthouses, cartoon daisies and strawberry bushes, ink-outlined clip-art, round candy-floss trees.
- **No religious buildings or objects:** no pagodas, temples, shrines, torii, altars, incense, Buddha or deity statues. Our title painting shows pagoda-like towers; in maps they become **secular**: tiered stone watchtowers, gatehouses, scholars' halls, granaries. Dong Son bronze-drum sun-star rings, cranes, cloud scrolls and Ly-dynasty dragon balustrades are allowed.
- **Colour script:** jade and teal shadows (never black), warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. Grass jade-teal (hue 80–150°, median saturation ≤ 0.55). Roads at least 0.15 luma brighter than grass. No bright pink or purple (our keying colours); the Rift's ink is indigo-black with a cold rim.
- **Readability:** the brightest things on screen are word cards, typed letters and shots. Ground under a word card stays below luma 0.6. A grey-and-blurred screenshot must still show lanes, foes, heroes and health bars.
- **Light:** one sun for the world, from the south-west (lower left of the Battle view), 35–45° high, long sharp shadows, drifting cloud shadows. Night: a low silver-blue moon, amber lanterns as warm light, thicker mist.
- **No code-drawn stand-ins** for art. Shaders and VFX that meet the layered VFX standard are allowed (water, sky, fog, wind, the Rift).
- **Sources allowed:** our own accepted art; free assets whose licence allows commercial use and shipping the raw files in a web build (CC0 first; CC-BY with credit in `docs/games/THIRD_PARTY.md`; MIT, BSD, zlib or Apache code). **Not allowed:** non-commercial (NC), no-derivatives (ND), "editorial" or "personal use" licences, packs of unclear origin, and store licences that tie assets to one engine or forbid shipping the files openly. Pack names are left to the asset researcher; this file says what kind is needed.
- **Budgets per map** (High / Medium): ≤ 150 / 100 draw calls, ≤ 1.5 / 0.7 million triangles, media ≤ 16 / 9 MB. A landmark band (cliff, falls, statue) gets ≤ 12 draw calls. Models a player sees up close keep at least 2,000 triangles and their normal and roughness maps.

### 1.5 The campaign (every stage, built and planned)

| # | Map | Status | Waves | Boss | Section |
|---|---|---|---|---|---|
| W1-1 | **Silverfall Meadow** (`w1-silverfall`) | Built: 5 days and 5 nights; 2D Low tier complete; 3D in progress | 5 nights | Mộc Tinh, small, retreats at 50 % | 3 (full) |
| W1-2 | **Whitestone Bay** (`w1-whitestone`) | Planned (vertical slice) | 10 | Storm Eagle | 4 (full) |
| W1-3 | **Old Rootwood** (`w1-rootwood`) | Planned (vertical slice) | 12 | Mộc Tinh, full, with seal windows | 5 (full) |
| W1-S | **Goldstair Terraces** (side map; was "Tea Hills", renamed because tea hills are banned) | Planned (MVP) | 8, no boss | — | 6 (full, compact) |
| W1-N | **Starsea Rift** (bonus map, Neon style pack) | Planned (MVP) | 8 | Rift Warden (proposal) | 7 (full, compact) |
| W2–W5 | Amber Dunes, Frostsong North, Starsea Isles, Emberstone Highlands (working names) | Planned after MVP | — | — | 8 (one paragraph each) |

The sandbox (`?sandbox=1`) plays on map 1's field and follows map 1.

---

## 2. One method for every map

1. **Lock the gameplay layout in the Battle view frame first** (lanes, Rift, Fort, build ground, nodes, water, crossings), checked with a projection script at 1280 × 720 and 1920 × 1080.
2. **Concept painting from the game camera** (ChatGPT, this file). Accepted at 8 or more against 1.2, with the lanes, Rift and Fort readable in a half-size copy.
3. **Grey-box in engine** at that frame; overlay the painting at 50 % and match landmark positions and value masses.
4. **Life before polish:** foes, heroes, helpers, villagers and the choppable trees on screen before any more ground polish.
5. **Landmark band, water and light per time of day**, then ground materials, then dressing.
6. **Judge in-game screenshots**, not single assets: an independent judge scores Battle view day, night and boss shots at both sizes against the painting and the reference board.

---

## 3. W1-1 Silverfall Meadow (`w1-silverfall`): full concept

### 3.1 Name and story beat

**Silverfall Meadow.** Where the Silverfall pours off the cliffs, the Rift tears open in the falling water; the valley's first Fort must hold five nights until the nameless banyan, Mộc Tinh, rises and is driven back.

### 3.2 Gameplay layout (layout v2, made for the Battle view)

Same rules and topology as today's map, re-laid to fit the 16:9 frame:
- one Rift; a shared road that splits around a knoll and merges again; an S-curve to the Fort;
- a stream with two bridges that only walkers care about (foes never cross it);
- three ore nodes (★★★ front line under the flight line, ★★ across the stream, ★ by the Fort);
- two alluvial zones for Rice Fields;
- 36 choppable trees in five clusters.

Route lengths stay close to today's (north branch 118 m, south branch 107 m; today 116 / 113 m), so balance moves little.

| Element | Today (sim metres) | Layout v2 |
|---|---|---|
| Rift | (−10, −46), off-screen | (−28, −26), at the foot of the falls, screen ≈ (335, 100) at 720p |
| Shared road | (−10, −46) → (6, −34) | (−28, −26) → (−20, −28) → (−12, −25) → split (−6, −22) |
| North branch | (−12, −20) → (−10, 0) | (2, −26) → (12, −23) → (16, −14) → (14, −5) → merge (9, 1) |
| South branch | (16, −20) → (12, 2) | (−9, −13) → (−6, −4) → (1, 1) → merge (9, 1) |
| Knoll (Drum Knoll, was "Rainbow Hill") | (2, −21), r 8 m, 2.6 m high | (4, −14), r 7 m, 2.6 m high; houses on it +10 % range (rule kept) |
| S to the Fort | (0, 12) → (0, 40) | (9, 1) → (16, 8) → (10, 15) → (−3, 15) → (−7, 20) → (−3, 24) → Fort |
| Fort | (0, 40) | (0, 26), bottom centre, screen ≈ (640, 629) |
| Flight line (Ghost Flame, Alicanto) | Rift → (20, −20) → Fort | Rift → (28, −20) → Fort, 3 m high, over the ★★★ node |
| Stream (Silver Brook), 3 m wide | straight strip x ≈ −24 | winds from the plunge pool (−30, −36) south along x ≈ −31…−34 |
| Bridges (walkers only) | (−24, −14), (−24, 26) | (−32, −12), (−32, 14) |
| Ore nodes | ★★★ (26, −30), ★ (−12, 32), ★★ (−34, 8) | ★★★ (28, −18), ★ (−18, 22), ★★ (−40, −8) across the stream |
| Rice Field zones | (−32, 8), (16, 28) | west bank terraces (−40…−35, −2…10); east of the Fort (16…20, 20…24) |
| Choppable trees (36) | five clusters | beside the Rift, along the west bank, the north-east corner, south-east and south-west of the Fort |
| Build ground | 96 × 96 m square | the Battle view trapezoid (z −30…30) minus lanes, water, nodes and a 3 m road margin |

**Battle view frame:** pitch 50°, 76 m, looking at (0, 5). Everything above is in frame at 1280 × 720 with HUD keep-outs clear:
- Rift ≈ (335, 100), Fort ≈ (640, 629), knoll ≈ (687, 187), merge ≈ (760, 319);
- the ★★★ node ≈ (962, 157), the bridges ≈ (255, 203) and (164, 463).

A 2 m foe is 22 px tall at the Rift and 33 px at the Fort (720p).

**If the layout must not change** (no sim change), the whole route only fits at pitch 44°, 104 m, looking at (0, 12): 7 px per metre at the Rift, a 2 m foe 14 px tall at 720p. Too small; v2 is the recommendation.

**Sketch** (north up; one character ≈ 2 m across, one row ≈ 4 m; `|` = the Battle view frame's side edges):

```
        x: -48       -24         0         +24        +48
 z -36   CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC   C cliff wall (rises out of frame)
   -32          WWWWW   T T                                 W three falls into the plunge pool
   -28       T    ~R=======       =               T   T     R Rift at the foot of the falls
   -24      T    ~~       ==============            T
   -20           ~           ==        ==      3            3 rich ore (front line)
   -16   |   T   ~           =   ^^^^   ==               |  ^ Drum Knoll + dragon stair
   -12   |  T    #           =   ^^^^    =               |  # bridge (walkers)
    -8    |  2   ~           ==         ==              |   2 ore across the stream
    -4     |     ~            ==       ==              |
     0     | r   ~              ========               |    merge
    +4      | r  ~                    ===             |     r alluvial terraces (Rice Field)
    +8       r r ~                      ==           |
   +12       |   #                     ==            |
   +16         | ~            =========            |
   +20         |~~      1    ==          r r       |        1 small ore by the Fort
   +24         |~              ===        r    T   |
   +28          ~|    T         FFF          T   |          F Fort (bottom centre)
   +32         ~~|  T                            |          hamlet below the frame edge
```

Guardian statue: x ≈ 54, z ≈ −20, just outside the right edge.

**Decision for the owner:** v2 changes the map data in `src/content/slice-1a.ts`. The golden replays are re-made, the bot balance gates re-run on both seed sets, and scenario coordinates updated. The 2D Low tier follows the data by itself.

### 3.3 The hero landmark: the Silverfall

- **What it is:** a limestone cliff wall 140 m wide and 60–90 m high closes the north of the valley. Three silver waterfalls (one 18 m wide, two 6 m) crash into a misty jade plunge pool.
- **The Rift:** where it opens, one strand of the falling water turns to **ink**. An indigo-black tear 8 m wide and 14 m tall stands in the spray, its edges peeling like burnt paper. Foes step out of the mist.
- **In the Battle view:** the cliff's foot, the pool, the spray and the Rift fill the top band (screen y 0–110, left of centre). The cliff faces run out of the top of the frame, so the eye reads them as endless.
- **On the ledges:** two broken stone watchtowers and an old carved stairway cut into the rock give a human ruler.
- **Second giant: the Guardian.** A 22 m stone statue of an old general, both hands on a sword planted point-down, moss in the armour, stands just outside the right edge (x ≈ 54, z ≈ −20). Its plinth and lower body enter the frame's right side; its head shows only in the Vista.
- **Third, inside play but low:** the Drum Knoll at the split, with a carved Ly-dynasty dragon stairway climbing to a bronze-drum terrace (a 6 m sun-star relief). Later maps build a Seal Dais on a terrace like it.
- **Never hides play:** everything tall is north of the Rift or outside the side edges. The knoll is 2.6 m.

### 3.4 Depth layers, light, weather, colour

| Layer (Battle view) | What |
|---|---|
| Foreground frame | Bottom corners: cinnabar tile roofs and lantern strings of the hamlet below the Fort, with sea-almond canopies cropping the corners (under the HUD, dithered when something is behind them). Left and right edges: forest-edge canopies. |
| Playfield | Jade-teal meadow with darker moss patches; limestone flagstone road with a worn verge; the knoll; Silver Brook with banks, reeds and stones; west-bank rice terraces; ore outcrops; the choppable trees. |
| Midground | The cliff foot, the plunge pool, three falls, spray and mist; ledges with ruins; the Guardian at the right edge. |
| Far background | Not in the Battle view (a gold-silver haze where the cliff leaves the frame). In the Vista: karst towers on the 140, 220 and 320 m rings. |
| Sky | Not in the Battle view, except as reflections in the pool and brook, cloud shadows, and once a day the **shadow of the sky turtle** gliding across the whole field (about 20 s). In the Vista: the day and night sky rings. |

**Time and weather, one beat per day and night** (the sun stays south-west; height, colour and weather change):

| Beat | What opens and attacks | Light, weather, colour |
|---|---|---|
| Day 1 | Fort, Archer Tower, villagers chop | Morning after rain, sun 40°, wet stones shining, mist lifting off the brook; jade and gold |
| Night 1 | 10 Hopping Zombies; the Rift opens for the first time | Clear sky, low moon behind the cliff (silver rim on its top edge), lanterns lit on the Fort; teal and amber |
| Day 2 | Barracks | High thin cloud, breeze in the grass and the falls' spray |
| Night 2 | Zombies and the first Ghost Flames on the flight line | Thin ground mist in the brook valley; Ghost Flames are the only cold-cyan lights in the sky |
| Day 3 | Gold Mine, Cannon Tower, Fort level 2 | Bright summer gold, big cumulus shadows; the sky turtle's shadow crosses the field |
| Night 3 | Split Blobs; Fire Feather Rain opens | Lantern night: paper lanterns rise from the hamlet and drift north over the field |
| Day 4 | Upgrades | Warm haze, dust motes in light shafts |
| Night 4 | Raccoon Dogs (drums), a River Serpent, packs | Fog banks roll in from the pool; foes appear out of the fog |
| Day 5 | Fort level 3 | A storm front stands over the cliff, light breaks low under it, wind bends the trees |
| Night 5 | River Serpents, then **Mộc Tinh rises** 25 m down the road | Thunderstorm and rain. Lightning outlines the cliff. The falls turn ink-dark at the Rift, the sky and mist shift 20 % toward the boss's amber-moss colour, root cracks spread across the road. When it retreats the rain stops and the moon comes out. |

### 3.5 Set dressing (counts and scale)

| Item | Count and scale |
|---|---|
| Cliff wall | 1, 140 m long, 60–90 m high (lower 15–20 m in frame), fluted limestone with moss on ledges, 3 vines, 2 ruined watchtowers (8–10 m) on ledges, 1 carved stair |
| Waterfalls | 3 (18 m, 6 m, 6 m wide), 1 plunge pool 30 × 12 m, 1 spray cloud, 1 cascade where the brook leaves the pool |
| Rift | 1, 8 × 14 m |
| Road | 225 m of flagstone lane (3.8 m core, ±15 % width), worn verge 0.5 m, junction plazas at the split and merge; a dressing item every 2–6 m (about 60: kerb stones, grass tufts, broken slabs, puddles); at the split, merge and bridge heads 6 larger pieces (2 roadside lantern posts 2.5 m, 2 milestones, 1 low stone wall, 1 carved stone waymarker) |
| Drum Knoll | 1, r 7 m, 2.6 m high; 1 dragon stairway (8 m wide, 10 m long); 1 bronze-drum terrace 6 m across; 4 old mountain pines 10–14 m |
| Silver Brook | 3 m wide, 80 m long, banks 1 m; 40 reed clumps (1.5–3 m), 30 river stones, 2 wooden bridges, 1 small weir |
| West-bank terraces | 4 steps, 0.6 m each, flooded silver when empty |
| Ore outcrops | ★★★ a 6 m rock spur with gold seams; ★★ a 3 m boulder pair; ★ a 2 m boulder pile |
| Choppable trees | 36 in 5 clusters, sea-almond and mountain pine 8–14 m, each clearly a tree (not a bush); stumps regrow at dawn |
| Forest edge | about 120 canopy blocks (10–16 m) in 2–4 staggered rows along the top-band sides and the side edges |
| Understory | 200 ferns and shrubs 1–2.5 m; 300 patches of wild sunflower and lilies; grass blades 1,600 (Medium) to 4,000 (High) |
| Rocks and wood | 60 limestone boulders 0.6–3.4 m; 10 fallen logs; 12 stumps |
| Hamlet (below the frame edge) | 6 stone-and-tile houses 5–7 m, 2 granaries, 4 chimney smokes, 6 lantern strings |
| Guardian statue | 1, 22 m, on a square plinth at the right edge |

### 3.6 Life on the map

- **Foes visible from the start of a wave.** At dusk the Rift opens (1.5 s ink tear in the falls) and the first pack stands in the spray before the wave starts. Every following pack waits visibly inside the Rift's glow.
- **Flying foes.** Ghost Flames and Alicanto follow the flight line; a faint ink trail in the air marks it.
- **Defenders:**
  - Draconis perches on a roof when he powers a house, otherwise circles at 4–6 m with his shadow on the ground;
  - the three owlet Helpers walk to houses and work beside the crews;
  - Barracks soldiers block the lane;
  - villagers chop trees (axe swings, wood chips, a tree falls only when empty);
  - farmers wade in the paddies; builders work under bamboo scaffolds.
- **Ambient:**
  - 6 egrets in the paddies, which rise when foes pass;
  - 2 water buffalo on the west bank; fish jumping in the pool; dragonflies over the brook;
  - swifts circling the falls; fireflies along the brook at night;
  - the sky turtle's shadow once on Day 3.
- **Movement everywhere:** three falls, spray and mist; ripples and foam on the pool; flowing water in the brook; banners on the Fort; level pennants on towers; swinging lanterns; chimney smoke; wind in grass and trees; cloud shadows.

### 3.7 Where every piece comes from

| Piece | Source | Status |
|---|---|---|
| Fort and level kits | `games/typing-defense/art-src/3d/buildings/keep.glb`, `3d/kits/keep-kit-l2…l4.glb` | Keep, relight (StylePack Epic) |
| Cannon Tower, Gold Mine, cart, gold piles | `3d/buildings/cannon.glb`, `gold-mine.glb`, `3d/props/gold-mine-cart.glb`, `gold-pile-1…4.glb` | Keep, relight |
| Archer Tower, Barracks, Rice Field shelter | Thatched today (`3d/buildings/archer.glb`, `barracks.glb`, `farm.glb`) | **Tripo rebuild by the owner** in limestone and tile (ticket 129); off-bible until then |
| Wooden bridges, kerb stones | `3d/props/cau-go.glb`, `3d/props/da-ke.glb` | Keep, relight |
| Cliff wall | Terrain mesh (code) + a free CC0 cliff and rock material set, triplanar and tinted to the bible + free CC0 rock and ledge meshes; `3d/landmarks/vach-thac-bac.glb` as the near cliff piece | Painted cliff tiles (122) failed; use CC0 as the base |
| Waterfalls, pool, brook | Water shader with flow maps and free CC0 water normal maps; `art-src/vfx/waterfall-foam.png`, `water-splash.png`; mist particles (game kit) | Art exists; shader to build |
| Rift | Shader + `art-src/vfx/ink-smoke.png`, `ink-splat.png`, `paper-scraps.png`, five-phase VFX standard | Art exists |
| Ruined watchtowers on ledges | `3d/ruins/ruin-l.glb`, `ruin-xl.glb` (check style) or Tripo | Check |
| Guardian statue | Tripo from `art-src/landmarks-epic/guardian-statue.png` | **Owner makes in Tripo** (128 source done) |
| Dragon stairway | Tripo from `art-src/landmarks-epic/dragon-stair.png` | **Owner makes in Tripo** |
| Bronze-drum terrace | New Tripo source image (low round terrace with a sun-star relief) | New ticket |
| Roadside lantern posts, milestones | Free CC0 stylized stone props (secular street-lamp style) or Tripo | Asset research |
| Trees, forest edge | Accepted 116 billboards `art-src/scenery/meadow/{almond-tree,mountain-pine,bamboo-clump,canopy-block}-v3/v4.png`; atlas `td:scenery` (199); layout (202) | Accepted; **renderer not wired** |
| Understory, rocks, logs, stumps | 117 and 118 deliveries in `art-src/scenery/meadow/*-v3/v4.png`, `scenery/shared/tree-stump-v3/v4.png` | Delivered, not yet accepted |
| Ground (meadow, moss, road, verge, yard) | A free CC0 PBR ground set (mossy grass, wet earth, limestone gravel, flagstone) as the base, our painted decals (123) on top | 095 tiles score 3.5; 122 scored 7.5; 201 blocked by quota |
| Rice terraces | 123 rice tiles on stepped terrain | Delivered, not yet accepted |
| Grass blades, wind | Instanced grass shader (code, MIT patterns), wind sway on billboards | Code |
| Hamlet houses, granaries | Tripo (owner), 3 house types in limestone and tile; or a free CC0 East Asian village kit if style and licence fit | New |
| Foes, boss, heroes, helpers, soldiers, workers | `art-src/3d/enemies/*.glb`, `bosses/moc-tinh.glb`, `heroes/draconis.glb`, `helpers/helper-owlet.glb` and attachments, `units/linh-giao.glb`, `workers/worker-base.glb` and kits | **All exist; not drawn in 3D yet** (steps C7, C8); clips from free CC0 animation libraries already chosen in `docs/games/CHARACTER_ANIMATION.md` |
| Buffalo, bamboo dragonfly | `3d/animals/trau.glb`, `chuon-chuon-tre.glb` | Exist |
| Egrets, swifts, fish | Free CC0 rigged birds or flipbooks; fish as particles | Asset research |
| Sky rings, far karst, sky turtle (Vista only) | `art-src/backdrops/w1-silverfall-epic/*.v3.png` and `.v3.alpha.png` (179), `sky-beast.png`, `sky-beast-top.png` (114) | Delivered (179) / accepted (114) |
| Cloud shadows, height fog, rain, lightning, god rays | Shaders (code); free CC0 noise textures; god rays from an MIT or zlib post-processing library | Code |
| Floating lanterns, fireflies | Particles with painted sprites (new small 2D ticket) | New |

### 3.8 What is wrong with today's version

Evidence: today's diagnostic captures at High, 1920 × 1080, `games/typing-defense/tmp/diag-0111/raw/3d-high-01-day-home.jpg`, `3d-high-04-night-home.jpg`, `3d-high-03-day-overview.jpg`, and the 2D tier `2d-04-night-home.jpg`.

1. **No life.** The 3D view draws ground, houses and word cards only. At Night 1 the HUD says "10 foes left" and the screen shows an empty lawn: no foes, no Draconis, no helpers, no villagers, no soldiers. The 2D debug tier shows more of the game than the 3D one.
2. **The threat is off-screen.** The default camera sees z −4 to +48 (the southern half). The Rift, the split, the rich ore and the whole north are never in frame. Foes walk about 50 m (13–26 s) before they could appear.
3. **The choppable trees are missing.** The 36 trees that villagers chop (an economy object) are not drawn in 3D at all (no tree code in `src/view/3d/`). The yellow-green blobs on the lawn are flat ground decals (flowers and clover), about 18 px across.
4. **Ground like a football pitch.** One flat mint green (095 tiles, scored 3.5), off the bible's jade-teal. Toy beige flagstones with white kerb specks. The ore nodes and stone yards are flat beige blobs floating in the grass with no rock, no gold, no height.
5. **The brook is a concrete gutter.** A straight grey strip 3 m wide with flat edges: no banks, reeds, reflections, flow or falls. Two small bridges sit on it like stickers.
6. **Nothing has scale.** Nothing on screen is taller than the 8 m Fort; there are no verticals, so the sun has nothing to throw shadows from. No sky, horizon or landmark in frame (the cliff and lookout stand outside the field and outside the camera).
7. **Night equals day.** The night capture has the day's lighting; only the HUD text changed. No moon, lanterns, mist or Rift glow.
8. **Composition.** About 60 % of the frame is empty lawn, the brook cuts the left edge, the road is the only drawing, and there is no foreground, depth or focal point. An untextured white block sits in the middle of the field (an unidentified placeholder).
9. **Off-bible models.** The Archer Tower, Barracks, Rice Field and the Lookout are thatched (banned); the rebuild (129) was never approved.
10. **The field was built for a square 2D screen.** A 96 × 96 m field with an 86 m deep lane cannot be shown whole at 16:9 and a readable unit size. This is why layout v2 exists.

### 3.9 ChatGPT image prompt

```text
Concept painting of one battle map for Wordwoven, an epic fantasy tower-defence game, shown exactly as the game camera sees it: high three-quarter view looking 50 degrees down, the whole battlefield in frame, 16:9, no sky. Along the top edge the foot of a colossal pale limestone cliff rises out of frame, three silver waterfalls crashing into a misty jade pool. Beside the pool an indigo-black ink rift tears the spray and a pack of hopping zombies in faded robes steps out. A worn limestone flagstone road leaves the rift, splits around a grassy knoll crowned by a carved dragon stairway and a bronze-drum terrace, rejoins, then curves down to a white stone fort with cinnabar tiled roofs at bottom centre. A jade stream with two wooden bridges runs down the left past flooded rice terraces. Upper right: a gold-veined rock spur. Two stone towers, small villagers, owl helpers, a white-and-gold feathered dragon on the fort. Low golden sun from lower left, long shadows, lanterns lit. Painterly-realistic, bold readable shapes. No text.
```

---

## 4. W1-2 Whitestone Bay (`w1-whitestone`): full concept

### 4.1 Name and story beat

**Whitestone Bay.** The Storm Eagle has seized the Stone Otters' boats and gold. Two Rifts open on the beach while the tide turns, and the player defends the bay to win back the feather that carries half of the banyan's lost name.

### 4.2 Gameplay layout

- **Rules kept:**
  - sea to the north; two Rifts on the sand;
  - two causeways around the White Stone Terrace, merging before the Fort;
  - the Boat Cove to the west;
  - a flight line from the north-east over the rich headland.
- **The Tide** changes every two waves. Low tide: the West Rift sends more and the fish ponds pay ×1.5. High tide: the East Rift sends more and the ponds pay ×0.8. Helpers are moved between the shores.

| Element | Layout (sim metres) |
|---|---|
| Sea, surf and sand bars | z ≤ −30 (the top band); the waterline moves ±6 m with the tide |
| West Rift, East Rift | (−30, −26), (30, −26) |
| West causeway | (−30, −26) → (−36, −18) → (−30, −8) → (−20, −4) → (−12, 6) → merge (0, 12), about 77 m to the Fort |
| East causeway | (30, −26) → (36, −16) → (28, −8) → (20, −2) → (12, 6) → merge (0, 12), about 76 m |
| End | (0, 12) → (−6, 18) → (−2, 22) → Fort (0, 26) |
| White Stone Terrace | (0, −12), 14 × 10 m, 3 m high; Draconis perches there; not walkable by foes |
| Ancient Mosaic Court (word vein, Seal Dais) | (−6, 2) |
| Boat Cove and fish ponds (Rice Field skin) | x −42…−34, z −10…6, with tiled stilt houses at (−38, 10) |
| Ore | ★★★ on the east headland (40, −10) under the flight line; ★ (14, 22) |
| Casuarina and sea-almond grove (Lumber Camp) | (32…38, 16…26) |
| Flight line | north-east sea (46, −34) → headland (40, −10) → Fort |

**Battle view frame:** the same as 1.3. Rifts at screen ≈ (313, 101) and (967, 101); the Terrace at the centre; the Fort at bottom centre. The Boat Cove sits at the left edge (≈ (146, 290)), clear of the top-left HUD panel.

```
        x: -48       -24         0         +24        +48
 z -36   ~~~~P~~~~~~~~~P~~~~~~~~~~~~~AAAA~~~~~~~~~~P~~~~~~   ~ sea   P sea pillars   A Sea Gate in the surf
   -32   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   -28   .........R.............................R.......L.   . white sand   R Rifts   L lantern tower (headland)
   -24           ==                             ==
   -20         ==                                ==
   -16   |     ==             SSSSSSS             ==     |   S White Stone Terrace
   -12   |      ==            SSSSSSS           ===  3   |   3 rich ore on the headland
    -8    |  ~~~~ ===          S S S          ===       |
    -4     | ~f~~   ====                  ====        |      ~ f Boat Cove and fish ponds
     0     | ~~~~      ==               ===           |
    +4      |  ~~       ===  M        ===            |       M Ancient Mosaic Court
    +8       |  h        =====   =====             |         h stilt houses
   +12       |  h            =====                 |
   +16         |              ===                  |T        T casuarina and sea-almond grove
   +20         |   T          ===       1        T |
   +24         |     T          ==                 T
   +28           |              FFF             T|
```

### 4.3 The hero landmark: the Sea Gate

- **What it is:** a colossal three-arched limestone gate, 40 m wide and 36 m high, standing in the surf at the mouth of the bay. Tiled roofs with upturned corners, Dong Son sun-star rings on the pillars, waves breaking through the arches.
- **Why it matters:** the Storm Eagle enters through the middle arch in its boss wave.
- **In frame:** its feet and lower arches fill the top band right of centre; its roofs are seen only in the Vista. Three sheer sea pillars (karst) stand in the bay at the top-left and top-right.
- **The headland:** a stone lantern tower (14 m) replaces the old striped lighthouse.

### 4.4 Depth layers, light, weather, colour

| Layer | What |
|---|---|
| Foreground frame | Bottom corners: sea-almond canopies and drying fishing nets on poles; the Fort's outer wall |
| Playfield | White sand and wet sand at the top, two pale causeways of fitted limestone, salt grass and dune lily, the Terrace, the Boat Cove |
| Midground | Surf, the Sea Gate's arches, sea pillars, moored boats, the stilt village |
| Far background (Vista) | Karst islands across the bay, a low golden sun |
| Sky (Vista; reflections in play) | Pink-gold clouds at golden hour (warm, not bright pink); the Storm Eagle's shadow in the boss wave |

- **Time:** golden hour, sun low from the south-west, long shadows across the sand.
- **Tide:** the water line and the cove change visibly every two waves (a shader uniform, wet-sand darkening).
- **Late waves:** a rising wind, spray and sea mist.
- **Boss wave:** a storm over the sea, lightning behind the Sea Gate.
- **Colours:** turquoise and teal water, white limestone, gold light, cinnabar boat sails as accents.

### 4.5 Set dressing

- 1 Sea Gate (40 × 36 m); 3 sea pillars (40–70 m); 1 lantern tower (14 m).
- 1 White Stone Terrace (14 × 10 × 3 m) with carved steps.
- 1 pier (40 m); 8 moored boats (6–9 m) with cinnabar sails; 5 stilt houses (tile roofs, 5–6 m).
- 4 fish ponds; 12 drying-net frames; 6 upturned basket boats.
- 40 casuarina and sea-almond trees (8–14 m) in 3 clusters; 150 salt-grass and dune-lily clumps.
- 50 white limestone boulders (0.5–4 m); 2 causeways about 155 m in all, with kerb stones every 2–6 m; 4 roadside lantern posts.
- Gulls: 30 in flocks.

### 4.6 Life on the map

- **Foes:**
  - a pack waits on the sand inside each Rift's glow before its wave;
  - the busier Rift (by tide) glows stronger;
  - Bifang hop toward houses near the causeway; Trolls carry their dome;
  - Alicanto and Sickle Weasels follow the flight line over the headland.
- **Defenders:** Stone Otter fishers in the cove and Helpers moving between shores at the tide change.
- **Ambient:** gulls; crabs on the wet sand at low tide; boats rocking; sails and nets flapping; surf rolling through the Sea Gate.
- **Boss wave:** the Storm Eagle (12 m wingspan) circles at 9 m and casts a moving shadow; it swoops to lift houses.

### 4.7 Where every piece comes from

| Piece | Source | Status |
|---|---|---|
| Sea Gate | Tripo from `art-src/landmarks-epic/stone-gate.png`, scaled up | **Owner makes in Tripo** (128 source done) |
| Lantern tower | Tripo from `art-src/landmarks-epic/lantern-tower.png` | **Owner makes in Tripo**; replaces `3d/landmarks/hai-dang.glb` (off-bible) |
| Sea pillars | Tripo from `art-src/landmarks-epic/karst-pillar.png` (3 scaled variants) or free CC0 rock meshes | Owner or asset research |
| White Stone Terrace, pier | `3d/landmarks/them-da-trang.glb`, `cau-tau.glb` | Exist; relight, check scale |
| Stilt houses | `3d/landmarks/nha-rai-da.glb` is thatched (banned) | **Tripo rebuild** with tile roofs |
| Boats, nets, basket boats | Free CC0 boat and fishing-prop kits, retextured; or Tripo | Asset research |
| Sea, surf, tide, wet sand | Water shader with shoreline foam (free CC0 foam and normal textures), tide uniform; free CC0 sand and wet-sand PBR set | Code + CC0 |
| Coast scenery billboards | New 2D tickets (casuarina, sea-almond, salt grass, dune lily, white boulders): `art-src/scenery/coast/` is empty | New |
| Foes, boss | `3d/enemies/tat-phuong.glb`, `troll.glb`, `alicanto.glb`, `kamaitachi.glb`, `cuong-thi.glb`; `3d/bosses/dai-bang-tinh.glb` | Exist |
| Gulls | Free CC0 bird flipbook or rigged bird | Asset research |
| Far islands, golden sky (Vista) | New ring set like 179 for the coast | New ticket |

### 4.8 What is wrong with today's version

- **Not built.** No 3D, no 2D tier; only the design text exists.
- **Off-bible assets:** two of the existing assets for this map must not be used as they are: the red-and-white striped lighthouse `hai-dang.glb` and the thatched otter stilt house `nha-rai-da.glb`.
- **Layout not fit for 16:9:** the design's old layout (Rifts at z −42, Fort at z 38) has the same problem as map 1 and is replaced by the layout above.

### 4.9 ChatGPT image prompt

```text
Concept painting of one battle map for Wordwoven, an epic fantasy tower-defence game, shown exactly as the game camera sees it: high three-quarter view looking 50 degrees down, the whole battlefield in frame, 16:9, no sky. Along the top edge a turquoise bay with white surf, sheer limestone sea pillars and a colossal three-arched carved stone sea gate standing in the waves, its roofs rising out of frame. On a white sand beach two indigo-black ink rifts open, far left and far right, each releasing a small pack of creatures. Two pale fitted-stone causeways curve down around a raised white limestone terrace in the centre, meet below it and end at a white stone fort with cinnabar tiled roofs at bottom centre. Left: a sheltered cove with fish ponds, moored boats with red sails and tiled stilt houses. Right: a rocky headland with a stone lantern tower and a glinting gold vein. Casuarina and sea-almond trees, drying nets. Golden-hour sun from lower left, long shadows, sea mist, gulls. Painterly-realistic, bold readable shapes. No text.
```

---

## 5. W1-3 Old Rootwood (`w1-rootwood`): full concept

### 5.1 Name and story beat

**Old Rootwood.** Following the banyan's roots into the old rainforest, the heroes reach the hollow tree where Mộc Tinh sleeps; read its true name aloud and the spirit becomes a tree again.

### 5.2 Gameplay layout

**Rules kept:**
- two Rifts and **two separate trails** that meet only just before the Fort;
- the Root River divides the map. Crossings: Stepping Stones (only Lam, the cat courier, can jump them), a bridging point for Tre (the bamboo engineer), and the Red Bridge for everyone;
- walkers off the trails move 30 % slower;
- the **Canopy** rule: a house with three or more standing trees close by takes 40 % less ranged damage;
- in phase 2 Mộc Tinh's root walls block a trail.

| Element | Layout (sim metres) |
|---|---|
| Hollow Banyan | foot at (0, −40), roots spreading over z −36…−30 |
| West Rift, East Rift | (−42, −10), (44, −14), at the side edges |
| West trail | (−42, −10) → (−34, −20) → (−24, −12) → (−30, 0) → (−24, 8) → (−14, 16) → (−4, 20) → Fort, about 80 m |
| East trail | (44, −14) → (36, −22) → (26, −12) → (30, 2) → (22, 12) → Red Bridge (6, 16) → (0, 22) → Fort, about 82 m |
| Root River | springs under the banyan (0, −30), runs down the centre, plunges into the Sinkhole (0, 0, 10 m across), re-emerges below it and flows south-east past the Red Bridge |
| Crossings | Stepping Stones (0, −22), Tre's bridging point (2, −10), Red Bridge (6, 16) |
| Ore | ★★ (−20, −4), ★★ (22, −6) |
| Forest (Lumber Camp) | ★★★ (−36, 18), ★★★ (36, 8) |
| Word veins (one Seal Dais only) | (−14, −6) or (14, −6) |
| Hill terraces (Rice Field skin) | (24…28, 20…24) |

```
        x: -48       -24         0         +24        +48
 z -36                      BBBBBBBBBBB                      B Hollow Banyan (trunk rises out of frame)
   -32                        BBBBBBB                        roots arch over the top band
   -28                           ~
   -24                          ~                            ~ Root River
   -20         ===              ::               =====       : Stepping Stones
   -16   |    == ====            ~~            ===   === |
   -12   |  R==     ==            +           ==       R |   R Rifts (west, east)   + Tre's bridging point
    -8    |         =            ~            ==        |
    -4     |       =   2  V     OOO     V   2  =       |     O Sinkhole with falls   V word veins   2 ore
     0     |      ==                           ==      |
    +4      |      ==           OOO           ===     |
    +8       |      ===           ~~         ==   T  |
   +12       |        ====         ~      ====     T |       T Lumber forest
   +16         T         ====      ~#=====         |         # Red Bridge
   +20         |T            =======~~       r r   |         r hill terraces
   +24         |                ==   ~~       r    |
   +28           |              FFF   ~~         |
```

**Battle view frame:**
- Rifts ≈ (127, 220) and (1161, 187), at the side edges; the west one sits below the top-left HUD panel;
- the banyan's root mass across the top centre; the Sinkhole at the centre; the Fort at bottom centre.

### 5.3 The hero landmark: the Hollow Banyan

- **What it is:** a banyan of impossible size: the trunk is 40 m across and runs out of the top of the frame, and aerial roots arch over the top band like the vaults of a great hall.
- **The mouth:** a dark hollow at its foot glows faintly with amber sap-light; the Root River springs from beneath it.
- **The Sinkhole:** at the centre of the map, a waterfall drops into the darkness of a 10 m round pit with mist rising out of it. It is the second focal point and never hides a lane.
- **The fight:** in the boss wave Mộc Tinh tears itself out of the banyan's roots, and its root walls rise across one trail at a time.

### 5.4 Depth layers, light, weather, colour

| Layer | What |
|---|---|
| Foreground frame | Bottom corners: giant fern fronds and buttress roots (dithered); hanging vines at the top corners |
| Playfield | Moss-and-leaf-litter trails edged with roots and stones, the river, the Sinkhole, clearings for building |
| Midground | Banyan roots, the root arches over the trails, an abandoned stilt house (timber, collapsed tile roof) |
| Far background (Vista) | Rainforest canopy layers in mist, distant karst |
| Sky (Vista) | A green-gold canopy ceiling with holes of sky |

- **Time:** late morning (10:30), humid. Shafts of sun slant from the lower left through the haze; dapple-light cookies drift on the ground.
- **Boss wave:** it darkens toward dusk; fireflies come out, the banyan's sap glows, and the boss colour tints the mist 20 %.
- **Colours:** deep jade and emerald shadows, gold light shafts, silver river, cinnabar Red Bridge as the one strong accent, orchid accents (muted, never bright purple).

### 5.5 Set dressing

- 1 Hollow Banyan (trunk 40 m across, roots spanning 60 m); 4 root arches (8–12 m) over the trails.
- 1 Sinkhole (10 m) with falls; 1 Red Bridge (12 m); 1 line of stepping stones (6 stones).
- About 160 rainforest giants and canopy blocks (12–20 m) along the edges; 60 tree ferns (4–6 m); 300 ferns and shrubs; 120 orchid and moss patches; 80 mossy boulders.
- 1 abandoned stilt house; 2 root walls (boss, 12 m long each); fireflies 200–400 (High).

### 5.6 Life on the map

- **Foes:**
  - packs wait in both Rifts' glow before their wave;
  - Water Wraiths rise from the river, half invisible (a ripple and two eyes);
  - Oni smash houses; Dokkaebi summon small Ghost Flames.
- **Defenders:** Lam (cat courier) leaps the stepping stones; Tre (bamboo engineer) builds the bridge.
- **Ambient:** butterflies in the light shafts, birds crossing the canopy holes, mist breathing out of the Sinkhole, leaves falling, the river's flow and the falls.

### 5.7 Where every piece comes from

| Piece | Source | Status |
|---|---|---|
| Hollow Banyan | `3d/landmarks/goc-da-rong.glb` exists but is not hero-sized | **Owner makes a new 40 m Tripo banyan** with detail kept (model quality floors) |
| Root arches, Sinkhole falls, Red Bridge, Stepping Stones | `3d/landmarks/re-vom.glb`, `thac-ho-sut.glb`, `cau-do.glb`, `da-ke.glb` | Exist; relight, check scale |
| Rainforest billboards | New 2D tickets: `art-src/scenery/rainforest/` is empty | New |
| Abandoned stilt house | Tripo (timber, collapsed tile roof; no thatch) | New |
| Ground and trails | Free CC0 forest-floor PBR set (moss, leaf litter, roots, mud) + our decals | Asset research |
| River, falls, Sinkhole mist | Water shader, `art-src/vfx/waterfall-foam.png`, mist particles | Code + art |
| Light shafts, dapple light | Post god rays (MIT or zlib library) + a free CC0 leaf-shadow texture as a light cookie | Code + CC0 |
| Foes and boss | `3d/enemies/oni.glb`, `dokkaebi.glb`, `ma-da.glb`, `kamaitachi.glb`, `tanuki.glb`; `3d/bosses/moc-tinh.glb`; `3d/projectiles/root-burst.glb` | Exist |
| Fireflies, butterflies | Particles with painted sprites | New small ticket |

### 5.8 What is wrong with today's version

- **Not built.** Only the design text and some landmark models exist.
- **The hero is missing:** `goc-da-rong.glb` is a small prop, not a hero landmark, and its detail must be checked before it is scaled up.
- **Layout not fit for 16:9:** the design's old layout (Rifts at x ±46 and the Fort at z 40) has the same depth problem as map 1 and is replaced above.

### 5.9 ChatGPT image prompt

```text
Concept painting of one battle map for Wordwoven, an epic fantasy tower-defence game, shown exactly as the game camera sees it: high three-quarter view looking 50 degrees down, the whole battlefield in frame, 16:9, no sky. Top centre: the foot of a colossal hollow banyan whose trunk rises out of frame, giant aerial roots arching over the ground like the vaults of a great hall, amber light glowing inside its hollow. A jade river springs from under the roots, runs down the middle past mossy stepping stones and plunges into a round sinkhole, a waterfall falling into misty darkness. Two separate mossy forest trails start from indigo-black ink rifts at the far left and far right edges, wind down each side between buttress roots and meet just before a white stone fort with cinnabar tiled roofs at bottom centre; the right trail crosses the river on a red lacquered bridge. Dense rainforest edges, tree ferns, orchids, an abandoned stilt house. Morning sun shafts slanting from lower left through humid haze, fireflies. Painterly-realistic, bold readable shapes. No text.
```

---

## 6. W1-S Goldstair Terraces (side map): compact full concept

**Name and story beat.** Goldstair Terraces: the harvest festival in the terraces above the valley. Golden Hours and runaway Golden Piggies test the economy; no boss.

**Gameplay layout.**
- One Rift on the highest terrace at the top centre (0, −28).
- A single flagstone stair-road zigzags down four terrace levels: (0, −28) → (−30, −22) → (−30, −12) → (28, −8) → (28, 4) → (−24, 8) → (−24, 18) → (0, 22) → Fort (0, 26), about 230 m in all.
- Each level is a buildable ledge 8–10 m deep; drops between levels are 2–3 m with stone retaining walls. Houses on a higher ledge get +10 % range (a terrain rule like the knoll).
- Rice Field terraces fill the inner bends.
- Golden Piggies run along the dykes between the paddies, from one side edge to the other.
- Battle view as in 1.3: the zigzag fills the frame from left to right four times; the Fort at bottom centre.

```
 z -32   AAAAAAAAAAAAAAAAA(R)AAAAAAAAAAAAAAAAAAAAAA   A aqueduct arches + water wheels, R Rift
   -24   ==================                             level 4
   -16   =  rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr        r rice terraces in the bends
    -8   ===========================================    level 3
     0                                             =
     4   ===========================================    level 2
    12   =  rrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    18   ===========================                    level 1
    26                         FFF                      Fort
```

**Hero landmark.**
- A colossal ancient limestone aqueduct (arches 30 m high) runs across the top band and pours silver water into the highest terrace.
- Four great bronze water wheels (12 m) turn beside it; the water spills from terrace to terrace in thin silver falls.
- The aqueduct's upper tiers rise out of frame.

**Depth layers, light, colour.**
- Foreground: dyke grasses and conical-hat farmers at the bottom corners.
- Playfield: the ledges and stair-road.
- Midground: the aqueduct, wheels and falls.
- Vista: karst peaks and cloud sea.
- Time: dawn, sun low from the south-west skimming the flooded paddies (a mirror of gold), mist pooled in the lower terraces.
- Colours: green, gold and silver steps, cinnabar festival banners.

**Set dressing.**
- 1 aqueduct (120 m long); 4 water wheels; 8 terrace falls.
- 24 paddy plots on 4 levels; 600 m of retaining walls; 2 granaries; 30 festival banners and 40 lantern strings.
- 20 bamboo and sea-almond clumps at the side edges. No scarecrows (off-bible rustic).

**Life.**
- Farmers planting and harvesting; 3 water buffalo; 12 white cranes rising when foes pass.
- Golden Piggies with a gold trail; flowing water everywhere.

**Sources.**
- Aqueduct and water wheels: **Tripo** (new source images), or free CC0 stone-arch kits plus Tripo wheels.
- Rice terraces: 123 rice tiles (pending) on stepped terrain.
- Retaining walls: free CC0 stone-wall material.
- Buffalo `3d/animals/trau.glb`; Golden Piggy `3d/animals/piggy.glb` (flagged cute, rebuild as a gilded bronze piggy spirit); farmers from `3d/workers/worker-base.glb` and kits.
- Cranes: free CC0 rigged bird.
- Water: shader.

**Wrong today.** Not built. The design called it "Tea Hills" with tea rows and a windmill, both banned by the bible; this concept replaces it.

**ChatGPT image prompt.**
```text
Concept painting of one battle map for Wordwoven, an epic fantasy tower-defence game, shown exactly as the game camera sees it: high three-quarter view looking 50 degrees down, the whole battlefield in frame, 16:9, no sky. Along the top edge a colossal ancient limestone aqueduct of tall arches rises out of frame, four great bronze water wheels turning beside it, silver water pouring into the highest rice terrace. Below, a vast staircase of flooded rice terraces in green, gold and mirror-silver steps down toward the camera, thin waterfalls spilling between levels. An indigo-black ink rift opens on the top terrace beside the aqueduct; one flagstone stair-road zigzags left and right down four terrace levels to a white stone fort with cinnabar roofs at bottom centre. Farmers in conical hats, water buffalo, white cranes, a small golden piggy running along a dyke, festival banners. Dawn sun from lower left skimming the water, long shadows, mist pooled in the lower terraces. Painterly-realistic, bold readable shapes. No text.
```

---

## 7. W1-N Starsea Rift (bonus map, Neon style pack): compact full concept

**Name and story beat.** Starsea Rift: the mountaintop where Draconis fell through a tear in the sky; the stolen constellation's name is still burning in the crater.

**Gameplay layout.**
- Floating rock islands above a sea of clouds, linked by **light bridges** that switch on and off by wave: a preview of World 4's rule, which changes the lane.
- Two Rifts: the sky tear at the top centre (0, −30) drops foes onto the top island; a second, smaller tear opens at the right edge (44, −10) from wave 4.
- Two lanes:
  - left: top island → west island → light bridge A → Fort island;
  - right: top island → crater rim → light bridge B → Fort island.
- When a bridge is off, its lane detours across the middle island (+20 m). The HUD shows the next switch.
- Fort island at the bottom centre (0, 26).
- Battle view as in 1.3.

```
 z -36            ***** SKY TEAR (R) *****                 * star-fall from the tear
   -28          ======= top island =======
   -20       ===                          ===
   -12   west island ==        (crater)     ==   R2        R2 second tear, from wave 4
    -4        ==            middle island     ==
     4    bridge A ::::                   :::: bridge B     : light bridges (on and off)
    14          ===                       ===
    22              ===== Fort island =====
    26                       FFF
```

**Hero landmark.**
- A gigantic tear in the night sky pours stars and cyan light like a waterfall onto the top island; its upper part is out of frame and its glow lights the whole map from the top.
- At the upper centre: Draconis' crash crater (20 m), with a broken ring of constellation stars hovering above it.

**Depth layers, light, colour.**
- Foreground: crystal shards and drifting cloud wisps at the bottom corners.
- Playfield: dark basalt islands with glowing crystal veins.
- Midground: the crater and the star-fall.
- Vista: a cloud sea and distant floating peaks under the star-sea.
- Light: night, the tear as key light (cold cyan from the top), crystal veins as fill, the Fort's lanterns as the only warm amber.
- Colours: deep indigo shadows, cyan and gold glow; **no bright magenta** (keying colour).
- StylePack Neon: ACES tone map, bloom 0.6.

**Set dressing.**
- 5 floating islands (20–40 m); 2 light bridges (30 m).
- 1 crash crater; 1 constellation ring; 80 crystal clusters (1–6 m); 40 basalt spires (5–15 m).
- Cloud sea (shader); falling stars 300–600 particles.

**Life.**
- Star-touched foes glow at their seams.
- Draconis is at home here: his feathers flare.
- Drifting star motes; the cloud sea flows under the islands; the bridges hum when they switch.

**Sources.**
- Islands, spires and crystals: free CC0 rock and crystal meshes with the Neon material, or Tripo.
- Crater: Tripo.
- The sky tear, star-fall, bridges and cloud sea: shaders and particles per the VFX standard.
- The Neon scenery atlas is separate (design rule 23.12), new 2D tickets.
- Models are shared with World 1 and relit by StylePack Neon.

**Wrong today.** Not built; the Neon style pack does not exist yet.

**ChatGPT image prompt.**
```text
Concept painting of one battle map for Wordwoven, an epic fantasy tower-defence game, shown exactly as the game camera sees it: high three-quarter view looking 50 degrees down, the whole battlefield in frame, 16:9. Along the top edge a gigantic tear in the night sky pours stars and cyan light like a waterfall onto a floating island of dark basalt; above the clouds, more floating islands with glowing crystal veins are linked by two bridges of solid light, one flickering off. At the upper centre a smoking crater where a feathered dragon fell, a broken ring of constellation stars hovering above it. Two luminous stone paths cross the islands and meet at a white stone fort with cinnabar roofs and warm amber lanterns on the bottom island, the only warm light in the scene. A sea of clouds flows beneath, lit cyan from above. Deep indigo shadows, cyan and gold glow, no bright magenta. Painterly-realistic, bold readable shapes. No text.
```

---

## 8. Later worlds (one paragraph each; working names)

**W2 Amber Dunes** (caravan-league desert, 3–5 maps). Red sandstone canyons and amber dunes under a white sun, with a green oasis city of domed caravanserais and great bronze sundials. The hero landmark of the first map is a colossal half-buried sphinx-like guardian of sandstone whose riddles become the boss's seal windows. Terrain rules: sandstorms shorten tower range by wave; dunes that shift and reroute a lane between nights; a fertile oasis that boosts farms. Lanes cross a dry riverbed and canyon bridges framed by the Battle view template; desert-fox couriers and hourglass-makers bring the life. Warm StylePack: gold and rust light, deep blue shadows, turquoise water.

**W3 Frostsong North** (northern villages, ice lakes, snow pine forests, walrus harbours; no religious symbols). The first map is a frozen lake harbour under green aurora, with a colossal frozen waterfall wall as its hero landmark and ice-locked longships along the shore. Terrain rules: ice that makes foes slide past towers; snow that slows walkers; heater houses as a new support building. Wood becomes ice crystal as a resource. Cold StylePack: silver-blue shadows, ember-orange windows, aurora green kept off the word cards.

**W4 Starsea Isles** (the Starsea of Space Typing, Neon StylePack). Floating islands under the star-sea joined by light bridges that switch by wave, with low gravity so more foes fly. The hero landmarks are the shattered star-keepers' observatory rings orbiting over the field, never over a lane. Here the masked "Eraser" behind the Rifts is revealed. It reuses the Starsea Rift kit from 7 at full scale.

**W5 Emberstone Highlands** (volcanic terraces, lava caves, llama-herding stone-cutters; no temples). Terraced fields on a smoking volcano's flank, lava channels that open and close lanes by wave, and hot springs that boost production. The hero landmark is a colossal basalt dam holding back a lava lake, glowing through its cracks across the top band. Wood becomes pumice. Fiery StylePack: obsidian shadows, molten orange light, jade terrace crops as the cool accent.

---

## 9. Why the current maps fail

Only map 1 exists. These are the reasons it fails, and they would repeat on every later map if the method stays.

1. **We built from rule rectangles, not from a picture.** The 3D ground was generated outward from the sim's debug shapes: road polylines became masks, the water rectangle became a strip, nodes became beige disks. Nobody ever painted the map as a shot from the game camera, so there was no target and nothing to compare against. Assets were accepted one by one (a tree on a magenta sheet, a ground tile), never in the frame the player sees.

2. **The field and the camera were never designed together.** The field is a 96 m square made for the old square 2D view. The design's camera (55° from 58 m) sees a band only 52 m deep, so the Rift, the split and the rich ore are always off-screen and foes walk 13–26 s before they could appear. "I can't see the monsters" comes first from geometry, before any art.

3. **The epic was put where the camera cannot look.** The plan placed the landmarks outside the field and the epic sky and karst on rings 140–320 m away. The play camera's top ray is 36° below the horizon, so none of it is ever seen in play. The title painting is epic; the map in play has nothing taller than the 8 m Fort.

4. **The 3D work was ordered so the stage was empty.** Ground, houses and word cards (C3, C6, C10) shipped before foes, heroes and scenery (C7, C8, C9), so the owner's first look at 3D had no foes, no Draconis, no helpers, no villagers and no trees. Even the 36 choppable trees, a gameplay object, are invisible. The 2D debug tier tells more about the game than the 3D view.

5. **The ground, the largest thing on screen, was left at score 3.** The mint-green 095 tiles are still in use. Their replacement (122) scored 7.5 and the next try (201) was blocked by quota. Nobody fell back to a free CC0 ground material while waiting, so the screen stayed a football pitch.

6. **No verticals, so lighting cannot work.** The Epic style pack (warm sun, teal shadows, fog, AO) is in the code, but on a flat lawn with one building there is nothing to cast shadows, catch rim light or sit in fog. Light design needs cliffs, trees, rocks and water to act on.

7. **Day and night are the same picture.** No moon, lanterns, mist or Rift glow, and no change of weather across five days. The game's structure (build by day, defend by night) has no visual expression.

8. **Water is treated as a rectangle.** The stream is the sim's water box drawn as a flat strip: no banks, reflections, flow or source. In a world about silver waterfalls, the only water on screen looks like concrete.

9. **Off-direction models and rustic leftovers.** Thatched towers and huts clash with the epic direction, and their rebuild (129) was never decided.

10. **We scored ourselves.** Scenes were self-scored, often against our own earlier screens, and no reference board sat beside the map shots. Words in the art bible were strong; the image they describe was never made.

**What changes now:** gameplay layout in the Battle view frame first, a concept painting per map accepted at 8 or more, a grey-box matched to the painting, life on screen before polish, then landmark band, water and per-beat light, and judging only in-game shots against the painting and the reference board (section 2).
