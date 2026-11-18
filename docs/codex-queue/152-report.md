# Phiếu 152 · Last Line · Đủ 11 ảnh, chờ chấm nhận và chốt cách đo mép

## Lượt tiếp tục 31/10/2026

**Đã sinh thành công bốn ảnh còn thiếu và một lượt sửa `pace-director`, giữ mọi ảnh, prompt và hậu kỳ cũ. Bộ chọn đủ 11 ảnh × bốn khổ = 44 PNG, có đủ prompt, tờ sinh/hậu kỳ, số đo và KA5 ở khổ gốc lẫn cỡ 720p. Không gặp HTTP 429 trong lượt này. Chưa tuyên bố Claude nhận hoặc chép vào `public/`.**

**Điểm phải xem trước khi đóng phiếu:** phép đo đường bao alpha 50%, dải Euclid 3 px cho 0 pixel alpha lẻ ngoài mép ở cả 11 bản chọn. Giữ thêm cách đo cũ (alpha >16, Diamond:3): `pace-director.v2` còn 2 pixel, `stat-new-word` còn 2, `rift` còn 17. Không giấu kết quả cũ và không cắt các pixel này để ép số. Vì hai cách định nghĩa mép khác nhau, ba ảnh này chỉ nhận 1 điểm “Dùng tiếp”, chờ Claude chốt; nếu bắt buộc giữ nguyên định nghĩa cũ thì **ba ảnh chưa qua chốt alpha**, phiếu chưa đóng. Cả ba vẫn tự chấm tổng từ 8 ở cỡ 720p. Đây là vấn đề đo mép, không phải công cụ hết hạn mức.

## 1. Bản chọn và những file giữ lại

Các đường dẫn dưới là master hậu kỳ 1024²; cạnh mỗi master có `.256.png`, `.128.png`, `.64.png` và `.prompt.txt`. Sáu bản cũ được chọn lại giữ nguyên từng byte. Hai bản có hậu tố `.v2` là tên giao được đề xuất, vì luật phiếu cấm ghi đè tên đã có. `pace-director.png` cũ vẫn là bản chưa đạt của lượt 30/10; `stat-wpm.png` là bản hậu kỳ đầu của lượt này, tương phản thấp hơn ngưỡng. Không dùng hai bản ấy thay cho bản chọn trong bảng.

| Nội dung | Master chọn | Lượt sinh | Tờ bản sinh / hậu kỳ |
| --- | --- | ---: | --- |
| sfx | [sfx](../../games/typing-survival/art-src/ui/icons/sfx.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/sfx-before-after.jpg) |
| music | [music](../../games/typing-survival/art-src/ui/icons/music.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/music-before-after.jpg) |
| shake | [shake](../../games/typing-survival/art-src/ui/icons/shake.png) | 2 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/shake-before-after.jpg) |
| reduced-motion | [reduced-motion](../../games/typing-survival/art-src/ui/icons/reduced-motion.png) | 2 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/reduced-motion-before-after.jpg) |
| read-aloud | [read-aloud](../../games/typing-survival/art-src/ui/icons/read-aloud.png) | 2 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/read-aloud-before-after.jpg) |
| pace-director | [pace-director.v2](../../games/typing-survival/art-src/ui/icons/pace-director.v2.png) | 2 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/pace-director.v2-resume3-before-after.jpg) |
| quality | [quality](../../games/typing-survival/art-src/ui/icons/quality.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/quality-before-after.jpg) |
| stat-wpm | [stat-wpm.v2](../../games/typing-survival/art-src/ui/icons/stat-wpm.v2.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/stat-wpm.v2-resume3-before-after.jpg) |
| stat-new-word | [stat-new-word](../../games/typing-survival/art-src/ui/icons/stat-new-word.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/stat-new-word-resume3-before-after.jpg) |
| stat-evenness | [stat-evenness](../../games/typing-survival/art-src/ui/icons/stat-evenness.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/stat-evenness-resume3-before-after.jpg) |
| rift | [rift](../../games/typing-survival/art-src/ui/icons/rift.png) | 1 | [Đối chiếu](../../games/typing-survival/art-src/_review/152/rift-resume3-before-after.jpg) |

Lượt này thêm năm bản sinh nguyên trạng: `stat-wpm.try1.png` (1536 × 1024), `stat-new-word.try1.png` (1254²), `stat-evenness.try1.png` (2172 × 724), `rift.try1.png` (1254²), `pace-director.try2.png` (1254²). Giữ khổ nguồn mà công cụ trả, không giả gọi nguồn đã đổi cỡ là bản sinh. Không có ảnh nào vượt ba lượt sinh. Bốn prompt try1 đã có từ lượt trước được dùng lại, không ghi đè sidecar; thêm prompt try2 của Pace. Mỗi bản chọn có prompt khớp từng byte với sidecar của lượt chọn.

## 2. Prompt, tham chiếu và hậu kỳ

Dùng kỹ năng `imagegen` và công cụ tích hợp `image_gen.imagegen`, từng ảnh một, `transparent_background: true`; không dùng CLI/API khác. Đã xem `gun-xung.norm.256.png`, `screens-epic/menu-bg.png` của 121, `frames-epic/button.alpha.png` của 127, HUD ảnh mẫu thương mại của chủ dự án và tờ 152 cũ trước khi sinh. Các ảnh 121/127 là tham chiếu đã có, không tự nhận chúng đã nghiệm thu. STYLE-UI là nguyên văn AD §4.3; KIND giữ khối icon raster hiện có của phiếu. Không quay về phong cách công nghiệp cũ của 015.

| Ảnh / lượt | Prompt dùng và chỗ sửa |
| --- | --- |
| stat-wpm · try1 | Giữ prompt có sẵn: mặt số bán nguyệt, ba vạch lớn, kim lam hướng cao sang phải, viền trắng vàng. Nguồn có alpha thật. Không sinh thêm; sửa thiếu tương phản bằng sáng toàn ảnh +5% theo giới hạn ±10%. |
| stat-new-word · try1 | Giữ prompt chip hình thoi, chân kết nối, lõi dữ liệu lam và chớp cam ở đỉnh; nền alpha. Không sửa prompt. |
| stat-evenness · try1 | Giữ prompt thước thủy nằm ngang, ống lam, một bọt giữa hai vạch định vị. Công cụ trả ảnh ngang; đặt lại vào canvas vuông bằng đổi cỡ giữ tỷ lệ và thêm lề, không bóp hình. |
| rift · try1 | Giữ prompt vết xé tím dọc, rìa kính răng cưa, khe sáng tím nhạt và trắng, vật liệu đặc, nền alpha. Không đổi màu tím để tránh bộ dò magenta. |
| pace-director · try1 → try2 | Giữ STYLE-UI và KIND, thay mặt trăng lưỡi liềm bằng mặt số móng ngựa hở một phần tư phía dưới; ba dấu lam lớn, kim lam cong có đầu mũi tên, chốt cam nhỏ và khoảng hở rộng giữa kim với vành. Nhấn ánh sáng nằm trong vật liệu đặc, contour gọn. Không dùng try1 làm ảnh để sửa bằng mã. |
| sfx, music, shake, reduced-motion, read-aloud, quality | Giữ nguyên bản chọn và lịch sử prompt của báo cáo 30/10 bên dưới; không sinh hoặc hậu kỳ lại. |

