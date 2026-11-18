# Thanh Thạch Ải map 1: message for ChatGPT (paste as one message)

Use ChatGPT in normal **Chat** mode, **High** reasoning (never Work mode). Attach the two files listed in part E, then paste everything between the two rules below. Concept source: [`MAP1_CONCEPT.md`](MAP1_CONCEPT.md).

---

## A. What I need from you

You are a senior art director on a commercial xianxia (cultivation-fantasy) strategy game. Below is the concept for the first battle map of **Thanh Thạch Ải** ("Bluestone Pass"), a 3D pass-defence typing game: beast tides walk from two stone gates at the far edge toward a formation heart at the centre of a paved mountain terrace, and the player, a sword cultivator standing near the heart, types English words to cast sword skills.

Do two things, in this order:

1. **Review the concept.**
   - Score it out of 10 against commercial games of this kind and setting: Where Winds Meet, Genshin Impact (Liyue), Black Myth: Wukong environments, Tale of Immortal's battle scenes, Diablo IV for readability. 8 is a shippable commercial map; we accept only 8.5 or more.
   - List the biggest gaps: composition, scale, depth, light, materials, life, readability.
   - Propose concrete improvements that **keep the gameplay layout**: the terrace size, the two gates, the two pillars, the heart, the barrier ring, the six mechanism sockets and the camera are fixed. You may change dressing, materials, light, the shape and detail of each planned piece, and what fills the rim and the side wedges.
2. **Paint one concept image over the attached base image (`greybox-prep-1080.png`).**
   - Keep its exact framing, camera and layout. The gates, pillars, heart disc, barrier ring and the six socket marks stay where they are (positions in part C; the second attachment `legend-prep-1080.png` shows a 5 m grid and labels, for reference only, do not paint the labels).
   - Replace each grey placeholder with the piece the legend in part C names, at the same position. No flat placeholder may remain.
   - Keep the dark HUD boxes plain and empty.
   - No text, letters, numbers, icons, UI or watermark anywhere.
   - Output 16:9, 1920×1080 or the same aspect.

After the image, add three lines on what you changed from the concept and why.

## B. Hard constraints

- **Camera.** Fixed strategy camera looking 55° down with a 28° vertical field of view, facing north, framing the whole 40 × 26 m terrace. The base image is a real capture from it. Do not move, tilt or widen it; no side view, no diorama, no floating island.
- **No sky, no horizon.** The top edge of the frame is 41° below the horizon. Land, cloud sea and cliff tops continue past every edge, all seen from above. No mountains silhouetted against sky, no clouds above a skyline.
- **Height budget.** Anything standing on the far edge (the gates) is at most 5 m tall or its top leaves the frame; the pillars (10 m closer) may reach 8 m. Design roofs and tops to be seen from above: tiles, ridge ends, pillar caps, the heart disc.
- **Gameplay reads first.**
  - The two beast corridors (gate → heart) are the clearest, brightest ground in the frame: worn polished bluestone flags, clearly brighter than the mossy slabs around them (about 1.3× luminance).
  - The ground inside the barrier ring (radius 9 m around the heart) stays mid-dark and quiet: word tags and damage numbers float there. No pale stone, no bright highlights there.
  - Nothing tall stands between the camera and a corridor. Tall pieces lean outward toward the frame edges.
  - One hero landmark: the formation heart. Everything else frames it.
- **Colours reserved for signals.** Never paint large areas in bright red, orange, gold or turquoise. Those are the game's enemy-warning, urgency, reward and typing colours. Vermilion only as a tiny seal mark; warm lantern light only as small points.
- **Setting.** Vietnamese-flavoured cultivation world, not a Chinese palace: grey-blue limestone like Ninh Bình and Hà Giang karst, old pines, indigo mist, ivory jade inlays, dark timber, indigo-grey roof tiles. **Not:** Chinese characters, red paper lanterns, golden palace roofs, golden dragons, Buddhist temple bells, torii.
- **Style.** Painterly-realistic: real material response (wet limestone, moss, lichen, dark timber, glazed tile, jade) with a painterly colour grade, cinematic morning light, epic scale. Not cute, not toy-like, not plastic, not low-poly, not flat ink-wash.
- **Only what we can build.** Every piece must come from:
  - our Tripo-made models: stone gate (×2, mirrored), formation heart, stone pillar (×2), three mechanisms, flying sword, limestone boulder, and if you keep them small stone lanterns;
  - tiled PBR ground materials (limestone flags, mossy slabs, gravel, mountain grass, exposed karst, stone steps) with painted overlays and eight ink-and-moss decals;
  - three painted rim plates seen from above (cloud sea; cliff tops and pine crowns; near mist) and grass or fern cards;
  - shaders for the barrier ring, the heart glow, low mist and the socket marks; bloom kept to thin bright cores.
  No water bodies, no buildings other than the gates, no crowds, no animals inside the terrace.

