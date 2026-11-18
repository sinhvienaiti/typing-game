# Phiếu 119 · Dragonhold · Màn tựa sử thi, ảnh chủ đạo và logo

Ngày bàn giao: **29/10/2026**, macOS, repo cha. Sinh bằng **image_gen tích hợp**, không dùng API/CLI thay thế.

**Đã có 5/5 bản chọn, 6 lượt sinh. Chưa đủ điều kiện nhận toàn phiếu:** ba ảnh nền qua mục 2–8; logo và huy hiệu đúng đề, đúng chữ/khổ, nhìn tốt trên nền sáng/tối nhưng **chưa qua ngưỡng sắc khóa 0% của mục 5**. Giữ tranh theo `ART_ACCEPTANCE.md` §5 và trình Claude quyết; không gọi phần này là đạt. Bản 512 px còn các đốm alpha rất nhỏ, được ghi riêng bên dưới.

**Kiểm lại theo yêu cầu hiện tại, 29/10/2026:** toàn bộ năm bản chọn, sáu nguồn sinh, prompt và tờ kiểm bên dưới đã có trước lượt làm việc này. Lượt này **không sinh ảnh mới, không ghi đè ảnh hoặc prompt**. Đã thêm script và chứng cứ đo lại tại [_review/119/recheck-20261029.py](../../games/dragon-hold/art-src/_review/119/recheck-20261029.py), [kết quả JSON](../../games/dragon-hold/art-src/_review/119/recheck-20261029.json); chỉ cập nhật báo cáo được phiếu cho phép sửa.

Đã xem lại năm bản hậu kỳ ở khổ đầy đủ, năm tờ “bản sinh | bản hậu kỳ”, tờ cỡ nhỏ, chữ logo, mép alpha và tờ so tham chiếu. Giữ điểm tự chấm mục 4; đây không phải lượt chấm độc lập của Claude. Đo lại xác nhận khổ đúng, prompt bản chọn khớp nguồn, cả sáu prompt khớp nhật ký gửi công cụ. Luma logo/menu lần lượt **0,112081 / 0,122171**, đạt. Alpha logo/huy hiệu vẫn có **752 / 583** pixel sắc khóa, tương ứng **0,177090% / 0,128281%**; bản 512 vẫn có **6 / 3** đốm nhỏ, logo 512 có lề trên/dưới **18 / 23 px**. Không đổi trạng thái thành đạt.

KA1 đo lại bằng `md5 -r`: [trước lượt kiểm](../../games/dragon-hold/art-src/_review/119/md5-before-recheck-20261029.txt) và [sau lượt kiểm](../../games/dragon-hold/art-src/_review/119/md5-after-recheck-20261029.txt) đều **465 tệp**, **0 thêm / 0 đổi / 0 mất**; [diff rỗng](../../games/dragon-hold/art-src/_review/119/recheck-20261029-recheck-diff.txt). So với mốc đầu phiếu vẫn chỉ **26 tệp thêm / 0 đổi / 0 mất**. Lệnh kiểm: `python3 -B games/dragon-hold/art-src/_review/119/recheck-20261029.py`. Script từ chối ghi đè chứng cứ đã có; muốn chạy lại dùng tên hồ sơ mới.

**Phần dừng và lý do:** không ép sửa hue trong phần sơn và không thay bản chọn hiện hữu. Phiếu cấm ghi đè tệp có sẵn; đồng thời `ART_ACCEPTANCE.md` §5 yêu cầu “Khi một ngưỡng số mâu thuẫn với tranh (muốn đạt số phải làm bẩn tranh), dừng lại, giữ tranh đẹp, ghi mâu thuẫn trong báo cáo để Claude quyết.” Mâu thuẫn cụ thể đã ghi ở mục 5 bên dưới và được phép đo mới xác nhận. Claude/chủ dự án cần xem hai alpha cùng bản 512 trước khi quyết định bước tiếp theo. **Toàn phiếu vẫn chưa đủ điều kiện nhận.**

Chỉ đạo mới “Chạy ngay, không chờ phiếu khác” đã thay điều kiện chờ 118 trong báo cáo cũ. Hồ sơ cũ được giữ nguyên tại [report-before-resume.md](../../games/dragon-hold/art-src/_review/119/report-before-resume.md); `manifest.json` cũ là hồ sơ chuẩn bị, **không phải trạng thái hiện tại**.

