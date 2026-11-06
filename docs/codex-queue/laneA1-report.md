# Làn A1 · Nén KTX2 atlas có sẵn

Hoàn tất cả hai việc, không bỏ atlas nào. Chỉ ghi trong các đường dẫn được phép; không sửa mã lab/game, không cài gói, không chạy build hay test game, không chạy lệnh git ghi.

**Việc 1 — ĐẠT.** Thêm `tools/vfx-flipbook/run.sh ktx2 <thư mục manifest> [--only id,id] [--force]`. Mã mới: `tools/vfx-flipbook/vfxflip/atlas_ktx2.py`; nối CLI tại `vfxflip/__main__.py` và hướng dẫn trong `run.sh`. Dùng nguyên bộ mã hoá phiếu 325: UASTC level 2, sRGB, lật Y, đủ mipmap. Đầu ra `<id>.uastc.ktx2`; manifest ghi nguyên tử, chỉ thêm/sửa trường `ktx2`. Checksum nguồn nằm trong `ktx2.uastc.sourceMd5`; kiểm cả checksum đầu ra trước khi bỏ qua. Có phát hiện nguồn hoặc mục manifest bị đổi trong lúc nén.

`tests/test_atlas_ktx2.py`: **13 test qua**, gồm giải mã pixel xác nhận lật Y, ảnh 64×32 có đủ 7 mip, manifest đúng hợp đồng, `--force` nén lại cho file giống từng byte, chọn id, phục hồi file hỏng, bảo toàn trường khác và xử lý lỗi ghi nguyên tử. Toàn bộ `run.sh test -q`: **86 passed**, không bỏ test. Log: `.local/vfxlab-laneA/test.log`.

**Việc 2 — ĐẠT.** Tạo 47 file `.uastc.ktx2` và cập nhật 47 mục `ktx2` trong `games/immortality-cultivation/art-src/lab/vfx/{beast,boss,foe,mech}/manifest.json`. Số mục trước/sau lần lượt: 13/13, 15/15, 15/15, 4/4.

| Thư mục | Số atlas | MiB GPU RGBA, gồm mip | MiB GPU KTX2 | MiB KTX2 trên đĩa |
| --- | ---: | ---: | ---: | ---: |
| beast | 13 | 264,67 | 66,17 | 17,70 |
| boss | 15 | 412,67 | 103,17 | 30,93 |
| foe | 15 | 408,67 | 102,17 | 30,98 |
| mech | 4 | 146,00 | 36,50 | 7,95 |
| **Tổng** | **47** | **1.232,00** | **308,01** | **87,55** |

MiB = byte / 1.048.576. GPU RGBA tính từng mức mip theo kích thước thật; GPU KTX2 là ước tính khi transcode sang BC7/ASTC 4×4, 16 byte/block, đã tính block đệm ở mip nhỏ. Đây là phép tính dung lượng texture, chưa phải đo GPU trong trình duyệt. Cột trên đĩa là kích thước file KTX2 đã nén Zstd. Tổng toàn bộ file trong bốn thư mục sau khi thêm KTX2 là 201,35 MiB.

Kiểm chứng cuối:

- Bộ kiểm manifest của làn 2, giới hạn đúng bốn thư mục: **47 task entries, 0 problems**. Chạy qua `node --import ./node_modules/tsx/dist/loader.mjs` từ thư mục game để tránh IPC của CLI `tsx` trong sandbox; bản kiểm chỉ đọc tại `.local/vfxlab-laneA/validate-manifests.ts`.
- Parser thật của lab `games/.wt-ic-lab-all/src/view/skills/flipbook.ts`: **47 KTX2 entries accepted by lab ktx2Of, 0 problems**; kiểm URL có md5 và số byte. Log: `.local/vfxlab-laneA/runtime.log`.
- Đối chiếu `.local/vfxlab-laneA/baseline.json`: toàn bộ PNG, JSON atlas và mọi trường manifest ngoài `ktx2` giữ nguyên. Kiểm đủ checksum, kích thước và mip của cả 47 KTX2. Số liệu: `.local/vfxlab-laneA/metrics.json`; log: `verification.log` cùng thư mục.
- Mở bằng WASM Basis của chính bộ mã hoá qua `tools/vfx-flipbook/ktx2/inspect.mjs`: `beast/beast-hit-spark-burst.uastc.ktx2` 2560×1280, 12 mip; `boss/boss-death-explosion-r2.uastc.ktx2` 2560×1280, 12 mip; `mech/pillar-shelter-ward-loop.uastc.ktx2` 2560×2560, 12 mip. Cả ba hợp lệ, bắt đầu transcode thành công. Chi tiết: `.local/vfxlab-laneA/inspect-three.json`.
- Chạy lại lệnh trên cả bốn thư mục: **0 nén lại, 47 bỏ qua**; mọi byte và mtime của tất cả file trong bốn thư mục giữ nguyên. Log: `.local/vfxlab-laneA/rerun.log`.

Không còn việc bắt buộc của phiếu. Chủ xem bảng dung lượng và có thể kiểm cảm quan trong lab ở bước nghiệm thu riêng; phiên này không mở trình duyệt theo ranh giới phiếu.
