# Phiếu 223 · Dragonhold · DH-08: bot headless chơi như lượt phím thật 35 WPM (chọn từ gần nhất, phản xạ tính từ lúc chữ hiện), đo lại G1, B4 và máu mất mỗi đợt

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §1.2 mục 13: "DH-08 · P1 · G3. Bot mất khoảng 150 máu mỗi đợt, người thật gần như không mất. **Sửa:** bot chọn từ gần nhất và có độ trễ khi chữ vừa hiện, cho giống dữ liệu chơi thật; đo lại G1 và B4. **Làm trước DH-06**".
- Cùng file, cuối §5.3: "Hôm nay bot mất khoảng 150 máu mỗi đợt vì Héo lan, còn người thật gần như không mất."
- `docs/games/map1/audit-2026-10-28.json`, mục DH-08:
  - "35 WPM thật kết thúc 100 % máu, máu không tụt quá 33 dưới mức đầu đợt. Bot lại mất khoảng 150 máu mỗi đợt, nên G1 86,7 % của bot không khớp cảm giác chơi";
  - cách sửa: "… Nếu người thật vẫn quá dễ, đề xuất tăng sức ép ±10 % trong dữ liệu ở mức Thường".
- "35 WPM thật" ở trên là kịch bản CDP `games/dragon-hold/tmp/map1-audit/scen/feel.mjs` gõ phím thật vào trình duyệt, không phải người.
  - `feel-35-1280/report.json` → `result.profile` là `{ wpm: 35, acc: 0.97, mode: "normal", seed: "1", size: "1280x720" }`.
  - Kết quả: thắng 10/10 đợt, kết thúc 653/653 máu.
  - Cách kịch bản gõ:
    - chọn từ gần nhất (`PICK`, dòng 58–68);
    - phím cách nhau `max(5, KEY_MS × (0,6 + 0,8 r) − 6)` ms, với `KEY_MS = 60000 / (35 × 5)` (dòng 32, 234–238);
    - trượt sang phím bên cạnh (bảng `NEAR`, dòng 33) với xác suất `1 − ACC`, chỉ từ chữ cái thứ hai (dòng 398–405);
    - không có phản xạ nào ngoài vòng hỏi 90 ms (dòng 376).
- `scripts/balance/reader.ts` đã có `Aim` `"nearest"`. `scripts/balance/typist.ts` đã trộn `danger`, `nearest`, `first` (kit `TARGET_MIX.fair` = 0,4 / 0,4 / 0,2). Nhưng phản xạ hiện tính từ lúc bot chọn từ (`typist.ts:95`, `typist.ts:122`), không tính từ lúc chữ hiện. Khoảng cách giữa bot và trình duyệt vì vậy đo được bằng số, không cần đoán.
- Chưa ai làm DH-08. Các commit chạm `scripts/balance` từ 27/10 thuộc D33, Codex 051 và 094; không commit nào về bot giống người.

**Không trùng:**
- 195 ước tính thời gian không có chữ (`idle-estimate.mjs`) cho DH-05; phiếu này không đụng phần đó.
- DH-06 (Chữ Bẫy) chờ phiếu này.
- 209 và 220 là cân bằng của Last Line.
- Phiếu này không đổi luật chơi và không đổi bot cũ.

**Báo cáo:** `docs/codex-queue/223-report.md` (tiếng Việt), thư mục `docs/codex-queue/223/`. Cả hai ở repo cha.

## Chỉ chạy khi

1. Có `docs/codex-queue/222-report.md` và `docs/codex-queue/222/attribution.json`. Thiếu thì dừng.
2. Nhánh là `dh-codex`. HEAD là `6aa593a2dce6637cccbe24a58709b86f7127f607`, hoặc một commit sau nó mà mọi commit mới (`git -C games/.wt-dh-codex log --name-only 6aa593a..HEAD`) chỉ chứa đường dẫn có trong `attribution.json`. Khác thì dừng.
3. Mọi đường dẫn trong `git -C games/.wt-dh-codex status --short -uall` đều có trong `paths` của `attribution.json`. Có đường dẫn lạ, hay đường dẫn nằm trong `unattributed`: dừng, ghi tên.
4. Trước khi sửa gì, `pnpm check` trong worktree xanh. Đỏ thì dừng, ghi các test đỏ. Không sửa file của 187, 194, 195, 197.
5. Năm file dữ liệu trình duyệt có và đọc được. sha256 của `samples.json` là `d9e4220369c0f6131db82c2ed41073ff108b58e5f40a79b86abc79246ce1f0f7`. Khác thì ghi lại, làm tiếp với file đang có.