Năm nguồn mới đều có alpha thật; không dùng nền khóa cho chúng. Hậu kỳ bằng ImageMagick 7 trực tiếp, không sửa `tools/art-normalize`. Thu toàn ảnh nguồn theo tỷ lệ để bbox alpha >16 có cạnh dài khoảng 717 px, rồi đặt tâm trên canvas 1024². Alpha được đưa từ khoảng 8…247 về 0…255 để dọn lớp nền và mặt gần đục; sau khi đặt lề, snap alpha 239…254 thành 255. Không co mask, bỏ thành phần, san phẳng, vẽ đè hoặc thay RGB. Các số pixel snap là 649 (WPM), 1.210 (chip), 365 (thước), 1.603 (Rift), 1.703 (Pace). Giữ các bản trung gian để so lại. WPM v2 chỉ thêm phép nhân RGB 1,05 toàn ảnh, clipping theo dải sRGB; alpha khớp từng pixel với WPM đầu. Các bản thu đều Lanczos trực tiếp từ đúng master, không làm nét cỡ 64.

Hồ sơ thao tác: [chuẩn bị](../../games/typing-survival/art-src/_review/152/resume3-prepare-log.json), [giao ảnh](../../games/typing-survival/art-src/_review/152/resume3-delivery-log.json), [sửa sáng WPM](../../games/typing-survival/art-src/_review/152/resume3-wpm-brighten.json). So tờ sinh/hậu kỳ không thấy mất phần vẽ; thay đổi kích thước vật trong ô là bước đặt lề bắt buộc, không phải xóa chi tiết.

## 3. Khổ, alpha, lề và sắc khóa

[Identify đủ 44 PNG](../../games/typing-survival/art-src/_review/152/resume3-identify-final.txt): mỗi ảnh đủ 1024², 256², 128², 64²; tất cả `srgba`, sRGB. [Kiểm artifact](../../games/typing-survival/art-src/_review/152/resume3-artifact-check.json) xác nhận 33 bản thu khớp pixel với Lanczos trực tiếp, 11 prompt khớp lượt chọn và alpha WPM không đổi khi tăng sáng.

Định nghĩa mới tách hai việc: **bbox/lề** vẫn dùng alpha >16 như phiếu; **contour hình học** dùng alpha 128, dải 3 px Euclid (`Edge Disk:3`). Cách cũ của báo cáo 30/10 lấy chính mask alpha >16 để dựng dải Manhattan (`Edge Diamond:3`); hai cách không tương đương ở mép mềm và đường xiên. Bảng giữ cả hai số, không dùng 0 của cách mới để nói số cũ đã biến mất. Quy tắc 50% contour là lựa chọn đo của lượt này, **không phải thay đổi đã được chủ dự án phê chuẩn**.

| Ảnh | Cạnh dài bbox % | Lệch tâm lớn nhất % | Alpha lẻ ngoài 3 px · contour 128/Disk | Chẩn đoán cũ · 16/Diamond | Sắc magenta thô, px | % trên alpha >0 | % nhiễm khóa thực |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| sfx | 70.117 | 0.049 | 0 | 0 | 37 | 0.019312 | 0.000000 |
| music | 70.020 | 0.049 | 0 | 0 | 31 | 0.012546 | 0.000000 |
| shake | 70.117 | 0.049 | 0 | 0 | 9 | 0.008455 | 0.008455 |
| reduced-motion | 70.117 | 0.000 | 0 | 0 | 9 | 0.008130 | 0.008130 |
| read-aloud | 70.020 | 0.049 | 0 | 0 | 70 | 0.032031 | 0.032031 |
| pace-director.v2 | 70.020 | 0.049 | 0 | 2 | 23 | 0.009925 | 0.000000 |
| quality | 70.020 | 0.049 | 0 | 0 | 19 | 0.007735 | 0.000000 |
| stat-wpm.v2 | 70.020 | 0.049 | 0 | 0 | 5 | 0.002255 | 0.000000 |
| stat-new-word | 70.020 | 0.049 | 0 | 2 | 41 | 0.015552 | 0.000000 |
| stat-evenness | 70.020 | 0.049 | 0 | 0 | 6 | 0.008868 | 0.000000 |
| rift | 69.922 | 0.000 | 0 | 17 | 1740 | 1.916152 | 0.000000 |

Sắc magenta thô: H = 285…315°, S >0,5, alpha >0; JSON còn giữ tỷ lệ theo toàn canvas. Nhiễm khóa thực chỉ áp dụng cho `shake`, `reduced-motion`, `read-aloud`, vì đó là ba nguồn sinh trên M, rồi được tách nền ở lượt trước. Các nguồn khác là alpha thật, không có màu khóa để sót. Đặc biệt **Rift có 1,9162% pixel alpha >0 mang hue gần magenta, đó là kính tím được yêu cầu**, không phải nền khóa. Nếu bộ kiểm mặc định coi mọi sắc magenta là nhiễm khóa dù nguồn alpha thật, Rift không qua bộ kiểm ấy; không được khử tím để ép số. Chờ Claude xác nhận cách áp dụng. Không phát biểu “mọi ảnh dưới 0,2% magenta” vì điều đó sai với Rift.

## 4. IoU và tương phản ở đúng cỡ

Đã đo đủ 55 cặp, thu toàn canvas về 32² bằng Lanczos, alpha ≥128; giữ thêm kết quả alpha >16 trong JSON. Không có cặp sáng/tắt trong phiếu. Shake và Reduced Motion là hai chức năng khác nhau, không áp ngưỡng ≥0,95 dành cho trạng thái bật/tắt.

