# Phiếu 220 · Last Line · Luật bến đầy §5.1 (TS-M1-12, N13): ba ứng viên sau núm `FULL_BAY` mặc định tắt, có test, đo trên V6 ở `c1-s1` hai bộ seed rồi `c1-s1..c1-s4`

**Nguồn:**
- `docs/codex-queue/209-report.md`: "**Luật bến đầy §5.1: cần.** V6 còn I Khá **14,9/15,1 %**, Nhanh **10,9/11,2 %**, đều trên 10 % ở cả hai bộ dù đã hết đảo TT." và "Chủ dự án/Claude cần xem ba việc: **không áp V6 khi còn cổng đỏ**, chốt phiếu luật bến đầy §5.1, và bố trí chơi thật cho B9."
- `docs/games/MAP1_PRODUCTION.md` §3.2 mục 9 (dòng 159): "**TS-M1-12** · P1 · G6. Ải 1 quá dễ; B1, B6, B7 trượt; Thử thách đảo thứ bậc. **Sửa:** chỉnh theo N13; luật §5.1 cho bến đầy; …". Last Line là game gần đủ cổng nhất: "Tuyến Cuối 03/11" (§0, dòng 12).
- `games/typing-survival/docs/changelog/2026-10-27-test-pass.md`, hàng N13: "Khá, Nhanh và người gõ 70 WPM nạp vào bến đầy gần nửa số từ (94/202, 40/151 từ "ĐẦY")".
- `games/typing-survival/AGENTS.md`, mục "Next": "Khá and Nhanh idle on stages 1, 2, 4 because the guns take no more magazines (a §5.1 rule for a full bay)".
- `docs/BUILD_S1.md` §5.1 (trong worktree), gạch "Bến": "Bến có súng đã đầy băng thì gõ từ của nó cũng không nạp được gì (như S0)."
- Mã ở worktree, HEAD `ba6d70e`:
  - `src/sim/weapons.ts:80–96`: `loadMagazine` trả `false` khi bến đầy. Nơi gọi: `src/sim/words.ts:248`, trong hàm `finish`.
  - `src/sim/pace.ts:171`: `flowSnapshot` chỉ tính `live` cho bến còn nhận băng.
  - `src/kit/balance/flow.ts:166`: `const idle = snapshot.live <= 0 && !snapshot.busy;`. Chỉ số I của báo cáo đếm từ dòng này.
  - `tests/survival/typist-bot.ts:164`: bến đầy có giá trị −1 (BUILD_S1 §11.2: "Bến đầy thì −1").
- `docs/HANDOFF_CURRENT.md:18`: 30/10 11:20, chủ dự án bảo Claude dừng việc của mình và giao nhiều việc cho Codex, chạy ba làn.

**Không trùng:**
- 209: chỉ đo số, không đổi luật;
- 210: hướng dẫn lần đầu;
- 206, 211: ảnh UI, làm ở `.wt-ts-art`;
- `ts-typefx` và `ts-vfx`: việc của Claude.

Chưa phiếu nào làm luật bến đầy (đã quét `docs/codex-queue/`).

**Loại phiếu:** mã sim đặt sau núm, mặc định tắt, rồi đo. Không đổi mặc định. Chọn luật và đưa số vào game là việc của Claude sau khi duyệt.

**Báo cáo:** `docs/codex-queue/220-report.md` (tiếng Việt) và thư mục `docs/codex-queue/220/`. Cả hai ở repo cha.

## Chỉ chạy khi

Kiểm điều 7 trước tiên. Rồi chạy các lệnh sau từ repo cha, lưu đầu ra vào `docs/codex-queue/220/start.txt`. Một điều không đạt thì dừng, ghi vào báo cáo, không sửa gì:
1. `git -C games/.wt-ts-codex branch --show-current` ra `ts-codex`.
2. `git -C games/.wt-ts-codex rev-parse HEAD` ra `ba6d70e9d6978eb4b430d119c409f3d47f9a364e`.
3. `git -C games/.wt-ts-codex status --short -uall` ra 0 dòng.
4. Lệnh sau ra 0 dòng (sim, nội dung, kit, bot, bộ từ và các script đo giống hệt `79db628`, mốc 209 đã đo; `scripts/balance-lib.ts` nạp `src/app/skill.ts`, file này nạp `src/app/english.ts`; Claude kiểm 30/10 khoảng 13:15):
   ```bash
   git -C games/.wt-ts-codex diff --stat 79db628 HEAD -- src/sim src/content src/kit tests/survival public/vocabulary \
     scripts/balance.ts scripts/balance-lib.ts scripts/overrides.ts scripts/rollup.ts scripts/chapter-hashes.ts \
     src/app/input.ts src/app/session.ts src/app/skill.ts src/app/english.ts
   ```
5. Có thư mục `games/.wt-ts-codex/node_modules/tsx` và file `games/.wt-ts-codex/node_modules/.bin/vitest`.
6. `shasum -a 256` các file 209 (chưa commit; chỉ đọc) ra đúng:

   | File | SHA-256 |
   |---|---|
   | `docs/codex-queue/209/runs/v6-s1.json` | `c7ada6119676b44bc7cd38c24ce626f9da374706fd5cd4cc40bc054c2ddfc407` |
   | `docs/codex-queue/209/runs/v6-s101.json` | `df4cb59c36fc3163630a9a5993cf8963c7c9a1aced7c8420fd8b43ecf6d97fc3` |
   | `docs/codex-queue/209/runs/v0-s1.json` | `d5fa479d1a6702eaacf6c453e21e15abfeff19747a4f338d6afb645cbcba385c` |
   | `docs/codex-queue/209/runs/v0-s101.json` | `424d6a08dda16cf96cd93286f5919171e8d37534b665f8ab56c01454109e79a6` |
   | `docs/codex-queue/209/tools/summarize.mjs` | `b73fd23e6334df7fd7e0ee0f0697a1e9f0021e11995eb6e7ea8d4af2ebec876e` |
   | `docs/codex-queue/209/tools/run-wave.mjs` | `3d6b158c729565666c4fbcca5f18eaff649a4cb4c79f9a4122ed5ff416e754b9` |
