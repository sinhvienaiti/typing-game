# Phiếu 150 · Last Line · Đã giao đủ bộ, chờ Claude chấm nhận

## Chạy tiếp 31/10/2026 · bắt đầu 01:24, giờ Việt Nam

Đã tạo đủ **11 ảnh chọn 1024² và 33 bản thu 256², 128², 64²**, nền alpha thật, sRGB RGBA. Có **12 bản sinh được giữ nguyên**: mười ảnh dùng lượt 1, riêng `load-guns` dùng lượt 2. Mọi bản sinh, bản chọn và bản thu đều có prompt tiếng Anh bên cạnh. Công cụ tích hợp `image_gen.imagegen` đã hoạt động; lượt này không gặp HTTP 429.

**Kết quả tự kiểm:** 44/44 file đúng khổ và kênh; alpha sạch ngoài mép 3 px ở cả hai ngưỡng dựng mặt nạ; hộp bao 70,020%; lệch tâm lớn nhất 0,098%; màu khóa còn lại dưới 0,061%; IoU lớn nhất 0,745. Tự chấm KA5 ở cỡ 720p từ **8 đến 10**. Đây là hồ sơ giao để Claude chấm lại, chưa phải xác nhận nghiệm thu của Claude hay chủ dự án.

**Điểm cần xem khi duyệt:** Shard giữ kính đen theo Lightbearer, đạt chênh luma trên nền thép sáng nhưng không đạt 0,25 trên nền than chì; hợp bộ chân dung kính đen `.v2` hơn sáu bản gốc màu thép. Hai hạn chế được ghi rõ ở phần tương phản và KA5, không tăng sáng hoặc sửa chân dung cũ để che chúng.

### 1. File giao và prompt qua từng lượt

Đường dẫn dưới đây tính từ `games/typing-survival/art-src/`. Với mỗi tên có `.png`, `.prompt.txt`, `.256.png`, `.128.png`, `.64.png` và prompt tương ứng của từng bản thu. Bản sinh nằm ở `.tryN.png`, prompt nguyên văn ở `.tryN.prompt.txt`.

| Tên / thư mục | Lượt chọn | Cỡ 720p / 1080p | Nội dung và sửa prompt |
| --- | ---: | --- | --- |
| `ui/icons/objective` | 1 | 20 / 30 | Giữ prompt đã chuẩn bị: bốn ngàm ngắm bao quanh cờ cyan cắm trên chân kim loại. |
| `ui/icons/hazard` | 1 | 20 / 30 | Giữ prompt: tấm lục giác, ba mảng lớn chia bằng vết nứt cam. |
| `ui/icons/learning-rule` | 1 | 20 / 30 | Giữ prompt: sách dữ liệu mở, trang sáng và tia sét cyan. |
| `ui/icons/equipment` | 1 | 20 / 30 | Giữ prompt: hai súng bắt chéo trên giá đỡ. |
| `ui/icons/warning` | 1 | 16 / 24 | Giữ prompt: tam giác vàng cam và gai nổi liền khối, không dấu chấm than. |
| `ui/icons/new-badge` | 1 | 16 / 24 | Giữ prompt: huy hiệu sao tám cánh, mặt trơn, hai đuôi ruy băng cyan. |
| `ui/icons/station-crest` | 1 | 20 / 30 | Giữ prompt: vòng trạm, tháp nhọn, hố đen và vành bồi tụ cam. |
| `ui/icons/chapter-crest` | 1 | 32 / 48 | Giữ prompt: hai trụ cao, đường đắp và hai ray sáng ở giữa. |
| `ui/icons/load-guns` | 2 | 20 / 30 | Lượt 1 đúng đề nhưng mũi hướng nạp có quầng alpha rộng. Lượt 2 chỉ đổi đoạn mô tả vật: băng đạn cắm một phần vào khe dưới thân súng, động tác đọc qua vị trí cơ khí; ánh sáng nằm trong vật liệu đặc. Giữ nguyên STYLE, KIND, tham chiếu và dòng nền. Không cắt bỏ quầng của tranh lượt 1. |
| `ui/icons/back` | 1 | 20 / 30 | Giữ prompt: mũi tên quay lại trên tấm kim loại cùng dáng. |
| `ui/foes/shard` | 1 | 20 / 30; thẻ ải 40 / 60 | Giữ prompt: ba mũi kính đen, lõi nứt cam và hai vuốt nhỏ; tham chiếu thêm Swarm gốc và v2. |

