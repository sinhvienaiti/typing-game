# Phiếu 436h — Thân nền nữ chính v5, hai mẫu tăng sức hút

Ngày thực hiện: 18/11/2026. Công cụ: `image_gen` tích hợp, **4/4 lần gọi**, mỗi mẫu một lần đầu và một lần sửa. Không gặp giới hạn dịch vụ.

**Kết quả:** đã tạo đủ hai hướng A/B để owner chọn khí chất. Đề xuất **A lần 2** và **B lần 2**. Cả hai **chưa đạt đủ điều kiện kỹ thuật để gửi Tripo**: A còn tay nghiêng mở thiếu; cả A và B còn khe giữa hình nghiêng và hình sau dưới 60 px. Không tự chấm điểm sức hút hoặc coi đây là kết quả chấm mù.

## Tệp giao

Thư mục ảnh: `games/immortality-cultivation/art-src/heroine/fashion/`.

| Mẫu | Ảnh | Prompt nguyên văn |
| --- | --- | --- |
| A lần 1 | `base-body.v5A-turn.v1-try1.png` | `base-body.v5A-turn.v1-try1.prompt.txt` |
| A lần 2 — đề xuất | `base-body.v5A-turn.v1-try2.png` | `base-body.v5A-turn.v1-try2.prompt.txt` |
| B lần 1 | `base-body.v5B-turn.v1-try1.png` | `base-body.v5B-turn.v1-try1.prompt.txt` |
| B lần 2 — đề xuất | `base-body.v5B-turn.v1-try2.png` | `base-body.v5B-turn.v1-try2.prompt.txt` |

Mọi PNG đều **1536 × 1024**, giữ nguyên đầu ra công cụ; không chỉnh hình thể, đổi bố cục hoặc tô sửa bằng hậu kỳ.

Tờ so sánh: [heroine-base-v5-436h.jpg](/private/tmp/typing-game-436h/heroine-base-v5-436h.jpg), 3072 × 1355 px, ba cột **v4 | v5A lần 2 | v5B lần 2**, mỗi cột có ô mặt phóng to từ khung nguồn 160 × 200 px. Đã mở kiểm tra tờ cuối.

Tệp kèm: [measurements.json](/private/tmp/typing-game-436h/measurements.json) chứa hộp bao, tọa độ vai/cổ tay, hàng đo khe và kết quả từng ảnh; `ABOUT.md` trong cùng thư mục. Dùng vị trí dự phòng được phiếu cho phép vì quyền ghi của phiên này không bao gồm thư mục `typing-game-review`; không sửa chỉ mục review ngoài phạm vi.

## Ảnh đầu vào

Cả bốn lần gọi đều nạp đúng hai ảnh của dự án dưới đây, có đường dẫn tuyệt đối trong từng prompt:

1. `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/heroine/fashion/base-body.v4-turn.v1-try2.png`: tỷ lệ, thân nền, đồ ôm thân và ba góc.
2. `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`: nhận diện gương mặt; không lấy phục trang, trang sức hoặc cảnh nền.

Không đưa ảnh bên thứ ba hoặc ảnh game khác vào công cụ. Các lần sửa vẫn dùng hai ảnh gốc, bổ sung lỗi đo được trong prompt.

## Số đo từng ảnh

Đo trên PNG gốc 1536 × 1024. Góc là đường nối **tâm vai → cổ tay** so với phương thẳng đứng hướng xuống; trái/phải tính theo phía trên ảnh. Mốc khớp được chọn bằng mắt, nên góc là ước lượng, sai số khoảng ±3°. Góc nghiêng chỉ đo tay gần nhìn thấy; tay xa bị che nên không khẳng định đã kiểm tra được cả hai tay.

Hộp bao lấy từ mặt nạ màu bằng ImageMagick và Python chuẩn: điểm có độ chênh kênh RGB >14 hoặc giá trị kênh lớn nhất <80, chia vùng từng hình; kiểm tra lại với ảnh. Chiều cao tính cả búi tóc đến hết bàn chân. Số đo biên/khe có sai số khoảng ±2 px do rìa khử răng cưa. Khe gối đo ở hàng **y=650**, giữa hai chân ở góc trước/sau; góc nghiêng chồng chân theo phối cảnh nên không dùng để đo khe gối. Khe giữa các hình là khoảng trống ngang nhỏ nhất trên cùng một hàng có cả hai hình.

