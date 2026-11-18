# Phiếu 240 · Last Line · Đã giao năm bản sửa, còn ngoại lệ trước nghiệm thu

Ngày 31/10/2026, Codex. Đã sinh **chín ảnh**, chọn năm bản, giao **20 PNG** (1024², 256², 128², 64²), đủ prompt nguyên văn cạnh từng ảnh. Đã sao lưu 31 file chốt cũ trước khi ghi đè. Không gặp HTTP 429 hoặc thông báo phải đợi.

**Chưa đóng phiếu:** cần Claude chấm lại từ 8. Kiểm khổ, sRGBA/sRGB, lề, tâm, màu khóa, tương phản ở cỡ dùng chính, cặp ô đạn và bảo toàn file đạt. **Còn alpha trung gian ngoài mép ở bản thu Lanczos; Station Crest–Hazard có IoU 0,816092 theo alpha ≥128, vượt 0,80.** Giữ tranh và ghi số thật; không tuyên bố mọi kiểm số đã đạt. Giới hạn ba lượt ý tưởng mới của Station Crest đã dùng hết.

## 1. Bộ giao và lượt chọn

Đường dẫn dưới trỏ master 1024². Mỗi bộ có ba bản thu trực tiếp từ master và prompt cạnh cả bốn PNG.

| Tên | Bản chọn | Tờ đối chiếu |
| --- | --- | --- |
| `shake` | [shake.c2-try1](../../games/typing-survival/art-src/ui/icons/shake.png) | [Sinh / chốt](../../games/typing-survival/art-src/_review/240/shake-before-after.jpg) |
| `reduced-motion` | [reduced-motion.c2-try2](../../games/typing-survival/art-src/ui/icons/reduced-motion.png) | [Sinh / chốt](../../games/typing-survival/art-src/_review/240/reduced-motion-before-after.jpg) |
| `stat-evenness` | [stat-evenness.try2](../../games/typing-survival/art-src/ui/icons/stat-evenness.png) | [Sinh / chốt](../../games/typing-survival/art-src/_review/240/stat-evenness-before-after.jpg) |
| `station-crest` | [station-crest.c2-try3](../../games/typing-survival/art-src/ui/icons/station-crest.png) | [Sinh / chốt](../../games/typing-survival/art-src/_review/240/station-crest-before-after.jpg) |
| `mag-empty` | [mag-empty.try3](../../games/typing-survival/art-src/ui/parts/mag-empty.png) | [Sinh / chốt](../../games/typing-survival/art-src/_review/240/mag-empty-before-after.jpg) |

- **Shake c2-try1:** đổi khung rỗng sang thiết bị đặc, lõi tinh thể lam lớn, hai bóng lệch hai bên và vạch rung dày. Dáng trung tâm là khối vuông xoay chéo; không còn màn hình rỗng. Chọn lượt đầu, không dùng thêm hai lượt còn lại.
- **Reduced Motion c2-try1 → c2-try2:** quả cầu đặc có vòng kẹp và ba vệt. Lượt đầu có quầng alpha phải sửa mạnh (4.826 pixel, tối đa 127/255 trong bước matte master), nên không chọn. Lượt 2 yêu cầu mặt vật hoàn toàn đặc, vệt lam tối hơn và giảm sắc về đầu trái, vòng kẹp chặn vệt; bước matte master còn 867 pixel, tối đa 29/255, RGB không đổi. Các vệt còn giống cánh kim loại ở bản lớn; ở 20 px đọc rõ quả cầu, còn ý “dịu lại” cần Claude xét.
- **Stat Evenness try2:** thay thanh ngang bằng ba cột cao bằng nhau, cùng lõi lam trên một bệ; thân tổng gần vuông, khoảng tối tách ba cột vẫn rõ ở 20/24 px. Không cần dùng try3.
- **Station Crest c2-try1 → c2-try2 → c2-try3:** lượt 1 là lục giác đặc, khác Chapter Crest nhưng gần Hazard (IoU alpha ≥128: 0,875354). Lượt 2 đổi sang khiên, còn 0,816092. Lượt 3 yêu cầu đỉnh phẳng, thân hẹp hơn và đáy nhọn sâu; công cụ giữ phần lớn dáng lượt 2, số IoU vẫn 0,816092. Chọn lượt 3 vì mép nguồn sạch hơn (484 pixel matte master, tối đa 10/255), vẫn giữ toàn bộ các lượt. Không bóp hình để ép qua số. Khiên chứa một trạm, không còn tháp mảnh đứng riêng.
- **Mag Empty try2 → try3:** lượt 2 tăng viền nhưng chênh với Mag Full chỉ 0,256744 ở 10 px. Lượt 3 làm tối lòng và hai đầu, tập trung vàng sáng lên viền. Hậu kỳ căn hộp bao 237×717 thành 233×716 theo vỏ Mag Full, giảm RGB toàn ảnh **5,6%**, trong giới hạn ±10%. Giữ vật liệu, lòng tối và phản lam rất nhẹ; không sửa Mag Full. Chênh đạt 0,301323 ở 10 px, IoU hai ngưỡng đều 1,00 ở 32 px.

