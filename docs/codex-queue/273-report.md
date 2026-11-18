# Báo cáo phiếu 273 · Tu Tiên · Atlas RGBA và mặt nạ A/B

**Trạng thái: hoàn tất bộ ứng viên và kiểm số; chờ anh xem, chưa nối lab.** Đã tiếp tục theo quyết định Claude lúc **21:03 ngày 04/11/2026**, tạo maskB dùng chung trên hợp vỏ U, cập nhật JSON và tạo đủ hai tấm xem trước. RGBA, maskA, phần số đo và tham số mục 1–2 được giữ nguyên từ lần chạy đã đạt.

Thực thi một làn theo lời giải đã chốt và skill `agent-orchestration`; không mở lại thiết kế, không dùng subagent hoặc AI tạo ảnh. Mọi đường ghi qua `/Volumes/SS990TPRO/htdocs/typing-game`.

## 1. Tệp bàn giao

Trong `tools/vfx-masks/`:

- `impact_masks.py`: tiếp tục từ mục 1–2; kiểm lại PNG và hồ sơ cũ, tính B.R một lần trên U, kiểm gốc/mũi, viền và lưu maskB. `--force` chỉ áp dụng cho JSON và kết quả trong `273-out`; không ghi đè PNG art-src.
- `preview-masked.ts`: nhập trực tiếp các hàm CPU của game và dùng look/lịch mặc định để ghép 11 tick. Không chép lại công thức bộ ghép.
- `README.md`: cách chạy offline, quy tắc giữ sản phẩm cũ, cách tính U và quy ước kiểm số.

Trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`:

- `fire-impact-k1-r2-v1a.a4.rgba.png` và `fire-impact-k1-r2-v1a.a4.maskA.png`: **không ghi lại**; MD5 và thời gian sửa trùng trước/sau lượt tiếp tục.
- `fire-impact-k1-r2-v1a.a4.maskB.png`: mới, RGBA 8 bit 2304 × 1536, cùng map B.R trong 24 ô.
- `fire-impact-k1-r2-v1a.a4.masks.json`: cập nhật phần B, kiểm và xem trước; trạng thái `candidate_complete_awaiting_owner_review`. Các phần `cells`, `noise`, `reconstruction`, `decode`, `geometry`, tham số A và mô tả đầu ra RGBA/maskA giữ nguyên.

Trong `.local/codex-runs/273-out/`:

- `preview-ticks.png`: 4224 × 412, 11 ô liền nhau, nhãn Tick tiếng Anh.
- `channels-k00-k23.png`: 1666 × 1564, sáu cột k00/04/08/12/16/20 và sáu hàng RGBA, A.R, A.G, A.B, A.A, B.R.
- `measurements.json`, `preview-measurements.json`, `verification.json`, `final-verification.json`, `resume-generate.log`, `preview.log`, ảnh chụp trạng thái Git dạng văn bản, bản JSON trước tiếp tục và MD5/thời gian sửa trước/sau.

Đã mở xem hai tấm hoàn chỉnh để kiểm bố cục, nhãn và nội dung kênh. Không tuyên bố nghiệm thu mỹ thuật. `channels-partial.png` và `maskB-constraint-check.json` là lịch sử lần dừng trước; dùng hai tấm tên hoàn chỉnh ở trên để xem kết quả cuối.

## 2. Cách tiếp tục và xem trước

B.R dùng đúng quyết định mới: `U = dilate(max_k(A.R_k) > 0,5, 2 px)`, lấy từ A.R PNG đã lưu; U có **22483 điểm**. Trong U dùng quãng đường dọc nét gần nhất chia chiều dài nét đó; không cắt điểm cách tâm >40 px. Ngoài U đặt 1; Gauss σ 1 có nền ngoài bằng 1, sau lọc đặt lại ngoài U bằng 1; cuối cùng viền 2 px mọi kênh về 0. B.G/B.B bằng 0, B.A bằng 255 trong ô. Cùng byte map được đóng vào cả 24 ô. Kiểm đầu mút lấy mẫu song tuyến tính tại tọa độ gốc/mũi đã đổi từ 1080 xuống 384.

CPU dùng `composeFlipbookMasked`, `blendPremultiplied`, `flipbookControl`, `FLIPBOOK_TIMING`, `FLIPBOOK_MASKED_LOOK`, `srgbToLinear` nhập từ đường game chính. Với mỗi tick, dùng `vFrame=tick*24/60`, f0/f1 kế tiếp không vòng và w phần lẻ; ctl lấy đúng đời 43/60 s, cool=erode=0, lịch `impact-key1`. Atlas chuyển sRGB sang tuyến tính trước ghép; mask chia byte/255; tint 1, soft 1; nền đá tối `#2a2c30` tuyến tính. HDR >1 kẹp trước mã hóa sRGB 8 bit để xem, không bloom.

