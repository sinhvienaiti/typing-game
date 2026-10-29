# Phiếu 186 · Dragonhold · Ô đất v3 theo bible: thông, ô liu, hoa cương (6 ô)

**Vì sao:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md` §3.3, §3.5) bỏ màu cỏ sân bóng tươi; đất phải ngả xanh thông và ô liu, có mảng vàng nắng. Các ô `pine-river` hiện dùng (phiếu 093) vẽ theo kiểu cũ; làn map phải kéo màu bằng shader. Chủ dự án 29/10: giao thêm việc cho Codex.

**Báo cáo:** `docs/codex-queue/186-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5.

## Luật chung

Như phiếu 155 (`docs/codex-queue/155-dh-road-art.md`, đọc trước): khối STYLE, MAP, TOP nguyên văn; ô 1024 × 1024 liền mép bốn phía; kiểm liền mép bằng dịch 50 %; luật màu tín hiệu; KA1 md5; M ≥ 8 và Q ≥ 8; cấm git có ghi, cấm sửa mã, cấm Tu Tiên.

**Nơi ghi:** `games/dragon-hold/art-src/ground-v3/meadow/` (mới), `_review/186*`, báo cáo.

## Sáu ô

| Tên | Nội dung (viết prompt tiếng Anh từ mô tả này) |
|---|---|
| `grass-pine` | cỏ núi xanh thông sẫm, ngắn, dày, vài lá thông rụng |
| `grass-olive` | cỏ ô liu xen mảng vàng nắng nhạt, khô hơn |
| `forest-floor` | sàn rừng thông: lá kim nâu, rêu sẫm, vài nón thông |
| `earth-dark` | đất núi sẫm, sỏi nhỏ, vệt nước mưa |
| `granite-moss` | đá hoa cương kem phẳng lấm rêu, nứt nhẹ |
| `river-bank` | bờ sông: sỏi tròn ướt, cát xám, rêu ở mép |

**Kiểm (ghi số):** liền mép; luma trung bình: `grass-pine` < `grass-olive` < `earth-dark`? (ghi cả sáu); hue cỏ trung vị 80–150°, bão hòa ≤ 0,55 (luật §3.3); tỉ lệ px tín hiệu (S > 0,6, V > 0,7, hue 0–60° hay 160–200°) ≤ 2 %; tờ thử `_review/186-mock.jpg` 2048 × 1152 ghép sáu ô thành một sườn thung có đường (dùng `road-flagstone` của 155 nếu có); KA5.

**Xong khi:** sáu ô có bản chọn, qua mục kiểm, tự chấm M ≥ 8 và Q ≥ 8.
