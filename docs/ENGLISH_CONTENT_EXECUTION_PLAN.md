# English content — four sequential execution groups

User instruction: execute the twelve agreed work items as four groups of three. Review each step before starting the next; complete and review a group before entering the following group. A blocked or partially completed step is never a PASS.

## Review rules

- PASS requires the stated deliverable, explicit editorial/source review, applicable executable gates and current evidence. Candidate counts and published counts are distinct.
- Every content promotion requires source/version/license/provenance verification, grammar/naturalness/CEFR review, exact/near dedup, a digest-bound decision and compatible game runtime output.
- Reproduce affected artifacts, reconcile E10/E11/E12, then verify Full Validation, Master Plan Acceptance and Platform CI on the resulting branch HEAD.
- When a step is blocked, record the exact missing input and evidence. Later steps stay queued. Do not relax a checksum, invent a source, mass-publish unchecked records, or redefine a long-term target as completed tooling work.
- Resume from the latest remote HEAD and this plan together with `ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md`. Preserve existing reviewed work.

## Group 1 — current queue, example corpus, translation source

| Step | Deliverable and PASS criterion | Current reviewed state |
| --- | --- | --- |
| 1 | Review all 316 candidates remaining after Slice 29; publish only eligible records. Verify the final four-record slice and an exhausted next-review queue without replaying old records. All content/runtime/report/CI gates pass. | PASS — all 316 reviewed/published; three workflows passed on `565659b` |
| 2 | Expand reviewed, published examples to the agreed minimum of 100,000 using reproducible, licensed source intake. Source capacity, editorial quality and runtime counts must independently support the result. | IN PROGRESS — new pinned English-only intake and first editorial pilot integrated; 2,233 published examples. Candidate capacity is available; remaining editorial work is not approved. |
| 3 | Recover exact pinned Tatoeba EN/VI/link bytes, or complete a separately versioned, fully reviewed source upgrade with checksums, license and attribution. Import validation and reproducibility pass. | Queued behind Step 2; historical source bytes currently unavailable |

The default typing-text candidate queue is bounded at 1,000 candidates. Exhausting that queue is Step 1 completion, not exhaustion of all original passages and not completion of Step 2.

## Group 2 — translation and dialogue expansion

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 4 | At least 20,000 reviewed published translation pairs; validate alignment, translation quality, licensing, dedup and runtime. | Queued behind Group 1 |
| 5 | Add a reproducible, licensed dialogue source or reviewed source extension; pin bytes/version, verify attribution and provide an audited import pilot. The configured MultiWOZ lane is exhausted. | Queued behind Step 4 |
| 6 | At least 10,000 reviewed published dialogues, with speaker/turn/context integrity and game compatibility. | Queued behind Step 5 |

## Group 3 — exercise and error corpora

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 7 | At least 30,000 published cloze exercises with valid source sentences, target presence and unambiguous accepted answers. | Queued behind Group 2 |
| 8 | At least 10,000 published transformations; verify meaning preservation, target grammar and accepted alternatives. | Queued behind Step 7 |
| 9 | At least 2,000 published common-mistake records with reviewed corrections, explanations and grammar references. | Queued behind Step 8 |

## Group 4 — example linkage, game review, release

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 10 | Review the outstanding example-link debt (baseline: 4,992 collocations, 504 verb patterns, 4,159 phrase items without `exampleIds`). Add only semantically correct whole-phrase/frame evidence; document unresolved coverage. No unsafe lemma-only auto-linking. | Queued behind Group 3 |
| 11 | Exercise the actual English-content selection/display/play/result flows in the integrated games. Record findings and fix material issues; re-run affected checks. CI alone does not claim manual UI review. | Queued behind Step 10 |
| 12 | Complete PR review and release readiness; merge/release only after preceding review gates pass and final checks are current. | Queued behind Step 11; PR #48 remains Draft |

## Review evidence

