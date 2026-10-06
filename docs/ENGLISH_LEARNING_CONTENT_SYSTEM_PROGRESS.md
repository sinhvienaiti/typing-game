# English Learning Content System — Progress

Status: COMPLETE

## Current checkpoint

- Current HEAD before this checkpoint: `76f6538006961d1cf784e0c6ef0311687e4eb760`
- Current phase: E12 release/audit/maintenance foundation complete; mandatory implementation scope complete
- PR: #48 — open, draft
- Published runtime release: `2026.10.0`
- Latest verified CI for the pre-checkpoint HEAD:
  - English Content Full Validation #51 — PASS
  - English Content Master Plan Acceptance #31 — PASS
  - Platform CI #978 — PASS

## Completed mandatory milestones

- E00–E02 foundation/contracts: complete
- E03 controlled lexical pilot: complete — 300 lexemes + 300 linked primary senses + 300 usage sidecars
- E04 phrase/pattern runtime: complete for the current mandatory architecture — 1,710 published records
- E05 grammar framework/runtime: complete — 300/300 topics (45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2)
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — 1,513 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
- E07–E09 parent runtime, `/english` launcher, and game capability integrations: complete
- E10 controlled batch/review pipeline: complete and enforced
- E11 readiness reporting: complete; long-term corpus scale goals remain intentionally outside the current mandatory publication phase
- E12 release/audit/maintenance foundation: complete and enforced

## Published runtime snapshot

- dictionary: 900 records
- grammar: 300 records
- sentences: 3,401 records
- phrases: 1,710 records
- total published rich records: 6,311
- attribution runtime: 4 source records
- editorial ledger: 6,311 decisions / 6,311 applied / 6,311 publish decisions

## Quality gates

The latest verified pre-checkpoint HEAD passes the required publication gates represented by the English content validation/acceptance workflows and Platform CI, including strict schema/provenance/license/reference/dedup/reproducibility/runtime checks. Publication remains review-gated; candidate/authoring data must not bypass reviewed promotion.

## Current milestone

`COMPLETE` — no unfinished mandatory milestone remains in the current master-plan implementation phase.

## Remaining mandatory milestones

None.

## Intentional continuation / non-blocking scale work

These are quality-first continuation tracks, not blockers for the current mandatory implementation phase:

1. Improve E04 example linkage only when valid reviewed evidence exists; do not auto-link unsafe lemma-only candidates.
2. Grow long-term E11 corpus scale targets gradually through new reviewed batches under the existing provenance/license/review/dedup/runtime gates.
3. Add source-specific importers only after exact source/version/license obligations are pinned.
4. Preserve the legacy `shared/vocabulary/levels/*.json` ABI unless a separate compatibility migration is explicitly approved.

## Blocker

None.

## Next actionable task

No mandatory implementation task remains. Future work should begin only from a newly approved reviewed batch, evidence-backed E04 enrichment, or an explicitly approved new master-plan scope. Every future run must first verify the latest branch HEAD and CI before doing work and must skip already completed artifacts.
