# Phiếu 128 · Wordwoven · Ảnh nguồn Tripo cho năm mốc khổng lồ

Ngày giao: 29/10/2026. Làm tại repo cha `/Users/toandx/htdocs/typing-game`, macOS.

**Đã sinh đủ năm mốc, giữ tám lượt sinh và prompt; bộ hậu kỳ đề nghị giao ở `_review/128/final-review/` qua kiểm 2–5, tự chấm M 8–8,5 và Q 9–10. Chưa đóng phiếu ở đường dẫn bản chọn chính: các PNG đã ghi sớm trong `landmarks-epic/` còn ba lỗi hue nền; tháp đèn ở đó vẫn là try2. Đã hỏi chủ dự án cho phép thay các bản chọn và ba tờ kiểm bằng bộ đã kiểm, chưa có câu trả lời tại lúc lập báo cáo. Không tự coi thời gian chờ là chấp thuận.** Claude vẫn cần chấm lại M và Q trước khi gửi danh sách dựng Tripo cho chủ dự án.

## 1. Phạm vi, nguồn và phần đã làm

- Bộ nguồn: [landmarks-epic/](../../games/typing-defense/art-src/landmarks-epic/). Tám `.tryN.png` là bản chép nguyên byte từ công cụ tích hợp **image_gen**, có `.tryN.prompt.txt` đúng prompt đã gửi cạnh từng ảnh. Có đủ năm `.png` và năm `.prompt.txt` bản chọn đầu.
- Bộ hậu kỳ đề nghị nhận: [final-review/](../../games/typing-defense/art-src/_review/128/final-review/). Năm PNG 1254 × 1254 và prompt cạnh ảnh; năm alpha chỉ phục vụ kiểm/ghép, không phải model.
- Hồ sơ: [scripts và số đo](../../games/typing-defense/art-src/_review/128/). `sources.json` và `sources-try3.json` lưu đường dẫn ảnh gốc do công cụ trả về.
- Đã đọc `ART_DIRECTION_2026-10-28.md` (thang M, bible Wordwoven), `ART_ACCEPTANCE.md` (thang Q, §5), prompt Fort và §3.1, §3.5, §3.7 bộ yêu cầu Tripo. Đã xem ảnh mẫu chủ dự án, Fort, lính, `td-1c-models-sheet.jpg`, màn tựa 113 và cảnh ghép ngày 114. Không sao chép nội dung ảnh mẫu.
- Không gọi Tripo, Meshy hoặc API 3D; không dùng CLI/API sinh ảnh khác, mạng ngoài image_gen, trình duyệt, dev server, build hay test game; không chạy lệnh Git. Không đọc/ghi các đường dẫn Tu Tiên, không ghi game khác. Không làm âm thanh vì phiếu chỉ yêu cầu ảnh nguồn.

Khối MODEL, TAIL và dòng nền giữ nguyên văn. Cả năm dùng **M · #FF00FF**, vì MODEL có rêu ngọc/patina xanh. Luật cũ “không đèn lồng, không gỉ xanh” trong gói Tripo được yêu cầu riêng của phiếu 128 thay thế; vẫn giữ camera, chân, ánh sáng và cấu trúc dựng được.

## 2. Các lượt sinh và prompt đã sửa

