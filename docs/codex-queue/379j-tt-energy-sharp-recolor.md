# Phiếu 379j · Tu Tiên · Cột hai tia gãy gắt: làm lại màu cho khớp bản dày

Anh (13/11 15:1x): "sao bạn không kêu codex tạo lại ảnh bản gãy gắt cho màu nó giống với 2 bản còn lại, chứ màu hiện tại nó đang không phù hợp". Bản gãy gắt `v5-try2` (Codex 379i) ra vàng cam đậm; bản điều phối chỉnh bằng giảm bão hoà thì xám xỉn. Cần **giữ nguyên hình của `v5-try2`** (đường gãy, độ dày, khe tối, chân, mây, tia phụ) và **đổi màu cho khớp `v4-try3`**.

**Model `gpt-6.1-sol`, mức `high`. Dùng công cụ `image_gen` ở chế độ sửa ảnh, tối đa 4 lần** (2 cho ảnh cột, 2 cho dải bốn khung), `view_image` tối đa 6. Báo cáo `docs/codex-queue/379j-report.md` (Codex tự viết).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-sharp.v2-try*.png`, `S/thunder-energy-sharp-frames.v2-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi ảnh gốc và ảnh màu tham chiếu), tấm ghép `S/thunder-energy-379j-sheet.jpg`. Giữ nguyên bản cũ. Cấm git ghi, sửa file có sẵn, mã.

## Ảnh
- Gốc để sửa (giữ hình): `S/thunder-energy-column.v5-try2.png`, `S/thunder-energy-column-frames.v5-try2.png`.
- Màu tham chiếu (khớp màu này): `S/thunder-energy-column.v4-try3.png` và `S/thunder-energy-column.v3-try4.png`.

## Màu đích
Lõi tia **trắng rực gần như thuần** (giống v4-try3), chuyển sang **quầng vàng nhạt ấm, trong** ở rìa, rồi mờ vào nền đen; tia phụ trắng ngà mảnh; không vàng đậm, không cam, không xám xỉn, không ngả xanh lục. Hình không đổi.

## Kiểm và tự chấm
Script: so màu với `v4-try3` trên vùng tia (điểm ảnh sáng > 50 %): độ bão hoà trung bình (HSL) trong ± 0,05 của v4-try3, sắc độ (hue) trung bình trong ± 8°; tỉ lệ điểm ảnh lõi gần trắng (> 90 % sáng, bão hoà < 0,15) ≥ 0,7 lần tỉ lệ đó ở v4-try3; làm y hệt phép so màu cho dải bốn khung mới với `S/thunder-energy-column-frames.v4-try3.png`; so hình với `v5-try2` (ảnh xám, sai khác trung bình nhỏ, đường gãy trùng). Tấm ghép: v4-try3 | v5-try2 | bản mới cùng cỡ, dải bốn khung mới, bản thu cao 120 px. Tự chấm năm tiêu chí: nguồn chính, tia phụ, độ dày, nét sét, đúng màu; điểm cuối là thấp nhất. Báo cáo ≤ 150 chữ.

Phản biện: PASS (Sonnet, 13/11; thêm so màu dải bốn khung)