| Ảnh | IoU lớn nhất · alpha ≥128 | Cặp gần nhất | IoU lớn nhất · alpha >16 |
| --- | ---: | --- | ---: |
| sfx | 0.5429 | stat-new-word | 0.5890 |
| music | 0.7163 | stat-new-word | 0.7385 |
| shake | 0.2659 | pace-director.v2 | 0.5333 |
| reduced-motion | 0.2336 | pace-director.v2 | 0.3506 |
| read-aloud | 0.6513 | stat-wpm.v2 | 0.7213 |
| pace-director.v2 | 0.3038 | read-aloud | 0.4252 |
| quality | 0.6020 | music | 0.6377 |
| stat-wpm.v2 | 0.6513 | read-aloud | 0.7213 |
| stat-new-word | 0.7163 | music | 0.7385 |
| stat-evenness | 0.2500 | stat-wpm.v2 | 0.3415 |
| rift | 0.3879 | music | 0.4179 |

Tương phản dùng luma sRGB Y′ = 0,2126R′ + 0,7152G′ + 0,0722B′, trung bình RGB vật theo trọng số alpha sau khi thu đúng cỡ. Đây là chênh luma trung bình của phiếu; không gọi là tỷ lệ WCAG. Giữ luminance tuyến tính như chẩn đoán bổ sung trong JSON, không trộn hai định nghĩa. Bảy icon cài đặt là 20/30 px, bốn icon hồ sơ/Rift là 24/36 px. Cả 11 bản chọn vượt 0,25 trên than chì `#14181f` ở cả hai cỡ; nền thép `#8c96a3` tương phản thấp hơn.

| Ảnh | Cỡ 720p / 1080p | 720p · than chì | 720p · thép | 1080p · than chì | 1080p · thép |
| --- | --- | ---: | ---: | ---: | ---: |
| sfx | 20 / 30 | 0.4257 | 0.0651 | 0.4251 | 0.0657 |
| music | 20 / 30 | 0.3889 | 0.1019 | 0.3881 | 0.1027 |
| shake | 20 / 30 | 0.4019 | 0.0889 | 0.3957 | 0.0951 |
| reduced-motion | 20 / 30 | 0.4205 | 0.0703 | 0.4295 | 0.0613 |
| read-aloud | 20 / 30 | 0.4542 | 0.0366 | 0.4520 | 0.0388 |
| pace-director.v2 | 20 / 30 | 0.4935 | 0.0027 | 0.4911 | 0.0003 |
| quality | 20 / 30 | 0.5024 | 0.0116 | 0.5030 | 0.0122 |
| stat-wpm.v2 | 24 / 36 | 0.2610 | 0.2298 | 0.2576 | 0.2332 |
| stat-new-word | 24 / 36 | 0.4008 | 0.0900 | 0.4003 | 0.0905 |
| stat-evenness | 24 / 36 | 0.4787 | 0.0122 | 0.4845 | 0.0064 |
| rift | 24 / 36 | 0.3014 | 0.1894 | 0.3028 | 0.1880 |

WPM đầu chưa đạt: 0,2467 / 0,2433. Bản v2 tăng sáng 5% cho 0,2610 / 0,2576; không làm sáng riêng kim hoặc viền bằng cách vẽ thêm. [Số đo cuối và toàn bộ cặp IoU](../../games/typing-survival/art-src/_review/152/resume3-measurements-final.json) là số của đúng bộ chọn trong bảng, không dùng số của ứng viên đầu. Trường `numerical_pass` trong JSON dùng định nghĩa contour 128 và nhiễm khóa thực đã công bố; nó không tự giải quyết bất đồng với cách đo cũ.

## 5. KA5 · Chấm bản hậu kỳ so với HUD thương mại

Đã xem năm master mới ở 1024², các tờ sinh/hậu kỳ, bộ 11 ảnh ở cỡ thật và tờ phóng nearest-neighbour để kiểm mất chi tiết. Mức tham chiếu là HUD thương mại của chủ dự án, không lấy bộ của ta làm chuẩn. Điểm thận trọng hơn lượt trước: filigree và vật liệu giàu ở bản lớn nhưng nhiều chi tiết biến mất ở 20–24 px. Thứ tự năm điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Ba ảnh còn bất đồng chốt alpha chỉ được 1 ở Dùng tiếp, dù phép đo contour 128 đạt. Tổng từ 8 không thay cho chốt kỹ thuật và Claude chấm nhận.

| Ảnh | Năm điểm 1024² | Tổng | Năm điểm 720p | Tổng | Thiếu hoặc cần xem |
| --- | --- | ---: | --- | ---: | --- |
| sfx | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | Loa và tia đọc được; trang trí dày hơn icon hệ thống mẫu. |
| music | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | 2 / 1 / 1,5 / 1,5 / 2 | 8.0 | Màng loa rõ; ba đỉnh sóng nhập mảng ở 20 px. |
| shake | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | 2 / 1 / 1,5 / 1,5 / 2 | 8.0 | Khung đọc được, dấu rung nhỏ ở 20 px. |
| reduced-motion | 1,5 / 2 / 1,5 / 1,5 / 2 | 8.5 | 1,5 / 1,5 / 1,5 / 1,5 / 2 | 8.0 | Neo và khung tĩnh có mặt; hình khung chưa trùng hẳn Shake. |
| read-aloud | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | Miệng và cung âm tách rõ; lưới chỉ còn mảng tối. |
| pace-director.v2 | 2 / 2 / 2 / 1,5 / 1 | 8.5 | 2 / 1,5 / 2 / 1,5 / 1 | 8.0 | Đã đọc thành mặt số; đầu kim cong nhỏ ở 20 px. Chờ chốt alpha. |
| quality | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | Ba mảng thấu kính phân biệt, phản xạ vụn giảm khi thu. |
| stat-wpm.v2 | 2 / 2 / 2 / 1,5 / 2 | 9.5 | 2 / 1,5 / 2 / 1,5 / 2 | 9.0 | Kim cao rõ; tương phản đạt nhưng gần ngưỡng nhất bộ. |
| stat-new-word | 2 / 2 / 2 / 1,5 / 1 | 8.5 | 2 / 1,5 / 2 / 1,5 / 1 | 8.0 | Dáng chip và lõi lam rõ; chân kết nối nhỏ. Chờ chốt alpha. |
| stat-evenness | 2 / 2 / 2 / 1,5 / 2 | 9.5 | 2 / 1 / 2 / 1,5 / 2 | 8.5 | Thước nằm ngang riêng dáng; bọt giữa chỉ còn ít pixel ở 24 px. |
| rift | 2 / 2 / 2 / 1,5 / 1 | 8.5 | 2 / 1,5 / 2 / 1,5 / 1 | 8.0 | Vết xé tím sáng, răng cưa rõ; chờ chốt alpha và hue tím hợp lệ. |