| Mốc | Lượt giữ | Lượt đề nghị nhận | Diễn biến |
| --- | --- | --- | --- |
| `guardian-statue` | 1 | try1 | Prompt nguyên văn. Tượng tướng thế tục bằng đá, hai tay trên chuôi kiếm, giáp phiến, mũ, vai mẻ và bệ vuông. Không thêm chi tiết tôn giáo. |
| `stone-gate` | 1 | try1 | Prompt nguyên văn. Ba vòm thông, vòm giữa cao nhất, mái ngói cong, mây cuộn, vòng mặt trời và dây leo bên phải. |
| `lantern-tower` | 1, 2, 3 | **try3** | Try1 có huy hiệu giống chữ triện. Try2 khóa huy hiệu/đèn về mây và mặt trời, thêm yêu cầu tháp dân sự, nắp nóc đá và bố cục vuông; huy hiệu lớn hết giống chữ nhưng một miếng đồng nhỏ dưới mái vẫn đáng ngờ. Try3 khóa các khớp, miếng đồng nhỏ thành mặt trơn; thân đèn đồng đặc, không sáng, hoa văn mây lớn. Hết ba lượt. Try3 sạch ký tự hơn nhưng tay đỡ thành mây, nét rồng không còn rõ; ghi thiếu và trừ đúng đề. |
| `karst-pillar` | 1 | try1 | Prompt nguyên văn. Một trụ đá vôi có rãnh đứng, rừng xanh trên đỉnh, thủy đình nhỏ và thác bám mặt đá; toàn bộ từ chân cắt tới mái trong khung. |
| `dragon-stair` | 1, 2 | **try2** | Try1 tự thêm cổng có mái trên chiếu nghỉ. Try2 khóa chiếu nghỉ thành sàn đá lộ thiên có lan can thấp; nhấn hai lan can rồng dài dạng rắn, mõm dài, bờm chảy và sóng uốn liên tục, gắn liền thân cầu thang. Đã bỏ được mái cổng thừa. |

Mỗi lần sinh là một ảnh riêng, không dùng ảnh trước làm đích sửa và không gọi thêm lượt ngoài bảng.

## 3. Hậu kỳ bảo toàn tranh

Không cắt giữa vì ảnh dọc sẽ mất đỉnh hoặc chân, trái §5. Thay vào đó: tách nền, thêm lề vuông trong suốt, đổi về 1128 × 1128 rồi thêm lề tới 1254 × 1254 và ghép lại nền magenta. **Đây là khác cách cắt giữa trong phiếu để giữ toàn bộ phần vẽ**, vẫn đúng khổ cuối. Không kéo dãn riêng chiều rộng/cao của vật; không chỉnh sáng, gamma, màu vật liệu; không tô lại mảng đá, rừng, hoa văn hoặc thác.

Lệnh nền, được script truyền bằng danh sách đối số, tương đương:

```sh
magick input.png -alpha on -fuzz 18% -transparent '#FF00FF' source-alpha.png
magick source-alpha.png -background none -gravity center \
  -extent SxS -filter Lanczos -resize 1128x1128! -extent 1254x1254 \
  -background '#FF00FF' -alpha remove -alpha off output.png
```

`S = max(rộng nguồn, cao nguồn)`. Tách màu toàn ảnh gồm lỗ vòm và khoảng hở trong đèn, tương đương phép tách nền của phiếu 106 nhưng không chỉ flood-fill góc ngoài.

Đo vòng đầu phát hiện màu nền pha ở mép sau nội suy. Bộ `final-review/` thêm bước sửa mép **sau đổi cỡ, trước ghép lại nền**:

```text
-channel A -fx 'a*(g<=r && g<=b && (max(r,b)-g)>0.5*max(r,b) && abs(r-b)<=0.2*(max(r,b)-g) ? 0 : 1)' +channel
```

Điều kiện này chỉ tách pixel có hue magenta ±12° và bão hòa >0,5; nhân alpha cũ để giữ phần vốn trong suốt. Các màu đó bị cấm trong vật ngay từ prompt. Không thay RGB của phần vẽ còn lại. Đã xem cả năm PNG hậu kỳ nguyên cỡ, năm tờ trước/sau và hàng 256 px: đá, hoa văn, lá, thác và cấu trúc còn nguyên, không có mảng san phẳng hoặc phủ màu để đạt số.

**Lỗi quy trình của lượt này:** đã ghi năm bản chọn đích trước khi kiểm hue hoàn tất. Sau khi có số lỗi, giữ nguyên các file đã ghi theo luật cấm ghi đè và chuẩn bị bộ sửa riêng. Không nói rằng ba bản đích này đã qua kiểm 3. Việc xin thay chỉ áp cho sản phẩm do chính lượt này tạo, không đụng file có trước mốc KA1.

