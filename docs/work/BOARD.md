# BOARD · Tu Tiên (cập nhật 05/11/2026, 00:35)

Luật: tối đa 3 việc đang làm. Mỗi việc kết thúc bằng bản chơi (hoặc bước lab anh đã duyệt) cùng video trước/sau. Cách dùng: `README.md`.

## Đang làm (tối đa 3)
| Việc | Trạng thái | Kế tiếp | File |
|---|---|---|---|
| Bỏ lửa gai nhọn (nhát chém kết phím 7, Hỏa) | Phiếu 275 sẵn | Codex sau 274b → Claude kiểm bằng script → video cho anh | `tasks/flame-slash.md` |
| Lửa phím 1 có mặt nạ vào lab | 273/273b anh duyệt; 274b (than đỏ) chạy lúc 00:54 | Claude gộp 274 → tạo worktree 264 → Codex 264 → video | `tasks/key1-fire.md` |
| Vòng ngọc Clear Wind | 259 chưa đạt (Kim phẳng, xám) | Codex 259b → Claude chỉnh tham số trong lab → tấm so | `tasks/jade-ring.md` |

## Hàng chờ Codex (nối tự động)
274b (00:54) → 275 → 264 (khi có `docs/codex-queue/264/READY`) → 259b

## Phụ, đang chạy
- Rà hình vẽ bằng mã: agent nhỏ → `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md` → các phiếu ngắn (`tasks/code-drawn-audit.md`).
- Video Song Long toàn sân (làn 2) → gửi anh (`tasks/twin-dragons.md`).

## Chờ anh
- Cân bằng Song Long: bot Chuẩn chỉ thắng 15 % (phiếu 272). Claude sẽ đề xuất sau 3 việc chính (`tasks/twin-dragons.md`).

## Đỗ lại (sau 3 việc chính)
- Đầu rồng A (thêm chân trước thứ hai), bốn góc nhìn, Tripo.
- Sửa cut-in (phiếu 268): đòn đầu ≤ 50 ms, cut-in khoảng 1 s.
- Âm: lớp gộp tiếng trúng hàng loạt, giới hạn số tiếng; cắt đoạn dâng của k5 từ stem; tiếng hô hạ các âm khác.
- Mặt nạ vẽ A5, A6, A8–A10; vết cháy Hỏa.

## Xong hôm nay (04/11, đã gộp vào `main` của game)
- 258/258b FlipbookPool v2 + công cụ đo GPU (`ceb51c2`).
- Mặt C3 bản nâng nét (`be7cfa0`, `2381c7b`).
- 271/271b/271c Song Long toàn sân, sau cờ (`35f1b77`).
- 269 âm theo bậc to + vang chung (`5de0d22`).
- 272 bot đo Song Long (số ở `tasks/twin-dragons.md`).
- 273/273b mặt nạ lửa phím 1 (anh duyệt).