Đã dùng nguyên văn STYLE-UI §4.3 hướng B trong `jobs.json`; không quay về khối phong cách công nghiệp cũ của phiếu 015. Các tham chiếu gồm `gun-xung.norm.256.png`, `panel-large.alpha.png` của 127 và `briefing-bg.png` của 121, cùng Swarm cho Shard. Đã xem ảnh HUD chuẩn của chủ dự án để đối chiếu mức hoàn thiện. Lệnh đầu tiên bị bộ kiểm tham số từ chối vì đường dẫn tương đối; đổi sang đường dẫn tuyệt đối trên Mac, không đổi prompt, không tính là lượt sinh.

Nguồn file công cụ trả về và danh sách 12 bản sinh: [generated-files-20261031.json](../../games/typing-survival/art-src/_review/150/generated-files-20261031.json). Không chuyển sang API hoặc công cụ tạo ảnh khác.

### 2. Hậu kỳ và bảo toàn tranh

Bản công cụ trả về không luôn là 1024² và thường có alpha phần đặc ở 252–253/255. Bước đầu đo theo mọi alpha >0 đã tính cả lớp rất mờ vào lề, khiến vật chỉ còn 57–68%; đã giữ lại kết quả đầu để đối chiếu, rồi căn theo hộp bao **alpha >16** đúng phiếu.

Quy trình cuối: đưa hai đầu matte 16/250 về 0/255, cắt khoảng rỗng theo hộp bao, thu đồng đều để cạnh dài 717 px, căn giữa canvas 1024². Sau đó sửa riêng điểm alpha trung gian ở ngoài mép 3 px; giữ khử răng cưa trong mép. Không đổi màu, gamma, độ sáng RGB, không phủ mảng hoặc thay phần vẽ. Tờ trước/sau đã được xem cho cả 11 ảnh, kiểm lại riêng Equipment, Station Crest và Load Guns sau lần sửa mép cuối.

Mép 3 px được đo bằng khoảng cách Euclid tới ranh giới mặt nạ, kiểm độc lập tại **alpha >16 và >127**. Bản giao 1024² và cả 33 bản thu đều có **0 pixel alpha trung gian ngoài dải mép** ở cả hai phép kiểm. Các bản thu lấy **trực tiếp từ bản 1024² cuối bằng Lanczos**, sau đó sửa riêng matte để đáp ứng kiểm alpha; không làm nét RGB, kể cả bản 64. Đây là bước sửa mép sau phép thu, không phải chuỗi thu 1024→256→128→64.

Kiểm sửa matte cuối ghi **0 pixel RGB bị đổi** cho mọi file so với đầu vào cùng khổ. Phần lớn sửa alpha là 1–10/255. Ở bản 1024², số điểm sửa mạnh hơn 16/255 nhiều nhất là 71/1.048.576 pixel của Equipment; Station Crest có 67. Bản 64 của Equipment có 46 điểm alpha được sửa, trong đó 17 điểm đổi hơn 16 mức; không thay nét vẽ RGB. Claude nên xem cả PNG gốc và bản 64 khi duyệt mép nhỏ này. [Số đo đầy đủ](../../games/typing-survival/art-src/_review/150/delivery-matte-audit-20261031.json).

Giữ nguyên mọi `.try*`, các bản hậu kỳ trung gian trong `_review/150/`, và các tờ xem trước lần sửa matte cuối. Những lần cập nhật bản chọn và bản thu trong lượt này chỉ tác động file mới tạo trong chính lượt này; **không file nào đã tồn tại ở đầu lượt bị thay đổi hoặc mất** theo KA1.

### 3. KA1 · MD5 trước và sau

Không ghi đè manifest cũ. Lượt này dùng hậu tố `resume2`: [trước](../../games/typing-survival/art-src/_review/150/md5-resume2-before.txt), [sau](../../games/typing-survival/art-src/_review/150/md5-resume2-after.txt), [diff](../../games/typing-survival/art-src/_review/150/md5-resume2-diff.txt), [JSON](../../games/typing-survival/art-src/_review/150/md5-resume2-summary.json).

| Kiểm | Kết quả |
| --- | ---: |
| File trước | 383 |
| File sau | 600 |
| Đường dẫn thêm | 217 |
| File đã có bị đổi | **0** |
| File đã có bị mất | **0** |
| Dòng dữ liệu bị xóa trong diff | **0** |

