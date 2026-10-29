# Phiếu 115 · Wordwoven · Khung UI ngọc, đá vôi và vàng lá

Ngày làm: 29/10/2026, tại repo cha trên macOS. Sau phiếu 114.

**Đã tạo đủ 9 ảnh, 10 lượt sinh cùng prompt, 9 bản alpha, 5 JSON 9-slice và toàn bộ tờ kiểm. Chưa hoàn tất việc giao: `plate-long` và `button` đã được xuất bản chọn quá sớm, trước khi kiểm tương phản; hai bản đó trượt. Bản sửa cuối của chúng và `button-active` đã chuẩn bị riêng, qua các ngưỡng kỹ thuật, nhưng chưa thay bản chọn vì phiếu cấm ghi đè file có sẵn. Đã hỏi chủ dự án cho phép sửa đúng các bản vừa tạo; chưa nhận được câu trả lời tại thời điểm viết báo cáo. Chưa có điểm chấm lại của Claude.**

## 1. Nơi giao và trạng thái

- Bộ hiện có: [ui/frames-epic/](../../games/typing-defense/art-src/ui/frames-epic/).
- **Ứng viên sửa cuối, cần duyệt để thay ba bản chọn:** [_review/115/corrected-v2/](../../games/typing-defense/art-src/_review/115/corrected-v2/). Sáu ảnh khác trong thư mục này là bản sao nguyên byte của bộ hiện có.
- [Mock của ứng viên cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-mock.jpg), [tờ cỡ nhỏ](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-small.jpg), [tờ chữ](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-text.jpg).
- Script, ảnh trung gian, số đo và băm: [_review/115/](../../games/typing-defense/art-src/_review/115/).

Không sửa file có trước phiếu; không ghi đè bộ hiện có để tự coi ngoại lệ đã được chấp thuận. Không chạy Git, game, build, test suite, dev server, trình duyệt hay mạng ngoài `image_gen`. Không đọc/ghi Tu Tiên, không ghi game khác. Không làm icon riêng từng ô, runtime hoặc âm thanh vì ngoài phạm vi phiếu. Không có frame chụp trình duyệt mới cần dọn.

Đã đọc chỉ đạo mỹ thuật 28/10, bible Wordwoven, thang Q và README `art-normalize`; đã xem ảnh tham chiếu chủ dự án, sheet HUD hôm nay, màn tựa 113 và ảnh ghép ngày 114. Mock dùng nền màn tựa 113, thu/phóng và cắt giữa về 1920 × 1080.

## 2. Lượt sinh và prompt

Sinh bằng công cụ tích hợp **`image_gen`**. Mọi `.tryN.png` là bản sao nguyên byte từ công cụ, không thay bằng ảnh hậu kỳ. `generation-records.json` ghi đường dẫn nguồn; `published-audit.json` xác nhận SHA-256 của đủ 10 bản thử trùng nguồn công cụ. Không xóa `.try*`.

STYLE-UI, FRAME, SAME và dòng nền M giữ nguyên văn. Bổ sung chung chỉ khóa khổ canvas, một vật thể ở giữa, lề sạch, góc gọn và tiết diện cạnh đều; không thêm chữ vào ảnh. Prompt nguyên văn nằm cạnh từng ảnh thử và bản chọn, bản tổng ở `prompts.json`.

