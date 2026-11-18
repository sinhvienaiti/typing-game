# Phiếu 354 · Trận pháp lôi bạc lam nhạt D65

Ngày thực hiện: 12/11/2026. Công cụ: **image_gen tích hợp**, 4/4 lượt (hai bản đầu, mỗi bản vẽ lại một lần); **view_image 6/6** (ba tham chiếu, ba lần kiểm tấm ghép). Phiếu 353 đã có báo cáo trước khi bắt đầu.

**Đã tạo đủ tệp; chưa đạt toàn bộ điều kiện kỹ thuật.** Hai bản chọn `v1-try2` đạt ngưỡng độ sáng, bão hòa và lề. Nền vẫn còn nhiễu tối đa 1/255; bản A còn 11 điểm rất tối có sắc vàng bão hòa. Không ghi PASS tuyệt đối, không hậu kỳ sửa PNG và không tích hợp vào game.

## Tệp bàn giao

Thư mục S: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

| Vai trò | Tệp trong S |
| --- | --- |
| A bạc, bản đầu giữ lại | `thunder-array-silver-a.v1-try1.png` + `thunder-array-silver-a.v1-try1.prompt.txt` |
| Vành bạc, bản đầu giữ lại | `thunder-array-silver-ring.v1-try1.png` + `thunder-array-silver-ring.v1-try1.prompt.txt` |
| A bạc, bản chọn | `thunder-array-silver-a.v1-try2.png` + `thunder-array-silver-a.v1-try2.prompt.txt` |
| Vành bạc, bản chọn | `thunder-array-silver-ring.v1-try2.png` + `thunder-array-silver-ring.v1-try2.prompt.txt` |
| Tấm ghép | [`thunder-array-354-sheet.jpg`](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-array-354-sheet.jpg), 1800 × 696 |

Mỗi prompt là nguyên văn đã gửi image_gen, ghi đường dẫn và vai trò từng tham chiếu. Chỉ dùng ảnh của repo do phiếu chỉ định, cộng bản bạc vừa tạo trong lượt sửa. Không dùng ảnh bên ngoài.

Các PNG đều 1254 × 1254, là bản sao nguyên vẹn đầu ra image_gen; đã so SHA-256 với tệp gốc của công cụ, cả bốn cặp giống nhau. Không đổi màu, làm sạch nền, thêm lề hay vẽ hình bằng mã.

## Tham chiếu và cách thực hiện

- `thunder-array-a.v1-try2.png`: khóa bố cục vòng chữ triện, hồi văn, tám quẻ, lớp mây/cánh sen, năm nút lôi và lõi nhỏ; không thiết kế lại.
- `thunder-array-ring.v1-try1.png`: khóa dải chữ triện rời, hai viền và bốn dấu hướng; bản sửa thu nhỏ đồng đều để tăng lề.
- `thunder-five-strike.v3-try1.png`: chỉ so thứ bậc sáng và ghép thử, dùng đúng **try1** theo phiếu dù báo cáo 353 chọn try2 cho đòn kết.
- Hai bản đầu có sắc lam rõ nhưng vùng mờ bão hòa vượt 0,3. Mỗi bản được vẽ lại một lần để giảm bão hòa; vành được tăng lề. Bản chọn gần bạc trung tính, ánh lam rất nhẹ; chủ nhân cần xem sắc lạnh đã đủ theo D65 chưa.

Hai mẫu đầu đã hiển thị trong hội thoại trước khi thực hiện hai lượt sửa. Không chạy nghiên cứu hay duyệt thiết kế mới: thực hiện đúng phiếu đổi màu có sẵn. Đánh giá dưới đây là tự kiểm lớp nguồn theo yêu cầu, không phải nghiệm thu hiệu ứng trong game.

## Phép đo

Đọc PNG bằng ImageMagick 7 thành RGB 8-bit, không ghi ngược vào PNG. HSV tính bằng `colorsys.rgb_to_hsv`; V = max(R,G,B)/255.

