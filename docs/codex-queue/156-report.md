# Phiếu 156 · Last Line · Ảnh nguồn Lightbearer và năm súng canh

**Ngày:** 29/10/2026. **Công cụ sinh:** `image_gen` tích hợp của Codex. **Trạng thái:** đã giao đủ tám bản chọn, tự chấm M/Q từ 8 ở cỡ đầy đủ và 256 px; chờ Claude chấm lại. **Chưa xác nhận trọn điều kiện kiểm 5:** hông và tâm gối ở góc sau bị áo choàng che, chỉ có thể ước lượng. Không biến hai số ước lượng thành số đo trực tiếp để đóng phiếu.

## 1. Bản giao và các lượt sinh

Gốc đường dẫn ảnh: [`games/typing-survival/art-src`](../../games/typing-survival/art-src/). Toàn bộ ảnh nguồn và prompt nằm trong [`models-src/`](../../games/typing-survival/art-src/models-src/). Có **12 lượt sinh**, giữ đủ 12 `.tryN.png` và 12 `.tryN.prompt.txt`; tám bản chọn có `.png` và `.prompt.txt` riêng.

| Bản chọn | Lượt chọn | Những gì đã sửa trong prompt từng lượt |
|---|---:|---|
| [`lightbearer-front.png`](../../games/typing-survival/art-src/models-src/lightbearer-front.png) | 3 | Lượt 1: khối bắt buộc, hai ảnh B, dáng nữ thanh, mũ viền vàng, áo choàng trơn, góc trước trực giao. Tay còn khép, áo choàng xuống gần cổ chân. Lượt 2: nhấn đường vai–cổ tay 45°, lòng bàn tay úp, gấu ngang gối; áo đã ngắn hơn nhưng tay vẫn hẹp. Lượt 3: thêm tọa độ tương đối vai/cổ tay, khuỷu thẳng và gấu ngang giáp gối. Chọn tư thế mở rõ nhất; không nắn tay bằng công cụ. |
| [`lightbearer-back.png`](../../games/typing-survival/art-src/models-src/lightbearer-back.png) | 2 | Lượt 1: nhìn thẳng sau, đính kèm bản trước đã chọn, giữ chiều cao và tỷ lệ; xuất hiện họa tiết phát sáng giống huy hiệu trên áo. Lượt 2: yêu cầu vải navy trơn, chỉ viền vàng ở cạnh và gấu, bỏ họa tiết bằng sinh lại. Không xóa họa tiết bằng hậu kỳ. |
| [`lightbearer-left.png`](../../games/typing-survival/art-src/models-src/lightbearer-left.png) | 1 | Thêm câu bắt buộc cùng nhân vật, nhìn đúng phía trái, mặt quay sang mép trái, trực giao 90°; giải thích hai tay A-pose chồng lên nhau khi nhìn ngang. Không sinh lại. |
| [`sentinel-pulse.png`](../../games/typing-survival/art-src/models-src/sentinel-pulse.png) | 1 | Dùng `gun-xung.png` cho nhóm nòng ngắn; chuyển thành hai nòng gắn chung vỏ trắng vàng. Vòng cyan là chi tiết vật lý gắn ở đầu nòng. Không sinh lại. |
| [`sentinel-heat.png`](../../games/typing-survival/art-src/models-src/sentinel-heat.png) | 1 | Dùng `gun-tia.png` cho ống hội tụ và lõi cam; thân quang học dài, vòng thấu kính, lõi nằm trong vỏ; trạng thái chưa bắn. Không sinh lại. |
| [`sentinel-scatter.png`](../../games/typing-survival/art-src/models-src/sentinel-scatter.png) | 2 | Lượt 1 có sáu miệng nòng, loại. Lượt 2 nhấn đúng năm: một giữa, hai mỗi bên, thân quạt rộng và nông, sống lưng thấp. Không cắt bỏ nòng bằng công cụ. |
| [`sentinel-rail.png`](../../games/typing-survival/art-src/models-src/sentinel-rail.png) | 1 | Dùng `gun-ray.png` cho hai ray dài; cầu nối và cuộn cyan nằm trên phần cứng, thân sau hẹp; không có mảnh hay tia bắn rời. Không sinh lại. |
| [`sentinel-mortar.png`](../../games/typing-survival/art-src/models-src/sentinel-mortar.png) | 1 | Dùng `gun-phao-sao.png` cho ống rộng chĩa lên; thân bay hình bầu chắc, lỗ thông hình sao lõm trên cổ nòng; không có chân hay bệ. Không sinh lại. |

