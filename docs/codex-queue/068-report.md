# Phiếu 068 · MF-I6 · Tờ decal mép và cổng pine-river

Ngày thực hiện: 28/10/2026, Mac mini M4, macOS. Dùng công cụ tạo ảnh tích hợp `image_gen`, hai lượt gọi; chuẩn hóa bằng ImageMagick 7. **Bản cuối đạt các kiểm của phiếu, tự chấm 9/10; chờ Claude chấm lại.**

## File giao

- [Ảnh chọn `edge-gate-sheet.png`](../../games/dragon-hold/art-src/decals/pine-river/edge-gate-sheet.png), RGBA8, 1024 × 1024.
- [Prompt nguyên văn](../../games/dragon-hold/art-src/decals/pine-river/edge-gate-sheet.prompt.txt).
- [JSON lưới và tên ô](../../games/dragon-hold/art-src/decals/pine-river/edge-gate-sheet.json).
- [Tờ duyệt nền tối, sáng, cỏ; mỗi ô 128 px](../../games/dragon-hold/art-src/_review/MF-I6/preview.jpg).
- [So sánh các file thử ở cỡ nhỏ](../../games/dragon-hold/art-src/_review/MF-I6/attempts-128.jpg).

Ảnh thử và prompt giữ tại `games/dragon-hold/art-src/decals/pine-river/edge-gate-sheet.try{1,2,3}.{png,prompt.txt}`. Hai ảnh sinh nguyên gốc, prompt, bản chuẩn hóa chọn, script chuẩn hóa, script đo, số đo và biên bản md5 nằm trong `games/dragon-hold/art-src/_review/MF-I6/`. Mỗi ảnh có file `.prompt.txt` cạnh nó; lệnh dựng tờ duyệt nằm trong `preview-command.json`.

## Lưới và cách chia nhóm

Đã đối chiếu bốn tờ `dirt-patches.alpha.png`, `forest-litter.alpha.png`, `flower-clusters.alpha.png`, `moss-puddles.alpha.png`: cùng 1024 × 1024, lưới 2 × 2, mỗi ô 512 × 512. Một số ảnh nguồn cũ có khổ 1254 × 1254; khổ giao theo các tờ alpha đã chuẩn hóa.

| Ô, gốc tọa độ trên trái | Tên trong JSON | Nội dung |
|---|---|---|
| 0: `(0, 0)` | Moss Carpet | Thảm rêu thấp cho cổng Yêu Rêu |
| 1: `(512, 0)` | Trampled Grass and Claw Marks | Cỏ giẫm, các rãnh cào cho cổng Thú Mục |
| 2: `(0, 512)` | Broken Branches and Dry Brown Leaves | Hai cành gãy ở trên, năm lá nâu ở dưới |
| 3: `(512, 512)` | Gray Pebble Cluster | Đúng ba viên sỏi xám, có khoảng trong suốt giữa các viên |

Phiếu liệt kê năm nhóm vật nhưng yêu cầu giữ bốn ô. Vì vậy cành và lá dùng chung ô thứ ba; JSON có hai `subregions` theo tọa độ toàn tờ: cành `[0,512,512,264]`, lá `[0,776,512,248]`. Chúng cắt được riêng, không làm đổi lưới. UV được ghi theo gốc trên trái; bộ đọc cần đổi chiều v nếu sử dụng quy ước dưới trái.

## Các lượt và bản chọn

1. **Lượt sinh 1 → `try1`:** đủ vật; cỏ và sỏi tối, còn nhiễu alpha và vài pixel màu giữ riêng. Ảnh nguồn 1254 × 1254 được thu về 1024 × 1024. Không chọn.
2. **Lượt sinh 2:** sửa prompt để tăng luma rêu, cỏ và sỏi, giữ cành/lá nâu trầm, yêu cầu mép alpha sạch. Lưu nguyên gốc tại `edge-gate-sheet.try2.raw.png` trong thư mục duyệt. Đây là **lượt sinh được chọn**.
3. **Hai file trung gian ghép lỗi:** `try2.png` dùng phép ghép tự thu khoảng trong suốt nên ra 1024 × 861; `try3.png` đã đổi phép ghép nhưng thiết lập gravity còn ảnh hưởng đến tọa độ cắt các ô sau. Đây là lỗi thao tác của Codex, không phải hai lượt tạo ảnh mới. Cả hai được giữ nguyên, có prompt nguồn cạnh ảnh, không dùng để tích hợp.
4. **Bản chuẩn hóa chọn:** sửa thao tác cắt về `NorthWest` trước từng nhóm và ghép bằng `append`; lưu thành `_review/MF-I6/edge-gate-sheet.selected.png`, rồi chép nguyên byte thành `edge-gate-sheet.png`. Không ghi đè file thử nào. Do các file thử đã có lỗi ghép và luật cấm ghi đè, bản cuối được chép từ bản chọn trong thư mục duyệt, không chép từ một file `tryN` lỗi.

