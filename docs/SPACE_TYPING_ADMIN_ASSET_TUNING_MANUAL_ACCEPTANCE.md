# Space Typing Admin Asset Tuning — Manual Acceptance

> Scope: A5 production-preview and authoring acceptance. This checklist is intentionally non-blocking for independent implementation work. Record failures here and fix them as follow-up defects; do not use an unperformed manual check as a reason to stop unrelated A5 work.

## 1. Preconditions

- Parent repo: `sinhvienaiti/typing-game`, branch `feat/space-typing-admin-uiux`.
- Child runtime: `sinhvienaiti/space-typing`, branch `feat/bgv-integration-current`.
- Portal origin and Space Typing origin must both be available through the local HTTPS setup.
- `/games.json` must resolve `space-typing` to the actual child origin.
- No Admin token should be placed in the child preview URL.
- Use a browser with audio enabled. Browser user-activation policies may require one click before WebAudio is audible; treat that separately from production-path correctness.

## 2. Open / handshake

1. Open Space Typing Admin → Ships.
2. Confirm the **Production Visual Preview** frame becomes ready without opening the gameplay app in a second tab.
3. Confirm the frame URL is the fixed child `/admin-preview.html` route with only preview session/nonce transport data.
4. Confirm failure is visible and contained if the child origin is unavailable.
5. Confirm an unavailable preview does not change the active revision, PlayerSave, Shop state, or Media current.

Expected:

- Preview reports production renderer readiness.
- No Admin credential is exposed to the child frame.
- The Admin page remains usable if preview cannot connect.

## 3. Draft vs Published isolation

For one canonical Ship (start with Vanguard):

1. Select **Published** and note the current image, visual profile and projectile recipe.
2. Switch to **Draft**.
3. Change one or more visual controls without saving.
4. Change Ship Image and/or Projectile Recipe without saving.
5. Confirm Draft preview changes.
6. Switch back to Published.
7. Confirm Published preview still renders the active revision and did not inherit unsaved Draft changes.
8. Run **Validate Draft**.
9. Confirm Published still does not change.
10. Save Draft.
11. Confirm Published still does not change until the normal History / Publish lifecycle is completed.

Expected:

- Draft is ephemeral preview state.
- Published is sourced from the active revision separately.
- Validate/Save Draft never relabels or mutates Published preview state.

## 4. A5.2 exact Ship image assignment

For one Ship:

1. Confirm **Choose image** opens the existing Media V2 Asset Picker.
2. Confirm only image assets are selectable.
3. Select an immutable Media version.
4. Confirm Draft preview changes immediately.
5. Save Draft and reload the page; confirm the exact selected version is restored.
6. Confirm Published still uses the active revision until publish.
7. Publish through normal History / Publish, then start a new gameplay session and confirm production uses the selected exact version.
8. Create another Media version of the same logical asset. Confirm the published Ship does **not** silently follow it.
9. Roll back to a historical revision and confirm the historical exact version resolves.
10. Use **Clear** and confirm Draft preview restores bundled/original Ship art.

Negative checks:

- raw filesystem path is rejected;
- arbitrary URL is rejected;
- upload alone does not change gameplay;
- no implicit `latest` / `current` resolution substitutes for the persisted version.

## 5. A5.3 production projectile recipe binding

For at least Vanguard, Volt and Aegis:

1. Select **Draft** and **Fire**.
2. Change **Projectile Recipe** among visibly different recipes such as `spear`, `electric`, `heavy`, `barrage` and `cosmic`.
3. Confirm the Fire preview changes immediately without saving.
4. Confirm the selected recipe changes the complete production presentation as one semantic unit: muzzle/trail/sprite/motion/impact geometry according to that recipe.
5. Confirm there are no independent writable controls for muzzle position, trail internals, raw projectile sprite path, impact geometry or a fake Weapon entity.
6. Save Draft and reload; confirm the recipe binding survives.
7. Confirm Published remains unchanged until publish.
8. Publish and start a new gameplay session; confirm production gameplay uses the published recipe.
9. Roll back and confirm the historical recipe is restored.

Expected:

- Fire uses the child production `PlayerShotSystem`.
- `ships.<id>.projectileArchetype` is the only A5.3 writable projectile binding currently exposed.
- Recipe internals remain derived/read-only.

## 6. A5.3 projectile audio parity

With browser audio enabled:

1. Use the Fire preview with bundled Vanguard `spear`; listen for production launch + crystal-like impact cue.
2. Change recipe to `electric`; confirm impact sound changes to the production `storm` identity along with the recipe.
3. Change recipe to `heavy`; confirm impact sound changes to the production `heavy` identity.
4. Try several other recipes and compare preview audio with the equivalent production gameplay projectile.
5. Confirm the launch cue is the normal production generic `Sfx.shot()` behavior.
6. Confirm Admin does **not** expose a separate `impactSfxAssetVersionId`, `launchSfxAssetVersionId`, arbitrary sound path, or arbitrary sound URL.

