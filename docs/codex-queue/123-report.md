# Phiếu 123 · Wordwoven · Decal mặt đất v2 và Rice Field v2

**Ngày:** 29/10/2026. **Trạng thái:** giao bản tự chấm đạt, chờ Claude chấm lại M và Q. Sinh bằng công cụ tích hợp `image_gen`, không dùng API ngoài.

## 1. Bộ giao

Đã làm **ba tờ decal và năm ô rice, tổng tám ảnh chính**. Tiêu đề phiếu ghi bảy ảnh và đoạn kết ghi hai tờ decal; lấy danh sách nội dung a/b/c làm chuẩn, không bỏ tờ c.

- `games/typing-defense/art-src/scenery/meadow/decals-v2/`: `ground-decals-a`, `ground-decals-b`, `road-edges-c`; mỗi tờ có `.png` nền #FF00FF, `.alpha.png` RGBA, `.prompt.txt`, hai nửa chọn `-left.png`, `-right.png` và prompt tương ứng.
- `games/typing-defense/art-src/scenery/meadow/rice-v2/`: `rice-flooded`, `rice-seedling`, `rice-green`, `rice-ripe`, `rice-stubble`; mỗi ô có PNG cuối và prompt nguyên văn.
- Mọi lượt sinh giữ đủ `.tryN.png` và `.tryN.prompt.txt` cạnh nhau. Tổng **14 lượt sinh**: bảy lượt cho các nửa decal, bảy lượt cho rice. Không ảnh nào quá hai lượt.
- Script, dữ liệu đo và cấu hình chọn: `games/typing-defense/art-src/_review/123/`.

Các PNG `.tryN` và hai nửa chọn giữ nguyên ảnh công cụ trả về, **1254 × 1254**. Script thu về 1024 × 1024 trước khi xử lý; tờ ghép cuối đúng 2048 × 1024, ô rice cuối đúng 1024 × 1024. Hai nửa chọn là bản lưu nguồn, không phải atlas dùng trực tiếp.

## 2. Prompt và lựa chọn từng lượt

Mọi prompt giữ nguyên STYLE + MAP + TOP của phiếu; decal có nguyên dòng nền M. Prompt ghi rõ chỉ vẽ mặt vật liệu, để bối cảnh sử thi không biến thành phong cảnh trong ô đất. Không chép nội dung ảnh tham chiếu của chủ dự án.

| Ảnh nguồn | Lượt 1 | Sửa ở lượt 2 | Chọn |
|---|---|---|---|
| `ground-decals-a-left` | Bốn mảng đất; đính kèm `trail-worn` làm mốc chất liệu, khaki và đá vôi | Không cần | 1 |
| `ground-decals-a-right` | Ngã ba, thẳng, cong, đá lát chìm; cùng tham chiếu `trail-worn` | Không cần | 1 |
| `ground-decals-b-left` | Dã quỳ, huệ, hai cụm sỏi; huệ còn giống hoa ly bông to | Nêu tên Polianthes tuberosa/Agave amica, hoa ống sáp nhỏ theo chùm, nụ dài; giữ ba món còn lại | 2 |
| `ground-decals-b-right` | Lá đỏ, gốc cổ thụ, vòng gỗ, vũng nước và lá sen; vật liệu già, thô, tự nhiên | Không cần | 1 |
| `road-edges-c-left` | Đính kèm cả `road-paved` và `trail-worn`; bờ đá thẳng/cong, phiến vỡ, quạt sỏi; yêu cầu lõi, vai sỏi và cỏ | Không cần | 1 |
| `road-edges-c-right` | Cùng hai tham chiếu; cỏ trùm, vệt bánh xe, ngã ba ba phiến, bậc ba phiến; trục dọc và vai đường bất quy tắc | Không cần | 1 |
| `rice-green` | Tám hàng, tâm 64 + 128k; chu kỳ đạt 128px nhưng S = 0,6121 vượt 0,55 | Đổi yêu cầu thành xanh ngọc xám, lớp sáp lá dịu, S mục tiêu 0,38–0,48; vẫn giữ tám hàng | 2 |
| `rice-seedling` | Dùng green lượt 2; cùng vị trí hàng, cây non thưa hơn và mặt nước bạc rộng | Không cần | 1 |
| `rice-ripe` | Dùng green lượt 2; đổi thành bông lúa vàng già, hạt nặng | Không sinh lại; dịch ngang tuần hoàn +8px bằng công cụ để khớp pha | 1 |
| `rice-stubble` | Dùng green lượt 2; màu đạt nhưng còn giống lúa khô đứng, chưa gặt | Nhấn chân rạ ngắn khoảng 8cm, mặt cắt cụt, bùn lộ giữa hàng, toàn bộ bông và lá dài đã thu hoạch | 2 |
| `rice-flooded` | Dùng green lượt 2 làm mốc thang; mặt nước bạc, trời phản chiếu dịu và rãnh cấy chìm | Không cần | 1 |

