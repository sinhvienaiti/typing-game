# Phiếu 328 · Mặt nạ ấn Kim từ tranh

Đã triển khai trong `W = /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-sigils`, nhánh `codex/lab-metal-sigils`, HEAD `1b9461e`. Dùng đúng lời giải đã chốt, không mở thêm vòng thiết kế/phản biện.

Mặc định tải tranh theo từng id; `?sigil=code` giữ đường giải tích. GroundMarks vẫn một lệnh vẽ, chỉ bật tranh khi cả crack và rift tải được. Mặt nạ là dữ liệu RGB, giữ aspect bằng geometry, không đổi scale hoạt ảnh; Kim dùng thân bạc và lõi vàng nhạt. Đường tranh không thêm biRing/cloudCurl; ấn chân và SOLID giữ nguyên.

## Tệp

Đường dẫn dưới đây tính từ W; số dòng theo diff với HEAD, tệp mới tính toàn bộ.

| Tệp | Thêm | Bớt |
| --- | ---: | ---: |
| `src/view/skills/painted-sigils.ts` | 98 | 0 |
| `scripts/vfx/sigil-masks-lib.ts` | 111 | 0 |
| `scripts/vfx/sigil-masks.ts` | 64 | 0 |
| `tests/view/painted-sigils.test.ts` | 221 | 0 |
| `src/view/skills/fxkit.ts` | 68 | 6 |
| `src/view/skills/sword-rain.ts` | 60 | 1 |
| `src/view/skills/sword-skills.ts` | 37 | 0 |
| **Tổng mã và test** | **659** | **7** |

Media mới: `W/art-src/lab/vfx/sigils/metal-{line,arrow,arcs,hex,spiral,crack,rift}.png` và `manifest.json`. Không sửa tranh nguồn, không tạo tranh mới. Báo cáo này (+59/−0 dòng) nằm ở repo cha: `docs/codex-queue/328-report.md`.

## Kiểm tra

| Lệnh/kiểm | Kết quả |
| --- | --- |
| `ART_MAGICK=/opt/homebrew/bin/magick npx tsx scripts/vfx/sigil-masks.ts` | Sandbox chặn socket IPC của tsx: `listen EPERM …/tsx-501/33814.pipe`; script chưa chạy, chưa ghi tệp. |
| `ART_MAGICK=/opt/homebrew/bin/magick node --import tsx scripts/vfx/sigil-masks.ts` | Qua, đủ 7 PNG và manifest; cùng trình nạp tsx, không mở socket IPC. |
| Chạy lại lệnh thay thế trên, không `--force` | Mã 1; MD5, kích thước và mtime của cả 8 tệp không đổi. |
| Chạy lại với `--force` | Mã 0; MD5 cả 7 PNG và manifest giống lần đầu. |
| `npx tsc --noEmit` | Qua, không có lỗi. |
| `ART_MAGICK=/opt/homebrew/bin/magick npx vitest run tests/view/painted-sigils.test.ts --maxWorkers=4` | 1 tệp, 55 test qua, không bỏ qua ảnh thật. |
| `ART_MAGICK=/opt/homebrew/bin/magick VITEST_MAX_THREADS=4 npx vitest run tests/lab tests/view --maxWorkers=4` | 45 tệp, 555 test qua = mốc 500 + 55 mới. |
| `git diff --check`; `git status --short --untracked-files=all` | Sạch lỗi khoảng trắng; chỉ 7 tệp mã/test được phép và hai liên kết có sẵn `art-src`, `node_modules`. |
| Xem trực tiếp cả 7 PNG | Hình đủ, nền đen, không thấy nét chính bị cắt; đối chiếu spiral với tranh gốc xác nhận lật ngang. Màu xanh trong PNG là kênh G dữ liệu quầng, không phải màu hiển thị Kim. |
| Kiểm dữ liệu PNG | Cả 7 có viền 2 px bằng 0 ở mọi kênh; chỉ có chunk IHDR/IDAT/IEND, không gAMA/iCCP. |

Một số test cũ giả lập `location` trong Node nên xuất cảnh báo URL tương đối của manifest; loader bắt lỗi và quay về giải tích, không có test lỗi.

## Bảy mặt nạ

Vùng cắt là `[x,y,w,h]`. GPU MB dùng đúng `W·H·4·4/3 / 10⁶` (RGBA8 và mipmap); aspect ghi 4 số lẻ.

| Id | Vùng cắt | Px | Aspect | hotT | hotShare | MD5 PNG | GPU MB |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| line | −52,305,1775,317 | 2048×512 | 5.5994 | 0.95 | 5.841280% | `70281eb84d95d0b974179e072199ee6d` | 5.5924 |
| arrow | −22,317,1724,297 | 512×128 | 5.8047 | 0.95 | 4.221639% | `577af623f198c34cdc318cd8f735ba68` | 0.3495 |
| arcs | 360,−6,933,933 | 512×512 | 1.0000 | 0.87 | 4.810413% | `121c9d15e4f73c35bd46e26ab02275d5` | 1.3981 |
| hex | 409,28,855,855 | 1024×1024 | 1.0000 | 0.95 | 3.893469% | `26e85f2c1a97cf269afd785fd4f0b1ae` | 5.5924 |
| spiral | 485,94,701,701 | 1024×1024 | 1.0000 | 0.95 | 6.252841% | `2f87eae85213840ffb47aa0e48bb6d01` | 5.5924 |
| crack | 202,4,1264,912 | 1024×1024 | 1.3860 | 0.95 | 4.625501% | `8ccdacf8e63963615e6d66501b78cad1` | 5.5924 |
| rift | 15,371,1643,187 | 2048×256 | 8.7861 | 0.95 | 9.019457% | `04afbfb5ecdcc74a27fd1feac1b1b1c5` | 2.7962 |

Tổng GPU **26.9135 MB ≈ 25.6667 MiB**. Cả 7 hộp sáng, vùng cắt, px và aspect khớp bảng phiếu; chỉ spiral có `flop: true`.

**Cần Claude/anh xem:** line, spiral và rift vượt mục tiêu hotShare 5% dù hotT đã chạm 0.95, vì nguồn còn nhiều điểm gần trắng. Giữ đúng vòng tăng 0.02 và trần 0.95 của phiếu, không tự giảm kênh B. Manifest lưu tỷ lệ dạng số 0–1 và hotT số thực đầy đủ (0.9500000000000002).

Không chạy build, dev server hay trình duyệt theo phạm vi phiếu. Claude cần so A/B trong lab ở mặc định và `?sigil=code`, đặc biệt lõi sáng ba mặt nạ trên, chiều xoắn/kiếm K5 và quá trình rã dần. Chưa kết luận chất lượng hoặc độ giống từng pixel trên GPU. Không dùng lệnh git ghi; không sửa bốn tệp thuộc làn 326.
