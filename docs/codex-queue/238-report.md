# Phiếu 238 · Last Line · Đã giao ba ảnh sửa, chờ Claude chấm lại

Ngày 31/10/2026, Codex. Đã làm lại đúng **Objective, Station Crest và Shard**, giữ chất liệu Lightbearer của tám ảnh đã nhận. Chọn **Objective try2, Station Crest try3, Shard try2**. Icon và chân dung Shard giống nhau từng byte ở cả bốn khổ. Công cụ tích hợp `image_gen.imagegen` sinh thành công bốn ảnh; không gặp 429.

**Chưa xác nhận nghiệm thu:** cần Claude chấm lại từ 8, có xét 20 px. Điểm bên dưới là Codex tự chấm trên bản hậu kỳ, đã xem PNG 1024², bản 64 và ô cỡ thật. Không tự ghi điểm thay Claude.

## 1. File giao và các lượt

Đường dẫn tính từ `games/typing-survival/art-src/`. Mỗi dòng có `.png` 1024², `.256.png`, `.128.png`, `.64.png`, `.prompt.txt`.

| Bộ giao | Chọn | Sửa đúng chỗ thiếu |
| --- | --- | --- |
| `ui/icons/objective` | try2 | Bỏ toàn bộ ngoặc ngắm; lá cờ lớn, cán rõ, lõi và nếp lam sáng. Giữ kim loại trắng vàng, than chì và cyan. |
| `ui/icons/station-crest` | try3 | Tháp đứng cao, đáy gọn hơn; vòng cam nhỏ riêng bên phải, không quấn thân. Lượt 2 có quầng plasma bán trong suốt rộng; lượt 3 đổi sang vòng kim loại đặc với ánh cam nằm trong vật liệu, mở rộng khoảng trống. |
| `ui/icons/shard` | try2 | Giữ ba mũi tinh thể, thân nêm và hai vuốt; tăng viền cam vàng, phản sáng bạc lam và lõi cam. |
| `ui/foes/shard` | cùng try2 | Dùng đúng nguồn và bản hậu kỳ của icon, đồng bộ dáng và ánh sáng cho thẻ ải 40/60 px. |

Giữ mọi bản sinh `.try2.png`, riêng tháp thêm `.try3.png`, với prompt nguyên văn cạnh ảnh. Shard ở hai thư mục là bản sao của **một lần sinh**, không tính hai lần. Không cần sinh try3 cho cờ và Shard sau khi kiểm nhỏ đạt. [Nhật ký nguồn công cụ và prompt](238/generated-files.json), [hồ sơ và lệnh kiểm đọc](238/README.md).

Prompt giữ nguyên STYLE-UI §4.3 và KIND tương ứng của 150; chỉ thay mô tả vật và ánh sáng cần sửa. Đã xem tờ 150, ảnh chuẩn HUD chủ dự án, Pulse Gun, panel 127, briefing 121, Swarm và Shard cũ. Các yêu cầu sinh dùng ảnh tham chiếu vật liệu cùng bộ; Shard có ảnh cũ làm tham chiếu nhận diện. Yêu cầu Shard đầu tiên bị bộ kiểm tham số từ chối vì 7 tham chiếu, tối đa 5; bỏ hai tham chiếu phụ, giữ nguyên prompt và gọi lại. Đây không phải lần sinh thành công. [Chi tiết](../../games/typing-survival/art-src/_review/238/tool-validation.txt).

## 2. Hậu kỳ không phá tranh

Nguồn trả về 1254², alpha thật. Đưa hai đầu alpha ≤16 / ≥250 về 0/255; cắt phần rỗng, căn hộp bao alpha >16 về cạnh dài 717 px trên canvas 1024². Thu từng khổ trực tiếp bằng Lanczos từ bản 1024²; sửa riêng alpha ngoài mép Euclid 3 px, kiểm ở cả ngưỡng mặt nạ >16 và >127. Không đổi màu, gamma hoặc độ sáng RGB; không làm nét bản 64, không phủ hay thay phần vẽ.

Đã bỏ bản hậu kỳ tháp try2 khỏi bộ giao vì bước matte của quầng plasma đổi 13.561 pixel, tối đa 127/255 ở khổ gốc. Giữ cả nguồn, bản hậu kỳ, số đo và tờ xem lượt đó để tra cứu. Try3 giảm còn 1.004 pixel, tối đa 11/255, RGB không đổi. Không dùng thao tác xóa quầng để ép bản try2 đạt.

| Bản chọn | Pixel sửa matte ngoài mép, 1024² | Mức đổi alpha lớn nhất | RGB bị đổi ở bước matte |
| --- | ---: | ---: | ---: |
| Objective try2 | 1.623 | 10/255 | 0 |
| Station Crest try3 | 1.004 | 11/255 | 0 |
| Shard try2 | 1.224 | 26/255 | 0 |

