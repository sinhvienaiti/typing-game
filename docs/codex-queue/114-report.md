# Phiếu 114 · Wordwoven · Trời và phông xa sử thi cho map 1

Ngày giao: 29/10/2026. Làm tại repo cha `/Users/toandx/htdocs/typing-game`, trên macOS.

**Đã giao đủ 9 bản chọn, 6 bản alpha, 15 lượt sinh cùng prompt nguyên văn và các ảnh kiểm. Tự chấm M ngày/đêm = 8/8; Q từng bản chọn = 8–10. Chưa nghiệm thu: chờ Claude chấm lại; yêu cầu nền magenta ở cả bốn mép không thể đồng thời áp cho lớp núi kín đáy, góc nhìn rùa từ trên còn hơi xiên sau ba lượt, và ô đêm lặp bốn lần sẽ lặp cả mặt trăng.**

## 1. Phạm vi và nguồn

Ảnh giao ở [backdrops/w1-silverfall-epic/](../../games/typing-defense/art-src/backdrops/w1-silverfall-epic/). Không thay bộ `w1-silverfall/` cũ. Đọc chỉ đạo 28/10, bible Wordwoven, thang Q, các mục 3.3, 3.8, 6 của `03-2d-scenery-ui-vfx.md`, prompt của bộ cũ và README `tools/art-normalize`. Đã xem ảnh tham chiếu chủ dự án và `ui/title-epic/title-backdrop.png` của phiếu 113 để đối màu bóng ngọc/teal, nắng vàng, đá vôi và thác bạc.

Sinh bằng **công cụ tích hợp `image_gen`**, không dùng API/CLI tạo ảnh hay mạng khác. Mỗi lần sinh được chép nguyên byte vào `.tryN.png`; không thu nhỏ hay sửa bản thử. Mỗi bản thử và bản chọn có prompt cạnh ảnh. Hậu kỳ ghi riêng trong script và JSON, không giả làm prompt sinh. Đường dẫn nguồn công cụ nằm trong `_review/114/<tên>.tryN.source.json`.

Không chạy lệnh Git, game, build, test suite, dev server hoặc trình duyệt. Không đọc/ghi Tu Tiên, không ghi game khác, không sửa mã hoặc tài liệu khác. Không làm âm thanh vì phiếu chỉ yêu cầu ảnh. Không có frame chụp trình duyệt mới để dọn.

## 2. Bộ giao và diễn biến prompt

STYLE, SKY, RING và dòng nền M giữ nguyên văn của phiếu. Những câu bổ sung chỉ khóa đúng lỗi đã thấy; không thêm chữ vào ảnh.

| Tên | Lượt đã giữ | Bản chọn | Khổ bản chọn | Thay đổi prompt và lý do chọn |
| --- | --- | --- | --- | --- |
| `sky-day-a` | 1 | try1 | 1536 × 1024 | Prompt gốc. Mây vàng lớn, tia nắng rõ; sửa dải mép và sương bằng công cụ. |
| `sky-day-b` | 1 | try1 | 1536 × 1024 | Prompt gốc và MATCH, đính kèm `sky-day-a.try1`. Khối mây khác ô a, cùng màu và chất liệu. |
| `sky-night` | 1 | try1 | 1536 × 1024 | Prompt gốc. Có trăng sau mây, Ngân Hà và luồng đèn hổ phách; sửa mép, sương và 4 pixel tím bão hòa bằng công cụ. |
| `layer-320` | 1, 2, 3 | **try3** | 1536 × 1024 | Lượt 1 bị STYLE kéo thành cảnh đền, ruộng và thác quá gần. Lượt 2 thêm yêu cầu chỉ đá lam xám nhạt, không công trình/ruộng/rừng/thác; nội dung đúng nhưng các đỉnh tụ giữa, che rùa khi ghép. Lượt 3 chuyển đỉnh cao sang trái, nhóm phụ sang phải, mở yên núi thấp ở giữa để thấy rùa và trời. |
| `layer-220` | 1, 2 | **try2** | 1536 × 1024 | Lượt 1 có hai thác và đền nhưng dồn thành núi giữa hình. Lượt 2 chuyển khối vách cao, hai thác, ruộng và phế tích sang trái; hạ yên núi giữa, giữ đỉnh phụ bên phải. |
| `layer-140-a` | 1, 2 | **try2** | 1536 × 1024 | Lượt 1 có cổng/thác tốt nhưng che thân rùa và lớp xa. Lượt 2 chuyển cổng khổng lồ cùng thác sang phải, đường đèn/bậc thang đi lên vách đó, hạ các gờ bên trái và mở thung lũng giữa. |
| `layer-140-b` | 1 | try1 | 1536 × 1024 | Prompt gốc và MATCH, đính kèm `layer-140-a.try1`; thay từ “sky” trong MATCH bằng “scenery”. Không nhà, giữ tháp đá, ruộng, thông và một thác mảnh. Bản a sau đó đổi bố cục ở lượt 2; giữ b vì mục đích tham chiếu màu/phong cách vẫn khớp, và đã kiểm ghép chéo a/b. |
| `sky-beast` | 1 | try1 | 1536 × 1024 | Prompt gốc. Rùa ngọc/đồng hướng phải, mai mang cả quần thể phế tích, vây dài và sương kéo theo. Thu nội dung còn 94% để thêm lề sạch. |
| `sky-beast-top` | 1, 2, 3 | **try2** | **1024 × 1024** | Lượt 1 dùng SAME với rùa bên hông nhưng góc còn xiên, dáng vây rối. Lượt 2 khóa camera thiên đỉnh, đầu phải, đuôi trái, bốn vây đối xứng, chỉ mái/tán cây; dáng bóng rõ hơn. Lượt 3 nhấn chính xác 90°, chỉ thấy mặt trên, đính kèm rùa bên hông và bản top try2 làm chuẩn dáng. Kiến trúc vẫn chưa thành mặt bằng thật sự; giữ try2 vì bốn vây và đuôi gọn, rõ hơn khi làm bóng. Không sinh lượt 4. |

