# Phiếu 283 · Tu Tiên · Code: làm ấm phần chung để khung bấm phím và khung trúng đầu ≤ 11,5 ms

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/283-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `fe47341`. Commit này đã gồm 264, 277, 278, 280 và 281. Lúc giao `git status --short` chỉ có `?? art-src` và `?? node_modules` (link của Claude): không đụng.

## Vì sao
Claude đo lại sau 280 (05/11 10:40, `docs/work/tasks/key1-fire.md`):
- **Phần Hỏa đã ổn:** `prewarmed = true` với 18 texture.
- **Còn chậm:**
  - khung bấm phím 32,5–39,8 ms (trước 235);
  - khung trúng đầu 39,5–49,7 ms (trước 108);
  - ngưỡng 11,5 ms.
- **Phần còn lại phần lớn là đồ dùng chung:**
  - hai mặt nạ của qi slash (`burst-star-mask`, `slash-crescent-mask`, khoảng 13 ms) và 1 shader, ở tuổi 0;
  - 2 shader bóng đổ, ở tuổi 1;
  - một texture canvas 1024×256 (có lẽ là số sát thương), ở tuổi 3;
  - 18 shader chạy lần đầu ở khung bấm phím, có lẽ do lần vẽ thật đầu tiên trên Metal.
- **Số đo:** `typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-280/`.

## Việc
1. **Tìm nơi tạo từng thứ trên** (mặt nạ screen-fx của qi slash, vật liệu bóng đổ, texture số sát thương), rồi làm ấm lúc nạp lab:
   - `renderer.initTexture` cho mỗi texture;
   - `renderer.compile(scene, camera)` với các vật thể đó đang hiện tạm.
2. **Một lần vẽ thật ngoài màn hình lúc nạp:**
   - render cảnh một khung vào một render target nhỏ, khoảng 64×64, cùng định dạng chuỗi bloom;
   - lúc đó mỗi pool Hỏa và Kim, pool qi slash và số sát thương có 1 thẻ ở tuổi 0;
   - rồi xóa sạch các thẻ đó.
   - Không thẻ nào còn sống sau prewarm; không âm nào phát; sim và nhịp không đổi.
3. **Làm ấm cho cả Kim:** cùng hàm, với tham số nguyên tố, để đổi nguyên tố trong lab cũng không khựng.
4. **`__lab.prewarmReport()`** trả danh sách texture và chương trình đã làm ấm, để Claude kiểm.

### Được ghi
- `src/lab/skills-main.ts`: chỉ phần prewarm và `__lab.prewarmReport`;
- `src/view/screen-fx.ts`, `src/view/hitfx.ts`, `src/view/renderer.ts`: chỉ thêm hàm prewarm, không đổi hành vi;
- `src/view/skills/element-fire.ts`, `src/view/skills/element-stage.ts`: chỉ phần prewarm;
- test mới `tests/view/skill-prewarm-shared.test.ts`, và các test hiện có của đúng các hàm prewarm này (cập nhật ca kiểm hành vi cũ, không nới);
- changelog `docs/changelog/2026-11-05-fire-lot1-art.md`;
- `docs/codex-queue/283-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa kit, sim, nội dung, `art-src`; đổi hình, số hay nhịp; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua. Mốc là 1000 test ở `fe47341`.
3. Test mới, với renderer giả có đếm lần gọi:
   - prewarm gọi `initTexture` cho mặt nạ qi slash và texture số;
   - có đúng một lần render vào target nhỏ;
   - sau prewarm, mọi pool có `count = 0`.
4. Build bằng bộ bọc của 274 (thư mục `/private/tmp/codex-283-dist`): grep không thấy `prewarmReport`; xóa thư mục build.
5. `git status --short` chỉ có các tệp được ghi.

## Claude làm sau
Đo lại cổng 7 với Hỏa và Kim. Đạt thì commit và gộp nhánh vào main, xử lý xung đột `element-fire.ts` với 275 và 279 đã gộp.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
