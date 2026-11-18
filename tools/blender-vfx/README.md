# Hai mẫu chất liệu Blender · D1

Chỉ gửi việc cho `render-service.sh` đang chạy ngoài sandbox. Không gọi Blender trực tiếp trong Codex.

- `spark_burst.py`: hit ngà/ngọc, 16 khung, seed 71101.
- `ink_smoke.py`: khói mực, 36 khung, seed 71102. Khối thể tích nhiễu giới hạn thay Mantaflow để giữ chi phí nhỏ; chưa phải mô phỏng thủy động lực.
- `common.py`: camera 55°, PNG RGBA, cấu hình EEVEE và compositor Blender 5.2; mặc định 512 px, 24 fps.
- `finish_samples.py`: MP4 nền đen, tấm 6 khung trên nền đen/sáng, phép đo alpha. `--flipbook` gọi `tools/vfx-flipbook/vfxflip/atlas.py` trực tiếp để giữ alpha gốc của khói đen.

Yêu cầu là file `.local/blender-queue/<tên-mới>.req`, ví dụ:

```text
tools/blender-vfx/spark_burst.py
.local/blender-samples/beast-hit-spark-burst
VFX_ENGINE=BLENDER_EEVEE
```

Thử nhỏ thêm `VFX_SIZE=64` và `VFX_TEST_FRAMES=2,5,10`; thư mục ra phải riêng với bản đủ. Đợi `.done` và đọc `.log` mỗi 10 giây. Blender có thể trả mã 0 khi Python lỗi, vì vậy phải kiểm tra cả traceback, `render.json` và số PNG.

Đóng gói:

```sh
tools/vfx-flipbook/.venv/bin/python tools/blender-vfx/finish_samples.py .local/blender-samples/beast-hit-spark-burst
```

Tham số nghệ thuật nằm đầu mỗi script. Dùng cùng Blender, engine, script và seed để chạy lại; `render.json` ghi hash nguồn và thời gian từng khung. Thư mục cấu hình và tệp tạm được đặt trong `.local/blender-home/` bởi `common.py`. Không chạy build hoặc test game, không chuyển sang `art-src`.

Mọi hình xuất có `.prompt.txt` đi kèm, ghi đúng ảnh khung cũ trong repo được dùng làm tham chiếu. Tấm đen lấy các khung tại 10, 25, 40, 55, 70, 90% theo cách chọn của làn C. Mẫu hit rất ngắn nên các ô cuối có thể trống: đó là nhịp tắt đã yêu cầu.