Mỗi lời gọi đều đính kèm **cả hai ảnh B** và nguyên câu `Use the attached images only to keep the same hero design, armour, cape, visor, colours and the sentinel guns' look. Draw the new view as described.` Hai góc phụ đính kèm thêm bản trước đã chọn; từng súng đính kèm icon riêng. Các khối MODEL và TAIL được giữ nguyên văn; các câu bổ sung chỉ định góc, tham chiếu, khung hoặc sửa lỗi cụ thể. Prompt nguyên văn đã gửi nằm cạnh từng ảnh; prompt bản chọn giống prompt của lượt chọn.

Tham số, ảnh đính kèm và nguồn file từ công cụ được lưu tại [`generation-manifest.json`](../../games/typing-survival/art-src/_review/156/generation-manifest.json), [`generation-addenda.json`](../../games/typing-survival/art-src/_review/156/generation-addenda.json), [`source-provenance.json`](../../games/typing-survival/art-src/_review/156/source-provenance.json).

## 2. Hậu kỳ giữ phần vẽ

**Nền đã dùng ở cả 12 lượt và tám bản giao: `#00FF00`.** Công cụ trả cả 12 ảnh đúng 1254 × 1254 px, nên không cần cắt giữa để sửa khổ. Hậu kỳ chỉ tách nền, cắt phần nền thừa, thu đồng dạng rồi thêm lề xanh; không kéo méo, thay vật liệu, chỉnh gamma, tăng sáng, vẽ đè hay ghép bộ phận.

Lệnh nền tảng, chạy bằng [`process.py`](../../games/typing-survival/art-src/_review/156/process.py):

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/typing-survival/art-src/_review/156/process.py lightbearer-front 3
```

Lệnh ImageMagick tương ứng, thay tên và cạnh hộp theo từng ảnh:

```sh
"$ART_MAGICK" <bản-sinh> -alpha on -fuzz 12% -transparent '#00ff00' \
  -trim +repage -filter Lanczos -resize 1054x1054 \
  -gravity center -background none -extent 1254x1254 \
  -background '#00ff00' -alpha remove -alpha off <bản-chọn>