Đã gọi `/sbin/md5 -r` trên toàn bộ `ui/icons/`, `ui/foes/`, `_review/150/` và các file `_review/150-*`. Manifest sau được chốt trước khi ghi chính nó, diff và JSON tổng kết, tránh băm đệ quy. Báo cáo nằm ngoài cây media được băm. Các con số trước khác lượt 30/10 vì dùng đúng trạng thái thư mục hiện tại, không tái sử dụng checkpoint cũ.

### 4. Khổ, alpha, màu khóa và dáng

`magick identify -format '%f %wx%h %[channels]\n'` đã chạy trên **44 file giao**, tất cả đúng 1024²/256²/128²/64² và `srgba`. Kiểm bổ sung xác nhận `sRGB` và prompt bản chọn/bản thu trùng prompt lượt được chọn. [Kết quả identify](../../games/typing-survival/art-src/_review/150/identify-delivery-20261031.txt), [xác nhận tổng](../../games/typing-survival/art-src/_review/150/validation-20261031.json).

Trong bảng: A = số pixel alpha trung gian ngoài mép 3 px, **0 cho cả bốn khổ và cả hai ngưỡng mặt nạ**; M = tỷ lệ pixel còn alpha >0 có hue cách magenta 300° tối đa 15° và S >0,5, đo trên bản 1024². Không dùng nền khóa để sinh; M là phép kiểm bảo thủ theo phiếu, có thể tính cả màu nhấn thật.

| Ảnh | Cạnh dài hộp bao | Lệch tâm lớn nhất | A | M (%) | IoU lớn nhất ở 32 px, alpha >16 / ảnh ghép cặp |
| --- | ---: | ---: | ---: | ---: | --- |
| objective | 70,020% | 0,049% | 0 | 0,0609 | 0,549 · hazard |
| hazard | 70,020% | 0,049% | 0 | 0,0424 | 0,745 · new-badge |
| learning-rule | 70,020% | 0,049% | 0 | 0,0151 | 0,713 · hazard |
| equipment | 70,020% | 0,049% | 0 | 0,0310 | 0,629 · shard |
| warning | 70,020% | 0,049% | 0 | 0,0181 | 0,597 · new-badge |
| new-badge | 70,020% | 0,049% | 0 | 0,0238 | 0,745 · hazard |
| station-crest | 70,020% | 0,098% | 0 | 0,0539 | 0,615 · learning-rule |
| chapter-crest | 70,020% | 0,049% | 0 | 0,0219 | 0,623 · hazard |
| load-guns | 70,020% | 0,049% | 0 | 0,0335 | 0,551 · hazard |
| back | 70,020% | 0,049% | 0 | 0,0563 | 0,669 · hazard |
| shard | 70,020% | 0,049% | 0 | 0,0582 | 0,654 · learning-rule |

Cả 55 cặp đều ≤0,80; kiểm thêm mặt nạ alpha >127 có cực đại **0,699**. Phiếu không có cặp sáng/tắt nên không áp dụng ngưỡng ≥0,95. [Hộp bao, luma, màu khóa](../../games/typing-survival/art-src/_review/150/metrics-delivery-20261031.json); [toàn bộ cặp IoU và kiểm từng khổ](../../games/typing-survival/art-src/_review/150/native-audit-delivery-20261031.json).

### 5. Cỡ thật và tương phản

Dùng luma Rec.709 trên sRGB 0–1, trung bình theo trọng số alpha của vật; lấy trị tuyệt đối chênh với nền. Cặp số trong bảng là **than chì `#14181f` / thép sáng `#8c96a3`**. Đây là chênh luma theo phiếu, không phải tỷ số WCAG.

| Ảnh | 1024² | 720p, đúng số px | 1080p, đúng số px |
| --- | --- | --- | --- |
| objective | 0,317 / 0,174 | 20: 0,325 / 0,166 | 30: 0,318 / 0,173 |
| hazard | 0,359 / 0,132 | 20: 0,359 / 0,132 | 30: 0,358 / 0,132 |
| learning-rule | 0,491 / 0,000 | 20: 0,488 / 0,003 | 30: 0,489 / 0,001 |
| equipment | 0,380 / 0,111 | 20: 0,379 / 0,112 | 30: 0,382 / 0,109 |
| warning | 0,405 / 0,086 | 16: 0,404 / 0,086 | 24: 0,406 / 0,085 |
| new-badge | 0,448 / 0,042 | 16: 0,451 / 0,039 | 24: 0,448 / 0,042 |
| station-crest | 0,332 / 0,159 | 20: 0,334 / 0,157 | 30: 0,332 / 0,159 |
| chapter-crest | 0,367 / 0,124 | 32: 0,367 / 0,124 | 48: 0,368 / 0,123 |
| load-guns | 0,370 / 0,121 | 20: 0,370 / 0,121 | 30: 0,370 / 0,121 |
| back | 0,482 / 0,009 | 20: 0,475 / 0,016 | 30: 0,479 / 0,012 |
| shard | 0,199 / 0,292 | 20: 0,199 / 0,291 | 30: 0,200 / 0,291 |

