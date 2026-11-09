# Tatoeba English-only intake

This lane resumes Group 1 Step 2. It is separate from the historical English–Vietnamese translation pilot. It does not recover or replace the old EN/VI/link pin, unlock Step 3, or claim that the 100,000 published-example target has passed.

## Approved source observation

The four official weekly exports were downloaded on 2026-11-07; their Last-Modified headers identify 2026-10-31 exports. `content/english/sources/tatoeba-english-2026-10-31.json` records their URLs, byte lengths and SHA-256 hashes. Weekly URLs are mutable: later bytes must not be substituted for these approved inputs.

The extraction contains 122,212 source-evidence candidates from 2,040,024 English rows. Owners and independent positive reviewers self-report English level 5 in the same observed language export. Positive ratings must be at least as recent as the sentence modification. Any fresh negative rating or configured action/problem tag excludes a record. The typing subset uses 5–30 words, at most 300 ASCII characters, initial capitals and final sentence punctuation; it excludes digits, URLs and markup delimiters. These structural filters are not an exhaustive assessment of grammar, bias, factual accuracy or suitability. Some historical creation timestamps are unknown (`\N`); modification timestamps must be known to check rating freshness.

Tatoeba documents sentence reviews as experimental. The 623 records with at least two independent positive ratings receive queue priority; even these records require local editorial decisions. Self-reported language levels do not establish professional/native-speaker certification. A rating is not a CEFR assessment.

## Offline pin and reproduction

The five committed `.jsonl.gz.b64` shards contain the canonical extraction, including sentence IDs/texts, current owners, modification times, self-reported language levels and qualifying ratings. They retain no user profile descriptions. Base64 keeps the compressed snapshot transportable through the GitHub text-file API. Decode base64 before comparing the compressed hash; decompressed JSONL has its own byte length and hash. Files and rows are ordered deterministically. This extraction, rather than a promise that a mutable upstream URL will remain available, is the offline pin.

To verify and reconstruct the extraction from the **exact four original files** in `.cache/english-content/tatoeba-english-intake`:

```sh
python scripts/build-tatoeba-english-snapshot.py
```

The builder refuses mismatched upstream hashes or changed canonical descriptors. `--write` only restores bytes that already match the approved pin; it cannot approve a new source version. Bzip2/tar parsing uses Python's standard library and reads named members without extracting archive paths. CI does not fetch the mutable weekly URLs.

To validate the pinned archive and prepare the next editorial packet:

```sh
node scripts/prepare-tatoeba-english-review.mjs --limit 24
```

This works offline from the committed snapshot. It reserves every controlled sentence ID/text, skips previous positive and negative local decisions, deduplicates source text, returns a partial/exhausted packet truthfully, and never reuses an older Tatoeba ID for changed content. Source records remain `candidate`; grammar, naturalness, standalone suitability, CEFR, exact/near dedup and license review remain pending. Every packet includes original evidence and a source digest. Editing text, assigning CEFR or changing provenance requires a new controlled-source digest before a decision can apply.

## Editorial pilot and publication

Pilot 01 reviewed all 24 selected records: 20 accepted, four rejected, two accepted with disclosed edits. The rejected records include a generalized regulatory claim, a violent threat and two context-dependent discourse prompts. Positive upstream ratings were insufficient for those cases. `content/english/reports/tatoeba-english-editorial-pilot-01.json` records each original/final text, rationale, source digests and cross-runtime token-overlap score. Two edits simplify an unnatural phrase and expand “contact” to “contact lens.” All accepted records have explicit A2/B1/B2 editorial levels; no unreviewed records receive a default CEFR label.

Authoring records remain draft. The E10 manifest and digest-bound ledger decide which records may enter runtime. Rejected records are retained with deprecated decisions so they cannot return as new work. The publisher, schema/source validator, E11 counts/coverage and runtime smoke include this lane. Runtime verification compares approved objects exactly and asserts rejected objects are absent. The historical 300 Tatoeba sentences and 300 translation exercises retain their original source snapshots and counts.

Near-duplicate checks retain the existing exact token-Jaccard definition and threshold. A global token-order prefix index replaces repeated all-pairs tokenization. Every candidate match still receives a full set-intersection calculation, and regression tests compare the complete ordered results against brute force across random corpora, boundary thresholds, punctuation, empty sets and Unicode. It is not an approximate dedup filter.

## License and attribution

The official text export is distributed under CC BY 2.0 France. Each record retains the Tatoeba Project name, sentence URL, current owner, snapshot and license; the URL provides contributor history. Current owner is not represented as the original or sole author. Local edits set `modified: true` and explain the change. Audio is not imported. No source pin, community rating or successful technical test constitutes approval of the remaining editorial backlog.

