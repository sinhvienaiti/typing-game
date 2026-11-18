# Phiếu 036 · Lời Gọi · Ống sự kiện bắn và trúng cho view 2D

Ngày 28/10/2026, Mac mini M4, macOS. **Kiểm 0–9 đạt.** Chưa commit. Mã làm trong `games/.wt-td-vfx`, nhánh `td-vfx`; không ghi vào bản checkout chính `games/typing-defense`.

`FxPipe` đọc riêng `CombatRing`, chuyển mỗi `FX.fire` thành đúng một `FxDraw.muzzle`, mỗi `FX.hit` thành đúng một `FxDraw.hit`, giữ vị trí, giá trị và tick. Con trỏ bắt đầu tại lúc tạo; bộ đếm ghi nhận phần tràn vòng; `stats()` trả bản sao mới. Giao diện vẽ mặc định là một hằng không làm gì. `FxView` được chuyển nguyên văn vào cùng chunk lười. Chưa bổ sung hình vẽ.

Đã đọc skill `game-vfx-layered` và `docs/games/VFX_STANDARD.md` (§1.2, §2.3, §3, §5.4–5.6); phần chụp, chấm hình, changelog và commit thuộc bước Claude theo ngoại lệ của phiếu.

## Nền và điều kiện đầu — Kiểm 0

Các lệnh trong báo cáo chạy từ repo cha, trừ khối ghi rõ chạy trong worktree. Lệnh Git chỉ đọc; khi trỏ bản checkout chính của game đều có `--no-optional-locks`.

```sh
git -C games/.wt-td-vfx log --oneline -3
```

```text
f4cd046 docs(td): line ceiling 10,900 from step 1B.V4 (2D VFX V4a), coordinator 28/10
ad4df6f docs(td): lane A2, days and the §12 gates - changelog, BUILD_NOTES §7.10, AGENTS state
e49189a fix(td): Thư giãn and Học keep their own 20 s typing cap (lane A2 item 3, test pass row 20)
```

Các điều kiện sau đều được kiểm trước khi ghi `src`:

```sh
git -C games/.wt-td-vfx branch --show-current
# td-vfx; thoát 0
git -C games/.wt-td-vfx merge-base --is-ancestor e49189a HEAD
# Không in gì; thoát 0
git -C games/.wt-td-vfx diff --quiet e49189a HEAD -- src tests scripts package.json pnpm-lock.yaml tsconfig.json vite.config.ts vitest.config.ts kit.config.json
# Không in gì; thoát 0
test -e games/.wt-td-vfx/node_modules/.bin/vitest
# Thoát 0; không cài gói
```

Trong worktree:

```sh
find src -name '*.ts' -not -path 'src/kit/*' -print0 | xargs -0 cat | wc -l
# 10499
node -e 'const fs=require("fs");const h=/Trần cứng 1B: \*\*(\d+)\.(\d{3})\*\*/.exec(fs.readFileSync("docs/td/BUILD_1B.md","utf8"));const n=fs.readFileSync("docs/td/BUILD_NOTES.md","utf8");const m=/Mốc đang làm: \*\*(1[AB]\.\w+)\*\*/.exec(n)[1];const r=new RegExp("^\\| "+m.replace(".","\\.")+" [^|]*\\|[^|]*\\|[^|]*\\| (\\d+)\\.(\\d{3}) \\|","m").exec(n);console.log(m,h[1]+h[2],r&&r[1]+r[2])'
# 1B.V4 10900 10900
```

Cả hai trần ≥ 10.574. HEAD chỉ thêm tài liệu so với `e49189a` trong phạm vi nền của phiếu.

Đã ghi đúng script đo byte của phiếu vào `tmp/036/budget-bytes.mjs`, rồi chạy:

```sh
cd games/.wt-td-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm build > tmp/036/base-build.log 2>&1 && node tmp/036/budget-bytes.mjs > tmp/036/base-bytes.json
# Thoát 0
```

```json
{"/":84975,"/?title=0":83525,"fxChunk":null,"portraitInEntry":1,"portraitInFx":null}
```

Trạng thái đầu, đã lưu ở `tmp/036/{worktree,main,queue}-before.txt`:

```sh
git -C games/.wt-td-vfx status --short --untracked-files=all
# Trống
git --no-optional-locks -C games/typing-defense status --short
# Trống
git status --short --untracked-files=all -- docs/codex-queue/
# ?? docs/codex-queue/035-report.md
```

