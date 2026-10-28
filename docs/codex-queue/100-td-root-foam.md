# Phiếu 100 · Lời Gọi · Decal nứt rễ báo trước và dải bọt thác

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 099 của lô). Số phiếu ảnh đổi thêm 1 vì 094 đã dùng cho từ vựng Rồng. Mọi số phiếu trong phiếu này đã đổi theo.

**Báo cáo:** `docs/codex-queue/100-report.md`.

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

**Vì sao:** kiểm kê map 1 (I5, P1, cổng G3). Phiếu 043 đã xong phần chấm lại và ba ảnh mới. Còn thiếu hai ảnh cho bước 1C:
- đòn Rễ Trồi của Mộc Tinh phải có decal báo trước trên đất ≥ 1,2 s (C8, VFX_STANDARD pha A);
- vách Thác Bạc cần dải bọt chảy lặp được (C9).

**Nơi ghi:** `games/typing-defense/art-src/vfx/`.

**Chỉ được ghi:**
- `vfx/root-crack-warn.*`, `vfx/waterfall-foam.*` (`.tryN.png`, `.tryN.prompt.txt`, `.png`, `.prompt.txt`, `.alpha.png`);
- `games/typing-defense/art-src/_review/100-*.jpg`, `games/typing-defense/art-src/_review/100/`;
- `docs/codex-queue/100-report.md`.

**Phong cách:** mở đầu bằng hai đoạn đầu của `vfx/ma-troi-wisp.prompt.txt`, như phiếu 043.

**`root-crack-warn`:**
- FLIPBOOK một lần, 16 khung, lưới 4 × 4, 1024², nền `#FF00FF` (mép rõ, mềm bằng dải tông bên trong).
- Nhìn thẳng từ trên xuống: các vết nứt mực tím nâu sẫm, giữa mỗi vết có một đường sáng mảnh màu son cam (màu báo nguy), tỏa ra từ tâm ô.
- Khung 1–10: vết nứt lan từ tâm ra tới ≥ 80 % bán kính ô. Khung 11–16: giữ nguyên, sáng lên hai nhịp.
- Đọc được ở ô 64 px.

**`waterfall-foam`:**
- Texture lặp theo chiều dọc (cuộn từ trên xuống), 1024², nền đen `#000000`.
- Vệt bọt trắng bạc với hai ba dải tông xanh xám, sọc chạy dọc, không có vật khác.
- Alpha lấy theo độ sáng như hai ảnh lặp của 043. Mép trái và phải mờ dần trong 4 % bề rộng (làm bằng công cụ).

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/vfx/`: chỉ có file mới.
2. `root-crack-warn.alpha.png`: 16/16 ô; lề ≥ 24 px; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; diện tích alpha không giảm từ khung 1 tới khung 10; ở khung 10 vết nứt chạm ≥ 80 % bán kính ô.
3. `waterfall-foam.alpha.png`: liền mép trên dưới, `E ≤ 1,25 · I` đo theo Y trên cả `L` và alpha; alpha trung bình ở 4 % cột ngoài cùng mỗi bên ≤ 0,05.
4. **Ảnh kiểm:**
   - `_review/100-crack.jpg`: 16 khung ở ô 64 px ghép lên `grass-a.png` của 095 (nếu chưa có thì nền `#7fa651`);
   - `_review/100-foam.jpg`: dải bọt lát 1 × 3 theo chiều dọc trên màu vách đá `#8a8f94`.
5. **KA5** ở cỡ đầy đủ và cỡ nhỏ (ô 64 px; bọt thu về 256 px).

**Xong khi:** hai ảnh qua mục 2–3 và tự chấm ≥ 8.
