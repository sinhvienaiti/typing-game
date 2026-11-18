# Phiếu 020 · Rồng Giữ Ải, Lời Gọi · làm lại 9 ảnh 2D dưới 8 điểm

**Luật mới của chủ dự án (27/10/2026):** "chỉ tiết kiệm chi phí với ảnh 3D, còn ảnh 2D thì cứ phải đạt trên 8 điểm thì mới cho pass, vì ảnh 2D chi phí sẽ luôn rẻ hơn". Luật đầy đủ ở `docs/games/ART_ACCEPTANCE.md` §2.2:
- ảnh 2D phải **từ 8 điểm**;
- dưới 8 mà sửa được bằng công cụ thì sửa trước;
- không thì tạo lại, **tối đa 3 lượt một ảnh**.

Chín ảnh dưới đây đang 7–7,5 điểm. Danh sách, chỗ thiếu và cách làm ở `docs/games/ART_FIX_QUEUE.md` §3b. Chủ dự án cũng yêu cầu Codex làm đúng, không sai sót: mục "Kiểm" là bắt buộc, và Claude chấm lại trước khi nhận.

**Thư mục làm việc:** gốc repo. Chỉ được ghi:
- `<thư mục của ảnh>/<tên>.try1.png`, `.try2.png`, `.try3.png` và `<tên>.tryN.prompt.txt` (prompt đã dùng);
- bản sửa bằng công cụ: `<tên>.fix.png`;
- `games/<game>/art-src/_review/020-*.jpg`, `games/<game>/art-src/_review/020/`;
- `docs/codex-queue/020-report.md`.

**Cấm:**
- ghi đè, đổi tên hay xóa file có sẵn: ảnh đang dùng giữ nguyên tên, **Claude thay sau khi duyệt**;
- chạy git; sửa mã, `ART_*.md`, `IMAGE_AUDIT_*.md`;
- đụng Tu Tiên, Space, `typing-game-handoff-*`;
- làm ảnh ngoài 9 ảnh này.

## Ảnh

| # | Mã | Ảnh đang dùng | Điểm | Mức | Điểm chính phải đạt (đọc đủ ở ART_FIX_QUEUE §3b, cột "Thiếu gì") |
|---|---|---|---:|---|---|
| 1 | T3 Rêu dưới tán | `games/dragon-hold/art-src/ground/pine-river/moss.png` | 7,5 | P1 | Ô đất lặp liền mép 1024×1024; rêu phẳng, chỉ chênh màu, không bóng, không gò; tương phản thấp ngang `grass-a.png`; chỉ 2–3 sắc xanh rêu và lam lục; không lá, cành, kim thông. Ghép 2×2 và 3×3 không thấy đường nối. |
| 2 | C23 Draconis tối thượng | `games/typing-defense/art-src/portraits/draconis-ult.png` | 7 | P1 | Mưa lông lửa rơi xuống, không phải xoáy; nền cam đào như bộ (không đỏ); nét vừa phải; đọc rõ trong dải cắt 3:1. |
| 3 | C9 Lam | `…/portraits/lam.png` | 7 | P2 | Chân dung đầu và thân trên (không toàn thân); cười lớn; lửa xanh; viền mực rõ; đủ lề phía tai và lửa; nền như chân dung khác. |
| 4 | C10 Tre | `…/portraits/tre.png` | 7 | P2 | Chân dung đầu và thân trên; có chuồn chuồn; búa đặt trên vai; viền mực rõ. |
| 5 | C25 Tre tối thượng | `…/portraits/tre-ult.png` | 7 | P2 | Giơ búa cao (không vung ngang); giàn tre đang **dựng lên**, không đang vỡ; nét vừa phải; đọc rõ trong dải cắt 3:1. |
| 6 | C22 Đại Bàng Tinh | `…/portraits/dai-bang-tinh.png` | 7 | P2 | Đầu và ngực, quay phải; có vệt mực, viền mực; không nét nào giống chữ trên đồ đồng. |
| 7 | S15-v2 Ô-liu v2 | `games/typing-defense/art-src/scenery/coast/olive-tree-v2.png` | 7 | P2 | Cùng màu, nét v1 (`olive-tree-v1.png`), nhưng dáng **nghiêng phải rõ**, khác v1 ở bóng dáng; lá ít, gom khối; khổ dọc, đủ lề gốc. |
| 8 | S16-v2 Phi lao v2 | `…/scenery/coast/casuarina-v2.png` | 7 | P2 | Cùng màu, nét v1, nhưng thân **ngả theo gió rõ**, khác v1; tán theo gió; lá gom khối; đủ lề gốc. |
| 9 | V35 Trại Lính, nhánh Giáo Dài | `games/typing-defense/art-src/branches/barracks-giao-dai.png` | 7,5 | P2 | Ảnh nguồn Tripo, nên chưa gửi Tripo tới khi đạt. Giữ dáng tháp hai tầng như bản hiện tại (phiếu 015c), cao **bằng** tháp `buildings/barracks-v2.png` cùng bề ngang chân; giá giáo bó kín thành một khối, không khe giữa mũi; không chấm xanh lạ. Nền BG-G 1024×1024 như phiếu 015c. Đính kèm `barracks-v2.png` và bản hiện tại làm ảnh mẫu. |