## File đã viết hoặc sửa

- `games/.wt-td-vfx/src/view/fx-pipe.ts`: mới, `FxDraw`, `FxStats`, `FxPipe` và nguyên khối `FxView`.
- `games/.wt-td-vfx/src/view/fx-2d.ts`: chỉ bỏ khối chuyển đi và bốn import chỉ khối đó dùng; `Particles`, `Kind` giữ nguyên.
- `games/.wt-td-vfx/src/view/debug-2d.ts`: đúng sáu dòng chỉ định, import kiểu, `fx` có thể null, bốn lời gọi tùy chọn.
- `games/.wt-td-vfx/src/main.ts`: nối chunk, prefetch, `ready()`, `chunks()`, đọc sự kiện mỗi vòng update; thêm chín dòng theo numstat.
- `games/.wt-td-vfx/vite.config.ts`: chỉ thêm `fx-pipe` vào biểu thức `LAZY`.
- `games/.wt-td-vfx/tests/td-fx-pipe.test.ts`: mới, đúng năm ca, có quét AST, mẫu đối chứng trong bộ nhớ và ván vàng.
- `games/.wt-td-vfx/tmp/036/**`: script đo byte, JSON trước/sau, log build/check/golden/đột biến, bản sao để khôi phục và ảnh chụp trạng thái Git dạng văn bản; bị Git bỏ qua.
- `docs/codex-queue/036-report.md`: báo cáo này ở repo cha.

## Kiểm 1 — `pnpm check`

```sh
cd games/.wt-td-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm check > tmp/036/check-1.log 2>&1
```

Thoát **0 ngay lần đầu**, không cần chạy lại. Các dòng kết quả:

```text
src/kit OK: 31 files match kit-manifest.json (kit 0.1.0, modules platform, input, vocab, learning, tools, balance)
✓ tests/boundary.test.ts (17 tests)
✓ tests/td-fx-pipe.test.ts (5 tests)
Test Files  33 passed (33)
Tests  355 passed (355)
✓ built in 1.88s
bundle budget (BUILD_1B §20) /: start 83.85 kB gzip (entry + ui/title.ts) ≤ 85 kB, headroom 1.15 kB
bundle budget (BUILD_1B §20) /?title=0: start 82.40 kB gzip (entry + app/learn.ts) ≤ 85 kB, headroom 2.60 kB
```

Hai dòng bundle trên trích phần đầu; log giữ đầy đủ phần chunk tải sau. `tsc --noEmit`, `vite build` và hai cổng bundle đều đạt. Ba phép đo thời gian nêu trong phiếu không hỏng.

## Kiểm 2–3 — Byte và số dòng

Trong worktree, sau build của Kiểm 1:

```sh
node tmp/036/budget-bytes.mjs > tmp/036/after-bytes.json
cat tmp/036/after-bytes.json
```

```json
{"/":83848,"/?title=0":82398,"fxChunk":1961,"portraitInEntry":0,"portraitInFx":1}
```

| Mục | Trước | Sau | Thay đổi |
| --- | ---: | ---: | ---: |
| `/`, byte gzip | 84.975 | 83.848 | −1.127 |
| `/?title=0`, byte gzip | 83.525 | 82.398 | −1.127 |
| Chunk `fx-pipe`, byte gzip | Không có | 1.961 | Chunk mới |
| Số lần có `Tối Thượng!` trong entry | 1 | 0 | Đã chuyển ra |
| Số lần có `Tối Thượng!` trong chunk FX | Không có | 1 | Đúng một |
| Dòng TypeScript của `src`, trừ `src/kit` | 10.499 | 10.550 | +51, ≤ +75 |

Cả hai trang giảm byte so với nền. Các byte sau sửa khác nhẹ bản cài thử của Claude; đây là số đo thực, không ép khớp số tham khảo.

```sh
find src -name '*.ts' -not -path 'src/kit/*' -print0 | xargs -0 cat | wc -l
# 10550, ≤ 10574
```

Hai test trần dòng trong `boundary.test.ts` thuộc Kiểm 1 đều đạt; trần tài liệu là 10.900.

## Kiểm 4–5 — Ván vàng và số đếm

Trong worktree:

