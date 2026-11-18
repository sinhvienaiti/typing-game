# Phiếu 104b · Tuyến Cuối · Esc ở thẻ ải

TS-M1-18, cổng G5. Thực hiện trong `/Users/toandx/htdocs/typing-game/games/.wt-ts-codex`, nhánh `ts-codex`, HEAD `5b4c1b5`. Worktree sạch trước khi làm. Bốn mục kiểm bằng mã/lệnh đã đạt; kiểm trình duyệt bàn giao Claude.

## Đã làm

- `src/app/main.ts`: thêm import `introKey`, cập nhật chú thích guard `intro` của `act()`, sửa khối listener của thẻ ải cùng dấu nguồn qua lần tải trang. Esc quay về màn trước, được tiêu thụ trước `installKeys` và bỏ qua `audio.resume()`.
- `src/app/journey.ts`: thêm hàm thuần `introKey(key, from): "back" | "enter" | "none"`.
- `tests/intro-key.test.ts`: **22 test mới**, viết và chạy đỏ trước khi sửa mã. Ngoài hàm thuần, test lấy `act()` và khối listener thật từ `main.ts`, chạy cùng `Journey`/`installKeys` trong Node để kiểm luồng sự kiện và nguồn qua lần tải trang.
- [Changelog](../changelog/2026-10-29-card-esc.md) và bằng chứng ở [104b/](104b/).

Đã đọc cách Esc của Cài đặt (`leaveSettings()`), Kho súng (`show(back)`), Hành trình và nạp súng (`Journey.act()` → `escape()`). Bản sửa dùng lại chuyển màn và vẽ màn của `Journey`. Nhánh Esc ở thẻ không gọi âm chọn/quay lại vì yêu cầu không mở âm thanh.

## Phân biệt nguồn mở thẻ

`reload()` hiện có ghi lựa chọn sắp chơi vào `survival.next` rồi tải lại trang. Trong khối listener thẻ ải, `pagehide` ghi `survival.cardFrom` khi có lựa chọn chờ này:

| Màn trước khi rời trang | Nguồn lưu | Esc ở thẻ mới |
| --- | --- | --- |
| `journey.screen === "loadout"` | `loadout` | `mode = "start"`, `journey.stage = level`, chép `world.header.kit.guns` theo thứ tự, gọi `journey.loadout()` |
| Hành trình đang mở, hoặc màn kết quả khi replay | `journey` | Về Hành trình bằng `journey.open(level.id)` |
| URL mở thẳng, không có dấu nguồn hợp lệ | `direct` | `none`, giữ nguyên thẻ |

Dấu gồm nguồn và nguyên lựa chọn chờ (`stage`, tên khóa súng theo thứ tự). Trang mới đọc một lần rồi xóa ngay, đối chiếu với ải và bộ súng của thế giới vừa tạo. Dấu sai ải, đảo thứ tự súng hoặc JSON hỏng đều rơi về `direct`. Test kiểm cả việc dùng dấu đúng một lần. Replay một ải chương được đánh dấu `journey`; không dùng độ dài lịch sử trình duyệt để suy đoán nguồn.

Khi quay về nạp súng, Esc không đến listener gõ chữ hoặc menu nạp súng nên không lùi thêm về giới thiệu ải. Bộ súng được chép nguyên thứ tự; người chơi chọn tiếp và bắt đầu lại qua `Journey.begin()`/`reload()` hiện có. Chữ cái, Enter, Space, phím số, mũi tên, Tab vẫn vào trận như trước và phím mở màn không trở thành chữ gõ. Esc quay lại được cả khi tài nguyên chưa sẵn sàng.

## Bốn mục kiểm bắt buộc

