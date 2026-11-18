# Báo cáo Phiếu 451 — Tia quạt Ánh Sáng A2

Ngày: 18/11/2026. Đã tạo đủ ba biến thể bằng **đúng 3 lần gọi `image_gen`**, mỗi lần đính kèm trực tiếp cả hai ảnh tham chiếu của phiếu. Không dùng ảnh bên thứ ba hoặc ảnh game khác.

## Tệp đã tạo

Thư mục: `games/immortality-cultivation/art-src/lab/vfx/light/stills/`.

| Biến thể | Ảnh | Prompt nguyên văn |
| --- | --- | --- |
| A — thẳng, quầng mỏng | `light-ray-a2.v1-try1.png` | `light-ray-a2.v1-try1.prompt.txt` |
| B — quầng dày, lõi sáng hơn | `light-ray-a2.v1-try2.png` | `light-ray-a2.v1-try2.prompt.txt` |
| C — hai sợi sáng hai bên lõi | `light-ray-a2.v1-try3.png` | `light-ray-a2.v1-try3.prompt.txt` |

Tờ ghép: [light-ray-a2-451.jpg](/private/tmp/typing-game-451/light-ray-a2-451.jpg). Dùng đường dẫn dự phòng vì sandbox không cho ghi vào thư mục review ngoài repo. Thông tin thư mục nằm ở `/private/tmp/typing-game-451/ABOUT.md`.

## Tham chiếu và xử lý

Cả ba prompt ghi rõ hai đường dẫn:

- `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`: lấy chất tia vàng từ ô trên phải, tách thành một tia ngang.
- `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png`: lấy lõi trắng ấm, màu vàng hổ phách và chất lấp lánh.

Công cụ trả ảnh 2172×724 dù prompt yêu cầu 2048×512. Chuẩn hóa bằng ImageMagick: co về 1920×512, thêm nền đen bên phải thành 2048×512; đưa các giá trị kênh tối ≤1% về 0 để nền đen tuyền. Không vẽ bổ sung tia hay hạt bằng code. Bản gốc của công cụ vẫn được giữ nguyên trong thư mục `generated_images` mặc định.

## Kiểm tra tệp giao

Ba ảnh PNG đều 2048×512, nền đen không trong suốt. Đã xem tờ ghép: mỗi ảnh có một tia ngang, lõi trắng ấm và quầng hổ phách, vài hạt sáng; không có kính, nguồn sáng dạng vật thể, nhân vật hay chữ. C có hai sợi mảnh chạy sát hai bên lõi.

Đo vùng có pixel khác đen sau chuẩn hóa:

| Biến thể | Lề trên | Lề dưới | Điểm cuối vùng sáng theo chiều ngang |
| --- | ---: | ---: | ---: |
| A | 178 px (34,8%) | 192 px (37,5%) | 86,2% |
| B | 144 px (28,1%) | 162 px (31,6%) | 87,5% |
| C | 156 px (30,5%) | 166 px (32,4%) | 87,7% |

Lề trên/dưới đều ≥128 px (25%); đuôi tan hết trước mốc 90%. Vị trí gốc sáng xấp xỉ phía trái theo mẫu; quầng mềm lan ra quanh gốc.

## Chờ chủ dự án xem

Xem tờ ghép để chọn độ dày quầng và hai sợi của C. Đây là ba mẫu nguồn để chọn, chưa phải nghiệm thu hiệu ứng ghép trong game và không tự gán điểm 8,5.

Không bỏ sót biến thể. Không sửa code, không làm video, không tích hợp vào game, không chạy build hoặc bộ test, không ghi đè/xóa ảnh có sẵn, không đổi nhánh và không thực hiện thao tác ghi Git. Không cập nhật tài liệu Tu Tiên, manifest hay chỉ mục review vì ngoài phạm vi ghi của phiếu.
