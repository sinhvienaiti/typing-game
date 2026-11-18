# Space Typing Admin — A8 Expedition Stage Runtime Checkpoint

Updated: 2026-10-14

## Status

**A8 Expedition Stage Runtime Boundary: COMPLETE**

Child runtime checkpoint:

- repo: `sinhvienaiti/space-typing`
- branch: `feat/bgv-integration-current`
- commit: `8e1c3844faed0de1da721d8db8115712a56d311c`
- commit message: `fix(expedition): freeze stage runtime policy per run`
- fresh child CI: `#2047` / run `38556868873` — **PASS**

## Closed regression

An Expedition run persisted under Stage Admin policy A can no longer inherit a later Published Stage policy B after reload/resume.

The durable boundary is now:

`Published/page Stage runtime → first Expedition persist freezes snapshot → browser-local Expedition envelope → encounter arms frozen snapshot → production createStageConfig consumes snapshot once`

Guaranteed behavior:

1. existing persisted/resumed run keeps its frozen Stage runtime snapshot;
2. a new run created after a newer Publish captures the newer page/session policy;
3. legacy saves with no Stage snapshot fail closed to bundled/default Stage configuration rather than inheriting current Published state;
4. snapshot survives Expedition persistence round-trip;
5. the Expedition override is one-shot at Stage factory consumption, so normal Campaign creation continues to use the current immutable page-session Published policy;
6. Admin Expedition remains read-only and browser-save-owned; no fake remote mutation backend was introduced.

## Regression evidence

Child production changes:

- `src/admin/stage-runtime-policy.ts`
- `src/expedition/store.ts`

Child regression test:

- `tests/expedition-stage-runtime-snapshot.test.ts`

Fresh CI #2047 passed child tests, strict build, Expedition audit and R01 browser QA.

## Parent ownership audit

The parent pin must advance to the exact child checkpoint above. `scripts/validate-space-admin-expedition.mjs` and `scripts/validate-space-admin-a8-world-stage-content.mjs` must retain exact-SHA guards and explicitly audit the new frozen-snapshot production semantics; changing only the SHA without semantic assertions is not accepted.

Historical/inaccessible CI logs remain non-blocking under `docs/SPACE_TYPING_CI_CONTINUATION_POLICY.md`. Use each new safe commit as the next diagnostic checkpoint.

## Continuation

The older `SPACE_TYPING_ADMIN_ASSET_TUNING_PROGRESS.md` pointer to `A7.0` is stale: A7 and the A8 World/Stage authority work are already present in the current parent history. Do not restart A7 from that pointer.

After this parent checkpoint is green, re-audit current Git state and continue the first genuinely unfinished technical unit. Manual browser QA remains a later acceptance activity and does not block safe implementation.