| Tên | Lượt giữ / chọn | Diễn biến và hậu kỳ |
| --- | --- | --- |
| `panel-large` | 1 / try1 | Đá vôi chạm, viền vàng và đồng góc tốt; hoa văn vẫn chạy dọc rail. Lấy tiết diện giữa cạnh, giữ góc, chuẩn hóa bằng công cụ. |
| `plate-long` | 1 / try1 | Đầu mây cuộn và ngọc tối đúng hướng. Hậu kỳ đầu kéo một khe ngọc quá hẹp thành lòng cao, làm vân dọc và tương phản thấp. Ứng viên sửa lấy toàn vùng ngọc sạch, giảm sáng và hòa vào rail. Không cần sinh lại. |
| `button` | 1 / try1 | Nút đá vôi/ngọc cùng bộ; model thêm huy chương mặt trời nhỏ ở góc. Cùng lỗi lấy mẫu lòng như plate; đã sửa bằng công cụ trong ứng viên cuối. |
| `button-active` | 1 / try1 | Đính kèm chính `button.png` đã chọn, có SAME. Bản sinh đổi cỡ hoa văn góc; hậu kỳ lấy ánh vàng của bản active để chiếu lên hình nút gốc. Giữ alpha và đường cắt giống button. Ứng viên cuối kế thừa lòng nút đã sửa. |
| `banner` | 1 / try1 | Dải ngọc đuôi én, hai huy chương mặt trời; model thêm trang trí ở giữa mép trên/dưới. Giữ vì vẫn có khoảng trống cho “Night 1”. |
| `tooltip` | **1, 2 / try2** | Try1 quá nhiều huy chương và mây góc. Try2 thêm chỉ dẫn bốn chốt tròn nhỏ dưới 1% bề rộng, viền vàng dây mảnh, lòng ngọc chiếm ưu thế 94%; giữ chất liệu và bevel. Đúng mức tiết chế hơn. |
| `portrait-ring` | 1 / try1 | Vòng đồng khắc tia mặt trời, bốn mảng ngọc; toàn lòng khóa màu được tách trong suốt. Thêm lề sạch bằng công cụ. |
| `crest` | 1 / try1 | Mặt trời Đông Sơn, cánh mây, đá vôi/ngọc và điểm son nhỏ; thu vào canvas có lề sạch. |
| `divider` | 1 / try1 | Đường vàng, ngọc hình thoi và hai đầu mây; huy chương giữa hơi lớn hơn ý “small” của phiếu. |

Tổng **10 lượt**, tooltip 2 lượt, tám ảnh còn lại 1 lượt. Không cần lượt 3 vì lỗi còn lại sửa được bằng công cụ.

## 3. Hậu kỳ, khổ và 9-slice

Nguồn vuông là **1254 × 1254**, nguồn ngang **2172 × 724**. Tỷ lệ nguồn đã đúng tỷ lệ đích nên phép cắt giữa theo tỷ lệ không bỏ nội dung. Bản thử được giữ nguyên; chỉ bản chọn và alpha được chuẩn hóa.

Tách nền bằng bản sao **nguyên trạng** của `tools/art-normalize/key-alpha.sh`, `common.sh`, `normalize.py`, `seam_analysis.py` tại `_review/115/art-normalize/`. Băm SHA-256 xác nhận bốn bản sao trùng công cụ repo. Cách này giữ WORK mặc định của công cụ nằm trong vùng phiếu cho phép, không viết vào `tools/art-normalize/.tmp/`.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/115/art-normalize/key-alpha.sh \
  IN.try1.png OUT.key.png --bg '#FF00FF' --mode global \
  --despill protect-interior --no-key-hue
```

Bốn ảnh không 9-slice: trim alpha, Lanczos fit trong 94% canvas, đặt giữa trên nền trong suốt. Dạng lệnh thực tế, với W/H lấy theo bảng:

```sh
/opt/homebrew/bin/magick IN.key.png -trim +repage -filter Lanczos \
  -resize '1444x481' -gravity center -background none -extent 1536x512 OUT.png
```

Ảnh vuông dùng fit `963x963`, extent `1024x1024`. Frame 9-slice được trim rồi chia góc nguồn, thu bằng Lanczos về 32 px; tooltip 16 px. Các cạnh lấy tiết diện giữa, giữ góc và ghép với lòng ngọc. Không dùng cách thu cả ảnh khi dựng thử: **ba cỡ bắt buộc và cỡ 320 × 96 đều kéo phần giữa, giữ kích thước góc**.

| Ảnh | Khổ cuối | L / R / T / B | Fill hiện có | Fill ứng viên sửa cuối |
| --- | --- | --- | --- | --- |
| `panel-large` | 1024 × 1024 | 32 / 32 / 32 / 32 | `#061e16` | giữ nguyên |
| `plate-long` | 1536 × 512 | 32 / 32 / 32 / 32 | `#0f231b` | `#081410` |
| `button` | 1536 × 512 | 32 / 32 / 32 / 32 | `#0f261d` | `#09130f` |
| `button-active` | 1536 × 512 | giống button | `#0f261d` | `#09130f` |
| `tooltip` | 1024 × 1024 | 16 / 16 / 16 / 16 | `#062819` | giữ nguyên |
| `banner` | 1536 × 512 | — | — | — |
| `portrait-ring` | 1024 × 1024 | — | — | — |
| `crest` | 1024 × 1024 | — | — | — |
| `divider` | 1536 × 512 | — | — | — |

