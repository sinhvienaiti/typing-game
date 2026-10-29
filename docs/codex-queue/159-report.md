# Phiếu 159 · Wordwoven · Làm lại vòng trời và phông xa

Ngày giao: 29/10/2026, macOS. Nguồn: phiếu 114, báo cáo 114 và mục «114, bảy ô vòng» trong bản chấm nhận 29/10.

**Đã giao 8 ô `.v2.png`, 4 alpha và prompt cạnh từng PNG; giữ nguyên toàn bộ bản cũ. Năm vòng không còn bị tách thành đảo bởi vai phẳng; vòng đêm chỉ có một mặt trăng. Tự chấm hình ảnh M = 8, Q = 8–9 trên bản hậu kỳ. Chưa nghiệm thu kỹ thuật: các ngưỡng mép/alpha cũ và một số pixel tím còn tồn tại, ghi số thật ở dưới để Claude quyết, không dùng điểm M/Q để coi các chốt này đã qua.**

## 1. Bộ giao

Thư mục: [backdrops/w1-silverfall-epic/](../../games/typing-defense/art-src/backdrops/w1-silverfall-epic/).

| Tên | Nguồn tranh | Bản mới | Việc đã làm |
| --- | --- | --- | --- |
| `sky-day-a` | try1 của 114 | `.v2.png` | Bỏ hậu kỳ phẳng cũ; chỉ hòa mép a/b, giữ mây và tia nắng. |
| `sky-day-b` | try1 của 114 | `.v2.png` | Giữ khối mây gốc; hòa hai mối với a. |
| `sky-night` | try1 của 114 | `.v2.png` | Giữ trăng, mây và đèn; hòa hai mối với b. |
| `sky-night-b` | **1 lượt sinh mới** | `.v2.try1.png`, `.v2.png` | Cùng màu đêm, ít đèn hơn, không trăng. |
| `layer-320` | try3 của 114 | `.v2.png`, `.v2.alpha.png` | PNG đục nguyên byte nguồn; tách nền lại, không nắn núi. |
| `layer-220` | try2 của 114 | `.v2.png`, `.v2.alpha.png` | PNG đục nguyên byte nguồn; giữ sông, thác, đền và sương gốc. |
| `layer-140-a` | try2 của 114 + hai dải nối mới | `.v2.png`, `.v2.alpha.png` | Giữ cổng/thác giữa ô; chỉ ghép tranh sinh tại hai mép. |
| `layer-140-b` | try1 của 114 + hai dải nối mới | `.v2.png`, `.v2.alpha.png` | Giữ núi/ruộng giữa ô; nối với a bằng cùng hai dải tranh. |

Mỗi bản chọn có `.v2.prompt.txt`; mỗi alpha có `.v2.alpha.prompt.txt`. Với hai ô 140, hồ sơ prompt ghi nguyên văn prompt nguồn và cả hai prompt sửa nối, có nhãn phân biệt. Các thao tác công cụ nằm trong script/JSON, không giả làm prompt sinh.

Vùng trời trong suốt của bốn ô núi chiếm khoảng **40,9–44,8% khung**; giữ các khoảng sương/sông có sẵn, không thêm chi tiết để lấp chúng. Điểm nhấn của a vẫn là cổng lớn; ruộng theo xanh ngọc và vàng lúa, riêng b còn sáng/dày hơn a nên bị trừ điểm hợp bộ.

Không giao lại hai ảnh rùa đã được người chấm nhận; chỉ đọc `sky-beast.alpha.png` khi dựng cảnh kiểm.

## 2. Sinh ảnh và hậu kỳ

Dùng skill `imagegen` và công cụ tích hợp **image_gen**, không dùng API/CLI tạo ảnh hay mạng khác. Tổng **3 lượt mới**: một ô đêm và hai dải nối 140. Mỗi dải nối dùng cho cả a/b; mỗi ô 140 nhận hai lượt sửa trong phiếu này, không vượt ba lượt. Giữ nguyên byte ba kết quả sinh và prompt cạnh ảnh.

