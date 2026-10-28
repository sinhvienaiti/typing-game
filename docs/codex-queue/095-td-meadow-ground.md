# Phiếu 095 · Lời Gọi · Bộ ô đất meadow cho mặt đất 3D của map 1 (w1-silverfall)

**Vì sao:** kiểm kê map 1 ngày 28/10 (I1, P0, cổng G2). Theo quyết định của chủ dự án, map 1 của Lời Gọi chuyển từ khung vẽ gỡ lỗi 2D sang 3D (bước 1C). Mặt đất 3D cần ô đất vẽ tay liền mép. Hôm nay chưa có ô nào. Claude dựng shader đất bằng các ô này (C3).

**Báo cáo:** `docs/codex-queue/095-report.md`.

## Luật chung

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `games/typing-defense/art-src` (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt đúng chỗ thiếu, tối đa 3 lượt tạo mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-defense/art-src/scenery/meadow/ground/<tên>.tryN.png` và `.tryN.prompt.txt` (N = 1, 2, 3);
  - `<tên>.tryN.tile.png`: bản đã làm liền mép bằng công cụ của lượt N;
  - bản chọn: `<tên>.png`, là bản `.tile` đã liền mép, kèm `<tên>.prompt.txt`;
  - `games/typing-defense/art-src/_review/095-*.jpg` và `_review/095/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu khác;
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - đụng game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, người, con vật, nhà, vật đứng trong ảnh.

## Phong cách

- Mở đầu mỗi prompt bằng nguyên văn khối **STYLE** ở `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3.1.
- Sau đó thêm dòng chung này, nguyên văn: `Seamless tiling ground texture seen straight from above, orthographic, no perspective, no horizon. Flat, even, shadowless light: no cast shadows, no highlights, no sun direction. Soft painted texture in a few large calm tone patches, no ink outlines on the ground, no objects standing on it. Square 1024 x 1024.` Ô đất không vẽ viền mực, vì viền mực trong STYLE là cho vật đứng.
- Xem các ảnh cảnh có sẵn ở `games/typing-defense/art-src/scenery/meadow/`, ví dụ `tall-grass-v1.png`, `wildflowers-v1.png`, `rock-small-v1.png`, để màu đất hợp với cây và đá sẽ đứng trên nó.
- Xem cảnh map 1 hôm nay (bản 2D) ở `games/typing-defense/tmp/map1-audit/sheets/` nếu có, để biết các vùng: đồng cỏ, đường quái, suối, sân Fort.

## Sáu ô

| Tên file | Nội dung | Ghi chú |
|---|---|---|
| `grass-a` | Cỏ non đồng bằng, xanh lúa non, vài mảng sáng tối rộng và êm | Ô nền chính, phủ phần lớn sân 96 m |
| `grass-b-clover` | Cùng tông với `grass-a`, có những đám cỏ ba lá nhỏ gom thành cụm | Ô xen kẽ để đỡ lặp |
| `dirt-path` | Đất nện màu nâu vàng ấm của đường quái đi, vết mòn mềm, vài viên sỏi nhỏ dẹt nằm sát mặt | Đường; đủ khác cỏ để đọc rõ từ camera cao |
| `path-edge-worn` | Nửa trên là cỏ của `grass-a`, nửa dưới là đất của `dirt-path`, ranh giới gồ ghề tự nhiên, cỏ thưa dần | **Chỉ liền mép trái và phải**; mép trên khớp `grass-a`, mép dưới khớp `dirt-path` |
| `stream-bank` | Bờ suối: bùn ẩm sẫm, sỏi tròn xám bạc, vài mảng cỏ ướt | Quanh rect nước của suối |
| `fort-paving` | Sân đá lát: phiến đá vôi trắng ngà ghép không đều, mạch có rêu mỏng | Quanh Fort và mỏ quặng |

## Làm liền mép (bắt buộc với mọi lượt)

Ảnh tạo ra hầu như không tự liền mép (phiếu 067 đã gặp). Với mỗi lượt, làm bản `.tile` bằng công cụ:

1. `R = roll(T, +512, +512)`.
2. `O = R · (1 − M) + T · M`, với `M(x, y) = max(w(|x − 512|), w(|y − 512|))`. Ở đây `w(d) = 1` khi `d ≤ 24`, giảm theo cosin về 0 khi `d` đi từ 24 tới 24 + b, và bằng 0 sau đó. Thử `b` từ 96 tới 192.
3. Với `path-edge-worn`, chỉ làm theo trục X: `roll(T, +512, 0)`, và mặt nạ chỉ có phần `w(|x − 512|)`.

Viết script bằng Node (không thêm gói) hay ImageMagick 7, lưu trong `_review/095/`, chạy lại được.

## Kiểm (bắt buộc, ghi số vào báo cáo)

Gọi `L = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1.

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/scenery/` (đệ quy) trước (`_review/095/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Khổ:** `magick identify` ra 1024×1024 cho cả sáu bản chọn, ảnh đặc (không alpha).
3. **Mép liền:**
   - Gọi `E` là trung bình `|L(cột 0) − L(cột 1023)|` và `|L(hàng 0) − L(hàng 1023)|`, `I` là trung bình độ lệch giữa hai px kề nhau bên trong ảnh. Phải có `E ≤ 1,25 · I`.
   - Chữ thập cũ (cột 511 so với 512, hàng 511 so với 512) cũng ≤ 1,25 · I.
   - Riêng `path-edge-worn` chỉ đo theo trục X.
   - Ghi `E`, `I` và tỉ số.
4. **Ghép đôi:**
   - Hàng trên của `path-edge-worn` so với hàng dưới của `grass-a`, và hàng dưới của nó so với hàng trên của `dirt-path`: chênh luma trung bình ≤ 0,04, chênh hue trung vị ≤ 8°.
   - `grass-a` và `grass-b-clover`: chênh luma trung vị ≤ 0,03, chênh hue trung vị ≤ 6°.
5. **Độ rối** (trung bình `|L − box5×5(L)|`, biên tuần hoàn): ≤ 0,035 ở cả sáu ô, để đất êm dưới thẻ chữ.
6. **Ảnh kiểm:**
   - `_review/095-tiles.jpg`: mỗi bản chọn lát 3 × 3, thu còn 768 px, có nhãn;
   - `_review/095-roll.jpg`: lượt gốc và bản `.tile`, cả hai dịch nửa ô;
   - `_review/095-together.jpg`: một khung ghép thử 4 × 3 ô gồm cỏ, mép đường, đường, bờ suối, sân đá, để thấy cả bộ hợp nhau.
   Xem ở cỡ đầy đủ; ghi "không thấy đường nối" hay chỉ chỗ thấy.
7. **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở 128 px.

## Báo cáo `docs/codex-queue/095-report.md`

- Bảng `| Ô | Lượt | Prompt thêm hay sửa | b đã chọn | Điểm 5 tiêu chí | Tổng | Còn thiếu |`.
- Đầu ra của bảy mục Kiểm, có số.
- Bản chọn và lý do.

**Xong khi:** sáu ô có bản chọn tự chấm từ 8 và qua mục Kiểm 1–5. **Nhận** khi Claude chấm lại từ 8.
