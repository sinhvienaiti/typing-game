# Space Typing Admin Asset Tuning — Progress / Handoff

Last updated: 2026-10-13

## Status

**A5.0 — Runtime Capability Matrix + Production Preview Harness: AUTOMATED CODE GATE GREEN**

A5.0 implementation is complete for the supported Ship procedural visual slice. Manual visual/lifecycle acceptance remains intentionally non-blocking and is tracked separately in `docs/SPACE_TYPING_ADMIN_ASSET_TUNING_MANUAL_ACCEPTANCE.md`.

Do not broaden this status into claims that 2D Media assignment, relief-3D assignment, arbitrary GLB, animated GLB, generic VFX authoring, generic SFX authoring, or a Weapon Admin entity are supported. They remain classified conservatively by the child executable capability matrix.

## Source of truth

### Parent Admin

- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- A5 code baseline: `99d9fecb22bb29bbd72009694992c324f620d308`
- Manual acceptance checkpoint: `20f2d0e30132653ec996d54bc9251d1358c49f94`
- PR: `#49`

### Child runtime

- Repo: `sinhvienaiti/space-typing`
- Runtime branch: `feat/bgv-integration-current`
- A5 runtime authority HEAD: `6f08e0905e9b13b8fb7204dba4db6b0cd8e28889`
- Latest child A5 commit: `test(admin): lock canonical Ship visual preview capability`

### Parent submodule reconciliation

The parent branch currently pins `games/space-typing` to historical child SHA:

`dbd7348daf23a7e8ef3d804c23205e22f82407f1`

This gitlink is **not** the A5 child runtime authority. A5 preview runs cross-origin through the canonical `/games.json` entry and the child-owned `/admin-preview.html` route; the parent Portal does not import the A5 production renderer from the parent submodule checkout.

Therefore:

- do **not** reset/revert `feat/bgv-integration-current` to `dbd7348...`;
- do **not** treat the parent gitlink as evidence that A5 child work is absent;
- do **not** fabricate a gitlink update through a normal file-content API;
- when a deliberate integration/submodule reconciliation milestone is performed later, compare the then-current child integration target and update the gitlink explicitly as its own operation.

Until that deliberate reconciliation, the A5 runtime source of truth is the child branch/HEAD above.

## Automated evidence

### Child

Child CI run `#1990` at `6f08e090...` passed the relevant suite, including:

- unit tests;
- Admin preview bridge smoke;
- strict TypeScript/Vite build;
- R01 browser QA.

### Parent A5-specific gate

Dedicated workflow: `.github/workflows/admin-a5-preview-ci.yml`

At code checkpoint `99d9fec...`:

- push run `#5` / run id `38397264145`: PASS;
- PR run `#6` / run id `38397272362`: PASS.

The A5 gate executes:

1. `scripts/validate-space-admin-asset-preview.mjs`;
2. root dependency install required by the Portal Vite build configuration;
3. Portal dependency install;
4. strict `pnpm --dir portal build` (`tsc --noEmit && vite build`).

An earlier workflow-only failure was traced to missing root `vosk-browser` installation. The preview validator itself passed. The workflow was corrected without weakening protocol/security assertions.

### Parent general Admin CI

The production preview integration previously passed full Space Typing Admin CI at parent checkpoint `86a03bcc3094cc0b374f510edd4037fdd8a684b2`.

At the time this progress document was prepared, the full Admin CI triggered by docs-only checkpoint `20f2d0e...` was still running. That does not invalidate the green A5 code gate above; re-check the newest branch CI before any future handoff claims that *all* branch workflows are green.

## A5.0 implementation completed

### A5.0.1 — Runtime capability matrix

Child executable matrix: `src/admin/asset-tuning-capabilities.ts`.

Every candidate field/domain is classified as one of:

- `SUPPORTED NOW`
- `REQUIRES CANONICAL MIGRATION`
- `READ-ONLY REFERENCE`
- `DEFERRED / UNSUPPORTED`

`SUPPORTED NOW` requires a complete named chain:

persisted field → validator → runtime resolver → production consumer → preview consumer → apply boundary.

### A5.0.2 — Ship runtime authority

Canonical Ship visual override now reaches the same visual resolver used by the production renderer.

The production path remains `drawCharacterShip()`; the Admin preview does not maintain a copied Ship renderer.

### A5.0.3 — Isolated child preview protocol

Child protocol v1 includes:

- `READY`
- `LOAD_CANDIDATE`
- `SET_SCENARIO`
- `SET_TUNING`
- `PAUSE`
- `RESET`
- `DISPOSE`
- `APPLIED`
- `ERROR`
- `DISPOSED`

Security/lifecycle properties include:

- exact parent origin;
- exact `event.source`;
- protocol version;
- CSPRNG session + nonce;
- monotonic request IDs;
- strict candidate parsing;
- fail-closed response typing;
- listener/RAF/pending-request cleanup.

### A5.0.4 — Production visual harness

Child has a dedicated `admin-preview.html` build entry.

The harness uses:

- production `drawCharacterShip()`;
- production `PlayerShotSystem` for Fire;
- scoped ephemeral candidate state;
- no mutation of the active gameplay Ship runtime session.

Supported scenarios:

- Idle
- Move
- Fire

Fire is explicitly the existing production Ship projectile path. A writable Weapon domain was **not** invented.

### A5.0.5 — Parent secure transport

Parent bridge: `portal/src/admin/space-typing-asset-preview.ts`.

