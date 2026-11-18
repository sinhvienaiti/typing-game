# Phiếu 167 · Wordwoven · Vẽ lại chín chân dung

Ngày làm: 29/10/2026, repo cha trên Mac mini M4, macOS.

**Đã giao đủ chín chân dung `.v2`, 27 bản thu và prompt cạnh từng ảnh; giữ 11 lượt sinh nguyên byte. Cả 36 PNG đạt khổ/kênh, lề, hai kiểm alpha và tương phản luma trên nền ngọc lấy từ khung 115/160. KA5 tự chấm trên bản hậu kỳ đạt 8,5–9. Chưa đóng phiếu: 24/36 cặp trượt IoU ≤ 0,80; giữ nguyên tranh theo ART_ACCEPTANCE §5 để Claude quyết. Chưa có chấm nhận độc lập của Claude.**

## 1. Nơi giao và bằng chứng

- Bộ ảnh: [art-src/portraits/](../../games/typing-defense/art-src/portraits/), chín tên của phiếu với hậu tố `.v2.png`, `.v2.256.png`, `.v2.128.png`, `.v2.64.png`. Không có ảnh mới nào được chép vào `public/`.
- [Tờ xem bốn hàng 167-sheet.jpg](../../games/typing-defense/art-src/_review/167-sheet.jpg): bản 256 px; cỡ 1080p trên hai nền; cỡ 720p trên hai nền; chân dung cạnh bốn trang trí 115 đã nhận và mảnh HUD mẫu.
- [Cũ–mới cùng cỡ 64 và 32 px, hai hàng](../../games/typing-defense/art-src/_review/167-old-new.jpg). Ảnh cũ chỉ được tách nền vào thư mục kiểm và căn cùng lề để so công bằng; file gốc không đổi.
- [Cỡ thật, không phóng to](../../games/typing-defense/art-src/_review/167-native.jpg), gồm cả Mộc Tinh 29/24 px ở lời boss.
- [Tổng hợp bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/167-raw-post.jpg). Mỗi ảnh còn có `<tên>-raw-post.jpg` và `<tên>-aligned-raw-post.jpg` trong [167/](../../games/typing-defense/art-src/_review/167/); tờ aligned đặt đúng cùng cỡ vật để so phần vẽ.
- [Thử đặt sau vòng chân dung 115](../../games/typing-defense/art-src/_review/167-ring.jpg), ghép tĩnh 96 px; đây không phải ảnh chạy game.
- [Cạnh bốn icon mới](../../games/typing-defense/art-src/_review/167-context.jpg): seeds, day, night, pause của bộ `134-final`. Các icon này chưa có chứng từ Claude nhận trong tài liệu đã đọc; không gọi chúng là đã nghiệm thu.

Chỉ ghi chín họ tên `.v2*`, `_review/167*` và báo cáo này. Không dùng Git, dev server, trình duyệt, mạng ngoài `image_gen`, build hay test suite game. Không đọc/ghi Tu Tiên, không đụng worktree, không sửa code hoặc tài liệu khác. Không có frame chụp game mới cần dọn.

## 2. Nguồn và prompt từng lượt

Dùng skill `imagegen` và công cụ tích hợp **image_gen**, một ảnh mỗi lần. STYLE-UI của phiếu 115 và PORTRAIT §3.4 được chép nguyên văn. Phần riêng đặt sau hai khối ghi rõ câu viền mực cũ được thay bằng mép vẽ sạch, vật liệu có chiều sâu và phong cách painterly-realistic mới. Không chép STYLE sách tranh cũ.

Mỗi lượt đính kèm ảnh cũ cùng tên, vòng 115 và keyart 113, với câu bắt buộc `Keep the same object identity as the attached image. Repaint it in the new style as described.` Vòng thật nằm ở **`ui/frames-epic/portrait-ring.png`**, khác đường dẫn `ui/frames/` của phiếu; báo cáo 115 và verdict 29/10 xác nhận đúng bộ, vòng đã được Claude nhận. Keyart dùng `ui/title-epic/keyart.png`. Đã xem ảnh chủ dự án `_refs/owner-epic-2026-10-28.webp` làm mốc hoàn thiện thương mại; ảnh này không được chép nội dung vào chân dung.

