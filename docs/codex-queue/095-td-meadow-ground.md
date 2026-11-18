# Phiếu 095 · Lời Gọi · Sáu ô đất meadow cho mặt đất 3D map 1

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 094 của lô). Số phiếu ảnh đổi thêm 1 vì 094 đã dùng cho từ vựng Rồng. Mọi số phiếu trong phiếu này đã đổi theo.

**Báo cáo:** `docs/codex-queue/095-report.md`.

## Luật chung (phiếu ảnh)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Lỗi sửa được thì sửa bằng công cụ trước (ImageMagick 7, `tools/art-normalize`, script Python hay Node viết riêng). Chưa đạt thì sửa prompt đúng chỗ thiếu, **tối đa 3 lượt sinh mỗi ảnh**.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/<số phiếu>/`, chạy lại được. Ảnh kiểm ở `_review/<số phiếu>-*.jpg`.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git;
  - sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, chữ ký, khung, viền trong ảnh (trừ phần chữ logo của 096).
- **Kiểm chung (bắt buộc, ghi số vào báo cáo):**
  - **KA1 md5:** `md5 -r` mọi file trong thư mục đích trước khi ghi (`_review/<số>/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
  - **KA5 tự chấm:** 5 tiêu chí của ART_ACCEPTANCE §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2, ở cỡ đầy đủ và cỡ nhỏ nêu trong phiếu. "Dùng tiếp" chỉ được 2 khi mọi kiểm số đo của phiếu đạt.
- **Báo cáo** `docs/codex-queue/<số>-report.md`, tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm KA5; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại ≥ 8. Claude mới là người chép ảnh vào `public/` khi tích hợp.

**Đo chung cho ô đất** (095, 098; cùng cách của `067-report.md` §4 và phiếu 093):
- `L = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1.
- **Độ rối** = trung bình `|L − box5×5(L)|`, biên tuần hoàn.
- **Mép liền:** `E` = trung bình `|L(cột 0) − L(cột N−1)|` và `|L(hàng 0) − L(hàng N−1)|`; `I` = trung bình độ lệch giữa hai px kề nhau bên trong ảnh theo X và Y. Đạt khi `E ≤ 1,25 · I`. Nếu ảnh sinh ra chưa liền, được làm liền bằng cách của phiếu 093 (`roll` nửa ô, phủ chữ thập giữa bằng mặt nạ cosin); khi đó đo thêm chữ thập: tỉ số ≤ 1,25.
- **Đốm lặp:** box-blur 129 px tuần hoàn trên `L`, lấy `p95 − p5`.

## Phiếu

**Vì sao:** kiểm kê map 1 (I1, P0, cổng G2). Map 1 lên 3D (bước 1C). Mặt đất w1-silverfall vẽ bằng shader đất (C3), trộn các ô đất này theo mặt nạ đường, suối, sân Fort. Hôm nay không có ô đất nào; `art-src/scenery/meadow/` chỉ có cây, bụi, đá.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/ground/` (thư mục mới).

**Chỉ được ghi:**
- `ground/<tên>.tryN.png`, `ground/<tên>.tryN.prompt.txt`, `ground/<tên>.png`, `ground/<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/095-*.jpg`, `games/typing-defense/art-src/_review/095/`;
- `docs/codex-queue/095-report.md`.

**Sáu ô** (`<tên>`):

| Tên | Nội dung |
|---|---|
| `grass-a` | Cỏ đồng chính: xanh mạ non ấm, vệt cọ lớn, vài mảng sáng tối rất nhẹ |
| `grass-b-clover` | Cùng nền cỏ với `grass-a`, thêm mảng cỏ ba lá tròn cỡ 30–60 cm và vài đốm hoa trắng to; không chấm li ti |
| `dirt-road` | Đường đất nện vàng nâu, hai vệt bánh xe mờ chạy dọc ảnh, sỏi vẽ thành mảng |
| `trail-worn` | Mép đường mòn: đất nén lẫn cỏ thưa; dùng ở dải chuyển giữa cỏ và đường |
| `stream-bank` | Bờ suối: bùn ướt và sỏi cuội tròn, nâu xám ấm |
| `stone-yard` | Sân lát quanh Fort và quặng: đá ong và đá vôi trắng, viên to không đều, mạch vữa mờ |

**Thang và góc nhìn:**
- Một ô phủ 8 × 8 m trên mặt đất (1024 px, khoảng 7,8 mm mỗi px).
- Camera chơi nhìn xuống 55° từ 58 m. Chi tiết nhỏ hơn 15 cm sẽ thành nhiễu, nên vẽ bằng mảng màu lớn và vệt cọ.
- Nhìn thẳng từ trên xuống, không phối cảnh. Ánh sáng phẳng, không bóng đổ, không hướng nắng.

**Phong cách:**
- Đọc `games/typing-defense/art-src/scenery/meadow/tall-grass-v1.prompt.txt`. Giữ câu đầu về phong cách nhà (storybook, bảng màu young-rice green, ripe-rice gold, river silver, bamboo brown, limestone white).
- **Khác cây cảnh:** ô đất không có viền mực, không có vật đứng (không cây, bụi, đá nổi khối, người, vật nuôi). Chỉ có vệt cọ mềm.
- Ảnh tham chiếu màu: `games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png` và các ô của `games/typing-defense/tmp/map1-audit/sheet-keyframes.jpg` (màu dải đất của bản 2D hôm nay).
- Prompt viết bằng tiếng Anh, có câu "seamless tileable texture, edges wrap on all four sides".

**Cỡ:** sinh ảnh vuông, rồi thu về 1024 × 1024 (Lanczos), sRGB 8 bit, không alpha.

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/scenery/`.
2. `magick identify`: 1024 × 1024, sRGB, không kênh alpha.
3. **Mép liền** (mục 1.1): `E ≤ 1,25 · I` cho cả sáu ô. Ghi `E`, `I`, tỉ số trước và sau khi làm liền.
4. **Độ rối:** hai ô cỏ ≤ 0,030; bốn ô còn lại ≤ 0,040.
5. **Đốm lặp:** `p95 − p5` ≤ 0,08 cho hai ô cỏ, ≤ 0,10 cho bốn ô còn lại.
6. **Màu đi với nhau** (trung vị trên cả ô):
   - hue của hai ô cỏ trong 75–110°; hai ô cỏ lệch nhau ≤ 8° hue và ≤ 0,05 luma (trộn không thấy ranh);
   - luma `dirt-road` ≥ luma `grass-a` + 0,08 (đường sáng hơn cỏ, đọc được làn);
   - luma `stone-yard` ≥ luma `grass-a` + 0,10, và S ≤ 0,30;
   - luma `stream-bank` ≤ luma `dirt-road` − 0,05;
   - 0 % px có hue 285–330° và S > 0,5.
7. **Ảnh kiểm:**
   - `_review/095-tiles.jpg`: mỗi ô một cột: ô ở 512 px, rồi ô lát 3 × 3 thu về 512 px;
   - `_review/095-mock.jpg`: một mặt đất thử 2048 × 1152 lát `grass-a`, có mảng `grass-b-clover`, một dải `dirt-road` viền `trail-worn`, một dải suối viền `stream-bank`, một sân `stone-yard`; mặt nạ mềm vẽ bằng script; thu về rộng 1280 px để giống khoảng cách chơi.
   Xem bằng mắt ở cỡ đầy đủ. Ghi "không thấy đường nối, không thấy lặp" hoặc chỉ chỗ thấy.
8. **KA5** ở cỡ đầy đủ và ở cỡ thu 256 px.

**Xong khi:** cả sáu ô qua mục 2–6 và tự chấm ≥ 8. Ô nào không đạt sau 3 lượt thì ghi rõ chỗ trượt và đề xuất cách khác.
