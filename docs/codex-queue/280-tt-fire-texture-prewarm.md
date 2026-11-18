# Phiếu 280 · Tu Tiên · Code: làm ấm texture Hỏa lúc nạp để khung trúng đầu ≤ 11,5 ms

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/280-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, nền `ee3ee97`. Làm tiếp trên các thay đổi **chưa commit** của 277 và 278; đọc `277-report.md` và `278-report.md` trước. Có `?? art-src` là link của Claude: không đụng.

## Vì sao
Claude kiểm lại 278 (05/11 08:50, `docs/work/tasks/key1-fire.md`):
- Đạt 6/7 cổng: chớp khung đầu lên 1,00, không còn lớp cũ, Kim trùng khít.
- Trượt cổng 7: khung trúng đầu tiên mất 108 ms và 86 ms (ngưỡng 11,5 ms). Nguyên nhân chính là **nạp texture lần đầu**: 79,5 ms ở khung trúng, 183 ms ở khung bấm phím. Hàm prewarm của 278 mới chỉ biên dịch chương trình.
- Số đo: `typing-game-review/captures/tu-tien/code-drawn/lot1/`.

## Việc
1. **Làm ấm texture.** Hàm prewarm phần lửa mà 278 đã thêm phải gọi `renderer.initTexture(tex)` cho mọi texture Hỏa sẽ dùng trong một lượt tung:
   - mọi atlas của `FlipbookPool` (brush impact, mặt nạ A và B, sao, vòng tay, vòng đất, dải vạch, các clip lửa cũ còn dùng);
   - texture của `SpritePool` và đất.
   Gọi lúc nạp xong, sau khi `load()` của từng pool xong. Pool nào nạp muộn thì gọi tiếp khi nó xong.
2. **Biên dịch theo cả cảnh.** Gọi `renderer.compile(scene, camera)` một lần với các mesh Hỏa đang hiện tạm (ẩn bằng `visible` sau khi xong, hoặc đặt opacity 0), để đúng biến thể shader và đúng định dạng render target của chuỗi bloom. Không vẽ gì ra màn.
3. **Cờ đo.** `__lab.fireImpact()` trả thêm `prewarmed: boolean` và danh sách id texture đã làm ấm, để Claude kiểm.
4. **Không đổi hình, số hay nhịp.**

### Được ghi
`src/view/skills/element-fire.ts`, `src/view/skills/element-stage.ts`, `src/lab/skills-main.ts` (chỉ chỗ gọi prewarm và trường mới của `__lab.fireImpact()`), `tests/view/key1-flash-age0.test.ts` hoặc một test mới `tests/view/fire-prewarm.test.ts`, changelog `docs/changelog/2026-11-05-fire-lot1-art.md`, và `docs/codex-queue/280-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa kit, sim, nội dung, `art-src`; nới phép kiểm; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua. Mốc là 995 test.
3. Test mới, dùng renderer giả có đếm lần gọi: prewarm gọi `initTexture` đủ một lần cho mỗi texture Hỏa đã nạp, và gọi `compile` một lần.
4. Build bằng bộ bọc của 274 (lệnh như phiếu 278, thư mục `/private/tmp/codex-280-dist`): grep không thấy `fxcode`; xóa thư mục build.
5. `git status --short` chỉ có các tệp của 277, 278 và 280.

## Claude làm sau
Đo lại cổng 7 (≤ 11,5 ms ở khung bấm và khung trúng đầu). Đạt thì commit 277, 278 và 280, rồi gộp vào main sau 275.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