Shard trong thẻ ải: 40 px **0,199 / 0,291**, 60 px **0,199 / 0,291**. Tất cả đạt ≥0,25 trên ít nhất một trong hai màu nền **được phiếu chỉ định**. Câu “hai nền tối” được hiểu theo hai mã màu ngay trong phiếu, vì màu thép thứ hai thực tế là sáng. **Không tuyên bố Shard đạt 0,25 trên than chì.** Nếu Claude yêu cầu riêng nền tối cho chân dung, đây là chốt cần xử lý tiếp; chưa tăng sáng quá giới hạn ±10% hoặc đổi kính đen sang vật liệu sáng để ép số.

### 6. KA5 · Chấm trên bản hậu kỳ so với game thương mại

Thứ tự năm điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**. Hai cột chấm độc lập ở khổ gốc và đúng cỡ 720p. “Dùng tiếp” nhận 2 theo kiểm số của bộ giao và cách hiểu hai nền đã nêu; nhận xét về nền dùng thực tế của Shard vẫn cần Claude duyệt.

| Ảnh | Gốc: năm điểm → tổng | 720p: năm điểm → tổng | Điểm còn thiếu ở cỡ thật |
| --- | --- | --- | --- |
| objective | 2/2/2/2/2 → **10** | 2/1/2/2/2 → **9** | Cờ đọc được; ngàm ngắm còn nhiều trang trí khi thu 20 px. |
| hazard | 2/2/2/2/2 → **10** | 2/1/2/2/2 → **9** | Lục giác và vết nứt rõ, vân vật liệu hòa lại. |
| learning-rule | 2/2/2/2/2 → **10** | 2/1/2/2/2 → **9** | Sách và tia sáng còn rõ; lớp trang mất ở 20 px. |
| equipment | 2/2/2/2/2 → **10** | 2/1/2/2/2 → **9** | Dáng X rõ, giá đỡ nhỏ khó tách khỏi báng súng. |
| warning | 2/2/2/2/2 → **10** | 2/2/2/2/2 → **10** | Tam giác và gai sáng đọc được ở 16 px. |
| new-badge | 2/2/2/2/2 → **10** | 2/1/2/2/2 → **9** | Đọc thành huy hiệu sao; hai đuôi nhỏ ở 16 px. |
| station-crest | 1/2/2/2/2 → **9** | 1/1/2/2/2 → **8** | Có thêm các trụ phụ so với mô tả gọn; vòng và hố đen hơi nhập ở 20 px. |
| chapter-crest | 2/2/1/2/2 → **9** | 2/2/1/2/2 → **9** | Hai trụ và đường đắp rõ; độ sâu mạnh hơn các icon phẳng cùng bộ. |
| load-guns | 1/2/2/2/2 → **9** | 1/1/2/2/2 → **8** | Băng đạn có mặt, nhưng trạng thái đang trượt khó phân biệt với súng đã nạp ở 20 px. |
| back | 2/2/2/2/2 → **10** | 2/2/2/2/2 → **10** | Mũi tên quay lại rõ. |
| shard | 2/2/1/2/2 → **9** | 2/1/1/2/2 → **8** | Ba mũi và lõi cam rõ hơn trong thẻ ải 40 px; kính đen khác sáu bản gốc màu thép. |

### 7. Tờ xem và kiểm riêng Shard

- [Tờ chính 150-sheet.jpg](../../games/typing-survival/art-src/_review/150-sheet.jpg): hàng 1 ảnh hậu kỳ ở 256 px; hàng 2 đúng cỡ 1080p trên hai nền; hàng 3 đúng cỡ 720p trên hai nền; hàng 4 bốn icon sẵn có và mảnh HUD chuẩn cùng cao 96 px, thêm Shard 40/60 px. Tên nằm dưới ảnh; không phóng lớn cỡ thật.
- Mười một tờ trước/sau nằm trong [`_review/150/`](../../games/typing-survival/art-src/_review/150/), theo tên `<tên>-before-after.jpg`. Hai bên cùng ô 512 px, thể hiện toàn bộ canvas nguồn/chọn, để thấy cả thay đổi lề lẫn nội dung tranh.
- [Shard cạnh sáu chân dung, 40 px](../../games/typing-survival/art-src/_review/150-shard-portraits.jpg): hai hàng đầu dùng **đúng sáu PNG gốc**, trên nền tối và sáng; hàng 3 thêm đối chiếu bộ `.v2` đã có. Không sửa sáu chân dung.

