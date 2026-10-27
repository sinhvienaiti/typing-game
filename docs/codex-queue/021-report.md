# Phiếu 021 · Lời Gọi · 5 việc nhỏ sau đợt test 27/10

**Kết quả:** đã sửa 4 việc trong 4 file được giao; việc 4 đã đo, cổng 5b **trượt: 29,5 %**, riêng Ngày 4 **29 %**. Cây cuối qua `pnpm check` (**346/346 test**, 32 file) và golden (**hai file `same: true`**). Gói `/` **84,99 kB gzip**, đúng **84.993 byte / 85.000**, còn **7 byte**; TypeScript **10.500 / 10.500 dòng**. **Chưa nghiệm thu trình duyệt**: sandbox chặn cổng riêng 4292 bằng `EPERM`; không có ảnh mới, số đo DOM thật hoặc file tải xuống thật của lượt này.

Làm sau [báo cáo 019](019-report.md). Repo con ban đầu sạch, HEAD `aa87ecac05391162e933a756ee9c6b1c6960fdf6`, đúng mốc đã kiểm của 019. Đường dẫn `src/...` và lệnh dưới đây tính từ `games/typing-defense`; bằng chứng `E/` là [tmp/codex-021](../../games/typing-defense/tmp/codex-021/). Chỉ sửa bốn file nguồn và báo cáo này; đầu ra kiểm trong `tmp/codex-021`, `dist` và cache do công cụ tạo. Không sửa sim, file vàng, BUILD_NOTES, media, kit, dependency hay game khác; không chạy lệnh Git ghi. Skill dùng: `threejs-qa-release`, trong phạm vi kiểm của phiếu.

## 1. Kết quả từng việc

Trong bảng, `check` là lệnh đầy đủ `env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm check`. Mỗi lượt nêu dưới đây thoát 0, gồm kit 31 file khớp, 346 test, TypeScript, bản dựng và cổng gói. Kích thước là gói `/` tại lượt kiểm của từng việc; bản rút gọn cuối của việc 3 được kiểm cùng việc 5.

| # | Việc | File:dòng đã sửa | Kiểm (lệnh, kết quả, ảnh) | Gói "/" | Dòng .ts |
|---|---|---|---|---|---|
| 1 | Nhãn kho đè Draconis | `src/view/debug-2d.ts:455` | `check`: 346/346, [check-1.log](../../games/typing-defense/tmp/codex-021/check-1.log). Node gọi hàm vẽ cây thật: khoảng cách 0; 2,99; 3 m không gọi vẽ nhãn; 3,01 và 5 m vẫn vẽ `900/1000`. `td-1b-wood` hai cỡ và ảnh Ngày 1, 1280×720: **chưa chạy do cổng bị chặn**. | 84,85 kB | 10.500 |
| 2 | Nhãn “Lời gọi Hoàn hảo” trên một dòng | `src/ui/td.css:213` | `check`: 346/346, [check-2.log](../../games/typing-defense/tmp/codex-021/check-2.log). Node xác nhận hai quy tắc CSS nằm trong khối màn thấp. `td-1b-story` 1280×720, ảnh thắng, `scrollWidth <= clientWidth` và `td-theme` hai cỡ: **chưa đo do cổng bị chặn**. | 84,84 kB | 10.500 |
| 3 | Chặn lưu file lặp trong 10 s | `src/main.ts:221` | `check`: 346/346, [check-3.log](../../games/typing-defense/tmp/codex-021/check-3.log); cây cuối cũng đạt. Node thực thi nguyên dòng xử lý hiện tại: bấm ngay hai lần và trước hạn chỉ gọi `copyNumbers` một lần; đúng hạn 10 s được lưu tiếp; lời báo khác không chặn. Hộp cát thua với `__td.flood(220)`, đếm file tải thật và `td-1b-tour`/`playtestFileReplays` hai cỡ: **chưa chạy do cổng bị chặn**. | 84,88 kB | 10.500 |
| 4 | Chỉ đo cổng 5b | Không sửa mã; số ở mục 2 | Lệnh đúng phiếu dưới `heavy.sh`, thoát 0, [balance.log](../../games/typing-defense/tmp/codex-021/balance.log): 5b **29,5 %, trượt**; Ngày 4 **29 %**, Đêm 4 **25 %**. Không sửa BUILD_NOTES hoặc cân bằng. | — (chỉ đo) | 10.500 |
| 5 | Kẹp dải nghĩa tránh HUD | `src/view/words/cards.ts:258`; bớt một dòng trắng trước `leaving` để bù dòng thêm | `check` cây cuối: 346/346, [check-final.log](../../games/typing-defense/tmp/codex-021/check-final.log). Node gọi bố cục thật, 14 mẫu tại hai cỡ: dải trong màn, không chạm các panel đã cho, gồm panel trái, phải và giữa. Ảnh 07 `td-1b-tour` và `td-1b-learn`/`cardsClean` hai cỡ: **chưa chạy do cổng bị chặn**. | 84,99 kB | 10.500 |

