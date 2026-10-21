# Voice architecture and checks

## Current implementation map

| Boundary | Source |
| --- | --- |
| Canonical parsing/safety/matching | [Protocol](../../../../shared/voice/protocol.mjs), [result policy](../../../../shared/voice/result-policy.mjs), [final matcher](../../../../shared/voice/final-matcher.mjs), [host](../../../../shared/voice/host.mjs), [bridge](../../../../shared/voice/bridge.mjs) |
| Reusable Portal capture/ASR | [Host factory](../../../../portal/src/voice/host-factory.mjs), [runtime](../../../../portal/src/voice/runtime.ts), [decoder](../../../../portal/src/voice/decoder.ts), [capture policy](../../../../portal/src/voice/capture-policy.ts), [model manifest](../../../../shared/voice/model-manifest.json) |
| Game authority/adapters | [Adapter](../../../../games/space-typing/src/input/voice-adapter.ts), [session](../../../../games/space-typing/src/input/voice-session.ts), [modes](../../../../games/space-typing/src/input/mode.ts), [ownership](../../../../games/space-typing/src/input/target-ownership.ts), [registry](../../../../games/space-typing/src/input/target-registry.ts), [Game](../../../../games/space-typing/src/Game.ts) |
| Feedback/attribution | [Feedback state](../../../../games/space-typing/src/input/voice-feedback.ts), [UI](../../../../games/space-typing/src/ui/voice-feedback.ts), [completion facts](../../../../games/space-typing/src/combat/completion-events.ts), [combat policy](../../../../games/space-typing/src/input/voice-combat-policy.ts) |

[Implementation status](../../../../games/space-typing/docs/VOICE_FINAL_V2_IMPLEMENTATION_STATUS.md) records completed work/outstanding human gates. [Local guide](../../../../docs/SPACE_VOICE_AND_WARP_LOCAL.md) contains later grammar/backpressure corrections; historical branch-switch/pull instructions are not authorization to change checkout. [Original V2 plan](../../../../games/space-typing/docs/VOICE_INPUT_PLATFORM_SPACE_TYPING_3_MODE_FINAL_V2_2026-10-04.md) is a specification. [Foundation README](../../../../shared/voice/README.md) mixes old “no production engine” prose and later notes: resolve against current source.

## Preserve the boundaries

- Portal owns mic/capture and local English recognition; child messages contain metadata, not raw PCM. Standalone typing works; Voice acceptance uses Portal `/space-typing`.
- Validate origin/source/instance/session/epochs. Match final timestamped words against capture-time target snapshots. Callback/wall-clock timestamps are not capture samples.
- Candidates/interim strings are not accepted hits. Revalidate phase, target unit/version, time window, eligibility and ownership; claim/apply synchronously. Duplicate accepted receipts cannot repeat effects.
- First accepted typed key owns its word/layer even after progress reset. New layers are new units. Speech completion of B cannot clear keyboard A. Keep speech reward/learning separate from typed characters/WPM/streak.
- Current feedback requires final-utterance or validated-keyword evidence. Heard/Checking precedes game acceptance. Render last recognized phrase as text, clear on lifecycle transitions, and do not persist it. Silence is not an invented unrecognized transcript.
- Prevent duplicate leading words/reconnect replay using capture spans, session and receipt identity. Identical text on a new unit can be legitimate; global text deduplication breaks it.
- TTS waits for capture-gate ACK and fresh resume/audio epoch. Bound preparation/reconnect deadlines and name the failing stage. Typing loads no mic/model; Hybrid keeps keyboard play on voice failure.
- Child `src/input/platform` copies are generated from parent contracts with [the sync generator](../../../../scripts/sync-space-voice-contract.mjs); do not hand-edit them.

## Targeted checks

Choose relevant commands from [platform](../../../../package.json) and [game](../../../../games/space-typing/package.json) scripts. From platform root:

```sh
pnpm voice:check
node scripts/sync-space-voice-contract.mjs --check
pnpm --dir games/space-typing exec vitest run tests/voice-session.test.ts tests/voice-adapter.test.ts tests/voice-gameplay.test.ts tests/voice-feedback.test.ts tests/voice-feedback-ui.test.ts
```

Relevant tests: [adapter](../../../../games/space-typing/tests/voice-adapter.test.ts), [session](../../../../games/space-typing/tests/voice-session.test.ts), [gameplay](../../../../games/space-typing/tests/voice-gameplay.test.ts), [host lifecycle](../../../../shared/voice/runtime-lifecycle.test.mjs), [capture backpressure](../../../../shared/voice/capture-backpressure.test.mjs). Locate matcher-specific cases before changing final-span semantics.

Browser checks: permission allow/deny/cancel; stop while loading; unplug/reconnect; competing tab; route exit; pause/TTS; late result; repeated leading token; Hybrid A/B; accepted/rejected feedback; narrow HUD; frame/end-to-end latency under load. `voice:e2e:local`, worker smoke and gameplay evals are useful automation, not proof of native devices, human corpus accuracy or real-mic latency. Preparation scripts can download/publish local artifacts; run them only when needed.
