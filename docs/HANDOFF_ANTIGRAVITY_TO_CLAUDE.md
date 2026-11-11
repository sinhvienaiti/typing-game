# Handoff: Antigravity -> Claude (`feature/english-learning-content-v2`)

**Ngày cập nhật:** 2026-11-11  
**Repository cha:** `sinhvienaiti/typing-game`  
**Nhánh làm việc hiện tại:** `feature/english-learning-content-v2` (tách từ commit `648b2f68` trên `feature/english-learning-content-system`)  
**Ràng buộc cứng:**
- **Không** sửa/merge/thay đổi nhánh `feature/english-learning-content-system` hay PR #48 (`draft: true`).
- **Không** sửa code trong 5 submodule `games/*` cho đến khi Claude trực tiếp mở nhánh trên từng repo con tương ứng (xem chi tiết kỹ thuật tại `docs/CLAUDE_GAME_SUBMODULES_HANDOFF.md`).
- Các script sau đã được chuyển thành **non-destructive validator** để bảo vệ dữ liệu rà soát thủ công — **tuyệt đối không chạy logic ghi đè**:
  - `scripts/build-e15-topic-packs.mjs`
  - `scripts/build-e14-lexical-pilot.mjs`
  - `scripts/build-v2-starter-activities.mjs`
  - `scripts/build-e13-enrichment-links.mjs`
  - `scripts/enrich-e16-translation-variants.mjs`
  - `scripts/build-e11-cloze-expansion.mjs`

---

## Phần 1 — Các phần Antigravity đã hoàn tất (Root Repo)

### 1.1. Tầng Index tĩnh O(1), Bounded Loader, Chấm điểm v2 & Evidence v2 (Phase 0 – Phase 2)

1. **Audit & Benchmark Phase 0 (`scripts/benchmark-english-content-v1.mjs`, `scripts/audit-english-content-e13-causal-gaps.mjs`, `scripts/audit-english-content-v1-hygiene.mjs`):**
   - Đo nút thắt quét tuần tự toàn kho trên v1 và sinh 3 báo cáo định lượng trong `content/english/reports/`.
   - **Kết quả tối ưu truy vấn đã đo trước khi mở rộng x5 (`content/english/reports/v2-phase1-runtime-benchmark.json`, timestamp `2026-11-10T16:57:13Z`):**
     - `availability_monkeytype`: từ `2,200.8 ms / 780 req / 852.89 MB` -> **`0.21 ms / 1 req / 0.0044 MB`** (`10,480x` nhanh hơn, giảm `192,178x` bytes).
     - `activity_cloze_20`: từ `623.05 ms / 215 req / 256.14 MB` -> **`3.34 ms / 2 req / 1.24 MB`** (`186.5x` nhanh hơn).
     - `activity_translation_20`: từ `640.66 ms / 215 req / 256.14 MB` -> **`4.03 ms / 2 req / 1.15 MB`** (`159x` nhanh hơn).
     - `activity_example-typing_20`: từ `577.68 ms / 261 req / 274.73 MB` -> **`2.57 ms / 2 req / 1.15 MB`** (`224.8x` nhanh hơn).
     - `resolve_10_ids_batch_cold`: từ `5,247.71 ms / 1,831 req / 2,072.04 MB` -> **`36.78 ms / 19 req / 8.86 MB`** (`142.7x` nhanh hơn).
2. **Tạo & xuất bản Static Indexes (`shared/indexes/`) + Nginx routing:**
   - Tạo `scripts/english-indexes-core.mjs`, `scripts/generate-english-content-indexes.mjs`, tích hợp vào `scripts/publish-english-content.mjs` (kèm `bytes` và `sha256` cho từng shard).
   - Sinh `shared/indexes/manifest.json`, `availability.json`, `activities/{activity}.json`, `by-id/{00..ff}.json`, `evidence/{00..ff}.json`, `packs/manifest.json` + `packs/{packId}.json`, và `lexical/e14-pilot.json` (tách riêng khỏi `shared/dictionary` để giữ nguyên ABI v1 `300/300/300`).
   - Thêm route `/english-content/indexes/` trong `infra/nginx/typing-game.local.dev.conf` và `infra/nginx/typing-game.local.play.conf`.