Ba ô có cây đổi trạng thái đều có nguyên câu `Same rows as the attached image: identical row positions and spacing. Change only the crop stage as described.` và dùng green lượt 2. Cả năm ô đều có nguyên câu liền mép bắt buộc. Không dùng lượt 3 vì các bản chọn đã qua số đo và tự chấm.

## 3. Hậu kỳ theo ART_ACCEPTANCE §5

Decal: tách nền magenta theo hue, cắt phần nền trống, giữ **toàn bộ vật**, đổi cỡ đồng tỷ lệ để cạnh dài nằm trong 452px rồi đặt giữa ô 512px. Lề nhỏ nhất 30px. Không xóa lá, đá hay rễ để lấy lề. Chỉ làm mềm alpha vào trong bằng khoảng cách tới mép: **20px ở tờ a, 9px ở tờ c**, tờ b giữ mép rõ. RGB của vật không đổi màu, không tăng sáng, không vẽ bù.

Rice: thu ảnh nguồn về 1024px; dịch tuần hoàn +8px riêng ripe. Làm liền mép trong dải **24px** bằng trọng số cosin giữa hai mép đối diện, giảm về 0 ở đầu trong. Chỉ dải mép thay đổi; không roll rồi phủ chữ thập giữa tranh, không phủ màu, không san phẳng luống, không chỉnh hue/saturation hay gamma. E sau sửa bằng 0 vì hai mép đối diện trùng nhau; vẫn xem tờ lát 3×3 để kiểm vệt lặp, không lấy E = 0 thay cho chấm tranh.

Lượt green đầu sai S được sinh lại, không ép giảm màu bằng công cụ. Huệ và rạ sai hình cũng sửa bằng sinh lại. Không có ngưỡng số còn mâu thuẫn với bản chọn buộc phải phá tranh.

Tám tờ **bản sinh | bản hậu kỳ**, hai bên cùng cỡ, ở `games/typing-defense/art-src/_review/`:

- [Tờ a](../../games/typing-defense/art-src/_review/123-ground-decals-a-before-after.jpg)
- [Tờ b](../../games/typing-defense/art-src/_review/123-ground-decals-b-before-after.jpg)
- [Tờ c](../../games/typing-defense/art-src/_review/123-road-edges-c-before-after.jpg)
- [Flooded](../../games/typing-defense/art-src/_review/123-rice-flooded-before-after.jpg)
- [Seedling](../../games/typing-defense/art-src/_review/123-rice-seedling-before-after.jpg)
- [Green](../../games/typing-defense/art-src/_review/123-rice-green-before-after.jpg)
- [Ripe](../../games/typing-defense/art-src/_review/123-rice-ripe-before-after.jpg)
- [Stubble](../../games/typing-defense/art-src/_review/123-rice-stubble-before-after.jpg)

## 4. Kiểm số trên ảnh giao

Nguồn đầy đủ: `_review/123/audit-final.json`, `delivery/metrics.json`, `identify.txt`. Không đo trên ảnh JPG thu nhỏ. H, S là trung vị HSV của pixel RGB sRGB; luma dùng 0,2126R + 0,7152G + 0,0722B. Diện tích decal tính pixel alpha > 0. Dải mép 3px đo phía trong đường biên vật; luma dùng RGB chưa nhân alpha để không nhầm mép mềm thành viền mực.

### 4.1 KA1

`md5 -r` đệ quy scenery: trước **322 file**, sau **381 file**; **59 file thêm, 0 file đổi, 0 file mất**. Diff chỉ có dòng thêm (ngoài tiêu đề diff).

Bằng chứng: `md5-before.txt`, `md5-after.txt`, `md5-diff.txt`. Cả 59 file thêm đều thuộc hai thư mục mới của phiếu.

### 4.2 Decal

Cả ba `.alpha.png`: **2048 × 1024, sRGB, RGBA 8-bit**, đủ **8/8** ô. Cả 24 ô có **lề tối thiểu 30px ≥ 24px** và **0% pixel alpha > 0 có H 285–330°, S > 0,5**. Bảng đọc từ trái sang phải, hàng trên rồi hàng dưới; đây cũng là thứ tự trong ảnh ghép.