| Ảnh | Tay trước trái/phải | Tay nghiêng | Tay sau trái/phải | Khe gối trước/sau (px) | Cao trước/nghiêng/sau (px) | Lề ngoài nhỏ nhất (px) | Khe trước–nghiêng / nghiêng–sau (px) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A lần 1 | 35,4° / 35,5° | 22,7° | 34,5° / 34,0° | 26 / 26 | 913 / 909 / 911 | 37 | 81 / 43 |
| A lần 2 | 36,0° / 35,2° | 31,0° | 34,3° / 33,8° | 33 / 34 | 903 / 902 / 903 | 44 | 89 / 33 |
| B lần 1 | 37,4° / 36,0° | 30,7° | 35,4° / 33,4° | 29 / 31 | 899 / 898 / 897 | 46 | 76 / 22 |
| B lần 2 | 37,9° / 36,1° | 40,1° | 36,3° / 36,7° | 34 / 34 | 901 / 895 / 897 | 49 | 101 / 43 |

- **A lần 1:** không đạt lề 40 px, tay nghiêng và khe 60 px; đã dùng lượt sửa.
- **A lần 2:** lề và chiều cao đạt; tay nghiêng vẫn thiếu, tay sau sát/dưới ngưỡng 35°, khe nghiêng–sau thiếu. Đã hết lượt của A.
- **B lần 1:** lề và chiều cao đạt; tay nghiêng, một tay sau và khe giữa hình chưa đạt; đã dùng lượt sửa.
- **B lần 2:** các góc tay đo được trong 35–45°, lề đạt, chiều cao gần 900 px, chênh cao ba góc dưới 1%; khe nghiêng–sau vẫn thiếu khoảng 17 px. Đã hết lượt của B.

## Đề xuất và điểm owner cần xem

**A: chọn `base-body.v5A-turn.v1-try2.png` để xem hướng lạnh lùng, cao quý.** Mắt và nét mi sắc hơn v4, môi đào trung tính, biểu cảm điềm tĩnh; búi tóc lớn hơn, eo cao và đường cong rõ hơn. So với A lần 1, lề ngoài đã đủ và tay nghiêng cải thiện. Tuy nhiên, nét lạnh vẫn thiên về điềm tĩnh; owner cần xem mức sức hút này đã đúng ý chưa. Chưa dùng làm nguồn Tripo do các lỗi dáng/khe kể trên.

**B: chọn `base-body.v5B-turn.v1-try2.png` để xem hướng dịu dàng, quyến rũ.** Nụ cười nhẹ và ánh mắt ấm phân biệt rõ với A; giữ vải đặc, kín thân và không trang sức. Lần sửa xử lý tay nghiêng tốt nhất trong bốn ảnh. Đề xuất owner xem B trước nếu ưu tiên biểu cảm có sức hút; đây là nhận xét lựa chọn, không phải điểm chất lượng độc lập. Vẫn cần sửa khe giữa hình trước bước Tripo.

Hai mẫu đều chân trần, đứng khá cân bằng và có khe gối rõ; da ấm hơn, tóc thành khối cao đầy đặn. Một số đường tóc mảnh sát thái dương và biến thiên sáng nhẹ của nền vẫn còn; nhận diện với chân dung gốc, độ quyến rũ và độ khớp mặt/búi tóc giữa góc cần owner cùng vòng chấm độc lập xác nhận. Không coi tỷ lệ 8,5 đầu hoặc tính đối xứng rig là đã được kiểm chứng 3D từ các số đo 2D này.

## Phạm vi đã giữ

Không tạo thêm lần thứ năm, không dựng Tripo, không làm video/âm thanh, không sửa code hoặc tài liệu game, không chạy build/test, không đổi nhánh và không thực hiện lệnh Git ghi. Giữ đủ bốn ảnh và prompt; không ghi đè ảnh nguồn hay ảnh có trước phiên. Không mở thêm vòng nghiên cứu hoặc chấm mù vì phiếu đã chốt hai hướng và chỉ giao tạo mẫu, tự đo, làm tờ so sánh.