Hàng RGBA của tấm kênh dùng alpha-over sRGB để xem dữ liệu, không phải bản ghép CPU. Lệch mép–tâm trong bảng là khoảng cách từ mép vỏ tới tâm gần nhất ở cỡ 384; có nửa độ dày nét, không phải phép đo độ trượt.

Lệnh đã chạy:

```sh
UV_CACHE_DIR=/Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/273-out/uv-cache \
PYTHONDONTWRITEBYTECODE=1 ART_MAGICK=/opt/homebrew/bin/magick \
uv run --offline --no-project --with numpy --with scipy --with pillow \
python3 tools/vfx-masks/impact_masks.py --force

ART_MAGICK=/opt/homebrew/bin/magick node --import ./games/immortality-cultivation/node_modules/tsx/dist/loader.mjs tools/vfx-masks/preview-masked.ts --force
```

Lệnh `node --import tsx ... --force` ở gốc repo báo `ERR_MODULE_NOT_FOUND` vì gốc không có liên kết tsx; đã dùng trực tiếp loader có sẵn trong game như cách báo cáo 259. Không cài gói hoặc sửa liên kết. Log lỗi đầu ở `preview-default-loader.log`; lệnh loader trực tiếp chạy thành công.

Python 3.9.6, NumPy 2.0.2, SciPy 1.13.1, Pillow 11.3.0. Cache uv mặc định bị sandbox chặn khóa như lần trước; dùng bản sao trong `273-out/uv-cache`. Bản sao `environments-v2` cần bỏ để uv tạo môi trường sạch, tránh lỗi rename thư mục sau khi sao chép cache. Chỉ dùng ba gói đã có offline; không tải mạng. Đã xóa riêng bản sao cache sau khi kiểm xong, không sửa cache gốc.

## 3. Kiểm bắt buộc

| Kiểm | Kết quả |
| --- | --- |
| 1 · Dựng ngược RGB | **Đạt:** sai số lớn nhất **0 mức**, **0 điểm vượt 1 mức**; alpha PNG bằng max RGB nguồn. |
| 2 · Nóng/sáng, khe mực, gốc sống lâu hơn mũi | **Đạt đủ 24/24 ô**, đọc lại PNG và đối chiếu số đo cũ; bảng bên dưới. |
| 3 · B.R gốc ≤0,05; ba mũi ≥0,95 | **Đạt:** gốc **0,002440087**; mũi lần lượt **0,999372549 / 0,997133866 / 0,996078431**. |
| 4 · Viền 2 px mọi kênh | **Đạt:** 0 giá trị khác 0 trên mọi ô của atlas nguồn, RGBA, maskA và maskB. |
| 5 · Điểm sáng tick 42 <2% tick 9 | **Đạt trên PNG cuối:** tick 9 **10379**, tick 42 **0**, tỉ lệ **0%**. |
| 6 · Phạm vi Git và bốn tệp art-src | Chỉ ghi các đường cho phép; đối chiếu trạng thái trước/sau và `ls -la` được lưu trong `273-out`, xem §5. |

