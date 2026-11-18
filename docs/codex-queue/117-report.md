# Phiếu 117 · Wordwoven · Cây thấp, cỏ và hoa v3, v4

Ngày giao: 29/10/2026. **Đã giao 10 bản chọn, qua kiểm số 2–7; tự chấm M ≥ 8, Q ≥ 8. Chờ Claude chấm nhận.**

## 1. Bản giao và ảnh kiểm

Thư mục ảnh: `games/typing-defense/art-src/scenery/meadow/`. Năm id `fern`, `reed-clump`, `tall-grass`, `wildflowers`, `raspberry-bush`, mỗi id có `-v3.png`, `-v4.png` và prompt cùng tên. `raspberry-bush` giữ id nhưng vật là cây sim. Không có ảnh nào của phiếu này ở `shared/`.

- [Tờ v1 | v2 | v3 | v4](../../games/typing-defense/art-src/_review/117-sheet.jpg): mỗi cây cao 256 px, nền `#3f5a48`.
- [Tờ 128 px](../../games/typing-defense/art-src/_review/117-small.jpg): cạnh dài của khung ảnh là 128 px, không phóng riêng vật để chấm.
- [Tờ trong cảnh, 1536 × 1024](../../games/typing-defense/art-src/_review/117-mock.jpg).
- [So với ảnh chủ dự án, hai bên cùng cao 640 px](../../games/typing-defense/art-src/_review/117-vs-ref.jpg).
- Mỗi bản có tờ `_review/117-before-after-<id>-v3.jpg` hoặc `-v4.jpg`, nhãn **Bản sinh | Bản hậu kỳ**, hai ô cùng cỡ; liên kết từng tờ ở bảng điểm phía dưới.

Đã dùng skill `imagegen` và công cụ tạo ảnh tích hợp của Codex. Lúc tiếp tục đã có 11 ảnh thô và các script nháp của phiếu; giữ nguyên, đối chiếu ảnh thô với nguồn tạo ảnh bằng SHA-256. Lượt này sinh thêm hai ảnh sim. Tổng cộng **13 lượt sinh cho 10 bản**, nhiều nhất hai lượt một bản; không dùng lượt 3. Mọi `.tryN.png` và `.tryN.prompt.txt` còn nguyên. `sources-audit-final.json` lưu nguồn và hash của cả 13 ảnh thô.

## 2. Prompt, từng lượt và lựa chọn

Mọi prompt giữ nguyên STYLE + MAP + SCENERY của phiếu, rồi phần riêng, chỉ dẫn biến thể/khổ/lề, cuối cùng dòng nền nguyên văn §3.8. Phần bổ sung chung yêu cầu khối lá trưởng thành, gân và chất liệu có thể tích, bóng ngọc lạnh, mặt trên vàng dịu; mô tả thế giới chỉ là chỉ đạo phong cách, ảnh chỉ có một cây trên nền khóa.

| Bản | Lượt 1 và khác biệt đã yêu cầu | Lượt 2, lý do và bản chọn |
|---|---|---|
| fern-v3 | Dương xỉ cao, lá vươn lên phải, ngọn cao khoảng 70% ngang khung, búp cuộn tối ở tâm | Không sinh thêm; chọn 1 |
| fern-v4 | Thấp rộng, nhiều tầng lá xòe sao, búp cuộn ở tâm | Không sinh thêm; chọn 1 |
| reed-clump-v3 | Lau cao, các bông bạc nghiêng trái, lá gom từ một chân | Không sinh thêm; chọn 1 |
| reed-clump-v4 | Dày hơn, bông dựng, có thân gãy ngắn ở phía trước | Không sinh thêm; chọn 1; chiều cao thấp hơn v3 được đặt theo mét trong tờ cảnh |
| tall-grass-v3 | Cỏ voi cao, phiến rộng đổ phải, gốc ngọc và đầu lá vàng | Không sinh thêm; chọn 1 |
| tall-grass-v4 | Bụi đầy, thấp rộng hơn, phiến lá xòe cả hai phía | Không sinh thêm; chọn 1 |
| wildflowers-v3 | Hoa vàng hai tầng nhưng nhụy quá lớn, giống hướng dương vườn | Lượt 2 nêu rõ Tithonia diversifolia/dã quỳ, nhụy nhỏ khoảng 1/5 hoa, một vòng cánh dài không đều, lá ba thùy sâu, thân phân nhánh; chọn 2 |
| wildflowers-v4 | Khóm ly trắng nhụy vàng, thấp rộng, lá dài ngọc | Không sinh thêm; chọn 1 |
| raspberry-bush-v3 | Sim dạng vòm, quả tím nặng phía trái, hoa hồng phía phải | Lượt 2 thêm quả tím thiên đỏ burgundy, bóng mận tối, phản sáng bạc-vàng trung tính, lá ngọc/ô liu độc lập với nền lam; chọn 2 |
| raspberry-bush-v4 | Hai khối lệch nhau, trái cao hơn, nhiều hoa hơn quả | Lượt 2 sửa màu như v3, nhưng ngọn cao nhất gần v3 quá; giữ lượt 2 làm đối chứng, chọn lại 1 sau khi tách nền an toàn |

