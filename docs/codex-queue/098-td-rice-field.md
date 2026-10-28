# Phiếu 098 · Lời Gọi · Năm ô Rice Field theo trạng thái

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 097 của lô). Số phiếu ảnh đổi thêm 1 vì 094 đã dùng cho từ vựng Rồng. Mọi số phiếu trong phiếu này đã đổi theo.

**Báo cáo:** `docs/codex-queue/098-report.md`.

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

**Vì sao:** kiểm kê map 1 (I3, P1, cổng G2). Ở 3D, Rice Field đổi mặt ruộng theo trạng thái (C6). Hôm nay chưa có ảnh nào.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/rice/` (thư mục mới).

**Chỉ được ghi:**
- `rice/<tên>.tryN.png`, `rice/<tên>.tryN.prompt.txt`, `rice/<tên>.png`, `rice/<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/098-*.jpg`, `games/typing-defense/art-src/_review/098/`;
- `docs/codex-queue/098-report.md`.

**Năm ô:** `rice-flooded` (bùn ngập nước, ánh trời bạc, chưa cấy), `rice-seedling` (mạ non), `rice-green` (lúa xanh), `rice-ripe` (lúa chín vàng), `rice-stubble` (gốc rạ).

**Luật vẽ:**
- Nhìn thẳng từ trên xuống, ánh sáng phẳng, liền mép cả bốn phía, 1024 × 1024, sRGB, không alpha.
- Một ô phủ 4 × 4 m. Hàng lúa chạy dọc ảnh, đúng 8 hàng mỗi ô, cách đều 128 px.
- Bốn ô có cây (`seedling`, `green`, `ripe`, `stubble`) có hàng ở **cùng vị trí**, để đổi trạng thái không bị nhảy. Cách đề xuất: sinh `rice-green` trước, rồi dùng nó làm ảnh tham chiếu cho ba ô kia; được dời ngang bằng công cụ cho khớp hàng.
- Phong cách như 095 (không viền mực, vệt cọ lớn).

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/scenery/`.
2. `magick identify`: 1024 × 1024, sRGB, không alpha.
3. **Mép liền** (mục 1.1): `E ≤ 1,25 · I` cho cả năm ô.
4. **Hàng lúa** (bốn ô có cây): lấy trung bình `L` theo từng cột, tính tự tương quan. Chu kỳ 128 ± 4 px. Độ lệch pha giữa hai ô bất kỳ ≤ 8 px.
5. **Màu** (trung vị):
   - `rice-seedling`, `rice-green`: hue 80–120°;
   - `rice-ripe`: hue 40–55°;
   - `rice-stubble`: hue 25–50°, S ≤ 0,35;
   - `rice-flooded`: S ≤ 0,30, luma 0,45–0,65.
6. **Ảnh kiểm:**
   - `_review/098-states.jpg`: năm ô cạnh nhau ở 512 px, rồi mỗi ô lát 3 × 3 thu về 512 px;
   - `_review/098-swap.gif` hoặc tờ 4 khung: cùng một chỗ đổi `seedling` → `green` → `ripe` → `stubble`, để thấy hàng có nhảy không.
7. **KA5** ở cỡ đầy đủ và 256 px.

**Xong khi:** năm ô qua mục 2–5 và tự chấm ≥ 8.
