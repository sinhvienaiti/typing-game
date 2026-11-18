# Phiếu 452a — Chòm Bắc Đẩu trên trời

**Ngày:** 18/11/2026. **Trạng thái:** đã tạo đủ hai phương án để owner chọn; chưa đạt toàn bộ ràng buộc kỹ thuật của nguồn ảnh.

## Đã làm

- Dùng công cụ tích hợp `image_gen` đúng **2 lần**, mỗi lần một biến thể, nạp đủ ba ảnh tham chiếu của dự án được chỉ định trong phiếu. Không dùng ảnh bên thứ ba.
- Hai PNG gốc đều **1536×1024**, được sao chép nguyên tệp từ kết quả công cụ, không chỉnh sửa hình, không ghi đè ảnh có sẵn:
  - A: `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/star-constellation.v1-try1.png` — tinh vân tím chàm mỏng bám dải nối.
  - B: `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/star-constellation.v1-try2.png` — không tinh vân, có bảy hoạ tiết triện hình học nhỏ bên các nút.
- Prompt nguyên văn nằm cạnh từng PNG: `star-constellation.v1-try1.prompt.txt`, `star-constellation.v1-try2.prompt.txt`. Mỗi prompt ghi đủ đường dẫn và vai trò của cả ba ảnh tham chiếu.
- Tờ ghép có nhãn A/B: `/private/tmp/typing-game-452/star-constellation-452.jpg` (**3152×1116**). Đã mở kiểm tra tờ ghép. Dùng vị trí dự phòng được phiếu cho phép vì thư mục review trên SSD nằm ngoài vùng sandbox được ghi.

## Kiểm tra nguồn ảnh

| Mục | A | B |
| --- | --- | --- |
| Đúng bảy nút, bốn sao làm gàu và ba sao làm cán | Có | Có |
| Dao Quang ở cuối cán lớn hơn các nút khác | Có, quan sát trực tiếp | Có, quan sát trực tiếp |
| Nhìn vuông mặt phẳng, không phối cảnh hoặc elip | Có | Có |
| Một thành phần, không đất, quái, người hoặc chữ đọc được | Có | Có |
| Biến thể đúng yêu cầu | Có tinh vân mỏng | Có triện hình học, không tinh vân |
| Toàn bộ phần sáng trong vùng 10–90% | **Chưa đạt** | **Chưa đạt** |
| Nền đen tuyệt đối RGB (0,0,0) | **Chưa đạt tuyệt đối** | **Chưa đạt tuyệt đối** |

Đo trên PNG nguyên bản bằng ImageMagick, lấy pixel có kênh RGB lớn nhất **>16/255** để phân biệt phần sáng rõ với nhiễu nền:

- A: hộp phần sáng x **11,26–92,12%**, y **24,41–68,55%**; có **558 pixel** ngoài vùng 10–90%.
- B: hộp phần sáng x **10,09–93,16%**, y **21,68–71,88%**; có **2.675 pixel** ngoài vùng 10–90%. Hoạ tiết bên Dao Quang vượt lề rõ hơn A.
- Ở ngưỡng >0, cả hai ảnh đều có nhiễu rất tối tới mép khung. Góc trên trái là RGB (1,0,0), góc dưới phải (0,1,0), nên không thể ghi nhận nền đen tuyệt đối dù mắt thường thấy đen.

Dải nối đọc thành năng lượng vàng có thân và hạt, nhưng còn các sợi sáng mảnh bên trong. Độ dày dải, tỷ lệ lõi trắng ≤30% và mức tăng đường kính Dao Quang khoảng 1,4 lần chưa được đo riêng; owner cần xem ở bản PNG đầy đủ trước khi chọn. Không chấm điểm hay tuyên bố nghiệm thu hiệu ứng trong game từ hai ảnh nguồn này.

## Chưa làm và việc owner cần xem

- Owner xem tờ A/B để chọn chất liệu: A có tím chàm, B thiên vàng với triện cổ. Cả hai hiện là mẫu lựa chọn, còn lỗi lề phải và nền cần xử lý trước khi dùng làm nguồn video.
- Không tạo lần thứ ba, không thu nhỏ, cắt, lọc nền hoặc vẽ sửa ảnh để che lỗi: phiếu yêu cầu đúng hai lần tạo và giữ ảnh gốc.
- Không làm video Firefly, không gắn vào lab hoặc runtime; các bước này nằm sau lựa chọn của owner và ngoài phiếu.
- Không sửa code, không chạy build hay bộ kiểm thử game, không sửa tài liệu Tu Tiên, không đổi nhánh hoặc thực hiện thao tác Git bị cấm.
- Không cập nhật chỉ mục review: tờ ghép nằm ở thư mục dự phòng `/private/tmp/typing-game-452/`, chưa được đưa vào cây review trên SSD. Có `ABOUT.md` tại thư mục dự phòng.
- Không gặp giới hạn công cụ. Tại lúc đọc quota: cửa sổ ngắn đã dùng 1%, cửa sổ tuần đã dùng 0%; phiếu này chỉ tạo ảnh.
