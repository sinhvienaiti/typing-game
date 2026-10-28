# Phiếu 109 · Tuyến Cuối · Bốn ảnh minh họa ải cho thẻ ải và màn Hành trình

**Vì sao:** kiểm kê map 1 (cổng G2). Người kiểm kê chấm thẻ ải 7, màn Hành trình 7, bảng tin 6,5: các màn này chỉ có chữ trên bảng tối, trong khi mức nhận là 8. Bốn ảnh nhỏ, mỗi ải một ảnh, cho người chơi thấy trước ải đó đánh ra sao. Claude gắn ảnh vào thẻ ải và các ô của Hành trình.

**Báo cáo:** `docs/codex-queue/109-report.md`.

## Luật chung (phiếu ảnh)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Tối đa 3 lượt sinh mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-survival/art-src/ui/stages/<tên>.tryN.png`, `.tryN.prompt.txt`;
  - bản chọn `<tên>.png`, `<tên>.prompt.txt`;
  - `games/typing-survival/art-src/_review/109-*.jpg` và `_review/109/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu;
  - dev server, trình duyệt;
  - đụng game khác, Tu Tiên;
  - chữ, số, logo, HUD trong ảnh.

## Phong cách

- **Mức chất lượng (chủ dự án 28/10 tối):** ngang ảnh chủ đạo của game thương mại, với ánh sáng điện ảnh, chiều sâu lớn và quy mô hùng vĩ. Ảnh tham chiếu của chủ dự án nằm ở `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`: lấy mức chi tiết, ánh sáng và cảm giác quy mô, không lấy nội dung. Chữ trên ảnh (nếu có) là tiếng Anh; ảnh này không có chữ.

- **Theo game, không theo màn tựa cũ:** dùng các ảnh của phiếu 088 làm mẫu chất liệu và màu: `games/typing-survival/art-src/arena/concept-fight.png`, `hull-left.png`, `far-structures.png`. Kiểu là 3D gọn, khối rõ, thép than chì, sọc cam đen, đèn LED xanh điện, hố đen cam.
- **Không** vẽ như ảnh chụp, không sàn ướt. `title-horizon.png` lệch phong cách, nên không dùng làm mẫu.
- **Quái là Bầy Hố Đen:** thân tối, gân năng lượng sáng (cam ở Swarm; vàng hổ phách ở Brute; vàng kim ở Pack Leader; xanh ở Scout và Shield Guard). Dáng lấy theo `games/typing-survival/art-src/ui/foes/*.png` (phiếu 089).
- **Tàu Vanguard** của người chơi ở gần mép dưới, nhỏ; quái tràn về phía nó từ cuối hành lang.

## Bốn ảnh, mỗi ảnh 1536 × 864 (16:9), nền đặc

Nhìn dọc hành lang thép từ sau và trên tàu, như góc của trận nhưng hạ thấp hơn một chút, để thấy bầy rõ.

| Tên file | Ải | Cảnh |
|---|---|---|
| `c1-s1` | Ải 1 · Ca trực đầu (trụ vững 2:30) | Bầy Swarm đông đặc tràn tới, vài Scout, một Brute đi sau; tàu bắn hai luồng (Pulse Gun xanh, Heat Beam cam) |
| `c1-s2` | Ải 2 · Săn Pack Leader | Ba Pack Leader to, gân vàng kim, giữa bầy; mỗi con có quầng đánh dấu mục tiêu mảnh (vẽ như ánh sáng, không chữ) |
| `c1-s3` | Ải 3 · Vách nứt | Một vết nứt không gian phát sáng cam tím xé ngang hành lang, bầy chui ra từ đó |
| `c1-s4` | Ải 4 · Khiên sáng | Hàng Shield Guard giơ khiên năng lượng xanh, chắn đạn phía trước; Splitter phía sau |

Đọc `games/typing-survival/src/content/chapter-1.ts` (chỉ đọc) để chắc tên và mục tiêu của từng ải. Ải nào khác bảng trên thì theo mã, và ghi rõ vào báo cáo.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước (`_review/109/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Khổ:** `magick identify` ra 1536 × 864 cho bốn bản chọn. Công cụ trả khổ khác thì cắt giữa rồi thu bằng Lanczos; ghi lệnh.
3. **Đọc được ở cỡ nhỏ:** thu về 384 × 216. Tách được tàu, bầy, và vật riêng của ải (Pack Leader, vết nứt, khiên) bằng mắt. Ghi "được" hay "không" cho từng ảnh.
4. **Không chữ, không HUD:** xem ở cỡ đầy đủ.
5. **Cùng bộ:** luma trung bình của bốn ảnh lệch nhau ≤ 0,06; hue trung vị lệch ≤ 15°.
6. **Tờ** `_review/109-sheet.jpg`: bốn ảnh ở 768 px, kèm bản 384 px, và `concept-fight.png` bên cạnh để so phong cách.
7. **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở 384 px.

**Xong khi:** bốn ảnh có bản chọn tự chấm từ 8 và qua mục Kiểm 1–5. **Nhận** khi Claude chấm lại từ 8.
