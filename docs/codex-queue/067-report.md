# Phiếu 067 · MF-I5 · Đồng cỏ yên và đất mòn nhạt

Ngày kiểm: 28/10/2026. Game: Rồng Giữ Ải, bộ `pine-river`.

**Kết quả: chưa đạt điều kiện xong.** Ba PNG đích cùng đủ ba lượt thử và prompt đã tồn tại trước phiên này. Hai ô cỏ của bản chọn có sẵn đạt hue và độ rối; ô đất đạt luma. Cả ba vẫn lộ đường nối khi dịch nửa ô. Không ghi đè ảnh, không tạo lượt thứ tư.

## 1. Phạm vi đã làm

- Đọc kế hoạch, phiếu MF-I5, luật duyệt ảnh và kỹ năng `imagegen`; xem tám ô nền gốc, chín lượt thử ở khổ đầy đủ và 128 px.
- Đo lại toàn bộ chín lượt thử và ba bản chọn bằng ImageMagick 7 cùng trình đo có sẵn trong `_review/MF-I5/measure.mjs`. Chỉ đọc trình đo; đầu ra nằm trong thư mục kiểm mới.
- Tạo ảnh đối chiếu bằng ImageMagick, gồm dịch vòng `-roll +627+627`, bảng ảnh đầy đủ/bản dịch và bảng chín ảnh 128 px. Đây là ảnh kiểm dẫn xuất, không phải lượt tạo ảnh mới.
- Lần chạy này không gọi `image_gen`: mọi tên ảnh đích và `.try1`–`.try3` đã có; phiếu cấm ghi đè, đổi tên, xóa file cũ và chỉ cho tối đa ba lượt. Prompt có sẵn được giữ nguyên. Không xác nhận được lịch sử công cụ tạo ảnh chỉ từ các file này.

## 2. File mới

- Báo cáo này: `docs/codex-queue/067-report.md`.
- Thư mục bằng chứng: `games/dragon-hold/art-src/_review/MF-I5-audit-067/`:
  - `md5-before.txt`, `md5-after.txt`, `md5-diff.txt`: KA1 cho toàn bộ 49 file của thư mục đích.
  - `identify.txt`: khổ tám ô tham chiếu, chín lượt thử và ba bản chọn.
  - `metrics-all.json`: số đo từng ảnh; `scores.json`: điểm từng tiêu chí ở hai cỡ.
  - `selected-equals-try3.json`: đối chiếu byte PNG và prompt giữa bản chọn có sẵn với lượt 3.
  - `all-tries-128.jpg`, `selected-and-roll.jpg` và ba file `meadow-calm-a.roll.jpg`, `meadow-calm-b.roll.jpg`, `soil-worn-pale.roll.jpg`.

Không tạo hay sửa file nào trong `art-src/ground/pine-river/`; không sửa bằng chứng kiểm cũ trong `_review/MF-I5/`.

## 3. KA1–KA4

**KA1 — đạt trong phiên này.** Chạy `md5 -r` trên toàn bộ 49 file trong thư mục `ground/pine-river` trước và sau. `diff -u` trả mã 0, đầu ra trống: 0 file đổi, 0 file mất, 0 file thêm trong thư mục đích. Mốc trước thuộc đầu phiên kiểm này; không dùng để xác nhận quá trình tạo ảnh trước đó.

Bằng chứng: [trước](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/md5-before.txt), [sau](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/md5-after.txt), [diff](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/md5-diff.txt).

**KA2 — khổ phù hợp phần lớn bộ hiện có.** Cả chín lượt thử và ba bản chọn đều 1254 × 1254 px, sRGB 8 bit. Bảy ô gốc cũng 1254 × 1254; riêng `moss.png` hiện là 1024 × 1024. Vì bộ tham chiếu không đồng nhất, không khẳng định khớp cả tám ô. Giữ nguyên `moss.png`. Đây là ô nền kín, không phải sprite/decal hay ảnh nguồn Tripo; kiểm alpha sạch và nền xám Tripo không áp dụng.

**KA3 — không áp dụng:** ô nền phủ kín ảnh, không có vật cần lề 24 px hay cắt nền.

**KA4 — đạt:** tỷ lệ pixel hue 0–50° hoặc 165–190°, saturation > 0,55 và value > 0,5 là **0,0000%** ở cả chín lượt thử và ba bản chọn, dưới ngưỡng 2%.

## 4. Cách đo và số đo từng lượt

Đọc RGB sRGB 8 bit, chuẩn hóa về 0–1; tính `L = 0,2126R + 0,7152G + 0,0722B`, không đổi sang luma tuyến tính. Hue theo HSV, đơn vị độ. Độ rối là trung bình `|L − box5×5(L)|`; bộ lọc dùng biên tuần hoàn.

