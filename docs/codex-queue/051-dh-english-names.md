# Phiếu 051 · Rồng Giữ Ải · Đổi tên tiếng Anh cho danh từ trong game (lượt đổi tên của game)

Làm **giống hệt phiếu 050** (`docs/codex-queue/050-td-english-names.md`): đọc phiếu đó trước, rồi áp dụng cho Rồng Giữ Ải với các thay đổi dưới đây.

- **Bảng tên:** `docs/games/NAMES_EN.md`:
  - mục "Rồng Giữ Ải": 21 tên phải đổi, 55 dòng mã;
  - các dòng chốt của "Quyết định của Claude (27/10/2026)", ví dụ Phun Lửa thành **Fire Breath**, Viêm Đế thành **Inferno**;
  - các dòng "Cần Claude xem" giữ tiếng Việt.
- **Tên riêng giữ nguyên:** Bạch Long, Hỏa Long, Draconis, tướng có tên riêng.
- **Worktree:** `games/.wt-dh-names` (nhánh `dh-names`, cắt từ `main` e91c155, đã `pnpm install`, `public/assets` là symlink). Chỉ ghi trong `games/.wt-dh-names/src/**`, `tests/**`, `scripts/**` ở các file `NAMES_EN.md` liệt kê cho Rồng Giữ Ải, cộng `games/.wt-dh-names/docs/changelog/2026-10-28-english-names.md` và `docs/codex-queue/051-report.md`.
- **Không đụng:**
  - `games/dragon-hold` (cây chính);
  - `games/.wt-dh-vfx` (làn VFX đang chạy);
  - `src/view/fx*`, `src/view/vfx*` (của làn VFX).

  Nếu một tên nằm trong các file này thì bỏ qua và ghi vào báo cáo.
- **Golden:** `pnpm check` của Rồng có golden (`tests/golden`) và phép cân bằng. Golden lệch thì dừng, không cập nhật.
- **Mức Dễ, thẻ tốc độ** (Codex 023): chuỗi ở đó cũng theo luật tên.
- Báo cáo `docs/codex-queue/051-report.md` theo mẫu của phiếu 050.

**Xong khi:** sáu kiểm của phiếu 050 đạt trên `games/.wt-dh-names`. Claude kiểm trong trình duyệt rồi mới commit.
