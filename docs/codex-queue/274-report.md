# Báo cáo phiếu 274 · Làm nguội ramp của flipbook có mặt nạ

**Trạng thái: đã sửa đúng lời giải chốt; kiểm mã đạt, kiểm màu preview chưa đạt.** `rampCool` mặc định 0, shader cũ giữ đúng băm. Với `rampCool = 1`, đoạn cuối xuống màu soot gần nền tối, chưa thành than đỏ có kênh đỏ trội rõ. Không đổi lời giải, ramp, soot hoặc ngưỡng kiểm để ép đạt; chưa nối lab.

## 1. Đã làm

- `games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts`: thêm `FlipbookMaskedLook.rampCool = 0`, phép làm nguội CPU, đúng dòng GLSL và uniform trong khối v2, uniform của pool và setter có JSDoc cạnh `hotLead`. Giữ nguyên dòng `cb` và shader đời cũ.
- `games/.wt-ic-flipbook-cool/tests/view/flipbook-v2.test.ts`: chỉ thêm một nhóm gồm **4 test**. Kiểm mặc định/0 khớp tuyệt đối ca «surviving ramp cap» của Test 4; tự tính ramp ở e = 0,5 và 0,9; kiểm đúng chuỗi GLSL, setter, attach và hai băm cũ. Bỏ nhóm mới khỏi tệp thì toàn bộ nội dung trùng byte với mốc ban đầu.
- `tools/vfx-masks/preview-masked.ts`: thêm `--ramp-cool`, `--out-prefix`, `--flipbook`; nhập động đúng mô-đun được chọn. Có tiền tố thì chỉ ghi vào `274-out`, không ghi `masks.json` hoặc đầu ra 273b. Thêm số đo màu tại tick 30/36 và vùng alpha >0. Bọc phần chạy trong hàm async để dùng được loader tsx của repo cha.
- `tools/vfx-masks/README.md`: ghi lệnh chạy, định nghĩa số đo và kết quả thực tế.
- Đầu ra, mốc trước/sau, bản diff và log nằm trong [274-out](../../.local/codex-runs/274-out/), có `ABOUT.md`.

Worktree đúng nhánh `codex/flipbook-ramp-cool`, HEAD `35f1b77`. Theo phiếu đã chốt, bỏ bước phản biện; không thiết kế lại.

## 2. Kiểm mã bắt buộc

| Kiểm | Kết quả |
| --- | --- |
| `node node_modules/typescript/bin/tsc --noEmit -p .` | **Đạt**, thoát 0, không lỗi. |
| `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` | **Đạt: 964/964 test, 87/87 tệp**, tăng 4 từ mốc 960. |
| Shader cũ | **Đạt**: VERTEX SHA-256 `c2f64aa0e39d46ec17b4f60ecd3932e42178f933784a72ee8fec1d38cc25a9c7`; FRAGMENT `3b5524bd2c052ed97c6261586915f9b218deb5756d0477d634e3605d05b93abd`. |
| Build tạm | **Đạt qua build API**, thoát 0; xem khác biệt CLI bên dưới. |
| `grep -rl "uRampCool" /private/tmp/codex-274-dist` | Không in gì, thoát 1 đúng nghĩa không có kết quả. Đã xóa thư mục build. |
| Kiểu của công cụ preview | **Đạt** khi kiểm riêng bằng TypeScript strict, `--types node`, `--typeRoots` trỏ đến gói có sẵn của game. |
| Diff | `git diff --check` không lỗi; test cũ không đổi. |

**Khác biệt CLI cần biết:** Vite **7.3.7** đang cài không nhận `--no-cache`; lệnh CLI có đủ hai cờ của phiếu thoát 1 với `Unknown option --cache`. Không bỏ cờ bị cấm. Dùng bộ chuyển tiếp [build-no-cache.mjs](../../.local/codex-runs/274-out/build-no-cache.mjs), chỉ chấp nhận đúng các cờ dưới đây, yêu cầu thư mục đích chưa tồn tại, rồi gọi Vite build API với `configLoader: "runner"` và cache riêng mới:

```sh
# Chạy trong games/.wt-ic-flipbook-cool
IC_VITE_CACHE_DIR=/private/tmp/codex-274-dist/.vite-cache node /Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/274-out/build-no-cache.mjs --no-cache --configLoader runner --outDir /private/tmp/codex-274-dist
```

Log: [tsc.log](../../.local/codex-runs/274-out/tsc.log), [vitest.log](../../.local/codex-runs/274-out/vitest.log), [build-cli.log](../../.local/codex-runs/274-out/build-cli.log), [build.log](../../.local/codex-runs/274-out/build.log), [build-verification.json](../../.local/codex-runs/274-out/build-verification.json).

## 3. Preview và phần chưa đạt