Prompt chọn được chép nguyên từ prompt của lượt chọn; không sửa prompt sau khi sinh. Dương xỉ và cỏ voi đầu ra thô là 1254 × 1254 dù prompt xin 1536; bản giao giữ khổ 1254 để tránh phóng lớn không cần thiết, đúng yêu cầu cạnh ≥ 1254. Lau 1024 × 1536; hoa và sim 1536 × 1024.

## 3. Hậu kỳ giữ tranh, theo ART_ACCEPTANCE §5

Script cuối: `_review/117/process-resume3.mjs`; dữ liệu xử lý: `delivery-resume3/processing.json`.

Tách các pixel nền gần màu khóa (lệch kênh lớn nhất ≤ 60), rồi lan trong miền màu khóa nối tới chúng: hue cách khóa ≤ 20°, S > 0,5 hoặc khoảng cách kênh ≤ 60. Cách này nhận cả lỗ nền giữa các lá, giữ phản sáng tím nằm trong quả và các mặt lá. Chỉ cắt lề rỗng, đổi cỡ đồng tỷ lệ, làm gọn alpha ở mép sau đổi cỡ và thêm lề. Chân đặt cách đáy khoảng 6%. RGB của phần cây giữ nguyên trước nội suy đổi cỡ; không đổi sáng/màu, không phủ mảng, không xóa lá, hoa, quả hay thân để đạt số.

Bản nháp dùng hạt nền lệch ≤ 12 bỏ sót một số khe lam; v3/v4 sim lượt 2 đo 0,626%/1,292%. Mở hạt tới ≤ 60 theo định nghĩa nền của phiếu sửa đúng khe nền, cho 0,301%/0,392%; không quét xóa toàn bộ pixel tím/lam trong vật. Với sim v4 lượt 1, cách này cho 0,256% và dáng khác v3 rõ hơn, nên đó là bản giao. Các ứng viên và phép đo nháp vẫn nằm trong thư mục phiếu, không phải bản tích hợp.

Không gặp trường hợp phải phá tranh để đạt ngưỡng ở bộ chọn cuối. Không ép luma mép hoặc san hình để qua kiểm. Đã xem ảnh hậu kỳ cỡ đầy đủ, bản tách trên nền khác và tờ 128 px trước khi chấm.

## 4. Số đo trên đúng bản giao

`magick identify` lưu nguyên kết quả ở `_review/117/final-identify.txt`; số đo đầy đủ ở `metrics-final.json`. Mép 10 px cả bốn phía có độ lệch kênh tối đa **0/255 ở cả 10 ảnh**. Nền M = `#FF00FF`; B = `#0000FF`.

Hộp bao dùng mask tương đương tách nền: pixel thuộc vật khi lệch màu khóa > 60 ở ít nhất một kênh; ghi `(x, y, rộng, cao)`, tọa độ từ 0. Đếm vùng theo liên thông 8 láng giềng. Luma Rec.709 trên RGB sRGB chuẩn hóa 0–1; dải mép là mask trừ phần co vào 3 px (cửa sổ 7 × 7). Hue kiểm trong ±12° và S > 0,5; tỷ lệ tính trên pixel vật.

