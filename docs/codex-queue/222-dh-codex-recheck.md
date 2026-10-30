# Phiếu 222 · Dragonhold · Kiểm lại độc lập phần chưa commit trên `dh-codex` (187, 194, 195, 197) trước khi Claude duyệt; chỉ đọc, chạy kiểm trên bản chép

**Nguồn:**
- `docs/HANDOFF_CURRENT.md` §2: "Codex không chạy git có ghi; Claude duyệt rồi mới commit." Cùng file, 30/10: "11:20: chủ dự án bảo Claude dừng mọi việc, chỉ giao việc cho Codex". Phần chưa commit trên `dh-codex` đang chờ một lượt duyệt mà chưa ai làm:
  - 187: nguồn cổng game là biến lúc build;
  - 194: 36 icon UI;
  - 195: bảng báo bộ từ lỗi, chặn Low ở bản phát hành, tự tua ×1,75;
  - 197: màn tựa.
- `tools/codex-run/README.md`, bảng "Chọn model": "Kiểm lại độc lập, phản biện (đọc diff, tìm lỗi người sửa bỏ sót) | `gpt-6.1-sol` | `xhigh`".
- `docs/codex-queue/195/resume2-report.md` (lượt 09:20 của 195): "Chưa thực hiện hoặc xác nhận lại 11 mục việc và 7 mục kiểm". Phần này đi qua nhiều lượt bị cắt rồi chạy lại: 194 ba lượt, 195 ba lượt, 197 hai lượt. Vì vậy cần một lượt kiểm độc lập trên trạng thái cuối.
- `docs/games/MAP1_PRODUCTION.md` §1.1, hàng Dragonhold:
  - G5: "Thiếu màn tựa, màn cài đặt, lối về cổng game";
  - G7: "Bản build không có từ vựng: quái không có chữ, thua ở đợt 1, không báo gì".
  Bốn phiếu trên đóng các mục này.

**Không trùng:**
- 187, 194, 195, 197 chỉ tự kiểm phần của mình, cùng một người làm.
- Từ 169 chưa có lượt kiểm độc lập nào cho `dh-codex`. (019 là kiểm lại Wordwoven.)
- Phiếu này không sửa gì. Claude sửa sau khi đọc báo cáo.
- 223 (bot giống người) chạy sau phiếu này và dùng danh sách quy file của nó.

**Báo cáo:** `docs/codex-queue/222-report.md` (tiếng Việt), thư mục `docs/codex-queue/222/`. Cả hai ở repo cha.

## Chỉ chạy khi

1. Có đủ `docs/codex-queue/187-report.md`, `194-report.md`, `195-report.md`, `197-report.md`.
   - Thiếu một báo cáo: vẫn kiểm phần có trong worktree, ghi rõ phiếu nào không có báo cáo.
   - Báo cáo nào ghi là đã dừng trước khi viết mã: kiểm phần đã có, ghi lại.
2. `git -C games/.wt-dh-codex branch --show-current` ra `dh-codex`, và `git -C games/.wt-dh-codex rev-parse HEAD` ra `6aa593a2dce6637cccbe24a58709b86f7127f607`. Khác thì dừng, ghi vào báo cáo: Claude đã commit hay đổi nhánh, nên phạm vi kiểm không còn đúng.
3. `df -g .` còn ít nhất 2 GB trống. Bản chép cần khoảng 0,2 GB, `dist` khoảng 35 MB.

Số lúc soạn phiếu (30/10, khoảng 12:55):
- `git status --short -uall` của worktree có **51** đường dẫn: 24 sửa, 27 mới;
- `git ls-files -co --exclude-standard` có **473** file.

Số khác lúc chạy thì không dừng: ghi lại, rồi quy file như việc 1.

## Thứ tự trong làn

Làn `s7`, chạy sau 220. 220 làm ở `.wt-ts-codex` và không đụng worktree này. Phiếu này phải xong trước 223, vì 223 ghi vào chính worktree này. Model `gpt-6.1-sol`, mức `xhigh`.

## Nơi làm

