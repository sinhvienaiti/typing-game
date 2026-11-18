# Phiếu 287 · Tu Tiên · Git và code: gộp `main` vào nhánh lô 1 Hỏa, giải xung đột

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/287-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `9434ac2`. Có thay đổi chưa commit của phiếu 286. Hai link `?? art-src` và `?? node_modules` là của Claude: không đụng, không commit.

**Phiếu này cho phép lệnh git ghi, chỉ trong worktree này và chỉ các lệnh dưới đây.** Không push, không đổi nhánh, không đụng worktree hay nhánh khác.

## Việc
1. **Commit 286.**
   - Đọc `docs/codex-queue/286-report.md` để biết đúng các tệp.
   - `git add` từng tệp, có đường dẫn; không dùng `-A`.
   - Email `toanjaco2@gmail.com`.
   - Thông điệp kết bằng dòng `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
2. **Gộp main:** `git merge --no-ff main`. `main` ở `bbb46d8`, có phiếu 275 và 279: nhát chém kết phím 7 Hỏa vẽ bằng dải `strip-fire-sheath` thật.
3. **Giải xung đột,** chắc chắn ở `src/view/skills/element-fire.ts`, có thể cả `src/lab/skills-main.ts` và các test:
   - **Giữ đủ cả hai bên.**
   - Từ main: đường dải lửa của nhát chém kết, `uStripK` tính theo tỉ lệ 2:1, mép đầu mềm, cờ `?slash=tongues`, `?stripK=`.
   - Từ nhánh lô 1: brush impact (264); thẻ sao, vòng tay, vòng đất, dải vạch (277); chớp tuổi 0 (278); prewarm (280, 283, 286); đường cũ sau `?fxcode=1`.
   - Hai bên cùng dùng dải `strip-fire-sheath`, thì nạp một lần và dùng chung, không nạp hai lần.
   - Prewarm của nhánh lô 1 phải làm ấm cả texture và chương trình của nhát chém kết mới (`flame-slash.ts`).
4. **Commit merge,** cùng email và cùng dòng Co-Authored-By.

### Được ghi
Các tệp bị xung đột và những chỗ cần nối hai bên (`element-fire.ts`, `flame-slash.ts`, `element-stage.ts`, `skills-main.ts`, các test liên quan), changelog `docs/changelog/2026-11-05-fire-lot1-art.md`, và `docs/codex-queue/287-report.md` ở repo cha.

### Cấm
Push; `git reset`, `git rebase`, `git stash`, `git checkout` sang nhánh khác; sửa repo cha ngoài báo cáo; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua, gồm cả test 275/279 (`flame-slash.test.ts`) và test lô 1. Ghi tổng số test.
3. Build bằng bộ bọc 274 (thư mục `/private/tmp/codex-287-dist`): grep không thấy `fxcode`, `stripK`, `prewarmReport`; xóa thư mục build.
4. `git log --oneline -4` và `git status --short`: chỉ còn `?? art-src` và `?? node_modules`.

## Claude làm sau
Đo cổng 7 và parity trên nhánh đã gộp. Đạt thì fast-forward `main` của game.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
