# Phiếu 352 · Tu Tiên · Trận pháp lôi bản nhạt

Đã tạo đủ ba loại ảnh, hai lần vẽ lại, prompt nguyên văn và tấm ghép đối chiếu. **Chưa đạt trọn bộ điều kiện kỹ thuật của phiếu**: A try2 đạt cả độ sáng trung vị và đỉnh sáng; B try2 còn đúng một pixel vượt trần đỉnh sáng; vành try1 vẫn vượt trần. Cả ba còn nhiễu nền rất tối, chưa phải đen thuần từng pixel. Không đánh dấu các lỗi này là PASS.

Đã dùng **5/5 lần gọi image_gen tích hợp**, **6/8 lần view_image** (bốn tham chiếu, hai lần kiểm tấm ghép). Chỉ dùng ảnh của repo. Không gặp HTTP 429 hoặc thông báo phải chờ. Đã đọc báo cáo 348 và xác nhận 350, 351, 351b có báo cáo trước khi tạo ảnh.

## Tệp bàn giao

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

| Tệp trong S | Vai trò |
| --- | --- |
| `thunder-array-pale-a.v1-try1.png` | A nhạt đầu; giữ để đối chiếu, không chọn |
| `thunder-array-pale-a.v1-try2.png` | A vẽ lại, dùng trên tấm ghép |
| `thunder-array-pale-b.v1-try1.png` | B nhạt đầu; giữ để đối chiếu, không chọn |
| `thunder-array-pale-b.v1-try2.png` | B vẽ lại, dùng trên tấm ghép; còn một pixel quá sáng |
| `thunder-array-pale-ring.v1-try1.png` | Vành rời nhạt; chưa đạt trần đỉnh sáng |
| `thunder-array-352-sheet.jpg` | 1740×2170 px, ba cột A/B/vành, ba hàng đậm/nhạt/ghép tia |
| `thunder-array-352-sheet.prompt.txt` | Công thức và argv ImageMagick nguyên văn để ghép |

Mỗi PNG có tệp cùng tên gốc với đuôi `.prompt.txt`, ghi đúng prompt gửi công cụ và đường dẫn ảnh đầu vào. Cả năm PNG đều **1254×1254 px**, được sao chép nguyên vẹn từ đầu ra image_gen; không tô, ép màu, cắt ngưỡng, sửa alpha hoặc giảm sáng bằng mã. Chỉ tấm ghép dùng resize và ghép cơ học bằng ImageMagick 7.

## Thiết kế và tham chiếu

- A lấy `S/thunder-array-a.v1-try2.png`: giữ bố cục bát quái, tám ô quẻ, dải cổ văn, lôi văn, sen/mây, năm nút điện và tâm thoáng.
- B lấy `S/thunder-array-b.v1-try2.png`: giữ hai rồng đuổi nhau, sao chòm nối cung, các vòng cổ văn, sen/mây, năm nút điện và tâm thoáng.
- Vành lấy `S/thunder-array-ring.v1-try1.png`: giữ vành chữ triện và bốn dấu phương vị; lòng vành rỗng.
- `S/thunder-five-strike.v2-try9.png` chỉ làm tham chiếu thứ bậc độ sáng trong mọi lần tạo; dùng chính ảnh này để ghép thử ở hàng dưới.
- Try2 nhận thêm try1 tương ứng làm ảnh đích để giữ thiết kế. Prompt chỉ yêu cầu đổi cường độ, màu và nền.

Màu chuyển sang ngà ngả đồng cổ, ít bão hòa, bỏ hổ phách và tím rực. A/B try2 dịu hơn rõ rệt; nét và nút điện không còn cạnh tranh thị giác với tia trên tấm ghép. Các mô-típ chính giữ được qua đối chiếu; đây không phải cam kết mọi nét khắc trùng pixel với ảnh gốc, vì công cụ sinh lại raster.

## Đo màu và độ sáng

Dùng ImageMagick 7 giải mã ảnh thành RGB 8-bit sau khi ghép alpha trên đen; tính bằng Python chuẩn, không chạy build/test. HSV tính trực tiếp trên RGB sRGB đã mã hóa, **không phải độ chói tuyến tính**: `V = max(R,G,B)/255`, `S = (max−min)/max`. Vùng sáng là **V > 0,15**, áp dụng giống nhau cho trận và tia.

Tia tham chiếu 1084×1924 px có trung vị V vùng sáng **0,964706**. Lõi tia được định nghĩa là V > 0,90, trung vị **0,996078**. Vì vậy:

- Trần trung vị của trận: `0,7 × 0,964706 = 0,675294`.
- Trần đỉnh sáng: `0,7 × 0,996078 = 0,697255`; trong raster 8-bit, kênh lớn nhất phải ≤177/255.
- Vàng kim sáng: H trong 45–60°, S >0,8, V >0,85; tỷ lệ tính trên vùng sáng V >0,15.

| Ảnh | Trung vị V | V trận / V tia | Trung vị S | V lớn nhất | Đỉnh / lõi tia | Số pixel vượt trần đỉnh | Vàng kim sáng |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| a try1 | 0,361 | 0,374 | 0,222 | 0,949 | 0,953 | 3536 | 0,00% |
| a try2 | 0,259 | 0,268 | 0,242 | 0,616 | 0,618 | 0 | 0,00% |
| b try1 | 0,380 | 0,394 | 0,288 | 1,000 | 1,004 | 10246 | 0,00% |
| b try2 | 0,267 | 0,276 | 0,283 | 0,718 | 0,720 | 1 | 0,00% |
| ring try1 | 0,451 | 0,467 | 0,301 | 0,925 | 0,929 | 2954 | 0,00% |