Tổng **15 lượt**, không ảnh nào quá 3 lượt. Tất cả `.try*` còn nguyên. Prompt bản chọn trùng prompt của lượt được chọn.

## 3. Hậu kỳ và khả năng chạy lại

Script và hồ sơ nằm trong [art-src/_review/114/](../../games/typing-defense/art-src/_review/114/). Chỉ dùng Python chuẩn và ImageMagick 7; không cài thêm thư viện.

- `prepare.py`: băm MD5 trước khi ghi vào backdrops, tạo prompt lượt 1; `ingest.py`: chép nguồn công cụ vào tên thử mới, ghi nguồn từng lượt.
- `process.py`, `final-stage.py`: hậu kỳ vòng đầu vào `stage-v1/`, `stage-final/`; giữ làm hồ sơ. Ảnh ghép đầu ở `check-v1/` **không phải bản giao**: núi dồn giữa và viền cây có vài mảng đen do lấy RGB của pixel alpha 0 làm màu sơn.
- **`process-v2.py`**: lấy RGB trực tiếp từ ảnh thử mới cho bốn lớp núi; lấp các túi sắc khóa dưới đường núi bằng sơn thật lân cận cùng cột trước khi nội suy. Không dùng RGB đen của vùng trong suốt. Dựng `stage-v2/selected/` và `stage-v2/delivery/`, là nguồn bản giao.
- **`review-v2.py`** dùng phép đo của `review.py`, thêm màu rùa đêm và cắt một ô sân cũ. Hồ sơ cuối: **`check-v2/`**.
- `supplement.py`: ghép thêm hai ô trơn b và kiểm bóng trên nền xám, đọc trực tiếp bộ đã giao; kết quả ở `supplement-v1/`.
- `publish.py`: kiểm chốt số, preflight toàn bộ tên đích, chép độc quyền các tên mới, đối chiếu SHA-256, ghi MD5 sau. `published.json` liệt kê đúng từng file đã giao.
- `audit-final.py`: đối chiếu byte bản giao, đo AA toàn cột và nối chéo a/b; kết quả ở **`audit-final.json`**.

Tách nền bằng **`tools/art-normalize/key-alpha.sh`**, với:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash tools/art-normalize/key-alpha.sh IN.png OUT.alpha.png \
  --bg '#FF00FF' --mode global --despill protect-interior --no-key-hue
