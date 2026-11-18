# Phiếu 383b · Tu Tiên · Map 1: vẽ lại 6 ô đất (giữ 8 decal)

Ô đất phiếu 383 đạt kỹ thuật (lặp liền, alpha sạch) nhưng "sạch nhưng thường": đá lát hành lang quá sáng trắng như xi măng mới; ô rêu lộ mẫu lặp đều; tổng thể nhạt, thiếu chiều sâu so với tranh map. Anh (15/11): cứ làm theo đề xuất của điều phối. Giữ nguyên 8 decal của 383.

Lô: 6 ảnh
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-13/tu-tien/codex-images/ground-383-sheet.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/383b-report.md` (Codex tự viết).

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/ground/thanh-thach/<tên>.v2.png` cho sáu ô (`lane-paving`, `court-paving`, `court-cracked`, `moss-patch`, `formation-worn`, `rubble-edge`), một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `A/ground/thanh-thach/ground-383b-sheet.jpg`. Giữ nguyên bản 383. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
Bản 383 trong `A/ground/thanh-thach/` (giữ bố cục phiến, sửa chất); tranh map `A/concept/map1-camera.v1-try6.png`, `A/concept/map1-camera.v1-try7.png` (màu và chất đá cổ); `A/lab/lookdev/PavingStones128/Color.jpg`, `A/lab/lookdev/Rock035/Color.jpg`, `A/lab/lookdev/Moss001/Color.jpg`.

## Ba sửa (1024×1024, nhìn thẳng từ trên, lặp liền bốn cạnh, ánh sáng phẳng)
1. **Hành lang tối và cũ hơn:** `lane-paving` cùng tông xám xanh với `court-paving.v2`, độ sáng trung bình (luma) chỉ cao hơn `court-paving.v2` khoảng 8–18 % (không trắng), mặt đá mòn bóng ở giữa, mép phiến sứt, vết thời gian.
2. **Rêu ngẫu nhiên:** `moss-patch` mảng rêu to nhỏ khác nhau, mọc theo khe và góc phiến, không lặp hình; xếp 3×3 không thấy mẫu lặp.
3. **Chiều sâu và chất cổ cho cả sáu ô:** biến thiên màu từng phiến (xám xanh, xám ấm, vài phiến sẫm), vết mòn, đốm phong hoá, khe sâu tối hơn, mép vỡ; vẫn vừa tương phản để không lấn quái và hiệu ứng. Không chữ, không màu tín hiệu.

## Kiểm và tự chấm
Script: lặp liền bốn cạnh, xếp 3×3; tỉ lệ luma trung bình `lane-paving.v2` / `court-paving.v2` trong 1,08–1,18 (luma = 0,2126 R + 0,7152 G + 0,0722 B trên toàn ảnh). Tấm ghép: 383 | 383b từng ô, mỗi ô 3×3, và một ô phối thử (hành lang + nền + vài decal 383) ở cỡ camera chơi. Tự chấm theo mặt yếu nhất (chất cổ, không lộ lặp, hợp tranh map, không lấn quái); dưới 8 vẽ lại. Báo cáo ≤ 150 chữ.

Phản biện: PASS (Sonnet, 15/11; sửa mốc đo độ sáng)