| Tờ / ô | Vật | Diện tích % (≥35) | Alpha 0,1–0,9 / alpha > 0 (%) | Luma mép / vật (≥0,6) |
|---|---|---:|---:|---:|
| ground-decals-a / 1 | Đất mòn sáng 1 | 56.54 | 14.30 | 0.959 |
| ground-decals-a / 2 | Đất mòn sáng 2 | 58.23 | 13.99 | 0.943 |
| ground-decals-a / 3 | Ngã ba đất | 44.41 | 17.16 | 0.884 |
| ground-decals-a / 4 | Lối thẳng | 38.82 | 17.52 | 0.931 |
| ground-decals-a / 5 | Đất dưới tán 1 | 57.98 | 19.78 | 0.942 |
| ground-decals-a / 6 | Đất dưới tán 2 | 60.51 | 17.91 | 1.064 |
| ground-decals-a / 7 | Lối cong | 41.12 | 17.21 | 0.903 |
| ground-decals-a / 8 | Đá lát lún dưới cỏ | 58.12 | 13.54 | 0.862 |
| ground-decals-b / 1 | Dã quỳ vàng | 55.14 | 0.00 | 0.993 |
| ground-decals-b / 2 | Huệ trắng | 54.88 | 0.00 | 0.987 |
| ground-decals-b / 3 | Lá bàng đỏ | 56.27 | 0.00 | 0.822 |
| ground-decals-b / 4 | Gốc cổ thụ | 55.83 | 0.00 | 0.790 |
| ground-decals-b / 5 | Sỏi vôi 1 | 52.29 | 0.00 | 0.742 |
| ground-decals-b / 6 | Sỏi vôi 2 | 58.10 | 0.00 | 0.653 |
| ground-decals-b / 7 | Vòng vụn gỗ | 57.02 | 0.00 | 0.738 |
| ground-decals-b / 8 | Vũng nước, lá sen | 59.47 | 0.00 | 0.876 |
| road-edges-c / 1 | Đá bờ thẳng | 52.86 | 7.83 | 0.867 |
| road-edges-c / 2 | Đá bờ cong | 48.30 | 8.28 | 0.908 |
| road-edges-c / 3 | Cỏ trùm mép đá | 55.82 | 7.14 | 1.127 |
| road-edges-c / 4 | Vệt bánh xe, vũng bạc | 60.92 | 6.70 | 1.001 |
| road-edges-c / 5 | Phiến vỡ tràn cỏ | 56.72 | 6.59 | 0.871 |
| road-edges-c / 6 | Quạt sỏi mép đường | 53.05 | 7.78 | 0.871 |
| road-edges-c / 7 | Ngã ba ba phiến | 54.28 | 7.07 | 0.999 |
| road-edges-c / 8 | Bậc đá ba phiến | 58.13 | 6.76 | 0.963 |

Mép mềm tờ a đạt **13,54–19,78% ≥ 10%**. Tờ b không có yêu cầu tỷ lệ mềm; tờ c dùng khoảng mềm 9px theo phiếu.

Hue `trail-worn` = **41,633°**. Tờ a theo thứ tự ô:

| Ô | H trung vị | Lệch so với trail (≤12°) |
|---|---:|---:|
| 1 | 38.182° | 3.451° |
| 2 | 38.710° | 2.923° |
| 3 | 41.538° | 0.094° |
| 4 | 43.902° | 2.270° |
| 5 | 32.571° | 9.061° |
| 6 | 33.333° | 8.299° |
| 7 | 40.645° | 0.987° |
| 8 | 40.000° | 1.633° |

Độ lệch lớn nhất **9,061°**, ở đất dưới tán; ô đá lát cũng đo và đạt dù không phải món đất thuần.

### 4.3 Rice

`magick identify` xác nhận cả năm ô **1024 × 1024, sRGB, RGB ba kênh, 8-bit, không alpha**. Bốn ô có cây đúng tám hàng; tự tương quan lấy từ profile luma trung bình theo cột, tìm đỉnh trong khoảng 96–160px. Pha là cực tiểu harmonic chu kỳ 128px, đo cùng quy tắc ở cả bốn ô.

