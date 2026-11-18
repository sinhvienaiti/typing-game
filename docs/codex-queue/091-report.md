# Phiếu 091 — Lời Gọi: bản chép từ vựng ghim trong repo game

Ngày 28/10/2026, Mac mini M4/macOS. **Hoàn tất sáu mục Kiểm của phiếu 091.**
Đây là phần từ vựng của cổng G7; không kết luận thay cho các phần production khác.

## Phạm vi và trạng thái

- Repo cha: `/Users/toandx/htdocs/typing-game`, HEAD quan sát ban đầu `15b675b5`.
- Mã: `games/.wt-td-codex`, nhánh `td-codex`, HEAD trước và sau
  `a5cc1476de934ed3034fc861d6351b232cf00bb5`; đầu phiên worktree sạch.
- Node `v24.22.0`, pnpm `11.21.0`, Python `3.9.6`, Vitest `3.2.7`.
- Nguồn duy nhất của bảy file: `git show 18338405eebd9cfdbd6d6bf666ea79361c00a564:shared/vocabulary/<file>`
  ở repo cha. Không đọc cây làm việc `shared/`. Đã đối chiếu lại từng byte với `git show` sau khi phục hồi đột biến.
- Không có lệnh Git ghi, commit hoặc push; không sửa `src/`, kit, golden, repo game chính hay game khác.
  Các thay đổi có sẵn của tác vụ khác ở repo cha được giữ nguyên.

## File đã đổi và mới

Mọi đường dẫn mã sau tính từ `games/.wt-td-codex/`:

| File | Thay đổi |
|---|---|
| `public/vocabulary/index.json` | Mới, đúng byte commit ghim, version 1 |
| `public/vocabulary/levels/001.json` đến `005.json` | Năm file mới, đúng byte commit ghim |
| `public/vocabulary/ATTRIBUTION.md` | Mới, giữ nguyên nguồn và giấy phép |
| `public/vocabulary/vocab-manifest.json` | Mới, pin/version/SHA-256, thứ tự khóa đúng phiếu |
| `vocab.config.json` | Mới, pin đủ 40 ký tự, bảy đường dẫn theo đúng thứ tự phiếu |
| `tests/vocab-pin.test.ts` | Mới, 5 ca: file/hash, pin/version, đủ level, hash bộ bài, quét phụ thuộc |
| `tests/td/typing.ts` | Chỉ sửa chú thích đầu file và URL đọc level sang `../../public/vocabulary/levels/` |
| `scripts/td/replay.ts` | Chỉ sửa câu chú thích và URL đọc level tương tự |
| `vite.config.ts` | Bỏ plugin mount cùng import và hằng `root` chỉ plugin dùng; giữ `env` |
| `AGENTS.md` | Chỉ hai dòng 257–258: Vite phục vụ bản ghim ở `public/vocabulary/` |
| `docs/changelog/2026-10-28-vocab-pin.md` | Mới, lý do G7, thay đổi, cách cập nhật pin và số đo |

Repo cha chỉ thêm báo cáo này và bằng chứng trong [091/](091/). `dist/` và cache dependency
là đầu ra được phép, bị Git bỏ qua.

Bảy file nguồn **123.831 byte**, manifest **720 byte**, cộng **124.551 byte**.
Manifest version **1**, pin `18338405eebd9cfdbd6d6bf666ea79361c00a564`.
Hash bộ bài thật sau `filterVocabularyEntries` rồi `deckFromLevels`: **`9f36cfeb`**.
Test quét mọi file trong `src/` (bỏ `src/kit/**`), `tests/`, `scripts/`, kể cả chú thích;
chuỗi tìm được ghép từ hai phần để không tự bắt chính test.

## Kiểm 1 — `pnpm check`

Đo trước bằng `pnpm test`, rồi `pnpm td:golden:check`, trong worktree.
Log đúng đường tuyệt đối yêu cầu:
`/Users/toandx/htdocs/typing-game/docs/codex-queue/091/before.txt`.

Trích đầu ra trước:

```text
 Test Files  32 passed (32)
      Tests  350 passed (350)
Exit code: 0
Exit code: 0
```