Mọi prompt dùng nguyên văn STYLE-UI Lightbearer §4.3, khối KIND của 152/153, phần vật riêng và dòng alpha. Phần KIND của crest cho phép chính chiếc huy hiệu là vật thể, không thêm khung trình bày. Prompt tiếng Anh, báo cáo tiếng Việt. Công cụ: **image_gen.imagegen tích hợp**, không dùng CLI/API thay thế. [Nhật ký nguồn và prompt](240/generated-files.json).

Đã xem tham chiếu HUD chủ dự án, tờ 152/153, Pulse Gun chuẩn cỡ, ảnh 121 và khung 127; thêm các ảnh được nhận để đối chiếu vật liệu. Khung 127 nguồn có nền khóa; tờ xem dùng bản alpha sẵn có, không sửa nguồn.

## 2. Hậu kỳ, khổ và alpha

Nguồn sinh 1254², alpha thật. Đưa hai đầu alpha ≤16 / ≥250 về 0/255, cắt phần rỗng và căn vật có cạnh dài 717 px trên canvas 1024². Chỉ sửa matte, không phủ hay vẽ lại nội dung; bốn icon không đổi sáng RGB. Ô đạn có căn kích thước và giảm sáng toàn ảnh như trên. Bước matte ban đầu chỉ dùng ở master; không dùng bản thu đã ép matte của ứng viên trung gian để giao.

**20/20 PNG giao** đúng khổ và sRGBA/sRGB. **15/15 bản thu** giống pixel phép Lanczos trực tiếp từ master, không làm nét bản 64. Tái lập lại từ cả năm nguồn sinh trong một thư mục mới, **20/20 bản khớp pixel với bộ giao**: [kết quả replay](../../games/typing-survival/art-src/_review/240/replay-verify-final/comparison.json). [Identify](../../games/typing-survival/art-src/_review/240/identify-delivery.txt).

| Tên | Hộp bao master | Cạnh dài / canvas | Lệch tâm lớn nhất | Hue gần magenta trên pixel alpha >0 |
| --- | --- | --- | --- | --- |
| shake | 717 × 494 | 70,020% | 0,049% | 0,01296% |
| reduced-motion | 717 × 654 | 70,020% | 0,049% | 0,01279% |
| stat-evenness | 717 × 656 | 70,020% | 0,049% | 0,02514% |
| station-crest | 599 × 717 | 70,020% | 0,049% | 0,04681% |
| mag-empty | 233 × 716 | 69,922% | 0,049% | 0,09075% |

Cạnh dài 68–72%, tâm ≤2% đều đạt. Màu gần khóa tối đa cả 20 PNG **0,090754%**, dưới 0,2%; nguồn alpha thật, không dùng nền khóa. Số trên vẫn ghi theo cách đo bảo thủ H=285…315°, S>0,5.

**Ngoại lệ alpha:** dưới đây là số pixel alpha 1…254 nằm ngoài dải Euclid 3 px quanh đường bao; mỗi ô là **ngưỡng >16 / ngưỡng ≥128**. Giữ cả hai định nghĩa, không chỉ báo cách có lợi.

| Tên | 1024² | 256² | 128² | 64² |
| --- | --- | --- | --- | --- |
| shake | 0 / 0 | 53 / 0 | 27 / 3 | 17 / 3 |
| reduced-motion | 0 / 0 | 96 / 2 | 25 / 0 | 24 / 0 |
| stat-evenness | 0 / 0 | 386 / 2 | 137 / 0 | 74 / 0 |
| station-crest | 0 / 0 | 80 / 0 | 46 / 0 | 8 / 0 |
| mag-empty | 354 / 0 | 125 / 0 | 4 / 0 | 8 / 0 |

