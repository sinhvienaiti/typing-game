# Báo cáo phiếu 277 · Hỏa, lô 1 thay hình bằng art

Đã làm phần mã và test mới, **chưa đạt toàn bộ kiểm bắt buộc**: 6 test cũ mâu thuẫn với đường mặc định mới; Vite không hỗ trợ cờ `--no-cache` mà phiếu bắt buộc. Chưa commit hoặc gộp.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD đúng `ee3ee97`. Lúc nhận chỉ có `?? node_modules`.

## Tệp đã ghi

Đường dẫn dưới đây tính từ worktree, trừ báo cáo này ở repo cha.

| Tệp | Việc đã làm |
| --- | --- |
| `src/view/skills/element-fire.ts` | Đường art mặc định; cờ dev `?fxcode=1` giữ đường cũ; thẻ sao, vòng tay, vòng đất, dải vạch; nạp media và đặt phẳng riêng cho các pool mới. |
| `tests/view/fire-lot1-art.test.ts` | 6 test dùng clip giả, không đọc ảnh: lượt 1–7 và ngân sách, đường cũ/spec cũ, tuổi 0/biến thể/kích thước/tuổi thọ, hướng và cuộn dải, tương đương các lớp giữ lại trong A/B, URL nạp dải. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Ghi thay đổi, số đo khung đầu, cách nạp và giới hạn kiểm tra. |
| `docs/codex-queue/277-report.md` ở repo cha | Báo cáo này. |

Đăng ký pool đã nằm trong constructor `FireLayers`, nên không cần sửa `element-stage.ts`. Không ghi tệp khác, test có sẵn, manifest hoặc media; không cài gói, chạy game chính, mở cổng mạng, tạo ảnh/âm thanh hay chạy lệnh Git ghi.

## Kết quả mã

- Sao: `fire-twinkle-set`, 8 biến thể × 16 khung, 24 fps; chọn hàng bằng luồng `Rand` riêng của view, đường kính `2 × reach`. Giữ cỡ nhỏ và thời gian sống cũ của nhát kiếm sông. Luồng riêng tránh dịch chuỗi ngẫu nhiên của than, khói và art không thay.
- Vòng tay: `fire-halo-ring`, 6 × 4 ô, 24 khung, 24 fps; quay về camera, một lần trong 0,3 giây. Vòng đất: `fire-halo-seal-loop`, 8 × 4 ô, 32 khung, 24 fps; phẳng XZ, 0,62 giây, xói từ 70 % tuổi thọ. Pool đã có xói trong mode `fire`; **không cần mờ ba khung cuối**.
- Dải: chọn **`strip-fire-sheath-v2.rgba.png` vì phiếu yêu cầu dùng `-v2` khi có cả hai**, không coi đây là một lần chấm đẹp. JSON cho biết bản này lấy khung 22, bản thường khung 106; ảnh 512 × 128. Dải phẳng nhận `dir`/`span`, cuộn 0,5 chu kỳ/giây theo đồng hồ từng thẻ, kể cả host chỉ chạy stream. Thay beam finisher và beam/lớp heat-field của cutSeam; giữ các thẻ `fire-trail` có sẵn quanh finisher.
- Tuổi 0: alpha bằng 1, không delay/fade-in. Đo trung bình ánh sáng tuyến tính Rec.709 từng ô bằng ImageMagick, chọn đỉnh sao `[3, 9, 9, 7, 11, 8, 12, 4]`, vòng tay 19, vòng đất 5. Khác `checks.peakFrame` trong JSON vì trường đó đo độ phủ. Sao và vòng tay chạy phần từ đỉnh đến cuối trong đúng tuổi thọ.
- Atlas vào `FlipbookPlayer.pool()`/`library("fire")` có sẵn. Chuẩn hóa biến thể sao trong bộ nhớ, không sửa manifest. `aura/strips` chưa có manifest, nên dải lấy URL từ `player.base`, đợi `library.load()`, rồi đăng ký một ô RGBA qua `library.add()`. Không chép ảnh vào worktree.
- Đường mặc định không đăng ký `FirePointPool`, hai `HeatRingPool` hoặc beam của Hỏa, kể cả khi thiếu clip. Nhánh `fxcode=1` giữ các thân mã cũ; không đổi `impact()` của phiếu 264. Mỗi pool mới một mesh instanced; không thêm cấp phát mỗi khung.