Primary references: [Downloads](https://tatoeba.org/en/downloads), [Terms of use](https://tatoeba.org/en/terms_of_use), [Attribution FAQ](https://en.wiki.tatoeba.org/articles/show/faq).

## Reviewed continuation batches

Batches 02 and 03 each inspected 200 candidates. Batch 02 published 181, rejected 19 and disclosed four edits. Batch 03 published 176, rejected 24 and disclosed four edits. At that checkpoint, the three batches contained 424 decisions publishing 377 English-only examples and retaining 47 rejections. The full corpus then had 2,590 published examples; 121,764 source candidates remained unreviewed.

The per-record reports `tatoeba-english-editorial-pilot-02.json` and `tatoeba-english-editorial-pilot-03.json` contain individual rationales, original/final wording, explicit CEFR for accepted records, intake/controlled source digests and nearest token-overlap evidence. Rejections include unframed factual claims, outdated present-tense office-holder assertions, universal stereotypes, unsafe unqualified medical/food-storage advice and pragmatic repeats. Rejected candidates retain their original evidence and cannot re-enter the review queue.

E11 readiness and exact runtime record coverage discover registered English-only batches directly from the E10 manifest. Source authoring remains draft; only digest-bound publication decisions count. After release/maintenance refresh, regenerate E11 readiness and runtime reports again so embedded release snapshots are current. The existing runtime smoke checks every accepted object exactly and every rejected object's absence; all accepted continuation records are also exercised through Monkeytype and Karaoke adapters.

## Batches 04–06 and current continuation

Three further 200-record batches reviewed 600 candidates: 531 accepted, 69 rejected and 18 disclosed edits. Batch 04 accepted 179; batch 05 accepted 172; batch 06 accepted 180. Their individual reports use the same original/final wording, rationale, explicit CEFR, source-digest and nearest-overlap evidence as earlier batches. One inverted raincoat conditional was rejected at 0.9333 token overlap; pragmatic repeats were also removed below that threshold.

At the end of batches 04–06, all six batches contained 1,024 explicit decisions: 908 published English-only records and 116 rejected records, with 28 documented edits. The full corpus then contained 3,121 examples, with a target deficit of 96,879 and 121,162 unreviewed English-only candidates. These counts do not approve Step 2 or unlock translations.

Local checks exercise all 908 approved English-only records through both game adapters (1,816 checks), verify exact approved runtime objects and rejected-object absence, and reconcile E10/E11/E12 plus the capacity report. Regenerate the release snapshot before final E11 freshness checks. Verify the resulting remote HEAD's three workflows in PR #48.

## Batches 07–09

Three further 200-record batches explicitly reviewed 600 candidates: 500 published, 100 rejected and 12 edited. Batch 07 published 160; batch 08 published 171; batch 09 published 169. Rejection rationales cover unsupported universals, insufficiently scoped medical/economic/historical assertions, unclear standalone wording and pragmatic repeats. The per-record reports preserve every original/final text, rationale, CEFR assignment and source digest.

At the end of batches 07–09, 1,624 decisions published 1,408 English-only examples and retained 216 rejections. Forty accepted records had disclosed edits. Runtime then contained 3,621 examples, with a target deficit of 96,379 and 120,562 unreviewed candidates. All 1,408 approved English-only records pass both game adapters (2,816 checks). Rejected IDs stay out of both runtime and future review packets. Candidate inventory and successful engineering checks do not approve Step 2 or unlock later steps.

## English batches 10–12: still execution Step 2

A further 600 records received explicit review: batch 10 published 165, batch 11 published 167 and batch 12 published 168. Total: 500 published, 100 rejected and nine disclosed edits. Individual reports retain source/final wording, rationale, CEFR for accepted records, digest evidence and nearest-overlap results. Edited final texts were also checked against active canonical sentence sources for exact collisions.

At the end of batches 10–12, English-only totals were: 2,224 decisions, 1,908 published, 316 rejected and 49 disclosed edits. Full runtime contains 4,121 examples, 6,009 sentence records and 16,904 rich records; the ledger has 17,220 decisions. All 1,908 approved English-only records pass both adapters (3,816 checks). The queue has 119,962 unreviewed candidates; 95,879 more approved publications are needed. These engineering checks and packet labels do not open execution Steps 3–12. Source/license pins and the historical translation lane are unchanged.

## English batches 13–15: preceding Step 2 checkpoint

All 600 new candidates received explicit individual decisions: batch 13 published 143/rejected 57/edited six; batch 14 published 143/rejected 57/edited two; batch 15 published 141/rejected 59/edited six. Total: 427 published, 173 rejected and 14 disclosed edits. Reports retain every original/final text, editorial rationale, explicit accepted-record CEFR, source digests and nearest-overlap evidence. Self-review removed additional semantic repeats below the token threshold; edited final texts were also checked against active canonical sentence sources. Source authoring remains draft and publication requires the exact digest-bound ledger overlay.

At the end of batches 13–15, English-only totals were: 2,824 decisions, 2,335 published, 489 rejected and 63 disclosed edits. Runtime: 4,548 examples, 6,436 sentence records and 17,331 rich records; ledger: 17,820 decisions. All 2,335 published English-only records match runtime exactly and pass both Monkeytype and Karaoke adapters (4,670 checks); rejected objects remain absent. There are 119,362 unreviewed English-only candidates and 95,452 more reviewed publications are needed. English editorial batch 16 followed at `sent.tatoeba.41120`. This is still execution Step 2; Steps 3–12 remain unopened. The historical EN/VI/link pin, all source checksums and the legacy vocabulary ABI are unchanged.

## English batches 16–18: preceding Step 2 checkpoint

A further 600 candidates received individual decisions: batch 16 published 103/rejected 97/edited two; batch 17 published 151/rejected 49/edited three; batch 18 published 164/rejected 36/edited four. Total: 418 published, 182 rejected and nine disclosed edits. Reports preserve source/final wording, explicit accepted-record CEFR, rationale, attribution, intake/controlled digests and nearest-overlap evidence. Unspecified context was not invented. Semantic repeats were rejected even below the token threshold, including additional hearing-news/turning-pale variants. Edited final text was compared against all active canonical sources.

At the end of batches 16–18, English-only totals were: 3,424 decisions, 2,753 published, 671 rejected and 72 disclosed edits. Runtime: 4,966 examples, 6,854 sentence records and 17,749 rich records; ledger: 18,420 decisions. All 2,753 approved English-only records match runtime exactly and pass both Monkeytype and Karaoke adapters (5,506 checks). All rejected records remain absent. There are 118,762 unreviewed English-only candidates and 95,034 more reviewed publications are needed. English editorial batch 19 followed at `sent.tatoeba.45621`. This is still execution Step 2, with Steps 3–12 queued. The historical EN/VI/link pin, all source checksums and the legacy vocabulary ABI are unchanged.

## English batches 19–21: preceding Step 2 checkpoint

All 600 candidates received individual decisions: batch 19 published 159/rejected 41/edited six; batch 20 published 156/rejected 44/edited one; batch 21 published 142/rejected 58/edited two. Total: 457 published, 143 rejected and nine disclosed edits. Original/final wording, editorial rationale, explicit accepted-record CEFR, attribution, source evidence and digests remain in the three reports. Cross-corpus review rejected additional semantic repeats, including accident-cause paraphrases and a fifteen-member committee sentence whose wording differed from the existing record. Edited final text was also checked against all active canonical sources.

At the end of batches 19–21, English-only totals were: 4,024 decisions, 3,210 published, 814 rejected and 81 disclosed edits. Runtime: 5,423 examples, 7,311 sentence records and 18,206 rich records; ledger: 19,020 decisions. All 3,210 approved English-only records match runtime exactly and pass both adapters (6,420 checks); rejected objects remain absent. The example manifest includes `examples/010.json`. There were 118,162 unreviewed English-only candidates and 94,577 more reviewed publications were needed. English editorial batch 22 followed at `sent.tatoeba.49931` using `--limit 200`. This remains execution Step 2; Steps 3–12 stay queued. The historical EN/VI/link pin, source checksums and legacy vocabulary ABI are unchanged.

## English batches 22–30: preceding Step 2 checkpoint

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 22 | 200 | 143 | 57 | 2 |
| 23 | 200 | 132 | 68 | 0 |
| 24 | 200 | 121 | 79 | 1 |
| 25 | 200 | 151 | 49 | 2 |
| 26 | 200 | 136 | 64 | 1 |
| 27 | 200 | 134 | 66 | 2 |
| 28 | 200 | 137 | 63 | 2 |
| 29 | 200 | 139 | 61 | 3 |
| 30 | 200 | 129 | 71 | 4 |
| Total | 1,800 | 1,222 | 578 | 17 |

Every candidate received an individual reading, explicit outcome and rationale. Review checked grammar, naturalness, standalone use, CEFR, canonical source evidence, attribution, exact/near matches and semantic repeats. Seventeen accepted edits preserve source meaning and disclose original/final wording, `modified: true`, an edit description and a recomputed controlled-source digest. Examples include the standard participle shaken, natural duration expressions, word order, collocations and clarified geographic/language scope. Edited final texts were checked against all active canonical sentence records as well as approved runtime/new-batch records; no exact collision was retained. Rejections remain in authoring, ledger and per-record editorial reports. Grammar that can be repaired without changing source meaning is edited and reviewed; duplication, missing factual context or an unsupported claim is not repaired by inventing new source content.

Current English-only totals: 5,824 decisions, 4,432 published, 1,392 rejected and 98 disclosed edits. Full runtime: 6,645 examples, 8,533 sentence records and 19,428 rich records; ledger: 20,820 applied decisions (19,428 publication and 1,392 deprecated). All 4,432 approved English-only records match runtime exactly and pass Monkeytype and Karaoke adapters (8,864 checks). Rejected IDs remain absent from runtime and future review packets. The example manifest now includes `examples/011.json`, `examples/012.json` and `examples/013.json`; the last shard contains 145 records. There are 116,362 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 127,595 before further rejection/dedup; none of this candidate capacity counts as publication. The reviewed-publication deficit is 93,355.

At the end of batches 22–30, English editorial batch 31 was next at `sent.tatoeba.67208`; that checkpoint has now been continued below. This remains execution Group 1 Step 2. Steps 3–12 remain queued; PR #48 stays Draft. Source/license pins, the historical EN/VI/link lane and legacy vocabulary ABI remain unchanged.

## English batches 31–33: preceding Step 2 checkpoint

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 31 | 200 | 146 | 54 | 5 |
| 32 | 200 | 158 | 42 | 7 |
| 33 | 200 | 156 | 44 | 8 |
| Total | 600 | 460 | 140 | 20 |

Each of the 600 candidates received an individual reading, explicit outcome and rationale for grammar, naturalness, independent use, CEFR and source suitability. Canonical snapshot evidence, CC BY 2.0 France attribution and source digests were verified. Twenty accepted edits retain original/final wording, `modified: true`, a change description and recomputed digest. Repairs include neither-of-us agreement, goal-in-life wording, uncountable testimony, buttering-up collocation, compound punctuation and arithmetic-list wording. Edited final texts were compared against all canonical sentence records as well as retained runtime records. Self-review removed twelve additional semantic repeats below the lexical threshold, including wait-here, family-introduction, surprise-meeting and help-enabled-completion variants. All 140 rejections remain traceable in authoring, ledger and reports, without a CEFR or runtime object. Source authoring remains draft; only the exact digest-bound publication decision permits runtime publication.

Current English-only totals: 6,424 decisions, 4,892 published, 1,532 rejected and 118 disclosed edits. Full runtime: 7,105 examples, 8,993 sentence records and 19,888 rich records; ledger: 21,420 applied decisions (19,888 publication and 1,532 deprecated). The continuation adds 460 published examples; 92,895 more reviewed publications are needed to reach 100,000. All 4,892 English-only approved objects match runtime exactly and pass both Monkeytype and Karaoke adapters (9,784 checks). The example manifest includes `examples/014.json`; the final shard contains 105 records. There are 115,762 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 127,455 before further rejection/dedup and is not publication approval.

Local validation passes schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact record coverage, capacity and master-plan checks. E12 release/maintenance is regenerated before final E11 readiness/runtime. Deterministic regeneration and tracked manifest-shard coverage are mandatory before push. These engineering gates do not satisfy the Step 2 publication target.

The verified preceding checkpoint `cd323b28477c1562b54c22beae9118a9990de7e1` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42448870529), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42448870531) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42448867006). Verify all three workflows on the resulting continuation HEAD and record current evidence in PR #48; this file intentionally retains the preceding verified SHA to avoid a self-referential SHA-only commit.

At the end of batches 31–33, English batch 34 was next at `sent.tatoeba.72913`; the continuation is recorded below. All 6,424 reviewed English-only IDs are excluded from the next packet, which has no assigned CEFR. This remains execution Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI and completed E04/typing-text batches remain unchanged.

## English batches 34–40: current Step 2 checkpoint

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 34 | 200 | 147 | 53 | 5 |
| 35 | 200 | 145 | 55 | 9 |
| 36 | 200 | 151 | 49 | 2 |
| 37 | 200 | 143 | 57 | 2 |
| 38 | 200 | 136 | 64 | 2 |
| 39 | 200 | 153 | 47 | 3 |
| 40 | 200 | 142 | 58 | 5 |
| Total | 1,400 | 1,017 | 383 | 28 |