Expected:

- Impact audio is recipe-derived and cannot drift into an invalid visual/sound combination.
- Launch audio is production-backed but read-only because it is a generic cue shared by multiple gameplay flows.
- Browser autoplay/user-activation policy may gate audibility before first interaction; that alone is not a runtime binding failure.

## 7. Production scenario parity

For the same Ship, test both Draft and Published sources:

- **Idle** — compare silhouette, colors, glow/core, engine count, proportions and selected Ship image with gameplay production rendering.
- **Move** — compare engine/boost presentation with gameplay production rendering.
- **Fire** — compare muzzle origin, projectile identity, trail, impact presentation and production audio with gameplay production rendering.

Expected:

- Ship rendering comes from the child production `drawCharacterShip()` path.
- Fire uses production `PlayerShotSystem` + production `Sfx` paths; there is no invented writable Weapon domain.
- Scenario state such as boost/recoil remains runtime scenario input, not persisted Ship authoring data.

## 8. High-frequency tuning

1. Drag/type rapidly through visual values where the browser emits many `input` events.
2. Switch images/recipes several times in normal UI cadence.
3. Watch the preview for several seconds.
4. Confirm it follows the latest Draft state without visibly replaying a long queue of stale candidates.
5. Confirm the Portal remains responsive.

Expected:

- Candidate updates are coalesced to animation frames.
- Stale UI generations do not overwrite the latest status.

## 9. Route lifecycle / cleanup

Repeat at least 20 times:

1. Open Ships.
2. Wait for preview READY.
3. Switch Ship and scenarios a few times.
4. Navigate to another Admin route.
5. Navigate back to Ships.

Observe browser task manager/devtools if convenient.

Expected:

- Only one active preview iframe exists after returning.
- No duplicate message/audio behavior.
- No continuously growing CPU usage from leaked RAF loops.
- No accumulating pending preview commands after route removal.
- Old preview iframe/listeners/audio resources are removed.

## 10. Security negative checks

Using devtools or a small local harness if needed:

- Message from wrong origin → ignored.
- Message from wrong `event.source` → ignored.
- Wrong protocol version → ignored/rejected.
- Wrong preview session/nonce → ignored/rejected.
- Duplicate/stale request ID → child rejects according to protocol.
- Unexpected response type for a pending command → parent rejects it.
- Arbitrary candidate URL/path does not become iframe `src`.
- Preview candidate cannot provide an arbitrary script/module URL.
- Projectile recipe cannot carry arbitrary projectile image/audio path or URL.

## 11. Revision / CAS behavior

1. Keep Ships page open on active revision A.
2. Publish another revision from a separate Admin flow if convenient.
3. Attempt Save Draft from the stale Ships page.

Expected:

- Existing active-revision CAS protection rejects stale overwrite.
- Preview transport does not bypass Revision/History semantics.

## 12. Skill/VFX boundary check

Confirm the current Admin does **not** present writable generic VFX CRUD or a free-form Skill `effectPreset` merely because production has `SkillFxSystem` effects.

Expected:

- existing Skill gameplay policy remains authorable where already canonical;
- Skill media/VFX binding remains marked migration-required until a persisted binding + validator + resolver + production consumer + production preview chain exists.

## 13. 3D relief status — A5.4 prerequisite

Do **not** treat arbitrary GLB or animated GLB as supported.

Current production 3D path is generated relief. A5.4 must first prove:

- exact immutable bundle representation/resolution;
- strict manifest/component validation;
- production `loadReliefShip()` / `DuelShip3D` consumption;
- repeated Admin mount/switch/unmount cleanup for geometry/material/texture/WebGL resources;
- cache ownership compatible with preview lifecycle.

These are A5.4 prerequisites, not a reason to create a raw path/URL or Portal-only 3D authoring shortcut.

## 14. Result log template

Copy this block for each manual pass:

```text
Date:
Parent SHA:
Child SHA:
Browser / machine:
Draft vs Published: PASS / FAIL / NOT RUN
Ship exact Media assignment: PASS / FAIL / NOT RUN
Exact-version reload/rollback: PASS / FAIL / NOT RUN
Projectile recipe binding: PASS / FAIL / NOT RUN
Projectile launch/impact audio parity: PASS / FAIL / NOT RUN
Idle parity: PASS / FAIL / NOT RUN
Move parity: PASS / FAIL / NOT RUN
Fire parity: PASS / FAIL / NOT RUN
High-frequency tuning: PASS / FAIL / NOT RUN
Route cleanup x20: PASS / FAIL / NOT RUN
Security negative checks: PASS / FAIL / NOT RUN
Revision/CAS: PASS / FAIL / NOT RUN
Skill/VFX boundary: PASS / FAIL / NOT RUN
Notes / defects:
```
