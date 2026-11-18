# Space Typing Voice and Warp Charge — local testing

Updated: 2026-10-04. Platform branch: `feat/space-voice-platform`.
Space Typing branch: `feat/bgv-integration-current`, pinned by the platform gitlink.

## Pull and run

Run in your existing `typing-game` checkout (Node 24 and pnpm):

```bash
cd /Users/jokerit/htdocs/typing-game
git fetch origin
git switch feat/space-voice-platform
git pull --ff-only origin feat/space-voice-platform
git submodule sync --recursive
git submodule update --init --recursive
./dev.sh space
```

The launcher updates dependencies, prepares art and the pinned English offline
Voice model, configures local HTTPS and starts Portal plus Space Typing. First
model preparation downloads about 41 MB and needs Python 3. Subsequent preparation
verifies the cached artifacts. If you run the lower-level `pnpm dev:space` directly,
run `pnpm voice:prepare` first.

Open **https://typing-game.local/space-typing**. Voice requires the Portal route
because Portal owns the microphone. The child origin alone is not the Voice host.

## Enable Voice

1. At the bottom right, change **Typing** to **Voice** or **Hybrid**.
2. Press **Mic**, allow microphone access and wait for **Listening · English**.
   Loading the model on the first activation can take longer than reconnecting.
3. Use **Practice · Free** to test without spending Warp, or Deploy for Campaign.
4. Read the displayed English word. The compact feedback panel shows what was
   heard and whether the game accepted it. For projectile/meteor NATO forms, read
   the displayed NATO word. Hybrid also accepts keyboard input.
5. Press Mic again to stop capture. The existing pronunciation/speaker toggle
   controls speech output, not microphone recognition.

If permission was denied, enable the microphone in the browser's permissions for
`typing-game.local`, then reconnect. A second tab's mic session or economy writer
can block activation/spending; close the other session and reload when needed.

## Connection timeouts

After pulling, restart `./dev.sh space` and reload the Portal tab with Cmd+Shift+R.
Both feature branches are required: the current Portal `main` branch has no Voice
host, so a child-only update can time out before requesting microphone permission.
The reported Mac's exact failed stage has not been observed.

The controls now distinguish Portal connection, permission, model loading, audio
activation and recognizer readiness. Portal handshake has an 8-second deadline;
preparation has 90 seconds, followed by a fresh 15-second recognizer deadline.
Audio activation is abortable and bounded to 10 seconds. Model progress is shown
in the existing compact control, and failed lazy imports can be retried.

## "Offline speech processing overloaded" fix (2026-10-05)

Symptom: saying any word paused the game and showed "Offline speech processing
overloaded. Close heavy game tabs, then reconnect."

Root cause, measured with the pinned Vosk worker on a 16 kHz spoken-word fixture
in 100 ms blocks:

| Recognizer | Block decode p95 / worst | Peak backlog | Accuracy |
|---|---|---|---|
| Open vocabulary (before) | 214 ms / 951 ms | 12 blocks, over the 10-block cap | "comet" heard as "comment" |
| Grammar of 154 game words (after) | 98 ms / 209 ms | 2 blocks | 15/15 |

Open-vocabulary Vosk stalls up to ~1 s when it finalizes an utterance, so the
1-second capture cap overflowed right after each spoken word. The runtime then
failed hard, and `voice-session.ts` paused the game and stopped the mic.

Fix:

- **Grammar:** the recognizer only listens for the vocabulary the game checks
  (`vocabulary-check`) plus every supported on-screen target, with `[unk]` as a
  catch-all (`portal/src/voice/decoder.ts`, `runtime.ts`, `shared/voice/host.mjs`).
  A target word outside the grammar rebuilds the recognizer, never in the middle
  of an utterance. `[unk]` words are never reported.
- **Backlog:** the cap is 3 s (`capture-policy.ts`, 30 blocks of 100 ms).
- **Overload recovery:** an overflow drops that utterance and restarts the
  recognizer. Only more than 3 overloads within 20 s end the session with the
  old message.
- **End-to-end check without a microphone:** `pnpm dev:portal`, then
  `pnpm voice:e2e`. Add `-- --stress` to block the page main thread 30 ms of
  every 40 ms. Both runs: 22–23 detections in 30 s, every word heard, no error.

## Warp behavior to test

Campaign/replay/Ascension/each rewarded Hidden deployment costs 10. Active has a
100 cap and regenerates every 6 min. Reserve has a 300 cap, regenerates every 12
min only with Active full, and spending it is off until explicitly enabled.
Refuel adds 20 for 8/12/18 SC, at most three times before the 04:00 Vietnam reset.
Practice is free and preserves learning without saving simulated economic rewards.
Expedition/Duel cost zero Warp and remain isolated.

Try duplicate Deploy/refill clicks, prepared continuation, quit/defeat, Phoenix,
clear/reload, Practice exit, two tabs and backup restore. Restore explicitly replaces
the whole profile and may roll spending back; export a backup before testing it.

## Verification and remaining acceptance

Space Typing: 1,626 tests across 253 files and build passed. Shared Voice/Learning:
115 tests passed. Portal build, six-file canonical Voice contract, real Vosk
Worker/WASM decoding with a WAV fixture and worklet module smoke tests passed.
The worklet smoke tests use a Node VM, not native browser capture. No real microphone/browser session
or end-to-end latency/frame benchmark was possible in the implementation environment.

Implementation details, economy bounds and exact remaining release gates:

- [Voice status](../games/space-typing/docs/VOICE_FINAL_V2_IMPLEMENTATION_STATUS.md)
- [Warp Charge status](../games/space-typing/docs/WARP_CHARGE_IMPLEMENTATION_STATUS.md)

Useful verification commands after bootstrap:

```bash
node --test shared/voice/*.test.mjs shared/learning/*.test.mjs
pnpm voice:check
pnpm --dir portal build
pnpm --dir games/space-typing check
pnpm --dir games/space-typing stamina:audit
```