7. Kiểm **trước khi tạo gì**: chưa có `games/.wt-ts-codex/tmp/codex-220/`, `docs/codex-queue/220/` và `docs/codex-queue/220-report.md` (30/10 13:15 đều chưa có). Có rồi là lượt trước bỏ dở: dừng, chỉ ghi `220-report.md` nói đã thấy gì; Claude dọn rồi chạy lại.

## Nơi làm

- **Làn và model:** làn `s7`, sau 197 (222 và 223 chạy sau phiếu này); `gpt-6.1-sol`, effort `high`, sandbox `workspace-write`.
- **Worktree** `games/.wt-ts-codex`, nhánh `ts-codex`, HEAD `ba6d70e` (Claude đã commit 205, 207, 210). Worktree có sẵn, Claude không cần dựng gì. Không làn nào khác dùng nó: 206 và 211 làm ở `.wt-ts-art`, còn `.wt-ts-typefx` là của Claude.
- **cwd của làn** là repo cha (`.`). Lệnh git và báo cáo chạy từ repo cha. Mọi lệnh `pnpm` và `node` của game chạy **trong** `games/.wt-ts-codex`.
- **Thư mục tạm** `games/.wt-ts-codex/tmp/codex-220/` (Git bỏ qua `tmp/`), gồm `runs/` và `tmpdir/`. Mọi lệnh `node`, `pnpm` đặt `TMPDIR` bằng đường dẫn tuyệt đối tới `tmpdir/`, để bộ nhớ đệm của `tsx` nằm trong repo: sandbox không ghi được ra ngoài repo (bài học 189). Mẫu:
  ```bash
  WT=games/.wt-ts-codex
  T="$PWD/$WT/tmp/codex-220"
  mkdir -p "$T/runs" "$T/tmpdir" docs/codex-queue/220/runs docs/codex-queue/220/tools docs/codex-queue/220/evidence docs/codex-queue/220/logs
  ```
- Luật chung của runner nói "không chạy build hay test suite của game". Phiếu này **được** chạy `pnpm check` và `pnpm exec vitest` trong `games/.wt-ts-codex`, như 205, 207, 210 đã làm. Không chạy ở chỗ khác.
- Không dùng `.local/bin/heavy.sh`, vì nó ghi vào `/tmp`. Dùng `nice -n 15`. Sandbox có thể báo `setpriority: Operation not permitted` (209 gặp ở 14/14 báo cáo, vẫn chạy xong): ghi lại, không coi là lỗi.

**Chỉ được ghi.** Trong worktree:
- `src/content/guns.ts`: chỉ thêm hằng `FULL_BAY` cùng chú thích tiếng Anh của nó (như phần còn lại của file);
- `src/sim/weapons.ts`;
- `src/sim/words.ts`: chỉ trong hàm `finish`;
- `src/sim/pace.ts`: chỉ trong `flowSnapshot`, chú thích JSDoc ngay trên nó (dòng 152–164: "a full gun's word does nothing" phải nói đúng luật khi núm bật) và dòng import;
- `src/sim/world.ts`: đúng **một dòng**, dòng 119 `guns: createGuns(header.kit),`, thêm tham số `stage.chapter` (xem R1). Không có dòng này thì `createGuns` không biết ải có phải ải chương không;
- `tests/survival/typist-bot.ts`: chỉ `options()`, chú thích đầu file dòng 16–18, cộng một hàm thuần export nếu cần cho test;
- `tests/full-bay.test.ts` (mới);
- `docs/changelog/2026-10-30-full-bay-knobs.md` (mới, tiếng Việt);
- `tmp/codex-220/`.

Ở repo cha: `docs/codex-queue/220-report.md` và `docs/codex-queue/220/`.

## Đọc trước

