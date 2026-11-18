# Phiếu 234 · Vá nốt 227-F2: mẫu học trả ra iframe phải đúng kiểu

Ngày 30/10/2026 · Repo cha · Node v24.22.0 · Claude làm thay Codex (owner dừng Codex 15:25).

**F2 đã đóng trong phạm vi mã và test.** 43 test mới viết trước mã, cả 43 đỏ; sau sửa 43/43 xanh.
Tắt riêng từng bước sửa đều làm 21 test đỏ. Probe của 233: **43/53 → 53/53**. Chưa chạy trình duyệt.

## 1. Điều kiện

- Có `233-report.md`, `228-report.md`. Nhánh `feat/space-typing-admin-uiux`, HEAD `5742e1a8` đầu và cuối.
- `git status --short -uall -- shared/learning portal`: **17 đường, 0 đường lạ**. Cả 17 nằm trong `files.txt` của 214/215 và `knownDirty` của 228. Xem [preflight.txt](234/preflight.txt), [status-before.txt](234/status-before.txt).
- Phiếu không có ghi chú chạy lại.

## 2. Ca đỏ (trước sửa)

| Bộ | Trước | Có test mới, chưa sửa mã | Log |
|---|---:|---:|---|
| Shared learning | 89/89 | **89 xanh / 23 đỏ** (112) | [learning-red.txt](234/learning-red.txt) |
| Portal | 109/109 | **109 xanh / 20 đỏ** (129) | [portal-red.txt](234/portal-red.txt) |
| Probe `233/parent-probe.mjs` | **43 xanh / 10 đỏ** | — | [probe233-before.txt](234/probe233-before.txt) |

Test mới:

- `shared/learning/lookup.test.mjs:146`–`:265` (23 test):
  - 10 test hồ sơ đã lưu: 5 trường × {object, array}. Mỗi test chạy 3 loại thực thể × lookup và query.
  - 10 test nhập sao lưu, cùng ma trận. Nhập cả chuỗi JSON lẫn object; hồ sơ nguồn không đổi.
  - 2 test kiểu nguyên thủy sai hoặc thiếu trường (10 giá trị sai + 5 trường thiếu), một cho hồ sơ lưu, một cho sao lưu.
  - 1 test hồ sơ lưu có mẫu không phải object (4 ca) và `recentSamples` không phải mảng (3 ca).
- `portal/tests/learning-bridge.test.mjs:197`–`:261` (20 test): {lưu, sao lưu} × 5 trường × {lookup, query}, mỗi test cả object lẫn array. Đi qua `ParentLearningBridge.handleMessage` từ đúng iframe/origin; kiểm `query-result`, đúng requestId/origin, 1 lần đọc kho, mẫu trả ra đúng năm khóa, không có `PRIVATE_NESTED_`, hồ sơ không đổi.

Lỗi đỏ đúng ca của 233, ví dụ lookup hồ sơ lưu: `gameId: { expectedAnswer: 'PRIVATE_NESTED_EXPECTED_ANSWER', userAnswer: 'PRIVATE_NESTED_USER_ANSWER' }` đi ra khung game.

Sửa một test cũ: `lookup.test.mjs:116` "backup accepts eight samples" dùng 8 mẫu chỉ có `occurredAt`. Theo luật mới các mẫu đó sai kiểu. Đổi fixture thành 8 mẫu đủ năm trường; ý test (nhận đúng 8 mẫu) giữ nguyên. Test này xanh cả trước và sau sửa.

## 3. Bản sửa

| Bước | Tệp:dòng | Nội dung |
|---|---|---|
| Luật kiểu | `shared/learning/query.mjs:38`–`:49` | `isLearningSample`: `occurredAt`, `gameId`, `activityType` là chuỗi; `result` là `"correct"`/`"wrong"`; `hintUsed` là boolean. Khai báo ở `query.d.mts:4`–`:5`. |
| 2 · Đường trả dữ liệu | `query.mjs:52`–`:70`, dùng ở `:311` | `contractSamples` dựng mỗi mẫu từ năm trường, đọc mỗi trường một lần, rồi kiểm kiểu. Sai kiểu thì bỏ cả mẫu (`:66`), không ép kiểu, không cắt chuỗi. Không phải mảng thì trả `[]`. Bảo vệ cả hồ sơ đã lưu. |
| 3 · Nhập sao lưu | `shared/learning/profile-backup.mjs:6`, `:132`–`:135` | Sau kiểm cấu trúc cũ, lọc `recentSamples` bằng cùng `isLearningSample` trên bản clone. `parseLearningProfileBackup` trả `LearningProfile`, không có chỗ báo cáo, nên chỉ bỏ, không đếm. |

