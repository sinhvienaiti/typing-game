# Phiếu 216 · Hạ tầng repo cha (host dragon., td., survival.) · nginx: bỏ alias `/vocabulary/` và `/typing-texts/` dùng chung khỏi ba host game, bộ kiểm chặn chúng quay lại

**Nguồn:**
- `docs/games/DEPLOY_INDEPENDENCE.md` §13, bước 5: "Bỏ alias `/vocabulary/`, `/typing-texts/` của ba game … ở `play.conf`, `dev.conf`; sửa `validate-play-mode.mjs`".
- `docs/games/MAP1_PRODUCTION.md` §4.6, cổng G7: "bản build trên server tĩnh không alias". Mục DH-02 cũng ghi bỏ alias của host dragon.
- `docs/HANDOFF_CURRENT.md` §4 mục 2 (làn T, chưa mở): "bỏ alias nginx".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Vì sao:** ba game đã mang bản ghim từ vựng riêng trong `public/vocabulary/` (pin `18338405`; phiếu 090 Last Line, 091 Wordwoven, 094 Dragonhold). Nhưng nginx ở máy nhà vẫn đè `/vocabulary/` của ba host bằng `shared/vocabulary` ở HEAD repo cha. Chơi qua `typing-game.local` thì game đọc từ vựng của repo cha, không phải bản ghim. Lệch pin thì không ai thấy, và G7 không chứng minh được.

Không trùng 111, 111b (bộ kiểm gói), 168–170 (`deploy:pack`), 187, 207, 208 (nguồn cổng game). Các phiếu đó sửa repo game. Phiếu này chỉ sửa cấu hình nginx và bộ kiểm của repo cha.

**Báo cáo:** `docs/codex-queue/216-report.md` (tiếng Việt), thư mục `docs/codex-queue/216/`.

## Đọc trước

- `docs/games/DEPLOY_INDEPENDENCE.md` §8 (bản ghim) và §13.
- `docs/codex-queue/090-report.md`, `091-report.md`, `094-report.md`: pin, số file, manifest sha256.
- `scripts/validate-play-mode.mjs` (cả file), `scripts/validate-space-integration.mjs` dòng 120–145 (nó cũng đọc hai file conf).
- `scripts/setup-nginx.sh`: cách conf được render (`__ROOT_DIR__`, `__SSL_CERT__`) và cài.
- `scripts/sync-game-kit.test.mjs`: mẫu test `node:test` của repo cha.

## Nơi làm (phiếu mã)

- Repo cha `/Users/toandx/htdocs/typing-game`, nhánh `feat/space-typing-admin-uiux`. Chạy sau phiếu 215 (cùng làn). Không phụ thuộc mã của 214, 215: hai phiếu đó không sửa `infra/` hay `scripts/validate-play-mode*`.
- Phiếu 195 ghi việc bỏ alias này là của Claude ("Ngoài phiếu"). Phiếu này nhận việc đó; Claude không làm song song.
- Chỉ được ghi bốn file:
  - `infra/nginx/typing-game.local.play.conf`;
  - `infra/nginx/typing-game.local.dev.conf`;
  - `scripts/validate-play-mode.mjs`;
  - `scripts/validate-play-mode.test.mjs` (mới).
- Cộng thêm: báo cáo, thư mục `216/`, file tạm dưới `tmp/` của repo cha (đã nằm trong `.gitignore`; xóa khi xong).
- Cây repo cha đang có sửa chưa commit của làn khác (`docs/`, `shared/game-kit/`, `media/`, `scripts/media/`). Không đụng.
- Trước khi làm, chạy:
  - `git branch --show-current`;
  - `git status --short -uall -- infra/nginx scripts/validate-play-mode.mjs scripts/validate-play-mode.test.mjs`.
- Kết quả:
  - đúng nhánh và sạch: làm tiếp; lưu `git status --short -uall` của cả repo vào `216/status-before.txt` (repo đang bẩn vì việc khác, kể cả `scripts/media/**` và file 214, 215 nếu Claude chưa commit);
  - nhánh khác, hay có sửa nào trong bốn file đó: dừng, ghi vào báo cáo.
- Được dùng git chỉ đọc. Test trước, mã sau. Chú thích và thông báo lỗi tiếng Anh.
- Phiếu này không đổi chữ nào người chơi thấy.
- Số dòng dưới đây là lúc Claude soạn phiếu (30/10, đã đối chiếu lại). Lệch thì tìm theo `server_name`.