Đây là **tự chấm**, chưa có giám khảo độc lập mới. Không tạo yêu cầu ghi `ART_REPLACE_LATER.md` ngoài phạm vi phiếu; các thiếu sót 8–8,5 đã ghi ngay tại đây để Claude xử lý khi nhận.

## 6. Tờ xem, KA1 và cách chạy lại

- [Tờ bốn hàng cuối · 152-sheet-final.jpg](../../games/typing-survival/art-src/_review/152-sheet-final.jpg): 11 bản 256 px; cỡ 1080p trên hai nền; cỡ 720p trên hai nền; bốn icon súng hiện có và mảnh HUD thương mại cùng cao 128 px. Có tên dưới mỗi ảnh.
- [Cỡ thật 1:1](../../games/typing-survival/art-src/_review/152/resume3-native-size-final.png), xem 100%; [phóng pixel ×8](../../games/typing-survival/art-src/_review/152/resume3-native-zoom-final.png) chỉ là phụ trợ, không thay cỡ thật.
- Giữ nguyên `152-sheet.jpg` cũ vì luật cấm ghi đè; tờ cuối dùng tên mới. Giữ cả tờ trung gian của lượt này, bản WPM chưa tăng sáng, Pace try1 và mọi `.try*`.

**KA1 lượt 31/10:** `/sbin/md5 -r` trước khi ghi: **499 file**; sau: **575 file**, **76 đường dẫn thêm, 0 đổi, 0 mất**; diff có **0 dòng nội dung bị xóa**. Giữ manifest cũ, dùng tên nối tiếp: [trước](../../games/typing-survival/art-src/_review/152/md5-resume3-before.txt), [sau](../../games/typing-survival/art-src/_review/152/md5-resume3-after.txt), [diff](../../games/typing-survival/art-src/_review/152/md5-resume3-diff.txt), [tổng hợp](../../games/typing-survival/art-src/_review/152/md5-resume3-summary.json). Snapshot bao toàn `ui/icons`, `_review/152/` và `_review/152-*.jpg`; không tự băm manifest sau, diff, JSON phụ thuộc nó. Báo cáo được phép cập nhật nằm ngoài snapshot media.

Script lưu trong `_review/152/`: `resume3-prepare.py` → `resume3-deliver.py` → `resume3-wpm-brighten.py` → `resume3-measure-final.py` → `resume3-proofs-final.py` → `resume3-verify.py` → `resume3-audit.py` → `resume3-report.py`. Mỗi script media chặn đích đã có. Có thể tái dựng trên bản sao hồ sơ trước lượt này với các nguồn `.try*` đã bổ sung, hoặc đổi sang tên đầu ra mới; **không chạy lại để ghi đè trên hồ sơ hiện tại**. `resume3-measure.py` và `resume3-proofs.py` giữ phép đo/tờ trung gian trước khi sửa tương phản WPM. Chạy bằng Python 3 chuẩn và `/opt/homebrew/bin/magick`, font Arial của macOS; không cần tải gói hay gọi mạng ngoài image_gen.

## 7. Khác phiếu và phần để Claude / chủ dự án xem

1. Hai tên chọn `pace-director.v2` và `stat-wpm.v2`, cùng `152-sheet-final.jpg`, thay cho ghi đè tên đã có. Chủ dự án/Claude dùng đúng tên chọn khi xem hoặc tích hợp; không xóa bản trước.
2. Nguồn công cụ trả khổ khác 1024² dù prompt yêu cầu vuông. Giữ nguồn nguyên trạng và giao master 1024² sau đặt lề, thu tỷ lệ thật; thước không bị kéo thành vật vuông.
3. **Chưa chốt định nghĩa dải mép.** Nếu dùng cách cũ, ba ảnh còn 2/2/17 pixel như bảng. Theo ART_ACCEPTANCE §5, dừng việc ép mask và giữ tranh để Claude quyết. Chưa coi ba ảnh này đã vượt mọi định nghĩa kiểm alpha.
4. **Tím của Rift là phần vẽ**, không phải nền M. Nếu bộ kiểm áp ngưỡng hue magenta chung, ghi nhận xung đột thay vì đổi màu hoặc xóa tranh. Cần Claude xác nhận miễn áp ngưỡng nhiễm khóa cho nguồn alpha thật.
5. Không sinh lại sáu bản cũ đã đủ điểm; không tạo âm thanh vì phiếu chỉ giao ảnh. Không sửa game, tài liệu khác, tool chung, không Git, build/test, dev server, trình duyệt, `public/`, game khác hoặc Tu Tiên. Chỉ đọc ảnh tham chiếu của chủ dự án theo yêu cầu; không ghi vào Wordwoven.

**Việc tạo ảnh đã đủ; phần nhận còn chờ Claude ≥8 và quyết định hai cách đo nêu trên. Không có hạn mức hoặc mốc giờ bắt buộc nào đang chặn lượt này.**

---

## Lịch sử báo cáo giữ nguyên từ 30/10

# Phiếu 152 · Last Line · Bảy bản chọn, chưa hoàn tất

## Lượt chạy lại 30/10 · Dừng vì vẫn HTTP 429

**Giờ ghi nhận ngay sau lỗi: 13:07:04 ngày 30/10/2026, UTC+7** (06:07:04 UTC, đồng hồ công cụ và macOS khớp nhau). Đã đọc báo cáo, kiểm kê hồ sơ và xem lại ảnh tham chiếu trước khi gọi công cụ. Gửi **nguyên văn** `stat-wpm.try1.prompt.txt` đang có tới công cụ tích hợp `image_gen.imagegen`, với `transparent_background: true`. Công cụ trả **HTTP 429 Too Many Requests · `usage_limit_reached` · gói `plus`**, không có ảnh đầu ra. Theo chỉ dẫn “Nếu vẫn 429 thì dừng, ghi giờ”, dừng ngay; không gọi tiếp các ảnh khác, không dùng CLI/API thay thế, không hậu kỳ thêm trong lượt này.

Dịch vụ trả `resets_at: 1793364445` và `resets_in_seconds: 24031`, tương ứng mốc **19:47:25 ngày 30/10/2026, UTC+7**. Đây chỉ là mốc dịch vụ báo, chưa xác minh hạn mức thực tế sẽ mở lại. Lỗi đầy đủ đã tóm lược tại [generation-block-resume2.json](../../games/typing-survival/art-src/_review/152/generation-block-resume2.json).

