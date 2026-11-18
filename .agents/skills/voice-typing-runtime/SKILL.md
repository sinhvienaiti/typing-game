---
name: voice-typing-runtime
description: Implement or diagnose Space Typing Typing, Voice and Hybrid modes, ASR sessions, microphone lifecycle, transcript feedback and speech-to-combat routing; use when recognition or input ownership changes.
---

Read [runtime boundaries and checks](references/voice-contracts.md). Trace the running parent and child together; a plan or stale foundation README cannot prove present availability.

1. Identify route/mode and failure stage: Portal handshake, permission, model preparation, audio activation, recognizer readiness, target admission, acceptance or feedback.
2. Keep reusable capture/ASR/provider lifecycle in the platform. Space Typing owns eligibility, ownership, semantic completion and rewards. Do not embed provider/model code in gameplay components.
3. Preserve session/input/audio/engine/model fences and capture-sample clocks. Bound queues, reject stale/duplicate receipts and synchronously revalidate live targets before effects. Never replay speech as fake keys.
4. Typing must not start mic/model. Hybrid keyboard A can coexist with voice B; voice cannot finish a keyboard-owned word/layer. Preserve controls when speech fails.
5. Interim transcript is provisional presentation only if supported. Current accepted results/feedback require final-utterance or validated-keyword evidence. Prevent duplicate leading-token acceptance using IDs, spans and unit identity, not arbitrary text slicing.
6. Verify permission denial/cancel, timeout, pause/TTS, reconnect, mode/route changes, late/duplicate results, feedback and latency under game load. Use the Portal for browser acceptance; separate fake-mic/WASM evidence from human microphone acceptance.

Use `typing-input-ime` for physical text events, `space-typing-playtest` for rendered feedback and `realtime-duel-pvp` for competitive eligibility. Do not infer ranked Voice support from PvE settings.
