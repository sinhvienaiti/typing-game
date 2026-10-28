# Báo cáo 105 · Rồng Giữ Ải · Cổng game và trang thử HUD

Ngày thực hiện: 28/10/2026, Mac mini M4, macOS. **Chưa hoàn thành phiếu**:
đã làm helper địa chỉ cổng và điều kiện nạp preview; dừng phần màn kết quả
theo điều kiện Esc của phiếu. Chưa chạy build hoặc bộ test vì chỉ dẫn phiên
cấm hai việc này; đã hỏi chủ về ngoại lệ cho các mục kiểm bắt buộc.

## File đã đổi

Đường dẫn mã dưới đây tính từ `games/.wt-dh-codex`:

| File | Nội dung |
| --- | --- |
| `src/app/portal.ts` | Mới; xuất `portalHome`, lấy nguồn đầu tiên khác rỗng đã trim, mặc định `https://typing-game.local`, nối `/`. |
| `tests/app/portal.test.ts` | Mới; năm ca được viết trước mã helper, chưa thực chạy. |
| `src/main.ts` | Chỉ sửa chú thích dòng 3 và điều kiện dòng nạp `ui-preview`, thêm `import.meta.env.DEV`. |
| `docs/changelog/2026-10-29-portal-button.md` | Mới; ghi rõ phần làm được, phần dừng và số đo. |

Repo cha chỉ ghi báo cáo này và thư mục bằng chứng
[`105/`](105/). Không đổi `src/ui/results.ts`, `tests/ui/results.test.ts`
hoặc CSS; file CSS màn kết quả được xác định là `src/ui/styles/dh.css`.

## Điều kiện dừng Esc

`createResults().handleAction` trong `src/ui/results.ts` đang nhận Esc khi
`pending` khác null để gọi `showPending()`: bỏ qua đoạn chờ thắng 2.600 ms,
mở bảng kết quả ngay. Khi `summary` đã có, Esc chỉ bị giữ lại và chưa thực
hiện hành động nào. Không thay đổi cả hai nhánh trong phiên này.

Theo câu “nếu Esc ở màn kết quả đang có việc khác thì dừng và báo, không
đổi”, đã gửi câu hỏi làm rõ: giữ Esc trong đoạn chờ và chỉ cho về cổng khi
bảng đã mở, hay dừng phần màn kết quả. Cần câu trả lời trước khi triển khai
nút, focus, Enter, Esc và test tương ứng. Hiện các phím lên/xuống còn chọn
từ trong Sổ Từ Ải; phần chuyển chúng sang hai nút cũng chưa thực hiện.

## Kết quả từng mục kiểm

1. **`pnpm check`: chưa chạy.** Script gồm kiểm SHA kit, toàn bộ Vitest và
   build; xung đột với luật đầu phiên “do not run the games' builds or test
   suites”. Số test trước/sau của phiên: **chưa đo / chưa đo**. File test
   helper mới có **5 ca**; không coi số ca viết ra là kết quả test xanh.
   Báo cáo 094 từng ghi 460 test đạt, nhưng đó là phép đo của phiên trước.
2. **Golden: đạt ở kiểm diff.**
   `git -C games/.wt-dh-codex diff --stat -- tests/golden`: mã thoát **0**,
   đầu ra **0 byte**, lưu trong [golden.txt](105/golden.txt).
   `git diff --check`: mã thoát **0**, đầu ra **0 byte**, lưu trong
   [whitespace.txt](105/whitespace.txt).
3. **Loại chunk production: chưa xác minh.** Không chạy `pnpm build` hoặc
   xem bản `dist` có sẵn như sản phẩm của mã mới. Bản cũ có **5 chunk JS**,
   **1.241.854 byte**, gồm `ui-preview-jAwQWz9e.js`; xem
   [assets-existing.json](105/assets-existing.json). Tổng JS trước/sau build
   của phiên: **chưa đo / chưa đo**. Còn phải build rồi kiểm cả tên preview
   và chuỗi `startUiPreview` trong `dist/assets/*.js`.
4. **Đột biến: chưa chạy**, vì cần build/test. Còn phải bỏ cờ `DEV` để kiểm
   chunk xuất hiện lại, và đổi mặc định helper để xác nhận test đỏ; sau mỗi
   lần trả mã về nguyên byte. Không sửa đột biến rồi suy đoán kết quả.
5. **Phạm vi Git: giữ nguyên phần có sẵn, chưa thỏa câu chữ tuyệt đối của
   phiếu.** Trước phiên có **118 dòng status**, gồm phiếu 094, 101 và **5 file
   080** đã được báo cáo 094 ghi nhận. Không xóa hoặc sửa các file này để ép
   status về phạm vi 094/101. Đối chiếu SHA-256: **118/118 file giữ nguyên**.
   Phiên 105 chỉ thêm **4 đường dẫn** trong worktree: helper, test helper,
   `src/main.ts` và changelog. Xem [trạng thái đầu](105/status-before.txt),
   [trạng thái cuối](105/status-after.txt), [SHA ban đầu](105/hashes-before.json)
   và [tổng hợp kiểm](105/audit.json).

Không chạy Git có ghi, dev server, trình duyệt, media, cập nhật golden hoặc
đổi kit; không ghi cây chính của game, worktree khác hay Tu Tiên.

## Việc chủ và Claude cần xem

Làm rõ phạm vi Esc và quyền chạy riêng các mục kiểm của phiếu 105. Sau khi
triển khai nốt, Claude cần chạy lại năm mục kiểm, duyệt diff và kiểm thắng /
thua bằng phím ở 1280 và 1920, cả khi nhúng qua `https://typing-game.local`.
Chưa có bằng chứng giao diện hoặc điều hướng `_top` trong phiên này.
