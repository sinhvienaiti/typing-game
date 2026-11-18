### 07/11/2026 09:54 · S3-1
Đã nối tiếp v1, tạo `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/blender/beast-hit-spark-burst/v2/`: PNG RGBA, MP4 nền đen, hai tấm 6 khung sáng/tối, prompt, script snapshot, `render.json` và `validation.json`.
7 tia chính/quạt 60°, 24 tia phụ, 180 hạt mịn; 32/32 khung khác nhau, 48 fps, 0,667 s, 512²; extent 64,45%, lề ≥44 px, alpha mép/cuối 0; render 8.402 s qua dịch vụ, sau probe nhỏ.
Giữ recipe cũ; thêm `tools/blender-vfx/s3_directional_spark_v2.py` nới máy 5,6→5,66; sửa tràn uint8 trong `s3_finish.py`. MP4 giải mã đủ 32 khung, sai số RGB trung bình 0,075/255 so PNG ghép đen.
Đã xem 4 tấm ghép; nguồn đúng hướng, tách lớp và viền sạch. Anh xem `preview-black.mp4` cùng `sheet-light.jpg`; chưa kiểm phát thời gian thực trong game/chấm 8,5. Không làm S3-2/S3-3, không sửa manifest/mã lab; dừng tại S3-1.

### 07/11/2026 10:02 · S3-2
Đã nối tiếp mẫu cũ, tạo `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/blender/beast-death-ink-smoke/v3/` và `mantaflow-v3-study/`: PNG RGBA, MP4 đen, hai tấm 6 khung sáng/tối, tấm cỡ thân, prompt, snapshot, render/validation/source-check JSON và nhận xét nguồn.
V3 trường nhiễu: 7 sợi cuộn, 48 khung 512²/32 fps/1,5 s; 46 khung có hình đều khác nhau, hai đầu trống chủ ý; lề ≥93 px, alpha mép/cuối 0, render 92,184 s; video giải mã đủ 48 khung, sai số 0,0872/255.
Mantaflow 96: thử nhỏ rồi render đủ 48 khung 192²; bake+render 115.435 s (<10 phút). FAIL hình: vẫn vón cụm ngang, không chọn dù alpha sạch; đã lưu bằng chứng, không bake lô.
Đã xem 9 tấm ghép, kiểm tỷ lệ khói/thân 1,3–1,6 với thân quy ước 64 px trên nền sáng/tối; chưa đo pixel trên quái thật hoặc phát kiểm trong host nên v3 còn NOT-ENOUGH-EVIDENCE cho nghiệm thu tầng A đầy đủ. Anh xem `v3/preview-black.mp4` và `v3/sheet-body-scale.jpg`.
Chỉ làm S3-2; giữ recipe cũ, thêm 2 recipe v3 và `tools/blender-vfx/s3_smoke_check.py`; không làm S3-3, sửa danh sách/manifest/mã lab, mở browser, chạy build/test game hay lệnh git ghi. Dừng tại đây.


### 07/11/2026 10:08 · S3-3
Đã tạo `.local/s3/compare-S3-3/`: 4 tấm sáng/tối (6 khung mỗi bên, bề ngang cực đại 96 px), 2 tấm clip gốc, 2 MP4 tốc độ gốc, prompt, snapshot, `metrics.json`, `verification.json` và `review.md` đủ 5 ô tầng A; script `tools/blender-vfx/s3_compare.py`.
Đối chứng Firefly take1/atlas theo manifest; manifest ghi chưa tích hợp và không thấy hai ID được gọi trong src, nên chưa xác nhận là clip đang dùng trong cảnh lab. Khói atlas tô mực chỉ để kiểm matte, chưa áp shader host.
Tia Blender v2 hơn về hướng lực, tách lớp, lề và nhịp 0,667 s; khói v3 hơn về sợi/khe rỗng và alpha nhưng còn mỏng, xám lam, FAIL phần vật liệu/màu khói mực; chưa thắng Firefly về thể tích/cuộn.
Tầng A tia: PASS 4 ô nguồn, ô cỡ/tốc độ thật NOT-ENOUGH-EVIDENCE; khói: FAIL ô vai trò, PASS ô 2–4, ô 5 thiếu bằng chứng. Đã xem 6/12 ảnh; video giải mã đủ 267 khung/48 fps, không chấm 8,5 hay kết luận thắng composite.
Anh xem hai `compare-light.jpg`/`compare-dark.jpg` và MP4 cùng `review.md`; chưa kiểm host theo ranh giới cấm browser. Không render lại, sửa lab/manifest/danh sách, chạy build/test hay làm S3-4; dừng chờ anh duyệt.
