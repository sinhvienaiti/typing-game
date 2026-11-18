# Phiếu 122 · Wordwoven · Ô đất v2 và vách đá vôi

Ngày kiểm và hoàn tất hồ sơ: 29/10/2026, Mac mini M4.

**Kết quả: CHƯA ĐẠT.** Tám PNG chọn có đủ ảnh và prompt; năm ô qua toàn bộ kiểm số 2–6. Hai ô cỏ trượt độ rối, cỏ chính trượt thêm đốm lặp, bờ suối trượt đốm lặp. Tự chấm mức chợ trên mock hậu kỳ **M = 7,5/10**, dưới mức nhận 8. Không coi bộ này là tài sản đã được duyệt.

Phiên này tiếp nối **bộ có sẵn**: khi bắt đầu đọc thư mục, đã có tám PNG chọn, 21 ảnh `.tryN`, 21 prompt lượt sinh, tám prompt chọn, các bản xử lý và số đo. Chưa có báo cáo hoặc bảng kiểm của phiếu. Vì cấm ghi đè và tối đa ba lượt mỗi ảnh, phiên này **không gọi thêm `image_gen`**, không sửa bất kỳ PNG/prompt có sẵn nào; hoàn tất kiểm độc lập, ảnh đối chiếu và báo cáo. Hồ sơ hiện có không đủ nhật ký request để xác minh lại công cụ sinh hoặc ảnh thực sự đính kèm của từng lượt; các mô tả sửa prompt dưới đây được đối chiếu từ chính các file prompt đang lưu, không phải nhật ký gọi công cụ mới.

## 1. Bộ chọn và tờ trước–sau

Thư mục tài sản: `games/typing-defense/art-src/scenery/meadow/ground-v2/`. Giữ nguyên 58 file: 21 cặp ảnh/prompt lượt sinh và tám cặp ảnh/prompt chọn. Không xóa lượt không chọn.

| Ô | Lượt đã có / lượt chọn | PNG chọn | Prompt chọn | Bản sinh và bản hậu kỳ cùng cỡ |
| --- | --- | --- | --- | --- |
| `grass-jade` | 3 / **2** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/grass-jade.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/grass-jade.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/grass-jade-before-after.jpg) |
| `grass-moss` | 3 / **3** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/grass-moss.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/grass-moss.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/grass-moss-before-after.jpg) |
| `road-paved` | 2 / **2** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/road-paved.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/road-paved.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/road-paved-before-after.jpg) |
| `trail-worn` | 3 / **3** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/trail-worn.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/trail-worn.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/trail-worn-before-after.jpg) |
| `stream-bank` | 3 / **3** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/stream-bank.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/stream-bank.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/stream-bank-before-after.jpg) |
| `courtyard` | 1 / **1** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/courtyard.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/courtyard.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/courtyard-before-after.jpg) |
| `cliff-face` | 3 / **3** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/cliff-face.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/cliff-face.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/cliff-face-before-after.jpg) |
| `cliff-moss` | 3 / **2** | [PNG](../../games/typing-defense/art-src/scenery/meadow/ground-v2/cliff-moss.png) | [prompt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/cliff-moss.prompt.txt) | [tờ so](../../games/typing-defense/art-src/_review/122/cliff-moss-before-after.jpg) |

Mọi lượt đã có giữ đúng tên `<tên>.tryN.png` và `<tên>.tryN.prompt.txt`. Prompt chọn trùng byte với prompt lượt chọn ở cả tám ô. Các prompt bắt đầu bằng STYLE + MAP + GROUND/CLIFF theo phiếu. Prompt `grass-moss` và `cliff-moss` có câu yêu cầu chỉ dùng ảnh đính kèm để khớp phong cách, màu và thang.

Mỗi tờ trước–sau rộng **2048 × 1060**: hai ảnh cùng cỡ 1024 × 1024, nhãn nằm ở dải riêng 36 px. Bên trái là lượt sinh chọn; bên phải là PNG hậu kỳ hiện có. Không lấy bản sinh đẹp hơn để chấm thay bản giao.