Trích đầu ra sau, `pnpm check`:

```text
src/kit OK: 31 files match kit-manifest.json (kit 0.1.0, modules platform, input, vocab, learning, tools, balance)
 Test Files  33 passed (33)
      Tests  355 passed (355)
✓ built in 1.44s
bundle budget (BUILD_1B §20) /: start 84.91 kB gzip (entry + ui/title.ts) ≤ 85 kB, headroom 0.09 kB; later 16.80 kB (app/dev-tools.ts 1.51, app/learn.ts 3.22, app/retry.ts 1.01, app/sandbox.ts 0.93, ui/profile.ts 0.95, ui/settings.ts 1.31, ui/sheets.ts 2.26, ui/tips.ts 1.16, view/audio-min.ts 4.44); total 101.70 kB
bundle budget (BUILD_1B §20) /?title=0: start 83.46 kB gzip (entry + app/learn.ts) ≤ 85 kB, headroom 1.54 kB; later 18.25 kB (app/dev-tools.ts 1.51, app/retry.ts 1.01, app/sandbox.ts 0.93, ui/profile.ts 0.95, ui/settings.ts 1.31, ui/sheets.ts 2.26, ui/tips.ts 1.16, ui/title.ts 4.67, view/audio-min.ts 4.44); total 101.70 kB
Exit code: 0
```

**350 → 355 test = 350 + 5 ca mới; 32 → 33 file** vì có thêm `vocab-pin.test.ts`.
Kit 31/31 file khớp, TypeScript và Vite build đạt, hai ngân sách gói đều đạt.
Đầu ra đầy đủ: [before.txt](091/before.txt), [check-after.txt](091/check-after.txt).

## Kiểm 2 — Golden và diff rỗng

`pnpm td:golden:check` trước và sau đều exit **0**; cả hai lượt phát lại có `same: true`,
`changed: {}`, `firstMovedAtTick: null`. Đầu ra sau:

```json
{"same":true,"changed":{},"firstMovedAtTick":null,"content":"f2a21037","deck":"9c9b91d8","ticks":19660,"commands":389,"problems":0,"rejected":0,"summary":{"kills":51,"livesLost":4,"wavesCleared":3,"calls":64,"callWords":66,"callsPerfect":21,"keys":318,"keyErrors":14,"gold":29.8,"wood":87,"food":29,"bossDamage":0,"bossRetreats":0,"lives":16,"ultCasts":1,"ultFeathers":22,"directOk":0,"directMissed":1,"reviewBack":7,"reviewRedeemed":5,"freshWords":8}}
{"same":true,"changed":{},"firstMovedAtTick":null,"content":"f2a21037","deck":"9c9b91d8","ticks":5695,"commands":49,"problems":0,"rejected":0,"summary":{"kills":9,"livesLost":2,"wavesCleared":0,"calls":15,"callWords":9,"callsPerfect":4,"keys":39,"keyErrors":3,"gold":416.6,"wood":160,"food":18,"bossDamage":2110,"bossRetreats":1,"lives":18,"ultCasts":1,"ultFeathers":21,"directOk":0,"directMissed":0,"reviewBack":0,"reviewRedeemed":0,"freshWords":0}}
```

```text
$ git -C games/.wt-td-codex diff --stat -- tests/golden
```

Không có đầu ra (**0 byte**), exit **0**. Không chạy `td:golden:update`.
Hash deck `9c9b91d8` trong golden là deck chữ đã lưu của golden; ca hash `9f36cfeb`
kiểm riêng bộ từ vựng thật vừa chép, đúng mục đích phiếu.
Log: [golden-after.txt](091/golden-after.txt), [golden.diff-stat.txt](091/golden.diff-stat.txt).

## Kiểm 3 — Đứng riêng ngoài repo cha

Thư mục đã dùng: `/var/folders/d7/2x1km_3s363175h285_zlz680000gn/T/td-091-alone/game`.
Đã kiểm đường dẫn nằm ngoài repo cha và `../../shared` không tồn tại. Chép worktree
bỏ `node_modules`, `.git`, `dist` cũ; nối `node_modules` bằng symlink tới dependency của worktree.