It:

- resolves the child origin through canonical `/games.json` entry `space-typing`;
- uses only fixed child route `/admin-preview.html`;
- does not accept an arbitrary script/module/iframe URL from Admin form state;
- does not pass Admin credentials to the child;
- checks exact child origin/source/session/nonce;
- rejects response-type mismatches;
- removes iframe/listeners and rejects pending work on teardown.

### A5.0.6 — Draft vs Published preview isolation

The Ships Admin page exposes separate preview sources:

- **Draft** — current in-memory candidate including unsaved visual changes;
- **Published** — separately materialized active revision.

`Validate Draft` and `Save Draft` do not overwrite/relabel Published preview state.

Normal Revision/History/Publish semantics remain authoritative for runtime changes.

### A5.0.7 — High-frequency update coalescing

Ship candidate updates are coalesced to at most one `LOAD_CANDIDATE` command per animation frame.

Route teardown cancels a queued animation frame and rejects queued waiters. UI generation guards prevent stale preview operations from overwriting the latest status or continuing into a stale scenario update.

### A5.0.8 — Exact Media runtime bridge

Parent has an exact-version Media runtime resolver/HTTP bridge; child has strict exact-version Media response validation.

Guardrail remains:

- runtime binding must pin exact immutable `assetVersionId`;
- upload alone does not change gameplay;
- no silent `current` / `latest` resolution may substitute for a pinned version.

This does **not** mean every domain already has a writable Media binding field.

### A5.0.9 — Manual acceptance separated from implementation blockers

Manual checklist:

`docs/SPACE_TYPING_ADMIN_ASSET_TUNING_MANUAL_ACCEPTANCE.md`

It covers:

- Draft vs Published isolation;
- production Idle/Move/Fire parity;
- rapid tuning responsiveness;
- route cleanup repeated 20 times;
- security negative checks;
- revision/CAS behavior;
- exact Media semantics.

Failures found there become follow-up defects; an unperformed manual check does not block independent A5 work.

### A5.0.10 — Conservative 3D boundary

Current child 3D runtime is generated relief, not arbitrary GLB.

The current relief path remains `READ-ONLY REFERENCE` in A5.0. Exact-version relief assignment remains `REQUIRES CANONICAL MIGRATION`. Arbitrary and animated GLB remain `DEFERRED / UNSUPPORTED`.

Audit found A5.4 lifecycle prerequisites before repeated Admin 3D mount/switch/unmount can be called clean:

- `DuelShip3D.dispose()` does not yet prove explicit geometry/material/texture cleanup;
- module-level 3D load caching must be reconciled with repeated Admin preview lifecycle;
- no canonical arbitrary-GLB/skeletal-animation semantic runtime exists yet.

Do not bypass those gaps with a second preview-only renderer.

## A5.0 exit-gate assessment

| Gate | Status | Evidence |
| --- | --- | --- |
| No writable field missing production consumer | PASS | executable child capability matrix |
| One real field chain end-to-end | PASS | Ship procedural visual profile |
| Preview uses production path | PASS | `drawCharacterShip()` + `PlayerShotSystem` |
| Preview is non-mutating | PASS by automated architecture/tests | scoped child candidate + Draft/Published isolation |
| Protocol/security is fail closed | PASS | child tests + parent static regression gate + strict build |
| Lifecycle cleanup implemented | PASS by automated implementation; manual stress pending | resource scopes + route teardown + manual x20 checklist |
| Branch/source reconciliation documented | PASS | this document |
| Exact Media semantics preserved | PASS | exact-version resolver/validator; no current/latest fallback |

Result: **A5.0 automated implementation gate is green.**

Manual visual/stress acceptance remains an explicit non-blocking checklist rather than a false automated claim.

## Capability decisions carried forward

### Supported now

- Ship procedural/profile visual fields already owned by canonical Ship policy.
- Existing Skill gameplay policy remains supported independently of A5 media/VFX authoring.

### Requires canonical migration

- per-Ship 2D Media assignment;
- persistent presentation scale/offset/rotation/pivot fields;
- exact-version relief 3D assignment;
- projectile profile authoring;
- Skill Media/VFX binding.

### Read-only reference

- gameplay aim/recoil/boost scenario state;
- current generated relief 3D runtime;
- current production projectile trail/impact behavior;
- current production VFX;
- current sample-backed/synthesized SFX.

### Deferred / unsupported

- arbitrary GLB;
- animated GLB semantic clips before a production animation runtime exists;
- generic uploaded-image VFX authoring;
- unproven writable Weapon Admin entity.

## First unfinished unit

With A5.0 automated code gate green, the next implementation unit is:

**A5.1 — Shared Asset Tuning Studio shell**

Before implementing A5.1:

1. fetch latest parent and child HEADs again;
2. re-check latest CI;
3. read the A5.1 section of `docs/SPACE_TYPING_ADMIN_ASSET_TUNING_PREVIEW_PLAN.md`;
4. keep the shared Studio shell separate from domain-specific persistence;
5. only render controls backed by capability-matrix `SUPPORTED NOW` fields;
6. keep `REQUIRES CANONICAL MIGRATION`, `READ-ONLY REFERENCE`, and `DEFERRED / UNSUPPORTED` visible as capability state rather than silently turning them into writable form fields;
7. preserve Draft / Published / Revision / History semantics and the child production preview harness.

Do not jump directly to Ship 3D authoring or generic VFX/SFX CRUD.
