# Atlas RGBA và mặt nạ A/B cho đòn lửa phím 1 · Phiếu 273 và 273b

Bộ công cụ xử lý ảnh bằng số theo lời giải đã chốt; không sinh ảnh bằng AI, không sửa mã game hoặc manifest. Phiếu 273 dùng B.R chung theo quyết định Claude lúc **21:03 ngày 04/11/2026**. Phiếu 273b đổi riêng A.A sang hạng phần trăm theo quyết định lúc **21:15**. Bộ hiện tại là **ứng viên chờ xem; chưa đạt toàn bộ kiểm 273b**, chưa nối lab.

## Chạy 273b

Từ `/Volumes/SS990TPRO/htdocs/typing-game`:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
PYTHONDONTWRITEBYTECODE=1 uv run --offline --no-project --with numpy --with scipy --with pillow python3 tools/vfx-masks/impact_masks.py --force --survival-rank
ART_MAGICK=/opt/homebrew/bin/magick node --import ./games/immortality-cultivation/node_modules/tsx/dist/loader.mjs tools/vfx-masks/preview-masked.ts --force
```

Gốc repo không có loader `tsx`; dùng loader đã cài trong game, không cài gói hay sửa liên kết. Python dùng NumPy 2.0.2, SciPy 1.13.1, Pillow 11.3.0 đã có offline. Khi sandbox chặn khóa cache uv mặc định, sao chép cache vào `273-out/uv-cache-273b`, bỏ `environments-v2` trong bản sao, rồi thêm `UV_CACHE_DIR=/Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/273-out/uv-cache-273b` trước lệnh uv. Cache gốc chỉ đọc; xóa riêng bản sao sau khi kiểm xong.

`--survival-rank` đi cùng `--force`. Công cụ kiểm nguồn và MD5 đầu ra, đọc lại kiểm cũ rồi giải mã f053–f120 để tính điểm chưa lượng tử hóa. Trước lần ghi đè đầu tiên, chép nguyên `maskA.png` và `masks.json` sang `maskA.v1.png` và `masks.v1.json`. Bản v1 không bị ghi đè; lần chạy tiếp vẫn lấy v1 làm mốc. Thiếu một trong hai bản v1 hoặc sai MD5 thì dừng. Chỉ A.A của maskA và hồ sơ hiện tại được cập nhật; RGB maskA, RGBA và maskB được kiểm giữ nguyên.

Không có `--survival-rank`, Python giữ đường tiếp tục 273: đọc RGBA/maskA, kiểm lại số đo đã lưu, tính B.R chung; maskB có sẵn phải trùng byte và không bị ghi lại. `--force` đơn lẻ chỉ cho ghi hồ sơ và đầu ra trong `273-out`, không cho tái tạo RGBA/maskA.

## Phiếu 274 · Xem riêng `rampCool` trong worktree

```sh
ART_MAGICK=/opt/homebrew/bin/magick node --import ./games/immortality-cultivation/node_modules/tsx/dist/loader.mjs tools/vfx-masks/preview-masked.ts --force --ramp-cool 1 --out-prefix cool --flipbook games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts
```

`--ramp-cool <số>` mặc định 0, chuyển vào look CPU. `--flipbook <đường dẫn>` nhập động mô-đun của worktree; đường tương đối tính từ gốc repo, mặc định vẫn là game chính. `--out-prefix <tên>` chuyển đầu ra sang `.local/codex-runs/274-out/`, thêm `<tên>-` vào tên tệp và chỉ đọc hồ sơ `masks.json`. Vì vậy lệnh trên tạo `cool-preview-ticks.png`, `cool-preview.mp4`, `cool-preview-area.json`, `cool-preview-measurements.json`, `cool-video-verification.json`, không ghi lại art hoặc đầu ra 273b. Không truyền tiền tố thì giữ đường xuất và hành vi cập nhật hồ sơ của 273b.

Đo màu trung bình sRGB 8 bit tại tick 30 và 36 trên chính các điểm có độ sáng tuyến tính >0,1, trước nhãn. Nếu không còn điểm vượt ngưỡng, ghi `null`, không thay bằng màu 0. Ghi thêm số điểm còn alpha >0 và màu trung bình tương ứng để phân biệt vùng còn sống với vùng vượt ngưỡng sáng. Giữ nguyên các ngưỡng kiểm 273b và giữ đầu ra nếu kiểm thất bại. Hệ số làm nguội không đổi alpha, nhưng đổi màu có thể đổi diện tích vượt ngưỡng độ sáng; không dùng hai diện tích này thay cho nhau.

**Kết quả 274:** mã đúng công thức đã chốt nhưng preview chưa đạt màu than đỏ. Với `rampCool = 1`, tick 12 = 0,561922; từ tick 17 trở đi không còn điểm vượt ngưỡng sáng, nên tick 18 không đạt dải kiểm cũ. Tick 30/36 còn 1.105/547 điểm alpha >0, màu trung bình sRGB lần lượt `[44,91; 42,61; 44,03]` và `[43,16; 43,52; 46,51]`; đỏ chưa trội rõ. `fbRamp` hiện trả màu `soot = [0.03, 0.022, 0.02]` khi r dưới 0,23. Không đổi ramp, soot, lịch hoặc ngưỡng để ép đạt. Bản đối chứng `--ramp-cool 0 --out-prefix baseline` khớp nguyên chuỗi diện tích và mọi điểm ảnh tấm tick 273b; số điểm alpha >0 khớp bản cool ở cả 43 tick. Chi tiết: `docs/codex-queue/274-report.md` và `.local/codex-runs/274-out/preview-comparison.json`.

## Công thức

Mọi phép tính theo ô 384 × 384; atlas 6 cột × 4 hàng, thứ tự hàng trước. Viền 2 px mọi kênh bằng 0. RGBA là sRGB với alpha thẳng; mặt nạ là dữ liệu tuyến tính, NoColorSpace.

Các kênh từ 273:

- RGBA: alpha bằng max RGB sRGB; chia RGB cho alpha; loang màu vào điểm alpha 0 bằng EDT trong từng ô. Kiểm dựng ngược sai tối đa 1 mức byte.
- A.R: smoothstep 0,03–0,12; maximum filter 5 × 5, Gauss σ 1. A.G: vành ngoài 4 px, Gauss σ 0,8, nhân nhiễu song tuyến tính lưới 24 px, hạt giống 273; một ngưỡng chung để khe mực đạt 25% ±3%.
- A.B: dải trong mép 0–3 px phía lồi của đường tâm; chọn alpha sáng nhất tới 4% diện tích sáng, làm mềm σ 0,6. Diện tích nóng hiệu dụng là tổng byte/255.
- B.R: map chung trên `U = dilate(max_k(A.R_k) > 0,5, 2 px)`. Trong U lấy chiều dài tích lũy tới hình chiếu gần nhất trên đường tâm, chia chiều dài chính nét đó; không cắt ở khoảng cách 40 px. Đặt ngoài U bằng 1 trước Gauss σ 1 rồi đặt lại ngoài U bằng 1. Sao chép map vào 24 ô; B.G/B.B bằng 0, B.A bằng 255 trong ô, cuối cùng viền mọi kênh về 0.

A.A theo hạng của 273b:

1. Vỏ nhị phân lấy trực tiếp từ byte A.R đã lưu: `A.R > 0,5`. Đếm tuổi sống liên tục từ f053+k tới f120, gồm khung hiện tại, dừng ở khung đầu alpha <0,08. Chuẩn hóa tuổi bằng phân vị 99 trong vỏ và kẹp [0,1]; EDT chia phân vị 99 của EDT trong vỏ, như 273.
2. Tính `s = 0,75·life_norm + 0,25·edt_norm` bằng số thực trước lượng tử hóa. Xếp hạng tăng từ 0 tới N−1; các điểm bằng điểm nhận hạng trung bình. Trong vỏ, `A.A = 0,02 + 0,98·rank(s)/(N−1)`.
3. Mép mềm `0 < A.R ≤ 0,5` lấy A.A của điểm vỏ nhị phân gần nhất nhân `A.R/0,5`. Phần còn lại đặt 0 trước lọc. Sau đó Gauss σ 0,6 px, mode constant/cval 0; lượng tử hóa bằng `numpy.rint`, giữ viền 2 px bằng 0.
4. Chỉ ghi kênh alpha vào bản sao maskA cũ; so RGB từng byte trước ghi và sau đọc lại PNG. Đo A.A trung bình trên vùng gốc/mũi là 20% đầu/cuối dọc đường tâm gần nhất, ở cả 24 ô.

## Xem trước CPU và video

`preview-masked.ts` nhập trực tiếp `composeFlipbookMasked`, `blendPremultiplied`, `flipbookControl`, `FLIPBOOK_TIMING`, `FLIPBOOK_MASKED_LOOK`, `srgbToLinear` từ `games/immortality-cultivation/src/view/skills/flipbook.ts`; không chép lại công thức shader.

Dựng đủ tick 0–42. Dùng `vFrame=tick*24/60`, không vòng, nội suy hai khung kế tiếp; ctl lấy tuổi tick/60, đời 43/60, cool=erode=0 và lịch `impact-key1`. Mẫu màu đổi sRGB sang tuyến tính, mặt nạ chia byte/255; look mặc định, tint 1, soft 1. Ghép premultiplied trên đá tối `#2a2c30` tuyến tính, kẹp HDR rồi mã hóa sRGB 8 bit. Đây là xem trước CPU không bloom, không phải nghiệm thu trong play host.