**Kết luận hợp bộ Shard:** cùng cách trình bày vật thể đơn, không khung ngoài; ánh lạnh bên trái và viền cam bên phải phù hợp. Dáng tam giác và ba mũi phân biệt Swarm tròn. So với sáu bản gốc, Shard sáng cam hơn và vật chiếm khung lớn hơn Swarm gốc; **hợp bộ ở mức một phần**, chấm Hợp bộ 1. So với bộ v2 kính đen thì vật liệu và ánh sáng liền bộ hơn. Giữ quy cách căn giữa, lề 70% theo phiếu, không làm lệch tâm Shard xuống dưới để bắt chước vị trí lệch của `swarm.png` cũ.

### 8. Script, sai khác và việc còn lại

Script trong `_review/150/`, chạy bằng Node trực tiếp trên macOS và ImageMagick 7 `/opt/homebrew/bin/magick`, font Arial hệ thống:

- `finish-20261031.mjs <nhãn-mới>`: chuẩn hóa khi bản chọn chưa tồn tại và đo hộp bao, alpha, màu khóa, luma, IoU; không ghi đè kết quả nhãn đã có.
- `refine-alpha-20261031.mjs`: bước căn lại hộp bao và hai đầu matte, lưu bản trung gian trước khi sửa.
- `final-matte-20261031.mjs`: mặc định chỉ kiểm khô; `--apply` thực hiện bước matte đầu và chọn `load-guns.try2`.
- `matte-delivery-20261031.mjs`: mặc định kiểm khô; `--apply` sửa matte bảo thủ ở cả hai ngưỡng cho 44 file, thu từng khổ trực tiếp từ bản 1024². Lưu ảnh trước khi sửa, không đụng RGB.
- `audit-native-20261031.mjs <nhãn-mới>`: kiểm bốn khổ, đo ở cỡ thật, ghi toàn bộ 55 cặp IoU.
- `sheets-20261031.mjs`: dựng tờ chính, 11 tờ trước/sau và tờ chân dung. Lần cập nhật vừa qua đã lưu các tờ trước đó với hậu tố `.before-final.jpg`.
- `validate-delivery-20261031.mjs`: chạy lại kiểm đọc bất kỳ lúc nào; `--save` chỉ dùng khi file kết quả chưa có.
- `seal-20261031.mjs`: chốt MD5 hậu tố `resume2`, cố ý từ chối ghi đè hồ sơ đã chốt. Script snapshot cũ nhận nhãn mới cho những lần sau.

Các script sửa ảnh có lưu độc quyền bản trước sửa nên sẽ từ chối chạy lại `--apply` trên chính bộ đã xử lý; có thể đọc thuật toán và tái hiện trên bản sao của các `.try*`. Kiểm đọc chạy lại bằng `node games/typing-survival/art-src/_review/150/validate-delivery-20261031.mjs`.

Sai khác có giải thích: dùng manifest mới để giữ manifest cũ; chuẩn hóa nguồn khác 1024² về khổ giao; sửa alpha sau Lanczos thay vì làm nét; Shard theo lề chuẩn thay vị trí lệch của Swarm cũ; ngưỡng tương phản tính trên ít nhất một trong hai mã nền đã cho. Không có bước san phẳng hoặc phủ lại tranh. Các bản đo đầu chưa đạt được giữ làm hồ sơ, số trong báo cáo này lấy từ nhãn **delivery-20261031** cuối.

**Không bỏ sót ảnh hoặc bản thu.** Chưa làm phần Claude chấm nhận, chủ dự án duyệt và chép `public/`, vì đó là bước nhận/gắn sau phiếu này. Các ảnh sát ngưỡng 8 được ghi ngay trong báo cáo; không sửa `ART_REPLACE_LATER.md` vì ngoài phạm vi được ghi. Chủ dự án/Claude cần xem kỹ **Station Crest 20 px, động tác Load Guns 20 px và Shard trên nền than chì/cạnh sáu bản gốc**.

Không chạy lệnh Git, build/test game, dev server, trình duyệt hoặc mạng ngoài công cụ sinh ảnh. Không đọc/ghi Tu Tiên, `.wt-*`, không sửa code/game docs/công cụ chung hoặc file thuộc tác vụ khác. Không có raw frame trình duyệt để prune; giữ bản sinh và các bước hậu kỳ theo yêu cầu bảo toàn file.

