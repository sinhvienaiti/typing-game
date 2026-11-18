# Phiếu 157 · Last Line · Icon súng canh và chân dung Bầy Hố Đen · báo cáo

Ngày 29/10/2026 · Mac mini M4 · hướng **B · Lightbearer**.

**Đã giao đủ 11 ảnh `.v2` và 33 bản thu, kèm prompt, 12 bản sinh nguyên gốc, 11 tờ trước–sau và các tờ đối chiếu. Chưa đủ điều kiện “xong mọi kiểm”: Pack Leader ở 34 px có tương phản lớn nhất 0,249279, dưới 0,25.** Giữ tranh, không làm tròn thành đạt; chuyển Claude quyết theo ART_ACCEPTANCE §5. Các ảnh còn lại qua phép đo trên ít nhất một trong hai nền HUD được phiếu quy định. Chưa có chấm nhận độc lập của Claude.

## 1. Bộ giao và nguồn

Dùng **skill imagegen, công cụ tích hợp image_gen**, không gọi API sinh ảnh ngoài. Mỗi ảnh đính kèm ảnh cũ cùng tên và có nguyên câu:

> Keep the same object identity as the attached image. Repaint it in the new style as described.

Năm súng bám đúng năm `models-src/sentinel-*.png` của 156: vỏ ceramic trắng, mép vàng, hốc graphite, Pulse hai nòng, Heat một thấu kính cam, Scatter năm nòng, Rail hai ray, Mortar nòng rộng hướng lên có lỗ sao. Sáu quái lấy kính đen nứt sáng từ `concepts/b-lightbearer-fight.png`. Thêm ảnh cỡ vật `gun-xung.norm.256.png`, khung `portrait-ring` của 127 và `loadout-bg` của 121 vào prompt của mười ảnh sau; Pulse đầu tiên dùng trực tiếp ảnh cũ và nguồn 156. Đã xem riêng ảnh mức hoàn thiện của chủ dự án.

Mỗi hàng có đủ `.v2.png`, `.v2.256.png`, `.v2.128.png`, `.v2.64.png`; mỗi PNG giao có prompt cùng tên bên cạnh. Bản sinh giữ ở `.v2.tryN.png` và `.v2.tryN.prompt.txt`. Không ghi đè ảnh cũ.

| Ảnh gốc giao | Lượt chọn | Prompt chính xác | Tờ hậu kỳ |
| --- | ---: | --- | --- |
| [Pulse Gun](../../games/typing-survival/art-src/ui/icons/gun-xung.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/icons/gun-xung.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-gun-xung-before-after.jpg) |
| [Heat Beam](../../games/typing-survival/art-src/ui/icons/gun-tia.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/icons/gun-tia.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-gun-tia-before-after.jpg) |
| [Scatter Gun](../../games/typing-survival/art-src/ui/icons/gun-tan.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/icons/gun-tan.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-gun-tan-before-after.jpg) |
| [Rail Gun](../../games/typing-survival/art-src/ui/icons/gun-ray.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/icons/gun-ray.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-gun-ray-before-after.jpg) |
| [Star Mortar](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-gun-phao-sao-before-after.jpg) |
| [Swarm](../../games/typing-survival/art-src/ui/foes/swarm.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/foes/swarm.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-swarm-before-after.jpg) |
| [Scout](../../games/typing-survival/art-src/ui/foes/scout.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/foes/scout.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-scout-before-after.jpg) |
| [Brute](../../games/typing-survival/art-src/ui/foes/brute.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/foes/brute.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-brute-before-after.jpg) |
| [Pack Leader](../../games/typing-survival/art-src/ui/foes/pack-leader.v2.png) | 2 | [Prompt](../../games/typing-survival/art-src/ui/foes/pack-leader.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-pack-leader-before-after.jpg) |
| [Shield Guard](../../games/typing-survival/art-src/ui/foes/shield-guard.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/foes/shield-guard.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-shield-guard-before-after.jpg) |
| [Splitter](../../games/typing-survival/art-src/ui/foes/splitter.v2.png) | 1 | [Prompt](../../games/typing-survival/art-src/ui/foes/splitter.v2.prompt.txt) | [Bản sinh – hậu kỳ](../../games/typing-survival/art-src/_review/157-splitter-before-after.jpg) |

