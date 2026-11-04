# Recipes

These are starting points. The VFX production pipeline research in docs/games (VFX_PRODUCTION_PIPELINE, written 04/11/2026) and the Tu Tien skills-lab integration plan (INTEGRATION_PLAN_2026-11-04) refine them; when a run proves a better setting, write it here.

## 1. Firefly Video → flipbook

1. **Decide the clip's role before generating.**

   | The clip | Its role |
   |---|---|
   | Beautiful at play size, loops or dies correctly, follows the action | **The final asset.** Keep it as it is; fix only visible faults |
   | Lovely motion inside, generic shape | Source of the inner motion; the shape comes from a painting |
   | Wrong at the root (a symmetric lotus, a closed ring) | Reject, or keep as a reference only |
   | Fire that must cling to a blade | A texture on a blade-hugging mesh, or an x-seamless strip (§2) |
   | A seal that needs exact strokes | No video: a painted image, SDF only when it measures better |
   | A creature that must keep its anatomy | Only a secondary fire texture |

   Firefly Video is good at continuous flow (trails, energy bands, rising auras) and weak at a one-off radial burst: its clips last 5 s with no 0.3 s pop.
2. **Prompt** under 600 characters.
   - Ask for: a static camera; one effect, centred, filling 65–75 % of the frame; pure black for additive sparks and glints; the shape language as geometry (how many strokes, where they curve, where the gaps are) and the colour steps.
   - Do not name games, studios or characters. Avoid "cinematic", "realistic", "volumetric", "lens flare", "bokeh" and "depth of field".
3. **Give it the shape as a first frame when the shape matters** (image-to-video).
   - Paint the first frame (ChatGPT, then Gemini; or reshape a frame of a liked Firefly clip), and a last frame when the dying shape matters.
   - Make it **opaque pure black, 1:1, 1080p, transparency off.**
   - Why not transparent:
     - the transparent mode runs only at 540p, 16:9;
     - a 1080p run with transparency on died silently after about 9 minutes (04/11/2026);
     - two Adobe help pages disagree on transparent first frames.
   - The opaque route is proven: `ff-a1-c5` kept a three-stroke brush shape with soft, living fire. It was the best fire body of that night (6.5 from both blind judges); the faults were in the drawn frame, not in the route.
   - Feed the frame through `firefly-upload-with-crop#upload` (game-art-pipeline browser tools).
4. **Batch.** Make 3–5 takes per item at once; Firefly rate-limits, so wait and resume.
5. **Get the files out** through the local receiver (`.local/ff-bridge`, see the browser-tools recipe). Only move the files you made.
6. **Cut** with `tools/vfx-flipbook`: atlas (4×4 to 8×8, 256–512 px cells), JSON, contact sheet, metrics.
   - Cut at the clip's native 24 fps. Keep 24 frames for the low tier and 48 for the high tier, never 14–16.
   - Keep the impact origin fixed; never centre on the brightest blob. Leave 4–8 px of clear border in every cell.
   - **Slowed playback:** run `minterpolate` on the RGBA frames before packing, then re-threshold alpha. Never interpolate the colour and alpha videos separately.
7. **Alpha.**
   - From a transparent clip: straight alpha, colour bled into clear texels.
   - From black: alpha = smoothstep(0.06, 0.22, max(R, G, B)), then premultiply. Black is not real alpha for soft bodies; let the shader's ink and coverage masks do that job.
8. **Loops.**
   - **Never crossfade the end of a clip into its start.** On 04/11/2026 an 8-frame wrap blend doubled the flames (ghosting) and flashed marks from another part of the clip inside a ring every loop. Both blind judges caught it.
   - A frame loop is allowed only when R_seam = D(last, first) / median D(consecutive frames) ≤ 1.2. Play it stepped or as hold-and-erode, and watch 20 loops at real speed and at 0.25×. Otherwise play once.
   - A band along a blade does not loop in time at all: it is an x-seamless strip that scrolls (§2). The silhouette stays fixed in blade space and only the inside moves.
