# Phiếu 187 · Dragonhold · Bản build không còn trỏ về cổng game ở nhà

**Vì sao:** phiếu 169 chạy `pnpm deploy:pack` và bộ kiểm gói báo **1 lỗi production**: bản build chứa hai tham chiếu nguồn tới cổng game ở nhà (`typing-game.local`). Bản demo nhà được phép (cờ `--allow-local-host`), nhưng bản phát hành phải tự đủ (`docs/games/DEPLOY_INDEPENDENCE.md`). Chủ dự án 29/10: giao thêm việc cho Codex.

**Báo cáo:** `docs/codex-queue/187-report.md`, thư mục `docs/codex-queue/187/`.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-dh-codex` (nhánh `dh-codex`, đã gộp vào `main` Dragonhold tới phiếu 169). Kiểm `git status` trước khi làm: phải sạch.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi; sửa `src/kit/**`; chạy `kit:sync`; dev server, trình duyệt, mạng; đụng game khác, worktree khác, Tu Tiên.
- Test trước, mã sau. Chú thích tiếng Anh. Luật chơi và ván vàng không đổi. Chữ người chơi thấy là tiếng Anh.

## Việc

1. Đọc `docs/codex-queue/169-report.md` và thư mục `169/` để thấy đúng hai tham chiếu (file, dòng, chuỗi).
2. Làm đường về cổng game cấu hình được lúc build: biến môi trường Vite (ví dụ `VITE_PORTAL_URL`), mặc định **trống** ở bản phát hành; khi trống thì nút "Back to portal" ở màn kết quả (phiếu 105, 105b) ẩn đi hoặc dẫn về trang đầu của chính game, không trỏ ra ngoài. Bản demo nhà đặt biến này khi build (`pnpm build:local` hay script tương ứng; ghi cách dùng vào README của game).
3. `pnpm deploy:pack` (không cờ) phải đạt **0 lỗi**; `pnpm deploy:pack:local` với biến cổng đặt vẫn đạt.
4. Test: nút cổng ẩn khi biến trống, hiện và trỏ đúng khi có biến; bộ kiểm gói không còn thấy `typing-game.local` trong bản phát hành.

## Kiểm (ghi số)

1. `pnpm check` xanh (ghi số test), ván vàng giữ nguyên; test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Đầu ra JSON của `deploy:pack` trước và sau, lưu vào `187/`.
3. `git status --short -uall`: chỉ các file của việc này, test, README, `docs/changelog/<ngày>-portal-link.md`.

**Xong khi:** bốn mục việc và ba mục kiểm đạt. Claude duyệt rồi commit.
