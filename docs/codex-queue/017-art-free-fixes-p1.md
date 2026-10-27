# Phiếu 017 · Rồng Giữ Ải, Lời Gọi · sửa ảnh 2D không tốn tiền (P1 và 3 ảnh bắt buộc trước Tripo)

**Bối cảnh:** luật 7 điểm của chủ dự án (26/10/2026, `docs/games/ART_ACCEPTANCE.md`) yêu cầu sửa bằng công cụ trước khi tạo lại. `docs/games/ART_FIX_QUEUE.md` §2 và §5 đã ghi sẵn lệnh cho từng ảnh. Phiếu này chỉ làm **14 ảnh 2D** dưới đây: ảnh P1 và 3 ảnh P2 bắt buộc sửa trước khi gửi Tripo. Không đụng model 3D, không làm mục P2/P3 khác.

Chủ dự án (27/10) giao một phần việc nhỏ cho Codex và yêu cầu làm đúng, không sai sót. Vì vậy phiếu có **bước kiểm bắt buộc** (mục "Kiểm"). Claude sẽ chạy lại các bước kiểm đó trước khi nhận.

**Thư mục làm việc:** gốc repo. Chỉ được ghi:
- file mới cạnh ảnh nguồn, đúng tên ở cột "Ra file" (cùng thư mục với ảnh nguồn, trừ khi bảng ghi thư mục khác);
- `games/<game>/art-src/_review/017-*.jpg`, `games/<game>/art-src/_review/017/` (ảnh xem nhanh, file kiểm);
- `docs/codex-queue/017-report.md` (báo cáo).

