# Phiếu 099 · Lời Gọi · Ghost Flame: tờ tham chiếu và flipbook chết

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 098 của lô). Số phiếu ảnh đổi thêm 1 vì 094 đã dùng cho từ vựng Rồng. Mọi số phiếu trong phiếu này đã đổi theo.

**Báo cáo:** `docs/codex-queue/099-report.md`.

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

**Vì sao:** kiểm kê map 1 (I4, P1, cổng G3). Ghost Flame không có model; trong game là sprite VFX. Flipbook bay lượn `ma-troi-wisp` đã có từ phiếu 043 (9/10). Còn thiếu: tờ tham chiếu (`ma-troi-sheet.prompt.txt` có prompt mà chưa có ảnh) và cảnh chết (lửa tắt thành tia lấp lánh như thủy tinh), để C7 và C11 làm cái chết theo loài.

**Nơi ghi:** `games/typing-defense/art-src/vfx/`.

**Chỉ được ghi:**
- `vfx/ma-troi-sheet.tryN.png`, `vfx/ma-troi-sheet.tryN.prompt.txt`, `vfx/ma-troi-sheet.png` (file mới; **không sửa** `ma-troi-sheet.prompt.txt` có sẵn);
- `vfx/ma-troi-death.tryN.png`, `.tryN.prompt.txt`, `vfx/ma-troi-death.png`, `.prompt.txt`, `.alpha.png`;
- `games/typing-defense/art-src/_review/099-*.jpg`, `games/typing-defense/art-src/_review/099/`;
- `docs/codex-queue/099-report.md`.

**Phần A, `ma-troi-sheet`:** sinh đúng theo `ma-troi-sheet.prompt.txt` (tờ tham chiếu, nền xanh navy, không cần alpha). Dùng cho giám khảo và làn VFX, không vào game.

**Phần B, `ma-troi-death`:**
- Mở đầu bằng hai đoạn đầu của `vfx/ma-troi-wisp.prompt.txt` (phong cách nhà và luật FLIPBOOK lưới 4 × 4, 1024², ô 256, lề ≥ 24 px).
- FLIPBOOK một lần, 16 khung, nền đen `#000000`:
  - khung 1 giống khung 1 của `ma-troi-wisp` về cỡ và màu;
  - khung 2–5: lửa co lại, chập chờn, mắt nhắm ở khung 4–5;
  - khung 6–10: vỡ thành 6–10 tia nhỏ trắng xanh như thủy tinh;
  - khung 11–16: tia rơi chậm, nhỏ dần tới hết; không mờ dần kiểu trong suốt.
- Hậu kỳ alpha theo cách của phiếu 043: đổi ảnh sáng trên nền đen sang RGBA thẳng (`games/typing-defense/art-src/_review/043/refine-alpha.py`; ghi bản đã dùng).

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/vfx/`: chỉ có file mới; `ma-troi-sheet.prompt.txt` và `ma-troi-wisp.*` giữ nguyên md5.
2. `ma-troi-death.alpha.png`: 1024 × 1024, RGBA; đủ 16/16 ô có hình; lề ≥ 24 px mỗi ô; viền nền 0 px (như 043).
3. **Khớp với wisp:** bbox khung 1 lệch ≤ 10 % so với bbox khung 1 của `ma-troi-wisp.alpha.png`; hue trung vị lệch ≤ 10°.
4. **Tắt hẳn:** tổng alpha khung 16 ≤ 5 % tổng alpha khung 1.
5. **Ảnh kiểm** `_review/099-sheet.jpg`: 16 khung thu về ô 64 px trên `backdrops/w1-silverfall/sky-a.png` và trên cùng nền nhân RGB 0,25 (như 043); cạnh đó là `ma-troi-sheet.png`.
6. **KA5:** `ma-troi-death` ở cỡ đầy đủ và ô 64 px; `ma-troi-sheet` chỉ chấm Đúng đề và Hợp bộ.

**Xong khi:** `ma-troi-death` qua mục 2–4 và tự chấm ≥ 8; `ma-troi-sheet` có ảnh đúng prompt.