Ô đêm đính kèm `sky-night.try1.png`, tức bản tranh trước hậu kỳ làm hỏng của 114. Prompt nguyên văn:

```text
Same night sky style, colours and lanterns as the attached image, but no moon: the milky way continues across, fewer lanterns, high thin clouds.
```

Hai dải nối bắt đầu đúng câu người chấm yêu cầu:

```text
Continue the karst range naturally across the middle; keep both sides unchanged.
```

Phần bổ sung khóa khung, màu, đá vôi, thác, ruộng xanh ngọc/vàng lúa trầm, nền magenta và vùng được sửa. Dải phải bổ sung giữ cổng bên trái; dải trái bỏ riêng câu đó. Prompt đầy đủ ở [dải phải](../../games/typing-defense/art-src/_review/159/join-140-right.try1.prompt.txt) và [dải trái](../../games/typing-defense/art-src/_review/159/join-140-left.try1.prompt.txt). Hai nguồn 768 × 1024 được ghép từ 25% mép tương ứng của a/b, theo đúng chiều lật thực tế.

Kết quả sửa nối có khổ 1086 × 1448, cùng tỉ lệ 3:4; thu Lanczos về 768 × 1024. Chỉ ghép vùng x = 154…613 của dải, tương ứng **230 px mỗi ô**, tức 15% cặp ô quanh mối nối. Hòa mép ngoài bằng mặt nạ cosin 32 px. **1.076 cột giữa mỗi ô giữ RGB gốc**, bao gồm điểm nhấn cổng và thác. Không dùng phần sinh lại ở ngoài dải được phép.

Trời hòa a/b trong **115 px mỗi mép**, theo cặp pixel ở cùng khoảng cách đến mép; trọng số từ 1/2 tại đường nối về 0 ở đầu trong. Đây là trộn hai phần tranh có sẵn, không phải profile màu theo hàng hay dải trời trơn. Phần giữa giữ nguyên RGB. Không đổi gamma hoặc độ sáng tài sản.

Tách nền bằng `tools/art-normalize/key-alpha.sh`, `ART_MAGICK=/opt/homebrew/bin/magick`, các tùy chọn:

```text
--bg #FF00FF --mode global --despill protect-interior --no-key-hue
```

Launcher và `key-dispatch.py` chỉ chuyển WORK vào `_review/159/normalize-work/`; không sửa công cụ repo, không ghi vào `tools/art-normalize/.tmp/`. Cảnh báo góc dưới còn alpha là đúng vì núi/sương kín đáy. Kiểm riêng dải trái 3 px của **cả bốn alpha: 0 pixel tím thấy được** trong hue 255–355°, S > 0,15; không còn cột tím cũ ở 140-a.

**Không thêm dải màu sương ở đáy.** Bản gốc đã có sương chuyển mềm; yêu cầu hòa về một màu chung được dừng ở đây vì luật hậu kỳ mới chỉ cho sửa mép, tách nền, đổi cỡ và chỉnh sáng nhẹ, cấm phủ màu/thay phần vẽ. Không ép đáy sang màu lớp 320, không cắt dải kem, không tạo vai 60/62%, không làm đồng màu dải 8%. Giữ tranh và ghi các ngưỡng chưa qua thay vì làm phẳng để lấy số.

## 3. Vòng 360° và tờ so

[159-ring.jpg](../../games/typing-defense/art-src/_review/159-ring.jpg): năm vòng, đặt cạnh tham chiếu chủ dự án. Hai hàng đầu là trời ngày/đêm; ba hàng sau chồng thêm lần lượt 320, 220, 140 theo alpha. Mỗi vòng nguồn **6144 × 1024** gồm bốn ô 1536 × 1024; bản trình bày mới thu nhỏ.

