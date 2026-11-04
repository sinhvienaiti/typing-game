# Báo cáo phiếu 273 · Tu Tiên · Atlas RGBA và mặt nạ A/B

**Trạng thái: dừng ở mục 3 / B.R theo lệnh của phiếu.** Đã tạo atlas RGBA thẳng và maskA; kiểm số của mục 1–2 đạt đủ 24 ô. Chưa có bộ ứng viên hoàn chỉnh, chưa nối lab. Không tự chọn cách khác cho hai yêu cầu B.R không đồng thời thỏa mãn trên dữ liệu hiện tại.

Thực hiện một làn theo lời giải Claude đã chốt, áp dụng skill `agent-orchestration`; không mở lại vòng thiết kế, không sinh ảnh bằng AI, không dùng subagent. Tất cả đường ghi qua `/Volumes/SS990TPRO/htdocs/typing-game`.

## 1. Điểm dừng cần Claude chốt

Mục 3 vừa yêu cầu **«Mọi ô dùng cùng một B.R»**, vừa yêu cầu **«Ngoài vỏ: 1»**. Vỏ thực tế thay đổi theo ô, dù đường tâm được giữ cố định. Nếu ghi 1 ngoài từng vỏ thì B.R khác nhau giữa các ô; nếu giữ B.R giống nhau thì có điểm ngoài vỏ không bằng 1. Chọn vỏ chung hoặc bỏ yêu cầu giống nhau đều là đổi lời giải, nên chưa thực hiện.

Ví dụ rõ cả khi xét vỏ mềm: tại tọa độ **(86, 141)** trong ô 384, **A.R(k00) = 255**, **A.R(k23) = 0**. Giá trị B.R theo đường tâm sau Gauss σ 1 ở đây là **0.378463368** (khoảng 97 byte), nhưng ngoài vỏ k23 phải bằng **1 = 255 byte**. Có **453 điểm** A.R(k00)=255 / A.R(k23)=0 với B.R < 0,95; tổng số điểm trong vỏ nhị phân k00, ngoài k23 và B.R < 0,95 là **4357**. Vỏ nhị phân k00 và k23 khác nhau ở **4770 điểm**.

Bằng chứng đầy đủ: `.local/codex-runs/273-out/maskB-constraint-check.json`, đồng thời nằm trong `reveal_constraint_check` của `masks.json`. Không tạo maskB giả hoặc bản ghép CPU dựa trên một cách hiểu tự chọn. Công cụ trả mã thoát **2 có chủ đích** và lưu `status: stopped`, `stopped_at: 3 / B.R`.

## 2. Đã tạo gì

Trong `tools/vfx-masks/`:

- `impact_masks.py`: tách RGBA, loang màu bằng EDT, giải mã f053–f120, tạo đủ bốn kênh maskA, in bảng 24 ô, kiểm xung đột B.R và lưu hồ sơ phần đã làm.
- `README.md`: cách chạy, công thức, quy ước số đo và điểm dừng.

Trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`:

- `fire-impact-k1-r2-v1a.a4.rgba.png` — 2304 × 1536, RGBA thẳng 8 bit.
- `fire-impact-k1-r2-v1a.a4.maskA.png` — cùng lưới, bốn kênh tuyến tính theo phiếu.
- `fire-impact-k1-r2-v1a.a4.masks.json` — tham số, hạt giống, đường nguồn và MD5, số đo 24 ô, phiên bản thư viện, trạng thái **chưa hoàn tất** và lý do dừng.

Trong `.local/codex-runs/273-out/`: `ABOUT.md`, `generate.log`, `measurements.json`, `verification.json`, `maskB-constraint-check.json`, tấm `channels-partial.png`, ảnh chụp trạng thái Git dạng văn bản trước/sau và phần so sánh. Tấm kênh đã được mở xem: đủ sáu cột k00/04/08/12/16/20, hàng B.R ghi rõ `NOT GENERATED`. Hàng RGBA chỉ là alpha-over sRGB để kiểm kênh, **không phải** phép ghép CPU tuyến tính được yêu cầu ở mục 5.

Chưa tạo `maskB.png`, `preview-masked.ts`, `preview-ticks.png`, `channels-k00-k23.png` vì các việc đó nằm sau điểm dừng. Không tạo tệp trong thư mục review ngoài phạm vi; Claude chuyển tấm cần giữ theo phiếu, thêm ABOUT và cập nhật index ở đó.

## 3. Lệnh và kiểm số

Lệnh thực chạy, từ gốc repo cha:

```sh
UV_CACHE_DIR=/Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/273-out/uv-cache \
PYTHONDONTWRITEBYTECODE=1 ART_MAGICK=/opt/homebrew/bin/magick \
uv run --offline --no-project --with numpy --with scipy --with pillow \
python3 tools/vfx-masks/impact_masks.py
```

Python 3.9.6, NumPy 2.0.2, SciPy 1.13.1, Pillow 11.3.0. Cache uv mặc định bị sandbox chặn khi tạo khóa (`Operation not permitted`); đã sao chép cache có sẵn vào thư mục đầu ra được phép ghi, dùng `UV_CACHE_DIR` như trên. Không tải mạng, không cài thêm thư viện. Sau khi kiểm xong đã xóa riêng bản sao cache do phiếu này tạo; cache gốc giữ nguyên.

Đã đọc đúng cách tạo atlas ở `…/impact-k1-r2/tools/a4clip.py`: ImageMagick `-colorspace sRGB -alpha off -filter Lanczos -resize 384x384! -depth 8 rgb:-`, rồi đặt viền 2 px về 0. Giải mã clip bằng ffmpeg ở cỡ gốc; không đổi fps, không crop hoặc ngưỡng hóa trước phép tính alpha. **RGB của f053–f076 sau đổi cỡ trùng từng byte với 24 ô atlas nguồn.** Chuỗi dùng tính tuổi sống có đủ 68 khung f053–f120.

| Kiểm bắt buộc | Kết quả |
| --- | --- |
| 1 · Dựng ngược RGB trên mọi điểm có alpha | **Đạt:** sai số lớn nhất 0 byte; **0 điểm vượt 1 mức**. Alpha ra trùng max RGB nguồn. |
| 2 · Vạch nóng, khe mực, gốc sống lâu hơn mũi | **Đạt 24/24 ô**, bảng dưới. |
| 3 · B.R ở gốc và ba mũi | **Chưa kiểm:** chưa tạo B.R vì xung đột mục 3. |
| 4 · Viền mọi kênh bằng 0 | **Đạt ở atlas nguồn, RGBA, maskA:** 0 giá trị khác 0 trên toàn bộ 24 viền. Chưa đủ bốn PNG vì thiếu maskB. |
| 5 · Điểm sáng tick 42 < 2% tick 9 | **Chưa chạy:** thiếu maskB, chưa ghép CPU. Không có hai số để báo. |
| 6 · Phạm vi tệp / Git | Phần ghi của phiếu nằm trong các đường được phép; repo có thay đổi sẵn và một thay đổi đồng thời của làn khác, chi tiết §5. |

Ngưỡng nhiễu mực cố định **0,35221400215267545**, nằm trong giao khoảng khả thi của cả 24 ô `[0,3432829720993641; 0,3646434556890935]`. Không đổi ngưỡng theo khung. Tất cả phép lọc chạy riêng từng ô; viền được đặt về 0 sau xử lý.

Vỏ nhị phân dùng A.R > 0,5. Diện tích vạch nóng/mực mềm được đo bằng **tổng giá trị kênh byte/255**, không đếm mọi điểm khác 0 sau Gaussian. JSON ghi thêm số điểm nóng đã chọn, điểm khác 0 và điểm > 0,5. Tâm cong tính qua ba đỉnh liên tiếp rồi nội suy theo đoạn; hai đầu dùng bộ ba đầu/cuối. Không có bộ ba suy biến. Phép sống sót đếm cả khung hiện tại tới trước khung tắt đầu tiên; điểm sáng lại sau đó không cộng thêm tuổi. EDT chia phân vị 99, trộn 75/25 và kẹp khi ghi byte.

Khoảng cách mép–đường tâm là trung bình khoảng cách Euclid từ mép vỏ nhị phân đến nét gần nhất, đơn vị px ở 384; bao gồm nửa độ dày nét, không nên đọc thành độ trượt của nét.

| k | Sáng px | Vỏ px | Mực px hiệu dụng | Khe mực % | Nóng/sáng % | A.A gốc | A.A mũi | Mép–tâm px |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 13168 | 17593 | 5014.23 | 23.108 | 4.005 | 0.5491 | 0.0944 | 11.955 |
| 01 | 12959 | 17478 | 4992.60 | 23.103 | 4.000 | 0.5496 | 0.0923 | 11.912 |
| 02 | 12899 | 17394 | 4970.73 | 23.335 | 4.002 | 0.5489 | 0.0907 | 11.878 |
| 03 | 12706 | 17247 | 4924.77 | 23.743 | 3.999 | 0.5518 | 0.0889 | 11.781 |
| 04 | 12592 | 17153 | 4908.73 | 24.049 | 4.004 | 0.5500 | 0.0860 | 11.752 |
| 05 | 12358 | 16995 | 4932.25 | 24.260 | 3.998 | 0.5511 | 0.0842 | 11.708 |
| 06 | 12280 | 16949 | 4909.87 | 24.747 | 3.999 | 0.5509 | 0.0834 | 11.727 |
| 07 | 12106 | 16812 | 4871.67 | 25.470 | 3.997 | 0.5484 | 0.0837 | 11.643 |
| 08 | 11903 | 16636 | 4836.05 | 25.805 | 3.999 | 0.5506 | 0.0854 | 11.593 |
| 09 | 11570 | 16319 | 4809.45 | 25.870 | 4.001 | 0.5513 | 0.0880 | 11.578 |
| 10 | 11457 | 16140 | 4785.56 | 25.886 | 3.997 | 0.5490 | 0.0893 | 11.632 |
| 11 | 11254 | 15901 | 4720.65 | 25.848 | 3.998 | 0.5504 | 0.0907 | 11.690 |
| 12 | 11018 | 15594 | 4698.72 | 24.708 | 4.003 | 0.5526 | 0.1014 | 11.861 |
| 13 | 10800 | 15393 | 4533.96 | 25.697 | 4.001 | 0.5551 | 0.1098 | 12.056 |
| 14 | 10635 | 15265 | 4473.37 | 25.764 | 3.995 | 0.5593 | 0.1190 | 12.115 |
| 15 | 10432 | 15101 | 4505.83 | 25.685 | 3.997 | 0.5621 | 0.1149 | 12.030 |
| 16 | 10291 | 15020 | 4379.54 | 26.139 | 4.002 | 0.5635 | 0.1126 | 12.036 |
| 17 | 9999 | 14826 | 4469.75 | 26.162 | 3.999 | 0.5645 | 0.1087 | 11.728 |
| 18 | 9882 | 14737 | 4528.25 | 26.062 | 3.996 | 0.5631 | 0.1071 | 11.634 |
| 19 | 9664 | 14514 | 4597.64 | 25.963 | 4.002 | 0.5629 | 0.1048 | 11.325 |
| 20 | 9344 | 14077 | 4747.15 | 25.287 | 4.000 | 0.5651 | 0.1015 | 11.081 |
| 21 | 8984 | 13661 | 4813.01 | 24.813 | 3.995 | 0.5640 | 0.0931 | 10.797 |
| 22 | 8851 | 13348 | 4794.62 | 24.290 | 3.999 | 0.5639 | 0.0906 | 10.707 |
| 23 | 8662 | 13091 | 4763.43 | 24.589 | 3.992 | 0.5620 | 0.0897 | 10.617 |

Đã đọc lại PNG để kiểm độc lập: dựng ngược, alpha, kích thước, viền, băm nguồn và các điều kiện 24 ô; kết quả ở `verification.json`. Kiểm cú pháp Python bằng `compile` trong bộ nhớ đạt, không tạo `.pyc`. Không chạy build hoặc bộ test của game.

## 4. Nguồn giữ nguyên

| Nguồn | MD5 |
| --- | --- |
| `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4.atlas.png` | `9f8ccff0541ae6648f6d9a45e6b729a9` |
| `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4-run2.mp4` | `2b7b3e7ed2b0d9866a5db41b56813021` |
| `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/a4/cells/atlas.meta.json` | `3f83a5ade626e7b65e7bbebbc8984b08` |
| `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/measure/v1a.try3.strokes.json` | `3b2c4910b26de209e4bdc74f626978e3` |

MD5 trước/sau của các nguồn trên trùng nhau. `masks.json` còn ghi MD5 công cụ và `a4clip.py` dùng đối chiếu. Không sửa hoặc xóa ảnh, clip, prompt hay metadata nguồn có sẵn.

## 5. Phạm vi, phần bỏ qua và bàn giao

Đã lưu `git status --short` trước/sau ở repo cha và submodule Tu Tiên. Trạng thái submodule **không đổi** so với lúc bắt đầu; media mới bị Git bỏ qua đúng cấu trúc repo. Repo cha có nhiều thay đổi từ trước. Trong lúc chạy, `docs/codex-queue/269-tt-lab-sound-tiers.md` được làn khác thay đổi; phiếu 273 không ghi vào tệp đó. Phần mới do phiếu 273 hiện trong status là `tools/vfx-masks/` và báo cáo này. `.local` bị bỏ qua; các tệp media được liệt kê bằng `ls -la` trong `art-files-ls.txt`, có dòng báo thiếu maskB đúng trạng thái dừng.

Không sửa mã game, manifest, script hoặc test của Tu Tiên; không đụng các làn audio hay tài liệu game. Không chạy lệnh Git ghi dữ liệu, dev server, trình duyệt, bộ sinh ảnh hoặc công cụ âm thanh. Không có hạn mức gây dừng; nguyên nhân là ràng buộc ở mục 3.

**Claude cần chốt trước khi tiếp tục:** «ngoài vỏ» của B.R dùng vỏ chung nào để giữ mọi ô giống nhau, hoặc xác nhận B.R được phép khác nhau ở phần ngoài vỏ từng ô. Sau quyết định đó mới tạo maskB, công cụ/bản ghép CPU, chạy đủ kiểm 3–5 và gửi tấm hoàn chỉnh cho anh. Các tệp hiện tại được giữ nguyên để tiếp tục từ phần đã làm; chưa dùng để nối lab ở phiếu 264.