| Ảnh | Khổ | Nền | Lẫn màu khóa % | Hộp bao | Lề trái/phải/trên/đáy % | Vùng > 1% |
|---|---|---|---:|---|---|---:|
| fern-v3 | 1254 × 1254 | M | 0.1197 | (129, 76, 996, 1103) | 10.29/10.29/6.06/5.98 | 1 |
| fern-v4 | 1254 × 1254 | M | 0.0293 | (63, 433, 1128, 746) | 5.02/5.02/34.53/5.98 | 1 |
| reed-clump-v3 | 1024 × 1536 | M | 0.0143 | (61, 93, 901, 1351) | 5.96/6.05/6.05/5.99 | 1 |
| reed-clump-v4 | 1024 × 1536 | M | 0.0154 | (67, 93, 890, 1351) | 6.54/6.54/6.05/5.99 | 1 |
| tall-grass-v3 | 1254 × 1254 | M | 0.0015 | (86, 76, 1081, 1103) | 6.86/6.94/6.06/5.98 | 1 |
| tall-grass-v4 | 1254 × 1254 | M | 0.0103 | (63, 259, 1128, 920) | 5.02/5.02/20.65/5.98 | 1 |
| wildflowers-v3 | 1536 × 1024 | M | 0.0080 | (321, 62, 893, 901) | 20.90/20.96/6.05/5.96 | 1 |
| wildflowers-v4 | 1536 × 1024 | M | 0.0170 | (77, 183, 1382, 780) | 5.01/5.01/17.87/5.96 | 1 |
| raspberry-bush-v3 | 1536 × 1024 | B | 0.3008 | (109, 62, 1317, 901) | 7.10/7.16/6.05/5.96 | 1 |
| raspberry-bush-v4 | 1536 × 1024 | B | 0.2564 | (77, 108, 1382, 855) | 5.01/5.01/10.55/5.96 | 1 |

Tất cả qua kiểm khổ, mép nền, tỷ lệ lẫn màu ≤ 0,5%, đáy ≤ 12%, lề trái/phải/trên ≥ 3% và đúng một vùng lớn.

| Ảnh | Luma trung vị vật | Luma trung vị mép 3 px | Mép/vật, cần ≥ 0,6 |
|---|---:|---:|---:|
| fern-v3 | 0.3450 | 0.3977 | 1.153 |
| fern-v4 | 0.3846 | 0.3891 | 1.012 |
| reed-clump-v3 | 0.5715 | 0.6493 | 1.136 |
| reed-clump-v4 | 0.5919 | 0.6464 | 1.092 |
| tall-grass-v3 | 0.4645 | 0.6135 | 1.321 |
| tall-grass-v4 | 0.4560 | 0.5831 | 1.279 |
| wildflowers-v3 | 0.4224 | 0.4484 | 1.062 |
| wildflowers-v4 | 0.5160 | 0.4932 | 0.956 |
| raspberry-bush-v3 | 0.2336 | 0.3156 | 1.351 |
| raspberry-bush-v4 | 0.3015 | 0.3160 | 1.048 |

| Cặp | Rộng/cao v3 → v4 | Lệch tỷ lệ tương đối | Cột ngọn cao nhất v3 → v4 (% khung) | Lệch (% bề rộng khung) | Qua bằng |
|---|---|---:|---|---:|---|
| fern | 0.903 → 1.512 | 67.45% | 69.89 → 47.74 | 22.14 | tỷ lệ |
| reed-clump | 0.667 → 0.659 | 1.24% | 22.41 → 53.08 | 30.67 | cột ngọn |
| tall-grass | 0.980 → 1.226 | 25.10% | 68.71 → 54.39 | 14.32 | tỷ lệ |
| wildflowers | 0.991 → 1.772 | 78.77% | 42.44 → 70.80 | 28.36 | tỷ lệ |
| raspberry-bush | 1.462 → 1.616 | 10.58% | 38.83 → 19.20 | 19.63 | cột ngọn |

Cột ngọn là trung bình vị trí các pixel trong ba hàng cao nhất, chuẩn hóa theo bề rộng ảnh. Dùng ngưỡng lệch cột ít nhất 15% **bề rộng khung**, chặt hơn cách tính tương đối trên vị trí ngọn. Cả năm cặp qua.

## 5. KA5: tự chấm bản hậu kỳ

M của cảnh vật xét trong tờ cảnh theo ART_DIRECTION §1.4, đối chiếu độ hoàn thiện ở ảnh đầy đủ và khả năng giữ khối ở 128 px. Điểm dưới đây là tự chấm, không thay kết quả Claude. Q theo năm mục: đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau, mỗi mục 0–2. Q = 9 dùng dãy 2/2/2/2/1: đạt quy cách nhưng mép còn ít pixel khóa cần giữ thận trọng khi tách tích hợp; Q = 10 dùng 2/2/2/2/2.

