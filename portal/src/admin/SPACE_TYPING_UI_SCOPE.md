# Space Typing Admin — UI/UX Scope

Branch: `feat/space-typing-admin-uiux`

This branch implements the UI/UX-first Holo Command Admin experience with mock data only. It intentionally does **not** write production config or mutate Space Typing runtime state.

Implemented navigation/screens:

- Dashboard: Overview, Analytics
- Audio & Music: Audio Defaults, Music Library, World / Stage Music
- Game Content: Ships, Equipment, Skills, Enemies, Bosses, Worlds & Stages, Typing Content
- Economy: Shop, Currencies, Rewards & Drops, Stamina / Warp
- Live Ops: Missions, Expedition, Events
- PvP: Duel Settings, Ranked, Alternative Modes
- Visuals: Backgrounds, VFX, UI Assets
- System: General Settings, Feature Flags, History & Publish
- Developer: QA Sandbox

Design direction:

- Space Typing `A · Holo Command`
- Exo 2 display font
- Be Vietnam Pro body font
- cyan → violet accents
- chamfered glass/solid operation panels
- dark space backgrounds
- dense desktop-first operations UI
- responsive fallback for narrower screens

The next phase, after UI approval, is field-by-field mapping to schemas, APIs, persistence, validation, publish/apply boundaries, and runtime consumers.