**Cả năm ảnh đạt tỷ lệ trung vị ≤0,7, trung vị S ≤0,45 và vàng kim sáng 0%. Chỉ A try2 đạt thêm trần đỉnh sáng.** Không dùng trung vị để che lỗi đỉnh sáng. B try2 có max 183/255 ở một pixel, thay vì ≤177/255. Vành có max 236/255 và 2.954 pixel vượt ngưỡng.

## Nền, lề, độ tròn và tâm

Hộp bao dùng V >8/255 để loại nền cực tối; đây không phải ngưỡng làm sạch ảnh. Lề là khoảng cách nhỏ nhất từ hộp bao đó đến mép khung. Độ tròn đo vành liên tục: tâm từ hộp bao; quét 360 tia cách 1°, bước bán kính 0,5 px trong dải 92–101,5% bán kính ước lượng; chọn điểm ngoài cùng V >24/255, lọc trung vị 7° để loại hạt/lóe rời. Sai lệch là `max(|r−median(r)|)/median(r)`. Ngưỡng đo thấp hơn phiếu 348 vì nét ở đây đã rất nhạt; số đo không chứng minh đường tròn hình học tuyệt đối. Đối chiếu mốc raster ≤2% của phiếu 348.

| Ảnh trên tấm ghép | Hộp bao [trái, trên, phải, dưới), px | Lề nhỏ nhất | Bán kính trung vị | Sai lệch bán kính | Pixel tối ≤8/255 ở tâm |
| --- | --- | ---: | ---: | ---: | ---: |
| a try2 | [224, 197, 1025, 986] | 15,71% | 384,5 px | 1,95% | 93,57% |
| b try2 | [218, 192, 1032, 999] | 15,31% | 403,5 px | 1,24% | 92,63% |
| ring try1 | [153, 131, 1094, 1073] | 10,45% | 457,0 px | 1,09% | 100,00% |

Vùng tâm khảo sát có bán kính 12,5% chiều rộng khung, lấy tâm hộp bao. Ba ảnh đều giữ lề ≥10%, tâm thoáng và đường tròn nhìn thẳng; sai lệch vành đo được dưới 2%.

**Nền đen thuần: chưa đạt.** Đo toàn dải viền ngoài 10% ở RGB sau ghép trên đen:

| Ảnh | Kênh sáng nhất trong viền, /255 | Pixel viền khác đen tuyệt đối |
| --- | ---: | ---: |
| a try2 | 1 | 13,34% |
| b try2 | 1 | 13,37% |
| ring try1 | 3 | 12,77% |

Vành có tâm sạch về thị giác: toàn vùng tròn giữa đường kính 55% khung chỉ có V tối đa **1/255**, nhưng **12,30%** pixel vùng này khác 0 tuyệt đối. Không gọi đó là nền/tâm đen thuần. Phiếu này yêu cầu nền đen nên vành xuất nền đen; không chứng nhận alpha trong suốt sạch cho bước quay lớp.

## Tự chấm theo mặt yếu nhất

Điểm sau là tự chấm ảnh nguồn theo phiếu, không phải hai giám khảo độc lập hoặc nghiệm thu hiệu ứng trong game. Lỗi số đo vẫn là FAIL dù điểm hình ảnh đạt 8.

| Tiêu chí | A try2 | B try2 | Vành try1 |
| --- | ---: | ---: | ---: |
| Nhạt, lùi về nền; tia dẫn mắt | 8,5 | 8,4 | 7,8 — nét và điểm lóe còn mạnh |
| Giữ bố cục và mô-típ tham chiếu | 8,6 | 8,5 | 8,4 |
| Tâm thoáng | 8,7 | 8,7 | 8,8 |
| Huyền bí, đọc được vai trò trận lôi | 8,2 | 8,2 | 8,0 — xét vai trò lớp cổ văn |
| Sang, cuốn hút | 8,0 | 8,0 | 8,0 |
| **Mặt yếu nhất về hình ảnh** | **8,0** | **8,0** | **7,8** |
| **Điều kiện kỹ thuật tuyệt đối** | **FAIL: nền** | **FAIL: nền và một pixel đỉnh** | **FAIL: nền và đỉnh** |

A/B try1 tự chấm **7,7 / 7,6** vì lõi, glint còn quá sáng; đã vẽ lại mỗi ảnh đúng một lần. Vành tự chấm 7,8; **chưa vẽ lại được vì ngân sách chỉ cho hai lượt vẽ lại, đã dành cho A/B**. Không gọi thêm lần thứ sáu và không dùng mã để sửa PNG. Kết quả còn thiếu điều kiện nghiệm thu, giữ nguyên để anh xem và điều phối bước sau.

## Tấm ghép và phần anh cần xem

`S/thunder-array-352-sheet.jpg`: mỗi cột là A, B, vành; trên là bản đậm 348, giữa là bản nhạt A try2/B try2/vành try1, dưới là bản nhạt ghép tia thu nhỏ. Tia cao 320 px trong ô ảnh 560×560, đặt +190+22 để điểm chạm gần tâm trận. Ghép **Screen 100%**, giữ cường độ tia; không tăng tương phản trận. Mỗi ô nhạt ghi lỗi còn tồn tại.

Anh cần xem **độ đọc của A/B khi đã lùi sâu về nền** và **vành rời còn sáng hơn hai bản trận**. Đây là ghép tĩnh để xét thứ bậc, không phải phối cảnh camera chơi hoặc nghiệm thu chuyển động.

Không làm video, âm thanh, tích hợp, sửa mã, sửa ảnh/tài liệu có từ trước, mở cổng, chạy build/test hoặc thao tác ghi Git. Không ghi sang thư mục review chung vì phiếu chỉ cho S và báo cáo này. Không có giới hạn thời gian từ công cụ; dừng tạo ở đúng ngân sách 5/5 của phiếu.