```

Nhân vật dùng hộp 1054 × 1054, súng dùng 1078 × 1078. Đây là giới hạn hộp, giữ tỷ lệ vật; không ép các súng thành cùng chiều rộng và chiều cao. Lệnh tách mặt nạ thay phần cuối bằng `-alpha extract <tên>-alpha.png`. Lệnh đầy đủ từng ảnh nằm trong tám file `<tên>-process.json`.

Phép đo đầu phát hiện viền xanh sau thu ảnh: ba góc nhân vật, Rail và Mortar vượt 0,5% nếu tính cả pixel biên có alpha > 127. Đã sửa **phông ở dải mép tối đa 2 px**, bằng [`refine-edges.py`](../../games/typing-survival/art-src/_review/156/refine-edges.py): chỉ nhận màu H = 120° ± 12°, S > 0,5 sát vùng nền; giữ nguyên RGB mọi pixel còn lại. Không đụng các điểm xanh nằm sâu trong phần vẽ. Bản trước sửa, mặt nạ và tờ kiểm đầu được giữ tại [`stage1/`](../../games/typing-survival/art-src/_review/156/stage1/); số đo trước sửa tại [`measurements.json`](../../games/typing-survival/art-src/_review/156/measurements.json), nhật ký sửa mép tại [`edge-refinement.json`](../../games/typing-survival/art-src/_review/156/edge-refinement.json). Không dùng ngưỡng để san phần vẽ.

Tám tờ **“bản sinh | bản hậu kỳ”**, mỗi bên cùng khổ, đã tạo bằng Arial của macOS:

| Ảnh | Tờ kiểm |
|---|---|
| Trước | [`156-lightbearer-front-before-after.jpg`](../../games/typing-survival/art-src/_review/156-lightbearer-front-before-after.jpg) |
| Sau | [`156-lightbearer-back-before-after.jpg`](../../games/typing-survival/art-src/_review/156-lightbearer-back-before-after.jpg) |
| Trái | [`156-lightbearer-left-before-after.jpg`](../../games/typing-survival/art-src/_review/156-lightbearer-left-before-after.jpg) |
| Pulse | [`156-sentinel-pulse-before-after.jpg`](../../games/typing-survival/art-src/_review/156-sentinel-pulse-before-after.jpg) |
| Heat | [`156-sentinel-heat-before-after.jpg`](../../games/typing-survival/art-src/_review/156-sentinel-heat-before-after.jpg) |
| Scatter | [`156-sentinel-scatter-before-after.jpg`](../../games/typing-survival/art-src/_review/156-sentinel-scatter-before-after.jpg) |
| Rail | [`156-sentinel-rail-before-after.jpg`](../../games/typing-survival/art-src/_review/156-sentinel-rail-before-after.jpg) |
| Mortar | [`156-sentinel-mortar-before-after.jpg`](../../games/typing-survival/art-src/_review/156-sentinel-mortar-before-after.jpg) |

## 3. Số đo trên bản giao

Nguồn số: [`measurements-final.json`](../../games/typing-survival/art-src/_review/156/measurements-final.json), do [`validate.py`](../../games/typing-survival/art-src/_review/156/validate.py) đọc RGB 8-bit và mặt nạ. Vật được tính ở alpha > 127. Vùng liền dùng bốn hướng kề; ngưỡng 1% = 15.725,16 px. Không bỏ qua pixel xanh bên trong vật để làm đẹp số.

**Cả tám bản: 1254 × 1254 px; sai lệch kênh lớn nhất trong dải 10 px ở bốn mép = 0/255, ngưỡng cho phép 12/255.**

| Ảnh | Lề trái / phải / trên / dưới (px) | Cao hộp bao (px) | Pixel vật | Pixel xanh trong vật | Tỷ lệ xanh | Vùng liền > 1% |
|---|---|---:|---:|---:|---:|---:|
| Front | 256 / 256 / 101 / 101 | 1052 | 261.239 | 51 | 0,0195% | 1 |
| Back | 247 / 248 / 100 / 101 | 1053 | 259.426 | 21 | 0,0081% | 1 |
| Left | 492 / 493 / 100 / 100 | 1054 | 145.327 | 81 | 0,0557% | 1 |
| Pulse | 88 / 89 / 172 / 173 | 909 | 552.839 | 68 | 0,0123% | 1 |
| Heat | 88 / 88 / 185 / 185 | 884 | 508.797 | 54 | 0,0106% | 1 |
| Scatter | 88 / 89 / 291 / 292 | 671 | 461.850 | 101 | 0,0219% | 1 |
| Rail | 88 / 88 / 141 / 142 | 971 | 318.144 | 91 | 0,0286% | 1 |
| Mortar | 208 / 209 / 89 / 89 | 1076 | 596.294 | 555 | 0,0931% | 1 |

Lề nhỏ nhất **88 px = 7,02%**, vượt 3%. Xanh trong vật cao nhất **0,0931%**, dưới 0,5%. Mortar có thêm một thành phần đúng **1 pixel** ở mặt nạ, không phải bộ phận rời; không xóa điểm vẽ này để ép thành một thành phần tuyệt đối. Tám vật có đúng một vùng lớn, đủ khung.

### Ba góc Lightbearer

Chiều cao hộp bao 1052 / 1053 / 1054 px: biên độ **2 px, khoảng 0,19%**, dưới 3%.

Mốc đọc bằng mắt trên bản sinh rồi chuyển bằng đúng tỷ lệ hậu kỳ; trục y tính từ mép trên ảnh. Mốc vai là tâm khớp dưới giáp vai; hông là vùng giáp hông ở đầu đùi; gối là tâm giáp gối. Sai số đọc bằng mắt khoảng ±10 px trên ảnh giao. Số thập phân trong JSON là kết quả tính tỷ lệ, không phải độ chính xác của phép đọc.

| Góc | Đỉnh mũ | Vai | Hông | Gối | Đế chân |
|---|---:|---:|---:|---:|---:|
| Trước | ≈100 | ≈358 | ≈576 | ≈802 | ≈1153 |
| Sau | ≈100 | ≈357 | **≈566*** | **≈808*** | ≈1153 |
| Trái | ≈100 | ≈367 | ≈586 | ≈814 | ≈1153 |

`*` **Ước lượng do áo choàng che.** Hông và tâm gối góc sau không quan sát trực tiếp được. Biên độ biểu kiến lớn nhất khoảng 20 px, 1,9% chiều cao, nhưng không dùng hai mốc bị che để tuyên bố đã chứng minh toàn bộ kiểm 5. Muốn lộ hoàn toàn chúng phải đổi hoặc bỏ phần áo choàng; dừng ở đây theo ART_ACCEPTANCE §5, giữ thiết kế để Claude quyết. Đỉnh hộp bao sau sửa mép có lệch 1 px so với đường chuẩn trước sửa mép, đã thể hiện trong bảng hộp bao.

Hai đường tâm vai–cổ tay ở góc trước đo được **40,23° và 40,37° so với phương đứng**, trong khoảng 40–50°. Điểm gốc bên trái: vai (503, 320), cổ tay (311, 547); bên phải: vai (750, 320), cổ tay (943, 547). Đây là phép đo tư thế trên ảnh, không xác nhận rig 3D.

Tờ đánh dấu: [`156-landmarks.jpg`](../../games/typing-survival/art-src/_review/156-landmarks.jpg); dữ liệu và script: [`landmarks.json`](../../games/typing-survival/art-src/_review/156/landmarks.json), [`landmarks.py`](../../games/typing-survival/art-src/_review/156/landmarks.py).

### Dáng súng ở 64 px

Thu toàn mặt nạ cùng khổ 1254 về 64 × 64 bằng ImageMagick, threshold 50%, không dịch hoặc xoay riêng từng súng để giảm IoU.

| Cặp | IoU |
|---|---:|
| Pulse – Heat | 0,6511 |
| Pulse – Scatter | 0,5140 |
| Pulse – Rail | 0,2540 |
| Pulse – Mortar | 0,5832 |
| Heat – Scatter | 0,6525 |
| Heat – Rail | 0,2235 |
| Heat – Mortar | 0,4865 |
| Scatter – Rail | 0,2637 |
| Scatter – Mortar | 0,5202 |
| Rail – Mortar | 0,3202 |

**10/10 cặp ≤ 0,80.** Đếm trực quan bản chọn: Pulse hai nòng; Scatter năm miệng; Rail hai ray có cầu nối; Mortar một ống rộng hướng lên. Các súng không có tay cầm, chân, bệ hay hiệu ứng bắn rời.

## 4. KA5 · tự chấm trên bản hậu kỳ

Đã xem từng PNG bản giao ở 1254 px, sau đó xem ở 256 px trong [`156-at-256.jpg`](../../games/typing-survival/art-src/_review/156-at-256.jpg). Không chấm trên bản sinh để thay cho bản hậu kỳ.

**Đúng nhân vật của hướng B.** Giữ dáng nữ thanh, mũ có hai cạnh vàng vút, giáp ceramic trắng vàng, suit graphite, đường cyan và áo choàng navy. Khác có chủ đích để làm nguồn rig: áo ngắn đến vùng giáp gối, tư thế đứng yên, bỏ họa tiết/hình hiệu, không có súng cạnh người, không có ánh sáng cảnh. Kính cyan bản trước tạo nét V hẹp theo hình mũ, không phải một khe ngang đơn giản; lớp lót trắng vàng chỉ đọc ở viền, chưa có góc lật vải cho thấy toàn mặt lót. Claude cần xem hai điểm này khi duyệt đúng thiết kế.

Tờ so bắt buộc: [`156-sheet.jpg`](../../games/typing-survival/art-src/_review/156-sheet.jpg), gồm ba góc cạnh vùng nhân vật B, năm súng cạnh năm icon cùng khổ hiển thị, và một hàng ba góc cạnh ảnh chủ dự án. **Đứng cạnh được về độ hoàn thiện giáp, vải và dáng nhân vật.** M được áp vào chất lượng ảnh nguồn model thương mại; không áp các tiêu chí trời, ba tầng cảnh hay ánh sáng điện ảnh của một ảnh nền vào nguồn Tripo buộc phông xanh, ánh sáng phẳng. Đây là cách diễn giải cần Claude chấm lại, không phải đã có nhận độc lập.

| Bản hậu kỳ | M · 1254 | Q · 1254 | M · 256 | Q · 256 | Phần còn yếu |
|---|---:|---:|---:|---:|---|
| Front | 8,5 | 9,0 | 8,5 | 8,5 | Tay sát đầu thấp khoảng A-pose; ngón nhỏ ở 256; kính nét V và lót vải chưa hiện đầy đủ. |
| Back | 8,5 | 8,5 | 8,5 | 8,5 | Áo che hông/gối và phần lớn giáp lưng; chỉ lộ giáp gáy, vai và yoke trên. |
| Left | 8,25 | 8,5 | 8,0 | 8,5 | Profile rất hẹp ở 256, hai tay chồng theo hướng nhìn; không thay bằng góc ba phần tư để làm đẹp. |
| Pulse | 8,5 | 9,5 | 8,5 | 9,5 | Vàng hơi bắt sáng, chưa hoàn toàn matte. |
| Heat | 8,5 | 9,5 | 8,5 | 9,5 | Vài vết xước nhỏ ở vỏ; lõi cam đọc rõ. |
| Scatter | 8,5 | 9,5 | 8,5 | 9,5 | Nòng giữa lớn hơn bốn nòng bên; đủ năm, dáng quạt rộng đọc rõ. |
| Rail | 8,5 | 9,5 | 8,0 | 9,0 | Cầu nối và coil mảnh hơn các súng còn lại ở 256. |
| Mortar | 8,5 | 9,5 | 8,5 | 9,5 | Vài lỗ thông sao có vẻ trang trí; vẫn là hốc gắn liền vào vỏ. |

Q dùng đúng năm tiêu chí 0–2. **Dùng tiếp = 2 cho cả tám:** một khối liền, đúng loại góc, đủ khung; đây là đánh giá khả năng dùng nguồn Tripo, chưa kiểm model thực. Front trừ 0,5 ở đúng đề và hình khối; Back/Left trừ thêm 0,5 ở đọc được; các súng trừ 0,5 ở hình khối/độ giản lược. Ở 256, Front và Rail trừ thêm 0,5 về đọc chi tiết. Tổng đúng như bảng.

## 5. KA1 và chạy lại

[`md5-before.txt`](../../games/typing-survival/art-src/_review/156/md5-before.txt) chụp **746 file** trước lần ghi đầu tiên. [`md5-after.txt`](../../games/typing-survival/art-src/_review/156/md5-after.txt) chụp **992 file**, thêm 246 dòng. [`md5-diff.txt`](../../games/typing-survival/art-src/_review/156/md5-diff.txt) **chỉ có dòng thêm, không có dòng bỏ hay sửa**. **746/746 file cũ nguyên MD5; không mất file nào.** Cả 12 `.tryN.png` khớp MD5 với file do công cụ sinh lưu ban đầu. Kết quả máy: [`ka1-result.json`](../../games/typing-survival/art-src/_review/156/ka1-result.json).

Ảnh chụp MD5 liệt kê toàn cây, kể cả file làm việc và bản chạy lại, trước khi tạo chính ba đầu ra `md5-after.txt`, `md5-diff.txt`, `ka1-result.json`; ba file đó không tự băm chính mình. Không ghi thêm media sau ảnh chụp này.

Các script đã dùng nằm trong [`_review/156/`](../../games/typing-survival/art-src/_review/156/). Có đường chạy lại không ghi đè bộ giao:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/typing-survival/art-src/_review/156/replay.py ten-thu-muc-moi
```

