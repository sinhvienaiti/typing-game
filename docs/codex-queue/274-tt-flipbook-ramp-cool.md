# Phiếu 274 · Tu Tiên · Code: than cuối đòn nguội về đỏ than (hệ số `rampCool` của shader có mặt nạ)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt. Không thiết kế lại.

**Báo cáo:** `docs/codex-queue/274-report.md` (tiếng Việt).

**Đường duyệt:**
- Claude chốt lúc 23:25 ngày 04/11.
- Anh đã duyệt nhịp cháy của lửa phím 1 (video 273b, lúc khoảng 22:00) và trước đó đã duyệt khung cuối A3, trong đó gốc nét "nguội thành than đỏ son".
- Bản xem trước 273b cho thấy điểm sống sau cùng vẫn trắng vàng. Nguyên nhân: trong `fbComposeMasked`, `r = (A.A − e)/(1 − e)` luôn chạm 1 ở điểm sống lâu nhất, nên dải màu bậc luôn cho trắng vàng.
- Đây là bản sửa nhỏ, có cổng mặc định 0, nên giữ nguyên mọi bản cũ. Bỏ bước phản biện.

## Làm ở đâu
- Worktree `games/.wt-ic-flipbook-cool`, nhánh `codex/flipbook-ramp-cool`, từ `main` `35f1b77`, có symlink `node_modules` (Claude đã tạo).
- cwd là gốc repo cha.

### Được ghi
- `games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts`;
- `games/.wt-ic-flipbook-cool/tests/view/flipbook-v2.test.ts`, chỉ **thêm** test, không sửa số của test cũ;
- `tools/vfx-masks/preview-masked.ts` (thêm cờ, mục 4) và `tools/vfx-masks/README.md`;
- `.local/codex-runs/274-out/`;
- `docs/codex-queue/274-report.md`.

### Cấm
- Sửa file khác. Mọi lệnh git trừ `status`, `diff`, `log`, `show`.
- Chạy Vitest hay Vite thiếu cờ `--no-cache --configLoader runner`. Mở cổng mạng.

## Việc (lời giải đã chốt)
1. **GLSL** (`FB_COMPOSE_GLSL`):
   - Thêm `uniform float uRampCool;` cạnh các uniform v2 khác, trong khối chèn sau `uniform vec4 uGrade;\n`.
   - Ngay sau dòng `float r = clamp((m.a - e) / max(1.0 - e, 1e-4), 0.0, 1.0);` thêm:
     ```glsl
     if (uRampCool > 0.0) r *= pow(clamp(1.0 - max(e, 0.0), 0.0, 1.0), uRampCool);
     ```
   - Dòng `vec3 cb = …` giữ nguyên, vì nó đã dùng `fbRamp(r)`.
   - Ý nghĩa: khi ngưỡng xói `e` tăng, điểm còn sống bị đẩy xuống phía son, rồi than. Với `uRampCool = 1`: e = 0,5 thì r lớn nhất 0,5 (cam); e = 0,75 thì 0,25 (son); e = 0,9 thì 0,1 (than).
   - `VERTEX` và `FRAGMENT` cũ (băm 258) **không đổi**. Chỉ đường v2 đổi.
2. **CPU** (`composeFlipbookMasked`):
   - Ngay sau `const r = clamp(…)`, thêm phép y hệt, với `look.rampCool`.
   - `FlipbookMaskedLook` thêm `readonly rampCool: number`.
   - `FLIPBOOK_MASKED_LOOK.rampCool = 0`, nên mặc định giữ nguyên mọi số cũ.
3. **Pool:**
   - uniform `uRampCool: { value: FLIPBOOK_MASKED_LOOK.rampCool }`;
   - setter `set rampCool(v: number)` cạnh `set hotLead`, có JSDoc;
   - đổi pool về đường cũ thì uniform không ảnh hưởng gì.
4. **Công cụ xem trước:**
   - `tools/vfx-masks/preview-masked.ts` thêm cờ `--ramp-cool <số>` (mặc định 0, chuyển vào look khi gọi `composeFlipbookMasked`) và `--out-prefix <tên>`.
   - Chạy với `--ramp-cool 1 --out-prefix cool`: ra `.local/codex-runs/274-out/cool-preview-ticks.png`, `cool-preview.mp4`, `cool-preview-area.json`, cùng dạng với 273b.
   - Import flipbook từ **worktree** `games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts` (thêm cờ `--flipbook <đường dẫn>`; mặc định giữ đường của game chính).
5. **Test mới** trong `flipbook-v2.test.ts`:
   - (a) mặc định `rampCool = 0` cho đúng số cũ: chạy lại một ca Test 4 có sẵn và so bằng nhau tuyệt đối;
   - (b) với `rampCool = 1`, ở e = 0,5 và A.A = 1, thân lấy màu ramp tại r = 0,5 (giữa cam và son theo `fbRamp`); ở e = 0,9 lấy màu tại r = 0,1 (than). Tính số mong đợi bằng chính hàm ramp viết tay trong test và so sai số 1e-6;
   - (c) chuỗi `FRAGMENT_V2` (lấy qua pool v2 như các test chuỗi sẵn có) chứa đúng dòng GLSL ở mục 1, và `VERTEX` hay `FRAGMENT` cũ vẫn đúng băm.

## Kiểm bắt buộc (trong worktree)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua. Mốc trước là 960 test; ghi số sau.
3. Build tạm với `IC_VITE_CACHE_DIR=/private/tmp/codex-274-dist/.vite-cache … --outDir /private/tmp/codex-274-dist --configLoader runner`: thoát 0. Rồi `grep -rl "uRampCool" /private/tmp/codex-274-dist` không in gì. Xóa thư mục build.
4. Chạy xem trước, mục 4. In chuỗi diện tích sáng tương đối (phải gần bằng chuỗi của 273b, vì `rampCool` chỉ đổi màu). In thêm, ở tick 30 và 36, màu trung bình (sRGB) của các điểm sáng: kênh đỏ phải lớn hơn hẳn kênh xanh lá và xanh dương (than đỏ).
5. `git status --short` trong worktree và ở repo cha: chỉ các file được ghi.

## Claude làm sau
Đọc diff, chạy lại kiểm, xem `cool-preview.mp4`, gửi anh. Nếu anh duyệt, phiếu nối lab (264) đặt `rampCool = 1` cho clip lửa phím 1.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
