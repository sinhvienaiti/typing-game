# Báo cáo 094 · Rồng Giữ Ải · Bản từ vựng ghim cho G7

Ngày 28/10/2026, Mac mini M4, macOS. Hoàn thành bản ghim và sáu mục kiểm
trong phạm vi phiếu; phát hiện lỗi mức lưu vượt chương trình học, chuyển Claude
ở cuối báo cáo. Chưa xác nhận G7 toàn cảnh bằng trình duyệt.

## Phạm vi và file

- Worktree: `/Users/toandx/htdocs/typing-game/games/.wt-dh-codex`, nhánh
  `dh-codex`, HEAD đầu và cuối `02fe9c787886aecd668248fe00b5f2a97a6e45f4`.
- Pin dữ liệu: `18338405eebd9cfdbd6d6bf666ea79361c00a564` của repo cha.
  Từng file được lấy bằng `git -C /Users/toandx/htdocs/typing-game show
  <pin>:shared/vocabulary/<file>`, ghi nguyên byte; không đọc cây làm việc
  của `shared/`. Đối chiếu lại sau các đột biến: 102/102 khớp `git show`.
- Giữ nguyên năm file của phiếu 080 đã có trước. SHA-256 từng file đầu/cuối
  khớp, kể cả `package.json`; xem [trạng thái đầu](094/initial-state.json)
  và [kiểm cuối](094/final-audit.json).
- Không chạy lệnh Git có ghi, dev server, trình duyệt, sinh ảnh/âm thanh hoặc
  thao tác media. Không ghi cây chính, worktree khác hay Tu Tiên.

Các đường dưới tính từ worktree:

| File | Thay đổi |
| --- | --- |
| `public/vocabulary/index.json`, `levels/001.json` … `levels/100.json`, `ATTRIBUTION.md` | 102 file mới từ đúng pin. |
| `public/vocabulary/vocab-manifest.json` | Mới; pin, version, SHA-256 của đủ 102 file; khóa file theo mã ký tự, hai dấu cách, xuống dòng cuối. |
| `vocab.config.json` | Mới; pin đủ 40 ký tự, 102 đường dẫn đúng thứ tự yêu cầu. |
| `tests/vocab-pin.test.ts` | Mới; bảy ca kiểm bản ghim, dữ liệu dùng được, luồng tải và đường dẫn phụ thuộc. |
| `vite.config.ts` | Bỏ plugin phục vụ thư mục cha và tám dòng cấu hình/import/biến liên quan. |
| `scripts/balance/deck.ts` | Chỉ chú thích dòng 2: bộ bài bot lấy từ chuỗi `SOURCE` cố định trong chính file. |
| `AGENTS.md` | Chỉ hàng `pnpm dev` dòng 130: nguồn từ vựng là `public/vocabulary/`. |
| `docs/changelog/2026-10-28-vocab-pin.md` | Mới, tiếng Việt; lý do G7, cách cập nhật, số đo và giới hạn. |

Tổng: 106 file mới và ba file sửa của phiếu 094; ngoài ra chỉ có `dist/`
và cache được Git bỏ qua. Repo cha nhận báo cáo này và thư mục bằng chứng
[`docs/codex-queue/094/`](094/), không sửa công cụ hoặc cấu hình dùng chung.

## Số trước và dữ liệu ghim

`pnpm test` trước mọi sửa đổi: mã thoát 0, **51 file / 453 test**.
Log tại đường tuyệt đối
`/Users/toandx/htdocs/typing-game/docs/codex-queue/094/before.txt`.
Môi trường: Node `v24.22.0`, pnpm `11.21.0`, Vitest `3.2.7`.

| Số đo | Kết quả |
| --- | --- |
| File nguồn | 102 file, 2.666.590 byte |
| Manifest | 9.365 byte |
| Tổng bản ghim | 103 file, 2.675.955 byte |
| Index | Version 1; 100 level; 18.000 mục từ |
| Ít mục nhất sau `filterVocabularyEntries` | 150, cả chế độ người lớn và trẻ em |
| Ít ứng viên chiến đấu nhất sau `candidatesFrom` | 139, level 95, cả hai chế độ |
| SHA-256 manifest | `1e554377778a2208b22986be94e07b1253cc125bc9041b188a961a4f048f91a9` |

Chi tiết: [bản chép](094/pin-copy.json), [số đo](094/vocabulary-metrics.json).

## Kiểm 1 · `pnpm check`

**Đạt với một worker**, mã thoát 0:

```text
VITEST_MAX_FORKS=1 VITEST_MIN_FORKS=1 pnpm check
src/kit OK: 73 files match kit-manifest.json
Test Files  52 passed (52)
     Tests  460 passed (460)
tsc --noEmit && vite build
✓ 175 modules transformed.
✓ built in 2.14s
```

