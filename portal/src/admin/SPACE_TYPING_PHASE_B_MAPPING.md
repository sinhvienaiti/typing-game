# Space Typing Admin — Phase B Integration Mapping

Branch: `feat/space-typing-admin-uiux`

Phase A remains the approved Holo Command UI/mock layer. Phase B maps that UI to canonical config, validation, revision persistence, publish/apply boundaries and child runtime consumers without bypassing immutable revisions.

## Source-of-truth rules

- `games/space-typing/contracts/space-typing-admin.v1.json` remains the child-owned Admin contract snapshot.
- `portal/src/admin/contracts/space-typing-admin.v1.json` remains a byte-equivalent parent mirror and is not expanded independently.
- Parent `RevisionStore` remains the canonical draft/history/publish persistence layer.
- UI edits create immutable draft revisions. They do **not** mutate the active runtime config directly.
- Publish and rollback remain compare-and-swap pointer changes.
- A child runtime adapter is only added after its real consumer and safe apply boundary are identified.
- Existing local v1 revisions must remain readable. New Phase B namespaces are additive and strictly validated when present.
- Revision-backed forms remember the active revision they hydrated from and reject Save Draft if another tab/process has published a newer active revision; they must never silently rebase stale UI state.

The machine-readable route/domain matrix is `admin/space-typing-phase-b-map.v1.json` and is validated in Admin CI.

## Current backend foundation

Already implemented before this Phase B increment:

- immutable revisions and CAS publish/rollback;
- local Admin service and token boundary;
- Audio config foundation;
- canonical World Music preview bridge and B2 migration pattern;
- Music Library authored-asset operations;
- child-owned Admin contract v1 and parent snapshot validation.

## B01 — General Settings + Feature Flags persistence

This increment adds two additive canonical config namespaces:

- `system.gameDefaults`, `system.network`, `system.maintenance`;
- `featureFlags.<flagId>` with `enabled`, `rolloutPercent`, `scope`, and `risk`.

Validation includes:

- enumerated game mode and difficulty;
- canonical kebab-case ship/flag IDs;
- semantic-version-shaped minimum version;
- bounded autosave/reconnect values;
- bounded maintenance message;
- feature rollout in `0..100`;
- controlled flag scope and risk classes.

Dangerous values such as maintenance, economy flags and competitive flags remain protected by revision Publish. A form Save Draft must never change the active revision.

## B02 — General Settings + Feature Flags UI wiring

The two screens now use the real Admin revision API instead of mock-only Save actions:

- hydrate from the current active revision;
- preserve fallback defaults for older v1 revisions that predate the additive namespaces;
- Save Draft clones the active config and calls `createRevision` only;
- no screen calls `publish` directly;
- validation errors are surfaced in the screen;
- maintenance/economy/competitive changes remain inactive until explicit History / Publish review;
- stale-form protection rejects Save Draft when the active revision changed after hydration, preventing silent lost-update rebases.

## Apply boundaries

The current mapping deliberately uses conservative boundaries:

- Audio policy: safe boundary.
- World Music: next track/state.
- Game content/economy/system/flags: new session unless a narrower child boundary is later proven safe.
- Live Ops: schedule/new-run boundaries.
- PvP: new match.
- Visuals: new scene.
- QA: new isolated QA run.

No screen may be marked runtime-connected merely because a UI mock exists.

## Ordered Phase B implementation

1. **B01 — System + Feature Flags persistence**: canonical namespaces, validation, API typing, revision tests, route/domain matrix. **Implemented.**
2. **B02 — Wire General Settings + Feature Flags UI**: hydrate active values, create immutable revisions on Save Draft, surface validation/error state, stale-active conflict protection, and never direct-publish. **Implemented.**
3. **B03 — Audio Defaults**: replace local UI state with active/draft revision state while preserving player-preference semantics.
4. **B04 — World Music**: map Stage-level editor data into authored policy drafts and canonical preview validation; keep runtime apply at next-track/state.
5. **B05 — History & Publish**: replace mock history/diff/status with real revision data, real validation gates and CAS conflicts.
6. **B06 — Content registries**: Ships → Equipment → Skills → Enemies → Bosses → Worlds/Stages. Each domain requires child consumer discovery before runtime apply.
7. **B07 — Economy**: Shop, Currencies, Rewards/Drops, Warp. Require impact validation and explicit dangerous-change confirmation.
8. **B08 — Live Ops**: Missions, Daily/Weekly, Expedition, Events with scheduling validation/timezone rules.
9. **B09 — PvP**: Duel, Ranked, Alternative Modes with server-authority/new-match boundaries and ranked admission gates.
10. **B10 — Visuals + QA + telemetry**: Backgrounds/VFX/UI assets authored manifests, isolated QA capability, then Overview/Analytics telemetry adapters.

## Exit criteria for each domain

A domain is only complete when all of the following are true:

1. Field-by-field UI → canonical schema mapping exists.
2. Server-side validation rejects malformed/dangerous invalid values.
3. Save Draft writes an immutable revision without affecting runtime.
4. Stale hydrated forms cannot silently rebase over a newer active revision.
5. Publish uses expected-active CAS.
6. Rollback targets an immutable valid revision.
7. Runtime consumer and apply boundary are explicit.
8. Regression tests cover draft isolation, publish, validation and backward compatibility.
9. Admin CI and Platform CI pass on the exact final parent HEAD.
