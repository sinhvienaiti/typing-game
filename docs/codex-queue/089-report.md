# Phiếu 089 · Tuyến Cuối · Sáu chân dung quái map 1

Ngày thực hiện: 28/10/2026. Người làm và tự chấm: Codex. Công cụ tạo ảnh: `image_gen` tích hợp; không dùng API ngoài hay CLI tạo ảnh.

**Kết quả:** đủ sáu bản chọn, tự chấm 9–9,5/10; cả sáu qua Kiểm 1–5. Chờ Claude chấm lại từ 8 để nhận và gắn vào bảng tin ở TS-M1-10.

## 1. Đầu ra và cách làm

- Sáu PNG và prompt bản chọn ở [`art-src/ui/foes/`](../../games/typing-survival/art-src/ui/foes/). Tổng cộng 12 lượt tạo: Brute 2, Swarm 2, Scout 2, Shield Guard 1, Splitter 2, Pack Leader 3. Giữ nguyên mọi `.tryN.png` và `.tryN.prompt.txt`.
- Bản thô từ công cụ, prompt tương ứng, tham số co/đệm, chương trình kiểm và số đo ở [`art-src/_review/089/`](../../games/typing-survival/art-src/_review/089/). Không ghi đè ảnh cũ hay lượt thử.
- Làm Brute trước; dùng Brute lượt 2 làm chuẩn chất liệu và hướng sáng cho năm quái còn lại. Mỗi lượt đều đưa ảnh `rainbow-*` tương ứng vào làm tham chiếu hình, không lấy màu. Đọc lớp Bầy Hố Đen trong `crowd.ts`; không dùng `title-horizon.png` làm mẫu.
- Công cụ trả ảnh 1254×1254. Dùng ImageMagick chỉ co đồng tỉ lệ và đặt lên canvas alpha 1024×1024 trước khi lưu lượt thử; giữ màu và alpha do công cụ tạo, không tô lại, không khóa màu hậu kỳ, không vẽ thêm. Các bản chọn là bản chép giống hệt lượt thử được chọn, cả PNG lẫn prompt (12/12 phép so sánh byte đúng).

## 2. Tự chấm từng lượt

Đã xem từng lượt ở khổ đầy đủ và 96 px trên nền `#0B0E14`. Năm tiêu chí theo ART_ACCEPTANCE §1, áp dụng ngưỡng ảnh 2D ở §2.2. Thứ tự trong cột điểm: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**, mỗi mục tối đa 2.