| Ô | H° | S | L trung vị | E | I | E/I (≤1,25) | Chu kỳ px | Pha px |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| rice-flooded | 78.462 | 0.0769 | 0.5378 | 0.000000 | 0.022265 | 0.000 | 129 | 66.730 |
| rice-seedling | 108.571 | 0.2333 | 0.4731 | 0.000000 | 0.037243 | 0.000 | 128 | 64.329 |
| rice-green | 110.000 | 0.4095 | 0.4247 | 0.000000 | 0.047273 | 0.000 | 128 | 61.160 |
| rice-ripe | 42.353 | 0.6180 | 0.5230 | 0.000000 | 0.069135 | 0.000 | 128 | 61.069 |
| rice-stubble | 34.468 | 0.2747 | 0.4806 | 0.000000 | 0.065489 | 0.000 | 128 | 63.599 |

**Lệch pha lớn nhất giữa hai ô có cây: 3.261px ≤ 8px.** Chu kỳ flooded chỉ ghi để tham khảo; ô chưa cấy không thuộc kiểm hàng cây.

Màu đạt từng điều kiện: seedling/green H 75–140°, S ≤ 0,55; ripe H 38–55° (phiếu không giới hạn S của ripe); stubble H 25–50°, S ≤ 0,35; flooded S ≤ 0,30, L 0,45–0,70.

E/I trước sửa mép trên các bản chọn: flooded **2,190**, seedling **1,667**, green **1,474**, ripe **1,572**, stubble **1,580**. Các giá trị trước/sau và profile 1024 cột giữ trong JSON, không chỉ giữ con số đạt cuối.

## 5. Ghép thử và tự chấm M, Q trên bản hậu kỳ

- [123-on-ground.jpg](../../games/typing-defense/art-src/_review/123-on-ground.jpg): 1280 × 480, ba hàng a/b/c, tám món mỗi hàng. Mỗi vật đúng **512px trên ô đất 1024px**, rồi mới thu từng ô xuống 160px. a/b trên grass-jade, c trên trail-worn của 122.
- [123-terraces.jpg](../../games/typing-defense/art-src/_review/123-terraces.jpg): 1280 × 856. Hàng đầu năm ô flooded → seedling → green → ripe → stubble, mỗi ô lát 3×3. Phần dưới ba bậc giả seedling/green/ripe, mặt ruộng dùng tile 3×3, bờ dùng courtyard v2. Chỉ ghép tranh thật và biến dạng phối cảnh ở ảnh kiểm.
- [123-vs-ref.jpg](../../games/typing-defense/art-src/_review/123-vs-ref.jpg): hai ảnh ghép và ảnh chủ dự án cùng cao 640px ở hàng trên; hàng dưới là đủ hai atlas 097 và năm ô 098. Không lấy bộ cũ làm thước điểm.

**đứng cạnh được:** chất liệu đá, đất, gỗ và nước đã có độ hoàn thiện thật, màu khoáng dịu, bóng khối tự nhiên, không viền mực hay hình đồ chơi; các hàng rice đọc rõ ở xa. Đây là mức vật liệu phát hành được, ảnh tham chiếu của chủ dự án vẫn là mốc 9.

### 5.1 Hòa nền từng nhóm

Tờ a: đất sáng 1/2, ngã ba, thẳng, cong và đá lát hòa mép tốt. Hai mảng đất dưới tán tối, có lá mục, còn đọc như đảo màu nâu trên grass-jade khi đặt giữa bãi trống; hợp khi đặt dưới tán như đề bài. Không phủ màu để che khác biệt này.

Tờ b: huệ, dã quỳ là hai điểm nhấn nổi rõ; hai cụm sỏi, gốc cây, vòng gỗ và vũng nước có mép vật liệu tự nhiên. Lá bàng đỏ thành một khối dày, là món **còn cảm giác đặt lên nền rõ nhất**; bờ đất nhỏ quanh vũng nước cũng đọc rõ khi đứng một mình trên cỏ. Không có quầng magenta hay viền mực. Lá đỏ và hoa nên rải thưa khi tích hợp.

Tờ c: cả tám món hòa vào đất khaki và đá vôi của trail-worn; cỏ trùm và quạt sỏi tự nhiên nhất. Bờ thẳng/cong, phiến vỡ, ngã ba và ba bậc có mối nối vật liệu và vai đường rõ. Vệt bánh xe có hai rãnh nước bạc. Trả lời câu PATH_QUALITY: **không**, các món mép đường không trông như vệt quệt. Bộ này là decal bổ trợ, chưa phải ảnh duyệt đường trong runtime.

Rice: flooded có nước bạc và nền bùn lộ; seedling thưa hơn green; ripe sáng vàng; stubble đã có đầu rạ cụt. Ở 256px còn nhận được bốn giai đoạn cây. Nhịp tám hàng còn đều và tính lặp dễ thấy trên mảng 3×3, là giới hạn của ô hàng lúa đúng đề, không phải đường nối bị hở.

