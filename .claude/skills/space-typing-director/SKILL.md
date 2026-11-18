---
name: space-typing-director
description: Route broad Space Typing tasks across project contracts and specialists when work spans gameplay, input, online, assets, admin, UX, performance or delivery.
---

# Space Typing director

1. Establish the requested result, affected surface (game, parent portal, admin,
   shared service or standalone benchmark), and repository ownership. Inspect root,
   branch, HEAD and dirty files in parent and affected submodule before assigning
   writes. Preserve other workers' changes.
2. Read relevant entries in the [source map](references/project-map.md). Compare
   code/tests with product contracts and record discrepancies. A dated plan or open
   editor tab does not establish implemented behavior.
3. Select the smallest useful set of project specialists below. Load their actual
   `SKILL.md` and only references relevant to the request. Delegate independent work
   with distinct file ownership when supported; keep shared interfaces and final
   integration with one lead.
4. Use installed engine specialists for implementation technique as needed. Project
   rules override generic defaults: no scaffold replacement, package manager switch,
   movement controls or broadened release audit by implication. Skill installation
   alone supplies no browser, Blender or paid-provider access. Inspect available
   tools; a detected API key does not itself authorize paid generation.
5. Carry the requested unit through implementation, relevant tests and review. Use
   rendered-page/input evidence for visible behavior. Report what was verified,
   remaining manual checks, and a precise continuation point if needed.

| Task | Project specialist |
| --- | --- |
| Stage, enemy, boss, objective, combat, equipment | [space-typing-gameplay](../space-typing-gameplay/SKILL.md) |
| Typing, composition, correction, caret, accuracy | [typing-input-ime](../typing-input-ime/SKILL.md) |
| ASR, microphone, Voice/Hybrid mode | [voice-typing-runtime](../voice-typing-runtime/SKILL.md) |
| Duel, synchronization, attack/impact semantics | [realtime-duel-pvp](../realtime-duel-pvp/SKILL.md) |
| Rewards, wallet, unlocks, Warp/stamina | [progression-economy](../progression-economy/SKILL.md) |
| Admin editing and runtime configuration | [admin-runtime-authoring](../admin-runtime-authoring/SKILL.md) |
| Concepts, Blender, models, GLB/animation | [game-asset-2d-to-3d](../game-asset-2d-to-3d/SKILL.md) |
| Projectile/hit/boss FX, SFX/BGM | [combat-vfx-audio](../combat-vfx-audio/SKILL.md) |
| Player/admin UX and rendered UI review | [game-ui-ux-review](../game-ui-ux-review/SKILL.md) |
| FPS, memory, render/asset budgets | [game-performance-quality](../game-performance-quality/SKILL.md) |
| Browser input, screenshots, animation evidence | [space-typing-playtest](../space-typing-playtest/SKILL.md) |
| CI, remote branches, worker continuation | [game-ci-resumable](../game-ci-resumable/SKILL.md) |

For focused work, use its specialist directly. Resolve generic overlap with the
[engine routing map](references/project-map.md); do not load every domain.
