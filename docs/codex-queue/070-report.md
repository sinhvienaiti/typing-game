# Phiếu 070 · MF-I4 · Sprite sự sống B: lá rơi, khói, đom đóm, bóng mây

Ngày thực hiện: 28/10/2026, Mac mini M4, macOS. Dùng công cụ tích hợp **`image_gen`**, bốn lượt gọi, mỗi tài sản một lượt; chuẩn hóa bằng ImageMagick 7. **Bốn bản chọn đạt kiểm kỹ thuật và tự chấm 9–9,5/10; chờ Claude chấm lại từ 8 điểm để nhận.**

## File giao

Thư mục: [`games/dragon-hold/art-src/fx/life/`](../../games/dragon-hold/art-src/fx/life/). Mỗi tên dưới đây có `.png`, `.json`, `.prompt.txt`, `.try1.png` và `.try1.prompt.txt`. Prompt giữ nguyên văn chuỗi đã gửi công cụ; bản chọn giống nguyên byte với bản `try1` sau chuẩn hóa.

| Ảnh chọn | Nội dung và lưới JSON | Khổ | Dung lượng |
|---|---|---:|---:|
| [`leaf-fall.png`](../../games/dragon-hold/art-src/fx/life/leaf-fall.png) | 4 hàng biến thể × 4 cột góc xoay, ô 32 px | 128 × 128 | 22.419 B; 21,89 KiB |
| [`smoke-puff.png`](../../games/dragon-hold/art-src/fx/life/smoke-puff.png) | 6 khung từ trái sang phải, ô 128 px | 768 × 128 | 59.984 B; 58,58 KiB |
| [`firefly.png`](../../games/dragon-hold/art-src/fx/life/firefly.png) | Một chấm sáng, một ô 32 px | 32 × 32 | 1.235 B; 1,21 KiB |
| [`cloud-shadow.png`](../../games/dragon-hold/art-src/fx/life/cloud-shadow.png) | Một ô độ sáng, lặp hai chiều | 512 × 512 | 28.520 B; 27,85 KiB |

Tất cả đều dưới **256 KiB**, đồng thời dưới 256.000 B. Lá, khói và đom đóm là PNG RGBA8, alpha thẳng; bóng mây là PNG xám **một kênh 8 bit**, không có alpha.

Ảnh sinh nguyên gốc và prompt nằm tại [`_review/MF-I4/`](../../games/dragon-hold/art-src/_review/MF-I4/) với tên `<tên>.source.{png,prompt.txt}`. Nguồn lá, đom đóm và mây có khổ thực 1254²; nguồn khói 1536 × 1024. [Nhật ký tạo ảnh](../../games/dragon-hold/art-src/_review/MF-I4/generation-record.json) ghi đường dẫn nguồn do công cụ trả về.

Tờ duyệt đã mở xem:

- [Cỡ ảnh gốc, nền tối và sáng](../../games/dragon-hold/art-src/_review/MF-I4/native.jpg).
- [Mỗi tờ ảnh ở khung 128 px](../../games/dragon-hold/art-src/_review/MF-I4/atlas-128.jpg).
- [Từng ô lá phóng lên 128 px](../../games/dragon-hold/art-src/_review/MF-I4/leaf-cells-128.jpg).
- [Khói và đom đóm, từng ô 128 px](../../games/dragon-hold/art-src/_review/MF-I4/smoke-firefly-cells-128.jpg).
- [Mây gốc và dịch nửa ô](../../games/dragon-hold/art-src/_review/MF-I4/cloud-half-roll.jpg), [lát 2 × 2 ở cỡ gốc](../../games/dragon-hold/art-src/_review/MF-I4/cloud-tiled.jpg).

Mỗi ảnh trong thư mục duyệt đều có `.prompt.txt` cạnh nó; tờ ghép kèm prompt nguồn và mô tả thao tác ghép. Chữ chú thích chỉ xuất hiện trong tờ duyệt; ảnh tài sản không có chữ, logo, người, thần hoặc nơi thờ.

## Lượt thử, chuẩn hóa và bản chọn

