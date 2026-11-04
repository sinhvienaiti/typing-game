# Phiếu 274b · Tu Tiên · Code: `rampCool` giữ than ở dải son, không rơi xuống muội

**Loại việc:** sửa nhỏ (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt.

**Báo cáo:** `docs/codex-queue/274b-report.md`.

**Đường duyệt:** Claude chốt lúc 23:35 ngày 04/11, sau khi xem bản xem trước của 274.
- Công thức 274 là `r *= (1 − e)^k`. Nó kéo mọi điểm còn sống về dưới 0,23, nên ramp trả màu muội (gần nền tối). Từ tick 18 lửa gần như tắt hẳn, trái luật "tàn bằng xói mòn, không tắt vụt".
- Muốn than đỏ thì phải giữ `r` trong dải son của `fbRamp` (khoảng 0,27–0,48), không đẩy về 0.

## Làm ở đâu
Cùng worktree `games/.wt-ic-flipbook-cool` (nhánh `codex/flipbook-ramp-cool`, có sẵn thay đổi chưa commit của 274), cwd là gốc repo cha.

### Được ghi
- `games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts`;
- `games/.wt-ic-flipbook-cool/tests/view/flipbook-v2.test.ts`, chỉ các test 274 đã thêm;
- `tools/vfx-masks/preview-masked.ts`, chỉ nếu cần;
- `.local/codex-runs/274-out/`;
- `docs/codex-queue/274b-report.md`.

### Cấm
- File khác; lệnh git ghi; Vitest hay Vite thiếu cờ `--no-cache --configLoader runner`; cổng mạng.

## Việc (lời giải đã chốt)
1. **GLSL:** thay dòng `if (uRampCool > 0.0) r *= pow(…);` bằng:
   ```glsl
   if (uRampCool > 0.0) r = min(r, mix(1.0, 0.40, uRampCool * smoothstep(0.2, 0.85, e)));
   ```
   - `uRampCool` nay là **độ mạnh**, từ 0 tới 1.
   - Với độ mạnh 1, trần của `r`: 1 khi e ≤ 0,2; khoảng 0,73 (cam) ở e = 0,5; 0,40 (giữa dải son) khi e ≥ 0,85.
   - Điểm sát mép xói (r nhỏ) vẫn ra muội. Như vậy than đỏ có viền mực tối, đúng khung cuối A3.
2. **CPU:** trong `composeFlipbookMasked`, đổi đúng như vậy: `r = Math.min(r, mix(1, 0.4, look.rampCool * smoothstep(0.2, 0.85, e)))`, dùng các hàm `mix` và `smoothstep` sẵn có trong file. Lưu ý trong hàm này có biến cục bộ tên `mix` che hàm cùng tên; đổi tên biến đó nếu cần, nhưng không đổi hành vi.
3. **JSDoc** của `rampCool` (look và setter) ghi: độ mạnh 0–1, công thức, mặc định 0.
4. **Test 274:**
   - giữ test (a), mặc định 0 cho số cũ;
   - viết lại (b): với độ mạnh 1, ở e = 0,5 và r = 1, trần là `mix(1, 0.4, smoothstep(0.2, 0.85, 0.5))`; ở e = 0,9 và r = 1, trần là 0,40. Màu thân bằng `fbRamp` viết tay trong test tại đúng số đó, sai số 1e-6;
   - giữ (c), kiểm chuỗi GLSL theo dòng mới.

## Kiểm bắt buộc
1. tsc không lỗi; Vitest đủ, mọi test qua (mốc 964).
2. Build tạm như phiếu 274; `grep -rl "uRampCool"` trên thư mục build không ra gì; xóa thư mục.
3. Chạy lại xem trước với `--ramp-cool 1 --out-prefix cool --flipbook <worktree>`, ghi đè các file `cool-*` trong `274-out`.
   - In diện tích sáng tương đối (gần bằng chuỗi 273b).
   - In màu trung bình sRGB của điểm sáng ở tick 18, 24, 30: kênh đỏ ≥ 2 lần kênh xanh lá và ≥ 4 lần kênh xanh dương.
   - In số điểm sáng ở tick 30 (phải > 0).
4. `git status --short`: chỉ các file được ghi.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