- **Vùng hình có cả phần mờ:** max(R,G,B) > 8. Ngưỡng này loại nền nhiễu 1/255, nhưng vẫn bắt quầng và hạt.
- **Vùng nét sáng:** max(R,G,B) > 89, tương đương V > 0,35. Ghi riêng để trung vị không bị phần quầng tối kéo xuống.
- **Lõi tia tham chiếu:** max(R,G,B) ≥ 217, tương đương V ≥ 0,85; có 41.181 pixel.
- Chỉ số độ sáng chính: **Y trên RGB sRGB đã mã hóa**, Y = 0,2126R + 0,7152G + 0,0722B, sau khi chuẩn hóa về 0–1. Đây là chỉ số so ảnh, không phải độ chói vật lý tuyến tính. Trung vị Y lõi tia = **0,960931**; trung vị V lõi = **0,988235**.
- Tỉ lệ sáng = trung vị Y của trận / trung vị Y lõi tia. Ghi cả vùng hình và nét sáng; cả hai phải ≤ 0,6.
- S trung vị đo trên vùng hình; ghi thêm S riêng vùng nét sáng.
- Điểm vàng bão hòa: H trong **45–60°**, **S > 0,3**, max kênh > 8. Đây là cách kiểm nghiêm cả phần rất tối; không bỏ các điểm tối để tuyên bố không có màu vàng.
- Lề là hộp bao mọi pixel max kênh > 8 đến từng mép, theo thứ tự **trái / trên / phải / dưới**.
- Kiểm bốn pixel góc và bốn ô góc 10% khổ. Đen thuần yêu cầu mọi kênh bằng 0.

| Bản | Số pixel hình | Y trung vị hình | Hình / lõi | Y trung vị nét sáng | Nét / lõi | S hình | S nét sáng | Điểm vàng bão hòa |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A try1 | 367.732 | 0,170700 | 0,177640 | 0,420350 | 0,437440 | 0,339286 | 0,239130 | 1 |
| Vành try1 | 225.410 | 0,125558 | 0,130663 | 0,533556 | 0,555249 | 0,349206 | 0,239766 | 2 |
| **A try2** | 338.077 | 0,191889 | **0,199691** | 0,436164 | **0,453897** | **0,073684** | 0,043165 | **11** |
| **Vành try2** | 135.613 | 0,115980 | **0,120695** | 0,500576 | **0,520929** | **0,050633** | 0,025974 | **0** |

Kiểm chéo bằng trung vị V ở vùng nét sáng: A try2 **0,447059**, tỉ lệ với lõi **0,452381**; vành try2 **0,505882**, tỉ lệ **0,511905**. Cả hai vẫn dưới 0,6.

| Bản | Lề T/Tr/P/D, % | Bốn pixel góc TL/TR/BL/BR | Max kênh trong bốn ô góc |
| --- | --- | --- | ---: |
| A try1 | 17,464 / 15,630 / 17,544 / 20,893 | B / B / G / G | 1 |
| Vành try1 | 11,722 / **9,968** / 12,121 / 13,876 | B / B / B / G | 1 |
| **A try2** | **17,703 / 15,869 / 17,703 / 21,132** | B / B / G / G | **1** |
| **Vành try2** | **18,501 / 15,710 / 19,059 / 21,611** | B / B / B / G | **1** |

B = RGB(0,0,0); G = RGB(0,1,0). Cả bốn ảnh **không đạt nền đen tuyệt đối**. Đây là lỗi kỹ thuật dù sai lệch chỉ 1/255.

**Điểm vàng còn lại của A try2:** 11 pixel, chỉ V = 0,035–0,047, S = 0,333–0,700. Các tọa độ (gốc trên trái, tính từ 0):
`(897,531), (898,531), (327,545), (327,546), (328,546), (351,717), (477,794), (476,795), (477,795), (476,796), (604,885)`.
Không có điểm vàng bão hòa trong vùng nét sáng của cả bốn ảnh, nhưng điều kiện “không có điểm” trên toàn vùng hình vẫn **không đạt ở A try2**.

