# Báo cáo phiếu 274b · Giữ than trong dải son của `fbRamp`

**Trạng thái: đã sửa đúng lời giải; kiểm mã và màu yêu cầu đạt.** Preview còn **472 điểm sáng ở tick 30**. Công cụ xem trước vẫn thoát 1 vì lỗi đơn điệu **9→10 có sẵn từ 273b**; không sửa lịch xói, ramp hoặc ngưỡng kiểm để ép đạt.

## 1. Đã làm

- `games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts`: thay phép nhân làm nguội bằng trần `min(r, mix(1, 0.4, rampCool * smoothstep(0.2, 0.85, e)))` ở cả GLSL và CPU. JSDoc của look và setter ghi độ mạnh 0–1, công thức và mặc định 0. Hàm CPU hiện không có biến cục bộ che tên `mix`, nên không cần đổi tên.
- `games/.wt-ic-flipbook-cool/tests/view/flipbook-v2.test.ts`: chỉ sửa nhóm 274. Hai ca màu kiểm r = `mix(1, 0.4, smoothstep(0.2, 0.85, 0.5))` và r = 0,4 bằng ramp viết tay, sai số 1e-6; cập nhật chuỗi GLSL. Giữ test mặc định 0 và kiểm băm shader cũ. Toàn bộ test ngoài nhóm 274 trùng byte với cả mốc trước 274 lẫn trước 274b.
- `tools/vfx-masks/preview-masked.ts`: chỉ mở rộng danh sách in số đo màu từ `[30, 36]` thành `[18, 24, 30, 36]`.
- Ghi đè đầu ra `cool-*` trong [274-out](../../.local/codex-runs/274-out/); thêm log, mốc và diff riêng mang tiền tố `274b-`.

Worktree giữ đúng nhánh `codex/flipbook-ramp-cool`; giữ toàn bộ thay đổi chưa commit của 274.

## 2. Kiểm mã và build

| Kiểm | Kết quả |
| --- | --- |
| TypeScript worktree | **Đạt**, `tsc --noEmit -p .`, thoát 0. |
| Vitest đầy đủ | **Đạt 964/964 test, 87/87 tệp**, có đủ `--no-cache --configLoader runner --maxWorkers 4`. |
| TypeScript strict của công cụ preview | **Đạt**, thoát 0. |
| Shader đời cũ | **Đạt**, hai băm cũ vẫn khớp trong test. |
| Build tạm | **Đạt**, thoát 0; dùng lại bộ chuyển tiếp Vite API của 274 với đủ hai cờ bắt buộc. |
| `grep -rl "uRampCool" /private/tmp/codex-274-dist` | Không in gì, thoát 1 đúng nghĩa không tìm thấy; **đã xóa thư mục build**. |
| Diff | `git diff --check` không lỗi. |

Vite đã cài không hỗ trợ CLI `--no-cache`, nên chạy đúng cách của 274, không chạy CLI thiếu cờ:

```sh
# Trong games/.wt-ic-flipbook-cool
IC_VITE_CACHE_DIR=/private/tmp/codex-274-dist/.vite-cache node /Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/274-out/build-no-cache.mjs --no-cache --configLoader runner --outDir /private/tmp/codex-274-dist
```

Log: [274b-tsc.log](../../.local/codex-runs/274-out/274b-tsc.log), [274b-vitest.log](../../.local/codex-runs/274-out/274b-vitest.log), [274b-build.log](../../.local/codex-runs/274-out/274b-build.log), [kiểm build và dọn thư mục](../../.local/codex-runs/274-out/274b-build-verification.json).

## 3. Preview và số đo

