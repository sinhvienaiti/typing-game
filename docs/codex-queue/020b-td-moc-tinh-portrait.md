# Phiếu 020b · Lời Gọi · vẽ lại chân dung Mộc Tinh (C21)

**Luật:** ảnh 2D phải từ 8 điểm (chủ dự án 27/10, `docs/games/ART_ACCEPTANCE.md` §2.2). Dưới 8 thì tạo lại, tối đa 3 lượt.

**Bối cảnh:**
- C21 `games/typing-defense/art-src/portraits/moc-tinh.png` được 6 điểm: ra toàn thân, mặt nhỏ ở 64 px, thiếu vệt mực tím và viền mực.
- Phiếu 017 đã cắt và thêm viền (`moc-tinh.crop.png`, bản lượt 2 ở `games/dragon-hold/art-src/_review/017/moc-tinh.crop.retry.png`). Claude chấm 7,5: khung đã đúng, nhưng vệt mực tím là hai dải phẳng như dán vào, không phải nét cọ, nên chưa đạt.
- Ảnh 2D rẻ, nên lần này tạo lại.

Chủ dự án yêu cầu Codex làm đúng, không sai sót: mục "Kiểm" là bắt buộc. Claude chấm lại trước khi thay ảnh.

**Được ghi:**
- `games/typing-defense/art-src/portraits/moc-tinh.tryN.png` và `moc-tinh.tryN.prompt.txt` (N = 1, 2, 3);
- `games/typing-defense/art-src/_review/020b-*.jpg`, `_review/020b/`;
- `docs/codex-queue/020b-report.md`.

**Cấm:**
- ghi đè, đổi tên, xóa file có sẵn;
- chạy git; sửa mã hay tài liệu `ART_*`;
- đụng file của phiếu 020 đang chạy song song (các ảnh khác trong `portraits/`, `scenery/`, `branches/`, `ground/`).

## Việc

1. **Đọc:**
   - `moc-tinh.prompt.txt`;
   - dòng C21 ở `docs/games/ART_FIX_QUEUE.md` §2;
   - xem 3 chân dung cùng bộ đã đạt (`draconis.png`, `helper-cham-happy.png`, `dai-bang-tinh.png`) để giữ khổ 1254×1254, nền xanh `#00FF00` phẳng, cỡ đầu trong khung, độ dày viền mực, cách đặt vệt mực.
   - Đính kèm `moc-tinh.png` làm mẫu dáng, màu, tán lá, quả.
2. **Prompt** = prompt cũ cộng các điểm sau:
   - chân dung đầu, tán và ngực (không chân, không toàn thân);
   - mặt to, đọc rõ ở 64 px;
   - viền mực tối quanh dáng như bộ;
   - **một nét cọ mực tím `#6B3FA0` tự nhiên** phía sau vai, đầu nét đậm, đuôi khô (không phải dải phẳng), không đè mặt;
   - nền `#00FF00` phẳng.
3. **Tự chấm** từng lượt theo 5 tiêu chí của `ART_ACCEPTANCE.md` §1, ở 128 px và 64 px. Từ 8 thì dừng; chưa tới 8 thì sửa prompt đúng chỗ thiếu, tối đa 3 lượt.

## Kiểm (bắt buộc)

1. **md5:** `md5 -r` của mọi file trong `portraits/` trước khi làm (`_review/020b/md5-before.txt`) và sau khi làm (`md5-after.txt`). `diff` chỉ được có các dòng file `moc-tinh.try*` mới thêm.
2. **Khổ và nền:** mỗi lượt 1254×1254, bốn góc `#00FF00` (± 8 mỗi kênh). Ghi `magick identify` và màu 4 góc.
3. **Tờ xem nhanh** `_review/020b-moc-tinh.jpg`:
   - một hàng: `moc-tinh.png` | bản retry của 017 | mọi lượt mới;
   - một hàng cỡ game: bản chọn ở 128 px và 64 px, đặt cạnh `draconis.png` cùng cỡ;
   - có nhãn (font Arial như các phiếu trước).

## Báo cáo `docs/codex-queue/020b-report.md`

Bảng `| Lượt | Prompt thêm | Điểm 5 tiêu chí | Tổng | Còn thiếu |`, kèm bản chọn và đầu ra mục Kiểm.

**Xong khi:** có lượt từ 8 điểm, hoặc đủ 3 lượt và ghi bản tốt nhất.
