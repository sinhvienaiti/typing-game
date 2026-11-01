# Camera, frame budget, base image and legend

The battle camera decides what a map can be. On 01/11/2026 all three games had concepts that painted a sky band or far mountains the battle camera never shows. Their landmarks stood 300 m to the side, outside the frame at any height. Compute first, then imagine.

## 1. Find the camera of record

- Read it from source: the camera rig file and its constants, every named view (home, close, overview), the tilt and zoom limits, and the look point. A doc or a plan may be out of date.
- Use the play build's camera, not a dev flag or a sandbox view. If an owner trial camera is pending, compute both cameras and keep every position valid in both. Dragonhold did this for the default and O3.
- Note the aspect ratios the game supports. 1280×720 is the reference frame, and 1920×1080 is the same frame at 1.5×.

## 2. Mirror it with `../scripts/frame-budget.mjs`

```bash
node .agents/skills/game-map-concept/scripts/frame-budget.mjs \
  --camera <game>/tmp/map-concepts/cam.json --layout <game>/tmp/map-concepts/map1.json \
  --check <game>/tmp/map-concepts/pairs.json --mvg <game>/tmp/map-concepts/blocks.mvg
```

- **`cam.json`** takes the engine's own world axes. Use the orbit form (`look`, `distance`, `pitch`, `yaw`, `fov`) or the direct form (`position`, `pitch`, `yaw`, `fov`). `yaw 0` looks toward −z.
  - If the sim's axes differ from the engine's, convert them first. Last Line's docs count z away from the heroine; in engine terms that is −z.
- **`--check`:** read three to six points from the running game. Use the engine's own `project()` through a debug hook or probe, or the screen positions it reports for bridge ends and foes. Spread the points over the top band, both wings and the bottom.
  - Any error over 2 px means the camera model is wrong. Fix it before you trust a single number.
  - The three games matched to 0–2 px.
- Keep the game's copy of the camera file, the layout file and the outputs under `games/<id>/tmp/map-concepts/`. They are not tracked; rerun the script to rebuild them.

## 3. Read the frame

| Output | What it decides |
|---|---|
| Sky line | `no sky` means the top edge looks below the horizon. Then no painting, prompt or build shows a horizon, a sky band, a skyline or far mountains above the ground. Sky lives on the title and results screens and in the intro sweep, and in play only as reflections in water |
| Rows | The ground under each screen row, how wide the frame is there, px per metre, and the height of a 2 m unit (`--unit`). These set the drawn size of foes and pieces |
| Height budget | How tall a thing standing on that row can be before the top edge cuts it. In the top band it is a few metres: Wordwoven had 1.6 m at y 20, and Last Line 4.3 m at its gate. Trees there show trunks only, with crowns overhanging from beyond the edge |
| Points: "rises into it above X m" | The foot is nearer than the bottom edge. A wall or tower there enters the frame from below, over the play and the HUD. Dragonhold's 16 m gatehouse would have covered both south house pads, so its rampart was cut to 8 m |
| Points: "shows only below X m" | The ground spot lies past the top edge. Only things below the play surface show there: an abyss, a lower span, a megastructure seen from above |
| Points: "leans out of the left/right edge" | The foot is in frame, but a tall piece there runs out through the side edge before the top edge, often across the side HUD cards. Check its top against them |
| Points: "outside the frame sideways" | Nothing placed there is ever seen. Move it or drop it |
| HUD footprints | The world ground each HUD box hides. Keep lanes, crossings, resources and the landmark's key read (a face, an eye) out of them. Transient cards, such as a wave card, must treat the landmark's screen box as a keep-out zone |
| Texel need | The texels per metre the ground needs to reach one texel per pixel at the nearest row, ×2 for dpr 2, and more at the closest zoom. Dragonhold's 2048 ground bake gave 5.1 cm per texel where the screen needed 2.8 cm (1.4 on Retina), so the ground was blurred 1.8–3.6× |