Step 1 uses explicit decisions in `content/english/reviews/decisions.d/e06-typing-text-30-*.json` through `e06-typing-text-43-*.json`, authoring shards, generated runtime/manifests and E10/E11/E12 reports. The queue-tail fix is covered by `scripts/typing-text-review-core.test.mjs`, including CLI stale-packet replacement for partial and exhausted queues. Record final CI run links in PR #48; do not create a timestamp-only commit solely to move CI to another SHA.

## Step 1 sign-off and Step 2 capacity review

Step 1 passed on commit `565659b885ffe52e1abdcddfd93c97808e563334`:

- [Platform CI #3201](https://github.com/sinhvienaiti/typing-game/actions/runs/42333877164) — success.
- [Master Plan Acceptance #1312](https://github.com/sinhvienaiti/typing-game/actions/runs/42333877161) — success.
- [Full Validation #952](https://github.com/sinhvienaiti/typing-game/actions/runs/42333874055) — success.
- 90 content/tooling tests, 3 runtime-count tests, all 316 Monkeytype/Karaoke adapter checks, all 28 linked lexical references, exact/near dedup and deterministic artifact regeneration passed.

Step 2 was then assessed with `node scripts/audit-english-example-source-capacity.mjs`. The reproducible report is `content/english/reports/example-source-capacity.json`.

| Capacity measure | Count |
| --- | ---: |
| Reviewed published examples | 2,233 |
| Required minimum | 100,000 |
| Current published deficit | 97,767 |
| Eligible unique raw sentences in the current original-source lane | 5,588 |
| Raw sentences not yet reviewed | 4,588 |
| Optimistic published upper bound using only remaining original-source raw sentences | 6,821 |
| Additional source gap if restricted to that original lane | 93,179 |

The upper bound covers this configured source lane only. It is not an assertion that no other upstream dataset exists. Further local review is possible, but does not make the full Step 2 deliverable achievable from these inputs alone; future rejection/dedup can reduce the bound. Other upstream sources require a reproducible, licensed, reviewed intake before their potential size can be counted.

### Active continuation: pinned English-only Tatoeba lane

The original-lane shortage is no longer an overall stop condition. Four official 2026-10-31 exports were acquired and checksum-verified on 2026-11-07. A separately versioned offline extraction retains 122,212 English source-evidence candidates in five canonical shards. See `docs/TATOEBA_ENGLISH_INTAKE.md` and `content/english/sources/tatoeba-english-2026-10-31.json`. The historical EN/VI/link pin is unchanged.

Pilot 01 explicitly reviewed 24 records: 20 published, four rejected and two edited. The digest-bound ledger, controlled source and per-record review report retain all outcomes, original/final texts, CEFR rationales and attribution. Rejections include a threat and context/factual-scope problems despite positive experimental source ratings. The queue skips these decisions permanently.

After excluding controlled IDs/texts and exact source duplicates, 122,164 candidates remain available. Combined with the original-source remainder, the optimistic intake bound is 128,985 examples before further editorial rejection and cross-source near dedup. Candidate availability does not establish that all of those examples will pass. The capacity report is now version 2 with separate original and new-source lanes, `editorial-review-required`, and every transition gate still false.

Local validation: 111 content/tooling tests plus three runtime-count tests; complete schema/source/review/license checks, E10, actual published-runtime smoke, E11 record coverage/reconciliation, E12 and master-plan audit. The source snapshot also reproduces byte-for-byte from all four pinned upstream inputs. Compare the resulting remote HEAD's three workflow runs in PR #48 before signing off that implementation batch.

Step 2 completion review is **not passed**. Group 1 is **not complete**. Steps 3–12 remain queued, following the user's strict transition rule. Continue bounded editorial review from `node scripts/prepare-tatoeba-english-review.mjs --limit 24`; do not stop merely because the original source lane is too small, and do not count the remaining candidate backlog as reviewed publication.