**Kết quả lượt này: 0 ảnh mới; giữ nguyên mọi bản sinh, bản hậu kỳ, prompt và tờ xem cũ.** Vẫn thiếu `stat-wpm`, `stat-new-word`, `stat-evenness`, `rift`; `pace-director` vẫn chưa đạt như phần báo cáo trước bên dưới. Không tăng số lượt sinh thành công, không sửa prompt. Các số đo và điểm cũ được giữ nguyên, không coi là đo lại trong lượt này. Phiếu vẫn chưa hoàn tất, chưa được Claude chấm nhận.

KA1 cho lượt chạy lại: gọi `/sbin/md5 -r` trước khi ghi, snapshot **265 file**; snapshot sau **268 file**, **3 đường dẫn thêm, 0 đổi, 0 mất**, diff có **0 dòng nội dung bị xóa**. Ba đường dẫn thêm là manifest trước, script kiểm và hồ sơ lỗi. Giữ nguyên cả `md5-before.txt` và `md5-after.txt` cũ; dùng tên mới để không ghi đè. Hồ sơ: [trước](../../games/typing-survival/art-src/_review/152/md5-resume2-before.txt), [sau](../../games/typing-survival/art-src/_review/152/md5-resume2-after.txt), [diff](../../games/typing-survival/art-src/_review/152/md5-resume2-diff.txt), [tổng hợp](../../games/typing-survival/art-src/_review/152/md5-resume2-summary.json). Snapshot sau không tự băm chính nó, diff và JSON sinh từ nó; báo cáo được phép cập nhật nằm ngoài snapshot media.

Script [audit-resume2.py](../../games/typing-survival/art-src/_review/152/audit-resume2.py) lưu cách ghi lỗi và kiểm hash; chỉ tạo file mới, chặn ghi đè. Lệnh: `PYTHONDONTWRITEBYTECODE=1 python3 games/typing-survival/art-src/_review/152/audit-resume2.py`; muốn tái dựng phải dùng bản sao đầu vào chưa có các đầu ra của lượt này. Không chạy lại trên hồ sơ hiện tại. Chủ dự án/điều phối cần cho chạy tiếp khi công cụ thực sự có hạn mức; không có ảnh mới để duyệt trong lượt này.

---

Ngày 30/10/2026, Codex. **Đã hậu kỳ bảy icon từ các bản sinh có sẵn, xuất 28 PNG và bảy prompt bản chọn. Sáu icon qua các chốt số đo trong báo cáo; `pace-director` chưa qua alpha và có KA5 ở 720p dưới 8. Còn thiếu bốn icon vì công cụ tạo ảnh hết hạn mức. Chưa đủ điều kiện đóng phiếu, chưa được Claude chấm nhận.**

Khi tiếp tục công việc, thư mục đã có mười ảnh thử cho bảy icon, đủ prompt cạnh ảnh, bốn prompt cho ảnh chưa sinh và manifest `md5-before.txt`. Giữ nguyên toàn bộ các file đó; lượt này không sinh thành công ảnh mới. Các bản chọn của 121 và khung 127 đã có để tham chiếu, dù hai báo cáo đó vẫn ghi chưa nghiệm thu. Đã xem `gun-xung.norm.256.png`, bản chọn `menu-bg.png` của 121, `button.alpha.png` của 127 và ảnh thương mại của chủ dự án trước khi hậu kỳ.

## 1. Ảnh giao và phần còn thiếu

Thư mục ảnh: [`games/typing-survival/art-src/ui/icons/`](../../games/typing-survival/art-src/ui/icons/). Mỗi tên có `.png` 1024 × 1024, `.256.png`, `.128.png`, `.64.png` và `.prompt.txt`. Prompt bản chọn khớp từng byte với prompt của đúng lượt thử. Không ghi đè ảnh cũ; không đụng `public/`.

| Tên | Lượt chọn / ảnh thử có sẵn | Kết quả | Bản sinh và bản hậu kỳ |
| --- | --- | --- | --- |
| [sfx](../../games/typing-survival/art-src/ui/icons/sfx.png) | 1 / 1 | Qua số đo, chờ Claude chấm | [Đối chiếu](../../games/typing-survival/art-src/_review/152/sfx-before-after.jpg) |
| [music](../../games/typing-survival/art-src/ui/icons/music.png) | 1 / 1 | Qua số đo, chờ Claude chấm | [Đối chiếu](../../games/typing-survival/art-src/_review/152/music-before-after.jpg) |
| [shake](../../games/typing-survival/art-src/ui/icons/shake.png) | 2 / 2 | Qua số đo, chờ Claude chấm | [Đối chiếu](../../games/typing-survival/art-src/_review/152/shake-before-after.jpg) |
| [reduced-motion](../../games/typing-survival/art-src/ui/icons/reduced-motion.png) | 2 / 2 | Qua số đo; dáng khung cần xem thêm | [Đối chiếu](../../games/typing-survival/art-src/_review/152/reduced-motion-before-after.jpg) |
| [read-aloud](../../games/typing-survival/art-src/ui/icons/read-aloud.png) | 2 / 2 | Qua số đo, chờ Claude chấm | [Đối chiếu](../../games/typing-survival/art-src/_review/152/read-aloud-before-after.jpg) |
| [pace-director](../../games/typing-survival/art-src/ui/icons/pace-director.png) | 1 / 1 | **Chưa đạt alpha và KA5 ở 720p; chưa dùng** | [Đối chiếu](../../games/typing-survival/art-src/_review/152/pace-director-before-after.jpg) |
| [quality](../../games/typing-survival/art-src/ui/icons/quality.png) | 1 / 1 | Qua số đo, chờ Claude chấm | [Đối chiếu](../../games/typing-survival/art-src/_review/152/quality-before-after.jpg) |
| `stat-wpm` | 0 ảnh; đã có prompt try1 | **Chưa sinh** | — |
| `stat-new-word` | 0 ảnh; đã có prompt try1 | **Chưa sinh** | — |
| `stat-evenness` | 0 ảnh; đã có prompt try1 | **Chưa sinh** | — |
| `rift` | 0 ảnh; đã có prompt try1 | **Chưa sinh** | — |

Lệnh `image_gen.imagegen` cho `stat-wpm.try1`, dùng nguyên prompt có sẵn và `transparent_background: true`, trả **HTTP 429, `usage_limit_reached`, gói `plus`**, không có ảnh đầu ra. Công cụ báo mốc mở lại `1793364445`, tương ứng **19:47:25 ngày 30/10/2026, UTC+7**; đây là mốc do công cụ trả, chưa xác minh việc hạn mức thực tế mở lại. Giữ lỗi tại [generation-block.json](../../games/typing-survival/art-src/_review/152/generation-block.json). Không gọi dồn ba ảnh còn lại sau cùng lỗi hạn mức, không chuyển sang CLI/API hoặc dịch vụ khác.