Không đổi `bridge.ts`, `core.mjs`, `core.d.mts` (kiểu `LearningSample` đã đủ), `recentMistakes`, `recentAnswers`. Diff riêng của 234: [task.diff](234/task.diff).

Các lựa chọn cần Claude/owner biết:

- **Thiếu trường cũng là sai kiểu.** `core.d.mts` khai báo cả năm trường bắt buộc; mọi mẫu do `core.mjs` tạo đều đủ năm trường.
- **`recentSamples` không phải mảng** trong hồ sơ lưu: trước sửa ném lỗi → `query-failed` cho cả yêu cầu; nay trả `[]`, các trường khác của bản ghi vẫn trả.
- **Nhập sao lưu chỉ bỏ mẫu sai kiểu, không cắt trường dư** của mẫu đúng kiểu. Trường dư vẫn bị đường trả dữ liệu bỏ như 228. Mẫu không phải object và danh sách quá 8 mẫu vẫn bị từ chối như cũ.
- `validateLearningProfile` dùng chung cho xuất sao lưu, reset và đếm. Nên `createLearningProfileBackup` và `resetLearningProfileSelection` cũng trả bản đã bỏ mẫu sai kiểu. Đầu vào không bị sửa.
- Chuỗi đúng kiểu vẫn đi qua nguyên vẹn (theo phiếu: không cắt chuỗi). Phiếu này không kiểm nội dung chuỗi.

## 4. Ca xanh và đột biến

| Bộ | Trước | Sau | Log |
|---|---:|---:|---|
| Shared learning, 13 file | 89/89 | **112/112**, mã 0 | [learning-green.txt](234/learning-green.txt) |
| Portal, 3 file | 109/109 | **129/129**, mã 0 | [portal-green.txt](234/portal-green.txt) |
| Probe 233, chạy tại chỗ, không sửa | 43/53 | **53/53**, mã 0 | [probe233-after.txt](234/probe233-after.txt) |
| `pnpm learning:check` | — | mã 0 | [learning-check.txt](234/learning-check.txt) |
| `tsc --noEmit` portal | — | mã 0 | [portal-tsc.txt](234/portal-tsc.txt) |

Đột biến bằng [mutate.mjs](234/mutate.mjs): sửa đúng một dòng, chạy 4 file test shared liên quan (84 test) và 2 file test portal về học (70 test), trả nguyên byte trong `finally`, kiểm SHA-256. [mutation.json](234/mutation.json).

| Đột biến | Đỏ khi tắt | Sau khôi phục |
|---|---|---|
| **M2** tắt bước 2: `query.mjs:66` luôn giữ mẫu | **21**: 11 shared (10 hồ sơ lưu + 1 nguyên thủy) + 10 portal (hồ sơ lưu) | 84/84, 70/70, hash khớp |
| **M3** tắt bước 3: bỏ dòng lọc `profile-backup.mjs:134` | **21**: 11 shared (10 sao lưu + 1 nguyên thủy) + 10 portal (sao lưu) | 84/84, 70/70, hash khớp |

Hai tập đỏ không trùng nhau: mỗi bước được test riêng bắt.

## 5. Phạm vi

- Sửa đúng 5 file: `shared/learning/query.mjs`, `profile-backup.mjs`, `query.d.mts`, `lookup.test.mjs`, `portal/tests/learning-bridge.test.mjs`. 4 file khác trong vùng giữ nguyên hash: [hashes-before.txt](234/hashes-before.txt), [hashes-after.txt](234/hashes-after.txt).
- Tạo mới: `docs/changelog/2026-10-30-learning-sample-types.md`, báo cáo này, `234/`.
- `git diff --check` 4 file đã theo dõi: mã 0. File chưa theo dõi kiểm bằng `--no-index --check`: 0 thông báo. [diff-check.txt](234/diff-check.txt).
- [status-after.txt](234/status-after.txt): so với trước, đường mới của 234 chỉ trong vùng cho phép. Lúc chụp có thêm **9 đường của làn khác** (`230/art-head-copy.json`, `230/logs/*`, `230/tools/run-balance.sh`, `232/golden.txt`, `232/prepare-ui.txt`), không phải của 234, không đụng tới.
- Không build portal (Vite ghi `dist`), không dev server, trình duyệt, mạng. Git chỉ đọc; không commit, push, stash, reset.

## 6. Kết luận

**F2 (P1-233-01) đã đóng:** cả 10 ca của 233 và 43 test mới xanh; cả hai đường (hồ sơ lưu, nhập sao lưu) đều có test riêng bắt khi tắt. Claude cần duyệt `task.diff` và ba lựa chọn ở §3 trước khi nhận 228 + 234 cùng commit. F7 (khoảng trắng log 216) vẫn ngoài phạm vi phiếu này.
