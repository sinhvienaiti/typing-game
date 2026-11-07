# LANE-2 · Làm lại video: phân loại, ảnh đầu, duyệt bản làm lại

Chạy bằng `lane-runner.md`. **Cổng:** A = anh duyệt; C = Claude chạy Firefly hoặc tạo đợt duyệt.

| # | Việc | Phiếu | Mức | Cần xong trước | Cổng | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|
| 1 | T0 phân loại: lặp mỗi lần một bước cho tới khi xong và đã ghi danh sách | `lane-S2-t0-step.md` | high | — | | doing (lặp) | `.local/s2/checkpoint.json` |
| 2 | S2b: danh sách làm lại từ ảnh cũ và 2 mẫu ảnh đầu mới | `lane-S2b-redo-image-samples.md` | high | 1 | | todo | |
| 3 | Claude chạy Firefly cho danh sách từ ảnh cũ, rồi tạo đợt duyệt | — | — | 2 | C | todo (Claude) | |
| 4 | Duyệt tầng A đợt làm lại (lặp mỗi đợt) | `lane-S2d-review-i2v.md` | high | 3 | | todo (lặp) | |
| 5 | Anh duyệt 2 mẫu ảnh đầu mới | — | — | 2 | A | todo (anh) | |
| 6 | Vẽ ảnh đầu cho từng dòng còn lại (lặp mỗi lần một dòng) | `lane-S2c-still-row.md` | high | 5 | A | todo (lặp) | |
| 7 | Claude gửi anh tấm ảnh mỗi 6 dòng; anh duyệt thì chạy Firefly, rồi tạo đợt duyệt | — | — | 6 | A, C | todo (Claude) | |

**Ghi chú cho runner:**
- Việc 1 lặp: trạng thái giữ `doing (lặp)` cho tới khi phiếu T0 ghi "T0 xong", rồi đổi thành `done`.
- Việc lặp (4, 6) giữ `todo (lặp)` cho tới khi không còn đợt hay dòng nào, rồi đổi thành `done`.