## Cách làm từng ảnh

1. **Đọc trước:**
   - `<tên>.prompt.txt` cạnh ảnh;
   - dòng của ảnh ở ART_FIX_QUEUE §3b;
   - 2–3 ảnh cùng bộ để giữ hợp bộ: chân dung cùng thư mục `portraits/`, cây cùng `scenery/coast/`, ô đất cùng `ground/pine-river/`.
   - Với Lời Gọi: giữ phong cách viền mực (`games/typing-defense/docs/art-requests/td/015b-priority.md`, mục phong cách).
2. **Sửa bằng công cụ trước** nếu mọi chỗ thiếu chỉ là khung, lề, nền, màu, lật ngang. Ví dụ C22: cắt đầu và ngực, lật ngang, thêm viền mực. Ra `<tên>.fix.png`, rồi tự chấm. Từ 8 điểm thì dừng ở đây.
3. **Không thì tạo lại:**
   - prompt = prompt cũ cộng câu nhấn đúng các điểm ở cột "Điểm chính phải đạt";
   - ghi prompt vào `<tên>.tryN.prompt.txt`, ảnh vào `<tên>.tryN.png`;
   - tự chấm theo thang 10 điểm của `ART_ACCEPTANCE.md` §1, ở cỡ ảnh hiện trong game.
   - Dưới 8 thì sửa prompt theo chỗ còn thiếu và thử tiếp, tối đa 3 lượt.
4. **Sau 3 lượt vẫn dưới 8:** ghi bản tốt nhất kèm lý do, không thử thêm.

## Kiểm (bắt buộc)

1. **md5:** trước khi làm, ghi `md5 -r` của 9 ảnh đang dùng vào `games/typing-defense/art-src/_review/020/md5-before.txt`; cuối cùng ghi `md5-after.txt`. `diff` hai file phải rỗng.
2. **File mới:** liệt kê mọi file mới (`find games/dragon-hold/art-src games/typing-defense/art-src -newer …/md5-before.txt -type f`). Chỉ được có tên theo mẫu ở trên.
3. **Riêng T3:**
   - đúng 1024×1024;
   - `bash tools/art-normalize/seam-check.sh <file> <file>.seam.png --axis xy` (export `ART_MAGICK=/opt/homebrew/bin/magick`), ghi MAE mép;
   - ghép 3×3, đặt cạnh ghép 3×3 của `grass-a.png`.
4. **Riêng C23 và C25:** cắt dải 3:1 ở giữa ảnh, đặt cạnh dải 3:1 của `draconis-ult.png` cũ.
5. **Riêng V35:** đặt cạnh `buildings/barracks-v2.png` cùng bề ngang chân. Đo chiều cao vật của mỗi ảnh theo px (hộp bao alpha hoặc nền), ghi tỉ lệ; đích ≥ 95 %.
6. **Tờ xem nhanh:** `_review/020-dh.jpg` và `_review/020-td.jpg`.
   - Mỗi hàng: ảnh đang dùng | mọi lượt thử | bản chọn ở cỡ game.
   - Cỡ game: chân dung 128 px và 64 px; cây 160 px; ô đất ghép 3×3.
   - Nhãn mã và điểm ở mỗi hàng (font `/System/Library/Fonts/Supplemental/Arial.ttf`).
   - Tự xem kỹ trước khi viết báo cáo.

## Báo cáo `docs/codex-queue/020-report.md`

Bảng: `| # | Mã | Cách (sửa / tạo lại) | Số lượt | File chọn | Điểm từng tiêu chí (5 × 0–2) | Tổng | Còn thiếu gì |`. Thêm kết quả kiểm mục 1, 2 (dán đầu ra) và số đo mục 3–5.

**Xong khi:** mỗi ảnh có bản từ 8 điểm, hoặc đã đủ 3 lượt và ghi bản tốt nhất. Claude chấm lại (ảnh 7,5–8,5 có người chấm thứ hai), rồi mới thay ảnh đang dùng, cập nhật các danh sách và bộ gửi Tripo.
