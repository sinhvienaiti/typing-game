# Rig profile, clip sources and retargeting

## 1. Rig profile

- **Canonical names.** Code reads only the canonical bone names: the UE-mannequin set that Mesh2Motion's human rig and Lam share (`pelvis`, `spine_01`–`spine_03`, `neck_01`, `head`, `clavicle`, `upperarm`, `lowerarm`, `hand`, `thigh`, `calf`, `foot`, `ball`, each with `_l` or `_r`), plus extras by name (`tail_01`…, `ear_l`, `bag_r`). The Animator knows clip keys and bone names only, so a later hero with the same names reuses it (`games/immortality-cultivation/src/lab/anim/rig.ts`).
- **Each rig ships a map** from its own bone names to the canonical ones, with:
  - its front axis (Lam faces −z, so the root's yaw is the facing + π);
  - its sockets (`FX_HAND_R`, `FX_FOOT_L`, `FX_MOUTH`…) for VFX and events;
  - masks as lists of canonical names (the upper-body bones of a hit additive).
  Leg length and standing heights are measured at load, not typed in.
- **The kit form** is `anim/profiles.ts` (CHARACTER_ANIMATION §6 P1). Until it exists, keep the map next to the game's Animator and list the copy in the game's sync-debt doc.

## 2. Rigging a model

- **Not Tripo's auto rig.** Measured 24/10 on Lam: 14,071 of 14,132 vertices were bound rigidly to `Hips` (CHARACTER_ANIMATION §5.3).
- **Rig in Blender** on the Mesh2Motion bone families (human, fox, horse, spider, bird, snake, dragon, kaiju), with extra bones for tails, capes, wings and banners, using Wordwoven's `games/typing-defense/scripts/models/blender/td_rig_*.py` (survey, tools, post, attach, review, compare).
- **Keep the model's detail.** Rig on the original mesh for Ultra, then reduce for the lower tiers with the same bone indices (`docs/games/MODEL_QUALITY.md` §2, §2b).

## 3. Clip sources and licences

Check every licence on its own page and record it in `docs/games/THIRD_PARTY.md` ([game-art-pipeline licences](../../game-art-pipeline/references/licences.md)).

| Source | Use | Terms |
|---|---|---|
| **Mesh2Motion** | First choice: rigs and clips per family; walk, strafes and back step already in the Tu Tien lab | CC0 assets, MIT app code. Skip `human-mocap-animations.glb` and `CarnegieMellonAnimations/` (CMU data, licence not checked) |
| **Quaternius Universal Animation Library 1 and 2, Standard** | 8-way locomotion, melee combos split per strike, hits, deaths, emotes | Treat as Quaternius Asset License v1.0 (QAL): the pack page says CC0, the licence page says QAL, and the stricter page wins. Commercial use, no credit, no redistribution as a pack. Record the download date and the QAL text word for word |
| **KayKit** character animations | Fallback only, for crowd clips the two above lack | CC0, but built for KayKit rigs (its page warns they may not look good on other humanoids), and the toy look rules out its models |
| **Mixamo** | Never | Adobe's terms could not be verified, and the raw files would ship in a public web build |

## 4. Retargeting (`retarget.ts`, `resample.ts`)

- **Work in armature space.** Rests and bone rolls differ: Mesh2Motion rests in a T-pose and Lam in an A-pose, and thigh and foot axes differ by up to 178°. So local rotations are never copied.
  - Per bone, first turn the source rest so the bone points where the target's bone points at rest.
  - Apply the source's world rotation relative to that aligned rest to the target's rest.
  - Bring local rotations back through the target's parents.
  - Scale the pelvis offset by the hip-height ratio. Bones the source lacks take a fill pose (the target's Idle frame 0).
- **Try three's `SkeletonUtils.retargetClip` first** on a new pair of rigs, and keep it when the probe and the matrix below pass.
- **Resample to 60 fps at load,** in memory: quaternions by squad, positions by Catmull-Rom, constant and STEP tracks kept as they are. The GLB is not changed.
- **Analyse at load:** ground speed, stride and contact phase of each gait; release, wind-up and swing ends of each strike.
- **A clip that fails on a character is not used there.** Mesh2Motion's `Jog` put Lam's feet 5.6 cm into the ground, so the lab does not use it.

## 5. The retarget test matrix

Required when the retarget code changes or a clip source is added.

- **3 characters × 10 clips.** Pick three targets that differ in proportion and rest pose (a short-legged stylised hero like Lam among them). Pick clips that cover idle, walk, run, a strafe, a turn, a strike with a release, a cast with the arms raised, a hit, a death and a dash or jump.
- **Per cell, the probe's gates** ([probe and judging](probe-and-judging.md) §1): foot slide, ground penetration, loop seam, transition ratio, near-bind frames, and the arms-out check.
- **Per cell, four retarget checks:**
  - **wrist:** hand orientation against the source, and no candy-wrapper twist at the wrist;
  - **shoulder:** clavicle and upper-arm angles against the source, with no shrug or arm sunk into the torso;
  - **twist:** forearm and upper-arm roll, with no flips between frames;
  - **hip drift:** the pelvis path against the source's, scaled by hip height, and no creep over a loop.
- **No numeric limits for the four checks yet.** Record their values per cell, judge the worst cells on frame sheets, and write the limits into CHARACTER_ANIMATION after the first full run.
- A sheet per character (one row per clip at the play camera and a close-up) goes to the blind judges without numbers.
