# Phiếu 439c — Quang: tia hội tụ ở giữa, tia quạt so le, bụi lấp lánh (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Bản 439b (`typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-b.jpg`): Claude ~5,5–6. Owner 17/11: "sửa tiếp, và cái đoạn kết, nó có 1 ánh sáng mạnh hơn, nhìn nó cứ lệch sao ấy, tự nhiên lại hướng về góc cuối, đáng lẽ nó nên ở giữa hoặc bỏ đi thì tôi nghĩ hợp lý hơn". Quyền, giới hạn, server 3148, cách đo (hình nêm, khung nền, probe `light-ult-glow-probe.mjs`, ngưỡng lõi/quầng) giữ nguyên như `docs/codex-queue/439b-tt-light-ult-glow.md` và `439-tt-light-ult-eyes-loop.md`. Chỉ sửa `src/lab/light-ult-*`.

## Việc (worktree `games/.wt-ic-lab-all`)
1. **Tia hội tụ ở giữa:** hướng tia hội tụ theo **trục giữa của quạt** (đường từ đỉnh quạt qua trung điểm hai mút tia ngoài), không chọn quái lệch một bên. Quạt thu dần từ hai bên vào trục giữa (0,3–0,4 s) rồi mới bắn tia hội tụ dọc trục; điểm trúng là quái gần trục nhất (lệch trục ≤ 5°), nếu không có thì điểm cuối tia trên trục ở tầm quạt. Ghi góc lệch trục vào báo cáo.
2. **Tia quạt so le:** 9–13 tia, độ dài ngẫu nhiên có hạt giống 65–100 % tầm (kiểm hệ số biến thiên ≥ 0,1 với hạt giống dùng), độ sáng 0,55–1,0, góc rải không đều (± 3° quanh lưới đều); 2–3 tia chính sáng hơn. Không còn kiểu răng lược đều.
3. **Bụi dư âm thành đốm lấp lánh** (riêng pha dư âm; 20–40 hạt dọc mỗi tia của 439b giữ nguyên): thay lớp phủ đều bằng cụm hạt: 40–70 đốm lấp lánh (nhấp nháy sao 4 cánh nhỏ từ `gold-dust-motes-loop-w2` hoặc sprite lấp lánh có sẵn trong `art-src/lab/vfx/light/`), dày hơn dọc các tia chính, có khoảng trống; tan trong 1–1,3 s.
4. **Thấu kính to hơn** 1,4–1,6 lần, viền vàng sáng nhẹ, đọc được ở camera chơi (bbox ≥ 18 px).

## Đo (bổ sung vào số đo của 439b)
- Góc lệch trục tia hội tụ ≤ 5° (in từ hook).
- Hệ số biến thiên độ dài tia ≥ 0,1; độ sáng đỉnh mỗi tia in ra.
- Độ phủ nêm ở 0,9 s ≥ 18 %; vùng trắng ≤ 6 %; lõi/quầng tia hội tụ như 439b.
Vòng lặp sửa → chụp → mở ảnh → so phân cảnh và nhận xét owner → sửa, tối đa 5 vòng.

## Nghiệm thu
Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms. Lưu `light-ult-codex-c.jpg/.mp4` mới trong `owner-review/2026-11-17/tu-tien/` (giữ file cũ), dòng `ABOUT.md`. Xoá khung thô của mình. Không commit.

## Giao nộp
`docs/codex-queue/439c-report.md`.