All 1,400 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest. Repairs cover plural possessives, articles, collocations, agreement, prepositions, passive tense, clause wording and clearer reference. Seven additional semantic repeats were removed during self-review, below the lexical threshold. All 383 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 7,824 decisions, 5,909 published, 1,915 rejected and 146 disclosed edits. Runtime: 8,122 examples, 10,010 sentence records and 20,905 rich records; ledger: 22,820 applied decisions (20,905 publication and 1,915 deprecated). This continuation adds 1,017 examples, leaving 91,878 more reviewed publications to reach 100,000. All 5,909 English-only approved objects match runtime exactly and pass both adapters (11,818 checks). Rejected IDs remain absent. The example manifest includes new `examples/015.json` and `examples/016.json`; shard 016 has 122 records. There are 114,362 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 127,072 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `30e2a514e26a4edcd6e971ea37fde79565ec1d3d` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42454527175), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42454527087) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42454523482). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 41 at `sent.tatoeba.248058` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 7,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 41–47

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 41 | 200 | 183 | 17 | 7 |
| 42 | 200 | 186 | 14 | 6 |
| 43 | 200 | 173 | 27 | 7 |
| 44 | 200 | 194 | 6 | 8 |
| 45 | 200 | 193 | 7 | 7 |
| 46 | 200 | 190 | 10 | 7 |
| 47 | 200 | 182 | 18 | 12 |
| Total | 1,400 | 1,301 | 99 | 54 |

All 1,400 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifty-four accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest. Repairs cover articles, collocations, agreement, prepositions, comma splices, coordination, clause wording and clearer standalone reference. Semantic repeats and near duplicates were removed during review. All 99 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 9,224 decisions, 7,210 published, 2,014 rejected and 200 disclosed edits. Runtime: 9,423 examples, 11,311 sentence records and 22,206 rich records; ledger: 24,220 applied decisions (22,206 publication and 2,014 deprecated). This continuation adds 1,301 examples, leaving 90,577 more reviewed publications to reach 100,000. All 7,210 English-only approved objects match runtime exactly and pass both adapters (14,420 checks). Rejected IDs remain absent. The example manifest includes new `examples/017.json` and `examples/018.json`; shard 018 has 423 records. There are 112,962 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,973 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 48 at `sent.tatoeba.264735` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 9,224 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 48–50

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 48 | 200 | 181 | 19 | 11 |
| 49 | 200 | 184 | 16 | 19 |
| 50 | 200 | 194 | 6 | 13 |
| Total | 600 | 559 | 41 | 43 |

All 600 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Forty-three accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest. Repairs cover articles, collocations, agreement, prepositions, comma splices, coordination, clause wording and clearer standalone reference. Semantic repeats and near duplicates (e.g. high-overlap variants of future prediction, delayed stopping of crying, headache bed-going, and neck hugs) were removed during review. All 41 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 9,824 decisions, 7,769 published, 2,055 rejected and 243 disclosed edits. Runtime: 9,982 examples, 11,870 sentence records and 22,765 rich records; ledger: 24,820 applied decisions (22,765 publication and 2,055 deprecated). This continuation adds 559 examples, leaving 90,018 more reviewed publications to reach 100,000. All 7,769 English-only approved objects match runtime exactly and pass both adapters (15,538 checks). Rejected IDs remain absent. Shard 018 was updated to its 500-record capacity and the example manifest includes new `examples/019.json`; shard 019 has 482 records. There are 112,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,931 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 51 at `sent.tatoeba.268742` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 9,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 51–60

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 51 | 200 | 194 | 6 | 1 |
| 52 | 200 | 191 | 9 | 0 |
| 53 | 200 | 195 | 5 | 0 |
| 54 | 200 | 196 | 4 | 0 |
| 55 | 200 | 196 | 4 | 0 |
| 56 | 200 | 194 | 6 | 0 |
| 57 | 200 | 195 | 5 | 1 |
| 58 | 200 | 196 | 4 | 0 |
| 59 | 200 | 192 | 8 | 0 |
| 60 | 200 | 195 | 5 | 0 |
| Total | 2,000 | 1,944 | 56 | 2 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (e.g. normalization of unhyphenated compound nouns and punctuation spacing). Near duplicates and intra-slice duplicate variations were removed during review. All 56 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 11,824 decisions, 9,713 published, 2,111 rejected and 245 disclosed edits. Runtime: 11,926 examples, 13,814 sentence records and 24,709 rich records; ledger: 26,820 applied decisions (24,709 publication and 2,111 deprecated). This continuation adds 1,944 examples, leaving 88,074 more reviewed publications to reach 100,000. All 9,713 English-only approved objects match runtime exactly and pass both adapters (19,426 checks). Rejected IDs remain absent. Shard 019 was completed with 500 records, new shards `examples/020.json`, `examples/021.json`, `examples/022.json` (500 records each), and `examples/023.json` (426 records) are registered in the manifest. There are 110,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,875 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 61 at `sent.tatoeba.282806` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 11,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 61–70

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 61 | 200 | 193 | 7 | 0 |
| 62 | 200 | 189 | 11 | 0 |
| 63 | 200 | 194 | 6 | 0 |
| 64 | 200 | 188 | 12 | 0 |
| 65 | 200 | 192 | 8 | 0 |
| 66 | 200 | 193 | 7 | 1 |
| 67 | 200 | 196 | 4 | 0 |
| 68 | 200 | 195 | 5 | 0 |
| 69 | 200 | 194 | 6 | 0 |
| 70 | 200 | 191 | 9 | 0 |
| Total | 2,000 | 1,925 | 75 | 1 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. One accepted edit preserves source meaning and discloses original/final text, modified provenance, the change description and a recomputed digest (e.g. normalization of spelling and punctuation). Near duplicates and intra-slice duplicate variations were removed during review. All 75 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 13,824 decisions, 11,638 published, 2,186 rejected and 246 disclosed edits. Runtime: 13,851 examples, 15,739 sentence records and 26,634 rich records; ledger: 28,820 applied decisions (26,634 publication and 2,186 deprecated). This continuation adds 1,925 examples, leaving 86,149 more reviewed publications to reach 100,000. All 11,638 English-only approved objects match runtime exactly and pass both adapters (23,276 checks). Rejected IDs remain absent. Shard 023 was completed with 500 records, new shards `examples/024.json`, `examples/025.json`, `examples/026.json` (500 records each), and `examples/027.json` (351 records) are registered in the manifest. There are 108,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,800 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 71 at `sent.tatoeba.297624` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 13,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 71–72

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 71 | 200 | 189 | 11 | 6 |
| 72 | 200 | 192 | 8 | 10 |
| Total | 400 | 381 | 19 | 16 |

All 400 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 71: flatly rejected offer, poet and a statesman, prevented him from attending, quite a humble man, talk of the town, Newsweek magazine article drop; Batch 72: cozy little house, capable at his job, woman-hater, henpecked, angling for a promotion, into the crowd, a reputation, sharpshooter, his entire fortune, gives his work all he's got). Near duplicates and intra-slice duplicate variations were removed during review. All 19 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 14,224 decisions, 12,019 published, 2,205 rejected and 262 disclosed edits. Runtime: 14,232 examples, 16,120 sentence records and 27,015 rich records; ledger: 29,220 applied decisions (27,015 publication and 2,205 deprecated). This continuation adds 381 examples across batches 71–72, leaving 85,768 more reviewed publications to reach 100,000. All 12,019 English-only approved objects match runtime exactly and pass both adapters (24,038 checks). Rejected IDs remain absent. Shard 027 was completed with 500 records and shard `examples/028.json` now holds 232 records. There are 107,961 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,781 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 73 at `sent.tatoeba.300949` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 14,224 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 73–80

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 73 | 200 | 189 | 11 | 5 |
| 74 | 200 | 190 | 10 | 4 |
| 75 | 200 | 191 | 9 | 3 |
| 76 | 200 | 193 | 7 | 3 |
| 77 | 200 | 192 | 8 | 3 |
| 78 | 200 | 193 | 7 | 3 |
| 79 | 200 | 191 | 9 | 4 |
| 80 | 200 | 192 | 8 | 3 |
| Total | 1,600 | 1,531 | 69 | 28 |

