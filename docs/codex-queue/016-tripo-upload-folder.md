# Phiếu 016 · Gom ảnh cần dựng 3D vào một thư mục để chủ dự án đưa lên Tripo

**Bối cảnh:** chủ dự án muốn mọi ảnh 2D cần dựng 3D của **Rồng Giữ Ải, Lời Gọi, Tuyến Cuối** nằm chung một thư mục, **nhóm theo face limit**, để đưa lên Tripo3D. **Không gồm Tu Tiên.**

Phiếu có thể chạy nhiều lần: lần sau chỉ thêm model mới và cập nhật mục lục.

**Nguồn danh sách:** `docs/games/3D_REQUESTS.md`, mục §3 (bảng theo face limit và cách rig). Ảnh lấy từ `art-src/` của từng game, **ảnh gốc**, không dùng `*.tripo.png` của phiếu 012 (chưa qua phản biện).

**Thư mục đích (ngoài repo, để media không bao giờ vào Git):** `D:\tripo-upload\`.

**Bố cục phẳng** (chủ dự án yêu cầu 25/10: không mở từng thư mục con, không phải đọc file hướng dẫn):

```text
D:\tripo-upload\
  INDEX.md                                             mục lục ngắn
  _GLB tải về\                                         chủ dự án lưu GLB tải về ở đây
  face 6000 - rig Tripo Biped (Idle Walk Attack Death) - multiview\
  face 6000 - KHÔNG bấm rig (Claude rig sau) - 1 ảnh\
  face 2000 - không rig - 1 ảnh\
  …                                                    một thư mục cho mỗi bộ (face, rig, chế độ)
    rong_moss-grunt_front.png  rong_moss-grunt_back.png     multiview: <game>_<id>_<front|back|left>.png
    loigoi_piggy.png                                        1 ảnh: <game>_<id>.png
```

- **Mã game:** `rong` (Rồng Giữ Ải), `loigoi` (Lời Gọi), `tuyencuoi` (Tuyến Cuối).
- **Không có thư mục con theo model**, không `tripo.txt`, không `_sheet.jpg`.
- Rig, face, chế độ đọc từ cột tương ứng của `3D_REQUESTS.md`. Thiết lập chung (tách nền, PBR, lưới tam giác) ghi một lần trong `INDEX.md`.
- **Ảnh đã có trong thư mục thì giữ nguyên;** chỉ thêm model mới vào đúng thư mục.
- **Lưu ý về ảnh lỗi chưa sửa:** ghi một dòng cạnh model trong `INDEX.md`.

## Việc

1. Đọc §3 của `3D_REQUESTS.md`; lấy mọi dòng của 3 game có trạng thái "có ảnh".
2. Chép ảnh (không di chuyển, không sửa) vào đúng thư mục theo bố cục phẳng ở trên, đặt tên đúng mẫu.
3. **Thiếu ảnh** thì không chép; ghi vào `INDEX.md` mục "Chờ ảnh".
4. Kiểm: số file, mã băm khớp nguồn, không trùng tên.
5. **`INDEX.md`:**
   - bảng thư mục: số model, số ảnh; dưới mỗi thư mục, danh sách `<game>_<id>`: tên Việt;
   - tổng số model, tổng credit rig;
   - thứ tự nên làm: Rồng Giữ Ải trước, rồi Lời Gọi bậc P, Tuyến Cuối, Lời Gọi bậc VS;
   - mục "Chờ ảnh".
6. Báo cuối: số model đã gom theo từng nhóm face, đường dẫn `INDEX.md`.

Không chạy git. Không ghi vào repo, trừ khi phát hiện dòng `3D_REQUESTS.md` sai đường dẫn ảnh. Khi đó chỉ sửa đúng dòng ấy và ghi lại.

**Xong khi:** `D:\tripo-upload\INDEX.md` và các nhóm face đã có, mọi model "có ảnh" của 3 game đều nằm trong đó.