| Mục | Trước | Sau / kết quả |
| --- | --- | --- |
| `pnpm check` | **159/159 test**, 17 file, exit 0 | **181/181 test**, 18 file, exit 0; kit **59 file**, typecheck và build xanh |
| `node --import tsx scripts/chapter-hashes.ts` | **152 dòng** | **152 dòng**, `diff -u` exit 0, **0 byte** |
| Đột biến Esc trả `enter` | Thay hàm thuần tạm thời bằng `return "enter"` | **9 đỏ, 13 xanh**, exit 1; khôi phục **22/22 xanh**, exit 0 |
| Phạm vi Git | Worktree sạch, HEAD `5b4c1b5` | `diff --stat` và `status --short -uall` chỉ có đường dẫn cho phép; `diff --check` xanh |

Test mới trước sửa: **15 đỏ, 7 xanh** (hàm mới chưa tồn tại và nhánh Esc chưa xử lý). Lượt `pnpm check` nền đầu tiên: **158 xanh, 1 đỏ** ở test hiệu năng cũ `survival-sim.test.ts`, đo **1,870875 ms**, ngưỡng **1,5 ms**. Sau đó chạy tuần tự từng file (`--maxWorkers 1 --no-file-parallelism`), cả nền lẫn sau sửa đều xanh. Không đổi test cũ hoặc nới ngưỡng. Build còn cảnh báo chunk trên 500 kB ở cả hai lượt xanh.

Để giới hạn đầu ra sinh tự động, [check-output.cjs](104b/check-output.cjs) được nạp bằng `NODE_OPTIONS`: tắt cache Vitest, dùng config loader `runner`, chạy từng file tuần tự; Vite ghi build vào `104b/check-output/`. Thư mục đầu ra này đã được xóa sau kiểm. Không đổi cấu hình dự án, không ghi đè `dist/` hay cache dự án. Chỉ chạy build nằm trong lệnh `pnpm check` bắt buộc của phiếu.

Lệnh chạy từ worktree:

```sh
NODE_OPTIONS="--require=$PWD/docs/codex-queue/104b/check-output.cjs" ../../.local/bin/heavy.sh pnpm check
../../.local/bin/heavy.sh --cores=1 node --import tsx scripts/chapter-hashes.ts
diff -u docs/codex-queue/104b/chapter-before.txt docs/codex-queue/104b/chapter-after.txt
```

Lệnh kiểm phạm vi chạy từ repo cha:

```sh
git -C games/.wt-ts-codex diff --stat
git -C games/.wt-ts-codex status --short -uall
git -C games/.wt-ts-codex diff --check
```

Bằng chứng: [nền lần đầu](104b/check-before.txt), [nền xanh tuần tự](104b/check-before-serial.txt), [sau sửa](104b/check-after.txt), [test trước mã](104b/test-red.txt), [test sau mã](104b/test-green.txt), [đột biến đỏ](104b/mutation-red.txt), [khôi phục xanh](104b/mutation-restored.txt), [hash trước](104b/chapter-before.txt), [hash sau](104b/chapter-after.txt), [diff hash rỗng](104b/chapter.diff.txt), [số liệu](104b/metrics.json), [diff stat](104b/diff-stat.txt), [status](104b/status-short.txt).

## Bỏ qua theo phạm vi và bàn giao

Không chạy dev server, trình duyệt hoặc tạo media; không sửa kit, sim, content, golden, cây chính, làn VFX hoặc Tu Tiên. Không chạy lệnh Git ghi. Test Node chưa xác nhận trải nghiệm trên trình duyệt.

Claude cần kiểm `survival-s1-loadout` ở **1280×720** và **1920×1080**: vào thẻ → Esc → nạp súng đúng ải, đúng bộ súng/thứ tự → đổi súng → bắt đầu lại → vào trận không có chữ gõ nhầm. Kịch bản hiện có đi từ thẻ vào trận bằng chữ `q`, chưa có bước Esc; cần kiểm bổ sung nhánh Esc trong lượt duyệt. Kiểm thêm replay về Hành trình và URL mở thẳng giữ thẻ khi Esc. Phiếu này không cho sửa `scripts/visual/` nên giữ nguyên kịch bản.