| Quái | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Còn thiếu |
|---|---:|---|---|---:|---|
| Brute | 1 | Dựng theo rainbow-tank; giáp than chì, gân hổ phách, đầu cúi. | 1,5 / 2 / 1 / 2 / 1 | 7,5 | Ánh cam lan vào giáp; S > 0,5 chiếm 33,29 %, không qua Kiểm 5. |
| Brute | 2 | Thu nửa bề rộng gân; giữ bóng giáp xám trung tính, hạn chế ánh cam tràn. | 1,5 / 1,5 / 2 / 2 / 2 | 9 | Dáng còn nhiều cánh theo mẫu; hộp bao rộng 72,4 % thay vì khoảng 80 %; vẫn lớn hơn Scout. |
| Swarm | 1 | Cầu gai nhỏ, lõi tròn, gân cam nóng; lấy Brute làm chuẩn vật liệu. | 1,5 / 2 / 1 / 2 / 1 | 7,5 | Khe và vòng chân gai phủ cam quá rộng: 39,50 %; không qua Kiểm 5. |
| Swarm | 2 | Giữ cả khe tối trung tính; thu gân và ánh tràn còn một phần ba, thu lõi cam. | 1,5 / 2 / 2 / 2 / 2 | 9,5 | Góc nhìn gần chính diện hơn góc ba phần tư; hình cầu vẫn có khối. |
| Scout | 1 | Côn trùng thon, nghiêng về trước, gân xanh điện; cùng vật liệu Brute. | 1,5 / 2 / 1 / 2 / 1 | 7,5 | Mảng xanh ở vai, chân và cánh làm tỷ lệ bão hòa cao 27,60 %; không qua Kiểm 5. |
| Scout | 2 | Thay mảng xanh rộng bằng than chì; chỉ để gân mảnh và mắt nhỏ, khử ám màu vùng bóng. | 2 / 2 / 1,5 / 2 / 2 | 9,5 | Mặt giáp hơi nhiều cạnh so với khối 3D đơn giản; cùng họ với cả bộ. |
| Shield Guard | 1 | Giữ côn trùng có sừng đi khom sau khiên hai thùy; viền trong khiên xanh lam. | 1,5 / 2 / 2 / 2 / 2 | 9,5 | Góc gần chính diện; lề trên 49 px, đủ ngưỡng 48 px nhưng ít dư. |
| Splitter | 1 | Hai thùy phồng, bốn chân cong, khe tách dọc và gân cam đỏ. | 1,5 / 2 / 1 / 2 / 1 | 7,5 | Ánh cam đỏ lan vào chân, khe tối: 31,85 % bão hòa cao; không qua Kiểm 5. |
| Splitter | 2 | Giữ hai thùy; giảm ánh tràn còn một phần tư, ưu tiên khe tách dọc, giáp xám trung tính. | 1,5 / 2 / 1,5 / 2 / 2 | 9 | Hai thùy còn cạnh hơn cảm giác phập phồng; góc gần chính diện. |
| Pack Leader | 1 | Cùng loài Brute, lớn hơn, gân vàng kim dày và sáng. | 1 / 2 / 1 / 2 / 1 | 7 | Đầu còn cúi như Brute; vùng bão hòa cao 40,63 %; không qua Kiểm 5. |
| Pack Leader | 2 | Nâng đầu lên trên vai, dựng ngực; giảm số nhánh gân và ánh vàng trên giáp. | 2 / 2 / 1 / 2 / 0,5 | 7,5 | Tư thế đã rõ nhưng bão hòa cao vẫn 35,06 %; không qua Kiểm 5. |
| Pack Leader | 3 | Khóa tư thế lượt 2; dùng vàng kim nhạt #FFE4A3/#FFF0C8, ít nhánh, lõi vàng đậm rất nhỏ. | 2 / 2 / 1,5 / 2 / 2 | 9,5 | Vàng kim thiên kem sáng hơn vàng đậm; chủ ý giữ gân dày và sáng mà thân vẫn trung tính. |

Không tạo thêm sau khi một lượt đạt điểm và các cổng kỹ thuật. Các lượt bị loại có vấn đề vật liệu hoặc tư thế nêu ngay trong bảng; không dùng ảnh dưới ngưỡng làm bản chọn.

## 3. Bản chọn và lý do

| Quái | Bản chọn | Điểm | Lý do |
|---|---|---:|---|
| Swarm | [`swarm.png`](../../games/typing-survival/art-src/ui/foes/swarm.png) ← `.try2` | 9,5 | Cầu gai gọn, bề ngang 55,2 %; lõi và gân cam rõ, giáp tối trung tính. |
| Scout | [`scout.png`](../../games/typing-survival/art-src/ui/foes/scout.png) ← `.try2` | 9,5 | Thân thon, nghiêng về trước; gân xanh điện, dáng hẹp hơn Brute. |
| Brute | [`brute.png`](../../games/typing-survival/art-src/ui/foes/brute.png) ← `.try2` | 9 | Đầu cúi, giáp dày, dáng rộng hơn Scout; hổ phách đậm tách khỏi vàng sáng của đầu đàn. |
| Shield Guard | [`shield-guard.png`](../../games/typing-survival/art-src/ui/foes/shield-guard.png) ← `.try1` | 9,5 | Khiên hai thùy và viền xanh là nét chính, nhận ra ngay ở 96 px. |
| Splitter | [`splitter.png`](../../games/typing-survival/art-src/ui/foes/splitter.png) ← `.try2` | 9 | Hai thùy phồng và rãnh dọc sáng cam đỏ đọc rõ, không lẫn cầu gai Swarm. |
| Pack Leader | [`pack-leader.png`](../../games/typing-survival/art-src/ui/foes/pack-leader.png) ← `.try3` | 9,5 | Đầu và ngực nâng cao; cùng loài Brute nhưng khung lớn hơn, gân vàng kim nhạt dày và sáng hơn. |

