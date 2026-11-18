# Phiếu 134 · Wordwoven · HUD và hệ thống

Ngày làm: 29/10/2026, repo cha trên Mac mini M4, macOS.

**Đã tạo đủ 12 icon, 13 lượt sinh, 48 PNG chọn và 48 prompt cạnh ảnh. Bộ chọn ở `games/typing-defense/art-src/ui/icons/134-final/`. Cả 48 file chọn đạt khổ, kênh màu và hai kiểm alpha. Các bản gốc đạt lề, tương phản luma và IoU. KA5 tự chấm ở 720p từ 8 đến 10. Chưa có lượt chấm nhận của Claude; chưa chép vào `public/`.**

## 1. Bộ chọn và hồ sơ

- **Chỉ lấy bộ chọn:** [ui/icons/134-final/](../../games/typing-defense/art-src/ui/icons/134-final/). Mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png` và prompt nguyên văn cạnh từng file.
- [Tờ xem cuối](../../games/typing-defense/art-src/_review/134-sheet-final.jpg): bốn hàng đúng nội dung phiếu, hai nền lấy từ bảng 115; bốn icon có sẵn là `hud-settings`, `vol-keyboard`, `vol-music`, `vol-effects`.
- [Cỡ 720p thực](../../games/typing-defense/art-src/_review/134-native720-final.jpg), [cùng pixel phóng 6× để soi](../../games/typing-defense/art-src/_review/134-native720-final-6x.jpg).
- Mỗi ảnh có [cặp bản sinh và hậu kỳ](../../games/typing-defense/art-src/_review/134/aligned/), căn cùng cỡ vật để so phần vẽ. Bản sinh chỉ cắt và căn khung; nguồn nguyên byte vẫn ở `.tryN.png`. Các tờ `*-before-after-final.jpg` còn giữ cả canvas nguồn trước căn lề.
- [Số đo bản gốc](../../games/typing-defense/art-src/_review/134/measurements-selected.json), [kiểm đủ 48 file](../../games/typing-defense/art-src/_review/134/final-package-audit.json), [khổ và kênh đủ 48 file](../../games/typing-defense/art-src/_review/134/identify-final-package.txt).

Các file nằm trực tiếp ở `ui/icons/` là lượt thử và bộ xuất trước kiểm toàn bộ bản thu; **không phải bộ chọn cuối**. Giữ nguyên chúng theo lệnh cấm ghi đè/xóa. Bộ `134-final/` có cùng 12 master nguyên byte, cùng prompt; 36 bản thu có thêm bước sửa mép sau Lanczos. Không dùng lại các bản thu ở gốc thư mục.

## 2. Tham chiếu, prompt và lượt sinh

Đã dùng skill `imagegen`, công cụ tích hợp **`image_gen`**, một vật mỗi lượt. STYLE-UI lấy nguyên văn ở chỉ đạo mỹ thuật 28/10; KIND ICON lấy ở §3.5 tài liệu định dạng Wordwoven. Khối riêng của phiếu đứng sau để ghi đè mức chiếm ô 80% của KIND thành 70%, giữ vật trong giới hạn 68–72%, ưu tiên hình lớn đọc ở 16–29 px. Dòng nền M nguyên văn, vật không có hồng/tím hồng. Không dùng STYLE sách tranh cũ.

115 đã có ở **`ui/frames-epic/`**, chưa có đường dẫn `ui/frames/` ghi trong phiếu. Đính kèm `panel-large.png`, `portrait-ring.png` của 115 và `title-epic/keyart.png` của 113. Riêng `play` đính kèm `pause.try1.png`; `sound-off` đính kèm `sound-on.try1.png`, cùng panel và key art. [Nhật ký sinh](../../games/typing-defense/art-src/_review/134/generation-records.json) ghi đầy đủ nguồn và tham chiếu. SHA-256 của **13/13** bản `.try*` trùng nguồn công cụ.

| Tên | Lượt giữ / chọn | Prompt đã sửa và kết quả |
| --- | --- | --- |
| `seeds` | 1 / 1 | Túi vải kem đổ hạt gạo vàng, dây ngọc. Không sinh lại; chỉnh lề bằng công cụ từ 68,36% lên 71,39% để dáng không trùng đĩa nút. |
| `day` | 1 / 1 | Đĩa mặt trời vàng sau núi đá vôi, tia lớn; giữ lượt đầu. |
| `night` | 1 / 1 | Trăng lưỡi liềm bạc, một sao bốn cánh, núi đá vôi; giữ lượt đầu. |
| `night-call` | **2 / 2** | Lượt 1 có mặt chiêng tròn nhưng thiếu trăng. Lượt 2 sửa phần riêng: trăng ngà lớn chiếm mặt chiêng, mặt sau trăng thoáng, cán treo dài và dùi chéo giúp dáng khác đĩa nút. Lượt 1 được giữ nguyên. |
| `review-book` | 1 / 1 | Sách đóng bìa đỏ son, dấu trang ngọc, cạnh giấy ngà. Không sửa prompt; tăng sáng toàn vật 5% bằng công cụ. |
| `chain` | 1 / 1 | Đúng ba vòng đồng liên kết chéo, khớp sáng hổ phách, ba lỗ rỗng; giữ lượt đầu. |
| `pause` | 1 / 1 | Hai thanh đá vôi trên đĩa ngọc, khe tối rộng; giữ lượt đầu. |
| `play` | 1 / 1 | SAME: đổi hai thanh thành tam giác phải, giữ đĩa, hoa văn và ánh sáng; giữ lượt đầu. |
| `sound-on` | 1 / 1 | Chuông tay bằng đồng, cán đá vôi và hai cung âm vàng; giữ lượt đầu. |
| `sound-off` | 1 / 1 | SAME: cùng chuông, cung đồng tối và vạch ngọc chéo; giữ lượt đầu. |
| `close` | 1 / 1 | Hai thanh đá vôi chạm giao chéo, tâm ngọc; giữ lượt đầu. |
| `warning` | 1 / 1 | Biển đồng tam giác có đinh và chấm nổi bằng đá ngà; không dùng chữ in; giữ lượt đầu. |

Tổng **13 lượt**, không ảnh nào quá 2 lượt. Prompt chọn là bản sao nguyên văn prompt của lượt chọn, kể cả các bản thu.

## 3. Hậu kỳ giữ phần vẽ

Nguồn công cụ là PNG **1254 × 1254**; mọi nguồn được giữ nguyên. Tách nền M bằng `tools/art-normalize` ở chế độ `global`, `protect-interior`, `--no-key-hue`; WORK chuyển vào `_review/134/`, không ghi vào thư mục công cụ. Cắt quanh alpha >16 với đệm 4 pixel nguồn, Lanczos giữ tỷ lệ và căn giữa canvas trong suốt 1024². Không san phẳng mặt vật, không xóa họa tiết, không ghép hình vẽ mới. Chỉ sách tăng sáng toàn ảnh 5%, trong giới hạn ±10%.

Sau nội suy, sửa sắc khóa trong dải mép 6 px của master, giữ alpha ở bước khử màu. Những điểm nằm trong phần sơn được giữ lại và tính đủ vào số dư màu khóa. Các điểm alpha lẻ ngoài dải mép 3 px do nội suy được làm tròn về 0/255. Tham số và số pixel nằm trong các `final-processing-*.json`.

Mỗi bản thu được lấy **trực tiếp từ master**, riêng từng cỡ, bằng Lanczos; không thu nối tiếp và không làm nét bản 64. Kiểm mở rộng trên cả 48 file phát hiện màu tím gần đen và một ít điểm alpha lẻ mới sinh khi nội suy. Đã sửa **chỉ dải mép 3 px** của bản thu trong bộ chọn mới. Bảng dưới ghi số pixel đã sửa theo thứ tự **256 / 128 / 64**; không phải số lỗi còn lại.

| Ảnh | Alpha lẻ đã làm tròn | Pixel sắc khóa đã sửa ở mép | Alpha lẻ còn lại | Sắc khóa còn lại (%) |
| --- | --- | --- | --- | --- |
| `seeds` | 18 / 4 / 0 | 31 / 3 / 3 | 0 / 0 / 0 | 0 / 0 / 0 |
| `day` | 0 / 0 / 1 | 33 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `night` | 0 / 0 / 0 | 122 / 12 / 1 | 0 / 0 / 0 | 0 / 0 / 0 |
| `night-call` | 36 / 3 / 0 | 84 / 7 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `review-book` | 0 / 0 / 0 | 32 / 3 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `chain` | 0 / 0 / 0 | 70 / 6 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `pause` | 0 / 0 / 1 | 4 / 1 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `play` | 0 / 0 / 2 | 6 / 2 / 1 | 0 / 0 / 0 | 0 / 0 / 0 |
| `sound-on` | 0 / 0 / 0 | 81 / 4 / 2 | 0 / 0 / 0 | 0 / 0 / 0 |
| `sound-off` | 0 / 0 / 0 | 147 / 12 / 1 | 0 / 0 / 0 | 0 / 0 / 0 |
| `close` | 0 / 0 / 0 | 45 / 1 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `warning` | 0 / 0 / 0 | 6 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |

Đã xem bản hậu kỳ đầy đủ của 12 master, cỡ trong game trên hai nền và các tờ trước/sau. Các bản thu chỉ sửa điểm viền, không thay hình khối hoặc chi tiết bên trong. Không có ngưỡng nào phải đạt bằng cách phủ hoặc xóa phần tranh.

## 4. KA1 · MD5 và khổ

Mốc trước được lập khi `ui/icons/` chưa có file: **0 file**. Chạy `md5 -r` mọi file đệ quy trong thư mục đích sau giao bộ chọn: **218 file**, thêm **218**, sửa **0**, xóa **0**. Diff chỉ thêm dòng. Tổng gồm nguồn, prompt, bộ xuất đầu và bộ chọn; bộ chọn có **48 PNG + 48 prompt**.

- [md5-before.txt](../../games/typing-defense/art-src/_review/134/md5-before.txt)
- [md5-after-final.txt](../../games/typing-defense/art-src/_review/134/md5-after-final.txt), [diff cuối](../../games/typing-defense/art-src/_review/134/md5-final.diff.txt), [tổng hợp](../../games/typing-defense/art-src/_review/134/md5-final-summary.json)

`md5-after.txt` là mốc bộ xuất đầu 122 file, được giữ nguyên; **mốc giao cuối là `md5-after-final.txt`**. Tên bổ sung tránh ghi đè hồ sơ đã tạo.

Lệnh `magick identify -format '%f %wx%h %[channels]\n'` đã chạy đủ 48 PNG chọn: 12 master **1024 × 1024**, 12 bản **256²**, 12 bản **128²**, 12 bản **64²**, tất cả **sRGBA**, sRGB, 8 bit. ImageMagick 7.1.2-34 in kênh là `srgba 4.0`; `4.0` là số kênh, không phải một khổ ảnh khác. Parser đầu chỉ chờ chuỗi kết thúc bằng `srgba`, đã sửa ở `publish-verified.py`; không có ảnh lỗi khổ/kênh vì lỗi parser đó.

## 5. Số đo bản gốc và độ đọc

Nền ngọc **`#051e15`** là trung vị từng kênh vùng giữa 256² của `panel-large` 115. Nền đá sáng **`#b5a490`** là trung vị 33.793 pixel viền sáng ít bão hòa của cùng panel (R>150, G>130, B>100, max−min≤75, alpha>127). Tờ cuối dùng hai màu này; các tờ cũ dùng mã tạm của phiếu được giữ làm hồ sơ.

