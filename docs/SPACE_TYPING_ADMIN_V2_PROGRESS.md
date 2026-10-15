# Space Typing Admin V2 — Progress

> Current execution tracker for `docs/SPACE_TYPING_ADMINISTRATOR_ADMIN_V2_MASTER_PLAN.md`.
>
> The Master Plan is the product/design source of truth. This file records what is actually implemented on the active integration branches. Checkpoint SHAs are informational: every worker must fetch latest parent/child HEAD before editing and must never reset newer work to a checkpoint.

## Current source of truth — 2026-10-15

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- Latest HEAD at this progress refresh: `f743799233406e8cea15e98d04741aa0ef0e65f9`
- PR #49 remains **DRAFT**. Do not mark Ready or merge without explicit human instruction.

Child:
- Repo: `sinhvienaiti/space-typing`
- Active Admin V2/runtime integration branch: `feat/bgv-integration-current`
- Current audited/pinned preview runtime: `6c57a2b7340b96a41e0f9f2b6fb5143ca532fd1c`
- Parent local tooling must preserve the exact gitlink by default. Following a child branch is opt-in only.

Historical child branches such as `feat/admin-world-music-stage-policy` are evidence/reference only. Do not switch back, reset, merge or overwrite newer integration work merely because an older document names them.

---

## Execution state

The roadmap has advanced beyond the old A4/A5 historical tracker. **Do not restart A0–A10.** Current implementation sequence executed from the 2026-10-14 override is:

`A10.5 → A11 → A12 → A13 → A14 → A15 → A16 → A17`

Current status:

| Phase | State | Current result |
| --- | --- | --- |
| A0–A10 | IMPLEMENTED / retained | Earlier architecture, Media, Shop/economy, Ships, Skills/Equipment, Enemies/Bosses, Worlds/Stages, Audio/VFX and economy work remains canonical subject to current validators. |
| A10.5 | IMPLEMENTED | Shared Production Preview foundation plus combat, world/stage and VFX core retrofit; preview coverage classified deliberately. |
| A11 | IMPLEMENTED | Runtime-owned Live Ops control plane; Shop-owned merchandising reused; scheduling/announcements fail closed when no canonical service exists. |
| A12 | IMPLEMENTED | Duel production room simulation; Ranked/Alternative Modes remain truthful read-only/fail-closed where authority is absent. |
| A13 | IMPLEMENTED | Server-side role templates/effective permissions, dangerous-permission emphasis and role-aware UI/action gates. |
| A14 | IMPLEMENTED | Human-readable History/Publish with audit attribution, before→after summaries and preserved CAS validation. |
| A15 | IMPLEMENTED | Runtime Inspector, Contract Inspector, Validation, Asset Diagnostics and QA Sandbox consolidated in permission-gated Developer Tools. |
| A16 | IMPLEMENTED | Accessibility/responsive/reduced-motion and production-preview keyboard/fullscreen/teardown polish. |
| A17 | PREPARED; MANUAL QUEUED | 25 task-based acceptance scenarios are executable/documented. Automated evidence is being wired into CI; browser/manual cases remain QUEUED and are not falsely marked PASS. |

---

## A10.5 — Production Preview Foundation + Core Retrofit

Locked architecture:

`Draft/Published → ProductionPreviewBridge → Domain Preview Adapter → CHILD PRODUCTION RENDERER/RUNTIME`

Completed properties:
- child gitlink safety in bootstrap/local development;
- shared Preview bridge/studio lifecycle rather than Ship-only infrastructure;
- Draft/Published candidates, replay/reset and stale-generation cancellation;
- explicit dispose/teardown and isolated iframe transport;
- Ships remains the reference production preview;
- Enemies/Bosses use child production drawing/VFX scenarios supported by runtime;
- Skills use production `SkillEngine` state simulation;
- Equipment uses production `resolveEquipmentPerks` resolution;
- Worlds/Stages use child production preview renderer paths;
- VFX reuses representative Ship fire/projectile/impact production context instead of duplicating renderer logic;
- every route is classified intentionally as production/contextual/data/media/no-preview;
- unsupported visual/gameplay scenarios fail soft instead of being fabricated.

Important A10.5 commits include:
- `a93fac4c5e6148c9ff3478f63fed1b804306b36b` — Skill/Equipment runtime preview.
- `71f08a516bbf474abd491c56ceaa6cc013314217` — production combat VFX preview context.
- `780eddbd0875448c9c186d44602409d2c15a6325` — preview coverage classification.
- `0c78e57cce555cab22da58010887a59cf0b5dfc1` — Equipment effect-display correctness.
- `ff971d998ca5cd67e2159ca76be4a5a50174ae23` — production-preview coverage validator/workflow protection.

