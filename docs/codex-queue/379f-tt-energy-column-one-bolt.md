# Phiếu 379f · Tu Tiên · Cột năng lượng: biến thể một tia chính rất dày

Anh (13/11, sau khi đồng ý thử ba tia): "vẽ tiếp cả loại 1 tia nhưng dày ngang 2-3 tia nữa nhé". Giữ mọi thứ khác của bản hai tia 379d.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần `image_gen`** (try1–try3 cho mỗi loại ảnh), `view_image` tối đa 8. Báo cáo `docs/codex-queue/379f-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column-1bolt.v1-try*.png`, `S/thunder-energy-column-1bolt-frames.v1-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-energy-379f-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`, và đưa vào image_gen để giữ chất)
`S/thunder-energy-column.v3-try4.png`, `S/thunder-energy-column-frames.v3-try4.png` (bản hai tia anh khen).

## Hình
Giống hệt bản hai tia về khổ 1024×1536, bề rộng thân, chân, mây, màu bạch kim, tia phụ mờ. Khác duy nhất: **một tia sét chính duy nhất**, bề dày bằng **tổng bề dày hai đến ba tia của bản hai tia** (khoảng 0,5–0,7 bề rộng thân), lõi trắng rực, gấp khúc gắt từ mây xuống chân như một tia sét khổng lồ; mép tia có điện nhỏ bám và vài nhánh ngắn. Ảnh frames: bốn khung liên tiếp, tia chính đổi đường gấp khúc giữa các khung.

## Kiểm và tự chấm
Script: đo `S/thunder-energy-column.v3-try4.png` và ảnh mới bằng cùng script: bề rộng thân (hàng 40/50/60 %, ngưỡng 50 % độ sáng lớn nhất của hàng, trung vị) bằng bản hai tia ± 8 %; trên ít nhất 2 trong 3 hàng, đúng **1** dải sáng chính, bề rộng dải đó ≥ 1,8 lần "bề rộng một tia của bản hai tia" (= trung vị bề rộng từng dải sáng riêng, cùng ngưỡng 50 %, trên các hàng mà ảnh hai tia có đúng 2 dải); chân cùng hàng; lề ≥ 6 %. Tấm ghép: một tia | hai tia | ba tia (try được chọn trong `docs/codex-queue/379e-report.md`; nếu báo cáo chưa có thì `S/thunder-energy-column-3bolt.v1-try3.png`) cạnh nhau cùng cỡ; dải bốn khung; bản thu cao 120 px. Tự chấm theo mặt yếu nhất (một tia dày uy lực, vẫn đọc là sét gấp khúc chứ không thành ống sáng); dưới 8 vẽ lại. Báo cáo ≤ 150 chữ, kèm nhận xét thật so với hai tia và ba tia.

Phản biện: PASS (Sonnet, 13/11; hai sửa đo đã làm)
