# Phiếu 069 · MF-I3 · Sprite sự sống A: chim và bướm

Ngày thực hiện: 28/10/2026. Công cụ ảnh: `image_gen` tích hợp, nền alpha thật; hai lần gọi, một cho mỗi tờ. Hậu xử lý cắt/căn ô, thu nhỏ và khóa màu bằng ImageMagick 7 trên macOS. Không dùng mạng ngoài công cụ tạo ảnh.

## 1. Trạng thái bàn giao

**Chưa đóng phiếu:** chim đã có bản chọn đạt; bướm đã có ứng viên sửa đạt tại `butterfly.try2.png`, nhưng file tên chuẩn `butterfly.png` còn là bản chưa đạt nối vòng.

Tôi đã ghi `butterfly.png` trước khi chạy xong kiểm tra nối vòng. Đây là lỗi thứ tự thao tác. Tôi giữ nguyên file đó theo luật không ghi đè và đã gửi câu hỏi xin phép thay duy nhất PNG này bằng ứng viên sửa đạt. Tại thời điểm ghi báo cáo chưa có trả lời; không xem thời gian chờ là đồng ý.

| Món | File nên duyệt | Tự chấm | Trạng thái |
|---|---|---:|---|
| Bird Flap | [`bird-flap.png`](../../games/dragon-hold/art-src/fx/life/bird-flap.png), giống byte với `bird-flap.try2.png` | 8,75/10 | Đạt các kiểm tài sản |
| Butterfly | [`butterfly.try2.png`](../../games/dragon-hold/art-src/fx/life/butterfly.try2.png) | 9/10 | Đạt các kiểm tài sản; chờ phép chép lên tên chuẩn |
| Butterfly, bản ghi sớm | [`butterfly.png`](../../games/dragon-hold/art-src/fx/life/butterfly.png) | 7,5/10 | **Không dùng:** sai khác nối vòng vượt ngưỡng |

Claude chưa chấm lại. Không tuyên bố đã được nhận hoặc đã kiểm chuyển động trong game.

## 2. File tạo ra

Trong `games/dragon-hold/art-src/fx/life/`, tổng cộng 14 file mới:

- `bird-flap.png`, `bird-flap.prompt.txt`, `bird-flap.json`.
- `bird-flap.try1.png`, `bird-flap.try1.prompt.txt`, `bird-flap.try2.png`, `bird-flap.try2.prompt.txt`.
- `butterfly.png`, `butterfly.prompt.txt`, `butterfly.json`.
- `butterfly.try1.png`, `butterfly.try1.prompt.txt`, `butterfly.try2.png`, `butterfly.try2.prompt.txt`.

Bằng chứng trong phạm vi được phép:

- [Tờ xem nền sáng/tối, cỡ đầy đủ, 128 px và chim khoảng 8–14 px](../../games/dragon-hold/art-src/_review/MF-I3-contact.jpg).
- [Số đo chi tiết từng ô, từng hàng và từng bản](../../games/dragon-hold/art-src/_review/MF-I3/validation.json).
- [MD5 trước](../../games/dragon-hold/art-src/_review/MF-I3/md5-before.txt), [MD5 sau](../../games/dragon-hold/art-src/_review/MF-I3/md5-after.txt), [diff](../../games/dragon-hold/art-src/_review/MF-I3/md5-diff.txt).
- `_review/MF-I3/{bird-flap,butterfly}-source.try1.png` và các `.prompt.txt` cùng tên: giữ nguyên ảnh công cụ trả về và nguyên văn prompt đã gửi.
- `_review/MF-I3/normalize.py`, `normalize-symmetric-loop.py`, `validate.py`: thao tác căn ô và cách đo để đối chiếu. Các script từ chối ghi đè đầu ra.
- `_review/MF-I3/{bird-flap,butterfly}-preview.jpg`, `butterfly-try2-preview.jpg`, `butterfly-anchor-inspection.jpg`: ảnh kiểm tra tĩnh, không phải ảnh chụp game.

