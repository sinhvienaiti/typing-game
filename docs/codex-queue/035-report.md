# Phiếu 035 · Tuyến Cuối · Khung đầu của bùng sáng và đèn

Ngày 28/10/2026, Mac mini M4. **Đạt Kiểm 0–8 trong phạm vi mã.** Không mở trình duyệt, không cài gói, không dùng mạng, không commit. Chuẩn đối chiếu: `docs/games/VFX_STANDARD.md` §3.1 luật 5, §3.4, §5.6; không thay số thiết kế hoặc sim.

## Nền thật và phạm vi

`git -C games/.wt-ts-vfx log --oneline -3` (thoát 0):

```text
ce9dea3 feat(view): a big kill's cloud as wide as its flash, thicker and darker; more chunks whose cold rims stay brighter (N6, judge round 1)
0e9752c fix(view): a big kill's smoke fades into the deck - no straight dark edge where the floor cuts a puff (N6, round 2)
b798127 feat(view): a big kill leaves an aftermath - a dark cloud the size of the flash, a scorch with glowing cracks, a field of wreckage that lies on (N6, judge round 1) - FEEL_PASS_S1 13
```

HEAD thực tế là `ce9dea3`, chưa có commit chỉ sửa tài liệu như giả định. Bốn file tài liệu ở checkout chính vẫn chưa commit. Các cổng mã của Kiểm 0 đều đạt nên tiếp tục; không sửa hay chuyển các tài liệu đó.

Các file đã sửa/tạo (mọi đường dẫn mã dưới `games/.wt-ts-vfx/`):

- `src/view/fx.ts`: chỉ `Glows` và hàm phụ `writeGlow`; cờ mới ở ô 17, tuổi đầu 0, `step` chỉ già hóa burst đã được flush; ghi burst và chép stamp theo thứ tự ở `flush`; ba mảng stamp cấp phát trong constructor.
- `src/view/lights.ts`: chỉ `GunLights`; `flash` đặt cờ mới, lần `update` đầu giữ nguyên công suất rồi xóa cờ; `hold` xóa cờ mới.
- `src/view/shots.ts`: bỏ đúng bốn đối số cuối `, F` của burst, giữ `NaN`.
- `src/view/typing-feel.ts`: bỏ đúng bốn đối số cuối `, F` của burst, giữ `NaN`.
- `tests/first-frame.test.ts`: mới, chín ca trong môi trường node, stub document rồi trả globals; đọc trực tiếp mảng instance, in các dòng `035 …`.
- `tmp/035/`: mã băm trước/sau, log test/check/đột biến, bản sao mã đã sửa và kết quả kiểm JSON; bị Git bỏ qua.
- `docs/codex-queue/035-report.md` ở repo cha: báo cáo này.

Không sửa atlas, shader, `Strips`, `Streaks`, `Column`, thông số sáng/mờ/cỡ/chuyển động, ưu tiên đèn hoặc `lit`. Không ghi vào checkout chính hay Tu Tiên.

## Kiểm 0 · Điều kiện đầu và test trước mã

Chạy từ repo cha, trước khi ghi `src`:

`git -C games/.wt-ts-vfx branch --show-current` → thoát 0, in `ts-vfx`.

`git -C games/.wt-ts-vfx merge-base --is-ancestor ce9dea3 HEAD` → thoát 0, không in gì.

`git -C games/.wt-ts-vfx diff --quiet ce9dea3 HEAD -- src tests scripts package.json pnpm-lock.yaml tsconfig.json vite.config.ts vitest.config.ts kit.config.json` → thoát 0, không in gì.

`test -e games/.wt-ts-vfx/node_modules/.bin/vitest` → thoát 0, không in gì.

Trạng thái đầu (cả ba lệnh thoát 0):

`git -C games/.wt-ts-vfx status --short --untracked-files=all`:

Không in gì.

`git --no-optional-locks -C games/typing-survival status --short`:

```text
 M AGENTS.md
 M docs/BUILD_S1.md
 M docs/FEEL_PASS_S1.md
 M docs/changelog/2026-10-27-feel-n4n6.md
```

`git status --short --untracked-files=all -- docs/codex-queue/`:

Không in gì.

Lệnh nền (từ repo cha):

```sh
cd games/.wt-ts-vfx && mkdir -p tmp/035 && ../../.local/bin/heavy.sh node --import tsx scripts/chapter-hashes.ts > tmp/035/before.txt
```

Thoát 0. Từ worktree:

```sh
wc -l tmp/035/before.txt
shasum -a 256 tmp/035/before.txt
```

```text
152 tmp/035/before.txt
ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e  tmp/035/before.txt
```

Đã viết test trước khi sửa `src`, rồi chạy:

```sh
cd games/.wt-ts-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm exec vitest run tests/first-frame.test.ts
```

Log lưu ở `tmp/035/test-before.txt`; thoát 1 đúng dự kiến:

```text
Test Files  1 failed (1)
Tests  7 failed | 2 passed (9)
```

Ca 6 và 9 đạt. Tên bảy ca hỏng:

- `1: a three-frame star starts whole and fades once per frame`
- `2: two to six-frame bursts have exactly one full frame and their designed visible life`
- `3: position, size and angle start at creation and advance on the next step`
- `4: embers, smoke scorches and rising puffs keep their own fade curves`
- `5: draw-phase bursts precede ordered stamps and leave no stale instance slots`
- `7: each flash matches held power at age zero and then follows lightLevel`
- `8: a new Ray flash lights the floor at full colour and power`

## Kiểm 1 · Toàn bộ kiểm tra được cho phép

```sh
cd games/.wt-ts-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm check
```

Thoát 0 ngay lần đầu; log `tmp/035/check.txt`:

```text
src/kit OK: 59 files match kit-manifest.json (kit 0.1.0, modules platform, input, vocab, speech, learning, three, tools, feedback, audio, balance)
Test Files  15 passed (15)
Tests  151 passed (151)
$ tsc --noEmit && vite build
✓ built in 1.13s
```

`tsc --noEmit` không lỗi. Bước sim chương có median 0,940 ms, p95 1,324 ms; không cần chạy lại. Vite cảnh báo một số chunk lớn hơn 500 kB sau nén mã; build vẫn đạt, không đổi cấu hình ngoài phạm vi.

## Kiểm 2 · Chạy riêng file mới

```sh
cd games/.wt-ts-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm exec vitest run tests/first-frame.test.ts
```

Thoát 0; log `tmp/035/test-after.txt`:

```text
Test Files  1 passed (1)
Tests  9 passed (9)
```

Không còn ca hỏng. Đã kiểm cả flash tạo sau `update`, scale khác 1, hold dùng lại slot flash, chuyển động/cỡ/góc, khói/than, stamp xen burst và dừng ba khung.

## Kiểm 3 · Mã băm sau sửa

```sh
cd games/.wt-ts-vfx && ../../.local/bin/heavy.sh node --import tsx scripts/chapter-hashes.ts > tmp/035/after.txt
```

Thoát 0. Từ worktree:

```sh
cmp tmp/035/before.txt tmp/035/after.txt
wc -l tmp/035/before.txt tmp/035/after.txt
shasum -a 256 tmp/035/before.txt tmp/035/after.txt
```

`cmp` thoát 0, không in gì. Hai lệnh còn lại thoát 0, in:

```text
152 tmp/035/before.txt
152 tmp/035/after.txt
304 total
ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e  tmp/035/before.txt
ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e  tmp/035/after.txt
```

## Kiểm 4 · Sim không đổi

```sh
git -C games/.wt-ts-vfx status --porcelain -- src/sim src/content src/kit src/app scripts tests/golden
```

Thoát 0, không in gì.

## Kiểm 5 · Bỏ early

```sh
grep -rnw early games/.wt-ts-vfx/src/view games/.wt-ts-vfx/src/app
grep -c "NaN, F)" games/.wt-ts-vfx/src/view/shots.ts
grep -c "NaN, F)" games/.wt-ts-vfx/src/view/typing-feel.ts
grep -c "NaN);" games/.wt-ts-vfx/src/view/shots.ts
grep -c "NaN);" games/.wt-ts-vfx/src/view/typing-feel.ts
```

Kết quả: lệnh đầu không in gì (thoát 1 do không có kết quả); hai lệnh kế in `0`, `0` (đều thoát 1); hai lệnh cuối in `4`, `4` (đều thoát 0). Đây là hành vi chuẩn của grep khi không tìm thấy, cổng đạt. Kết quả chi tiết ở `tmp/035/checks4-5.json`.

## Kiểm 6 · Hai đột biến

Trước đột biến, chép `src/view/fx.ts` và `src/view/lights.ts` đã sửa vào `tmp/035/fx.fixed.ts`, `tmp/035/lights.fixed.ts`. Làm lần lượt và phục hồi trong `finally` sau từng lần. Mỗi lần chạy đúng lệnh:

```sh
cd games/.wt-ts-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm exec vitest run tests/first-frame.test.ts
```

(a) Đổi `const fresh = b[o + 17] === 1` thành `const fresh = false` trong `Glows.step`, làm burst mới già đi và di chuyển như burst cũ. Thoát 1; log `tmp/035/mutation-a.txt`:

```text
Test Files  1 failed (1)
Tests  5 failed | 4 passed (9)
```

Tên ca hỏng:

- `1: a three-frame star starts whole and fades once per frame`
- `2: two to six-frame bursts have exactly one full frame and their designed visible life`
- `3: position, size and angle start at creation and advance on the next step`
- `4: embers, smoke scorches and rising puffs keep their own fade curves`
- `5: draw-phase bursts precede ordered stamps and leave no stale instance slots`

(b) Bỏ nhánh cờ mới trong `GunLights.update`. Thoát 1; log `tmp/035/mutation-b.txt`:

```text
Test Files  1 failed (1)
Tests  2 failed | 7 passed (9)
```

Tên ca hỏng:

- `7: each flash matches held power at age zero and then follows lightLevel`
- `8: a new Ray flash lights the floor at full colour and power`

Không có ca hỏng ngoài dự kiến. Đã phục hồi hai file rồi chạy từ repo cha:

```sh
cmp games/.wt-ts-vfx/src/view/fx.ts games/.wt-ts-vfx/tmp/035/fx.fixed.ts
cmp games/.wt-ts-vfx/src/view/lights.ts games/.wt-ts-vfx/tmp/035/lights.fixed.ts
```

Cả hai thoát 0, không in gì. Biên bản ở `tmp/035/mutations.json`. Mã cuối khớp từng byte với mã đã qua `pnpm check` và test riêng.

## Kiểm 7 · So trạng thái đầu/cuối

```sh
git -C games/.wt-ts-vfx status --short --untracked-files=all
```

Thoát 0; đầu sạch, cuối chỉ thêm đúng:

```text
 M src/view/fx.ts
 M src/view/lights.ts
 M src/view/shots.ts
 M src/view/typing-feel.ts
?? tests/first-frame.test.ts
```

```sh
git --no-optional-locks -C games/typing-survival status --short
```

Thoát 0; cuối giống đầu từng dòng:

```text
 M AGENTS.md
 M docs/BUILD_S1.md
 M docs/FEEL_PASS_S1.md
 M docs/changelog/2026-10-27-feel-n4n6.md
```

```sh
git status --short --untracked-files=all -- docs/codex-queue/
```

Thoát 0; đầu không in gì, cuối chỉ thêm:

```text
?? docs/codex-queue/035-report.md
```

Không có báo cáo làn khác tại thời điểm kiểm. Bản chụp ở `tmp/035/initial-status.json`, `tmp/035/checks7-8-final.json`.

## Kiểm 8 · Diff numstat

```sh
git -C games/.wt-ts-vfx diff --numstat
```

Thoát 0:

```text
44	26	src/view/fx.ts
7	1	src/view/lights.ts
4	4	src/view/shots.ts
4	4	src/view/typing-feel.ts
```

File test mới chưa được Git theo dõi nên không có trong numstat. `git -C games/.wt-ts-vfx diff --check` cũng thoát 0, không in gì.

## Bảng trước/sau từ console 035

Mỗi chuỗi bắt đầu ở khung tạo (f0), bước 1/60 s. Số dưới đây lấy từ dòng `035 …`, làm tròn 4 chữ số. Các số 0 cuối gồm cả khung không còn instance và alpha ≤ 1e-6; không sửa sai số tuổi float32 đã có.

**Bùng sáng theo đời** (`CELL.soft`):

| Đời | Trước | Sau |
|---|---|---|
| `2F` | 0.2500, 0.0000, 0.0000, 0.0000 | 1.0000, 0.2500, 0.0000, 0.0000 |
| `3F` | 0.4444, 0.1111, 0.0000, 0.0000, 0.0000 | 1.0000, 0.4444, 0.1111, 0.0000, 0.0000 |
| `4F` | 0.5625, 0.2500, 0.0625, 0.0000, 0.0000, 0.0000 | 1.0000, 0.5625, 0.2500, 0.0625, 0.0000, 0.0000 |
| `5F` | 0.6400, 0.3600, 0.1600, 0.0400, 0.0000, 0.0000, 0.0000 | 1.0000, 0.6400, 0.3600, 0.1600, 0.0400, 0.0000, 0.0000 |
| `6F` | 0.6944, 0.4444, 0.2500, 0.1111, 0.0278, 0.0000, 0.0000, 0.0000 | 1.0000, 0.6944, 0.4444, 0.2500, 0.1111, 0.0278, 0.0000, 0.0000 |

