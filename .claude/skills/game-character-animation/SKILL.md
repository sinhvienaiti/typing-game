---
name: game-character-animation
description: "Build or review character animation in any game of this repo (Dragonhold, Wordwoven, Last Line, Tu Tien and later games; three.js): rig profiles and canonical bone names, clip sources and retargeting, the clip and event contract, the state machine with inertialized transitions, the typed wind-up and release, procedural layers (acting, lean, recoil, breathing, look-at), foot locking with two-bone IK, secondary springs on tails, ears, capes and hair, contact and release events that the body, VFX, sound, camera and hit-stop answer on one frame, the motion lab and probe, and judging motion. Use when a hero, companion, dragon, foe or crowd moves stiffly, snaps, slides, floats or pops to the bind pose; before adding a clip source, an animation library or a retarget step; and when timing a skill's body against its effects. Shared system, bar 9. Not for designing the character or its sources (game-character-design), combat VFX (game-vfx-layered) or always-on glow (game-hero-presence-vfx)."
---

# Character animation

Character animation is a shared system: every game reuses it, so it passes only when two independent blind judges both score 9 or more with no category under 8.5, and the owner signs off last ([SHARED_SYSTEMS_BAR.md](../../../docs/games/SHARED_SYSTEMS_BAR.md) §2–4). Owner, 02/11/2026: every gesture, every motion of the limbs, body and head must be smooth.

**Sources, in this order:**
- **Working code:** Tu Tien's motion lab, `games/immortality-cultivation/src/lab/anim/` (the Animator and its layers) and `games/immortality-cultivation/src/lab/motion-probe.ts`. The file headers give the reasons and the numbers. The code moves into a kit `anim/` module later (CHARACTER_ANIMATION §6 P1) and reaches games through `kit:sync`; before that, a game that copies it follows its own AGENTS.md rule for copied code.
- **Design:** [CHARACTER_ANIMATION.md](../../../docs/games/CHARACTER_ANIMATION.md) §5 (tiers, library choices, clip pipeline and contract, state table, procedural layers, crowds, events, tier budgets, lab, judging). The lab's plan and judge rounds: [MOTION_PLAN.md](../../../docs/games/tu-tien/MOTION_PLAN.md).
- **Each game's own docs** keep its clips, numbers and schedule, and win over this skill for that game.

**References:**
- [Runtime layers](references/runtime-layers.md): frame order, half-lives, acting, foot lock, springs, tier budgets.
- [Rig and retarget](references/rig-and-retarget.md): rig profile, clip sources and licences, retargeting, the retarget test matrix.
- [Events and sync](references/events-and-sync.md): one event, every listener on the same frame.
- [Probe and judging](references/probe-and-judging.md): the probe's gates, captures, blind judging.

## Procedure

1. **Official three.js first.** Start from `AnimationMixer`, `AnimationAction`, `AnimationUtils.makeClipAdditive` and `SkeletonUtils` (`clone`, `retargetClip`). Write our own code only when a measurement shows a gap, and write the reason in the game's doc.
   - Example: the lab samples clips itself (`ClipSampler` in `rig.ts`) because three's `PropertyMixer` writes a bone only when its mixed value changed, so constant tracks and a paused clip left last frame's IK and layers in the bones.
   - The split games' `tests/boundary.test.ts` allow only `three`, `three/examples/jsm` and `@fontsource` (Wordwoven and Last Line add `a11y-dialog`). Any other package needs a kit and boundary change the owner decides. That is why the lab has its own springs.
