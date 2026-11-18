# Phiếu 379g · Tu Tiên · Cột năng lượng hai tia: tia dày hơn một chút

Anh xem một tia | hai tia | ba tia (13/11): "làn 2 tia, bạn nghĩ sao nếu cho tia dày hơn 1 chút?". Điều phối đề xuất 1,3 lần; anh chốt: "tăng khoảng 1,4 lần tôi nghĩ hợp lý hơn". Làm **1,4 lần**, giữ khe tối giữa hai tia (dày quá ~1,6 lần thì hai tia nhập thành mảng sáng như bản một tia). Sửa trên chính ảnh hai tia; giữ mọi thứ khác.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần `image_gen`** (try1–try3 cho mỗi loại ảnh; chế độ sửa ảnh, đưa ảnh gốc vào), `view_image` tối đa 8. Báo cáo `docs/codex-queue/379g-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column.v4-try*.png`, `S/thunder-energy-column-frames.v4-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi ảnh gốc đã sửa), tấm ghép `S/thunder-energy-379g-sheet.jpg`. Giữ nguyên bản cũ. Cấm git ghi, sửa file có sẵn, mã.

## Ảnh gốc
`S/thunder-energy-column.v3-try4.png`, `S/thunder-energy-column-frames.v3-try4.png`.

## Sửa
Hai tia sét chính **dày khoảng 1,4 lần** bản gốc (lõi trắng và quầng vàng nhạt cùng dày ra), giữ đúng đường gấp khúc, điểm tách và chạm nhau; **khe tối giữa hai tia** ở chỗ tách vẫn rộng ít nhất bằng nửa bề dày một tia. Bề rộng thân tổng được tăng theo (tối đa khoảng 1,3 lần gốc) để giữ khe tối. Chân, mây, tia phụ, màu giữ nguyên. Bốn khung sửa giống hệt.

## Kiểm và tự chấm
Script (cùng một script đo cả ảnh gốc và ảnh mới; hàng 40/50/60 % chiều cao thân, ngưỡng 50 % độ sáng lớn nhất của hàng): trên các hàng có đúng 2 dải sáng, trung vị bề rộng một dải của ảnh mới bằng 1,3–1,5 lần ảnh gốc; khe giữa hai dải (độ sáng < 40 % lớn nhất) ≥ 0,5 bề rộng một dải; bề rộng thân ≤ 1,3 lần gốc; ít nhất 2 trong 3 hàng đo có đúng 2 dải sáng, nếu không thì ghi FAIL và vẽ lại; chân cùng hàng; lề ≥ 6 %. Tấm ghép: gốc | mới cùng cỡ, dải bốn khung mới, bản thu cao 120 px. Tự chấm theo mặt yếu nhất; dưới 8 làm lại. Báo cáo ≤ 120 chữ.

Phản biện: PASS (Sonnet, 13/11; sửa trần bề rộng và điều kiện hàng đo)