Chạy từ gốc repo cha:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node --import ./games/immortality-cultivation/node_modules/tsx/dist/loader.mjs tools/vfx-masks/preview-masked.ts --force --ramp-cool 1 --out-prefix cool --flipbook games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts
```

Đã tạo và giữ:

- [cool-preview-ticks.png](../../.local/codex-runs/274-out/cool-preview-ticks.png): 4.224 × 412; đã xem toàn tấm và [phóng riêng ba tick cuối](../../.local/codex-runs/274-out/cool-tail-ticks.png).
- [cool-preview.mp4](../../.local/codex-runs/274-out/cool-preview.mp4): **373.929 byte**, H.264/yuv420p, 768 × 768, 60 fps, **430/430 khung**, 7,166667 giây. ffprobe xác nhận, ffmpeg giải mã toàn bộ không lỗi.
- [cool-preview-area.json](../../.local/codex-runs/274-out/cool-preview-area.json), [cool-preview-measurements.json](../../.local/codex-runs/274-out/cool-preview-measurements.json), [cool-video-verification.json](../../.local/codex-runs/274-out/cool-video-verification.json).

Công cụ thoát **1 có chủ ý sau khi giữ đủ đầu ra**: tick 18 = 0, ngoài dải 0,10–0,30 của kiểm 273b. Đơn điệu với nhiễu 2% đạt; tick 12 = 0,561922 đạt; tick 42 = 0 đạt; video đạt. Đây không phải lỗi hạn mức.

Chuỗi diện tích sáng Rec.709 tuyến tính >0,1, chia tick 9 = 10.384 điểm; đã in cả số trước/sau mã hóa sRGB trong [cool-preview.log](../../.local/codex-runs/274-out/cool-preview.log):

```text
0:0.278794  1:0.678929  2:0.950019  3:1.035439  4:1.038906  5:0.993355
6:1.026098  7:1.007319  8:0.999422  9:1.000000  10:1.007608  11:0.799018
12:0.561922  13:0.401868  14:0.255104  15:0.120955  16:0.025905
17:0.000000  18:0.000000  19:0.000000  20:0.000000  21:0.000000  22:0.000000
23:0.000000  24:0.000000  25:0.000000  26:0.000000  27:0.000000  28:0.000000
29:0.000000  30:0.000000  31:0.000000  32:0.000000  33:0.000000  34:0.000000
35:0.000000  36:0.000000  37:0.000000  38:0.000000  39:0.000000  40:0.000000
41:0.000000  42:0.000000
```

**Chuỗi này không gần bằng 273b theo yêu cầu Kiểm 4.** Chênh lệch lớn nhất là 0,297092 lần diện tích tick 9. Đổi màu vẫn làm đổi diện tích vượt một ngưỡng độ sáng cố định dù alpha không đổi.

| Tick | e | Điểm sáng >0,1 | Màu trung bình sRGB của điểm sáng | Điểm alpha >0 | Màu trung bình sRGB trên vùng alpha >0, sau ghép nền |
| --- | ---: | ---: | --- | ---: | --- |
| 30 | 0,918182 | 0 | `null` | 1.105 | `[44,908597; 42,612670; 44,026244]` |
| 36 | 0,959091 | 0 | `null` | 547 | `[43,160878; 43,522852; 46,511883]` |

**Yêu cầu đỏ lớn hơn hẳn xanh lá/xanh dương chưa đạt.** Theo chính công thức chốt, r lớn nhất lần lượt chỉ còn 0,081818 và 0,040909. Cả hai dưới 0,23, nên `fbRamp` trả hoàn toàn màu `soot = [0.03, 0.022, 0.02]` tuyến tính. Màu này gần nền tối; không phải dải son `[0.693, 0.04, 0]`. Cũng theo ramp hiện tại, r = 0,5 cho `[0.8465, 0.2565, 0.0005]`, còn r = 0,1 cho đúng soot; test mới xác nhận sai số ≤1e-6.

## 4. Đối chứng, bảo toàn và phạm vi

Chạy thêm `--ramp-cool 0 --out-prefix baseline`, không truyền `--flipbook`, để kiểm đường nhập mặc định game chính. **Toàn bộ JSON diện tích khớp tuyệt đối 273b; tấm tick trùng mọi điểm ảnh** (`magick compare -metric AE`: `0 (0)`). MD5 PNG khác do metadata, không do điểm ảnh. Bản đối chứng giữ lỗi 273b cũ ở 9→10 nên cũng thoát 1; video đạt, 497.217 byte. Số điểm alpha >0 giữa baseline và cool khớp ở **43/43 tick**. Chi tiết trong [preview-comparison.json](../../.local/codex-runs/274-out/preview-comparison.json).

**58/58 tệp art được kiểm giữ nguyên MD5, mtime và kích thước; không thêm tệp trong thư mục art**, kể cả `masks.json`. Xem [art-verification.json](../../.local/codex-runs/274-out/art-verification.json).

Trạng thái worktree sau cùng:

```text
 M src/view/skills/flipbook.ts
 M tests/view/flipbook-v2.test.ts
?? node_modules
```

`?? node_modules` là symlink có từ mốc ban đầu, không do phiếu này tạo. Repo cha có nhiều thay đổi sẵn và các luồng khác đang làm việc, nên không thể ghi rằng toàn repo chỉ có tệp của phiếu này. Đã lưu Git trước/sau trong `274-out`; các dòng thay đổi ngoài phạm vi quan sát được được ghi nguyên trong [git-comparison.json](../../.local/codex-runs/274-out/git-comparison.json), không sửa hay hoàn tác chúng. Các công cụ đã là untracked từ trước; bản trước và diff riêng được giữ để Claude đọc.

Không ghi src/scripts/tests/docs của game chính; không sửa manifest hoặc nối lab. Không chạy build/test game khác, không mở cổng hoặc trình duyệt, không sinh ảnh AI/âm thanh, không dùng Git ghi. Không chuyển đầu ra sang thư mục review vì ngoài đường ghi cho phép của phiếu.

## 5. Bàn giao

**Claude cần xem `cool-preview.mp4`, đoạn tick 17–36 và số đo màu trên trước khi gửi anh.** Phần mã đáp ứng lời giải đã chốt; kết quả chưa đạt yêu cầu màu cuối của phiếu. Mặc định vẫn 0; chưa đặt 1 ở lab. Claude quyết định bước tiếp theo về màu/ramp theo số đo thực tế; phiếu này không tự thiết kế lại.

Không gặp hạn mức hoặc thời gian phải chờ; không cần runner chạy lại do quota.
