# Phiếu 093 · Rồng Giữ Ải · Làm liền mép ba ô nền của phiếu 067 bằng công cụ (map L2-cau)

**Vì sao:** phiếu 067 (MF-I5) tạo ba ô nền `meadow-calm-a`, `meadow-calm-b`, `soil-worn-pale`. Màu và độ rối đạt, nhưng khi dịch nửa ô (`-roll +627+627`) cả ba còn lộ đường nối. Ở mép, độ lệch trung bình lớn gấp 2,3–3,7 lần độ lệch giữa hai px kề nhau bên trong ảnh (`docs/codex-queue/067-report.md` §4). Lát lên bản đồ, đường nối sẽ thành lưới ô vuông. Theo `docs/games/ART_ACCEPTANCE.md` §2.2, lỗi sửa được thì **sửa bằng công cụ trước**. Phiếu này không tạo ảnh mới.

**Báo cáo:** `docs/codex-queue/093-report.md`.

## Nơi làm

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Ảnh:** `games/dragon-hold/art-src/ground/pine-river/`. Đây là media, không vào Git.

**Chỉ được ghi:**
- `games/dragon-hold/art-src/ground/pine-river/<tên>.fix1.png` với `<tên>` là `meadow-calm-a`, `meadow-calm-b`, `soil-worn-pale` (file mới);
- `games/dragon-hold/art-src/_review/093-*.jpg`, `games/dragon-hold/art-src/_review/093/` (số đo, ảnh kiểm, script đã dùng);
- `docs/codex-queue/093-report.md`.

**Cấm:**
- ghi đè, đổi tên, xóa file có sẵn. Bản chọn `<tên>.png` giữ nguyên; Claude chép `.fix1.png` sang tên đó sau khi duyệt;
- gọi công cụ tạo ảnh (image_gen); vẽ lại nội dung;
- mọi lệnh git; sửa mã hay tài liệu khác;
- dev server, trình duyệt;
- đụng game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`).

## Cách làm (đề xuất; được đổi nếu ra kết quả tốt hơn, ghi rõ lý do)

Ảnh vuông `T` cạnh `N = 1254`, nửa cạnh `h = 627`.

1. `R = roll(T, +h, +h)`. Mép của `R` liền khi lát, vì đó là phần giữa của `T`; đường nối của `R` nằm ở chữ thập giữa ảnh (x = h, y = h).
2. Phủ lên chữ thập đó bằng phần giữa liền của `T`, theo mặt nạ mềm `M(x, y) = max(w(|x − h|), w(|y − h|))`. Trong đó `w(d) = 1` khi `d ≤ a`, giảm theo cosin về 0 khi `d` đi từ `a` tới `a + b`, và bằng 0 sau đó. Đề xuất `a = 24`, `b = 160`; thử `b` từ 96 tới 224 và chọn giá trị đạt kiểm mà ít bóng chồng nhất.
3. `O = R · (1 − M) + T · M`, tính trên RGB sRGB 8 bit. Giữ khổ `N × N` và hồ sơ màu của `T`.

Viết script bằng Node (không thêm gói) hay ImageMagick 7, lưu vào `_review/093/`, chạy lại được.

## Kiểm (bắt buộc, ghi số vào báo cáo)

Dùng đúng cách đo của `067-report.md` §4: `L = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1; độ rối = trung bình `|L − box5×5(L)|` với biên tuần hoàn.

1. **KA1 md5:** `md5 -r` mọi file trong `ground/pine-river/` trước (`_review/093/md5-before.txt`) và sau. `diff` chỉ có ba dòng `.fix1.png` mới.
2. **Mép liền** (với mỗi `.fix1.png`). Gọi `E` là trung bình `|L(cột 0) − L(cột N−1)|` và `|L(hàng 0) − L(hàng N−1)|`, `I` là trung bình độ lệch giữa hai px kề nhau bên trong ảnh theo X và Y. Phải có `E ≤ 1,25 · I`; hôm nay tỉ số là 2,3–3,7. Ghi `E`, `I`, tỉ số trước và sau cho cả ba ảnh.
3. **Chữ thập cũ không thành đường nối mới:** đo tỉ số tương tự dọc x = h và y = h của `O` (cột h−1 so với cột h, hàng h−1 so với hàng h): ≤ 1,25.
4. **Giữ đặc tính của phiếu 067:**
   - hue trung vị của hai ô cỏ trong 88–95°;
   - độ rối của hai ô cỏ ≤ 0,030, và không thấp hơn 85 % độ rối của bản gốc (pha trộn không được làm nhòe ảnh);
   - luma trung vị của ô đất trong 0,64–0,70;
   - KA4 (hue 0–50° hoặc 165–190°, S > 0,55, V > 0,5) vẫn 0 %.
5. **Ảnh kiểm:**
   - `_review/093-roll.jpg`: mỗi ảnh một hàng gồm gốc, gốc `-roll +627+627`, `.fix1`, `.fix1` cũng `-roll +627+627`, mỗi ô 627 px;
   - `_review/093-tile3x3.jpg`: mỗi `.fix1` lát 3 × 3 rồi thu còn 1254 px, đặt cạnh bản gốc lát 3 × 3.
   Xem bằng mắt ở cỡ đầy đủ; ghi "không thấy đường nối" hoặc chỉ chỗ thấy.
6. **KA5 tự chấm:** 5 tiêu chí của `ART_ACCEPTANCE.md` §2.2, ở cỡ đầy đủ và 128 px. Riêng tiêu chí "Dùng được cho bước sau" chỉ cho 2 khi mục Kiểm 2 và 3 đạt.

## Báo cáo `docs/codex-queue/093-report.md`

Tiếng Việt: cách làm và tham số đã chọn; bảng số đo trước và sau của sáu mục Kiểm; điểm KA5; đường dẫn ảnh kiểm.

**Xong khi:** cả ba `.fix1.png` qua mục Kiểm 1–4 và tự chấm ≥ 8. Ảnh nào không đạt thì ghi rõ chỗ trượt và đề xuất cách khác (ví dụ ghép theo đường cắt tối ưu). **Nhận** khi Claude chấm lại ≥ 8; khi đó Claude chép `.fix1.png` thành `<tên>.png`.