3. **Runtime Loader, Adapters & Chấm điểm đa đáp án (`shared/english-content/`):**
   - `shared/english-content/index-bucket.mjs`: hàm băm bucket 256 nhánh thuần JS chạy được trên trình duyệt (không phụ thuộc `node:crypto`).
   - `shared/english-content/runtime-loader.mjs`: cache LRU có giới hạn kích thước, giới hạn concurrency, kiểm tra tính toàn vẹn `bytes`/`sha256` & khóa `contentVersion` đồng bộ xuyên phiên; thêm `resolvePublishedByIds`, `getEvidence`, `loadAvailability`, `loadActivityIndex`, `loadTopicPacksManifest`, `loadTopicPack`, `loadLexicalPilot`.
   - `shared/english-content/activity-source.mjs`: đếm O(1), lọc CEFR + random seed + `maxAnswerLength`, giới hạn hội thoại `<= 100` lượt, thêm `loadPublishedTopicPack`.
   - `shared/english-content/game-adapters.mjs` & `activity-dataset.mjs`: bảo toàn payload `v1` (`answerText: string`) cho các game cũ, đồng thời truyền bổ sung `acceptedAnswers[]`, `gradingMode`, `cefr`, `targetConfidence`, `learningFocus`, `packId`; bổ sung `hasVerifiedTargetAttribution()` để cách ly các bản ghi E11 gán `targetIds` xoay vòng (`ex.cloze.e11.*`, `ex.transformation.e11.*`), không làm sai lệch điểm grammar mastery.
   - `shared/english-content/grading.mjs`: `evaluateEnglishAnswer` & `normalizeEnglishForGrading` hỗ trợ `exact-normalized | closed-choice | guided-self-check`, biến thể viết tắt giữ nguyên nghĩa, và trả về 3 trạng thái `correct | incorrect | needs-review`.
4. **Learning Evidence v2 (`shared/learning/`):**
   - `shared/learning/evidence-v2.mjs` & `shared/learning/browser-evidence-store.mjs`: phân tách `typing-fluency` khỏi các chiều năng lực ngữ nghĩa/ngữ pháp (`recognition`, `recall`, `usage-discrimination`, `comprehension`, `production`); chặn ghi event `"wrong"` vào profile khi kết quả là `needs-review` trong khi vẫn giữ `LEARNING_PROFILE_VERSION = 1`.
5. **Portal `/english` (`portal/src/english-content/`, `portal/src/main.ts`, `portal/src/styles.css`):**
   - Hiển thị số lượng bài O(1), bộ lọc CEFR, nút random seed mới, luồng chọn **Topic Pack** và **Guided Multi-Answer Practice Runner** ngay trên Portal nối tới `BrowserLearningEvidenceStore` + `BrowserLearningProfileStore`.
   - Do Monkeytype chưa nhận `typing-game:english-content:v1:activity-dataset`, tạm loại `"monkeytype"` khỏi `RichPracticeGameId` trong `portal/src/english-content/activity-session.ts`.

---

### 1.2. Mở rộng nội dung x5 & Rà soát thủ công tuần tự Mục 1 – Mục 5 (không dùng script ghi đè)

Toàn bộ dữ liệu dưới đây đã được rà/sửa trực tiếp qua từng lô và khóa bảo vệ bằng validator không ghi đè:

| Mục | Phạm vi & File chính | Kết quả định lượng hiện tại |
|---|---|---|
| **Mục 1 — E15 Topic Packs** | `content/english/packs/*.json` + schema `shared/schemas/english-content/topic-pack.schema.json` + validator `scripts/build-e15-topic-packs.mjs` | **15** Topic Packs (`pack.*` từ A1 -> C1) với **343** mục học kiểm tay theo mạch `pre-check -> input -> practice -> contrast -> post-check`, toàn bộ tham chiếu `contentId` hợp lệ và prompt dịch chuẩn. |
| **Mục 2 — E14 Từ vựng đa nghĩa** | `content/english/dictionary/e14-sense-pilot.json` + validator `scripts/build-e14-lexical-pilot.mjs` | **750** lexemes (`163` từ đa nghĩa, `917` senses, `1,769` verified example links) đối chiếu với `e03` & `shared/vocabulary`, xuất riêng qua `shared/indexes/lexical/e14-pilot.json`. |
| **Mục 3 — Contextual Usage & E16 Contrast** | `content/english/sentences/v2-starter-contextual-exercises.json`, `v2-e16-contrast-exercises.json` + `decisions.d/v2-*.json` + validator `scripts/build-v2-starter-activities.mjs` | **2,000** bài (`1,200` `contextual-usage` + `800` bài đối chiếu lỗi hay gặp E16), loại bỏ tham chiếu topic sai và làm sạch câu thiếu ngữ cảnh. |
| **Mục 4A/4B — Sentence Building & Listening Typing** | `content/english/sentences/v2-starter-building-exercises.json`, `v2-starter-listening-exercises.json` + `decisions.d/v2-*.json` + validator `scripts/build-v2-starter-activities.mjs` | **2,500** bài `sentence-building` + **1,000** bài `listening-typing` (A1–C1), đã rà độ tự nhiên, ngữ pháp và tính phù hợp CEFR. |
| **Mục 4C — E13 Morphological Example Links** | `content/english/reviews/enrichment-links.d/e13-morphological-links.json` + validator `scripts/build-e13-enrichment-links.mjs` | **3,547** liên kết ví dụ biến thể hình thái sạch (`177` collocations -> `1,102` links; `372` phrase items -> `2,445` links; tổng **4,493** E04 example links được áp dụng khi publish). |
| **Mục 5A — E11 Translation & E16 Variants** | `content/english/sentences/e11-translation-slice-01..40.json` + `decisions.d/e11-translation-slice-*.json` + validator `scripts/enrich-e16-translation-variants.mjs` | **20,000** bản ghi trên 40 slice: sửa **8** ID trùng, loại bỏ biến thể sai ngữ pháp (`I've to`, `he's.`, v.v.), dịch dứt điểm toàn bộ **1,002** prompt placeholder `"Dịch sang tiếng Anh: ..."` (**0** còn sót), giữ **`6,821` bản ghi dịch nhiều đáp án**. |
| **Mục 5B — E11 Common Mistakes** | `scripts/build-e11-mistake-expansion.mjs` + các `e11-mistake-slice-*.json` liên quan | Sửa **9** bản ghi `"read"` thì quá khứ gắn nhầm lỗi chia động từ ngôi 3 số ít -> `pastTenseHomographReadAmbiguityCount: 0` trên toàn bộ `10,388` mistakes. |
| **Mục 5C — E11 Cloze** | `content/english/sentences/e11-cloze-slice-01..100.json` (`98` slice chỉnh sửa) + `decisions.d/e11-cloze-slice-01..100.json` (`98` file cập nhật digest) + validator `scripts/build-e11-cloze-expansion.mjs` | **50,000** bản ghi trên 100 slice: giảm `properNounMidSentenceBlankSuspects` từ `1,259` xuống còn `99`, loại trùng lặp nội bộ (`0` dups trong E11), đồng bộ `sourceDigest` cho toàn bộ ledger (`118` bản ghi nhiều đáp án hợp lệ). |

---

### 1.3. Kiểm định & Publish sau lần chỉnh sửa cuối (toàn bộ exit code `0`)

- `node scripts/publish-english-content.mjs`: xuất bản **`268,121` bản ghi runtime** (`dictionary=900`, `grammar=300`, `sentences=257226`, `phrases=9695`), `4,493` E04 example links, tạo chỉ mục `74,429` evidence targets, `15` packs, `750` E14 entries.
- `node scripts/validate-english-content-reviews.mjs`: **`275,431 / 275,431`** review decisions khớp hoàn toàn (`publishDecisions: 268,121`).
- Non-destructive validators riêng lẻ:
  - `node scripts/build-e11-cloze-expansion.mjs`: `100` slices / `50,000` records `ok`.
  - `node scripts/enrich-e16-translation-variants.mjs`: `40` slices / `20,000` records / `6,821` multi-variant `ok`.
