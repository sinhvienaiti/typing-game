# Phiếu 379e · Tu Tiên · Cột năng lượng: biến thể ba tia chính (so với bản hai tia)

Anh xem cột năng lượng 379d (hai tia chính, hẹp 2/3): "bản 2 tia sét khá đẹp r, cơ mà nếu để 3 tia liệu có đẹp hơn k nhỉ?". Vẽ một biến thể ba tia để đặt cạnh bản hai tia; giữ mọi thứ khác của 379d.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần `image_gen`** (try1–try3 cho mỗi loại ảnh), `view_image` tối đa 8. Báo cáo `docs/codex-queue/379e-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column-3bolt.v1-try*.png`, `S/thunder-energy-column-3bolt-frames.v1-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-energy-379e-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`, và đưa vào image_gen để giữ chất)
`S/thunder-energy-column.v3-try4.png`, `S/thunder-energy-column-frames.v3-try4.png` (bản hai tia anh khen: khổ, bề rộng thân, độ dày tia, màu, chân nổ, mây, tia phụ).

## Hình
Giống hệt bản hai tia về khổ 1024×1536, **bề rộng thân** (giữ đúng, không rộng thêm), chân, mây, màu bạch kim, tia phụ mờ. Khác duy nhất: **ba tia sét chính dày**, gấp khúc gắt, từ mây xuống chân; tia giữa dày nhất, hai tia bên mảnh hơn một chút (khoảng 3/4 tia giữa); ba tia tách và chạm nhau ở vài điểm, không xoắn đều, vẫn đọc rõ từng tia (có khe tối giữa các tia). Ảnh frames: bốn khung liên tiếp như bản hai tia.

## Kiểm và tự chấm
Script: đo `S/thunder-energy-column.v3-try4.png` và ảnh mới bằng cùng một script: bề rộng thân (hàng 40/50/60 %, ngưỡng 50 % độ sáng lớn nhất của hàng, trung vị) của ảnh mới bằng bản hai tia ± 8 %; trên ít nhất 2 trong 3 hàng đo, tìm được đúng 3 dải sáng (tia chính) tách nhau bởi khe có độ sáng < 40 % độ sáng lớn nhất của hàng; chân cùng hàng; lề ≥ 6 %. Tấm ghép: hai tia | ba tia cạnh nhau cùng cỡ; hai dải bốn khung; bản thu cao 120 px của cả hai; và một ô ghép thử chùm 5 cột trộn (hai tia, ba tia, hai tia, ba tia, hai tia). Tự chấm theo mặt yếu nhất (ba tia vẫn rõ từng tia, không thành "nhiều tia hợp lại", không rộng thêm); dưới 8 vẽ lại. Báo cáo ≤ 150 chữ, kèm nhận xét thật: ba tia đẹp hơn, kém hơn hay chỉ khác.

Phản biện: PASS (Sonnet, 13/11; ba sửa đã làm)
