# Phiếu 433b: Kim mưa kiếm — sửa cho giống phân cảnh


Phản biện: PASS (Sonnet, 17/11)
**Owner miễn luật hạn mức (nguyên văn):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau"; "cho codex làm việc đi, nó vẫn còn kìa".

## Bối cảnh
Chụp bản 433 (`typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-rain-r1.jpg`), so phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` (nửa trái): 4/10. Lỗi: trận pháp trên trời mờ, nhạt; kiếm quá nhỏ, gần như không thấy từ góc trên; lúc 1,2 s kiếm đã cắm hết, không thấy kiếm đang rơi, không có vệt sáng; thiếu tia lửa và vết nứt khi cắm; bụi vàng yếu. Console báo không nạp được atlas `metal-slash-arc` và `metal-crescent-sym`.

## Việc (chỉ `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts` và chỗ nối trong `metal-ult-layered.ts`)
1. Trận pháp: đường kính 10–14 m, cao 9–12 m, độ sáng đỉnh mỗi kênh 0,8–0,9 với lõi vàng, hiện trong 0,3 s và giữ tới khi mưa xong; thêm các tia sáng rủ xuống từ trận (thẻ dọc mảnh có sẵn hoặc ribbon) như phân cảnh khung 1.
2. Kiếm: cao 2,2–3,5 m (gấp ~3 lần hiện tại); thanh lớn cuối cao 8–10 m. Rơi trong 0,35–0,6 s mỗi thanh, so le để luôn có kiếm đang rơi trong suốt 0,6–2,4 s; mỗi thanh có vệt sáng vàng phía sau dài 3–6 m mờ dần.
3. Cắm đất: mỗi thanh lóe `metal-impact-v2`, thêm decal vết nứt nhỏ (dùng `art-src/lab/vfx/metal/metal-ground-mark.*` có sẵn; không vẽ bằng code) mờ trong 1,5 s; kiếm lớn có vết nứt lớn và `metal-big-burst-v2`.
4. Dư âm: bụi vàng rõ hơn (nhiều hạt hơn, sáng hơn, mỗi kênh ≤ 0,9).
5. Sửa hoặc bỏ tham chiếu tới 2 atlas không tồn tại.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; probe CPU in: cỡ kiếm, số kiếm đang rơi ở mỗi mốc 0,8/1,2/1,6/2,0 s (≥ 4), thời điểm kiếm lớn, mọi thứ trả về pool sau 4 s, 0 lỗi nạp atlas.
- Để lệnh chụp cho Claude như 433. p95 `stress.html` ≤ 16,7 ms.
- Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/433b-report.md`.
