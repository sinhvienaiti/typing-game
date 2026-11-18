# Phiếu 379c · Tu Tiên · Cột năng lượng: thu hẹp thân một phần ba

Anh xem cột năng lượng 379b (13/11 12:1x): "nó lại hơi dày r, nên giảm 1/3 lại là được". Chỉ sửa bề rộng thân; giữ nguyên mọi thứ khác (chất plasma, vằn điện, nhánh ngắn ở rìa, chân nổ, mây nhỏ, màu, khổ ảnh, chiều cao, vị trí chân).

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần `image_gen`** (chế độ sửa ảnh, đưa ảnh gốc vào), `view_image` tối đa 6. Báo cáo `docs/codex-queue/379c-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column.v2-try*.png`, `S/thunder-energy-column-frames.v2-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi ảnh gốc đã sửa), tấm ghép `S/thunder-energy-379c-sheet.jpg`. Giữ nguyên bản v1. Cấm git ghi, sửa file có sẵn, mã.

## Ảnh gốc (đưa vào image_gen để sửa)
`S/thunder-energy-column.v1-try3.png` và `S/thunder-energy-column-frames.v1-try3.png`.

## Sửa
Bề rộng thân cột còn **khoảng 2/3 bản gốc** (thân rộng khoảng 22 % chiều cao thay vì ~33 %). Thu hẹp bằng cách vẽ lại thân hẹp hơn, **không kéo méo** (vằn điện giữ tỉ lệ tự nhiên, không bị bóp dẹt theo chiều ngang). Mây đỉnh và vụ nổ chân thu theo cho cân với thân mới (rộng hơn thân một chút). Bốn khung của ảnh frames sửa giống hệt.

## Kiểm và tự chấm
Script: đo bề rộng thân trên bản gốc và bản mới: ở các hàng 40 %, 50 %, 60 % chiều cao thân, lấy khoảng điểm ảnh có độ sáng > 50 % độ sáng lớn nhất của hàng đó, rồi lấy trung vị ba hàng; tỉ lệ mới/gốc trong 0,6–0,72; chân cùng hàng pixel với bản gốc (lệch ≤ 2 % chiều cao); lề ≥ 6 %. Tấm ghép: gốc | mới cạnh nhau cùng cỡ, dải bốn khung mới, bản thu cao 120 px. Tự chấm theo mặt yếu nhất (đúng 2/3 bề rộng, không méo, giữ chất gốc); dưới 8 làm lại. Báo cáo ≤ 150 chữ.

Phản biện: PASS (Sonnet, 13/11; sửa cách đo bề rộng)
