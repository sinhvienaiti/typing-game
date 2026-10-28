# Phiếu 093 · Rồng Giữ Ải · Làm liền mép ba ô nền MF-I5

Ngày kiểm: 28/10/2026. Bộ `pine-river`, map `L2-cau`.

**Kết quả: cả ba `.fix1.png` đạt Kiểm 1–4; tự chấm KA5 từ 9 điểm ở khổ đầy đủ.** Đã xem ảnh dịch nửa ô, lát 3 × 3 và bản 128 px. Chưa có lượt chấm lại của Claude; chưa thay ba bản chọn `.png`.

## 1. Cách sửa và tham số

Chỉ xử lý pixel bằng Node và ImageMagick 7, không gọi công cụ tạo ảnh, không vẽ lại nội dung. Giữ khổ **1254 × 1254**, RGB sRGB 8 bit; dịch vòng **627 px**. Pha trên giá trị sRGB 8 bit, làm tròn một lần khi xuất.

Đã thử đúng mặt nạ chữ thập đề xuất với `a = 24`, `b = 96, 128, 160, 192, 224`. Cách này đưa một phần mép lỗi của ảnh gốc trở lại mép ngoài qua nhánh ngang/dọc của mặt nạ. Cỏ A và đất trượt ngưỡng với cả năm giá trị. Vì vậy đổi sang **ghép tuần tự theo X rồi Y**, vẫn dùng cùng hàm cosin và pixel của ảnh gốc.

Gọi `X`, `Y` là phép dịch vòng nửa ô theo từng trục; `wx = w(|x − 627|)`, `wy = w(|y − 627|)`:

```text
S = (1 − wx) · X(T) + wx · T
O = (1 − wy) · Y(S) + wy · S
```

Tính `S` trong bộ nhớ với độ chính xác số thực, chưa làm tròn. Tương đương pha bốn bản `XY(T)`, `Y(T)`, `X(T)`, `T`; không có bộ lọc làm mờ bổ sung. Nhánh vá theo Y dùng `S` đã sửa theo X, nên không đưa mép X lỗi của `T` trở lại.

| b (px) | Chữ thập đề xuất: E/I, cỏ A / cỏ B / đất | Tuần tự X–Y: E/I, cỏ A / cỏ B / đất |
| ---: | --- | --- |
| **96** | 1,2971 / 1,1242 / 1,2710 | **1,1198 / 0,9684 / 1,1075** |
| 128 | 1,3746 / 1,1607 / 1,3081 | 1,1339 / 0,9692 / 1,1177 |
| 160 | 1,4382 / 1,1977 / 1,3422 | 1,1457 / 0,9757 / 1,1337 |
| 192 | 1,4946 / 1,2433 / 1,3753 | 1,1546 / 0,9790 / 1,1369 |
| 224 | 1,5443 / 1,2931 / 1,4163 | 1,1670 / 0,9935 / 1,1458 |

**Chọn `a = 24`, `b = 96` cho cả ba ảnh:** cả năm phương án tuần tự đều qua kiểm số; bản 96 có vùng pha hẹp nhất, giữ nhiều độ rối nhất và ít bóng chồng hơn khi xem bảng so sánh. Giữ nguyên dải trung tâm rộng 49 px; mỗi phía chuyển tiếp 96 px, trọng số về 0 từ khoảng cách 120 px.

Mọi chunk PNG ngoài `IDAT` được giữ nguyên byte. Ảnh nguồn không có chunk hồ sơ màu `iCCP`, `sRGB`, `gAMA`, `cHRM`, `cICP`; không tự thêm hay chuyển hồ sơ. ImageMagick nhận cả nguồn và đầu ra là sRGB 8 bit. Giải mã PNG xuất ra khớp đúng từng byte RGB đã tính. Chạy lại thuật toán cũng tái tạo đúng byte ba file PNG bàn giao.

Bằng chứng thử: [chữ thập](../../games/dragon-hold/art-src/_review/093/sweep.json), [tuần tự](../../games/dragon-hold/art-src/_review/093/sweep-separable.json), [bảng chữ thập](../../games/dragon-hold/art-src/_review/093/sweep-627.jpg), [bảng tuần tự](../../games/dragon-hold/art-src/_review/093/sweep-separable-627.jpg), [tái tạo byte](../../games/dragon-hold/art-src/_review/093/replay-verification.json).

## 2. Kiểm 1 — KA1, giữ nguyên ảnh cũ

Chạy `/sbin/md5 -r` cho **mọi file** trong `ground/pine-river/`, sắp theo tên, trước khi tạo đầu ra và sau khi tạo đủ ba ảnh.

