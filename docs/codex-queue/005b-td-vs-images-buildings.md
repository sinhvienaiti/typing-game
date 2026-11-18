# Phiếu 005b · Lời Gọi · ảnh 2D bậc VS, công trình và prop (để dựng 3D sau)

**Mục tiêu:** tạo ảnh 2D nguồn cho phần **công trình và prop** của bậc VS (khoảng 70 món). Chủ dự án sẽ dựng 3D từ các ảnh này trong Tripo sau.

**Thư mục làm việc:** `games/typing-defense`. Chỉ ghi vào `games/typing-defense/art-src/` (media, gitignored).

## Nguồn

- **Danh sách và đường dẫn đích:** `../../docs/games/3D_REQUESTS.md`, các dòng Lời Gọi · VS công trình/prop ở trạng thái "chờ ảnh".
- **Prompt pack:**
  - `../space-typing/docs/art-requests/td/02-tripo-buildings-props-vs.md`;
  - file chính `02-tripo-buildings-props.md` cùng thư mục.
  - Mỗi khối ```text là một ảnh, dán nguyên văn.

## Cách làm

- Ảnh đã có thì bỏ qua.
- Mỗi ảnh kèm `<tên>.prompt.txt`.
- Tự kiểm theo bảng kiểm của file chính. Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
- **Giới hạn mỗi lần chạy: 45 ảnh.** Còn thừa thì ghi danh sách còn lại vào README để chạy tiếp.
- Viết `art-src/README-vs-buildings.md`: bảng ảnh, nhận xét từng ảnh, việc chủ dự án cần xem.

**Không được đụng:** file ngoài `games/typing-defense/art-src/`. Không chạy git.

**Xong khi:** mọi món công trình và prop VS "chờ ảnh" đã có ảnh, hoặc nằm trong danh sách còn lại có ghi lý do.
