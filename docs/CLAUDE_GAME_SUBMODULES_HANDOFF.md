# Claude Handoff Spec — Game Submodules (`games/*`) for English Content v2

**Scope Boundary:** This document specifies all **game submodule changes** intentionally excluded from the root-repository v2 implementation on branch `feature/english-learning-content-v2`. Root-repo contracts, indexes, adapters, Topic Packs, and Portal `/english` keep **100% backward compatibility** with `typing-game:english-content:v1:activity-dataset` and `typing-game:learning:v1:attempt` until these submodule updates are implemented by Claude.

---

## 0. Submodule Topology & Safety Rules

- `games/monkeytype` (`sinhvienaiti/monkeytype`, currently on feature commit `eee4a246`)
- `games/recall-typing` (`sinhvienaiti/recall-typing`, currently on commit `3ace1f48`)
- `games/vocab-shooter` (`sinhvienaiti/vocab-shooter`, currently on commit `01ddaafd`)
- `games/space-typing` (`sinhvienaiti/space-typing`, currently on commit `14dccb2b`)
- `games/karaoke-typing` (`sinhvienaiti/karaoke-typing`, gitlink `-3402d0e0` — **NOT checked out in this workspace / public CI**; DO NOT break `v1` postMessage contracts consumed by Karaoke Typing).

Each modified game needs a commit/branch in its own submodule repository first, followed by updating the submodule gitlink pointer in the parent repository.

---

## 1. Priority 1 — `games/monkeytype` (High Impact)

### 1.1 Replace the 463-shard sequential crawler in `rich-content.ts`
- **File:** `games/monkeytype/frontend/src/ts/learning/rich-content.ts` (`createRichEnglishContentClient`, `loadByPrefix`, `loadPublishedPracticeExercises`, `loadPublishedContextClozeExercises`, `loadPublishedSentenceBuilderExercise`)
- **Problem:** Currently `loadByPrefix` loops sequentially (`for (const shard of shards) await loadShard(...)`). Calling `loadPublishedContextClozeExercises` fetches **both** all `exercises-*` (~245 MB, 203 shards) **and** all `examples-*` (~275 MB, 260 shards) sequentially (~520 MB, 463 HTTP requests) just to slice `<= 40` items. Furthermore `shardCache` has no eviction cap.
- **Required Fix:**
  1. Read `https://typing-game.local/english-content/indexes/availability.json` and `indexes/activities/{activity}.json` instead of scanning all shards.
  2. Pick shard subset by `cefr` and randomized seed/cursor, then resolve linked `sourceSentenceIds` via `indexes/by-id/{bucket}.json` (256-bucket SHA-256 hash prefix).
  3. Enforce `maxConcurrency` (e.g., 4–6), bounded LRU shard/bucket caches (e.g., 24 shards / 32 buckets), and pin a single `contentVersion` per session.
  4. Verify shard `bytes` / `sha256` if provided in `manifest.json`.

### 1.2 Upgrade Answer Grading & Error UX in `rich-practice.ts` / `rich-practice-ui.ts` / `context-cloze.ts`
- **Files:**
  - `games/monkeytype/frontend/src/ts/learning/rich-practice.ts`
  - `games/monkeytype/frontend/src/ts/learning/rich-practice-ui.ts`
  - `games/monkeytype/frontend/src/ts/learning/context-cloze.ts`
- **Required Fix:**
  1. Consume the shared v2 grading rules (`acceptedAnswers[]`, `gradingMode`, meaning-preserving normalization for contractions `cannot`/`can't`, `do not`/`don't`, whitespace, optional end punctuation when permitted).
  2. Support the three-way outcome `"correct" | "incorrect" | "needs-review"`:
     - **Do NOT** record `result: "wrong"` to v1 `typing-game:learning:v1:attempt` when an item is open-ended / `guided-self-check` or returns `"needs-review"`.
     - Distinguish in feedback UI (`rich-practice-ui.ts`) between ungrammatical error, context-fit mismatch, and open answer needing self-check.
  3. **Fix Grammar Mastery Pollution:** In `buildRichPracticeLearningEvents`, **stop blindly emitting `entityType: "grammar"` mastery events for every `gr.*` in `targetIds` when `targetConfidence === "unverified-rotational"` (or on `ex.cloze.e11.*` / `ex.transformation.e11.*`)**, because E11 cloze/transformation slices assigned `gr.*` round-robin by CEFR regardless of blank content.

### 1.3 Receive Portal `/english` Activity Datasets & Topic Packs via `postMessage`
- **Files:**
  - `games/monkeytype/frontend/src/ts/learning/review-dataset.ts`
  - `games/monkeytype/frontend/src/ts/learning/rich-practice-ui.ts` (or dedicated launcher handler)
- **Required Fix:**
  1. Currently Monkeytype only listens to `typing-game:learning:v1:review-dataset` and ignores `typing-game:english-content:v1:activity-dataset`.
  2. Add a validated listener for `ENGLISH_ACTIVITY_DATASET_MESSAGE` (supporting multi-answer `acceptedAnswers[]`, `gradingMode`, `packId`, `learningFocus`) so Portal `/english` can launch Monkeytype directly into specific Topic Packs or filtered activity slices. Once implemented, add `"monkeytype"` back to `RichPracticeGameId` in root `portal/src/english-content/activity-session.ts`.

---

## 2. Priority 2 — `games/recall-typing`, `games/vocab-shooter`, `games/space-typing`

All three submodules already listen for `typing-game:english-content:v1:activity-dataset` and map items into `VocabularyEntry` for character-by-character typing (`entry.en[cursor]`).

- **Files:**
  - `games/recall-typing/src/learning/shared.ts` & `src/types.ts`
  - `games/vocab-shooter/src/learning/shared.ts` & `src/types.ts`
  - `games/space-typing/src/learning/shared.ts` & `src/types.ts`
- **What Root Repo Already Preserves For Free:**
  - Root `activity-dataset.mjs` still emits `version: 1`, `type: "typing-game:english-content:v1:activity-dataset"`, and `answerText: string`.
  - Root `activity-source.mjs` enforces `maxAnswerLength` (200 for Recall/Shooter, 240 for Space) when building payloads for those games until updated.
- **Recommended Claude Enhancements:**
  1. Preserve optional additive v2 item properties in parsers (`acceptedAnswers?: string[]`, `gradingMode?: string`, `learningFocus?: string`, `entityKind?: string`, `senseId?: string`, `packId?: string`, `cefr?: string`) rather than discarding them.
  2. If implementing free-input / choice variants (e.g., `contextual-usage` multiple-choice / gap-type mode), support `acceptedAnswers[]` validation and forward `needs-review` cleanly without emitting false `wrong` v1 attempts.
  3. Emit optional v2 skill-evidence hints (e.g., distinguishing `typing-fluency` keystroke speed from `recall` / `recognition` / `usage-discrimination`) so Portal can record richer Learning Evidence v2 alongside v1 events.
  4. Review hard length caps (`cleanAnswer.length > 200` / `240`) if longer `listening-typing` / `contextual-usage` sentences should wrap gracefully in UI.

---

## 3. Priority 3 — `games/karaoke-typing`

- Keep `typing-game:english-content:v1:activity-dataset` (`contentId`, `entityType`, `entityId`, `promptText`, `answerText`, `meaningVi`, `audioText`) and `typing-game:learning:v1:attempt` ABI untouched so Karaoke Typing works seamlessly without submodule edits.
