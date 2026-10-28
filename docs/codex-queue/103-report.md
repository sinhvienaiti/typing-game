# Phiếu 103 — Lời Gọi: thẻ kết và dải nghĩa lúc rời đi

Thực hiện ngày **28/10/2026**, Mac mini M4; repo cha
`/Users/toandx/htdocs/typing-game`, mã trong `games/.wt-td-codex`, nhánh
`td-codex`. HEAD trước và sau: `034e86f269352687b3c2e425958a9729df0ecc87`
(phiếu 091 đã được Claude commit). Worktree trước khi làm sạch.

**Kết quả:** A6 đã sửa; A8 tách hộp cột thuần và sửa lỗi chồng dải nghĩa
ở cột đông. Sáu mục kiểm bằng lệnh đều đạt, giữ cả hai trần. Cảnh Đêm 3
trong ảnh kiểm kê cần Claude kiểm lại bằng trình duyệt trước khi nhận.

## File đã đổi

Tính từ worktree:

- `src/ui/sheets.ts`: điều kiện hiện Knowledge.
- `src/view/words/lanes.ts`: hàm thuần `columnBox`, rút gọn chú thích đầu file.
- `src/view/words/cards.ts`: dùng hộp thuần khi tách cột và đặt thẻ.
- `tests/td-sheet-cards.test.ts`: **8 ca mới**.
- `docs/changelog/2026-10-29-sheet-cards.md`: changelog tiếng Việt.

Tại repo cha: báo cáo này và [thư mục log, số đo](103/), gồm script chạy
lại bốn đột biến [run-mutations.py](103/run-mutations.py).

## Cách sửa và đối chiếu mã hiện tại

**A6:** `Sheet.show(kind, w, run)` đã nhận `w: World`, có `w.mode: Mode`
(`src/sim/world.ts`). Dùng trực tiếp `w.mode === "learn" || w.knowledge > 0`.
`src/app/retry.ts` cũng dùng `Mode` cho `RunOf.mode`; nơi dựng thẻ kết hiện
truyền World tại `src/main.ts:314`. Không cần thêm mode vào `ResultsOf`,
sửa nơi gọi hay đọc lại mode từ cài đặt. Ba ca yêu cầu kiểm cả kết thắng
và kết thua: Cân bằng/0 ẩn; Học/0 hiện; Thử thách/3 hiện đúng giá trị.

**A8 — khác mô tả phiếu ở mã hiện tại:** `WordCards.draw` đã đưa các thẻ
`mean` còn hạn vào `lanes`, gồm cột riêng khi lời gọi kết thúc. Hai thẻ
thông thường cùng cột đã được giãn theo chiều cao. Không thêm lại một
lần nữa. Lỗi xác nhận được bằng test là `columnHeights` chặn độ cao ở
`COLUMN.max = 240`: một thẻ 58 px và năm dải nghĩa 34 px cho vị trí
`[0, 74, 148, 222, 240, 240]`, hai dải cuối nằm cùng chỗ.

Tách phần tính hộp sang `columnBox(cards, lock)`, nhận kích thước đo thật
của mọi thẻ. Phép xếp thẻ đã đo dùng `[0, 74, 148, 222, 296, 370]`; nửa
bề rộng của dải nghĩa cũng đi vào hộp tách cột. Phần tính chiều cao và
bề rộng khi khóa được chuyển nguyên hành vi; slot −1 không bị khóa khi
`lock = -1`. Giữ nguyên thuật toán tách ngang, các vùng tránh HUD/hành
động, hàm thuần `columnHeights` cũ, `MS.mean = 1000`, chữ và màu.

Không khẳng định đã tái hiện bằng mắt đúng ảnh “kind” dưới “walk” ở Đêm 3;
phiếu cấm server và trình duyệt. Đây là phần Claude cần đối chiếu lại.

## Kiểm 1 — Test trước, mã sau; tsc

| Lượt | File đạt | Test đạt | Test đỏ | Exit |
|---|---:|---:|---:|---:|
| `pnpm test` trước | 33 | 355 | 0 | 0 |
| Thêm test, chưa sửa mã; `pnpm vitest run tests/td-sheet-cards.test.ts` | 0/1 | 2 | 6 | 1 |
| Test đích sau sửa | 1 | 8 | 0 | 0 |
| `pnpm test` sau, đã phục hồi đột biến | 34 | **363 = 355 + 8** | 0 | 0 |
| `pnpm exec tsc --noEmit` sau | — | — | 0 lỗi | 0 |

Lượt đỏ có một ca A6, ba ca gọi hàm thuần chưa tồn tại, và **hai ca `draw`
tái hiện chồng hộp thật trong logic hiện tại** ở chiều rộng 1280/1920.
Hai ca A6 còn lại đã xanh trước sửa. Các test layout dùng node DOM giả và
kích thước cố định, không phải ảnh render hay nghiệm thu trình duyệt.

Các ca A8 thuần kiểm cặp thẻ, cột đông và tách ngang cột lân cận bằng
toàn bộ hộp dải nghĩa. Hai ca `draw` kiểm vị trí tại 0/500/999 ms, dải
nghĩa vẫn `mean`, tới 1000 ms chuyển `fold` đúng hạn.

Log: [test trước](103/test-before.txt), [test đỏ](103/test-red.txt),
[test đích](103/test-targeted.txt), [test sau](103/test-after.txt),
[tsc sau, rỗng 0 byte](103/tsc-after.txt).

## Kiểm 2 — Golden giống hệt

`pnpm td:golden:check` trước và sau đều exit **0**. Hai JSON kết quả trùng
nhau từng byte: `same: true`, `changed: {}`, `firstMovedAtTick: null`.

