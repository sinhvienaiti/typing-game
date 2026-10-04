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

## Small in-game feedback panel

The child mounts a compact, non-interactive panel at the lower-right edge. It is
hidden in Typing and outside combat. A validated `detection` first displays the
heard keyword with **Checking…**; only the game's outgoing `resolution` may
change that to **Accepted**. Rejected ownership/eligibility remains explicit.
This presentation path never calls gameplay completion or records a learning miss.

An injected decoder may call `onFeedback(value)` with the canonical `feedback`
payload to expose its final transcript even when it found no target. This is
diagnostic metadata, not a `detection`. Use `result=recognized` with the genuine
transcript (at most 200 characters); include `detectionId` only if the same final
utterance generated that candidate. Omitting it means the final mapping found
no candidate, rather than a match still in progress. `result=unrecognized` requires
`transcript=null` and `evidence=final-utterance` after a completed speech segment.
Do not manufacture this event from a silence timeout or guess a nearby target.
A keyword-only engine may show its genuine validated keyword; it must not invent
a full ASR transcript. Partial hypotheses are not accepted by this contract.

Feedback follows the same active host/session/input/audio/engine/model fences as
detections, with ordered capture samples. The child ignores late/duplicate words,
correlates resolution with the displayed candidate, and clears speech on pause,
stop or mode change. After four seconds the word collapses to the small listening
indicator. Text is rendered with `textContent`, announced politely, and kept out
of save/learning data. Panel layout reserves space above controls on narrow views
and moves the music toast above it.

There is still no production decoder or enabled Voice selector. The mounted
adapter does not probe or start automatically. Tests exercise injected final
metadata and DOM rendering; real-microphone and browser visual acceptance remain
part of the engine/gameplay release gates.

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

## Recognition grammar and overload policy

The Portal runtime recognizes only the checked vocabulary and supported target
forms (Vosk grammar plus `[unk]`); a new form rebuilds the recognizer after the
current utterance. Capture allows 3 s of undecoded audio. An overflow drops that
utterance and restarts the recognizer; more than 3 overloads in 20 s fail the
session. Measurements and the end-to-end fake-microphone check (`pnpm voice:e2e`)
are in `docs/SPACE_VOICE_AND_WARP_LOCAL.md`.

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