## Việc

1. **Mốc đầu.**
   - Ghi HEAD repo cha. Ghi nhánh và HEAD của `games/dragon-hold` (`main`), `games/typing-defense` (`a2-days`), `games/typing-survival` (`main`).
   - Chạy `node scripts/validate-play-mode.mjs` và `node scripts/validate-space-integration.mjs`. Lưu đầu ra và mã thoát vào `216/validate-before.txt`. Lúc Claude soạn phiếu: cả hai qua.
   - Liệt kê mọi khối `location` có `alias` hay `root` trỏ vào `__ROOT_DIR__/shared/` hay `games/space-typing/`, trong cả hai file conf: file, dòng, host, đường. Lưu `216/aliases-before.json`.
2. **Ba game tự phục vụ từ vựng** (kiểm tĩnh, chỉ đọc repo game). Với mỗi game:
   - `public/vocabulary/vocab-manifest.json` có pin `18338405eebd9cfdbd6d6bf666ea79361c00a564`. sha256 từng file khớp manifest.
   - `dist/vocabulary/` có đủ file, cùng sha256 với `public/vocabulary/`. `dist` thiếu hay cũ thì ghi lại; **không** build lại.
   - Quét `src/` (trừ `src/kit/`) và mọi `.js` trong `dist/`: có chuỗi `typing-texts` không. Lúc Claude soạn phiếu: không game nào có; cả ba gọi `/vocabulary/` cùng nguồn.
   - Chế độ dev: `vite.config.ts` không tắt `publicDir`; plugin `serveSharedFolders` (nếu có) không mount `/vocabulary/` hay `/typing-texts/`. Vậy Vite tự phục vụ `public/vocabulary/`.
   - Game nào còn gọi `typing-texts` mà không có bản chép trong `public/`: giữ alias đó cho riêng host đó, ghi rõ trong báo cáo. Vẫn bỏ các alias khác.
   - Lưu `216/vocab-self-serve.json` (game, pin, số file, khớp hay lệch, chuỗi tìm thấy).
3. **Test trước** ở `scripts/validate-play-mode.test.mjs` (`node:test`, `node:assert/strict`). Ghi số đỏ trước khi sửa mã, lưu log vào `216/`.
   - **Hàm thuần, trong bộ nhớ** (fixture dựng từ chính văn bản conf thật, không ghi cứng số dòng):
     1. Conf thật sau bước 5: không báo gì cho dragon, td, survival, ở cả play và dev.
     2. Thêm lại `location <đường> { alias __ROOT_DIR__/shared/…; }` vào khối của từng host (3 host × 3 đường `/vocabulary/`, `/typing-texts/`, `/shared/typing-texts/` × play, dev): báo đúng host và đường đó.
     3. Biến thể vẫn bị bắt: modifier `^~` hay `=`; đường không có `/` cuối (`/vocabulary`); thêm dấu cách hay tab; tên khác nhưng trỏ vào shared (`location /words/ { alias __ROOT_DIR__/shared/vocabulary/; }`); `root __ROOT_DIR__/shared/…`.
     4. Dòng chú thích `# location /vocabulary/ {`: không báo.
     5. Khối `tutien.`, `space.` và portal `typing-game.local` giữ alias của chúng: không báo.
     6. Alias `/assets/space-typing/models/` của survival: không báo (còn được phép tới khi gộp 205).
     7. Kiểm ngoặc: thiếu một `}`, hay thừa một `}` đứng trước `{`: báo lỗi.
   - **Chạy CLI** (tiến trình con bằng `process.execPath`, `cwd` là gốc repo cha):
     8. Không tham số, trên repo: mã thoát 0, in dòng PASS.
     9. `--play-conf <fixture>` có `/vocabulary/` thêm lại vào khối dragon: mã thoát 1; stderr nêu `dragon.typing-game.local` và `/vocabulary/`.
     10. `--dev-conf <fixture>` có `/shared/typing-texts/` thêm lại vào khối td: mã thoát 1, nêu đúng host và đường.
   - File fixture cho CLI ghi dưới `tmp/validate-play-mode-test/` của repo cha, xóa trong `after`. Không dùng `os.tmpdir()`.
   - Test không phụ thuộc vào việc ba game đã checkout hay đã build.
