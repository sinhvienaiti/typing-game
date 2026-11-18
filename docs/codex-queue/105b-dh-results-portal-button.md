# Phiếu 105b · Rồng Giữ Ải · Nút "Về cổng game" ở màn kết quả

**Vì sao:** phiếu 105 đã làm `portalHome()` và bỏ chunk `ui-preview` khỏi bản production (commit `50fbeab`). Phần nút ở màn kết quả dừng đúng luật, vì hai phím đã có việc:
- Esc đang bỏ qua đoạn chờ thắng 2,6 s và mở bảng kết quả ngay;
- lên và xuống đang chọn từ trong Sổ Từ Ải.

**Quyết định của điều phối viên (28/10):**
- Esc, lên, xuống **giữ nguyên** việc hôm nay.
- Trái và phải chuyển tiêu điểm giữa hai nút.
- Enter bấm nút đang có tiêu điểm.

Kiểm kê map 1: DH-24, cổng G5.

**Báo cáo:** `docs/codex-queue/105b-report.md`, và thư mục `docs/codex-queue/105b/`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Mã:** worktree `games/.wt-dh-codex` (nhánh `dh-codex`, head `50fbeab`; đã có 080, 094, 101, 105 phần 1). Mọi đường dẫn tính từ worktree.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:**
  - sửa `src/kit/**`, `src/sim/**`, `src/content/**`, `src/typing/**`;
  - sửa golden hay chạy `dh:golden:update`;
  - ghi vào cây chính hay worktree khác (`.wt-dh-mappilot`, `.wt-dh-vfx` là của các làn Claude);
  - dev server, trình duyệt; media;
  - đụng Tu Tiên.
- Test trước, mã sau. Chuỗi người chơi thấy là tiếng Việt; tên game và danh từ game theo `docs/games/NAMES_EN.md`.

**Chỉ được ghi:**
- `src/ui/results.ts` và file CSS của màn kết quả (ghi tên vào báo cáo);
- test của màn kết quả trong `tests/ui/`;
- `docs/changelog/2026-10-29-results-portal.md` (mới, tiếng Việt);
- báo cáo và `docs/codex-queue/105b/`.

## Việc

1. Thêm nút thứ hai **"Về cổng game"** cạnh nút "Chơi lại", cùng kiểu và cùng cỡ. Nhãn phím theo `keyLabel` như nút "Chơi lại".
2. Nút là thẻ `<a href="<portalHome(import.meta.env.VITE_PORTAL_ORIGINS)>" target="_top">`, để khi game nằm trong khung của portal thì cả trang về cổng. `portalHome` ở `src/app/portal.ts`.
3. **Phím, chỉ khi bảng kết quả đã mở:**
   - trái và phải chuyển tiêu điểm giữa "Chơi lại" và "Về cổng game";
   - Enter bấm nút đang có tiêu điểm;
   - mặc định tiêu điểm ở "Chơi lại", như hôm nay.
4. Esc, lên, xuống giữ nguyên hành vi hôm nay. Nếu trái và phải đã có việc khác ở màn này thì dừng và báo, không đổi.
5. Màn kết quả phải vừa khung 1280×720: không tràn, không đè Sổ Từ Ải. Nếu hai nút không vừa một hàng thì đặt hàng dưới, ghi rõ.
6. **Test:**
   - bảng có hai nút, nút thứ hai có `href` đúng của `portalHome` và `target="_top"`;
   - phải rồi Enter kích hoạt nút về cổng; trái đưa tiêu điểm về "Chơi lại";
   - lên và xuống vẫn chọn từ trong Sổ Từ Ải;
   - Esc vẫn bỏ qua đoạn chờ thắng.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `pnpm check` xanh; ghi số test trước và sau. Test `tests/ui/tags-bodies.test.ts` có ngân sách thời gian và hay trượt khi máy tải nặng: nếu riêng nó đỏ thì chạy lại riêng nó 3 lần và ghi số.
2. Golden giữ: `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng.
3. **Đột biến:** bỏ xử lý phím phải thì test phải đỏ; trả lại thì xanh.
4. `git -C games/.wt-dh-codex status --short -uall`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** bốn mục đạt. Sau đó Claude kiểm màn thắng và màn thua ở 1280 và 1920 bằng phím, cả khi mở trong portal.