Phiếu này không cần Claude duyệt 194, 195, 197 trước. Nó chỉ không được đụng vào file của các phiếu đó.

## Nơi làm

- Worktree `games/.wt-dh-codex`, nhánh `dh-codex`.
  - Làn `s7`, chạy sau 222. cwd của làn là repo cha (`.`); lệnh `pnpm` chạy trong worktree.
  - Model `gpt-6.1-sol`, mức `high`.
- `TMPDIR` là đường tuyệt đối của `games/.wt-dh-codex/tmp/codex-223/tmpdir`. Mọi đầu ra đo để ở `games/.wt-dh-codex/tmp/codex-223/`.
- Chạy `tsx`:
  - `pnpm dh:balance` dùng CLI `tsx`. Gặp `listen EPERM` (195 đã gặp, xem `docs/codex-queue/195/balance.log`) thì chạy `TSX_DISABLE_CACHE=1 node --import=tsx scripts/balance/run.ts <cùng tham số>`;
  - script đo riêng: `TSX_DISABLE_CACHE=1 node --import=tsx tmp/codex-223/<tên>.ts`.
- Dữ liệu trình duyệt, chỉ đọc:
  - `games/dragon-hold/tmp/map1-audit/feel-35-1280/`: `samples.json`, `timeline.json`, `rc-raw.json`, `report.json`, `idle.json`;
  - kịch bản: `games/dragon-hold/tmp/map1-audit/scen/feel.mjs`, `scen/hook.mjs`.

### Dữ liệu trình duyệt: định dạng và bối cảnh

- **`samples.json`:** mảng 7.149 dòng, khoảng 100 ms một dòng, dạng `[ms, phase, wave, words, visibleWords, liveFoes, hp]`.
  - `phase`: 0 prep, 1 warning, 2 wave, 3 break, 4 victory, 5 defeat (hằng `SAMPLER` trong `feel.mjs`).
  - `ms` là `performance.now()` của trang.
- **`rc-raw.json` → `letters`:** 905 phím chữ, mỗi phím `{ t, key, wave, … }`. `t` cũng là `performance.now()` của cùng trang, nên so thẳng được với `ms`. `rc-raw.hurt` ghi 0/0 vì móc không gắn được: không dùng.
- **`timeline.json`:** 363 ảnh trạng thái, khoảng 1 s một lần, có `t`, `tick`, `phase`, `wave`, `hp`, `hpMax`, `words`, `kills`, `keys`… Dùng để nối `ms` với tick của sim.
- **`report.json`:**
  - `result.hpAtWave`;
  - `result.real`: 682 s, 905 chữ cái, 13 phím sai;
  - `result.stats`: 168 từ, 36 kỹ năng, 6 Viêm Đế, 27 từ Thẻ Ôn.
- **Kịch bản chơi ở chế độ `normal`:**
  - thẻ tốc độ 35 WPM, rồi Học trước;
  - mỗi lượt nghỉ: mua đồ (`shop`, dòng 183–199), làm Thẻ Ôn, rồi Shift + Enter gọi đợt sớm (dòng 281);
  - trong đợt (dòng 370–373):
    - Alt + 1 mỗi ≥ 8 s khi có ≥ 3 quái;
    - Alt + 2 mỗi ≥ 11 s khi có ≥ 5 quái;
    - Alt + 5 khi Rage ≥ 1000;
    - Alt + 7 khi máu < 45 %.
- **Thế giới trên trình duyệt:**
  - seed 1, mức Thường, `typistWpm` 35 lấy từ thẻ tốc độ;
  - không đặt `accuracyPm`, `cvPm`, nên lấy mặc định `PACE`: 950 và 250 (`src/content/rules.ts:132–133`, `src/app/app.ts:514–520`).