## 1. Tệp đã làm và các lượt sinh

Thư mục bản chọn: [ui/title-epic/](../../games/dragon-hold/art-src/ui/title-epic/). Mọi nguồn sinh giữ nguyên byte dưới tên `.tryN.png`, cùng `.tryN.prompt.txt`. Prompt bản chọn giữ nguyên prompt của lượt tương ứng. [Nhật ký gửi công cụ](../../games/dragon-hold/art-src/_review/119/generation-record.json) ghi toàn bộ prompt thực tế, ảnh đính kèm và tên kết quả công cụ.

| Ảnh | Lượt đã dùng / chọn | Khổ nguồn → bản chọn | Kết quả |
|---|---|---|---|
| [title-backdrop.png](../../games/dragon-hold/art-src/ui/title-epic/title-backdrop.png) | 2 / 2 | 1536 × 1024 → giữ nguyên | Đạt khổ và hai vùng luma. |
| [keyart.png](../../games/dragon-hold/art-src/ui/title-epic/keyart.png) | 1 / 1 | 1536 × 1024 → giữ nguyên | Rồng trưởng thành trên cổng, phun lửa xuống cầu; lính rêu và sói héo tiến vào. |
| [poster.png](../../games/dragon-hold/art-src/ui/title-epic/poster.png) | 1 / 1 | 1024 × 1536 → giữ nguyên | Cùng trận đánh, dựng lại dọc, có khoảng trời cho logo. |
| [logo.png](../../games/dragon-hold/art-src/ui/title-epic/logo.png) | 1 / 1 | 2172 × 724 → giữ nguyên | Tỷ lệ đúng 3:1, cạnh dài ≥1536; đúng “Dragonhold”. Có `logo.alpha.png`, `logo.512.png`. |
| [emblem.png](../../games/dragon-hold/art-src/ui/title-epic/emblem.png) | 1 / 1 | 1254 × 1254 → 1024 × 1024 | Rồng, cổng, hai đỉnh núi trong vòng vàng/sắt. Có `emblem.alpha.png`, `emblem.512.png`. |

**Prompt từng lượt:**

- **Màn tựa lượt 1:** dùng prompt đã chuẩn bị, giữ nguyên STYLE + TITLE. Bố cục đẹp nhưng núi/mây sáng và lò lửa đi vào vùng đặt chữ; luma trượt cả hai vùng.
- **Màn tựa lượt 2:** giữ nguyên các khối bắt buộc, thêm đoạn sửa bố cục ở cuối: đường núi thấp, trời giữa trên yên hơn, tia sáng lệch phải, lò lửa ở dưới phải, khu vực menu được yêu cầu nằm trong bóng tự nhiên. Kết quả menu thực tế nằm trên rừng/sương tối nhiều hơn mặt đá; đo đạt và ghép mock đọc được. Không sửa tranh bằng hộp tối.
- **Keyart lượt 1:** giữ prompt đã chuẩn bị; đính kèm đúng huy hiệu 096 chỉ lấy màu Hỏa Long, lính rêu và sói héo chỉ lấy dáng/màu. Không lấy nét dễ thương của rồng cũ.
- **Poster lượt 1:** đính kèm `keyart.png` đã chọn và đã xem, giữ câu tham chiếu bắt buộc; dựng lại dọc cùng rồng, cổng, cầu, ánh sáng và bầy quái.
- **Logo lượt 1:** STYLE-UI thay câu cấm chữ cuối bằng LOGO nguyên văn; thêm khổ 3:1, lề 64 px, lòng chữ rõ. Công cụ trả 2172 × 724 thay vì 3072 × 1024 dự kiến; vẫn đúng yêu cầu cạnh dài ≥1536, không phóng to.
- **Huy hiệu lượt 1:** STYLE-UI + EMBLEM nguyên văn; thêm lề rộng và yêu cầu cổng/rồng/hai đỉnh núi rõ ở cỡ nhỏ. Nguồn lớn hơn đích nên chỉ thu xuống.

Không có lượt sinh nào bị bỏ hoặc xóa. Chưa dùng hết ba lượt cho bất kỳ ảnh nào; không sinh tiếp chỉ để đuổi các điểm sắc khóa trong vùng sơn tối khi §5 yêu cầu giữ tranh.

## 2. Hậu kỳ không phá tranh

