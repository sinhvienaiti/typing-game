# Phiếu 018 · Tuyến Cuối · chép kit mới (số sát thương) và kiểm "86116"

**Bối cảnh:** `pnpm kit:check` ở repo cha báo `games/typing-survival` lệch kit ở 2 file: `src/kit/feedback/index.ts`, `src/kit/feedback/numbers.ts`. Làn Rồng Giữ Ải đã sửa `shared/game-kit` (parent `52bdc8df`, `fc69a921`, `df2f4882`, `21e8eaf9`). Theo bản sửa đó, hộp số tính theo mực chữ thật, `settle()` lặp tới khi không hai số nào chạm, và số không đi vào vùng cấm hay quá mép trên. Tuyến Cuối còn bản cũ, nên hai số của một lần nổ Pháo Sao chạm nhau, đọc thành "86116". Lỗi này ghi ở `games/typing-survival/docs/changelog/2026-10-26-feel-pass-s1.md` (dòng có "86116").

Chủ dự án (27/10) giao một phần việc nhỏ cho Codex và yêu cầu làm đúng, không sai sót. Mọi bước dưới đây có số kiểm. Claude chạy lại trước khi nhận.

**Thư mục làm việc:** `games/typing-survival`. Lệnh kit chạy ở gốc repo cha (`../..`).

**Được sửa:**
- `src/kit/**` (chỉ bằng lệnh sync, không sửa tay);
- mã game ở `src/view/**`, `src/app/**`, chỉ khi `pnpm check` hỏng vì API kit đổi, và sửa ít nhất có thể;
- `tests/**` khi test phải theo API mới;
- `tmp/codex-018/` (bằng chứng, không vào Git);
- `docs/codex-queue/018-report.md` ở repo cha (báo cáo).

**Cấm:**
- lệnh `git` có ghi (`add`, `commit`, `checkout`, `reset`, `restore`, `stash`, `push`…); chỉ được lệnh đọc `show`, `diff`, `log`, `archive`. Claude commit sau khi duyệt;
- sửa `src/sim/**`, `src/content/**`, `shared/game-kit/**`;
- sửa tay file trong `src/kit/`;
- đụng game khác, Tu Tiên, media (`media.md5`, ảnh, `.glb`).

## Việc

1. **Mã băm trước:** `pnpm exec tsx scripts/chapter-hashes.ts > tmp/codex-018/hashes-before.txt`. Phải ra đủ 152 dòng trận chương.
2. **Chép kit:** ở gốc repo cha chạy `node scripts/sync-game-kit.mjs --target games/typing-survival`, rồi `node scripts/sync-game-kit.mjs --check`. Dòng `games/typing-survival` phải là `OK`. Hai dòng `immortality-cultivation` (Tu Tiên) vẫn báo lệch: để nguyên. Ghi `diff -u` của hai file kit (bản cũ lấy từ `git show HEAD:src/kit/feedback/numbers.ts` …; chỉ đọc, không chạy lệnh git nào ghi) vào `tmp/codex-018/kit.diff`.
3. **`pnpm check`** trong `games/typing-survival`, qua khóa máy: `../../.local/bin/heavy.sh pnpm check`.
   - Nếu hỏng vì kit đổi API, đọc cách Rồng Giữ Ải đã theo: `games/dragon-hold`, commit `5187d76` và `e117ce0`. Muốn xem diff thì dùng `git -C ../dragon-hold show <sha>`; chỉ đọc. Ý chính của hai commit: đọc vùng cấm của số trước khi các bộ vẽ chạy, và dùng `NumberField` của kit.
   - Sửa tối thiểu trong `src/view` hoặc `src/app`, rồi chạy lại tới khi đạt.
   - Ghi số test.
4. **Mã băm sau:** chạy lại bước 1 ra `hashes-after.txt`. `diff hashes-before.txt hashes-after.txt` phải rỗng (sim không đổi).
5. **Trình duyệt.** Mỗi lệnh chạy qua `../../.local/bin/heavy.sh --gpu …`. Dev server riêng: `pnpm exec vite --host 127.0.0.1 --port 4290 --strictPort` (chạy nền); tắt khi xong.
   - `URL=http://127.0.0.1:4290/ OUT_DIR=tmp/codex-018/guns-<cỡ> SCENES=f6 GUNS=phao node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/survival-feel-guns.mjs --width=<w> --height=<h>`, ở 1280×720 và 1920×1080.
     - Tìm khung có hai số của cùng một lần nổ. Trước đây là `f6-phao-20.png`; tên có thể khác, thì tìm khung có hai số gần nhau nhất.
     - Cắt phóng to 4× vùng hai số, ra `tmp/codex-018/zoom-<cỡ>.png`.
     - Đo khe giữa mực hai số theo px (cột trống giữa hai vùng mực), ghi số.
   - `SCENES=f1,layout` của `scripts/visual/scenarios/survival-feel.mjs` ở hai cỡ: kiểm `noNumberOnProtected` vẫn đạt, và mọi kiểm khác giữ như trước. Chạy thêm một lượt trên `tmp/codex-018/base`: chép mã gốc ra bằng `git archive HEAD | tar -x -C tmp/codex-018/base` nếu được phép, không được thì so với số trong changelog.
   - 0 lỗi console, 0 ngoại lệ.
6. **Xem ảnh:** tự xem các ảnh zoom và ảnh `f1` ở hai cỡ. Số không chạm nhau, không đè dòng từ, bến, giáp, biển.

## Báo cáo `docs/codex-queue/018-report.md` (repo cha)

- Lệnh đã chạy, kèm đầu ra rút gọn của `--check`, `pnpm check` (số test), `diff` mã băm.
- Mọi file mã game đã sửa: lý do và số dòng.
- Bảng trình duyệt: cảnh × cỡ → đạt hay không, khe mực giữa hai số (px), lỗi console.
- Cái gì chưa chắc: ghi rõ, không đoán.

**Xong khi:** `--check` báo `typing-survival: OK`, `pnpm check` đạt, mã băm không đổi, hai số của một lần nổ có khe mực ≥ 2 px ở cả hai cỡ. Claude duyệt diff và commit.