| Tên | Lượt giữ / chọn | Prompt đã thay gì và kết quả |
| --- | --- | --- |
| draconis | 1, 2 / **2** | Lượt 1 thêm chiều sâu vảy/giáp nhưng bám bố cục cũ, cánh và thân sát mép. Lượt 2 yêu cầu nhìn xa hơn, cánh gập sau vai, cổ cong, toàn sừng và đáy giáp khép kín trong nền khóa; giải quyết bằng sinh lại, không cắt mất cánh. |
| helper-cham-happy | 1 / **1** | Kính tròn tím nguyên vẹn, khăn/dây chấm kem, cánh đẩy kính; lông có khối, vải dệt và đồng khắc, bỏ đường mực. |
| helper-cham-scared | 1 / **1** | Giữ kính tím nhưng nghiêng, mắt/mỏ hoảng, hai cánh nâng, một giọt mồ hôi chạm trán; giữ dấu nhận diện cùng nhân vật. |
| helper-phay-happy | 1 / **1** | Dây hồng với mũi khâu cong, đuôi cong đầu hồng, mỏ mở đang nói và cánh ra cử chỉ; giữ màu nhận diện, thay vật liệu. |
| helper-phay-scared | 1 / **1** | Giữ dây và đuôi hồng; mắt có lệ, mỏ kêu, hai cánh dang bất đối xứng. |
| helper-gach-happy | 1 / **1** | Mắt lim dim bình thản, dây nâu mũi khâu ngắn, hai cổ tay ba sọc kem; cánh gập. |
| helper-gach-scared | 1, 2 / **2** | Lượt 1 đúng mắt nhắm/cánh áp má nhưng chỉ có hai sọc kem rõ trên mỗi cổ tay. Lượt 2 đính kèm bản sinh mới làm đích sửa, ảnh cũ và hai mẫu phong cách; chỉ yêu cầu mở đủ **ba sọc kem mỗi cổ tay**, giữ phần còn lại. Bản chọn đã thấy đủ ba sọc. |
| narrator | 1 / **1** | Bà Cú Mực giữ kính nửa vầng, khăn chàm viền kem, lọ mực và bút tre; lông bạc/nâu, vải dệt và kính/đồng có chiều sâu. |
| moc-tinh | 1 / **1** | Mộc Tinh giữ mặt gỗ già, râu rễ, tán xanh, quả cam và một vệt mực tím sau vai; dùng nền M để giữ lá xanh, vệt mực là tím lam sâu, không phải magenta. |

Tổng **11 lượt**; không ảnh nào quá hai lượt, không dùng lượt 3. Không sinh tiếp chỉ để ép IoU bằng biến dạng đầu/thân hoặc thay đồ nhận diện. Prompt nguyên văn nằm cạnh đủ 11 `.tryN.png`, chín bản chọn và 27 bản thu. `generation-records.json` lưu đường dẫn công cụ và vai trò ảnh tham chiếu; `delivery-audit.json` xác nhận **11/11 bản thử trùng byte nguồn công cụ**. Tên riêng Draconis, Chấm, Phẩy, Gạch, Bà Cú Mực và Mộc Tinh được giữ; không vẽ tên trong ảnh.

## 3. Hậu kỳ giữ tranh

Nguồn công cụ đều **1254 × 1254**; giữ nguyên nguồn `.try*`. Tách nền bằng bản sao nguyên trạng của `normalize.py` và `seam_analysis.py` trong `_review/167/art-normalize/`; SHA-256 đối chiếu công cụ repo ở `tool-copies.json`. WORK và mọi ảnh trung gian nằm trong phạm vi 167. Đã đặt `ART_MAGICK=/opt/homebrew/bin/magick`.

```sh
python3 -B games/typing-defense/art-src/_review/167/process.py <tên> <lượt> --run <thư-mục-mới>
```

