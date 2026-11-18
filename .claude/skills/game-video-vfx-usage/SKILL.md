---
name: game-video-vfx-usage
description: "Decide where generated video (Adobe Firefly image-to-video, or any pre-rendered clip) may be used in any game of this repo, and how: the four-tier table (SHOULD, OPTIONAL, AVOID, NEVER) per game part, the salvage rule for existing clips, and the source QA gate a clip must pass before it becomes a flipbook or a game asset. Use before generating, picking, cutting, wiring or reviewing any video for VFX, cut-ins, menus, loading, transitions, map ambience, UI glow, auras or deaths; whenever a skill is planned as one video; and whenever a clip shows stray creatures, scenery or a fixed angle. game-vfx-production picks the tool; this skill limits what video is for."
---

# Video in the game: where, how, and the source gate

Sources: [Gemini analysis 15/11/2026](../../../docs/games/tu-tien/source/gemini-video-vfx-approach-2026-11-15.md) (two rounds, each passed twice, sources spot-checked) and our own audit of 49 lab clips on 15/11: 10 had creatures baked in, 7 had ground or scenery baked in.

The owner, 15/11: "bạn đang quá lạm dụng video, khiến nó đang làm việc không có chút hiệu quả nào". This applies the 12/11 rule "components first" ([AGENTS.md](../../../AGENTS.md)) to video.

## The core fact

Code integration fixes only what happens **around** a clip:
- foe hit flash, freeze and burn;
- ground decals and light;
- hit-stop, shake and sound.

It cannot fix what is baked **inside** the pixels:
- creatures or scenery;
- one fixed camera angle against our 4 views;
- a flat card with no parallax;
- no occlusion with foes standing inside the effect;
- blur when scaled.

A whole-scene video on a camera-facing card stays fake however well it is wired.

## Procedure

1. **Name the game part** and look it up in the tier table below.
   - NEVER means no video, full stop.
   - AVOID needs a written reason in the brief.
2. **For world-space use, plan the effect as layers first** (`game-vfx-layered`):
   - per-foe effect;
   - ground decal;
   - mesh with shader;
   - particles;
   - light, shake, hit-stop and sound.
   Video may supply **one** component of that recipe, never the composed skill.
3. **Before generating, check the energy itself is a video job.** Consider the other routes first:
   - shaders with scrolling noise for slashes, beams, qi and water flows;
   - Blender sims rendered to flipbooks, which give true alpha and can be rendered side and top from one sim;
   - stills rotated and scaled by code for rings, seals and ground marks.
   Firefly wins only on painterly motion for screen-space work and single amorphous puffs.
4. **Generate to the source rules** below: image-to-video from an approved still, Firefly Video model only.
5. **Pass the source QA gate** before any flipbook cut. Record the result next to the clip in the manifest (`contentCheck: pass` with the checker and the date). A clip with no recorded pass is never wired.
6. **Wire it by the "how" column**, then judge the composed effect in the built host in all 4 views (the 8.5 bar).

## Tier table

