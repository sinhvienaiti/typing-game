# Phiếu 105 · Rồng Giữ Ải · Nút "Về cổng game" ở màn kết quả; bỏ `ui-preview` khỏi bản production

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 105). Phiếu 100 của lô (từ vựng Rồng) là phiếu **094** trong hàng; mọi chỗ ghi "phiếu 100" ở đây đã đổi thành 094.

**Báo cáo:** `docs/codex-queue/105-report.md`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo). Mã nằm trong worktree nêu ở từng phiếu; mọi đường dẫn mã tính từ worktree đó.
- **Được dùng git chỉ đọc:** `show`, `log`, `diff`, `status`, `ls-tree`. **Cấm** mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`, `worktree`…).
- **Cấm:**
  - sửa `src/kit/**` của game (bản chép từ kit, có kiểm sha256);
  - sửa file golden hay chạy lệnh cập nhật golden (`dh:golden:update`, `td:golden:update`…);
  - ghi vào cây chính của game (`games/<id>`), worktree khác, game khác; đụng Tu Tiên;
  - sửa file ở repo cha (nginx, `scripts/`, `shared/`), trừ khi phiếu cho phép;
  - dev server, trình duyệt (sandbox không mở được cổng); media (ảnh, âm, GLB).
- **Cách làm:** test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn. Chuỗi người chơi thấy: câu tiếng Việt, danh từ game tiếng Anh (`docs/games/NAMES_EN.md`).
- **Mỗi phiếu có changelog** `docs/changelog/2026-10-29-<tên>.md` trong worktree, tiếng Việt: làm gì, vì sao, số đo.
- **Báo cáo** `docs/codex-queue/<số>-report.md` và thư mục `docs/codex-queue/<số>/` (log, số đo): file đã đổi; đầu ra của từng mục Kiểm, có số; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chạy lại kiểm, đọc diff, kiểm trên trình duyệt ở 1280 và 1920 khi phiếu đụng giao diện, rồi commit trên nhánh của worktree và gộp.

## Phiếu

**Vì sao:** kiểm kê map 1.
- **DH-24 (P2, G5):** màn kết quả chỉ có "Chơi lại"; không có lối về cổng game.
- **DH-23 phần 1 (P2, G7):** bản build còn chunk `ui-preview` (trang thử HUD trên thế giới giả, `src/main.ts:15`), chỉ cần ở dev.
- Hàm lấy địa chỉ cổng game viết một lần ở đây; màn tựa (DH-13) và màn cài đặt (DH-15) của Claude dùng lại.

**Nơi làm:** worktree `games/.wt-dh-codex`, **sau phiếu 094 và 101**. Giữ nguyên thay đổi của hai phiếu đó.

**Chỉ được ghi:**
- `src/app/portal.ts` (mới);
- `src/ui/results.ts` và file CSS của màn kết quả (ghi tên);
- `src/main.ts` (chỉ dòng nạp `ui-preview`);
- `tests/app/portal.test.ts` (mới), test màn kết quả trong `tests/ui/`;
- `docs/changelog/2026-10-29-portal-button.md` (mới);
- `docs/codex-queue/105-report.md`, `docs/codex-queue/105/`.

**Cấm thêm:** sửa `src/kit/learning/**` (nguồn portal trong kit là việc của DEPLOY_INDEPENDENCE §9, Claude làm sau).

**Việc:**
1. **`src/app/portal.ts`:** `export function portalHome(origins: string | undefined): string`. Lấy nguồn đầu tiên khác rỗng trong danh sách phân cách dấu phẩy (đã `trim`); không có thì `"https://typing-game.local"`. Trả về nguồn đó cộng `/`. Chỗ gọi truyền `import.meta.env.VITE_PORTAL_ORIGINS`.
2. **Màn kết quả:**
   - thêm nút thứ hai "Về cổng game", nhãn phím `Esc` theo kiểu của nút "Chơi lại" (`keyLabel`);
   - nút là thẻ `<a href="<portalHome>" target="_top">`, để khi game nằm trong khung của portal thì cả trang về cổng;
   - phím mũi tên trái, phải, lên, xuống chuyển tiêu điểm giữa hai nút; Enter bấm nút đang chọn; Esc bấm "Về cổng game";
   - nếu Esc ở màn kết quả đang có việc khác thì dừng và báo, không đổi.
3. **`src/main.ts:15`:** chỉ nạp `./ui/ui-preview` khi `import.meta.env.DEV`, để Vite bỏ chunk này khỏi bản production. Sửa chú thích dòng 3 cho đúng.
4. **Test:**
   - `portalHome(undefined)`, `portalHome("")`, `portalHome(" https://a.example , https://b.example")`;
   - màn kết quả có hai nút; Esc kích hoạt nút về cổng; mũi tên chuyển tiêu điểm.

**Kiểm (bắt buộc):**
1. `pnpm check` xanh; ghi số test trước và sau.
2. Golden giữ: `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng.
3. Sau `pnpm build`: `ls dist/assets | grep -i preview` rỗng; `grep -l "startUiPreview" dist/assets/*.js` rỗng. Ghi tổng cỡ `dist/assets/*.js` trước và sau.
4. **Đột biến:** bỏ điều kiện `import.meta.env.DEV` thì kiểm 3 phải thấy chunk; đổi giá trị mặc định của `portalHome` thì test phải đỏ.
5. `git -C games/.wt-dh-codex status --short -uall`: chỉ các file trong "Chỉ được ghi" và file của 094, 101.

**Xong khi:** năm mục đạt. Claude kiểm màn thắng và màn thua ở 1280 và 1920, bằng phím, cả khi mở trong portal qua `https://typing-game.local`.