**Cấm:**
- Ghi đè hay xóa bất kỳ file nào có sẵn. Công cụ `tools/art-normalize` đã chặn ghi đè; với `magick`, luôn ghi ra tên mới.
- Chạy git, sửa mã game, sửa `ART_FIX_QUEUE.md`, `ART_REPLACE_LATER.md`, `IMAGE_AUDIT_*.md` (Claude cập nhật sau khi duyệt).
- Tạo ảnh bằng AI, tải gì từ mạng.
- Đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`), Space, `typing-game-handoff-*`.

## Chuẩn bị

1. `export ART_MAGICK=/opt/homebrew/bin/magick`. Đọc `tools/art-normalize/README.md` §1 và phần lệnh của `key-alpha`, `pad-margin`, `flat-bg`, `icon`.
2. **Ghi md5 trước khi làm:** `md5 -r` của mọi ảnh nguồn ở cột "Nguồn" vào `games/dragon-hold/art-src/_review/017/md5-before.txt` (cả 14 dòng, ảnh Lời Gọi cũng ghi ở đây).

## Việc

Đọc dòng tương ứng trong `docs/games/ART_FIX_QUEUE.md` (§2 cho C21, §5.1/§5.2 cho các mục khác) trước khi làm từng ảnh. Bảng dưới là tóm tắt; khi lệch, làm theo `ART_FIX_QUEUE.md`.

| # | Mã | Nguồn | Việc | Ra file |
|---|---|---|---|---|
| 1 | C21 Chân dung Mộc Tinh | `games/typing-defense/art-src/portraits/moc-tinh.png` | Cắt khung đầu, tán và ngực (bỏ phần thân dưới), vuông, nền giữ như ảnh chân dung khác trong cùng thư mục (so `draconis.png`, `dai-bang-tinh.png`); mặt phải to rõ ở 64 px. Viền mực: viền tối 2–3 px quanh dáng (magick morphology hoặc edge trên mặt nạ dáng). Vệt mực tím: một nét cọ tím `#6B3FA0`, độ đục 60–80 %, phía sau vai, không đè mặt. | `moc-tinh.crop.png` (1024×1024) |
| 2 | V37 Mỏ Vàng, Lò Đúc Tiền | `games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png` | Tô miệng lò và dòng vàng chảy sang màu than đỏ sẫm, không phát sáng (`#5A1E14` tới `#7A2A18`). Chọn vùng bằng mặt nạ sắc vàng sáng, giới hạn trong hộp quanh miệng lò (ghi tọa độ hộp vào báo cáo). Các phần vàng khác (mái, đồ trang trí) giữ nguyên. | `gold-mine-lo-duc-tien.coal.png` |
| 3 | V18 Bộ cấp Ruộng Lúa L2 | `games/typing-defense/art-src/kits/farm-kit-l2.png` | `key-alpha IN farm-kit-l2.alpha.png --bg '#00FF00' --mode global --fuzz 25%`. Kiểm cỏ góc trước phải còn; viền xanh ngọn bó lúa còn. | `farm-kit-l2.alpha.png` |
| 4 | V69 Hạt Mộc Tinh | `games/typing-defense/art-src/projectiles/seed-drop.png` | `flat-bg IN seed-drop.flat.png --src-bg auto --bg '#00FF00' --size 1024x1024` | `seed-drop.flat.png` |
| 5 | T2 Cỏ xuân B | `games/dragon-hold/art-src/ground/pine-river/grass-b.png` | `magick IN -modulate 100,115,85 grass-b.hue.png`, rồi `magick grass-b.hue.png -virtual-pixel tile -filter Lanczos -distort Resize 1024x1024 grass-b.1024.png`. Ghép xen A/B 2×2 (với `grass-a`, đổi khổ cùng cách) để xem nối. | `grass-b.hue.png`, `grass-b.1024.png` |
| 6 | T3 Rêu dưới tán | `games/dragon-hold/art-src/ground/pine-river/moss.png` | Chỉ đổi khổ 1024 như T2. Không chỉnh tương phản. | `moss.1024.png` |
| 7 | T7 Đá rêu dốc | `games/dragon-hold/art-src/ground/pine-river/rock.png` | Chỉ đổi khổ 1024 như T2. | `rock.1024.png` |
| 8 | D4 Decal rêu, vũng nước | `games/dragon-hold/art-src/decals/pine-river/moss-puddles.v1.alpha.png` | Chỉ vùng rêu (mặt nạ sắc vàng lục): giảm sáng khoảng 10 %, xoay sắc về xanh đậm. Xóa các px tím hồng lẻ (đặt alpha 0 hoặc tô màu rêu kề). Giữ kênh alpha. | `moss-puddles.v1.tone.png` |
| 9 | D2 Decal cụm hoa | `games/dragon-hold/art-src/_review/015-flower-clusters.png` | `key-alpha IN flower-clusters.015.alpha.png --bg '#0000FF' --despill protect-interior`, rồi `pad-margin … flower-clusters.015.1024.png --size 1024 --margin 9.375% --grid 2x2`. Kiểm đường chia 2×2 trống, màu tím của hoa còn nguyên. | trong `games/dragon-hold/art-src/decals/pine-river/`: `flower-clusters.015.alpha.png`, `flower-clusters.015.1024.png` |
| 10 | D3 Decal sỏi, lá, kim thông | `games/dragon-hold/art-src/decals/pine-river/forest-litter.alpha.png` | Xóa khoảng 34 px xanh lá còn trên sỏi (tô xám sỏi kề bên, hoặc hạ alpha về 0 nếu ở mép). Ghi số px đã đổi. | `forest-litter.clean.png` |
| 11 | I08 Icon Vảy Cứng | `games/dragon-hold/art-src/ui/icons/hard-scale.png` | `-modulate 115,105,104` chỉ trên vùng đỏ cam sáng (mặt nạ sắc, giữ viền nâu), ra `hard-scale.warm.png`. Rồi `icon hard-scale.warm.png games/dragon-hold/art-src/icons/normalized --sizes 256,64`. | `hard-scale.warm.png`, `icons/normalized/hard-scale.warm.256.png`, `.64.png` |
| 12 | I11 Icon Long Hống | `games/dragon-hold/art-src/_review/015-skill-roar.png` | `icon IN games/dragon-hold/art-src/icons/normalized --sizes 256,64` | `icons/normalized/015-skill-roar.256.png`, `.64.png` |
| 13 | U2 Icon Tháp Cung | `games/typing-defense/art-src/ui/buildings/archer.png` | `key-alpha IN archer.alpha.png --bg auto`; `pad-margin archer.alpha.png archer.1024.png --size 1024 --margin 10%`; chỉnh màu cờ về `#D9479B` bằng mặt nạ vùng cờ, ra `archer.flag.png`. | `archer.alpha.png`, `archer.1024.png`, `archer.flag.png` |
| 14 | U4 Icon nhà Trại Lính | `games/typing-defense/art-src/ui/buildings/barracks.png` | Cắt sát vật (trim theo nền) trước khi đệm vuông, ra `barracks.trim.png`; rồi `icon barracks.trim.png games/typing-defense/art-src/ui/buildings/normalized --sizes 256,64`. | `barracks.trim.png`, `ui/buildings/normalized/barracks.trim.256.png`, `.64.png` |

