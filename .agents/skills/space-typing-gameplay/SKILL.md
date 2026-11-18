---
name: space-typing-gameplay
description: Implement or review Space Typing stage flow, enemies, bosses, objectives, skills, equipment and combat timing; use when gameplay behavior or campaign integration changes.
---

Read affected current code before adopting a design assumption. Use [the source map](references/gameplay-contracts.md) to find the runtime and relevant tests; read only the rows needed for the task.

1. Identify the mode: main Campaign/Recall, Campaign 3D, Duel, Expedition, or a Defense proposal/benchmark. Trace entry, encounter, completion, rewards and persistence for that mode.
2. Read the game's `docs/PROJECT_CONTEXT.md` and affected implementation. Label plans, historical milestones and implemented behavior separately; resolve contradictions explicitly.
3. Preserve stationary combat and letter ownership. Trace input through target ownership, completion, projectile/impact timing, objectives and reward attribution. Keep skill/proc/environment/voice origins distinct from typed completions.
4. Change the smallest owning domain. Check layer replacement, elite/boss phases, stage-clear gates and world/campaign hooks when affected. Use available engine specialist skills for rendering techniques.
5. Run relevant domain tests, then verify the player-visible sequence with `space-typing-playtest` when behavior changes. Report actual evidence and deferred device/manual checks.

Use `typing-input-ime` for event/scoring semantics, `voice-typing-runtime` for speech completion, `realtime-duel-pvp` for Duel authority, `progression-economy` for settlement, and `admin-runtime-authoring` for authored runtime configuration. Project contracts take precedence over generic skill defaults.
