# Phiếu 451c — Ba mẫu bảo kính chiêu Ánh Sáng

Ngày: 18/11/2026. Trạng thái: đã tạo đủ ba mẫu, chờ owner chọn; chưa nghiệm thu mỹ thuật, chưa gửi Tripo.

## Sản phẩm

Thư mục ảnh và prompt: `games/immortality-cultivation/art-src/lab/vfx/light/stills/`.

| Mẫu | Ảnh | Prompt chính xác đã gửi |
| --- | --- | --- |
| A — Nhật Luân Kính | `light-relic-mirror-a.v1-try1.png` | `light-relic-mirror-a.v1-try1.prompt.txt` |
| B — Liên Hoa Kính | `light-relic-mirror-b.v1-try1.png` | `light-relic-mirror-b.v1-try1.prompt.txt` |
| C — Thái Cực Kính | `light-relic-mirror-c.v1-try1.png` | `light-relic-mirror-c.v1-try1.prompt.txt` |

Tờ chọn mẫu: [light-relic-mirror-451c.jpg](/private/tmp/typing-game-451c/light-relic-mirror-451c.jpg). Dùng thư mục dự phòng được phiếu cho phép vì thư mục review trên SSD nằm ngoài vùng được cấp quyền ghi; không sửa chỉ mục review.

## Nguồn và cách tạo

Dùng công cụ tích hợp `image_gen`, đúng **3 lượt**, mỗi lượt một mẫu. Cả ba lượt đều đính kèm đúng hai ảnh riêng của dự án:

- `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png`: chỉ tham chiếu bảng màu và độ bóng kim loại.
- `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ray-a2.v1-try2.png`: chỉ tham chiếu tông vàng hổ phách.

Đường dẫn đầy đủ và vai trò của từng ảnh đều có trong mỗi prompt. Không sử dụng ảnh bên thứ ba hoặc ảnh game khác.

Công cụ trả ảnh 1254×1254 dù prompt yêu cầu 1024×1024. Khi lưu, dùng ImageMagick thu đồng tỷ lệ toàn ảnh xuống 840×840 rồi mở rộng biên bằng màu điểm ảnh mép tới 1024×1024. Không cắt vật thể, không vẽ thêm hoặc sửa hình dáng; phần nền bổ sung là nền xám nối từ mép ảnh. Bản gốc của công cụ được giữ nguyên tại `/Users/toandx/.codex/generated_images/01a1edb4-d030-7bc0-965b-4499d95a3392/`.

## Kiểm tra và phần owner cần xem

Ba PNG đã lưu đều có kích thước 1024×1024, vật thể nằm trọn khung với lề lớn hơn 8%; prompt riêng và tờ ghép đã có. A nhấn vào phượng vàng và hồng ngọc; B vào cánh sen, viền ngọc trai và đài sen nối thân; C vào hai vòng vàng–bạc lệch trục có chốt và ngọc bích ở tâm.

Owner cần chọn A/B/C theo độ sang và sức hút, đồng thời xem kỹ các đầu cánh, cuống đài sen và chốt vòng có phù hợp làm nguồn Tripo. Kết nối mặt sau và độ liền khối 3D chưa thể xác nhận chỉ từ một ảnh 3/4. Mẫu B có bề mặt cánh thiên về ánh xà cừ hơn ngà mờ; cần owner xem có hợp ý không.

Không chấm điểm thay hai giám khảo mù. Chưa làm Tripo vì phiếu chỉ yêu cầu ba phương án để owner chọn. Không sửa code, không làm video, không chạy build hoặc bộ kiểm thử game; không ghi đè ảnh cũ, không commit, không đổi nhánh.

