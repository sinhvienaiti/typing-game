# Làn 2 · Vẽ ảnh đầu cho MỘT dòng LÀM-LẠI-ẢNH (sau khi anh duyệt mẫu)

Mỗi lần chạy lấy **dòng đầu tiên** của `docs/work/tasks/vfx-streams/stream-2-image.md` có cột ảnh `sửa` hoặc `mới` và trạng thái `todo`.
- Vẽ 2 bản đúng như mục 2 của `lane-S2b-redo-image-samples.md`: tham chiếu nội bộ bắt buộc, theo kiểu try2 anh đã duyệt và `path-to-8.md` §5; lưu vào `stills/skills/` với tên `<job>-still.v1-try<k>.png`.
- Tự chấm, chọn bản tốt.
- Thêm mục việc Firefly cho bản đã chọn vào `.local/s2/i2v-jobs.json` (cách ghi như S2b: aspect không dấu cách, `takes: 2`, prompt theo §5).
- Đổi trạng thái dòng thành `still-ready`.
- Thêm ảnh vào tấm ghép đợt `.local/s2/still-batch-<n>.jpg`, mỗi tấm 6 dòng, để Claude gửi anh.

**Mức `high`.** Tối đa 8 ảnh xem. Không chạy Firefly, không sửa video, manifest hay mã.