Danh mục máy: [deliverables.json](../../games/typing-survival/art-src/_review/157/deliverables.json). Đường dẫn gốc công cụ trả về: [generation.json](../../games/typing-survival/art-src/_review/157/generation.json). **12/12 bản `.tryN.png` trùng MD5 với file công cụ sinh**, đã kiểm trong [final-checks.json](../../games/typing-survival/art-src/_review/157/final-checks.json).

## 2. Lượt sinh và sửa prompt

Mọi prompt mở bằng nguyên khối **STYLE-UI** của ART_DIRECTION §4.3, tiếp đến KIND ICON hoặc PORTRAIT, vai trò từng ảnh đính kèm, mô tả riêng và dòng alpha thật. KIND được viết theo định dạng của 149/015: khối lớn gọn, đủ vật, không huy hiệu/khung vẽ trong icon, không chữ, giữ lề; không chép phong cách công nghiệp cũ.

| Nhóm/lượt | Đã yêu cầu hoặc sửa | Quyết định |
| --- | --- | --- |
| Năm súng · lượt 1 | Giữ tên/nhận diện súng cũ, lấy **hình thân mới của 156 làm chuẩn**; bỏ tay cầm, tàu, bệ, đạn và hiệu ứng bắn rời. Nêu rõ 2 nòng / 1 kính / 5 nòng / 2 ray / 1 nòng rộng có lỗ sao. | Chọn cả năm. Không sinh lại. |
| Swarm · lượt 1 | Giữ mắt tròn và gai; thêm chân trước, thân kính đen phản quang và nứt cam. | Chọn. |
| Scout · lượt 1 | Thân hẹp, chân dài, mắt lam trắng, nứt cam và khoảng trống quanh chân. | Chọn; còn vài đường lam ngoài mắt, trừ điểm đúng đề/hợp bộ. |
| Brute · lượt 1 | Giữ đầu và hàm cũ; vai lớn, cẳng tay nặng, nứt hổ phách. | Chọn; vẫn có gai vai lớn. |
| Pack Leader · lượt 1 | Yêu cầu vương miện và nứt vàng; công cụ vẫn bám dàn gai lưng cũ. | Không chọn: dấu nhận diện vương miện chưa đạt, Đúng đề 1/2; giữ nguyên bản sinh. |
| Pack Leader · lượt 2 | Đổi sang chân dung chính diện cao hẹp; **năm gai mọc trên đầu, phía trên mắt**, gai giữa cao nhất; vai hẹp, móng thu vào. | Chọn: vương miện đã rõ. Không chạy lượt 3 để đổi một tranh đạt hình chỉ vì sai số tương phản rất nhỏ. |
| Shield Guard · lượt 1 | Giữ mặt có sừng sau khiên; khiên năng lượng lam lớn, thân kính đen nứt cam. | Chọn; trang trí khiên hơi gần bộ UI phe ta. |
| Splitter · lượt 1 | Ba thùy kính sát nhau, hai khe tách rộng, ánh cam bên trong. | Chọn; chưa phải ba cá thể có đầu riêng. |

## 3. Hậu kỳ và bảo toàn phần vẽ

Công cụ sinh trả **1254 × 1254, sRGBA, alpha thật**; không dùng nền khóa M/G. Bản giao là **1024 × 1024, sRGBA**, ba bản thu **256² / 128² / 64²**, tất cả đúng khổ: [identify-final.txt](../../games/typing-survival/art-src/_review/157/identify-final.txt).

Phần thân đục của bản sinh thường có alpha khoảng 253/255 thay vì 255. Hậu kỳ đầu cắt theo mọi alpha > 0 khiến một số vùng alpha rất mờ kéo lệch hộp, nên vài vật còn nhỏ hoặc lệch tâm. Đã giữ nguyên lần đầu ở [processed/](../../games/typing-survival/art-src/_review/157/processed/) và số đo [measurements.json](../../games/typing-survival/art-src/_review/157/measurements.json), không dùng làm bộ giao.

Bản chọn cuối ở [processed-v2/](../../games/typing-survival/art-src/_review/157/processed-v2/):