| Số đo | Trước | Sau | Kết quả |
| --- | ---: | ---: | --- |
| File trong thư mục | 49 | 52 | Thêm đúng 3 `.fix1.png` |
| File cũ đổi nội dung | — | 0 | Đạt |
| File cũ mất | — | 0 | Đạt |
| Dòng nội dung thêm trong `diff -U 0` | — | 3 | Chỉ ba tên được phép |

| File mới | MD5 |
| --- | --- |
| `meadow-calm-a.fix1.png` | `64a791548c0891877af3236762a08407` |
| `meadow-calm-b.fix1.png` | `8feb28e67502cddfc86670f23894dbb4` |
| `soil-worn-pale.fix1.png` | `2bd57c6e2a267ed2cd763004adc8e1e9` |

Bằng chứng: [trước](../../games/dragon-hold/art-src/_review/093/md5-before.txt), [sau](../../games/dragon-hold/art-src/_review/093/md5-after.txt), [diff](../../games/dragon-hold/art-src/_review/093/md5-diff.txt), [đối chiếu danh sách](../../games/dragon-hold/art-src/_review/093/md5-verification.json). Kiểm cuối xác nhận thư mục vẫn khớp mốc sau.

## 3. Kiểm 2 — mép ngoài

Dùng đúng quy ước phiếu 067 §4: RGB sRGB 0–1, `L = 0,2126R + 0,7152G + 0,0722B`. `E` là trung bình của sai khác trái/phải và trên/dưới; `I` là trung bình sai khác pixel kề theo X và Y bên trong ảnh. Các giá trị dưới đây là đơn vị L 0–1, lấy từ PNG, không đo JPG.

| Ảnh | E trước | I trước | E/I trước | E sau | I sau | E/I sau | ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `meadow-calm-a` | 0,026072905 | 0,007945153 | 3,281611 | 0,008598516 | 0,007678785 | **1,119776** | Đạt |
| `meadow-calm-b` | 0,013421493 | 0,005170259 | 2,595903 | 0,004771606 | 0,004927078 | **0,968445** | Đạt |
| `soil-worn-pale` | 0,011470266 | 0,004869771 | 2,355402 | 0,005227398 | 0,004720018 | **1,107495** | Đạt |

Số phụ theo từng trục sau sửa, `E_X/I_X` và `E_Y/I_Y`: cỏ A **1,264888 / 0,981109**; cỏ B **0,958694 / 0,978703**; đất **1,199381 / 1,032572**. Riêng trục X của cỏ A còn cao hơn 1,25; ngưỡng bắt buộc của phiếu áp dụng cho `E/I` trung bình hai trục như đã định nghĩa, không phải hai ngưỡng riêng. Ghi số phụ để Claude xem kỹ trục này khi duyệt.

## 4. Kiểm 3 — chữ thập giữa ảnh

Gọi `C` là trung bình sai khác cột 626/627 và hàng 626/627; chia cho `I` của chính ảnh đang đo. “Trước vá” trong bảng là ảnh gốc **đã roll +627+627**, nơi mép lỗi cũ trở thành chữ thập. `I` sau roll tính từ việc thay cặp giữa ảnh bằng cặp mép: `I_R = I_T + (E_T − C_T) / 1253`.

| Ảnh | C trước vá | I trước vá | C/I trước vá | C sau | I sau | C/I sau | ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `meadow-calm-a` | 0,026072905 | 0,007959303 | 3,275777 | 0,008598516 | 0,007678785 | **1,119776** | Đạt |
| `meadow-calm-b` | 0,013421493 | 0,005177105 | 2,592471 | 0,004771606 | 0,004927078 | **0,968445** | Đạt |
| `soil-worn-pale` | 0,011470266 | 0,004874686 | 2,353027 | 0,005227398 | 0,004720018 | **1,107495** | Đạt |

Để phân biệt với “trước vá”, `C/I` tại giữa ảnh nguồn chưa roll lần lượt là **1,050049 / 0,936934 / 1,090666**. Sau sửa, C và E bằng nhau do hai vị trí cùng lấy các cặp pixel giữa ảnh nguồn qua phép ghép tuần tự. Các số từng trục cũng bằng các số phụ ở mục 3; không xuất hiện đường chữ thập mới khi xem ảnh đầy đủ.

## 5. Kiểm 4 — giữ màu và độ rối

Hue theo HSV, độ. Độ rối là trung bình `|L − box5×5(L)|`, biên tuần hoàn. KA4 đếm hue 0–50° hoặc 165–190°, `S > 0,55`, `V > 0,5`.

