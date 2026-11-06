# Phiếu 325 · Báo cáo

Đã làm xong lệnh `upgrade`, 73 test và hai bộ xuất thật. Còn chặn ở việc lưu bản review vào SSD: sandbox không cho ghi `typing-game-review/` dù phiếu cho phép; các file chờ chép được giữ trong `/private/tmp`.

## File

- Sửa `tools/vfx-flipbook/run.sh`, `.gitignore`, `vfxflip/{__main__,pipeline,timing,grade,video_export}.py`.
- Thêm `vfxflip/{motion,ktx2,upgrade}.py`, `ktx2/encode.mjs`, `tests/test_upgrade.py` trong cùng công cụ.
- Giữ nguyên các file đã được Claude chuẩn bị: `requirements.txt`, `ktx2/{package.json,package-lock.json}`; không sửa bảng cấu hình.
- Xuất `games/immortality-cultivation/art-src/lab/vfx/hybrid/{manifest.json,azure-cloud-dragon.*,fire-comet.*}`: mỗi clip có atlas PNG, JSON, vector PNG và 4 KTX2; rồng thêm 2 MP4.

## Môi trường và kiểm tra

- Không chạy cài đặt, không dùng mạng. Gói có sẵn: Python 3.12, numpy 2.5.4, scipy 1.18.1, Pillow 13.0.0, pytest 9.1.1, OpenCV 4.14.0; `ktx2-encoder` 0.6.0, `ktx-parse` 1.1.0.
- Chú thích `run.sh` ghi các lệnh cài riêng cho công cụ: `uv venv --python ~/AudioLab/python/cpython-3.12-macos-aarch64-none/bin/python3.12 tools/vfx-flipbook/.venv`, `uv pip install --python tools/vfx-flipbook/.venv/bin/python -r tools/vfx-flipbook/requirements.txt`, `npm install --no-audit --no-fund --prefix tools/vfx-flipbook/ktx2`.
- Trước sửa: **54 passed**. Sau sửa, đúng lệnh kiểm của phiếu: **73 passed in 18.27s**, **0 skipped**. OpenCV, hai codec × hai transfer và kiểm tra đầu cuối đều đã chạy. Có kiểm tra `6 fps --no-mv` và trần atlas không ghi vào đích.
- `git diff --check`: sạch. MD5/dung lượng của 12 file PNG/KTX2 đều khớp manifest; 8 KTX2 có 12 mipmap, đúng transfer sRGB=2/linear=1 và supercompression UASTC=2/ETC1S=1.
- Bộ đọc cũ trước xuất: `333 task entries, 0 problems`. Sau xuất: `hybrid 2 entries parse OK, 2 from this task`; `338 task entries, 0 problems`. Phần tăng là 2 mục của phiếu + 3 mục phiên khác thêm đồng thời (metal 16→17, star 18→19, void 18→19); phạm vi ban đầu cộng phiếu là 333+2=335.
- Bộ đọc lab từ `games/.wt-ic-lab-elements/src/view/skills/flipbook.ts`: nhận `azure-cloud-dragon, fire-comet`. File kiểm: `/private/tmp/codex-325-parse.mts`.
- Lệnh `tsx` trực tiếp bị `listen EPERM` ở IPC. Chạy cùng script qua `node --import ./games/<game>/node_modules/tsx/dist/loader.mjs <script>` thành công với cả hai bộ đọc. Không mở trình duyệt, không chạy build/test game.

## Số đo

Cả hai atlas: ô 768×432, lưới 4×8, cỡ 3072×3456 (dưới trần 4096). Rồng: 31 khung, 6 fps, một lần, nguồn [0,121), bước 4, look neutral. Sao chổi: 32 khung, 24 fps, lặp, nguồn [29,61), bước 1, look cool. KTX2: UASTC mức 2; ETC1S chất lượng 150; lật Y, có mipmap.

| Clip / lớp | PNG (byte) | UASTC (byte; giây mã hoá) | ETC1S (byte; giây mã hoá) |
|---|---:|---:|---:|
| azure-cloud-dragon / màu | 8,944,837 | 6,155,689; 19.995 s | 1,108,886; 17.795 s |
| azure-cloud-dragon / vector | 3,147,325 | 6,061,442; 33.994 s | 1,082,877; 6.712 s |
| fire-comet / màu | 4,814,051 | 3,493,680; 12.579 s | 605,250; 10.512 s |
| fire-comet / vector | 2,567,476 | 3,996,636; 21.964 s | 863,030; 6.693 s |

| Clip | strength (UV/bước) | warpRatio trung vị | p90 |
|---|---:|---:|---:|
| azure-cloud-dragon | 0.03952 | 0.593106 | 0.623217 |
| fire-comet | 0.01129 | 0.435435 | 0.532519 |

warpRatio dùng vector sau mã hoá/giải mã, so warp riêng khung đầu với khung sau. Không dùng kết quả blend ở w=1 để đo vì nó chính là khung sau.

| Video rồng | Cỡ | Khung / fps | Byte | SSIM so đúng đoạn nguồn |
|---|---|---|---:|---:|
| crf23, CRF 23 | 1920×1080 | 121 / 24 | 4,896,047 | 0.985045 |
| 720p, CRF 20 | 1280×720 | 121 / 24 | 3,862,105 | 0.980285 |

## Cảnh báo và phần cần xem

- `azure-cloud-dragon`: effect reaches the video frame edge: top,bottom; video frame edge inside the cell: faded over 35 px; no fade-out in the cut: neutral fade over the last 10 frames. Flags: [].
- `fire-comet`: effect reaches the video frame edge: top; video frame edge inside the cell: faded over 35 px. Flags: [].
- Rồng có tổng UASTC màu + vector 12.22 MB, lớn hơn tổng PNG 12.09 MB; ETC1S nhỏ hơn nhưng cần xem chất lượng trong demo A/B phiếu 326. Chưa chấm chất lượng hình hay chốt cách đóng gói.
- Không xuất video sao chổi vì không yêu cầu `--videos`; clip lặp chỉ xuất atlas. Preview hiện là khung atlas rời của pipeline, chưa phải demo trộn vector trong lab.
- `mkdir` thư mục review và `node scripts/review-index.mjs` đều bị sandbox trả `EPERM`; chưa tạo được ABOUT hay cập nhật INDEX trên SSD. Đã giữ đúng 6 file `<job>__v1.{sheet.jpg,preview.mp4,metrics.json}` và `ABOUT.md` tại đường dẫn tạm dưới đây; sheet dùng Arial, metrics kèm toàn bộ kết quả upgrade, không có khung thô.

Bản chờ chép: `/private/tmp/codex-325-vfxflip-real/captures/tu-tien/vfxflip-325/`.

Cần một phiên được ghi thư mục review chép 7 file này vào `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/vfxflip-325/`, rồi chạy `node scripts/review-index.mjs`. Không cần xuất lại media. Không có hạn mức API hay giờ chờ cụ thể.
