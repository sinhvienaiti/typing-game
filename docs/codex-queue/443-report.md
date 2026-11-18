# Phiếu 443 — Ba hướng trận pháp trên trời

Đã tạo đủ ba hướng bằng công cụ tích hợp `image_gen`: **6 lượt**, mỗi hướng **2 lượt**, ngày 17/11/2026. Cả sáu ảnh là PNG **1536 × 1024**, một cảnh mỗi ảnh; prompt nguyên văn nằm cạnh từng ảnh. Không ghi đè ảnh có sẵn.

## Tệp giao nộp

Thư mục ảnh: [sky-formation](../../games/immortality-cultivation/art-src/concept/ult-metal/sky-formation/).

| Hướng | Ảnh đầu | Ảnh dùng trong tờ so sánh |
| --- | --- | --- |
| A — Kiếm trận | `sky-formation-a.v1-try1.png` | `sky-formation-a.v1-try2.png` |
| B — Bát quái thiên môn | `sky-formation-b.v1-try1.png` | `sky-formation-b.v1-try2.png` |
| C — Sen vàng | `sky-formation-c.v1-try1.png` | `sky-formation-c.v1-try2.png` |

Mỗi ảnh có tệp cùng tên gốc, đuôi `.prompt.txt`, tổng cộng sáu prompt. Cả hai đường dẫn ảnh tham chiếu được ghi rõ trong từng prompt và được truyền trực tiếp vào công cụ:

- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: chỉ dẫn dùng ô trên trái của nửa trái cho camera, cảnh, chất liệu và sắc vàng.
- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try1.png`: lấy ngôn ngữ chữ cổ, vân mây và quẻ để thiết kế lại thành khối nhiều tầng.

Tờ so sánh có nhãn **A, B, C**, ghép nguyên khung ba ảnh lượt 2, kích thước **4608 × 1096**:

[Mở sky-formation-443.jpg](/private/tmp/typing-game-443/sky-formation-443.jpg).

Đã dùng vị trí dự phòng được phiếu cho phép vì thư mục review trên SSD nằm ngoài vùng sandbox được ghi. Có `ABOUT.md` trong `/private/tmp/typing-game-443/`. Không ghi vào thư mục review hoặc sửa chỉ mục bên ngoài phạm vi phiếu.

## Khác biệt và phần cần owner xem

- **A:** bốn tầng vòng có thân dày, vành ngoài treo nhiều kiếm chĩa xuống. Lượt 2 sửa mép trên sát khung và làm lộ mặt trên các tầng. Phù hợp nhất để nhận diện ngay chiêu Kiếm trận.
- **B:** bốn tầng bát quái có khoảng cách, cửa sáng xuyên tâm làm điểm nhấn. Lượt 2 giữ toàn bộ cấu trúc trong khung và cho thấy mặt trên tầng chính.
- **C:** bốn tầng cánh sen mở, chất năng lượng trong suốt rõ hơn. Lượt 2 chuyển từ vòng trang trí kèm hoa nhỏ sang từng vành cánh sen, tạo hình khác A/B rõ ràng hơn.

Các ảnh đều thể hiện ánh sáng rủ từ trận xuống sân đá, vùng sáng bên dưới và khoảng không giữa trận với đàn quái. Tuy vậy, **A/B vẫn thiên về vàng đúc hơn dải năng lượng**; số kiếm hàng trăm ở A chưa thể xác nhận bằng mắt. C còn nhiều huy hiệu quẻ trên cánh. Khoảng hở từ tầng thấp nhất tới quái có thể cần tăng thêm khi dựng. Owner cần xem các điểm này cùng hình dáng tổng thể trước khi chọn hướng.

Đây là **ảnh ý tưởng để chọn hướng**, chưa phải xác nhận hình học hoặc camera 3D trong game. Prompt yêu cầu camera chếch xuống 55°; không coi ảnh sinh là phép đo góc camera. Chuyển động quay ngược chiều chỉ được gợi bằng vệt khí trong ảnh tĩnh, chưa được kiểm chứng. Chưa có đánh giá mù hoặc nghiệm thu 8,5 cho hiệu ứng trong play host.

## Kiểm tra và phần bỏ qua

Đã xem cả sáu ảnh, kiểm tra kích thước bằng ImageMagick, kiểm tra đủ sáu prompt và xem tờ ghép có đúng thứ tự A/B/C. Ảnh gốc giữ nguyên; tờ ghép chỉ thêm nhãn ngoài khung, không cắt hoặc vẽ lại nội dung.

Không sửa code, không tạo video, không tạo âm thanh, không dựng 3D, không chạy build/test của game; các phần này ngoài phiếu. Không dùng ảnh bên thứ ba hoặc ảnh game khác, không tạo thêm agent, không chạy lệnh Git. Không cần lượt tạo thứ bảy và không có lỗi hạn mức.

**Chờ owner chọn A, B hoặc C và chỉ ra phần muốn giữ/chỉnh trước khi giao việc dựng trận pháp 3D.**
