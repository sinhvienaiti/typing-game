# Làn Codex A · Việc A3 · KTX2 cho các thư mục flipbook còn lại của làn 2, 4 và A2

Bối cảnh (07/11 02:25):
- A1 đã thêm lệnh `tools/vfx-flipbook/run.sh ktx2` và nén `beast/`, `boss/`, `foe/`, `mech/`: bộ nhớ GPU giảm khoảng 4 lần.
- A2 đã nén 13 atlas mới của nó.
- Còn các atlas PNG khác trong `meta/`, `cutin-mat/`, `world/`, `charge-fill/`, `spirit/`, `expansion-phases/`, `foe-i2v/`.

**Model `gpt-6.1-sol`, mức `medium`** (việc máy móc). Báo cáo: `docs/codex-queue/laneA3-report.md` (tiếng Việt, ngắn).

## Việc
1. Chạy `run.sh ktx2` cho 7 thư mục trên. Mục nào đã có KTX2 khớp `md5` thì lệnh tự bỏ qua.
2. **Đạt khi:**
   - bộ kiểm manifest (cách chạy như `lane-2-flipbooks.md`) báo `0 problems` cho 7 thư mục;
   - báo cáo có bảng: thư mục · số atlas · MiB GPU RGBA (gồm mip) · MiB GPU KTX2 · MiB KTX2 trên đĩa;
   - kiểm 3 file bằng `tools/vfx-flipbook/ktx2/inspect.mjs`.

## Ranh giới
- **Chỉ ghi:**
  - file `.ktx2` mới và mục `ktx2` trong manifest của 7 thư mục trên;
  - `.local/vfxlab-laneA/`;
  - báo cáo.
- **Không đụng:**
  - các thư mục hệ (phiên lab-flipbooks quản);
  - `beast/`, `boss/`, `foe/`, `mech/`;
  - `.wrong-ref-2026-11-07/`.
- Không sửa mã, PNG hay JSON atlas. Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