1. Lấy mặt nạ thân ở alpha > 127. Dựng vùng lõi bằng Erode Disk:3 và vùng đỡ bằng Dilate Disk:3. Chỉ chuẩn hóa **alpha**: lõi thành 255, ngoài vùng đỡ thành 0, giữ alpha sinh trong dải mép. Giữ nguyên mọi kênh RGB.
2. Cắt nền trong suốt thừa, thu **đồng dạng** vào hộp 717 × 717 bằng Lanczos, đặt giữa canvas 1024². Không kéo méo, xoay hoặc ghép bộ phận.
3. Kiểm lại/chuẩn hóa dải alpha 3 px ở khổ giao. **So từng kênh RGB giữa bản hình học và bản alpha cuối: 0 kênh thay đổi cho cả 11 ảnh.** Không đổi gamma, chỉnh sáng, sơn đè, phủ màu hoặc san phần vẽ.
4. Ba bản thu lấy trực tiếp từ master 1024 bằng Lanczos, không qua chuỗi thu và không làm nét 64.

Script cuối: [process_v2.py](../../games/typing-survival/art-src/_review/157/process_v2.py); lệnh và thông số: [processing-v2.json](../../games/typing-survival/art-src/_review/157/processing-v2.json). Tờ trước–sau ở bảng §1 hiển thị hai canvas cùng cỡ 1024; khác cỡ vật là do chuẩn hóa lề, không phải mất phần vẽ.

## 4. Khổ, alpha và khung

Số đo trên **bản giao**; master trùng byte với ứng viên đã đo. Hộp bao lấy alpha > 16, tọa độ **trái / trên / phải loại trừ / dưới loại trừ**. Lệch tâm là trị tuyệt đối lớn nhất của hai trục, chia cạnh ảnh.

**11/11 ảnh: alpha min 0, max 255; pixel bán trong suốt nằm ngoài dải mép 3 px = 0; kênh RGB thay đổi do bước sửa alpha = 0.** Không có màu khóa thực; vẫn đo hue magenta 300° ± 15°, S > 0,5 trên mọi pixel alpha > 0 để kiểm phòng viền lẫn màu. Cả 11 dưới 0,2%.

| Ảnh | Hộp bao x0 / y0 / x1 / y1 | Cạnh dài / canvas | Lệch tâm lớn nhất | Pixel alpha 1–254 | Hue M / pixel alpha > 0 |
| --- | --- | ---: | ---: | ---: | ---: |
| Pulse Gun | 154 / 219 / 869 / 805 | 69,82% | 0,049% | 8 172 | 0,0424% |
| Heat Beam | 154 / 220 / 869 / 804 | 69,82% | 0,049% | 8 989 | 0,0212% |
| Scatter Gun | 154 / 273 / 869 / 750 | 69,82% | 0,049% | 7 555 | 0,0807% |
| Rail Gun | 154 / 164 / 869 / 859 | 69,82% | 0,049% | 10 343 | 0,0562% |
| Star Mortar | 222 / 154 / 801 / 869 | 69,82% | 0,049% | 8 775 | 0,0512% |
| Swarm | 154 / 172 / 869 / 852 | 69,82% | 0,049% | 13 554 | 0,0371% |
| Scout | 212 / 154 / 811 / 870 | 69,92% | 0,049% | 21 291 | 0,0819% |
| Brute | 154 / 165 / 869 / 858 | 69,82% | 0,049% | 15 721 | 0,0342% |
| Pack Leader | 289 / 153 / 735 / 869 | 69,92% | 0,098% | 14 447 | 0,0560% |
| Shield Guard | 181 / 154 / 843 / 869 | 69,82% | 0,049% | 16 046 | 0,0487% |
| Splitter | 154 / 239 / 869 / 784 | 69,82% | 0,049% | 12 443 | 0,0288% |

Cạnh dài **715–716 px = 69,82–69,92%**, trong 68–72%; lệch tâm lớn nhất **0,098%**, dưới 2%. Nguồn số và cách đo: [measurements-v2.json](../../games/typing-survival/art-src/_review/157/measurements-v2.json), script [validate_v2.py](../../games/typing-survival/art-src/_review/157/validate_v2.py).

### 4.1 Tương phản đúng cỡ trong game

Thu từ master về đúng **28 / 42 px** cho súng và **34 / 51 px** cho quái. Luma dùng trọng số Rec.709 trên các kênh sRGB chuẩn hóa, ghép alpha lên nền, lấy trung bình trong vùng alpha > 127. Ghi trị tuyệt đối của chênh luma; không dùng điểm sáng nhất, không bỏ phần thân tối. Hai nền giữ đúng mã phiếu: **than chì #14181f** và **thép sáng #8c96a3**.