| Golden | Ticks | Commands | Problems | Rejected | Content | Deck |
|---|---:|---:|---:|---:|---|---|
| Thường | 19.660 | 389 | 0 | 0 | `f2a21037` | `9c9b91d8` |
| Boss | 5.695 | 49 | 0 | 0 | `f2a21037` | `9c9b91d8` |

`git diff -- tests/golden` rỗng. Không chạy lệnh cập nhật golden.
Log: [trước](103/golden-before.txt), [sau](103/golden-after.txt),
[đối chiếu](103/verification.json), [diff golden](103/golden.diff.txt).

## Kiểm 3 — Build và gzip

`pnpm build` trước và sau đều exit **0**, gồm `tsc --noEmit`, Vite và
`scripts/bundle-budget.mjs`. Script repo tính gói `/` bằng tập import
tĩnh của entry và `src/ui/title.ts`, gzip từng file rồi cộng, trần
**85.000 byte**. Đo byte chính xác từ cùng manifest sau mỗi build:

| Thành phần `/` | Trước | Sau | Chênh |
|---|---:|---:|---:|
| Entry gzip | 80.239 byte | 80.190 byte | −49 |
| Title gzip | 4.667 byte | 4.667 byte | 0 |
| **Gói `/` gzip** | **84.906 byte (84,91 kB)** | **84.857 byte (84,86 kB)** | **−49** |
| Còn dưới trần | 94 byte | **143 byte** | +49 |

Gói `/?title=0` cũng đạt: **83,46 → 83,41 kB** gzip.
Log: [build trước](103/build-before.txt), [build sau](103/build-after.txt),
[byte trước](103/bundle-before.json), [byte sau](103/bundle-after.json).

## Kiểm 4 — Trần dòng TypeScript

Dùng đúng quy tắc `codeLines` trong **`tests/boundary.test.ts`**: mọi
`src/**/*.ts` trừ `src/kit/**`, đếm ký tự newline như `wc -l`; không tính
test, script, tài liệu. Hai test trần dòng trong file này cũng xanh.

| Phạm vi | Trước | Sau | Chênh |
|---|---:|---:|---:|
| `src/ui/sheets.ts` | 132 | 132 | 0 |
| `src/view/words/cards.ts` | 278 | 275 | −3 |
| `src/view/words/lanes.ts` | 87 | 89 | +2 |
| **81 file TypeScript game** | **10.499** | **10.498** | **−1** |

Trần **10.500**, còn **2 dòng**. Rút gọn chú thích đầu `lanes.ts` bảy
dòng, không đổi hành vi; phần logic lặp ở `cards.ts` được chuyển sang
hàm thuần. Số đo và SHA-256 file của 091: [trước](103/before.json),
[sau](103/after.json).

## Kiểm 5 — Đột biến

Mỗi lần chỉ sửa một file, chạy `pnpm vitest run tests/td-sheet-cards.test.ts`,
rồi phục hồi byte gốc trong `finally`; SHA-256 sau phục hồi được lưu.

| Đột biến | Đỏ | Xanh | Exit | Log |
|---|---:|---:|---:|---|
| Bỏ điều kiện mode, chỉ còn `knowledge > 0` | 1 | 7 | 1 | [a6-mode](103/mutation-a6-mode.txt) |
| Hiện dòng Knowledge vô điều kiện | 1 | 7 | 1 | [a6-unconditional](103/mutation-a6-unconditional.txt) |
| Bỏ lệnh đưa thẻ `mean` vào cột trước layout | 2 | 6 | 1 | [a8-omit-mean](103/mutation-a8-omit-mean.txt) |
| Chặn lại độ cao ở 240 px | 3 | 5 | 1 | [a8-rise-cap](103/mutation-a8-rise-cap.txt) |

**4/4** đột biến bị bắt. Toàn bộ test sau phục hồi **363/363**.
Số đo: [mutations.json](103/mutations.json).

## Kiểm 6 — Phạm vi và giữ 091

`git -C games/.wt-td-codex status --short -uall` sau cùng:

```text
 M src/ui/sheets.ts
 M src/view/words/cards.ts
 M src/view/words/lanes.ts
?? docs/changelog/2026-10-29-sheet-cards.md
?? tests/td-sheet-cards.test.ts
```

**5 file**, đều nằm trong danh sách được ghi. 091 đã ở HEAD nên không còn
file bẩn của 091 trong status; SHA-256 của toàn bộ file nguồn/config/test
và bản ghim từ vựng đã ghi nhận trước vẫn khớp sau sửa. HEAD không đổi.
`git diff --check` exit **0**, đầu ra **0 byte**. Không sửa kit, golden,
cây chính của game, game khác, scripts/config repo cha hoặc media.
Log: [status](103/status.txt), [scope](103/scope-check.json),
[diff check](103/diff-check.txt), [verification](103/verification.json).

## Phần để lại cho Claude

- Không mở dev server, preview hay trình duyệt, đúng giới hạn phiếu.
- Chạy lại sáu kiểm, đọc diff; chạy **`td-1b-story`, `td-theme` và Đêm 3 ở
  1280/1920**. Đối chiếu lại dải “kind · loại, hạng, kiểu” với “walk”,
  gồm lúc khóa thẻ, lúc lời gọi còn và đã kết thúc.
- Cột đông có thể cao hơn 240 px để giữ đủ hộp; cần xem mép trên trong
  cảnh thật. Chưa có bằng chứng ảnh để nhận A8 ở đúng cảnh kiểm kê.
- Không commit hay merge; Claude thực hiện sau khi nghiệm thu.