4. **Sửa bộ kiểm** `scripts/validate-play-mode.mjs`:
   - Tách phần chạy vào `main()`. `main()` chỉ chạy khi file được gọi trực tiếp, để test import được mà không đọc file.
   - Giữ **mọi** kiểm hiện có và chữ thông báo của chúng, trừ đúng một thay đổi ghi ở dưới (vòng lặp bắt buộc `/vocabulary/`, `/typing-texts/`).
   - Thêm tham số tùy chọn `--play-conf <đường>` và `--dev-conf <đường>`; mặc định là hai file trong `infra/nginx/`. Tham số lạ thì in cách dùng, thoát mã 2.
   - Hằng số mới: `SELF_SERVED_HOSTS` (dragon, td, survival) và `SHARED_DATA_ROUTES` (`/vocabulary/`, `/typing-texts/`, `/shared/typing-texts/`).
   - Hàm export `sharedDataAliases(config, host)`: trả danh sách `{ host, route, line }`. Luật, trong khối HTTPS của host đó (tìm bằng `serverBlockFor` có sẵn), bỏ qua dòng chú thích:
     - `location` có hay không modifier (`=`, `^~`, `~`, `~*`) mà đường bắt đầu bằng `/vocabulary`, `/typing-texts` hay `/shared/typing-texts`;
     - `alias` hay `root` trỏ vào `__ROOT_DIR__/shared/`.
   - Với ba host đó, trong cả play và dev: mỗi chỗ tìm thấy là một lỗi, ví dụ `play nginx dragon.typing-game.local must serve its own pinned vocabulary; remove /vocabulary/ (line 151)`.
   - Vòng lặp đang **bắt buộc** `/vocabulary/`, `/typing-texts/` cho mọi game mới: chỉ còn bắt buộc cho `tutien.` (giữ nguyên hành vi).
   - Survival vẫn bắt buộc `/assets/space-typing/models/`. Thêm chú thích: `// Remove with the nginx alias once ticket 205 (own models) is merged.`
   - Kiểm mới cho mỗi file conf: ngoặc `{` `}` cân, số mở chưa lúc nào âm (bỏ qua chú thích `#` và chuỗi trong nháy); mỗi host trong bốn host game có đúng một khối `server_name <host>;`.
   - Dòng PASS nói thêm rằng dragon, td, survival tự phục vụ từ vựng ghim, không alias dữ liệu dùng chung.
5. **Sửa hai file conf.** Chỉ trong ba khối HTTPS `dragon.`, `td.`, `survival.`:
   - `play.conf`: dragon bỏ `/vocabulary/`, `/typing-texts/` (khoảng dòng 151–160); td bỏ `/vocabulary/`, `/typing-texts/`, `/shared/typing-texts/` cùng dòng chú thích của nó (khoảng 174–189); survival như td (khoảng 203–218).
   - `dev.conf`: dragon khoảng 198–207; td khoảng 229–244; survival khoảng 266–281.
   - Giữ nguyên `root`, `index`, `gzip`, `/assets/<game>/`, `/assets/`, `location /` và mọi `proxy_*`.
   - Survival **giữ** `location /assets/space-typing/models/` ở cả hai file. Thay chú thích phía trên bằng: `# Temporary: Space Typing models until ticket 205 (own models) is merged; Claude removes this block then.`
   - Không đổi thụt lề hay dòng trống ở chỗ khác.
6. **Khối khác không đổi.** Tính sha256 từng khối `server` (theo `server_name`) trước và sau, ở cả hai file. Mọi khối trừ ba khối trên phải giống từng byte: khối chuyển HTTP, portal `typing-game.local`, `monkeytype.`, `shooter.`, `recall.`, `karaoke.`, `space.`, `tutien.`. Lưu `216/blocks-unchanged.json`.
7. **Bản changelog nháp** ở `216/changelog.md`: đổi gì, vì sao, số trước và sau. Claude chép vào `docs/changelog/<ngày>.md` của repo cha khi commit (luật một file mỗi ngày, `docs/changelog/README.md`).

## Cấm