## 2. Prompt và các lượt

Dùng skill `imagegen`; yêu cầu sinh mới duy nhất trong lượt tiếp tục là công cụ tích hợp nêu trên. Không có ảnh nào vượt ba lượt. Khối STYLE-UI trong mọi prompt đã có là nguyên văn §4.3 của AD: kính khói, than chì, chỉ vàng trắng, lam điện và cam vàng. Khối KIND yêu cầu icon raster một vật, mặt vật liệu sáng, hình khối rộng, đọc được ở 20 px và lề 15%. Không dùng lại khối phong cách công nghiệp cũ của 015.

Bảng này đối chiếu các sidecar đang có; không suy diễn thêm lịch sử gọi công cụ của lượt trước.

| Ảnh | Nội dung prompt và thay đổi giữa các lượt có sẵn |
| --- | --- |
| sfx · try1 | Loa hình kèn trắng vàng, lưới than chì bên trái, tia lam bốn cánh bên phải; nền trong suốt. Giữ prompt, không có lượt sửa. |
| music · try1 | Thùng loa cao, màng loa tròn tối, dải sóng lam ba đỉnh ở nửa trên; nền trong suốt. Giữ prompt. |
| shake · try1 → try2 | Try1 được trả khổ ngang 1536 × 1024. Try2 nhấn mạnh khổ vuông 1:1, nền magenta phẳng cả lòng màn hình, chỉ vẽ viền thiết bị và bốn dấu rung; chọn try2 1254². |
| reduced-motion · try1 → try2 | Try1 cũng là ảnh ngang. Try2 khóa khổ vuông, lòng khung và khoảng trống neo là magenta, neo nhỏ treo dưới khung; chỉ dẫn dùng vật liệu và bevel rộng của Shake. Chọn try2. |
| read-aloud · try1 → try2 | Try1 là ảnh ngang. Try2 khóa khổ vuông và magenta trong mọi khoảng trống, giữ miệng có lưới cùng hai cung âm lam; chọn try2. |
| pace-director · try1 | Mặt số mở hình lưỡi liềm, kim lam cong từ chốt nhỏ, đầu cam vàng. Không sửa prompt trong lượt này; quầng sáng và cách đọc ở 20 px cần sửa ở lượt sinh sau. |
| quality · try1 | Thấu kính tam giác, ba mảng kính lớn, vỏ trắng vàng/than chì, hai sắc lam và một mảng phản xạ cam. Giữ prompt. |
| stat-wpm · try1 | Kim lam chỉ cao trên mặt số bán nguyệt; prompt được gửi nguyên văn nhưng bị chặn trước khi có ảnh. |
| stat-new-word, stat-evenness, rift · try1 | Đã có sidecar lần lượt là chip hình thoi đang sáng, thước thủy với bọt giữa, vết xé tím dọc có rìa kính. Chưa gửi trong lượt này vì hạn mức. |

## 3. Hậu kỳ, bảo toàn tranh và khổ

Bảy bản được chọn đều là nguồn **1254 × 1254**. Bốn nguồn có alpha thật; ba nguồn `shake`, `reduced-motion`, `read-aloud` có nền magenta. Với ba nguồn khóa màu, gọi nguyên hàm `key` của `tools/art-normalize/normalize.py`: `bg='#FF00FF'`, `mode='global'`, `despill='protect-interior'`, `no_key_hue=True`, không co mask. Dùng `ART_MAGICK=/opt/homebrew/bin/magick`; chỉ đổi `WORK` trong bộ nhớ sang `_review/152/normalize-work/`, không sửa công cụ và không ghi thư mục tạm dùng chung ngoài phạm vi.

Giữ tỉ lệ toàn ảnh, thu bằng Lanczos rồi đặt lên canvas trong suốt 1024² sao cho bbox alpha >16 dài khoảng 717 px và nằm giữa. Không cắt bỏ phần vẽ. Nguồn alpha có mặt vật thể chủ yếu ở 252–253 thay vì 255; sửa alpha bằng `-level 3.1372549%,96.8627451%` (8…247 thành 0…255), không đổi RGB. Sau đặt lề, làm tròn phần alpha gần đục 249…254 lên 255. Khử sắc magenta còn sót chỉ trong dải mép 3 px của ba ảnh tách nền, không xóa pixel hay đổi alpha tại bước khử sắc này. Số pixel từng bước có trong [delivery-log.json](../../games/typing-survival/art-src/_review/152/delivery-log.json).

Không tăng sáng, chỉnh gamma hoặc làm nét RGB; không san phẳng vật liệu, tô đè hay xóa hoa văn. Việc điều chỉnh alpha được ghi riêng, không gọi nó là alpha nguồn nguyên trạng. Các bản trung gian vẫn còn để kiểm lại. Mỗi bản 256/128/64 được thu **trực tiếp từ bản gốc 1024**, không thu nối tiếp, không làm nét bản 64.

**Mâu thuẫn cần Claude quyết theo ART_ACCEPTANCE §5:** `pace-director` vẫn có **884 pixel bán trong suốt ngoài dải mép 3 px**, phần đáng kể nằm quanh quầng sáng đầu mũi tên. Không tiếp tục cắt quầng sáng, biến nó thành mảng đục hay xóa chấm để ép ngưỡng. Bản được giữ trong tên giao là bản để xem xét, **không phải bản đã đạt**. Nên sửa đúng prompt ở try2: ánh sáng nằm trong mặt kim, bờ cắt gọn, mặt số và kim tách nhau rõ ở 20 px.

[identify-delivered.txt](../../games/typing-survival/art-src/_review/152/identify-delivered.txt) ghi đủ 28 dòng: **7 × 1024², 7 × 256², 7 × 128², 7 × 64²; tất cả `srgba`**. [artifact-check.json](../../games/typing-survival/art-src/_review/152/artifact-check.json) xác nhận đúng khổ, prompt khớp byte và cả 21 bản thu khớp pixel với phép Lanczos trực tiếp từ bản gốc. Chưa thể có 44 PNG vì thiếu bốn ảnh nguồn.

## 4. Alpha, lề và dáng riêng

Đo trên **đúng bảy file `.png` giao**, không lấy số của ứng viên trung gian. Mặt nạ vật là alpha >16. Dải mép dùng hiệu nở/co Diamond bán kính 3 px của mặt nạ, tức khoảng cách Manhattan. Ngoài dải đó đếm mọi pixel có 0 < alpha <255. Pixel mang sắc khóa: H trong 285–315°, S >0,5, alpha >0. Báo cả tỷ lệ trên canvas và tỷ lệ trên số pixel alpha >0; cả hai đều dưới 0,2%.

