# Phiếu 448 — Hào quang tĩnh cho kiếm lớn

Ngày thực hiện: 18/11/2026. Phiếu có phản biện PASS (Sonnet, 18/11). Đã gọi công cụ tích hợp `image_gen` đúng **4 lần**, mỗi hướng A–D đúng một lần; không vẽ lại. Đây là bộ mẫu chờ owner chọn, chưa nghiệm thu trong game.

## Tệp đã tạo

Thư mục: `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/`.

| Mẫu | Ảnh | Prompt nguyên văn |
| --- | --- | --- |
| A — Quầng sáng mềm | `giant-sword-aura.v1-try1.png` | `giant-sword-aura.v1-try1.prompt.txt` |
| B — Dải khí tiên | `giant-sword-aura.v1-try2.png` | `giant-sword-aura.v1-try2.prompt.txt` |
| C — Hình thoi, sao hai đầu | `giant-sword-aura.v1-try3.png` | `giant-sword-aura.v1-try3.prompt.txt` |
| D — Tia sáng rủ xuống | `giant-sword-aura.v1-try4.png` | `giant-sword-aura.v1-try4.prompt.txt` |

Tờ chọn mẫu: [giant-sword-aura-448.jpg](/private/tmp/typing-game-448/giant-sword-aura-448.jpg), 2176×1250, có nhãn A–D. Hàng trên là ảnh hào quang; hàng dưới là ảnh hào quang đặt sau kiếm trên nền đá tối. Có `ABOUT.md` cùng thư mục. Dùng đường dẫn dự phòng vì thư mục review trên SSD nằm ngoài vùng sandbox được ghi; không chạy công cụ tạo chỉ mục cho thư mục review đó.

## Tham chiếu và xử lý

Cả bốn lần gọi đều đính kèm đúng hai ảnh của dự án; đường dẫn tuyệt đối và vai trò được ghi trong từng prompt:

- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/sword-fall-streak.v1-try1.png`: sắc vàng, khí tiên và hướng kiếm chĩa xuống.
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: chỉ hướng ánh sáng quanh kiếm lớn ở nửa trái, ô dưới trái.

Chọn `image_gen` theo phiếu: vẽ riêng một thành phần hào quang tái sử dụng, không tạo cả cảnh hay kỹ năng. Không dùng ảnh bên thứ ba.

Công cụ trả ảnh gốc 1254×1254 dù prompt yêu cầu 1024×1024. Đã dùng ImageMagick thu đồng đều xuống 860×860, đặt giữa nền đen 1024×1024 để bảo đảm lề, không vẽ thêm hình. Ảnh gốc vẫn giữ tại thư mục mặc định của công cụ, không bị ghi đè. Bốn PNG giao nộp đã kiểm tra kích thước và toàn bộ lề 82 px: RGB đều bằng 0. Ảnh không có kiếm thật, chữ, vòng tròn hay lông nhọn; đã mở xem tờ ghép cuối.

Tờ ghép dùng chính ảnh `sword-fall-streak` được tách theo đường bao kiếm, đặt phía trước hào quang. Nền đá lấy từ vùng trống `(20,360,180,100)` của cùng ảnh storyboard. Bốn ô dùng chung kiếm, nền, kích thước và vị trí. Đây là ghép thử 2D; không phải mô hình Tripo hoặc ảnh chụp runtime. Đã xóa các tệp trung gian do phiên này tạo trong thư mục tạm.

## Những điểm owner cần xem

- **A:** vẫn có nhiều dải khí uốn, gần B hơn quầng sáng mờ như yêu cầu; chưa phân biệt hướng đủ rõ.
- **B:** đọc rõ khí tiên vàng mềm, ôm dọc hai bên khe.
- **C:** phân biệt rõ nhất nhờ dáng thoi dài và hai đốm sao ở hai đầu.
- **D:** có các tia dọc và nhiều hạt sáng, vẫn giữ các dải khí mềm bên trong.
- **Sai khác chung:** khe đen do công cụ vẽ hẹp và ngắn hơn mục tiêu khoảng 12% × 70%, nhất là sau bước thu ảnh để giữ lề. Vài điểm trong khe A–B còn sắc rất tối ở mức RGB 1. Vì vậy chưa đánh dấu đạt toàn bộ hình học của phiếu. Không gọi thêm lần thứ năm để sửa vì giới hạn đúng bốn lần.

Owner cần chọn hướng A–D và xem độ ôm kiếm trong hàng ghép thử trước khi có bước tiếp theo. Chưa có nghiệm thu hiệu ứng tổng hợp ở camera chơi.

## Không thực hiện

Không sửa code, không tích hợp vào game, không làm video, không tạo âm thanh; không chạy build hay bộ test của game. Không sửa các tài liệu Tu Tiên, không dùng ảnh game khác, không ghi đè ảnh đã có trước phiên, không commit hoặc thay đổi nhánh.
