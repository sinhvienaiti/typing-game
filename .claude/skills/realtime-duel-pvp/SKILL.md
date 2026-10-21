---
name: realtime-duel-pvp
description: Implement or review Space Typing real-time Duel input, network authority, accuracy attacks, projectile timing, health, rounds and presentation; use for PvP synchronization or fairness changes.
---

Read [authority and timing contracts](references/duel-contracts.md) and affected current code before editing.

1. Distinguish Practice/local engine, online Friend Room, Ranked and alternative modes. Trace intent through protocol, authority/engine, event, prediction and visual/audio feedback.
2. Preserve real-time input → attack event → spawn → projectile travel → impact → damage. Authority-clock damage must not move to launch or client animation callbacks. Do not convert combat to turns.
3. Preserve server authority, input sequence, match/round identity, stale/duplicate rejection and equal treatment of both players. Prediction cannot mint damage, health or completion.
4. Check accuracy cannon, missile/bomb/laser, health/shield/lives where present, reset/KO, announcer, low-HP and victory FX. Shared timing must align damage, animation and sound.
5. Run focused engine/protocol/network tests and browser checks with independent sessions. Exercise latency, replay/reconnect, simultaneous hits, rounds and fairness; report measured evidence.

Use `typing-input-ime` for filtering, `combat-vfx-audio` for presentation, `game-performance-quality` for measurement and `space-typing-playtest` for two-player evidence. Project authority contracts override generic examples.