- Của 209 (chưa commit, chỉ đọc): `209-report.md`, `209/method.md`, `209/decision-v6.md`, `209/variants.json`, `209/tools/summarize.mjs`, `209/tools/run-wave.mjs`.
- `docs/games/BALANCE.md`: §3 (chỉ số, dải đích), §7 (B1–B9).
- Trong worktree:
  - `docs/BUILD_S1.md` §5.1 (gạch "Bến", "Rèn"), §11.2 (bot), §11.3 (báo cáo).
  - `src/content/guns.ts`: `MAG_MAX` 2, `MAG_CAP` 3, `FORGE.mags` `[MAG_MAX, MAG_MAX, MAG_CAP]` (dòng 17–31).
  - `src/content/chapter-1.ts` dòng 51, 69, 86, 103: ải 1–4 đều 2 bến, cấp `[1, 1]` (ải 4: `[2, 1]`). Vì vậy sức chứa mọi bến ở ải 1–4 là 2 băng.
  - `src/sim/weapons.ts`: `createGuns`, `loadMagazine`, `nextMagazine`. Năm súng gọi `nextMagazine(G, bay)` trong `src/sim/guns/*.ts` (`xung`, `tia`, `tan`, `ray`, `phao`); `nextMagazine` nhận `G: Guns`, không nhận `w`.
  - `src/sim/words.ts` hàm `finish` (khoảng dòng 242–261): đẩy `EV.word`, rồi `EV.load` khi nạp được.
  - `src/sim/pace.ts` `flowSnapshot` (dòng 165–182) và `src/kit/balance/flow.ts:166`.
  - `src/sim/hash.ts` dòng 22–33 và 44: `mixObject` trộn **mọi typed array và mọi số ở tầng đầu** của `w.guns`, `w.typing`, `w.stats`, `w.pace` và các phần khác. Thêm một mảng hay một số ở tầng đầu các object này là đổi cả 152 mã băm chương, dù núm đang tắt.
  - `scripts/overrides.ts`: `--set` ghi thẳng vào object được export, lúc chạy. `ROOTS` gồm mọi export của `guns.ts`, nên `--set=FULL_BAY.extra=1` dùng được ngay khi hằng có mặt. Luật phải đọc số **lúc gọi**, không chép vào biến cấp module.
  - `tests/survival/typist-bot.ts`: `options()` (dòng 152–168, gồm chú thích); `act()` (dòng 218–222): bot chờ khi mọi bến có giá trị âm.
  - Mẫu test: `tests/guns.test.ts:413–427` (gõ trọn một từ bằng `step(w, [...word].map(...))`), `tests/overrides.test.ts` (`applySet` rồi `undo`), `tests/survival/arena.ts` (dựng thế giới với súng tự chọn).
- Phía view, chỉ đọc để ghi "view cần gì":
  - `src/view/typing-feel.ts:140`: một từ được coi là đã nạp khi sự kiện `EV.load` ngay sau nó **cùng bến**;
  - `src/view/strip.ts:197`: nhãn `FULL` (phiếu cũ gọi là "ĐẦY");
  - `src/view/hud.ts:173` và `:333`: số ô băng và lớp `is-full` đi theo `cap`;
  - `src/view/shots.ts:137`.

## Ba ứng viên

Cả ba luật chỉ chạy ở ải chương (`w.stage.chapter > 0`), kể cả khi núm bật. Trận thử `s0` giữ luật của S0 (BUILD_S1 §5.1: "như S0"), và vết vàng `s0-trace` ghim luật đó.

| Núm | Mặc định | Luật |
|---|---|---|
| `FULL_BAY.extra` | 0 | **R1.** Sức chứa của bến là `min(MAG_CAP, FORGE.mags[level − 1] + extra)`. Ở mọi ải chương hiện có, `FORGE.mags` của cấp 1–2 là 2 và `MAG_CAP` là 3, nên `extra` từ 1 trở lên đều ra 3: chỉ `extra=1` có nghĩa, đừng tốn biến thể cho `extra=2`. Giá trị lẻ hay âm thì dùng `max(0, floor(extra))`. |
| `FULL_BAY.spill` | 0 | **R2**, bật khi ≥ 1. Từ gõ xong ở bến đầy nạp vào bến **khác** còn nhận băng: bến ít băng nhất trước, bằng nhau thì bến số nhỏ hơn. Băng giữ `clean` và `fast` của từ, mang thông số súng của bến nhận. Không có bến nào nhận thì không có gì xảy ra. |
| `FULL_BAY.boost` | 0 | **R3**, bật khi > 0. Từ gõ xong ở bến đầy nhân sát thương của **băng xếp cuối** bến đó (ô `bay × MAG_CAP + mags − 1`) với `1 + boost`. Mỗi ô băng được tăng nhiều nhất một lần. Ô đã tăng thì từ sau không làm gì, tới khi một băng được bắn hết và một băng mới nạp vào ô cuối. |

- Khi nhiều núm cùng bật (chỉ dùng trong test và trong biến thể phụ): R1 áp lúc tạo thế giới. Với từ của bến đầy, R2 đi trước; không có bến nhận thì mới tới R3.
- Bến không có súng (`gun < 0`) không bao giờ tính là "đầy".
- Ở ải 1–4, cả hai bến đều có súng và cùng sức chứa. R2 chỉ có tác dụng khi bến kia còn chỗ.

## Việc

1. **Mốc, trước mọi sửa đổi.**
   - Nhánh, HEAD, `status` vào `220/start.txt` (mục "Chỉ chạy khi").
   - `git status --short -uall` của repo cha vào `220/evidence/parent-status-before.txt`.
   - `shasum -a 256 tests/golden/s0-trace.json` (chạy trong worktree) vào `220/evidence/golden-before.txt`.
   - Trong worktree, `TMPDIR="$T/tmpdir" node --import tsx scripts/chapter-hashes.ts > "$T/chapter-before.txt"`, chép sang `220/chapter-before.txt`. Phải có 152 dòng.
   - `TMPDIR="$T/tmpdir" pnpm check > ../../docs/codex-queue/220/logs/check-before.txt 2>&1` trong worktree. Ghi mã thoát, số file test, số test, số file kit khớp. Theo `210-report.md`: 296 test trong 26 file, kit 61/61. Ghi số thật đo được.
