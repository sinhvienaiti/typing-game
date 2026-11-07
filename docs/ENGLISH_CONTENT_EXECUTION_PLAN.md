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
| 2 | Expand reviewed, published examples to the agreed minimum of 100,000 using reproducible, licensed source intake. Source capacity, editorial quality and runtime counts must independently support the result. | IN PROGRESS — new pinned English-only intake and nine editorial batches integrated; 3,621 published examples. Candidate capacity is available; remaining editorial work is not approved. |
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
| Reviewed published examples | 3,621 |
| Required minimum | 100,000 |
| Current published deficit | 96,379 |
| Eligible unique raw sentences in the current original-source lane | 5,588 |
| Raw sentences not yet reviewed | 4,588 |
| Optimistic published upper bound using only remaining original-source raw sentences | 8,209 |
| Additional source gap if restricted to that original lane | 91,791 |

The upper bound covers this configured source lane only. It is not an assertion that no other upstream dataset exists. Further local review is possible, but does not make the full Step 2 deliverable achievable from these inputs alone; future rejection/dedup can reduce the bound. Other upstream sources require a reproducible, licensed, reviewed intake before their potential size can be counted.

### Active continuation: pinned English-only Tatoeba lane

The original-lane shortage is no longer an overall stop condition. Four official 2026-10-31 exports were acquired and checksum-verified on 2026-11-07. A separately versioned offline extraction retains 122,212 English source-evidence candidates in five canonical shards. See `docs/TATOEBA_ENGLISH_INTAKE.md` and `content/english/sources/tatoeba-english-2026-10-31.json`. The historical EN/VI/link pin is unchanged.

Pilot 01 explicitly reviewed 24 records: 20 published, four rejected and two edited. The digest-bound ledger, controlled source and per-record review report retain all outcomes, original/final texts, CEFR rationales and attribution. Rejections include a threat and context/factual-scope problems despite positive experimental source ratings. The queue skips these decisions permanently.

After all 1,624 local decisions and excluding controlled IDs/texts and exact source duplicates, 120,562 candidates remain available. Combined with the original-source remainder, the optimistic intake bound is 128,771 examples before further editorial rejection and cross-source near dedup. Candidate availability does not establish that all of those examples will pass. The capacity report is now version 2 with separate original and new-source lanes, `editorial-review-required`, and every transition gate still false.

Local validation: 112 content/tooling tests plus three runtime-count tests; complete schema/source/review/license checks, E10, actual published-runtime smoke, E11 record coverage/reconciliation, E12 and master-plan audit. The source snapshot also reproduces byte-for-byte from all four pinned upstream inputs. Compare the resulting remote HEAD's three workflow runs in PR #48 before signing off that implementation batch.

Step 2 completion review is **not passed**. Group 1 is **not complete**. Steps 3–12 remain queued, following the user's strict transition rule. Continue bounded editorial review from `node scripts/prepare-tatoeba-english-review.mjs --limit 24`; do not stop merely because the original source lane is too small, and do not count the remaining candidate backlog as reviewed publication.

### Editorial continuation: batches 02 and 03

A further 400 candidates received individual editorial decisions: batch 02 accepted 181 and rejected 19; batch 03 accepted 176 and rejected 24. Eight accepted records have disclosed edits, including an ambiguous multiplicative comparison, place-name agreement, compound punctuation, a precise relative clause and an expanded physical-education abbreviation. The two reports retain every original/final text, rationale, CEFR and source digest.

After batches 02 and 03, the English-only lane had reviewed 424 records, published 377 and rejected 47; the runtime at that checkpoint contained 2,590 examples and 15,373 rich records. Exact/near lexical dedup also passes against the existing runtime and within the new batches. Pragmatic duplicates were explicitly rejected even when their token overlap was below the numerical threshold.

Self-review detected that readiness counted only the first explicitly configured English-only shard. E11 readiness and record coverage now discover every registered English-only batch from the manifest and apply the digest-bound review overlay. A regression checks each batch is counted exactly once and that deprecated/unapproved records do not increase its count. The redundant first-shard target entry was removed; locked targets are unchanged. E12 release snapshots must be refreshed before the final E11 readiness/runtime reconciliation, because readiness embeds release bytes.

The source integration checkpoint `bb0ce40898a6975f108760da91b5faed15f3670e` passed all three remote workflows: [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42357377757), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42357377770), [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42357372993). Verify the continuation commit's workflows separately before sign-off. Step 2 remains in progress; it has not met 100,000 published examples.

### Editorial continuation: batches 04–06

| Batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 04 | 200 | 179 | 21 | 4 |
| 05 | 200 | 172 | 28 | 8 |
| 06 | 200 | 180 | 20 | 6 |
| Total | 600 | 531 | 69 | 18 |

Every candidate has an individual rationale. Rejections include unsupported factual/medical/legal generalizations, insufficiently framed quotations, unsuitable standalone wording and lexical/pragmatic duplicates. An inverted counterfactual was rejected after exact Jaccard review found 0.9333 overlap with the selected non-inverted sentence. Eighteen accepted edits address collocations, punctuation, tense, comparison ambiguity and self-contained wording; source modification markers and decision digests were refreshed. Self-review simplified one initially overcomplicated responsibility paraphrase and reassessed its CEFR.

At the end of batches 04–06, the English-only lane had reviewed 1,024 candidates: 908 published and 116 rejected, with 28 disclosed edits. Runtime at that checkpoint: 3,121 examples, 5,009 sentence records and 15,904 rich records; ledger: 16,020 decisions. All 908 approved English-only records pass both Monkeytype and Karaoke adapters (1,816 checks). Rejected IDs remain excluded from runtime and future packets. Source/version/license pins and legacy vocabulary output are unchanged.

The prior continuation `e81e3e48def60bd04386f003fce509f300d42a0d` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42358545415), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42358545421) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42358540969). Record the new continuation HEAD's checks in PR #48 after publication. At that checkpoint the remaining reviewed-publication deficit was 96,879; Step 2 and Group 1 had not passed.

### Editorial continuation: batches 07–09

| Batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 07 | 200 | 160 | 40 | 3 |
| 08 | 200 | 171 | 29 | 5 |
| 09 | 200 | 169 | 31 | 4 |
| Total | 600 | 500 | 100 | 12 |

All 600 candidates received individual decisions and rationale. Review rejected unsupported biological universals, unscoped current economic/medical assertions, insufficiently framed quotations and pragmatic repeats. Twelve disclosed edits improve written-register wording, compound punctuation, fixed expressions and standalone questions while preserving source meaning. Exact source evidence and intake/controlled digests are retained; rejected IDs never re-enter the queue.

Current totals across nine English-only batches: 1,624 decisions, 1,408 published, 216 rejected and 40 disclosed edits. Runtime: 3,621 examples, 5,509 sentence records and 16,404 rich records; ledger: 16,620 decisions. All 1,408 approved English-only records pass both adapters (2,816 checks). The next queue has 120,562 unreviewed candidates, not approved publications. The remaining reviewed-publication deficit is 96,379. Step 2 remains IN PROGRESS; Steps 3–12 stay queued.

Prior checkpoint `88802d34bb7ea4049c23f6a4ca8f674f9ab35c47` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42364035182), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42364035316) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42364030575). Verify the new continuation's exact HEAD and record its workflow evidence in PR #48. Preserve the source pin, reviewed-only publication, deterministic generation and E12-before-final-E11 reconciliation order.