```text
$ pnpm --config.verify-deps-before-run=false test
 Test Files  33 passed (33)
      Tests  355 passed (355)
Exit code: 0
$ pnpm --config.verify-deps-before-run=false build
✓ built in 591ms
bundle budget (BUILD_1B §20) /: start 84.91 kB gzip (entry + ui/title.ts) ≤ 85 kB, headroom 0.09 kB; later 16.80 kB (app/dev-tools.ts 1.51, app/learn.ts 3.22, app/retry.ts 1.01, app/sandbox.ts 0.93, ui/profile.ts 0.95, ui/settings.ts 1.31, ui/sheets.ts 2.26, ui/tips.ts 1.16, view/audio-min.ts 4.44); total 101.70 kB
bundle budget (BUILD_1B §20) /?title=0: start 83.46 kB gzip (entry + app/learn.ts) ≤ 85 kB, headroom 1.54 kB; later 18.25 kB (app/dev-tools.ts 1.51, app/retry.ts 1.01, app/sandbox.ts 0.93, ui/profile.ts 0.95, ui/settings.ts 1.31, ui/sheets.ts 2.26, ui/tips.ts 1.16, ui/title.ts 4.67, view/audio-min.ts 4.44); total 101.70 kB
Exit code: 0
```

**33/33 file, 355/355 test; build exit 0.** Đây là 32 file/350 test gốc cộng một file/5 ca mới.
Không gọi `pnpm test` trơn trên symlink. `dist/vocabulary/` có đúng bảy file nguồn cộng
`vocab-manifest.json`; toàn bộ nội dung trùng byte bản ghim trong worktree.

| File trong `dist/vocabulary/` | Byte | SHA-256 |
|---|---:|---|
| `ATTRIBUTION.md` | 3,101 | `8f162dc2d3a977ab521537d3fdd770ca200bec144623854dbba95301d65c9269` |
| `index.json` | 12,195 | `a0cbb72a84bf8d224d203df5891461b25230807248627e60018070dec4ff9b9b` |
| `levels/001.json` | 17,371 | `75857e4a581f33dbbbb366e820cc28c68ca25206a748558d09af7231dc40096f` |
| `levels/002.json` | 18,046 | `d775598e98c47926d6f56079e98ba448db4029367dfa669cf3e5a7e6c200c07c` |
| `levels/003.json` | 18,363 | `b3ab7ad8a63b08323ddff1230f485d6f8ab00cd893cebaf35d73b9a973dbff31` |
| `levels/004.json` | 26,688 | `766386de1dc7cbbefa71d0edb66d3c537c704b37f63845109fa37824f6fce3a1` |
| `levels/005.json` | 28,067 | `0781d04d0df20229d772c875d51cd88852139e7117e08146c6c9186bccc79fed` |
| `vocab-manifest.json` | 720 | `f92b36089e7ddc04898d38401808bfb261ad36f00647cfdee45a9c58123fcdbb` |

Đã xóa toàn bộ `$TMPDIR/td-091-alone`; dependency gốc của worktree còn nguyên.
Log: [alone-test.txt](091/alone-test.txt), [alone-build.txt](091/alone-build.txt),
[alone-summary.json](091/alone-summary.json), [cleanup.txt](091/cleanup.txt).

## Kiểm 4 — Ba đột biến đều bị bắt

Mỗi lần chỉ sửa một đích, chạy đúng `pnpm vitest run tests/vocab-pin.test.ts`,
rồi phục hồi byte gốc trong `finally` trước khi sang đột biến kế tiếp.

| Đột biến | Đầu ra | Exit | Ca bắt lỗi |
|---|---|---:|---|
| Đổi một byte khoảng trắng thành tab trong `levels/004.json`, JSON vẫn hợp lệ | `Test Files 1 failed (1); Tests 1 failed, 4 passed (5)` | 1 | SHA-256 không khớp |
| Xóa mục `ATTRIBUTION.md` khỏi `manifest.files` | `Test Files 1 failed (1); Tests 1 failed, 4 passed (5)` | 1 | Manifest thiếu một khóa trong bảy file bắt buộc |
| Đổi ký tự đầu của pin trong config từ `1` sang `0`, vẫn đủ 40 hex | `Test Files 1 failed (1); Tests 1 failed, 4 passed (5)` | 1 | Pin manifest khác config |

