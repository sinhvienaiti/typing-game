# Phiếu 334 · Dấu đất Ám và Quang nhìn từ trên

Hoàn tất ngày 11/11/2026. Dùng `image_gen` tích hợp: **2/4 lần gọi**, `view_image`: **6/6 ảnh** (5 tham chiếu và 1 tấm ghép để tự chấm cả hai đầu ra). Không vẽ lại.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

## Tệp đã thêm

- `S/dark-ground-mark-top.v1-try3.png` và `S/dark-ground-mark-top.v1-try3.prompt.txt`.
- `S/light-ground-mark-top.v1-try3.png` và `S/light-ground-mark-top.v1-try3.prompt.txt`.
- `S/top-down-334-sheet.jpg`: 1992 × 1436 px, mỗi hệ một hàng theo thứ tự gốc cũ → Gemini → Codex, có tên tệp.

Hai ảnh mới đều **1254 × 1254 px**, RGB, khổ 1:1; chép bằng `cp -n`. Mỗi tệp prompt ghi công cụ, ba đường dẫn tham chiếu theo vai trò, prompt tiếng Anh nguyên văn và khổ thật.

## Tự chấm ảnh nguồn

Điểm tổng lấy **tiêu chí thấp nhất**, không lấy trung bình. Đây là tự chấm ảnh nguồn theo phiếu, chưa phải nghiệm thu hiệu ứng ghép trong game.

| Ảnh mới | Đọc ra ngay | Cuốn hút, sang, ngang game thương mại | Góc nhìn tròn từ trên | Bảng màu | Nền đen, không chữ/watermark | Khung đầu video | Điểm thấp nhất | Lề trái / trên / phải / dưới | Vẽ lại | Nhận xét |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `dark-ground-mark-top.v1-try3.png` | 9,0 | 8,5 | 8,5 | 8,7 | 8,8 | 8,3 | **8,3** | 113 / 106 / 128 / 162 px; **9,01 / 8,45 / 10,21 / 12,92%** | Không | Dấu đá nứt Ám đọc rõ, khôi phục vòng hoa văn, khói mực và hạt tím; tâm hơi lệch, cần giữ hình khi làm video. |
| `light-ground-mark-top.v1-try3.png` | 9,0 | 8,6 | 8,5 | 8,8 | 8,8 | 8,4 | **8,4** | 129 / 102 / 139 / 176 px; **10,29 / 8,13 / 11,08 / 14,04%** | Không | Vòng Quang, khe vàng và tia sáng rõ, gần thiết kế gốc; lõi sáng mạnh, cần giữ chi tiết quanh tâm khi làm video. |

## Kiểm tra và lưu ý

- Đo bằng ImageMagick 7: lấy hộp bao của mọi điểm có **kênh RGB lớn nhất > 3/255**, tính lề đến bốn cạnh; giữ cả tia mờ và hạt sáng trong phép đo. Mọi cạnh đều ≥ 6%, nên không tạo `-pad.png`. Một số cạnh chưa đạt 10% mong muốn trong prompt nhưng đạt ngưỡng kiểm tra của phiếu.
- Kiểm từng ô góc 32 × 32 px: Ám có cực đại trái trên / phải trên / trái dưới / phải dưới **1 / 1 / 2 / 2** trên 255; Quang **1 / 1 / 2 / 1**. Nền gần đen thuần; không có chữ đọc được hay watermark trong ảnh mới, chỉ hoa văn trừu tượng.
- **Ảnh tham chiếu thắng:** ảnh Ám gốc có đá tím than và khe nứt hồng tím, khác mô tả thuần tím thẫm/đen mực; đã giữ cả sắc hồng tím đó. Quang khớp vàng kim nhạt và trắng ngà. Giữ nền đá, các vòng và ngôn ngữ hoa văn của ảnh gốc; bản Gemini chỉ định hướng bố cục, phiếu 331 định hướng lề và độ hoàn thiện.
- Chủ nhân xem `top-down-334-sheet.jpg`, nhất là độ tròn, sắc hồng tím của Ám và độ sáng lõi Quang trước khi đưa sang Firefly. Chuyển động chưa được kiểm vì phiếu chỉ tạo ảnh.
- Không có phần bị bỏ do hạn mức. Không sửa mã, tệp cũ hoặc tệp ngoài phạm vi; không chạy build/test game, không mở cổng, không dùng ảnh bên thứ ba hoặc lệnh Git ghi.
