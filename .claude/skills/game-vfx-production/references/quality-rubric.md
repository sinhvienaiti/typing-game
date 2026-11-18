# Quality rubric: from 6 to 8.5

Score at the size the player sees (play camera and close), on light and dark ground, in motion at real speed, and beside official footage of Genshin Impact, Honkai: Star Rail, Wuthering Waves or Naraka. Judges write what they see before any score.

| Band | What it looks like |
|---|---|
| ≤ 5 | Code-drawn shapes: blobs, rings or stars that read as UI, a static glow, soft round "bubble" particles, a stain or ink splat, stepping or popping frames |
| 6 | Readable and correct colours, but generic and plain. One layer, little motion inside the shape, no sparkle, soft edges, no dark backing, the same every time |
| 7 | Real art, but one thing holds it back: the motion is a little stiff, the shape is generic, the sparkle is thin, the look is too pale on light ground, or the loop seam shows |
| 8.5 | Market level. Designed shape language (curves, hierarchy of big, medium and small), smooth graceful motion with life inside the shape, a crisp silhouette on a dark backing, a thin hot core, sparkle (glints, motes) that feels premium, colour steps, variety between repeats. It reads at 70 px and is rich at 500 px |
| 9+ | All of 8.5, plus a signature moment people would clip and share, and perfect timing with the sound and the hit |

Fail at once, whatever the other scores:
- the look is drawn by code;
- the real weapon or character is hidden;
- a reserved signal colour is used;
- the effect whites out the screen;
- there is a visible pop or stepping.

## Numbers before any judge

Run these at the play camera, with the same frames each time, before a judge sees anything (VFX_PRODUCTION_PIPELINE §3.2, §7; INTEGRATION_PLAN_2026-11-04 §2.8). They do not replace the judges; they catch regressions and the faults judges keep naming. Values marked TRIAL are first guesses, to be tuned against the judges.

| Check | How | Gate |
|---|---|---|
| First frame | Energy of the flash and the impact light on the hit's first drawn frame, over their own peak | ≥ 0.95 |
| Body reveal | The body appears in stroke order (root first, needle tips last) | full shape by frame 3, at full colour |
| Decay | Erosion along a painted survival order, with colour cooling; never a uniform fade | decay ≥ 3 × attack |
| Body left at the next blow | Lit body area at the age the next blow lands, over its peak | ≤ 15 % (TRIAL) |
| White-out | Pixels with luma ≥ 0.95 in the play field, every frame | ≤ 6 %; an ultimate ≤ 15 % for at most 3 frames |
| Contrast on both stones | OKLab ΔE of the final image against the same frame with that layer hidden, median over the layer's coverage, on light (#d6d0c2-like) and dark stone | body ≥ 0.12, accent ≥ 0.18 (TRIAL) |
| Edges and core | Pale share (alpha 0.05–0.5) of the lit area; white core share | pale < 15 %; core ≤ 5 % |
| Gaps | The grey version at 80–150 px | two gaps ≥ 3 px at 100 px |
| Frames | Source frames of a burst | 24 (low tier) to 48 (high tier) |
| Overlap | Translucent layers over one pixel round an object | ≤ 2 |
| Loops | Frame loops: R_seam; strips: the wrap step against the median inner step | ≤ 1.2, and nothing seen in 20 loops at 0.25× |

Measuring pitfalls (A1 baseline, 04/11/2026):
- **Screen passes occlude.** A screen-space impact patch (an inverted graphic burst held for 3 frames) hides every pool under it. Measure the pools' first frames with the screen passes bypassed, and the screen burst on its own.
- **Lights decay before the first draw.** A light set inside the update and decayed later in the same frame draws at 0.89 of its peak (e^(−7/60) at 60 Hz).
- **Damage numbers cover the effect.** They are drawn over the finished frame from about frame 8 after a hit. Mask pixels that are identical with the effect on and off before measuring the body.
- **Shared pools.** The caster's release effect often shares the impact's pool. Measure inside the hit's own region.
- **The frame-time method has limits.** Per-layer costs below about 0.7 ms do not separate from run-to-run noise with a CPU-plus-one-pixel-readback timer (the same variant moved by up to 1.6 ms between rounds). Alternate A/B/B/A over several rounds and trust only the full-set number.

Before calling anything done, answer in writing:
1. Which tool made the look, and why is it the most beautiful option?
2. What do the loved references do that this does not yet do?
3. Where is the sparkle?
4. Is the motion smooth at real speed and at 0.25×?
5. Would it stand next to the official footage?