Chuẩn hóa giữ toàn bộ dáng rêu nguồn vốn tràn 8 px qua đường giữa: dùng vùng cắt riêng cho hai cụm phía trên, thu mỗi nhóm vừa khung 368 × 368, đặt giữa ô 512 × 512. Alpha dưới 0,125 được đưa về 0; trên 0,94 đưa về 1, giữ chuyển tiếp ở mép. Giới hạn saturation của hue 0–50° và 165–190° ở 0,45 để loại các pixel màu nóng còn sót. Script [normalize.py](../../games/dragon-hold/art-src/_review/MF-I6/normalize.py) ghi đúng các thao tác. Script từ chối ghi nếu đầu ra đã tồn tại.

## KA1 · Không thay đổi file có sẵn

Chạy `/sbin/md5 -r` trên toàn bộ file trong thư mục đích trước và sau. Trước: **106 file**. Sau: **115 file**. Đối chiếu theo đường dẫn: **106/106 file cũ giữ nguyên**, không xóa, không đổi tên; đúng **9 file mới** thuộc `edge-gate-sheet.*`. `diff -u` chỉ có chín dòng dữ liệu thêm, không có dòng dữ liệu bị bỏ.

- [md5-before.txt](../../games/dragon-hold/art-src/_review/MF-I6/md5-before.txt)
- [md5-after.txt](../../games/dragon-hold/art-src/_review/MF-I6/md5-after.txt)
- [md5-diff.txt](../../games/dragon-hold/art-src/_review/MF-I6/md5-diff.txt)

MD5 ảnh cuối: `67fe423f5541da49de87718fb74fab6b`. Ảnh cuối và bản `selected.png` giống nguyên byte.

## KA2, KA3 · Khổ, alpha và lề

`magick identify`: **PNG 1024 × 1024, 8-bit sRGB, RGBA**. JSON đúng bốn ô 512 × 512. Không có chữ, logo, người, thần hay nơi thờ trong ảnh tài sản.

Bảng dưới dùng mọi pixel có alpha > 0; bbox là tọa độ trong ô, cạnh phải/dưới không bao gồm. Mỗi ô có **0 pixel alpha > 0 trong dải lề 48 px**. Lề nhỏ nhất toàn tờ: **72 px**. Nền ngoài hình trong suốt; các mép được nhìn trên nền tối, sáng và cỏ, không thấy viền nền màu. Số pixel alpha trung gian là chuyển tiếp mép, không phải nền đục.

| Ô | Bbox trong ô | Pixel thấy được | Pixel alpha = 255 | Pixel alpha trung gian |
|---|---|---:|---:|---:|
| Rêu | `[72,88,440,424]` | 79.036 | 74.751 | 4.285 |
| Cỏ/vết cào | `[74,72,437,440]` | 101.351 | 94.588 | 6.763 |
| Cành/lá | `[73,72,438,440]` | 58.202 | 48.698 | 9.504 |
| Sỏi | `[72,90,440,421]` | 62.836 | 59.195 | 3.641 |

Ngưỡng kiểm alpha 50 % cho đúng 12 cụm vật: một rêu, một cỏ, hai cành, năm lá, ba sỏi; không có cụm nhiễu rời ngoài các vật. Kiểm nền xám `#E6E6E6` và trim dành cho nguồn Tripo không áp dụng cho tờ decal.

## KA4 · Màu giữ riêng và luma

Đo HSV: hue trong `[0,50]` hoặc `[165,190]`, saturation > 0,55 và value > 0,5. Mẫu số là mọi pixel alpha > 0, không bỏ các mép bán trong suốt. **Bản cuối: 0 pixel vi phạm ở từng ô, tổng 0/301.425 = 0 %.**

Luma tính trên kênh sRGB chuẩn hóa: `Y = 0,2126R + 0,7152G + 0,0722B`; không tuyến tính hóa. Lấy trung vị decal trên pixel alpha ≥ 128 để nền trong suốt không kéo trung vị về 0. Ô nền lấy trung vị toàn ảnh. Các mốc nền được chọn theo vật liệu trước khi tạo ảnh: rêu → `moss`, cỏ giẫm → `grass-a`, cành/lá → `pine-litter`, sỏi trên lối đi → `path`. Đường dẫn nằm trong `art-src/ground/pine-river/` và được ghi trong JSON; không dùng màu đất tùy ý để khớp kết quả.