9. **Upscaling.**
   - **Never upscale video.** Firefly's video upscaler is Topaz, a partner model (adobe.com/products/firefly/partner-models/topaz.html).
   - **Images:** use the Firefly Upscaler, Adobe's own model (picker value `adobe:firefly:colligo:clio:v4:upscaler`).
     - The same picker lists Topaz Bloom and Topaz Gigapixel: never pick them.
     - The output is capped at 6144 px a side ("Output too large"). For a 2× upscale of a larger image, scale the input to ≤ 3072 px first, then bring the result back to the target size.
     - Afterwards, check the face or shape: shift (phase correlation, should be 0 px), skin or body ΔE2000, and sharpness.
   - A 256 px cell shown at 80 px needs no upscale.

## 2. Motion strips that tile in x (a band along a blade, a trail)

1. **Source:** a clip whose inside flows along the band (streaks, flame tongues). Straighten one frame into a 512×128 (or 1024×128) band.
   - **A cone** (streaks converging on an apex): map it to `u = ln(x − x_apex)`, `v = (y − y_c)/(x − x_apex)`. The cone becomes a band of constant height, and its zoom toward the apex becomes a constant scroll.
   - **Keep one period short.** The texture's scale should change by no more than about 1.5× across it. On a long period the texture drifts (crisp lines at one end, haze at the other) and the wrap shows as a density front.
2. **The wrap.**
   - Take the period plus an overlap from the clip's own continuation.
   - Cut through the overlap along a minimal-error vertical path. Compute the cost on the square root of the encoded values, so faint haze counts too.
   - Feather 1 px along the cut. Use 3–10 px for streaks that run along x, so their ends do not line up on the cut.
   - **Never blend whole columns or frames.**
   - Pick among the best candidates by the final seam numbers, then by eye.
3. **Check.**
   - Wrap step ≤ 1.2 × the median inner step: one column, then 4-column blocks on square-root values, and the faint outer rows on their own.
   - Tile the strip 3× and scroll 20 periods at real speed and at 0.25×.
   - A pure scroll cannot jump between loops. The eye check is for the wrap line and for one striking element that repeats every period (the "wallpaper" look); two samples at two speeds in the shader soften that.
4. **Strongly structured textures** (feather plates, scales) keep a visible break at the wrap even when the numbers pass. Use them as fixed cards, not scrolling strips.
5. **Output.**
   - Fade only the outer few rows, since v clamps in the shader.
   - Store rgb on black plus a straight-alpha copy.
   - Write the scroll speed and the natural aspect in the JSON, so the shader's repeat `k` can undo any stretch. The speed is in periods per second: from the clip's measured flow, or the shader's own when the clip does not drift.
   - Shader side: `u' = fract(k·u − v·t + φ)` with `RepeatWrapping` in u and `ClampToEdgeWrapping` in v; a phase φ per object; the flow always runs backward.
6. **Script:** `games/immortality-cultivation/art-src/lab/vfx/aura/strips/source/a7_strip.py`.

## 3. Blender fire or smoke → flipbook (headless)

1. **What Blender is for.**
   - Use Blender for data: heat, coverage and motion vectors.
   - Use it for shapes a simulation really makes (smoke, rising fire, bands).
   - Do not use it as the painter of a designed brush shape: on 04/11/2026 the stepped-ramp Mantaflow impacts scored 3.5–4.5 from blind judges (round blobs, sticker edges). Paint the shape and let Firefly Video or the shader move it.
2. **Script and run.** Write a script under the game's `art-src/lab/vfx/<element>/blender/` and run `Blender -b --python script.py` through `heavy.sh --cores=8`.
3. **Scene:** a Mantaflow domain (gas, fire + smoke), a flow object shaped to the effect, and forces for the shape.
   - For an impact: a directional force and a vortex for curved tongues.
   - For a band: wind along x, with the domain a long strip.
   - Start at a low resolution and raise it only where it shows.