2. **Tái tạo V6, trước mọi sửa đổi.**
   - Chép `209/tools/summarize.mjs` và `209/tools/run-wave.mjs` vào `220/tools/`, rồi sửa đường dẫn. Ghi `diff -u` giữa bản 209 và bản 220 vào `220/tools/changes-from-209.diff`. Những chỗ phải sửa:
     - `run-wave.mjs`: `base` thành `games/.wt-ts-codex/tmp/codex-220`; `report` thành `docs/codex-queue/220` (đọc `220/variants.json`, ghi `220/evidence/wave-*.json`); `cwd` của tiến trình đo là **gốc worktree** (209 dùng một bản chép `main/`). Vì cwd đổi, `--json` và `--out` phải là đường **tuyệt đối** `$T/runs/<tên>.json|.md` (209 dùng `../runs/…`, từ gốc worktree sẽ ghi sai ra `games/runs/`). `.err` vẫn ở `$T/runs/`. Danh sách ải nhận từ tham số (mặc định `c1-s1`). Id `x-<v>` lấy chuỗi `--set` của khóa `<v>` trong `variants.json` (`x-v0` là chuỗi rỗng); không thêm khóa `x-*` vào `variants.json`. Trần số tiến trình theo mục "Máy dùng chung".
     - `summarize.mjs`: đọc `220/variants.json`. Bảng `oldValues` thêm `FULL_BAY.extra`, `FULL_BAY.spill`, `FULL_BAY.boost` đều là 0. Chốt `cells.length !== 36` và `stage !== 'c1-s1'` chỉ áp cho báo cáo một ải; báo cáo bốn ải có 144 ô, 36 ô mỗi ải, và `get()` phải lọc thêm theo `stage` (bản 209 lấy ô đầu tiên khớp bot/chế độ, ở báo cáo bốn ải đó luôn là `c1-s1`). Bỏ phần so với mốc kiểm kê 28/10 (`evidence/audit-2026-10-28`). Thay `evidence/main.commit` bằng `220/evidence/worktree.commit` (HEAD đầy đủ của worktree). Thay luật chọn nền B của 209 bằng luật ở Việc 6.
   - Chuỗi V6 (`209/variants.json`, khóa `v6`): `c1-s1.drainRate=2.4,MODE_SPECS.challenge.surge=1.0,MODE_SPECS.challenge.rate=1.06`.
   - Hai báo cáo, chạy cùng lúc, trong worktree:
     ```bash
     cd games/.wt-ts-codex
     T="$PWD/tmp/codex-220"
     TMPDIR="$T/tmpdir" nice -n 15 node --import tsx scripts/balance.ts --stages=c1-s1 --seeds=100 --first=1 --g3c \
       --set='c1-s1.drainRate=2.4,MODE_SPECS.challenge.surge=1.0,MODE_SPECS.challenge.rate=1.06' \
       --json="$T/runs/v6-s1.json" --out="$T/runs/v6-s1.md" > /dev/null 2> "$T/runs/v6-s1.err"
     ```
     Bộ thứ hai dùng `--first=101` và tên `v6-s101.*`. Không truyền `--bots`, `--modes`, `--off`: mặc định đã là ba chế độ, 11 bot, cộng Chuẩn tắt nhịp.
   - So từng ô (36 ô × 2 bộ) và **mọi trường** của `summary` (thắng, S, P, I, O, N, Q, `killSeconds`, `stepsPerWave`, `spawnMin`, `spawnMax`, `learnOk`…) với `209/runs/v6-s1.json` và `v6-s101.json`. Mong đợi: 0 ô lệch, SHA-256 hai JSON trùng với bảng ở "Chỉ chạy khi". Kết quả ghi vào `220/evidence/v6-repro.json`.
   - **Một ô lệch là dừng.** Ghi ô, trường, hai giá trị vào báo cáo, không sửa mã. SHA-256 khác nhưng mọi trường trùng thì ghi lại và làm tiếp.
3. **Test trước, ghi số đỏ trước khi viết mã.** Viết `tests/full-bay.test.ts`, chạy `TMPDIR="$T/tmpdir" pnpm exec vitest run tests/full-bay.test.ts`, lưu log vào `220/logs/tests-red.txt`. Nếu file không nạp được vì `FULL_BAY` chưa có, đó vẫn là số đỏ hợp lệ: ghi đúng như vitest in ra. Test bao các ý sau.
   - **Mặc định không đổi gì.** `FULL_BAY` bằng `{ extra: 0, spill: 0, boost: 0 }`. Thế giới `c1-s1` có `cap` `[2, 2]`. Gõ trọn từ của một bến đầy: `mags`, `damage`, `rate`, `crit`, `pierce`, `perfect` của mọi bến giữ nguyên, không có `EV.load`. (Mã băm khi núm tắt do Kiểm 3, 4 và 5 lo, không ghim trong test.)
   - **R1.** Với `extra=1`, ở `c1-s1` mọi bến có `cap` 3. Kit cấp `[1, 3]` thì vẫn 3 (bị chặn ở `MAG_CAP`). `extra=2` cho kết quả như `extra=1`. Ở trận thử `s0`, `cap` vẫn là 2.
   - **R2.** Với `spill=1`:
     - bến 0 đầy, bến 1 có 0 băng: gõ từ của bến 0 thì bến 1 có 1 băng; ô của băng đó mang `clean`, `fast` của từ (kiểm `damage`, `pierce`, `rate`, `perfect` theo súng của bến 1); có `EV.load` với `slot` 1 và `value` bằng `mags[1]`; bến 0 không đổi;
     - hai bến đều đầy: không đổi gì, không có `EV.load`;
     - kit 3 bến: chọn bến ít băng nhất, bằng nhau chọn bến số nhỏ hơn;
     - ở `s0`: không đổi gì.
   - **R3.** Với `boost=0.3`:
     - bến đầy: sát thương ô cuối nhân 1,3;
     - từ thứ hai vào cùng bến đầy: không đổi thêm;
     - sau `nextMagazine`: băng đã tăng lên đầu hàng vẫn giữ mức tăng; ô cuối mới (sau một lần nạp) chưa tăng, và tăng được đúng một lần;
     - ở `s0`: không đổi gì.
   - **Thứ tự** khi `spill=1` và `boost=0.3` cùng bật: còn bến nhận thì R2; không còn thì R3.
   - **`--set` tới được luật lúc chạy.** `applySet("FULL_BAY.spill=1")` của `scripts/overrides.ts` trả đúng dòng `FULL_BAY.spill 0→1`. Một thế giới tạo **sau** lệnh đó có luật R2. `undo()` xong thì thế giới mới không còn luật. Làm như vậy cho cả ba núm.
   - **`flowSnapshot(w).live`:**
     - núm tắt: bến đầy không tính;
     - R1: bến có 2/3 băng được tính;
     - R2: bến đầy được tính khi và chỉ khi còn bến khác nhận băng; hai bến đều đầy thì `live` là 0;
     - R3: bến đầy được tính khi ô cuối chưa tăng; đã tăng thì không.
   - **Giá trị bến của bot** (`options()` của `typist-bot.ts`, hay hàm thuần mà Việc 4 tách ra):
     - núm tắt: bến đầy là −1;
     - R1: bến có 2/3 băng có giá trị dương;
     - R2: bến đầy có đúng giá trị của bến nhận (cùng công thức `need × (cap − mags)` của bến nhận); không có bến nhận thì −1;
     - R3: bến đầy chưa tăng có giá trị `need[súng của bến] × boost`; đã tăng thì −1.
   - Test đặt núm chỉ qua `applySet` và luôn `undo()` trong `finally` hay `afterEach`, để test khác không thấy núm bật.