| Ảnh | Cạnh dài bbox % | Lệch tâm lớn nhất % | Alpha lẻ ngoài mép, px | Pixel sắc khóa | % canvas | % pixel alpha >0 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| sfx | 70,117 | 0,049 | 0 | 37 | 0,003529 | 0,019312 |
| music | 70,020 | 0,049 | 0 | 31 | 0,002956 | 0,012546 |
| shake | 70,117 | 0,049 | 0 | 9 | 0,000858 | 0,008455 |
| reduced-motion | 70,117 | 0,000 | 0 | 9 | 0,000858 | 0,008130 |
| read-aloud | 70,020 | 0,049 | 0 | 70 | 0,006676 | 0,032031 |
| pace-director | 70,020 | 0,049 | **884** | 12 | 0,001144 | 0,005839 |
| quality | 70,020 | 0,049 | 0 | 19 | 0,001812 | 0,007735 |

IoU: thu toàn canvas về 32² bằng Lanczos, mặt nạ alpha ≥128; đo đủ **21 cặp của bảy ảnh đã có**. Giữ thêm phép đo alpha >16 để thấy độ nhạy của ngưỡng. Bảy ảnh đều dưới 0,80 ở cả hai phép đo. Bốn ảnh chưa sinh chưa có số và chưa được tính là đạt. `shake`/`reduced-motion` là hai chức năng khác nhau, không phải cặp sáng/tắt của cùng một asset.

| Ảnh | IoU lớn nhất, alpha ≥128 | Cặp gần nhất | IoU lớn nhất, alpha >16 |
| --- | ---: | --- | ---: |
| sfx | 0,4874 | music | 0,5399 |
| music | 0,6020 | quality | 0,6377 |
| shake | 0,2418 | read-aloud | 0,5052 |
| reduced-motion | 0,1870 | pace-director | 0,2791 |
| read-aloud | 0,4774 | sfx | 0,5399 |
| pace-director | 0,3910 | music | 0,4775 |
| quality | 0,6020 | music | 0,6377 |

## 5. Cỡ thật và tương phản

Bảy ảnh cài đặt đều thử ở **20 px / 30 px**, trên than chì `#14181f` và thép sáng `#8c96a3`. Bốn ảnh thiếu thuộc cỡ **24 px / 36 px**, chưa có ảnh để thử. [Tờ cỡ thật](../../games/typing-survival/art-src/_review/152/native-size-proof.png) giữ pixel 1:1; xem ở 100% để chấm, không dùng bản phóng làm thay thế.

Luma trong bảng là Y′ = 0,2126R′ + 0,7152G′ + 0,0722B′, sRGB chuẩn hóa 0…1, trung bình RGB của vật có trọng số alpha sau khi thu đúng cỡ. Đây là phép đo **chênh luma trung bình** mà phiếu yêu cầu, không phải tỷ lệ WCAG hay tương phản thấp nhất ở mọi điểm trên viền. Cả bảy đạt ≥0,25 trên nền than chì; thép sáng cho độ chênh thấp và không nên là nền ưu tiên.

| Ảnh | 20 px · than chì | 20 px · thép sáng | 30 px · than chì | 30 px · thép sáng |
| --- | ---: | ---: | ---: | ---: |
| sfx | 0,4257 | 0,0651 | 0,4251 | 0,0657 |
| music | 0,3889 | 0,1019 | 0,3881 | 0,1027 |
| shake | 0,4019 | 0,0889 | 0,3957 | 0,0951 |
| reduced-motion | 0,4205 | 0,0703 | 0,4295 | 0,0613 |
| read-aloud | 0,4542 | 0,0366 | 0,4520 | 0,0388 |
| pace-director | 0,4418 | 0,0491 | 0,4417 | 0,0491 |
| quality | 0,5024 | 0,0116 | 0,5030 | 0,0122 |

Giữ thêm chẩn đoán **luminance tuyến tính sRGB** trong JSON, không trộn hai định nghĩa: tại 20 px, chênh tuyến tính của `music` là 0,2413, `shake` 0,2243, `reduced-motion` 0,2333, dưới 0,25. Nếu người duyệt định nghĩa chốt tương phản theo luminance tuyến tính thay vì luma, ba ảnh này còn trượt chốt đó. Không tăng sáng tranh để ép một định nghĩa chưa thống nhất. Phép đo ứng viên ban đầu dùng chẩn đoán tuyến tính làm điều kiện chặt hơn; phép đo cuối ghi rõ công thức luma dùng cho bảng này và vẫn giữ toàn bộ số tuyến tính.

Số đầy đủ, bbox, mọi cặp IoU và phương pháp: [measurements-final.json](../../games/typing-survival/art-src/_review/152/measurements-final.json). Số ứng viên ban đầu nằm riêng ở `measurements-candidates.json`, không được dùng thay cho bản giao.

## 6. KA5 · Tự chấm trên bản hậu kỳ

Đã xem bản giao ở 1024², các tờ trước/sau và ảnh đặt đúng 20/30 px trên hai nền. So độ hoàn thiện với HUD thương mại của chủ dự án: vật liệu và bevel có chiều sâu, ánh sáng lam/vàng và mặt trắng hợp Lightbearer; ở 20 px nhiều chi tiết vật liệu chỉ còn thành mảng. Không lấy độ đẹp bản lớn để cho trọn điểm đọc ở cỡ nhỏ.

Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” của sáu ảnh qua số đo là 2 theo định nghĩa luma đã công bố; `pace-director` chỉ 0,5. Điểm không thay cho chốt kỹ thuật hoặc việc Claude chấm lại.

