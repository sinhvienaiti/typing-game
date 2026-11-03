# Recipes

These are starting points. The VFX production pipeline research in docs/games (VFX_PRODUCTION_PIPELINE, written 04/11/2026) refines them; when a run proves a better setting, write it here.

## 1. Firefly Video → flipbook

1. **Prompt** under 600 characters.
   - Ask for: a static camera; one effect, centred, filling 65–75 % of the frame; the transparent background option for normal-blended bodies; pure black for additive sparks and glints; the shape language and the colour steps.
   - Do not name games, studios or characters. Avoid "cinematic", "realistic", "volumetric", "lens flare", "bokeh" and "depth of field".
2. **Batch.** Make 3–5 takes per item at once; Firefly rate-limits, so wait and resume.
3. **Get the files out** through the local receiver (`.local/ff-bridge`, see the browser-tools recipe). Only move the files you made.
4. **Cut** with `tools/vfx-flipbook`: atlas (4×4 to 8×8, 256–512 px cells), JSON, contact sheet, metrics.
   - **Loops:** find the best loop window and cross-check the seam.
   - **Bands that tile in x:** check the left and right edges.
5. **Alpha.**
   - From a transparent clip: straight alpha, colour bled into clear texels.
   - From black: alpha = smoothstep(0.06, 0.22, max(R, G, B)), then premultiply.

## 2. Blender fire or smoke → flipbook (headless)

1. Write a script under the game's `art-src/lab/vfx/<element>/blender/` and run `Blender -b --python script.py` through `heavy.sh --cores=8`.
2. **Scene:** a Mantaflow domain (gas, fire + smoke), a flow object shaped to the effect, and forces for the shape.
   - For an impact: a directional force and a vortex for curved tongues.
   - For a band: wind along x, with the domain a long strip.
   - Start at a low resolution and raise it only where it shows.
3. **Shading:** a Principled Volume with emission from flame through a colour ramp with steps: white-gold core ≤ 5 %, amber, vermilion, dark wine edge. Density darkens the rim.
4. **Render:** EEVEE (fast) or Cycles (clean); film transparent; an orthographic or game-camera view; 24–60 frames; PNG RGBA. Optionally render a second pass for motion vectors so the runtime can blend frames.
5. **Atlas and preview:** the same as Firefly, step 4. Write a preview on black, on light stone and on dark stone.

## 3. Glint and twinkle sheets

- Firefly Video glint sheet on black, or one painted master star (thin long arms, tiny bright centre, soft halo) with 3 sizes and a short flash flipbook (on 1–2 frames, hold, shrink 3–5 frames).
- At runtime: clamp the size in screen pixels; only the centre is HDR.

## 4. Painted marks (cracks, scorch, seams)

- Paint 4–8 variants per set in one chat and one set standard, top-down on black.
- Pack the channels: R shape, G growth from the impact (for reveal and erosion), B hot lines (glow and cooling), A coverage.
- The shader reveals along G, glows on B, cools over time and erodes away. Rotate and scale the variants at random.

## 5. Smooth motion

- **Frames:** bursts need ≥ 24 frames; loops 32–64. Slowed playback needs frame blending (motion vectors, or a per-pixel switch between frames over the interval), never a lower visible frame rate.
- **Timing:** fast attack (peak on the first frame), a held peak, a slow burn-down by erosion and cooling.
- **Variety:** jitter rotation, scale and start frame, so repeated effects never look stamped.

## 6. Sound (SFX)

- Use Firefly sound effects (Adobe model) and layer the ingredients: transient, body, tail, sweetener.
- Use loudness tiers by power, a baked tail plus an in-game reverb send, and timing to the effect's frame.
- Combat sound is big and reverberant; only keys and light UI stay soft (game-art-pipeline audio §5).
