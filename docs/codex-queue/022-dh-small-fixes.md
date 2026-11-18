# Phiếu 022 · Rồng Giữ Ải · 4 việc nhỏ sau đợt test 27/10 (chỉ mã, không trình duyệt)

**Bối cảnh:** sau đợt test 27/10, agent sửa của Claude để lại 3 việc nhỏ viết sẵn cho Codex. Người kiểm lại tìm thêm 1 lỗi nhẹ do lượt sửa gây ra. Changelog ở `games/dragon-hold/docs/changelog/2026-10-27-test-pass.md`. Làn Claude của game này đã xong (HEAD `17b1547`, đã đẩy lên GitHub), nên Codex làm một mình trong cây này.

Chủ dự án (27/10) giao việc nhỏ cho Codex và yêu cầu làm đúng, không sai sót. Sandbox của Codex **không mở được cổng** (`listen EPERM`), nên phiếu này **không có bước trình duyệt**. Claude chạy các kịch bản trình duyệt sau khi đọc diff.

**Thư mục làm việc:** `games/dragon-hold` (lệnh dưới đây chạy ở đó).

**Cấm:**
- lệnh git có ghi (chỉ `status`, `diff`, `log`, `show`); Claude commit;
- sửa `src/sim/**`, `src/content/**` (trừ khi việc ghi rõ), golden, `src/kit/**`;
- đụng media, game khác, Tu Tiên;
- mở dev server hay Chrome.

## Việc

1. **Đếm ngược và lời "phím 1–8" hiện hai lần.**
   - `src/ui/hud.ts`, dòng pha (khoảng dòng 420–432):
     - lúc `warning` ghi "Đợt N sắp tới" và bỏ số giây;
     - lúc `break` có đồng hồ ghi "Nghỉ giữa đợt"; giữ nhánh "đứng chờ khi mở …";
     - bỏ phần gọi sớm, vì nút gọi sớm và dòng "sau N s" đã có trên thẻ đợt.
   - `src/ui/learning-frame.ts` (khoảng dòng 315): ở dòng chờ của Bày binh và lúc nghỉ, bỏ câu "phím 1–8 chọn món ở dải dưới". Đầu dải Bộ Mang Theo (`src/ui/shop-strip.ts:296`) đã ghi câu đó.
   - Sửa test liên quan (`tests/ui/hud.test.ts` và các test khác) nếu chúng khóa chữ cũ.
2. **`dh-focus` nhận cỡ màn.**
   - `scripts/visual/scenarios/dh-focus.mjs` dòng 28 đang cứng `{ width: 1280, height: 720 }`.
   - Thêm `const [W, H] = process.env.SIZE === '1920' ? [1920, 1080] : [1280, 720]`, truyền vào `boot`, ghi `W×H` vào tên ảnh.
   - Chỉ sửa kịch bản; `node --check` phải qua.
3. **Dấu × trên thẻ đợt quá nhỏ ở 1280.**
   - Ở `src/ui/styles/dh.css` (`.dh-foe__count`) và các số đếm "Quái bay ×N", "Tướng ×N" trong `src/ui/wave-card.ts` (khoảng dòng 258, 270–280), bọc dấu × trong một span riêng, để dấu × cao ít nhất 70 % chữ số và đậm như chữ số.
   - Sửa `tests/ui/wave-card.test.ts` nếu cần.
4. **Lỗi lượt sửa: chữ vừa gõ đúng nảy lại khi gõ sai ngay sau đó.**
   - **Nguyên nhân** (người kiểm lại đo ở `games/dragon-hold/tmp/mac-2026-10-27/test/recheck/repop.mjs`): trong `src/ui/tags.ts` (khoảng dòng 874–894), phím sai đổi trạng thái hồng nên HTML của thẻ dựng lại. Lớp `j` vẫn được gắn vì `ticking` còn đúng, nên span mới chạy lại hoạt ảnh `dh-letter` từ đầu (scale 1,19 lên 1,43). Ở 70 WPM, 84/85 phím sai rơi vào lúc chữ đang nảy.
   - **Cách sửa đề xuất:** span dựng lại tiếp tục hoạt ảnh đang chạy thay vì chạy lại từ đầu. Ví dụ đặt `animation-delay` âm bằng thời gian đã trôi kể từ `tag.tickAt`, qua một biến CSS trên span. Giữ nguyên hành vi khi gõ đúng liên tiếp, và giữ nhánh giảm chuyển động.
   - **Test** trong `tests/ui/` (môi trường node, dùng `tests/ui/fake-world.ts` như các test cạnh đó): dựng HTML thẻ sau một phím đúng, rồi sau một phím sai ở +100 ms. Span của chữ vừa gõ phải mang độ trễ âm khoảng 100 ms, không bắt đầu lại từ 0.

## Kiểm (bắt buộc)

1. Sau mỗi việc có sửa mã: `../../.local/bin/heavy.sh pnpm check`. Ghi số test; tsc và build phải xanh.
2. Golden: `../../.local/bin/heavy.sh pnpm exec tsx scripts/balance/golden.ts` (hoặc lệnh golden trong `package.json`). Bốn ca phải giữ nguyên mã băm, vì không việc nào được đổi sim.
3. `node --check scripts/visual/scenarios/dh-focus.mjs`.
4. Cuối cùng dán `git diff --stat` và `git diff` đầy đủ vào báo cáo.

## Báo cáo `docs/codex-queue/022-report.md` (repo cha)

Bảng `| # | Việc | File:dòng | Kiểm (lệnh, kết quả) | Còn cần Claude kiểm trên trình duyệt |`. Cột cuối ghi rõ kịch bản và cỡ cho Claude:
- việc 1 và 3: `ui-preview` ở 1280×720 và 1920×1080, cảnh warning, break, prep;
- việc 2: `SIZE=1920 dh-focus`;
- việc 4: `repop.mjs` ở 1280.

**Xong khi:** 4 việc có kết quả, `pnpm check` và golden đạt trên cây cuối.