- **Chỉ đọc:** worktree `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD `6aa593a`.
  - Được đọc file. Được dùng git chỉ đọc: `diff`, `status`, `log`, `show`, `ls-files`.
  - Đặt `GIT_OPTIONAL_LOCKS=0` cho mọi lệnh git, để `git status` không ghi lại index.
  - Không ghi gì vào worktree, kể cả `tmp/`, `dist/`, `node_modules/`.
- **Mọi lệnh build, test, đo chạy trong bản chép** `games/dragon-hold/tmp/codex-222/tree`. Đây là `tmp/` của checkout chính, Git đã bỏ qua.
  - cwd của làn là repo cha (`.`); lệnh `pnpm` chạy trong `tree`.
  - `TMPDIR` là đường tuyệt đối của `games/dragon-hold/tmp/codex-222/tmpdir`, cho mọi lệnh.

### Dựng bản chép (đúng thứ tự này)

```sh
export GIT_OPTIONAL_LOCKS=0
R=$PWD                                   # repo cha
W=$R/games/.wt-dh-codex
C=$R/games/dragon-hold/tmp/codex-222
mkdir -p $C/tree $C/tmpdir $C/logs
touch $C/start.marker
git status --short > $C/logs/parent-status-before.txt
git -C $W status --short -uall > $C/logs/status-before.txt
git -C $W rev-parse HEAD > $C/logs/head-before.txt
git -C $W ls-files -co --exclude-standard -z > $C/files.z
(cd $W && xargs -0 shasum -a 256 < $C/files.z) > $C/logs/worktree-before.sha256
rsync -a --from0 --files-from=$C/files.z $W/ $C/tree/
rsync -a --exclude=.vite --exclude=.vite-temp $W/node_modules/ $C/tree/node_modules/
ln -s $R/games/dragon-hold/public/assets $C/tree/public/assets
mkdir -p $C/dragon-hold/tmp/map1-audit/feel-35-1280
cp $R/games/dragon-hold/tmp/map1-audit/feel-35-1280/samples.json $C/dragon-hold/tmp/map1-audit/feel-35-1280/
(cd $C/tree && xargs -0 shasum -a 256 < $C/files.z) > $C/logs/copy.sha256
diff $C/logs/worktree-before.sha256 $C/logs/copy.sha256   # phải rỗng
```

Vì sao làm như vậy:
- **`node_modules` chép thật** (khoảng 107 MB, mọi liên kết bên trong là tương đối), không dùng liên kết.
  - Khi nạp `vite.config.ts`, Vite ghi vào `node_modules/.vite-temp/`.
  - Vitest ghi `node_modules/.vite/vitest/<băm>/results.json`.
  - Nếu dùng liên kết, các file này rơi vào worktree. Worktree đã có hai thư mục đó từ các lượt trước; không đụng tới chúng.
- **`public/assets` là liên kết tuyệt đối** tới `games/dragon-hold/public/assets`.
  - Liên kết của worktree là tương đối (`../../dragon-hold/public/assets`), chép sang sẽ gãy.
  - Liên kết này không có trong `ls-files`, vì Git bỏ qua `public/assets/**`.
- **`samples.json`:** `tests/app/idle-estimate.test.ts:16` (của 195) đọc `resolve("../dragon-hold/tmp/map1-audit/feel-35-1280/samples.json")` theo cwd.
  - Trong worktree, đường này trỏ vào `tmp/` của checkout chính.
  - Trong bản chép, nó trỏ vào `games/dragon-hold/tmp/codex-222/dragon-hold/...`, nên phải chép file vào đúng chỗ đó.
  - Ghi sha256 của file gốc trước và sau. Lúc soạn phiếu là `d9e4220369c0f6131db82c2ed41073ff108b58e5f40a79b86abc79246ce1f0f7`.
  - Test đọc một file ngoài repo mà Git bỏ qua. Tự xếp mức cho việc này trong danh sách lỗi.
- Không dùng `rsync --delete`. Không chép theo chiều ngược lại.

Claude đã thử đúng quy trình này ngày 30/10 lúc 12:59, rồi xóa bản thử:
- `pnpm check` chạy được trong bản chép;
- `find games/.wt-dh-codex -newer start.marker` không in gì, tức là không có gì ghi vào worktree;
- bỏ bước chép `samples.json` thì có đúng 1 test đỏ (ENOENT ở `idle-estimate.test.ts`).

### `pnpm` và `tsx` trong sandbox

- `pnpm dh:balance` chạy CLI `tsx`. Trong sandbox, CLI này có thể báo `listen EPERM` lúc mở ống IPC; 195 đã gặp (`docs/codex-queue/195/balance.log`).
  - Đặt `TMPDIR` trong workspace trước.
  - Vẫn lỗi thì chạy `TSX_DISABLE_CACHE=1 node --import=tsx scripts/balance/run.ts <cùng tham số>`. 195 đã chạy được cách này.
  - Ghi rõ đã dùng cách nào.
- Nếu `pnpm` đòi cài gói, kiểm deps hay ra mạng: dừng lệnh đó. Chạy thẳng bốn bước của `check`: `node src/kit/verify-kit.mjs`, `node_modules/.bin/vitest run`, `node_modules/.bin/tsc --noEmit`, `node_modules/.bin/vite build`. Ghi lại.

## Chỉ được ghi

- `games/dragon-hold/tmp/codex-222/**`: bản chép, `tmpdir`, log, test dò. Xóa hết ở cuối (việc 6).
- `docs/codex-queue/222-report.md`, `docs/codex-queue/222/**`.

## Đọc trước

- **Bốn phiếu:** `187-dh-portal-link.md`, `194-dh-ui-art-icons.md`, `195-dh-deck-notice-and-idle-speed.md`, `197-dh-title-screen.md`.
- **Bốn báo cáo:** `187-report.md`, `194-report.md`, `195-report.md`, `197-report.md`.
- **Danh sách file:** `187/status-final.txt`, `194/files-194.txt`, `195/files-195.txt`, `197/files-197.txt`.
- **Diff riêng:** `194/task.diff`, `195/task.diff`, `195/app-195.diff`, `195/learning-195.diff`, `197/app-197.diff`.
- **Phần còn lại:** `197/browser-handoff.md`, `194/media-files.txt`, `194/integration.md`, `194/remaining-svg.md`.
- **Luật:**
  - `AGENTS.md` repo cha: chữ người chơi thấy là tiếng Anh; không hình vẽ bằng mã; không emoji;
  - `games/.wt-dh-codex/AGENTS.md`;
  - `docs/games/IN_GAME_SETTINGS.md` §1 và §3;
  - `docs/games/DEPLOY_INDEPENDENCE.md`;
  - `docs/games/dragon-lane/06-other-systems.md` §10: hàng "Tự tua" do 195 thêm.
- Diff riêng trong báo cáo chỉ để tham khảo. Dựng lại từ `git -C games/.wt-dh-codex diff` và nội dung file mới.

## Việc

1. **Quy file.** Gán mỗi đường dẫn trong `git -C games/.wt-dh-codex status --short -uall` và trong diff cho 187, 194, 195 hay 197. Dựa vào mục "Chỉ được ghi" của từng phiếu và danh sách file trong báo cáo của nó.
   - **File chung:** gán từng khối diff theo số dòng. Lúc soạn, các file chung dự kiến là `README.md`, `src/app/app.ts`, `src/app/learning.ts`, `src/ui/results.ts`, `tests/ui/results-screen.test.ts`, `scripts/ui-art/prepare.mjs`, `src/ui/ui-art.json`, `tests/app/deck-app.test.ts`. Tự kiểm lại, đừng tin danh sách này.
   - **Ghi `222/attribution.json`:**
     ```json
     { "head": "6aa593a2…", "paths": { "<đường dẫn>": { "status": "M", "tickets": ["187", "195"], "hunks": [{ "lines": "120-134", "ticket": "195" }] } }, "unattributed": [] }
     ```
     223 đọc file này. Đường dẫn không gán được thì ghi vào `unattributed` và vào báo cáo.
   - **Ngoài phạm vi là một lỗi:**
     - đường dẫn nằm ngoài "Chỉ được ghi" của phiếu sở hữu nó (ví dụ 194 cấm `src/app/**`);
     - đường dẫn nằm trong mục "Cấm" của một phiếu khác.
     Chạm `src/sim/**`, `src/kit/**`, `src/view/**` hay golden thì ít nhất là major.
2. **Đối chiếu từng phiếu.**
   - Mỗi phiếu một bảng: mọi mục Việc và mọi dòng Cấm, mỗi dòng ghi đạt, không đạt hay không kiểm được, kèm file:dòng.
   - Đọc mã để tìm lỗi. Ít nhất các điểm dưới đây.

   **Chung cả bốn phiếu:**
   - listener không được gỡ: `keydown`, `error` ở pha bắt, pointer;
   - trạng thái rò giữa các lần chơi lại (`restart`, Retry, quay lại màn tựa);
   - lời hứa đến muộn sau `dispose`;
   - hình vẽ bằng mã: SVG, canvas, gradient, hình CSS, emoji, ký tự như `✓`, `⌨`, `★`;
   - chữ tiếng Việt người chơi thấy, ngoài nghĩa của từ đang học và hai tên riêng Hỏa Long, Bạch Long.

   **187:**
   - `VITE_PORTAL_URL` được đọc lúc build;
   - plugin trong `vite.config.ts` thay đúng một khai báo `PARENT_ORIGIN` của `src/kit/learning/contract.ts`, không sửa file kit;
   - bản phát hành không chứa `typing-game.local`;
   - URL sai hay có thông tin đăng nhập bị từ chối;
   - không có URL thì không gửi `postMessage` ra ngoài và không có nút cổng.

   **194:**
   - bảng `src/ui/ui-art.json`: 53 mục (36 đã nhận, 17 tạm), tên và key không trùng;
   - `icon()` chọn cỡ: ô 20 → 64, ô 46 → 128, ô 120 → 256;
   - listener `error` ở pha bắt cảnh báo một lần mỗi URL và ẩn ảnh;
   - `prepare.mjs` không thay file cũ khi lỗi giữa chừng; `--check` không ghi gì và thoát 1 ở đúng các ca phiếu nêu;
   - md5 media so với `194/media-files.txt` (159 WebP và manifest). 197 nói manifest chỉ thêm `art: {}`: kiểm bằng cách so JSON;
   - không thêm `filter`, `mix-blend-mode`, `opacity` để đổi màu ảnh;
   - đã bỏ rêu CSS `.dh-panel::before/::after`, và không quy tắc nào còn cần hai giả phần tử đó.

   **195:**
   - `buildDeck` phân biệt `load-failed`, `empty`, `too-small` (dưới 70 từ);
   - bảng báo không tạo `run`, router, vòng lặp, thẻ tốc độ;
   - Retry boot đúng một lần, kể cả khi bấm nhiều lần hay khi kết quả đến muộn;
   - chữ tiếng Anh đúng từng chuỗi của phiếu;
   - `allowedQualities(true)` không có `low`. `?q=low` ở bản phát hành ra `medium`, kể cả tùy chọn truyền thẳng vào `startApp`. Bản dev giữ `low`. Giá trị lạ ra `undefined`;
   - `idleSpeedUp` chỉ đúng khi đủ ba điều: pha `wave`; không có chữ sống; không quái nào đang ở hay sẽ vào Vùng Chữ trong 90 tick (xét cả quái bay, quái đang đánh, quái bị chặn, quái đóng băng, quái sắp ra từ hàng đợi);
   - pha `warning` (báo đợt) và mọi pha khác ngoài `wave` luôn ×1;
   - luôn ×1 khi có bảng mở, đang đặt hay sửa, đang dừng, đang đếm 3-2-1;
   - chốt 0,3 s trước khi bật;
   - ×2 bấm tay thắng, không nhân dồn với ×1,75;
   - tự tua chỉ đổi số bước sim mỗi khung;
   - xét đòn báo trước của quái (`telegraph`) và Héo lan khi đang tua. `195-report.md` §4 nêu `src/audio/map-events.ts:245–247` và `src/view/fx.ts:1294` hẹn giờ theo thời gian thật trong khi sim tua. Xếp mức cho rủi ro này.

   **197:**
   - thứ tự: màn tựa → Start → thẻ tốc độ (khi không có `?wpm=`) → `begin()`. Có `?wpm=` thì Start vào thẳng `begin()`. `?title=0` bỏ qua màn tựa;
   - phím đi qua bộ định tuyến có sẵn, không thêm bộ nghe `keydown` trên `window`;
   - router được dời lên trước `buildDeck`; việc này không làm đổi phím ở thẻ tốc độ, menu dừng, Thẻ Ôn;
   - Enter trên Start chỉ bắt đầu khi đủ bốn nguồn; Enter trên "Back to portal" thì đi cổng;
   - Esc không rời màn tựa; mũi tên đi vòng qua các nút;
   - rê chuột thì đổi focus, bấm chuột thì bấm nút;
   - chữ cái không vào sim khi màn tựa đang mở;
   - bộ từ lỗi trên màn tựa: Start tắt, nút cổng vẫn dùng được;
   - ảnh có `accepted: null` thì không gửi yêu cầu ảnh;
   - có `handle.state().title`; có móc `onShow`, `onHide`, `setBackdrop`;
   - bảy kịch bản đã thêm `title=0` đều qua `node --check`.
3. **Chạy lại các kiểm ngoại tuyến trong bản chép.** Log để ở `$C/logs/`, cuối cùng chép vào `222/`.
   1. `pnpm check`: mã thoát; số file kit khớp; số file test; số test đạt và đỏ; `tsc` và `vite build` có đạt không.
   2. `pnpm exec vitest run tests/golden/golden.test.ts`. `md5 -q tests/golden/m0.json` phải ra `75f74947dac170d05fd659f99417940e`.
   3. `pnpm exec vitest run tests/english-ui.test.ts`.
   4. `pnpm prepare-ui-art --check --art-src $R/games/dragon-hold/art-src`. Chỉ chạy với `--check`: không có cờ này, lệnh sẽ ghi vào `public/assets` thật của checkout chính qua liên kết.
   5. `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local`, rồi `node src/kit/tools/deploy/check-pack.mjs dist --game dragon-hold --json --allow-local-host > $C/logs/pack-local.json`.
   6. `env -u VITE_PORTAL_URL pnpm deploy:pack`, rồi `node src/kit/tools/deploy/check-pack.mjs dist --game dragon-hold --json > $C/logs/pack-prod.json`, rồi `grep -rl typing-game.local dist | wc -l`.
      - Ghi `ok`, `problems`, `report.files`, `report.bytes`, `report.localHost`, `report.vocabularyNotShipped.count`, `report.external`.
      - Chạy bước 6 sau bước 5, để `dist` cuối cùng là bản phát hành.
   7. `pnpm dh:balance --seeds=20 --bots=b35 --jobs=4 --json=$C/logs/balance-b35.json > $C/logs/balance-b35.md`.
      - Chạy `uptime` ngay trước. Tải 1 phút trên 10 thì dùng `--jobs=2`.
      - Ghi G1 (thắng % ở balanced, 40 seed), thắng % ở relax và challenge, hai bộ seed, thời gian chạy.
   8. `node scripts/balance/idle-estimate.mjs $R/games/dragon-hold/tmp/map1-audit/feel-35-1280/samples.json > $C/logs/idle-estimate.json`.
      - Ghi before, after, tám dòng bảng nhạy.
      - Ghi sha256 của `samples.json` trước và sau.
   9. `node --check` cho bảy kịch bản 197 đã sửa (danh sách ở `197-report.md` §3).
4. **So số.** Mỗi phiếu một bảng gồm: mục Kiểm của phiếu, số báo cáo ghi, số đo lại, khớp hay lệch.
   - Số của phiếu trước được đo trên trạng thái cũ. Ví dụ 187 ghi 509 test; `pnpm check` của 194 đỏ vì 195 còn dở.
   - Lệch vì một phiếu chạy sau: ghi "lệch có lý do" kèm số phiếu gây ra. Không tính là lỗi.
   - Lệch không giải thích được: là một lỗi.
5. **Danh sách lỗi.**
   - Mỗi lỗi ghi:
     - mức: blocker, major, minor hay note;
     - phiếu;
     - file:dòng;
     - ca hỏng: đầu vào hay trạng thái nào cho kết quả sai nào;
     - một câu đề xuất sửa (không tự sửa).
   - Các lỗi sau là blocker: sai luật chơi; golden đổi; build hay `check` đỏ; lộ `typing-game.local` ở bản phát hành; chữ tiếng Việt người chơi thấy; hình vẽ bằng mã; kẹt phím (người chơi không thoát được màn).
   - **Test dò:** được viết để chứng minh một lỗi, chỉ trong `tree/tests/_probe-222/`, và chỉ sau khi xong mục 3. Chạy riêng bằng `pnpm exec vitest run tests/_probe-222`. Chép test và log vào `222/probes/`.
   - Thêm danh sách việc Claude cần xem trên trình duyệt, ở 1280 × 720 và 1920 × 1080. Lấy từ `197/browser-handoff.md` cộng các rủi ro bạn tìm thấy. Mỗi dòng: một thao tác và điều cần thấy.
   - Không sửa gì, cả trong worktree lẫn trong bản chép (trừ thư mục test dò).
6. **Dọn.**
   - Gỡ liên kết trước: `rm $C/tree/public/assets`. Rồi `rm -rf $C`.
   - Kiểm `games/dragon-hold/public/assets/dragon-hold/ui/icons/` vẫn đủ file như lúc đầu (lúc soạn phiếu: 160).

## Cấm

- Ghi bất cứ gì vào `games/.wt-dh-codex`:
  - sửa hay định dạng file;
  - chạy `pnpm`, `vite`, `vitest`, `tsc`, `node` với cwd ở đó;
  - xóa `dist/` hay `tmp/` của nó.
- Mọi lệnh git có ghi, ở repo cha, worktree hay checkout chính.
- Chạy `pnpm prepare-ui-art` mà không có `--check`. Ghi vào `games/dragon-hold` ngoài `tmp/codex-222/`.
- Đụng worktree khác (`.wt-dh-vfx`, `.wt-dh-keys`, `.wt-dh-models`, `.wt-dh-mappilot`, `.wt-td-*`, `.wt-ts-*`), game khác, Tu Tiên.
- Dev server, `vite preview`, trình duyệt, mạng. `kit:sync`, `dh:golden:update`.
- Sửa lỗi tìm thấy. Viết lại hay "dọn" báo cáo của phiếu khác.

## Kiểm (ghi số)

1. **Worktree không đổi:**
   - `status-before.txt` và `status-after.txt` giống từng byte (`cmp`);
   - `worktree-before.sha256` và `worktree-after.sha256` cùng số file, 0 khác. Bản sau dùng `ls-files` chạy lại; danh sách file cũng phải giống;
   - HEAD trước và sau giống nhau;
   - `find games/.wt-dh-codex -newer $C/start.marker` không in gì.
2. **Bản chép đúng:**
   - trước khi chạy bất cứ gì, `diff` hai bản sha256 rỗng. Ghi số file (lúc soạn: 473);
   - sau mục 3, chạy lại sha256 trên bản chép: vẫn khớp. `dist`, `tmp`, `node_modules` không nằm trong danh sách.
3. **`pnpm check` trong bản chép:** mã thoát; số file và số test đạt, đỏ; số file kit; build có đạt không. md5 golden đúng `75f74947dac170d05fd659f99417940e`.
4. **Đo lại:**
   - `deploy:pack`, bản phát hành và bản local: mã thoát, số `problems` theo loại, số file, số byte, `localHost`, số file trong `dist` chứa `typing-game.local`;
   - `dh:balance` với b35: thắng % mỗi chế độ, seed, thời gian;
   - `idle-estimate`: đầu ra.
5. **Theo phiếu:** mỗi phiếu 187, 194, 195, 197 có bảng Kiểm của phiếu, gồm số báo cáo ghi và số đo lại.
6. **Lỗi:** đếm theo mức; lỗi nào cũng có file:dòng. Chỉ được ghi "0 lỗi" khi kèm danh sách mọi file đã đọc (đường dẫn, số dòng).
7. **Cuối lượt:**
   - `$C` đã xóa; log nằm ở `222/`;
   - `git status --short` của repo cha so với `222/parent-status-before.txt` chỉ thêm `docs/codex-queue/222-report.md` và `docs/codex-queue/222/`;
   - thay đổi chạy cùng lúc của làn khác (`s8`, `s9`) ghi riêng, không đụng.

## Báo cáo gồm

- **Kết luận** một đoạn: sẵn sàng cho Claude duyệt hay chưa; số lỗi theo mức.
- **Mốc:** HEAD, nhánh, status đầu và cuối, sha256; cách đã chạy `pnpm` và `tsx` (thẳng, hay qua `node --import=tsx`).
- **Quy file:** bảng (bản đầy đủ ở `222/attribution.json`) và các đường dẫn không gán được.
- **Đối chiếu:** bốn bảng việc, cấm, kiểm, mỗi phiếu một bảng.
- **Số đo lại:** bảng so với số báo cáo.
- **Lỗi:** danh sách, xếp từ nặng tới nhẹ.
- **Trình duyệt:** danh sách việc cho Claude kiểm ở hai cỡ.
- **File đã đọc:** danh sách.
- **Log trong `222/`:**
  - `check.log`, `golden.log`, `english-ui.log`, `prepare-check.log`;
  - `pack-local.json`, `pack-prod.json`;
  - `balance-b35.json`, `balance-b35.md`, `idle-estimate.json`;
  - `status-before.txt`, `status-after.txt`;
  - `worktree-before.sha256`, `worktree-after.sha256`, `copy.sha256`;
  - `parent-status-before.txt`, `parent-status-after.txt`;
  - `probes/` nếu có.

**Xong khi:** sáu mục việc và bảy mục kiểm đều đạt, có số. Sau đó Claude đọc danh sách lỗi, sửa hay giao sửa, kiểm trên trình duyệt ở hai cỡ, rồi commit.