- `pnpm english-content:validate`: PASS (`45` schemas, `300` curriculum topics, `39` grammar scale batches / `288` topics, legacy vocabulary ABI preserved).
- `pnpm english-content:test`: **`120 / 120` PASS** (`0` fail, `0` skipped).
- `pnpm learning:check` & `pnpm learning:test`: PASS (**`59 / 59` PASS**).
- `pnpm english-content:licenses`, `pnpm english-content:e10`, `pnpm english-content:e12:audit`, `pnpm english-content:dedupe`, `pnpm english-content:coverage`, `pnpm english-content:pilot`: toàn bộ PASS.
- `pnpm english-content:e11`, `pnpm english-content:e11:runtime`, `pnpm english-content:e11:records`: **khớp `11 / 11` mục tiêu E11** (`missingCount: 0`, `extraCount: 0` cho `grammar-topics=300`, `verb-patterns=510`, `collocations=5000`, `phrasal-verbs=1000`, `idioms-chunks=3185`, `common-mistakes=10388`, `example-sentences=129813`, `translation-pairs=20600`, `cloze-exercises=50600`, `sentence-transformations=30100`, `dialogue-examples=10125`).
- `pnpm english-content:runtime:smoke` & `pnpm english-content:e11:games`: PASS (`35` game/activity flows trên `5` game, `202` items).
- `pnpm build:portal`: PASS (`tsc --noEmit && vite build`).
- `games/` git status: **0** thay đổi trên toàn bộ 5 submodules.

---

## Phần 2 — Các phần Claude cần xử lý để tối ưu

Phần còn lại giao cho Claude gồm **3 nhóm việc chính** (từ bắt buộc cho tích hợp game đến tối ưu UX/hiệu năng và mở rộng dữ liệu dài hạn):

### Nhóm A — Nâng cấp code bên trong các Game Submodule (`games/*`)
*(Chi tiết tên file/hàm ở repo con xem thêm trong `docs/CLAUDE_GAME_SUBMODULES_HANDOFF.md`)*

1. **Ưu tiên 1 — `games/monkeytype` (`sinhvienaiti/monkeytype`, gitlink hiện tại `eee4a246`):**
   - **Thay thế bộ crawler tuần tự 474 shards (`214` `exercises-*` + `260` `examples-*`):** trong `games/monkeytype/frontend/src/ts/learning/rich-content.ts` (`createRichEnglishContentClient`, `loadByPrefix`, `loadPublishedPracticeExercises`, `loadPublishedContextClozeExercises`, `loadPublishedSentenceBuilderExercise`), chuyển sang đọc `shared/indexes/availability.json`, `indexes/activities/{activity}.json`, và giải `sourceSentenceIds` qua `indexes/by-id/{00..ff}.json`; thêm `maxConcurrency` (4–6), bounded LRU shard/bucket cache, pin 1 `contentVersion` xuyên phiên và verify `bytes`/`sha256` từ `manifest.json`.
   - **Nâng cấp chấm điểm & feedback UI:** trong `rich-practice.ts`, `rich-practice-ui.ts`, `context-cloze.ts`, áp dụng logic chấm đa đáp án chuẩn hóa v2 (`acceptedAnswers[]`, `gradingMode`, contraction equivalence `can't` / `cannot`), hỗ trợ kết quả 3 trạng thái `"correct" | "incorrect" | "needs-review"`. **Tuyệt đối không gửi `result: "wrong"` vào `typing-game:learning:v1:attempt` khi kết quả là `needs-review` / `guided-self-check`**; UI phân biệt rõ lỗi sai ngữ pháp vs lệch ngữ cảnh vs câu cần tự đối chiếu.
   - **Chặn làm nhiễu Grammar Mastery:** trong `buildRichPracticeLearningEvents`, ngừng phát event `entityType: "grammar"` cho mọi `gr.*` khi `targetConfidence === "unverified-rotational"` hoặc với `ex.cloze.e11.*` / `ex.transformation.e11.*`.
   - **Nhận dataset & Topic Pack từ Portal `/english`:** bổ sung listener cho `typing-game:english-content:v1:activity-dataset` trong `review-dataset.ts` / launcher để hỗ trợ `acceptedAnswers[]`, `gradingMode`, `packId`, `learningFocus`.
   - **Mở lại Monkeytype trên Portal:** sau khi Monkeytype xong phần trên, thêm `"monkeytype"` trở lại vào `RichPracticeGameId` và `CAPABILITY_ID` trong `portal/src/english-content/activity-session.ts`.