- **Phiên bản:**
  - `tests/golden/m0.json` không đổi từ `67cacc2` (28/10, 07:51), trước lượt chạy trình duyệt (28/10, khoảng 17:43). Luật sim trong phạm vi golden vì vậy giữ nguyên.
  - Bộ từ khác nhau: trình duyệt dùng từ vựng ghim, bot dùng `botDeck()`.

### Mốc đối chiếu

Claude đã chạy thử trên trạng thái hiện tại ngày 30/10:
- `pnpm dh:balance --trace=b35:1`: thắng; `metrics.waves[].heroDamage` theo đợt là 0, 107, 229, 101, 50, 188, 160, 75, 117, 183 (tổng 1.210);
- `pnpm dh:balance --seeds=20 --bots=b35`: balanced 85,0 % (40 seed).

Dùng hai số này để kiểm đường đo của bạn. Số bạn đo phải khớp.

## Chỉ được ghi (tính từ worktree)

- `scripts/balance/human.ts` (mới): hai bot và các hàm đo dùng lại được.
- `scripts/balance/bot.ts`: tối đa 40 dòng thêm cộng xóa (`git diff --numstat`). Chỉ để thêm một móc tùy chọn cho typist riêng.
- `scripts/balance/run.ts`: tối đa 16 dòng thêm cộng xóa. Chỉ để tra tên bot mới ở `--bots=`, `--trace=` và trong worker.
- `tests/sim/bot-human.test.ts` (mới).
- `docs/changelog/<ngày chạy>-human-like-bot.md` (mới, tiếng Việt), dự kiến `2026-10-30-human-like-bot.md`.
- `tmp/codex-223/**`: script đo dùng một lần, JSON, `TMPDIR`.
- Ở repo cha: `docs/codex-queue/223-report.md`, `docs/codex-queue/223/**`.

## Việc

1. **Mốc đầu.** Lưu vào `223/`:
   - `start-status.txt` (`git status --short -uall`), `start.diff` (`git diff`), HEAD;
   - md5 của `tests/golden/m0.json`, phải là `75f74947dac170d05fd659f99417940e`;
   - `src-before.sha256`: sha256 mọi file dưới `src/` và `tests/golden/`;
   - `bots-before.txt`: `BOT_NAMES` và `M0_BOTS` đúng thứ tự. Lúc soạn phiếu:
     - `BOT_NAMES` có 15 tên: b0, b25, b35, b60, typingOnly, noTyping, child, novice, steady, skilled, sloppy, fast, b35good, b35poor, b35off;
     - `M0_BOTS`: b0, b25, b35, b60, typingOnly, noTyping;
   - `default-before.json`: `pnpm dh:balance --seeds=3 --jobs=4 --json=tmp/codex-223/default-before.json` (15 bot mặc định, hai bộ seed, ba chế độ);
   - `check-before.log`: `pnpm check` (lúc soạn phiếu: 69 file, 593 test).
2. **Số trình duyệt** (seed 1, 1280, 35 WPM, 97 %). Mỗi đợt 1–10 một hàng; ghi `223/browser-waves.json` và một bảng. Các cột:
   - máu đầu đợt (mẫu đầu tiên có `phase` 2 của đợt), máu thấp nhất trong đợt, độ tụt = đầu đợt − thấp nhất;
   - số chữ cái gõ trong đợt (các `letters` có `t` nằm trong cửa sổ đợt) và số chữ cái mỗi phút;
   - số từ gõ xong. Ghi cách suy, ví dụ từ `timeline.kills` hay từ cột `words`. Không suy được thì ghi "không đo được" và lý do;
   - phản xạ: mỗi lần `visibleWords` từ 0 lên ≥ 1 trong đợt, đo thời gian tới phím chữ đầu tiên ngay sau đó. Ghi p50, p90, số mẫu; sai số ±100 ms vì mẫu thưa;
   - tỉ lệ chọn từ gần nhất: theo mã `PICK` thì là 100 % số lần chọn tự do (từ đang khóa và chữ `urgent` đi trước). Ghi đúng như vậy, không ước lượng thêm.

   Script đọc dữ liệu là `tmp/codex-223/browser.mjs` (Node, chỉ đọc); chép một bản vào `223/`.