Các số này là bước sửa matte sau căn khổ, không gồm việc đưa hai đầu alpha về 0/255. Tờ “bản sinh | bản hậu kỳ” hiển thị toàn bộ canvas hai bên, cùng cỡ; không cắt vật để giấu sai khác.

## 3. Kiểm khổ, alpha, lề, màu khóa và dáng

**16/16 PNG giao** đúng 1024²/256²/128²/64², sRGB, sRGBA. Cả bốn khổ của từng bộ có **0 pixel alpha trung gian ngoài mép 3 px**, ở cả hai ngưỡng mặt nạ. Các ô 20/30/40/60 là phép thu để xem, không phải file giao nên không áp dụng bước ép matte của bản xuất lên các ô này. [Identify](../../games/typing-survival/art-src/_review/238/identify-delivery.txt), [kiểm tổng và MD5](../../games/typing-survival/art-src/_review/238/validation-delivery.json).

| Ảnh | Cạnh dài hộp bao 1024² | Lệch tâm lớn nhất | Màu khóa (%) | IoU lớn nhất >16 / >127 tại 32 px |
| --- | ---: | ---: | ---: | --- |
| Objective | 70,020% | 0,049% | 0,0270 | 0,540 / 0,508 · learning-rule |
| Station Crest | 70,020% | 0,049% | 0,0578 | 0,541 / 0,448 · new-badge |
| Shard | 70,020% | 0,049% | 0,0365 | 0,656 / 0,642 · learning-rule |

Màu khóa đo bảo thủ hue cách magenta tối đa 15°, S >0,5, trên pixel alpha >0; nguồn sinh dùng alpha thật, không dùng nền khóa. Tất cả khổ giao ≤0,2%. Các bản thu có cạnh dài hộp bao 70,313–71,875%, lệch tâm 0% theo hộp bao. Hộp bao 68–72% và tâm ≤2% đều đạt.

Đã tính lại đủ **55 cặp** của bộ 11 tên, dùng ba ảnh mới và tám ảnh đã nhận. Cực đại toàn bộ **0,745** ở >16 và **0,699** ở >127, đều ≤0,80. Shard icon/chân dung là cùng một ảnh nên không đưa thành hai tên khác nhau trong phép phân biệt dáng. [Toàn bộ cặp và cực đại từng tên](../../games/typing-survival/art-src/_review/238/iou-delivery.json).

## 4. Kiểm cỡ thật và tương phản

Chênh luma Rec.709 trung bình theo trọng số alpha trên sRGB 0–1, không phải tỷ số WCAG. Mỗi ô dưới đây theo thứ tự **`#11161d` / `#14181f` / `#8c96a3`**. Hai nền sau giữ nguyên quy định của 150; nền đầu là nền tối thực tế mà 238 yêu cầu cho Shard.

| Ảnh | 1024² | 20 px | 30 px |
| --- | --- | --- | --- |
| Objective | 0,417 / 0,409 / 0,082 | 0,419 / 0,410 / 0,081 | 0,417 / 0,408 / 0,082 |
| Station Crest | 0,429 / 0,420 / 0,071 | 0,429 / 0,420 / 0,070 | 0,430 / 0,422 / 0,069 |
| Shard | 0,289 / 0,280 / 0,211 | 0,291 / 0,282 / 0,209 | 0,291 / 0,282 / 0,209 |

Shard **40 px: 0,290 / 0,282 / 0,209**; **60 px: 0,290 / 0,281 / 0,210**. Cả ba ảnh đạt ≥0,25 trên hai nền tối ở mọi cỡ kiểm. Shard cũ chỉ khoảng 0,199 trên than chì; bản mới khoảng 0,282 ở 20 px. Không tuyên bố đạt 0,25 trên thép sáng: viền và kính tối tạo nhận diện trên nền đó.

Mỗi lượt thành công có ô 20/30 px trên cả ba nền; Shard thêm 40/60 px. Số đo đầy đủ gồm khổ thu, alpha và matte nằm trong các file `*.metrics.json` của [`_review/238/`](../../games/typing-survival/art-src/_review/238/).

## 5. Tờ xem và tự chấm KA5

