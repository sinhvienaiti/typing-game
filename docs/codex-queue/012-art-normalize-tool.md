# Phiếu 012 · Công cụ hậu kỳ ảnh `tools/art-normalize` và xử lý ảnh Rồng Giữ Ải còn lỗi

**Bối cảnh:** các phiếu ảnh trước để lại cùng một loại lỗi mà `image_gen` không tự sửa được:
- nền chưa phẳng đúng mã màu;
- sai khổ;
- decal thiếu lề;
- phông xa chưa liền mép khi lặp ngang;
- biểu tượng chưa có alpha.

Các lỗi này sửa bằng ImageMagick, không cần sinh lại ảnh. Phiếu này làm một công cụ dùng chung cho mọi game, rồi chạy nó trên ảnh của Rồng Giữ Ải. Phiếu 010a, 010b, 010c của Tu Tiên sẽ dùng lại công cụ này.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `tools/art-normalize/`: script, README, test nhỏ;
- `games/dragon-hold/art-src/`: chỉ thêm file mới, xem mục 2; không ghi đè ảnh có sẵn;
- `games/dragon-hold/art-src/2d/README-normalize.md`.

Không chạy git commit, push, reset, stash, clean.

## Cách chạy lệnh

- ImageMagick 7 ở `~/.local/bin/magick` trong WSL Ubuntu. Ổ `D:` là `/mnt/d`.
- Gọi bằng `wsl -e bash /mnt/d/typing-game/tools/art-normalize/<x>.sh …`.
- Script viết bằng bash, `set -euo pipefail`, tìm `magick` qua `PATH` rồi tới `~/.local/bin/magick`.
- Có thể dùng Python 3 của WSL nếu cần đo. Không cài gói mới bằng `sudo`.

## 1. Công cụ `tools/art-normalize/`

Mỗi lệnh nhận file vào và file ra; không bao giờ ghi đè file vào.

| Lệnh | Làm |
|---|---|
| `key-alpha.sh <in> <out> [--bg auto\|#RRGGBB] [--fuzz 12%]` | Tách nền phẳng thành alpha: lấy màu nền từ 4 góc (`auto`), làm mềm mép 1 px, khử viền màu nền còn bám (defringe) |
| `pad-margin.sh <in> <out> --size 1024 --margin 8%` | Cắt sát vật (trim) rồi đặt vào giữa ô vuông với lề tối thiểu. Ảnh nhiều vật trong 4 phần tư (atlas 2×2): `--grid 2x2` xử lý từng phần tư |
| `flat-bg.sh <in> <out> --bg '#E6E6E6' --size 1024x1024` | Ảnh nguồn gửi Tripo: tách vật khỏi nền gần đúng, đặt lên nền phẳng đúng mã, vật ở giữa, lề 8 %, đúng khổ yêu cầu |
| `seamless.sh <in> <out> --axis x\|xy [--blend 12%]` | Làm liền mép khi lặp: ngang cho phông, cả hai chiều cho ô đất |
| `seam-check.sh <in> <out> --axis x\|xy` | Ghép ảnh kề chính nó (2×1 hoặc 2×2) và in sai lệch trung bình cột hoặc hàng ở mép |
| `icon.sh <in> <outdir> --sizes 256,64` | Tách alpha, cắt sát, vuông hóa, xuất các cỡ |
| `sheet.sh <out.png> <files…> [--bg dark\|light\|checker] [--tile 256]` | Làm ảnh xem nhanh (montage, có tên file) |

- **README:** cách dùng; giới hạn của từng lệnh (ví dụ key-alpha khó với vật cùng màu nền).
- **Test nhỏ** `tools/art-normalize/test.sh`:
  - tạo ảnh giả bằng `magick`;
  - kiểm khổ ra, alpha ở góc bằng 0, lề đúng;
  - kiểm sai lệch mép sau `seamless.sh` nhỏ hơn trước.

## 2. Chạy trên ảnh Rồng Giữ Ải

Đọc trước:
- `games/dragon-hold/art-src/2d/README-m0-wave1-3.md`;
- `README-m0-wave4-5.md`;
- `README-m0-redo.md`.

Xuất bản xử lý **cạnh ảnh gốc** với hậu tố, không ghi đè:

1. **4 decal D1–D4** (`art-src/decals/pine-river/`):
   - atlas 2×2 nền khóa màu → `<tên>.alpha.png`, 1024², alpha, lề ≥ 8 % trong từng phần tư (48 px ở khổ 1024 cho mỗi phần tư 512).
   - Các decal đợt 1–3 khác có cùng lỗi thì xử lý luôn.
2. **Phông xa B1** (`art-src/backdrops/pine-river-far.png`):
   - → `pine-river-far.seamless.png`, liền mép ngang;
   - ảnh kiểm ghép 2×1 → `art-src/_review/pine-river-far.seam.png`.
3. **20 icon đợt 4–5** → thư mục `art-src/icons/normalized/` (256 và 64), cùng ảnh xem nhanh 256/64/32 px.
4. **Ảnh nguồn Tripo** (sinh vật, lính, prop có 2 góc trong `art-src/`):
   - → `<tên>.tripo.png`: nền `#E6E6E6` phẳng, đúng khổ prompt, vật ở giữa, lề 8 %.
   - Không sửa hình vật. Ảnh nào tách nền làm hỏng mép thì bỏ, ghi lý do.
5. **Ảnh xem nhanh** trong `art-src/_review/`. Mở xem ảnh trước khi khẳng định kết quả đạt.

## 3. Báo cáo

Viết `games/dragon-hold/art-src/2d/README-normalize.md`:
- bảng từng ảnh: file vào, file ra, lệnh đã chạy, số đo trước và sau (lề, sai lệch mép, mã nền góc), đạt hay chưa;
- những ảnh vẫn phải sinh lại bằng `image_gen` vì lỗi nằm ở hình chứ không ở nền hay khổ (ví dụ góc cánh E01-S, khuỷu tay G01, U1);
- những gì chủ dự án nên xem.

**Xong khi:**
- công cụ và test chạy được (`test.sh` đạt);
- 5 việc ở mục 2 làm xong, hoặc ghi lý do;
- README đã có.
