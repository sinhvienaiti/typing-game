# Phiếu 444 — Bốn mẫu vệt sáng kiếm bay

Đã tạo **4 ảnh bằng công cụ tích hợp `image_gen`**, đúng một lượt cho mỗi hướng A–D, ngày 17/11/2026. Phiếu đã có phản biện PASS (Sonnet, 17/11). Đây là các mẫu thành phần tĩnh để owner chọn, chưa nghiệm thu hoặc gắn vào game.

## Tệp giao nộp

Thư mục: [stills](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/).

| Nhãn | Ảnh | Prompt nguyên văn |
| --- | --- | --- |
| A — Vệt thẳng | [sword-trail.v1-try1.png](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try1.png) | [try1.prompt.txt](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try1.prompt.txt) |
| B — Khí tiên xoắn | [sword-trail.v1-try2.png](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try2.png) | [try2.prompt.txt](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try2.prompt.txt) |
| C — Đuôi tách sợi | [sword-trail.v1-try3.png](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try3.png) | [try3.prompt.txt](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try3.prompt.txt) |
| D — Đuôi hạt | [sword-trail.v1-try4.png](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png) | [try4.prompt.txt](../../games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.prompt.txt) |

[Tờ so sánh sword-trail-444.jpg](/private/tmp/typing-game-444/sword-trail-444.jpg), kích thước **4192 × 1112**, A–D từ trái sang phải, giữ toàn bộ khung từng ảnh và đặt nhãn ngoài ảnh. Có `ABOUT.md` cùng thư mục. Dùng vị trí dự phòng vì thư mục review trên SSD nằm ngoài vùng sandbox được ghi; không sửa chỉ mục review ngoài phạm vi phiếu.

Hai ảnh dự án sau được truyền trực tiếp vào **cả bốn lượt**, với đường dẫn và vai trò ghi trong từng prompt:

- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/sword-fall-streak.v1-try1.png`: sắc vàng ấm và khí tiên mảnh, bỏ toàn bộ kiếm.
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: chỉ lấy cảm giác vệt rơi ở ô trên phải của nửa trái, bỏ cảnh và phần tím.

## Kiểm tra và điểm cần owner xem

Công cụ trả ảnh **1254 × 1254** dù prompt yêu cầu 1024. Đã dùng ImageMagick thu đồng đều về **1024 × 1024 PNG RGB**, không cắt khung, tô lại hoặc tăng sáng. Bản sinh ban đầu còn nguyên trong thư mục mặc định của công cụ. Đã xem cả bốn ảnh và tờ ghép; đủ bốn prompt. Mỗi ảnh có một vệt dọc, lõi trắng ấm, quầng vàng và hạt nhỏ; không thấy kiếm, chữ hay vòng.

Số đo dưới đây lấy bề rộng lớn nhất **trên từng hàng**, tính cả hạt và quầng, theo kênh RGB lớn nhất:

| Mẫu | Rộng tại RGB > 4/255 | Rộng tại RGB > 1/255 | Khoảng dọc tại RGB > 4/255 |
| --- | --- | --- | --- |
| A | 53 px (5,2%) | 60 px (5,9%) | y=134–873 |
| B | 63 px (6,2%) | 80 px (7,8%) | y=126–869 |
| C | 80 px (7,8%) | 92 px (9,0%) | y=136–868 |
| D | 81 px (7,9%) | 94 px (9,2%) | y=100–880 |

**Chưa đạt tuyệt đối mọi ràng buộc nguồn:** nền nhìn đen nhưng còn nhiễu RGB mức 1; quầng rất tối của C/D vượt 8%. Đầu vệt ở khoảng 85% chiều cao; đuôi A–C thấy rõ từ khoảng 12–13%, D từ khoảng 10%. Không dùng ngưỡng đo để xoá nhiễu hoặc che phần vượt giới hạn.

- **A:** lõi thẳng, đuôi mềm, nhưng còn sợi khí phụ nên chưa thuần một vệt sao băng.
- **B:** sợi khí xoắn quanh lõi rõ hơn; cần owner xem độ mảnh và nhịp xoắn.
- **C:** đuôi tách sợi ở phần trên; có quầng tối rộng hơn giới hạn.
- **D:** hạt thưa dần lên trên, nhưng vẫn còn sợi khí liên tục; chưa thành chuỗi hạt tách biệt hoàn toàn.

Owner cần chọn hình dáng muốn giữ và xem các điểm lệch trên trước bước xử lý nguồn hoặc gắn vào kiếm. Chưa có nghiệm thu hiệu ứng tổng hợp 8,5 trong play host.

## Phạm vi và phần bỏ qua

Không tạo thêm vì phiếu cho tối đa bốn lượt; không có lỗi hạn mức dịch vụ. Không sửa code, làm video/âm thanh, chạy build/test, dùng ảnh bên thứ ba hoặc ảnh game khác. Không xoá hay ghi đè ảnh có sẵn, không tạo agent, không chạy lệnh Git. Việc chọn mẫu và kéo vệt theo tốc độ rơi thuộc bước tiếp theo của owner/coordinator.
