# LANE-2 · Làm lại video: phân loại, ảnh đầu, duyệt bản làm lại

Chạy bằng `lane-runner.md`. **Cổng:** A = anh duyệt; C = Claude chạy Firefly hoặc tạo đợt duyệt.

| # | Việc | Phiếu | Mức | Cần xong trước | Cổng | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|
| 1 | T0 phân loại: lặp mỗi lần một bước cho tới khi xong và đã ghi danh sách | `lane-S2-t0-step.md` | high | — | | done | 640/640 đã xếp, danh sách đã ghi (Claude xác nhận 13:30) |
| 2 | S2b: danh sách làm lại từ ảnh cũ và 2 mẫu ảnh đầu mới | `lane-S2b-redo-image-samples.md` | high | 1 | | done | `.local/s2/i2v-jobs.json` (133 việc; 27 needsCopy); 4 PNG + prompt; `.local/s2/still-samples-2.jpg`; đề xuất/kiểm: `.local/s2/still-samples-review.md` (chờ anh duyệt) |
| 3 | Claude chạy Firefly cho danh sách từ ảnh cũ, rồi tạo đợt duyệt | — | — | 2 | C | doing (Claude): đợt 1 xong 07/11 14:44 (10 việc, 20 bản): sạch, giữ hình nhưng gần đứng yên. Đợt thử 2 xong 10/11 09:30 (4 việc `-i2v3`, prompt có cú bùng nổ, 8 bản): chuyển động mạnh hơn (đo bước 12–14 so với 7–10), mỗi việc có ít nhất 1 bản giữ hình; bản kia đôi khi bịa vật mới hoặc mất chủ thể. Chờ anh duyệt cách viết rồi chạy 119 việc còn lại | |
| 4 | Duyệt tầng A đợt làm lại (lặp mỗi đợt) | `lane-S2d-review-i2v.md` | high | — (làm được khi trong `.local/video-review/todo/` có đợt `redo-XX` chưa có kết quả) | C: Claude xem 24 clip redo-02 ở tốc độ thật, cỡ chơi (16:35: cả 24 đều NOT-ENOUGH-EVIDENCE, 4 lượt liền chỉ đo Băng Nguyệt take2) | todo (lặp) | redo-02: chỉ đăng ký silhouette Băng Nguyệt take2 [46,70) @24 contain 0,9. ECC 24/24 mỗi ngưỡng; convex hull IoU sau khớp min 0,950–0,966; mask còn nhạy ánh sáng. Chưa A-PASS; không suy cỡ bbox từ singular values affine. Bằng chứng registration-evidence và registration-hull-evidence; partial cập nhật đúng 1/24 mục. Bước sau: Claude phát tốc độ thật/cỡ chơi và kiểm matte; không đo lặp bbox/ECC. |
| 5 | Anh duyệt 2 mẫu ảnh đầu mới | — | — | 2 | A | todo (anh): đã gửi tấm 14:05 | |
| 6 | Vẽ ảnh đầu cho từng dòng còn lại (lặp mỗi lần một dòng) | `lane-S2c-still-row.md` | high | 5 | A | todo (lặp) | |
| 7 | Claude gửi anh tấm ảnh mỗi 6 dòng; anh duyệt thì chạy Firefly, rồi tạo đợt duyệt | — | — | 6 | A, C | todo (Claude) | |

**Ghi chú cho runner:**
- Việc 1 lặp: trạng thái giữ `doing (lặp)` cho tới khi phiếu T0 ghi "T0 xong", rồi đổi thành `done`.
- Việc lặp (4, 6) giữ `todo (lặp)` cho tới khi không còn đợt hay dòng nào, rồi đổi thành `done`.