## 2. Prompt được sửa qua từng lượt

Các đoạn sửa là phần thêm sau khối bắt buộc; toàn văn chính xác ở các `.tryN.prompt.txt` cạnh ảnh.

| Ô | Lượt 1 | Lượt 2 | Lượt 3 và lý do chọn |
| --- | --- | --- | --- |
| `grass-jade` | Cỏ ngọc dịu, cụm 20–50 cm, sắc sage và rơm khô phân đều; sau vá độ rối 0,070316, đốm 0,105819 | Đẩy cụm lên 40–90 cm, nét tối thiểu 20 cm, chuyển màu mềm, chia sáng đều bốn góc | Thử 12–20 khối turf lớn, nét mềm như suede; độ rối 0,058442, đốm 0,163737, kém lượt 2. **Giữ lượt 2**, vẫn trượt số |
| `grass-moss` | Khớp màu cỏ chính, rêu và ba lá 20–50 cm; S 0,619048 và nền quá tối | Turf rêu cắt sát, màu sage có xám, chỉ tối hơn cỏ chính 3%; S vẫn 0,612613 | Rêu nhung xám ngọc, nét 25–50 cm, RGB gợi ý 78/107/78, S mục tiêu 25–35%. **Chọn lượt 3**: S 0,459016, đốm đạt; độ rối còn trượt |
| `road-paved` | Đá vôi cũ 1–2 m, kem và xám ấm, khe rêu mỏng; độ rối 0,048858, đốm 0,159413 | Nhấn mạnh albedo, khối khoáng rộng, khoảng 6–8 phiến theo bề ngang, nét ≥ 20 cm, viên chạy dọc. Sau vá và hạ sáng toàn ảnh 10%: mọi số đạt | Không có lượt 3; giữ lượt 2 |
| `trail-worn` | Đất xám buff, vụn vôi 20–60 cm, turf sage; độ rối 0,064274 | Đất liên tục, ít mảnh đá lớn, mảng khoảng 1 m, nét ≥ 20 cm; độ rối 0,059786, đốm 0,171878 | Khối khoáng 30–100 cm, chuyển mềm trong mảng, ba vật liệu gần sáng nhau. **Chọn lượt 3**, vá mép và hạ sáng toàn ảnh 10%; vừa qua ngưỡng rối |
| `stream-bank` | Cuội 25–80 cm trong bùn xám, ánh ướt tiết chế; độ rối 0,055635 | Đá phẳng chìm trong bùn, viên 40–80 cm, nét ≥ 20 cm, tương phản vật liệu nhỏ; độ rối 0,037337, đốm 0,139083 | Khối đá tròn rộng, nét ≥ 25 cm, than xám và bạc gần sáng nhau. **Chọn lượt 3** vì độ rối 0,029027; đốm 0,133576 vẫn trượt |
| `courtyard` | Đá lát vuông lớn, màu kem ấm, khe tối mảnh, vài vết nứt | Không có | Không có; chọn lượt 1. Roll 128/128 trước vá để tránh đặt khe đá thật đúng đường đo tâm |
| `cliff-face` | Gân vôi 1–3 m, trắng phấn và bạc xám; đốm 0,339091 | Nhấn albedo, màu khoáng bạc thay bóng lõm quá tối, gân 0,5–1 m; đốm 0,212035 | Khoảng 24 rãnh rộng 0,5 m, từng ô 1,5 m có lượng trắng/xám cân bằng. **Chọn lượt 3**, vá mép và hạ sáng 9%; mọi số đạt |
| `cliff-moss` | Khớp vách chính, rêu ngọc và dây leo áp vào gân, mảng rộng; đốm 0,144794 | Khớp gân 0,5 m, rêu xám ngọc như nỉ, chia đều đá/rêu trong vùng 1,5 m | Thử gân 1 m, rêu nhẵn hơn, nét ≥ 30 cm; đốm 0,186876, kém lượt 2. **Giữ lượt 2**, vá mép và hạ sáng 8%; mọi số đạt |

