# Phiếu 449 — Viền sáng tĩnh quanh lõi Hư Không

Ngày thực hiện: 18/11/2026. Phiếu có phản biện PASS (Sonnet, 18/11). Đã gọi công cụ tích hợp `image_gen` đúng **3 lần**, A–C mỗi biến thể một lần, cả ba đều trả ảnh thành công. Đã tạo đủ bộ mẫu và tờ ghép; **chưa đạt toàn bộ yêu cầu hình học chính xác**, chi tiết bên dưới. Chờ owner chọn, chưa tích hợp hoặc nghiệm thu trong game.

## Tệp đã tạo

Thư mục: `games/immortality-cultivation/art-src/concept/ult-void/blackhole/`.

| Mẫu | Ảnh PNG 1024×1024 | Prompt nguyên văn |
| --- | --- | --- |
| A — Viền nhật hoa đều, mảnh | `void-core-rim.v1-try1.png` | `void-core-rim.v1-try1.prompt.txt` |
| B — Sáng lệch một bên, tia lửa xoáy nhẹ | `void-core-rim.v1-try2.png` | `void-core-rim.v1-try2.prompt.txt` |
| C — Sợi sáng rất mảnh cong về mép | `void-core-rim.v1-try3.png` | `void-core-rim.v1-try3.prompt.txt` |

Tờ chọn mẫu có nhãn A–C: [void-core-rim-449.jpg](/private/tmp/typing-game-449/void-core-rim-449.jpg), 1632×572. Có `ABOUT.md` cùng thư mục. Dùng đường dẫn dự phòng được phiếu cho phép vì thư mục review trên SSD nằm ngoài vùng sandbox được ghi; không cập nhật chỉ mục review ngoài sandbox.

## Tham chiếu và xử lý

Cả ba lần gọi đều đính kèm đúng hai ảnh của dự án, đường dẫn tuyệt đối và vai trò có trong từng prompt:

- `games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-blackhole-storyboard.v1-try1.png`: viền mảnh quanh lõi tại ô 2 và ô 3.
- `games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-accretion-ring.v1-try1.png`: màu vàng trắng nóng và chất liệu ánh sáng, không lấy bố cục vành bồi tụ.

Chọn `image_gen` theo phiếu, chỉ tạo một thành phần viền tái sử dụng mỗi lần, không tạo toàn cảnh hay kỹ năng hoàn chỉnh. Không dùng ảnh bên thứ ba.

Công cụ trả cả ba ảnh gốc 1254×1254 dù prompt yêu cầu 1024×1024. Đã dùng ImageMagick dịch tâm và thu phóng đồng đều trên nền đen thành 1024×1024; lấy đường sáng mạnh nhất theo 180 hướng để ước lượng tâm và đường kính nguồn, đưa đường kính trung vị về 512 px. Không vẽ thêm viền, không vẽ mặt nạ tròn, không bóp méo cục bộ, không thay màu. Hệ số thu phóng A/B/C lần lượt khoảng 0,754554 / 0,681700 / 0,735722.

Ảnh gốc được giữ nguyên trong `/Users/toandx/.codex/generated_images/01a1ecc8-1a5b-7471-878d-ebdf87b83284/`:

- A: `exec-0374860b-b649-41a2-a7ba-13b86964d2f1.png`.
- B: `exec-f588fd19-54aa-4900-939e-d1ab42d5fc94.png`.
- C: `exec-8c454a74-84c7-4384-9ba6-528e5c823aed.png`.

## Kiểm tra và điểm owner cần xem

Đã mở xem hai ảnh tham chiếu, ba kết quả sinh và tờ ghép cuối. Ba PNG đều 1024×1024; pixel tâm và góc đều RGB (0,0,0). Không có quả cầu có bề mặt 3D, vành bồi tụ, cảnh nền hoặc chữ trong ảnh nguồn; nhãn A–C chỉ ở tờ ghép.

| Mẫu | Đường kính viền trung vị | Khoảng đường kính theo hướng, phân vị 5–95% |
| --- | --- | --- |
| A | 512 px | 504–518 px |
| B | 512 px | 504–516 px |
| C | 512 px | 506–522 px |

Các số đo dùng đỉnh sáng theo 360 hướng sau chuẩn hóa, không phải đường biên của một mặt nạ hình học hoàn hảo. Vì vậy **chưa bảo đảm hình tròn rỗng đen tuyền có đường kính đúng 512 px tại mọi hướng**: còn lệch tròn và ánh sáng lấn nhẹ ở sát mép trong; khoảng 20–23% pixel trong vùng bán kính 250 px có ít nhất một kênh khác 0, phần lớn rất tối nhưng có pixel sáng gần mép. Dải lề ngoài 100 px còn nhiễu tối tối đa RGB 1. Không tự đánh dấu đạt nền và vùng rỗng đen tuyệt đối. Không sinh lần thứ tư vì phiếu giới hạn đúng ba lần.

- **A:** đọc rõ viền mảnh và quầng mềm; độ sáng còn biến thiên nhẹ quanh chu vi.
- **B:** phía trên phải rực hơn, có sợi và tia lửa ôm mép; quầng gọn hơn A và C.
- **C:** các sợi cong rõ và dài hơn B; owner nên xem mức độ rực có phù hợp vai trò viền phụ sau lõi không.

Owner cần chọn hướng A–C trong tờ ghép và xem các sai khác hình học trước khi giao bước xử lý hoặc tích hợp. Không chấm điểm 8,5 cho một lớp nguồn; chưa có bằng chứng nghiệm thu hiệu ứng tổng hợp tại camera chơi.

## Không thực hiện

Không sửa code, không làm video hoặc âm thanh, không chạy build hay bộ test game. Không sửa src/scripts/tests hoặc tài liệu Tu Tiên. Không ghi đè ảnh đã có trước phiên, không xóa ảnh, không đổi nhánh; không commit, push, reset, clean hoặc stash. Không sửa manifest hoặc tài liệu ngoài phạm vi phiếu.