4. **Render data, not final colour.**
   - Heat: emission only. Coverage: absorption only. Make them two passes; one pass with both let the absorption eat the emission.
   - Use EXR, or PNG with the view transform Raw (AgX compresses the highlights).
   - Colour comes from the shader's stepped ramp.
5. **Motion vectors only from Cycles.** EEVEE returns 0 for the `velocity` attribute. Vectors pay off only where the fire really travels.
6. **Atlas and preview:** the same as Firefly, §1 step 6. Write a preview on black, on light stone and on dark stone.

## 4. Ink, body and core in one fragment (the shader contract)

Draw the dark backing, the body and the hot core in the same fragment, as a three-layer "over" with premultiplied blending `ONE, ONE_MINUS_SRC_ALPHA`. There is no extra backing layer, so it does not add to the overlap count.

```
α   = 1 − (1 − a_ink)(1 − a_body)(1 − a_core)
RGB = C_ink·a_ink·(1 − a_body)(1 − a_core) + C_body·a_body·(1 − a_core) + C_core·a_core
```

- **Caps.**
  - Body ≤ 0.85–0.9 a channel.
  - The HDR core only on hot lines, ≤ 5 % of the lit area.
  - Ink alpha 0.35 (Metal) to 0.45–0.7 (Fire), broken 20–35 %. Put it only on the inner rim, under stroke roots and inside curves; leave the outer 35–50 % of each tongue without ink, or it reads as a sticker edge.
- **Masks.**
  - Store colour atlases with straight alpha and premultiply once in the shader.
  - Control masks are data (`NoColorSpace`): coverage, ink, hot lines and survival order in RGBA; reveal order and motion influence at half resolution.
  - Derive the reveal and survival orders from the painted strokes (distance along each stroke from its root), never draw shapes in code.
- **Check:** compare the GPU result with a CPU version on test patches (empty, partly covered, fully covered), on light and on dark stone, to ±1/255. HDR above 1.0 reaches the bloom only on a float composer target (three.js r170 `EffectComposer` uses HalfFloat).

## 5. Glint and twinkle sheets

- Firefly Video glint sheet on black, or one painted master star (thin long arms, tiny bright centre, soft halo) with 3 sizes and a short flash flipbook (on 1–2 frames, hold, shrink 3–5 frames).
- At runtime: clamp the size in screen pixels; only the centre is HDR.

## 6. Painted marks (cracks, scorch, seams)

- Paint 4–8 variants per set in one chat and one set standard, top-down on black.
- Pack the channels: R shape, G growth from the impact (for reveal and erosion), B hot lines (glow and cooling), A coverage.
- The shader reveals along G, glows on B, cools over time and erodes away. Rotate and scale the variants at random.

## 7. Smooth motion

- **Frames:** bursts need ≥ 24 frames; loops 32–64. Slowed playback needs frame blending (motion vectors, or a per-pixel switch between frames over the interval), never a lower visible frame rate.
- **Timing:**
  - Fast attack: the flash and the impact light at ≥ 95 % of their own peak on the first drawn frame.
  - The body appears in stroke order over 2–4 frames, at full colour, never fading up.
  - A held peak, then a slow burn-down by erosion and cooling: the decay lasts at least three times the attack.
  - A light set during the update and decayed in the same frame shows less than its peak on its first frame; start the decay on the next frame.
- **Variety:** jitter rotation, scale and start frame, so repeated effects never look stamped.

## 8. Sound (SFX)

- Use Firefly sound effects (Adobe model) and layer the ingredients: transient, body, tail, sweetener.
- Use loudness tiers by power, a baked tail plus an in-game reverb send, and timing to the effect's frame.
- Combat sound is big and reverberant; only keys and light UI stay soft (game-art-pipeline audio §5).
