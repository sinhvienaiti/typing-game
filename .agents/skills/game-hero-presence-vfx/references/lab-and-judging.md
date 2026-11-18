# Lab, measurement, capture and judging

## 1. The lab page

- **Where:** extend the game's existing effects showcase, bench or lookdev page (for example `runFxShowcase` in `games/dragon-hold/src/view/bench.ts`, or Tu Tien's `lookdev.html` and `bench.html`). If the game has none, add a dev-only page inside the game. Never build a parent-repo page that re-creates the renderer.
- **Real pipeline:** import the game's own stage or scene constructor, camera module and quality table. Pick the tier with the game's own quality setting, the one players use. A lab that sets its own tone mapping or bloom is judging a different picture.
- **Independence:** the page never reads files from the parent repo. A clone of the game alone must run it (VFX_STANDARD §4.5).
- **Controls:**
  - a switch and an intensity per layer;
  - state buttons;
  - clock hold, step ±1 frame, 0.25× and 1×;
  - ground: light, dark, the real map;
  - camera: play, close-up, and the menu or intro pose;
  - reduced motion through the game's setting;
  - bloom exactly as the tier ships it.
- **Readouts:** `renderer.info` (calls, triangles), live motes, lights, frame time and the per-layer delta, as JSON the capture script can read.

## 2. Cost per layer

- Use the game's heaviest bench scene (crowd included), a fixed camera and warmed-up shaders.
- For each layer, run at least 600 frames on and 600 off, in alternating blocks. Report the median and p95 delta. GPU timer queries (`EXT_disjoint_timer_query_webgl2`), where available, give per-pass numbers.
- Measure at the default tier and at Ultra, at dpr 1 and 2, through `.local/bin/heavy.sh --perf`. It waits for free disk space and takes the whole browser pool, so no other browser run skews the timings. Capture runs (§5) use `--gpu`.
- **Starting caps,** proposed here until the game measures its own:
  - one layer: at most 0.25 ms;
  - one character's whole presence: at most 0.75 ms, and at most 25 % of the measured VFX headroom, whichever is lower, at the default tier at 1080p.
  Combat VFX peaks sit on top of presence, which spends headroom every frame. Write the game's adjusted numbers into its own doc.
- No allocation per frame. Check with the allocation timeline over 10 s of idle.

## 3. Measurements before judging

| Check | How | Pass |
|---|---|---|
| Glow class | Audit colour × intensity of each glow-class layer before tone mapping, or render the layer alone to a float target and read the maximum | At most 0.9 a channel; HDR only on layers marked core |
| Bloom spread | Width of a thin core with bloom on and off, at 1080p | At most 1.5× (starting cap). The old Last Line bloom widened shots 2.5–3.5× |
| White-out | Share of field pixels with luma of 0.95 or more, presence alone, play camera | At most 1 % |
| Protected zones | Presence on against off, inside the masks of the word strip, learning frame, telegraphs and HUD | At most 10 % added luminance |
| Word-tag contrast | p99 over an idle loop and an action | At least 7:1 |
| Silhouette | Edge contrast with presence on and off, on light and dark ground | Higher with presence on |
| First frame | Flashes at state changes, at age 0 | At least 95 % of peak |
| Frame time | §2 | Inside the caps and the game's frame gate |

## 4. Shared typing feedback

- The typing feedback (focus strip and letter effects) is a shared system with a bar of 9. Lowering the shared bloom once erased the typing marks (LESSONS §5).
- **When to re-run:**
  - a presence layer sits near the word strip, or where finished letters land (a core, a hand);
  - or the change touched bloom, tone mapping, exposure, the composer or kit code.
- **What to run:**
  - always: the game's in-play typing capture at the play camera, presence off against on, with the same seed and clock;
  - if kit code or global post changed: also the Lab scripts `tools/typing-feedback-lab/scripts/capture.mjs` (through `heavy.sh --gpu`) and `perf.mjs` (through `heavy.sh --perf`); their headers give the run lines.
  Compare the sheets side by side, and the numbers: contrast, key-to-frame time, 60 fps at 15 keys a second.
- Any visible change to the strip or the letters is a shared-system change: two judges at 9 or more, and the owner signs off (`docs/games/SHARED_SYSTEMS_BAR.md`). Otherwise revert its cause.

## 5. Capture matrix

- Each layer alone, then assembled.
- 1280×720 and 1920×1080.
- Play camera and close-up, plus the menu or intro pose if the character appears there.
- Light ground, dark ground, and the real map.
- The default tier and Ultra; Low once, to prove it still reads.
- **States:**
  - idle over one full breathing period, in 250 ms steps;
  - ready at each step;
  - action with the combat VFX on, in 16.7 ms steps around the release;
  - hit, victory, defeat.
- The reduced-motion version of each state.
- A short real-time clip (about 3 s) per state, for the owner.
- Label each sheet frame with frame number, ms, state and layer. Write a `meta.json` with renderer info and counters.
- **Where:** `games/<id>/tmp/presence/<date>/` (or the worktree's `tmp/`), never `art-src`, `public` or `docs`.
- **Cleanup:** keep the sheets and JSON, then prune your own raw frames. Run `node tools/capture-prune/prune.mjs <folder>` to list, then again with `--apply`.

## 6. Judging

- **The bar.** Owner, 01/11: "tôi không muốn dùng tạm được nữa, tôi muốn phải đạt trên 8.5 trở lên".
  - Two independent blind judges, both at 8.5 or more.
  - Judged in the built play host, at the player's settings, with no URL flags.
  - No provisional pass, no "best of three", no "better than before".
- **Blind:**
  - neutral labels (A, B, C), with the key kept outside the judges' folder;
  - judges do not read the report, the prompt or the brief;
  - each writes what they see before giving the score.
- **Against what:** compare with the board of commercial references, not with our previous round. Score market level and appeal (captivating, stylish, luxurious, modern). Plain fails, even when nothing is wrong (`docs/games/ART_ACCEPTANCE.md`).
- **At real size:** judge the assembled character at its play-camera height, plus a 2× crop for detail. A layer that works only in close-up counts only for close-up shots.
- **The lab's layer-alone check is a filter, not acceptance.**
- **Below 8.5:** fix exactly what both judges named. After two rounds without a real gain, change method in the same report: ready-made, licence-safe sources, another technique, or a search brief for the owner ([game-art-pipeline](../../game-art-pipeline/SKILL.md) step 8).
- **Owner:** for a subjective direction, show the owner options first and build only on the one he picks. A change to a shared system (typing feedback) needs his sign-off last.
- **ChatGPT as a second opinion,** under the browser rules of [game-art-pipeline](../../game-art-pipeline/SKILL.md) (Chat mode, thinking High, never Work):
  - ask for a link for each point;
  - open each source and mark each main claim correct, partly correct, or unsupported;
  - say where you disagree.