```sh
../../.local/bin/heavy.sh node --import tsx scripts/td/golden.ts --check > tmp/036/golden.log 2>&1
../../.local/bin/heavy.sh node --import tsx scripts/td/golden.ts --boss --check > tmp/036/golden-boss.log 2>&1
```

Cả hai thoát **0**. Dòng JSON đầy đủ ở hai log; các trường cần đối chiếu:

```text
golden:      "same":true, "content":"f2a21037", "ticks":19660, "problems":0, "rejected":0
golden boss: "same":true, "content":"f2a21037", "ticks":5695,  "problems":0, "rejected":0
```

Dòng in trong Kiểm 1 và lần kiểm sau khôi phục giống nhau, khớp toàn bộ bảng của phiếu:

```text
036 golden counts {"ticks":19660,"muzzle":133,"arrow":90,"shell":1,"bolt":11,"fireball":23,"wordShot":8,"feather":0,"hit":102,"crit":12,"stats":{"read":489,"fire":133,"hit":102,"lost":0}}
```

Test chỉ khẳng định các bất biến yêu cầu: danh sách lời gọi bằng đúng danh sách quét độc lập, không mất sự kiện, có `fireball`, `arrow`, `hit`. Số đếm cố định được đối chiếu trong báo cáo, không khóa trong test.

## Kiểm 6 — Chuyển nguyên văn và phạm vi dòng

Trong worktree:

```sh
node -e 'const {execFileSync}=require("child_process");const fs=require("fs");const old=execFileSync("git",["show","e49189a:src/view/fx-2d.ts"],{encoding:"utf8"});const block=old.slice(old.indexOf("/** A heal ring (0)")).trimEnd();console.log(block.length,fs.readFileSync("src/view/fx-pipe.ts","utf8").includes(block))'
# 7095 true
```

Từ repo cha:

```sh
git -C games/.wt-td-vfx diff --numstat e49189a -- src/view/fx-2d.ts src/view/debug-2d.ts vite.config.ts src/main.ts
```

```text
9       3       src/main.ts
6       6       src/view/debug-2d.ts
0       138     src/view/fx-2d.ts
1       1       vite.config.ts
```

Đúng hạn mức từng file. `git diff --check` cũng thoát 0, không in gì.

## Kiểm 7 — Hai đột biến

Bản tốt được chép bằng nội dung byte sang `tmp/036/fx-pipe.saved.ts` trước khi thử. Mỗi đột biến bắt đầu từ bản tốt, không chồng hai lỗi.

Lệnh đúng dùng cho từng lần chạy riêng file, trong worktree:

```sh
env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm exec vitest run tests/td-fx-pipe.test.ts
```

(a) Đổi điều kiện nhánh `FX.hit` thành `false`, nên bỏ qua hoàn toàn sự kiện trúng. Log: `tmp/036/mutation-a-targeted.log`. Thoát **1**, `Test Files 1 failed (1)`, `Tests 4 failed | 1 passed (5)`. Các ca hỏng:

- `1 reads fire and hit once, in ring order, ignoring other kinds`.
- `2 starts at creation and accounts for overwritten slots`.
- `3 returns a fresh stats copy and supports the default draw`.
- `5 matches an independent scan of the golden run`.

Ca 1, 2, 5 hỏng đúng yêu cầu. Ca 3 hỏng thêm vì kiểm bản sao thống kê sau một sự kiện bắn và một sự kiện trúng qua giao diện vẽ mặc định: đột biến làm `hit` từ 1 thành 0.

(b) Thêm `const probe = { n: 1 };` làm câu đầu trong thân vòng đọc. Log: `tmp/036/mutation-b.log`. Thoát **1**, `Test Files 1 failed (1)`, `Tests 1 failed | 4 passed (5)`. Chỉ ca sau hỏng, phát hiện `ObjectLiteralExpression`:

- `4 allocates nothing in read, with an in-memory positive control`.

Khôi phục và kiểm lại:

```sh
cp tmp/036/fx-pipe.saved.ts src/view/fx-pipe.ts
cmp src/view/fx-pipe.ts tmp/036/fx-pipe.saved.ts
# Không in gì; thoát 0
env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm exec vitest run tests/td-fx-pipe.test.ts > tmp/036/restored-test.log 2>&1
# Thoát 0; Test Files 1 passed (1); Tests 5 passed (5)
```

