# Phiếu 287b · Tu Tiên · Code: giải xung đột gộp `main` vào nhánh lô 1 Hỏa (không lệnh git)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/287b-report.md`.

**Vì sao có phiếu này:** phiếu 287 kẹt từ 12:01 vì sandbox của Codex không ghi được `.git` của worktree. Claude đã tự làm phần git lúc 14:20: commit 286 (`07b73f6`), rồi `git merge --no-ff main`. Merge đang dừng ở 2 tệp xung đột. **Phiếu này không dùng lệnh git ghi nào**; Claude sẽ commit merge sau khi kiểm.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, đang ở giữa merge (`MERGE_HEAD` = `main` `bbb46d8`). Hai link `?? art-src` và `?? node_modules` là của Claude: không đụng.

## Việc
1. **Giải xung đột** trong `src/view/skills/element-fire.ts` và `src/lab/skills-main.ts` (xóa hết dấu `<<<<<<<`, `=======`, `>>>>>>>`). **Giữ đủ cả hai bên**, như phiếu 287 bước 3:
   - từ `main` (275/279): đường dải lửa `strip-fire-sheath` của nhát chém kết, `uStripK` tính theo tỉ lệ 2:1, mép đầu mềm, cờ `?slash=tongues`, `?stripK=`;
   - từ nhánh lô 1: brush impact (264); thẻ sao, vòng tay, vòng đất, dải vạch (277); chớp tuổi 0 (278); prewarm (280, 283, 286); đường cũ sau `?fxcode=1`.
2. Hai bên cùng dùng dải `strip-fire-sheath`: nạp một lần, dùng chung.
3. Prewarm của nhánh lô 1 phải làm ấm cả texture và chương trình của nhát chém kết mới (`flame-slash.ts`). Thêm một test cho điều đó vào test prewarm có sẵn.

### Được ghi
`src/view/skills/element-fire.ts`, `src/lab/skills-main.ts`, `src/view/skills/flame-slash.ts`, `src/view/skills/element-stage.ts` (chỉ phần prewarm), các test liên quan trong `tests/`, changelog `docs/changelog/2026-11-05-fire-lot1-art.md`, và `docs/codex-queue/287b-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi (`add`, `commit`, `merge`, `reset`, `checkout`, `stash`…); sửa tệp khác; mở cổng mạng.

## Kiểm bắt buộc
1. `grep -rn '^<<<<<<<\|^>>>>>>>' src tests` không còn dòng nào.
2. `tsc --noEmit -p .` không lỗi.
3. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua, gồm `flame-slash.test.ts` và các test lô 1. Ghi tổng số test.
4. Build bằng bộ bọc 274 (thư mục `/private/tmp/codex-287b-dist`): grep không thấy `fxcode`, `stripK`, `prewarmReport`; xóa thư mục build.

## Claude làm sau
`git add` từng tệp, commit merge, đo cổng 7 và parity trên nhánh đã gộp; đạt thì fast-forward `main` của game.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