```

Wrapper mặc định ghi WORK vào `tools/art-normalize/.tmp/`, nằm ngoài phạm vi được phép ghi của phiếu. Vì vậy launcher `bin/python3` và `key-dispatch.py` giữ nguyên CLI/thuật toán, chỉ chuyển biến WORK sang `_review/114/normalize-work/` trong tiến trình. Không sửa công cụ repo; tắt ghi bytecode. Công cụ cảnh báo góc dưới của lớp núi còn alpha > 8 là đúng vì lớp núi kín đáy; không coi cảnh báo này là lỗi tách trời phía trên.

Khổ nguồn của ba lượt `sky-beast-top` là 1254 × 1254. Bản chọn try2 là ảnh vuông nên không cần bỏ nội dung khi cắt giữa, thu bằng Lanczos:

```sh
/opt/homebrew/bin/magick sky-beast-top.try2.png -filter Lanczos \
  -resize '1024x1024^' -gravity center -extent 1024x1024 -strip normalized.png
```

Tám bản chọn khác vốn là 1536 × 1024, không phóng to. Hai rùa được thu nội dung 94%, đặt giữa canvas cùng khổ trên alpha; không cắt chi.

Mép dùng trọng số cosin `w(t) = (1 − cos(πt))/2`. Trời: 8% ngoài mỗi bên là profile màu theo hàng dùng chung a/b, chuyển vào tranh trong 12% kế tiếp; sương phẳng từ 80% chiều cao. Núi: 8% ngoài là vai lặng, chuyển trong 8% kế tiếp; nội suy đường núi về y = 614 hoặc 635, không pha magenta vào màu sơn. Vai 140 a/b dùng cùng màu ngọc. Đáy far/mid phẳng từ 80%, near từ 85%.

Màu sương đáy RGB cuối: 320 = `(135,178,193)`, 220 = `(36,93,111)`, 140 a/b = `(52,116,119)`. Khử sắc khóa dư bằng màu sơn lân cận, không xóa chi tiết hay làm rỗng alpha của rùa. Vòng đầu sửa 3/1 pixel ở núi 140 a/b và 64/44 pixel ở rùa bên hông/top, cộng 1/2 pixel dư sau key. Vòng cuối sửa màu thêm 19/9 pixel ở hai núi gần, 1791/655 pixel ở hai rùa trong dải hue rộng 265–355°, S > 0,15; tất cả tìm được sơn lân cận, không phải dùng màu trung tính thay thế. Số này tách riêng với chốt hue cấm 285–330°, S > 0,5.

Chạy lại hậu kỳ và kiểm vào **tên thư mục mới**, dùng các nguồn và stage trung gian đã giữ:

```sh
python3 games/typing-defense/art-src/_review/114/process-v2.py recheck-stage
python3 games/typing-defense/art-src/_review/114/review-v2.py recheck-stage recheck-review
python3 games/typing-defense/art-src/_review/114/audit-final.py audit-recheck.json
```

Các writer từ chối ghi đè. `prepare.py`, `ingest.py`, `publish.py` không chạy lại vào các tên đã tồn tại. Không cần sinh lại ảnh để tái lập hậu kỳ. **Không dùng trường `seam_after.skyline_edges` của nhật ký stage-v1**: phép đo ban đầu đọc ảnh magenta đục nên trả `[0,0]`; số cuối ở `check-v2/measurements.json` đọc alpha thật, rồi `audit-final.json` kiểm trực tiếp file đã giao.

## 4. KA1 · MD5

Băm bằng `/sbin/md5 -r` **mọi file đệ quy trong `art-src/backdrops/`**, kể cả prompt và các thư mục khác đang có.

| Mốc | Số file |
| --- | ---: |
| `_review/114/md5-before.txt` | 32 |
| `_review/114/md5-after.txt` | 86 |
| Thêm | **54** |
| Sửa | **0** |
| Xóa | **0** |

54 file mới gồm 15 PNG thử + 15 prompt thử + 9 PNG chọn + 9 prompt chọn + 6 alpha. `md5-diff.txt` chỉ có dòng dữ liệu thêm; các dòng `---`, `+++`, `@@` là đầu mục diff. `md5-summary.json` đối chiếu theo đường dẫn, không chỉ so thứ tự. `audit-final.json` xác nhận bản giao trùng byte với stage đã kiểm. Không có file bộ cũ bị thay.

## 5. Kiểm kỹ thuật 2–5 và 8

### 5.1 Khổ, nền, alpha, màu tín hiệu

**Khổ đạt:** 8 ảnh 1536 × 1024, `sky-beast-top` 1024 × 1024. Sáu alpha cùng khổ bản chọn, min/max = **0/255**. Ba trời đặc, alpha = 255 toàn ảnh.

| Bản chọn | Sai số nền 10 px mép trên | Sai số magenta lớn nhất trên cả bốn mép | Hue khóa trong lòng vật đục | Hue tín hiệu cấm trên pixel thấy được |
| --- | ---: | ---: | ---: | ---: |
| `layer-320` | 0 | **198 — xem ngoại lệ dưới** | 0% | **0 px; 0%** |
| `layer-220` | 0 | **219 — xem ngoại lệ dưới** | 0% | **0 px; 0%** |
| `layer-140-a` | 0 | **203 — xem ngoại lệ dưới** | 0% | **0 px; 0%** |
| `layer-140-b` | 0 | **203 — xem ngoại lệ dưới** | 0% | **0 px; 0%** |
| `sky-beast` | 0 | **0, đạt cả bốn phía** | 0% | **0 px; 0%** |
| `sky-beast-top` | 0 | **0, đạt cả bốn phía** | 0% | **0 px; 0%** |
| Ba ô trời | Không áp khóa nền | Không áp khóa nền | Không áp khóa nền | **0 px; 0% từng ảnh** |

“Lòng vật đục” dùng alpha ≥ 250, hue khóa 300° ± 12°, S > 0,5. Chốt tín hiệu đếm **mọi pixel alpha > 0**, hue 285–330°, S > 0,5. Không bỏ qua pixel viền để làm số 0. Mẫu số là số pixel nhìn thấy; tử số 0 cũng đồng nghĩa 0% trên toàn canvas.

**Ngoại lệ nền bốn mép:** câu kiểm 3 yêu cầu magenta ở 10 px của cả bốn phía, trong khi prompt núi yêu cầu chân núi nối hai mép ở 60/62% và sương đục kín tới đáy. Hai yêu cầu không thể cùng đúng. Giữ cấu trúc vòng trụ: magenta phía trên đường núi, sơn/sương ở hai mép phía dưới và toàn đáy. Không thêm khung magenta 10 px vì sẽ tạo khe hở trong vòng. Vì vậy **không báo đạt nguyên văn câu “cả bốn mép” cho bốn ô núi**; các số sai số thực ở bảng được giữ để chủ dự án/Claude quyết cách ghi ngoại lệ.

Lề alpha thấy được của rùa, theo trái/trên/phải/dưới: bên hông **64/57/84/87 px**; top **42/100/51/111 px**. Không chi nào chạm mép.

### 5.2 Mép ghép trước và sau

Đường núi tính từ trên ảnh, theo alpha ≥ 128. Sai số màu núi là MAE R/G/B giữa hai cột biên, theo các hàng dưới cả hai đường núi. Trời lấy trung bình dải 8% ở từng hàng; bảng ghi độ lệch kênh lớn nhất trong mọi hàng, là phép kiểm chặt hơn MAE toàn ảnh.

| Ô | Đường núi trái/phải trước → sau, px | MAE R/G/B trước → sau, /255 |
| --- | --- | --- |
| `layer-320` try3 | 504/499 → **614/614** | 10,77/7,57/5,94 → **0/0/0** |
| `layer-220` try2 | 552/563 → **614/614** | 12,95/12,98/13,75 → **0/0/0** |
| `layer-140-a` try2 | 508/508 → **635/635** | 17,86/17,96/18,13 → **0/0/0** |
| `layer-140-b` try1 | 473/474 → **635/635** | 15,72/17,98/13,23 → **0/0/0** |

Độ cao đích 614/635 là làm tròn 60/62% của 1024; sai số so với đích nguyên = **0%**; so với phần trăm toán học < 0,04%. Điểm cao nhất bốn lớp lần lượt y = **154, 180, 199, 261**, nằm trong dải của từng prompt.

| Trời | Độ lệch kênh lớn nhất trước, /255 | Sau, /255 | Biến thiên ngang trong mỗi dải mép 8% sau |
| --- | ---: | ---: | ---: |
| `sky-day-a` | 53,44 | **0** | **0** |
| `sky-day-b` | 22,82 | **0** | **0** |
| `sky-night` | 9,01 | **0** | **0** |

Không mây chạm mép ở bản chọn; dải ngoài là trời trơn theo từng hàng. Kiểm chéo **mép phải 140-a → mép trái 140-b** và **sky-day-a → sky-day-b** trên file giao: max RGBA = **0**, MAE = **0**. Không chỉ kiểm a tự nối với a.

### 5.3 Dải alpha và soi 4×

Đo bổ sung trên **toàn cột**, không giới hạn cửa sổ gần đường núi: lấy tất cả pixel alpha 13–242 (xấp xỉ 0,05–0,95); nếu khoảng từ pixel đầu tới cuối dài hơn 3 px thì đếm cột đó. Cách này còn tính cả những đoạn rời, nên bảo thủ hơn chỉ đếm một dải liên tục.

| Lớp | Cột có khoảng AA > 3 px | Tỉ lệ | Ngưỡng |
| --- | ---: | ---: | ---: |
| 320 | 40/1536 | **2,60%** | ≤ 5%, đạt |
| 220 | 48/1536 | **3,13%** | ≤ 5%, đạt |
| 140-a | 37/1536 | **2,41%** | ≤ 5%, đạt |
| 140-b | 55/1536 | **3,58%** | ≤ 5%, đạt |

Các cột dốc có khoảng AA dài nhất 30/46/62/39 px; không giấu cực đại này, nhưng tiêu chí của phiếu xét **tỉ lệ cột**, không đòi mọi cột ≤ 3 px. Số đếm toàn cột ở `audit-final.json`; không dùng số cửa sổ ±8 trong bản kiểm đầu thay cho phép đo này.

[114-edge.jpg](../../games/typing-defense/art-src/_review/114-edge.jpg) phóng đúng 4× bằng nearest-neighbour, trên nền tối và sáng. Đã xem thêm từng crop ở nguyên cỡ trong `check-v2/edge-*.jpg`: không còn viền hồng liên tục hoặc lỗ đen do hậu kỳ vòng đầu. Còn vài nét lam/tối ở cạnh vách rất dốc; cần xem cùng ảnh đầy đủ, không tự nhận viền hoàn hảo ở mọi pixel.

### 5.4 Thử vòng

[114-ring.jpg](../../games/typing-defense/art-src/_review/114-ring.jpg): mỗi ô rộng **384 px**; hai lớp xa xếp ô/lật/ô/lật; 140 xếp a/b lật/b/b lật; trời ngày xếp a/b lật/b/b lật, đêm xếp cùng ô/lật xen kẽ.

**Không thấy đường nối màu hoặc bậc gãy tại x = 384/768/1152 khi xem tờ đầy đủ.** Dải vai lặng hai bên khá rộng, nên nhìn ra nhịp nhóm núi và khoảng nghỉ; đây là dấu lặp nội dung, không phải mép lệch màu. Vòng đêm có **bốn mặt trăng** khi dùng cùng một ô bốn lần. Giữ phép thử đúng phiếu và ghi rõ lỗi bố trí này; không che trong tờ kiểm.

## 6. Ảnh ghép, đọc nhỏ và bóng rùa

- [Ngày](../../games/typing-defense/art-src/_review/114-composite-day.jpg): **1536 × 1024**, sky-day-a → rùa alpha thu **45%**, giữa trên tại y = 0 → 320 → 220 → 140-a, đều theo alpha. Thấy cổng/thác phải, hai thác trái, các lớp núi lam và thung lũng giữa; thân, đầu và vây lớn của rùa tách được khỏi vách.
- [Đêm](../../games/typing-defense/art-src/_review/114-composite-night.jpg): cùng kích thước/thứ tự, thay sky-night. Trên RGB sRGB mã hóa, ba lớp núi nhân **R × 0,36; G × 0,45; B × 0,58**, giữ alpha. **Bổ sung ngoài ví dụ phiếu:** rùa cũng nhân **R × 0,50; G × 0,62; B × 0,78** để không giữ nắng vàng ban ngày giữa trời đêm. Chỉ đổi trong ảnh kiểm, không sửa PNG tài sản dùng chung.
- [Tờ so](../../games/typing-defense/art-src/_review/114-vs-ref.jpg): hai ảnh mới và ảnh chủ dự án cùng **cao 640 px phần hình**; bên dưới là ghép bộ cũ sky-a/320/220/140-a. Có chú thích “đứng cạnh được” và lý do dưới từng ảnh mới. Chữ chỉ ở tờ kiểm, không nằm trong tài sản.
- [Hai ảnh ghép nhỏ](../../games/typing-defense/art-src/_review/114/check-v2/small-composites.jpg): mỗi ảnh **384 × 256**. [Từng ô nhỏ](../../games/typing-defense/art-src/_review/114/check-v2/small-tiles.jpg) để chấm Q riêng.
- [Ghép hai ô trơn b](../../games/typing-defense/art-src/_review/114/supplement-v1/composite-plain.jpg), [bản 384 px](../../games/typing-defense/art-src/_review/114/supplement-v1/composite-plain-small.jpg): kiểm thêm sky-day-b và 140-b trên cảnh hoàn chỉnh, không chỉ dùng điểm từ ảnh a.

**Đọc ở 384 px:**

| Ý cần đọc | Ngày | Đêm |
| --- | --- | --- |
| Tháp đá cao | Rõ vách sáng, rừng trên đỉnh, tầng lam phía sau | Đọc rõ dáng và tầng lam, chi tiết đá tối hơn |
| Thác bạc | Nhận rõ hai vệt trái và thác lớn phải | Vệt bạc vẫn tách khỏi rừng tối |
| Cổng đá | Vòm cổng lớn bên phải và đường bậc thang còn đọc được | Vòm còn đọc được; từng đèn nhỏ không còn tách riêng |
| Quái thú | Nhận ra đầu phải, mai mang phế tích và vây dài | Nhận ra dáng rùa, mai và vây; phế tích đọc theo khối |

[114-beast-shadow.jpg](../../games/typing-defense/art-src/_review/114-beast-shadow.jpg) dùng ảnh sân có sẵn `games/.wt-td-1c/tmp/lane-l/td-1c-ground-sheet-1920x1080.jpg`, chỉ đọc. File mang tên 1920×1080 nhưng thực tế là tờ **2608 × 1504**; cắt một ô `632×352+660+380`, thu/phóng thành **1920 × 1080** để kiểm dáng bóng trên một sân, thay vì phủ một bóng qua nhiều ô của tờ so. Đây là mock trên ảnh có sẵn, không phải capture runtime mới.

Bóng lấy `sky-beast-top.alpha`, RGB đen, **alpha × 0,35**, Gaussian **sigma 24 px**, đặt giữa. [Bóng trên nền xám](../../games/typing-defense/art-src/_review/114/supplement-v1/shadow-on-grey.jpg) để đối chứng: nhận ra mai, đầu phải, đuôi trái và bốn vây; lên sân xanh vẫn nhận ra dáng lớn nhưng đầu/vây qua mảng đá và đường vàng đọc yếu hơn. Chưa chứng minh chuyển động hay chiếu bóng theo camera 3D, vì phiếu cấm chạy game.

## 7. KA5 · Mức chợ và Q

Đây là **Codex tự chấm**, mốc chủ dự án = **M 9**; chưa phải Claude duyệt. M của ô phông chấm trong cảnh ghép, không lấy tranh lẻ đẹp làm đủ. Hai rùa xét thêm chất lượng cutout và dáng bóng; không gán M 8 cho sân cũ trong ảnh mock.

| Cảnh đánh giá | M đầy đủ | M ở 384 px | So với tham chiếu |
| --- | ---: | ---: | --- |
| Ghép ngày với a | **8** | **8** | Đứng cạnh được: có rùa lớn làm thước đo, cổng/vách trăm mét, thác, tầng sương, ánh vàng có hướng và đá/rừng hoàn thiện. Chưa tới 9 vì vai vòng và đáy sương còn phẳng, chưa có tiền cảnh sân thật. |
| Ghép đêm | **8** | **8** | Đứng cạnh được: trời hội đèn, trăng sau mây, rùa và các lớp núi lam có chiều sâu. Kiến trúc tối, cần chỉnh sáng trong lần tích hợp riêng; không chấm cao hơn vì đèn trên cổng chưa thật nổi sau phép nhân màu. |
| Ghép các ô trơn b | **8** | **8** | Vẫn đọc được thế giới đá vôi và rùa lớn; bớt điểm nhấn kiến trúc đúng vai trò ô trơn. Gần và giữa dày chi tiết hơn cảnh a. |

Q theo thứ tự **đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau**, mỗi mục 0–2. Chấm ở kích thước đầy đủ và 384 px; Q không thay các chốt kỹ thuật bắt buộc.

| Bản chọn | M để đối chiếu | Q đầy đủ | Q ở 384 px | Phần còn thiếu |
| --- | ---: | --- | --- | --- |
| `sky-day-a` | 8, cảnh ngày | **10** (2/2/2/2/2) | **10** | Dải mép lặng rộng là yêu cầu ghép, không phải trời tự nhiên toàn ảnh. |
| `sky-day-b` | 8, cảnh b | **9** (2/2/2/2/1) | **9** | Nhịp mây lặp vẫn nhận thấy khi trải vòng. |
| `sky-night` | 8, cảnh đêm | **9** (2/2/2/2/1) | **9** | Lặp tile sẽ lặp cả mặt trăng; cần xử lý bố trí riêng trước tích hợp. |
| `layer-320` | 8, cảnh ngày/đêm | **9** (2/2/2/2/1) | **9** | Vai và sương đáy phẳng; gần mép nhìn rõ nhịp cụm núi lặp. |
| `layer-220` | 8, cảnh ngày/đêm | **9** (2/2/2/2/1) | **9** | Vài cạnh dốc còn nét lam/tối; hai thác và phế tích vẫn rõ. |
| `layer-140-a` | 8, cảnh ngày/đêm | **9** (2/2/2/2/1) | **9** | Cổng đúng tầm, đường đèn nhỏ đọc thành nhịp sáng; còn mép vách cần Claude xem. |
| `layer-140-b` | 8, cảnh b | **9** (2/2/1/2/2) | **9** | Ruộng và rừng sáng/dày hơn a; cùng palette nhưng độ nhộn nhịp hơi khác. |
| `sky-beast` | **8**, cutout và cảnh | **9** (2/2/2/1/2) | **9** | Quần thể trên mai rất dày, có vài vây/đuôi chồng nhau trong góc bên hông. |
| `sky-beast-top` | **8**, bộ rùa và bóng | **8** (1/2/2/1/2) | **8** | Đúng dáng rùa để làm bóng nhưng kiến trúc còn xiên, **chưa phải camera 90° hoàn toàn** sau ba lượt. |

Ảnh top đã hết ba lượt. Nếu Claude không nhận góc nhìn: đề xuất dựng/render orthographic từ một model rùa tương ứng, hoặc sửa riêng mái/phế tích theo mặt bằng bằng một phiếu sau; không cố ép méo ảnh để giả camera thẳng đứng. Không tạo model hay chạy render 3D trong phiếu này.

## 8. Khác phiếu và việc cần duyệt

1. **Bốn mép magenta của núi:** giữ yêu cầu vòng trụ kín đáy, báo trung thực phần kiểm bốn mép không đạt nguyên văn; bảng số đo ở mục 5.1. Cần thống nhất ngoại lệ trước nghiệm thu đầy đủ.
2. **Góc rùa top:** giữ try2 tốt nhất sau ba lượt, hạ Q xuống 8 và ghi phần chưa đúng; cần Claude xem dáng bóng cùng ảnh top, không chỉ nhìn điểm tổng.
3. **Trời đêm lặp trăng:** phép thử vòng theo phiếu có bốn trăng. Cần một phương án đặt trăng một lần hoặc ô đêm trơn trong bước riêng; không sửa runtime hay tự thêm tài sản thứ mười trong phiếu này.
4. **Tham chiếu b:** ô 140-b dùng a try1 làm chuẩn; a đổi bố cục ở try2 sau lần kiểm ghép. Giữ b vì màu/phong cách vẫn khớp; đã đo nối chéo và dựng cảnh b riêng, không tự tuyên bố đã sinh b với a try2 đính kèm.
5. **Ảnh kiểm đêm và bóng:** thêm nhân màu rùa đêm; cắt một ô trong tờ sân cũ để kiểm bóng rõ. Công thức và hộp cắt đã ghi ở mục 6.

**Cần chủ dự án/Claude xem:** [tờ so](../../games/typing-defense/art-src/_review/114-vs-ref.jpg), [vòng ghép](../../games/typing-defense/art-src/_review/114-ring.jpg), [mép 4×](../../games/typing-defense/art-src/_review/114-edge.jpg), [bóng trên sân](../../games/typing-defense/art-src/_review/114-beast-shadow.jpg), và `sky-beast-top.alpha.png`. Chưa đóng nghiệm thu khi chưa có Claude chấm lại M ≥ 8, Q ≥ 8 và giải quyết các ngoại lệ trên. Bộ media mới đã giao đủ; không có thay đổi runtime, âm thanh, model hoặc bộ cũ.
