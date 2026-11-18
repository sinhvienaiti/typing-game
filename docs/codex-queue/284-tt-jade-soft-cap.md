# Phiếu 284 · Tu Tiên · Code: vòng ngọc đổi nắp cứng 0,95 thành nắp mềm để đĩa ngọc hết phẳng

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/284-report.md`.

**Worktree:** `games/.wt-immortality-cultivation-codex`, nhánh `codex/jade-ring-material`, HEAD `453fd43` (đã có 259 và 259b). Lúc giao chỉ có `?? node_modules` và có thể `?? art-src` (link của Claude): không đụng.

## Vì sao
Claude chỉnh 50 bộ số trong lab (05/11 10:55, `docs/work/tasks/jade-ring.md`):
- Không bộ nào đạt Kiểm 9.
- **Nguyên nhân:** nắp cứng 0,95 theo độ sáng Rec. 709 cắt ít nhất nửa đĩa ngọc về đúng 0,95. Đĩa thành phẳng, mất nét chạm và độ bóng, đúng chỗ anh chê "phẳng, xám".
- Bốn núm `jadeAlbedo`, `jadeRough`, `jadeNormal`, `jadeSheen` không nâng được gì; sheen bị bộ giới hạn headroom bỏ hết.
- Kiểm 8 (tràn mép) đã đạt.

## Việc
1. **Thay phép cắt cứng bằng nắp mềm có điểm gối (knee)**, cùng chỗ và cùng trọng số Rec. 709 (`luma = dot(rgb, vec3(0.2126, 0.7152, 0.0722))`):
   ```glsl
   float softCap(float y, float knee, float cap) {
     return y <= knee ? y : knee + (cap - knee) * (1.0 - exp(-(y - knee) / (cap - knee)));
   }
   ```
   - Nhân màu theo `softCap(luma, knee, cap) / max(luma, 1e-4)`.
   - `cap` giữ 0,95, vẫn dưới ngưỡng bloom như trước.
   - `knee` mặc định 0,72, mở cờ lab `?jadeKnee=` và `__lab.jadeRing({ knee })`.
   - Bản CPU dùng để test và đo phải dùng cùng công thức.
2. **Lớp bóng (sheen)** đi qua nắp mềm thay vì bị bộ giới hạn headroom bỏ hết.
   - Vệt bóng phải còn thấy được ở `jadeSheen > 0`.
   - Trần tổng vẫn ≤ 0,95.
3. **Ánh sáng mép khi tan** (`swRingDe`) vẫn nằm ngoài trần, như 259b.
4. **`ringCap()`** báo thêm tỉ lệ điểm ảnh ngọc đang ở trên 0,94. Mục đích: chứng minh đĩa không còn bị dồn lên trần.

### Được ghi
Đúng các tệp phiếu 259 và 259b đã cho ghi, cộng các test hiện có kiểm phép cắt cũ (cập nhật cho đúng nắp mềm, không nới), một test mới `tests/view/jade-soft-cap.test.ts`, và `docs/codex-queue/284-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa file khác; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua.
3. Test mới:
   - `softCap` liên tục và đơn điệu, đạo hàm liên tục tại `knee`;
   - `softCap(y)` < `cap` với mọi `y` hữu hạn;
   - trên bộ số tổng hợp của một đĩa sáng, tỉ lệ điểm ảnh ≥ 0,94 giảm từ trên 50 % xuống dưới 10 %;
   - vệt sheen còn khác 0.
4. Build bằng bộ bọc của 274 (thư mục `/private/tmp/codex-284-dist`): grep không thấy `jadeKnee`; xóa thư mục build.
5. `git status --short` chỉ có các tệp được ghi.

## Claude làm sau
Chỉnh `knee` và `sheen` trong lab tới Kiểm 9, gửi anh tấm so, rồi gộp.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