Số ở bảng prompt là số sau vá của mỗi lượt trước chỉnh sáng, trừ chỗ ghi rõ sau chỉnh sáng. Không so điểm theo bộ 095: bộ cũ chỉ dùng đối chiếu cách đo và lỗi màu.

## 3. Hậu kỳ và giới hạn §5

Tính lại chuỗi xử lý đang lưu từ ảnh sinh đến PNG chọn, giải mã RGB 8 bit và đối chiếu **trùng từng pixel ở cả tám ô**:

1. Giải mã/chuẩn hóa về 1024 × 1024, sRGB, RGB, 8 bit.
2. Riêng sân: dịch vòng +128 px cả hai trục, giữ nguyên mọi pixel nguồn.
3. Làm liền tuần tự X rồi Y như phiếu 093: mỗi trục roll nửa ô 512 px, dải giữa giữ nguồn với `core = 8 px`, chuyển bằng cosin trong `fade = 48 px` hai phía. Không giảm tương phản hay lọc mờ toàn ảnh.
4. Chỉnh sáng toàn ảnh: đường và đất chuyển tiếp ×0,90; vách trắng ×0,91; vách rêu ×0,92. Các ô khác ×1,00. Không dịch hue, không giảm S, không phủ màu hoặc san mảng thấp tần.

Vá mép làm vài cụm cỏ, đường vân hoặc phiến đá pha mềm ở vùng chữ thập; phần này được chỉ ra khi chấm. Tờ trước–sau giữ đủ phần vẽ để Claude xem mức pha này có chấp nhận được không.

**Mâu thuẫn cần giữ lại:** muốn kéo hai ô cỏ xuống độ rối 0,035 bằng nén tương phản/lọc mờ sẽ xóa nhiều nét lá đã vẽ. Bờ suối cần giảm mảng sáng tối hơn nữa để qua đốm 0,12; không làm phẳng khoáng và ánh ướt để đạt số. Theo ART_ACCEPTANCE §5, dừng chỉnh các ô này, giữ tranh và ghi rõ trượt; không lặp cách san mảng của 095. Các ô đều đã có đủ ba lượt nên không sinh lượt 4.

## 4. KA1 và định dạng

Snapshot bằng `/sbin/md5 -r` trên **mọi file** dưới `games/typing-defense/art-src/scenery/`, sắp đường dẫn. Giữ mốc `md5-before.txt` cũ; bổ sung `md5-audit-before.txt` trước lần ghi đầu tiên của phiên kiểm này.

| Mốc so | Trước | Sau | Đổi nội dung | Mất | Thêm |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mốc trước tài sản của phiếu → sau giao hồ sơ | 264 | 322 | **0** | **0** | **58** |
| Mốc bắt đầu phiên kiểm này → sau giao hồ sơ | 322 | 322 | **0** | **0** | **0** |

58 dòng thêm đều thuộc `meadow/ground-v2/`. `diff -U 0` có **0 dòng nội dung bị bỏ**, chỉ thêm dòng; không tính dòng tiêu đề diff. Bộ 095 và mọi file scenery đã có ở mốc đầu giữ nguyên.

Bằng chứng: [md5 trước](../../games/typing-defense/art-src/_review/122/md5-before.txt), [md5 trước phiên kiểm](../../games/typing-defense/art-src/_review/122/md5-audit-before.txt), [md5 sau](../../games/typing-defense/art-src/_review/122/md5-after.txt), [diff](../../games/typing-defense/art-src/_review/122/md5-diff.txt), [đối chiếu](../../games/typing-defense/art-src/_review/122/md5-verification.json).

`magick identify` kiểm lại: **8/8 PNG chọn = 1024 × 1024, sRGB, RGB ba kênh, 8 bit, không alpha**. [Đầu ra identify](../../games/typing-defense/art-src/_review/122/identify-audit.txt).