2. **A rig profile with canonical bone names.** Code reads canonical names only; each rig ships a map from its own names, its front axis and its sockets ([rig and retarget](references/rig-and-retarget.md) §1).
3. **Retarget in armature space,** never by copying local rotations: rests and bone rolls differ between sources and our models. Resample to 60 fps at load, then run the clip through the probe.
4. **A clip and event contract** per family (CHARACTER_ANIMATION §5.4). A strike is one clip with `windup_end` and `release` markers, not separate clips. Clip metadata travels in the GLB extras.
5. **A state machine with inertialization** (CHARACTER_ANIMATION §5.5, `inertial.ts`). On a switch the new clip takes over at once, and the per-bone difference decays on a critically damped spring. One clip is evaluated, and nothing passes through the bind pose. Half-lives per transition are in [runtime layers](references/runtime-layers.md) §2.
6. **The wind-up follows the typing; the release comes ≤ 50 ms after the last key.**
   - While a word is typed, clip time = progress × (release − lead). On the last key the clip runs on from just before `release` at swing speed.
   - Never hold the shot for a clip, and never let a hit-stop hold it: a new release cuts a stop still holding (`games/immortality-cultivation/src/lab/feel.ts`).
   - Foes hold at `windup_end` until the sim's strike event, and never release before the sim.
   - Acting is its own layer (`acting.ts`): anticipation with the typing, a decisive release, a hold, overshoot and settle, then recovery. Poses are bold enough to read when the character is 30–70 px tall at the play camera.
7. **Procedural layers in a fixed frame order** ([runtime layers](references/runtime-layers.md) §1). Every layer is a spring written by half-life, so it is frame-rate independent and blends with whatever interrupts it. Nothing allocates per frame.
8. **Foot lock with two-bone IK** (`foot-ik.ts`): a planted foot stays where it touched while the body moves, turns, leans or crouches. It pivots on the heel, then the ball; the reach is soft; the foot steps when drift or twist grows too large; no foot is solved under the ground.
9. **Secondary motion with our own springs** (`springs.ts`): tails, ears, bags, capes, hair and ribbons on bones. Fixed 60 Hz steps drawn between the last two, tips in the character root's space, cone and turn-rate limits, sphere and capsule colliders. Light ribbons that are not on bones belong to game-hero-presence-vfx.
10. **One event, one frame.** One sim tick emits the release, contact or hit. The body, every VFX layer, the sound, the camera kick and the hit-stop answer it on that frame, with no `setTimeout`. The sim owns damage, hits and deaths; animation never delays or moves a sim event, and clip markers only drive view reactions ([events and sync](references/events-and-sync.md)).
11. **A lab plus the motion probe.** A dev-only lab page with the game's renderer, play camera and real models; a fixed-step clock; a trigger per state and per skill; the probe sampling what was drawn. Prove with a grep of `dist` that the lab never ships. Run the capture scenario after each change ([probe and judging](references/probe-and-judging.md)).
12. **Judge, demo at 7, pass at 9.**
   - Two blind judges, not from the animation lane, score the eight categories before reading any metric, beside commercial references, in the built play host at the player's settings with no URL flags. The bar is both ≥ 9, no category under 8.5.
   - When both judges reach 7 in every category, send the owner a movement demo with what is done and what still blocks 8.5, and keep going.
   - Metrics go with the scores and never replace them. Tu Tien round 1 brought bind-pose frames, layer pops and key-to-release inside the gates and still scored 5.4 and 5.4: the motion was smooth but had no acting.
13. **Three tries, then discuss** (owner, 02/11): after three reworks without a clear gain in the judges' scores, stop. Work out a different approach with ChatGPT (show it the clips or sheets, the judges' notes and what was tried) before the fourth try.

## Boundaries

- Designing the character, its sources and which parts are geometry or VFX: [game-character-design](../game-character-design/SKILL.md).
- Shots, skills, impacts and their five phases: [game-vfx-layered](../game-vfx-layered/SKILL.md). This skill owns the body's timing they sync to.
- Always-on glow, halos and motes: [game-hero-presence-vfx](../game-hero-presence-vfx/SKILL.md).
- Model import, face floors and maps: `docs/games/MODEL_QUALITY.md`. Tripo: [game-art-pipeline tripo](../game-art-pipeline/references/tripo.md).
- In Space Typing, its contracts and [game-asset-2d-to-3d](../game-asset-2d-to-3d/SKILL.md) come first; this skill is reference there.
- Captures go to the owner's review folder, `typing-game-review/captures/<game>/<topic>/`, beside the source, with an `ABOUT.md` (AGENTS.md "Test captures", 04/11/2026). A game's `tmp/shots` may link there. Prune your own raw frames with `node tools/capture-prune/prune.mjs <folder> --apply` once the sheets and numbers exist.

Techniques beyond this repo (Claude reads these directly): `~/.agents/skills/threejs-gameplay-systems/references/game-feel.md`.