**Định nghĩa:** luma Y′ = (0,2126R + 0,7152G + 0,0722B)/255 trên sRGB; lấy trung bình vật có trọng số alpha sau khi thu đúng cỡ. ΔY′ là trị tuyệt đối hiệu trung bình đó với nền. Ngưỡng 0,25 được kiểm trên nền ngọc ở **cả 720p và 1080p**. JSON cũng lưu luminance tuyến tính dưới `contrast_linear`; đây là phép đo khác, nhiều vật không đạt 0,25 theo phép tuyến tính. Không dùng nhầm hai phép đo.

IoU: master Lanczos về canvas 32², mặt nạ alpha >16, không căn/cắt lại riêng từng cặp. Bảng lấy cặp lớn nhất **ngoài cặp trạng thái**; các cặp trạng thái có ngưỡng riêng. Alpha lẻ là pixel 0<alpha<255 ngoài dải mép 3 px quanh mặt nạ alpha>127. Sắc khóa: hue lệch màu M ≤15°, S>0,5, alpha>0; mẫu số là mọi pixel alpha>0.

| Ảnh | Hộp alpha>16 · cạnh dài/canvas | Lệch tâm max | Alpha lẻ ngoài mép | Sắc khóa còn lại · số/diện tích có alpha | ΔY′ nền ngọc 720p / 1080p | IoU lớn nhất · ảnh khác |
| --- | --- | --- | --- | --- | --- | --- |
| `seeds` | 731 × 683 · 71.39% | 0.049% | 0 | 0 / 323907 · 0.0000% | 0.4606 / 0.4609 | 0.7870 · `pause` |
| `day` | 684 × 718 · 70.12% | 0.000% | 0 | 11 / 331531 · 0.0033% | 0.4113 / 0.4107 | 0.7620 · `pause` |
| `night` | 674 × 718 · 70.12% | 0.000% | 0 | 3 / 290243 · 0.0010% | 0.4587 / 0.4583 | 0.6925 · `pause` |
| `night-call` | 601 × 718 · 70.12% | 0.049% | 0 | 13 / 238714 · 0.0054% | 0.3937 / 0.3934 | 0.6703 · `pause` |
| `review-book` | 637 × 718 · 70.12% | 0.049% | 0 | 11 / 363983 · 0.0030% | 0.2600 / 0.2594 | 0.7743 · `pause` |
| `chain` | 718 × 691 · 70.12% | 0.049% | 0 | 6 / 237607 · 0.0025% | 0.3335 / 0.3343 | 0.5688 · `review-book` |
| `pause` | 718 × 712 · 70.12% | 0.000% | 0 | 16 / 314938 · 0.0051% | 0.3535 / 0.3533 | 0.7870 · `seeds` |
| `play` | 718 × 715 · 70.12% | 0.049% | 0 | 34 / 316307 · 0.0107% | 0.3300 / 0.3300 | 0.7870 · `seeds` |
| `sound-on` | 662 × 718 · 70.12% | 0.000% | 0 | 5 / 247825 · 0.0020% | 0.3494 / 0.3495 | 0.6561 · `pause` |
| `sound-off` | 660 × 718 · 70.12% | 0.000% | 0 | 7 / 264069 · 0.0027% | 0.2965 / 0.2960 | 0.6710 · `pause` |
| `close` | 713 × 718 · 70.12% | 0.049% | 0 | 17 / 296085 · 0.0057% | 0.4529 / 0.4536 | 0.6173 · `review-book` |
| `warning` | 718 × 618 · 70.12% | 0.000% | 0 | 34 / 252678 · 0.0135% | 0.3336 / 0.3321 | 0.6835 · `day` |