| Ảnh | Năm điểm ở 1024² | Tổng | Năm điểm ở 720p, 20 px | Tổng | Nhận xét |
| --- | --- | ---: | --- | ---: | --- |
| sfx | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | Loa và tia sáng khác nhau rõ; góc nhìn miệng kèn hơi nghiêng so với yêu cầu mặt trước. |
| music | 2 / 2 / 2 / 2 / 2 | 10,0 | 2 / 1 / 2 / 2 / 2 | 9,0 | Màng loa và sóng đọc được; ở 20 px ba đỉnh sóng mất độ tách và bề mặt khá dày. |
| shake | 2 / 2 / 2 / 2 / 2 | 10,0 | 2 / 1 / 2 / 2 / 2 | 9,0 | Khung hở rõ, dấu rung rất nhỏ ở 20 px. |
| reduced-motion | 1,5 / 2 / 2 / 2 / 2 | 9,5 | 1,5 / 1 / 2 / 2 / 2 | 8,5 | Có khung tĩnh và neo; góc khung không trùng hẳn Shake, neo thu còn ít pixel. |
| read-aloud | 2 / 2 / 2 / 2 / 2 | 10,0 | 2 / 1,5 / 2 / 2 / 2 | 9,5 | Miệng và hai cung khác được loa thường; lưới chỉ còn mảng tối ở cỡ thật. |
| pace-director | 2 / 2 / 2 / 2 / 0,5 | 8,5 | 2 / 1 / 2 / 2 / 0,5 | **7,5** | 20 px dễ đọc thành trăng lưỡi liềm hơn là mặt số có kim; còn quầng sáng vi phạm alpha. |
| quality | 2 / 2 / 2 / 2 / 2 | 10,0 | 2 / 1,5 / 2 / 2 / 2 | 9,5 | Ba mảng quang học chính vẫn tách nhờ lam/cam; phản xạ vụn ở bản lớn biến mất khi thu. |

Sáu ảnh đạt tự chấm ở cả hai cỡ; **`pace-director` chưa đạt**. Điểm 10 ở bản lớn nghĩa là đủ cả năm tiêu chí của bảng này, không khẳng định hoàn hảo hoặc thay thế điểm ở cỡ game. Bốn ảnh chưa sinh không có điểm.

## 7. Tờ xem, KA1 và cách chạy lại

- [Tờ bốn hàng 152-sheet.jpg](../../games/typing-survival/art-src/_review/152-sheet.jpg): bản 256 px, cỡ 1080p trên hai nền, cỡ 720p trên hai nền, bốn icon súng hiện có và mảnh HUD thương mại cùng cao 128 px. Bốn vị trí thiếu ghi rõ “CHƯA SINH”; không có hình thay thế bằng mã.
- [Tờ cỡ thật](../../games/typing-survival/art-src/_review/152/native-size-proof.png), [mặt nạ 32 px](../../games/typing-survival/art-src/_review/152/silhouette-proof.png), bảy tờ bản sinh/hậu kỳ liên kết ở mục 1.

**KA1:** giữ manifest gốc 106 file trong `ui/icons`; bổ sung manifest lúc tiếp tục gồm 175 file trong `ui/icons`, `_review/152/` và `_review/152-*.jpg`. Đã gọi `/sbin/md5 -r` từng file. Snapshot sau có **261 file**: so với mốc gốc **155 đường dẫn thêm, 0 đổi, 0 mất**; so với mốc tiếp tục **86 thêm, 0 đổi, 0 mất**. Cả hai diff có **0 dòng nội dung bị xóa**, chỉ có dòng nội dung thêm. Không quy mọi tên mới kể từ mốc gốc là sản phẩm của riêng lượt này khi repo có agent khác cùng làm.

Hồ sơ: [md5-before.txt](../../games/typing-survival/art-src/_review/152/md5-before.txt), [md5-resume-before.txt](../../games/typing-survival/art-src/_review/152/md5-resume-before.txt), [md5-after.txt](../../games/typing-survival/art-src/_review/152/md5-after.txt), [diff mốc gốc](../../games/typing-survival/art-src/_review/152/md5-before-diff.txt), [diff mốc tiếp tục](../../games/typing-survival/art-src/_review/152/md5-resume-before-diff.txt), [tổng hợp](../../games/typing-survival/art-src/_review/152/md5-summary.json). Snapshot sau không tự băm chính nó, hai diff, JSON tổng hợp hoặc báo cáo viết sau snapshot; không thêm media sau snapshot.

Script lưu tại `_review/152/`: `prepare-resume.py`, `measure-resume.py`, `deliver-resume.py`, `measure-final.py`, `proofs-resume.py`, `audit-resume.py`. Dùng Python chuẩn và ImageMagick 7 có sẵn, không cài thư viện. Chạy từ repo cha với `PYTHONDONTWRITEBYTECODE=1 python3 <đường-dẫn-script>`. Thứ tự: prepare → measure-resume → deliver → measure-final → proofs → audit. Phải chờ prepare kết thúc trước khi đo; lần đo gọi sớm đầu tiên đã dừng vì file ứng viên chưa tạo xong, không ghi kết quả, sau đó mới chạy lại đầy đủ. Các writer chặn đích đã tồn tại; để tái dựng cần một bản sao thư mục đầu vào chỉ có try/prompt và đích trống, không chạy đè bộ hiện tại.

## 8. Sai khác và việc cần xem

1. Chưa đủ 11 ảnh: thiếu `stat-wpm`, `stat-new-word`, `stat-evenness`, `rift` và 12 bản thu tương ứng do hạn mức `image_gen`. Bốn prompt try1 còn nguyên để tiếp tục khi công cụ hoạt động lại.
2. `pace-director` được giữ để duyệt, không được coi là đã đạt. Cần sửa prompt ở try2 để rõ mặt số/kim ở 20 px và bỏ quầng sáng bằng sinh lại; không xóa phần vẽ để ép alpha theo ART_ACCEPTANCE §5.
3. `reduced-motion` cùng họ thiết bị nhưng không trùng chính xác dáng góc với Shake. Đã trừ điểm đúng đề; Claude xem có cần try3 khi hạn mức mở lại.
4. Chốt luma dùng Y′ sRGB như mục 5; đã công bố các trường hợp không đạt nếu dùng luminance tuyến tính. Claude cần thống nhất định nghĩa trước nghiệm thu.
5. Không cập nhật `ART_REPLACE_LATER.md` dù quy chuẩn chung đề nghị ghi ảnh 8–8,5 ở đó, vì phiếu chỉ cho sửa báo cáo. Ghi các điểm cần nâng ngay trong báo cáo này.

Chủ dự án xem tờ cỡ thật và độ hợp chất liệu Lightbearer. Claude chấm lại sáu ảnh qua số đo, quyết định về mặt số, quầng sáng và hai cách tính tương phản; chỉ Claude chép ảnh vào `public/` sau khi nhận. Không chạy Git, build/test game, server, trình duyệt, mạng ngoài lệnh tạo ảnh; không tạo âm, sửa game, đọc/ghi Tu Tiên hoặc đụng `.wt-*`. Không có capture trình duyệt hay raw frame cần prune; các ảnh try bắt buộc giữ nguyên.

**Trạng thái cuối: bàn giao một phần, phiếu 152 chưa hoàn tất và chưa nghiệm thu.**
