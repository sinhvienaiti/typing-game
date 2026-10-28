# Phiếu 101 · Rồng Giữ Ải · Hai câu chữ của map 1

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 101). Phiếu 100 của lô (từ vựng Rồng) là phiếu **094** trong hàng; mọi chỗ ghi "phiếu 100" ở đây đã đổi thành 094.

**Báo cáo:** `docs/codex-queue/101-report.md`.

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

**Vì sao:** kiểm kê map 1 (DH-16, P1, cổng G5).
- Tên ải 1 vẫn ghi "Bản thử: Cầu và Suối".
- Câu thua khi chưa gõ phím nào nói "Hỏa Long dùng Fire Breath", nhưng Fire Breath là chiêu riêng (phím chiêu 1). Đòn chữ là phun lửa thường.

**Nơi làm:** worktree `games/.wt-dh-codex`, **sau phiếu 094**. Giữ nguyên mọi thay đổi của 094.

**Chỉ được ghi:**
- `src/content/data/stages.ts` (chỉ dòng `nameVi` của ải 1, khoảng dòng 13);
- `src/ui/results.ts` (chỉ câu của nhánh `cause === "typing"` trong `starHint`, khoảng dòng 196);
- file test trong `tests/` đang khớp hai chuỗi cũ (tìm bằng `grep -rn "Bản thử\|dùng Fire Breath hạ" tests`);
- `docs/changelog/2026-10-29-text-fixes.md` (mới);
- `docs/codex-queue/101-report.md`.

**Việc:**
1. `nameVi: "Bản thử: Cầu và Suối"` → `nameVi: "Ải 1 · Cầu và Suối"` (dấu `·` U+00B7, có cách hai bên).
2. Câu thua: `". Gõ chữ trên đầu quái để Hỏa Long dùng Fire Breath hạ chúng."` → `". Gõ chữ trên đầu quái để Hỏa Long phun lửa vào chúng."`. Không đổi câu của nhánh `blight` và nhánh cuối.
3. Sửa test theo chuỗi mới. Thêm một ca nếu chưa có test nào kiểm câu của nhánh `typing`.

**Kiểm (bắt buộc):**
1. `pnpm check` xanh.
2. `grep -rn "Bản thử" src tests`: rỗng. `grep -rn "Fire Breath hạ" src tests`: rỗng.
3. Golden giữ: `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng.
4. `git -C games/.wt-dh-codex diff --stat`: chỉ các file trong "Chỉ được ghi" và file của phiếu 094.

**Xong khi:** bốn mục đạt. Claude xem thẻ đợt, màn kết quả ở 1280 và 1920 để chắc chữ không tràn.
