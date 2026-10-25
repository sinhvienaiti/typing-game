# Phiếu 015 · Làm đủ ảnh 2D cho Rồng Giữ Ải, Lời Gọi, Tuyến Cuối

**Bối cảnh:** chủ dự án muốn hình ảnh 2D của các game ngoài Tu Tiên **đầy đủ**, để hoàn thành các game này. Tu Tiên do session khác lo: **không đụng** `games/immortality-cultivation` và `docs/games/tu-tien`.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `docs/games/IMAGE_AUDIT_2026-10-25.md` (mới);
- bộ prompt của từng game:
  - `docs/games/dragon-lane/art-requests/`;
  - `games/typing-defense/docs/art-requests/td/`;
  - thư mục yêu cầu ảnh của Tuyến Cuối, nếu chưa có thì tạo `games/typing-survival/docs/art-requests/`;
- `art-src/` của 3 game (ảnh, prompt `.prompt.txt`, README giao nhận);
- mục bảng 3D của 3 game trong `docs/games/3D_REQUESTS.md`.

Không chạy git, không sửa mã. Không ghi đè ảnh có sẵn: bản cũ đổi tên thành `.v1.png`.

## Việc

1. **Kiểm kê** (viết `IMAGE_AUDIT_2026-10-25.md`, tiếng Việt). Với từng game, đọc tài liệu thiết kế và bộ prompt:
   - **Rồng Giữ Ải:** `docs/games/dragon-lane/` (canon, DESIGN §9 các mốc, `art-requests/`). Mốc hiện tại M0, kế tiếp M0b.
   - **Lời Gọi:** `games/typing-defense/docs/` (`td/BUILD_1B.md`, `art-requests/td/`). Bậc P và VS; phiếu 005a, 005b đang lo VS.
   - **Tuyến Cuối:** `games/typing-survival/docs/` (`BUILD_S1.md`, S1/S2). Dùng chung model Space.

   Lập bảng mọi ảnh 2D game cần ở mốc hiện tại và mốc kế:
   - nhân vật, quái, công trình, prop;
   - ảnh nguồn cho 3D;
   - đất, decal, phông;
   - VFX, icon, UI, màn tựa.

   Mỗi dòng ghi: **đã có** (đường dẫn), **thiếu**, hay **có nhưng lỗi** (theo các README giao nhận cũ). Cuối file: tổng thiếu theo game.
2. **Tạo ảnh còn thiếu** bằng `image_gen`, theo phong cách và quy ước của bộ prompt từng game.
   - Ảnh nguồn cho 3D: nền `#E6E6E6`, tư thế A với người, đúng góc như bộ cũ.
   - Mỗi ảnh có `<tên>.prompt.txt`. Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
   - **Thứ tự ưu tiên:** ảnh nguồn 3D còn thiếu → ảnh có lỗi đã ghi (ví dụ E01-S góc cánh của Rồng: thử thêm 1 lần) → ảnh 2D dùng trực tiếp trong game.
   - **Bỏ qua** phần bậc VS của Lời Gọi mà 005a, 005b đang làm hoặc đã làm. Đọc `.local/codex-runs/005*/last.md` và thư mục ảnh để biết.
   - **Tối đa 45 ảnh mỗi lần chạy.** Còn thiếu thì ghi danh sách vào cuối `IMAGE_AUDIT` dưới mục "Còn lại cho phiếu 015b".
3. **Cập nhật `3D_REQUESTS.md`** cho ảnh nguồn 3D mới: face limit, cách rig, clip, theo luật rig ở §1.1 của file đó.
4. **README giao nhận** trong `art-src/` mỗi game có ảnh mới: bảng ảnh, lượt sinh, đạt hay chưa. Kèm ảnh xem nhanh `art-src/_review/015-*.jpg` (ImageMagick trong WSL: `~/.local/bin/magick`, font `/mnt/c/Windows/Fonts/arial.ttf`).

**Không dùng `tools/art-normalize`**: phiếu 012 chưa qua phản biện.

**Xong khi:**
- bản kiểm kê đầy đủ 3 game;
- ảnh thiếu đã tạo (tối đa 45) hoặc đã ghi vào danh sách còn lại;
- `3D_REQUESTS` và README đã cập nhật.