Tách global, `protect-interior`; tám ảnh nền G có `--no-key-hue`, Mộc Tinh nền M không bật tùy chọn này để giữ vệt mực tím. Cắt phần nền trống theo alpha > 16, thu đều bằng Lanczos để cạnh dài 716 px, đặt giữa canvas trong suốt 1024². Không kéo méo, không thay màu hoặc ánh sáng, không phủ hay bỏ phần vẽ. Độ sáng đổi **0%**. Ba bản thu đều đọc trực tiếp master 1024, Lanczos; không làm nét bản 64.

Sau Lanczos, sửa lượng tử alpha ngoài dải mép 3 px: alpha ≥ 128 trả về 255, alpha < 128 trả về 0, chỉ tại pixel lẻ nằm ngoài dải mép của silhouette 50%. **RGB không đổi ở bất kỳ pixel nào** của bước này. Đây là sửa matte rất nhỏ, không phải vẽ lại hay cắt silhouette; hồ sơ ghi đầy đủ tọa độ và alpha trước/sau trong `finished-01/<tên>.tryN/edge-repair.json`. Tổng thay đổi tương đương diện tích alpha trên master từ 0,055 đến 28,518 pixel trên 1.048.576 pixel; Mộc Tinh lớn nhất, **0,00272%** canvas. Tờ aligned cho thấy vẫn giữ tán, râu, mép lông, bút, kính và nét khô của vệt mực. Các bản thu cũng chỉ sửa matte tương tự sau bước thu trực tiếp.

Không san phẳng tranh để đuổi số. Mâu thuẫn IoU được giữ nguyên và ghi ở mục 5.

## 4. KA1, khổ, alpha và tương phản

KA1: trước khi viết prompt/ảnh, `md5 -r` đã băm **69 file có sẵn** trong `portraits/`, lưu `md5-before.txt`; `_review/167*` và báo cáo khi đó chưa tồn tại. Bộ mới thêm **94 file** trong portraits: 11 PNG thử + 11 prompt thử + 36 PNG chọn/thu + 36 prompt. `delivery-audit.json` xác nhận **69/69 file cũ nguyên vẹn**, không sửa hoặc xóa file cũ. `md5-after.txt` băm toàn portraits, `_review/167*` và báo cáo; `md5.diff.txt` chỉ có dòng thêm. Chỉ loại ba hồ sơ hậu kiểm tự tham chiếu (`md5-after.txt`, `md5.diff.txt`, `md5-summary.json`), không loại ảnh hay script.

Đã chạy đúng `magick identify -format '%f %wx%h %[channels]\n'` trên **36 file giao**; log ở `identify-delivery.txt`: 9 bản 1024², 9 bản 256², 9 bản 128², 9 bản 64², tất cả **srgba**. ImageMagick 7.1.2-34 còn in hậu tố `4.0` sau tên kênh. Kiểm đầu dùng `endswith('srgba')` nên báo false giả; đã sửa bộ đọc và kiểm lại trực tiếp file giao, `delivery-audit.json` và `delivery-recheck-01/metrics.json` đều xác nhận khổ/kênh đạt. Không đổi ảnh để chữa lỗi bộ đọc.

Alpha: lấy silhouette alpha ≥ 128, dải mép là Dilate trừ Erode, kernel Square bán kính 3 px. Đếm pixel 0 < alpha < 255 ngoài dải đó. Sắc khóa: hue cách G 120° hoặc M 300° tối đa 15°, S > 0,5; mẫu số là mọi pixel alpha > 0, không dùng toàn canvas để làm nhỏ tỷ lệ. Cả **36/36 ảnh có 0 pixel alpha mềm ngoài dải**, alpha min/max **0/255**, và sắc khóa ≤ 0,2%.

Màu nền không dùng màu tạm khi đã có panel: lấy từ `ui/frames-epic/panel-large.v2.png` của 115/160. Trung vị RGB vùng giữa x/y 35–65%, alpha ≥ 250 cho **ngọc #061e15**; mẫu đá vôi ở 20% mép ngoài, HSV S < 0,3, V > 0,6, alpha ≥ 250 cho **#c1b29c**. Hai mẫu có lần lượt 122.130 và 163.409 pixel. Đây là màu dùng trên các tờ xem.