2. **Ưu tiên 2 — `games/recall-typing` (`3ace1f48`), `games/vocab-shooter` (`01ddaafd`), `games/space-typing` (`14dccb2b`):**
   - Trong `src/learning/shared.ts` & `src/types.ts` của từng game: giữ lại các trường mở rộng v2 thay vì loại bỏ (`acceptedAnswers[]`, `gradingMode`, `learningFocus`, `entityKind`, `senseId`, `packId`, `cefr`).
   - Hỗ trợ chế độ chọn/gõ đa đáp án (vd `contextual-usage`), forward `needs-review` sạch (không phạt `wrong` v1), phát gợi ý Evidence v2 phân biệt `typing-fluency` với `recall`/`recognition`/`usage-discrimination`, và xử lý UI wrap text cho câu vượt ngưỡng `200` / `240` ký tự nếu muốn nới `maxAnswerLength`.

3. **Ưu tiên 3 — `games/karaoke-typing` (gitlink `-3402d0e0`, chưa checkout ở local/CI):**
   - **Không chỉnh sửa** và phải giữ nguyên 100% tương thích ABI v1 (`typing-game:english-content:v1:activity-dataset` & `typing-game:learning:v1:attempt`).

4. **Quy trình Git với Submodule:** Commit & push trên nhánh của từng repo con `games/*`, chạy build verify từng game (`pnpm build:monkeytype`, `pnpm build:recall`, `pnpm build:shooter`, `pnpm build:space`), sau đó mới cập nhật con trỏ submodule gitlink trong root repo.

---

### Nhóm B — Tối ưu Root Repo, Vận hành Portal & Chốt Benchmark trước Release

1. **Quyết định kiến trúc giao diện Portal (`portal/src/english-content/`):**
   - Hiện Antigravity giữ mini **Topic Pack & Guided Multi-Answer Practice Runner** ngay trong `portal/src/english-content/page.ts` + `activity-session.ts` để test nội dung v2 mà chưa cần sửa `games/*`.
   - Sau khi Claude nâng cấp xong `games/monkeytype` (và các game khác), thống nhất với người dùng xem nên **giữ** Practice Runner trong Portal như chế độ luyện nhanh hay **tinh gọn Portal** về chỉ lọc CEFR/pack và đẩy thẳng sang iframe games.
2. **Dọn workspace, cập nhật Benchmark sau mở rộng x5 & Test E2E trên trình duyệt:**
   - Toàn bộ công việc v2 đã được commit trên `feature/english-learning-content-v2`; 5 file queue tạm trong `content/english/review-queues/*.json` tiếp tục được giữ ngoài commit theo quy ước repo (`scratch/`, `pnpm-lock.yaml`, `portal/pnpm-lock.yaml` đã được xóa sạch).
   - Chạy `bash scripts/setup-nginx.sh dev` (hoặc `play`, cần quyền `sudo`) để Nginx local nạp route mới `/english-content/indexes/`.
   - Chạy lại `node scripts/benchmark-english-content-v1.mjs` để cập nhật số đo benchmark trên corpus `268,121` bản ghi (bản lưu hiện tại đo ở `2026-11-10T16:57:13Z` trước khi chốt rà sửa Mục 1–5).
   - Test E2E trên trình duyệt thật / DevTools throttling (mobile cold/hot p95 latency, peak heap, shard requests, offline cache/release rollback, IndexedDB `evidence-v2` + `profile v1`) và chốt tiêu chí định lượng `GO / ITERATE / STOP` cùng người dùng trước khi release (chưa định nghĩa sẵn trong `docs/ENGLISH_LEARNING_CONTENT_V2_PLAN.md`).

---

### Nhóm C — Dư địa Tối ưu Nội dung Dài hạn (đã đo trên dữ liệu hiện tại)

Các hạng mục sau không phải lỗi blocker cho v2 hiện tại, nhưng là phần tồn đọng đã đo cụ thể nếu Claude/đội biên tập muốn tối ưu tiếp chất lượng & độ phủ kho học liệu:

1. **E13 — Ví dụ cho Phrase & `verb-pattern` (`shared/phrases/`, đo trực tiếp sau publish cuối):**
   - Tỉ lệ phrase hiện **chưa có câu ví dụ (`withoutExamples`)**:
     - `collocation`: **`4,794 / 5,000`** (`206` đã có)
     - `chunk`: **`1,867 / 2,000`** (`133` đã có)
     - `idiom`: **`1,103 / 1,185`** (`82` đã có)
     - `phrasal-verb`: **`737 / 1,000`** (`263` đã có)
     - `verb-pattern`: **`254 / 510`** (`256` đã có) — toàn bộ `254` pattern còn thiếu đều thuộc nhóm `unsupported-frame` (có câu chứa lemma trong kho 129k câu nhưng cần matcher/biên tập phân tích cấu trúc cú pháp như `verb + object + bare infinitive`, `verb + object + from + -ing`).
   - Hướng tối ưu: xây dựng syntactic frame matcher cho `254` `verb-pattern` và bổ sung/nạp câu ví dụ mới cho nhóm `true-absence` ở collocation/idiom/phrasal-verb/chunk.
2. **E11 — Cải thiện dữ liệu kế thừa còn sót trong `content/english/reports/v2-phase0-v1-hygiene-audit.json`:**
   - **`315` `ex.transformation.e11.*`** bị gắn cờ `heuristicTopicMismatchCount` (gán topic xoay vòng như `past-simple` cho câu modal/hiện tại).
   - **`99` `ex.cloze.e11.*`** còn gắn cờ `properNounMidSentenceBlankSuspects` (đã giảm mạnh từ `1,259` xuống `99`, chủ yếu là tên người/địa danh/thứ ngày nếu muốn lọc sạch về `0` hoặc gán `targetConfidence: "verified"` theo ngữ pháp thật).
3. **E14 — Phủ rộng Từ vựng đa nghĩa từ `750` lên `18,000` từ legacy:**
   - `e14-sense-pilot.json` hiện phủ `750` từ (`163` từ đa nghĩa / `917` senses); còn khoảng **`17,250` từ** trong `shared/vocabulary` legacy chưa có phân tách sense và ví dụ theo từng nghĩa.
4. **E16 Translation Variants & 2 loại bài tập trống trong `exercises-*`:**
   - `translation`: vẫn còn **`13,777 / 20,600` (`66.88%`)** bài mới có 1 đáp án đơn (chủ yếu câu dài/nhiều vế); có thể bổ sung biến thể tự nhiên theo ngữ cảnh.
   - `exerciseTypesWithZeroPublishedRecordsInExercisesShards`: 2 loại **`collocation`** và **`grammar-typing`** hiện chưa có bản ghi độc lập trong `shared/sentences/exercises/*.json` (đang phục vụ gián tiếp qua `shared/phrases/collocations` và `cloze`/`transformation`); có thể bổ sung shard bài tập chuyên biệt nếu game cần.
5. **E17 Pilot (Reading / Listening / Adaptive Journey):**
   - Thiết kế luồng đọc hiểu ngắn + TTS fallback + kiểm định pre/post unseen items & delayed recall `7/14` ngày khi đã có dữ liệu hiệu quả từ E14/E15/E16.

---

## Lệnh Verify Nhanh Khi Bắt Đầu Phiên Mới

```bash
# 1. Kiểm tra tính toàn vẹn dữ liệu & validator không ghi đè
node scripts/validate-english-content-reviews.mjs
node scripts/build-e11-cloze-expansion.mjs
node scripts/enrich-e16-translation-variants.mjs
node scripts/build-v2-starter-activities.mjs
node scripts/build-e13-enrichment-links.mjs
node scripts/build-e14-lexical-pilot.mjs
node scripts/build-e15-topic-packs.mjs

# 2. Validate, Publish, Unit tests & E11 readiness
pnpm english-content:validate
pnpm english-content:test
pnpm learning:check && pnpm learning:test
pnpm english-content:e10
pnpm english-content:e11 && pnpm english-content:e11:runtime && pnpm english-content:e11:records
pnpm english-content:runtime:smoke
pnpm english-content:e11:games # lưu ý: cập nhật timestamp trong content/english/reports/step11-game-integration-verification.json
pnpm build:portal
```