---

## Hồ sơ hai lượt bị hạn mức trước đó · giữ nguyên để tra cứu

# Phiếu 150 · Last Line · Chưa hoàn tất: hết hạn mức sinh ảnh

## Chạy lại 30/10/2026 · vẫn HTTP 429, dừng theo phiếu

**Lượt chạy lại lúc khoảng 13:01–13:02 ngày 30/10/2026 (UTC+7) vẫn chưa sinh được ảnh.** Đã đọc báo cáo cũ, kiểm tra thư mục, xem lại ảnh chuẩn chủ dự án, mẫu `gun-xung.norm.256.png`, ảnh 121, khung 127 và `swarm.png`. Thư mục chỉ có 11 prompt đã chuẩn bị, chưa có ảnh của phiếu 150 để giữ hoặc hậu kỳ. Không sửa prompt, không ghi đè file media hay hồ sơ lần trước.

Gọi lại công cụ tích hợp `image_gen.imagegen` cho **objective** bằng đúng prompt đã lưu, `transparent_background: true`. Công cụ trả ngay **HTTP 429 · usage_limit_reached · The usage limit has been reached**, không trả ảnh. Theo lệnh “Nếu vẫn 429 thì dừng, ghi giờ”, đã dừng; không gọi tiếp mười ảnh và không chuyển sang công cụ/API khác.

- Giờ ghi nhận lỗi: **13:02:08 ngày 30/10/2026**, giờ Việt Nam (đồng hồ công cụ: `2026-10-30 06:02:08 UTC`; yêu cầu sinh xảy ra ngay trước đó).
- Công cụ tiếp tục báo mở hạn mức lúc **19:47:25 ngày 30/10/2026**, còn `24334` giây tại thời điểm trả lỗi. Đây là mốc công cụ trả về, chưa phải xác nhận hạn mức sẽ hoạt động.
- [Lỗi lượt chạy lại](../../games/typing-survival/art-src/_review/150/generation-error-resume-2026-10-30.json). Prompt được gọi là [objective.try1.prompt.txt](../../games/typing-survival/art-src/ui/icons/objective.try1.prompt.txt); không tính lỗi hạn mức là một ảnh sinh thành công.

### KA1 lượt chạy lại

Giữ nguyên `md5-before.txt` / `md5-after.txt` và mọi hồ sơ cũ. Để tuân thủ cấm ghi đè, bản kê mới mang hậu tố `resume`: [trước](../../games/typing-survival/art-src/_review/150/md5-resume-before.txt), [sau](../../games/typing-survival/art-src/_review/150/md5-resume-after.txt), [diff](../../games/typing-survival/art-src/_review/150/md5-resume-diff.txt), [kết quả JSON](../../games/typing-survival/art-src/_review/150/md5-resume-summary.json). Đều dùng `/sbin/md5 -r` trên toàn bộ hai thư mục đích và hồ sơ 150.

| Số đo | Kết quả |
| --- | ---: |
| File trong manifest trước | 315 |
| File trong manifest sau | 318 |
| Đường dẫn thêm | 3 |
| File đã có bị đổi | 0 |
| File đã có bị mất | 0 |

Diff dữ liệu chỉ thêm dòng. Ba file thêm là hồ sơ lỗi mới, manifest trước và script [snapshot-resume-after.mjs](../../games/typing-survival/art-src/_review/150/snapshot-resume-after.mjs). Manifest sau được tính trước khi ghi chính nó, diff và JSON để tránh tự băm đệ quy. Script ghi độc quyền, cố ý từ chối ghi đè nếu chạy lại cùng tên; script snapshot cũ nhận nhãn pha mới cho lần kiểm sau. Báo cáo là tài liệu duy nhất được cập nhật, nằm ngoài cây media được băm.

### Phần còn thiếu và chủ dự án cần xem

Vẫn **0/11 ảnh gốc, 0/33 bản thu**. Chưa có đầu vào để đo khổ, alpha, luma, IoU, dựng tờ “bản sinh | bản hậu kỳ”, `150-sheet.jpg`, so Shard với sáu chân dung hoặc chấm KA5. Không ghi điểm giả và không tuyên bố đạt nghiệm thu. Chủ dự án/điều phối cần xem lỗi hạn mức; chưa có ảnh mới để duyệt. Claude chấm nhận và gắn `public/` vẫn để sau khi có bộ ảnh đạt.