Luma là Rec.709 trên kênh sRGB chuẩn hóa, Y′ = 0,2126 R + 0,7152 G + 0,0722 B; trung bình vật có trọng số alpha. Ngưỡng phiếu nói **luma**, không phải độ chói tuyến tính; JSON lưu thêm linear luminance để phân biệt rõ hai phép đo. Bảng dưới ghi delta Y′ trên hai màu thực tế.

| Ảnh | Bbox master (px) | Cạnh dài | Lệch tâm lớn nhất | Alpha mềm ngoài mép, cả 4 cỡ | Sắc khóa master | Sắc khóa lớn nhất 4 cỡ | ΔY′ ngọc / đá |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| draconis | 630 × 716 | 69.922% | 0.000% | 0 | 0.08619% | 0.15480% | 0.4701 / 0.1392 |
| helper-cham-happy | 704 × 716 | 69.922% | 0.000% | 0 | 0.02118% | 0.02118% | 0.3667 / 0.2425 |
| helper-cham-scared | 716 × 681 | 69.922% | 0.049% | 0 | 0.04715% | 0.05614% | 0.3751 / 0.2341 |
| helper-phay-happy | 716 × 715 | 69.922% | 0.049% | 0 | 0.03884% | 0.03884% | 0.4140 / 0.1952 |
| helper-phay-scared | 716 × 684 | 69.922% | 0.000% | 0 | 0.05954% | 0.09983% | 0.3991 / 0.2101 |
| helper-gach-happy | 648 × 716 | 69.922% | 0.000% | 0 | 0.03780% | 0.06711% | 0.4210 / 0.1882 |
| helper-gach-scared | 668 × 716 | 69.922% | 0.000% | 0 | 0.06056% | 0.08884% | 0.4038 / 0.2054 |
| narrator | 695 × 716 | 69.922% | 0.049% | 0 | 0.07010% | 0.07010% | 0.3519 / 0.2574 |
| moc-tinh | 716 × 681 | 69.922% | 0.049% | 0 | 0.06148% | 0.06464% | 0.3456 / 0.2636 |

Lề đều đạt 68–72%, lệch tâm ≤ 2%. Delta trên nền ngọc đều ≥ 0,25. Tám ảnh G, riêng Mộc Tinh M. Tỷ lệ sắc khóa theo từng khổ 1024 / 256 / 128 / 64:

| Ảnh | 1024 | 256 | 128 | 64 |
| --- | ---: | ---: | ---: | ---: |
| draconis | 0.08619% | 0.08354% | 0.06345% | 0.15480% |
| helper-cham-happy | 0.02118% | 0.01651% | 0.00000% | 0.00000% |
| helper-cham-scared | 0.04715% | 0.05614% | 0.01658% | 0.00000% |
| helper-phay-happy | 0.03884% | 0.03386% | 0.01623% | 0.00000% |
| helper-phay-scared | 0.05954% | 0.09983% | 0.06629% | 0.00000% |
| helper-gach-happy | 0.03780% | 0.02633% | 0.06711% | 0.00000% |
| helper-gach-scared | 0.06056% | 0.08884% | 0.06498% | 0.06010% |
| narrator | 0.07010% | 0.03790% | 0.06441% | 0.00000% |
| moc-tinh | 0.06148% | 0.06464% | 0.04658% | 0.05757% |

`delivery-recheck-01/metrics.json` có số pixel, mẫu số, bbox, luma và alpha riêng từng file, không chỉ kết luận đạt.

## 5. Cỡ trong game và mâu thuẫn IoU

Cỡ lấy từ UI_IMAGERY: thanh đội 54/65 px, Bà Cú Mực 40/48 px, boss Mộc Tinh 48/58 px và lời boss 24/29 px. Bảng native ghi delta với nền ngọc thực tế; JSON cũng giữ phép đo phụ trên màu tạm #1f3b33 để truy vết.