Ca `CELL.star4`, đời 3F, intensity 3, dòng `035 star3F`: trước `[0.444444,0.111111,0,0]`, sau `[1,0.444444,0.111111,0]`. Alpha ở tuổi 0 là 1; RGB vẫn nhân intensity 3.

**Đèn theo loại** (cường độ chia cho đèn giữ cùng công suất):

| Loại LIGHT | Trước | Sau |
|---|---|---|
| `xung` | 0.4444, 0.1111, 0.0000, 0.0000, 0.0000 | 1.0000, 0.4444, 0.1111, 0.0000, 0.0000 |
| `xungFirst` | 0.6267, 0.3403, 0.1406, 0.0278, 0.0000, 0.0000, 0.0000 | 1.0000, 0.6267, 0.3403, 0.1406, 0.0278, 0.0000, 0.0000 |
| `tan` | 0.6267, 0.3403, 0.1406, 0.0278, 0.0000, 0.0000, 0.0000 | 1.0000, 0.6267, 0.3403, 0.1406, 0.0278, 0.0000, 0.0000 |
| `ray` | 0.6944, 0.4444, 0.2500, 0.1111, 0.0278, 0.0000, 0.0000, 0.0000 | 1.0000, 0.6944, 0.4444, 0.2500, 0.1111, 0.0278, 0.0000, 0.0000 |
| `phao` | 0.7415, 0.5216, 0.3403, 0.1975, 0.0934, 0.0278, 0.0008, 0.0000, 0.0000, 0.0000 | 1.0000, 0.7415, 0.5216, 0.3403, 0.1975, 0.0934, 0.0278, 0.0008, 0.0000, 0.0000 |
| `big` | 0.7901, 0.6049, 0.4444, 0.3086, 0.1975, 0.1111, 0.0494, 0.0123, 0.0000, 0.0000, 0.0000 | 1.0000, 0.7901, 0.6049, 0.4444, 0.3086, 0.1975, 0.1111, 0.0494, 0.0123, 0.0000, 0.0000 |

Các dòng gốc sau sửa (trước sửa có đầy đủ ở `tmp/035/test-before.txt`):

```text
035 star3F [1,0.444444,0.111111,0]
035 burst 2F [1,0.25,0,0]
035 burst 3F [1,0.444444,0.111111,0,0]
035 burst 4F [1,0.5625,0.25,0.0625,0,0]
035 burst 5F [1,0.64,0.36,0.16,0.04,0,0]
035 burst 6F [1,0.694444,0.444444,0.25,0.111111,0.027778,0,0]
035 light xung [1,0.444444,0.111111,0,0]
035 light xungFirst [1,0.626736,0.340278,0.140625,0.027778,0,0]
035 light tan [1,0.626736,0.340278,0.140625,0.027778,0,0]
035 light ray [1,0.694444,0.444444,0.25,0.111111,0.027778,0,0]
035 light phao [1,0.741512,0.521605,0.340278,0.197531,0.093364,0.027778,0.000772,0,0]
035 light big [1,0.790123,0.604938,0.444444,0.308642,0.197531,0.111111,0.049383,0.012346,0,0]
```

## Số dòng src

Chạy từ worktree trước và sau:

```sh
find src -name '*.ts' -not -path 'src/kit/*' | xargs cat | wc -l
```

Cả hai thoát 0: trước **12.402**, sau **12.426**, tăng **24** dòng TypeScript ngoài kit. Không tính CSS hoặc test.

## Cách chọn và phần còn lại

- Nền thực tế chưa có commit tài liệu: tiếp tục vì nhánh, tổ tiên, diff mã và hash đều khớp cổng bắt buộc; ghi rõ ở trên.
- “Không ghi hai lần ở tuổi 0” được hiểu theo các khung thời gian đang chạy: ca 2 xác nhận đúng một khung alpha 1 khi dt > 0; khi dt = 0 thì giữ nguyên theo ca 6. Cờ mới xóa sau lần flush đầu, không dùng tuổi âm hay bù dt.
- Mảng tạm có capacity stamp: vị trí/màu 4 float mỗi stamp, cỡ/góc 2 float mỗi stamp. Cấp phát trong constructor; bước khung chỉ dùng số, ghi mảng, `copyWithin` và đường upload vốn có, không tạo mảng tạm mới.
- Không tuyên bố nghiệm thu hình từ test node. Phiếu chỉ chứng minh alpha/công suất/tuổi và tính toàn vẹn của instance; phép đo theo §5.6 do Claude làm sau.