Việc 1 dùng nguyên điều kiện được giao. `AgentStore` ghi rõ hero ở slot 0, lớp vẽ `agents` lấy hình hero khi `a === 0`; nhãn kho nằm tại `(x, z + TREE.radiusM + 2)`. Điều kiện khoảng cách Manhattan do đó đo đúng quanh điểm vẽ nhãn, trên trục x/z của thế giới.

Việc 3 chỉ bỏ lời gọi lưu khi lời báo bắt đầu bằng “Đã lưu” và thời hạn chưa hết; vẫn cho lưu lại khi hết hạn. Đường Chơi lại Ngày n vẫn tới `retryDay`. Kiểm Node thay `copyNumbers` bằng bộ đếm; nó xác nhận nhánh chặn, **không** thay cho bằng chứng có đúng một file trong trình duyệt.

Việc 5 kiểm sau khi tính vị trí ngang cuối của thẻ `mean`, trước khi đặt DOM. Chỉ xét panel cắt qua chiều cao của dải; thử x hiện tại rồi các mép panel với khoảng hở 6 px, lấy vị trí đầu tiên nằm trong màn và tránh được tất cả panel liên quan. Dải đã hợp lệ giữ x cũ. Nếu không có vị trí ngang đủ rộng trong màn thì giữ x cũ; chưa thể chứng minh cảnh chật hoặc `cardsClean` bằng ảnh của cây cuối. Cần Claude xem ảnh 07 và chạy đúng hai kịch bản trước khi nghiệm thu.

Bản thử đầu của việc 5 qua test nhưng vượt gói `/` (**85,03 kB**); các lượt rút tiếp còn **85,02 kB**. Đã rút phần mã mới xuống bản cuối **84,99 kB**, giữ nguyên các file ngoài phạm vi. Log thử giữ ở `E/check-5-attempt.log`, `E/check-5.log`, `E/check-5-final.log`. Không để bản vượt trần trong cây cuối. Cả ba file `.ts` đã sửa giữ nguyên số dòng: `debug-2d.ts` **831**, `main.ts` **378**, `cards.ts` **278**; đối chiếu [baseline.json](../../games/typing-defense/tmp/codex-021/baseline.json) với [metrics-final.json](../../games/typing-defense/tmp/codex-021/metrics-final.json).

Đầu dò độc lập của lượt này:

```text
../../.local/bin/heavy.sh node --import tsx tmp/codex-021/node-checks.mts
exit 0; pass: true
```

[Mã đầu dò](../../games/typing-defense/tmp/codex-021/node-checks.mts), [kết quả JSON](../../games/typing-defense/tmp/codex-021/node-checks.json), [log](../../games/typing-defense/tmp/codex-021/node-checks.log). Đầu dò gọi `DebugView.trees`, `WordCards.layout` và nguyên dòng xử lý copy hiện tại; Canvas/DOM được thay bằng bộ ghi lời gọi. Không coi đây là phép kiểm cảm nhận, DOM hoặc bố cục mọi thẻ của kịch bản thật.

## 2. Cổng 5b và Ngày 4

```text
env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh \
  node --import tsx scripts/td/balance.ts \
  --stage-seeds=12 --stage-sets=1 --seeds=20 --nights=4 --threads=4
exit 0; 69,9 s; Node v24.22.0; 4 luồng
```

Lệnh chạy đủ ma trận ải 12 seed, một bộ, rồi bảng BUILD_1A6 §12 trên **20 seed, 4 đêm**. Số 5b lấy ở bảng §12, bot **35 WPM, 95 %**, Cân bằng, theo lịch mở, từ vựng thật:

| Phép đo | Kết quả | Đích | Kết luận |
|---|---|---|---|
| 5b · tỉ lệ gõ ban Ngày, gộp bốn ngày | 29,5 % | 30–45 % | **Trượt** |
| Ngày 4 · tỉ lệ gõ ban Ngày | 29 % (bảng từng ngày làm tròn số nguyên) | Ghi riêng theo phiếu | Chuyển lượt cân bằng cùng 5b |
| Đêm 4 · tỉ lệ gõ | 25 % (làm tròn) | Ghi kèm để phân biệt Ngày/Đêm | Chỉ báo số |

Bảng từng ngày in: Ngày 1 **30 %** / Đêm 1 **30 %**; Ngày 2 **30 %** / Đêm 2 **16 %**; Ngày 3 **29 %** / Đêm 3 **24 %**; Ngày 4 **29 %** / Đêm 4 **25 %**. 5b in một chữ số thập phân, nên không dùng con số gộp 29 % làm tròn trong hàng “từng bot” thay cho **29,5 %**.

Cùng lệnh còn báo **5a trượt: 8,48 s / trần 8 s**. Đây là số đo để Claude xem trong lượt cân bằng; không sửa luật hay trần. 5c đạt **23,0 %**; không có bất biến vỡ hoặc lệnh bị từ chối. `balance.ts` thoát 0 dù một cổng cân bằng trượt; không tính exit 0 là cổng 5b đạt.

## 3. Phần trình duyệt chưa chạy

Đã thử đúng máy chủ riêng từ repo con thật:

```text
env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh \
  pnpm exec vite --host 127.0.0.1 --port 4292 --strictPort
exit 1
Error: listen EPERM: operation not permitted 127.0.0.1:4292
```

Log: [server.log](../../games/typing-defense/tmp/codex-021/server.log). Vite đã thoát, không có máy chủ do lượt này mở còn cần tắt. Không đổi cổng/host hoặc tìm đường vượt sandbox; không khởi chạy Chrome khi máy chủ chưa mở được.

Các lượt sau **chưa chạy**, không được tính là đạt hoặc trượt của game:

| Kịch bản | 1280×720 | 1920×1080 | Bằng chứng còn cần |
|---|---|---|---|
| `td-1b-wood` | Chưa chạy | Chưa chạy | Kết quả kịch bản; thêm ảnh Draconis cạnh cây đang chặt ở Ngày 1, 1280×720 |
| `td-1b-story` | Chưa chạy | Không yêu cầu trong phiếu | `td-1b-story-won-1280x720.png`, nhãn một dòng, thẻ trong màn, `sheet.scrollWidth <= sheet.clientWidth` |
| `td-theme` | Chưa chạy | Chưa chạy | Thẻ thua và các kiểm của kịch bản |
| `td-1b-tour` | Chưa chạy | Chưa chạy | Ảnh 07 sau sửa; `playtestFileReplays` |
| `td-1b-learn` | Chưa chạy | Chưa chạy | `cardsClean` |

Cần kiểm tay hộp cát thua bằng `__td.flood(220)`, bấm “Chép số chơi thử” hai lần trong 10 s: đúng một file `loi-goi-choi-thu-*.json`, HUD còn lời báo đã lưu. Node chưa thay phần này.

Mẫu lệnh cho Claude khi cổng được phép mở, lần lượt từng cỡ/kịch bản trong bảng, sau đó tắt server:

```bash
URL=http://127.0.0.1:4292/ OUT_DIR=tmp/codex-021/scen \
  ../../.local/bin/heavy.sh --gpu node src/kit/tools/cdp-run.mjs \
  scripts/visual/scenarios/td-1b-tour.mjs --width=1280 --height=720
```

Đã đọc ảnh gốc `tmp/mac-2026-10-27/test/verify-fix/final/scen/td-1b-tour-07-choang-1280x720.png`: dải “safe · an toàn” chạm bảng hộp cát bên phải. Ảnh này thuộc mã trước sửa, chỉ dùng hiểu lỗi; không lấy làm bằng chứng mã cuối đạt.

## 4. Kiểm chung