- Lề: tất cả **68–72%**, lệch tâm tối đa **0,049%**, dưới 2%.
- **48/48 file chọn:** alpha lẻ ngoài mép = **0**. 36 bản thu có **0 pixel sắc khóa**, 12 master có tỷ lệ từ **0 đến 0,0135%**, dưới 0,2%.
- IoU vật khác lớn nhất **0,7870**, dưới 0,80. Không đổi ngưỡng alpha sau khi kiểm; lỗi sát ngưỡng của `seeds` được sửa bằng lề trong giới hạn, giữ nguyên tranh.
- `pause/play`: IoU toàn đĩa **1.0000**, đạt ≥0,90; cùng viền đĩa ngoài.
- `sound-on/sound-off`: IoU **0.9539**, đạt cả ngưỡng riêng 0,85 và mức chặt 0,95.
- ΔY′ nền ngọc nhỏ nhất là sách: **0,2600 / 0,2594**, đạt ≥0,25. Các số nền sáng có đầy đủ trong JSON.

## 6. KA5 · Tự chấm theo mức game thương mại

Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục 0–2. Chấm trên **bộ chọn sau hậu kỳ**, đối chiếu chất liệu và mức hoàn thiện với HUD ảnh mẫu chủ dự án, không chấm theo chuẩn sách tranh cũ. “Dùng tiếp” được 2 sau khi cả 48 file chọn qua kiểm số. Điểm cao của bản gốc không thay điểm ở cỡ 720p.