**Claude cần xem trên trình duyệt, cả 1280×720 và 1920×1080:**

- Cảnh `f5` và `f8`, đặc biệt lúc f0 vừa sáng đủ; trắng xóa ≤ 6 % vùng sân, dùng `tools/vfx-sheet measure --field` khi phiếu 037 sẵn sàng.
- Tương phản dòng từ ≥ 7 : 1 ở p99 (mốc cũ 7,40–7,49).
- Nền dưới dòng từ: p50 tăng ≤ 0,02 theo FEEL §4.1.
- Rail Gun (Ray) và Heat Beam (Tia) quanh tàu: kiểm lóe/đèn mới có che dòng từ, rửa màu hoặc lấn nền quanh tàu không.
- Chạy lại `survival-s1-stage` ở hai cỡ; replay trận trình duyệt trong Node phải cùng mã băm.

Đã bỏ qua theo ranh giới phiếu: trình duyệt, ảnh/âm thanh mới, sửa `FEEL_PASS_S1.md` §12, dòng `early` trong `AGENTS.md` của game, changelog và commit. Claude cập nhật tài liệu và changelog sau khi đo, rồi mới commit.

## Claude duyệt (28/10/2026)

**Nhận.** Commit trên nhánh `ts-vfx` của `games/typing-survival` (worktree `games/.wt-ts-vfx`), chưa gộp: `5d9c8cb` (mã và test của phiếu), `e7c3927` (changelog `docs/changelog/2026-10-28-first-frame.md` với số đo trình duyệt).

- Đọc diff: `Glows` (cờ mới ở ô 17, `step` không già hóa burst mới, `flush` ghi burst ở tuổi 0 rồi mới chép stamp từ ba mảng riêng), `GunLights` (cờ `fresh`, `hold` xóa cờ), bỏ đúng 8 đối số `, F`. Không đụng sim, cường độ, đời hay công thức mờ dần. Không cấp phát trong khung.
- Chạy lại: `pnpm check` lượt 1 hỏng đúng test đo thời gian bước sim (máy đang chạy nhiều làn), lượt 2 đạt 151/151; file test mới 9/9, các dòng `035 …` khớp bảng; mã băm chương 152 dòng, `ae7e9859…626e`, trùng `before.txt`; đột biến (a) tự làm lại: hỏng đúng ca 1–5.
- Trình duyệt, 1280 × 720 và 1920 × 1080 (Vite riêng ở 4161, đã tắt), mọi khung của phát bắn Xung, Tán, Ray, Pháo Sao, đo bằng `tools/vfx-sheet` cạnh bốn file view của `ce9dea3` cùng kịch bản: khung phát bắn là đỉnh (tỉ lệ 1,00 ≥ 0,95); f0 sáng hơn 3–9 % (lõi đã gần trắng), các khung sau sáng hơn rõ (lõi Ray f2 1.805 → 2.550): đường mờ dần chậm đúng một khung như thiết kế. Trắng xóa ≤ 1,7 % vùng sân; tương phản dòng từ p99 ≥ 7,50. `survival-feel f8`: tương phản dòng từ 7,80 / 7,69, nền dưới dòng từ p50 0,204 (tăng tối đa +0,016, trần +0,02), hai bến như cũ; chỉ "mắt → đòn" trượt như trước. Không lỗi console.
- **Đối với `main` (đã tới `3f63fcf`):** `git merge-tree` báo một xung đột ở `src/view/shots.ts` (dòng cụm lửa: `main` đổi đời `0.3 + r() * 0.15`, nhánh bỏ `, F`; gộp: giữ đời của `main`, bỏ `, F`). `fx.ts` tự gộp. Phiếu vẫn đúng trên `main`: `Glows` và `GunLights` ở `main` chưa đổi, vẫn có 8 lời gọi `NaN, F)`.
- Chưa làm, để lúc gộp (bản checkout chính đang có làn sửa ghi `AGENTS.md`, `FEEL_PASS_S1.md`): sửa đoạn "Bùng ở khung đầu" của `FEEL_PASS_S1.md` §12, dòng `early` trong `AGENTS.md`, mục "Lóe cũ mất khung đầu" của changelog N4/N6; chạy lại `survival-s1-stage` sau khi gộp (mã băm chương không đổi nên sim chắc chắn giữ).