Bốn bản `title-backdrop.png`, `keyart.png`, `poster.png`, `logo.png` **giống nguyên byte nguồn được chọn**. Không chỉnh gamma, không phủ mảng tối, không xóa núi/mây, không thay phần vẽ. Huy hiệu chỉ thu bằng Lanczos:

```sh
/opt/homebrew/bin/magick emblem.try1.png -gravity center -crop 1254x1254+0+0 +repage -filter Lanczos -resize '1024x1024>' emblem.png
```

Lệnh dùng đường dẫn đầy đủ được lưu trong [processing.json](../../games/dragon-hold/art-src/_review/119/processing.json). Crop huy hiệu bằng đúng toàn bộ khổ vuông nguồn, không bỏ phần vẽ.

Tách nền bằng **bản sao nguyên trạng** của `tools/art-normalize/key-alpha.sh`, `common.sh`, `normalize.py`, `seam_analysis.py` trong `_review/119/normalize-tool/`. Hash bốn bản sao khớp nguồn. Cách này giữ WORK tạm trong phạm vi được phép, không ghi `tools/art-normalize/.tmp/`.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/dragon-hold/art-src/_review/119/normalize-tool/key-alpha.sh INPUT OUTPUT --bg '#FF00FF' --mode global --despill protect-interior --no-key-hue
```

`--no-key-hue` được bật vì prompt quy định nội dung không có hồng/magenta/tím tươi. Sau tách nền chỉ dọn thành phần alpha rời **nhỏ hơn 20 px**, nối 8 hướng: logo 7 đốm / 75 px, huy hiệu 1 đốm / 1 px. Không xóa thành phần lớn hoặc bộ phận huy hiệu. Nguồn trước dọn vẫn còn tại `_review/119/*-keyed.png`.

Năm tờ cùng cỡ “bản sinh | bản hậu kỳ”:

- [Màn tựa](../../games/dragon-hold/art-src/_review/119-title-backdrop-before-after.jpg)
- [Keyart](../../games/dragon-hold/art-src/_review/119-keyart-before-after.jpg)
- [Poster](../../games/dragon-hold/art-src/_review/119-poster-before-after.jpg)
- [Logo](../../games/dragon-hold/art-src/_review/119-logo-before-after.jpg)
- [Huy hiệu](../../games/dragon-hold/art-src/_review/119-emblem-before-after.jpg)

Điểm M bên dưới chấm trên bản hậu kỳ đã giao, gồm bản alpha khi áp dụng.

## 3. Kiểm bắt buộc

### KA1 · Không sửa ảnh và prompt cũ

Đã chạy **`md5 -r` từng file dưới `art-src/ui/`, đệ quy**, cả trước phần chuẩn bị cũ, trước lần tiếp tục này và sau bàn giao.

| Mốc so | Trước | Sau | Thêm | Đổi | Mất |
|---|---:|---:|---:|---:|---:|
| Mốc đầu phiếu → giao | 439 | 465 | 26 | 0 | 0 |
| Mốc tiếp tục → giao | 444 | 465 | 21 | 0 | 0 |

26 tệp thêm gồm 5 prompt chuẩn bị cũ và 21 tệp của lần tiếp tục. Diff thực tế chỉ thêm dòng nội dung; mã thoát 1 của `diff -u` là có khác biệt do thêm file, không phải lỗi kiểm.

Chứng cứ: [trước](../../games/dragon-hold/art-src/_review/119/md5-before.txt), [trước lần tiếp tục](../../games/dragon-hold/art-src/_review/119/md5-before-resume.txt), [sau giao](../../games/dragon-hold/art-src/_review/119/md5-after-delivery.txt), [diff từ mốc đầu](../../games/dragon-hold/art-src/_review/119/md5-delivery-original-diff.txt), [diff từ mốc tiếp tục](../../games/dragon-hold/art-src/_review/119/md5-delivery-resume-diff.txt), [JSON kiểm cuối](../../games/dragon-hold/art-src/_review/119/delivery-audit.json). Sáu `.tryN.png` cũng được hash đối chiếu với kết quả gốc của công cụ: **6/6 giống nguyên byte**.

### Mục 2–4 · Khổ, chữ logo, không chữ lạc

Khổ bản chọn đúng bảng mục 1. Bản alpha giữ cạnh dài nguồn bản chọn: logo **2172**, huy hiệu **1024**; bản 512 là **512 × 171** và **512 × 512**, không phóng to.

Logo đã xem toàn từ và từng chữ: **D-r-a-g-o-n-h-o-l-d, đủ 10 chữ, D hoa, phần còn lại thường**, không chữ thừa/lạ. Font đối chiếu **Arial**, đường dẫn `/System/Library/Fonts/Supplemental/Arial.ttf`.

- [Toàn từ cạnh Arial](../../games/dragon-hold/art-src/_review/119/logo-word-vs-arial.jpg)
- [Tờ tra mười chữ](../../games/dragon-hold/art-src/_review/119/logo-letters-4x.jpg)
- [Các crop đúng 4×, từng chữ](../../games/dragon-hold/art-src/_review/119/letters/): tờ tra thu nhỏ; các `*-4x.png` và `*-vs-arial.jpg` giữ phóng 4×. Cắt từ bản alpha để kiểm chữ sau hậu kỳ; nhãn “bản sinh” trên thẻ chỉ nguồn chữ vẽ, không phải ảnh magenta chưa tách.

Đã xem ảnh đầy đủ: **title-backdrop, keyart, poster và emblem không có chữ/số đọc được**. Các cờ có hình rồng trang trí, không phải ký tự. Kiểm bằng mắt, không dùng OCR hay mạng.

### Mục 5 · Alpha: còn ngoại lệ, chưa đạt toàn mục

Sắc khóa được đếm đúng điều kiện **alpha > 0, hue 285–330° và S >0,5**; tỷ lệ tính trên số pixel alpha >0. Alpha đo theo 8 bit, bbox cũng dùng alpha >0.

| Bản | Alpha min–max | Pixel sắc khóa / pixel hiện | Tỷ lệ | Đốm rời <20 px | Lề trái / trên / phải / dưới |
|---|---|---:|---:|---:|---|
| logo.alpha.png | 0–255 | 752 / 424642 | **0,177090%** | 0 | 132 / 86 / 186 / 107 |
| emblem.alpha.png | 0–255 | 583 / 454471 | **0,128281%** | 0 | 84 / 55 / 84 / 88 |
| logo.512.png | 0–255 | 73 / 27700 | **0,263538%** | **6** | 29 / **18** / 41 / **23** |
| emblem.512.png | 0–255 | 241 / 116789 | **0,206355%** | **3** | 40 / 25 / 40 / 42 |

Chứng cứ số: [alpha-measurements.json](../../games/dragon-hold/art-src/_review/119/alpha-measurements.json). Bản alpha đầy đủ đạt min/max, không đốm nhỏ và lề ≥24 px, **trượt sắc khóa 0%**. Bản 512 phát sinh đốm rất nhỏ sau Lanczos; logo 512 còn thiếu lề trên/dưới nếu áp ngưỡng 24 px cho cả bản thu. Không giấu các kết quả này.

[Tờ mép 4× trên nền sáng/tối](../../games/dragon-hold/art-src/_review/119-edge.jpg): không thấy viền hồng liên tục ở các đoạn đã cắt. Tuy vậy, kết quả nhìn không thay thế phép đếm toàn ảnh.

**Mâu thuẫn với phần vẽ / điểm dừng §5:** 681/752 pixel bị báo của logo và 526/583 của huy hiệu có kênh sáng nhất ≤32/255, tức nằm gần đen. Ví dụ logo (358,127) là RGBA **(2,0,1,255)**, vẫn thuộc dải hue/S bị cấm. Bước thử sửa có chốt chỉ xử lý sắc khóa cách vùng trong suốt ≤8 px; nó dừng ở phần sơn nằm sâu hơn. Ví dụ logo (564,243) là **(78,38,63,255)**. Không tự coi tất cả những điểm này là nền và không ép hue bằng cách sửa phần sơn bên trong.

Hai script `repair-alpha.py`, `repair-alpha-v2.py` dừng **trước khi xuất bất kỳ ảnh sửa nào**, giữ nguyên các alpha đã giao; hai thư mục ứng viên tương ứng rỗng. Không có “bản sạch” bị giấu. Chưa khắc phục các điểm này bằng một lượt sinh khác, và không dùng màu phẳng phủ chúng.

**Hệ quả:** logo/emblem là bản chọn để duyệt tranh, **chưa phải alpha qua toàn bộ chốt kỹ thuật**. Claude cần quyết định ngoại lệ/chiến lược xử lý tiếp. Không tích hợp hai alpha này vào runtime trong phiếu.

### Mục 6 · Chỗ cho logo/menu

Đo trên bản cắt giữa **1536 × 864**, gốc (0,80) của ảnh 1536 × 1024. Luma Rec.709 trên kênh sRGB, chuẩn hóa 0–1. Pixel crop: logo `768x208+384+51`; menu `492x320+46+475`. Sai số làm tròn tọa độ <1 px so với phần trăm.

| Ảnh | SD logo, ngưỡng ≤0,12 | SD menu, ngưỡng ≤0,14 |
|---|---:|---:|
| title-backdrop.try1 | 0,192143 · trượt | 0,169963 · trượt |
| **title-backdrop.try2 / bản chọn** | **0,112081 · đạt** | **0,122171 · đạt** |

[119-title-mock.jpg](../../games/dragon-hold/art-src/_review/119-title-mock.jpg): crop 16:9, logo alpha rộng **691 px ≈45%**, giữa trên, y=52; khối xám **461 × 302 px ≈30% ×35%** ở góc dưới trái. Hộp xám chỉ xuất hiện trên mock kiểm, không nung vào bản nền. Đã xem mock; logo tách khỏi trời, menu không đè cổng/điểm lửa chính.

### Mục 7 · Đúng game

[119-models.jpg](../../games/dragon-hold/art-src/_review/119-models.jpg): **khớp** màu rồng đỏ cam, bụng kem ấm, sừng/gai sẫm; rồng mới dữ và trưởng thành. **Khớp** lính gỗ/rêu có mắt vàng xanh, vải tím xám và sói giáp đá sẫm có gân vàng xanh. Không thay thành người, orc hay loài quái khác.

Sai khác nhỏ: giáp đá và gân của bầy quái chìm hơn trong ánh lửa ở cỡ nhỏ; đầu mút cánh rồng keyart ra ngoài mép trên. Màn tựa lượt 2 có một bóng rồng rất nhỏ ở gần rồng chính; không xóa bằng công cụ.

### Mục 8 · Đọc nhỏ

Đã xem [119-small.jpg](../../games/dragon-hold/art-src/_review/119-small.jpg) ở đúng cỡ thẻ, không dùng bản phóng thay nghiệm thu.

| Bản nhỏ | Nhận diện |
|---|---|
| Keyart, cạnh dài 384 px | Rõ rồng, cổng ải, dòng lửa và bầy quái; vách đá/tượng tạo quy mô. Mặt riêng từng lính không đọc rõ. |
| Poster, cạnh dài 384 px | Rõ cùng rồng/cổng và hai vách; bầy quái thành một dòng tối dưới lửa, vẫn nhận ra cuộc xung phong. |
| Emblem, ảnh 64 ×64 px | Nhận ra huy hiệu tròn vàng/sắt, rồng cam phía trên, cổng sáng phía dưới và hai đỉnh núi trắng. Các chi tiết trang trí nhỏ nhập khối, khá dày. |
| Logo, cạnh dài 512 px | Đọc đúng Dragonhold; cánh ở D và nét lửa dưới từ còn rõ. |

### Mục 9 · So mức chợ

[119-vs-ref.jpg](../../games/dragon-hold/art-src/_review/119-vs-ref.jpg), khổ **3764 ×1412**: hàng trên title-mock, keyart, poster và tham chiếu chủ dự án, **mỗi ảnh cao 640 px**, không kéo méo. Hàng dưới có huy hiệu 096 và `pine-river-far.png` cũ. Có dòng nhận xét dưới từng ảnh mới.

Tự đánh giá **đứng cạnh được** về quy mô cổng/tượng, ba lớp sâu + trời, ánh sáng bình minh có hướng và hoàn thiện đá/rừng/nước. Chưa tự chấm ngang 9 của ảnh mẫu: cảnh mới dày chi tiết và mang tính tranh quảng bá hơn, keyart cắt đầu cánh, huy hiệu nhỏ khá rối. Đây là điểm Codex; **Claude chưa chấm nhận**.

## 4. KA5 · Điểm trên bản hậu kỳ

Q gồm năm tiêu chí theo bảng trong `ART_ACCEPTANCE.md`: **đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau**, mỗi tiêu chí 0–2. Chấm ở ảnh đầy đủ và cỡ sử dụng; logo ở 512 px, huy hiệu thêm kiểm 64 px.

| Ảnh | M đầy đủ | Q đầy đủ (năm thành phần) | M nhỏ | Q nhỏ | Điểm còn thiếu |
|---|---:|---|---:|---:|---|
| title-backdrop | 8,5 | **9,5** (2 / 2 / 2 / 1,5 / 2) | 8 | 9 | Có thêm bóng rồng nhỏ; menu không hoàn toàn là mặt đá như prompt sửa. |
| keyart | 8,5 | **9** (2 / 2 / 2 / 1,5 / 1,5) | 8 | 8,5 | Cánh chạm/cắt mép trên, vùng logo trên trái còn mây sáng; bầy quái nhỏ khá dày. |
| poster | 8,5 | **9,5** (2 / 1,5 / 2 / 2 / 2) | 8 | 9 | Bầy quái và lửa nhập khối khi thu 384 px. |
| logo | 8,5 | **9** (2 / 2 / 2 / 2 / 1) | 8 | 8,5 | Alpha trượt sắc khóa; bản 512 có đốm nhỏ và thiếu lề theo chốt 24 px. |
| emblem | 8,5 | **9** (2 / 2 / 2 / 2 / 1) | 8 | 8 | Trang trí dày ở 64 px; alpha trượt sắc khóa, bản 512 có đốm nhỏ. |

M của logo/huy hiệu chấm theo vật liệu và khả năng nhận diện của logo game thương mại. **M/Q ≥8 không miễn kiểm kỹ thuật:** hai alpha vẫn chưa đạt mục 5, nên toàn phiếu chưa đủ điều kiện “xong”. Không ghi vào tài liệu ngoài phạm vi như `ART_REPLACE_LATER.md`.

## 5. Script, giới hạn và việc cần xem

Script và hồ sơ đều ở [_review/119/](../../games/dragon-hold/art-src/_review/119/):

- `acquire.py`: phát lại việc sao nguyên byte kết quả công cụ, từ chối tên đã tồn tại; không gọi sinh lại.
- `process.py`: chọn lượt, thu huy hiệu, chạy key-alpha trong WORK được phép, đo luma.
- `finish.py`: đo alpha, dọn bụi rất nhỏ trước xuất alpha, thu 512, dựng mock và các tờ kiểm.
- `lettering.py`: mười crop 4× và đối chiếu Arial.
- `final-audit.py`: `md5 -r`, diff thật, khổ, prompt, hash nguồn sinh và hash bản sao công cụ.
- `repair-alpha*.py`: hai phép thử có chốt bảo vệ, đã dừng trước khi xuất; không chạy tiếp bỏ chốt.
- Các script chuẩn bị cũ vẫn giữ nguyên. Mọi script xuất ảnh từ chối ghi đè; muốn tái tạo phải dùng bộ đích mới, không chạy đè lên hồ sơ đã giao.

Lệnh thực hiện chính:

```sh
python3 -B games/dragon-hold/art-src/_review/119/process.py
python3 -B games/dragon-hold/art-src/_review/119/finish.py
python3 -B games/dragon-hold/art-src/_review/119/lettering.py
python3 -B games/dragon-hold/art-src/_review/119/final-audit.py
```

Chỉ ghi ảnh/prompt trong `ui/title-epic/`, tờ kiểm và script trong vùng `_review/119*`, cùng báo cáo này. Không sửa tệp có trước trong UI hoặc hồ sơ chuẩn bị. Báo cáo được cập nhật theo ngoại lệ cho phép sửa báo cáo của phiếu.

Không chạy Git, build/test game, server, trình duyệt, mạng ngoài công cụ tạo ảnh; không tích hợp runtime; không làm âm thanh; không đọc/ghi Tu Tiên hoặc game khác. Ảnh kiểm là ghép tĩnh trong vùng phiếu, không có raw frame trình duyệt phải prune.

**Chủ dự án/Claude cần xem:** [mock màn tựa](../../games/dragon-hold/art-src/_review/119-title-mock.jpg), [so tham chiếu](../../games/dragon-hold/art-src/_review/119-vs-ref.jpg), năm bản lớn và bản nhỏ; chấm lại M/Q. Riêng logo/huy hiệu cần quyết mục 5 trước khi nhận. Giữ các bản đẹp hiện tại, chưa ép sửa màu phần sơn để đạt con số 0%.
