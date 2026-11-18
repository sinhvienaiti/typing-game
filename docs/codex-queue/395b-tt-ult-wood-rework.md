# Phiếu 395b: Làm lại tuyệt kỹ Mộc cho giống ảnh đích


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Agent Claude chụp bản 395 (16/11), so với ảnh đích `games/immortality-cultivation/art-src/concept/ult-wood/ult-wood-moment-b.v1-try1.png`: **trượt**. Ảnh so sánh: `typing-game-review/owner-review/2026-11-16/tu-tien/ult-wood/395-top-reference.jpg`, `395-behind-phases.jpg`.
- Góc trên: rễ nhỏ, rải lấm tấm; không có vòng tường rễ dày ở vành, không có mầm sáng ở tâm.
- Góc sau lưng: một thẻ lá rất to che người tung chiêu lúc trói và lúc vỡ.
Chạy sau phiếu 397 trong cùng làn (đọc lại `skills-main.ts`, giữ phần nối của 397).

## Việc (worktree `games/.wt-ic-lab-all`, các file `src/lab/wood-ult-*`)
1. Bố cục theo ảnh đích: vòng rễ lớn, dày, cao, liền mạch quanh vành vùng 30 m (nhiều cụm chồng lấn, lớn gấp 2–4 lần hiện tại), vài nhánh rễ nối vào tâm; bên trong thưa hơn.
2. Mầm sáng ở tâm phải đọc rõ từ góc trên: lớn hơn, đặt đúng tâm vùng, là điểm nhấn HDR duy nhất.
3. Bỏ thẻ lá cỡ lớn che người tung chiêu: giới hạn cỡ thẻ gần camera, không thẻ nào che nhân vật hay quá 15 % khung.
4. Giữ trói không bọc thân, âm, lịch sự kiện, probe như 395.

## Nghiệm thu
- Kiểm kiểu, probe 100 quái như 395.
- Chụp lại góc trên và sau lưng **ở đúng khoảnh khắc trúng đòn** (0,6–0,84 s) và lúc trói, ghép cạnh ảnh đích, vào `typing-game-review/owner-review/2026-11-16/tu-tien/ult-wood/` (ghi đè bản 395, cập nhật `ABOUT.md`). Nếu sandbox chặn trình duyệt, để lệnh chụp cho Claude.
- Chỉ sửa `src/lab/wood-ult-*` và `art-src/lab/vfx/wood-ult/` trong worktree. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/395b-report.md`.