## Kiểm bắt buộc

1. **Kiểm kiểu: PASS**, thoát 0:
   `node node_modules/typescript/bin/tsc --noEmit -p .`
2. **Vitest: FAIL do 6 kỳ vọng cũ**, lệnh đúng cờ:
   `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`
   Kết quả **985 qua / 6 lỗi / 991 test**, **88 tệp qua / 2 tệp lỗi / 90 tệp**. Mốc bàn giao: 985 test / 89 tệp; thêm đúng 6 test / 1 tệp.
3. **Test mới: 6/6 PASS**. Lượt 1–7: pool cũ không đăng ký, count 0; **158 lần phát sao, tối đa 17/256 thẻ, 0 rơi**. Các lần phát than, sprite và art không thay giống nhau trong A/B. Kiểm tuổi 0 dùng khung/alpha và mẫu độ sáng giả; chưa phải phép đo pixel GPU.
4. **Build tạm chưa thực hiện được.** Đã chạy:
   `IC_VITE_CACHE_DIR=/private/tmp/codex-277-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-277-dist --no-cache --configLoader runner`
   Vite **7.3.7** thoát 1 trước khi build: `CACError: Unknown option --cache`. Không tự bỏ cờ bị phiếu cấm. Đã gửi câu hỏi xin dùng lệnh build đúng như 264 (`--configLoader runner`, cache nằm trong thư mục tạm sạch), chưa nhận câu trả lời tại lúc báo cáo. **Chưa grep bundle**; `/private/tmp/codex-277-dist` không được tạo, không còn thư mục build để dọn.
5. **Diff/phạm vi: PASS**. `git diff --check` sạch. `git diff --stat`: một tệp theo dõi, 245 dòng thêm / 97 dòng bỏ; hai tệp mới chưa theo dõi không nằm trong stat. Trạng thái worktree:

```text
 M src/view/skills/element-fire.ts
?? docs/changelog/2026-11-05-fire-lot1-art.md
?? node_modules
?? tests/view/fire-lot1-art.test.ts
```

## Sáu test cũ cần xử lý phạm vi

Không sửa chúng vì phiếu cấm. Đã gửi câu hỏi xin chuyển các ca liên quan sang kiểm đường cũ với `?fxcode=1`, chưa nhận câu trả lời tại lúc báo cáo.

- `element-layer.test.ts:588`: bắt buộc hai pool vòng mã vẫn được đăng ký.
- `element-layer.test.ts:621`: bắt buộc có vòng mã để kiểm vật chất/soot.
- `element-layer.test.ts:916`: bắt buộc hơn ba lần phát điểm mã.
- `element-layer.test.ts:952`: bắt buộc phát vòng mã trong release/plant.
- `element-layer.test.ts:1019`: bắt buộc hai beam mã từ finisher/cutSeam.
- `key1-brush-impact.test.ts:266`: so số lần phát điểm mã brush/lotus, trong khi đường mới không phát điểm mã.

Không thêm fallback về mã hoặc đổi môi trường test để làm xanh những kỳ vọng trái phiếu.

## Claude nhận tiếp

Giải quyết quyền sửa 6 ca cũ và cờ build, chạy lại kiểm bắt buộc, grep bundle không có `fxcode`, rồi dọn build tạm. Sau đó chạy parity **ONLY lô 1**, perf, quay video trước/sau ở camera chơi và hai giám khảo mù ≥ 8,5. Các bước hình ảnh/GPU này được phiếu giao Claude; báo cáo không tuyên bố nghiệm thu thị giác hay hiệu năng. Không gặp hạn mức công cụ hoặc mốc giờ phải đợi.