4. **Mã.** Tên hàm dưới đây là gợi ý, đổi được nếu hợp mã hơn. `words.ts`, `pace.ts` và `typist-bot.ts` phải cùng dùng **một** bộ hàm của `weapons.ts`, không viết lại điều kiện ở ba nơi.
   - `src/content/guns.ts`: `export const FULL_BAY = { extra: 0, spill: 0, boost: 0 };`, chỉ có lá số, kèm một dòng chú thích nói ba luật và phiếu 220. Không thêm `as const` (để `applySet` và kiểu TS không vướng nhau), không `Object.freeze`.
   - `src/sim/weapons.ts`:
     - `createGuns(kit, chapter = 0)`: `cap[b] = gun[b] >= 0 ? Math.min(MAG_CAP, FORGE.mags[level[b] − 1] + (chapter > 0 ? Math.max(0, Math.floor(FULL_BAY.extra)) : 0)) : 0`. Đọc `FULL_BAY` trong thân hàm, mỗi lần gọi.
     - Dấu "đã tăng" của R3 nằm trong một **object lồng**, ví dụ `fullBay: { boosted: new Uint8Array(slots) }`. Không thêm typed array hay số ở tầng đầu của object `createGuns` trả về (lý do ở `hash.ts`, mục Đọc trước). `loadMagazine` đặt dấu về 0 ở ô nó ghi. `nextMagazine` dời dấu cùng `damage`, `rate`, `crit`, `pierce`, `perfect`. Ghi trong chú thích và trong báo cáo: dấu này nằm ngoài mã băm; nếu Claude chọn R3, một phiếu sau đưa nó vào `hashWorld` và cập nhật 152 mã băm có chủ đích.
     - Hàm thuần dùng chung, ví dụ `spillTarget(w, bay)` trả bến nhận hay −1, `canBoost(w, bay)` trả boolean. Cả hai đọc `FULL_BAY` và `w.stage.chapter` lúc gọi.
     - Hàm áp luật, ví dụ `fullBayWord(w, bay, clean, fast)`: R2 gọi `loadMagazine(w, target, clean, fast)` rồi trả bến nhận; R3 nhân ô cuối, đặt dấu, trả một mã riêng; không có gì thì trả −1.
     - `loadMagazine` giữ đúng nghĩa cũ (trả `false` khi đầy). `tests/survival/arena.ts` và `tests/survival-sim.test.ts:504` gọi thẳng hàm này.
   - `src/sim/world.ts:119`: `guns: createGuns(header.kit, stage.chapter),`. Không đổi dòng nào khác.
   - `src/sim/words.ts`, hàm `finish`: khi `loaded` là `false` thì gọi hàm áp luật. Giữ `EV.word` như cũ. Với R2, đẩy `EV.load` ngay sau `EV.word` với `slot` là bến nhận, `ref` là chỉ số từ, `value` là `w.guns.mags[bến nhận]`, `flags` của từ (cùng hình dạng `EV.load` hiện có ở dòng 257). Với R3, không đẩy gì, không thêm loại sự kiện mới.
   - `src/sim/pace.ts`, `flowSnapshot`: bến có súng được tính `live` khi `mags < cap`, hoặc `spillTarget(w, b) >= 0`, hoặc `canBoost(w, b)`. Sửa JSDoc ngay trên hàm cho đúng luật khi núm bật. `pace.ts` đã import `./weapons` (dòng 24), nên không sinh vòng import mới.
   - `tests/survival/typist-bot.ts`, `options()`: bến đầy có giá trị theo bảng ở Việc 3; R1 không cần mã riêng vì `G.cap` đã đổi. Sửa chú thích dòng 16–18 ("A full gun's word loads nothing…") cho đúng luật khi núm bật. Có thể tách một hàm thuần export để test gọi thẳng.
   - Núm đều 0 thì mọi giá trị trả về, mọi sự kiện và mọi byte được băm giữ nguyên. Kiểm 3 và Kiểm 4 chứng minh điều này.
   - Mã sim giữ tính thuần (`tests/survival-boundary.test.ts`): không `Math.random`, không đồng hồ, không DOM.
   - Không đổi view, HUD hay app. Nhãn `FULL` (`src/view/strip.ts:197`) giữ nguyên. Báo cáo liệt kê view cần gì nếu một luật được chọn (mục Báo cáo).