- [238-sheet-delivery.jpg](../../games/typing-survival/art-src/_review/238-sheet-delivery.jpg): ba ảnh mới cạnh tám ảnh nhận, cùng ô 256 px; hàng 30 và 20 px cùng cỡ cho cả 11 ảnh, thêm hàng cỡ thật theo 150, bốn icon cũ và mảnh HUD chuẩn cùng cao 96 px. Có Shard 40/60 px trên ba nền.
- [Objective try2: trước/sau và cỡ nhỏ](../../games/typing-survival/art-src/_review/238/objective.try2.small-before-after.jpg).
- [Station Crest try2: trước/sau và cỡ nhỏ, không chọn](../../games/typing-survival/art-src/_review/238/station-crest.try2.small-before-after.jpg).
- [Station Crest try3: trước/sau và cỡ nhỏ, chọn](../../games/typing-survival/art-src/_review/238/station-crest.try3.small-before-after.jpg).
- [Shard try2: trước/sau, 20/30/40/60 px](../../games/typing-survival/art-src/_review/238/shard.try2.small-before-after.jpg).
- [Shard cạnh sáu chân dung gốc, đúng 40 px](../../games/typing-survival/art-src/_review/238-shard-portraits.jpg).

Thứ tự năm điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**. Chấm so với độ hoàn thiện UI game thương mại trong tham chiếu chủ dự án, trên ảnh giao.

| Ảnh | 1024² | 20 px | Hạn chế còn thấy |
| --- | --- | --- | --- |
| Objective | 2/2/2/1/2 → **9** | 2/2/2/1/2 → **9** | Viền cờ dày làm lá cờ hơi cứng; nhận diện cán và cờ đã rõ, không còn khung ngoặc. |
| Station Crest | 1/2/2/2/2 → **9** | 1/2/2/2/2 → **9** | Vòng kim loại gợi biểu tượng hố đen hơn là mô tả bồi tụ tự nhiên; ở 20 px vẫn là tháp cao và vòng tách, không thành đĩa bay. |
| Shard | 2/2/1/2/2 → **9** | 2/1/1/2/2 → **8** | 20 px đọc được ba mũi và lõi sáng, vân kính hòa lại. Sáng và cam hơn sáu chân dung gốc nên hợp bộ một phần; không sửa sáu ảnh đó. |

Shard 40/60 px tự chấm **9** (2/2/1/2/2): hình khối và lõi đọc rõ hơn. Ánh lạnh trái và viền cam phù hợp cách trình bày vật thể đơn, nhưng cường độ sáng khác sáu bản gốc; đây là điểm Claude/chủ dự án cần xem trực tiếp. Không dùng điểm tự chấm để thay điều kiện Claude ≥8.

## 6. Bảo toàn file và phạm vi

Trước lần ghi đè đầu tiên đã chép **15 file cũ** của Objective, Station Crest và chân dung Shard vào [`_review/238/prev/`](../../games/typing-survival/art-src/_review/238/prev/), giữ cấu trúc `ui/icons` và `ui/foes`. Icon Shard chưa có ở đầu lượt nên là bộ mới. Bản sao cũ khớp MD5 ban đầu 15/15.

| KA1, toàn bộ `ui/icons` và `ui/foes` | Kết quả |
| --- | ---: |
| File trước / sau | 588 / 603 |
| File thêm | 15 |
| File cũ đổi theo quyền ghi đè của 238 | 15 |
| File mất / đổi ngoài danh sách được phép | 0 / 0 |
| File được bảo vệ giữ nguyên MD5 | 573/573 |

Khác yêu cầu “diff chỉ thêm” của 150: **238 cho phép ghi đè đúng ba tên**, nên diff có 15 thay đổi chủ động, kèm đủ bản sao cũ. Tám ảnh đã nhận, mọi `try1`, sáu chân dung khác và các file ngoài danh sách bản chốt giữ nguyên. [MD5 trước](../../games/typing-survival/art-src/_review/238/md5-before.txt), [MD5 sau](../../games/typing-survival/art-src/_review/238/md5-after.txt), [danh sách chính xác các file thêm/đổi](../../games/typing-survival/art-src/_review/238/validation-delivery.json).

Prompt nguồn/chọn mới nằm đúng cạnh bản sinh và bản chốt. Các sidecar `.64.prompt.txt`, `.128.prompt.txt`, `.256.prompt.txt` cũ của 150 không thuộc danh sách được sửa nên giữ nguyên; prompt chuẩn để truy vết bộ 238 là `<tên>.prompt.txt` và `<tên>.tryN.prompt.txt`.

Không chạy Git, build/test game, dev server, trình duyệt, công cụ âm thanh hay mạng ngoài image_gen. Không ghi `public/`, game khác, Tu Tiên, `.wt-*`, mã game hoặc tài liệu ngoài phạm vi. Không có raw frame trình duyệt cần prune. Giữ ảnh sinh và hồ sơ hậu kỳ theo phiếu.

**Còn lại:** Claude chấm lại ba ảnh ở 20 px và Shard ở 40/60 px; chủ dự án xem mức sáng Shard cạnh sáu chân dung. Việc tích hợp `public/` để bước gắn sau khi nhận, không thuộc phiếu 238.