Mỗi tài sản có đúng **một lượt sinh → `try1` → bản chọn**. Không cần lượt 2 hoặc 3 vì chuẩn hóa xong đã đạt. Giữ nguyên mọi ảnh thử và nguồn.

1. **Lá:** sinh bốn lá gốc trong lưới 2 × 2: Green Willow Leaf, Green Birch Leaf, Rust Maple Leaf, Copper Beech Leaf. Cắt từng ô, loại alpha dưới 0,04 để trim, thu vừa 24² rồi đặt giữa ô 32². Khóa hue lá xanh trong 88–125°; lá gỉ trong 10–30°, saturation tối đa 0,65, value tối đa 0,68. Mỗi lá được xoay hình học chính xác 0°, 90°, 180°, 270° để bốn khung giữ cùng dáng và chất liệu. Đây là xoay trong mặt phẳng, chưa phải chuyển động lật mặt hoặc phối cảnh. JSON có `frames: 4` **cho mỗi hàng biến thể**, tổng 16 ô; `rotationDegrees` và `variants` ghi rõ cách đọc.
2. **Khói:** sinh sáu khung trong lưới nguồn 3 × 2. Cắt cùng khổ, chuyển RGB sang xám, thu cùng tỉ lệ về 96² và đặt giữa ô 128². Giữ chung vị trí phát; làm mờ alpha ở mép, nhân độ đặc lần lượt 0,58 / 0,64 / 0,70 / 0,60 / 0,36 / 0,14 để cuối chuỗi tan dần. Xếp thành lưới 6 × 1. JSON đặt `loop: false`: phát từng làn, khi tích hợp có thể gối nhiều làn để thành khói liên tục.
3. **Đom đóm:** cắt vùng giữa 627² từ nguồn rồi thu về 32²; chỉ đưa alpha dưới 0,004 về 0. Giữ màu và quầng sáng từ ảnh sinh.
4. **Bóng mây:** chuyển sang xám, thu về 512²; làm mượt Gaussian sigma 16 với `virtual-pixel tile`, để bộ lọc lấy mẫu qua mép đối diện. Kết quả giữ nhiễu mây thấp tần, giảm đường nối. PNG chỉ chứa kênh xám; JSON ghi đây là dữ liệu mật độ để bộ tích hợp điều chỉnh cường độ trong vật liệu.

Thao tác nằm trong [normalize.py](../../games/dragon-hold/art-src/_review/MF-I4/normalize.py); phép đo nằm trong [measure.py](../../games/dragon-hold/art-src/_review/MF-I4/measure.py). Các script tạo mới trong thư mục duyệt để lưu vết, không sửa công cụ hay mã game. Khi dựng tờ lát mây, một lệnh `+clone` không chạy được; đã dùng `montage` với bốn đầu vào. Lỗi này không tạo file và không ảnh hưởng PNG. [review-commands.json](../../games/dragon-hold/art-src/_review/MF-I4/review-commands.json) ghi cách dựng thành công. Một thuộc tính phụ `png:color-type` của ImageMagick không đọc được; kiểu PNG được xác minh trực tiếp từ IHDR trong [validation.json](../../games/dragon-hold/art-src/_review/MF-I4/validation.json).

## KA1 · Giữ nguyên file có sẵn

Chạy `/sbin/md5 -r` trên **mọi file trong thư mục đích `fx/life`** trước và sau. Trước: **14 file**. Sau: **34 file**. **14/14 file cũ giữ nguyên**, không mất file; đúng **20 file mới** của bốn tên được phép. `diff -u` chỉ có dòng dữ liệu thêm, không có dòng dữ liệu bị bỏ hoặc sửa.

- [md5-before.txt](../../games/dragon-hold/art-src/_review/MF-I4/md5-before.txt)
- [md5-after.txt](../../games/dragon-hold/art-src/_review/MF-I4/md5-after.txt)
- [md5-diff.txt](../../games/dragon-hold/art-src/_review/MF-I4/md5-diff.txt)