### 5.2 Điểm

Đã xem các PNG cuối ở cỡ đầy đủ, ảnh ghép, từng ô rice 256px và **toàn atlas decal thu còn 256px** (khắt khe hơn 256px mỗi vật). Bản xem alpha trên nền trung tính ở `_review/123/*-full-opaque.jpg`; bản nhỏ ở `_review/123/delivery/*-256.jpg`. M chấm từ hai ảnh ghép hậu kỳ, Q chấm ảnh cuối.

Năm số Q theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Dùng tiếp chỉ cho 2 vì kiểm số ảnh cuối đã đạt.

| Ảnh chọn | M trên ghép | Q đầy đủ: năm tiêu chí | Tổng | Q 256px: năm tiêu chí | Tổng | Điểm còn thiếu |
|---|---:|---|---:|---|---:|---|
| ground-decals-a | 8,0 | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9,0 | Hai ô dưới tán nâu hơn cỏ, chi tiết lá nhập ở cỡ nhỏ |
| ground-decals-b | 8,0 | 1,5 / 2 / 1,5 / 2 / 2 | 9,0 | 1,5 / 1,5 / 1,5 / 2 / 2 | 8,5 | Huệ còn cách điệu về tán; lá đỏ và vòng gỗ dày, hoa là điểm nhấn mạnh |
| road-edges-c | 8,2 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | Độ cong bờ còn nhẹ, sỏi nhỏ nhập khi thu cả atlas |
| rice-flooded | 8,0 | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9,0 | Phản chiếu bạc hơi đều khi lát lớn |
| rice-seedling | 8,0 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | Mạ cách điệu thành dải liên tục, nhịp lặp khá rõ |
| rice-green | 8,2 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | Tán lá có hướng thuận rõ, nhịp luống đều |
| rice-ripe | 8,2 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | Các cụm bông còn lặp nhịp rõ trên mảng lớn |
| rice-stubble | 8,0 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | Gốc rạ dày, cỡ nhỏ nhập thành khối rơm |

Hai ảnh ghép: **on-ground M = 8,0; terraces M = 8,0**. Tự chấm đạt M ≥ 8 và Q ≥ 8 cho cả tám ảnh; chưa có điểm chấm lại của Claude, chưa coi là nghiệm thu của chủ dự án.

## 6. Script, phạm vi và việc cần xem

- `process.py`: đọc RGB qua ImageMagick 7, tách nền, giữ khung toàn vật, alpha mềm, sửa mép rice và đo. Chỉ thư viện chuẩn Python; không cài thêm gói.
- `review.py`, `deliver.py`: ghép atlas, tờ so, ảnh ghép và chép bản chọn; `deliver.py` giữ tờ magenta cùng bố cục alpha và mật độ ba tile ở bậc ruộng giả.
- `inspect.py`: ảnh alpha cỡ đầy đủ trên nền trung tính. `audit.py`: đo lại **file giao**, identify và MD5. `selection-preview.json`: chọn lượt và độ dịch hàng. `run.sh`: thứ tự chạy hậu kỳ từ nguyên liệu gốc. `write-report.py`: lập bảng báo cáo từ số đo.
- Script chặn ghi đè. Để tái dựng toàn bộ, dùng bản sao bộ nguyên liệu chỉ có `.tryN.png`/prompt trong cùng cây thư mục và đầu ra trống; không chạy chồng `run.sh` lên bộ giao đang có. Không cần mạng cho hậu kỳ.
- Đã đọc tiêu chuẩn, 097, 098, phiếu 123, ảnh chủ dự án và ô đất v2; không chạy game, dev server, trình duyệt, build hay test suite. Không dùng lệnh Git. Không đọc/ghi vùng Tu Tiên, không sửa mã hoặc tài liệu khác.
- Không bỏ món nào. Khác phiếu chỉ ở tổng tám ảnh theo danh sách thật, kích thước nguồn công cụ 1254px giữ nguyên để lưu, và tờ ghép kiểm là cảnh dựng bằng script đúng yêu cầu, không phải kiểm runtime.
- Không có capture trình duyệt cần prune. Mọi bản sinh được giữ theo yêu cầu; ảnh kiểm nằm trong vùng `_review/123` được phiếu cho phép.

**Claude/chủ dự án cần xem:** ba ảnh ghép chính, tám tờ trước–sau, đặc biệt huệ trắng, mảng lá đỏ và hai ô đất dưới tán. Chấm lại M và Q trước tích hợp; bộ giao chưa được chép vào `public/`.
