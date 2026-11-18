# Vòng 4 · Bước 2 · Cột Lôi: số sát thương không che quái bị đánh (sau `tp2=1`)

Giám khảo vòng 3: số "101" của từng quái nằm đè lên đúng các quái vừa bị đánh trong 1,10–1,67 s, nên không đọc được quái nhận đòn (`docs/work/consult/r3-step1b-panel.md`). Phản ứng thân quái của R3-1 có chạy (đến 20°) nhưng bị che. Luật: `path-to-8.md` §7.

## Nguồn
- Số sát thương: `src/view/hitfx.ts` (`DamageNumbers`, `IcNumberSprites`, `DrawnNumberField`); chỗ lab tạo số cho mỗi đòn nằm trong `src/lab/skills-main.ts` (tìm nơi gọi hệ số khi có sự kiện `impact`). Số tổng ("418×4") là dòng tiêu đề ở trên; giữ nguyên.

## Việc (chỉ điểm này)
- Với Cột Lôi khi `tp2=1`: số của từng quái **bật ra khỏi thân**:
  - xuất hiện trên đầu quái rồi trôi lên và **lệch ra xa tâm giáng** (theo hướng đòn trên màn hình), sao cho trong 1,03–1,70 s không đè lên thân quái nào bị đánh;
  - giữ cỡ chữ, màu và thời lượng hiện có; chỉ đổi điểm đặt và đường đi;
  - số của nhiều quái gần nhau không chồng lên nhau (dãn theo thứ tự trúng).
- `tp2` tắt hoặc chiêu khác: số y như cũ.

## Ngân sách (§7)
- Thêm ≤ 1,0 ms p95; không thêm draw call; không cấp phát mỗi khung. Mã khoảng ≤ 120 dòng không tính test.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:** `src/view/hitfx.ts` (chỉ phần đặt vị trí, có cờ), chỗ nối trong `src/lab/skills-main.ts`, test trong `tests/`, báo cáo `docs/codex-queue/laneL1-report.md`.
- **Không:** sửa media hay manifest; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Đạt khi
- Test node: với Cột Lôi + `tp2`, hộp chữ của mỗi số không giao hộp màn hình của bất kỳ quái bị đánh nào trong 1,03–1,70 s (dùng phép chiếu camera chơi của lab); `tp2` tắt thì vị trí số như cũ; không cấp phát mỗi khung.
- `npx --no-install tsc --noEmit` sạch; chạy riêng các file test liên quan. Claude chạy toàn bộ vitest.
- Báo cáo ≤ 6 dòng.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
