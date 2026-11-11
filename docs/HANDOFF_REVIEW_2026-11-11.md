# Kiểm tra bàn giao Antigravity → Claude (2026-11-11)

Phạm vi: hai file `docs/HANDOFF_ANTIGRAVITY_TO_CLAUDE.md` và `docs/CLAUDE_GAME_SUBMODULES_HANDOFF.md`, đối chiếu với checkout `/Volumes/SS990TPRO/htdocs/typing-game-english`, nhánh `feature/english-learning-content-v2`, HEAD `648b2f68`. Mọi lệnh chạy ở chế độ không ghi đè; số file thay đổi trong `git status` trước và sau khi chạy giữ nguyên (538).

## 1. Bảng kiểm

| # | Khẳng định trong bàn giao | Kết quả | Bằng chứng |
|---|---|---|---|
| 1 | Nhánh v2 tách từ `648b2f68` trên `feature/english-learning-content-system` | Đúng | `git log`, `git merge-base`; hai nhánh cùng trỏ `648b2f68`, kể cả `origin/...-system` |
| 2 | Toàn bộ công việc v2 nằm trên nhánh v2 | **Thiếu sót lớn**: nhánh v2 chưa có commit nào, 480 file sửa + 58 file mới chưa commit | `git status --short` = 538 dòng; `git log main..HEAD` chỉ gồm commit cũ của nhánh system |
| 3 | 6 script build đã thành validator không ghi đè | Đúng | Không có `writeFile`/`rmSync`/`renameSync` trong 6 file; chạy cả 6, status `ok`, không đổi file |
| 4 | `validate-english-content-reviews`: 275.431/275.431, publish 268.121 | Đúng | Chạy lại, cùng số |
| 5 | Cloze 100 slice / 50.000; translation 40 slice / 20.000 / 6.821 đa đáp án | Đúng | Output hai validator |
| 6 | 15 Topic Packs / 343 mục; E14 750 lexeme, 163 đa nghĩa, 917 sense, 1.769 link | Đúng | `build-e15-topic-packs`, `build-e14-lexical-pilot` |
| 7 | Mục 3/4: 1.200 + 800 + 2.500 + 1.000 bài; E13 3.547 link (177→1.102, 372→2.445) | Đúng | Đếm trực tiếp 4 file `v2-*-exercises.json`; `build-e13-enrichment-links` |
| 8 | Các file/script/code nêu tên đều tồn tại (indexes, runtime-loader, grading, evidence-v2, portal, nginx route) | Đúng | Kiểm 42 đường dẫn; `shared/indexes/` có manifest, availability, 17 activity, 256 by-id, 256 evidence, 15 packs, lexical; route `/english-content/indexes/` có trong 2 conf nginx |
| 9 | `hasVerifiedTargetAttribution()`, 3 trạng thái chấm, `LEARNING_PROFILE_VERSION = 1`, bỏ `monkeytype` khỏi `RichPracticeGameId` | Đúng | grep trong `game-adapters.mjs`, `grading.mjs`, `core.mjs`, `activity-session.ts` |
| 10 | Benchmark Phase 1 (`2026-11-10T16:57:13Z`) và các con số speedup | Đúng số trong file | `v2-phase1-runtime-benchmark.json`, mục `comparison`; chưa đo lại (xem mục 3) |
| 11 | Hygiene audit: 315 topic mismatch, 99 proper-noun suspect, 66,88 % translation 1 đáp án, 2 loại bài trống | Đúng | `v2-phase0-v1-hygiene-audit.json` (sinh 2026-11-11T07:43Z) |
| 12 | E13 `withoutExamples`: collocation 4.794/5.000, chunk 1.867/2.000, idiom 1.103/1.185, phrasal-verb 737/1.000, verb-pattern 254/510 | Đúng | Đếm `exampleIds` rỗng trong `shared/phrases/*` |
| 13 | `english-content:validate` PASS (39 batch / 288 topic) | Đúng | exit 0 |
| 14 | `english-content:test` 120/120; `learning:test` 59/59; `learning:check` PASS | Đúng | exit 0, đúng số (test mất ~6 phút) |
| 15 | e10, e11, e11:runtime, e11:records (11/11, missing 0, extra 0), runtime:smoke, e11:games (35 flow / 5 game / 202 item), licenses, e12:audit, dedupe, coverage, pilot PASS | Đúng | Tất cả exit 0 |
| 16 | `build:portal` PASS | Đúng | `tsc --noEmit && vite build` exit 0 |
| 17 | Submodule: monkeytype `eee4a246`, recall `3ace1f48`, shooter `01ddaafd`, space `14dccb2b`, karaoke `-3402d0e0` chưa checkout; 0 thay đổi | Đúng | `git submodule status`; `git -C games/* status` đều 0 |
| 18 | Monkeytype: `loadByPrefix` quét tuần tự, `shardCache` không giới hạn, chưa nghe `activity-dataset` | Đúng | `rich-content.ts:367,419`; `review-dataset.ts` 0 lần khớp |
| 19 | Recall/Shooter cắt 200 ký tự, Space 240 | Đúng | `src/learning/shared.ts` từng game |
| 20 | Monkeytype quét "463 shard = 203 exercises + 260 examples" | Lệch nhẹ | Hiện có 214 shard exercises (203 cũ + 11 mới chưa commit) + 260 examples = 474 |
| 21 | Tiêu chí GO/ITERATE/STOP ở mục `P1-06` và `P2-01` trong `ENGLISH_LEARNING_CONTENT_V2_PLAN.md` | **Sai** | File plan chỉ có nhãn `P1-01`, `P1-02`; không có `P1-06`, `P2-01` |
| 22 | `scratch/`, `pnpm-lock.yaml`, `portal/pnpm-lock.yaml` đã dọn | Đúng | Không tồn tại trên đĩa, chưa từng được track |
| 23 | Giữ `content/english/review-queues/*.json` ngoài commit | Hợp lý | 5 file queue chưa track, chỉ `README.md` được track; 4 queue khác đã trong `.gitignore` |
| 24 | PR #48 là draft, không được đụng | Không kiểm được | `gh` chưa đăng nhập; chỉ xác nhận nhánh `origin/feature/english-learning-content-system` tồn tại và không bị đụng |
| 25 | `e11:games` và `e12:audit` là lệnh "kiểm tra" thuần | Lưu ý | `e11:games` ghi lại `reports/step11-game-integration-verification.json` (đổi timestamp); file này vốn đã nằm trong diff chưa commit |