- `preview-ticks.png` vẫn chọn tick 0, 1, 3, 6, 9, 12, 18, 24, 30, 36, 42; 4224 × 412, nhãn Tick tiếng Anh.
- `preview.mp4`: 768 × 768 (ô 384 nhân 2), H.264/yuv420p, 60 fps. Một lượt gồm 43 tick ở tốc độ thật (43 khung), rồi 43 tick ở 15 fps (mỗi tick giữ 4 khung). Lặp cặp đó hai lần: **430 khung, 7,1667 giây**. Nhãn Tick nhỏ ở góc; đo diện tích trước khi thêm nhãn. Khung thô chỉ ở bộ nhớ, không ghi hàng loạt ảnh ra đĩa. `ffprobe -count_frames` phải đọc đủ 430 khung, đúng codec/pixel format/kích thước/tốc độ; tệp dưới 5.000.000 byte.
- `preview-area.json`: số điểm có độ sáng Rec.709 tuyến tính >0,1 sau kẹp HDR, chia số tick 9, cho từng tick 0–42. Ghi thêm số sau mã hóa sRGB 8 bit để kiểm sai số lượng tử hóa. In nguyên chuỗi ra log.

Kiểm đơn điệu áp dụng từ 9→10 đến 41→42: mức tăng tối đa cho phép là 0,02 lần diện tích tick 9. Tick 12 phải trong 0,50–0,80; tick 18 trong 0,10–0,30; tick 42 đúng 0. Khi kiểm thất bại, công cụ vẫn giữ ảnh, video và JSON, ghi `CPU_preview_checks_failed` rồi thoát mã 1; không ghi trạng thái đạt.

