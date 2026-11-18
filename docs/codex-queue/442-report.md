# Phiếu 442 — Ảnh tĩnh tia sét năng lượng dày

Ngày: 17/11/2026. Đã dùng đúng **4 lượt `image_gen`**, mỗi biến thể một lượt, theo phiếu có phản biện PASS (Sonnet, 17/11). Bộ ảnh nguồn chờ owner chọn trước bước Firefly image-to-video. **A/B có sai lệch vị trí chấm đáy: khoảng 76% thay vì 80%; chưa đạt đầy đủ vị trí neo của phiếu.**

## Đã tạo

Thư mục: `games/immortality-cultivation/art-src/lab/vfx/thunder/stills-55/`.

| Nhãn | Ảnh | Prompt nguyên văn | Hình dạng |
| --- | --- | --- | --- |
| A | `thunder-bolt-thick.v1-try1.png` | `thunder-bolt-thick.v1-try1.prompt.txt` | Cú sét lớn đi xuống, thân năng lượng dày, nhánh tỏa hai bên, bùng sáng ở chân |
| B | `thunder-bolt-thick.v1-try2.png` | `thunder-bolt-thick.v1-try2.prompt.txt` | Hai dòng sét xoắn thành một thân, có khe tím tối giữa các luồng |
| C | `thunder-bolt-thick.v1-try3.png` | `thunder-bolt-thick.v1-try3.prompt.txt` | Một đoạn sét nối ngang nghiêng phối cảnh, hai chấm neo sáng |
| D | `thunder-bolt-thick.v1-try4.png` | `thunder-bolt-thick.v1-try4.prompt.txt` | Dải plasma nối ngang, thân bè và cuộn sóng rõ hơn C |

Tờ chọn có nhãn A–D: [thunder-bolt-thick-442.jpg](/private/tmp/typing-game-442/thunder-bolt-thick-442.jpg). Dùng đường dẫn dự phòng của phiếu vì quyền ghi phiên này không bao gồm thư mục `typing-game-review`; không thử ghi vượt sandbox.

Đối chiếu ảnh gốc và ảnh đóng gói: [442-source-packaging.jpg](/private/tmp/typing-game-442/442-source-packaging.jpg). Thông số, phép biến đổi và SHA-256: [442-metrics.json](/private/tmp/typing-game-442/442-metrics.json). Thư mục tạm có `ABOUT.md`.

## Tham chiếu và xử lý

Đã mở xem và gửi kèm đúng hai ảnh dự án trong cả bốn lượt:

- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: chỉ lấy nửa phải cho màu tím, chất năng lượng, phân nhánh và cú sét lớn ở ô dưới trái của nửa phải.
- `games/immortality-cultivation/art-src/lab/vfx/light/stills-55/light-prism-burst.v1-try4.png`: lấy cách trình bày một thành phần trên nền đen, lề và chấm neo sáng; không lấy hình nổ lăng kính màu vàng.

Đường dẫn tuyệt đối và vai trò từng tham chiếu có trong mỗi prompt. Không dùng ảnh bên thứ ba hoặc ảnh game khác. Dùng `image_gen` theo công cụ đã chốt trong phiếu để vẽ hình, quầng và hạt; không mở thêm vòng thiết kế hoặc giao agent. Hai mẫu A/B đã được hiển thị và xem trước khi tạo C/D.

Công cụ trả bốn ảnh gốc **1254×1254**. ImageMagick đưa nền dưới ngưỡng 0,8% về đen, thu đồng tỷ lệ và dịch toàn ảnh vào canvas đen **1024×1024**; không cắt tia, kéo giãn, xoay hoặc vẽ thêm chi tiết. Giữ nguyên ảnh gốc trong `/Users/toandx/.codex/generated_images/01a1e997-bb14-7fb3-9995-de7542c9d465/`; tên tệp và phép biến đổi nằm trong JSON. Mọi tệp giao trong repo được ghi qua đường dẫn `/Volumes/SS990TPRO/htdocs/typing-game`.

## Kiểm tra nguồn

Đã xem bốn ảnh sinh và tờ ghép cuối. Mỗi ảnh có một thành phần năng lượng tím, lõi trắng tím nhỏ hơn thân/quầng, nhánh phụ và hạt điện. A/B có khoảng bảy đến tám nhánh lớn nhìn thấy; C/D có hai chấm neo. Không thấy mặt đất, quái, nhân vật, mây, chữ, vòng tròn hoặc mandala.

| Mẫu | Khung bao mọi pixel khác đen, từ góc trên trái | Pixel trắng¹ | Chấm đáy ước lượng |
| --- | --- | --- | --- |
| A | (220, 133)–(804, 887) | 3,47% | (528, 779), y = 76,10% |
| B | (224, 133)–(801, 886) | 2,76% | (512, 783), y = 76,49% |
| C | (137, 326)–(889, 698) | 2,19% | Hai đầu nối ngang |
| D | (135, 278)–(887, 746) | 2,43% | Hai đầu nối ngang |

¹ Pixel trắng: cả ba kênh RGB ≥230; mẫu số là pixel có maxRGB >16. Đây là phép kiểm vùng trắng của toàn thành phần, không phải phép phân vùng riêng lõi hoặc điểm nghiệm thu mỹ thuật. Cả bốn PNG RGB đều 1024×1024; **0 pixel khác đen ngoài vùng x/y = 123…900**.

**Sai lệch cần owner xem:** A/B có hạt và dư quầng phía dưới chân. Khi thu toàn bộ hình để giữ lề, chân ở khoảng 76%, chưa đúng 80%. Không cắt phần sáng hoặc làm méo ảnh để ép neo. A cũng uốn chữ S khá rõ thay vì đường đánh thẳng cứng. C/D đã có bề dày nhưng dáng cùng họ; D bè và cuộn nhiều lớp hơn. Góc 55° là chỉ dẫn phối cảnh trong prompt, chưa được xác minh trong host chơi. Các bề rộng phần trăm của thân chưa có phép phân vùng riêng để chứng nhận.

Tự đánh giá để owner tham khảo, theo thang 10; không thay giám khảo độc lập:

| Mẫu | Sức hút | Sát phiếu | Dễ đọc ở cỡ nhỏ | Độ sạch |
| --- | --- | --- | --- | --- |
| A | 8,4 | 7,8 | 8,5 | 9,0 |
| B | 8,5 | 7,8 | 8,4 | 9,0 |
| C | 8,2 | 8,2 | 8,5 | 9,0 |
| D | 8,5 | 8,3 | 8,6 | 9,0 |

Đây là mẫu nguồn cho owner chọn, chưa có nghiệm thu hiệu ứng tổng hợp 8,5 trong game. Owner cần chọn hướng cú đánh A/B và hướng nối ngang C/D, đồng thời xem có chấp nhận sai lệch neo A/B hay cần phiếu chỉnh ảnh riêng. Không tự tạo thêm vì đã dùng hết bốn lượt cho phép.

## Không thực hiện

Không tạo video, âm thanh hoặc gắn runtime vì phiếu chỉ làm ảnh tĩnh. Không sửa code, tài liệu Tu Tiên, board hoặc đường dẫn ngoài phạm vi. Không chạy build/test của game, đổi nhánh, commit, push, reset, clean hoặc stash. Không xóa hay ghi đè ảnh có sẵn. Không gặp giới hạn công cụ hoặc thời gian chờ.