5. **Kiểm sau mã, trước khi đo.**
   - `pnpm exec vitest run tests/full-bay.test.ts` xanh, log vào `220/logs/tests-green.txt`.
   - Đột biến: tạm cho `spillTarget` luôn trả −1, chạy lại test, ghi số đỏ; làm như vậy với `canBoost` luôn `false` và với R1 bỏ `extra`. Trả mã lại, xanh lại. Log vào `220/logs/mutations.txt`.
   - `pnpm check` (Kiểm 1), SHA-256 vết vàng (Kiểm 3), `chapter-hashes` sau (Kiểm 4). Một mục đỏ thì sửa mã trước khi đo.
6. **Đo trên `c1-s1`.**
   - Bốn biến thể cố định. Mỗi biến thể là chuỗi V6 cộng đúng một núm:

     | Id | Thêm vào chuỗi V6 |
     |---|---|
     | `f1` | `FULL_BAY.extra=1` |
     | `f2` | `FULL_BAY.spill=1` |
     | `f3` | `FULL_BAY.boost=0.15` |
     | `f4` | `FULL_BAY.boost=0.3` |

   - Ghi chuỗi đầy đủ của từng id vào `220/variants.json` **trước** khi chạy, kèm `v6` và `v0` (rỗng).
   - Tối đa **2 biến thể nữa** (`f5`, `f6`), tức tối đa 6 biến thể. Chỉ đổi núm `FULL_BAY.*` trên nền chuỗi V6, ví dụ ghép hai luật hay đổi mức `boost`. Ghi lý do bằng số của `f1`–`f4` vào `220/decision.md`, có giờ UTC, **trước** khi chạy. Lần chạy nào đổi số đều tính là một biến thể; không có lượt thử ngắn ngoài ngân sách.
   - Mỗi biến thể chạy đủ seed 1–100 (`--first=1`) và 101–200 (`--first=101`), có `--g3c`, cùng lệnh như Việc 2. Tên file: `<id>-s1.*`, `<id>-s101.*`.
   - Đo theo đúng chỉ số và luật đếm của 209 (`209/method.md`):
     - B1: số ô và số chỉ số lệch, luật sát mép;
     - B2, B3, B4, B5, B6, B7, B8; G3c, G3m, G5, G8, §7.6;
     - Nhàn I của Khá và Nhanh ở Cân bằng;
     - thứ bậc Thử thách: Nhanh − Mới, và luật không đảo của 209 (Khá và Nhanh không thấp hơn Mới quá 5 điểm).
   - Bảng "tác động so với V6" (cùng seed): Δ thắng, S, P, I, O của sáu bot Mới–Nhanh ở Cân bằng và Thử thách.
   - Lưu ý cách đọc I: I đếm lúc `live` bằng 0 mà bot không gõ (`flow.ts:166`).
     - R2 không đổi được I theo định nghĩa: khi mọi bến đều đầy thì không còn bến nhận, nên `live` vẫn là 0. R2 chỉ đổi I qua cách bot chọn bến và qua trận đấu.
     - R3 hạ I một phần vì bến đầy chưa tăng được tính `live`. Đây đúng là ý của luật (còn từ có ích để gõ), nhưng phải ghi rõ trong báo cáo.
   - **Chọn biến thể tốt nhất**, ghi vào `220/decision.md` trước Việc 7:
     - "Đạt" là đạt điều kiện ở mục 9 của phiếu 209, trên **cả hai** bộ seed. Điều kiện đó gồm B1 (đã gồm I ≤ 10 %), B7 theo luật sát mép, B2–B5, B8, B6 ≥ +10 điểm ở Cân bằng và Thử thách, G3c, G3m, G5, G8, §7.6, và Thử thách không đảo.
     - Nhiều biến thể đạt thì chọn biến thể đổi ít núm nhất. Còn hòa thì chọn I Khá lớn nhất nhỏ hơn.
     - Không biến thể nào đạt thì chọn biến thể có ít điều kiện bắt buộc trượt nhất, cộng trên hai bộ (cách 209 chọn V6). Hòa thì chọn I Khá lớn nhất nhỏ hơn, rồi ít ô B1 lệch hơn.
7. **Chạy bốn ải.** Ba cấu hình, mỗi cấu hình hai bộ seed, tổng **6 báo cáo**:

   | Id | `--set` |
   |---|---|
   | `x-v0` | không có |
   | `x-v6` | chuỗi V6 |
   | `x-<id tốt nhất>` | chuỗi của biến thể tốt nhất |

   - Mỗi báo cáo: `--stages=c1-s1,c1-s2,c1-s3,c1-s4 --seeds=100 --first=1|101 --g3c`.
   - Phiếu 209 viết rằng hằng toàn cục (`MODE_SPECS`) cần báo cáo này trước khi commit; `x-v0` là mốc để thấy V6 và luật mới đổi gì ở ải 2–4.
   - Chạy ải là độc lập (`scripts/balance-lib.ts` `runMatrix`, mỗi ải một vòng riêng). Vì vậy:
     - phần `c1-s1` của `x-v0` phải trùng `209/runs/v0-s*.json`;
     - phần `c1-s1` của `x-v6` phải trùng `209/runs/v6-s*.json`;
     - phần `c1-s1` của `x-<tốt nhất>` phải trùng báo cáo `c1-s1` của biến thể đó.
     Mọi trường, 0 ô lệch. `x-v0` và `x-v6` chạy **sau** khi đổi mã, nên đây cũng là một chứng minh nữa rằng núm tắt không đổi gì. Một ô lệch là lỗi chặn: ghi vào báo cáo, phiếu chưa xong.
   - Bảng cho từng ải `c1-s2`, `c1-s3`, `c1-s4` (V0 / V6 / tốt nhất, hai bộ seed): ô B1 lệch, I Khá và Nhanh ở Cân bằng, B3, B6, B7, G3c, Thử thách Nhanh − Mới. Đánh dấu mọi cổng mà biến thể tốt nhất làm xấu hơn V6 hay V0.
