# Phiếu 446 — Bốn mẫu kiếm năng lượng

Ngày: 18/11/2026. Trạng thái: đã tạo đủ mẫu, chờ owner chọn; chưa nghiệm thu nguồn hoặc tích hợp vào game.

## Sản phẩm

Đã gọi công cụ tích hợp `image_gen` **đúng 4 lần**, một lần cho mỗi biến thể, không tạo lại.

Thư mục ảnh: `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/`.

| Nhãn | Ảnh | Prompt nguyên văn |
| --- | --- | --- |
| A | `energy-sword.v1-try1.png` | `energy-sword.v1-try1.prompt.txt` |
| B | `energy-sword.v1-try2.png` | `energy-sword.v1-try2.prompt.txt` |
| C | `energy-sword.v1-try3.png` | `energy-sword.v1-try3.prompt.txt` |
| D | `energy-sword.v1-try4.png` | `energy-sword.v1-try4.prompt.txt` |

Tờ so sánh: [energy-sword-446.jpg](/private/tmp/typing-game-446/energy-sword-446.jpg), 1440×820, nhãn A–D và một hàng thân kiếm cao khoảng 30 px trên nền đá tối. Có `ABOUT.md` cùng thư mục. Dùng đường dẫn dự phòng vì thư mục review bên cạnh repo nằm ngoài quyền ghi của sandbox; chưa cập nhật chỉ mục review.

## Tham chiếu và xử lý

Cả bốn lần đều truyền trực tiếp đúng hai ảnh của phiếu vào `referenced_image_paths`; đường dẫn tuyệt đối và vai trò từng ảnh đã ghi trong mỗi prompt:

- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/sword-fall-streak.v1-try1.png`: dáng kiếm và vàng ấm; thay vật liệu đặc bằng năng lượng.
- `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png`: bảng màu và khí sáng tương thích vệt D.

Công cụ trả ảnh 1254×1254. Dùng ImageMagick 7 thu về **1024×1024**, đặt các kênh ≤1,2% về đen để làm sạch nền; không vẽ thêm hình, đổi silhouette hay cắt khí. Các ảnh gốc trong thư mục mặc định của công cụ được giữ nguyên.

Riêng nền hàng kiểm tra dùng ảnh nội bộ Tu Tiên `games/immortality-cultivation/art-src/ground/thanh-thach/court-paving.v2.png`, giảm sáng còn 28%; chỉ ghép cục bộ, không gửi ảnh nền này vào công cụ AI. Ghép kiếm bằng Screen. Font: `/System/Library/Fonts/Supplemental/Arial.ttf`.

## Kiểm tra và điểm cần owner xem

Cả bốn ảnh: một thanh kiếm hướng mũi xuống, thân vàng trong mờ, lõi sáng, nền đen, không chữ và không vòng. Ở hàng 30 px vẫn nhận ra mũi kiếm và đốc chắn ngang; khác biệt chất liệu giữa các mẫu giảm rõ khi thu nhỏ. A và B đọc hình tốt nhất.

Đo thân sáng bằng thành phần liên thông lớn nhất tại ngưỡng kênh RGB lớn nhất >160/255, bỏ các hạt rời. Đo lề toàn hiệu ứng tại ngưỡng >16/255. Các ngưỡng này chỉ hỗ trợ kiểm tra bố cục, không thay nghiệm thu thị giác.

| Mẫu | Chiều cao thân sáng | Lề nhỏ nhất, kể cả khí/hạt | Nhận xét |
| --- | --- | --- | --- |
| A | 656 px — 64,1% | 148 px — 14,5% | Gọn và sắc; vẫn có sợi khí chéo trong lưỡi. |
| B | 658 px — 64,3% | 148 px — 14,5% | Hai sợi khí lượn nhẹ rõ nhất ở ảnh lớn. |
| C | 591 px — 57,7% | 142 px — 13,9% | Thân ngắn hơn mức 60%; khí phía trên làm tổng vùng sáng cao 71,1%. Cạnh pha lê chưa khác biệt mạnh với A/B. |
| D | 618 px — 60,4% | 89 px — 8,7% | Hạt khí phía trên vượt yêu cầu lề 12%; tổng vùng sáng cao 77,0%. Chuôi còn khá sắc, độ tan khí chưa mạnh. |

Tự chấm để tham khảo, không phải điểm nghiệm thu trong play host:

| Mẫu | Hấp dẫn /10 | Đúng brief /10 | Đọc ở 30 px /10 | Sạch ảnh /10 |
| --- | --- | --- | --- | --- |
| A | 8,2 | 8,3 | 8,2 | 9,0 |
| B | 8,3 | 8,4 | 8,1 | 9,0 |
| C | 7,9 | 7,4 | 8,0 | 8,8 |
| D | 7,8 | 6,8 | 8,0 | 8,5 |

**Owner cần xem tờ ghép ở 100% và chọn mẫu. C và D có sai lệch bố cục nêu trên, chưa đạt đầy đủ brief.** Không tạo thêm để giữ đúng giới hạn bốn lần; không tự coi các mẫu là đã được duyệt.

## Phạm vi và phần chưa làm

Không sửa code, không làm video, không chạy build hoặc bộ test của game. Không đổi nhánh, commit hoặc chạy các thao tác Git bị cấm. Không dùng ảnh game khác hoặc ảnh bên thứ ba. Không ghi đè hay xóa ảnh đã có trước phiếu.

Chưa gắn sprite hoặc vệt D vào runtime, chưa thay mô hình Tripo và chưa chấm hiệu ứng tổng hợp trong play host: các bước này nằm sau quyết định của owner và ngoài phạm vi phiếu.