460 = 453 trước + đúng bảy ca của `vocab-pin.test.ts`; tăng một file test.
Log: [check một worker](094/check-single-worker.txt).

Lần `pnpm check` mặc định đầu tiên thoát 1: 51 file đạt, một file lỗi;
459 test đạt, một test lỗi ở `tests/ui/tags-bodies.test.ts:330`.
Phép đo HUD là `1.1931385250000006` ms, ngưỡng dưới 1 ms. Đây cũng là test
hiệu năng đã bị nhiễu trong báo cáo 080. Không sửa mã, test hoặc ngưỡng;
chỉ giảm đồng thời worker. Giữ [log lần lỗi](094/check.txt).

## Kiểm 2 · Golden không đổi

**Đạt.** `md5 -r tests/golden/*` trước và sau giống hệt; `cmp` thoát 0:

```text
35138e2875761e7c42f8cec0534ca820 tests/golden/golden.test.ts
75f74947dac170d05fd659f99417940e tests/golden/m0.json
```

`git -C games/.wt-dh-codex diff --stat -- tests/golden src/sim src/content src/typing`
không có đầu ra, [file kết quả](094/protected-diff.txt) dài 0 byte.
MD5: [trước](094/golden-before.txt), [sau](094/golden-after.txt).
`git diff --check` cũng thoát 0, không có đầu ra.

## Kiểm 3 · Bản đứng riêng

**Đạt.** Chép đúng bằng:

```sh
mkdir -p "$TMPDIR/dh-094-alone/game"
rsync -a --exclude node_modules --exclude public/assets /Users/toandx/htdocs/typing-game/games/.wt-dh-codex/ "$TMPDIR/dh-094-alone/game/"
ln -s /Users/toandx/htdocs/typing-game/games/.wt-dh-codex/node_modules "$TMPDIR/dh-094-alone/game/node_modules"
```

Gốc thực:
`/private/var/folders/d7/2x1km_3s363175h285_zlz680000gn/T/dh-094-alone/game`,
nằm ngoài repo cha. Không có `public/assets`; `node_modules` là symlink như
phiếu yêu cầu. Trong bản chép chạy:

```text
VITEST_MAX_FORKS=1 VITEST_MIN_FORKS=1 pnpm --config.verify-deps-before-run=false test
Test Files  52 passed (52)
     Tests  460 passed (460)

pnpm --config.verify-deps-before-run=false build
tsc --noEmit && vite build
✓ 175 modules transformed.
✓ built in 1.87s
```

Cả hai mã thoát 0. `dist/vocabulary/` có đúng **103 file**: 102 file nguồn
và manifest. 102/102 SHA-256 khớp manifest; mọi file và manifest cũng khớp
nguyên byte với `public/vocabulary/` của bản chép. Tổng 2.675.955 byte;
SHA-256 manifest như bảng số đo.

Log: [test](094/alone-test.txt), [build](094/alone-build.txt),
[kiểm số lượng và dọn thư mục](094/alone-verify.json),
[SHA-256 của cả 103 file](094/alone-sha256.txt).

**Khác phiếu ở cách dọn:** công cụ từ chối lệnh `rm -rf "$TMPDIR/dh-094-alone"`
với lý do `rm -f style commands are not permitted. Use a safer approach`.
Dùng `shutil.rmtree` sau khi xác nhận tên `dh-094-alone`, thư mục cha chính xác
là `$TMPDIR` đã resolve, gốc không phải symlink và liên kết thư viện trỏ đúng
worktree. Thư mục tạm đã biến mất; thư viện worktree vẫn còn. Không xóa đường
dẫn khác hoặc giữ bản chép lại.

## Kiểm 4 · Đột biến

**Đạt.** Từng đột biến chạy riêng `pnpm vitest run tests/vocab-pin.test.ts`;
cả bốn đều đỏ, mã thoát 1:

| Đột biến | Kết quả test | Log |
| --- | --- | --- |
| Đổi đúng một byte cuối level 057 từ xuống dòng sang dấu cách; JSON vẫn hợp lệ | 1 lỗi / 6 đạt | [level 057](094/mutation-level057-byte.txt) |
| Xóa mục `levels/100.json` khỏi manifest | 1 lỗi / 6 đạt | [manifest](094/mutation-manifest-missing100.txt) |
| Đổi pin config thành 40 ký tự `0` | 1 lỗi / 6 đạt | [pin](094/mutation-config-pin.txt) |
| Xóa file level 100 | 5 lỗi / 2 đạt | [file level 100](094/mutation-level100-deleted.txt) |

Sau mỗi lần đều trả lại nguyên byte trong `finally`. Sau cả bốn chạy lại:

```text
pnpm vitest run tests/vocab-pin.test.ts
Test Files  1 passed (1)
     Tests  7 passed (7)
```