| Ảnh | Cỡ gốc | Cỡ 720p | Nhận xét ở cỡ nhỏ |
| --- | --- | --- | --- |
| `seeds` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Hạt gạo vẫn tách thành cụm; mất vân vải ở 20 px. |
| `day` | 2/2/2/2/2 = **10** | 2/1/2/1/2 = **8** | Đĩa mặt trời và tia rõ; các khối núi chồng vào nhau ở 20 px. |
| `night` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Lưỡi liềm khác hẳn ngày; sao nhỏ không còn nét khắc ở 20 px. |
| `night-call` | 2/2/1/2/2 = **9** | 2/1/1/2/2 = **8** | Đã có trăng trên mặt chiêng; bộ treo trang trí nhiều hơn các vật còn lại. |
| `review-book` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Sách đỏ và cạnh giấy rõ; dải ngọc chỉ còn một đuôi nhỏ ở 16 px. |
| `chain` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Ba vòng đúng số; điểm sáng khớp nối gộp thành ánh vàng ở 16 px. |
| `pause` | 2/2/2/2/2 = **10** | 2/2/2/2/2 = **10** | Hai thanh sáng và khe tối đọc rõ. |
| `play` | 2/2/2/2/2 = **10** | 2/2/2/2/2 = **10** | Tam giác sáng đọc rõ, cùng đĩa với pause. |
| `sound-on` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Thân chuông và cung vàng còn rõ; nét đồng nhỏ chỉ còn chất liệu. |
| `sound-off` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Vạch ngọc phân biệt được ở 16 px; cung âm được làm tối, giữ dáng cặp. |
| `close` | 2/2/2/2/2 = **10** | 2/2/2/2/2 = **10** | Bốn nhánh chữ thập chéo tách rõ, không cần đọc họa tiết. |
| `warning` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | Tam giác rõ; đinh và chấm nổi rất nhỏ ở 16 px. |