Không xóa ảnh nguồn hoặc file thử. Ảnh kiểm tra đều nằm dưới `_review/MF-I3*`; không có khung chụp trình duyệt cần dọn.

## 3. Nội dung và cách chuẩn hóa

Bird Flap có ba hàng: thân tròn đuôi xòe ngắn; thân thon, cánh nhọn, đuôi chẻ; thân gọn với cánh rộng. Mỗi hàng tám pha, hướng đầu lên trên, góc nhìn cao theo brief, màu xám nâu sẫm. Ảnh nguồn 2.048 × 768 px. Thu nhỏ cả tờ trực tiếp làm một số đầu cánh cắt qua biên ô, nên lượt sửa cắt riêng 24 sprite, giữ chung tỉ lệ 0,185 và neo theo thân vào ô 64 px. Bản chọn 512 × 192 px.

Butterfly có ba hàng kem, xanh lơ nhạt, tím lavender nhạt hơn `#8E7CC3`. Ảnh nguồn thực tế công cụ trả về là 1.448 × 1.086 px; prompt yêu cầu 1.024 × 768 px. Lượt sửa lấy từng con riêng và neo theo thân, sau đó ghép vào tờ 128 × 96 px. Pha cánh khép được giảm chiều cao để thân không dài đột ngột so với các pha mở. Chu kỳ bốn khung là **mở – nửa – khép – nửa**; hai pha nửa cánh dùng chung raster nguồn do công cụ tạo, cách ghép đối xứng thông thường cho vòng bốn khung. Không đảo thứ tự khung để né kiểm nối vòng.

Hai tờ dùng HSV saturation tối đa 0,30; alpha nhỏ hơn 0,08 được đưa về 0, RGB tại pixel trong suốt hoàn toàn được đưa về 0. Giữ alpha mềm còn lại; không nướng nền sáng hoặc tối vào sprite. Chỉ dùng ImageMagick để cắt, căn, thu nhỏ, chuẩn hóa màu/alpha và ghép; không vẽ chim hoặc bướm bằng mã.

Các `.try1.prompt.txt` là nguyên văn prompt gửi `image_gen`. Các `.try2.prompt.txt` giữ nguyên văn đó và thêm ghi chú hậu xử lý. **Lượt 2 là sửa bố trí từ ảnh nguồn lượt 1, không phải lần gọi tạo ảnh thứ hai cho cùng món.** File prompt tên chuẩn giữ nguyên prompt nguồn; cách chuẩn hóa ghi tại đây và trong script.

JSON giữ đúng năm khóa yêu cầu:

```json
{"cell":64,"cols":8,"rows":3,"frames":8,"loop":true}
{"cell":32,"cols":4,"rows":3,"frames":4,"loop":true}
```

`frames` là số khung trong một chu kỳ **mỗi hàng**, không phải số ô toàn tờ. Chọn hàng theo dáng chim hoặc màu bướm rồi chạy ngang các cột; không nối hàng này sang hàng khác.

## 4. KA1 · Bảo toàn file

Thư mục đích `art-src/fx/life` chưa tồn tại trước lượt này: 0 file cũ. Đã lập `md5-before.txt` trước khi ghi ảnh, rồi chạy thực sự `md5 -r` cho từng file đích và lưu `md5-after.txt`.

`diff` là `0a1,14`, chỉ có 14 dòng file mới; không có dòng bị xóa hoặc thay đổi. Không ghi đè, đổi tên hay xóa file nào. Không chạy lệnh Git nào.

MD5 bản chim chọn và `bird-flap.try2.png`: `a841f1343d16b6b6c05d33ace82d2d14`. MD5 ứng viên bướm đạt: `7aed57c6a0a7deb209fef72d71f97763`. MD5 bướm tên chuẩn chưa đạt: `cb012b5de100c2a8656163343e503c3c`.

## 5. KA2, lưới, alpha, dung lượng và KA4