| Ảnh chọn | MD5 |
|---|---|
| `leaf-fall.png` | `f12cb09ec53d7cbe49d7f743eee913c5` |
| `smoke-puff.png` | `463a2f6238013e6d7b5e5a867fd60820` |
| `firefly.png` | `cb48552b2036562294a2bf3fbd697a6b` |
| `cloud-shadow.png` | `a1c32eb39c57ad564baa3bb086664d9a` |

## KA2, KA3 · Khổ, lưới và alpha

`magick identify` xác nhận đúng bốn khổ ở bảng giao. Đã đối chiếu kích thước với `cell × cols`, `cell × rows`, kiểm JSON và IHDR; cả bốn đạt. Mọi phép đo dưới đây tính cả pixel alpha nhỏ hơn 50 %, không bỏ qua mép mờ.

| Tài sản | Pixel alpha > 0 | Pixel 0 < alpha < 255 | Lề trong suốt nhỏ nhất trong từng ô | Pixel thấy được ở dải mép ngoài 2 px |
|---|---:|---:|---:|---:|
| Lá, tổng 16 ô | 4.632 | 3.916 | 4 px, mọi ô | 0 |
| Khói, tổng 6 ô | 15.895 | 15.895 | 24 / 24 / 24 / 22 / 23 / 23 px | 0 |
| Đom đóm | 118 | 117 | 10 px | 0 |
| Mây | Toàn ô; không dùng alpha | 0 | Không áp dụng cho ô liền mép | Không áp dụng |

Khói có alpha lớn nhất từng khung **146 / 162 / 177 / 151 / 90 / 33** trên thang 255; không có lõi đục cứng. Đom đóm nằm trong bbox `[10,10,22,22]` của ô 32². Đã xem trên nền tối `#25342E` và sáng `#D9DFD0`: không thấy viền nền hay ô chữ nhật quanh sprite. Các ô không chạm nhau. Lề 24 px và nền `#E6E6E6` của nguồn Tripo không áp dụng cho bộ sprite này.

## KA4 · Màu giữ riêng

Đo hue trong `[0,50]` hoặc `[165,190]`, saturation > 0,55, value > 0,5; mẫu số là mọi pixel có alpha > 0, kể cả mép mờ. Bóng mây lấy toàn ô.

| Nhóm | Pixel thuộc dải giữ riêng / pixel thấy được | Tỉ lệ |
|---|---:|---:|
| Lá xanh Willow, 4 khung | 0 / 956 | **0 %** |
| Lá xanh Birch, 4 khung | 0 / 1.388 | **0 %** |
| Lá gỉ Maple, 4 khung — ngoại lệ | 504 / 1.424 | **35,3933 %** |
| Lá đồng Beech, 4 khung — ngoại lệ | 412 / 864 | **47,6852 %** |
| Khói | 0 / 15.895 | **0 %** |
| Đom đóm | 0 / 118 | **0 %** |
| Bóng mây | 0 / 262.144 | **0 %** |

Toàn tờ lá: **916 / 4.632 = 19,7755 %**, tất cả thuộc hai hàng lá gỉ được phép. Trung vị HSV của phần lá alpha ≥ 128, bốn góc xoay giống nhau:

| Lá gỉ | Hue | Saturation | Value | Dải MF-I2 |
|---|---:|---:|---:|---|
| Rust Maple Leaf | 17,1429° | 0,6493 | 0,4902 | Đạt 10–30°; S, V ≤ 0,70 |
| Copper Beech Leaf | 23,7037° | 0,6486 | 0,5255 | Đạt 10–30°; S, V ≤ 0,70 |

Lõi đom đóm alpha ≥ 128 có HSV trung vị **67,9245° / 0,2663 / 0,7765**, là vàng xanh nhạt; không dùng vàng kim `#FFC83A`. Hai lá xanh có hue trung vị khoảng 88°, hợp sắc rêu. Chi tiết từng ô trong [metrics.json](../../games/dragon-hold/art-src/_review/MF-I4/metrics.json).

## Bóng mây · Liền mép và thấp tần

