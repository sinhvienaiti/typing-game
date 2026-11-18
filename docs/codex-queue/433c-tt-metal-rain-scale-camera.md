# Phiếu 433c: Kim mưa kiếm — phóng to cho camera chơi và thêm nhịp camera đẩy vào


Phản biện: PASS (Sonnet, 17/11)
**Owner miễn luật hạn mức (nguyên văn):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau"; "cho codex làm việc đi, nó vẫn còn kìa".

## Bối cảnh
Bản 433b (`typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-rain-r2.jpg`) ~5/10 so phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` (nửa trái): camera chơi xa hơn phân cảnh nhiều nên kiếm nhỏ, trận pháp bị đẩy lên mép trên và khuất sau thẻ tên chiêu, vết nứt và vệt sáng gần như không thấy. Owner 17/11 đồng ý làm cả hai: "đồng ý, triển khai cho tôi đi".

## Việc (worktree `games/.wt-ic-lab-all`)
1. **Phóng to trong `src/lab/metal-ult-rain.ts`:** kiếm cao 5–6 m (kiếm lớn 14–18 m); trận pháp đặt cao 6–8 m và đường kính 14–18 m, tâm đặt sao cho toàn bộ trận nằm trong khung hình camera chơi (cách mép trên ≥ 12 % chiều cao màn hình, không chồng lên thẻ tên chiêu); vệt sáng dày gấp đôi và dài 5–8 m; vết nứt `metal-ground-mark` to gấp 2–3 lần.
2. **Nhịp camera đẩy vào (file mới `src/lab/ult-camera-punch.ts`, gọi từ `metal-ult-layered.ts`):** khi phát chiêu, camera chơi trượt mượt (ease in/out) về phía tâm trận, giảm khoảng cách còn 55–65 %, hạ góc nhìn 5–8°, giữ suốt đoạn mưa kiếm và kiếm lớn (0,5–2,6 s), rồi trả về vị trí cũ trong 0,6 s. Không giật, không xuyên qua mặt đất, người chơi luôn trong khung. Có thể tắt bằng `?ultCam=0`. Viết dạng dùng chung được cho các tuyệt kỹ khác (tham số: tâm, tỉ lệ khoảng cách, góc, thời lượng).
3. Không đổi luật sát thương, số, âm thanh.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; probe in: cỡ kiếm, độ cao và đường kính trận, toạ độ màn hình của trận (mép trên ≥ 12 % khung, không giao thẻ tên chiêu) ở camera chơi 1280×720; đường cong camera (khoảng cách, góc) theo thời gian; camera về đúng vị trí ban đầu sai số < 1 cm; `?ultCam=0` giữ camera cố định.
- p95 `stress.html` 100 quái ≤ 16,7 ms; để lệnh chụp cho Claude (góc chơi ở 0,4/1,2/2,4/3,2 s).
- Chỉ sửa `src/lab/metal-ult-*` và file mới `src/lab/ult-camera-punch.ts`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/433c-report.md`.