Mẫu đối chứng AST chỉ tồn tại trong chuỗi bộ nhớ; kết quả đúng `['ObjectLiteralExpression', 'ArrayLiteralExpression', 'call push', 'ArrowFunction']`. Với mã đã khôi phục, danh sách vi phạm là `[]`.

**Sai sót khi chạy lệnh:** lượt (a) đầu dùng `pnpm test -- tests/td-fx-pipe.test.ts`, thành `vitest run -- tests/td-fx-pipe.test.ts`; Vitest đã chạy cả 33 file thay vì chỉ file mới. Log giữ ở `tmp/036/mutation-a.log`: 32 file khác đạt, riêng file mới hỏng đúng bốn ca kể trên (351 đạt, 4 hỏng). Sau đó đã chạy lại riêng đúng một file với `pnpm exec vitest run ...`, là kết quả nghiệm thu (a). Không sửa file ngoài phạm vi để xử lý việc này.

## Kiểm 8–9 — Sim, phần khác và trạng thái Git

```sh
git -C games/.wt-td-vfx status --porcelain -- src/sim src/content src/kit src/typing src/ui src/app scripts tests/golden tests/td docs
# Không in gì; thoát 0
git -C games/.wt-td-vfx status --short --untracked-files=all
```

```text
 M src/main.ts
 M src/view/debug-2d.ts
 M src/view/fx-2d.ts
 M vite.config.ts
?? src/view/fx-pipe.ts
?? tests/td-fx-pipe.test.ts
```

Đúng sáu file của phiếu; `tmp/` và `dist/` bị bỏ qua. Worktree sạch trước phiếu.

```sh
git --no-optional-locks -C games/typing-defense status --short
# Không in gì cả trước lẫn sau; không có chênh lệch của làn a2-days tại lúc kiểm
git status --short --untracked-files=all -- docs/codex-queue/
```

```text
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
```

`035-report.md` đã có từ đầu và thuộc phiếu khác; phiếu này chỉ thêm `036-report.md`. Trạng thái sau lưu ở `tmp/036/{worktree,main,queue}-after.txt`; phạm vi không đổi ở `tmp/036/untouched-status.txt` (rỗng).

## Chỗ còn để Claude sửa

Các tham chiếu dưới đây chưa sửa theo phân công; số dòng trong worktree hiện tại:

- `src/view/debug-2d.ts:767`: `(its shadow: fx-2d.ts)` phải trỏ `fx-pipe.ts`.
- `src/view/boss-2d.ts:40`: `fx-2d.ts's FxView emits into it too` phải trỏ file mới.
- `AGENTS.md:161`: `FxView` trong `src/view/fx-2d.ts` phải đổi sang `fx-pipe.ts`.
- `AGENTS.md:175`: outcomes trong `view/fx-2d.ts` phải đổi sang `fx-pipe.ts`.
- `src/view/fx-2d.ts:5–8`: chú thích đầu file vẫn mô tả `FxView`, chân dung, bóng lông, vòng và kết quả lời gọi; chưa chỉnh để giữ diff chỉ gồm khối chuyển đi và import. Có thể chuyển mô tả này sang đầu `fx-pipe.ts` trong bước tài liệu của Claude.
- `docs/td/BUILD_NOTES.md:954`: mục lịch sử §7.3 ghi `FxView` trong `src/view/fx-2d.ts`; nếu cần chỉ dẫn hiện tại, thêm ghi chú chuyển file ở §7 thay vì viết lại lịch sử.
- `docs/td/BUILD_1B.md:623`: hàng ngân sách cũ vẫn gộp `Tối Thượng, gõ trực tiếp, hoảng` dưới `fx-2d.ts`; cân nhắc làm rõ ở bước cập nhật tài liệu.

`boss-2d.ts:13` và `AGENTS.md:142` nói pool hạt ở `fx-2d.ts` vẫn đúng. Các số dòng/hồ sơ cũ khác trong BUILD_NOTES là bằng chứng lịch sử, không coi là lỗi mã.

## Những lựa chọn và phần bỏ qua

