# Space Typing Admin Asset Tuning — Manual Acceptance

> Scope: A5 production preview acceptance only. This checklist is intentionally non-blocking for independent implementation work. Record failures here and fix them as follow-up defects; do not use an unperformed manual check as a reason to stop unrelated A5 work.

## 1. Preconditions

- Parent repo: `sinhvienaiti/typing-game`, branch `feat/space-typing-admin-uiux`.
- Child runtime: `sinhvienaiti/space-typing`, branch `feat/bgv-integration-current`.
- Portal origin and Space Typing origin must both be available through the local HTTPS setup.
- `/games.json` must resolve `space-typing` to the actual child origin.
- No Admin token should be placed in the child preview URL.

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

1. Select **Published** and note the current silhouette/colors/engine layout.
2. Switch to **Draft**.
3. Change `primary`, `secondary`, `accent`, `wingSpan`, `bodyLength`, and `engineCount` without saving.
4. Confirm Draft preview changes.
5. Switch back to Published.
6. Confirm Published preview still renders the active revision and did not inherit unsaved Draft changes.
7. Run **Validate Draft**.
8. Confirm Published still does not change.
9. Save Draft.
10. Confirm Published still does not change until the normal History / Publish lifecycle is completed.

Expected:

- Draft is ephemeral preview state.
- Published is sourced from the active revision separately.
- Validate/Save Draft never relabels or mutates Published preview state.

## 4. Production scenario parity

For the same Ship, test both Draft and Published sources:

- **Idle** — compare silhouette, colors, glow/core, engine count and proportions with gameplay production rendering.
- **Move** — compare engine/boost presentation with gameplay production rendering.
- **Fire** — compare muzzle origin, projectile identity, trail and impact presentation with gameplay production rendering.

Expected:

- Ship rendering comes from the child production `drawCharacterShip()` path.
- Fire uses the production `PlayerShotSystem`; there is no invented writable Weapon domain.
- Scenario state such as boost/recoil remains runtime scenario input, not persisted Ship authoring data.

## 5. High-frequency tuning

1. Drag/type rapidly through visual values where the browser emits many `input` events.
2. Watch the preview for several seconds.
3. Confirm it follows the latest Draft state without visibly replaying a long queue of stale candidates.
4. Confirm the Portal remains responsive.

Expected:

- Candidate updates are coalesced to animation frames.
- Stale UI generations do not overwrite the latest status.

## 6. Route lifecycle / cleanup

Repeat at least 20 times:

1. Open Ships.
2. Wait for preview READY.
3. Switch Ship and scenarios a few times.
4. Navigate to another Admin route.
5. Navigate back to Ships.

Observe browser task manager/devtools if convenient.

Expected:

- Only one active preview iframe exists after returning.
- No duplicate message behavior.
- No continuously growing CPU usage from leaked RAF loops.
- No accumulating pending preview commands after route removal.
- Old preview iframe/listeners are removed.

## 7. Security negative checks

Using devtools or a small local harness if needed:

- Message from wrong origin → ignored.
- Message from wrong `event.source` → ignored.
- Wrong protocol version → ignored/rejected.
- Wrong preview session/nonce → ignored/rejected.
- Duplicate/stale request ID → child rejects according to protocol.
- Unexpected response type for a pending command → parent rejects it.
- Arbitrary candidate URL/path does not become iframe `src`.
- Preview candidate cannot provide an arbitrary script/module URL.

## 8. Revision behavior

1. Keep Ships page open on active revision A.
2. Publish another revision from a separate Admin flow if convenient.
3. Attempt Save Draft from the stale Ships page.

Expected:

- Existing active-revision CAS protection rejects stale overwrite.
- Preview transport does not bypass Revision/History semantics.

## 9. Exact Media semantics

This is a guardrail check, not a request to create new writable fields:

- Uploading a Media version alone must not change gameplay.
- Any future runtime Media binding must pin an exact immutable `assetVersionId`.
- Preview/runtime must not silently resolve `current`/`latest` in place of the pinned version.

## 10. 3D relief status — deferred from A5.0 manual gate

Do **not** mark repeated 3D mount/switch/unmount as A5.0 acceptance yet.

Current production 3D path is generated relief. The audited child runtime still has lifecycle work before it is safe for an Admin stress loop:

- `DuelShip3D.dispose()` currently disposes the renderer but does not yet prove full geometry/material/texture cleanup.
- module-level 3D load caching must be reconciled with repeated Admin mount/unmount behavior.
- arbitrary GLB and animated GLB semantic clips remain unsupported until a real production runtime exists.

These are A5.4 prerequisites, not a reason to fake a 3D authoring capability in A5.0.

## 11. Result log template

Copy this block for each manual pass:

```text
Date:
Parent SHA:
Child SHA:
Browser / machine:
Draft vs Published: PASS / FAIL / NOT RUN
Idle parity: PASS / FAIL / NOT RUN
Move parity: PASS / FAIL / NOT RUN
Fire parity: PASS / FAIL / NOT RUN
High-frequency tuning: PASS / FAIL / NOT RUN
Route cleanup x20: PASS / FAIL / NOT RUN
Security negative checks: PASS / FAIL / NOT RUN
Revision/CAS: PASS / FAIL / NOT RUN
Notes / defects:
```
