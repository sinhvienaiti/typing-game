# Làn Codex A · Việc A1 · Nén KTX2 cho atlas flipbook có sẵn

Bối cảnh (07/11 01:45):
- Làn 6 (`c93e2f3`, nhánh `codex/lab-all`) cho quái trong lab dùng 15 atlas PNG của `beast/`, `boss/` và `mech/`. Nạp đủ cả 15 thì tốn khoảng 298 MiB GPU.
- Phiếu 325 đã cho lab đọc được KTX2. Hàm `ktx2Of` trong `games/.wt-ic-lab-all/src/view/skills/flipbook.ts` (dòng 198–214) đọc mục `ktx2` trong manifest: `yFlip: true`, `uastc` hoặc `etc1s` là `{ file, md5, bytes }`. Thiếu KTX2 thì lab tự quay về PNG.
- Nhưng `tools/vfx-flipbook/run.sh` mới chỉ có `upgrade`, lệnh này dựng lại atlas từ clip nguồn. Chưa có lệnh nén atlas PNG đang có.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneA1-report.md` (tiếng Việt, ngắn). Làm lần lượt; mỗi việc tự kiểm theo "Đạt khi" rồi mới sang việc kế.

## Ranh giới
- **Được ghi:**
  - mã trong `tools/vfx-flipbook/` (lệnh mới và test của nó);
  - file `.ktx2` mới và mục `ktx2` trong `manifest.json` của 4 thư mục `art-src/lab/vfx/{beast,boss,foe,mech}/`;
  - `.local/vfxlab-laneA/`;
  - báo cáo.
- **Cấm:**
  - sửa PNG hay JSON atlas có sẵn, và mọi trường manifest khác `ktx2`;
  - ghi vào các thư mục `vfx` khác. `meta/`, `cutin-mat/`, `world/`, `expansion-phases/` sắp được cắt lại; các thư mục hệ thuộc phiên khác;
  - sửa mã lab hay game;
  - cài gói mới (bộ mã hoá đã cài ở `tools/vfx-flipbook/ktx2/node_modules`);
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Danh sách việc
1. **Lệnh `ktx2`:**
   - `tools/vfx-flipbook/run.sh ktx2 <thư mục manifest> [--only id,id] [--force]` đọc từng mục manifest, nén atlas PNG của mục đó thành KTX2 UASTC bằng bộ mã hoá phiếu 325.
   - Giữ đúng cách lật Y mà `ktx2Of` đòi (`yFlip: true`). Mipmap như cách `upgrade` đang làm.
   - Ghi `<id>.uastc.ktx2` cạnh PNG và thêm mục `ktx2` vào manifest (ghi nguyên tử, giữ nguyên mọi trường khác). Chạy lại không đổi gì nếu file đã khớp `md5`.
   - **Đạt khi:**
     - test của công cụ qua, gồm test mới cho lệnh `ktx2` trên một atlas nhỏ tổng hợp: lật Y đúng, manifest đúng định dạng `ktx2Of`, chạy lại cho ra file giống từng byte;
     - `run.sh test -q` qua toàn bộ.
2. **Áp cho `beast/`, `boss/`, `foe/`, `mech/`:**
   - **Đạt khi:**
     - bộ kiểm manifest (cách chạy như `docs/work/codex-lanes/lane-2-flipbooks.md`) báo `0 problems` cho 4 thư mục;
     - báo cáo có bảng: thư mục · số atlas · MiB GPU kiểu RGBA (gồm mip) · MiB KTX2 · MiB trên đĩa;
     - mở 3 file KTX2 bất kỳ bằng chính thư viện mã hoá (hoặc `ktx info` nếu có) để kiểm kích thước và số mip.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