Tổng: 25 khẳng định kiểm, 21 đúng, 1 sai (#21), 1 lệch nhẹ (#20), 1 không kiểm được (#24), 1 thiếu sót lớn về trạng thái git (#2).

## 2. Quyết định

**Đúng và an toàn, làm ngay trong checkout này**
- Chạy lại toàn bộ validator, test, smoke, audit, build portal: đã làm, tất cả qua (bảng trên).
- Viết file review này và commit riêng.

**Sai hoặc mâu thuẫn với repo**
- Tham chiếu `P1-06`/`P2-01` trong plan không tồn tại; tiêu chí GO/ITERATE/STOP cho E2E chưa được viết ở đâu.
- Bàn giao mô tả nhánh v2 như đã có công việc, nhưng thực tế mọi thứ còn là working tree chưa commit. Nếu checkout này bị reset hay đổi nhánh thì mất toàn bộ 4 ngày việc của Gemini.

**Cần anh quyết (không làm)**
- Commit 538 file việc của Gemini lên nhánh v2 (trừ 5 file `review-queues/*.json`). Tôi không tự commit vì luật phiên là chỉ commit file tôi đổi. Đề xuất chia 4 commit: (a) script + shared code + portal + nginx + package.json, (b) nội dung nguồn `content/english/**` + decisions, (c) sản phẩm publish `shared/**` + `shared/indexes/`, (d) docs + reports.
- Nhóm A (sửa 4 submodule `games/*`): cần mở nhánh trên từng repo con; chỉ làm khi anh đồng ý và sau khi root đã commit.
- Chạy lại `benchmark-english-content-v1.mjs`: script ghi đè 2 file report chưa commit của Gemini, nên chỉ nên chạy sau khi đã commit (a)–(d).
- `bash scripts/setup-nginx.sh dev` cần `sudo`: anh tự chạy.
- Test E2E trên trình duyệt: cần nginx và tiêu chí GO/ITERATE/STOP chưa có; anh quyết tiêu chí trước.
- Nhóm C (E13 frame matcher, E11 cleanup, E14 mở rộng, E16 variants, E17): việc dài hạn, chưa làm.

## 3. Việc đã làm

- Chạy 7 validator, `english-content:validate/test`, `learning:check/test`, e10, e11 (3 lệnh), runtime:smoke, e11:games, licenses, e12:audit, dedupe, coverage, pilot, build:portal: tất cả exit 0, số liệu khớp bàn giao.
- Không đụng submodule, không push, không chạy publish/generate/indexes/benchmark/setup-nginx.
- Commit file này: xem mã commit trong báo cáo phiên (chỉ `docs/HANDOFF_REVIEW_2026-11-11.md`).

## 4. Việc chờ anh

1. Có commit 538 file việc của Gemini lên `feature/english-learning-content-v2` không, và chia commit thế nào.
2. Có cho mở nhánh và sửa `games/monkeytype` (ưu tiên 1) rồi recall/shooter/space (ưu tiên 2) không.
3. Tự chạy `setup-nginx.sh` (sudo) và quyết tiêu chí GO/ITERATE/STOP cho E2E.

## 5. Điểm Gemini viết sai hoặc gây hiểu nhầm

- Không nói rõ rằng toàn bộ công việc v2 chưa commit (#2).
- Dẫn mục `P1-06`, `P2-01` không có trong plan (#21).
- "463 shard" là số cũ; nay 474 vì có 11 shard exercises mới (#20).
- Liệt kê `e11:games` trong "lệnh verify" nhưng lệnh này ghi lại report (#25).
- "PR #48 draft" không kiểm được từ máy này (#24).

## 6. Phân loại file chưa commit (bổ sung 12/11 00:30)

Trạng thái mới: lúc 00:20 ngày 12/11 (sau commit `80c7e565` của tôi) commit `b7c6d681` (tác giả toandx, 1.094 file: 614 thêm, 480 sửa, ~529 MB JSON) và `867cb168` (sửa 2 file bàn giao theo bảng kiểm) đã đưa toàn bộ việc v2 vào nhánh. Con số 538 trong `git status` trước đó gộp thư mục `shared/indexes/` (547 file) và các thư mục mới khác thành một dòng. Bảng dưới phân loại nội dung `b7c6d681` để anh quyết giữ nguyên hay tách lại; working tree hiện chỉ còn 5 file `review-queues` chưa track.

### Nhóm 1 — File v2 mới do Gemini tạo (614 file, ~34 MB): nên commit, đã nằm trong `b7c6d681`
- Nội dung nguồn: 15 packs, `e14-sense-pilot.json`, 4 bộ `v2-*-exercises.json` + 4 ledger `decisions.d/v2-*`, `e13-morphological-links.json`, schema `topic-pack`.
- Mã: 10 script mới, `grading.*`, `index-bucket.*`, 5 file `shared/learning/evidence-v2*` và `browser-evidence-store*`, 3 test mới.
- Sản phẩm publish: `shared/indexes/**` (547 file, ~24 MB), 11 shard `shared/sentences/exercises/203..213`.
- Báo cáo: 6 report mới (`e13-*`, `e14-*`, `v2-phase0/1-*`), 3 file docs.

### Nhóm 2 — File có sẵn Gemini sửa (480 file, ~495 MB): đề xuất giữ toàn bộ
| File | Diff một dòng | Ý kiến |
|---|---|---|
| `package.json` | thêm `english-content:indexes`, mở rộng `learning:check` | Giữ |
| `infra/nginx/*.conf` (2) | thêm route `/english-content/indexes/` + CORS | Giữ |
| `scripts/publish-english-content.mjs` | thêm `bytes`/`sha256` cho shard, gọi sinh indexes, gom `v2-*` | Giữ |
| `scripts/validate-english-content.mjs`, `smoke-published-english-content.mjs` | thêm schema topic-pack, validate và đếm bộ `v2-*` | Giữ |
| `scripts/build-e11-cloze-expansion.mjs` | viết lại thành validator không ghi đè (+136/−222) | Giữ |
| `scripts/build-e11-mistake-expansion.mjs` | loại homograph "read" khỏi cờ lỗi ngôi 3 | Giữ |
| `shared/english-content/*.mjs` + `.d.mts` + test (11) | runtime-loader LRU/pin version/by-id; activity-source đếm O(1), CEFR, `maxAnswerLength`; adapters thêm `acceptedAnswers`, `gradingMode`, `hasVerifiedTargetAttribution`; format lại code | Giữ (120 test qua) |
| `portal/src/**` (4) | Practice Runner, Topic Pack, Evidence v2, CSS | Giữ (build qua) |
| `shared/{dictionary,grammar,phrases,sentences}/manifest.json` | thêm `bytes`/`sha256`, count 251.726 → 257.226 | Giữ (sản phẩm publish) |
| `shared/sentences/exercises/*` (140), `mistakes/*` (7), `phrases/items/*` (7), `collocations/*` (2) | publish lại: 5.500 bài mới, 9 mistake "read", example links E13 | Giữ (sản phẩm publish) |
| `content/english/sentences/e11-cloze-slice-*` (98) + `decisions.d` (98) | rà tay chỗ trống danh từ riêng, cập nhật `sourceDigest` | Giữ (dữ liệu rà tay) |
| `content/english/sentences/e11-translation-slice-*` (40) + `decisions.d` (40) | dịch 1.002 placeholder, thêm biến thể, sửa 8 ID trùng | Giữ |
| `content/english/sentences/e11-mistake-slice-*` (6) + `decisions.d` (6) | thay 9 bản ghi "read" | Giữ |
| `content/english/batches/manifest.json`, `releases/2026.10.0.json` | thêm 4 batch v2, count mới | Giữ |
| `content/english/reports/*` (7 sửa) | số liệu publish mới; `e11-readiness.json` vẫn nhúng nguyên văn file (kiểu cũ) | Giữ |

### Nhóm 3 — Không nên vào Git
- Trong `b7c6d681` không có media, cache hay file tạm (chỉ json/mjs/mts/ts/css/md/conf).
- 5 file `content/english/review-queues/{grammar-e06-common-mistakes,grammar-e06-corrections,grammar-e06-transformations,tatoeba-e11-translation-next-review,typing-text-e06-exercises}.json` (1,1 MB) chưa track, đúng ý bàn giao; 4 queue tương tự đã có trong `.gitignore` nhưng 5 file này **chưa**: đề xuất thêm 5 dòng vào `.gitignore` (chờ anh).
- `scratch/`, lockfile: không tồn tại trên đĩa.

### Nhóm 4 — Không chắc
- `shared/indexes/**` (547 file, 24 MB): sinh ra từ publish, nhưng repo vốn track mọi sản phẩm publish trong `shared/*`; nếu anh muốn giảm dung lượng thì ignore và sinh lúc deploy.
- `content/english/reports/v2-phase0-runtime-baseline.json`, `v2-phase1-runtime-benchmark.json`: số đo phụ thuộc máy, sẽ bị ghi đè khi chạy lại benchmark.
- `content/english/reports/step11-game-integration-verification.json`: mỗi lần `e11:games` lại đổi timestamp, gây diff nhiễu.
- `docs/HANDOFF_*.md` (2 file): tài liệu bàn giao tạm, có thể xoá sau khi xong Nhóm A.

Việc chờ anh: giữ `b7c6d681` nguyên khối, hay tách thành 4 commit (mã / nội dung nguồn / sản phẩm publish / docs+reports) bằng `git reset --soft` rồi commit lại (không mất file); và có thêm 5 queue vào `.gitignore` không.