Các nhánh thử giữ lại trong review: `edge-refined/` là thử alpha lỗi, làm nền đen do không nhân alpha cũ, **loại hoàn toàn**; `edge-clean/` sửa được alpha nhưng còn tháp try2; `final-review/` dùng tháp try3. Không xóa nhánh thử hoặc `.try*`. Đây là thử công cụ, không phải lượt sinh bổ sung. Các file `vs-ref.jpg` trung gian có chú thích lệch vị trí; bản xem đúng cuối là `final-review/vs-ref-caption.jpg`, ghép chú thích thành ô riêng ngoài hình.

## 4. Số đo bộ hậu kỳ đề nghị nhận

Số đầy đủ: [final-review/metrics.json](../../games/typing-defense/art-src/_review/128/final-review/metrics.json). Lề theo **trái / trên / phải / dưới**. Màu nền đo cả dải 10 px bốn phía. Hue trong vật dùng đúng mẫu số pixel có ít nhất một kênh lệch nền >60; không loại pixel viền khỏi phép đo hue.

| Mốc | Khổ nguồn | Khổ cuối | Sai số mép R/G/B | Hue nền trong vật | Lề, px | Vùng liền >1% ảnh |
| --- | --- | --- | --- | --- | --- | ---: |
| guardian-statue try1 | 1024 × 1536 | 1254 × 1254 | 0/0/0 | 401/340618 = **0,117727%** | 342/82/342/78 | **1** |
| stone-gate try1 | 1312 × 1199 | 1254 × 1254 | 0/0/0 | 627/611020 = **0,102615%** | 82/129/76/135 | **1** |
| lantern-tower try3 | 1254 × 1254 | 1254 × 1254 | 0/0/0 | 612/379114 = **0,161429%** | 356/79/353/81 | **1** |
| karst-pillar try1 | 1145 × 1374 | 1254 × 1254 | 0/0/0 | 486/437221 = **0,111157%** | 376/76/349/79 | **1** |
| dragon-stair try2 | 1254 × 1254 | 1254 × 1254 | 0/0/0 | 484/674128 = **0,071796%** | 138/77/129/82 | **1** |

Tất cả qua ngưỡng cạnh vuông, nền ≤12/kênh, hue ≤0,5%, lề trái/phải/trên ≥37,62 px và dưới ≤150,48 px. Hộp bao lấy mọi pixel alpha >0 sau tách nền; vùng liền dùng alpha ≥128, nối 8 hướng. Vùng phụ lớn nhất của cổng/karst chỉ 8/3 px, không phải vật thứ hai. Không tự xóa các vùng nhỏ để ép phép đếm.

**Bản chọn đầu đang nằm ở đường dẫn chính:**

| Mốc | Hue hiện tại | Kiểm hue |
| --- | ---: | --- |
| guardian-statue | 0,301772% | Đạt |
| stone-gate | **0,657226%** | Chưa đạt |
| lantern-tower, vẫn try2 | **0,757595%** | Chưa đạt; còn chi tiết giống ký tự |
| karst-pillar | **0,592291%** | Chưa đạt |
| dragon-stair | 0,224323% | Đạt |

Kiểm nhìn bộ `final-review/`: không chữ, số, logo, chữ ký, khung; không tượng thần/Phật, bàn thờ, lư hương, chuông chùa hay đồ cúng. Tượng là tướng cầm kiếm, đèn là đèn đồng không thắp, thủy đình là kiến trúc nghỉ chân trống. Rồng là chạm khắc kiến trúc. Chân là mặt cắt của model; không có nền đất, đường hoặc bóng đổ ngoài vật. Các mặt chân xiên trên ảnh là do camera 3/4, không ép thành một đường ngang bằng cách cắt tranh.

## 5. Tờ kiểm và thang kích thước

Các tờ gốc đúng tên yêu cầu đã được tạo: [128-scale.jpg](../../games/typing-defense/art-src/_review/128-scale.jpg), [128-vs-ref.jpg](../../games/typing-defense/art-src/_review/128-vs-ref.jpg), [128-small.jpg](../../games/typing-defense/art-src/_review/128-small.jpg). Chúng phản ánh bản chọn đầu, gồm tháp try2; không dùng để chứng nhận bộ sửa cuối.