Ngày, đêm và 140: **a | b lật | b | b lật**. Với 320/220, a và b cùng một ảnh; thứ tự vẫn là ảnh | ảnh lật | ảnh | ảnh lật. Ô có trăng/cổng chỉ xuất hiện một lần. Không buộc mép trái và phải cùng một ô phải giống nhau: các mối tự lật đã trùng pixel sẵn.

| Vòng | Nhận xét khi kiểm vòng và crop 1:1 | M tự chấm theo cảnh vòng hậu kỳ |
| --- | --- | ---: |
| Ngày | **Liền như một dãy núi** trong cảnh chồng lớp; vòm mây không còn bị cắt thành cụm bằng dải trời trơn. | 8 |
| Đêm | **Liền như một dãy núi** trong cảnh đêm chồng lớp; đúng một trăng, b không trăng; nhịp Ngân Hà còn lặp gương. | 8 |
| 320 | **Liền như một dãy núi**; tháp xa và yên núi chạy tới chỗ nối, không vai phẳng. | 8 |
| 220 | **Liền như một dãy núi**; thung lũng/sông liên tục, không khe sương trống giữa đảo. | 8 |
| 140 | **Liền như một dãy núi**; hai dải sửa nối cổng/ruộng sang núi trơn, không tạo đường chân núi ngang. | 8 |

M đánh giá cảnh vòng có các tầng núi và trời, không gán M của cả thế giới cho riêng một ô trời. Còn nhịp lặp gương của núi/ruộng, vòng 140 hơi dày, cảnh đêm tối hơn tham chiếu; chưa chấm lên 8,5. Không sinh toàn cảnh 4:1 cho lớp nào vì điều kiện «còn thành đảo cách nhau bởi dải phẳng» không còn xảy ra. Không thêm dải phẳng bằng công cụ.

Ảnh kiểm:

- [Bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/159/raw-vs-final/): tám tờ, mỗi bên 1536 × 1024, cùng nền magenta khi so alpha; bốn tờ `.opaque.jpg` bổ sung so đúng PNG đục. Không cắt khung nguồn.
- [Cảnh ngày](../../games/typing-defense/art-src/_review/159-composite-day.jpg), [cảnh đêm](../../games/typing-defense/art-src/_review/159-composite-night.jpg), [tờ so kèm bộ cũ](../../games/typing-defense/art-src/_review/159-vs-ref-full.jpg).
- [Mép 4×](../../games/typing-defense/art-src/_review/159-edge.jpg): cả bốn núi, mép trái/phải, nền sáng/tối; không có cột tím liên tục hay vai bị san.
- [Kiểm nguyên cỡ và cỡ nhỏ](../../games/typing-defense/art-src/_review/159/checks/): `ring-*-full.jpg` giữ 6144 × 1024 phần hình; `joins-*-1to1.jpg` ghép bốn crop nối **không thu nhỏ**, gồm mối khép vòng; từng ô nhỏ rộng 384 px. Có cả `stack-night-140.png` cho vòng đêm chồng đủ tầng.

Cảnh ngày/đêm một góc giữ rùa đã nhận, thu 45%, đặt giữa trên. Phép nhân màu **chỉ trong ảnh kiểm đêm**: núi R/G/B × 0,36/0,45/0,58; rùa × 0,50/0,62/0,78, giữ alpha. Đây là mô phỏng ánh sáng theo phiếu 114, không phải sửa màu PNG giao. Ở 384 px vẫn nhận ra tháp đá, thác, cổng và dáng rùa; đêm đọc kiến trúc theo khối, đèn nhỏ yếu. Không chứng minh camera/ánh sáng runtime vì phiếu cấm chạy game.

## 4. Số đo và chốt chưa qua

