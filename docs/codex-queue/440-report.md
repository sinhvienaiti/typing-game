# Phiếu 440 — Ảnh tĩnh nổ ánh sáng lăng kính

Ngày: 17/11/2026. Đã dùng đúng **4 lượt `image_gen`**, mỗi biến thể một lượt, theo phiếu đã có phản biện PASS (Sonnet, vòng 3). Đây là bộ ảnh nguồn chờ owner chọn cho bước image-to-video.

## Đã tạo

Thư mục: `games/immortality-cultivation/art-src/lab/vfx/light/stills-55/`.

| Nhãn | Ảnh | Prompt nguyên văn | Dáng |
| --- | --- | --- | --- |
| A | `light-prism-burst.v1-try1.png` | `light-prism-burst.v1-try1.prompt.txt` | Tia sao nghiêng, bung ngang; nhiều tia phụ |
| B | `light-prism-burst.v1-try2.png` | `light-prism-burst.v1-try2.prompt.txt` | Bùng sáng dọc từ chân nhỏ |
| C | `light-prism-burst.v1-try3.png` | `light-prism-burst.v1-try3.prompt.txt` | Hoa ánh sáng xòe thấp, bè ngang |
| D | `light-prism-burst.v1-try4.png` | `light-prism-burst.v1-try4.prompt.txt` | Cầu năng lượng vỡ thành mảnh lăng kính |

Tờ ghép có nhãn A–D: [light-prism-burst-440.jpg](/private/tmp/typing-game-440/light-prism-burst-440.jpg). Dùng vị trí dự phòng của phiếu vì quyền ghi hiện tại không bao gồm thư mục `typing-game-review`.

Số kiểm tra và thông số đóng gói: [440-metrics.json](/private/tmp/typing-game-440/440-metrics.json). Thư mục tạm có `ABOUT.md`.

## Tham chiếu và xử lý

Đã xem và gửi kèm đúng hai ảnh của dự án vào cả bốn lượt tạo:

- `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`: lấy cú nổ tại điểm trúng trong ô dưới trái.
- `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png`: lấy vàng ấm, lõi trắng, chất tia hổ phách và kim tuyến.

Đường dẫn tuyệt đối và vai trò từng ảnh được ghi trong mỗi `.prompt.txt`. Không dùng ảnh bên thứ ba hoặc ảnh game khác. Chọn `image_gen` để vẽ hình, chất sáng và hạt của thành phần tĩnh theo công cụ mà phiếu chỉ định. Hai mẫu A/B được hiển thị trước khi tạo C/D.

Công cụ trả ảnh gốc 1254×1254. ImageMagick chỉ đóng gói: đưa nhiễu nền dưới ngưỡng 1% về đen, thu đồng tỷ lệ và dịch toàn bộ ảnh lên canvas đen 1024×1024. Không vẽ thêm thành phần, không kéo giãn hình, không cắt tia. Đưa chấm hội tụ đã xác định trên ảnh gốc về (512, 635), tương ứng 62,01% chiều cao. Ảnh gốc vẫn giữ nguyên trong `/Users/toandx/.codex/generated_images/01a1e8e2-56ff-79d2-ae99-ea2176eaf056/`; tên tệp và phép biến đổi được ghi trong JSON.

## Kiểm tra ảnh giao

Tọa độ tính từ góc trên trái, bao cả pixel sáng rất yếu sau đóng gói:

| Mẫu | Khung bao phần khác đen (x₀, y₀)–(x₁, y₁) | Bề ngang | Tỷ lệ trắng¹ |
| --- | --- | --- | --- |
| A | (143, 280)–(866, 774) | 70,70% | 1,30% |
| B | (210, 146)–(805, 744) | 58,20% | 1,35% |
| C | (148, 295)–(878, 716) | 71,39% | 1,23% |
| D | (148, 187)–(880, 766) | 71,58% | 2,32% |

¹ Pixel trắng: cả ba kênh RGB ≥ 230; mẫu số là pixel có ít nhất một kênh > 16. Đây là kiểm tra vùng trắng, không phải điểm chất lượng mỹ thuật.

Cả bốn là PNG RGB 1024×1024; mọi pixel ngoài vùng x/y = 123…900 đều RGB(0,0,0). Phần trên chân nổ cao dưới 50% khung, tia văng phía dưới dừng trước 88%. Đã xem ảnh nguồn và tờ ghép cuối: mỗi ảnh có một cú nổ, lõi nhỏ, quầng vàng, tia có vệt và hạt lấp lánh; không có cảnh, mặt đất, nhân vật, quái, chữ, mandala hay vòng tròn đồng tâm.

**Điểm cần owner xem:** A có nhiều tia phụ nên tám cánh chính chưa tách bạch hoàn toàn; giữ nguyên mẫu và ghi nhận hạn chế, không tạo lại vượt giới hạn một lượt mỗi biến thể. D thể hiện mảnh lăng kính rõ nhất; C thấp và xòe ngang rõ nhất. Góc 55° là định hướng phối cảnh của ảnh, chưa được kiểm chứng trong cảnh chơi. Owner chọn mẫu trước khi chuyển sang Firefly. Bộ này chỉ được kiểm tra độ phù hợp làm ảnh nguồn, chưa nghiệm thu hiệu ứng tổng hợp trong game.

## Không thực hiện

Không tạo video, âm thanh hay gắn runtime vì phiếu chỉ làm bước 1. Không sửa code, chạy build/test của game, đổi nhánh, commit, push, xóa hoặc ghi đè ảnh có sẵn. Không sửa tài liệu Tu Tiên hay các đường dẫn ngoài phạm vi phiếu. Không gặp giới hạn công cụ.