**Xem bộ cuối ở đây**:

- [Tờ thang cuối](../../games/typing-defense/art-src/_review/128/final-review/scale.jpg): cùng vạch đất y=840, **22 px/m**, chiều cao hình lần lượt 484/352/308/748/220 px cho 22/16/14/34/10 m; Fort 176 px cho 8 m; lính 40 px cho 1,8 m (làm tròn). Chỉ co/phóng đều, không kéo ngang để đồng thời ép cả rộng lẫn cao. Cổng 18 m và cầu thang rộng 8 m là kích thước 3D dự kiến, chưa thể kiểm chính xác bề ngang thế giới từ một ảnh chiếu 3/4.
- [So tham chiếu cuối](../../games/typing-defense/art-src/_review/128/final-review/vs-ref-caption.jpg): tờ thang và ảnh chủ dự án cùng cao **640 px phần hình**; dưới là hàng thứ ba bộ model hiện có (Fort, nhà mái ngói, vách đá), cắt nguyên hàng rồi đổi cỡ. Chú thích ở ô riêng, không phủ lên ảnh.
- [Năm ô đúng 256 × 256](../../games/typing-defense/art-src/_review/128/final-review/small.jpg), sau đó mới cộng ô nhãn bên dưới. Không phóng vật lên riêng để giả khả năng đọc ở cỡ nhỏ.
- Tờ **bản sinh | bản hậu kỳ**, mỗi ô hình 640 × 640, giữ trọn ảnh: [tượng](../../games/typing-defense/art-src/_review/128/final-review/guardian-statue-before-after.jpg), [cổng](../../games/typing-defense/art-src/_review/128/final-review/stone-gate-before-after.jpg), [tháp đèn](../../games/typing-defense/art-src/_review/128/final-review/lantern-tower-before-after.jpg), [karst](../../games/typing-defense/art-src/_review/128/final-review/karst-pillar-before-after.jpg), [cầu thang](../../games/typing-defense/art-src/_review/128/final-review/dragon-stair-before-after.jpg).

**Đứng cạnh được:** các khối đá cổ, bệ tượng, vòm lớn và trụ karst làm Fort cùng lính nhỏ lại; đá vôi sáng, mái ngói và khối chắc vẫn liên hệ được bộ model hiện có. Bộ mới chi tiết hơn, mái/rêu trầm hơn bộ cũ, chưa phải cảnh có ánh sáng điện ảnh. Không lấy tờ nguồn ánh sáng phẳng làm chứng cứ rằng camera 55° trong game đã đạt: chưa dựng 3D hay chạy game theo phạm vi phiếu.

## 6. KA5 · Codex tự chấm trên hậu kỳ cuối

Mốc chủ dự án = M9. M dưới đây chấm chất lượng **nguồn model** cùng tờ thang, không gán chất lượng cảnh MMO cho ảnh nền magenta. Q theo thứ tự **đúng đề / đọc được / hợp bộ / hình khối / dùng tiếp**, mỗi mục 0–2.