Phép đo là `100 × |L₁ − L₂| / 255` giữa hai hàng/cột sát đường nối. Đã đo mép đối diện và đường nối ở giữa sau `-roll +256+256`; hai cách cho cùng kết quả.

| Hướng | Trung bình | Lớn nhất | Cổng ≤ 2 % |
|---|---:|---:|---|
| Trái–phải, đường nối dọc sau dịch nửa ô | **0,084252 %** | **0,392157 %** | Đạt |
| Trên–dưới, đường nối ngang sau dịch nửa ô | **0,106464 %** | **0,392157 %** | Đạt |

Ảnh chỉ chứa xám, miền giá trị **103–186/255**. Trung bình sai khác tuyệt đối với lọc trung bình 5 × 5 là **0,0000321** trên thang 0–1, xác nhận ít chi tiết cao tần. Đã xem ảnh dịch nửa ô và lát 2 × 2: chuyển tiếp mềm, không thấy đường nối sắc. Mẫu mây lặp lại vẫn nhận ra khi nhìn cả tờ lát lớn; đây là một ô nguồn, chưa phải đánh giá chuyển động bóng mây trong game.

## KA5 · Tự chấm từng lượt

Theo năm tiêu chí của ART_ACCEPTANCE §1–2.2, mỗi tiêu chí 0–2: **đúng đề / đọc được trong game / hợp bộ / hình khối / dùng cho bước sau**. Chấm dựa trên xem tài sản tĩnh ở cỡ gốc và 128 px; chưa chứng minh chất lượng chuyển động hay độ rõ trong cảnh game thật.

| Lượt và bản chọn | Cỡ đầy đủ | Tổng | Cỡ 128 px | Tổng | Kết luận |
|---|---|---:|---|---:|---|
| `leaf-fall.try1` → `leaf-fall.png` | 2 / 1,5 / 1,5 / 2 / 2 | **9** | 2 / 1,5 / 1,5 / 2 / 2 | **9** | Đạt tự chấm |
| `smoke-puff.try1` → `smoke-puff.png` | 2 / 1,5 / 2 / 1,5 / 2 | **9** | 2 / 1,5 / 2 / 1,5 / 2 | **9** | Đạt tự chấm |
| `firefly.try1` → `firefly.png` | 2 / 1,5 / 2 / 2 / 2 | **9,5** | 2 / 1,5 / 2 / 2 / 2 | **9,5** | Đạt tự chấm |
| `cloud-shadow.try1` → `cloud-shadow.png` | 2 / 2 / 2 / 1,5 / 2 | **9,5** | 2 / 2 / 2 / 1,5 / 2 | **9,5** | Đạt tự chấm |

Lá có dáng phân biệt tốt nhưng hơi thiên về tranh thực vật; lá Willow mảnh và chi tiết gân giảm ở 32 px. Khói có đường cong mềm, cuối chuỗi nhạt đúng chủ ý; chỉ sáu khung nên độ liền chuyển động cần người tích hợp kiểm tiếp. Đom đóm dịu, giảm độ nổi trên nền sáng. Mây mượt và liền mép, còn cảm giác lặp của một mẫu duy nhất khi lát diện rộng. Các điểm trừ này đã tính vào bảng.

## Phần bỏ qua và việc cần xem

Không bỏ tài sản nào trong bốn tài sản yêu cầu. Không tạo thêm lượt vì lượt đầu đã đạt. Không có âm thanh hay nguồn Tripo trong phiếu. Không tích hợp runtime, không chạy Git, build, test, dev server, trình duyệt hoặc mạng ngoài công cụ tạo ảnh; không đọc hay ghi game Tu Tiên và không sửa tài liệu hoặc mã ngoài phạm vi giao.

**Claude cần chấm lại bốn bản cuối từ 8 điểm để nhận**, ưu tiên xem lá ở 32 px và độ nhẹ của khói, đom đóm trên nền sáng. Khi tích hợp cần phát đúng hàng biến thể lá, giữ alpha thẳng, phát khói một lượt rồi gối các làn và dùng mây như dữ liệu độ sáng. Chưa có kiểm chuyển động trong game vì phiếu cấm chạy game.