3. **Số headless của b35 trên cùng seed.**
   - Chạy `pnpm dh:balance --trace=b35:1`. Đầu ra JSON có `metrics.waves`.
   - Viết script đo `tmp/codex-223/measure.ts`, gọi `runBot` với `onTick` để lấy đúng các cột của việc 2:
     - máu đầu đợt, máu thấp nhất, độ tụt, `heroDamage`;
     - số từ xong, chữ cái mỗi phút;
     - phản xạ: từ `bornTick` của từ tới phím đầu gõ vào nó. Chỉ tính các từ ra lúc không còn từ sống nào, giống định nghĩa ở trình duyệt;
     - tỉ lệ chọn từ gần nhất: từ được chọn có `distance` nhỏ nhất trong các từ đang thức. Không tính từ đang khóa và chữ đặc biệt.
   - Sau đó chạy cho seed 20261023…20261042 và 21261026…21261045, mức Thường. Ghi p50 và p90 mỗi đợt.
   - Hàm đo dùng lại được (dựng bảng mỗi đợt từ một lượt chạy) đặt trong `human.ts` và có test. Phần nối dùng một lần đặt trong `tmp/codex-223/`.
4. **Hai bot mới, chỉ chạy khi gọi đúng tên** (trong `scripts/balance/human.ts`).

   **`b35cdp`** chép hành vi của `feel.mjs`, để so với lượt trình duyệt:
   - **Chọn từ** đúng thứ tự `PICK`, xét mọi từ sống, kể cả từ đang ngủ:
     1. từ đang khóa, gõ tiếp từ chữ đã gõ;
     2. từ `urgent`;
     3. từ cờ (`kind === "flag"`) không có quái sống;
     4. từ có quái gần tâm đài nhất;
     5. từ không có quái.
   - **Nhịp phím:**
     - sau mỗi phím chờ `max(5, KEY_MS × (0,6 + 0,8 r) − 6)` ms, với `KEY_MS` = 342,857 ms;
     - sau mỗi từ chờ `KEY_MS × (0,5 + r)`.
   - **Trượt phím:**
     - chỉ từ chữ thứ hai của từ (`i > 0`, hay từ đã có chữ gõ), xác suất 0,03;
     - nhấn một phím trong bảng `NEAR` của `feel.mjs` (chép nguyên bảng);
     - sau phím trượt, nếu khóa đã sang từ khác hay từ đã mất thì bỏ từ đó và chọn lại.
   - Không Backspace, không Esc.
   - **Khi không có từ:** thử lại theo phân bố đo ở việc 2 (vòng hỏi 90 ms cộng độ trễ eval). Không dùng 450 ms.
   - **Kỹ năng** như dòng 370–373 của `feel.mjs`, gửi bằng `SimCommand` có sẵn. Ánh xạ phím: Alt + 1 → `{ type: "skill", skill: "breath" }`; Alt + 2 → `skyfire`; Alt + 5 → `inferno`; Alt + 7 → `{ type: "consumable", item: "small-potion" }`. Kiểm lại ánh xạ trong `KEYS` (`src/content/rules.ts:726–753`) và `src/ui/hud.ts`.
   - **Lượt nghỉ:**
     - dùng `Plan` với `policy` của `BOTS.b35`, nhưng `skills: false`, vì b35cdp tự gửi kỹ năng;
     - thêm `{ type: "call-early" }` sau khi mua xong, như Shift + Enter của kịch bản. `Plan` hiện không gọi lệnh này.
   - **Thế giới:** seed, mức Thường, `typistWpm` 35, `accuracyPm` 950, `cvPm` 250, như thẻ tốc độ trên trình duyệt. Tay gõ vẫn đúng 97 %.

   **`b35human`** giống b35 (cùng `humanHands` của bot `standard`: 35 WPM, 95 %, CV 0,25, raw). Chỉ khác ở hai điều DH-08 nêu:
   - **Chọn từ gần nhất trước:** trộn mục tiêu nghiêng về gần nhất, trọng số `nearest` ≥ 0,6. Ghi trọng số đã chọn và lý do.
   - **Phản xạ tính từ lúc chữ hiện:**
     - phím đầu của một từ không được sớm hơn `bornTick` cộng thời gian nhận ra từ;
     - thời gian nhận ra theo kit `RECOGNIZE`: từ quen 0,35–0,6 s, đang học 0,5–0,9 s, mới 0,8–1,6 s. Nhóm không rõ thì dùng 450 ms × (0,6–1,4) như `hands.ts` (00 §4.3);
     - từ đã hiện đủ lâu trước khi bot rảnh thì không chờ thêm, chỉ còn khoảng cách phím;
     - phản xạ p50 của b35human không được nhỏ hơn p50 đo ở trình duyệt.

   **Luật chung cho hai bot:**
   - Không đặt trường `standard`, để B1–B9 của bộ bot mặc định giữ nguyên.
   - Không thêm vào `BOTS`, `BOT_NAMES`, `M0_BOTS`.
   - Xúc xắc riêng như `runBot` (seed XOR tên bot). Cùng seed chạy hai lần ra cùng `finalHash`.
   - Không sửa `typist.ts`, `hands.ts`, `reader.ts`, `policy.ts`, `meter.ts`, `report.ts`, `golden-spec.ts`. Dùng lại bằng import hay bọc.
   - **Móc trong `bot.ts`:**
     - một trường tùy chọn trên `BotSpec` cho typist riêng (typist này cần đọc `world` để gửi kỹ năng), và một nhánh trong `runBot`;
     - bot cũ không đặt trường này, nên đi đúng đường cũ với cùng các lần rút xúc xắc;
     - `meter.scan` vẫn nhận `busy` và số lần nhả khóa.
   - **`run.ts`:**
     - dùng một hàm tra tên đặt trong `human.ts` (ví dụ `findBot(name)` trả `BOTS[name] ?? HUMAN_BOTS[name]`) ở `--bots=`, `--trace=` và trong worker;
     - không có `--bots=` thì danh sách vẫn là `BOT_NAMES`.
   - `report.ts` không sửa. Hệ quả với hai bot mới: `label` là tên bot, `capacityWpm` là 0, không có `learnOk`. Đừng dùng ba trường đó.