| Bản cuối đề nghị | M đầy đủ | M 256 px | Q đầy đủ | Q 256 px | Mức và phần còn thiếu |
| --- | ---: | ---: | --- | --- | --- |
| guardian-statue try1 | **8,5** | **8** | **9** (2/2/1/2/2) | **9** (2/2/1/2/2) | Đạt tự chấm. Dáng tướng và kiếm mạnh; giáp/chạm dày hơn model cũ, chi tiết giáp nhỏ gom lại ở 256 px. |
| stone-gate try1 | **8,5** | **8,5** | **9** (2/2/1/2/2) | **9** (2/2/1/2/2) | Đạt tự chấm. Ba vòm và khối mái rõ, đá/đồng hoàn thiện; mức chi tiết dày và palette ngói trầm hơn bộ cũ. |
| lantern-tower try3 | **8** | **8** | **9** (1/2/2/2/2) | **9** (1/2/2/2/2) | Đạt tự chấm tổng điểm, có thiếu riêng: tay đỡ thành mây, không còn đọc rõ rồng; góc này chỉ thấy hai đèn mỗi tầng, không chứng minh đủ bốn quanh tầng. Đã hết ba lượt; cần Claude quyết nét nhận diện này. |
| karst-pillar try1 | **8,5** | **8,5** | **9** (2/2/1/2/2) | **9** (2/2/1/2/2) | Đạt tự chấm. Vách cao và thủy đình làm thước; đá/rừng gần chất liệu minh họa hơn bộ cũ, vài dây leo nhỏ cần chủ dự án chú ý khi dựng. |
| dragon-stair try2 | **8,5** | **8** | **10** (2/2/2/2/2) | **9** (2/2/2/1/2) | Đạt tự chấm. Hai lan can dài và chiếu nghỉ trống đúng đề; ở 256 px các sóng rồng và bậc nhỏ sát nhau, chi tiết thân bớt tách rõ. |

Điểm này chưa thay Claude duyệt. Không sửa tài liệu `ART_REPLACE_LATER.md` vì ngoài phạm vi cho ghi; phần thiếu đã ghi ngay trong báo cáo.

## 7. KA1 · MD5 trước/sau

Mốc trước được lập bằng `md5 -r` trên mọi file của `games/typing-defense/art-src/` trước khi ghi ảnh/prompt. Kết quả:

| Phép kiểm | Kết quả |
| --- | ---: |
| File ở mốc trước | **5.634** |
| File ở mốc sau, trước khi tạo chính snapshot sau | **6.349** |
| Dòng file thêm | **715** |
| File cũ đổi hash | **0** |
| File cũ mất | **0** |
| Dòng dữ liệu bị trừ trong `diff -u` | **0** |

`diff` chỉ có dòng thêm. Số thêm là **toàn cây đang có người khác làm đồng thời**, không nhận toàn bộ 715 file là do phiếu này tạo. Không phục hồi hay sửa file của người khác. Snapshot sau bao gồm snapshot trước và các script/ảnh review đã có tại lúc chụp; không tự băm `md5-after.txt` vào chính nó.

[md5-before.txt](../../games/typing-defense/art-src/_review/128/md5-before.txt) · [md5-after.txt](../../games/typing-defense/art-src/_review/128/md5-after.txt). Lệnh: `python3 games/typing-defense/art-src/_review/128/audit.py`; dùng `md5 -r` theo lô và `diff -u`, không Git.

## 8. Chạy lại và việc cần xem

Script lưu trong `_review/128/`: `bootstrap.py` lưu cách lập baseline/prompt đầu; `review.py` là vòng đầu; `review-edge-refined.py` là thử lỗi giữ lại; `review-edge-clean.py` sửa alpha; **`review-final.py` là bộ hậu kỳ cuối**, `caption.py` ghép chú thích ngoài hình, `audit.py` chốt MD5. Các script ảnh không ghi đè output đã có; `bootstrap.py`/`audit.py` dừng khi snapshot đích đã tồn tại. `commands.json` ở từng nhánh lưu lệnh ImageMagick đã chạy. Crop soi chi tiết tháp: `magick lantern-tower.try2.png -crop 90x100+612+170 +repage -resize 540x600 _review/128/lantern-roof-detail.jpg` (đường vào thực tế nằm trong `landmarks-epic/`). Không có capture trình duyệt để prune; `.try*` giữ nguyên theo phiếu.

**Cần chủ dự án/Claude xem:** bộ `final-review/`, tờ so cuối, năm tờ trước/sau và riêng thiếu nét rồng của tháp try3. Đề nghị nhận bộ cuối sau khi Claude chấm M ≥8, Q ≥8; việc dựng năm model Tripo là của chủ dự án. Hiện chưa thay các bản chọn chính do câu cấm ghi đè; câu hỏi xin thay đã nêu rõ đây là sửa lỗi ghi bản chọn sớm trong chính lượt làm này. Không báo hoàn tất đúng đường dẫn khi phép thay chưa được trả lời.