Child preview runtime used by the parent:
- `52a6d2a8408dfd26a21936795036df9c6ec5b160` — Skill/Equipment production runtime simulation.
- `6c57a2b7340b96a41e0f9f2b6fb5143ca532fd1c` — World/Stage production preview renderer and current child integration HEAD.

---

## A11–A16 completion checkpoints

- A11 Live Ops: `f73b4b46220151d178bcf0bc31b8dc745b48e94d`
- A12 PvP/Modes: `acccf79e5f90aa2481bcd2b5db566731bb72cd88`
- A13 Roles/Permissions: `b3bc43b67af6ec457e86d5a5149d45c79f011677`
- A14 History/Publish: `de033f43f5d84bd70639a99629600c2605935203`
- A15 Developer Tools cleanup: `5b9539b0263e7e3f25074f412795591247a2aff0`
- A16 UX/preview polish: `6fd3ca3ae2b94a9616418c4179756deb15355afc`

A13 details:
- role templates: Super Admin, Publisher, Content Editor, Media Manager, Developer/QA, Viewer;
- role assignment/overrides are server/deployment-owned (`TYPING_GAME_ADMIN_ROLE`, `TYPING_GAME_ADMIN_PERMISSION_OVERRIDES`);
- request/browser headers cannot elevate role;
- unknown roles resolve to no permissions;
- server mutation checks remain authoritative; UI gating is only the usability layer.

A14 details:
- primary change review is grouped in administrator language with before→after values;
- actor/action/timestamp/result activity comes from the audit log;
- raw revision/path diagnostics move under Advanced;
- publish/rollback still use expected-active CAS and backend validation.

A15 details:
- technical screens are consolidated under permission-gated Developer Tools;
- writable normal workflows such as Ships and Music Library are not mislabeled developer-only;
- no fake backend/control plane was introduced while consolidating diagnostics.

A16 details:
- production preview controls are keyboard accessible;
- status is announced through `aria-live`;
- fullscreen state/listeners are cleaned up;
- responsive preview sizing and reduced-motion behavior are protected;
- async actions cannot resurrect disposed preview chrome.

---

## A17 — Acceptance preparation

Canonical checklist:
- `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

Current A17 preparation:
- 25 end-to-end scenarios, including all 22 Master Plan minimum tasks;
- each scenario records expected behavior and automated evidence;
- browser/visual cases are explicitly `MANUAL: QUEUED`;
- no manual PASS may be inferred from code inspection;
- `scripts/validate-space-admin-a17-acceptance.mjs` protects scenario coverage and A13–A16 safety evidence.

Manual testing remains non-blocking for independent implementation. It becomes release/Ready gating only when the user chooses to perform final acceptance or when a future change genuinely depends on a visual/manual observation.

---

## CI / validator state

Fresh CI after A16 exposed stale presentation/audit assumptions. Per project policy, inaccessible old logs are not blockers; fresh commits are used to reveal the next concrete failure.

CI triage already performed:
- re-audited child delta `4f62c94… → 6c57a2b…`; only isolated Admin preview modules changed, not Background/VFX ownership contracts;
- updated the visuals audited child pin without weakening ownership checks;
- migrated VFX validation to inspect the A10.5 wrapper + retained read-only contract surface instead of requiring old presentation banners in one file.

Recent CI-fix commits:
- `107bbf0e8868f6faf37c2420c478268694571bb2` — re-audit visuals against pinned preview runtime.
- `c29d970fb26795c2ad21d575c30a71ac28ad5517` — validate VFX retrofit through wrapper + legacy boundary.

At this progress refresh, Admin CI still reports the umbrella `Validate Admin contract snapshot` step failing; that step also chain-imports Music Library validation, so CI is being split/wired more granularly rather than guessing from an unavailable log. Do not treat this temporary red state as permission to weaken canonical ownership/CAS/media/preview validators.

---

## Safety rules that remain mandatory

- Fetch latest parent and child HEAD before every new implementation unit/commit series.
- Never reset/revert/overwrite newer worker code.
- Preserve the parent-pinned child gitlink unless explicit follow-branch mode is requested.
- Do not create fake remote users, fake scheduler services, fake player management or fake Ranked season services.
- Do not weaken validators to make CI green.
- Do not create Shop/Ships/Weapon shadow models disconnected from runtime.
- Do not expose raw filesystem asset paths as normal administrator editing controls.
- Media upload/replace must not implicitly mutate gameplay references.
- Production Preview must reuse child-owned renderer/runtime; do not copy rendering/VFX logic into Portal.
- Preview must not mutate active revision, PlayerSave, wallet, ownership, entitlement or progression.
- Manual QA remains queued/non-blocking until release acceptance, and must never be marked PASS without human execution.
- PR #49 remains DRAFT until explicit user instruction.