Phiếu không quy định cửa sổ cho mảng thấp tần hoặc mốc của ±5%. Báo cáo dùng trung bình hộp 65 × 65 và tính độ lệch tương đối so với trung vị L toàn ảnh: `100 × (box65×65(L) / median(L) − 1)`. Đây là quy ước đo được nêu rõ để duyệt lại; theo quy ước này, các lượt cỏ đều vượt ít nhất một phía của ±5%.

| Ảnh | Hue trung vị (°) | L trung vị | Độ rối 5×5 | Mảng 65×65, lệch tương đối |
| --- | ---: | ---: | ---: | ---: |
| `meadow-calm-a.try1` | 78.6207 | 0.655368 | 0.007759 | -6.89% … +7.58% |
| `meadow-calm-a.try2` | 86.3014 | 0.613997 | 0.005995 | -5.91% … +6.41% |
| `meadow-calm-a.try3` | 92.8767 | 0.612633 | 0.007597 | -7.57% … +7.98% |
| `meadow-calm-b.try1` | 76.0976 | 0.640778 | 0.006877 | -12.86% … +9.95% |
| `meadow-calm-b.try2` | 87.3418 | 0.606442 | 0.003779 | -6.39% … +3.99% |
| `meadow-calm-b.try3` | 94.5205 | 0.583818 | 0.004840 | -7.90% … +4.67% |
| `soil-worn-pale.try1` | 35.2174 | 0.654154 | 0.005317 | -5.83% … +7.57% |
| `soil-worn-pale.try2` | 33.9130 | 0.660844 | 0.005846 | -6.13% … +7.06% |
| `soil-worn-pale.try3` | 37.7143 | 0.686962 | 0.004349 | -2.74% … +2.73% |

Ngưỡng bắt buộc: cỏ có hue 88–95° và độ rối ≤ 0,030; đất có L trung vị 0,64–0,70. Cỏ lượt 1 và 2 trượt hue. Cỏ lượt 3 đạt hue; tất cả lượt cỏ đạt độ rối. Cả ba lượt đất đạt luma.

### Lát nửa ô và sai khác dọc mép

Dịch vòng nửa chiều rộng và chiều cao bằng `magick <ảnh> -roll +627+627 -quality 95 <ảnh-kiểm>.jpg`; xem ảnh 1254 px, không phóng 400%. Đường nối cũ nằm giữa ảnh tại x/y = 627. Số đo lấy trực tiếp từ PNG gốc, không lấy từ JPG nén.

Sai khác dọc mép là trung bình và phân vị 95 của `|L(trái) − L(phải)|` hoặc `|L(trên) − L(dưới)|` theo từng cặp pixel đối diện. Bảng dùng phần trăm toàn thang L; không phải phần trăm tương đối so với độ sáng nền. Phiếu không đặt ngưỡng số cho mép; đánh giá bắt buộc vẫn là không thấy đường nối.

| Bản chọn có sẵn (= lượt 3) | Trái/phải, TB / P95 | Trên/dưới, TB / P95 | Chênh pixel kề bên trong ảnh, X / Y | Quan sát dịch nửa ô |
| --- | ---: | ---: | ---: | --- |
| `meadow-calm-a` | 2.915% / 8.093% | 2.299% / 6.606% | 0.778% / 0.811% | Lộ đường nối; chưa đạt |
| `meadow-calm-b` | 1.393% / 4.283% | 1.291% / 3.502% | 0.531% / 0.503% | Lộ đường nối; chưa đạt |
| `soil-worn-pale` | 1.065% / 2.662% | 1.229% / 3.109% | 0.437% / 0.537% | Lộ đường nối; chưa đạt |

Đường thẳng đứng và ngang hiện rõ nhất ở `meadow-calm-a`; `meadow-calm-b` và đất có đường mảnh hơn nhưng vẫn thấy ở cỡ đầy đủ. Sai khác trung bình tại mép lớn hơn chênh pixel kề trong ảnh khoảng 2,3–3,7 lần. Không coi việc độ rối thấp hoặc hue/luma đạt là bằng chứng liền mép.

[Bảng bản chọn và dịch nửa ô](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/selected-and-roll.jpg). Xem cỡ đầy đủ: [cỏ A](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/meadow-calm-a.roll.jpg), [cỏ B](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/meadow-calm-b.roll.jpg), [đất](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/soil-worn-pale.roll.jpg).

## 5. KA5 — tự chấm lại từng lượt

Điểm dưới đây được chấm lại trong phiên kiểm này, không phải điểm lịch sử của người tạo ảnh. Mỗi ô ghi đủ năm điểm theo thứ tự **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**, mỗi tiêu chí tối đa 2. “Hình khối” của ô đất đánh giá mặt phẳng và góc nhìn từ trên. Cột 128 px đánh giá bản thu nhỏ; lỗi đường nối đã xác định ở cỡ đầy đủ vẫn trừ tiêu chí dùng tiếp.