## 5. Mép liền và chữ thập

`L = 0,2126R + 0,7152G + 0,0722B` trên sRGB mã hóa 0–1, không tuyến tính hóa. `E` là trung bình hai độ lệch mép X/Y; `I` là trung bình hai độ lệch pixel kề bên trong X/Y. “Trước” là ảnh sinh lượt chọn giải mã ở 1024, trước mọi hậu kỳ; “sau” là PNG chọn giải mã lại.

| Ô | E trước | I trước | E/I trước | E sau | I sau | E/I sau ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `grass-jade` | 0.074249 | 0.057272 | 1.296441 | 0.061962 | 0.056147 | **1.103568** |
| `grass-moss` | 0.077869 | 0.055290 | 1.408376 | 0.054029 | 0.054321 | **0.994623** |
| `road-paved` | 0.061906 | 0.043939 | 1.408914 | 0.034250 | 0.037840 | **0.905145** |
| `trail-worn` | 0.071179 | 0.058274 | 1.221446 | 0.050542 | 0.051203 | **0.987103** |
| `stream-bank` | 0.048031 | 0.032455 | 1.479908 | 0.033510 | 0.032009 | **1.046893** |
| `courtyard` | 0.103769 | 0.037385 | 2.775692 | 0.030080 | 0.036763 | **0.818214** |
| `cliff-face` | 0.093849 | 0.058721 | 1.598209 | 0.052016 | 0.052339 | **0.993829** |
| `cliff-moss` | 0.095998 | 0.060012 | 1.599658 | 0.058788 | 0.054023 | **1.088204** |

Chữ thập: `C` là trung bình độ lệch cột 511/512 và hàng 511/512. Trước vá đo trên nguồn đã roll nửa ô; riêng sân đã roll thêm 128/128 theo chuỗi xử lý. Vì vậy C trước sân khác E của ảnh sinh chưa dịch. Sau vá đo lại đúng tâm PNG giao, không bỏ qua khe đá.

| Ô | C trước vá | I nguồn roll | C/I trước | C sau | I sau | C/I sau ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `grass-jade` | 0.074249 | 0.057284 | 1.296171 | 0.061962 | 0.056147 | **1.103568** |
| `grass-moss` | 0.077869 | 0.055312 | 1.407803 | 0.054029 | 0.054321 | **0.994623** |
| `road-paved` | 0.061906 | 0.043962 | 1.408192 | 0.034250 | 0.037840 | **0.905145** |
| `trail-worn` | 0.071179 | 0.058288 | 1.221152 | 0.050542 | 0.051203 | **0.987103** |
| `stream-bank` | 0.048031 | 0.032469 | 1.479272 | 0.033510 | 0.032009 | **1.046893** |
| `courtyard` | 0.031336 | 0.037457 | 0.836600 | 0.030080 | 0.036763 | **0.818214** |
| `cliff-face` | 0.093849 | 0.058756 | 1.597273 | 0.052016 | 0.052339 | **0.993829** |
| `cliff-moss` | 0.095998 | 0.060043 | 1.598831 | 0.058788 | 0.054023 | **1.088204** |

Cả tám qua mép và chữ thập theo ngưỡng trung bình hai trục của phiếu. Số từng trục và mọi phép tính: [audit-measurements.json](../../games/typing-defense/art-src/_review/122/audit-measurements.json).

## 6. Độ rối, đốm lặp và màu

Bộ lọc box5 và box129 đều tuần hoàn. Độ rối = trung bình `|L − box5(L)|`; đốm = `p95 − p5` của box129(L), phân vị nội suy tuyến tính. Hue/S theo HSV, lấy trung vị toàn ô; L cũng là trung vị.

