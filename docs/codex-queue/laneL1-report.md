07/11/2026 13:08 · Chỉ xử lý #10 (lane-L1-measure-fixes); blocked chờ Claude xác minh Vitest, do chỉ thị trực tiếp lượt này cấm bộ test game.
Chỉ sửa games/.wt-ic-lab-all/tests/lab/pilot-measure-fixes.test.ts: fixture dùng ID blood-ring-burst/water-ring-burst hợp lệ; giữ role ringBurst và toàn bộ assertion. ID có chữ hoa trước đây bị parser từ chối trước khi gọi hiệu ứng.
Fixture reset hook kiếm trước stage như lab thật; cập nhật thêm bước 0 giây để pool loại card hết tuổi sau update(2), đúng hợp đồng vẽ rồi tăng tuổi. Không sửa parser, mã hiệu ứng, media, manifest hay thay đổi của tác nhân khác.
Đã qua: npx --no-install tsc --noEmit; node --check scripts/visual/scenarios/lab-pilot-ab.mjs; 2 self-test Node của kịch bản (ngưỡng 0,5%, P1/P2/P4); git diff --check.
4 probe Node trực tiếp qua: Blood K1/vòng riêng chung pool, vị trí sàn và kết thúc; Water không sinh vòng; cổng baseline/pilot rộng 1,75 thân boss, đúng pivot/sàn và giữ điểm sinh. Không chạy build, Vitest, trình duyệt hay Git ghi.
Claude cần chạy npx --no-install vitest run --maxWorkers=4 trong games/.wt-ic-lab-all, rồi quay/đo P1/P2/P4; chưa có nghiệm thu thị giác/hiệu năng. Đã nhả khóa; không làm việc tiếp theo.