**Kết quả 273b hiện tại:** tick 12 = 0,683744; tick 18 = 0,191641; tick 42 = 0. Tuy nhiên tick 9→10 tăng 0,024846 (sau mã hóa PNG: 0,026207), vượt 0,02. Kiểm đơn điệu chưa đạt. Không sửa shader, màu ramp, lịch hay công thức hạng để ép đạt; Claude cần xem số đo và quyết định bước tiếp theo.

## Tệp và hồ sơ

Trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`:

- `fire-impact-k1-r2-v1a.a4.maskA.png`, `fire-impact-k1-r2-v1a.a4.masks.json`: cập nhật 273b.
- `fire-impact-k1-r2-v1a.a4.maskA.v1.png`, `fire-impact-k1-r2-v1a.a4.masks.v1.json`: bản cũ nguyên vẹn.
- `fire-impact-k1-r2-v1a.a4.rgba.png`, `fire-impact-k1-r2-v1a.a4.maskB.png` và mọi nguồn khác: giữ nguyên.

Trong `.local/codex-runs/273-out/`: hai ảnh xem trước, video, `preview-area.json`, `preview-measurements.json`, `measurements.json`, `273b-survival-rank-verification.json`, `273b-video-verification.json`, báo cáo kiểm cuối và log/trạng thái/băm có tiền tố `273b-`. `channels-k00-k23.png` được tạo lại với A.A mới, vẫn gồm 6 cột k00/04/08/12/16/20 và 6 hàng RGBA/A.R/A.G/A.B/A.A/B.R.

Các log/verification không có tiền tố `273b-` từ lượt cũ giữ làm lịch sử; chúng không xác nhận A.A mới. Trong `masks.json`, `sources.builder` và `continuation` là lịch sử 273; `survival_rank` ghi công cụ, bản sao, kiểm và phiên bản của 273b. `preview`/`checks.preview_area` phản ánh kết quả mới, kể cả FAIL.

Claude chuyển đầu ra cần duyệt sang thư mục review và gửi anh; phiếu này chỉ được ghi vào `273-out`. Chưa nối lab. Màu sống cuối vẫn trắng vàng theo ramp 258; thay màu than đỏ cần phiếu shader riêng. Không chạy build/test game, trình duyệt hoặc dev server.