- Mọi lệnh git có ghi.
- Chạy `scripts/setup-nginx.sh`, `play.sh`, `scripts/play.sh`, `sudo`, `nginx` (kể cả `nginx -t`), `brew services`.
- Ghi ra ngoài repo: `/etc/hosts`, `/opt/homebrew/etc/nginx`, `~/`, `os.tmpdir()`.
- Dev server, trình duyệt, mạng. Build lại game.
- Sửa khối `tutien.`, `space.`, portal `typing-game.local`, `monkeytype.`, `shooter.`, `recall.`, `karaoke.`, khối chuyển HTTP. Bỏ alias model của survival.
- Sửa `validate-space-integration.mjs`, `setup-nginx.sh`, `play.sh`, `scripts/play.sh`, `package.json`, `docs/games/**`, `docs/HANDOFF_CURRENT.md`, `docs/CODEX_QUEUE.md`.
- Sửa `shared/**` (kể cả `shared/game-kit/tools/vite-shared-plugin.ts`), chạy `kit:sync`.
- Đụng repo game (`games/dragon-hold`, `games/typing-defense`, `games/typing-survival`: chỉ đọc), mọi worktree `games/.wt-*`, Tu Tiên.
- Nới bộ kiểm hay bỏ kiểm cũ để làm xanh.

## Kiểm (ghi số)

1. `node scripts/validate-play-mode.mjs` trên repo: mã thoát 0. Lưu `216/validate-after.txt`.
2. `node --test scripts/validate-play-mode.test.mjs`: số test; số đỏ trước khi sửa mã, số xanh sau. Log trong `216/`.
3. `node scripts/validate-space-integration.mjs`: vẫn mã thoát 0. Nó đòi `/vocabulary/` và `/shared/typing-texts/` có trong mỗi file; portal và `space.` vẫn giữ nên vẫn qua. Không sửa file này.
4. Kiểm tĩnh hai file conf, lưu `216/conf-static.json`:
   - ngoặc cân, không lúc nào âm;
   - số khối `server` trước và sau bằng nhau (play hiện có 11);
   - số `location` mỗi host trước và sau. Chỉ ba host game giảm: dragon −2, td −3, survival −3, ở mỗi file.
   - Không chạy `nginx -t` (cần sudo).
5. Trong ba host game, ở cả hai file: **0** `location` tới `/vocabulary`, `/typing-texts`, `/shared/typing-texts`; **0** `alias` hay `root` vào `__ROOT_DIR__/shared/`. Survival còn đúng 1 khối `/assets/space-typing/models/`, có chú thích 205. `tutien.` giữ nguyên.
6. `216/blocks-unchanged.json`: mọi khối khác cùng sha256 trước và sau.
7. `216/vocab-self-serve.json`: ba game khớp pin, `dist/vocabulary` khớp `public/vocabulary` (hay ghi rõ chỗ lệch), 0 chuỗi `typing-texts`.
8. `git status --short -uall` của cả repo sau khi làm, lưu `216/status-after.txt`: phần chênh so với `216/status-before.txt` đúng bốn file của phiếu, cộng báo cáo và `216/` (`tmp/` đã xóa hay bị git bỏ qua). `git diff --check` trên bốn file: 0 lỗi.
9. Báo cáo liệt kê **đúng** các đường đã đổi, mỗi đường một dòng.
10. Báo cáo ghi lệnh chủ dự án chạy một lần sau khi Claude commit:
    - đọc `scripts/setup-nginx.sh` rồi ghi đúng lệnh. Claude đọc ra là `pnpm setup:play` (tức `bash scripts/setup-nginx.sh play`; script tự hỏi mật khẩu sudo cho `nginx -t` và reload); ai đang ở chế độ dev thì `pnpm setup:dev`;
    - `./play.sh` cũng tự gọi lệnh này (dòng 352);
    - `MAP1_PRODUCTION.md` DH-03 ghi `sudo bash scripts/setup-nginx.sh play`. Nếu chạy cả script dưới sudo là sai trên macOS (`brew --prefix` khi là root), ghi lại để Claude sửa tài liệu.

## Rủi ro (ghi vào báo cáo)

- Chế độ Play ở máy nhà giữ alias cũ tới khi chủ dự án chạy lại setup-nginx.
- Sau đó, `/vocabulary/` của ba host đi qua `location /` (`try_files … /index.html`). File từ vựng thiếu sẽ nhận `index.html` với mã 200, không phải 404. Chỉ ghi lại cho lượt G7 (§4.6 "không fallback SPA"); không sửa ở phiếu này.

**Xong khi:** hai file conf sạch alias dữ liệu dùng chung ở ba host game; bộ kiểm báo lỗi khi alias quay lại; test xanh; khối khác giữ nguyên từng byte; báo cáo có lệnh cho chủ dự án và danh sách đường đã đổi. Claude duyệt rồi commit. Khi 205 đã gộp, Claude bỏ alias model của survival và dòng bắt buộc tương ứng trong bộ kiểm.