| Ảnh | Hue trước → sau | L trung vị trước → sau | Độ rối trước → sau | Giữ độ rối | KA4 trước → sau |
| --- | ---: | ---: | ---: | ---: | ---: |
| `meadow-calm-a` | 92,876712 → **92,876712°** | 0,612632941 → 0,612648627 | 0,007596965 → **0,007278933** | **95,8137%** | 0 → **0%** |
| `meadow-calm-b` | 94,520548 → **94,500000°** | 0,583818039 → 0,584101176 | 0,004840302 → **0,004572554** | **94,4684%** | 0 → **0%** |
| `soil-worn-pale` | 37,714286 → 37,714286° | 0,686962353 → **0,686962353** | 0,004348805 → 0,004193897 | 96,4379% | 0 → **0%** |

Hai ô cỏ đều trong hue **88–95°**, độ rối **≤ 0,030** và giữ **≥ 85%** bản gốc. Đất giữ L trung vị trong **0,64–0,70**. KA4 có đúng **0 pixel** vi phạm ở cả ba ảnh trước và sau.

Đã chạy lại trình đo có sẵn của 067 (`_review/MF-I5/measure.mjs`, chỉ đọc) cho sáu PNG nguồn/đích. Hue, L, độ rối, mép và chênh pixel kề khớp trình sửa trong sai số **< 10⁻¹²**. Bằng chứng: [số đo đầy đủ](../../games/dragon-hold/art-src/_review/093/metrics-final.json), [đo độc lập bằng script 067](../../games/dragon-hold/art-src/_review/093/independent-metrics.json), [kết quả các ngưỡng](../../games/dragon-hold/art-src/_review/093/final-checks.json).

## 6. Kiểm 5 — ảnh kiểm và quan sát

Các bảng không chèn lề giữa ô; thứ tự hàng luôn là **cỏ A / cỏ B / đất**:

- [093-roll.jpg](../../games/dragon-hold/art-src/_review/093-roll.jpg), **2508 × 1881**: mỗi hàng bốn ô **627 × 627**, trái sang phải là **gốc / gốc roll +627+627 / fix1 / fix1 roll +627+627**.
- [093-tile3x3.jpg](../../games/dragon-hold/art-src/_review/093-tile3x3.jpg), **2508 × 3762**: mỗi hàng, **gốc lát 3 × 3 ở trái / fix1 lát 3 × 3 ở phải**. Lát ở 3762 × 3762 rồi thu từng ô tổng còn **1254 × 1254**.
- [Đối chiếu 128 px](../../games/dragon-hold/art-src/_review/093/compare-128.jpg), **512 × 384**, cùng thứ tự bốn cột với bảng roll.
- Bản dịch fix1 ở đủ **1254 × 1254**: [cỏ A](../../games/dragon-hold/art-src/_review/093/meadow-calm-a.fix1.roll.jpg), [cỏ B](../../games/dragon-hold/art-src/_review/093/meadow-calm-b.fix1.roll.jpg), [đất](../../games/dragon-hold/art-src/_review/093/soil-worn-pale.fix1.roll.jpg).

Đã mở ba PNG fix1 và ba bản dịch ở cỡ đầy đủ, cả hai bảng bắt buộc ở độ phân giải gốc và bảng 128 px.

| Ảnh | Trước sửa | Sau sửa, cỡ đầy đủ và lát 3 × 3 | 128 px |
| --- | --- | --- | --- |
| Cỏ A | Chữ thập rõ ở bản roll; mép dựng thành ô khi lát | **Không thấy đường nối** ở mép lát hoặc giữa ảnh. Vẫn nhận ra nhịp lặp của các cụm cỏ sáng/tối; vùng pha mềm nhẹ, không thành dải thẳng rõ | Không thấy đường nối; vẫn là nền cỏ có mảng |
| Cỏ B | Đường mảnh ở bản roll, có bước đổi mảng khi lát | **Không thấy đường nối**. Giữ các nét cỏ chéo và mảng tối sẵn có; không thấy bóng chồng tách thành hai lớp rõ | Không thấy đường nối; cụm tối còn nhận ra |
| Đất | Đường mảnh qua giữa bản roll | **Không thấy đường nối**. Bề mặt mòn mềm, sáng đều, không có chữ thập mới | Không thấy đường nối; nền đất yên |

Mô típ còn lặp khi lát 3 × 3; nhận xét “không thấy đường nối” chỉ nói về mép và chữ thập, không khẳng định đã hết lặp mô típ. Phiếu này sửa đường nối, không xử lý lại các mảng thấp tần ngoài yêu cầu. Không chạy bản đồ trong trình duyệt theo giới hạn của phiếu.

## 7. Kiểm 6 — KA5 tự chấm

Theo năm tiêu chí của `ART_ACCEPTANCE.md` §1 và mức ảnh 2D §2.2; mỗi tiêu chí tối đa 2 điểm. Thứ tự: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**. Với ô nền, hình khối đánh giá mặt phẳng nhìn từ trên. Điểm trước lấy từ tự chấm bản chọn trong báo cáo 067; điểm sau là tự chấm lần này.