| Ô | Rối trước → sau | Ngưỡng | Đốm trước → sau | Ngưỡng | Kết quả 2–6 |
| --- | --- | ---: | --- | ---: | --- |
| `grass-jade` | 0.054882 → **0.053719** | 0.035 | 0.122198 → **0.122424** | 0.09 | **Trượt |
| `grass-moss` | 0.054431 → **0.053327** | 0.035 | 0.055422 → **0.054215** | 0.09 | **Trượt |
| `road-paved` | 0.039033 → **0.033529** | 0.045 | 0.148418 → **0.118645** | 0.12 | **Đạt |
| `trail-worn` | 0.050936 → **0.044702** | 0.045 | 0.131456 → **0.116545** | 0.12 | **Đạt |
| `stream-bank` | 0.029502 → **0.029027** | 0.045 | 0.138103 → **0.133576** | 0.12 | **Trượt |
| `courtyard` | 0.034086 → **0.033438** | 0.045 | 0.094074 → **0.092383** | 0.12 | **Đạt |
| `cliff-face` | 0.056537 → **0.050418** | 0.055 | 0.140261 → **0.118893** | 0.12 | **Đạt |
| `cliff-moss` | 0.058420 → **0.052499** | 0.055 | 0.133249 → **0.117961** | 0.12 | **Đạt |

| Ô | Hue trung vị | S trung vị | L trung vị | Pixel hue 285–330°, S > 0,5 |
| --- | ---: | ---: | ---: | ---: |
| `grass-jade` | 106.154° | 0.523810 | 0.380279 | **0 / 0%** |
| `grass-moss` | 99.474° | 0.459016 | 0.349329 | **0 / 0%** |
| `road-paved` | 37.895° | 0.121053 | 0.672224 | **0 / 0%** |
| `trail-worn` | 41.633° | 0.295455 | 0.486369 | **0 / 0%** |
| `stream-bank` | 52.500° | 0.093750 | 0.320405 | **0 / 0%** |
| `courtyard` | 37.895° | 0.154545 | 0.808814 | **0 / 0%** |
| `cliff-face` | 53.333° | 0.081081 | 0.524322 | **0 / 0%** |
| `cliff-moss` | 72.414° | 0.275000 | 0.306966 | **0 / 0%** |

| Quan hệ | Số đo | Kết quả |
| --- | ---: | --- |
| Hue hai cỏ trong 80–150° | 106,154° / 99,474° | Đạt |
| Lệch hue ≤ 10° | 6,680° | Đạt |
| Lệch L hai cỏ ≤ 0,06 | 0,030949 | Đạt |
| S cỏ ≤ 0,55 | 0,523810 / 0,459016 | Đạt |
| L đường − L cỏ chính ≥ 0,15 | 0,291945 | Đạt |
| L sân − L cỏ chính ≥ 0,15 | 0,428535 | Đạt |
| L đất chuyển tiếp nằm giữa cỏ và đường | 0,380279 < 0,486369 < 0,672224 | Đạt |
| L đường − L bờ suối ≥ 0,10 | 0,351820 | Đạt |
| Pixel tím bão hòa bị cấm | 0 ở cả tám ô | Đạt |

`grass-moss` thấp hue hơn cỏ chính: về cảm nhận hơi ấm/ôliu hơn yêu cầu “cooler”, dù số màu qua ngưỡng. `cliff-moss` cũng còn ngả ôliu, chưa thật ngọc; đã trừ ở Hợp bộ.

## 7. Mặt đất thử và so mức chợ

Đã xem tám PNG chọn ở cỡ 1024; tám tờ trước–sau cùng cỡ; bảng 256; bảng lát; mock 2048 và bản thu 1280; tờ cạnh ảnh mẫu. Không dùng trình duyệt.