| Game part | Tier | How |
| --- | --- | --- |
| Cut-ins, cinematics | SHOULD | Screen-space video, one layer, 720p–1080p at 24–30 fps, a DOM `<video>` or one VideoTexture. A full painted composition is allowed (the 8.5 bar still applies). |
| Title and menu backgrounds | SHOULD | A DOM `<video>` behind the canvas, a seamless loop, opaque. |
| Loading screens | SHOULD | A DOM `<video>` loop, so it keeps playing while shaders compile. Small file. |
| Screen transitions | SHOULD | Screen-space luma wipe or flipbook; frame 1 black, the peak covers the screen. |
| Ultimates | SHOULD for the cut-in part; NEVER as one world card | The world part is built from a mesh dome or pillar, a ground decal, 8–16 single-puff flipbook cards and per-foe hits. |
| Skill impact (secondary bursts) | OPTIONAL | Flipbook, 1–3 small cards per struck foe, capped about 32–48 live; 4x4 atlas, KTX2; additive for energy, premultiplied for smoke, ink and water; height fade at the ground. |
| Skill release at the caster | OPTIONAL | A shader flare is preferred; otherwise 1–2 flipbook cards at the cast point, no hands or weapons baked in. |
| Foe deaths | OPTIONAL | A dissolve shader on the foe, plus one shared instanced puff card per death. |
| Map ambience: waterfalls, caustics | OPTIONAL | A looping tileable atlas mapped on the water or waterfall mesh UVs, not floating cards. |
| Map ambience: fog, clouds | AVOID | Scrolling noise on meshes or planes. |
| UI frame and icon glow | OPTIONAL for a one-off flare; AVOID for many icons at once | One shared sprite sheet or a border shader; never many videos at once. |
| Skill charge (typing-sustained) | AVOID | Its length follows typing speed: a rune quad plus inward particles plus a Fresnel cylinder. |
| Skill aftermath | AVOID | An eroding decal plus a few particles (overdraw). |
| Item and equipment auras | AVOID | A mesh shell or a scrolling ribbon on the model (`game-hero-presence-vfx`). |
| Character presence | AVOID | Ribbons, rotated stills and shaders (`game-hero-presence-vfx`). |
| Skill travel (swords, slashes, bolts, beams) | NEVER | A mesh with a trail ribbon; a card cannot bend along a path or foreshorten. |
| Ground decals (cracks, scorch, rings, arrays) | NEVER video | A still on a flat XZ quad or decal, animated by a shader. A Firefly **Image** still from a top-down (90°) view is fine. |

## Salvage rule for existing clips

A clip may stay in world space, cut to a flipbook, only if it meets all five conditions:
1. one amorphous material;
2. on pure black;
3. no solid objects or scenery;
4. radial or single-axis symmetry;
5. spawned as several small cards so foes stand between them.

Two kinds of clip may also stay with an orientation lock:
- an axis beam, on a ribbon or crossed planes;
- a flat ring, on an XZ plane.

Everything else is rebuilt:
- summoned creatures and objects at a fixed angle;
- baked ground or scenery;
- whole-scene ultimates.

A rebuilt clip may live on only as a cut-in, if it reaches 8.5 there.

## Source rules (Firefly)

- **Material:** one clip holds one material (only fire, or only lightning, or only smoke, or only a splash). No monster, sword, rock, gate, floor, sky or horizon.
- **Background:** pure black, or Firefly's transparent-background option (Firefly Video model, verified 15/11). After export, crush levels to black (luma under 0.05 becomes 0).
- **Framing:** the effect sits in the centre 80 %. The outer 8 % stays black in every frame; enforce it with a vignette at atlas time.
- **Timing:** a one-shot starts and ends black (use a black end frame). A loop uses the same start and end still, or a 12-frame cross-fade.
- **Angle:**
  - world cards: radially symmetric, or straight front or straight top (90°);
  - never a 25–45° three-quarter view for anything placed in the 4-camera scene;
  - screen-space clips are exempt.
- **Reference and model:** start from an approved still, with the reference path written in the prompt file. Adobe models only.

## Source QA gate (before any flipbook or wiring)

1. **Content.** Look at a frame sheet, at least 8 frames, zoomed. Record each:
   - creatures, figures or silhouettes, dark ones on dark ground included;
   - scenery: tiles, rocks, gates, trees, sky, horizon;
   - whether it is a whole scene.
   Any yes fails it, except the intended summoned subject of a cut-in.
   **Who checks:** two independent checks (two fresh agents, or one agent and the owner). This is a pass/fail fitness check, not an art score.
2. **Background:** a script checks that luminance at the corners and the outer 8 % is ≤ 0.015.
3. **Margins:** a script checks that no pixel above RGB 12 touches the outer 5 % in any frame.
4. **Envelope:** a one-shot starts and ends near zero energy, or a loop has a clean seam.
5. **Angle:** matches the angle rule for its use.
6. **Lab test:** the clip is placed by its "how" row in the lab, viewed in all 4 views with foes inside the effect, and the owner signs off.

Never regenerate a source layer only because it does not reach 8 on its own. The composed effect is what gets scored (AGENTS.md, judging VFX in two tiers).
