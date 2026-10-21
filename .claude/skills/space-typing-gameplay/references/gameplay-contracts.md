# Gameplay contracts and source map

Links resolve from the installed `.agents/skills` location. Read current source/tests; these are navigation anchors, not frozen future behavior.

## Product and mode boundaries

[Project context](../../../../games/space-typing/docs/PROJECT_CONTEXT.md) defines stationary typing combat, letter ownership, shared English vocabulary and parent integration. [Characters and combat](../../../../games/space-typing/docs/CHARACTERS_AND_COMBAT.md) explains build intent. Ordinary abilities must not consume target letters; do not add manual movement as an incidental combat fix.

[Main orchestration](../../../../games/space-typing/src/main.ts) and [Game](../../../../games/space-typing/src/Game.ts) join domains. Locate symbols (`handleKey`, `typeTarget`, `completeWord`, `completeBossWord`) instead of historical line numbers.

[Defense V2](../../../../games/space-typing/docs/SPACE_TYPING_DEFENSE_PLAN_V2_2026-10-18.md) is a review/design draft. [Defense benchmark](../../../../games/space-typing/src/bench/defense-bench.ts) is a performance scenario, not implemented Defense gameplay. [Campaign 3D main](../../../../games/space-typing/src/campaign3d/main.ts) has its own entry/rules; do not silently replace main Campaign behavior with them.

## Read according to the change

| Domain | Current source | Regression anchors |
| --- | --- | --- |
| Stage flow/pacing/clear | [Stage](../../../../games/space-typing/src/campaign/stage.ts), [pacing](../../../../games/space-typing/src/campaign/stage-pacing.ts), [scheduler](../../../../games/space-typing/src/events/stage-scheduler.ts), [clear gate](../../../../games/space-typing/src/campaign/stage-clear-gate.ts) | [Scheduler](../../../../games/space-typing/tests/stage-scheduler.test.ts), [clear gate](../../../../games/space-typing/tests/stage-clear-gate.test.ts) |
| Enemy/elite/layers | [Registry](../../../../games/space-typing/src/enemies/registry.ts), [elite](../../../../games/space-typing/src/enemies/elite.ts), [layers](../../../../games/space-typing/src/enemies/layers.ts), [runtime profile](../../../../games/space-typing/src/enemies/runtime-profile.ts) | [Ranks/layers](../../../../games/space-typing/tests/enemy-rank-layers.test.ts), [typing profiles](../../../../games/space-typing/tests/enemy-typing-profile.test.ts) |
| Boss/objectives | Game boss methods, [objectives](../../../../games/space-typing/src/events/objectives.ts) | [Boss typing](../../../../games/space-typing/tests/boss-typing-mechanics.test.ts), [boss skills](../../../../games/space-typing/tests/boss-skills.test.ts) |
| Skills/equipment/builds | [Skill engine](../../../../games/space-typing/src/skills/engine.ts), [skill progression](../../../../games/space-typing/src/skills/progression.ts), [equipment](../../../../games/space-typing/src/equipment/loadout.ts), [stats](../../../../games/space-typing/src/characters/stats.ts) | [Skills](../../../../games/space-typing/tests/skills.test.ts), [equipment](../../../../games/space-typing/tests/equipment.test.ts), [perks](../../../../games/space-typing/tests/equipment-perks.test.ts) |
| Completion/rewards | [Completion facts](../../../../games/space-typing/src/combat/completion-events.ts), [enemy reward runtime](../../../../games/space-typing/src/enemies/reward-runtime.ts), [credit drops](../../../../games/space-typing/src/rewards/combat-credit-drops.ts) | [Reward integration](../../../../games/space-typing/tests/enemy-reward-integration.test.ts), [credit integration](../../../../games/space-typing/tests/combat-credit-game-integration.test.ts) |
| Campaign/world integration | [Progress](../../../../games/space-typing/src/campaign/progress.ts), [world registry](../../../../games/space-typing/src/worlds/registry.ts), [Campaign 3D plan](../../../../games/space-typing/src/campaign3d/plan.ts) | [Replay](../../../../games/space-typing/tests/stage-replay.test.ts), [Campaign 3D](../../../../games/space-typing/tests/campaign3d.test.ts) |

## Review the full effect chain

For a changed attack, state when ownership, progress, damage, visuals, sound, drops, objectives and stage clear occur. Check death/despawn during flight, duplicate completion, boss layer replacement, pause/resume and encounter reset. Visual projectiles must agree with the owning mechanic's timing; do not assume every existing attack shares one damage model.

Completion facts distinguish typing, voice, skill, proc, environment and script. Typed rewards require actual accepted typed letters. Avoid counting auxiliary effects as extra player input.

From platform root, select tests for the mechanism, for example `pnpm --dir games/space-typing exec vitest run tests/stage-clear-gate.test.ts tests/enemy-rank-layers.test.ts`. [Game scripts](../../../../games/space-typing/package.json) define commands. Build for runtime/type integration changes; a skill documentation edit alone needs no game build.
