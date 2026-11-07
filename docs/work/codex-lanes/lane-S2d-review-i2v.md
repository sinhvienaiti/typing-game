# Làn 2 · Duyệt tầng A cho MỘT đợt video làm lại từ ảnh

Claude chạy Firefly cho các việc trong `.local/s2/i2v-jobs.json`, rồi chạy `python3 -I .local/video-review/build-sheets.py` để tạo đợt `todo/redo-XX.json`.

Mỗi lần chạy lấy **một** đợt `redo-XX` chưa có kết quả. Chấm **tầng A theo vai trò** (`path-to-8.md` §1, 5 ô; không chấm vẻ đẹp tầng B). Ghi `.local/video-review/results/redo-XX.json` theo khuôn của `lane-C-video-review.md`, kèm `kind`.
- **Đạt** tầng A: đổi dòng trong `stream-2-image.md` thành `i2v-done` và chuyển sang danh sách GIỮ-CHỈNH (`stream-1-keep.md`) để cắt flipbook.
- **Trượt:** ghi lý do; đây là lần thứ hai thì đổi thành `blocked: cần anh xem`.

**Mức `high`.** Tối đa 15 ảnh. Nhớ luật khoá file danh sách.
