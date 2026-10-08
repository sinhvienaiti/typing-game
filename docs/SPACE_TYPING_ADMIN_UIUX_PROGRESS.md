# Space Typing Admin UI/UX Progress

## PROJECT STATE
STATUS: IN_PROGRESS

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- Validated implementation HEAD before this metadata checkpoint: `d088e554b2a62d588ffab67ff7c068df41db444b`
- PR: #49 — OPEN, DRAFT
- Space Typing Admin CI run `37744985962` (#489): PASS on `d088e554b2a62d588ffab67ff7c068df41db444b`.
- Platform CI run `37744985956` (#1426): PASS on `d088e554b2a62d588ffab67ff7c068df41db444b`.

Child:
- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- Validated HEAD: `3435ca12b447ee11c28d3cbe8f8d63d885d8cbf9`
- Child CI run `37740600521` (#1753): PASS.
- Parent `games/space-typing` is pinned to exactly that tested child SHA.

## COMPLETED MILESTONES
The following slices are confirmed present by current Git state and the full Admin/Platform validation chain; do not redo them unless a later commit regresses them:
- B06.1 Ships — DONE
- B06.2 Equipment — DONE
- B06.3 Skills — DONE
- B06.4 Enemies — DONE
- B06.5 Bosses — DONE
- B06.6 Worlds & Stages — DONE
- Mandatory Typing Content — DONE
- Shop / economy runtime ownership slice — DONE
- Currencies — DONE
- Rewards & Drops runtime contract slice — DONE
- Warp economy — DONE
- Missions — DONE
- Feature Gates — DONE
- Events — DONE
- Duel — DONE
- Ranked — DONE
- Alternative Modes — DONE
- Backgrounds — DONE
- VFX — DONE

## BACKGROUNDS — CLOSED CHECKPOINT
- Child owns the runtime-backed Backgrounds contract, runtime loader integration, contract test, and audit.
- The audit follows the real call chain `stage.ts -> fetchKit() -> parseKit()` rather than adding fake production imports/calls.
- The parent integration gap discovered during VFX work is now closed: `/admin/space-typing/backgrounds` is routed to the Phase B runtime-backed screen and `/api/admin/space-typing/backgrounds/contract` is exposed through the authenticated Admin service.
- Backgrounds remains runtime-backed/read-only because no truthful Admin write/apply boundary exists.

## VFX — CLOSED CHECKPOINT
- Child commit `c444b5f1d2bf873a1e6ad368746c095f11cf3c24` added the runtime-backed VFX contract; `3435ca12b447ee11c28d3cbe8f8d63d885d8cbf9` fixed the canonical quality mapping audit.
- Canonical VFX ownership is `Game.ts` plus production VFX systems (`CombatFxSystem`, `SkillFxSystem`, player/enemy projectile systems and related screen feedback) with visual-quality budgets owned by `src/performance/quality.ts`.
- There is no standalone runtime-consumed VFX authoring manifest, persistence seam, or safe apply boundary. Therefore the Admin surface is intentionally `runtime-derived-readonly`; no fake profile CRUD, sliders, Save Draft, Publish, or write endpoint was added.
- Child contract exposes real quality tiers/profiles, combat limits/events, VFX domains, runtime sources and ownership with `writeCapability=false`, `adminPreviewWriteCapability=false`, `authorableFields=[]`, and `applyBoundary=none`.
- Parent now exposes authenticated `/api/admin/space-typing/vfx/contract`, routes `/admin/space-typing/vfx` to the runtime-backed Phase B screen, and validates the exact child SHA plus the no-write boundary.
- Parent Backgrounds and VFX routes now take precedence over the older prototype/mock implementations in the extended UI layer.
- Advancing the child pin changed only VFX contract/audit/test/CI files. Shop and Currencies were re-audited against that exact diff; only their intentional audited-SHA checkpoints/assertions were refreshed. Guard behavior was not weakened.

## QUALITY GATES AT VFX CLOSE
Child:
- Full child test suite: PASS.
- Existing Warp/Missions/Feature Gates/Events/Duel/Ranked/Alternative Modes/Backgrounds audits: PASS.
- VFX contract test/audit: PASS.
- Canonical build: PASS.
- CI: `37740600521` (#1753) — PASS on `3435ca12b447ee11c28d3cbe8f8d63d885d8cbf9`.

Parent:
- Admin contract snapshot + exact child pin validation: PASS.
- Complete Admin UI scope + Phase B mapping: PASS.
- Shop/Currencies/Rewards/Warp/Missions/Feature Gates/Events/Duel/Ranked/Alternative Modes/Audio validators: PASS.
- Immutable revision/CAS tests and canonical preview bridges: PASS.
- Space Typing tests and child audits: PASS.
- Space Typing build: PASS.
- Portal build: PASS.
- Space Typing Admin CI: `37744985962` (#489) — PASS.
- Platform CI: `37744985956` (#1426) — PASS.

## CURRENT MILESTONE
**UI Assets** — next mandatory B10 Visuals milestone after Backgrounds and VFX.

## UI ASSETS STARTING RULES
The current route/domain map labels UI Assets as an authored asset manifest with a new-scene boundary, but this is a planning assumption, not permission to invent a new runtime adapter. The child runtime remains source of truth.

Before implementation:
- trace the real UI/HUD/icon/sprite/font asset owners and loaders;
- identify actual gameplay consumers and scene/lifecycle boundaries;
- determine whether a runtime-consumed canonical manifest exists;
- classify candidate fields as authorable, runtime-backed read-only, or unsupported;
- only expose write capability if a real persistence + loader + apply boundary exists.

If no real authorable boundary exists, use the established Backgrounds/VFX pattern: child-owned runtime contract + audit/test + read-only Admin diagnostics/control plane. Do not create mock upload/edit/save behavior.

## CURRENT BLOCKER
NONE. VFX is closed and green. UI Assets audit is next.

## NEXT EXACT ACTION
1. Fetch latest parent and child HEADs before every edit; preserve newer worker commits.
2. Audit child UI asset ownership/loaders/consumers: UI/HUD renderers, icons/textures/sprites, generated/static assets, fonts, `import.meta.glob`/registries, `Game.ts` call sites and scene lifecycle.
3. Determine whether a real authored manifest and safe apply boundary exist.
4. Implement the smallest truthful child contract/audit/test for UI Assets.
5. Run full child tests/audits/build and require exact green child SHA before parent pin.
6. Pin parent only after child green; wire authenticated API + Phase B UI + validator/map based on proven ownership.
7. Re-audit any intentional exact-child-SHA guards after the pin without weakening them.
8. Run full Parent Admin CI + Platform CI, update this checkpoint, then continue to isolated QA capability and finally Overview/Analytics telemetry adapters.

## STATUS
`IN_PROGRESS` — Backgrounds and VFX are CLOSED/DONE; UI Assets is the active milestone.