Tall things also **lean outward** on screen. A mast at the lane edge runs out toward the frame edge and up into the side HUD cards: on Last Line a 10 m mast crossed gun card 2. Project the top and the foot of every tall piece, not only its foot.

When the budget is too small for a piece the stage needs, pick one of these, in this order:
1. Design it low and wide, and good-looking **from above**. At 40–60° the camera sees roof tiles, the tops of pillars, the faces of daises and the backs of foes. Briefs for textures and Tripo sources must care about those top faces.
2. Change the view, never the sim. Tu Tiên raised its view headroom from 2.5 m to about 5.5 m, so the arena shrank about 8 % and the gates fit.
3. Move the tall part to the wings, below the play surface, or into the intro sweep.

## 4. Capture the base image

1. **Play host, battle camera, real moment.** Run a wave with foes on the lanes, a held clock and a fixed seed. Use the shipping quality tier.
2. **Canvas only.** Hide every DOM layer (HUD, word tags, cards) before the shot. Paint out lane-cue numbers or any text that is left. The image has no text at all.
3. **Take out what is being replaced only where it covers a planned piece.** For example, clone deck plates over the old ship. Keep everything the gameplay fixes: lanes, gates, the defended point, houses, foes.
4. **Desaturate about 45 %**, as Dragonhold did, so the blocks read and today's look does not anchor the painter. Say in the legend that only positions count, not the look.
5. **Draw a translucent block for every planned piece** at its projected place and height (`--mvg` writes the draw file). Give each block a distinct flat colour.
   - Draw a block below the play surface only where the camera would see it: mask it out where the deck or ground hides it.
6. **Grey the HUD boxes.**
   - Measure them from the DOM on the play host, taking the union of the phases (prep, wave, break), plus a 4 px margin.
   - Always-on boxes are flat mid grey (`--mvg` draws 50 % grey at 92 %). Boxes shown only at times (tutorial rows, boss bar) are light grey.
7. **Make it 1280×720, a PNG, with no text.**

The raw frames and the base image are captures, so they stay under the game's `tmp/` (for example `games/<id>/tmp/map-concepts/`), never in `art-src`, `public` or `docs` (`AGENTS.md`). Link the base image from the concept doc: `node tools/capture-prune/prune.mjs <folder>` keeps images a doc links, so run it without `--apply` first, check the list, then prune your raw frames with `--apply`. Paintings returned by ChatGPT, Gemini or Firefly are generated art, not captures: they go to `games/<id>/art-src/_review/maps/` with their `.prompt.txt` sidecars (the 01/11 bases of Dragonhold, Wordwoven and Last Line also sit there). All of these are media and never go into Git.

## 5. Write the legend (`map<N>-base-legend.md`, beside the image)

1. **What the image is.**
   - The capture source: host, branch and commit, date, stage id and seed.
   - The camera numbers.
   - What was hidden, removed or desaturated.
   - The sky line, for example "no sky: the top edge looks 21° below the horizon".
   - A statement that the blocks are placement codes, not colours to paint.
2. **Keep as they are.** The gameplay elements, with their screen positions: lanes as polylines, the defended point, gates, crossings, houses, units.
3. **Colour table.** One row per block, with its colour, the element (what it becomes, in a sentence), its world position and size, its screen box at 720p, and notes, such as "only its lowest 3 m are in frame".
4. **Grey boxes.** Each HUD zone in px, always-on or at times, plus the transient cards that are not greyed.
5. **Signal colours.** The reserved colours, never large areas. Block colours are labels, not palette, and the painting has none of them as flat areas.
6. **How it was made.** The script names and the folder, so it can be rebuilt after the raw frames are pruned.

`tmp/` is not tracked, so copy the colour table, the grey boxes and the signal colours into the concept doc's battle-frame section (`concept-doc.md` §3.2) as well; the doc is the copy that survives.