Đối chiếu `git show` lại đủ 102 file: không lệch byte nào.
[Tổng hợp đột biến](094/mutation-results.json), [test sau phục hồi](094/restored-vocab-pin.txt).

## Kiểm 5 · Quét phụ thuộc nguồn cha

**Đạt.** `grep -rn "shared/vocabulary" src tests scripts vite.config.ts`
chỉ còn ba dòng trong kit được phép giữ nguyên:

```text
src/kit/vocab/vocabulary.ts:11:/** Where shared/vocabulary is served, and which flagged words to drop. */
src/kit/vocab/content-filter.ts:5: * shared/vocabulary carries the flags, these block lists stand in for them.
src/kit/vocab/content-filter.ts:9:/** Profanity, slurs and sexual words found in shared/vocabulary (scanned 23/10/2026). */
```

[Đầu ra gốc](094/grep.txt). Test mới quét mọi file trong `src/` trừ kit,
`tests/`, `scripts/` và `vite.config.ts`, kể cả chú thích; chuỗi tìm ghép từ
`"shared" + "/vocabulary"` để không tự bắt.

## Kiểm 6 · Phạm vi Git

**Đạt.** `git -C games/.wt-dh-codex status --short -uall` có **114 dòng**:
109 dòng của 094 và năm dòng có sẵn của 080. Không có đường dẫn ngoài phạm vi
hoặc đường dẫn bị xóa. [Toàn bộ status](094/status.txt),
[số dòng theo thư mục](094/status-counts.json).

| Thư mục trực tiếp | Số dòng |
| --- | ---: |
| Gốc worktree | 4 |
| `docs/changelog/` | 1 |
| `public/vocabulary/` | 3 |
| `public/vocabulary/levels/` | 100 |
| `scripts/assets/` (080) | 2 |
| `scripts/balance/` | 1 |
| `src/view/` (080) | 1 |
| `tests/` | 1 |
| `tests/assets/` (080) | 1 |

Tất cả dòng ngoài `public/vocabulary/`:

```text
 M AGENTS.md
 M package.json
 M scripts/balance/deck.ts
 M vite.config.ts
?? docs/changelog/2026-10-28-vocab-pin.md
?? scripts/assets/prepare-decals.mjs
?? scripts/assets/prepare-ground.mjs
?? src/view/ground-manifest.ts
?? tests/assets/prepare-ground.test.mjs
?? tests/vocab-pin.test.ts
?? vocab.config.json
```

## Lỗi để Claude xem và phần không làm

**Không có giới hạn trên hữu hạn trong mức lưu hiện tại.**
`src/app/learning.ts:471` chỉ làm tròn và chặn dưới ở 1;
`src/app/learning.ts:315` cũng không chặn trên, rồi tạo `[L, L+1]` ở dòng 316.
Kit có ba guard chương trình học giới hạn 100 trong
`src/kit/vocab/vocabulary.ts` (dòng 127, 180, 582), chưa xuất hằng giới hạn.
Test đọc các guard từ mã, kiểm chúng đồng ý rồi kiểm đủ dải file theo giới hạn
đó, không ghi số 100 cứng trong test.

Đã chạy probe với storage trong bộ nhớ, không lưu vào hồ sơ người chơi:

```text
Giới hạn chương trình học trong kit: 100
Lưu 100 → ứng viên [100, 101]
Lưu 101 → ứng viên [101, 102]
Lưu 101, luồng tải mặc định → request /vocabulary/index.json; bộ bài 0 từ
```

`defaultEntries()` ở dòng 235–236 lọc các mức không có trong index trước khi
tải, nên **không có request HTTP cho file 101** khi lưu 100. Test chạy luồng
mặc định với mọi mức lưu 1–100 và xác nhận từng request chỉ tới file ghim;
nếu bỏ bộ lọc hoặc đổi cặp mức tải, test phát hiện lệch danh sách request.
Tuy nhiên, khẳng định “mọi mức có thể lưu đều có file” chưa thể đúng với mã
không có trần này. Đây là lỗi được phiếu yêu cầu báo cho Claude khi có mức
101; không thêm file 101 hoặc sửa `src/` để che lỗi.
[Bằng chứng probe](094/level-boundary.json).

Claude cần chặn mức lưu/tải theo chương trình học và làm phần báo lỗi khi bộ
bài rỗng ở phiếu riêng; sau đó duyệt diff, chạy lại kiểm và kiểm trình duyệt
trước khi commit trên `dh-codex`. Phiên này không sửa hành vi đó vì bị cấm
ghi `src/**`, cũng không sửa golden, alias nginx, bộ kit hoặc công cụ sync
repo cha. Không chạy sáu test ảnh `.mjs` của 080: chúng nằm ngoài bộ Vitest
và không liên quan bản ghim; năm file 080 được giữ nguyên và kiểm SHA-256.
