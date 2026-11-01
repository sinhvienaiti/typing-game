---
name: game-hero-presence-vfx
description: "Build or review the always-on presence of a character in any game of this repo (Dragonhold, Wordwoven, Last Line, Tu Tien and later games; three.js or 2D canvas): rim glow, emissive channels, halos and light rings, orbiting motes, light ribbons, aura pulses, ground glow, a character light, and how they change in idle, ready, action, hit, victory and defeat. Use when a hero, companion, drone, dragon, elite or boss should look radiant, divine or premium, or reads as plain, flat or lost on the map; for the runtime side of the radiance kit; and before adding glow, bloom, tone mapping or exposure changes to make a character shine. Not for designing the character, its source images or the geometry-or-VFX split (game-character-design), combat shots, skills and impacts (game-vfx-layered), or capes and hair on bones (character animation)."
---

# Hero presence VFX

Presence is the set of layers that make a character feel radiant while nothing is being cast. Unlike a shot, it is on screen every frame: its cost never goes away, and every mistake (a washed screen, a hidden word tag, a glow in a reserved colour) stays in view the whole game. Build it as separate, switchable layers, judge each alone, then judge the whole at the size the player sees.

This skill holds the reusable method and recipes. A recipe verified in any game is recorded in [recipes](references/recipes.md) §4, not in a docs file. Each game's docs keep its measured numbers and decisions, which win over this skill's starting caps for that game:
- [docs/games/VFX_STANDARD.md](../../../docs/games/VFX_STANDARD.md): §3.5 bloom and colour, §3.6 readability, §3.7 budgets, §3.8 reduced motion, §4.5 lab and captures.
- [docs/games/LESSONS_FROM_THREE_GAMES.md](../../../docs/games/LESSONS_FROM_THREE_GAMES.md): §5 (bloom, typing marks) and §11 (character design, the radiance kit).
- `docs/games/MODEL_QUALITY.md` (keep the model's maps), `docs/games/SHARED_SYSTEMS_BAR.md` (bar 9), `docs/games/ART_ACCEPTANCE.md` (appeal).
- Which kit parts are geometry and which are VFX: the [pipeline decision](../game-character-design/references/pipeline-decision.md) of game-character-design.

**The bloom rule** (LESSONS §5, from the Last Line rescue of 01/11): only thin HDR cores (3–6) bloom; halos, haze and soft glows stay at or under 0.9 a channel. Those two values are the layer's job. Strength 0.4–0.5, radius 0.1–0.15, Neutral or AgX tone mapping (not ACES) and MSAA on High and Ultra are the game's post settings; a presence task never retunes them. Where a game's post still differs, build to the rule and report the gap. Presence must also read on every tier that ships without bloom.

## Procedure

1. **Read the game as it is.** The branch its play host builds; its renderer (three version, WebGL2 GLSL or WebGPU, or 2D canvas; tone mapping, exposure, bloom and MSAA per tier); play camera; motion setting; reserved signal colours; and the sockets in its model contracts (the kit copy in the game's `src/kit/three/model-contracts.ts`, plus any contract of the game's own). Current source beats plans and the examples in this skill.
2. **Research, then split.** Which parts belong to the model or its textures (armour channels in the emissive map, a crown, a halo ring, the cape mesh) and which are runtime layers comes from the researched [pipeline decision](../game-character-design/references/pipeline-decision.md). While that decision is open, do not guess:
   - no painted light (glow, rays, rim light) in a 3D source image; emissive parts are painted as their colour only;
   - one line per kit part in the brief, with its socket, so either outcome can be built;
   - when two options are close, build that part both ways in the lab and judge them.
   For a subjective look, show the owner two or three options at play-camera size before building.
3. **Write the presence brief.** Name the character and role. Say what the play camera actually sees: the height in px at 720p and 1080p, and the side it faces. List the states and the layers picked from [the layer menu](references/layers.md), each with anchor socket, colour, bloom class, tiers, budget and reduced-motion class. Add the colours it must not use, the reference board, the capture scenario and the acceptance numbers.
4. **One module per layer, each with a switch.** Each layer gets its own file or class, with `enabled` and `intensity`. It is anchored by socket name, allocates nothing per frame, uses seeded randomness, builds its shaders and pooled lights at load, and compiles in the game's shader warm-up so nothing compiles mid-fight. It obeys the bloom rule and never retunes the global bloom, exposure or tone mapping. Build it in the game's own view first. It moves to `shared/game-kit` only once the look is accepted and a second game needs it, and reaches games through `pnpm kit:sync --target games/<id>`, never by editing a game's `src/kit/` (`pnpm kit:check` fails on hand edits).
5. **Judge each layer alone in the lab** ([lab and judging](references/lab-and-judging.md)). The lab uses the game's own renderer, camera, composer, bloom and MSAA at the tier. It has light and dark ground, a held clock, per-layer switches and a per-layer ms reading. Redo or drop a weak layer here; stacking more layers does not save it.
6. **Assemble at the play camera.** Check at the character's real on-screen size with the HUD, word strip and combat VFX on:
   - the silhouette is sharper with presence than without;
   - brightness goes idle < ready < action < combat feedback;
   - nothing covers word tags, the learning frame or enemy telegraphs;
   - white-out and contrast stay inside the limits.
7. **Budget each layer in ms.** Measure on/off deltas at the default tier and Ultra, at dpr 1 and 2, through `.local/bin/heavy.sh --perf` (it takes the whole browser pool, so no other run skews the numbers). Presence is paid every frame out of the VFX headroom of VFX_STANDARD §3.7.
8. **Re-run the shared typing feedback.** Do this if a layer sits near the word strip or where typed letters land, or if anything global changed. Run its measurements before and after, and compare. A visible change is a shared-system change: bar 9, and the owner signs off.
9. **Reduced motion.** Every layer declares keep, soften or drop (VFX_STANDARD §3.8) through the game's own motion setting. Capture the reduced version too.
10. **Capture, prune, judge.** Follow the capture matrix and blind judging in [lab and judging](references/lab-and-judging.md). Two blind judges must both score 8.5 or more, in the built play host at the player's settings, with no URL flags. They score market level and appeal against commercial references. Prune your raw frames, keep the sheets and JSON, and write the game's changelog. Add each recipe you verified to [recipes](references/recipes.md) §4.

## Boundaries

- Shots, skills, impacts, traps and enemy attacks belong to [game-vfx-layered](../game-vfx-layered/SKILL.md). The release flash at the caster belongs there too: presence may swell into it and settle after, never replace it.
- Capes, hair, tails and cloth on bones are character animation (`docs/games/CHARACTER_ANIMATION.md`, bar 9), not presence. Light ribbons that are not part of the mesh are presence.
- Sockets, emissive maps and model cleanup go through the game's model pipeline. Ask for a missing socket instead of guessing an offset.
- An aura that carries a game rule (an elite marker, a leader's buff radius) is a signal, owned by the game's rules; presence must not look like it.
- In Space Typing, its own contracts and [combat-vfx-audio](../combat-vfx-audio/SKILL.md) come first; this skill is reference there.
- Research list and licence rules: [recipes](references/recipes.md). Per-game notes: [worked examples](references/worked-examples.md).

Techniques beyond this repo (Claude reads these directly): `~/.agents/skills/threejs-aaa-graphics-builder/references/{shader-cookbook,technical-art,visual-scorecard}.md`. Their generic defaults (bloom threshold 0.85, rim strength 1.5) lose to the bloom rule above. Their scorecard's fail line holds here too: glow never stands in for a weak model.
