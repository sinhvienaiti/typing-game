---
name: combat-vfx-audio
description: Change Space Typing projectile, impact, explosion, boss/skill effects, pickups, announcer, SFX, or music interaction. Use for combat presentation and audio readability; coordinate authoritative damage timing with gameplay or PvP skills.
---

# Combat presentation and sound

1. Identify mode and trace the event to visual/audio consumers using [the presentation map](references/presentation-map.md). Preserve combat timing: launch cue, projectile arrival, confirmed impact and damage can be distinct events.
2. Define the intended player cue before editing. Keep target text, caret/progress and threats readable under heavy overlap. Preserve distinctive ship/enemy/boss feedback without covering words or relying on color alone.
3. Reuse projectile recipes, sprite manifests, effect renderers, audio groups and lifecycle. Match alpha/blending/pivots/frame timing to metadata; asset generation or a preview image alone does not prove integration.
4. Mix against typing, pronunciation, warnings, BGM and announcer priorities. Check first user gesture, mute/volume, pause/resume, repeated events, cleanup and missing media. Keep critical feedback available when optional art/audio fails.
5. Run focused contract/lifecycle tests, inspect normal-speed action and selected slow-motion frames, and measure extra load. Use audible playback for perceived-sound claims; offline amplitude metrics cannot prove balance or pleasantness.

Use [realtime-duel-pvp](../realtime-duel-pvp/SKILL.md) for synchronized damage, [game-performance-quality](../game-performance-quality/SKILL.md) for measured budgets, and [space-typing-playtest](../space-typing-playtest/SKILL.md) for evidence. Available generic graphics/audio skills can supply techniques; provider access is optional.