Fill là trung vị RGB trong lòng. Ánh active lấy trung vị `(243,166,68)` ở viền sáng của bản sinh; lớp sáng đi sâu tối đa 32 px. Alpha button/active trùng nhau, đường cắt trùng nhau. Hai bản không đồng nhất ánh sáng vì đó là thay đổi được yêu cầu.

Sau matte, sửa riêng pixel có sắc khóa còn dư: panel 0, plate 3, button 0, banner 1047, tooltip 0, ring 532, crest 398, divider 267. Đây là đếm sửa màu hậu kỳ, khác với kết quả cuối 0 pixel hue cấm. Xóa các thành phần alpha dưới 20 px do chính hậu kỳ phát sinh; tất cả `.try*` nguyên vẹn. Số thành phần và kích thước từng thành phần đã xóa nằm trong `<tên>.finish.json`.

## 4. KA1 · MD5

Chạy `md5 -r` đệ quy **mọi file** trong `games/typing-defense/art-src/ui/`, trước khi ghi bộ mới và sau khi giao bộ hiện có.

| Mốc | Số file |
| --- | ---: |
| `md5-before.txt` | 104 |
| `md5-after.txt` | 156 |
| Thêm | **52** |
| Sửa file có trước phiếu | **0** |
| Xóa | **0** |
| Dòng `<` trong diff | **0** |

52 file gồm 10 PNG thử + 10 prompt thử + 9 PNG chọn + 9 prompt chọn + 9 alpha + 5 JSON. Diff chỉ thêm dòng. Ứng viên sửa nằm ngoài `ui/`, chưa làm thay đổi các băm sau giao. Hồ sơ: `md5-after.json`, `md5-after.diff.txt`.

## 5. Kiểm số và ảnh kiểm

Tất cả chín bản hiện có **và** ứng viên cuối: đúng khổ, alpha min **0**, max **255**; **0 pixel / 0%** có alpha > 0 và hue 285–330°, S > 0,5; **0 thành phần dưới 20 px**. Vùng 100 × 100 ở giữa vòng chân dung có alpha max **0**. Xem tờ mép 4×: không thấy viền hồng. Vẫn có vài thành phần rời lớn hơn 20 px trong chi tiết banner/ring, đã ghi đầy đủ ở JSON, không giấu bằng cách đổi ngưỡng.

Độ lệch chuẩn luma theo chiều kéo là giá trị tệ nhất của từng hàng/cột trong dải cạnh giữa, chuẩn hóa 0–1. Lòng chữ đo WCAG bằng sRGB tuyến tính, màu chữ `#f3ead2`; dùng **pixel nền sáng nhất trong vùng ghi chữ rộng**, không chỉ lấy trung vị có lợi.

| Ảnh | Std cạnh max hiện có | Std max ứng viên cuối | WCAG tối thiểu hiện có | WCAG tối thiểu ứng viên cuối |
| --- | ---: | ---: | ---: | ---: |
| `panel-large` | 0 | 0 | **9,003** | **9,003** |
| `plate-long` | 0 | **0,02028** | **6,187 · trượt** | **9,768** |
| `button` | 0 | **0,01698** | **3,987 · trượt** | **8,261** |
| `button-active` | 0 | **0,01698** | không bắt buộc đo riêng | lòng giữa giống button |
| `tooltip` | 0 | 0 | **8,944** | **8,944** |

Ngưỡng std ≤ 0,05: đạt. Các rail giữa không có đinh, huy chương hay hoa văn đơn lẻ bị kéo dài. Ứng viên giữ biến thiên vân ngọc nhẹ ở phần bóng trong rail, không biến cả viền thành màu phẳng.