| Lượt có sẵn | Khổ đầy đủ: 5 tiêu chí → tổng | 128 px: 5 tiêu chí → tổng | Điểm cần sửa |
| --- | --- | --- | --- |
| `meadow-calm-a.try1` | 1 / 1,5 / 2 / 2 / 1 → **7,5** | 1 / 2 / 2 / 2 / 1 → **8** | Cỏ vàng hơn hue yêu cầu; mảng và mép chưa đạt. |
| `meadow-calm-a.try2` | 1,5 / 1,5 / 2 / 2 / 1 → **8** | 1,5 / 2 / 2 / 2 / 1 → **8,5** | Hue 86,30°; mảng sáng tối còn rộng, mép chưa liền. |
| `meadow-calm-a.try3` | 1,5 / 1,5 / 2 / 2 / 1 → **8** | 1,5 / 2 / 2 / 2 / 1 → **8,5** | Hue đạt; mảng còn đậm và đường nối rõ. |
| `meadow-calm-b.try1` | 1 / 1,5 / 2 / 2 / 1 → **7,5** | 1 / 2 / 2 / 2 / 1 → **8** | Hue quá vàng; mảng tối lớn, tương phản cao. |
| `meadow-calm-b.try2` | 1,5 / 1,5 / 2 / 2 / 1 → **8** | 1,5 / 2 / 2 / 2 / 1 → **8,5** | Yên hơn; hue 87,34° còn thiếu, mép chưa chứng minh liền. |
| `meadow-calm-b.try3` | 1,5 / 1,5 / 2 / 2 / 1 → **8** | 1,5 / 2 / 2 / 2 / 1 → **8,5** | Hue đạt; mảng tối và đường nối vẫn còn. |
| `soil-worn-pale.try1` | 2 / 1,5 / 2 / 2 / 1 → **8,5** | 2 / 2 / 2 / 2 / 1 → **9** | Luma đạt; bề mặt còn hạt và mép chưa liền. |
| `soil-worn-pale.try2` | 2 / 1,5 / 2 / 2 / 1 → **8,5** | 2 / 2 / 2 / 2 / 1 → **9** | Luma đạt; hạt còn rõ và mép chưa liền. |
| `soil-worn-pale.try3` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Mòn mềm, không chuỗi sỏi; còn đường nối mảnh. |

[Chín lượt ở 128 px](../../games/dragon-hold/art-src/_review/MF-I5-audit-067/all-tries-128.jpg). Nét vẽ mềm, nhìn thẳng từ trên và hợp bộ `pine-river`; không thấy chữ, logo, người, thần, nơi thờ, chấm hoa hay chuỗi sỏi trong ba bản chọn. Cỏ còn cụm nét chéo tương phản, cần giảm mảng khi sửa.

**Điểm mỹ thuật từ 8 không thay thế các kiểm bắt buộc.** Cả ba bản chọn hiện có vẫn chưa được chấp nhận vì đường nối. Chưa có lượt chấm lại của Claude trong phiên này. Không ghi danh sách nâng ảnh ở tài liệu khác vì ngoài đường dẫn được phép.

## 6. Bản chọn hiện có, phần bỏ qua và việc cần duyệt

Ba bản chọn có sẵn là `meadow-calm-a.png`, `meadow-calm-b.png`, `soil-worn-pale.png`; mỗi PNG và `.prompt.txt` trùng byte với cặp lượt 3 tương ứng. Không chọn hoặc sao chép bản mới trong phiên này. Trong các lượt có sẵn, lượt 3 của cỏ là lượt duy nhất đạt hue; đất lượt 3 yên nhất và có luma 0,686962. Đó là cơ sở giữ chúng để chủ dự án xem, không phải quyết định nghiệm thu.

Bỏ qua việc tạo/sửa và xuất ảnh đích mới vì toàn bộ tên đầu ra đã tồn tại, đủ ba lượt; luật phiếu cấm ghi đè, đổi tên, xóa file cũ. Không tự mở lượt 4 hay dùng tên khác để lách giới hạn. Các prompt có sẵn không được sửa. Chưa thể hoàn tất sản phẩm đạt đủ kiểm trong phạm vi hiện tại.

Chủ dự án/Claude cần xem ba ảnh dịch nửa ô được liên kết ở trên, xác nhận cách đo ±5%, và quyết định phạm vi cho một bản sửa mới hoặc việc thay bản chọn. Hướng sửa: ghép mép tuần hoàn có vùng chuyển tiếp mềm, giảm biên độ mảng sáng tối cỏ, giữ hue hiện đã đạt; sau sửa đo lại và chấm lại ≥ 8. Chỉ nghiệm thu khi không còn đường nối.

Không chạy Git, dev server, trình duyệt, mạng hay build/test game. Không đụng game khác, Tu Tiên hoặc công cụ âm thanh. Không có frame chụp trình duyệt/render mới; năm JPG kiểm đều được báo cáo dùng đến, không tạo bộ frame thô cần dọn.