Khổ và kênh được đọc bằng `magick identify`; các kiểm pixel đọc raster RGBA 8 bit do ImageMagick giải mã. Mọi bản dưới đây đều có đúng khổ toàn tờ và RGBA; biên ô phải xét riêng, không chỉ chia hết kích thước.

| File | Khổ; lưới | Byte | Lề alpha nhỏ nhất trong ô | Alpha ở biên ô | KA4 |
|---|---|---:|---:|---|---:|
| `bird-flap.try1.png` | 512 × 192; 8 × 3 ô 64 | 64.212 | 0 px | Chưa đạt | 0 % |
| `bird-flap.try2.png` = `bird-flap.png` | 512 × 192; 8 × 3 ô 64 | 40.442 | 6 px | 0 ở toàn bộ biên | 0 % |
| `butterfly.try1.png` | 128 × 96; 4 × 3 ô 32 | 17.941 | 0 px | Chưa đạt | 0 % |
| `butterfly.png`, bản ghi sớm | 128 × 96; 4 × 3 ô 32 | 9.567 | 4 px | 0 ở toàn bộ biên | 0 % |
| `butterfly.try2.png` | 128 × 96; 4 × 3 ô 32 | 7.433 | 4 px | 0 ở toàn bộ biên | 0 % |

Mỗi PNG dưới cả 256.000 byte lẫn 256 KiB. Bản chim chọn có 86.977 pixel alpha 0, 11.327 pixel hiện, 9.512 pixel alpha bán trong suốt; alpha khác 0 nhỏ nhất 20/255. Bướm sửa có 10.230 pixel alpha 0, 2.058 pixel hiện, 1.568 pixel alpha bán trong suốt; alpha khác 0 nhỏ nhất 21/255. Cả hai có **0 pixel alpha 0 nhưng RGB khác 0**; toàn bộ dải 2 px quanh mỗi ô trong suốt hoàn toàn. Đã xem mép trên cả nền sáng và tối, không thấy viền nền bị nướng hoặc cánh tràn ô ở hai bản đạt.

KA4: đếm pixel alpha > 0 có hue trong 0–50° hoặc 165–190°, saturation > 0,55 và value > 0,5. Tất cả các bản có **0 pixel**, tương ứng 0 % trên cả số pixel hiện lẫn toàn canvas.

KA3 nền phẳng `#E6E6E6`, thống kê 10 px mép và lề Tripo 24 px không áp dụng: đây là sprite alpha, không phải ảnh nguồn Tripo.

## 6. Kiểm nối vòng

MAE chính là trung bình trị tuyệt đối sai khác từng kênh RGBA, trên toàn bộ một ô, thang 0–255; gồm alpha và pixel trống. Đo các cặp liền kề trong cùng hàng, so cặp cuối → đầu với giá trị lớn nhất. Kiểm thêm RGBA đã nhân alpha để tránh dựa vào RGB ẩn. Cả hai cách đều phải đạt cho ứng viên chọn. Không đổi công thức giữa các hàng hoặc các bản.

| Bản | Hàng | MAE cuối → đầu | MAE liền kề lớn nhất | Kết quả |
|---|---:|---:|---:|---|
| Chim chọn / lượt sửa 2 | 1 | 5,463562 | 12,132263 | Đạt |
| | 2 | 6,788574 | 10,175781 | Đạt |
| | 3 | 5,001526 | 10,270874 | Đạt |
| Bướm tên chuẩn ghi sớm | 1 | 28,689941 | 26,804443 | Trượt |
| | 2 | 31,751953 | 29,753418 | Trượt |
| | 3 | 25,776611 | 22,981201 | Trượt |
| Bướm lượt sửa 2 | 1 | 26,804443 | 26,804443 | Đạt |
| | 2 | 29,753418 | 29,753418 | Đạt |
| | 3 | 21,925293 | 22,981201 | Đạt |

Kiểm RGBA nhân alpha, ghi dạng “cuối → đầu / liền kề lớn nhất”:

- Chim: `5,192354 / 11,427036`; `6,287239 / 9,468037`; `4,797775 / 9,808936` — cả ba đạt.
- Bướm sửa: `25,299610 / 25,299610`; `28,130252 / 28,130252`; `20,613493 / 21,428147` — cả ba đạt.

Số đo cặp liền kề đầy đủ, hai bản thu nhỏ trực tiếp ban đầu và tọa độ hộp alpha từng ô nằm trong `validation.json`. Chim lượt 1 qua kiểm nối vòng nhưng trượt biên ô; bướm lượt 1 trượt biên ô và hàng đầu trượt phép đo RGBA nhân alpha.

## 7. KA5 · Tự chấm theo năm tiêu chí

Thứ tự: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng được cho bước sau**; mỗi tiêu chí tối đa 2. Điểm kết luận lấy mức thấp hơn giữa cỡ đầy đủ và bản rộng 128 px. Với bướm, cỡ đầy đủ chính là 128 px.

| Bản | Cỡ đầy đủ: năm điểm | Tổng | Cỡ 128 px: năm điểm | Tổng |
|---|---|---:|---|---:|
| Chim lượt 1, thu nhỏ trực tiếp | 2 / 1,5 / 1,75 / 1,75 / 0,5 | 7,5 | 2 / 1,25 / 1,75 / 1,75 / 0,5 | 7,25 |
| Chim lượt sửa 2, bản chọn | 2 / 1,75 / 1,75 / 1,5 / 2 | 9 | 2 / 1,5 / 1,75 / 1,5 / 2 | **8,75** |
| Bướm lượt 1, thu nhỏ trực tiếp | 2 / 1,5 / 1,75 / 1,75 / 0,5 | 7,5 | Như cỡ đầy đủ | 7,5 |
| Bướm tên chuẩn ghi sớm | 2 / 1,75 / 1,75 / 1,5 / 0,5 | 7,5 | Như cỡ đầy đủ | 7,5 |
| Bướm lượt sửa 2, ứng viên chọn | 2 / 1,75 / 1,75 / 1,5 / 2 | **9** | Như cỡ đầy đủ | **9** |

Lý do chọn: chim sửa giữ dáng thân/đuôi khác nhau, đọc được ở bản nhỏ, cánh không bị cắt và các vòng đạt. Trừ điểm vì pha khép ở 8 px gom thành dấu nhỏ, nét lông phần lớn mất khi thu nhỏ, thân vẫn có dao động nhẹ. Bướm sửa giữ ba màu nhạt, rõ bốn thùy khi mở, không lẫn màu tín hiệu, hai pha nửa cánh đối xứng giữ nhịp vòng. Trừ điểm vì râu và chi tiết cánh mất ở cỡ nhỏ, dáng khép vẫn đơn giản và góc nhìn chưa được đối chiếu trong camera game. Đây là tự chấm tài sản tĩnh; Claude cần xem lại trước khi nhận.

## 8. Việc bỏ qua và việc chủ dự án cần xem

- Không sửa mã game, tài liệu kế hoạch, hàng đợi hoặc danh sách thay ảnh; chỉ ghi báo cáo được giao và media/bằng chứng đúng phạm vi.
- Không chạy build, test suite, dev server, trình duyệt, đẩy media hoặc bất kỳ lệnh Git nào. Không đọc/ghi Tu Tiên và không đụng game khác.
- Không tạo âm thanh: phiếu không yêu cầu.
- Không chứng nhận tích hợp, chi phí draw call, hiệu năng hoặc dải chuyển động 10 giây trong game; đó là bước tiếp theo của lớp L8, ngoài phiếu ảnh này.
- Chủ dự án cần quyết định việc thay duy nhất `butterfly.png` bằng `butterfly.try2.png`. Nếu giữ luật không ghi đè cả file mới tạo trong phiên này, ứng viên đạt vẫn được giao ở tên `.try2.png`, còn phiếu chưa hoàn tất điều kiện tên bản chọn.
- Claude cần chấm lại hai bản đạt từ tờ xem và PNG alpha; chỉ nhận khi chấm lại từ 8 điểm.
