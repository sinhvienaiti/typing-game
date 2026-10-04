# Voice platform foundation

The production bridge has **no installed engine factory**. It reports
`offlineEngineAvailable=false`. No SpeechRecognition fallback, microphone
request, model download or inference worker is created by opening Typing.
The Portal loads the metadata bridge only after a message from the active Space
Typing iframe passes source/origin checks. Other game/learning routes are unchanged.

## Modules

- `protocol.mjs`: draft v1 metadata parser with bounds and normalized full spoken forms.
- `target-snapshot.mjs`: exact matching against an immutable parsed snapshot; no nearest-target authority.
- `result-policy.mjs`: capture-sample freshness/ACK/eligibility/ownership guards and terminal receipts. Current stable snapshots survive long waits; superseded snapshots and receipts have at least ten seconds of retention, bounded by configured capacity.
- `host.mjs`: injected local-runtime lifecycle. Unit tests cover late permission, cancelled preparation, concurrent start, target compilation during pause, TTS generation fencing and teardown. It does not implement production capture or decoding.
- `bridge.mjs`: active frame/origin/instance/session fencing and capability gate.

Acceptance is a synchronous claim boundary. Callers must skip effects whenever
`duplicate=true`, including a replay of an originally accepted receipt. A policy
decision alone does not authorize a game mechanic: revalidate its phase, status,
window, resources and unit, claim ownership, then apply gameplay effects without
an async gap. The child retains authority over completion, score and learning.

`emittedAtMs` is telemetry and must use the normalized performance time origin;
it is not word-end timing. `audioStartSample`, `audioEndSample`, ACK sample times
and freshness must use the same monotonically increasing capture-owned clock.
The future real transport still needs explicit clock anchors; a child wall clock
or a worker emission timestamp must never masquerade as capture sample time.

## Canonical child copies

```bash
pnpm voice:test
pnpm voice:sync
pnpm voice:check
# Standalone sibling checkout:
node scripts/sync-space-voice-contract.mjs --check --target ../space-typing
```

The generator copies protocol/matcher/policy source and declarations byte for
byte into `games/space-typing/src/input/platform`, with a SHA-256 manifest. Do not
edit these child files by hand. CI checks the pinned child against canonical
parent source. Updating the parent requires the child commit and gitlink to agree.

## Release gate

Do not install a production engine factory until there is a pinned WASM/model/
tokenizer/license manifest and measured engine evidence under game load. Sherpa
v1.13.8 source audit found its stock KWS JS wrapper and WASM export list do not
expose the native dynamic-keyword stream API. A custom binding needs verification;
there is no measured KWS-versus-ASR winner yet.

Capture/Worklet, stateful resampling, bounded PCM/worker backpressure, atomic
model cache, real TTS wiring, mic UI, semantic voice combat, passive mapping,
speaking aggregation, save/run profile attribution and campaign coverage remain
unimplemented. Core tests are not recognition accuracy or latency measurements.
See the pinned child's `docs/VOICE_FINAL_V2_IMPLEMENTATION_STATUS.md` for the
full checkpoint and gates from Final V2.
