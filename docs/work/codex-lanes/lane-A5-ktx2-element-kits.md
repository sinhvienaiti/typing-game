# Làn Codex A · Việc A5 · KTX2 cho bộ flipbook của 14 hệ và các thư mục chiêu

Bối cảnh (07/11 09:15):
- A1 và A3 đã nén KTX2 cho các thư mục quái, boss, thế giới, meta và các thư mục khác. Bộ nhớ GPU còn khoảng 1/4.
- Lab tự dùng KTX2 khi manifest có mục `ktx2` (`setFlipbookKtx2` trong `src/lab/skills-main.ts`; `?ktx2=0` quay về PNG).
- Lớn nhất còn lại là bộ hệ và các thư mục chiêu phím 8/9. Bản đo lab-perf ngày 06/11 ghi 48 atlas phím 8/9 chiếm 1,87 GB.
- Phiên lab-flipbooks quản các thư mục này, nhưng đã dừng và tắt việc tự cắt, nên giờ ghi được.

**Model `gpt-6.1-sol`, mức `medium`** (việc máy móc). Báo cáo: `docs/codex-queue/laneA5-report.md` (tiếng Việt, ngắn).

## Việc
1. Chạy `tools/vfx-flipbook/run.sh ktx2 <thư mục>` cho mọi thư mục có `manifest.json` flipbook dưới `games/immortality-cultivation/art-src/lab/vfx/`, **trừ**:
   - `sigils/` (định dạng khác);
   - `hybrid/` (bản demo A/B anh đang xem);
   - `first-frames/` (ảnh tĩnh);
   - các thư mục đã nén xong (`beast`, `boss`, `foe`, `mech`, `meta`, `cutin-mat`, `world`, `charge-fill`, `spirit`, `expansion-phases`, `foe-i2v`): lệnh tự bỏ qua mục khớp `md5`, chạy lại cũng không sao.
2. **Đạt khi:**
   - bộ kiểm manifest (cách chạy như `lane-2-flipbooks.md`) báo `0 problems` cho mọi thư mục đã chạy;
   - báo cáo có bảng: thư mục · số atlas · MiB GPU RGBA (gồm mip) · MiB GPU KTX2 · MiB trên đĩa, cộng dòng tổng;
   - kiểm 3 file bất kỳ bằng `tools/vfx-flipbook/ktx2/inspect.mjs`.

## Ranh giới
- **Chỉ ghi:**
  - file `.ktx2` mới và mục `ktx2` trong manifest (giữ nguyên mọi trường khác);
  - `.local/vfxlab-laneA/`;
  - báo cáo.
- Không sửa mã, PNG hay JSON atlas. Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