Đã in đủ ba chuỗi “Gold 120 · Rice 40”, “Resume”, “Archer Tower · Level 2” bằng **Arial 24 px**, màu cream, trên cả bốn lòng. Font đúng `/System/Library/Fonts/Supplemental/Arial.ttf`.

Kiểm góc bổ sung: `published-audit.json` và `corrected-audit.json` ban đầu báo false khi so cả RGB ẩn dưới alpha 0; ImageMagick thay các kênh không nhìn thấy đó khi nội suy. Phép kiểm đúng ở **`visible-corner-audit.json`**, so nguyên RGBA nhìn thấy và alpha, chuẩn hóa RGB của pixel alpha 0. Không coi RGB ẩn là biến dạng góc. Giữ cả hồ sơ thô để truy vết.

| Tờ kiểm | Bộ hiện có, tên đúng phiếu | Ứng viên sửa cuối |
| --- | --- | --- |
| Chín bản và ba cỡ 9-slice, rest/active | [115-sheet.jpg](../../games/typing-defense/art-src/_review/115-sheet.jpg) | [tờ sửa cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-sheet.jpg) |
| Mép 4× | [115-edge.jpg](../../games/typing-defense/art-src/_review/115-edge.jpg) | [mép sửa cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-edge.jpg) |
| Chữ 24 px | [115-text.jpg](../../games/typing-defense/art-src/_review/115-text.jpg) | [chữ sửa cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-text.jpg) |
| HUD giả 1920 × 1080 | [115-mock.jpg](../../games/typing-defense/art-src/_review/115-mock.jpg) | [mock sửa cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-mock.jpg) |
| Cùng cao 640 px với ảnh tham chiếu, HUD hôm nay ở dưới | [115-vs-ref.jpg](../../games/typing-defense/art-src/_review/115-vs-ref.jpg) | [so tham chiếu sửa cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-vs-ref.jpg) |
| Ring/crest 64 px và frame 320 × 96 | [115-small.jpg](../../games/typing-defense/art-src/_review/115-small.jpg) | [cỡ nhỏ sửa cuối](../../games/typing-defense/art-src/_review/115/corrected-v2-sheets/115-small.jpg) |

Ở 64 px nhận ra vòng chân dung rỗng với bốn mảng ngọc và huy chương mặt trời có cánh mây; không kỳ vọng đọc từng nét khắc. Ở 320 × 96 nhận ra cả năm khung, phân biệt rest/active và đọc rõ “Resume”.

**So tham chiếu: bộ hiện có “chưa” do vân lòng hai ảnh bị kéo và tương phản thấp; ứng viên sửa cuối “đứng cạnh được” ở mức M = 8.** Chất liệu, bevel, góc đồng/vàng và bảng màu hòa với cảnh sử thi, hơn rõ HUD giấy kem. Chưa đạt M = 9 của ảnh mẫu: độ phong phú của HUD tham chiếu lớn hơn; icon và từng ô nội dung không nằm trong phiếu này.

## 6. KA5 · Điểm tự chấm

Q theo thứ tự: đúng đề / đọc được / hợp bộ / hình khối / dùng được cho bước sau. Điểm ở cỡ sử dụng, không chấm từ ảnh nguồn phóng lớn.

| Ảnh | M hiện có | Q hiện có | M ứng viên cuối | Q ứng viên cuối | Điểm còn thiếu |
| --- | ---: | ---: | ---: | ---: | --- |
| `panel-large` | 8 | 9 = 2/2/2/1/2 | 8 | 9 | Vân mây trong lòng bị đổi tỷ lệ khi kéo sang khung rất thấp. |
| `plate-long` | **7,5** | 8 = 2/1/2/1/2 | **8** | **9 = 2/2/2/1/2** | Bản sửa giữ chất liệu nhưng lòng vẫn biến tỷ lệ ở cỡ vuông. |
| `button` | **7,5** | 8 = 2/1/2/1/2 | **8** | **9 = 2/2/2/1/2** | Như plate; bản hiện có chưa được thay. |
| `button-active` | **7,5** | 8 = 2/1/2/1/2 | **8** | **9 = 2/2/2/1/2** | Giữ chính xác hình nút, ánh vàng rõ; cần thay đồng bộ lòng sửa. |
| `banner` | 8 | 9 = 1/2/2/2/2 | 8 | 9 | Trang trí giữa mép thêm ngoài brief, chiếm ít khoảng trống. |
| `tooltip` | 8 | 9 = 2/2/2/1/2 | 8 | 9 | Vân lòng đổi tỷ lệ nhẹ khi kéo rất dẹt; viền/chốt vẫn rõ. |
| `portrait-ring` | 8 | 9 = 2/2/2/2/1 | 8 | 9 | Còn một thành phần alpha rời 43 px ở bản lớn; không thấy ở 64 px. |
| `crest` | 8,5 | 10 = 2/2/2/2/2 | 8,5 | 10 | Nét khắc nhỏ chỉ đóng vai trò chất liệu ở 64 px. |
| `divider` | 8 | 9 = 1/2/2/2/2 | 8 | 9 | Ngọc hình thoi giữa hơi lớn so với chữ “small”. |