| Bản | M đầy đủ | Q đầy đủ | M 128 px | Q 128 px | Đọc ở 128 px, nét tốt và chỗ còn thiếu | Tờ trước–sau |
|---|---:|---:|---:|---:|---|---|
| fern-v3 | 8.3 | 9 | 8.1 | 9 | Nhận ra dương xỉ, búp cuộn và lá vươn phải; gân lá và mặt dưới ngọc có chiều sâu, chi tiết lá con mờ đi khi thu nhỏ. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-fern-v3.jpg) |
| fern-v4 | 8.4 | 9 | 8.2 | 9 | Nhận ra dương xỉ xòe thấp, tâm cuộn rõ; khối tầng mạnh, còn vài điểm màu khóa nhỏ ở khe lá. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-fern-v4.jpg) |
| reed-clump-v3 | 8.2 | 9 | 8.2 | 9 | Nhận ra lau bạc nghiêng trái; bông sáng gom tốt, sợi nhỏ hợp lại khi thu nhỏ. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-reed-clump-v3.jpg) |
| reed-clump-v4 | 8.2 | 9 | 8.2 | 9 | Nhận ra lau dày dựng thẳng; thân gãy đọc được ở ảnh đầy đủ, không còn rõ ở 128 px. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-reed-clump-v4.jpg) |
| tall-grass-v3 | 8.0 | 9 | 8.0 | 9 | Nhận ra cỏ phiến rộng đổ phải; mặt lá có chất liệu, đầu vàng hơi nhiều so với bụi cỏ thật. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-tall-grass-v3.jpg) |
| tall-grass-v4 | 8.0 | 9 | 8.0 | 9 | Nhận ra bụi cỏ đầy xòe hai phía; khối lớn rõ, đầu vàng chiếm diện tích khá lớn. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-tall-grass-v4.jpg) |
| wildflowers-v3 | 8.1 | 9 | 8.1 | 9 | Nhận ra khóm hoa vàng cao hai tầng; dã quỳ đúng hơn lượt 1, gân lá mất ở cỡ nhỏ. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-wildflowers-v3.jpg) |
| wildflowers-v4 | 8.3 | 10 | 8.1 | 10 | Nhận ra ly trắng tâm vàng ngay ở 128 px; cánh có thể tích, vài bông vẫn khá đều nhau. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-wildflowers-v4.jpg) |
| raspberry-bush-v3 | 8.1 | 9 | 8.0 | 9 | Nhận ra bụi sim hoa hồng, quả tối bên trái; phản sáng quả hơi bóng, vài mặt lá còn ngả lam trong ngưỡng. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-raspberry-bush-v3.jpg) |
| raspberry-bush-v4 | 8.2 | 9 | 8.0 | 9 | Nhận ra sim hai khối lệch, hoa nhiều hơn quả; cánh và gân lá hoàn thiện, quả tím mất chi tiết khi nhỏ. | [Xem](../../games/typing-defense/art-src/_review/117-before-after-raspberry-bush-v4.jpg) |

**M chung `117-mock.jpg`: 8,0/10. Đứng cạnh được**: lớp cây thấp có chất liệu, khối và bóng ngọc–vàng cùng bộ 116, trước tháp đá/thác/rùa trời của 114 cho cảm giác cảnh sử thi, không còn viền mực và dáng đồ chơi như v1/v2. Chưa ngang mức 9 của ảnh chủ dự án: mặt nước ghép còn mềm, chưa có ánh sáng và bóng tiếp xúc runtime; phần lính làm thước kế thừa chất lượng cũ. Điểm 8 chỉ là tờ kiểm mỹ thuật của bộ cây, chưa xác nhận cảnh game thực.

Tờ cảnh dùng `116-mock.jpg` làm lớp sau; đất cỏ lấy từ `scenery/meadow/ground-v2/grass-jade.png` của 122; nước cắt từ phần sông đã vẽ trong `backdrops/w1-silverfall-epic/layer-140-b.png` của 114. Mã chỉ đặt lớp/mặt nạ kiểm, không vẽ cây, đá hay lính thay tranh. Không sửa các nguồn này. `scene-final2/layout.json` ghi tất cả vị trí, kích thước và nguồn.

