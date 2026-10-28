# Phiếu 106 · Lời Gọi · Cảnh vật meadow: thêm biến thể v3 và v4 cho 13 loại (26 ảnh)

**Vì sao:** bước 1C đưa map 1 (w1-silverfall) lên 3D. Theo C0 (`games/typing-defense/docs/td/BUILD_1C_MAP1.md` §10) và TK §23.10, mỗi loại cảnh vật cần ít nhất 4 biến thể, để rừng và đồng cỏ 3D không lặp. Hôm nay mỗi loại mới có v1 và v2. Ảnh cần xong trước C9 (07/11).

**Báo cáo:** `docs/codex-queue/106-report.md`.

## Luật chung (phiếu ảnh)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt đúng chỗ thiếu, tối đa 3 lượt sinh mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-defense/art-src/scenery/meadow/<loại>-v3.*` và `<loại>-v4.*`;
  - `games/typing-defense/art-src/scenery/shared/tree-stump-v3.*` và `tree-stump-v4.*`;
  - các dạng: `.tryN.png`, `.tryN.prompt.txt`, bản chọn `.png`, `.prompt.txt`;
  - `games/typing-defense/art-src/_review/106-*.jpg` và `_review/106/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả v1, v2 và `.v1.png`); xóa file `.try*`;
  - mọi lệnh git;
  - sửa mã hay tài liệu;
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - đụng game khác; đọc hay ghi Tu Tiên;
  - chữ, số, logo, khung trong ảnh.

## 13 loại

- **12 loại ở `games/typing-defense/art-src/scenery/meadow/`:** `almond-tree`, `bamboo-clump`, `canopy-block`, `fern`, `mountain-pine`, `raspberry-bush`, `reed-clump`, `rock-medium`, `rock-small`, `rotten-log`, `tall-grass`, `wildflowers`.
- **1 loại ở `scenery/shared/`:** `tree-stump`.

## Prompt

- Đọc `<loại>-v1.prompt.txt` và `<loại>-v2.prompt.txt` của từng loại, cùng `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3.1 (STYLE), §3.2 (SCENERY), §3.8 (dòng nền) và §3.9 (dòng MATCH, SAME).
- Mở đầu bằng khối STYLE nguyên văn, rồi khối SCENERY nguyên văn.
- Đính kèm `<loại>-v1.png` và `<loại>-v2.png` làm ảnh tham chiếu, với dòng MATCH của §3.9: cùng phong cách, màu, viền mực, ánh sáng, nhưng **một cá thể khác**.
- **Dáng phải khác rõ v1 và v2:** khác hướng nghiêng, chiều cao, số và cách xếp khối tán hay khối đá. Ghi trong prompt khác ở điểm nào. Ví dụ: cây thấp và tán rộng; cây cao, gầy, nghiêng trái; bụi hai khối lệch.
- **Dòng nền theo đúng §3.8.** Cây cỏ có màu xanh lá: nền M (`#FF00FF`), không có hồng hay tím trong vật. Đá, gốc cây, khúc gỗ mục không có xanh lá: nền G (`#00FF00`). Vật có cả xanh lá và hồng hay tím: nền B. Ghi nền đã dùng cho từng loại.
- Khổ: cạnh dài ≥ 1024 px, như v1, v2 (hôm nay 1254 × 1254).

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/scenery/` (đệ quy) trước (`_review/106/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Khổ:** `magick identify`: cạnh dài ≥ 1024 cho cả 26 bản chọn.
3. **Nền sạch:**
   - 10 px mép bốn phía là màu nền đúng: mỗi kênh lệch ≤ 12 so với màu nền;
   - trong vật (px lệch màu nền > 60 ở một kênh), px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %.
4. **Một vật, chân ở đáy:**
   - tách nền bằng `magick <ảnh> -fuzz 18% -fill none -draw "color 0,0 floodfill" -alpha extract -trim -format '%X %Y %w %h' info:` (hoặc cách tương đương, ghi lệnh);
   - đáy hộp bao cách mép dưới ≤ 12 % chiều cao ảnh; lề trái, phải, trên ≥ 3 %;
   - đúng một khối liền lớn (đếm vùng liền có diện tích > 1 % ảnh: phải là 1).
5. **Khác v1, v2:** tỉ lệ rộng : cao của hộp bao, và vị trí cột cao nhất, phải khác ít nhất một trong hai bản cũ ≥ 15 %. Ghi bảng số cho từng loại.
6. **Tờ so** `_review/106-sheet.jpg`: mỗi loại một hàng v1, v2, v3, v4, cùng cỡ cao 256 px, trên nền `#7fa651`, có nhãn.
7. **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở 128 px.

## Báo cáo `docs/codex-queue/106-report.md`

Tiếng Việt:
- bảng `| Loại | Bản | Lượt | Nền | Khác v1, v2 ở đâu | Điểm 5 tiêu chí | Tổng |`;
- đầu ra bảy mục Kiểm;
- bản chọn và lý do.

**Xong khi:** đủ 26 ảnh có bản chọn tự chấm từ 8 và qua mục Kiểm 1–5. Loại nào không đạt sau 3 lượt thì ghi bản tốt nhất kèm lý do. **Nhận** khi Claude chấm lại từ 8.