Không chạy Git, build/test, dev server, trình duyệt hoặc mạng ngoài công cụ sinh ảnh; không đọc/ghi Tu Tiên, `.wt-*`; không sửa mã hay tài liệu khác. Hồ sơ cũ bên dưới được giữ để tiếp tục công việc sau khi công cụ sinh ảnh hoạt động.

---


Ngày 30/10/2026, Codex. **Chưa sinh được ảnh nào; chưa có ảnh đủ điều kiện giao hoặc nghiệm thu.** Công cụ tích hợp `image_gen` trả HTTP 429, `usage_limit_reached`, ngay yêu cầu đầu tiên cho `objective`. Đã chuẩn bị và lưu nguyên văn **11 prompt tiếng Anh**, chưa chuyển sang API, CLI hoặc công cụ tạo ảnh khác.

## Đã chuẩn bị

Đã đọc `ART_ACCEPTANCE.md`, khối STYLE-UI của Last Line tại `ART_DIRECTION_2026-10-28.md` §4.3, định dạng phiếu 015, dàn ý UIC-LL-2 và báo cáo 121/127. Đã xem ảnh chuẩn của chủ dự án, `gun-xung.norm.256.png`, `briefing-bg.png`, `panel-large.alpha.png`, `swarm.png` và `swarm.v2.png`.

Ảnh 121 và khung 127 đã có để tham chiếu vật liệu và bố cục. Báo cáo hai phiếu đó vẫn ghi các chốt chưa đạt; việc dùng làm tham chiếu không phải xác nhận đã nghiệm thu chúng. Prompt dùng nguyên văn STYLE-UI hướng **B · Lightbearer**; khối KIND riêng xác định icon gọn hoặc chân dung không có khung ngoài, phần riêng bám nội dung phiếu và dòng cuối yêu cầu alpha trong suốt thật. Với Shard, giữ cách trình bày của Swarm, bổ sung ánh viền và kính đen theo hướng B.

| Ảnh | Prompt đã lưu | Trạng thái sinh | Cỡ 720p / 1080p |
| --- | --- | --- | --- |
| objective | `ui/icons/objective.try1.prompt.txt` | Công cụ từ chối vì hạn mức | 20 / 30 |
| hazard | `ui/icons/hazard.try1.prompt.txt` | Chưa gọi | 20 / 30 |
| learning-rule | `ui/icons/learning-rule.try1.prompt.txt` | Chưa gọi | 20 / 30 |
| equipment | `ui/icons/equipment.try1.prompt.txt` | Chưa gọi | 20 / 30 |
| warning | `ui/icons/warning.try1.prompt.txt` | Chưa gọi | 16 / 24 |
| new-badge | `ui/icons/new-badge.try1.prompt.txt` | Chưa gọi | 16 / 24 |
| station-crest | `ui/icons/station-crest.try1.prompt.txt` | Chưa gọi | 20 / 30 |
| chapter-crest | `ui/icons/chapter-crest.try1.prompt.txt` | Chưa gọi | 32 / 48 |
| load-guns | `ui/icons/load-guns.try1.prompt.txt` | Chưa gọi | 20 / 30 |
| back | `ui/icons/back.try1.prompt.txt` | Chưa gọi | 20 / 30 |
| shard | `ui/foes/shard.try1.prompt.txt` | Chưa gọi | 20 / 30; thẻ ải 40 / 60 |

Các đường dẫn trong bảng tính từ `games/typing-survival/art-src/`. Chưa có prompt sửa lượt 2 hoặc 3, chưa có `.tryN.png`, bản chọn `.png`, `.prompt.txt` hay ba bản thu. Lỗi hạn mức xảy ra trước khi công cụ trả ảnh, nên không ghi nhận một lượt sinh thành công và không tạo ảnh rỗng để thay thế.

## Lỗi công cụ và hồ sơ chạy lại

