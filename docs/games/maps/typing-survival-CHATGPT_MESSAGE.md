# Last Line, map 1: message for ChatGPT (paste below the line)

Mode: Chat, High reasoning. Attach `games/typing-survival/art-src/_review/maps/map1-base-1280x720.png` (required) and, for the heroine's identity only, `games/typing-survival/art-src/ui/screens-epic/results-lose-bg.png` (optional). Source concept: `docs/games/maps/typing-survival-MAP_CONCEPTS.md` §1–§6.

---

You are the senior art director of a premium sci-fi action game. The game is **Last Line**, a typing survival game in a 3D web engine (three.js). The player types words to load guns. A lone heroine and her drone hold one straight lane, a causeway on a space station at the edge of a black hole, against the Black Hole Horde. We need the battle map to reach commercial-game level (epic, majestic, cinematic light). Our own art is not the reference.

## (a) What I need from you, in two steps

**Step 1: Review.** Review the map 1 concept below as a senior art director against the commercial bar.
1. Score it out of 10 for a commercial release, with a three-line why.
2. List the gaps that keep it from 8.5.
3. Propose concrete improvements that **keep the gameplay layout and the camera exactly as they are** (materials, light, the landmark's silhouette, depth cues, life, colour script), each with its place in the frame (px at 1280 × 720) and why it helps.
4. Flag anything that would hurt readability during play.

**Step 2: Paint.** Paint **one** concept image **over the attached base image** (1280 × 720).
- The base is a real frame from the game's battle camera.
- Keep its exact camera, perspective and layout.
- Every coloured block marks a planned element at its true place and size. Paint the real thing there; the block colours are labels, not paint colours.
- Every grey box is a HUD or gun-card zone. Leave each one flat neutral grey, and put nothing important under it.
- No text of any kind.
- Your painting decides only light, materials, mood and scale.
- If your review proposes changes, paint them only if they keep the layout.

Base image legend (screen px at 1280 × 720, x from the left, y from the top):

| Block | Element | Where |
|---|---|---|
| cyan | the heroine, 2.6 m tall, seen from behind, holding the left card's gun | x 623–657, y 484–571 (68 px tall: keep her this small) |
| white | support drone at her right shoulder, fires the right card's gun | x 668–704, y 486–518 |
| pale cyan-white line | the Line (the defended edge) across the deck | y 495–504 |
| violet, outlined | muster ground: the deck past the gate where the Horde queues | x 448–832, y 0–70 |
| lime | the gate: a low sill across the deck and two squat bastions (2.5 m) | sill y 61–74; bastions x 345–432 and 848–935, y 24–80 |
| blue | steel buttresses under the deck edge, every 12 m | along both deck edges |
| pale gold | **the hero landmark**: the lower arc of a colossal broken station ring, 2.4 km across, 6 km away on the left, far below the causeway | arc x 0–472, y 0–172; its lit face is the brightest region, x 150–330, y 110–172 |
| near-black, thin warm rim | the black hole's shadow, ahead and below the far end (the deck hides its middle) | two lobes, x 192–470 and 810–1088, y 0–≈240 |
| orange | the accretion disk, a sea of plasma kilometres below | every side area not covered by another block |
| lavender | a lower service bridge 700 m below, running off the right edge | x 1100–1280, y 515–600 |
| pink | three small evacuation shuttles, far out on the right | x 1109–1178, y 110–136 |
| grey | HUD and gun cards | top bar y 12–80; word box x 500–780, y 352–458; gun cards x 32–262 and 1018–1248, y 216–316 (tabs above at y 176–216); chips x 32–164 and 1116–1248, y 338–372 |

Kept from the real frame: the deck, its walls and posts, and the foes (packs at y 120–270 and in the queue). Keep their places, repaint their look. The hazard stripes, the red glow on the Line and the white glow at the top centre are today's placeholders: do not keep them.

## (b) Hard constraints

1. **Camera.** Locked: pitch 36° below the horizon, vertical FOV 42°, 19.8 m up and 17.75 m behind the heroine. The lane is 24 m wide and runs straight from the bottom centre to the gate sill near the top edge. The deck leaves the top edge 56 m out.
2. **No sky and no horizon.** Every view ray in this frame points down (15° below horizontal at the top edge). The frame never sees the horizon, so do not paint one, nor a sky band, a skyline or stars above a horizon. Beside and beyond the deck we look down into the abyss: the disk far below, the black hole's shadow ahead and below, structures rising from the depth.
3. **Gameplay readability first.**
   - The lane, the gate sill, the Line and the foes read instantly; abyss light never washes out the foes.
   - The deck stays dark graphite, darkest round the heroine and round the grey word box (the player's eyes live there).
   - Nothing bright right behind the lane, behind a grey zone, or in the lower side areas (y 372–720 beside the deck).
   - The heroine stays at her block's size.
   - Nothing along the lane taller than the low parapet posts (it would lean into the gun cards).
4. **Colours reserved for signals.**

   | Colour | Reserved for |
   |---|---|
   | Purple-violet | the Horde only (foes are black glass and dark chitin with glowing purple veins) |
   | Red | a foe attack only: none in this frame, so no red |
   | Gold | Pack Leaders only, near the lane |
   | Cyan | the heroine, her drone, the Line and friendly lamps |
   | Orange-gold | the disk, kept in the abyss and off the deck |
   | Blue | Shield Guards' shields |

5. **Licences and style.**
   - Paint an original image.
   - Do not copy or imitate a specific existing game, film or artist.
   - No logos, signatures or watermarks.
   - Painterly-realistic, crisp large shapes, commercial game quality.

## (c) Map 1 concept: Chapter 1, stage 1, "First Shift"

**World.** The VC-7 causeway, a 4 km bridge of graphite steel and pale ancient stone. It runs from the station's citadel (behind the camera) out over the accretion disk toward the black hole, which lies ahead and below. The Horde crawls out of the black hole's shadow and walks the causeway toward the citadel. Stage 1 is Span One, "first light", the first real watch.

**Gameplay.** Hold for 150 s. Foes come over the gate in packs of 4–12; two surges; the first Brutes push through the swarm late. The heroine's gun (bay 1, a compact twin-barrel energy carbine) and the drone's gun (bay 2, a heat beam) fire as the player finishes words.

**Hero landmark: the Broken Ring of VC-7.** A colossal station ring, 2.4 km across, standing nearly upright 6 km out on the left, its centre about 1 km below the deck.
- Only its lower arc is in the frame: a U from the top edge down to y ≈ 141 near x 230, and back up.
- Its broken top lies above the frame.
- Its pale stone-and-steel inner face blazes in the disk's light from below: the brightest region of the frame.
- Behind it, the black hole's shadow gives it a black backdrop.

**Depth layers.**
- **Foreground:** a dark stone dais under the heroine with her faint cyan glyph ring; the Line as its front lip; a low stone parapet capped with steel, short lamp posts, a cyan running light.
- **Playfield:** long graphite plates and pale stone bands, inset seams, faint cyan glyph inlays, light wear; the packs walking in.
- **Gate band:** the low sill and two squat bastions; past them 2–3 packs queue, purple veins glinting.
- **Below the deck edge:** heavy buttresses every 12 m; two cyan coolant falls pouring into the abyss.
- **Far and abyss:** the ring; the lower bridge; tiny shuttles; the disk's plasma kilometres below, brightest on the left under the ring; the black hole's shadow at the top on both sides.

**Light and colour.** Key: warm gold up-light from the disk below and ahead-left. Fill: cool navy from above. Cyan rim on the heroine; dust shafts rising from the abyss. Mood: heroic, vast, lonely. Colour script: graphite and navy 55 %, orange-gold 30 % (abyss, mostly left), black 10 % (the shadow), cyan 5 %; purple only on foes.

**The heroine** (seen from behind and high above): slim, white-gold ceramic armour over graphite, a dark helmet with swept crest fins, a navy three-panel cape with fine gold filigree, thin cyan seam lights down her back. **The drone:** a white-gold teardrop with one large cyan eye and short fins.

**Life where the player looks:** the foes on the lane and in the queue; the heroine raising her gun; the drone's eye light sweeping the near deck; the shuttles; the coolant falls.

## (d) The other maps, for a quick idea review

Same camera and rules; each stage is a farther span with its own landmark far out and far below. Trial: map 1's set at a cold night light, a citadel beacon's beam sweeping the abyss. Stage 2: a tilted 700 m monolith on the right whose antenna crown glows gold when a Pack Leader arrives. Stage 3: a violet tear in space under the bridge that brightens on the side where a rift is about to open. Stage 4: three shield-emitter pylons below on the right holding a cracked hexagonal curtain of blue light, the source of the foes' shields. Stage 5: a capsized freighter crashed onto the causeway past the gate, its belly pulsing violet with the nests. Stage 6: a broken antenna spire in a violet storm whose lightning numbs her guns. Stage 7: a parallel causeway shattered into drifting segments on the left. Stage 8: the station's collapsed core, a pale sphere with debris spiralling in, under the gravity well. Stage 9: a white-and-gold archive spire ringed by turning rings of abstract glyphs. Stage 10, the boss: a void serpent coils up out of the black hole on the right and looks up at the Line.

Tell us in two or three lines which of these ideas is weakest for this top-down camera and what you would do instead.

## (e) Attachments

1. **Required:** `games/typing-survival/art-src/_review/maps/map1-base-1280x720.png`. It is the base to paint over.
2. **Optional:** `games/typing-survival/art-src/ui/screens-epic/results-lose-bg.png`. Use it only to keep the heroine's and the drone's identity, materials and colours. Do not copy its camera or composition.

Answer in this order:
1. Score and three-line why.
2. Gaps.
3. Improvements with their screen positions.
4. Readability flags.
5. Two or three lines on the other maps.
6. The painted image.