```text
Cây cuối:
env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm check
exit 0
src/kit OK: 31 files match kit-manifest.json
Test Files 32 passed (32)
Tests      346 passed (346)
tsc --noEmit && vite build && bundle-budget: đạt
/:         84,99 kB gzip; 84.993 / 85.000 byte; còn 7 byte
/?title=0: 83,54 kB gzip; 83.543 / 85.000 byte; còn 1.457 byte
Dòng src/**/*.ts, bỏ src/kit/**: 10.500 / 10.500

env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm td:golden:check
exit 0
 td-1a:      same: true; ticks 19660; commands 389
 td-1b-boss: same: true; ticks 5306; commands 45
 Cả hai: changed {}; firstMovedAtTick null; problems 0; rejected 0
 content cd59313e; deck 9c9b91d8

git diff --check
exit 0
```

Log: [check-final.log](../../games/typing-defense/tmp/codex-021/check-final.log), [golden-final.log](../../games/typing-defense/tmp/codex-021/golden-final.log). Số byte dùng `node:zlib.gzipSync`, cùng cách với `scripts/bundle-budget.mjs`; quy tắc dòng dùng số ký tự xuống dòng của `.ts` trong `src`, bỏ `src/kit`, như `tests/boundary.test.ts`. [metrics-final.json](../../games/typing-defense/tmp/codex-021/metrics-final.json) giữ cả SHA-256 của bốn file sửa để đối chiếu đúng cây đã kiểm.

Môi trường vẫn báo `Your node_modules are out of sync with your lockfile. The workspace structure has changed since last install`. Dùng `pnpm_config_verify_deps_before_run=warn` để chạy các cổng hiện có, không tự cài lại workspace hay sửa lockfile. Tất cả lệnh nặng đi qua `heavy.sh`.

**Claude/chủ dự án cần xem:** phần trình duyệt ở mục 3; khoảng trống gói `/` chỉ **7 byte**; chuyển **5b 29,5 %** và **5a 8,48 s** sang lượt cân bằng. Chưa thể gọi toàn bộ phiếu đã nghiệm thu vì các kiểm ảnh/DOM/tải file còn thiếu. Không có việc sửa mã nào bị bỏ vì ngân sách; phần chưa làm là các kiểm cần máy chủ/trình duyệt bị sandbox chặn.

## 5. Diff cuối đầy đủ

Lệnh chạy trong `games/typing-defense`, chỉ có bốn file thuộc phiếu. Báo cáo này là file mới ở repo cha, không nằm trong diff repo con. Không gom thay đổi của các agent khác ở repo cha.

`git diff --stat`:

```text
 src/main.ts             | 2 +-
 src/ui/td.css           | 2 +-
 src/view/debug-2d.ts    | 2 +-
 src/view/words/cards.ts | 2 +-
 4 files changed, 4 insertions(+), 4 deletions(-)
```

`git diff` đầy đủ:

```diff
diff --git a/src/main.ts b/src/main.ts
index 4ce0192..80f64a7 100644
--- a/src/main.ts
+++ b/src/main.ts
@@ -218,7 +218,7 @@ const sheets = new Chunk("sheets", async () => {
     else if (action === "retry" || action === "copy") void retryChunk.get().then((m) => {
       if (m === null) return tellLost((action === "copy" ? "Chép số chơi thử" : "Chơi lại Ngày n") + " chưa tải được · F5 để thử lại");
       const run = { world, session, seed, sandbox, deck, mode: startMode, header: runHeader, learn: runLearn, fresh: freshRun };
-      if (action === "copy") (m.copyNumbers(run, profile, source), tellLost("Đã lưu file chơi thử và chép số")); // test pass 27/10: it said nothing
+      if (action === "copy") (lost?.text.startsWith("Đã lưu") && performance.now() < lost.until) || (m.copyNumbers(run, profile, source), tellLost("Đã lưu file chơi thử và chép số"));
       else m.retryDay(run);
     });
     else if (action === "title") showTitle(world.phase !== "defeat");
diff --git a/src/ui/td.css b/src/ui/td.css
index 48c5583..95b9c64 100644
--- a/src/ui/td.css
+++ b/src/ui/td.css
@@ -210,4 +210,4 @@ body.is-paused #tdCanvas { filter: saturate(0.55) sepia(0.3) brightness(0.9); }
 .td-review ul { margin: 2px 0 6px; padding-left: 18px; }
 .td-review b { color: var(--vd-jade-ink); }
 /* A short screen (1280 × 720: a won card with 5 words to review was ~730 px): the numbers in two columns, tighter rows. */
-@media (max-height: 800px) { .td-sheet { padding: 12px 18px 14px; } .td-sheet h2 { margin: 0 0 4px; } .td-sheet dl { grid-template-columns: 1fr auto 1fr auto; margin: 4px 0 8px; padding: 6px 10px; } .td-sheet button { margin-top: 5px; padding: 6px 12px; } .td-stars i { font-size: 28px; } }
+@media (max-height: 800px) { .td-sheet { padding: 12px 18px 14px; } .td-sheet h2 { margin: 0 0 4px; } .td-sheet dt { white-space: nowrap; } .td-sheet dl { grid-template-columns: 1fr auto 1fr auto; gap: 3px 10px; margin: 4px 0 8px; padding: 6px 10px; } .td-sheet button { margin-top: 5px; padding: 6px 12px; } .td-stars i { font-size: 28px; } }
diff --git a/src/view/debug-2d.ts b/src/view/debug-2d.ts
index 7542152..cca16d2 100644
--- a/src/view/debug-2d.ts
+++ b/src/view/debug-2d.ts
@@ -452,7 +452,7 @@ export class DebugView {
       if (grow(t) < 0) this.disc(x, z, TREE.radiusM * (1.6 + grow(t)), null, `rgba(95, 170, 60, ${-grow(t)})`, 3);
       if (T.marked[t] === 1) this.disc(x, z, TREE.radiusM, null, COLOR.lamp, 3.5);
       if (T.progress[t]! > 0) this.bar(x, z + TREE.radiusM + 0.4, 2.4, T.progress[t]!, COLOR.lamp);
-      if (T.progress[t]! > 0 && !labels.some(([lx, lz]) => Math.abs(lx - x) < this.px(70) && Math.abs(lz - z) < this.px(24))) labels.push([x, z]), this.text(T.left[t] + "/" + TREE.reserve, x, z + TREE.radiusM + 2, 11, COLOR.ink, 800, COLOR.stump);
+      if (T.progress[t]! > 0 && Math.abs(w.agents.x[0]! - x) + Math.abs(w.agents.z[0]! - z - TREE.radiusM - 2) > 3 && !labels.some(([lx, lz]) => Math.abs(lx - x) < this.px(70) && Math.abs(lz - z) < this.px(24))) labels.push([x, z]), this.text(T.left[t] + "/" + TREE.reserve, x, z + TREE.radiusM + 2, 11, COLOR.ink, 800, COLOR.stump);
     });
   }
 
diff --git a/src/view/words/cards.ts b/src/view/words/cards.ts
index b367131..81f2571 100644
--- a/src/view/words/cards.ts
+++ b/src/view/words/cards.ts
@@ -255,6 +255,7 @@ export class WordCards {
         const expire = column.b >= 0 ? C.expire[column.b]! : -1;
         card.y = column.roofY - column.heights[k]! - card.height;
         card.x = boxes[index]!.x + offset + (typing ? 18 : 0) + (now < card.shakeUntil ? Math.sin(now * 0.25) * 6 : 0);
+        if (card.leave === "mean") { const { half } = card, hits = panels.filter((p) => card.y < p.bottom && card.y + card.height > p.top); card.x = [card.x, ...hits.flatMap((p) => [p.left - half - 6, p.right + half + 6])].find((x) => x >= half + SAFE.side && x + half <= width - SAFE.side && hits.every((p) => x + half + 6 <= p.left || x - half - 6 >= p.right)) ?? card.x; }
         const left = expire < 0 || s < 0 ? 0 : Math.max(0, (expire - w.tick) / Math.max(1, expire - C.born[column.b]!));
         card.bar.style.transform = "scaleX(" + left.toFixed(3) + ")";
         if (C.kind[column.b] === CALL_KIND.direct) card.el.style.setProperty("--t", (100 * left).toFixed(0) + "%"); // the window's clock ring
@@ -262,7 +263,6 @@ export class WordCards {
       });
     });
   }
-
   private leaving(card: Card, now: number): void {
     if (card.leave === "mean") {
       if (now - card.leaveAt >= MS.mean) Object.assign(card, { leave: "fold", leaveAt: now }).el.classList.add("is-gone");
```
