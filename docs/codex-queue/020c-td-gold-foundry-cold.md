# Phiếu 020c · Lời Gọi · vẽ lại nhánh Lò Đúc Tiền với lò nguội (V37, ảnh nguồn Tripo)

**Luật:** ảnh 2D phải từ 8 điểm (chủ dự án 27/10, `docs/games/ART_ACCEPTANCE.md` §2.2). Ảnh nguồn Tripo còn theo luật không ánh sáng: không có vùng phát sáng nào nướng vào texture.

**Bối cảnh:**
- V37 `games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png` được 8,5 điểm, nhưng miệng lò cháy cam và dòng vàng chảy phát sáng. Gửi Tripo như vậy thì model sẽ "sáng" mãi.
- Phiếu 017 đã tô màu than lên đúng vùng đó hai lần. Kết quả là một mảng đỏ phẳng đè lên lòng lò, Claude không nhận.
- Ảnh 2D rẻ, nên lần này tạo lại.

Chủ dự án yêu cầu Codex làm đúng, không sai sót: mục "Kiểm" là bắt buộc. Claude chấm lại trước khi gửi Tripo.

**Được ghi:**
- `games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.tryN.png` và `.tryN.prompt.txt` (N = 1, 2, 3);
- `games/typing-defense/art-src/_review/020c-*.jpg`, `_review/020c/`;
- `docs/codex-queue/020c-report.md`.

**Cấm:**
- ghi đè, đổi tên, xóa file có sẵn;
- chạy git; sửa mã hay tài liệu `ART_*`;
- đụng file của phiếu 020 và 020b.

## Việc

1. **Đọc:**
   - `gold-mine-lo-duc-tien.prompt.txt`;
   - mục V37 trong `games/typing-defense/docs/art-requests/td/02-tripo-buildings-props-vs.md`;
   - `docs/games/ART_FIX_QUEUE.md` §5.1 dòng V37.
   - Đính kèm ảnh hiện tại làm mẫu dáng (giữ nguyên bố cục: ống khói, mái ngói đỏ, gian lò đá có vòng xoắn, máng, bao tiền, thùng vàng, nền đá với vân vàng, cửa hầm, ray nếu có).
2. **Prompt** = prompt cũ cộng: *the foundry is cold and idle: the furnace mouth is soot-black stone with no fire and no glow; the trough holds a few cooled gold ingots, matte ochre, not molten, no light, no emissive colour anywhere*. Màu vàng của thỏi và vân quặng giữ vàng đất đậm (khoảng `#C8962E`), không vàng chanh sáng.
3. **Tự chấm** từng lượt theo 5 tiêu chí ở cỡ 128 px. Thêm một điều kiện: không vùng nào trông như đang phát sáng. Đạt thì dừng; chưa thì sửa prompt, tối đa 3 lượt.

## Kiểm (bắt buộc)

1. **md5:** `md5 -r` của mọi file trong `branches/` trước (`_review/020c/md5-before.txt`) và sau. `diff` chỉ được có dòng file `.try*` mới.
2. **Độ sáng vùng lò:** đo độ sáng trung bình (`-colorspace Gray`) và tỉ lệ px có độ sáng > 0,85 trong hộp quanh miệng lò và máng của bản chọn. So với cùng hộp trên ảnh hiện tại. Đích: tỉ lệ px sáng gắt giảm ít nhất 80 %. Ghi tọa độ hộp và số đo.
3. **Khổ và nền:** 1024×1024, nền xanh BG-G phẳng như ảnh hiện tại. Ghi `magick identify` và màu 4 góc.
4. **Tờ xem nhanh** `_review/020c-v37.jpg`:
   - hàng 1: ảnh hiện tại | mọi lượt;
   - hàng 2: bản chọn ở 128 px và 64 px, đặt cạnh `branches/gold-mine-ham-sau.png` (nhánh kia) cùng cỡ để xem hợp bộ;
   - có nhãn.

## Báo cáo `docs/codex-queue/020c-report.md`

Bảng `| Lượt | Prompt thêm | Điểm 5 tiêu chí | Tổng | Có vùng phát sáng? | Còn thiếu |`, kèm bản chọn và đầu ra mục Kiểm.

**Xong khi:** có lượt từ 8 điểm và không vùng phát sáng, hoặc đủ 3 lượt và ghi bản tốt nhất.