Điểm thấp nhất **8** (`day`, `night-call`) ở cỡ 720p. Đây là **tự chấm Codex**, không phải kết quả nhận của Claude. Claude cần xem file chọn đầy đủ và cỡ thật, nhất là bộ treo chiêng và các chi tiết bị thu nhỏ; chủ dự án xem tờ cuối để quyết mức mỹ thuật.

## 7. Cách chạy lại và khác phiếu

Script dùng Python chuẩn và ImageMagick 7, nằm toàn bộ trong [_review/134/](../../games/typing-defense/art-src/_review/134/). Không cần mạng hay thư viện Python bổ sung. `ART_MAGICK=/opt/homebrew/bin/magick`, font Arial hệ thống đúng phiếu. Các writer tạo mới độc quyền; script sinh/đóng gói không chạy đè lên bộ đang có.

Kiểm lại bản giao không sinh ảnh, không ghi đè: từ repo cha, chọn một tên JSON **chưa tồn tại**:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/134/measure-selected.py \
  games/typing-defense/art-src/ui/icons/134-final recheck-owner-01.json
```

Các bước chính: `prepare.py` chuẩn bị prompt; `process.py` giữ hậu kỳ đầu; `finalize-candidates.py` tách nền/căn lề/sửa mép; `refine-framing.py` chỉnh riêng lề seeds; `package-final.py` tạo bộ chọn và kiểm đủ 48 file; `measure-selected.py` đo master; `sheets-selected.py`, `native-selected.py`, `aligned-compare.py` dựng bằng chứng. `generation-records.json` cùng băm nguồn xác nhận xuất xứ. Các script đời đầu được giữ để giải thích lịch sử, không dùng để thay bộ cuối.

Các khác biệt có chủ đích:

1. Dùng bộ 115 ở `frames-epic/` vì đó là nơi ảnh thực có, cùng key art 113; không tạo mới hay sửa khung.
2. Bộ chọn nằm trong **`ui/icons/134-final/`**, vẫn thuộc thư mục được phép. Đã xuất bộ đầu ở gốc icons trước kiểm alpha toàn bộ bản thu; tôi giữ các file đó, đóng gói bản sửa ở thư mục mới để tuân thủ cấm ghi đè. Bộ đầu có lỗi viền ở một số bản thu; bộ chọn mới qua **48/48** kiểm.
3. Tờ bắt buộc `134-sheet.jpg` và tờ `134-sheet-v2.jpg` được giữ nguyên. Tờ phản ánh bộ giao và đúng màu panel 115 là **`134-sheet-final.jpg`**; mốc băm giao cuối có hậu tố `-final` cùng lý do.
4. Các bản thu vẫn Lanczos trực tiếp từ master; thêm sửa mép sau nội suy vì phép thu làm xuất hiện màu khóa/alpha lẻ. Không làm nét, không đổi phần sơn.

Không làm âm thanh, code, runtime hay gắn `public/` vì ngoài phiếu. Không chạy Git, build, test suite, dev server, trình duyệt hoặc mạng ngoài công cụ tạo ảnh. Không đọc/ghi Tu Tiên, không chạm worktree, game khác hoặc công cụ Audio Lab. Không có capture trình duyệt/render cần dọn.

**Còn lại:** Claude chấm nhận độc lập ≥8 và chọn đúng bộ `134-final/` khi gắn. Không có ảnh nào bị bỏ; chưa tự nhận đã nghiệm thu.