Mỗi ảnh tạo **một lần**. Nếu kết quả hỏng rõ (mất vật, nền sót lớn, cắt mất thân) thì sửa tham số và làm lại tối đa một lần nữa, ghi cả hai lần vào báo cáo. Không nhận kết quả nào mà mắt thấy còn lỗi; khi bí, ghi "không đạt" kèm lý do thay vì cố.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **Ảnh nguồn không đổi:** ghi `md5-after.txt` cùng cách, rồi `diff md5-before.txt md5-after.txt` phải rỗng.
2. **Không ghi đè:** liệt kê mọi file mới tạo (`find games/*/art-src -newer games/dragon-hold/art-src/_review/017/md5-before.txt -type f`). Mọi file trong danh sách phải nằm trong cột "Ra file" hoặc `_review/017*`. File lạ thì xóa và ghi lại.
3. **Khổ và kênh:** `magick identify -format '%f %wx%h %[channels]\n'` cho mọi file ra. Tile T2, T3, T7: đúng 1024×1024. Ảnh có tách nền (V18, D2, U2, U4): có alpha, bốn góc alpha = 0.
4. **Tile liền mép (T2, T3, T7):** `bash tools/art-normalize/seam-check.sh <file 1024> <file>.seam.png --axis xy --reference <nguồn>`, ghi số MAE mép trước và sau.
5. **Màu đích:** C21 (màu vệt mực), V37 (màu trung bình vùng lò sau khi tô, ≤ độ sáng 35 %), I08 (màu trung bình vùng cam sau chỉnh, so `#E58A5F`), U2 (màu cờ, so `#D9479B`): đo bằng `magick … -format '%[fx:mean.r*255],…' info:` trên vùng đã chọn, ghi số.
6. **Ảnh xem nhanh:** mỗi game một tờ `_review/017-dh.jpg` và `_review/017-td.jpg`. Mỗi hàng: nguồn | kết quả | kết quả ở cỡ game (icon 64 px và 32 px, tile ghép 2×2, decal trên nền cỏ `grass-a.png`). Có nhãn mã ở mỗi hàng (font `/System/Library/Fonts/Supplemental/Arial.ttf`). Tự xem kỹ cả hai tờ trước khi viết báo cáo.

## Báo cáo `docs/codex-queue/017-report.md`

Bảng: `| # | Mã | Lệnh đã chạy (đủ tham số) | Ra file | Số kiểm (mục 3–5) | Tự chấm /10 theo ART_ACCEPTANCE.md | Còn thiếu gì |`. Thêm kết quả kiểm mục 1 và 2 (dán đầu ra), và mọi chỗ lệch so với `ART_FIX_QUEUE.md`.

**Xong khi:** 14 dòng đều có file ra và số kiểm, hoặc ghi "không đạt" kèm lý do; mục 1 và 2 sạch. Claude duyệt, chấm lại, rồi mới thay ảnh dùng trong game và cập nhật các danh sách.
