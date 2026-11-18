# Phiếu 096 · Rồng Giữ Ải · Huy hiệu và chữ logo cho màn tựa

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 095 của lô). Số phiếu ảnh đổi thêm 1 vì 094 đã dùng cho từ vựng Rồng. Mọi số phiếu trong phiếu này đã đổi theo.

**Báo cáo:** `docs/codex-queue/096-report.md`.

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

**Vì sao:** kiểm kê map 1 (DH-14, P1, cổng G5). Rồng chưa có màn tựa; mở game là gặp ngay câu hỏi tốc độ. Claude sẽ làm màn tựa trên nền cảnh map (DH-13) và cần một hình tựa.

**Lưu ý chữ:** công cụ tạo ảnh hay viết sai dấu tiếng Việt. Vì vậy phiếu tách làm hai phần. Phần A (huy hiệu không chữ) là bắt buộc. Phần B (chữ logo) là thử: chỉ nhận khi đúng hết dấu. Nếu không, Claude đặt chữ bằng font của game.

**Nơi ghi:** `games/dragon-hold/art-src/ui/title/` (thư mục mới).

**Chỉ được ghi:**
- `ui/title/title-emblem.*`, `ui/title/title-logo.*` (các dạng `.tryN.png`, `.tryN.prompt.txt`, `.png`, `.prompt.txt`, `.alpha.png`, `.256.png`);
- `games/dragon-hold/art-src/_review/096-*.jpg`, `games/dragon-hold/art-src/_review/096/`;
- `docs/codex-queue/096-report.md`.

**Phong cách:**
- Câu phong cách nhà ở dòng đầu `games/dragon-hold/art-src/backdrops/pine-river-far.prompt.txt` (storybook, rừng thông sương, moss green, pine blue, muted violet, warm cream).
- Màu Hỏa Long: xem `games/dragon-hold/art-src/ui/icons/skill-fire-breath.png`, `skill-sky-fire.png`, `dragon-heart.png`.

**Phần A, `title-emblem` (bắt buộc):**
- Hỏa Long (rồng lửa đỏ cam, bụng kem ấm, sừng và gai sẫm) cuộn quanh hoặc đậu trên một cổng ải bằng đá cũ, hai bên có cây thông, một lọn lửa nhỏ.
- Toàn khối là một huy hiệu tròn trịa, rộng hơn cao (khoảng 4 : 3), để chữ đặt bên dưới.
- Đọc được dáng ở 64 px. Không chữ, không số.
- Nền `#FF00FF` phẳng để tách; vật không có màu hồng hay tím sáng.

**Phần B, `title-logo` (thử, tối đa 3 lượt):**
- Chữ vẽ tay "Rồng Giữ Ải" màu kem ấm, viền xanh thông sẫm, ánh than hồng nhẹ; nét cọ có chân.
- Đúng từng chữ: R-ồ-n-g, G-i-ữ, Ả-i. Ba dấu phải đúng: `ồ` (o, mũ, huyền), `ữ` (ư, ngã), `Ả` (A hoa, hỏi).
- Nền `#FF00FF`.

**Hậu kỳ:** tách nền bằng `tools/art-normalize` (hay ImageMagick, ghi lệnh). Ra `<tên>.alpha.png` cạnh dài 1024 px và `<tên>.256.png` cạnh dài 256 px.

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/dragon-hold/art-src/ui/`.
2. **Tách nền sạch:** 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở 4× phóng (`_review/096-edge.jpg`).
3. **Lề:** bbox của vật cách mép ảnh ≥ 32 px ở bản 1024.
4. **Ảnh kiểm** `_review/096-proof.jpg`: mỗi bản chọn trên nền tối `#14201a` và nền sáng `#efe6d2`, ở 1024, 256 và 64 px. Ghi: ở 64 px còn nhận ra rồng và cổng không.
5. **Chính tả (phần B):** cắt phóng 4× từng chữ có dấu, đặt cạnh cùng chữ in bằng một font hệ thống có dấu tiếng Việt (ghi tên font). Sai một chữ hay một dấu là loại lượt đó.
6. **KA5** ở 1024 và 256 px.

**Xong khi:** `title-emblem` có alpha, qua mục 2–4 và tự chấm ≥ 8. Phần B: hoặc một bản đúng chính tả và ≥ 8, hoặc ghi "không đạt sau N lượt, dùng font" kèm ảnh lượt tốt nhất.