**M chung `115-mock.jpg` hiện có: 7,5. M chung mock ứng viên cuối: 8.** Không báo bộ trong `ui/` đã đạt khi ba bản chọn cần thay còn nằm riêng trong review. Chờ Claude chấm độc lập M/Q sau khi chủ dự án quyết định ngoại lệ ghi đè.

## 7. Script và cách chạy lại

Các script chỉ dùng Python chuẩn và ImageMagick 7, không cài thư viện:

- `key-sources.py`: key từng `.try*`, bỏ qua tên đã có; nhật ký riêng từng ảnh.
- `finish-assets.py`: trim, Lanczos, tạo góc/rail, khử sắc khóa, lọc bụi, PNG/alpha/JSON.
- `finish-active.py`: giữ hình/alpha nút và áp lớp ánh vàng từ ảnh sinh active.
- `render-nine.py`: dựng 9-slice; `verify-and-sheets.py`: đo và dựng các tờ kiểm.
- `prepare-corrections.py`: lấy lại lòng ngọc đủ cao, giảm sáng, chuẩn bị `corrected/` và bộ kiểm v1 riêng; không sửa `ui/`.
- `feather-corrections.py`: hòa vùng ngọc ở góc vào thân, giữ nét vàng/đá, tạo **`corrected-v2/`** và bộ kiểm cuối riêng.
- `audit-delivery.py`, `audit-visible-corners.py`: SHA-256 nguồn, góc giữ nguyên, alpha active, bản sao công cụ.
- `md5-audit.py`: băm toàn UI và diff với trước phiếu.

Chạy kiểm ứng viên cuối vào tên thư mục mới, không sinh ảnh lại, không ghi đè hồ sơ:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/115/recheck-v2.py recheck-owner-01
```

Số đo hiện có ở `metrics.json`; số cuối ứng viên ở **`corrected-v2-review/metrics.json`**. `corrected/`, `corrected-review/`, `corrected-sheets/` là ứng viên sửa trước khi hòa mượt góc, được giữ để truy vết, không phải bản cuối.

## 8. Còn lại và lý do

Tôi đã xuất các bản chọn đầu trước khi hoàn thành đo tương phản. Đây là lỗi quy trình của tôi; không phải do giới hạn công cụ hay thiếu ảnh tham chiếu. Đã chuẩn bị đầy đủ bản sửa và bằng chứng để duyệt, nhưng **chưa thay 9 file PNG/alpha/JSON của `plate-long`, `button`, `button-active`** vì lệnh “cấm ghi đè … file có sẵn” của phiếu. Mọi bản thử và file có trước phiếu vẫn nguyên vẹn.

Sau khi được phép thay các file do chính phiếu này vừa tạo: lưu bản trước sửa trong review, thay đồng bộ ba bộ, tạo bộ ảnh kiểm cuối mới từ đúng bản giao, cập nhật băm sau giao và báo cáo. Nếu không được phép, giữ nguyên tất cả và chủ dự án có thể lấy ba bộ đạt chuẩn từ `corrected-v2/` để xử lý tiếp. Không coi sự im lặng là cho phép. Chưa hoàn tất điều kiện “xong khi” và chưa nghiệm thu Claude.