8. **Changelog** `docs/changelog/2026-10-30-full-bay-knobs.md` trong worktree, tiếng Việt:
   - ba núm và luật, mặc định tắt, chỉ ở ải chương;
   - số test trước và sau;
   - bảng tổng các biến thể (hai bộ seed) và bảng bốn ải;
   - điều chưa quyết: dấu R3 nằm ngoài mã băm; view chưa hiện luật; B9 cần người thật;
   - khuyến nghị **một** luật kèm số, để Claude quyết.

   Không đổi mặc định, `src/content/chapter-1.ts`, `MODE_SPECS` hay số nào khác.
9. **Dọn.** Sau khi đã chép mọi đầu ra vào `220/runs/` và kiểm SHA-256, xóa `tmp/codex-220/tmpdir/`. Giữ `tmp/codex-220/runs/`. Chỉ xóa file mình tạo.

## Máy dùng chung (Việc 2, 6, 7)

- Mỗi báo cáo là một tiến trình Node một luồng. Tối đa **4 báo cáo cùng lúc** (máy có 10 nhân). Tải 1 phút > 10 thì tối đa 2. Làn khác có thể đo cùng lúc (ví dụ 226 của Wordwoven, theo trần riêng của nó); trần ở đây chỉ đếm tiến trình của phiếu này.
- Ghi `uptime` trước mỗi đợt; ghi giờ bắt đầu, giờ kết thúc, số tiến trình cùng lúc (theo mẫu `209/evidence/wave-*.json`, lưu ở `220/evidence/wave-*.json`).
- Ước lượng theo 209: một báo cáo `c1-s1` mất 190–290 s; báo cáo bốn ải khoảng gấp 4. Toàn phiếu tối đa 2 + 12 + 6 = 20 báo cáo, khoảng 2,5–3 giờ máy. Ghi số thật.
- Test thời gian ở làn khác có thể đỏ trong lúc này. Ghi giờ để Claude đối chiếu.

## Cấm

- Mọi lệnh git có ghi. Được dùng `status`, `diff`, `log`, `rev-parse`, `show`.
- Sửa `src/view/**`, `src/app/**`, `src/kit/**`, `src/audio/**`, `tests/golden/**`, `scripts/**`. Chạy `kit:sync`.
- Sửa số nào khác trong `src/content/**` (kể cả `chapter-1.ts`, `balance.ts`, `MODE_SPECS`), hay đổi mặc định của `FULL_BAY`.
- Thêm typed array hay số ở tầng đầu bất kỳ phần nào `hashWorld` trộn. Thêm loại sự kiện `EV` mới.
- Sửa `world.ts` ngoài dòng 119, sửa `words.ts` ngoài `finish`, sửa `pace.ts` ngoài `flowSnapshot`, JSDoc của nó và import.
- Quá 6 biến thể; quá 4 tiến trình đo cùng lúc (quá 2 khi tải > 10).
- `pnpm install`, mạng, dev server, trình duyệt, `heavy.sh`. Ghi ra ngoài repo.
- Đụng worktree khác (`games/.wt-ts-art`, `.wt-ts-typefx`, `.wt-ts-vfx`, `.wt-dh-*`, `.wt-td-*`). Ghi vào checkout chính `games/typing-survival`. Đụng game khác, Tu Tiên.
- Chữ tiếng Việt trong chuỗi người chơi thấy (phiếu này không thêm chuỗi nào).

## Kiểm (ghi số)

1. `pnpm check` trong worktree thoát 0, log ở `220/logs/check-after.txt`. Số test bằng mốc cộng số test mới, 0 test hỏng. Mốc theo `210-report.md` là 296 test trong 26 file; ghi số thật, sau phiếu phải là 27 file. Kit verify khớp mọi file (61/61 theo 205, 210). `tsc` và build xanh. Nếu chỉ test thời gian của `tests/survival-sim.test.ts` ("steps 700 foes and 2,000 rounds in ≤ 1.5 ms") đỏ trong lúc tải 1 phút > 8, chạy riêng file đó tối đa 3 lần, ghi từng lần.
2. Test mới: số đỏ trước khi viết mã, số xanh sau; ba đột biến của Việc 5 đều làm test đỏ, trả lại thì xanh.
3. SHA-256 của `tests/golden/s0-trace.json` trước và sau đều là `42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea`.
4. `scripts/chapter-hashes.ts` trước và sau: mỗi lần 152 dòng; `diff 220/chapter-before.txt 220/chapter-after.txt` thoát 0.
5. Tái tạo V6: 0 ô lệch (mọi trường `summary`, 36 ô × 2 bộ) so với `209/runs/v6-s1.json` và `v6-s101.json`. Phần `c1-s1` của `x-v0` và `x-v6` (chạy sau khi đổi mã) cũng 0 ô lệch so với 209.
6. Báo cáo đo:
   - mỗi `.err` có đúng các dòng `--set: … old→new` của biến thể, ví dụ `c1-s1.drainRate 2→2.4, MODE_SPECS.challenge.surge 1.1→1, MODE_SPECS.challenge.rate 1.12→1.06, FULL_BAY.boost 0→0.15`; `x-v0` không có dòng nào;
   - số biến thể ≤ 6;
   - số báo cáo `c1-s1` = 2 + 2 × số biến thể; cộng đúng 6 báo cáo bốn ải;
   - mọi lệnh thoát 0;
   - mỗi JSON `c1-s1` có 36 ô, mỗi ô `runs` 100; mỗi JSON bốn ải có 144 ô; Markdown có đủ 10 cặp G3c mỗi ải;
   - JSON, MD và `.err` của mọi báo cáo nằm ở `220/runs/`, SHA-256 trùng bản trong `tmp/codex-220/runs/`.