Đã chạy từ gốc repo cha:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node --import ./games/immortality-cultivation/node_modules/tsx/dist/loader.mjs tools/vfx-masks/preview-masked.ts --force --ramp-cool 1 --out-prefix cool --flipbook games/.wt-ic-flipbook-cool/src/view/skills/flipbook.ts
```

Đầu ra: [video](../../.local/codex-runs/274-out/cool-preview.mp4), [tấm tick](../../.local/codex-runs/274-out/cool-preview-ticks.png), [phóng tick 18/24/30](../../.local/codex-runs/274-out/cool-tail-ticks.png), [diện tích](../../.local/codex-runs/274-out/cool-preview-area.json), [số đo đầy đủ](../../.local/codex-runs/274-out/cool-preview-measurements.json), [log](../../.local/codex-runs/274-out/cool-preview.log). Đã xem hai tấm PNG; không dùng chúng làm nghiệm thu nghệ thuật trong game.

Điểm sáng được tính đúng như 273b: Rec.709 tuyến tính >0,1 sau kẹp HDR, trước mã hóa sRGB, không tính nhãn. Màu là trung bình sRGB 8 bit của chính các điểm sáng sau ghép nền đá tối:

| Tick | Điểm sáng | Màu trung bình sRGB [R; G; B] | R/G | R/B | R ≥ 2G và R ≥ 4B |
| --- | ---: | --- | ---: | ---: | --- |
| 18 | 1.857 | [203,735057; 54,861066; 10,408724] | 3,714 | 19,573 | **Đạt** |
| 24 | 1.050 | [199,926667; 54,470476; 12,979048] | 3,670 | 15,404 | **Đạt** |
| 30 | **472 > 0** | [195,048729; 53,953390; 16,805085] | 3,615 | 11,607 | **Đạt** |

Chuỗi diện tích tương đối, chia cho 10.384 điểm sáng của tick 9:

```text
0:0.278794   1:0.678929   2:0.950019   3:1.035439   4:1.038906   5:0.993355
6:1.026098   7:1.007319   8:0.999422   9:1.000000  10:1.024846  11:0.860555
12:0.683744  13:0.564522  14:0.489503  15:0.396668  16:0.302292  17:0.230162
18:0.178833  19:0.150424  20:0.140119  21:0.129430  22:0.118933  23:0.109977
24:0.101117  25:0.094954  26:0.084168  27:0.073767  28:0.063367  29:0.053448
30:0.045455  31:0.039484  32:0.032839  33:0.026098  34:0.016468  35:0.004815
36:0.000482  37:0.000000  38:0.000000  39:0.000000  40:0.000000  41:0.000000
42:0.000000
```

So với 273b, tick 0–13 trùng tuyệt đối; chênh lệch tuyệt đối lớn nhất **0,027350 lần diện tích tick 9**, tại tick 35 (mới 0,004815; cũ 0,032165). Màu son có độ sáng thấp hơn màu trắng vàng nên diện tích vượt ngưỡng cố định giảm; số điểm alpha >0 vẫn khớp bản đối chứng ở **43/43 tick**. Tại tick 37–39, còn alpha nhưng không còn điểm vượt ngưỡng sáng 0,1. Phiếu không đặt dung sai định lượng riêng cho chữ “gần”; bảng đối chiếu từng tick được giữ trong [274b-preview-comparison.json](../../.local/codex-runs/274-out/274b-preview-comparison.json).

**Lỗi kiểm cũ còn tồn tại:** 9→10 tăng **2,484592%** (bản PNG 8 bit: **2,620676%**), y hệt 273b, vượt ngưỡng 2%. Đây là kiểm duy nhất khiến công cụ thoát 1. Tick 12 = 0,683744, tick 18 = 0,178833 và tick 42 = 0 đều đạt dải kiểm cũ; từ tick 10 trở đi diện tích giảm đơn điệu.

Video đạt: **450.718 byte**, H.264/yuv420p, 768×768, 60 fps, **430/430 khung**, 7,166667 giây; ffprobe xác nhận và ffmpeg giải mã toàn bộ không lỗi. [Hồ sơ video](../../.local/codex-runs/274-out/cool-video-verification.json).

## 4. Phạm vi và bàn giao

**58/58 tệp art giữ nguyên MD5, mtime và kích thước; không thêm tệp art.** [Hồ sơ bảo toàn](../../.local/codex-runs/274-out/274b-art-verification.json).

Trạng thái worktree trước/sau đều:

```text
 M src/view/skills/flipbook.ts
 M tests/view/flipbook-v2.test.ts
?? node_modules
```

Symlink `node_modules` có sẵn từ trước. Repo cha có thay đổi của các luồng khác, nên không thể báo toàn repo chỉ có tệp của phiếu. Đã lưu trạng thái trước/sau và chênh lệch riêng trong `274-out/274b-*-status-*.txt` và `274b-git-comparison.json`; không sửa hoặc hoàn tác tệp của luồng khác.

Đối chiếu cuối: trạng thái worktree không thêm/bớt dòng; repo cha chỉ thêm `?? docs/codex-queue/274b-report.md`. [Kiểm tổng hợp](../../.local/codex-runs/274-out/274b-final-verification.json).

Chỉ sửa ba tệp nguồn/test/công cụ nêu ở mục 1, ghi đầu ra và báo cáo được phép. Không nối `rampCool = 1` vào lab hoặc game chính vì ngoài phiếu; không sửa lịch xói, mặt nạ hoặc ramp. Không chạy build/test game chính hay game khác, không mở cổng, không dùng Git ghi, không tạo ảnh AI hoặc âm thanh. Không chuyển capture sang thư mục review vì phiếu không cho ghi ở đó.

**Claude cần xem video mới và đoạn tick 18–30; lỗi tăng diện tích 9→10 vẫn là nợ cũ cần quyết định riêng.** Không gặp hạn mức hay yêu cầu chờ.
