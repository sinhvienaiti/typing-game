# Báo cáo làn Codex A2

Chỉ xử lý media có sẵn; dùng `take1.mp4`, bỏ tên có `wrong-`. Không sinh ảnh, sửa video gốc, mã game/lab hoặc chạy build/test game. Log, sheet và số đo: `.local/vfxlab-laneA2/`.

- `meta/`: đã xem đủ 5 sheet, giữ 5 atlas; manifest 19 → 24. Hình chính đủ mép, không trống. Chỉ số nối: `ui-sunburst-halo-loop` 0,909; `hero-halo-ring-loop` 0,335 (đều ≤ 1,0). Bộ kiểm 4 thư mục: **0 problems**.
- `cutin-mat/`: đã xem đủ 5 sheet, giữ 5 atlas; manifest 3 → 8. Ba vòng lặp có chỉ số nối 0,790 / 0,777 / 0,783. Các dải tia/hạt là chất liệu phủ khung; hình chính đủ mép. Bộ kiểm: **0 problems**.
- `world/`: đã xem 2 sheet, giữ 2 atlas; manifest 12 → 14. Chỉ số nối `sky-route-ember-stream-loop`: 0,878.
- `expansion-phases/`: thêm `mountain-crushing-imperial-seal-manifest` từ clip `i2v-mountain-crushing-imperial-seal-manifest-r2`; manifest 22 → 23. Tái dùng atlas làn 4 sau khi đối chiếu MD5 nguồn; đã xem sheet, thân ấn đủ mép. Giữ vai `manifest` và phát đảo theo tiến độ gõ.
- Bỏ `i2v-yin-yang-void-mirror-manifest-r2` theo phiếu: vành dưới cụt biên lúc nở. Không đụng `void-wave`, `dark-big-burst` hoặc `.wrong-ref-2026-11-07/`.

Tổng PNG: 13 atlas, số mục 56 → 69; bộ kiểm 4 thư mục **0 problems**. PNG **44.11 MiB**; đã nén đủ **13 KTX2 UASTC, 29.33 MiB** bằng `run.sh ktx2 --only` đúng id. MD5 nguồn/PNG/KTX2 khớp; chiều rộng lớn nhất 4096, chiều cao lớn nhất 2880 px (mỗi cạnh ≤ 4096). Cả 6 vòng lặp có chỉ số nối ≤ 1,0.

Dùng nguyên cấu hình làn 4. Cần chủ xem hình trong lab khi tích hợp; đây là kiểm cắt atlas, chưa phải nghiệm thu trong game. Các cảnh báo nguồn chạm biên/fade của công cụ được giữ trong manifest; dải chất liệu đi xuyên biên được phân biệt với thân hình chính.