7. Bảng mỗi biến thể × bộ seed (`220/summary.md` và `summary.json`, sinh bằng `220/tools/summarize.mjs`; chạy lại ra cùng SHA-256):
   - B1: số ô lệch, số chỉ số lệch;
   - I của Khá và Nhanh ở Cân bằng (đích ≤ 10 %);
   - B3 (Mới ở Cân bằng ≥ 70 %, Trẻ em ở Thư giãn ≥ 85 %), B6, B7;
   - G3c (tốt nhất ≤ 97 %);
   - Thử thách Nhanh − Mới ≥ 0;
   - B9: "THIẾU SỐ: cần người thật chơi".
8. Tải máy: `uptime` đầu mỗi đợt, số tiến trình cùng lúc, tổng giờ máy (cộng các dòng "cả lệnh … s"), tổng thời gian thật. `TMPDIR` đã dùng: `games/.wt-ts-codex/tmp/codex-220/tmpdir`, ghi đường tuyệt đối.
9. Worktree sau phiếu:
   - `git -C games/.wt-ts-codex status --short -uall` chỉ có đường dẫn trong "Chỉ được ghi";
   - `git -C games/.wt-ts-codex diff --quiet -- src/view src/app src/kit src/audio tests/golden scripts` thoát 0;
   - `git -C games/.wt-ts-codex diff --name-only -- src/content` chỉ ra `src/content/guns.ts`;
   - `git -C games/.wt-ts-codex diff --numstat -- src/sim/world.ts` ra `1	1`;
   - `git -C games/.wt-ts-codex diff --check` thoát 0;
   - HEAD vẫn là `ba6d70e`.
10. Repo cha: `git status --short -uall` trước và sau, lưu ở `220/evidence/`. Phiếu này chỉ thêm `220-report.md` và `220/`. Thay đổi của làn khác thì liệt kê, không đụng.
11. `tmp/codex-220/tmpdir/` đã xóa; `tmp/codex-220/runs/` còn.

## Báo cáo phải có

- Kết luận đầu tiên: luật nào được khuyến nghị, kèm núm và số, hay vì sao chưa luật nào đủ.
- Số đỏ/xanh của test, ba đột biến, số `pnpm check` trước và sau, Kiểm 3 và 4.
- Tái tạo V6 (Kiểm 5).
- Bảng tổng các biến thể (Kiểm 7), bảng Δ so với V6, bảng bốn ải, `decision.md`.
- Phần "View cần gì nếu chọn luật này", chỉ liệt kê, không sửa:
  - **R1:** `hud.ts:173` vẽ 3 ô băng và `:333` (`is-full`) tự theo `cap`; kiểm bố cục thẻ bến với 3 ô.
  - **R2:** `typing-feel.ts:140` chỉ coi là nạp khi `EV.load` cùng bến, nên từ tràn sẽ hiện `FULL` và tiếng "full". Cần một hiệu ứng nối từ bến đầy sang bến nhận, và chữ tiếng Anh cho nhãn mới. `shots.ts:137` đọc bến từ `R.slot` nên bến nhận đã đúng.
  - **R3:** không có sự kiện nên người chơi không thấy gì. Cần một sự kiện hay cờ, một nhãn tiếng Anh trên dải chữ và một tiếng; cả hai qua phiếu ảnh và âm thật, không vẽ bằng mã.
- Ghi chú về mã băm: dấu R3 nằm ngoài `hashWorld`.
- Kiểm 8–11.

**Xong khi:** đủ chín việc và mười một mục kiểm có số; mặc định tắt và không đổi một byte nào khi tắt (Kiểm 3, 4, 5); báo cáo khuyến nghị một luật kèm số hay nói rõ vì sao chưa. Claude duyệt, chọn luật, rồi commit mã trên `ts-codex` cùng changelog, và commit `docs/codex-queue/220*` ở repo cha.

## Lưu ý

- Mọi số ở đây là số của bot. Khuyến nghị nói "bot đạt", không nói "người chơi thấy vừa". B9 cần người thật chơi.
- Hai bộ seed lệch nhau tới 16 điểm thắng (review-fix mục 4): không kết luận từ một bộ.
- V6 chưa được áp vào game (209: "không áp V6 khi còn cổng đỏ"). Phiếu này dùng V6 làm nền đo, không đưa V6 vào `src/content`.
- G3m đo trong `tests/survival/arena.ts` (ải chương `COUNTER_STAGE`, một súng, nạp thẳng bằng `loadMagazine`). Vì vậy G3m chỉ thấy R1 (sức chứa 3); R2 và R3 không chạy ở đó. Ghi điều này cạnh số G3m của từng biến thể, đừng đọc G3m như bằng chứng cho R2 hay R3.