- [Lỗi nguyên dạng có cấu trúc](../../games/typing-survival/art-src/_review/150/generation-error.json): HTTP 429, `usage_limit_reached`, thông báo `The usage limit has been reached`.
- Công cụ báo `resets_at: 1793364445`, tương ứng **19:47:25 ngày 30/10/2026, giờ Việt Nam**; thời điểm trả lỗi còn `64881` giây. Đây là mốc do công cụ báo, chưa được kiểm tra lại bằng một yêu cầu sinh sau mốc đó.
- [jobs.json](../../games/typing-survival/art-src/_review/150/jobs.json): 11 prompt nguyên văn, tên đích, cỡ và các đường dẫn tham chiếu cho từng yêu cầu. Khi hạn mức được mở lại, gọi công cụ tích hợp mỗi lần một ảnh với `prompt`, `referenced_image_paths` và `transparent_background: true` như công việc đã lưu.
- [prepare.mjs](../../games/typing-survival/art-src/_review/150/prepare.mjs): dựng prompt từ STYLE-UI hiện có, kiểm tra tên đích chưa tồn tại, ghi prompt bằng chế độ độc quyền. Chạy từ repo cha: `node games/typing-survival/art-src/_review/150/prepare.mjs`. Script cố ý từ chối chạy lại trên bộ đã có; khi tiếp tục dùng `jobs.json`, không ghi đè các prompt hiện tại.
- [snapshot.mjs](../../games/typing-survival/art-src/_review/150/snapshot.mjs): gọi `/sbin/md5 -r` cho từng file, tạo manifest và so sánh; mỗi tên kết quả chỉ được ghi một lần.

Chưa tạo script hậu kỳ, đo hình hoặc dựng tờ xem vì chưa có đầu vào. Không thực hiện lệnh mạng nào ngoài yêu cầu công cụ sinh ảnh tích hợp.

## KA1 · Bảo toàn file

Phạm vi băm: toàn bộ `ui/icons/`, `ui/foes/`, `_review/150/` và các file `_review/150-*` nếu có. Snapshot trước được tạo trước khi ghi prompt hoặc ảnh; script snapshot đã có và được tính trong baseline.

| Số đo | Kết quả |
| --- | ---: |
| File trong manifest trước | 250 |
| File trong manifest sau | 265 |
| Đường dẫn thêm | 15 |
| File đã có bị đổi | 0 |
| File đã có bị mất | 0 |

15 dòng thêm gồm 11 prompt, `prepare.mjs`, `jobs.json`, `generation-error.json` và `md5-before.txt`. Diff nội dung chỉ có dòng thêm. Manifest sau được tính trước khi ghi chính nó, diff và JSON kết quả để tránh tự băm đệ quy. Báo cáo này nằm ngoài cây media được băm.

- [md5-before.txt](../../games/typing-survival/art-src/_review/150/md5-before.txt)
- [md5-after.txt](../../games/typing-survival/art-src/_review/150/md5-after.txt)
- [md5-diff.txt](../../games/typing-survival/art-src/_review/150/md5-diff.txt)
- [md5-summary.json](../../games/typing-survival/art-src/_review/150/md5-summary.json)

## Các chốt chưa thể kiểm

| Kiểm bắt buộc | Kết quả |
| --- | --- |
| Đủ 11 bản gốc và 33 bản thu | 0 / 44 file ảnh |
| Khổ 1024², 256², 128², 64²; sRGBA | Chưa có ảnh để chạy `magick identify` |
| Hộp bao 68–72 %, lệch tâm ≤ 2 % | Chưa đo |
| Alpha trung gian ngoài mép 3 px | Chưa đo |
| Pixel màu khóa còn alpha > 0 | Chưa đo |
| Chênh luma trên hai nền HUD | Chưa đo |
| IoU lớn nhất từng ảnh ở 32 px | Chưa đo |
| Tờ `_review/150-sheet.jpg` | Chưa tạo |
| 11 tờ “bản sinh \| bản hậu kỳ” | Chưa tạo |
| Shard cạnh sáu chân dung ở 40 px | Chưa dựng; chưa kết luận hợp bộ |
| KA5 năm tiêu chí ở cỡ gốc và 720p | **Chưa chấm**, không có bản hậu kỳ |
| Claude chấm lại ≥ 8 | Chưa thực hiện |

## Sai khác và phần còn lại

Phiếu dừng sau bước chuẩn bị vì hạn mức toàn công cụ, không phải do điểm mỹ thuật. Không gọi tiếp mười ảnh còn lại khi lỗi đã xác định là hạn mức. Chưa có tờ xem để chủ dự án duyệt hình; phần cần xử lý trước là mở lại khả năng sinh ảnh, rồi tạo đủ bộ, hậu kỳ không phá tranh, đo, xem cỡ thật, chấm KA5 và gửi Claude chấm nhận.

Không ghi đè, đổi tên hoặc xóa file cũ; không sửa mã, tài liệu khác, công cụ chung hay ảnh sáu chân dung. Không chạy Git, build/test game, dev server, trình duyệt hoặc âm thanh. Không đọc/ghi Tu Tiên, `.wt-*` hay ghi vào game khác. Không tích hợp `public/`. Không có capture trình duyệt hoặc raw frame để prune.