- Không có điểm chưa rõ cần hỏi chủ dự án. Dùng nguyên cách nối chunk được chỉ định, chỉ đọc phần mới từ lúc tạo, giữ `FxView` và pool hạt nguyên văn.
- `read()` chụp số `written` đầu lần đọc vào một số vô hướng `end`; vòng đọc không cấp phát. AST kiểm thêm cả template không có nội suy và spread object để bao phủ lệnh cấm template/spread.
- Giữ chú thích đầu `fx-2d.ts`; chưa sửa chú thích/tài liệu cũ ngoài phạm vi. Không viết BUILD_NOTES §7 hay changelog, không commit: Claude làm sau nghiệm thu trình duyệt.
- Không mở cổng, dev server hay trình duyệt; không tạo ảnh/âm thanh; không cài gói hay dùng mạng. Không đụng Tu Tiên và các làn khác.

## Claude phải xem trước khi commit

- `td-1b-chunks` với chunk FX mới: `__td.ready()` đợi chunk settled và `__td.chunks()` có trường `fx`.
- Chân dung “Tối Thượng!” và mưa lông lửa trong `td-1b-ult`.
- Word Shot trúng, vòng và kết quả của lời gọi trực tiếp.
- Console không có lỗi.

Sau khi xem: sửa các tham chiếu cũ, ghi byte và số dòng vào BUILD_NOTES §7, viết changelog, rồi commit phiếu. Phần vẽ V4a trên `FxDraw` chỉ bắt đầu sau commit đó.

## Claude duyệt (28/10/2026)

**Nhận.** Commit trên nhánh `td-vfx` của `games/typing-defense` (worktree `games/.wt-td-vfx`), chưa gộp: `bc3d949` (mã và test của phiếu), `65cbcb7` (chú thích `debug-2d.ts`, `boss-2d.ts`, đầu `fx-2d.ts` và `fx-pipe.ts`, hai dòng `AGENTS.md` chỉ sang `fx-pipe.ts`), `48b5c99` (changelog `docs/changelog/2026-10-28-td-fx-pipe.md`, mục lục, `BUILD_NOTES.md` §7.11).

- Đọc diff: `FxPipe` đúng hợp đồng (con trỏ từ lúc tạo, phần tràn vào `lost`, một lời gọi mỗi `FX.fire`/`FX.hit`, `stats()` bản sao mới, `read` không cấp phát); `FxView` chuyển nguyên văn; `main.ts` nối chunk `fx` trong `prefetch`, `ready()` chờ nó, `chunks()` có `fx`; `debug-2d.ts` đúng 6 dòng.
- Chạy lại: `pnpm check` 355/355 test, 33 file, hai dòng ngân sách gói ("/" 83,85 kB, chừa 1,15 kB; "/?title=0" 82,40 kB); chạy lại sau commit chú thích: vẫn 355/355, 10.555 dòng. Hai ván vàng `"same":true`, `f2a21037`, 19.660 và 5.695 tick. Dòng `036 golden counts` khớp báo cáo. Đột biến (b) tự làm lại: chỉ ca 4 hỏng.
- Trình duyệt, 1280 × 720 và 1920 × 1080 (Vite riêng ở 4162, đã tắt): trong trang thật, bộ đọc của chính trang (bắt bằng cách bọc `FxPipe.prototype.read` trên máy chủ dev) thấy 14 lần bắn (11 cầu lửa của Draconis đúng chỗ đứng, 3 bolt) và 3 lần trúng, không mất, số đếm bằng số lời gọi; `td-1b-ult` 13/13, `td-1b-direct` 16/16, `td-1b-chunks` đạt ở cả hai cỡ; chân dung "Tối Thượng!", vỡ trống thành chữ, vòng hồi máu đều vẽ; thẻ chữ đọc được; không lỗi console ngoài lỗi của chunk bị chặn có chủ ý. Lượt `td-1b-ult` 720p đầu hỏng do Claude sửa `fx-pipe.ts` (thử đột biến) trong lúc nó chạy, chạy lại thì đạt.
- Lệch nhỏ so với phiếu, không ảnh hưởng: đột biến (a) hỏng thêm ca 3 (Codex đã ghi lý do); byte thật lệch bản cài thử 1–2 byte và chunk 1.961 thay vì 1.947.
- Lúc gộp: `BUILD_NOTES.md` §7.11 và mục lục changelog nằm ở phần cuối file mà làn `a2-days` cũng ghi; gộp tay. `main` của Lời Gọi chưa đi tiếp từ `ad4df6f` nên mã gộp thẳng được.