Độ sáng là Rec.709 tuyến tính >0,1, loại toàn bộ dải nhãn. Số trước làm tròn byte CPU là **10384 / 0**; số đọc lại PNG là **10379 / 0**. Chênh 5 điểm ở ngưỡng do lượng tử hóa sRGB 8 bit. Cả hai phép đo đều đạt. Đã kiểm byte đọc bằng ImageMagick của cả RGBA, maskA và maskB trùng hoàn toàn với Pillow; không có đổi màu hoặc premultiply ngầm trong đầu vào xem trước.

Kiểm cuối đọc lại PNG xác nhận B.R chung, ngoài U bằng 1 (trừ viền 0), G/B bằng 0, A bằng 255 trong ô; đối chiếu MD5 nguồn và mã CPU game; kiểm cú pháp Python trong bộ nhớ. Toàn bộ cờ trong `final-verification.json` đạt. Không chạy build hoặc bộ test game.

| k | Sáng px | Vỏ px | Mực px hiệu dụng | Khe mực % | Nóng/sáng % | A.A gốc | A.A mũi | Mép–tâm px | Kiểm 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 13168 | 17593 | 5014.23 | 23.108 | 4.005 | 0.5491 | 0.0944 | 11.955 | Đạt |
| 01 | 12959 | 17478 | 4992.60 | 23.103 | 4.000 | 0.5496 | 0.0923 | 11.912 | Đạt |
| 02 | 12899 | 17394 | 4970.73 | 23.335 | 4.002 | 0.5489 | 0.0907 | 11.878 | Đạt |
| 03 | 12706 | 17247 | 4924.77 | 23.743 | 3.999 | 0.5518 | 0.0889 | 11.781 | Đạt |
| 04 | 12592 | 17153 | 4908.73 | 24.049 | 4.004 | 0.5500 | 0.0860 | 11.752 | Đạt |
| 05 | 12358 | 16995 | 4932.25 | 24.260 | 3.998 | 0.5511 | 0.0842 | 11.708 | Đạt |
| 06 | 12280 | 16949 | 4909.87 | 24.747 | 3.999 | 0.5509 | 0.0834 | 11.727 | Đạt |
| 07 | 12106 | 16812 | 4871.67 | 25.470 | 3.997 | 0.5484 | 0.0837 | 11.643 | Đạt |
| 08 | 11903 | 16636 | 4836.05 | 25.805 | 3.999 | 0.5506 | 0.0854 | 11.593 | Đạt |
| 09 | 11570 | 16319 | 4809.45 | 25.870 | 4.001 | 0.5513 | 0.0880 | 11.578 | Đạt |
| 10 | 11457 | 16140 | 4785.56 | 25.886 | 3.997 | 0.5490 | 0.0893 | 11.632 | Đạt |
| 11 | 11254 | 15901 | 4720.65 | 25.848 | 3.998 | 0.5504 | 0.0907 | 11.690 | Đạt |
| 12 | 11018 | 15594 | 4698.72 | 24.708 | 4.003 | 0.5526 | 0.1014 | 11.861 | Đạt |
| 13 | 10800 | 15393 | 4533.96 | 25.697 | 4.001 | 0.5551 | 0.1098 | 12.056 | Đạt |
| 14 | 10635 | 15265 | 4473.37 | 25.764 | 3.995 | 0.5593 | 0.1190 | 12.115 | Đạt |
| 15 | 10432 | 15101 | 4505.83 | 25.685 | 3.997 | 0.5621 | 0.1149 | 12.030 | Đạt |
| 16 | 10291 | 15020 | 4379.54 | 26.139 | 4.002 | 0.5635 | 0.1126 | 12.036 | Đạt |
| 17 | 9999 | 14826 | 4469.75 | 26.162 | 3.999 | 0.5645 | 0.1087 | 11.728 | Đạt |
| 18 | 9882 | 14737 | 4528.25 | 26.062 | 3.996 | 0.5631 | 0.1071 | 11.634 | Đạt |
| 19 | 9664 | 14514 | 4597.64 | 25.963 | 4.002 | 0.5629 | 0.1048 | 11.325 | Đạt |
| 20 | 9344 | 14077 | 4747.15 | 25.287 | 4.000 | 0.5651 | 0.1015 | 11.081 | Đạt |
| 21 | 8984 | 13661 | 4813.01 | 24.813 | 3.995 | 0.5640 | 0.0931 | 10.797 | Đạt |
| 22 | 8851 | 13348 | 4794.62 | 24.290 | 3.999 | 0.5639 | 0.0906 | 10.707 | Đạt |
| 23 | 8662 | 13091 | 4763.43 | 24.589 | 3.992 | 0.5620 | 0.0897 | 10.617 | Đạt |

