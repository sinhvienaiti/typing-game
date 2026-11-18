# Phiếu 047 · Tài liệu · Cột trạng thái `3D_REQUESTS.md` sau khi nhập Tripo đợt 2 (chỉ tài liệu)

**Bối cảnh:** phiếu 034 đã cập nhật cột cuối "Trạng thái ảnh 2D" của `docs/games/3D_REQUESTS.md` §3. Khi đó 86 dòng Lời Gọi ghi `có ảnh · đợt 2 Tripo (chủ dự án đang dựng)`. Ngày 28/10 Claude đã nhập đợt 2 ([`docs/games/3D_IMPORT_2026-10-28.md`](../games/3D_IMPORT_2026-10-28.md)):
- 85 model đã có GLB trong `games/typing-defense/art-src/3d/`;
- còn thiếu đúng một model, `loigoi_cannon-kit-l2`.

Phiếu này đưa cột cuối và đoạn trạng thái ở §1 về đúng hiện trạng. Cách làm giống phiếu 034 (`docs/codex-queue/034-3d-requests-status.md` và `034-report.md`).

**Thư mục làm việc:** repo cha (`.`).

**Chỉ được ghi:**
- `docs/games/3D_REQUESTS.md`: chỉ ô cột cuối của các dòng bảng §3, và đoạn "Trạng thái 28/10/2026" đầu §1;
- `docs/codex-queue/047-report.md`.

**Cấm:**
- sửa cột khác, thứ tự dòng, số dòng;
- ghi vào `games/**`, `typing-game-handoff-2026-10-25/**`, media;
- lệnh git có ghi;
- mạng; dev server;
- đụng Tu Tiên (mục §6 giữ nguyên).

## Nguồn sự thật (chỉ đọc)

1. **Có GLB:** file ở cột "Nơi lưu GLB gốc" của dòng có trên đĩa.
2. **Điểm và mức của đợt 2:** bảng "Bảng ghép và chấm" trong `docs/games/3D_IMPORT_2026-10-28.md`, cột "Mã model", "Đích", "Điểm", "Mức". Ghép theo mã model (`loigoi_<id>`) và theo đích, hai cách phải ra cùng một dòng.
3. **Thiếu GLB:** mục "Model không đạt" của cùng tài liệu.

## Việc

1. Viết một lệnh `node` nhỏ, chạy tại chỗ, không lưu vào repo. Lệnh đọc từng dòng bảng §3 và tính trạng thái mới:
   - dòng nằm trong bảng nhập đợt 2 và có GLB → `có GLB · Tripo đợt 2 (28/10), <Điểm> <Mức>`, ví dụ `có GLB · Tripo đợt 2 (28/10), 8,5 Tạm chấp nhận`. Điểm giữ dấu phẩy thập phân như trong bảng; bỏ phần ngoặc "(7 và 8)".
   - `loigoi_cannon-kit-l2` → `có ảnh · đợt 2 Tripo: thiếu GLB, chủ dự án dựng lại`.
   - các dòng khác giữ nguyên ô cuối hiện có.
2. Thay **chỉ ô cuối**. Ô cũ có ghi chú sau dấu ` · ` mà không phải chữ "đợt 2 Tripo (chủ dự án đang dựng)" thì giữ ghi chú đó ở cuối.
3. Sửa đoạn "Trạng thái 28/10/2026" đầu §1:
   - đếm lại theo từng game;
   - thêm một dòng trỏ tới `3D_IMPORT_2026-10-28.md`, kèm số Đạt và Tạm chấp nhận.

## Kiểm (bắt buộc)

1. Chạy lại lệnh ở việc 1 sau khi sửa. Mọi ô cuối phải khớp trạng thái tính được. In số dòng lệch; con số phải bằng 0.
2. **Bảng đếm:**
   - tổng 143;
   - Rồng: 24 `có GLB`;
   - Lời Gọi: 116 `có GLB` (31 cũ và 85 đợt 2) và 1 thiếu GLB (`cannon-kit-l2`);
   - Tuyến Cuối: 1 `có GLB` và 1 dùng chung.

   Đếm thêm 85 dòng đợt 2 theo mức: phải ra 44 Đạt và 41 Tạm chấp nhận như tài liệu nhập. Lệch thì ghi lý do từng dòng, không sửa cho khớp.
3. Một lệnh `node` so từng dòng cũ với dòng mới: mọi ô trừ ô cuối giống hệt. In số dòng vi phạm; con số phải bằng 0. `git diff --word-diff` chỉ được đổi ở ô cuối và đoạn §1.
4. `git status --short`: so với lúc bắt đầu, chỉ có **thêm** `docs/games/3D_REQUESTS.md` và `docs/codex-queue/047-report.md`.

## Báo cáo `docs/codex-queue/047-report.md`

- Bảng đếm trước và sau, theo game và trạng thái.
- Danh sách dòng có ghi chú cũ được giữ.
- Kết quả bốn lệnh kiểm.

**Xong khi:** bốn kiểm đạt.