- [122-tiles.jpg](../../games/typing-defense/art-src/_review/122-tiles.jpg), **4096 × 1060**: tám cột, mỗi cột nhãn + ô 512 px + lát 3 × 3 thu về 512 px bằng Lanczos.
- [122-256.jpg](../../games/typing-defense/art-src/_review/122-256.jpg), **2048 × 292**: tám ô đúng 256 px để chấm cỡ nhỏ.
- [122-mock.jpg](../../games/typing-defense/art-src/_review/122-mock.jpg), **1280 × 720**; [bản đầy đủ](../../games/typing-defense/art-src/_review/122/mock-full.jpg), **2048 × 1152**: cỏ chính có vùng cỏ rêu, đường vôi viền đất chuyển tiếp, suối viền cuội, sân đá vuông và vách đứng trộn hai ô vách ở mép gần.
- [122-vs-ref.jpg](../../games/typing-defense/art-src/_review/122-vs-ref.jpg): mock cạnh ảnh chủ dự án và ô trên trái cắt `504x282+4+4` từ `td-1c-ground-sheet-1920x1080.jpg`; **cả ba phần ảnh cùng cao 640 px**, nhãn nằm ngoài phần ảnh.
- Tám `<tên>-roll.jpg` trong [thư mục kiểm](../../games/typing-defense/art-src/_review/122/) lưu ảnh chọn dịch nửa ô để xem tâm/mép.

Mock dùng chiếu trực giao nghiêng 55° và mặt nạ mềm; 64 px/m trên bản 2048, đúng thang ô đất 8 m, vách 12 m. Đây là phép ghép kiểm vật liệu được phiếu cho phép, **không phải ảnh render tích hợp camera phối cảnh ở 58 m**. Nước chỉ là dải màu ngọc để nhìn bờ; không phải tài sản nước phát hành. Không thêm sương, god ray hoặc ánh sáng mới nhằm nâng điểm. [Thông số mock](../../games/typing-defense/art-src/_review/122/mock-spec.json).

Đã mở ảnh tham chiếu của chủ dự án, bộ ô 095/bảng lát cũ, sân 3D hôm nay và `114-ring.jpg`. Bộ mới dùng xanh dịu, xám kem và khoáng bạc, đi cùng họ nắng vàng/sương lam của 114; bản ghép này giữ ánh sáng albedo để lộ đúng chất liệu.

**Chưa đứng cạnh được:** đất đá có chất liệu, đường và sân đọc rõ hơn sân cũ, vách đã gợi mép cao nguyên; nhưng cỏ còn nét vụn và đốm vàng xanh lặp, vách tạo nhịp sọc đều. Mock chưa cho cảm giác quy mô và khối sáng tối hoàn thiện ở mức ảnh mẫu.

| Ô | Quan sát 1024 px / bảng lát | Cỡ 256 px / trên mock |
| --- | --- | --- |
| `grass-jade` | Không thấy đường nối cứng; nhận ra cụm cỏ khô vàng và ba lá lặp theo ô, vùng pha giữa mềm hơn xung quanh | Đọc được nhiều sắc nhưng vẫn rối; mảng vàng tạo nhịp chéo khi lát rộng |
| `grass-moss` | Không thấy đường nối cứng; cụm lá tròn và các kênh tối tạo dấu lặp | Mềm hơn cỏ chính, vẫn thành thảm lá hạt nhỏ; màu hơi ôliu |
| `road-paved` | Không thấy đường nối cắt ngang đột ngột; có mạch đá mờ/chồng gần vùng vá | Làn trắng xám đọc rõ, viên và khe vẫn thấy; vài mạch vân lặp |
| `trail-worn` | Không thấy đường nối cứng; cụm sỏi và turf lặp nhẹ, còn nhiều chi tiết dưới thang mong muốn | Dùng dải hẹp chuyển cỏ sang đường hợp màu; xem toàn ô vẫn hơi hạt |
| `stream-bank` | Không thấy đường nối cứng; nhận ra viên sáng lớn và bóng cuội lặp | Bờ tối tách đường và nước rõ; mảng cuội sáng tối vẫn nổi hơn nền mong muốn |
| `courtyard` | Khe đá vuông vẫn đều; vài vết nứt pha mềm và nhịp viên lặp | Sân đọc rõ nhất; lưới vuông là vật liệu chủ ý, vết nứt lặp là phần còn thiếu |
| `cliff-face` | Mép không có vạch cắt rõ, song nhịp gân dọc và chỗ ngắt rãnh theo hàng lặp vẫn nhận ra | Trên vách đứng đọc đúng đá vôi; các sọc gần đều làm giảm cảm giác tự nhiên |
| `cliff-moss` | Không thấy vạch mép cứng; dải rêu đậm và đá trắng lặp thành sọc | Đọc được rêu/đá nhưng rêu ngả ôliu, tương phản sọc nổi khi đứng cạnh vách trắng |