| Ảnh | 720p than chì | 720p thép sáng | 1080p than chì | 1080p thép sáng | Kết quả |
| --- | ---: | ---: | ---: | ---: | --- |
| Pulse Gun | 0,4042 | 0,0697 | 0,4103 | 0,0675 | Đạt trên than chì |
| Heat Beam | 0,4214 | 0,0455 | 0,4291 | 0,0452 | Đạt trên than chì |
| Scatter Gun | 0,3847 | 0,0828 | 0,3953 | 0,0812 | Đạt trên than chì |
| Rail Gun | 0,3784 | 0,0731 | 0,3921 | 0,0681 | Đạt trên than chì |
| Star Mortar | 0,3778 | 0,0914 | 0,3845 | 0,0913 | Đạt trên than chì |
| Swarm | 0,1646 | 0,3061 | 0,1681 | 0,3095 | Đạt trên thép sáng |
| Scout | 0,1508 | 0,2848 | 0,1579 | 0,2943 | Đạt trên thép sáng |
| Brute | 0,1725 | 0,2949 | 0,1749 | 0,2988 | Đạt trên thép sáng |
| Pack Leader | 0,2019 | 0,2493 | 0,2080 | 0,2533 | **Thiếu 0,000721 ở 34 px** |
| Shield Guard | 0,2021 | 0,2608 | 0,2059 | 0,2653 | Đạt trên thép sáng |
| Splitter | 0,1883 | 0,2729 | 0,1918 | 0,2771 | Đạt trên thép sáng |

**Giới hạn cần quyết:** cả sáu quái đều dưới 0,25 trên nền than chì. Năm quái qua ngưỡng nhờ nền thép sáng; Pack Leader ở 34 px vẫn thiếu **0,000721** trên nền thép, còn ở 51 px đạt **0,253281**. Không coi “0,2493 ≈ 0,25” là qua. Phiếu viết “ít nhất một trong hai nền tối” nhưng lại quy định nền thép sáng cho Last Line; báo cáo dùng **ít nhất một trong hai mã nền được nêu**, đồng thời ghi đầy đủ hai số để Claude xem cách áp dụng. Nếu bắt buộc nền than chì riêng thì cả sáu quái chưa qua kiểm tương phản.

Đã xem tranh nhỏ: vương miện Pack Leader và khiên lam Shield Guard vẫn đọc ra. Giữ màu kính đen và nứt vàng của Pack Leader theo **ART_ACCEPTANCE §5**, không chỉnh màu/làm phẳng tranh chỉ để đưa số sát ngưỡng qua 0,25. **Dùng tiếp của Pack Leader chỉ 1/2**, chờ Claude quyết. Các quái tối khác cũng cần xem trực tiếp trên nền dự định gắn, không suy từ phép đạt trên thép sáng thành đã đạt trên mọi nền.

### 4.2 Dáng ở 32 px và 34 px

Thu toàn canvas về cỡ kiểm bằng Lanczos, threshold alpha > 127; không dịch, xoay hoặc đổi tỷ lệ riêng để giảm IoU. **55/55 cặp trong cả phiếu ở 32 px ≤ 0,80**; lớn nhất **0,7344**, Swarm – Shield Guard.

| Ảnh | Cặp có IoU 32 px lớn nhất | IoU |
| --- | --- | ---: |
| Pulse Gun | Heat Beam | 0,6582 |
| Heat Beam | Scatter Gun | 0,6877 |
| Scatter Gun | Heat Beam | 0,6877 |
| Rail Gun | Shield Guard | 0,3671 |
| Star Mortar | Swarm | 0,7171 |
| Swarm | Shield Guard | 0,7344 |
| Scout | Star Mortar | 0,5142 |
| Brute | Swarm | 0,6163 |
| Pack Leader | Star Mortar | 0,4981 |
| Shield Guard | Swarm | 0,7344 |
| Splitter | Swarm | 0,6030 |

Riêng sáu chân dung ở **34 px: 15/15 cặp ≤ 0,80**, lớn nhất **0,7291**:

| Cặp quái | IoU 34 px |
| --- | ---: |
| Swarm – Scout | 0,4343 |
| Swarm – Brute | 0,6152 |
| Swarm – Pack Leader | 0,4536 |
| Swarm – Shield Guard | 0,7291 |
| Swarm – Splitter | 0,5855 |
| Scout – Brute | 0,4602 |
| Scout – Pack Leader | 0,3520 |
| Scout – Shield Guard | 0,4298 |
| Scout – Splitter | 0,4377 |
| Brute – Pack Leader | 0,3025 |
| Brute – Shield Guard | 0,6218 |
| Brute – Splitter | 0,5583 |
| Pack Leader – Shield Guard | 0,4127 |
| Pack Leader – Splitter | 0,3448 |
| Shield Guard – Splitter | 0,5329 |

## 5. Tờ xem và chấm trên bản hậu kỳ

- [157-sheet.jpg](../../games/typing-survival/art-src/_review/157-sheet.jpg): hàng 256 px; hàng 1080p trên hai nền; hàng 720p trên hai nền; bốn icon cũ, mảnh HUD tham chiếu chủ dự án và tham chiếu 121/127.
- [157-old-new-64.jpg](../../games/typing-survival/art-src/_review/157-old-new-64.jpg): đúng **hai hàng cũ / mới, cùng canvas 64 px**. Súng cũ dùng bản `.norm` của 108, quái cũ dùng master của 089.
- [157-sentinel-match.jpg](../../games/typing-survival/art-src/_review/157-sentinel-match.jpg): năm nguồn 156 cạnh năm icon mới cùng khổ hiển thị, thêm các ô 28/42 px. Chỉ tách xanh nguồn 156 trong tờ xem; không sửa file nguồn.
- [157-foes-small.jpg](../../games/typing-survival/art-src/_review/157-foes-small.jpg): sáu chân dung ở 34/51 px trên hai nền.
- **11 tờ “bản sinh | bản hậu kỳ”**: liên kết riêng từng ảnh ở §1. Font ghi nhãn Arial của macOS.

Đã xem **từng PNG giao 1024²**, sau đó xem các cỡ 28/34 px và 42/51 px trên hai nền. Chấm M theo mức hoàn thiện icon/chân dung thương mại, so chi tiết và độ đọc của HUD trong ảnh chủ dự án; không áp tiêu chí trời và ba lớp cảnh của tranh nền lên icon alpha.

Q theo đúng thứ tự **Đúng đề · Đọc được · Hợp bộ · Hình khối · Dùng tiếp**, mỗi tiêu chí 0–2. Đây là tự chấm của Codex, chưa có nhận độc lập.

| Ảnh hậu kỳ | M gốc / 720p | Q gốc · năm tiêu chí | Q 720p · năm tiêu chí | Phần còn yếu |
| --- | ---: | --- | --- | --- |
| Pulse Gun | 8,5 / 8,5 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Vàng khá bóng; hai nòng vẫn tách được ở 28 px. |
| Heat Beam | 8,5 / 8,5 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Lõi cam rõ; dáng thân gần Pulse nhưng một miệng kính lớn. |
| Scatter Gun | 8,5 / 8,5 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Đúng năm nòng; ở 28 px hai nòng ngoài rất nhỏ. |
| Rail Gun | 8,5 / 8,0 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Hai ray và coil đúng nguồn; khe ray mảnh ở 28 px. |
| Star Mortar | 8,5 / 8,5 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Nòng rộng hướng lên rõ; lỗ sao thành điểm lam ở 28 px. |
| Swarm | 8,5 / 8,0 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Giữ mắt tròn/gai cũ; thân vẫn khá gần vật cơ khí dù đã có chân bò. |
| Scout | 8,5 / 8,0 | 1,5 · 2 · 1,5 · 2 · 2 = **9,0** | 1,5 · 1,5 · 1,5 · 2 · 2 = **8,5** | Còn phản quang/đường lam trên thân ngoài mắt; chân mảnh, dễ chìm trên than chì. |
| Brute | 8,5 / 8,5 | 2 · 2 · 2 · 1,5 · 2 = **9,5** | 2 · 1,5 · 2 · 1,5 · 2 = **9,0** | Vai và tay nặng hơn Scout; gai vai vẫn lớn hơn yêu cầu phụ của prompt. |
| Pack Leader | 8,5 / 8,0 | 2 · 2 · 2 · 2 · 1 = **9,0** | 2 · 1,5 · 2 · 2 · 1 = **8,5** | Vương miện năm gai đã rõ; Dùng tiếp chỉ 1 do kiểm tương phản 34 px chưa qua. |
| Shield Guard | 8,5 / 8,5 | 2 · 2 · 1,5 · 2 · 2 = **9,5** | 2 · 1,5 · 1,5 · 2 · 2 = **9,0** | Khiên lam nhận ra ngay; chỉ vàng/glyph trên khiên hơi giống bộ UI phe ta. |
| Splitter | 8,5 / 8,0 | 1,5 · 2 · 2 · 2 · 2 = **9,5** | 1,5 · 1,5 · 2 · 2 · 2 = **9,0** | Đọc ba thùy với hai khe tách; chưa thành ba cá thể có mặt riêng. |