| Ảnh | Trước, đủ khổ / 128 px | Sau, đủ khổ: năm tiêu chí → tổng | Sau, 128 px: năm tiêu chí → tổng | Mức và phần còn thiếu |
| --- | --- | --- | --- | --- |
| `meadow-calm-a.fix1` | 8 / 8,5 | 1,5 / 1,5 / 2 / 2 / 2 → **9** | 1,5 / 2 / 2 / 2 / 2 → **9,5** | **Đạt**; mảng cỏ còn tương phản và nhịp lặp |
| `meadow-calm-b.fix1` | 8 / 8,5 | 1,5 / 1,5 / 2 / 2 / 2 → **9** | 1,5 / 2 / 2 / 2 / 2 → **9,5** | **Đạt**; cụm cỏ chéo/tối còn nổi |
| `soil-worn-pale.fix1` | 9 / 9 | 2 / 2 / 2 / 2 / 2 → **10** | 2 / 2 / 2 / 2 / 2 → **10** | **Đạt**; không thấy lỗi cần sửa trong phạm vi phiếu |

Chỉ cho tiêu chí dùng tiếp 2 điểm sau khi Kiểm 2 và 3 đều đạt. Đây là tự chấm tài sản ảnh; chưa khẳng định nghiệm thu hiển thị trong game hay điểm chấm lại của Claude.

## 8. Bàn giao, chạy lại và phần bỏ qua

Ba file mới chờ duyệt, cùng ở `games/dragon-hold/art-src/ground/pine-river/`:

- [meadow-calm-a.fix1.png](../../games/dragon-hold/art-src/ground/pine-river/meadow-calm-a.fix1.png).
- [meadow-calm-b.fix1.png](../../games/dragon-hold/art-src/ground/pine-river/meadow-calm-b.fix1.png).
- [soil-worn-pale.fix1.png](../../games/dragon-hold/art-src/ground/pine-river/soil-worn-pale.fix1.png).

Script đã dùng: [fix-seams.mjs](../../games/dragon-hold/art-src/_review/093/fix-seams.mjs), [make-review.mjs](../../games/dragon-hold/art-src/_review/093/make-review.mjs), [validate.mjs](../../games/dragon-hold/art-src/_review/093/validate.mjs). Chỉ dùng module có sẵn của Node và `/opt/homebrew/bin/magick`, không thêm gói. Font bảng thử là `/System/Library/Fonts/Supplemental/Arial.ttf`.

Chạy từ repo cha, chuỗi thao tác ban đầu là:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/dragon-hold/art-src/_review/093/fix-seams.mjs sweep
node games/dragon-hold/art-src/_review/093/fix-seams.mjs sweep-separable
node games/dragon-hold/art-src/_review/093/fix-seams.mjs finalize 96 separable
node games/dragon-hold/art-src/_review/093/make-review.mjs
node games/dragon-hold/art-src/_review/093/fix-seams.mjs audit
```

Các thao tác tạo file dùng chế độ ghi độc quyền, từ chối ghi đè. Không chạy lại chuỗi tạo ảnh lên bộ bàn giao đã tồn tại. Để **chạy lại thuật toán trên bộ hiện tại mà không ghi file**, dùng:

```sh
node games/dragon-hold/art-src/_review/093/fix-seams.mjs replay 96 separable
```

Lệnh này tính lại cả PNG và xác nhận byte trùng với ba file bàn giao. Script ảnh kiểm bỏ qua đầu ra đã có. Trong phiên đã sửa tương thích `diff` của macOS sang `-U 0`; bảng kiểm được ghép trực tiếp từ đường dẫn ảnh sau khi cách truyền luồng MIFF bị treo. Tiến trình treo do phiên này tạo đã được ngắt; không để server hay tiến trình nền phục vụ game.

**Bỏ qua:** không thay bản chọn `.png`, không tạo prompt mới vì không tạo ảnh bằng AI; không vẽ lại, không chạy Git, dev server, trình duyệt, build/test game. Không sửa tài liệu khác hoặc đọc/ghi vùng Tu Tiên. Các JPG đều là ảnh kiểm dẫn xuất được liên kết trong báo cáo, không phải frame chụp trình duyệt/render; không tạo bộ frame thô cần dọn.

**Claude/chủ dự án cần xem:** hai bảng ảnh kiểm, ba bản roll đầy đủ, đặc biệt trục X cỏ A và nhịp lặp các cụm cỏ. Claude chấm lại từng ảnh **≥ 8** thì mới chép `.fix1.png` sang `<tên>.png` theo phiếu; phiên này giữ nguyên toàn bộ bản chọn.