5. **Test viết trước** trong `tests/sim/bot-human.test.ts`. Ghi số đỏ trước khi viết mã.
   1. `BOT_NAMES`, `M0_BOTS`, `Object.keys(BOTS)` đúng như `bots-before.txt`. `findBot("b35cdp")` và `findBot("b35human")` trả bot, nhưng hai tên này không nằm trong `BOT_NAMES`. Tên lạ trả `undefined`.
   2. b35cdp chọn từ trên một `TypingView` dựng tay đúng thứ tự: khóa > `urgent` > cờ > gần nhất > không có quái.
   3. Nhịp phím của b35cdp:
      - khoảng giữa hai phím nằm trong [max(5, 0,6 KEY_MS − 6), 1,4 KEY_MS − 6];
      - khoảng sau một từ nằm trong [0,5; 1,5] × KEY_MS;
      - không trượt ở chữ đầu; phím trượt thuộc `NEAR[chữ]`.
   4. b35human không nhấn phím đầu trước `bornTick` + phản xạ. Với từ đã hiện từ lâu, bot nhấn ngay khi rảnh.
   5. Thế giới của cả hai bot có `pace` bằng `pace` của `createWorld(STAGE_M0, seed, { typistWpm: 35, deck })`, không đặt độ chuẩn và CV.
   6. Cùng seed, hai lần chạy ngắn (ví dụ 2 phút sim) ra cùng `finalHash` và cùng log.
   7. Hàm đo mỗi đợt, trên một lượt dựng tay, cho đúng độ tụt máu, số từ, phản xạ.

   Cả file test chạy dưới 10 s. Không sửa golden và các file `tests/sim/bot-*.test.ts` cũ.