Lưu ý khi Claude duyệt: Brute còn nhiều cánh như ảnh mẫu và rộng 72,4 % thay vì khoảng 80 %. Pack Leader rộng 75,4 % và cao 820 px, so với Brute 741×760 px; khác biệt còn đến từ tư thế ngẩng và gân vàng sáng. Swarm, Shield Guard và Splitter nhìn gần chính diện hơn yêu cầu ba phần tư. Đây là các điểm trừ đã tính, không che bằng khung hay nền.

## 4. Kiểm bắt buộc

### Kiểm 1 · KA1 MD5

Chạy `/sbin/md5 -r` đệ quy trước khi tạo ảnh: **95 file**. Lượt sau: **188 file trong ảnh chụp danh sách**, gồm **93 file mới**. **95/95 file gốc giữ nguyên MD5; 0 file đổi; 0 file mất.** `diff -u`: 93 dòng thêm của file mới, 0 dòng xóa; mã thoát 1 do có file mới. **Đạt.**

Đối chiếu: [`md5-before.txt`](../../games/typing-survival/art-src/_review/089/md5-before.txt), [`md5-after.txt`](../../games/typing-survival/art-src/_review/089/md5-after.txt), [`md5-diff.txt`](../../games/typing-survival/art-src/_review/089/md5-diff.txt), [`ka1-result.json`](../../games/typing-survival/art-src/_review/089/ka1-result.json).

Danh sách mỗi lượt được chốt trước khi ghi file kết quả của chính lượt đó để tránh tự băm. Ba file sinh sau ảnh chụp danh sách cuối là `md5-after.txt`, `md5-diff.txt`, `ka1-result.json`; không nằm trong chính `md5-after.txt`. Báo cáo nằm ngoài cây `art-src`.

### Kiểm 2 · Khổ

Đầu ra `magick identify -format` cho sáu bản chọn:

```text
swarm.png 1024x1024 srgba 4.0
scout.png 1024x1024 srgba 4.0
brute.png 1024x1024 srgba 4.0
shield-guard.png 1024x1024 srgba 4.0
splitter.png 1024x1024 srgba 4.0
pack-leader.png 1024x1024 srgba 4.0
```

Cả sáu **1024×1024**, có kênh alpha. **Đạt.**

### Kiểm 3 · Alpha

Đo RGBA 8 bit bằng ImageMagick; mỗi dải mép có 16×1024 = 16.384 pixel. Luma = `(0,2126R + 0,7152G + 0,0722B) / 255` trên pixel có alpha 1–254; không ghép nền trước khi đo.

| Quái | Alpha min–max | Alpha 0 ở mép trên / phải / dưới / trái (%) | Pixel alpha 1–254 | Luma trung bình |
|---|---|---|---:|---:|
| Swarm | 0–255 | 100,0000 / 100,0000 / 100,0000 / 100,0000 | 162846 | 0,26408 |
| Scout | 0–255 | 100,0000 / 100,0000 / 100,0000 / 100,0000 | 212345 | 0,26963 |
| Brute | 0–255 | 100,0000 / 100,0000 / 100,0000 / 100,0000 | 302446 | 0,26970 |
| Shield Guard | 0–255 | 99,7437 / 100,0000 / 100,0000 / 100,0000 | 364912 | 0,26826 |
| Splitter | 0–255 | 100,0000 / 100,0000 / 100,0000 / 100,0000 | 224998 | 0,26276 |
| Pack Leader | 0–255 | 100,0000 / 100,0000 / 100,0000 / 100,0000 | 317117 | 0,32819 |

Cả sáu alpha min 0, max 255; từng dải mép ≥99 %; luma vùng alpha chuyển tiếp ≤0,35. Xem trên nền tối không thấy viền nền trắng. **Đạt.**

### Kiểm 4 · Khung đều

Đo đúng lệnh trong phiếu:

```sh
magick <ảnh> -alpha extract -threshold 6% -trim -format '%X %Y %w %h' info:
```

Đáy hộp bao tính `y + h`; lề ghi theo trái / trên / phải / dưới.

| Quái | Đầu ra `%X %Y %w %h` | Lề L/T/R/B (px) | Đáy y | Bề ngang / canvas |
|---|---|---|---:|---:|
| Swarm | `+229 +333 565 537` | 229 / 333 / 230 / 154 | 870 | 55,18 % |
| Scout | `+202 +123 620 747` | 202 / 123 / 202 / 154 | 870 | 60,55 % |
| Brute | `+142 +110 741 760` | 142 / 110 / 141 / 154 | 870 | 72,36 % |
| Shield Guard | `+143 +49 738 821` | 143 / 49 / 143 / 154 | 870 | 72,07 % |
| Splitter | `+152 +258 721 612` | 152 / 258 / 151 / 154 | 870 | 70,41 % |
| Pack Leader | `+126 +50 772 820` | 126 / 50 / 126 / 154 | 870 | 75,39 % |

