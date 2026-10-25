# Phiếu 016 · Gom ảnh cần dựng 3D vào một thư mục để chủ dự án đưa lên Tripo

**Bối cảnh:** chủ dự án muốn mọi ảnh 2D cần dựng 3D của **Rồng Giữ Ải, Lời Gọi, Tuyến Cuối** nằm chung một thư mục, **nhóm theo face limit**, để đưa lên Tripo3D. **Không gồm Tu Tiên.**

Phiếu có thể chạy nhiều lần: lần sau chỉ thêm model mới và cập nhật mục lục.

**Nguồn danh sách:** `docs/games/3D_REQUESTS.md`, mục §3 (bảng theo face limit và cách rig). Ảnh lấy từ `art-src/` của từng game, **ảnh gốc**, không dùng `*.tripo.png` của phiếu 012 (chưa qua phản biện).

**Thư mục đích (ngoài repo, để media không bao giờ vào Git):** `D:\tripo-upload\`.

```text
D:\tripo-upload\
  INDEX.md                      mục lục tiếng Việt: bảng mọi model, tổng credit rig, thứ tự nên làm
  face-02000\  face-04000\  face-06000\  face-08000\  face-10000\  face-20000\ …   (theo số trong bảng)
    _sheet.jpg                  ảnh xem nhanh cả nhóm, có nhãn
    <game>__<id>\               ví dụ dragon-hold__E01, typing-defense__barracks
      front.png  back.png  left.png    đúng ô Multiview của Tripo; một ảnh thì image.png
      tripo.txt                 hướng dẫn cho model này
```

## `tripo.txt` mỗi model ghi

- **Chế độ:** Multiview to 3D, hoặc Image to 3D; ảnh nào vào ô nào.
- **Face limit.**
- **Rig:**
  - `Tripo Biped, 20 credit`, kèm clip preset cần chọn;
  - hoặc `KHÔNG bấm rig, tải GLB không xương, Claude rig trong Blender`;
  - hoặc `Không rig`.
- **Thiết lập chung:** theo §2 của `3D_REQUESTS.md` (tách nền bật, texture HD, PBR, lưới tam giác, Smart Low Poly tắt).
- **Sau khi tải GLB:** đặt tên đúng `<id>.glb` và chép về đường dẫn ở cột GLB đích của `3D_REQUESTS.md`.
- **Lưu ý về ảnh** nếu README giao nhận ghi lỗi chưa sửa.

## Việc

1. Đọc §3 của `3D_REQUESTS.md`; lấy mọi dòng của 3 game có trạng thái "có ảnh".
2. Chép ảnh (không di chuyển, không sửa) vào đúng nhóm face; viết `tripo.txt`.
3. **Thiếu ảnh** thì không tạo thư mục model; ghi vào `INDEX.md` mục "Chờ ảnh".
4. Làm `_sheet.jpg` mỗi nhóm bằng ImageMagick trong WSL (`~/.local/bin/magick montage`, font `/mnt/c/Windows/Fonts/arial.ttf`).
5. **`INDEX.md`:**
   - bảng model theo nhóm face: game, id, tên Việt, chế độ, rig, credit;
   - tổng số model, tổng credit rig;
   - thứ tự nên làm: Rồng Giữ Ải trước, rồi Lời Gọi bậc P, Tuyến Cuối, Lời Gọi bậc VS;
   - mục "Chờ ảnh".
6. Báo cuối: số model đã gom theo từng nhóm face, đường dẫn `INDEX.md`.

Không chạy git. Không ghi vào repo, trừ khi phát hiện dòng `3D_REQUESTS.md` sai đường dẫn ảnh. Khi đó chỉ sửa đúng dòng ấy và ghi lại.

**Xong khi:** `D:\tripo-upload\INDEX.md` và các nhóm face đã có, mọi model "có ảnh" của 3 game đều nằm trong đó.