**Không khẳng định “không thấy lặp”.** Mép đạt số không đồng nghĩa không nhận ra mô típ lặp. Tám tờ trước–sau cho thấy phần khoáng/lá còn nguyên, nhưng cũng bộc lộ vùng pha mềm cần người duyệt xem kỹ.

## 8. KA5 trên bản hậu kỳ

M là điểm cảnh **122-mock.jpg**, dùng chung làm điểm bối cảnh cho cả tám thành phần. Mỗi ô có Q riêng: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Dùng tiếp chỉ có 2 khi mọi kiểm số 2–6 của ô đã qua.

| Ô | M trên mock | Q ở 1024: năm tiêu chí → tổng | Q ở 256: năm tiêu chí → tổng |
| --- | ---: | --- | --- |
| `grass-jade` | **7,5** | 2 / 1,5 / 1,5 / 1,5 / 1 → **7,5** | 2 / 1 / 1,5 / 1,5 / 1 → **7** |
| `grass-moss` | **7,5** | 2 / 1,5 / 1,5 / 2 / 1 → **8** | 2 / 1,5 / 1,5 / 2 / 1 → **8** |
| `road-paved` | **7,5** | 2 / 2 / 2 / 1,5 / 2 → **9,5** | 2 / 2 / 2 / 1,5 / 2 → **9,5** |
| `trail-worn` | **7,5** | 2 / 1,5 / 2 / 1,5 / 2 → **9** | 2 / 2 / 2 / 1,5 / 2 → **9,5** |
| `stream-bank` | **7,5** | 2 / 1,5 / 2 / 1,5 / 1 → **8** | 2 / 1,5 / 2 / 1,5 / 1 → **8** |
| `courtyard` | **7,5** | 2 / 2 / 2 / 1,5 / 2 → **9,5** | 2 / 2 / 2 / 1,5 / 2 → **9,5** |
| `cliff-face` | **7,5** | 2 / 1,5 / 2 / 1,5 / 2 → **9** | 2 / 1,5 / 2 / 1,5 / 2 → **9** |
| `cliff-moss` | **7,5** | 2 / 1,5 / 1,5 / 1,5 / 2 → **8,5** | 2 / 1,5 / 1,5 / 1,5 / 2 → **8,5** |

Đây là tự chấm Codex, **chưa có điểm Claude**. Q ≥ 8 ở vài ô không thay thế kiểm số; M chung vẫn dưới 8 nên chưa ô nào được tuyên bố nhận theo phiếu.

## 9. Chỗ trượt sau ba lượt và cách khác

| Ô | Trượt cụ thể | Hướng khác đề nghị Claude/chủ dự án quyết cho phiếu sau |
| --- | --- | --- |
| `grass-jade` | Rối 0,053719 > 0,035; đốm 0,122424 > 0,09; Q thấp ở cỡ nhỏ | Dùng ảnh tham chiếu **thảm cỏ thực sự thấp nhìn thẳng từ trên** với khối cỏ/màu 0,5–1,5 m; làm bản hướng chất liệu trước khi sinh tile. Bớt hình lá riêng, rơm khô gom theo mảng lớn gần sáng, giữ chất liệu từ đầu sinh thay vì làm mờ hậu kỳ |
| `grass-moss` | Rối 0,053327 > 0,035; màu còn ấm hơn yêu cầu | Chọn tham chiếu rêu nhung liền khối, ba lá chỉ thành vài mảng ép sát mặt đất; khóa màu theo bản cỏ mới đã duyệt trước khi sinh biến thể |
| `stream-bank` | Đốm 0,133576 > 0,12 | Tham chiếu bùn xám liên tục với ít cuội chìm đồng sáng; ánh ướt là mảng bạc rộng gần sáng nền. Cần sửa cấu trúc vật liệu ngay ở bản vẽ mới, không nén toàn bộ sáng tối bản này |