Tất cả 12 PNG chọn/alpha đúng **1536 × 1024**; bốn alpha min/max **0/255**, bốn trời **255/255**. [measurements.json](../../games/typing-defense/art-src/_review/159/measurements.json) đo stage đã xem; [audit-final.json](../../games/typing-defense/art-src/_review/159/audit-final.json) kiểm hash, khổ, prompt và màu trên chính file giao.

| Núi | Đường núi trái/phải, px từ trên | Cột có khoảng alpha 13–242 dài >3 px | Sai số nền 10 px trên / cả bốn mép | Hue khóa trong vật đục | Hue tín hiệu cấm thấy được |
| --- | --- | --- | --- | --- | --- |
| 320 | 503 / 499 | 293/1536 = **19,08%** | 18 / 229 | 0% | **0 px** |
| 220 | 551 / 562 | 246/1536 = **16,02%** | 17 / 249 | 0% | **1 px** |
| 140-a | 473 / 407 | 272/1536 = **17,71%** | 12 / 255 | 0,000231% | **4 px** |
| 140-b | 473 / 410 | 348/1536 = **22,66%** | 13 / 255 | 0,000324% | **6 px** |

Alpha đo toàn cột bằng khoảng từ pixel bán trong đầu tới cuối, giữ cùng cách kiểm bảo thủ của 114; cực đại lần lượt 25/91/115/55 px. **Chưa đạt ngưỡng ≤5%**, không hạ ngưỡng hoặc bẻ cây/đá để tự công bố đạt. Các pixel tím rời rạc có cả pixel đục, tọa độ ghi trong audit; không phải cột tím ở mép. Giữ phần sơn bên trong thay vì quét màu cả vật: **chốt 0% màu tín hiệu chưa qua ở ba alpha**, dù hue khóa đục vẫn thấp hơn 0,5%. Ô đêm b có thêm 8 pixel hue 285–330°, S > 0,5 trong trời sao; phép đo mở rộng này cũng được giữ nguyên, không ghi thành 0.

Ngưỡng nền 10 px cả bốn phía mâu thuẫn với núi/sương kín đáy; dải trên nguồn cũng chưa đều trong ±12 ở 320/220/140-b. Alpha trời phía trên đã tách, không sửa nền nguồn thành mảng mới chỉ để qua số. Đường núi không đúng mốc 614/635 của phiếu cũ; 320 còn giữ đỉnh gốc y = 210 thay vì kéo lên 15%. Đây là các chốt cần Claude quyết theo luật mới giữ tranh.

| Trời | Sai khác lớn nhất giữa trung bình hai dải 8%, /255 | Mối thực tế a/b sau hòa |
| --- | ---: | --- |
| Ngày a | 38,740 | RGBA MAE/max = 0 tại hai cột ghép |
| Ngày b | 26,569 | Như trên |
| Đêm a | 21,667 | RGBA MAE/max = 0 tại hai cột ghép |
| Đêm b | 69,341 | Như trên |

**Cả bốn không qua luật ≤6/255 của hai dải 8%**; mây tự nhiên vẫn chạy tới mép, không ép dải này thành trời trơn. Trước hòa, ba nguồn trời cũ có sai khác 53,44/22,82/9,01 theo hồ sơ 114. Không dùng chỉ số tự so trái/phải để thay chỉ số nối đúng a.phải/b.phải và b.trái/a.trái.

Mối 320/220 tự lật: MAE/max RGBA = 0. Mối 140 sau sửa là hai cột **kề nhau của cùng tranh sinh**, có biến thiên chi tiết tự nhiên: MAE RGB phải = **15,377/13,159/9,835**, trái = **8,745/9,633/5,464**, alpha MAE = 0,759/0. Chưa đạt nguyên văn ≤8 từng kênh của luật cũ. Crop 1:1 không đọc thành vết cắt cảnh; không hòa thành cột sơn phẳng để ép chỉ số về 0.

Q theo đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau:

