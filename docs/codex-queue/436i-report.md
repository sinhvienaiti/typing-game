# Phiếu 436i — v5B, chỉ sửa tay và ngón

Ngày thực hiện: 18/11/2026. Công cụ: `image_gen` tích hợp, **1/2 lần gọi**. Không gặp giới hạn dịch vụ. Giữ bản sửa đầu; không dùng lượt thứ hai vì tay nghiêng đã về cạnh hông và ngón tay nhìn rõ hơn, tránh thêm một lượt tái sinh làm lệch mẫu đã chọn.

## Tệp giao

- Ảnh: [base-body.v5B-turn.v2-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/base-body.v5B-turn.v2-try1.png).
- Prompt nguyên văn: [base-body.v5B-turn.v2-try1.prompt.txt](../../games/immortality-cultivation/art-src/heroine/fashion/base-body.v5B-turn.v2-try1.prompt.txt).
- **Tờ so sánh đã kiểm tra:** [heroine-base-v5b-436i.jpg](/private/tmp/typing-game-436i/final/heroine-base-v5b-436i.jpg), 3072 × 1416 px, hai cột **v1 | v2**, bên dưới là năm bàn tay nhìn thấy được ở mỗi bản.
- [measurements.json](/private/tmp/typing-game-436i/measurements.json): hộp bao, tọa độ vai/cổ tay và góc đo của cả nguồn lẫn bản sửa. [ABOUT.md](/private/tmp/typing-game-436i/ABOUT.md) ghi mục đích thư mục.

Ảnh đầu vào duy nhất: `games/immortality-cultivation/art-src/heroine/fashion/base-body.v5B-turn.v1-try2.png`. Đã mở kiểm tra rồi nạp trực tiếp làm ảnh **edit**, ghi đường dẫn tuyệt đối vào prompt. Không dùng ảnh khác hoặc ảnh bên thứ ba. PNG giao giữ nguyên đầu ra công cụ, không tô sửa hay ghép lại nhân vật bằng hậu kỳ.

Thư mục review nằm ngoài các gốc được phép ghi của phiên, nên dùng vị trí dự phòng phiếu cho phép; không sửa chỉ mục review. Tờ nháp cùng tên ở cấp trên `/private/tmp/typing-game-436i/` có lỗi cắt ô phóng to do thiết lập gravity của ImageMagick; **chỉ dùng bản trong `final/`**. Giữ nguyên tờ nháp theo ràng buộc không xoá/ghi đè ảnh. Tệp `side-hand-try1.png` cùng cấp là ô tay nghiêng phóng to phục vụ kiểm tra.

## Số đo

Đo ngay sau lượt sửa trên PNG **1536 × 1024**. Góc là đường **tâm vai → cổ tay** so với phương thẳng đứng hướng xuống, đo trên mặt phẳng ảnh; trái/phải tính theo phía người xem. Mốc chọn bằng mắt, góc có sai số khoảng ±3°. Hộp bao dùng điểm có chênh lệch kênh RGB >14 hoặc kênh lớn nhất <80, chia vùng trước x=0–599, nghiêng x=600–929, sau x=930–1535. Chiều cao gồm búi tóc đến bàn chân; biên khử răng cưa gây sai số khoảng ±2 px. Lề là khoảng cách đến mép ngoài toàn ảnh.

| Ảnh | Tay trước trái/phải | Tay nghiêng gần, góc chiếu 2D | Tay sau trái/phải | Cao trước/nghiêng/sau (px) | Lề nhỏ nhất (px) |
| --- | --- | --- | --- | --- | --- |
| v1-try2 — nguồn | 38,0° / 38,2° | 40,2° — vươn ra trước | 38,4° / 38,1° | 901 / 895 / 897 | 49 |
| v2-try1 — bản sửa | 38,4° / 38,0° | 0,6° — chiếu xuống cạnh hông | 38,4° / 38,1° | 900 / 894 / 897 | 48 |

| Ảnh | Hộp bao trước (x1,y1,x2,y2) | Hộp bao nghiêng | Hộp bao sau |
| --- | --- | --- | --- |
| v1-try2 | 59,49,583,949 | 663,50,917,944 | 955,49,1472,945 |
| v2-try1 | 59,49,583,948 | 663,50,818,943 | 953,48,1474,944 |

**Không so góc nghiêng 0,6° trực tiếp với góc mở 38° ở hình trước/sau.** Trong profile thật, tay mở sang hai bên theo chiều sâu bị thu ngắn, hình chiếu gần thẳng đứng. Cổ tay nghiêng chuyển từ (873,419) về (727,445), vai gần (725,246); cánh tay che eo/hông thay vì tạo đường chéo ra trước bụng. Ảnh 2D không đủ xác nhận chính xác góc mở trong không gian hoặc tay xa đang bị che.

## Kiểm tra và điểm chủ dự án cần xem

- Hình trước và sau giữ dáng A; năm bàn tay lộ ra đều đọc được một ngón cái và bốn ngón còn lại, các ngón duỗi và có khe rõ hơn nguồn. Không xác nhận bàn tay xa bị che ở góc nghiêng.
- Tay nghiêng ở cạnh hông đúng hướng sửa. Các ngón nằm trước da đùi/hông: khe được đọc qua phần da phía sau và bóng giữa ngón, **không phải khe nền xám xuyên qua**. Chủ dự án nên xem ô phóng to này trước bước Tripo.
- Mặt, tóc, biểu cảm, thân, tỷ lệ, đồ liền thân, nền, ánh sáng và vị trí ba hình nhìn ổn định khi đặt cạnh nguồn; chiều cao mỗi hình chỉ lệch 0–1 px. Đây là kiểm tra thị giác, không phải cam kết các vùng ngoài tay giữ nguyên từng pixel sau chỉnh sửa bằng mô hình sinh ảnh.
- Không tự chấm sức hút, không tuyên bố đạt chấm mù hoặc đã kiểm chứng rig/3D.

## Phần không làm

Không tạo `v2-try2` vì lượt đầu đã xử lý đúng hướng sửa. Không mở lại thiết kế mặt/dáng, không sửa chân, tóc hay sức hút. Không dựng Tripo vì phiếu này chỉ giao ảnh, số đo và so sánh. Không sửa code, tài liệu game hoặc tệp phối hợp; không chạy build/test, làm video, xoá/ghi đè ảnh nguồn, đổi nhánh hay thực hiện lệnh Git ghi.
