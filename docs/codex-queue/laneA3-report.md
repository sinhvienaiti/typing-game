# Làn A3 · KTX2 cho 7 thư mục flipbook

Đã hoàn tất ngày 07/11/2026: chạy `tools/vfx-flipbook/run.sh ktx2` cho đủ 7 thư mục dưới `games/immortality-cultivation/art-src/lab/vfx/`. Tạo mới 90 file `.uastc.ktx2`, cập nhật trường `ktx2` tương ứng; bỏ qua 13 atlas có KTX2 khớp MD5 (meta 5, cutin-mat 5, world 2, expansion-phases 1). Không bỏ thư mục nào.

| Thư mục | Số atlas | MiB GPU RGBA (gồm mip) | MiB GPU KTX2 | MiB KTX2 trên đĩa |
| --- | ---: | ---: | ---: | ---: |
| meta | 24 | 710.67 | 177.67 | 49.39 |
| cutin-mat | 8 | 321.33 | 80.33 | 18.38 |
| world | 14 | 534.00 | 133.50 | 40.57 |
| charge-fill | 14 | 672.00 | 168.00 | 32.93 |
| spirit | 4 | 192.00 | 48.00 | 10.59 |
| expansion-phases | 23 | 862.50 | 215.63 | 105.26 |
| foe-i2v | 16 | 768.00 | 192.00 | 37.45 |
| **Tổng** | **103** | **4060.50** | **1015.14** | **294.58** |

GPU được tính từ kích thước từng mip: RGBA 4 byte/pixel; UASTC 16 byte/block 4×4, làm tròn block ở từng mip. Tổng giảm khoảng 4 lần (75%). Đây là dung lượng block nén, không phải phép đo GPU thực tế trong game; runtime cần dùng định dạng nén tương ứng.

## Kiểm tra

- Bộ kiểm manifest gốc được sao chép vào `.local/vfxlab-laneA/a3-validate-manifests.ts`, chỉ giới hạn vòng lặp vào 7 thư mục. Chạy từ thư mục game bằng `node --import tsx /Volumes/SS990TPRO/htdocs/typing-game/.local/vfxlab-laneA/a3-validate-manifests.ts`: **103 task entries, 0 problems**. Dùng cách gọi này vì CLI `tsx` bị sandbox chặn IPC pipe.
- `.local/vfxlab-laneA/a3-verify.py`: **103 atlas, 0 problems**; kiểm MD5 nguồn/đầu ra, byte count, kích thước, đủ mip và block UASTC/Zstd. Đối chiếu snapshot trước khi nén: PNG, JSON atlas, KTX2 có sẵn và mọi trường manifest ngoài `ktx2` nguyên vẹn.
- `node tools/vfx-flipbook/ktx2/inspect.mjs <file>` mở và bắt đầu transcode thành công 3 file dưới đây; cả ba là UASTC, sRGB, Zstd, 4096×2304, 13 mip:
  - `meta/reward-linh-sa-stream.uastc.ktx2`
  - `charge-fill/light-charge-fill.uastc.ktx2`
  - `foe-i2v/foe-elite-crest-regen.uastc.ktx2`

Log và số liệu: `.local/vfxlab-laneA/a3-encode-*.log`, `a3-validator.log`, `a3-verification.log`, `a3-metrics.json`, `a3-inspect-three.json`; snapshot nguồn: `a3-baseline.json`.

Không sửa mã, PNG, JSON atlas, không chạy build/test game, không mở trình duyệt/cổng mạng hay dùng lệnh git ghi. Không đụng các thư mục bị cấm. Chủ dự án chỉ cần xem bảng dung lượng và kết quả kiểm ở trên; không có lựa chọn hình ảnh cần duyệt trong việc này.
