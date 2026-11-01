# Worked examples (01/11/2026)

These are examples, not rules: four genres and four cameras, so a new game can find the closest case. Each game's own concept doc is the current source for its numbers:
- Dragonhold, Wordwoven and Last Line: `docs/games/maps/<game>-MAP_CONCEPTS.md`, with the `-CHATGPT_MESSAGE.md` and `-CHATGPT_REVIEW.md` files beside each.
- Tu Tiên: `docs/games/tu-tien/MAP1_CONCEPT.md`.
- The 01/11 base images, legends and paintings: `games/<id>/art-src/_review/maps/` (new base images stay under `tmp/`, see `camera-and-base.md` §4).

## Dragonhold, map 1 "Bridge and Brook" (lane defence, fantasy mountain pass)

- **Camera.** Pitch 55°, 95 m, vertical FOV 30°, looking 4 m north of the dragon platform. The camera sits at (0, 78.4, 50.5). The player can tilt 40–75° and zoom 0.6–1.3×.
- **Frame.** No sky at any allowed tilt: the horizon sits at y −1,559 at the default and y −767 at 40°. The frame covers about 100 × 65 m of ground.
  - In the top band, a piece shows whole only up to about 6 m at z −36.
  - An 8 m arch just fits at z −30.5.
  - A 16 m gatehouse at the bottom would cover the south pads, so the rampart became 8 m and the gatehouse left the frame.
- **Scale.** The West Warden, a stone dragon carved from the left cliff, stands 22 m tall: ten times a 1.4×-drawn soldier. It sits on the left wing, with its face kept below the wave card.
- **Read order.** Fire dragon with the Warden (living fire against dead stone) → the platform and the two lanes → the bridge and the ford → the north gate muster → the rampart, tower and cascade as the frame.
- **Light.** Dawn from the upper right. Gold lands only on the Warden's east planes, the bridge crowns, the platform rim and a few grass edges. The meadow is subdued olive. Only the fire and the braziers bloom.
- **Signals.** Red, orange, gold and turquoise are reserved. Blight yellow-green appears only in foe eyes and cracks. Violet appears only as a thin haze at the gates.
- **Review.** 8.1, with 8.7–9.0 expected after the changes. The main changes:
  - too many landmarks, so the supporting ones were toned down;
  - one masonry language, with four granite families;
  - two lane materials;
  - the river kept to dark slate-teal with foam only at named places;
  - a thin threat at the gate;
  - a heavy foreground rampart.
- **Paintings.** Without the base: layout 5.5–6.5. The second try's fixes:
  - the bastion was 2.9× its block;
  - the lane, river and Warden had drifted east;
  - the HUD boxes had shifted;
  - the rampart was drawn front-on;
  - the banners were red.

## Wordwoven, map 1 "Silverfall Meadow" (tower defence, East Asian fantasy)

- **Camera.** Home view: 42°, 46 m, vertical FOV 42°. The top edge looks 21° below the horizon. A sky band would need a 16.5° tilt.
- **Height budget.**

  | Screen y | 20 | 45 | 70 | 90 | 135 | 180 | 360 | 540 |
  |---|---|---|---|---|---|---|---|---|
  | Height (m) | 1.6 | 3.5 | 5.2 | 6.5 | 9 | 11 | 18 | 22 |

  A standing giant could only show in the lower half, where it would hide the play.
- **Scale.** It comes from the ground and the top edge:
  - the Rift's ink tide spilling down the road;
  - a cropped forest edge with crowns overhanging from beyond the frame;
  - a limestone spur whose top leaves the frame;
  - a 16 m inlaid sun-star ring, kept low-contrast;
  - the gorge edge in the top-right corner;
  - giant cloud shadows, and the dragon's long shadow.
- **Review.** 7.9: "should not be redesigned. It should be edited." The scores and changes:
  - focal points scored 7.2, readability 7.6 and depth 7.5;
  - the value table in `composition.md` §5;
  - dark fired-tile roofs instead of thatch;
  - the Rift's interior at 8–15 %;
  - no glowing gold.
- **Paintings with the owner-attached base.**
  - Try 1: market 7.4/7.5, layout 8.3/8.5, readability 6.8/7.5.
  - Try 2 drifted (the lower half 45–85 px up), and layout fell to 6.4/6.5. The retry listed every element's box.
  - Foes painted as villagers or a cute raccoon, and zombies in our side's navy, needed explicit foe kinds and a separate colour family.

## Last Line, Chapter 1 stage 1 "First Shift" (one-lane survival, sci-fi causeway over a black hole)

- **Camera.** Pitch 36°, vertical FOV 42°, 19.8 m up and 17.75 m behind the heroine. The top edge looks 15° below the horizon at the centre and 12.6° at the corners, so there is no sky.
- **Frame limits.**
  - At the gate (z 40) only 4.3 m of height shows.
  - Tall things at the deck edge lean into the gun cards, so nothing along the lane is taller than the 1.82 m lamp posts.
- **Scale from below.** The field stands high, so the epic lies below the deck: an accretion disk, the black hole's shadow ahead and below, and the Broken Ring.
  - The Ring is 2.4 km across and 6 km out, its centre 958 m below the deck; only its lower arc shows, from the top edge down to about y 141.
  - It needed thickness, ribs, asymmetric damage and haze to read at that size. A smooth lit U read as a few hundred metres.
- **Light budget.** One brightest region, the Ring's lit face, in the free band above gun card 1. The heroine's basin and the lower side areas stay darkest. The orange abyss was cut from 30 % of the frame to 15 %, so the deck no longer floats as a silhouette over a glowing carpet.
- **Signals.**
  - Purple belongs to the Horde only.
  - Red marks foe attacks only.
  - Gold belongs to Pack Leaders, so the heroine and the Ring became ivory.
  - Cyan marks our side, kept sparse.
- **Review.** 8.0. The weakest stage idea, a violet storm, was replaced by a near-black cyclone because it clashed with the Horde's purple.

## Tu Tiên, map 1 "Thanh Thạch Ải" (arena defence, painterly-realistic xianxia)

- **Camera.** 55°, vertical FOV 28°, fixed. The top edge looks 41° below the horizon. The arena fills about 85 % of the frame, and the outer rim is a thin top band plus two side triangles.
- **Height budget.** About 2.5 m at the far edge was too low for the gates. The owner chose a view-only headroom change to about 5.5 m (the arena about 8 % smaller), and gates that are wide, low and good-looking from above.
- **Design for top faces.** At 55° the camera sees roof tiles, pillar tops, the disc's face and the backs of beasts. Tripo sources must care about the top.
- **Value plan.** The beast corridors are 1.3× the surrounding stone. Inside the Kết Giới ring it is mid-dark and calm, so the words stand out. The rim is darkest and the Trận Tâm core brightest, with no area at ≥ 0.95 luma over more than 6 % of the arena.
- **The rim.** Painted from above (a sea of cloud, cliff tops, pine crowns), never a horizon.
