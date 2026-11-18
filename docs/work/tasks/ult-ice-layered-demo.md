# Ult ice layered demo (Hàn Thiên Quy Tịch rebuilt from layers)

Owner 15/11/2026: "Cho em xem thử 1 chiêu trước". He rejected whole-scene ult videos: they bake monsters and scenery (`ult-ice-cold-silence` has dozens of frozen beast statues), and the real foes and ground get no effect. Gemini analysis: `docs/games/tu-tien/source/gemini-video-vfx-approach-2026-11-15.md`. Audit: `typing-game-review/captures/tu-tien/clip-content-audit/` (17 bad clips).

## Goal
Rebuild **one** ultimate, Ice "Cold Heaven Returns to Silence", in the lab (`games/.wt-ic-lab-all`, key 8 item 12) **without** the `ult-ice-cold-silence` scene video. The new version sits beside the old one so the owner can toggle and compare (for example Shift+key or `?ultIce=layered`).

## Recipe (components only, reuse first)
Reuse the existing ice kit in `art-src/lab/vfx/ice/` (ice-charge, ice-caster-seal, ice-ground-impact, ice-ground-mark, ice-hit-affliction, ice-big-burst, ice-impact, ice-crescent-sym) and `element-kit.ts` (status rim "bind").
1. **Charge at the caster** (0–0.6 s): ice-charge plus ice-caster-seal under the caster, frost motes.
2. **Release:** a cold shock ring spreads from the caster across the field (a ground ring, a still rotated and scaled by code), with a light dip and a blue tint.
3. **Ground, real field:** a frost decal spreads behind the ring (ice-ground-mark tiled and staggered, crack decals), then melts over `linger`.
4. **On every real foe the ring reaches** (per-foe delay by distance): an ice shell over the model (a fresnel or ice material on a cloned mesh, or the bind rim plus ice-hit-affliction), a frozen pose (animation paused) for 3 s bind, frost puffs. At the end the shell shatters (ice-impact or ice-big-burst small, shards), and the damage number shows.
5. **Accent (one only):** a few tall crystal spikes from stills placed by code at foe clusters (count scales with foes), rising and then breaking. Support layers stay pale (one accent per effect).
6. Screen: a short white-blue flash on the strike, hit-stop, camera kick, the existing ice sound tiers.

## Must
- Works in all 4 views (Alt+1–4). No baked creatures or scenery anywhere.
- No new generated media unless a piece is truly missing. If so, list it and stop; do not generate.
- Measure frame time at 100 foes (stress scene) against the old version.
- Deliver to the parent session: a before/after clip (old video vs layered) at the top and behind views, 1280×720, under `typing-game-review/owner-review/2026-11-15/tu-tien/ult-ice-layered/` with an `ABOUT.md`, the lab key, and a SCORECARD row.
- Commit nothing, no media in Git, do not switch branches.

## Log
- 15/11 · Claude · v1 built in `games/.wt-ic-lab-all` (uncommitted): `src/lab/ice-ult-layered.ts` + wiring in `skills-main.ts` (key 8 item 12 casts it, Y toggles the old video, `?ultIce=video`, `__lab.iceUlt()`). Only the ice kit's 11 existing clips, no new media; on a 87-foe herd: 87 frozen and shattered with numbers, 66 frost seals inside the paving, 6 spikes. 100 foes (stress): both versions hold 60 fps, 0 frames over 33 ms. Clips and SCORECARD: `owner-review/2026-11-15/tu-tien/ult-ice-layered/`, `captures/tu-tien/ult-ice-layered/SCORECARD.md`. Weak points: the ice shell is the affliction card (frost), not an ice-encased model; the spikes read thin from the top.