All 1,600 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 73: natural gerund, proper prepositional idiom, pronoun clarity; Batch 74: adjective order, idiomatic noun complement; Batch 75: article usage, modern collocation; Batch 76: preposition correction, natural gerund complement; Batch 77: talent for dancing, eye for beauty, same design as; Batch 78: take her place, different from, too short notice; Batch 79: plays the piano, natural for the part, which one I should buy, eye for a good bargain; Batch 80: closed housekeeping, coming into contact, lowercase ill). Near duplicates and intra-slice duplicate variations were removed during review. All 69 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 15,824 decisions, 13,550 published, 2,274 rejected and 290 disclosed edits. Runtime: 15,763 examples, 17,651 sentence records and 28,546 rich records; ledger: 30,820 applied decisions (28,546 publication and 2,274 deprecated). This continuation adds 1,531 examples across batches 73–80, leaving 84,237 more reviewed publications to reach 100,000. All 13,550 English-only approved objects match runtime exactly and pass both adapters (27,100 checks). Rejected IDs remain absent. Shard 028 was completed with 500 records, new shards `examples/029.json` and `examples/030.json` (500 records each), and shard `examples/031.json` (263 records) are registered in the manifest. There are 106,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,712 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 81 at `sent.tatoeba.313724` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 15,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 81–90

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 81 | 200 | 189 | 11 | 2 |
| 82 | 200 | 193 | 7 | 3 |
| 83 | 200 | 191 | 9 | 3 |
| 84 | 200 | 193 | 7 | 3 |
| 85 | 200 | 194 | 6 | 3 |
| 86 | 200 | 192 | 8 | 3 |
| 87 | 200 | 193 | 7 | 3 |
| 88 | 200 | 193 | 7 | 3 |
| 89 | 200 | 193 | 7 | 2 |
| 90 | 200 | 191 | 9 | 2 |
| Total | 2,000 | 1,922 | 78 | 27 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-seven accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 81: burned her left hand, express her feelings; Batch 82: clear-headed, all to herself, in a soft voice; Batch 83: Breakfast is included, using too much praise, When the manager gives a plan; Batch 84: for misconduct, stretched his legs, into the sky; Batch 85: Reading literature, United States,, exchange it for; Batch 86: cop-out, customer is always right principle, interfere with my affairs; Batch 87: want to press you, girls' school, Do you want to go; Batch 88: just in case, entered a war, Neither of my parents is alive; Batch 89: it is important to clearly distinguish, halfway; Batch 90: why he was so sad, custom-made). Near duplicates and intra-slice duplicate variations were removed during review. All 78 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 17,824 decisions, 15,472 published, 2,352 rejected and 317 disclosed edits. Runtime: 17,685 examples, 19,573 sentence records and 30,468 rich records; ledger: 32,820 applied decisions (30,468 publication and 2,352 deprecated). This continuation adds 1,922 examples across batches 81–90, leaving 82,315 more reviewed publications to reach 100,000. All 15,472 English-only approved objects match runtime exactly and pass both adapters (30,944 checks). Rejected IDs remain absent. Shard 031 was completed with 500 records, new shards `examples/032.json`, `033.json`, `034.json` (500 records each), and shard `examples/035.json` (185 records) are registered in the manifest. There are 104,359 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,632 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `23b60c9ec791a4afe06b9d8a66c3bceb7bf76a7a` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 91 at `sent.tatoeba.370950` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 17,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 91–100

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 91 | 200 | 193 | 7 | 1 |
| 92 | 200 | 195 | 5 | 2 |
| 93 | 200 | 189 | 11 | 2 |
| 94 | 200 | 194 | 6 | 3 |
| 95 | 200 | 190 | 10 | 2 |
| 96 | 200 | 198 | 2 | 2 |
| 97 | 200 | 199 | 1 | 2 |
| 98 | 200 | 198 | 2 | 2 |
| 99 | 200 | 199 | 1 | 3 |
| 100 | 200 | 198 | 2 | 2 |
| Total | 2,000 | 1,953 | 47 | 21 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-one accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 91: ask for help; Batch 92: Why is it that you can write, heard afterward; Batch 93: One has to protect one's family, The president abolished slavery; Batch 94: which is why, going to, near the station; Batch 95: conditional comma, causing problems; Batch 96: good at science, work and home life; Batch 97: onto your computer, debating health care; Batch 98: with computers, whitewater; Batch 99: flooring is hardwood, conditional comma, Washington, D.C.; Batch 100: windowsill, gives off light). Near duplicates and intra-slice duplicate variations were removed during review. All 47 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 19,824 decisions, 17,425 published, 2,399 rejected and 338 disclosed edits. Runtime: 19,638 examples, 21,526 sentence records and 32,421 rich records; ledger: 34,820 applied decisions (32,421 publication and 2,399 deprecated). This continuation adds 1,953 examples across batches 91–100, leaving 80,362 more reviewed publications to reach 100,000. All 17,425 English-only approved objects match runtime exactly and pass both adapters (34,850 checks). Rejected IDs remain absent. Shard 035 was completed with 500 records, new shards `examples/036.json`, `037.json`, `038.json` (500 records each), and shard `examples/039.json` (138 records) are registered in the manifest. There are 102,359 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,584 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `dd962a51f93f6c8d4df7140e69882f05a91798ac` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 101 at `sent.tatoeba.681375` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 19,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 101–110

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 101 | 200 | 198 | 2 | 1 |
| 102 | 200 | 198 | 2 | 1 |
| 103 | 200 | 198 | 2 | 4 |
| 104 | 200 | 197 | 3 | 2 |
| 105 | 200 | 198 | 2 | 2 |
| 106 | 200 | 192 | 8 | 1 |
| 107 | 200 | 183 | 17 | 3 |
| 108 | 200 | 196 | 4 | 0 |
| 109 | 200 | 198 | 2 | 2 |
| 110 | 200 | 198 | 2 | 1 |
| Total | 2,000 | 1,956 | 44 | 17 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Seventeen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 101: kids' favorite meal; Batch 102: push-ups; Batch 103: reason for being late, French fries, three-year sentence, Chickenpox; Batch 104: modern structure, backyard; Batch 105: Venice, Italy,, Band-Aid; Batch 106: send word; Batch 107: time heals all wounds, buy me some saffron, make my son eat; Batch 108: clean historical narratives preserved; Batch 109: repay, last resort; Batch 110: Rio Grande). Near duplicates and intra-slice duplicate variations were removed during review. All 44 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 21,824 decisions, 19,381 published, 2,443 rejected and 355 disclosed edits. Runtime: 21,594 examples, 23,482 sentence records and 34,377 rich records; ledger: 36,820 applied decisions (34,377 publication and 2,443 deprecated). This continuation adds 1,956 examples across batches 101–110, leaving 78,406 more reviewed publications to reach 100,000. All 19,381 English-only approved objects match runtime exactly and pass both adapters (38,762 checks). Rejected IDs remain absent. Shard 039 was completed with 500 records, new shards `examples/040.json`, `041.json`, `042.json` (500 records each), and shard `examples/043.json` (94 records) are registered in the manifest. There are 100,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,540 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `019f633215918667b9319e34e569502aa645f7c3` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 111 at `sent.tatoeba.803149` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 21,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 111–120

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 111 | 200 | 196 | 4 | 2 |
| 112 | 200 | 198 | 2 | 0 |
| 113 | 200 | 195 | 5 | 2 |
| 114 | 200 | 198 | 2 | 1 |
| 115 | 200 | 195 | 5 | 6 |
| 116 | 200 | 196 | 4 | 4 |
| 117 | 200 | 193 | 7 | 2 |
| 118 | 200 | 187 | 13 | 2 |
| 119 | 200 | 191 | 9 | 3 |
| 120 | 200 | 188 | 12 | 3 |
| Total | 2,000 | 1,937 | 63 | 25 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-five accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 111: for only a few years, difficulty hearing; Batch 112: clean historical texts preserved; Batch 113: South, Thirty thousand; Batch 114: Lincoln South; Batch 115: anyone who protested, nothing could be done, five hundred, West, senators, North; Batch 116: Great Plains, Louisiana Territory, president lowercase, three and a half million; Batch 117: President Polk Oxford comma, homework by Friday; Batch 118: English-speaking, divided into; Batch 119: parents' house, patient's bedside, hard-boiled eggs; Batch 120: anyway, broken English, Mass). Near duplicates and intra-slice duplicate variations were removed during review. All 63 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 23,824 decisions, 21,318 published, 2,506 rejected and 380 disclosed edits. Runtime: 23,531 examples, 25,419 sentence records and 36,314 rich records; ledger: 38,820 applied decisions (36,314 publication and 2,506 deprecated). This continuation adds 1,937 examples across batches 111–120, leaving 76,469 more reviewed publications to reach 100,000. All 21,318 English-only approved objects match runtime exactly and pass both adapters (42,636 checks). Rejected IDs remain absent. Shard 043 was completed with 500 records, new shards `examples/044.json`, `045.json`, `046.json` (500 records each), and shard `examples/047.json` (31 records) are registered in the manifest. There are 98,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,477 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `9cf4fe7ea920c58e4544e39b972e2cf5eeb6dc21` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 131 with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 25,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 131–140

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 131 | 200 | 180 | 20 | 2 |
| 132 | 200 | 187 | 13 | 2 |
| 133 | 200 | 188 | 12 | 2 |
| 134 | 200 | 186 | 14 | 1 |
| 135 | 200 | 179 | 21 | 1 |
| 136 | 200 | 184 | 16 | 2 |
| 137 | 200 | 187 | 13 | 1 |
| 138 | 200 | 184 | 16 | 2 |
| 139 | 200 | 183 | 17 | 1 |
| 140 | 200 | 185 | 15 | 4 |
| Total | 2,000 | 1,843 | 157 | 18 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Eighteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 131: Earth capitalize, called a cab because comma; Batch 132: bad-tempered, asking the teacher questions; Batch 133: asking my father questions, precautions Oxford comma; Batch 134: go to sleep on Saturday night; Batch 135: breastfed unhyphenated; Batch 136: play the violin, play the trumpet; Batch 137: recite the Quran; Batch 138: forgot to write, were pictures; Batch 139: main cause of global warming; Batch 140: neighbors, mustache, ice water, isn't it tag). Near duplicates and intra-slice duplicate variations were removed during review. All 157 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 27,824 decisions, 25,047 published, 2,777 rejected and 420 disclosed edits. Runtime: 27,260 examples, 29,148 sentence records and 40,043 rich records; ledger: 42,820 applied decisions (40,043 publication and 2,777 deprecated). This continuation adds 1,843 examples across batches 131–140, leaving 72,740 more reviewed publications to reach 100,000. All 25,047 English-only approved objects match runtime exactly and pass both adapters (50,094 checks). Rejected IDs remain absent. Shard 050 was completed with 500 records, new shards `examples/051.json`, `052.json`, `053.json` (500 records each), and shard `examples/054.json` (260 records) are registered in the manifest. There are 94,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,206 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `3838e126da6cc5ea666280f010350fc3437d8db2` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 151 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 29,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 141–150

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 141 | 200 | 183 | 17 | 1 |
| 142 | 200 | 173 | 27 | 1 |
| 143 | 200 | 192 | 8 | 1 |
| 144 | 200 | 188 | 12 | 1 |
| 145 | 200 | 187 | 13 | 1 |
| 146 | 200 | 178 | 22 | 2 |
| 147 | 200 | 176 | 24 | 1 |
| 148 | 200 | 196 | 4 | 4 |
| 149 | 200 | 192 | 8 | 1 |
| 150 | 200 | 195 | 5 | 1 |
| Total | 2,000 | 1,860 | 140 | 14 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fourteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 141: With social media comma; Batch 142: Out of all my children comma; Batch 143: chickenpox closed compound; Batch 144: Hey, guys comma; Batch 145: show-off hyphenated; Batch 146: short-order cook, snowstorm; Batch 147: feet than to live comma removed; Batch 148: forced open, freshwater, mayor lowercase, For an old man comma; Batch 149: sweater is small, and; Batch 150: businessman closed compound). Near duplicates and intra-slice duplicate variations were removed during review. All 140 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 29,824 decisions, 26,907 published, 2,917 rejected and 434 disclosed edits. Runtime: 29,120 examples, 31,008 sentence records and 41,903 rich records; ledger: 44,820 applied decisions (41,903 publication and 2,917 deprecated). This continuation adds 1,860 examples across batches 141–150, leaving 70,880 more reviewed publications to reach 100,000. All 26,907 English-only approved objects match runtime exactly and pass both adapters (53,814 checks). Rejected IDs remain absent. Shard 054 was completed with 500 records, new shards `examples/055.json`, `056.json`, `057.json` (500 records each), and shard `examples/058.json` (120 records) are registered in the manifest. There are 92,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,066 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `559305537ef4f30ad8a4176465377f0a996f014e` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 151 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 29,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 151–160

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 151 | 200 | 190 | 10 | 2 |
| 152 | 200 | 178 | 22 | 4 |
| 153 | 200 | 177 | 23 | 4 |
| 154 | 200 | 189 | 11 | 3 |
| 155 | 200 | 192 | 8 | 2 |
| 156 | 200 | 195 | 5 | 3 |
| 157 | 200 | 188 | 12 | 4 |
| 158 | 200 | 181 | 19 | 5 |
| 159 | 200 | 166 | 34 | 2 |
| 160 | 200 | 175 | 25 | 5 |
| Total | 2,000 | 1,831 | 169 | 34 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-four accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 151: leftovers, eighty kilometers comma; Batch 152: Tidy up comma, streetcar, Oval Office, last-minute; Batch 153: Bullfighting, anymore, Western civilization, broke his arm comma; Batch 154: half a dozen, Hurry up comma, high interest; Batch 155: in favor of going comma, on the whole; Batch 156: timetable, scolded them comma, dining room serial comma; Batch 157: run-down, streetlights, passkey, tax-free; Batch 158: shop will be closed comma, take a walk comma, Yesterday comma, Once comma, fool than comparative; Batch 159: passport photo comma, once-in-a-lifetime; Batch 160: smoke semicolon he drinks, Mass, busy today semicolon otherwise, platinum-blonde, barbed-wire). Near duplicates and intra-slice duplicate variations were removed during review. All 169 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 31,824 decisions, 28,738 published, 3,086 rejected and 468 disclosed edits. Runtime: 30,951 examples, 32,839 sentence records and 43,734 rich records; ledger: 46,820 applied decisions (43,734 publication and 3,086 deprecated). This continuation adds 1,831 examples across batches 151–160, leaving 69,049 more reviewed publications to reach 100,000. All 28,738 English-only approved objects match runtime exactly and pass both adapters (57,476 checks). Rejected IDs remain absent. Shard 058 was completed with 500 records, new shards `examples/059.json`, `060.json` (500 records each), and shard `examples/061.json` (451 records) are registered in the manifest. There are 90,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,897 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `ca5d5d11f70903fc467425f4f36e785c345bc02e` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 161 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 31,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 161–170

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 161 | 200 | 178 | 22 | 2 |
| 162 | 200 | 177 | 23 | 2 |
| 163 | 200 | 170 | 30 | 2 |
| 164 | 200 | 161 | 39 | 2 |
| 165 | 200 | 171 | 29 | 4 |
| 166 | 200 | 177 | 23 | 2 |
| 167 | 200 | 175 | 25 | 6 |
| 168 | 200 | 182 | 18 | 5 |
| 169 | 200 | 173 | 27 | 5 |
| 170 | 200 | 174 | 26 | 5 |
| Total | 2,000 | 1,738 | 262 | 35 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-five accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 161: uppercuts, Last week comma; Batch 162: a couple of minutes, legwarmers; Batch 163: sandcastle, okay; Batch 164: windchimes, Recently comma; Batch 165: streetlamp, okay, soccer and, PIN; Batch 166: mousepad, do it too comma removed; Batch 167: you too comma removed, favor, lawnmower, whitewater, savor, Last Sunday comma; Batch 168: motorhome, On Saturdays comma, Every once in a while comma, everything and, Earth; Batch 169: Tom and I'm, playing too comma removed, Two years ago comma, shoehorn, at home too comma removed; Batch 170: okay, dog and his, King-size, Mary and they, Tonight comma). Near duplicates and intra-slice duplicate variations were removed during review. All 262 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 33,824 decisions, 30,476 published, 3,348 rejected and 503 disclosed edits. Runtime: 32,689 examples, 34,577 sentence records and 45,472 rich records; ledger: 48,820 applied decisions (45,472 publication and 3,348 deprecated). This continuation adds 1,738 examples across batches 161–170, leaving 67,311 more reviewed publications to reach 100,000. All 30,476 English-only approved objects match runtime exactly and pass both adapters (60,952 checks). Rejected IDs remain absent. Shard 061 was completed with 500 records, new shards `examples/062.json`, `063.json`, `064.json` (500 records each), and shard `examples/065.json` (189 records) are registered in the manifest. There are 88,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,634 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `f19aae1a89d8cc3397332e159d47a4e2de7dce7c` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 171 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 33,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 171–180

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 171 | 200 | 177 | 23 | 10 |
| 172 | 200 | 178 | 22 | 3 |
| 173 | 200 | 185 | 15 | 6 |
| 174 | 200 | 183 | 17 | 3 |
| 175 | 200 | 170 | 30 | 5 |
| 176 | 200 | 179 | 21 | 5 |
| 177 | 200 | 176 | 24 | 4 |
| 178 | 200 | 175 | 25 | 3 |
| 179 | 200 | 185 | 15 | 4 |
| 180 | 200 | 175 | 25 | 7 |
| Total | 2,000 | 1,783 | 217 | 50 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifty accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 171: spent on Christmas presents, First comma, serial comma, otherwise semicolon, snored comma and, checkbook closed compound, workload closed compound, fell into pool, at the postgraduate level, wasn't only fined semicolon; Batch 172: joke soon comma removed, rich comma or, shorts-and-T-shirt hyphenated; Batch 173: Saltwater closed compound, crow comma but, in the hospital, wise man semicolon, serial comma, teaching comma and; Batch 174: brand-new hyphenated, stove comma and, Yesterday morning comma; Batch 175: strong that result clause, like you comma and, Earth capitalized, drinking poison and comma removed, In many ways comma; Batch 176: each other comma and, Christmas Day capitalized and comma, reliable comma and, terse comma and, volatile comma and; Batch 177: hooky spelling, sensitive child comma and, weaned comma they, Last night comma; Batch 178: now is wrong comma removed, treehouse closed compound, serial comma; Batch 179: inquiries American spelling, quarreled American spelling, top-secret hyphenated, appreciate it if; Batch 180: really close comma and, steady rain comma and, completely blank comma and, serial comma, sandcastle closed compound, evils I prefer redundant then removed, receives it poorer comma removed). Near duplicates and intra-slice duplicate variations were removed during review. All 217 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 35,824 decisions, 32,259 published, 3,565 rejected and 553 disclosed edits. Runtime: 34,472 examples, 36,360 sentence records and 47,255 rich records; ledger: 50,820 applied decisions (47,255 publication and 3,565 deprecated). This continuation adds 1,783 examples across batches 171–180, leaving 65,528 more reviewed publications to reach 100,000. All 32,259 English-only approved objects match runtime exactly and pass both adapters (64,518 checks). Rejected IDs remain absent. Shard 065 was completed with 500 records, new shards `examples/066.json`, `067.json` (500 records each), and shard `examples/068.json` (472 records) are registered in the manifest. There are 86,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,417 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `f19aae1a89d8cc3397332e159d47a4e2de7dce7c` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 181 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 35,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 181–190

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 181 | 200 | 177 | 23 | 8 |
| 182 | 200 | 181 | 19 | 11 |
| 183 | 200 | 170 | 30 | 7 |
| 184 | 200 | 183 | 17 | 8 |
| 185 | 200 | 190 | 10 | 9 |
| 186 | 200 | 173 | 27 | 1 |
| 187 | 200 | 162 | 38 | 8 |
| 188 | 200 | 174 | 26 | 5 |
| 189 | 200 | 189 | 11 | 2 |
| 190 | 200 | 187 | 13 | 3 |
| Total | 2,000 | 1,786 | 214 | 62 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 181: others semicolon, well-prepared hyphenated, wait comma and, got comma removed, father comma and, before comma removed, Yesterday comma, Valentine's Day; Batch 182: door comma and, him comma and, him comma and, me comma and, carefully comma, Mary comma and, well-loved hyphenated, him comma and, while comma removed, serial comma, door comma and; Batch 183: room comma and, crash comma injuring, all right spelling, depending comma, him comma and, make comma removed, room comma and; Batch 184: without comma removed, so comma removed, and comma removed, mailbox comma, but comma removed, serial comma, Moon capitalized, table comma and; Batch 185: economic phrasing, children comma removed, because comma removed, Fourth of July, bus comma and, pear semicolon, that relative pronoun added, him comma and, home comma exhausted; Batch 186: him comma and; Batch 187: and comma removed, and comma removed, him comma and, him comma and, him comma and, serial comma, it has semicolon, serial comma; Batch 188: serial comma, him comma and, Mary comma and, serial comma, them comma and; Batch 189: bank comma and, hour comma and; Batch 190: alibi comma so, Mary comma and, documents comma and he). Near duplicates and intra-slice duplicate variations were removed during review. All 214 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 37,824 decisions, 34,045 published, 3,779 rejected and 615 disclosed edits. Runtime: 36,258 examples, 38,146 sentence records and 49,041 rich records; ledger: 52,820 applied decisions (49,041 publication and 3,779 deprecated). This continuation adds 1,786 examples across batches 181–190, leaving 63,742 more reviewed publications to reach 100,000. All 34,045 English-only approved objects match runtime exactly and pass both adapters (68,090 checks). Rejected IDs remain absent. Shard 068 was completed with 500 records, new shards `examples/069.json`, `070.json`, `071.json` (500 records each), and shard `examples/072.json` (258 records) are registered in the manifest. There are 84,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,203 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `9b762cb888db09a0a03d09a259c7b91340b157fe` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 191 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 37,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 191–200

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 191 | 200 | 167 | 33 | 3 |
| 192 | 200 | 175 | 25 | 3 |
| 193 | 200 | 178 | 22 | 3 |
| 194 | 200 | 168 | 32 | 2 |
| 195 | 200 | 174 | 26 | 3 |
| 196 | 200 | 177 | 23 | 1 |
| 197 | 200 | 169 | 31 | 5 |
| 198 | 200 | 178 | 22 | 2 |
| 199 | 200 | 171 | 29 | 2 |
| 200 | 200 | 183 | 17 | 18 |
| Total | 2,000 | 1,740 | 260 | 42 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Forty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 191: comma before and; Batch 192: introductory temporal comma, comma before and, removed comma before because; Batch 193: added that, comma before and; Batch 194: serial Oxford comma, comma before and; Batch 195: introductory comma, comma before and, directional into my glass; Batch 196: comma before and; Batch 197: removed comma before because, serial Oxford comma, comma before and; Batch 198: introductory comma, comma before and; Batch 199: comma before and, added definite article the radio; Batch 200: comparative than I had imagined, hyphenated full-time, hyphenated old-fashioned, parallel article a manipulator, comma placement before but, comma before and, capitalized Fourth of July, terminal question marks, serial Oxford comma, hyphenated lip-sync). Near duplicates and intra-slice duplicate variations were removed during review. All 260 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 39,824 decisions, 35,785 published, 4,039 rejected and 657 disclosed edits. Runtime: 37,998 examples, 39,886 sentence records and 50,781 rich records; ledger: 54,820 applied decisions (50,781 publication and 4,039 deprecated). This continuation adds 1,740 examples across batches 191–200, leaving 62,002 more reviewed publications to reach 100,000. All 35,785 English-only approved objects match runtime exactly and pass both adapters (71,570 checks). Rejected IDs remain absent. Shard 072 was completed with 500 records, new shards `examples/073.json`, `074.json` (500 records each), and shard `examples/075.json` (498 records) are registered in the manifest. There are 82,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,943 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `4587ff99cb844f3609e6384cfdcecd0f40b55cff` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 201 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 39,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 201–210

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 201 | 200 | 173 | 27 | 3 |
| 202 | 200 | 172 | 28 | 12 |
| 203 | 200 | 176 | 24 | 8 |
| 204 | 200 | 170 | 30 | 7 |
| 205 | 200 | 163 | 37 | 9 |
| 206 | 200 | 143 | 57 | 5 |
| 207 | 200 | 159 | 41 | 6 |
| 208 | 200 | 177 | 23 | 7 |
| 209 | 200 | 174 | 26 | 3 |
| 210 | 200 | 182 | 18 | 4 |
| Total | 2,000 | 1,689 | 311 | 64 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixty-four accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 201: capitalized Business School, removed comma before because, hyphenated reddish-brown; Batch 202: people's, introductory commas, comma before and, serial Oxford commas, removed redundant a in after half an hour, semicolon for comma splice, comma before or, closed compound shoelaces; Batch 203: introductory commas, serial Oxford comma, capitalized Mommy, comma before and/but, added definite article before undergraduate level, removed extraneous comma; Batch 204: introductory comma, hyphenated well-liked and added Oxford comma, removed comma between coordinate adjectives, comma before and, lowercased teddy bear; Batch 205: hyphenated high-interest, comma before but, removed comma before because, comma before or, removed comma before too/without, removed comma between coordinate verbs, introductory comma; Batch 206: comma before and, serial Oxford comma, hyphenated well-informed; Batch 207: added comma after interjection Boy, comma before and, hyphenated well-mannered, serial Oxford comma; Batch 208: comma before nonrestrictive temporal clause, really hard for colloquial real hard, serial Oxford comma, comma before and, removed extraneous comma before prepositional phrase; Batch 209: terminal question mark for suggestion, closed compound overindulge, adverb strangely for strange; Batch 210: closed compound underway, supplied missing preposition for, adverb placement for I will just never understand, hyphenated compound verb sweet-talk). Near duplicates and intra-slice duplicate variations were removed during review. All 311 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 41,824 decisions, 37,474 published, 4,350 rejected and 721 disclosed edits. Runtime: 39,687 examples, 41,575 sentence records and 52,470 rich records; ledger: 56,820 applied decisions (52,470 publication and 4,350 deprecated). This continuation adds 1,689 examples across batches 201–210, leaving 60,313 more reviewed publications to reach 100,000. All 37,474 English-only approved objects match runtime exactly and pass both adapters (74,948 checks). Rejected IDs remain absent. Shard 075 was completed with 500 records, new shards `examples/076.json`, `077.json`, `078.json` (500 records each), and shard `examples/079.json` (187 records) are registered in the manifest. There are 80,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,631 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `dca819fa3ce58cbbdbf97bb3ec9fc01aa281084d` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 211 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 41,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 211–220

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 211 | 200 | 182 | 18 | 6 |
| 212 | 200 | 175 | 25 | 6 |
| 213 | 200 | 189 | 11 | 3 |
| 214 | 200 | 179 | 21 | 4 |
| 215 | 200 | 191 | 9 | 1 |
| 216 | 200 | 182 | 18 | 2 |
| 217 | 200 | 178 | 22 | 3 |
| 218 | 200 | 184 | 16 | 3 |
| 219 | 200 | 186 | 14 | 2 |
| 220 | 200 | 180 | 20 | 2 |
| Total | 2,000 | 1,826 | 174 | 32 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 211: really for colloquial real, clause fix can't thank you enough for doing, coordinating comma before and, closed compound ballgame, hyphenated big-time; Batch 212: comma splice fix I'm sorry, but I know, hyphenated pick-up line, hyphenated plus-one, comma before and, comma before and then; Batch 213: semicolon for coordinate clauses, comma before and, adverb well for good; Batch 214: hyphenated make-believe, hyphenated tone-deaf, badly off for bad off, between your father and me for reflexive myself; Batch 215: coordinating comma before and; Batch 216: coordinating comma before and, hyphenated compound adjective laid-back; Batch 217: coordinating comma before and, supplied missing preposition of in a lot of work; Batch 218: semicolon for run-on clause, semicolon for comma splice, standard adverb loudly for flat loud; Batch 219: really bad news for colloquial real bad news, really anxious for colloquial real anxious; Batch 220: coordinating comma before or, hyphenated compound noun good-luck charm). Near duplicates and intra-slice duplicate variations were removed during review. All 174 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 43,824 decisions, 39,300 published, 4,524 rejected and 753 disclosed edits. Runtime: 41,513 examples, 43,401 sentence records and 54,296 rich records; ledger: 58,820 applied decisions (54,296 publication and 4,524 deprecated). This continuation adds 1,826 examples across batches 211–220, leaving 58,487 more reviewed publications to reach 100,000. All 39,300 English-only approved objects match runtime exactly and pass both adapters (78,600 checks). Rejected IDs remain absent. Shard 079 was completed with 500 records, new shards `examples/080.json`, `081.json`, `082.json` (500 records each), and shard `examples/083.json` (13 records) are registered in the manifest. There are 78,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,457 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `a90bdff0589d8736e05df82570077c4897f2aa25` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 221 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 43,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 221–230

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 221 | 200 | 178 | 22 | 4 |
| 222 | 200 | 177 | 23 | 1 |
| 223 | 200 | 174 | 26 | 1 |
| 224 | 200 | 157 | 43 | 2 |
| 225 | 200 | 164 | 36 | 2 |
| 226 | 200 | 166 | 34 | 1 |
| 227 | 200 | 174 | 26 | 1 |
| 228 | 200 | 178 | 22 | 2 |
| 229 | 200 | 170 | 30 | 2 |
| 230 | 200 | 176 | 24 | 2 |
| Total | 2,000 | 1,714 | 286 | 18 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Eighteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 221: coordinating comma before but, really small for colloquial real small, semicolon for run-on sentences, hyphenated long-term; Batch 222: closed compound speakerphone; Batch 223: really bad for colloquial real bad; Batch 224: hyphenated compound noun heads-up, really close for colloquial real close; Batch 225: closed compound speechwriter, closed compound sleepover; Batch 226: apostrophe in possessive dollars' worth; Batch 227: supplied missing preposition about; Batch 228: open compound reasonably priced, terminal question mark for suggestion; Batch 229: supplied missing preposition of in a couple of days, really hard for colloquial real hard; Batch 230: corrected typo to ask for at ask, really sorry for colloquial real sorry). Near duplicates and intra-slice duplicate variations were removed during review. All 286 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 45,824 decisions, 41,014 published, 4,810 rejected and 771 disclosed edits. Runtime: 43,227 examples, 45,115 sentence records and 56,010 rich records; ledger: 60,820 applied decisions (56,010 publication and 4,810 deprecated). This continuation adds 1,714 examples across batches 221–230, leaving 56,773 more reviewed publications to reach 100,000. All 41,014 English-only approved objects match runtime exactly and pass both adapters (82,028 checks). Rejected IDs remain absent. Shard 083 was completed with 500 records, new shards `examples/084.json`, `085.json` (500 records each), and shard `examples/086.json` (227 records) are registered in the manifest. There are 76,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,171 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `c96a5f42a9709d327459e9c83ce81bc56430775e` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 231 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 45,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 231–240

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 231 | 200 | 171 | 29 | 4 |
| 232 | 200 | 173 | 27 | 3 |
| 233 | 200 | 173 | 27 | 4 |
| 234 | 200 | 179 | 21 | 5 |
| 235 | 200 | 172 | 28 | 5 |
| 236 | 200 | 171 | 29 | 3 |
| 237 | 200 | 175 | 25 | 2 |
| 238 | 200 | 173 | 27 | 2 |
| 239 | 200 | 182 | 18 | 1 |
| 240 | 200 | 178 | 22 | 2 |
| Total | 2,000 | 1,747 | 253 | 31 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-one accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 231: coordinating commas before and/so; Batch 232: coordinating comma before and, really for colloquial real, hyphenated black-tie; Batch 233: hyphenated missing-persons, semicolon for comma splice, corrected homophone typo You're for Your, coordinating comma before and; Batch 234: interjection commas and exclamations, semicolon for comma splices; Batch 235: corrected typo point of view, hyphenated no-show, hyphenated dog-and-pony show, supplied infinitive marker to, coordinating comma before but; Batch 236: closed compound someday, really for colloquial real, semicolon for comma splice; Batch 237: semicolon for comma splice, capitalized General Assembly; Batch 238: hyphenated stand-up guy, really decent guy for colloquial real decent guy; Batch 239: capitalized Secret Service; Batch 240: hyphenated red-eye for overnight flight, closed compound voicemail). Near duplicates and intra-slice duplicate variations were removed during review. All 253 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 47,824 decisions, 42,761 published, 5,063 rejected and 802 disclosed edits. Runtime: 44,974 examples, 46,862 sentence records and 57,757 rich records; ledger: 62,820 applied decisions (57,757 publication and 5,063 deprecated). This continuation adds 1,747 examples across batches 231–240, leaving 55,026 more reviewed publications to reach 100,000. All 42,761 English-only approved objects match runtime exactly and pass both adapters (85,522 checks). Rejected IDs remain absent. Shard 086 was completed with 500 records, new shards `examples/087.json`, `088.json` (500 records each), and shard `examples/089.json` (474 records) are registered in the manifest. There are 74,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,918 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `7511014b2e88a38ec9ce09eb47c8702b70f03260` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 241 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 47,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 241–250

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 241 | 200 | 171 | 29 | 2 |
| 242 | 200 | 184 | 16 | 3 |
| 243 | 200 | 178 | 22 | 3 |
| 244 | 200 | 184 | 16 | 0 |
| 245 | 200 | 177 | 23 | 1 |
| 246 | 200 | 185 | 15 | 2 |
| 247 | 200 | 188 | 12 | 2 |
| 248 | 200 | 177 | 23 | 2 |
| 249 | 200 | 187 | 13 | 2 |
| 250 | 200 | 182 | 18 | 3 |
| Total | 2,000 | 1,813 | 187 | 20 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 241: comma after introductory connective So, supplied missing subject pronoun you; Batch 242: vocative commas before Tom, removed extraneous comma between subject clause and predicate; Batch 243: lowercased maneuver in Heimlich maneuver, terminal period on imperative, removed redundant article the in both of us; Batch 245: supplied comma after introductory connective So before vocative Tom; Batch 246: hyphenated compound adjective empty-handed, supplied missing definite article the before superlative most beautiful; Batch 247: hyphenated compound noun chain-smoker, hyphenated compound adjective piping-hot; Batch 248: closed compound noun racetrack, closed compound noun lumberyard; Batch 249: removed extraneous comma before adverb yet, normalized inner double quotes to single quotes; Batch 250: standardized American spelling favorite in favorite song, supplied coordinating comma between coordinate adjectives long and baggy, hyphenated compound adjective right-sized). Near duplicates, cross-corpus duplicates (such as sent.tatoeba.4025341 matching published 2569031) and intra-slice duplicate variations were removed during review. All 187 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 49,824 decisions, 44,574 published, 5,250 rejected and 822 disclosed edits. Runtime: 46,787 examples, 48,675 sentence records and 59,570 rich records; ledger: 64,820 applied decisions (59,570 publication and 5,250 deprecated). This continuation adds 1,813 examples across batches 241–250, leaving 53,213 more reviewed publications to reach 100,000. All 44,574 English-only approved objects match runtime exactly and pass both adapters (89,148 checks). Rejected IDs remain absent. Shard 089 was completed with 500 records, new shards `examples/090.json`, `091.json`, `092.json` (500 records each), and shard `examples/093.json` (287 records) are registered in the manifest. There are 72,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,731 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `68b35c1ce2a1b54eab8697ef1779d9108687cc53` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 251 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 49,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 251–260

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 251 | 200 | 181 | 19 | 4 |
| 252 | 200 | 174 | 26 | 6 |
| 253 | 200 | 159 | 41 | 7 |
| 254 | 200 | 164 | 36 | 5 |
| 255 | 200 | 173 | 27 | 6 |
| 256 | 200 | 177 | 23 | 7 |
| 257 | 200 | 172 | 28 | 5 |
| 258 | 200 | 180 | 20 | 3 |
| 259 | 200 | 183 | 17 | 3 |
| 260 | 200 | 174 | 26 | 3 |
| Total | 2,000 | 1,737 | 263 | 49 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Forty-nine accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 251: standardized agreement where water or moisture is present, normalized inner double quotes to single quotes, standardized American spelling counseling, standardized American spelling traveling; Batch 252: standardized American spelling tumor, hyphenated compound adjective long-distance, capitalized proper noun Father's Day, removed extraneous comma before but, standardized American spelling humor, removed extraneous comma before until; Batch 253: normalized inner double quotes, comma after introductory prep phrase, removed extraneous comma before on account of, comma between independent clauses, hyphenated two-week, removed comma before infinitive of purpose, hyphenated white-tie; Batch 254: capitalized Eiffel Tower, hyphenated first-class, standardized compound sentence punctuation or, standardized American spelling favor, standardized American spelling judgment; Batch 255: Oxford comma in series, coordinate comma between long, dark, coordinating comma before so, removed redundant colon after are, normalized inner quotes, standardized closed compound churchgoing; Batch 256: standardized American spelling canceled, standardized compound hardworking, standardized American spelling focused, standardized single word anymore, hyphenated suspended compound left- and right-handed, capitalized proper noun Socialist Party, standardized single word anymore; Batch 257: capitalized vocative Dad, standardized American spelling and hyphenation color-blind, standardized American spelling barbecue, comma after introductory prep phrase, supplied preposition by; Batch 258: standardized American spelling flavorless, Oxford comma in series, Oxford comma in series; Batch 259: standardized American spelling judgmental, closed compound skydiving, supplied possessive Alzheimer's; Batch 260: comma after introductory sentence adverb Usually, coordinating comma before and, comma between coordinate adjectives long, warm). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 263 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 51,824 decisions, 46,311 published, 5,513 rejected and 871 disclosed edits. Runtime: 48,524 examples, 50,412 sentence records and 61,307 rich records; ledger: 66,820 applied decisions (61,307 publication and 5,513 deprecated). This continuation adds 1,737 examples across batches 251–260, leaving 51,476 more reviewed publications to reach 100,000. All 46,311 English-only approved objects match runtime exactly and pass both adapters (92,622 checks). Rejected IDs remain absent. Shard 093 was completed with 500 records, new shards `examples/094.json`, `095.json`, `096.json` (500 records each), and shard `examples/097.json` (24 records) are registered in the manifest. There are 70,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,468 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `d51e50597c3b0226ef5886d6f7602761d58c89af` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 261 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 51,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 261–270

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 261 | 200 | 187 | 13 | 7 |
| 262 | 200 | 171 | 29 | 6 |
| 263 | 200 | 170 | 30 | 5 |
| 264 | 200 | 168 | 32 | 7 |
| 265 | 200 | 174 | 26 | 5 |
| 266 | 200 | 162 | 38 | 4 |
| 267 | 200 | 164 | 36 | 4 |
| 268 | 200 | 159 | 41 | 4 |
| 269 | 200 | 176 | 24 | 7 |
| 270 | 200 | 160 | 40 | 9 |
| Total | 2,000 | 1,691 | 309 | 58 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 261: standardized closed compound heatstroke, comma after introductory sentence adverb Usually, Oxford comma in series, removed superfluous indefinite article before surgery, corrected number agreement to plural worlds in proverb, standardized past subjunctive after It's time, normalized to natural verbal form exercise; Batch 262: coordinating comma between independent clauses, standardized directional preposition into her car, standardized American spelling favorite, Oxford comma in series, coordinating comma between independent clauses, coordinating comma before but; Batch 263: standardized American collective noun agreement eats, standardized closed compound seabed, coordinating comma between balanced independent clauses, coordinating comma between balanced clauses, standardized American spelling airplane; Batch 264: standardized American spelling protesters, standardized American spelling color, standardized American spelling color, standardized American spelling color, standardized singular count noun a sunburn, capitalized celestial body the Moon, hyphenated compound adjective most-read; Batch 265: supplied definite article the before musical instrument, standardized closed compound email, standardized conjunction as in comparative clause, coordinating comma between imperative clauses, standardized modal contraction You'd better; Batch 266: standardized American spelling industrialized, coordinating comma between compound predicates with temporal connective, coordinating comma between imperative clauses, coordinating comma between compound predicates; Batch 267: standardized natural nominal colocation the exact date, removed superfluous comma before prepositional phrase except for, standardized hyphenated compound adjective laid-back, standardized formal subjunctive were after wish; Batch 268: coordinating comma between independent clauses, standardized hyphenated compound noun number-crunching, standardized closed compound honeybees, standardized directional preposition to YouTube; Batch 269: comma after introductory subordinate clause, comma after introductory locative prepositional phrase, comma after introductory prepositional phrase, removed redundant adverb together after transitive align, standardized natural bare meal noun take my boyfriend lunch, standardized hyphenated compound noun pencil-pusher, comma after introductory subordinate clause; Batch 270: standardized hyphenated compound noun party-pooper, standardized natural prepositional phrase get off work, standardized plural count noun types of movies, standardized natural negative adverbial clause either, coordinating comma between independent clauses, standardized predicate negative is not good for reading, standardized two independent sentences to prevent comma splice, coordinating comma between independent clauses before so, removed superfluous parenthetical commas around adverbial phrase in private). Near duplicates, cross-corpus duplicates (such as sent.tatoeba.5308251 matching published 2268994) and intra-slice duplicate variations were removed during review. All 309 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 53,824 decisions, 48,002 published, 5,822 rejected and 929 disclosed edits. Runtime: 50,215 examples, 52,103 sentence records and 62,998 rich records; ledger: 68,820 applied decisions (62,998 publication and 5,822 deprecated). This continuation adds 1,691 examples across batches 261–270, leaving 49,785 more reviewed publications to reach 100,000. All 48,002 English-only approved objects match runtime exactly and pass both adapters (96,004 checks). Rejected IDs remain absent. Shard 097 was completed with 500 records, new shards `examples/098.json`, `099.json` (500 records each), and shard `examples/100.json` (215 records) are registered in the manifest. There are 68,355 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,158 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `931a64714d93342d93ae59cc3de55e5391c680f6` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 271 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 53,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 271–280

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 271 | 200 | 180 | 20 | 6 |
| 272 | 200 | 176 | 24 | 8 |
| 273 | 200 | 186 | 14 | 6 |
| 274 | 200 | 187 | 13 | 2 |
| 275 | 200 | 190 | 10 | 2 |
| 276 | 200 | 193 | 7 | 1 |
| 277 | 200 | 191 | 9 | 7 |
| 278 | 200 | 191 | 9 | 4 |
| 279 | 200 | 189 | 11 | 2 |
| 280 | 200 | 188 | 12 | 1 |
| Total | 2,000 | 1,871 | 129 | 39 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-nine accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 271: Oxford comma in series, standardized closed compound counterintuitive, standardized lowercase jack-o'-lantern, standardized natural liquid colocation glass of water, standardized American prepositional idiom on weekends, standardized closed compound sandcastle; Batch 272: coordinating comma between independent clauses before so, standardized formal subjunctive were after wish, standardized preposition from after different, standardized closed compound hotspots, coordinating comma between independent clauses before and, standardized open compound real estate developer, removed superfluous parenthetical comma before prepositional phrase in his or her own way, comma before concluding adverbial phrase no matter what; Batch 273: standardized closed compound snowbank, standardized adjective form from innovating to innovative, standardized American spelling from cauterised to cauterized, standardized plural possessive parents' house, standardized compound adjective low-income, coordinating comma between independent clauses before and; Batch 274: standardized compound noun cash-flow before problem, standardized second conditional verb form from you're to you were; Batch 275: standardized closed compound seasickness, standardized closed compound catchphrase; Batch 276: standardized closed compound shipshape; Batch 277: standardized compound adjective handicap-accessible, standardized open compound fairy tales, added comma after introductory adverb Obviously, standardized verb collocation from do to provide before medical aid, added comma after introductory adverb Essentially, standardized compound Whatever happened, expanded nonstandard contracted relative pronoun who're to who are; Batch 278: added coordinating comma before and, added missing indefinite article a before simple breach of contract, capitalized proper noun Navy, removed redundant pronoun it before gerund working here; Batch 279: removed redundant definite article before both of you, added coordinating comma before but; Batch 280: standardized compound adjective non-life-threatening). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 129 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 55,824 decisions, 49,873 published, 5,951 rejected and 968 disclosed edits. Runtime: 52,086 examples, 53,974 sentence records and 64,869 rich records; ledger: 70,820 applied decisions (64,869 publication and 5,951 deprecated). This continuation adds 1,871 examples across batches 271–280, leaving 47,914 more reviewed publications to reach 100,000. All 49,873 English-only approved objects match runtime exactly and pass both adapters (99,746 checks). Rejected IDs remain absent. Shard 100 was completed with 500 records, new shards `examples/101.json`, `102.json`, `103.json` (500 records each), and shard `examples/104.json` (86 records) are registered in the manifest. There are 66,353 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,027 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `73bb268c946261caeef234f26b527ca226d9c3ad` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 281 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 55,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 281–290

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 281 | 200 | 187 | 13 | 3 |
| 282 | 200 | 192 | 8 | 7 |
| 283 | 200 | 188 | 12 | 4 |
| 284 | 200 | 184 | 16 | 6 |
| 285 | 200 | 191 | 9 | 4 |
| 286 | 200 | 181 | 19 | 6 |
| 287 | 200 | 186 | 14 | 1 |
| 288 | 200 | 187 | 13 | 2 |
| 289 | 200 | 192 | 8 | 2 |
| 290 | 200 | 190 | 10 | 2 |
| Total | 2,000 | 1,878 | 122 | 37 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-seven accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 281: standardized verb form disperse, added comma after introductory sentence adverb Structurally,, standardized directional preposition into his car; Batch 282: standardized subordinate clause word order where we are, standardized closed compound healthcare, standardized colloquial have got to have to, added coordinating comma before and, added comma between coordinate predicates, capitalized proper noun Army, added comma after introductory adverb Hopefully,; Batch 283: standardized hyphenated compound noun clock-watching, corrected subject-verb agreement to plural What are, standardized prepositional phrase on Monday, standardized idiom lie low; Batch 284: added coordinating comma before and, standardized closed compound campsite, standardized prepositional phrase on Monday, standardized prepositional phrase on Monday, standardized prepositional phrase on Monday, removed superfluous indefinite article a before comparative easier; Batch 285: standardized formal subjunctive were after wish, standardized adverb really before adjective conscientious, capitalized proper playing card Queen of Spades, standardized prepositional phrase clear to you; Batch 286: added comma after introductory sentence adverb Hopefully,, standardized hyphenated compound bow-hunting, standardized closed compound adverb overnight, standardized singular noun phrase double standard, standardized temporal idiom from now on, standardized closed compound adjective hardworking; Batch 287: standardized modal auxiliary negative could never swim; Batch 288: capitalized proper noun American Dream, standardized formal subjunctive were after wish; Batch 289: replaced inappropriate question mark with a period on conditional imperative clause, supplied missing infinitive particle to before verb do; Batch 290: standardized colloquial adverb real to really before adjective proud, hyphenated compound adjective high-quality before noun tires). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 122 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 57,824 decisions, 51,751 published, 6,073 rejected and 1,005 disclosed edits. Runtime: 53,964 examples, 55,852 sentence records and 66,747 rich records; ledger: 72,820 applied decisions (66,747 publication and 6,073 deprecated). This continuation adds 1,878 examples across batches 281–290, leaving 46,036 more reviewed publications to reach 100,000. All 51,751 English-only approved objects match runtime exactly and pass both adapters (103,502 checks). Rejected IDs remain absent. Shard 104 was completed with 500 records, new shards `examples/105.json`, `106.json` (500 records each), and shard `examples/107.json` (464 records) are registered in the manifest. There are 64,353 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,905 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `3cebf4a64d1f27150175d0458fa5ba986e6807e4` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 291 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 57,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.