Lề nhỏ nhất toàn bộ là **49 px ≥48**; đáy cả sáu ở **y=870**, trong 840–900 (84,96 % chiều cao). **Đạt.**

### Kiểm 5 · Không còn màu cầu vồng

Saturation dùng HSV: `(max(R,G,B) − min(R,G,B)) / max(R,G,B)`, đặt 0 khi max bằng 0. Mẫu số chỉ gồm pixel alpha >128. Đếm nghiêm ngặt `S > 0,5`; không loại gân khỏi mẫu số.

| Quái | Pixel alpha >128 | Pixel S >0,5 | Tỷ lệ | Kết quả |
|---|---:|---:|---:|---|
| Swarm | 159093 | 23591 | 14,828 % | Đạt ≤25 % |
| Scout | 199298 | 33924 | 17,022 % | Đạt ≤25 % |
| Brute | 288919 | 60851 | 21,062 % | Đạt ≤25 % |
| Shield Guard | 351142 | 73797 | 21,016 % | Đạt ≤25 % |
| Splitter | 217399 | 45313 | 20,843 % | Đạt ≤25 % |
| Pack Leader | 300887 | 25821 | 8,582 % | Đạt ≤25 % |

Đã xem lại chất liệu: thân than chì mờ, không giữ mảng màu cầu vồng của nguồn; các màu cam, xanh và vàng tập trung vào năng lượng. **Đạt.**

Số đo đầy đủ: [`measurements-final.json`](../../games/typing-survival/art-src/_review/089/measurements-final.json); cả 12 lượt: [`measurements-attempts.json`](../../games/typing-survival/art-src/_review/089/measurements-attempts.json); kiểm bản chép: [`selection-copy-check.json`](../../games/typing-survival/art-src/_review/089/selection-copy-check.json).

### Kiểm 6 · Tờ xem nhanh

- [`089-sheet.jpg`](../../games/typing-survival/art-src/_review/089-sheet.jpg): **3216×1152**; hàng 1 sáu bản chọn trên nền `#0B0E14`, mỗi ảnh 512×512; hàng 2 sáu nguồn tương ứng 512×512; có tên tiếng Anh. Chỉ bỏ nền xanh chroma của nguồn trong bộ nhớ khi ghép tờ xem, không sửa ảnh nguồn.
- [`089-small.jpg`](../../games/typing-survival/art-src/_review/089-small.jpg): **1056×318**; hàng 1 ảnh 96×96, hàng 2 ảnh 64×64, nền `#0B0E14`, có nhãn. Đã xem trực tiếp cả hai tờ.
- Ở 96 px: Swarm là cầu gai nhỏ cam; Scout thon xanh; Brute rộng hổ phách; Shield Guard có khiên xanh; Splitter hai thùy cam đỏ; Pack Leader đầu cao và gân vàng sáng. Sáu con tách được bằng hình và màu gân. Ở 64 px, gân phụ và phần chân khuất giảm rõ nhưng các nét chính còn đọc được.

## 5. Phạm vi bỏ qua và việc cần người nhận xem

- Không gắn ảnh vào bảng tin: đó là TS-M1-10 của Claude, ngoài phạm vi phiếu này. Không sửa mã game, tài liệu khác, kho ảnh Space Typing, hay khu vực Tu Tiên. Không chạy lệnh Git, build, test suite, dev server hoặc trình duyệt. Không tạo âm thanh.
- Tờ xem là kiểm ảnh tĩnh; chưa có bằng chứng bố cục bảng tin trong game. Claude cần chấm lại đủ sáu ảnh, đặc biệt cặp Brute / Pack Leader ở 96 px và độ lớn của Brute đã ghi ở trên. Chỉ nhận khi điểm chấm lại từ 8.
- Các ảnh, prompt và bằng chứng đều ở đúng nhánh đường dẫn được phép; `art-src` là media, không đưa vào Git.