## 4. Băm dữ liệu

Nguồn giữ nguyên:

| Nguồn | MD5 |
| --- | --- |
| `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4.atlas.png` | `9f8ccff0541ae6648f6d9a45e6b729a9` |
| `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4-run2.mp4` | `2b7b3e7ed2b0d9866a5db41b56813021` |
| `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/a4/cells/atlas.meta.json` | `3f83a5ade626e7b65e7bbebbc8984b08` |
| `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/measure/v1a.try3.strokes.json` | `3b2c4910b26de209e4bdc74f626978e3` |

Ba PNG đầu ra:

| Tệp | MD5 |
| --- | --- |
| `fire-impact-k1-r2-v1a.a4.rgba.png` | `9c2e2446eaffd655b7424fd2a5798240` |
| `fire-impact-k1-r2-v1a.a4.maskA.png` | `d900551e350f09352bc4265ea75b0b9a` |
| `fire-impact-k1-r2-v1a.a4.maskB.png` | `a82cd18bca3033cf94490c562602fec8` |

`masks.json` giữ `sources.builder` làm băm lịch sử công cụ lần đầu; `continuation.builder` là băm công cụ tiếp tục. Không dùng băm công cụ cũ để khẳng định nguồn ảnh bị đổi. Băm mã game CPU và công cụ TS nằm trong `preview`.

## 5. Phạm vi và phần bàn giao cho Claude

Không tái tạo RGBA hoặc maskA theo lệnh chạy lại. Không sửa hoặc xóa atlas, clip, ảnh, prompt, metadata nguồn có sẵn. Không sửa mã game, manifest, script/test hoặc docs Tu Tiên. Không chạy Git ghi dữ liệu, build/test game, mở cổng, trình duyệt, dev server, AI tạo ảnh hay âm thanh.

Không chuyển ảnh sang thư mục review vì ngoài phạm vi ghi của phiếu; Claude chuyển `preview-ticks.png` và `channels-k00-k23.png` sang `typing-game-review/captures/tu-tien/impact-k1-r2/masks/`, thêm ABOUT/cập nhật index và gửi anh. **Anh cần xem hai tấm này.** Chưa nối lab: phiếu 264 làm việc đó sau khi anh duyệt. Đây là ứng viên, không phải nghiệm thu hình trong play host. Không có hạn mức gây dừng hoặc công việc còn thiếu trong phạm vi công cụ.

Đối chiếu trạng thái cuối: repo cha có nhiều thay đổi sẵn trước lượt này; trạng thái submodule Tu Tiên **không đổi**. Các dòng mới trong `git status --short` so với mốc trước tiếp tục: ` M docs/codex-queue/273-report.md`. Danh sách chi tiết các công cụ mới ở `git-status-allowed-paths.txt`; `.local` và media art-src bị Git bỏ qua theo cấu trúc repo, nên bốn tệp được liệt kê riêng bằng `ls -la` ở `art-files-ls.txt`. Phiếu này không ghi các đường ngoài danh sách cho phép.

Bản so sánh cũng ghi nhận dòng `?? docs/codex-queue/259-report.md` không còn ở mốc sau; đó là thay đổi đồng thời ngoài phiếu 273, tệp này chỉ được đọc để tham khảo loader, không được phiếu 273 ghi hoặc xóa.