## C. Legend of the base image (world metres; x east, z north-negative; heart at 0;0)

| Placeholder in the base image | Position | Replace with |
|---|---|---|
| Pale disc at centre with a rune ring | heart (0; 0), radius 3 m | Formation heart: concentric bluestone rings, an ivory jade core glowing softly (the brightest point after the sun), four low stone posts |
| Small teal dot south of the heart | Tâm nhãn (0; +3) | A 1 m carved stone circle where the cultivator stands |
| Thin white circle | barrier ring, radius 9 m | Ivory jade inlay line, 0.25 m wide, cloud pattern, faint breathing glow; quiet dark slabs inside |
| Two beige lit wedges from the top corners to the ring | corridors from gate A (−15; −18) and gate B (+15; −18) | Polished bluestone flags, brighter than the rest, scratch marks and ink stains near the gates, mossy drainage gutters at the edges |
| Two grey cylinders | pillars T (−6.4; −7.7) and P (+6.4; −7.7), radius 0.9 m | Bluestone pillars about 4.5 m tall with jade caps and an old iron ring |
| Two brown post-and-lintel frames at the top | gates A and B, width about 5 m | Stone gates: two massive square bluestone posts, a stone lintel, a low wide indigo-grey tiled roof seen from above, a small stone lantern each side; at most 5 m tall |
| Six thin outlines (two strips, four circles) | sockets at (−10.2; −12.3) strip, (+10.2; −12.3) strip, (−11.5; −8), (+11.5; −8), (−10; −2), (+10; −2) | Carved stone sockets: strips are grooves with peg holes, posts are round carved pedestals; subtle, visible only up close |
| Dashed lines from the top corners | sky lanes from (±20; −18) | No object; a wisp of mist at each far corner |
| Beige flat ground with grid | the terrace | Large uneven bluestone slabs with moss in the joints, a few cracked flags, shallow 0.2 m steps at the sides, decals |
| Dark olive flat area outside the terrace | rim | Far edge: a 1.2 m dry-stone wall, then cloud sea seen from above with a few karst tops and pine crowns. Sides: low stone balustrade, then the cliff edge dropping into cloud, pines clinging to the rock (only their crowns visible), boulders, mist. Near edge: the head of a stone stair down to the sect gate, two railing posts with stone lanterns (mostly under the typing bar) |

## D. Concept (what we plan to build)

**Light.** One key light: low early-morning sun from the north-east (upper right of the frame), slightly warm, long shadows to the south-west so posts, gates and steps have volume; shadows kept off the corridors. Fill: cool indigo mist bounced from the cloud sea; a 0.3 m low mist layer outside the barrier ring, never inside it. Secondary: the ivory heart glow; small warm stone lanterns at the gates and railing. Eye order: heart → the two gates (and the beasts pouring in) → the two pillars → the misty rim.

**Value hierarchy.** Corridors 1.3× the surrounding slabs; inside the ring mid-dark; rim darkest; heart brightest; no large area near white.

**Materials, one family.** Grey-blue limestone (slabs, pillars, balustrade, gates), moss and lichen, dark ironwood (lintels), indigo-grey yin-yang tiles, ivory jade (inlays, heart core), old iron (pillar rings, lanterns), mist.

**Life.** Mist drifting slowly through the gates; sparse falling pine needles; lantern flicker; a few tiny cranes over the far cloud sea (never inside the terrace); mountain grass swaying at the side wedges.

## E. Attachments

1. `greybox-prep-1080.png`: the real camera capture (base image to paint over).
2. `legend-prep-1080.png`: the same capture with a 5 m grid, coordinates and labels (reference only).

Both are in `games/immortality-cultivation/tmp/plan-2026-11-01/` on the owner's Mac.

---
