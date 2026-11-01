# Judging a concept painting and a built map

The bar is in `AGENTS.md` and `ART_ACCEPTANCE.md`. Two independent blind judges must both score 8.5 or more, with appeal scored next to market level. There is no provisional pass. The market-level scale is ART_DIRECTION §1.3, where the owner's reference `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` is a 9. Our own self-scores ran higher than the judges' (8 against 7), so never accept your own work.

## 1. Blind judging

The round setup (fresh judges, the judge folder, the key, the brief template, answers in Vietnamese) is in [game-art-pipeline judging](../../game-art-pipeline/references/judging.md). For maps:

- **Use neutral labels** (A/B/C). Keep the key outside the judges' folder. Judges do not read reports, prompts or the concept's claims.
- **Judges write "what I see" first, then the scores.**
- **Put the shot beside the reference board** at the same height, and give one line: "stands beside it" or "not yet".
- **Bring in a third judge** when the two land on either side of a pass mark or differ by 2 points or more.

## 2. Criteria and pass marks for a concept painting

Every criterion passes at 8.5 from both judges, as in `game-art-pipeline` ("pass mark 8.5 on every axis"). The 01/11 retries still used 8 for layout and readability; that lower mark is retired. Appeal was added on the evening of 01/11.

| Criterion | What the judge checks | Pass |
|---|---|---|
| Market level (M) | ART_DIRECTION §1.3, against the commercial board | 8.5 |
| Appeal | Captivating, stylish, luxurious, modern, rich in detail. Clean but plain fails (owner 01/11: "đừng làm hình ảnh của game trở nên nhàm chán, đơn giản, thiếu đi sự hấp dẫn") | 8.5 |
| Layout fidelity | Every gameplay element and planned piece on its block in the base. Overlay the painting at 50 % on the base, or compare edges, and measure the drift in px for each element | 8.5 |
| Readability | The half-size greyscale and blurred copy shows lanes, foes, our units and health bars, and decorative floors vanish. Lanes are one value step over the ground. The play zone is calm. Foes separate from the ground | 8.5 |

Measured on 01/11:
- without a base: market level 7–7.5, layout 5.5–7.5;
- with a base: layout 8.3–8.5 on the first try;
- a lower half that drifted 45–85 px dropped layout to 6.4–6.5.

The painting is a target for the build, so layout fidelity is not optional.

## 3. Reject list (paint again if any holds)

- It looks like a miniature, a diorama, a park or a floating island.
- A lane is not the clearest ground, or roads are far brighter than one step.
- A tall object hides a lane, a slot or the defended point. A piece leans into a HUD card.
- Two landmarks compete for the eye, or there are many equal attractions.
- A reserved signal colour covers a large area. There is glowing gold in the world, red outside a foe attack, or the foe faction's colour pooled on the ground.
- A horizon, a sky band, a skyline or a white glow at the top centre shows when the camera has no sky.
- The layout, the camera, the hero's size or a grey HUD box moved off the base.
- Something bright sits behind a grey zone, under the word line or right behind the foe lane, or the brightest region sits outside its free band.
- Shadows have no caster, there are two light directions, or mist or haze is the brightest mass.
- Foes do not read as the game's foes (villagers, cute animals, our side's colours), or they sink into the ground.
- It contains any text, number, logo or UI.

## 4. Judging the built map

- **Use the built play host with the player's settings and no URL flags.**
  - Dev-only gaps count as P0. Dragonhold's ground textures loaded only in dev, and nobody saw it until the play build was judged.
- **Take the shots:**
  - at 1280×720 and 1920×1080, at the player's default tier and on High and Ultra;
  - with the default camera, plus the tilt and zoom extremes the player can reach;
  - at each beat that changes the look (day, night, storm, boss);
  - for roads, a crop at a bend and one at a junction or bridgehead (PATH_QUALITY).
- **Put each shot beside the accepted painting and the reference board.** The question is "does the build match the painting and stand beside the board?", not "is it better than before?".
- **Numbers next to the scores:**
  - the lane-core luma step;
  - ground luma under the word tags;
  - the play-zone luma limit;
  - foe wash-out from the environment's light (Last Line allows at most 10 %);
  - word-tag contrast;
  - frame time and draw calls per tier on the real GPU bench (`.local/bin/heavy.sh --gpu`, at dpr 1 and 2);
  - texel density at the nearest row.
- **Ultra must differ from High for real.** A Quality change must take effect, reloading if it has to.
- **Shared systems** (typing feedback, keyboard sounds, character animation) keep their bar of 9. Rerun their measuring scenario after any map change that touches light, bloom or the grade: a global bloom cut once erased the typing glow.
- **Keep only the contact sheets, compare shots and JSON numbers.** Prune the raw frames.
