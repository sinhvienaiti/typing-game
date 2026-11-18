# Phiếu 431b — Phân cảnh 5 tuyệt kỹ còn lại

Ngày: 17/11/2026. Trạng thái: **đủ 5 hệ, đã ghép bảng để owner xem**. Tiếp phiếu 431 theo chỉ định làm tiếp trong phiếu 431b; không mở thêm vòng thiết kế.

## Giao nộp

Thư mục ảnh: `games/immortality-cultivation/art-src/concept/ult-storyboards/`.

| Hệ | Bản đưa vào bảng ghép | Nội dung bốn khung |
|---|---|---|
| Tinh Tú | `star-storyboard.v1-try1.png` | Chòm sao trên không → sao băng chéo bắn tỉa → nổ tinh thể kim cương → bụi sao tan. |
| Quang | `light-storyboard.v1-try1.png` | Nâng thấu kính → tia từ thấu kính mở quạt → tia hội tụ kết đòn → ánh vàng tan. |
| Phong | `wind-storyboard.v1-try2.png` | Tụ lưỡi gió bên trái → lưỡi trăng khuyết quét ngang → lưỡi lớn kéo quái sang phải → quái còn dồn bên phải. |
| Thổ | `earth-storyboard.v1-try2.png` | Nứt thẳng phía trước người tung → gai đá nối tiếp trên cùng đường → tảng lớn cuối đường hất quái → hàng đá hạ xuống, còn sẹo thẳng. |
| Băng | `ice-storyboard.v1-try1.png` | Mảnh băng tụ trên không → bão mảnh băng rơi phủ vùng → vỏ băng quanh quái vỡ → mảnh vụn và sương tan. |

- `ult-storyboards-431b.jpg`: **4656×2080**, hàng trên **Tinh Tú · Quang · Phong**, hàng dưới **Thổ · Băng · ô trống**; không chèn chữ.
- `ult-storyboards-431b.prompt.txt`: thứ tự đọc và lệnh ImageMagick thực tế để ghép; không gọi sinh ảnh thêm.
- Mỗi PNG **1536×1024**, bốn khung 2×2: **trên trái → trên phải → dưới trái → dưới phải** tương ứng **tụ lực → phát chiêu → trúng đòn → dư âm**.
- Giữ cả `wind-storyboard.v1-try1.png` và `earth-storyboard.v1-try1.png`. Lượt 2 nới khoảng trống, giữ trọn lưỡi gió, đàn quái và đỉnh đá trong khung. Mỗi ảnh có nguyên văn prompt cạnh ảnh dưới tên tương ứng `.prompt.txt`.

## Công cụ và tham chiếu

Đã dùng **image_gen tích hợp 7/10 lần**: Tinh Tú 1, Quang 1, Phong 2, Thổ 2, Băng 1. Chép nguyên PNG công cụ sinh; chỉ bảng JPEG được ghép bằng ImageMagick, không cắt hoặc vẽ lại nội dung.

Mọi lần đều thực sự đưa hai ảnh tham chiếu vào công cụ, đã xem trước khi sinh; đường dẫn tuyệt đối được ghi trong từng prompt:

1. `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: phong cách, sân đá, góc nhìn, người áo trắng quay lưng và đàn quái.
2. `games/immortality-cultivation/art-src/concept/ult-<hệ>/ult-<hệ>-moment-a.v1-try1.png`, với `<hệ>` là `star`, `light`, `wind`, `earth`, `ice`: chỉ màu và chất liệu, bỏ bố cục vòng tròn của ảnh cũ.

Không dùng ảnh bên thứ ba. Đây là minh họa phân cảnh theo `ULT_CHOREOGRAPHY.md`, chưa phải thành phần VFX để đưa vào game.

## Kiểm tra và điểm owner cần xem

Đã xem trực tiếp cả bảy ảnh sinh và bảng ghép; kiểm kích thước, đủ prompt, đối chiếu bản sao với PNG gốc. Năm bản chọn có người áo trắng quay lưng, đàn quái phía trước và sân đá nhìn chéo xuống; không thấy chữ, watermark hoặc vòng tròn mọc từ đất. Góc khoảng 55° được yêu cầu và kiểm bằng mắt, không phải thông số camera được đo.

Owner xem cách ra chiêu và sức nặng ở khung trúng đòn, nhất là hướng kéo ngang của Phong và nhịp gai đá nối tiếp của Thổ. Ảnh tĩnh chỉ gợi chuyển động; chưa chứng minh được thời gian quét, thứ tự trúng đòn hay tiếng băng vỡ đồng loạt. Tinh Tú có vài điểm sáng còn khá rõ ở dư âm; owner xem độ tan mong muốn khi dựng.

Chưa chấm mù hoặc nghiệm thu 8,5 trong bản chơi. Không làm code, video, âm thanh, build hoặc bộ kiểm thử vì ngoài phạm vi. Không sửa tài liệu thiết kế Tu Tiên, không ghi đè/xóa ảnh có sẵn, không đổi nhánh hoặc thực hiện lệnh Git ghi dữ liệu. Không gặp giới hạn công cụ; không có phần bắt buộc nào còn thiếu.