| Ảnh | 720p / 1080p | ΔY′ ngọc ở 720p / 1080p | IoU lớn nhất, alpha > 16 | Cặp lớn nhất | IoU cùng cặp, alpha ≥ 128 |
| --- | --- | --- | ---: | --- | ---: |
| draconis | 54 / 65 | 0.4698 / 0.4700 | 0.76410 | helper-phay-scared | 0.72571 |
| helper-cham-happy | 54 / 65 | 0.3664 / 0.3665 | 0.88443 | helper-phay-happy | 0.85827 |
| helper-cham-scared | 54 / 65 | 0.3751 / 0.3752 | 0.89901 | helper-phay-scared | 0.89503 |
| helper-phay-happy | 54 / 65 | 0.4137 / 0.4140 | 0.88443 | helper-cham-happy | 0.85827 |
| helper-phay-scared | 54 / 65 | 0.3990 / 0.3991 | 0.89901 | helper-cham-scared | 0.89503 |
| helper-gach-happy | 54 / 65 | 0.4211 / 0.4211 | 0.90686 | helper-gach-scared | 0.90055 |
| helper-gach-scared | 54 / 65 | 0.4037 / 0.4038 | 0.90686 | helper-gach-happy | 0.90055 |
| narrator | 40 / 48 | 0.3516 / 0.3515 | 0.81352 | helper-gach-happy | 0.81675 |
| moc-tinh | 48 / 58 | 0.3458 / 0.3459 | 0.89260 | helper-cham-scared | 0.86162 |

**IoU chưa đạt: 24/36 cặp vượt 0,80**, lớn nhất Gạch vui–hoảng **0,90686**. Draconis có IoU lớn nhất 0,76410, đạt. Đo ở 32 px từ master bằng Lanczos, alpha > 16; còn ghi alpha ≥ 128 để tránh kết luận chỉ dựa vào một ngưỡng thuận lợi. Không có cặp sáng/tắt trong phiếu này; vui/hoảng vẫn được kiểm như hai ảnh khác nhau, không tự áp ngoại lệ ≥ 0,95.

Mâu thuẫn cần Claude quyết theo **ART_ACCEPTANCE §5**: phiếu đòi giữ nhận diện, trang bị và tỷ lệ của sáu Thư Đồng, trong khi mặt nạ alpha ở cỡ nhỏ bỏ hết tín hiệu kính tím, khăn chấm, dây hồng, đuôi cong, sọc cổ tay, mắt và mỏ. Ngay Mộc Tinh và cú cũng có thể IoU cao vì đều là bust gần vuông. Đây là đánh giá của người làm, **không phải tuyên bố rằng không thể thiết kế lại tư thế**. Không kéo hẹp đầu, xóa cánh, thêm lỗ hoặc thay đồ để ép số, không hạ ngưỡng kiểm. Đề nghị Claude xem tờ cũ–mới và native, quyết ngoại lệ cho bộ chân dung; nếu vẫn giữ chốt silhouette thì cần định hướng lại bố cục trước lượt tiếp. Không tự coi ngoại lệ đã được nhận.

Nhìn ở cỡ thật: Chấm phân biệt bằng kính/khăn tím, Phẩy bằng dây hồng và đuôi cong, Gạch bằng cổ tay sọc; bản hoảng đổi mắt/mỏ và cánh. Đó là lượt tự xem đã biết brief, không phải thử mù. Bà Cú Mực vẫn có kính thấp và khăn chàm ở 40 px nhưng mất phần họa tiết nhỏ. Mộc Tinh rõ tán/râu/mặt gỗ ở 48 px; **24 px là cỡ yếu nhất**, còn nhận ra nhân vật cây nhưng khó đọc biểu cảm/mắt. Cần Claude xem riêng cỡ 24 px khi gắn; không làm nét hay xóa tán để tăng mặt bằng hậu kỳ.

## 6. KA5 tự chấm trên bản hậu kỳ

Thứ tự Q: Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp. **Dùng tiếp chỉ 1/2 cho cả bộ**, do chốt IoU toàn phiếu chưa được giải quyết. M là mức hoàn thiện so với HUD thương mại chủ dự án, tách với tổng Q. Các giá trị này là tự chấm, không thay Claude.

