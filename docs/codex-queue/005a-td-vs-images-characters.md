# Phiếu 005a · Lời Gọi · ảnh 2D bậc VS, nhân vật, quái và đồ cầm (để dựng 3D sau)

**Mục tiêu:** tạo ảnh 2D nguồn cho phần **nhân vật, đồng hành, lính, thợ, quái và đồ cầm** của bậc VS. Chủ dự án sẽ dựng 3D từ các ảnh này trong Tripo sau.

**Thư mục làm việc:** `games/typing-defense`. Chỉ ghi vào `games/typing-defense/art-src/` (media, gitignored).

## Nguồn

- **Danh sách và đường dẫn đích:** `../../docs/games/3D_REQUESTS.md`, các dòng Lời Gọi · VS ở trạng thái "chờ ảnh". Đường dẫn ở đây đã quy đổi về repo `games/typing-defense`. Nếu khác prompt pack, dùng đường dẫn của 3D_REQUESTS và ghi lại chỗ khác.
- **Prompt pack:**
  - `../space-typing/docs/art-requests/td/01-tripo-characters-enemies-vs.md` (bậc VS);
  - file chính `01-tripo-characters-enemies.md` cùng thư mục: cách làm §1, màu giữ riêng §3.7, kiểm ảnh §4.
  - Mỗi khối ```text là một ảnh, dán nguyên văn.
- **Nhiều góc:** góc phụ (`-side`, `-back`) đính kèm ảnh chính của chính món đó.
- **Đồ cầm** (búa, khiên, giáo…) là ảnh riêng, như prompt yêu cầu.

## Cách làm

- Ảnh đã có thì bỏ qua.
- Mỗi ảnh kèm `<tên>.prompt.txt`.
- Tự kiểm theo §4 của file chính. Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
- **Giới hạn mỗi lần chạy: 45 ảnh.** Còn thừa thì ghi danh sách còn lại vào README để lần sau làm tiếp.
- Viết `art-src/README-vs-characters.md`: bảng ảnh đã tạo, nhận xét từng ảnh, việc chủ dự án cần xem.

**Không được đụng:** file ngoài `games/typing-defense/art-src/`. Không chạy git.

**Xong khi:** mọi món nhân vật, quái và đồ cầm VS "chờ ảnh" đã có ảnh, hoặc nằm trong danh sách còn lại có ghi lý do.
