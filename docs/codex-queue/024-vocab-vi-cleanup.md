# Phiếu 024 · Từ vựng chung · Sửa nghĩa tiếng Việt sai và lặp (chỉ dữ liệu, không trình duyệt)

**Bối cảnh:** người chơi thấy nghĩa tiếng Việt trên thẻ chữ của cả bốn game, nên một nghĩa sai là một lỗi dạy sai. Hai đợt test 27/10 đã tìm thấy:
- "buồn bả" (đúng: "buồn bã") ở `shared/vocabulary/levels/001.json`, mục `L001-009` "sad" (Tuyến Cuối n19);
- nghĩa lặp lại chính nó: Rồng Giữ Ải phát hiện 43, chuyển người điều phối.

Claude đã quét sơ bộ 18.000 mục và thấy 14 mục có một nghĩa ghép lặp đúng các nghĩa đơn đứng cạnh, ví dụ:
- "cow": `bò cái; bò; cái`. "cái" đứng một mình không có nghĩa là bò.
- "beer": `bia; rượu; rượu bia`.

Mười bốn mục đó:

| Cấp | Từ |
|---|---|
| 005 | usually |
| 008 | cow |
| 013 | beer |
| 019 | stove |
| 024 | asthma |
| 025 | beat, bet |
| 026 | reduce, shift |
| 027 | blind |
| 049 | torso |
| 056 | await |

Phần đuôi của danh sách (khoảng 2 mục sau "await") chưa xem hết. Hãy tự quét lại cho đủ.

**Thư mục làm việc:** repo cha (`.`). Chỉ được sửa:
- trường `vi` trong `shared/vocabulary/levels/*.json`;
- `index.json`, `lookup.json`, nếu lệnh tạo lại ghi chúng;
- báo cáo.

**Cấm:**
- đổi `en`, `id`, `ipa`, thứ tự mục, số mục;
- đổi định dạng JSON (giữ nguyên `stableJson` của `scripts/vocabulary-core.mjs`);
- lệnh git có ghi;
- đụng game nào, Tu Tiên, media;
- mở dev server.

Làn của Claude đang chạy bot trong các game; bot dựng bộ bài từ `en`, nên chỉ sửa `vi` không đổi mã băm. Không chạy test hay build của game.

## Việc

1. **Lỗi đã biết:** "buồn bả" → "buồn bã".
2. **Nghĩa lặp**, gồm 14 mục trên và các mục khác tự tìm được, dùng `;` để tách nghĩa:
   - bỏ nghĩa nào trùng hệt một nghĩa khác trong cùng mục;
   - bỏ một nghĩa đơn **chỉ khi** đứng một mình nó không mang nghĩa của từ tiếng Anh. Ví dụ "cái" của "cow" thì bỏ; "bò" giữ.
   - giữ nghĩa ghép khi nó đúng.

   Mỗi mục ghi quyết định và lý do một dòng.
3. **Rà chính tả nghĩa tiếng Việt** trên cả 100 cấp, bằng máy trước:
   - tách âm tiết, kiểm cấu trúc âm tiết tiếng Việt (phụ âm đầu, vần, dấu thanh hợp lệ, vị trí dấu);
   - liệt kê âm tiết hiếm (xuất hiện ≤ 2 lần trong cả kho);
   - tìm các cặp hay nhầm hỏi/ngã ("bả/bã", "nghỉ/nghĩ", "sửa/sữa", "dỗ/dổ"…) đặt sai theo từ ghép quen ("buồn bã", "nghỉ ngơi", "suy nghĩ", "sửa chữa", "sữa bò"…).

   Chỉ sửa khi chắc chắn. Mọi ca còn ngờ đưa vào bảng "Cần Claude xem", không sửa.
4. **Tạo lại và kiểm:** `node scripts/generate-vocabulary.mjs`. Lệnh này đọc các cấp, kiểm (`validateLevels`) rồi ghi `index.json` và `lookup.json`. Phải chạy qua; `git diff --stat` chỉ được có các file cấp, cùng `index.json` và `lookup.json` nếu chúng đổi (chúng không chứa `vi` nên nên giữ nguyên).

## Kiểm (bắt buộc)

1. `node scripts/generate-vocabulary.mjs` thoát mã 0.
2. Một lệnh `node` nhỏ đọc lại 100 file. Mọi mục còn đủ `id`, `en`, `ipa`, đúng như trước; chỉ `vi` đổi. In số mục đổi.
3. `git diff --stat` và toàn bộ `git diff -U0 -- shared/vocabulary`, dán vào báo cáo.

## Báo cáo `docs/codex-queue/024-report.md`

- Bảng `| Cấp | id | en | vi cũ | vi mới | Lý do |` cho mọi mục đã sửa.
- Bảng "Cần Claude xem" cho các ca còn ngờ.
- Số âm tiết đã quét, số ca máy bắt, số ca đã sửa.
- Kết quả 3 lệnh kiểm.

**Xong khi:** việc 1–4 xong, ba lệnh kiểm đạt.
