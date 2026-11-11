# LANE-2 · Làm lại video: phân loại, ảnh đầu, duyệt bản làm lại

Chạy bằng `lane-runner.md`. **Cổng:** A = anh duyệt; C = Claude chạy Firefly hoặc tạo đợt duyệt.

| # | Việc | Phiếu | Mức | Cần xong trước | Cổng | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|
| 1 | T0 phân loại: lặp mỗi lần một bước cho tới khi xong và đã ghi danh sách | `lane-S2-t0-step.md` | high | — | | done | 640/640 đã xếp, danh sách đã ghi (Claude xác nhận 13:30) |
| 2 | S2b: danh sách làm lại từ ảnh cũ và 2 mẫu ảnh đầu mới | `lane-S2b-redo-image-samples.md` | high | 1 | | done | `.local/s2/i2v-jobs.json` (133 việc; 27 needsCopy); 4 PNG + prompt; `.local/s2/still-samples-2.jpg`; đề xuất/kiểm: `.local/s2/still-samples-review.md` (chờ anh duyệt) |
| 3 | Claude chạy Firefly cho danh sách từ ảnh cũ, rồi tạo đợt duyệt | — | — | 2 | C | doing (Claude): 35/131 việc `-i2v3` xong; đã chọn bản đẹp cho cả 35 (`.local/s2/picks-i2v3.json`), 3 việc cả hai bản hỏng nên xếp làm lại `-i2v4` (khoá màu). Firefly vẫn báo "Please try again later" tới 11/11 15:00; thử lại định kỳ. Còn 95 việc + 3 làm lại | |
| 4 | Duyệt tầng A đợt làm lại (lặp mỗi đợt) | `lane-S2d-review-i2v.md` | high | — (làm được khi trong `.local/video-review/todo/` có đợt `redo-XX` chưa có kết quả) | C: Claude xem 24 clip redo-02 ở tốc độ thật, cỡ chơi (16:35: cả 24 đều NOT-ENOUGH-EVIDENCE, 4 lượt liền chỉ đo Băng Nguyệt take2) | todo (lặp) | redo-02: chỉ đăng ký silhouette Băng Nguyệt take2 [46,70) @24 contain 0,9. ECC 24/24 mỗi ngưỡng; convex hull IoU sau khớp min 0,950–0,966; mask còn nhạy ánh sáng. Chưa A-PASS; không suy cỡ bbox từ singular values affine. Bằng chứng registration-evidence và registration-hull-evidence; partial cập nhật đúng 1/24 mục. Bước sau: Claude phát tốc độ thật/cỡ chơi và kiểm matte; không đo lặp bbox/ECC. |
| 5 | Anh duyệt 2 mẫu ảnh đầu mới | — | — | 2 | A | todo (anh): đã gửi tấm 14:05 | |
| 6 | Vẽ ảnh đầu cho từng dòng còn lại (lặp mỗi lần một dòng) | `lane-S2c-still-row.md` | high | 5 | A | todo (lặp) | |
| 7 | Claude gửi anh tấm ảnh mỗi 6 dòng; anh duyệt thì chạy Firefly, rồi tạo đợt duyệt | — | — | 6 | A, C | todo (Claude) | |

**Ghi chú cho runner:**
- Việc 1 lặp: trạng thái giữ `doing (lặp)` cho tới khi phiếu T0 ghi "T0 xong", rồi đổi thành `done`.
- Việc lặp (4, 6) giữ `todo (lặp)` cho tới khi không còn đợt hay dòng nào, rồi đổi thành `done`.