| Ô | Ô nền | Luma nền | Luma bản cuối | Chênh lệch | Giới hạn |
|---|---|---:|---:|---:|---|
| Rêu | `moss.png` | 0,435053 | 0,432340 | −0,002713 | Đạt ±0,08 |
| Cỏ/vết cào | `grass-a.png` | 0,457738 | 0,441027 | −0,016711 | Đạt ±0,08 |
| Cành/lá | `pine-litter.png` | 0,282084 | 0,303992 | +0,021908 | Đạt ±0,08 |
| Sỏi | `path.png` | 0,571367 | 0,535221 | −0,036146 | Đạt ±0,08 |

Số đo các file thử, theo thứ tự rêu / cỏ / cành-lá / sỏi:

| File | Khổ | Luma từng ô | Số pixel KA4 vi phạm từng ô |
|---|---|---|---|
| `try1` | 1024 × 1024 | 0,355639 / 0,376894 / 0,258936 / 0,461561 | 12 / 13 / 310 / 12 |
| `try2` — ghép lỗi | 1024 × 861 | 0,438784 / 0,501595 / 0,472188 / 0,364906 | 0 / 0 / 0 / 0 |
| `try3` — cắt lỗi | 1024 × 1024 | 0,432340 / 0,437198 / 0,399746 / 0,513076 | 0 / 0 / 0 / 0 |

Các số của `try2`/`try3` chỉ để lưu vết lỗi, không chứng minh đạt lưới hay nội dung. Chi tiết đầy đủ trong [metrics.json](../../games/dragon-hold/art-src/_review/MF-I6/metrics.json); cách đo trong [measure.py](../../games/dragon-hold/art-src/_review/MF-I6/measure.py).

## KA5 · Tự chấm năm tiêu chí

Theo ART_ACCEPTANCE §1–2.2. Mỗi dãy điểm theo thứ tự: **đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau**, mỗi tiêu chí tối đa 2. Đã xem ảnh đầy đủ và ảnh mỗi ô 128 px; file ghép sai vẫn được xem và chấm trượt.

| Bản | Cỡ đầy đủ | Tổng | Mỗi ô 128 px | Tổng | Kết luận |
|---|---|---:|---|---:|---|
| `try1` | 2 / 1,5 / 1,5 / 2 / 0,5 | 7,5 | 2 / 1 / 1,5 / 2 / 0,5 | 7 | Trượt: nhiễu alpha, màu và luma |
| `try2` | 0,5 / 0,5 / 1,5 / 0 / 0 | 2,5 | 0,5 / 0,5 / 1,5 / 0 / 0 | 2,5 | Loại: sai ghép, sai khổ |
| `try3` | 1 / 0,5 / 1,5 / 0,5 / 0 | 3,5 | 1 / 0,5 / 1,5 / 0,5 / 0 | 3,5 | Loại: sai cắt, mất nhóm vật |
| Bản cuối từ lượt sinh 2, chuẩn hóa đúng | 1,5 / 1,5 / 2 / 2 / 2 | **9** | 1,5 / 1,5 / 2 / 2 / 2 | **9** | **Đạt tự chấm** |

Trừ điểm bản cuối vì rãnh cào còn khá đều, có thể gợi rãnh lối đi; tán rêu có nhiều chi tiết nhỏ. Ở 128 px vẫn phân biệt được rêu, cỏ bị cào, cành gãy, lá nâu và ba viên sỏi xám. Nét vẽ, bảng màu, góc nhìn thẳng xuống và hình khối hợp các tờ có sẵn; không còn sỏi trắng theo chuỗi hay lá đỏ như tín hiệu máu.

## Phần bỏ qua và việc cần xem

Không sửa mã, tài liệu thiết kế, tờ decal cũ hay game khác; không chạy Git, build, test, dev server, trình duyệt hoặc mạng ngoài công cụ tạo ảnh. Không có nguồn Tripo hay âm thanh trong phiếu. Không tích hợp vào runtime vì phiếu chỉ giao ảnh và JSON.

Claude cần chấm lại bản cuối từ 8 điểm để nhận; ưu tiên xem dáng rãnh cào trong tờ duyệt và cách dùng chung ô cành/lá. Chỉ dùng `edge-gate-sheet.png` và JSON bên cạnh để tích hợp; các file `try2`/`try3` lỗi được giữ theo luật không ghi đè, không xóa.