Đã chạy với `replay-check`: **8/8 ảnh tạo lại trùng từng pixel RGB** với bản giao, lưu tại [`replay-check/verification.json`](../../games/typing-survival/art-src/_review/156/replay-check/verification.json). Script dùng ảnh sinh đã giữ, không gọi sinh ảnh hoặc mạng lần nữa, và từ chối thư mục đầu ra đã tồn tại. `sheets.py` tạo tờ so; `validate.py` kiểm số; `landmarks.py` dựng bằng chứng tư thế; `snapshot.py` thực hiện `md5 -r` và `diff`.

## 6. Việc bỏ qua và việc cần xem

- Không dựng 3D, rig hoặc gọi Tripo/Meshy/API 3D: đó là phần chủ dự án làm bằng tay sau khi Claude nhận. Không làm Vanguard đã bỏ.
- Không sinh âm, chạy server, trình duyệt, build, test game hoặc lệnh Git. Không đọc hay ghi Tu Tiên; không sửa game code, icon, ảnh B hay tài liệu ngoài báo cáo này.
- Không cập nhật `ART_REPLACE_LATER.md`: nằm ngoài danh sách được ghi; các điểm sát ngưỡng và thiếu sót đã ghi ở bảng trên để Claude chuyển tiếp nếu cần.
- **Claude cần xem ảnh giao đầy đủ, tờ trước–sau, nét kính/lót vải và hai mốc hông/gối bị che.** Kiểm 2, 3, 4, 6 đạt số; kiểm 5 đạt chiều cao, góc tay và căn mốc quan sát được, còn giới hạn đo góc sau như đã nêu. Không ghi “đủ mọi điều kiện xong” khi giới hạn đó chưa được quyết.
- Sau khi Claude chấm lại M ≥ 8, Q ≥ 8 và quyết phần kiểm 5, Claude gửi chủ dự án danh sách dựng: **Lightbearer (ba góc cho một nhân vật), Pulse Gun, Heat Beam, Scatter Gun, Rail Gun, Star Mortar** — sáu model, không phải tám model.
