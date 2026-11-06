# Phiếu 310 · Trang xem lại Firefly dùng lại được

Đã sửa `tools/review-gallery/build.py`, `serve.mjs`; thêm
`notes-2026-11-05.json`, `test_build.py`, `README.md` trong cùng thư mục.
CLI nhận đủ các cờ trong phiếu; logic gom việc, nhóm và trạng thái là hàm thuần.
Notes mẫu giữ nguyên NOTE, STONE, lý do loại, tiêu đề và lead có địa chỉ lab 4310.
CSS và nhãn cũ được giữ; mở video lớn cũng dừng video xem trước.

Kiểm: `python3 -B -m unittest discover -s tools/review-gallery -p test_build.py -v`
qua **8/8 test**; `node --check tools/review-gallery/serve.mjs` qua.
Harness HTTP qua root/cổng mặc định và cũ, Range, HEAD, lỗi URL, traversal và symlink.
Harness phát video qua: không tự phát, rê chuột/rời chuột, đổi clip, mở/đóng khung lớn,
tối đa một video phát. CSS và NOTE/STONE đã được so bằng mã với bản gốc.

Hai dòng tổng từ đối chiếu HTML:

```text
Mẫu trước sửa: 246 việc video; 345 bản; 152 ảnh; in=224, out=21, no=1.
Bản mới, cùng dữ liệu mẫu: 246 việc video; 345 bản; 152 ảnh; in=224, out=21, no=1.
```

Cả **246 thẻ** khớp thứ tự, ID, `data-state` và nhóm; HTML không chứa `/Volumes`.
Trong lúc làm có thêm hai ảnh vào sprint: lần chạy trực tiếp sau sửa thấy 154 ảnh.
Để so đúng dữ liệu bước 0, bản đối chiếu dùng danh mục trong HTML mẫu, tạo symlink
tạm tới chính các file gốc. Không sửa hoặc chép nội dung media.
Mẫu, bản mới và mã so sánh nằm tại `/private/tmp/review-gallery-310-_at6c50l/`
(`baseline.html`, `frozen.html`, `compare.py`, `comparison.json`).
Mọi lần chạy CLI đều truyền `--out` vào thư mục tạm.

Chưa kiểm HTTP qua cổng thật: sandbox trả `listen EPERM` tại `127.0.0.1`;
harness chạy handler thật với phần nghe cổng được mô phỏng. Không còn máy chủ chạy.
Không sửa trang của anh, `.claude/launch.json` hay file game; không chạy build/test game.
Anh cần đổi đường dẫn mục `review-gallery` trong `.claude/launch.json` từ scratchpad
sang `tools/review-gallery/serve.mjs`, theo README. Đợt 05/11 cần truyền file notes mẫu.
