# Phiếu 007 · Tu Tiên Thủ Ải · bộ prompt ảnh M0b và ảnh 2D nguồn để dựng 3D

**Mục tiêu:** có ảnh bản sắc và ảnh 2D nguồn của mọi nhân vật, thú và vật cần dựng 3D cho game. Chủ dự án sẽ dựng 3D trong Tripo sau.
- **Hướng hình:** 3D trước, có đo (canon D03, D36).
- Nhân vật, bot, Thú Vương và chiêu lớn là 3D thật. Bầy thú cũng là 3D nếu bench HN0 đạt.
- Mọi ảnh đều cần cho 3D.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/` (bộ prompt, Markdown, tiếng Việt kèm prompt tiếng Anh);
- `games/immortality-cultivation/art-src/` (ảnh, media, gitignored);
- mục "Tu Tiên Thủ Ải" trong `docs/games/3D_REQUESTS.md` (chỉ mục này).

Không sửa file nào khác. Không chạy git.

## Nguồn phải đọc

- `docs/games/tu-tien/00-canon.md`, đọc kỹ:
  - §0 định danh, giọng, đối tượng; §2 từ điển;
  - §8 trận pháp và sân (Trận Tâm, Trận Trụ, cơ quan);
  - §9 người chơi; §10 thú (5 họ, tinh anh, thú tướng, Thú Vương, §10.9 trình bày thú);
  - §11 ngũ hành; §12 trường phái Kiếm, Thổ thể, đan phù;
  - phần mỹ thuật, M0b và danh sách tài sản (tìm "M0b", "mỹ thuật", "GLB", "Tripo").
- `docs/games/tu-tien/DANH_GIA_2026-10-24.md`: bản sắc "sơn thủy huyền ảo chất Việt, không máu (vệt mực)".
- **Mẫu cách viết bộ prompt:** `docs/games/dragon-lane/art-requests/m0/README.md` và `01-creatures.md`.
  - Có khối "Instructions for the image tool".
  - Mỗi ảnh là một khối ```text đủ dòng chung, dán nguyên văn.
  - Có bảng mã, file, khổ, đính kèm.
  - Luật ảnh gửi Tripo: nền xám phẳng `#E6E6E6`, tư thế chữ A cho nhân vật hai chân, góc phụ đính kèm ảnh chính, không chữ, không bóng, không hiệu ứng.
- **Không chép** tên, giao diện, hình hay truyện của Quỷ Cốc Bát Hoang. Dùng tên của canon.

## Việc

1. **Viết bộ prompt** `docs/games/tu-tien/art-requests/m0b/`:
   - `README.md`: mục lục, thứ tự làm, thiết lập Tripo, bảng face limit và rig theo luật của `3D_REQUESTS.md` §1.1;
   - `00-identity.md`: 2 ảnh bản sắc (một cảnh ải lúc thú triều, một chân dung tu sĩ) để chủ dự án duyệt phong cách;
   - các file cho từng nhóm: người chơi và bot; 5 họ thú; tinh anh; thú tướng; Thú Vương; Trận Tâm, Trận Trụ, cơ quan; pháp bảo hoặc kiếm bay của chiêu "vạn kiếm".
   - Nhân vật hai chân có ảnh chính nhìn thẳng (tư thế A) và ảnh phụ nhìn sau. Thú bốn chân nhìn ngang, ảnh phụ nhìn thẳng.
2. **Tạo ảnh** bằng `image_gen`, đúng thứ tự trong README:
   - 2 ảnh bản sắc trước, rồi người chơi Kiếm tu (2 góc), rồi Thú Vương, thú tướng, 5 họ thú, rồi còn lại.
   - Lưu vào `games/immortality-cultivation/art-src/<nhóm>/<id>.png`, kèm `<id>.prompt.txt`.
   - Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
   - **Giới hạn lần chạy này: 40 ảnh.** Còn thừa thì ghi danh sách còn lại.
3. **Viết** `games/immortality-cultivation/art-src/README-m0b.md`: bảng ảnh, nhận xét từng ảnh, việc chủ dự án cần duyệt.
4. **Thay mục "chờ canon"** của Tu Tiên trong `docs/games/3D_REQUESTS.md` bằng bảng thật:
   - id, ô ảnh Multiview, đường dẫn, face limit, cách rig kèm lý do, clip cần có, nơi lưu GLB, trạng thái ảnh;
   - luật rig như §1.1 của file đó: Tripo 20 credit cho người hai chân chuẩn; tự rig Blender cho thú bốn chân có vồ, cắn, húc, cho Thú Vương và nhân vật chữ ký; không rig cho đồ tĩnh.

**Xong khi:** bộ prompt viết xong; tối đa 40 ảnh đã tạo, có nhận xét; mục Tu Tiên trong 3D_REQUESTS có bảng. Báo cáo cuối liệt kê đường dẫn và việc chủ dự án cần duyệt.