Với cả cảnh, cần giảm dấu lặp của cỏ/vách trước khi tích hợp lên địa hình có khối và ánh sáng của sân thật. Không tự mở lượt thứ tư hoặc sửa mã để che lỗi vật liệu trong phạm vi phiếu này.

## 10. Script, bằng chứng và việc bỏ qua

Các script đã có được giữ nguyên: `process.mjs` (giải mã, vá, đo), `light.mjs`, `offset.mjs`, `revision-prompts.mjs`, `last-prompts.mjs`, `deliver.mjs`. **Không chạy lại `deliver.mjs`** vì đầu ra đã tồn tại.

Bổ sung trong `_review/122/`:

- `review-audit.mjs`: tính lại nguồn → PNG, đo trước/sau/chữ thập, xuất tám cặp trước–sau, tám roll, bảng lát, bảng 256, mock và tờ cạnh tham chiếu. Ghi mới độc quyền, từ chối ghi đè; chỉ tạo lại khi các đích chưa tồn tại.
- `verify-readonly.mjs`: tính lại pixel/prompt/số đo và MD5. Chạy không cờ hoàn toàn chỉ đọc; `--write-evidence` chỉ dùng lần đầu để ghi mốc sau/diff/đối chiếu, từ chối ghi đè.
- `write-report.py`: lập báo cáo từ số đo kiểm độc lập, chỉ tạo file chưa có.

Lệnh đã dùng:

```sh
node games/typing-defense/art-src/_review/122/review-audit.mjs
node games/typing-defense/art-src/_review/122/verify-readonly.mjs --write-evidence
python3 games/typing-defense/art-src/_review/122/write-report.py
```

Lệnh **chạy lại kiểm chứng mà không ghi file**:

```sh
node games/typing-defense/art-src/_review/122/verify-readonly.mjs
```

Dùng trực tiếp Node, Python chuẩn và `/opt/homebrew/bin/magick`; không cài thư viện, không dùng `tools/art-normalize`. Font tờ kiểm: `/System/Library/Fonts/Supplemental/Arial.ttf`.

**Khác phiếu:** tiếp nối tài sản đã có thay vì sinh mới; giữ nguyên các PNG chưa qua số để tôn trọng luật không ghi đè và §5; mock chiếu trực giao đơn giản thay camera phối cảnh runtime. Những khác biệt này được công khai, không đổi ngưỡng nhận.

**Bỏ qua:** không sinh thêm vì ba ô trượt đều đã đủ ba lượt; không tích hợp hoặc sao chép vào `public`; không chạy Git, build/test game, dev server, trình duyệt, mạng; không sửa game, âm thanh, tài liệu khác hoặc vùng Tu Tiên. Không ghi vào game khác. Chỉ thêm file đúng vùng cho phép. Các JPG là ảnh kiểm tĩnh được báo cáo liên kết, không có phiên chụp browser hoặc bộ frame thô mới cần dọn.

**Claude/chủ dự án cần xem:** `122-vs-ref.jpg`, `122-mock.jpg`, bảng lát và tám cặp trước–sau; quyết cách làm lại ba ô trượt và mức pha ở chữ thập. Phiếu **chưa đủ điều kiện “xong khi”**, chờ vòng mỹ thuật mới được giao riêng và chấm lại M ≥ 8, Q ≥ 8 cùng mọi kiểm số 2–6.

