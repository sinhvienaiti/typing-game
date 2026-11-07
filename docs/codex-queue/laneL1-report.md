# Làn 1 · #12 R3-1 · hoàn tất phần mã (07/11/2026 15:55)
- Trong `games/.wt-ic-lab-all`: sửa `src/lab/thunder-impact-r2.ts`, `src/lab/herd.ts`, `src/lab/skills-main.ts`; thêm `tests/lab/thunder-body-r3.test.ts` (tổng 182 dòng thêm).
- Chỉ khi `tp2=1`: nghiêng khỏi điểm giáng 10° ngay H0, đỉnh 14° ở 40 ms; nhún/nảy trong 80 ms theo chiều cao thân, về lại ở 300 ms; giữ viền Lôi 0,1 s, sát thương, choáng và cách chết; làm mới instance cùng khung trúng.
- Đạt 43/43 test riêng trong `thunder-body-r3`, `five-phase-clip`, `clip-skills`; TypeScript bốn file thay đổi và `git diff --check` đạt; phản ứng dùng bộ đệm cấp trước, không thêm shader/draw call.
- Không sửa media/manifest, không chạy build hay bộ test toàn game, không mở trình duyệt/cổng mạng hoặc ghi Git; chưa đo p95 hay xác nhận chất lượng hình ảnh.
- Chờ Claude làm #13: quay A/B góc chơi, đo Δp95 ≤ +1,0 ms và chấm mù pha/cả chiêu; không tự mở cổng #14. Dừng sau đúng một việc.
