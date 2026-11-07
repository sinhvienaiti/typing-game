# Làn 1 · #14 R3-2 · hoàn tất phần mã (07/11/2026)
- Trong `games/.wt-ic-lab-all`: sửa `src/lab/thunder-travel-r2.ts`, cập nhật `tests/lab/thunder-travel-r2-probe.mjs`, thêm `tests/lab/thunder-guide-r3.test.ts` (172 dòng thêm).
- Dùng lại `thunder-ribbon-loop`: đầu sáng từ tay lên trời ở 120 ms, tới đỉnh cột ở 180 ms; đuôi thuôn, bề rộng thẻ phần thân 0,5–0,8 m; bỏ đường dẫn cũ, tắt dải đúng khung giáng; `tp2` tắt giữ nguyên B8 và đồng hồ đòn.
- Đạt 35/35 test riêng (`thunder-guide-r3`, `five-phase-clip`, `clip-skills`), probe `thunder-travel-r2-probe.mjs`, TypeScript các file thay đổi (0 lỗi kể cả phụ thuộc) và `git diff --check`.
- Không thêm texture, shader, video hay draw call so với R2; tối đa 13 đoạn trong một draw, dùng lại bộ đệm/vector/options; không chạy build, bộ test toàn game, trình duyệt/cổng mạng, không sửa media/manifest hay ghi Git.
- Chờ Claude làm #15: quay A/B pha bay và cả chiêu ở góc chơi, kiểm tra nối đoạn/đầu sáng/bề rộng thực, đo Δp95 ≤ +1,0 ms và p95 ≤ 11,5 ms, chấm mù; chưa nghiệm thu hình ảnh. Không tự mở cổng #16; dừng sau đúng một việc.