| Ảnh | M gốc / 720p | Q gốc | Q 720p | Điểm còn thiếu |
| --- | --- | --- | --- | --- |
| draconis | 8,5 / 8,5 | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | Vảy nhỏ gom lại; dáng sừng/cánh và giáp vẫn rõ. |
| helper-cham-happy | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | Hoa văn đồng nhỏ biến mất, kính/khăn tím giữ nhận diện. |
| helper-cham-scared | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | Giọt mồ hôi nhỏ; hoảng dựa chủ yếu vào mắt, mỏ và cánh. |
| helper-phay-happy | 8 / 8 | 2/2/2/2/1 = **9** | 2/1,5/2/2/1 = **8,5** | Mỏ mở đang nói dễ lẫn hoảng nếu xem riêng mặt; tư thế và đuôi giúp đọc. |
| helper-phay-scared | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | Nước mắt thành chấm sáng nhỏ; cánh và mỏ vẫn rõ. |
| helper-gach-happy | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | Cổ tay sọc rõ hơn từng mũi khâu; mắt bình thản còn đọc. |
| helper-gach-scared | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | Đủ ba sọc, nhưng silhouette gần bản vui nhất bộ. |
| narrator | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/1,5/2/2/1 = **8,5** | 40 px mất họa tiết khăn và lọ; kính thấp/khăn chàm còn nhận ra. |
| moc-tinh | 8,5 / 8 | 2/2/2/2/1 = **9** | 2/1,5/2/2/1 = **8,5** | 48 px mặt nhỏ trong tán; cỡ lời boss 24 px cần xem riêng. |

Riêng Mộc Tinh ở 24 px: Q **8 = 2/1/2/2/1**, biểu cảm không đọc đủ; không dùng điểm gốc thay cho điểm cỡ nhỏ. Không sửa `ART_REPLACE_LATER.md` vì phiếu chỉ cho ghi báo cáo này.

## 7. Chạy lại và các khác biệt còn mở

Script đã dùng nằm trong `_review/167/`: `process.py`, hai bản sao art-normalize, `refine.py`, `measure.py`, `measure-final.py`, `sheets.py`, `publish.py`, `audit.py`, `md5-audit.py`, `write-report.py`. Writer đều từ chối ghi đè. Hồ sơ ứng viên đầu và lỗi kiểm đầu được giữ, không thay bằng kết quả đẹp hơn.

Kiểm lại chính 36 file giao vào thư mục mới, không sinh ảnh, không mở game:

```sh
python3 -B games/typing-defense/art-src/_review/167/recheck.py recheck-owner-02
```

Lệnh tạo hard link chỉ để đọc trong thư mục mới, đo lại ảnh giao và ghi `metrics.json`/`delivery-source.json`; không sửa inode ảnh. Dựng lại ứng viên vào tên mới: `process.py` hỗ trợ `--run`; `refine.py` nhận thư mục đích mới. Các script xuất bản chọn/báo cáo là thao tác một lần, chạy lại trên tên đã có sẽ dừng an toàn. Tờ từng ảnh đã có đủ; không chạy `sheets.py` đè các tờ này.

Khác phiếu và phần chưa nhận:

1. `frames/` trong phiếu đã cũ; dùng bản 115 đã nhận ở `frames-epic/`, không chờ nhầm.
2. Nguồn công cụ 1254² được giữ nguyên; bản giao chuẩn hóa 1024² đúng quy cách.
3. Sau thu Lanczos trực tiếp có sửa lượng tử alpha nhỏ, không sửa RGB hoặc làm nét; toàn bộ thay đổi được ghi và có tờ so.
4. **Không có đủ bốn icon độc lập đã được Claude nhận trong hồ sơ Wordwoven đã đọc.** Hàng 4 dùng đúng bốn trang trí 115 đã nhận (portrait-ring, crest, banner, divider); tờ context bổ sung bốn icon 134 đang chờ Claude. Không tự nâng trạng thái của chúng.
5. Không bỏ ảnh nào, không bỏ lượt sinh nào. **Không ép IoU bằng phá tranh; 24 cặp trượt được giữ nguyên. Vì vậy chưa đạt điều kiện “mọi kiểm 1–5”, chưa đóng phiếu.** Claude cần chấm lại ≥ 8, quyết ngoại lệ IoU và xem Mộc Tinh 24 px; Claude là người chép ảnh vào public khi nhận.

