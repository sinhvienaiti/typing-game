# Phiếu 360 · Ngũ Lôi toả quạt và thu năng lượng

Ngày thực hiện: 12/11/2026. Công cụ: image_gen tích hợp. Đã dùng **6/6 lượt tạo ảnh**: hai bản đầu và bốn bản vẽ lại; **5/8 lượt view_image**: ba tham chiếu và hai lần xem tấm ghép. Không gặp HTTP 429; đã chạm trần lượt gọi của phiếu.

Đã tạo đủ hai chủ đề, mỗi chủ đề ba phiên bản, sáu prompt nguyên văn và tấm ghép có ô kiểm cao đúng 120 px. **Chưa đạt toàn bộ điều kiện:** đòn kết try3 còn 2,6280% xanh/tím, vượt ngưỡng 2%; cả hai bản chọn còn nhiễu tối đa 1/255 trong ô góc. Không ghi PASS trọn bộ. Đòn kết tự chấm yếu nhất 7,8 nên còn cần sửa; không tự gọi lượt thứ bảy.

## Tệp bàn giao

S = `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

- [Đòn kết try3](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-five-fan.v1-try3.png), 1671 × 941, khổ ngang xấp xỉ 16:9 do kích thước đầu ra công cụ.
- [Thu năng lượng try3](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-five-gather.v1-try3.png), 1672 × 941, khổ ngang xấp xỉ 16:9.
- [Tấm ghép](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-fan-360-sheet.jpg), 1320 × 1160; bên trái là ảnh lớn, bên phải là ô cao 120 px, không tăng sáng hay làm sắc. Tấm ghép cuối dùng hai bản try3.
- Giữ đủ `thunder-five-fan.v1-try1.png` đến `try3.png` và `thunder-five-gather.v1-try1.png` đến `try3.png`. Mỗi ảnh có `<tên>.prompt.txt` cùng thư mục, ghi nguyên văn prompt và đường dẫn/vai trò tham chiếu.

Chỉ dùng ba tham chiếu riêng của repo mà phiếu chỉ định. Ảnh đòn kết v4 chỉ cho màu và nét mực; bỏ bố cục hội tụ xuống một điểm. Ảnh trận bạc chỉ cho ngữ cảnh bảng màu, không vẽ trận hay chữ vào đầu ra. Các lượt sửa dùng chính ảnh vừa tạo làm đích chỉnh. Hai mẫu đầu đã hiển thị cho chủ nhân trước bốn lượt vẽ lại.

## Kiểm bố cục tại 120 px

Đã thực sự thu nhỏ toàn ảnh xuống cao 120 px bằng ImageMagick 7 rồi mở tấm ghép ở độ phân giải gốc để nhìn ô kiểm.

| Bản chọn | Số thân/luồng | Số điểm dưới | Khoảng tối và hành động |
| --- | ---: | ---: | --- |
| Đòn kết try3 | 5 | 5 điểm chạm | Năm thân tách rõ, giữa dày nhất, hai ngoài xiên ra; năm vụ nổ nhỏ riêng và mảnh đá, không nhập thành một điểm. |
| Thu năng lượng try3 | 5 | 5 điểm nguồn | Năm sợi mảnh có khoảng tối, chỉ gặp nhau ở tâm mây phía trên; điểm dưới nhỏ và yên, không có vụ nổ hay tia giáng dày. |

Các điểm dưới nằm thành hàng ngang, cách nhau gần đều. Mây nằm phía trên và có lề đen; không có mặt đất được vẽ. Khung thu có hạt sáng và tâm mây rực hơn try2. Hướng chuyển động hút lên vẫn cần xác nhận khi làm video: ảnh tĩnh chỉ cung cấp gợi ý đầu hạt/đuôi hạt, không chứng minh chuyển động 0,4 giây.

## Phép đo kỹ thuật

Theo cách đo phiếu 353: đọc PNG gốc thành RGB 8-bit bằng ImageMagick 7, V = max(R,G,B)/255; HSV bằng `colorsys.rgb_to_hsv`. Mẫu số tỷ lệ màu là mọi pixel **V > 0,35**. Xanh/tím là H trong **190–300°**, không lọc độ bão hoà, yêu cầu ≤ 2%. Vàng sáng là H trong **45–60°**, S > 0,8, V > 0,85, yêu cầu ≤ 5%. Vì không lọc S, xám hơi lạnh cũng tính vào xanh/tím; không tự đổi phép đo để ảnh đạt.

Lề tính theo hộp bao mọi pixel max(R,G,B) > 8, theo thứ tự **trái / trên / phải / dưới**. Yêu cầu phiếu này ≥ 8%. Góc kiểm cả bốn pixel ngoài cùng và bốn ô góc 10%; yêu cầu đen tuyệt đối.

| Ảnh | Điểm sáng | Xanh/tím % | Vàng sáng % | Lề >8, % (T/Tr/P/D) | Max ô góc |
| --- | ---: | ---: | ---: | --- | ---: |
| fan try1 | 170423 | 2,2485 | 0,0000 | 6,64 / 14,45 / 7,89 / 15,83 | 1/255 |
| fan try2 | 157625 | 3,1194 | 0,0000 | 13,40 / 14,56 / 14,35 / 18,28 | 1/255 |
| **fan try3** | **186186** | **2,6280** | **0,0000** | **13,41 / 14,56 / 14,30 / 18,28** | **1/255** |
| gather try1 | 35181 | 2,0721 | 0,0000 | 12,50 / 14,45 / 12,98 / 19,34 | 1/255 |
| gather try2 | 24549 | 0,3707 | 0,0000 | 13,10 / 14,45 / 13,16 / 19,77 | 1/255 |
| **gather try3** | **30624** | **0,2057** | **0,0000** | **13,10 / 14,45 / 13,40 / 20,19** | **1/255** |

Góc ngoài cùng của fan try3: `(0,0,0) / (0,0,0) / (1,1,0) / (0,1,0)`. Gather try3: `(1,1,0) / (0,0,0) / (0,0,0) / (0,1,0)`, theo thứ tự trên trái / trên phải / dưới trái / dưới phải. Sai lệch rất nhỏ nhưng vẫn là lỗi nền, không coi là đen tuyệt đối.

Hai bản chọn đạt lề và ngưỡng vàng sáng; chỉ gather try3 đạt thêm ngưỡng xanh/tím. Không có bản nào đạt đủ nền đen tuyệt đối. Chỉ tấm ghép được thu nhỏ/thêm nhãn bằng ImageMagick với Arial của máy Mac; không hậu kỳ sửa màu, xoá nhiễu, ghép tia hay thêm lề vào PNG nguồn.

## Tự chấm theo mặt yếu nhất

Đây là tự chấm nguồn tĩnh, không phải hai giám khảo mù hay nghiệm thu hiệu ứng trong play host. Các lỗi nền được ghi riêng như điều kiện kỹ thuật bắt buộc.

| Bản chọn | Đếm 5/5 ở 120 px | Khoảng tối | Cùng bộ bạch kim | Lực/nhịp thu | Khung đầu video | Thấp nhất |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| fan try3 | 9,0 | 8,8 | 7,8 | 8,6 | 8,4 | **7,8** |
| gather try3 | 8,7 | 8,8 | 8,6 | 8,2 | 8,4 | **8,2** |

Fan try1 thiếu lề; try2 sửa được lề nhưng màu lạnh tăng; try3 giảm màu lạnh, vẫn vượt ngưỡng nên điểm đồng bộ màu dưới 8. Gather try1 hơi lạnh và đầu/đuôi hạt dễ gây hiểu nhầm hướng; try2 giảm màu lạnh và làm nguồn dưới yên; try3 tăng hạt dẫn cùng ánh tâm mây. Cả hai chủ đề đã dùng đủ hai lượt vẽ lại được phân bổ.

## Phần không làm và việc chủ nhân cần xem

- Không sửa mã, tích hợp runtime, tạo video/âm thanh, mở cổng, chạy build/test hay thao tác ghi Git. Không sửa tệp đã có trước phiếu; chỉ thêm các PNG, prompt, tấm ghép và báo cáo được cho phép.
- Không tuyên bố nghiệm thu 8,5 hoặc PASS đầy đủ. Bản đòn kết vẫn cần sửa tỷ lệ xanh/tím và cả hai nguồn cần nền đen tuyệt đối; trần 6 lượt của phiếu đã dùng hết, không tự mở lượt thứ bảy.
- Chủ nhân xem ô 120 px để xác nhận cách đọc năm thân/năm điểm; xem độ xiên hai tia ngoài và lực của năm vụ chạm. Với khung thu, xem gợi ý hạt hút lên và mức sáng tâm mây trước khi dùng làm khung đầu video.
- Tệp bàn giao và mọi bản thử đã được giữ nguyên. Không có giờ mở lại do công cụ cung cấp.
