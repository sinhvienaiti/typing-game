# English Learning Content Expansion v2.1 — Root-Repo Architecture & Execution Plan

**Branch:** `feature/english-learning-content-v2` (branched from PR #48 checkpoint `648b2f68` on `feature/english-learning-content-system`)  
**PR #48 Policy:** Strictly preserved untouched and in Draft (`draft: true`).  
**Scope Boundary:** Root repository only (`shared/`, `portal/`, `scripts/`, `content/`, `infra/`, `docs/`). All edits inside `games/*` submodules are explicitly **excluded** from this plan and tracked separately in [CLAUDE_GAME_SUBMODULES_HANDOFF.md](./CLAUDE_GAME_SUBMODULES_HANDOFF.md).

---

## 1. Phase 0 Empirical Baseline Findings (Measured on `648b2f68`)

Reports generated:
- `content/english/reports/v2-phase0-runtime-baseline.json`
- `content/english/reports/e13-causal-gap-audit.json`
- `content/english/reports/v2-phase0-v1-hygiene-audit.json`

### Key Measured Problems Resolved by v2.1
1. **Unbounded Runtime Scans (P1-01):**
   - `findById` for 10 IDs (cold): **534 requests (530 shards), 614.54 MB** scanned (`~2,037 ms` disk parse in Node).
   - `loadPublishedEnglishActivityRecords` for 20 items: **204 requests / 244.89 MB** (`cloze` & `translation`) or **261 requests / 274.67 MB** (`example-typing`).
   - `publishedEnglishActivityAvailability` on Portal `/english`: **485–509 requests / 564–567 MB** scanned just to render item counts.
   - Always returns first `limit` items from shard `000` with no CEFR filter or fresh randomization seed.
2. **Adapter Multi-Answer Truncation & Translation Coverage Gap (P1-02):**
   - **6,644 published exercises** (`1,280` cloze, `2` translation, `5,362` transformation) have `acceptedAnswers.length > 1`, but `shared/english-content/game-adapters.mjs` drops alternatives 2..N to single `answerText`.
   - Meanwhile **99.99%** (`20,598 / 20,600`) of translation exercises have only 1 recorded `acceptedAnswers` string (`5,466` records even share `sourceSentenceIds` across alternate Vietnamese prompts without alternate English targets).
3. **Hidden V1 Attribution & Rule Hygiene Defects (Audit Supplement):**
   - **50,000** `ex.cloze.e11.*` and **30,000** `ex.transformation.e11.*` assign grammar `targetIds` round-robin (`topicRotator % topicsByCefr[cefr].length`), producing false links such as blanking `"Singapore"` under `gr.a2.too-much-many-enough-noun` (`1,259` mid-sentence capitalized proper noun cloze blanks detected; `315` heuristic past-simple/present-modal mismatches detected in transformations).
   - **9** `err.e11.*` records flag grammatically valid Past Simple homographs like `"She read the Quran."` as 3rd-person singular errors (`"She reads..."`).
   - **2** advertised game activities (`sentence-building`, `contextual-usage`) currently have **0** published records in `exercises-*`.
   - On `129,813` published examples, only **0.69%** (`900`) carry `grammarIds` and **0.25%** (`331`) carry `lexicalIds`, proving topic/evidence lookup must rely on reviewed indexes and manifests rather than ad-hoc runtime filtering.
4. **E13 Full Causal Gap Breakdown (9,695 Phrase Items vs 129,813 Examples):**
   - **Collocations (`5,000`):** `111` linked, **`111` matcher-false-negative** + **`61` gapped editorial candidates** (`172` recoverable in existing corpus), `4,717` true absence.
   - **Phrasal Verbs (`1,000`):** `239` linked, **`65` matcher-false-negative** + **`26` gapped editorial candidates** (`91` recoverable), `670` true absence.
   - **Chunks (`2,000`):** `97` linked, **`36` matcher-false-negative** + **`3` editorial candidates**, `1,864` true absence.
   - **Idioms (`1,185`):** `25` linked, **`93` matcher-false-negative** + **`10` editorial candidates** (`103` recoverable — 4x current linked coverage!), `1,057` true absence.
   - **Verb Patterns (`510`):** `256` linked, **`254` unsupported syntactic frames** (all 254 have lemma hits in corpus requiring structural frame adjudication), `0` true absence.
   - **Vocabulary Overlap:** All `300 / 300` E03 lexemes map to the `18,000` legacy vocabulary keys (`17,700` legacy words await future E14 enrichment).

---

## 2. Optimized Root-Repo Architecture (v2.1)

### 2.1 Bucketed Static Indexes (`shared/indexes/`)
Instead of a single ~25 MB monolithic JSON lookup file for 262,621 records:
- `shared/indexes/manifest.json` — `contentVersion`, `releaseDigest`, bucket count (`256`), shard counts, pack summary.
- `shared/indexes/availability.json` (~2 KB) — exact counts by `(activity, cefr)` and overall dataset totals.
- `shared/indexes/activities/{activity}.json` — compact shard descriptors (`dataset`, `shardId`, `path`, `count`, `cefrCounts`, `maxAnswerLength`, `curatedTargetCount`).
- `shared/indexes/by-id/{00..ff}.json` — 256 SHA-256 prefix buckets mapping `contentId -> [dataset, shardPath, offset]`.
- `shared/indexes/evidence/{00..ff}.json` — 256 SHA-256 prefix buckets mapping canonical `targetId` (`lex.*`, `sense.*`, `col.*`, `pv.*`, `pat.*`, `chunk.*`, `idiom.*`, `gr.*`, `sent.*`) -> reviewed `{ exampleIds, exerciseIds, usageIds, mistakeIds }`.
- `shared/indexes/packs/manifest.json` & `packs/{packId}.json` — curated Topic Pack definitions pinned to `contentVersion`.
- `scripts/publish-english-content.mjs` populates `bytes` and `sha256` inside `shared/*/manifest.json` (already permitted by `runtime-manifest.schema.json`).
- Both `infra/nginx/typing-game.local.dev.conf` and `infra/nginx/typing-game.local.play.conf` serve `/english-content/indexes/`.

### 2.2 Bounded Loader, Multi-Answer Grading & Learning Evidence v2
- `shared/english-content/runtime-loader.mjs`: Bounded LRU shard/bucket caches, bounded concurrency (`maxConcurrency`), session `contentVersion` pinning, `resolvePublishedByIds(ids, options)`, `getEvidence(targetId, filters)`.
- `shared/english-content/activity-source.mjs`: Indexed O(1) availability counts, CEFR + seeded cursor + length-bounded selection (`loadPublishedEnglishActivityRecords`), `loadPublishedTopicPack(loader, packId)`.
- `shared/english-content/grading.mjs`: Pure normalized multi-answer evaluator supporting `exact-normalized | closed-choice | guided-self-check` with 3-state outcome `correct | incorrect | needs-review` and meaning-preserving contraction normalization.
- `shared/english-content/game-adapters.mjs` & `activity-dataset.mjs`: Backward-compatible `v1` payload (`answerText` preserved for Karaoke/Recall/Shooter/Space) plus additive `acceptedAnswers[]`, `gradingMode`, `cefr`, `targetConfidence`, `learningFocus`, `packId`, while preventing rotational E11 `gr.*` IDs from inflating `grammar` mastery.
- `shared/learning/evidence-v2.mjs`: Local IndexedDB-compatible evidence tracker separating `typing-fluency`, `recognition`, `recall`, `usage-discrimination`, `comprehension`, and `production` without breaking `LEARNING_PROFILE_VERSION = 1`.
- `portal/src/english-content/`: Fast `/english` counts, CEFR selector, Randomized Seed mode, Topic Pack launcher & Portal-native multi-answer Practice Runner (allowing immediate playtesting of Topic Packs, `contextual-usage`, `sentence-building`, and `needs-review` flows inside Portal without modifying `games/*`).

---

## 3. Execution Phases (Root Repo Only)

| Phase | Scope | Acceptance Gate |
|---|---|---|
| **Phase 0** *(Done)* | Baseline benchmark + E13 causal audit + V1 hygiene audit | 3 empirical JSON reports written; root causes quantified |
| **Phase 1** | Shard `bytes/sha256` + `shared/indexes/` generator + Nginx routes + `runtime-loader.mjs` + `activity-source.mjs` + `grading.mjs` + `game-adapters.mjs` / `activity-dataset.mjs` + `evidence-v2.mjs` + Portal `/english` runner | Cold 10-ID lookup & `/english` availability drop from **~567 MB / ~509 requests** to **< 1 MB / <= 15 requests**; 6,644 multi-answer exercises preserved; 0 v1 regressions; all tests & `build:portal` concepts verified |
| **Phase 1.5** | Quarantine rotational E11 `targetIds` attribution; fix ambiguous `"read"` Past Simple rule in `build-e11-mistake-expansion.mjs` + slice; publish starter `sentence-building` & `contextual-usage` reviewed batches | `0` advertised activities with `0` published count; rotational E11 items cannot corrupt `gr.*` mastery |
| **Phase 2A & 2B** | **E13 Recovery + E15 3 Topic Packs Pilot + E14 150-Lexeme/Sense Evidence Pilot**: promote safe morphological/determiner/placeholder example links via `enrichment-links.d/` (zero lemma-only noise); publish 3 reviewed Topic Packs + 150–200 high-value lexeme sense-disambiguated links | Schema + provenance + license + ledger digest checks 100% pass; Portal Topic Pack practice & pre/post tracking verified |
| **Phase 3** | E16 targeted pilot (multi-variant `translation` enrichment + contrast sets) & full CI / Master Plan Acceptance verification on `feature/english-learning-content-v2` | All validators, unit tests, smokes, and E12 audit pass cleanly; Claude handoff spec remains synced |
