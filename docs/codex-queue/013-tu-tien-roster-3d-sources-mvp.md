# Phiếu 013 · Tu Tiên Thủ Ải · ảnh nguồn 3D cho 4 nhân vật MVP

**Bối cảnh:** chủ dự án duyệt cả 10 chân dung của phiếu 009 ngày 25/10 ("10 ảnh kia đạt"; canon D49). Bước kế: ảnh nguồn để dựng 3D (chủ dự án dựng bằng Tripo, Claude rig trong Blender).

Phiếu này làm **4 nhân vật MVP**: Kiếm nữ, Kiếm nam, Thổ thể nam, Thổ thể nữ, cộng pháp khí cầm tay của họ. Sáu nhân vật sau MVP để phiếu 013b.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/13-roster-3d-sources.md` (file prompt mới);
- `games/immortality-cultivation/art-src/cultivators/` và `art-src/treasures/` (ảnh);
- `games/immortality-cultivation/art-src/README-013.md`;
- mục 6.1 (bảng Tu Tiên) của `docs/games/3D_REQUESTS.md`.

Không chạy git, không sửa mã hay canon.

## Nguồn phải đọc trước

- Canon `docs/games/tu-tien/00-canon.md`:
  - D47: phong cách quý phái;
  - D49: danh sách nhân vật và pháp khí đã duyệt;
  - §21.2: quy trình model, clip của `cultivators`, 8.000–30.000 tam giác.
- **Mẫu viết ảnh nguồn:** `docs/games/tu-tien/art-requests/m0b/01-cultivators-bots.md`. Giữ đúng khối luật nguồn Tripo của file này:
  - tư thế A, tay thẳng xuống và mở 30° khỏi thân, bàn tay để trống, ngón tách;
  - gần trực giao, camera ngang ngực;
  - nền phẳng tuyệt đối `#E6E6E6`, không bóng tiếp đất, không cảnh, không hiệu ứng;
  - giữ đủ khoảng trống quanh đỉnh miện và gót chân.
- **Chân dung đã duyệt, dùng làm chuẩn thiết kế** (giữ mặt, tóc, miện hoặc trâm, phục sức, bảng màu): `games/immortality-cultivation/art-src/roster/{kiem-nu,kiem-nam,tho-the-nam,tho-the-nu}.png` và prompt cạnh ảnh.
- **Ghi chú của phiếu 008 về Kiếm nữ:** `art-src/README-m0b.md`. Bản cũ `cultivators/kiem-tu.png` có tay chưa mở đủ, nền chưa đúng mã.

## Việc

1. **Viết file prompt `13-roster-3d-sources.md`** theo cách viết của `01-cultivators-bots.md`. Mỗi ảnh một khối `text` cùng phần ghi 3D:
   - face limit;
   - cách rig;
   - danh sách clip;
   - ảnh đính kèm.
2. **Tạo ảnh bằng `image_gen`.** Mỗi nhân vật 2 ảnh: trước và sau, 1024×1536.
   - Ảnh sau đính kèm ảnh trước (chuẩn hình khối, tư thế) và chân dung (chuẩn phục sức).
   - Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
   - Ảnh đã có thì bỏ qua.

| Mã | Ảnh | Đính kèm | Ghi chú |
|---|---|---|---|
| NV01 Kiếm nữ | `cultivators/kiem-nu.png`, `kiem-nu-back.png` | `roster/kiem-nu.png`; bản cũ `cultivators/kiem-tu.png` để sửa | Mở tay đủ 30°, nền đúng mã. Bản cũ `kiem-tu.*` giữ nguyên làm lịch sử |
| NV03 Kiếm nam | `cultivators/kiem-nam.png`, `-back.png` | `roster/kiem-nam.png` | |
| NV02 Thổ thể nam | `cultivators/tho-the-nam.png`, `-back.png` | `roster/tho-the-nam.png` | Găng đá ngọc là đồ mặc, nằm trên tay, bàn tay vẫn mở. Thay `tho-the-tu.*` của phiếu 007 (giữ làm lịch sử) |
| NV04 Thổ thể nữ | `cultivators/tho-the-nu.png`, `-back.png` | `roster/tho-the-nu.png` | Trượng đá là vật riêng: tay để trống |
| PB01-S | `treasures/thanh-phong-kiem-side.png` | `treasures/thanh-phong-kiem.png` | Góc cạnh của kiếm, nếu phiếu 007b chưa làm |
| PB03 | `treasures/truong-da-tho.png`, `-side.png` | `roster/tho-the-nu.png` | Trượng đá đầu vuông của Thổ thể nữ: vật tĩnh, nền `#E6E6E6`, đặt thẳng đứng giữa ảnh |

- **Áo dài nhiều lớp:** giữ đúng như chân dung, nhưng tà áo và tay áo không che chân, bàn tay hay khớp vai. Bóng áo tách khỏi thân đủ để rig.
- **Bot Đạo Đồng** không có ảnh nguồn riêng: bot dùng model của trường phái còn lại và đổi màu áo (canon §21.2). Ghi `BOT01` là đã thay thế trong `3D_REQUESTS.md`.

3. **Cập nhật mục 6.1 của `docs/games/3D_REQUESTS.md`.** Thêm hoặc sửa dòng NV01–NV04, PB01, PB03:
   - đường ảnh trước và sau;
   - **face limit 20000** cho cả 4 nhân vật;
   - **cách rig: tự rig Blender cho cả 4 nhân vật**:
     - lý do: áo dài nhiều lớp cần xương tà áo; preset Tripo thiếu các clip Cast;
     - một bộ xương mẫu người + tà áo dùng chung, chép clip giữa các nhân vật, nên 0 credit rig;
   - clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory;
   - **pháp khí:** không rig, gắn ổ cắm ở tay.
4. **Kiểm từng ảnh.** Mở xem từng ảnh. Đo màu nền ở 4 góc và quanh chân.
   - Lệch `#E6E6E6` thì ghi số đo, không sửa bằng mã.
   - **Không dùng `tools/art-normalize`** trừ khi `docs/CODEX_QUEUE.md` ghi phiếu 012 "Claude đã duyệt".
5. **Viết `README-013.md`.**
   - Bảng ảnh: lượt sinh, đạt hay chưa, số đo nền, độ mở tay.
   - Những gì chủ dự án nên xem trước khi gửi Tripo.
   - Ảnh xem nhanh `art-src/_review/013-sources.png`, làm bằng ImageMagick trong WSL: `~/.local/bin/magick`, ổ `D:` là `/mnt/d`.

**Xong khi:**
- file prompt viết xong;
- 8 ảnh nhân vật cùng ảnh pháp khí có đủ, hoặc ghi lý do cho ảnh thiếu;
- `3D_REQUESTS.md` đã cập nhật;
- README và ảnh xem nhanh đã có.
