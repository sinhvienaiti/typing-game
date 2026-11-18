# Presentation ownership

| Concern | Source | Focused tests |
| --- | --- | --- |
| Player projectile identity/flight/impact | [Player shots](../../../../games/space-typing/src/vfx/player-shots.ts) | [Player shots](../../../../games/space-typing/tests/player-shots.test.ts), [authored shot origin](../../../../games/space-typing/tests/authored-ship-shot-origin.test.ts), [Admin projectile authority](../../../../games/space-typing/tests/admin-projectile-authority.test.ts) |
| Painted sprite loading | [Combat sprites](../../../../games/space-typing/src/vfx/combat-vfx-sprites.ts), [preparation](../../../../games/space-typing/scripts/bg-art/prepare-combat-vfx.mjs) | [Combat sprites](../../../../games/space-typing/tests/combat-vfx-sprites.test.ts), [VFX polish](../../../../games/space-typing/tests/vfx-polish.test.ts) |
| Enemy/boss feedback | [Enemy visuals](../../../../games/space-typing/src/enemies/visuals.ts), [boss profile](../../../../games/space-typing/src/boss/visual-profile.ts) | [Enemy VFX](../../../../games/space-typing/tests/enemy-vfx.test.ts), [boss FX](../../../../games/space-typing/tests/boss-fx.test.ts) |
| Duel presentation | [Combat visuals](../../../../games/space-typing/src/duel/combat-visuals.ts), [Duel sound](../../../../games/space-typing/src/audio/duel-sound.ts) | [Combat juice](../../../../games/space-typing/tests/duel-combat-juice.test.ts), [Duel audio](../../../../games/space-typing/tests/duel-audio.test.ts), [sound](../../../../games/space-typing/tests/duel-sound.test.ts) |
| Announcer/mix | [Announcer](../../../../games/space-typing/src/audio/announcer.ts), [mix](../../../../games/space-typing/src/audio/mix.ts) | [Announcer SFX](../../../../games/space-typing/tests/announcer-sfx.test.ts), [audio mix](../../../../games/space-typing/tests/audio-mix.test.ts), [SFX lifecycle](../../../../games/space-typing/tests/sfx-lifecycle.test.ts) |
| Pickups | [Credit sound](../../../../games/space-typing/src/audio/credit-sound.ts) | [Credit sound](../../../../games/space-typing/tests/credit-sound.test.ts), [pickups](../../../../games/space-typing/tests/credit-crystal-pickups.test.ts) |
| World/stage music | [Runtime](../../../../games/space-typing/src/audio/world-music-runtime.ts), [adapter](../../../../games/space-typing/src/audio/world-music-adapter.ts) | [Music adapter](../../../../games/space-typing/tests/world-music-runtime-adapter.test.ts), [controller](../../../../games/space-typing/tests/music-controller.test.ts) |

Read [Duel V2 plan](../../../../games/space-typing/docs/DUEL_COMBAT_TYPING_VISUAL_AUDIO_FINAL_V2_2026-10-01.md), [implementation status](../../../../games/space-typing/docs/DUEL_VISUAL_AUDIO_FINAL_V2_IMPLEMENTATION_STATUS_2026-10-01.md) and [audio experience plan](../../../../games/space-typing/docs/AUDIO_EXPERIENCE_PERFORMANCE_PLAN.md) only for relevant design intent. Today's consumers/events determine implementation truth; old plans are not current listening evidence.

## Failure checks

- Before reusing shader/post-processing recipes, identify whether this effect uses Canvas or Three.js and follow the [engine compatibility check](../../space-typing-director/references/project-map.md#compatibility-before-reusing-recipes). Keep GLSL/chunks/imports compatible with the installed renderer/version.
- Preserve Duel deferred impact/confirmed-hit semantics. Do not move damage to keypress to align a decorative flash; inspect current engine integration.
- Inspect frame count, playback FPS, lifetime, pivot, alpha convention and blend mode. Look for opaque rectangles, cropped frames and tinted fringes in the actual renderer.
- Keep effect collections bounded and avoid per-frame asset construction. Measure overlap with matched quality/DPR/viewport.
- Honor audio groups/ducking and announcer interruption priorities rather than creating competing queues.
- Repeat restart, scene switch, mute/unmute and pause/resume. Detect duplicate loops, orphaned voices and late decode callbacks.
- Preserve [local-only/redistribution boundaries](../../../../games/space-typing/docs/LOCAL_ASSETS_README.md).

## Evidence tools

Read [visual testing](../../../../games/space-typing/docs/VISUAL_TESTING.md) for shot/skill/boss galleries and [SFX levels evaluation](../../../../games/space-typing/scripts/visual/evals/sfx-levels.js). That evaluation measures offline peak/length/level; label it as measurement, not a listening test. Start real audio through a user gesture before judging playback.

From repo root, select relevant checks:

```bash
pnpm --dir games/space-typing test tests/player-shots.test.ts tests/combat-vfx-sprites.test.ts
pnpm --dir games/space-typing test tests/audio-mix.test.ts tests/sfx-lifecycle.test.ts
pnpm --dir games/space-typing vfx:audit
pnpm --dir games/space-typing sfx:audit
```
