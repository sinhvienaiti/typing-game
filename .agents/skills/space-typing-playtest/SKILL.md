---
name: space-typing-playtest
description: Run real-browser Space Typing QA with representative typing, gameplay, canvas, asset/audio, layout and interaction evidence. Use after user-visible changes or for playtesting; unit tests and synthetic input do not establish real IME, listening, or perceptual acceptance.
---

# Playtest the actual user surface

1. Determine mode, route and build: standalone 2D, Portal embed, Duel, Campaign 3D, Admin or development gallery. Read [the scenario/tooling map](references/scenarios.md), inspect controls, and select relevant scenarios.
2. Detect healthy local services and their code/build identity before launching another. If needed, start a temporary server on an unused port with strict binding and retain its process handle. Never kill an unrelated listener to claim a fixed port; stop only your own processes.
3. Use available generic game-playtest/QA skills when useful, otherwise repository Chrome/CDP tooling. Providers are optional; do not install game dependencies merely to satisfy a skill. Use an isolated browser profile to preserve the user's save, wallet, account and settings.
4. Exercise user interactions: start, focus input, type/correct words, activate a relevant skill/overlay, resize and observe outcomes. Use deterministic Test Lab setups when useful; label injected state, synthetic composition and fake audio accurately.
5. Inspect canvas/screenshots, page exceptions, warnings, failed assets, HUD overlap and animation over time. Verify audio after a gesture; listening and native OS IME acceptance require separate evidence.
6. Report route/build, scenario, viewport/DPR/quality, steps, observations and artifact paths. Separate passed, failed and untested cases. If browser execution is blocked, finish independent work and retain a manual checklist; unit tests alone cannot establish that the game works.

Use [typing-input-ime](../typing-input-ime/SKILL.md), [realtime-duel-pvp](../realtime-duel-pvp/SKILL.md), [game-ui-ux-review](../game-ui-ux-review/SKILL.md) or [game-performance-quality](../game-performance-quality/SKILL.md) for domain acceptance criteria.