Bốn master icon đạt cả hai cách đo. Master Mag Empty sau căn kích thước đạt theo đường bao 50%, còn 354 pixel theo >16. Bản thu có đuôi alpha do Lanczos. Cách ép matte cũ xử lý được số nhưng ở Reduced Motion 64² đổi tới 112/255 tại vài pixel chi tiết; đã giữ ứng viên đó trong hồ sơ, **bản giao giữ nét Lanczos trực tiếp**. Vì [ART_ACCEPTANCE §5](../games/ART_ACCEPTANCE.md#5-hậu-kỳ-không-được-phá-tranh-29102026) yêu cầu “Khi một ngưỡng số mâu thuẫn với tranh … dừng lại, giữ tranh đẹp, ghi mâu thuẫn trong báo cáo để Claude quyết”, dừng sửa để ép số, chờ Claude chốt alpha. Không ghi “alpha sạch hoàn toàn” hoặc cho 2 điểm Dùng tiếp.

## 3. Cỡ nhỏ, tương phản và dáng

Tờ chính có ô icon **20/24 px**, thêm 30/36 px; ô đạn **10/15 px**, trên **#14181f** và **#8c96a3**. Đủ ba cặp Shake–Reduced Motion, Mag Empty–Mag Full, Station Crest–Chapter Crest ở **20/30 px** trên cả hai nền. Có cỡ 720p và 1080p theo 152/153, bốn icon cũ và mảnh HUD thương mại cùng cao, khung 127 và cảnh 121.

Luma sRGB Y′ = 0,2126R′ + 0,7152G′ + 0,0722B′, trung bình màu vật theo trọng số alpha; chênh với luma nền, không phải tỷ lệ WCAG.

| Tên | Cỡ canvas px | Chênh than chì | Chênh thép sáng |
| --- | ---: | ---: | ---: |
| shake | 20 | 0,442785 | 0,048029 |
| shake | 24 | 0,442084 | 0,048730 |
| shake | 30 | 0,442807 | 0,048007 |
| shake | 36 | 0,440835 | 0,049979 |
| reduced-motion | 20 | 0,433112 | 0,057702 |
| reduced-motion | 24 | 0,434366 | 0,056448 |
| reduced-motion | 30 | 0,435601 | 0,055213 |
| reduced-motion | 36 | 0,434503 | 0,056312 |
| stat-evenness | 20 | 0,414236 | 0,076578 |
| stat-evenness | 24 | 0,421355 | 0,069459 |
| stat-evenness | 30 | 0,416428 | 0,074386 |
| stat-evenness | 36 | 0,418299 | 0,072515 |
| station-crest | 20 | 0,363403 | 0,127411 |
| station-crest | 24 | 0,361642 | 0,129172 |
| station-crest | 30 | 0,361454 | 0,129360 |
| station-crest | 36 | 0,361197 | 0,129617 |
| mag-empty | 10 | 0,253245 | 0,237569 |
| mag-empty | 15 | 0,250357 | 0,240457 |
| mag-empty | 20 | 0,245071 | 0,245743 |
| mag-empty | 30 | 0,238238 | 0,252576 |

Tất cả icon vượt 0,25 trên than chì. **Mag Empty đạt 0,25 tại cỡ dùng 10/15 px**; không tuyên bố đạt tại master, 20 hoặc 30 px (đó là ô so cặp bổ sung). Ô đạn có biên khá sát, nên cách thu khi tích hợp cần giữ nguyên.

| Cỡ | Luma rỗng | Luma đầy đã nhận | Chênh |
| --- | ---: | ---: | ---: |
| 10 px | 0,346009 | 0,647333 | 0,301323 |
| 15 px | 0,343122 | 0,643226 | 0,300104 |
| 20 px | 0,337836 | 0,649626 | 0,311790 |
| 30 px | 0,331003 | 0,650271 | 0,319268 |

IoU thu toàn canvas 32², Lanczos, hai ngưỡng alpha:

| Ảnh | IoU lớn nhất >16 · cặp | IoU lớn nhất ≥128 · cặp |
| --- | --- | --- |
| shake | 0,799242 · stat-wpm.v2 | 0,708812 · stat-new-word |
| reduced-motion | 0,684358 · stat-new-word | 0,629283 · stat-new-word |
| stat-evenness | 0,653846 · reduced-motion | 0,578512 · quality |
| station-crest | 0,778920 · hazard | 0,816092 · hazard |
| mag-empty | 1,000000 · mag-full | 1,000000 · mag-full |

Cực đại đã tính đủ 55 cặp của 152, 21 cặp của 153 và 55 cặp của bộ icon ải. Cặp trạng thái ô đạn phải ≥0,95, các tên khác ≤0,80. Shake–Reduced Motion **0,673716 / 0,587031**; Station Crest–Chapter Crest **0,597052 / 0,564384**; Mag Empty–Mag Full **1,00 / 1,00**. Bộ 152 đạt theo cả hai ngưỡng; bộ 153 đạt cả hai. Bộ ải đạt theo >16, **chưa đạt theo ≥128 do Station Crest–Hazard**. Không sửa Hazard, Chapter Crest hoặc bất kỳ ảnh đã nhận nào. [Toàn bộ cặp và số đo](../../games/typing-survival/art-src/_review/240/comparison.json).

## 4. Tờ xem và KA5

- [Tờ chính · cỡ thật](../../games/typing-survival/art-src/_review/240-sheet-small.jpg).
- [Tờ phụ · nearest để soi mất nét](../../games/typing-survival/art-src/_review/240-sheet-nearest.jpg): vùng icon phóng 4×, vùng cặp 2×, riêng ô đạn 10/15 phóng 8×; không dùng tờ phóng để thay kiểm cỡ thật.
- Năm tờ sinh/chốt ở bảng §1, đã xem; các lượt không chọn vẫn có tờ riêng trong hồ sơ.

Tự chấm **trên bản giao**, so mức hoàn thiện HUD thương mại, thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục 0–2. Các ngoại lệ kỹ thuật còn mở nên Dùng tiếp chỉ 1 ở cả năm ảnh. Điểm tự chấm không thay Claude.

| Tên | 1024² | Cỡ dùng 720p | Còn phải xem |
| --- | --- | --- | --- |
| shake | 2/2/2/2/1 → 9 | 2/1,5/2/1,5/1 → 8 | 20 px còn lõi và bóng hai bên; vạch rung mất một phần chi tiết. |
| reduced-motion | 1,5/2/2/2/1 → 8,5 | 1,5/1,5/2/2/1 → 8 | Vòng kẹp và quả cầu rõ; ba vệt vẫn có thể gợi tăng tốc thay vì dịu lại. |
| stat-evenness | 2/2/2/2/1 → 9 | 2/2/2/2/1 → 9 | Ba cột bằng nhau rõ, vân tinh thể nhỏ hòa lại. |
| station-crest | 2/2/2/2/1 → 9 | 2/1,5/2/1,5/1 → 8 | Khiên đặc còn khối ở 20 px; trạm giữa mất chi tiết; IoU với Hazard còn quá ngưỡng ≥128. |
| mag-empty | 2/2/2/2/1 → 9 | 2/1/2/2/1 → 8 | 10 px rất hẹp; rỗng/đầy tách màu rõ, nhưng lòng ô rỗng cần Claude xét trực tiếp trên nền tối. |

## 5. Bảo toàn, phạm vi và phần để lại

| KA1 · ui/icons + ui/parts | Kết quả |
| --- | ---: |
| File trước / sau | 579 / 606 |
| Thêm | 27 |
| File cũ đổi theo quyền ghi đè đúng năm tên | 31 |
| Bản sao cũ khớp MD5 | 31/31 |
| File mất / đổi ngoài danh sách cho phép | 0 / 0 |
| File cũ được bảo vệ giữ nguyên | 548/548 |

Khác luật diff chỉ thêm của 152/153: phiếu 240 cho ghi đè đúng năm bản chốt, nên có 31 thay đổi chủ động và đủ bản sao cũ trong [prev](../../games/typing-survival/art-src/_review/240/prev/). Cập nhật cả prompt cỡ thu để mỗi PNG giao có prompt đúng lượt chọn bên cạnh. Mọi try cũ và ảnh đã nhận giữ nguyên byte. [MD5 trước](../../games/typing-survival/art-src/_review/240/md5-before.txt), [sau](../../games/typing-survival/art-src/_review/240/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/240/md5-diff.txt), [kiểm giao](../../games/typing-survival/art-src/_review/240/validation-delivery.json).

Chỉ ghi đúng các tên/lượt được phép, _review/240* và hồ sơ phiếu 240. Không lệnh Git, build/test game, dev server, trình duyệt, âm thanh, public/, Tu Tiên hoặc .wt-*. Không có capture game/raw frame phải prune. Các tờ xem là hậu kỳ ảnh tài sản theo phạm vi phiếu.

**Không làm tiếp:** không sinh vượt ba lượt Station Crest hoặc tổng ba lượt Mag Empty; không chỉnh ảnh đã nhận; không ép các số alpha bằng thao tác làm hỏng nét thu. Chưa tích hợp public/ và chưa có điểm Claude. Giữ mọi nguồn, prompt, ứng viên và script để tiếp tục theo quyết định của chủ dự án. [Hướng dẫn hồ sơ và tái lập](240/README.md).

**Chủ dự án/Claude cần xem:** tờ cỡ thật, nhất là Reduced Motion có đọc đúng “dịu lại”, ô Mag Empty ở 10 px, và Station Crest ở 20 px cạnh Chapter Crest. Chốt cách xử lý ngoại lệ alpha và IoU với Hazard trước khi đóng phiếu; không coi đây là bộ đã đạt đầy đủ chỉ vì tự chấm từ 8. Không có thời điểm chờ công cụ trong lượt này.