Đổi byte khoảng trắng giữ nguyên nội dung bộ bài, chứng minh kiểm SHA-256 bắt được lệch byte
ngay cả khi ca deck hash vẫn xanh. Sau phục hồi:

```text
 Test Files  1 passed (1)
      Tests  5 passed (5)
Exit code: 0
```

Log: [mutation-level-004-byte.txt](091/mutation-level-004-byte.txt),
[mutation-manifest-attribution.txt](091/mutation-manifest-attribution.txt),
[mutation-config-pin.txt](091/mutation-config-pin.txt),
[vocab-pin-restored.txt](091/vocab-pin-restored.txt), [mutations.json](091/mutations.json).

## Kiểm 5 — Chỉ kit còn chuỗi đường dẫn cũ

Đầu ra nguyên văn trong worktree:

```text
$ grep -rn "shared/vocabulary" src tests scripts vite.config.ts
src/kit/vocab/vocabulary.ts:11:/** Where shared/vocabulary is served, and which flagged words to drop. */
src/kit/vocab/content-filter.ts:5: * shared/vocabulary carries the flags, these block lists stand in for them.
src/kit/vocab/content-filter.ts:9:/** Profanity, slurs and sexual words found in shared/vocabulary (scanned 23/10/2026). */
```

Exit **0**, đúng **3 dòng**, tất cả trong `src/kit/**`; không sửa kit.
Log: [grep.txt](091/grep.txt).

## Kiểm 6 — Phạm vi Git

Đầu ra nguyên văn:

```text
$ git -C games/.wt-td-codex status --short -uall
 M AGENTS.md
 M scripts/td/replay.ts
 M tests/td/typing.ts
 M vite.config.ts
?? docs/changelog/2026-10-28-vocab-pin.md
?? public/vocabulary/ATTRIBUTION.md
?? public/vocabulary/index.json
?? public/vocabulary/levels/001.json
?? public/vocabulary/levels/002.json
?? public/vocabulary/levels/003.json
?? public/vocabulary/levels/004.json
?? public/vocabulary/levels/005.json
?? public/vocabulary/vocab-manifest.json
?? tests/vocab-pin.test.ts
?? vocab.config.json
```

**15 file thay đổi/mới**, tất cả thuộc danh sách được phép. `git diff --check` exit **0**,
không có đầu ra. HEAD không đổi. Log: [status.txt](091/status.txt),
[scope-check.txt](091/scope-check.txt), [diff-check.txt](091/diff-check.txt), [head.txt](091/head.txt).

## Khác phiếu và phần để lại

- Số byte thực tế từ commit ghim là **123.831**, ít hơn thiết kế §4 một byte:
  `levels/001.json` **17.371** thay vì 17.372. Không sửa byte nguồn để khớp số cũ.
- Bản chép đứng riêng bỏ thêm metadata `.git` và đầu ra `dist` cũ, để không mang liên kết Git
  tới repo cha và để kiểm đúng đầu ra build mới. Toàn bộ mã, test, config và nội dung public được chép.
- Công cụ thực thi từ chối lệnh `rm -rf "$TMPDIR/td-091-alone"` với lý do
  `rm -f style commands are not permitted. Use a safer approach`. Thay bằng
  `shutil.rmtree` đúng thư mục đó sau khi kiểm phạm vi, thư mục gốc không phải symlink
  và `game/node_modules` là symlink. Không xóa riêng `node_modules`; đã xác nhận dependency gốc còn nguyên.
- Không làm phần hạ tầng nginx, công cụ sync ở repo cha, portal origin, deploy, media hay browser;
  các phần này ngoài phạm vi phiếu hoặc bị cấm. Không có ảnh/âm nên không sinh prompt/media.
- Không cần quyết định thêm từ chủ dự án cho phạm vi này. Claude cần chạy lại kiểm, duyệt diff,
  rồi tự commit trên `td-codex` và gộp vào `a2-days` theo quy trình của phiếu.
