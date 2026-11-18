# Phiếu 297 · Tu Tiên · Code: làm ấm vật liệu số sát thương (`IcNumberSprites`)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu rất ngắn, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/297-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `c15af6f` (đã có 291). `?? art-src`, `?? node_modules` là link của Claude: không đụng. **Không lệnh git ghi.**

## Vì sao
Đo 05/11 16:30 (`typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-291/`, số trong `docs/work/tasks/key1-fire.md`): sau 291 không còn chương trình bóng muộn, nhưng **khung 13** (cả Hỏa và Kim) còn link muộn một chương trình: vật liệu số sát thương `IcNumberSprites` (`src/view/hitfx.ts` quanh dòng 754), làm khung đó 14,8–25,6 ms. Có từ trước 291.

## Việc
1. Tìm đúng khóa chương trình của vật liệu số lúc chơi (define, blending, sương, đèn nếu vào khóa, target), như cách phiếu 291 làm với bóng.
2. Thêm vào lượt làm ấm chung (283/286/291) để biên dịch đúng chương trình đó lúc nạp (một số mẫu hiện tạm rồi trả lại), không để số nào còn hiện sau làm ấm.
3. Test trong `tests/view/skill-prewarm-shared.test.ts`: lượt làm ấm tạo đúng khóa chương trình của vật liệu số; trạng thái trả lại.

### Được ghi
`src/view/hitfx.ts` (chỉ phần cần cho làm ấm), `src/view/renderer.ts`, `src/view/skills/element-stage.ts` (phần làm ấm), `src/lab/skills-main.ts` (phần làm ấm), `tests/view/skill-prewarm-shared.test.ts`, changelog `docs/changelog/2026-11-05-fire-lot1-art.md`, `docs/codex-queue/297-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; đổi hình, số, nhịp; sửa tệp khác; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi. 2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`) qua (mốc 1031). 3. Build bộ bọc 274 (`/private/tmp/codex-297-dist`), grep không thấy `fxcode`, `stripK`, `prewarmReport`; xóa thư mục build.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