6. **Hiệu chỉnh b35cdp trên seed 1.**
   - Mục tiêu: độ tụt máu mỗi đợt cách lượt trình duyệt không quá 15 máu, ở ít nhất 8/10 đợt.
   - Tối đa 3 lần thử. Mỗi lần chỉ đổi một nhóm, và ghi bảng mỗi đợt:
     - lần 1: đúng như việc 4;
     - lần 2 và 3: chọn theo số, trong các hướng sau.
       - Mua đồ như `shop` của kịch bản (dòng 183–199): phím 1–5 (`carry-n`) theo giá; ô chọn bằng `wave % 3` lần mũi tên; phím 6 hai lần; rồi `` ` `` (`edit-mode`) và `=` (`upgrade`) hai lần. Ánh xạ sang `place`, `buy`, `upgrade` qua `KEYS` và `src/ui/placement-ui.ts`.
       - Bộ từ thật, dựng như `tests/app/pinned-deck.test.ts`.
       - Phản xạ chậm hơn hay nhanh hơn, trong khoảng đã đo được.
   - Không đạt sau 3 lần: chỉ ra bằng số cơ chế nào lệch, kèm bảng mỗi đợt của cả ba nguồn (trình duyệt, b35cdp, b35). Các cơ chế cần xét:
     - Héo lan theo `stepBlight` trong `src/sim/combat.ts`: từ chờ quá `graceTicks`, quái đứng trong Vùng Chữ mà không có từ;
     - đòn đánh của quái;
     - bẫy;
     - hồi máu.
7. **Đo.**
   - `uptime` trước mỗi lượt. Tối đa 4 jobs; tải 1 phút trên 10 thì tối đa 2.
   - Lệnh: `pnpm dh:balance --bots=b35,b35cdp,b35human,steady,sloppy --seed-sets=2 --seeds=20 --modes=balanced --jobs=4 --json=tmp/codex-223/measure.json`. `steady` và `sloppy` cần cho B4.
   - Lấy từ JSON và script đo, cho mỗi bot:
     - **G1:** thắng % ở balanced, mỗi bộ seed và gộp 40 seed, so với dải `M0_GATES.win35` [75, 90] (`src/content/rules.ts:762`). Thắng % do `measure.ts` tính phải khớp `winPct` trong JSON;
     - **B4:** `kit.killSeconds` của bot so với `sloppy` (phải nhỏ hơn); `kit.s` của `steady` so với `sloppy` (không được đổi);
     - **máu mất mỗi đợt:** p50 và p90, cả độ tụt lẫn `heroDamage`, từ script đo;
     - khóa bị mất (`typing.locksLostPct`), nhàn I (`kit.i`), an toàn S (`kit.s`);
     - thời gian chạy.
   - Bảng cũ so với mới: b35 (cũ) so với b35cdp và b35human.
8. **Đề xuất cho Claude.**
   - Bot nào nên đại diện cho G1 và B4: giữ b35 hay đổi, vì sao, kèm số.
   - Nếu b35cdp hay b35human cho thấy người chơi vẫn thấy dễ, đo thêm bot được đề xuất (2 × 20 seed, balanced; ghi G1 và máu mất mỗi đợt):
     - với cờ `--pace=1.1` và `--pace=0.9` có sẵn (tải × 1,1 hay × 0,9, cùng quái);
     - và chỉ trong `measure.ts`: Héo lan × 1,1 ở mức Thường, bằng cách đổi trong bộ nhớ `PRESSURE.difficultyPm.normal` từ 1000 thành 1100. Đối tượng này không bị đóng băng. Cách này không chạy qua `pnpm dh:balance`, vì worker không thấy giá trị đã đổi. Ghi giá trị đã dùng.
   - Không sửa `src/content/**`.
9. **Changelog** trong worktree, gồm:
   - làm gì, vì sao (DH-08);
   - hai bot mới và cách gọi: `--bots=b35cdp,b35human`, `--trace=b35human:1`;
   - số test trước và sau;
   - bảng G1, B4 cũ và mới;
   - đề xuất.

## Cấm

- Sửa `src/**` và `tests/golden/**`.
- Sửa file trong `scripts/balance` ngoài `bot.ts` và `run.ts` (trong giới hạn dòng). Đổi hành vi bot cũ. Chạy `dh:golden:update`.
- Sửa file của 187, 194, 195, 197 (danh sách ở `222/attribution.json`), kể cả `scripts/balance/idle-estimate.mjs` và các file `tests/app/*` của chúng.
- Mọi lệnh git có ghi. `kit:sync`.
- Ghi vào `games/dragon-hold/**` (dữ liệu trình duyệt chỉ đọc), worktree khác, game khác, Tu Tiên.
- Dev server, trình duyệt, mạng.

## Kiểm (ghi số)

1. **Golden:** md5 của `tests/golden/m0.json` trước và sau đều là `75f74947dac170d05fd659f99417940e`. Test golden xanh 10/10; nó chạy lại b35, noTyping, sloppy và phải ra đúng log cũ.
2. **Phạm vi:**
   - sha256 mọi file dưới `src/` và `tests/golden/` trước và sau giống nhau (0 khác);
   - `git -C games/.wt-dh-codex diff --stat` và status: ngoài file của 187, 194, 195, 197, chỉ có `scripts/balance/bot.ts`, `run.ts`, `human.ts`, `tests/sim/bot-human.test.ts` và changelog;
   - `git diff --numstat`: `bot.ts` ≤ 40, `run.ts` ≤ 16.
3. **`pnpm check`:** mã thoát 0; số test = trước + mới, 0 đỏ; 75 file kit; build xanh. Test mới đỏ trước khi viết mã (ghi số).
4. **Bot cũ không đổi:**
   - `bots-before.txt` giống `bots-after.txt`;
   - `default-before.json` và `default-after.json` (cùng lệnh ở việc 1) giống nhau sau khi bỏ `steps`, tức lệnh `cmp <(jq -S 'del(.byMode[][].steps)' default-before.json) <(jq -S 'del(.byMode[][].steps)' default-after.json)` trả mã 0. Claude đã thử: hai lượt liền nhau trên mã không đổi chỉ khác ở `steps`.
5. **Hiệu chỉnh trên seed 1:** bảng mỗi đợt của trình duyệt, b35cdp và b35, gồm độ tụt máu, số từ, chữ cái mỗi phút, phản xạ p50 và p90. Ghi số đợt nằm trong ±15 máu: n/10.
6. **Đo:**
   - số seed mỗi bộ, số bộ, các bot, các chế độ;
   - thời gian chạy và `uptime` trước mỗi lượt; số jobs;
   - G1 mỗi bot, mỗi bộ seed; B4; máu mất mỗi đợt p50 và p90.
7. **Dọn:**
   - `tmp/codex-223/tmpdir` đã xóa;
   - JSON thô đã chép vào `223/`, sha256 khớp với bản trong `tmp/codex-223/`;
   - không có ảnh chụp nào, nên không cần `capture-prune`.

## Báo cáo gồm

- **Kết luận** một đoạn: bot nào giống lượt trình duyệt; G1 và B4 cũ và mới; đề xuất.
- **Mốc:** điều kiện chạy (HEAD, status so với `attribution.json`), số test trước.
- **Bảng trình duyệt** mỗi đợt, kèm cách tính.
- **Bảng hiệu chỉnh** của từng lần thử.
- **Bảng đo** 2 × 20 seed.
- **Phần `--pace` và Héo lan × 1,1**, nếu có làm.
- **Các dòng đã đổi** trong `bot.ts` và `run.ts` (chép nguyên).
- **Bảy mục kiểm** kèm số.
- **File trong `223/`:**
  - `start-status.txt`, `start.diff`, `src-before.sha256`, `src-after.sha256`;
  - `bots-before.txt`, `bots-after.txt`;
  - `default-before.json`, `default-after.json`;
  - `check-before.log`, `check-after.log`, `tests-red.log`;
  - `browser.mjs`, `measure.ts`, `browser-waves.json`, `calibration-*.json`, `measure.json`;
  - `status-final.txt`.

**Xong khi:** chín mục việc và bảy mục kiểm đều đạt, có số. Sau đó Claude duyệt diff, chọn bot đại diện cho G1 và B4, rồi commit cùng hay sau phần 187–197.