| Bản chọn | Q đầy đủ / 384 px | Thành phần | Thiếu còn lại |
| --- | --- | --- | --- |
| sky-day-a | 9 / 9 | 2/2/2/2/1 | Chờ ngoại lệ dải 8%. |
| sky-day-b | 9 / 9 | 2/2/2/2/1 | Nhịp mây lặp gương. |
| sky-night | 9 / 9 | 2/2/2/2/1 | Mật độ đèn a cao hơn b. |
| sky-night-b | 9 / 9 | 2/2/2/2/1 | Ngân Hà lặp; tám pixel tím rời. |
| layer-320 | 8 / 8 | 1/2/2/2/1 | Đỉnh/mép khác mốc cũ, alpha vượt ngưỡng. |
| layer-220 | 9 / 9 | 2/2/2/2/1 | Một pixel tím và alpha vượt ngưỡng. |
| layer-140-a | 9 / 9 | 2/2/2/2/1 | Bốn pixel tím; cần duyệt hai dải nối. |
| layer-140-b | 8 / 8 | 2/2/1/2/1 | Ruộng sáng và dày hơn a; sáu pixel tím. |

## 5. KA1, hồ sơ và việc bỏ qua

MD5 bằng `/sbin/md5 -r`, đệ quy toàn `art-src/backdrops/`: **86 → 112 file, thêm 26, sửa 0, xóa 0**. Gồm 12 PNG chọn/alpha + 12 prompt + 1 lượt đêm + prompt lượt đêm. [md5-before.txt](../../games/typing-defense/art-src/_review/159/md5-before.txt), [md5-after-relative.txt](../../games/typing-defense/art-src/_review/159/md5-after-relative.txt), [diff chỉ thêm](../../games/typing-defense/art-src/_review/159/md5-diff-relative.txt), [published.json](../../games/typing-defense/art-src/_review/159/published.json). Kiểm SHA-256: 12 PNG giao trùng byte stage đã xem. Lần kiểm kê đầu so đường dẫn tương đối với tuyệt đối nên dừng assertion; giữ hồ sơ đó, không sửa tài sản. Bản `*-relative` là kết quả chốt đã chuẩn hóa đường dẫn, không có thay đổi file cũ.

Script ở [_review/159/](../../games/typing-defense/art-src/_review/159/): `prepare.py`, `finish.py`, `review.py`, `publish.py`, `audit-final.py`, `key-dispatch.py`; nguồn ba lượt mới có SHA-256 trong audit. Có thể dựng lại hậu kỳ/ảnh kiểm từ nguồn đã giữ, vào tên mới để tránh ghi đè:

```sh
python3 games/typing-defense/art-src/_review/159/finish.py recheck-1
python3 games/typing-defense/art-src/_review/159/review.py recheck-1
```

Không sinh toàn cảnh 360° vì năm vòng không còn thành đảo; không dùng thêm lượt để lấy điểm số bằng thay phần vẽ. Không làm lại rùa hoặc bóng rùa đã được nhận; đối chứng bóng vẫn ở [114-beast-shadow.jpg](../../games/typing-defense/art-src/_review/114-beast-shadow.jpg). Không chỉnh runtime, model, bộ cũ, âm thanh, mã game, tài liệu game hay Tu Tiên. Không chạy Git, build, test suite, server hoặc trình duyệt. Không tạo capture trình duyệt nên không có raw frame cần prune; hồ sơ ảnh hậu kỳ khoảng 200 MB, giữ để tái lập.

**Cần Claude xem:** [vòng mới](../../games/typing-defense/art-src/_review/159-ring.jpg), [so nguồn/hậu kỳ](../../games/typing-defense/art-src/_review/159/raw-vs-final/), [mép 4×](../../games/typing-defense/art-src/_review/159-edge.jpg), các crop nối 1:1 và bảng chốt chưa qua ở mục 4. Chỉ đổi sang `.v2` sau khi người chấm duyệt hình ảnh và quyết các xung đột kỹ thuật; phiếu này chưa đổi tài sản đang dùng.
