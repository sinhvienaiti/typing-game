# Phiếu 034 · Tài liệu · Cập nhật cột trạng thái của `docs/games/3D_REQUESTS.md` (chỉ tài liệu)

**Bối cảnh:** `docs/games/3D_REQUESTS.md` §3 liệt kê 143 model của Rồng Giữ Ải, Lời Gọi và Tuyến Cuối. Cột cuối là "Trạng thái ảnh 2D", và cột này đã cũ:
- 128 dòng vẫn ghi "chờ ảnh", dù đa số đã có ảnh, đã nằm trong thư mục gửi Tripo đợt 2, hoặc đã có GLB.
- Ngày 27/10 Claude đếm được:
  - Rồng: 24 model đã có GLB;
  - Lời Gọi: 31 model đã có GLB, 86 model nằm trong `typing-game-handoff-2026-10-25/tripo-upload-dot2` (chủ dự án đang dựng trên Tripo);
  - Tuyến Cuối: 1 model đã có GLB, 1 model dùng chung (`rainbow-scout` dùng model của `rainbow-tank`, chủ dự án chốt 26/10).

**Thư mục làm việc:** repo cha (`.`).

**Chỉ được ghi:**
- `docs/games/3D_REQUESTS.md`: chỉ ô cột cuối của các dòng bảng §3, và một đoạn trạng thái ngắn đầu §1;
- `docs/codex-queue/034-report.md`.

**Cấm:**
- sửa cột khác, thứ tự dòng, số dòng;
- ghi vào `games/**`, `typing-game-handoff-2026-10-25/**`, media;
- lệnh git có ghi;
- mạng;
- dev server;
- đụng Tu Tiên (mục §6 của tài liệu giữ nguyên).

## Nguồn sự thật (chỉ đọc)

1. **Có GLB:** file ở cột "Nơi lưu GLB gốc" của dòng có trên đĩa. Đối chiếu thêm với sổ model `tools/map-factory/registry/out/assets.<game>.json` (các mục `source: "original"`).
2. **Trong đợt gửi Tripo 2:** tên `loigoi_<id>` có trong các thư mục `face …` của `typing-game-handoff-2026-10-25/tripo-upload-dot2/` (kể cả đuôi `.alpha`, `.flat`, `_front`, `_back`, `_left`). Ảnh trong `_cu-khong-gui/` không tính.
3. **Có ảnh 2D:** file ảnh ở cột "Ô ảnh Tripo · đường dẫn ảnh 2D" có trên đĩa.

## Việc

1. Viết một lệnh `node` nhỏ, chạy tại chỗ, không lưu vào repo. Lệnh đọc từng dòng bảng §3 và tính trạng thái mới theo thứ tự ưu tiên:
   - có GLB → `có GLB`;
   - ngược lại, có trong `tripo-upload-dot2` → `có ảnh · đợt 2 Tripo (chủ dự án đang dựng)`;
   - ngược lại, có ảnh trên đĩa → `có ảnh`;
   - còn lại → `chờ ảnh`.

   Riêng dòng `rainbow-scout`: `dùng chung model rainbow-tank (chủ dự án 26/10)`.
2. Thay **chỉ ô cuối** của mỗi dòng. Ô cũ có ghi chú quan trọng (ví dụ "015: …") thì giữ ghi chú sau dấu ` · `, rút gọn nếu dài.
3. Đầu §1 thêm một đoạn "Trạng thái 28/10/2026", 3–5 dòng: số model theo từng trạng thái của từng game, và đường dẫn sổ model 025.

## Kiểm (bắt buộc)

1. Chạy lại lệnh ở việc 1 sau khi sửa: mọi ô cuối khớp trạng thái tính được. In số dòng lệch, phải bằng 0.
2. Bảng đếm in ra: tổng 143. Rồng: 24 `có GLB`. Lời Gọi: 31 `có GLB`, 86 trong đợt 2. Tuyến Cuối: 1 `có GLB`, 1 dùng chung. Lệch thì ghi lý do từng dòng, không sửa cho khớp.
3. `git diff --word-diff -- docs/games/3D_REQUESTS.md`: chỉ ô cuối của dòng bảng và đoạn mới ở §1 đổi. Một lệnh `node` so từng dòng cũ với dòng mới: mọi ô trừ ô cuối giống hệt. In số dòng vi phạm, phải bằng 0.
4. `git status --short`: so với lúc bắt đầu, chỉ có **thêm** `docs/games/3D_REQUESTS.md` và `docs/codex-queue/034-report.md`.

## Báo cáo `docs/codex-queue/034-report.md`

- Bảng đếm trước và sau, theo game và trạng thái.
- Danh sách dòng có ghi chú cũ được giữ.
- Kết quả bốn lệnh kiểm.

**Xong khi:** bốn kiểm đạt.