M và Q đều từ 8 cho bộ chọn, nhưng **điểm không thay được kiểm số**. Pack Leader chưa đủ điều kiện xong toàn phiếu. Các ảnh M/Q sát 8–8,5 cần Claude chấm lại theo ART_ACCEPTANCE §4; không ghi vào ART_REPLACE_LATER vì ngoài phạm vi được phép ghi.

## 6. KA1 và chạy lại

Dùng **md5 -r** trước lần ghi đầu và sau khi giao; **diff chỉ có dòng thêm**, không có file cũ thay đổi hoặc mất:

| Phạm vi | Trước | Sau | File cũ nguyên MD5 | Thêm | Sửa / mất |
| --- | ---: | ---: | ---: | ---: | ---: |
| Hai thư mục đích ui/icons và ui/foes | 80 | 192 | **80/80** | 112 | **0 / 0** |
| Toàn cây art-src | 1 765 | 2 224 | **1 765/1 765** | 459 | **0 / 0** |

Bằng chứng: [md5-before.txt](../../games/typing-survival/art-src/_review/157/md5-before.txt), [md5-after.txt](../../games/typing-survival/art-src/_review/157/md5-after.txt), [md5-diff.txt](../../games/typing-survival/art-src/_review/157/md5-diff.txt); toàn cây dùng các file `md5-art-*`; [ka1-result.json](../../games/typing-survival/art-src/_review/157/ka1-result.json). Ảnh chụp MD5 ghi trạng thái tại lúc chạy, không tự băm các file kết quả đang được tạo; không có media sinh mới sau ảnh chụp này.

[final-checks.json](../../games/typing-survival/art-src/_review/157/final-checks.json) xác nhận **44/44 PNG đúng khổ/sRGBA**, **44/44 prompt giao trùng prompt lượt chọn**, **11/11 master trùng file đã đo**, **12/12 bản sinh nguyên MD5**.

Các script đã dùng nằm trong [_review/157/](../../games/typing-survival/art-src/_review/157/). Chạy lại vào thư mục mới, không ghi đè bộ giao:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/typing-survival/art-src/_review/157/replay.py ten-thu-muc-moi
```

Đã chạy với `replay-check`: **11/11 bản tái tạo trùng từng pixel RGBA**, xem [verification.json](../../games/typing-survival/art-src/_review/157/replay-check/verification.json). Lệnh này chỉ đọc 12 nguồn đã giữ và tái tạo hậu kỳ, không gọi mạng/sinh ảnh. `deliver.py`, `sheets.py`, `final_checks.py`, `snapshot.py` đều giữ trong thư mục kiểm; các lệnh giao chính từ chối đè file đã tồn tại.

## 7. Việc bỏ qua và việc cần xem

- **Không gắn runtime/public, không sửa code hoặc đổi tham chiếu ảnh cũ**: Claude gắn sau khi nhận. Không chạy Git, build, test game, dev server hay trình duyệt; không đọc/ghi Tu Tiên, worktree hay công cụ audio.
- Không tạo âm, model 3D, ảnh nền, UI mới ngoài 11 mục. Không dùng hình vẽ bằng mã thay ảnh.
- Không sửa ART_REPLACE_LATER hoặc tài liệu khác ngoài báo cáo này vì không nằm trong danh sách cho phép.
- **Claude/chủ dự án cần xem:** tờ nguồn 156 cạnh icon mới; sáu chân dung trên đúng nền dự định dùng; vương miện Pack Leader và khiên lam ở 34 px; vết lam còn lại trên Scout; Splitter mới thể hiện ba thùy chứ chưa ba đầu riêng.
- **Điểm cần quyết trước khi nhận trọn phiếu:** Pack Leader 34 px **0,249279 < 0,25**; cách áp dụng nền thép sáng trong câu “hai nền tối”. Giữ tranh, báo đúng số, không tự tuyên bố đủ mọi điều kiện xong.