**Tâm vành try2:** nhìn rõ một khoảng tâm trống lớn, không có hình hay hạt sáng. Kiểm đĩa tâm có đường kính khoảng 55% đường kính vành cho max kênh = **1/255**, nên **không đạt yêu cầu tâm đen thuần ≥ 55%**. Bỏ nhiễu ≤ 8 thì vùng trống nhìn thấy rộng khoảng 83% đường kính vành; con số này không thay thế điều kiện đen thuần.

**Hình tròn:** kiểm bằng mắt trên ảnh nguồn và tấm ghép: hai vòng nhìn chính diện, không phối cảnh, không có biến dạng elip rõ. Không tuyên bố đã chứng minh tròn hoàn hảo bằng phép đo hình học; hạt và dấu hướng làm hộp bao không đại diện chính xác cho đường tròn.

## Tự chấm theo mặt yếu nhất

Điểm chỉ là tự chấm mỹ thuật nguồn, tách khỏi các lỗi kỹ thuật đã nêu. Không phải điểm từ hai giám khảo độc lập hay nghiệm thu runtime.

| Bản | Lùi về nền, còn huyền bí | Giữ bố cục | Tâm thoáng | Hợp tia bạch kim | Thấp nhất |
| --- | ---: | ---: | ---: | ---: | ---: |
| A try1 | 7,7 | 8,8 | 8,5 | 7,8 | **7,7** |
| Vành try1 | 7,7 | 8,6 | 8,8 | 7,8 | **7,7** |
| **A try2** | 8,3 | 8,8 | 8,5 | 8,2 | **8,2** |
| **Vành try2** | 8,2 | 8,6 | 8,8 | 8,1 | **8,1** |

Hai bản đầu dưới 8 đã được vẽ lại đúng một lần. Bản chọn lui rõ về nền, vẫn đọc được chữ triện và bát quái, không tranh chủ thể với tia trắng ngà-vàng nhạt. Sắc lam ở try2 rất nhẹ, gần xám bạc; đây là điểm cần chủ nhân xem trực tiếp, không tự coi là đã được duyệt.

## Tấm ghép và việc chủ nhân cần xem

Tấm ghép gồm A try2, vành try2 và ô A try2 ghép tia `thunder-five-strike.v3-try1.png`. Mỗi ô rộng 600 px. Tia thu nhỏ cao 340 px, dùng phép ghép **Screen** giữ nguyên màu, đặt điểm giáng gần lõi trận; không hạ sáng riêng trận hay tăng sáng riêng tia. Nhãn bằng font `/System/Library/Fonts/Supplemental/Arial.ttf`. Đã xem lại tấm ghép cuối.

Chủ nhân xem độ lạnh của bạc lam rất nhẹ ở hai bản chọn, độ thoáng của tâm A khi tia đè lên, và thứ bậc sáng ấm–lạnh trong ô ghép. Đây là ghép ảnh tĩnh để kiểm nguồn, không phải bằng chứng chất lượng chuyển động trong game.

## Không làm và trạng thái tiếp tục

- Không sửa mã, tệp nguồn có sẵn, game docs, công cụ hay tài sản tham chiếu; không chạy build/test; không mở cổng; không ghi Git.
- Chỉ thêm bốn PNG, bốn prompt và tấm ghép trong S, cùng báo cáo này. Chỉ tấm ghép do phiếu này tạo được chỉnh lại vị trí và nhãn trong quá trình kiểm; các PNG không thay đổi.
- Không tạo âm thanh, video, ảnh ngoài phạm vi hay gọi thêm trợ lý/giám khảo. Không tích hợp runtime.
- **Đã dùng hết 4/4 lượt image_gen của phiếu.** Không có HTTP 429 và công cụ không cung cấp giờ reset. Không gọi lượt thứ năm.
- Còn lỗi nền 1/255, tâm vành chưa đen tuyệt đối và 11 pixel vàng tối ở A. Cần chủ nhân/coordinator quyết định cách xử lý hoặc cấp phiếu bổ sung; không tự mở thêm lượt trong lần chạy lại và không dùng mã hậu kỳ để né giới hạn.