Cỡ dùng trong cảnh: dương xỉ 1,5–2,3 m; lau 2,2–3 m; cỏ voi 1,7–2,5 m; hoa 0,6–1 m; sim 1,2–1,8 m. Thước tiền cảnh `units/linh-giao.png` cao 1,8 m = 94 px, cùng tỷ lệ 52 px/m với cây. Lính nhỏ có sẵn trong 116 giữ nguyên ở lớp sau. Tờ ghép tĩnh không xác lập phối cảnh camera runtime 55°/58 m.

## 6. KA1 và cách chạy lại

- `md5-before.txt`: 234 file trước → 405 file sau; **+171, đổi/mất 0**.
- `md5-before-resume.txt`: 381 file trước → 405 file sau; **+24, đổi/mất 0**.

`md5-before.txt` là mốc cũ có sẵn trước các lượt sinh đầu, được giữ nguyên. `md5-before-resume.txt` được lập trước lần ghi đầu của lượt tiếp tục. So mốc tiếp tục, đúng 24 file thêm trong scenery: hai ảnh sim lượt 2 + hai prompt, mười bản chọn + mười prompt. So mốc cũ có thêm các file đã xuất hiện trước lúc tiếp tục; không gán tất cả cho phiếu này. Hai `diff` chỉ có dòng thêm, không có dòng `<` của file đổi/mất.

Snapshot dùng `/sbin/md5 -r <từng file>` đệ quy, sắp theo đường dẫn. `deliver-final2.py` thực hiện lệnh này và `diff`; lưu `md5-after.txt`, `md5-diff.txt`, `md5-diff-resume.txt`, `audit-delivery.json`. SHA-256 xác nhận bản chọn giống hệt ứng viên đã đo và prompt giống lượt được chọn. Không chạy lệnh Git nào.

Các script cuối ở `games/typing-defense/art-src/_review/117/`:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/117/process-resume3.mjs replay-processing
node games/typing-defense/art-src/_review/117/review-final.mjs replay-visual
node games/typing-defense/art-src/_review/117/mock-final2.mjs replay-scene
```

`measure.mjs <json-mới> <các-thư-mục-ứng-viên>` đo lại bằng RGB đọc từ ImageMagick. `process-resume3.mjs` mặc định tạo `delivery-resume3`; script tờ kiểm dùng bộ này cố định. Khi chạy lại, dùng tên thư mục đầu ra chưa tồn tại như ví dụ để giữ luật không ghi đè. `deliver-final2.py` và `finalize-report.py` cố ý từ chối ghi đè bản giao/báo cáo đã có. Font tờ kiểm: `/System/Library/Fonts/Supplemental/Arial.ttf`. Giữ cả script/dữ liệu nháp để truy nguyên, không xóa file có sẵn.

## 7. Khác phiếu, bỏ qua và việc cần duyệt

- Tiếp tục từ các ảnh thô đã có, thay vì sinh lại cả mười ảnh; xác minh nguồn trước khi dùng. Không ghi đè bất kỳ file có sẵn, kể cả script và baseline MD5.
- Dùng khổ vuông 1254 thay vì 1536 xin trong prompt vì công cụ trả 1254 và phiếu cho phép; không giảm dưới sàn.
- Bổ sung tranh cỏ 122 và mảnh nước 114 vào tờ kiểm trước 116 để có bờ suối; chỉ ghi sản phẩm ghép trong `_review/117/` và các JPG 117 cho phép.
- Không tích hợp game, không tắt viền trong `prepare-scenery`, không chuyển v1/v2 hay xóa ảnh cũ; đây là bước Claude làm sau khi nhận. Không chạy build, test, server hay trình duyệt; không có ảnh chụp runtime và không khẳng định đã kiểm camera thật.
- Không tạo âm thanh; không đọc/ghi Tu Tiên hay game khác, không sửa tài liệu ngoài báo cáo này. Không ghi `ART_REPLACE_LATER.md` vì ngoài phạm vi cho phép; các điểm còn thiếu đã ghi ngay ở bảng trên.

**Claude cần xem** ảnh chọn đầy đủ và 128 px, mười tờ trước–sau, nhất là mép lá sim và dương xỉ, rồi chấm lại M/Q. Khi tích hợp bộ v3/v4, tắt viền mực theo phiếu và kiểm cỡ mét trên sân thật. Chủ dự án có thể bắt đầu từ `117-sheet.jpg` và `117-mock.jpg`.
