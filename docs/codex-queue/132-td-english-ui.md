# Phiếu 132 · Wordwoven · Đổi toàn bộ chữ người chơi thấy sang tiếng Anh

**Vì sao:** chủ dự án quyết định ngày 28/10/2026 tối (`AGENTS.md`, mục "Language, names and art level"): đây là game tiếng Anh.
- Mọi chữ người chơi đọc đều bằng tiếng Anh: tên game, menu, nút, gợi ý phím, bảng tin, kết quả, tooltip, thẻ, banner, toast, câu truyện.
- Tiếng Việt chỉ còn ở **nghĩa của từ đang học**: trường `vi` của mục từ vựng, và chỗ hiện nghĩa đó (ví dụ "thank · cảm ơn").
- Tên game là **Wordwoven** (trước là "Lời Gọi").
- Luật 27/10 (danh từ tiếng Anh trong câu tiếng Việt) bị thay.

**Báo cáo:** `docs/codex-queue/132-report.md` và thư mục `docs/codex-queue/132/`. Ghi ở **repo cha**, không ghi trong worktree.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Mã:** worktree `games/.wt-td-codex` (nhánh `td-codex`, vừa gộp nhánh chính mới nhất). Mọi đường dẫn mã tính từ worktree.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:**
  - sửa `src/kit/**` (bản chép kit). Chuỗi tiếng Việt trong kit thì liệt kê vào báo cáo; Claude sửa kit sau;
  - đổi id, khóa lưu trữ, tên event, tên file, luật, số, sim;
  - đổi golden hay chạy lệnh cập nhật golden;
  - ghi vào cây chính của game hay worktree khác; đụng game khác, Tu Tiên;
  - dev server, trình duyệt; media.
- Chú thích trong mã vẫn bằng tiếng Anh, ngắn.

**Chỉ được ghi:** `src/ui/**` (màn tựa, cài đặt, hồ sơ, tạm dừng, kết quả, bảng dạy `tips.ts`), `src/app/**`, `src/view/**` (thẻ gọi, nhãn), `src/content/**` (chỉ chuỗi người chơi thấy: tên nhà, quái, câu truyện, câu của Bà Cú Mực), `index.html`, các test trong `tests/` có so khớp chuỗi cũ, `docs/changelog/2026-10-29-english-ui.md` (mới, tiếng Việt), báo cáo và `docs/codex-queue/132/`.

## Việc

1. **Liệt kê** mọi chuỗi người chơi thấy có chữ tiếng Việt trong các thư mục được ghi. Cách làm: tìm ký tự có dấu tiếng Việt (`[À-ỹ]` cộng `đĐ`) trong chuỗi literal và template. Bỏ qua chú thích. Bỏ qua chỗ đọc hay hiện trường `vi` của từ vựng (nghĩa của từ). Ghi thành bảng `docs/codex-queue/132/strings-before.md`: `| file:dòng | chuỗi cũ |`.
2. **Dịch** từng chuỗi sang tiếng Anh: ngắn, rõ, giọng game, kiểu Mỹ, viết hoa giống chuỗi cũ (chuỗi cũ hoa hết thì bản dịch hoa hết).
   - Danh từ game giữ đúng tên tiếng Anh đang dùng (`docs/games/NAMES_EN.md`).
   - Gợi ý phím gọn, ví dụ `↑ ↓ select · Enter play · Esc back`.
   - Tên game ở màn tựa, `<title>` và mọi chỗ hiện tên là **Wordwoven**.
   - Dòng phụ của tên game cũ (nếu có) đổi thành một câu ngắn tiếng Anh, hoặc bỏ.
3. **Giữ độ dài:** chuỗi mới không dài hơn chuỗi cũ quá 20 % ở nút, nhãn và ô nhỏ. Dài hơn thì rút gọn và đánh dấu vào bảng.
4. **Bảng duyệt** `docs/codex-queue/132/strings.md`: `| file:dòng | chuỗi cũ | chuỗi mới | ghi chú |`, đủ mọi chuỗi đã đổi. Claude duyệt từng dòng.
5. **Còn sót:** chạy lại bước 1 sau khi sửa. Danh sách còn lại chỉ được gồm nghĩa từ vựng, `src/kit/**` và chú thích. Ghi đầu ra vào `docs/codex-queue/132/remaining.md`.
6. **Test:** sửa các test đang so chuỗi cũ sang chuỗi mới. Thêm một test quét chuỗi literal trong `src/` (trừ `src/kit/**` và các file hiện nghĩa từ vựng, liệt kê rõ) và đỏ khi gặp chữ có dấu tiếng Việt.
7. **Changelog** `docs/changelog/2026-10-29-english-ui.md`.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `pnpm check` xanh; ghi số test trước và sau. Có test thời gian đỏ khi máy tải nặng thì chạy lại riêng nó 3 lần và ghi số.
2. Luật chơi không đổi: `pnpm td:golden:check` cả hai `same:true`; trần gói "/" 85 kB và trần dòng vẫn giữ.
3. **Đột biến:** thêm tạm một chuỗi `"Bắt đầu"` vào một file UI thì test quét phải đỏ; xóa đi thì xanh.
4. `git -C games/.wt-td-codex status --short -uall`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** bốn mục đạt và đủ ba bảng (`strings-before.md`, `strings.md`, `remaining.md`). Sau đó Claude duyệt chữ, kiểm từng màn ở 1280 và 1920 (chữ không tràn), rồi commit và gộp.
