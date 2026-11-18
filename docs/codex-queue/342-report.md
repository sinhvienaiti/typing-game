# Phiếu 342 · Xoáy mây kiếp góc ba phần tư · 12/11/2026

Đã đọc báo cáo 341 trước khi chạy. Tạo bằng **image_gen: 2/3 lần gọi**; **view_image: 3/4 lần** (hai tham chiếu và tấm so). Chọn **try2**; giữ try1 để đối chiếu. Không gặp giới hạn công cụ.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.

- `S/thunder-five-cloud-vortex-3q.v2-try1.png` và `.prompt.txt`: bản đầu, chưa đạt lề ngang.
- **`S/thunder-five-cloud-vortex-3q.v2-try2.png` và `.prompt.txt`**: bản đề nghị, 1254 × 1254; prompt nguyên văn, có đủ đường dẫn hai tham chiếu. PNG chép nguyên từ công cụ, không hậu kỳ.
- `S/thunder-five-vortex-342-compare.jpg`: 1920 × 1014, ảnh nhìn từ trên bên trái và try2 bên phải; cùng phép thu nhỏ toàn khung, chỉ ghép và thêm nhãn bằng ImageMagick, Arial.

## Kiểm và tự chấm

Đo trên PNG bằng ImageMagick 7 xuất RGB 8-bit và Python. Đúng cách phiếu 338: vùng sáng có `max(R,G,B) > 0,35`; tím có hue HSB từ 255° đến 330°, không lọc độ bão hòa. Lề tới bbox có `max(R,G,B) > 2%`; bốn vùng góc rộng/cao 6%.

| Bản | Lề trái / phải / trên / dưới | Tím trong vùng sáng | Cực đại RGB bốn góc |
| --- | --- | ---: | --- |
| try1 | 3,35 / 4,07 / 17,15 / 16,83% | 0,0798% | 1 / 1 / 2 / 1 |
| **try2** | **13,48 / 14,35 / 25,52 / 23,44%** | **0,0939%** (290/308.957 điểm) | **1 / 1 / 2 / 1** |

try1 chưa đạt lề nên vẽ lại với khung rộng hơn. try2 đạt các ngưỡng đo; không chữ, không vật thể thừa. Bốn góc gần đen, không khẳng định mọi điểm nền đều đúng #000000.

| Tiêu chí try2 | Tự chấm / 10 | Quan sát |
| --- | ---: | --- |
| Bề dày, phối cảnh | 8,6 | Elip ngang; thành mây trước dày, che chân phễu; mép sau mỏng hơn |
| Cùng bộ ảnh nhìn từ trên | 8,8 | Giữ mây cuộn trắng xanh và năm mầm sét; tâm đổi thành phễu sáng theo phiếu |
| Nền sạch | 9,2 | Lề đạt, nền gần đen, tím rất ít |
| Làm khung đầu video | 8,4 | Trọn hình, có sợi mây rủ; chưa kiểm chuyển động |
| **Mặt yếu nhất** | **8,4** | Tự chấm ảnh nguồn, chưa phải nghiệm thu hiệu ứng trong game |

Góc 35° được yêu cầu trong prompt; tranh cho phối cảnh nghiêng rõ nhưng không thể xác nhận góc máy chính xác bằng hình học. **Anh xem try2 và tấm so**, nhất là độ dày mép trước và độ lõm tâm. Đủ ảnh, prompt, tấm so và báo cáo; không bỏ hạng mục. Không tích hợp mã, tạo video, chạy build/test, mở cổng, dùng ảnh ngoài repo hay ghi Git vì ngoài phạm vi; không sửa tệp có sẵn.
