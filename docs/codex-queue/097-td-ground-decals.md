# Phiếu 097 · Lời Gọi · Hai tờ decal mặt đất

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 096 của lô). Số phiếu ảnh đổi thêm 1 vì 094 đã dùng cho từ vựng Rồng. Mọi số phiếu trong phiếu này đã đổi theo.

**Báo cáo:** `docs/codex-queue/097-report.md`.

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

**Vì sao:** kiểm kê map 1 (I2, P1, cổng G2). Shader đất của C3 cần decal để mặt đất không phẳng: chỗ đất mòn, ngã ba, khóm hoa, gốc cây, dấu cây luật đã chặt.

**Cần trước:** phiếu 095 (dùng `grass-a.png` để thử ghép). Nếu 095 chưa có `grass-a.png`, ghép thử trên màu phẳng `#7fa651` và ghi rõ.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/decals/` (thư mục mới).

**Chỉ được ghi:**
- `decals/ground-decals-a.*`, `decals/ground-decals-b.*` (bản sinh `.tryN.*` và hai nửa `-left`, `-right`; bản ghép `.png` trên nền `#FF00FF`; `.alpha.png`);
- `games/typing-defense/art-src/_review/097-*.jpg`, `games/typing-defense/art-src/_review/097/`;
- `docs/codex-queue/097-report.md`.

**Cách làm:** mỗi tờ là lưới 4 × 2, 2048 × 1024, ô 512 × 512. Sinh hai ảnh vuông 2 × 2 (bốn món mỗi ảnh), rồi ghép bằng script thành một tờ.

**Nội dung:**
- **Tờ a (đất):** đất mòn ×2, đất dưới tán (sẫm, có lá kim và lá mục) ×2, mảng ngã ba (ba nhánh đất mòn gặp nhau) ×1, mẩu lối mòn thẳng ×1, mẩu lối mòn cong ×1, chỗ đất trống nhỏ ×1.
- **Tờ b (vật nhỏ):** khóm hoa dại ×2 (trắng và vàng, điểm son nhỏ), sỏi rải ×2, lá rụng ×1, gốc cây nhìn từ trên ×1, vòng vụn gỗ (dấu cây luật đã chặt) ×1, mảng cỏ ba lá ×1.

**Luật vẽ:**
- Nhìn thẳng từ trên xuống, ánh sáng phẳng, không bóng đổ.
- Thang như 095: 128 px mỗi mét; một ô 512 px là 4 m.
- Tờ a không có viền mực; mép mềm làm bằng công cụ: sau khi tách nền, làm mềm alpha 12–24 px vào trong hình.
- Tờ b có viền mực mảnh như cây cảnh meadow, mép rõ.

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/scenery/`.
2. `.alpha.png` đúng 2048 × 1024, RGBA. Đủ 8/8 ô có vật; bbox mỗi vật cách mép ô ≥ 24 px; vật chiếm ≥ 35 % diện tích ô.
3. **Tách nền sạch:** 0 % px có alpha > 0 mà hue 285–330° và S > 0,5.
4. **Mép mềm của tờ a:** trong mỗi ô, px có alpha 0,1–0,9 chiếm ≥ 10 % số px có alpha > 0.
5. **Màu:** hue trung vị các món đất của tờ a lệch ≤ 12° so với `dirt-road.png` của 095.
6. **Ảnh kiểm** `_review/097-on-grass.jpg`: mỗi món ghép lên `grass-a.png` đúng thang (ô decal 512 px trên ô đất 1024 px), thu về rộng 1280 px. Ghi: món nào trông như dán, món nào hòa vào đất.
7. **KA5** ở cỡ đầy đủ và cỡ thu 128 px mỗi ô.

**Xong khi:** hai tờ qua mục 2–5 và tự chấm ≥ 8.
