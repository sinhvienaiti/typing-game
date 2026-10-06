# Space Typing Admin — UI/UX Scope

Branch: `feat/space-typing-admin-uiux`

Current visual revision: `A-HOLO-04`

This branch implements the complete UI/UX-first Holo Command Admin experience with mock data only. It intentionally does **not** write production config or mutate Space Typing runtime state.

Implemented navigation/screens:

- Dashboard: Overview, Analytics
- Audio & Music: Audio Defaults, Music Library, World / Stage Music
- Game Content: Ships, Equipment, Skills, Enemies, Bosses, Worlds & Stages, Typing Content
- Economy: Shop, Currencies, Rewards & Drops, Stamina / Warp
- Live Ops: Missions, Daily / Weekly, Expedition, Events
- PvP: Duel Settings, Ranked, Alternative Modes
- Visuals: Backgrounds, VFX, UI Assets
- System: General Settings, Feature Flags, History & Publish
- Developer: QA Sandbox

Cross-screen UX implemented:

- Holo Command shell/sidebar/topbar
- Exo 2 display font + Be Vietnam Pro body font
- shared cyan → violet Holo tokens
- chamfered glass/solid operation panels
- real Space Typing galaxy background and ship/background assets where appropriate
- line SVG navigation icons
- global `Cmd/Ctrl + K` command palette
- responsive desktop/laptop layouts
- keyboard focus-visible treatment and reduced-motion handling
- mock-only badges so fake telemetry is not presented as live production data
- sticky draft/save patterns for editable screens
- integrated preview patterns instead of standalone preview pages
- detailed World Music hierarchy down to Stage, including multi-stage selection, multi-track assignment, matrix view, inheritance/fallback preview
- revision diff/publish/rollback UX
- dangerous-change warnings for economy/ranked/system domains

Final UI review hardening already applied:

- removed the obsolete first-generation World Music renderer so only the Stage-level V2 editor remains
- corrected World selection so the selected stage starts at that World's first real stage instead of Stage 001
- unified `--st-admin-*` and game-style `--holo-*` design tokens
- corrected Admin route scrolling inside the 48px parent portal shell
- added focus-visible and reduced-motion accessibility handling
- added line-SVG sidebar icons and global command search
- cleaned command-palette keyboard listeners on every close path
- added accessible labels for range, search, filter and playlist-weight controls
- added explicit `aria-pressed` state for segmented controls, toggles and Stage selection controls
- connected World Music `Inherit / Replace` to persistent mock UI state so Effective Playlist and resolved-source preview stay consistent with the selected assignment mode
- constrained History actions so only Draft revisions can Publish and only older Published revisions can Rollback
- strengthened `validate-space-admin-ui.mjs` with final accessibility/state regression guards and one-shot workflow/script cleanup checks
- removed all one-shot implementation workflows/scripts after they ran

Design direction:

- Space Typing `A · Holo Command`
- dark space command-center appearance
- dense game-operations information architecture
- actual game assets reused where available
- no generic SaaS visual language

The next phase, only after UI approval, is field-by-field mapping to schemas, APIs, persistence, validation, publish/apply boundaries, and runtime consumers.
