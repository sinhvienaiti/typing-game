# Phiếu 227 · Repo cha (cổng game, nginx, Audio Lab) · Kiểm lại độc lập 214–217 (tên tiếng Anh ở cổng game, tra cứu học, alias nginx, nhận âm Firefly ở Audio Lab) trước khi Claude duyệt

**Nguồn:**
- `.local/codex-lane-mac-s8.txt`: làn s8 chạy 214, 215, 216, 217 thẳng trong repo cha. `docs/HANDOFF_CURRENT.md` dòng 18: "30/10, 11:20: chủ dự án bảo Claude dừng mọi việc, chỉ giao việc cho Codex". Vì vậy các sửa chưa commit của bốn phiếu nằm cạnh việc dở của Claude (`shared/game-kit/feedback/typing-fx/`, `shared/game-kit/ui/quick-settings/css.ts`, `scripts/media/*`), và chưa ai duyệt.
- `docs/codex-queue/215-portal-learning-lookup.md`, tiêu đề: "portal đang từ chối, Dragonhold coi từ đã học là từ mới". Đây là đường `postMessage`: sai origin là lỗi bảo mật.
- `docs/codex-queue/216-nginx-game-aliases.md` bỏ alias `/vocabulary/`, `/typing-texts/` dùng chung khỏi ba host game. Đó là cổng G7 của cả ba game (`docs/games/MAP1_PRODUCTION.md` §0: "G7 chặn cả ba game theo cùng một cách").
- `tools/codex-run/README.md`, bảng "Chọn model": kiểm lại độc lập, phản biện dùng `gpt-6.1-sol` `xhigh`.

**Loại phiếu:** phản biện, **chỉ đọc**. Không sửa gì. Mọi kết luận phải có bằng chứng (lệnh, mã thoát, file:dòng). Không tin số trong báo cáo cũ: chạy lại rồi so. Không chắc thì ghi "chưa chắc" và cần gì để chắc.

**Không trùng:** 011, 019 (phản biện Wordwoven trong repo game). Chưa phiếu nào kiểm lại 214–217.

**Báo cáo:** `docs/codex-queue/227-report.md` (tiếng Việt), thư mục `docs/codex-queue/227/`.

## Chỉ chạy khi

Kiểm điều 5 trước tiên, trước khi tạo bất cứ thứ gì. Rồi ghi đầu ra của cả năm điều vào `227/preflight.txt`:

1. Mỗi phiếu 214, 215, 216, 217: có `docs/codex-queue/<n>-report.md`, và lượt chạy đã xong (`.local/codex-runs/<n>-<slug>/last.md` có). Phiếu nào thiếu báo cáo, hay báo cáo nói đã dừng giữa chừng: ghi "thiếu" hay "dừng", chỉ kiểm phần đã có. Cả bốn đều thiếu thì dừng.
2. `git branch --show-current` là `feat/space-typing-admin-uiux`. Khác thì ghi lại và làm tiếp (chỉ đọc).
3. Ghi `git rev-parse HEAD`. Cuối phiếu ghi lại lần nữa; HEAD tiến thì liệt kê `git diff --name-only <đầu> <cuối>` (thường là commit giấy tờ của điều phối).
4. Đường của bốn phiếu còn chưa commit: `git status --short -- portal shared/learning infra/nginx scripts/validate-play-mode.mjs scripts/game-dir.sh scripts/bootstrap.sh tools/audio-lab/firefly tools/audio-lab/build tools/audio-lab/common/launch.py tools/audio-lab/pytest.ini` có dòng. Phiếu nào đã được Claude commit (đường của nó không còn trong status): tìm commit bằng `git log --oneline -5 -- <đường>`, rồi dùng `git diff <commit>^ <commit> -- <đường>` thay cho diff cây làm việc ở Việc 2–3, ghi mã commit vào `preflight.txt`.
5. `tmp/codex-227/` và `docs/codex-queue/227/` chưa có. Có, và `227/preflight.txt` cho thấy đó là lượt trước của chính phiếu này bị cắt: xóa `tmp/codex-227/`, làm lại từ đầu (giữ `227/` cũ trong `227/prev-<giờ>/`). Có mà không rõ của ai: dừng.

Lúc soạn phiếu (30/10, khoảng 13:10) cả bốn báo cáo đều nói đã xong: 214 (11:23), 215 (13:06, lượt thứ ba; hai lượt trước bị cắt), 216 (11:31), 217 (11:47). Phản biện 30/10 khoảng 13:20 đã chạy lại ngoài repo: portal 77/77, learning 84/84, test 216 94/94, `validate:play-mode` và `validate:space-integration` mã 0, `core-snapshot` ra đúng `f091f364…`, test mới của 217 qua wrapper chép 20/20, `tsc` mã 0, `vite build --configLoader runner` vào thư mục ngoài repo mã 0 (JS chính 610.938 byte, tổng JS 4.979.637, CSS 127.854) và không ghi file nào dưới `portal/`.

## Nơi làm

- Repo cha, gốc `/Users/toandx/htdocs/typing-game` (cwd của làn: `.`), nhánh `feat/space-typing-admin-uiux`. Không worktree.
- **Chỉ được ghi:** `tmp/codex-227/` (git bỏ qua `/tmp/`), `docs/codex-queue/227/`, `docs/codex-queue/227-report.md`.
- Ngoại lệ duy nhất: `node --test scripts/validate-play-mode.test.mjs` của 216 tự tạo rồi tự xóa `tmp/validate-play-mode-test/`. Được phép chạy; sau khi chạy thư mục đó phải không còn (hay chỉ còn thư mục con của lượt khác).
- Lệnh `pnpm` chạy với `pnpm_config_verify_deps_before_run=false` (như 215), để không cài gói, không ra mạng.
- Mọi lệnh git (`status`, `diff`, `log`, `show`…; repo cha và submodule) chạy với `GIT_OPTIONAL_LOCKS=0`: không làm mới index, không giữ khóa, vì cây đang có việc dở của người khác.
- Luật chung của runner cấm chạy build hay test suite. Phiếu này **được** chạy đúng các lệnh ở bảng Việc 4 và lệnh build ở dưới, không lệnh build hay test nào khác (không test của game, không `pnpm check` ở đâu cả).
- Ngay sau điều 5 của "Chỉ chạy khi", trước mọi lệnh khác: `mkdir -p tmp/codex-227 && touch tmp/codex-227/marker`. Mốc này dùng cho Kiểm 7.
- Build portal chỉ vào `tmp/codex-227/`, bằng binary của portal:
  ```bash
  (cd portal && ./node_modules/.bin/tsc --noEmit)
  (cd portal && ./node_modules/.bin/vite build --configLoader runner --outDir ../tmp/codex-227/portal-dist --emptyOutDir)
  ```
  `--configLoader runner` nạp `vite.config.ts` mà không ghi file tạm vào `portal/node_modules/.vite-temp/` (điều phối đã chạy thử 30/10, vite 7.3.6). Không chạy `pnpm --dir portal build`: nó ghi `portal/dist`.
- Test Audio Lab của 217 chạy qua một bản chép wrapper, cache và thư mục tạm trong `tmp/codex-227/audiolab/`. Không chạy `run.sh`: `launch.py` đặt `sys.pycache_prefix` vào `~/AudioLab/cache` trước khi wrapper chạy.
  ```bash
  mkdir -p tmp/codex-227
  sed -e 's/parents\[3\]/parents[2]/' -e 's#tmp/firefly-ingest#tmp/codex-227/audiolab#' \
    docs/codex-queue/217/run-tests.py > tmp/codex-227/run-tests-217.py
  /Users/toandx/AudioLab/.venv/bin/python -I tmp/codex-227/run-tests-217.py firefly build/tests/test_build_firefly_licence.py
  /Users/toandx/AudioLab/.venv/bin/python -I tmp/codex-227/run-tests-217.py
  ```
  Đọc bản chép trước khi chạy: `repo` phải là gốc repo cha, `root` phải là `tmp/codex-227/audiolab`. venv ở `~/AudioLab/.venv` chỉ được đọc.

## Đọc trước

- Bốn phiếu và bốn báo cáo: `docs/codex-queue/21{4,5,6,7}-*.md`, `21{4,5,6,7}-report.md`, các thư mục `214/` … `217/` (mục "Nơi làm", "Chỉ được sửa", "Cấm", "Kiểm" của từng phiếu là thước đo).
- 214: `portal/public/games.json`, `portal/src/game-card.ts`, `portal/src/main.ts`, `portal/src/styles.css`, `portal/tests/game-card.test.mjs`, `portal/tests/fixtures/legacy-games.json`, `scripts/game-dir.sh`, `scripts/bootstrap.sh`.
- 215: `shared/learning/{core,query,message-contract,profile-backup}.mjs` cùng `.d.mts`, `shared/learning/lookup.test.mjs`, `shared/learning/README.md`, `portal/src/learning/bridge.ts`, `portal/tests/learning-lookup.test.mjs`, `portal/tests/learning-bridge.test.mjs`. Chỉ đọc để đối chiếu: `shared/game-kit/learning/contract.ts` (`LEARNING_LOOKUP_MESSAGE` dòng 7, `LOOKUP_MAX_IDS = 200` dòng 23), `shared/game-kit/learning/bridge.ts:166-174`, `games/dragon-hold/src/app/learning.ts:20-30` (`RECALLS`, `isRightRecall`) và `:170-194` (`parseLookup`).
- 216: `infra/nginx/typing-game.local.play.conf`, `.dev.conf`, `scripts/validate-play-mode.mjs`, `scripts/validate-play-mode.test.mjs`; chỉ đọc `scripts/validate-space-integration.mjs`, `scripts/setup-nginx.sh`, `docs/games/DEPLOY_INDEPENDENCE.md` §8, §13.
- 217: `tools/audio-lab/firefly/**`, `tools/audio-lab/build/policy.py`, `build/licence_check.py`, `build/tests/test_build_firefly_licence.py`, `common/launch.py`, `pytest.ini`. Chuỗi giấy phép của dự án: "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)" (`docs/games/audio/firefly/README.md:7`). Không mở `tools/audio-lab/keys/`: đó là việc dở của Claude.

## Việc

1. **Mốc.** Viết `tmp/codex-227/snap.mjs` (Node, không gói). Script ghi JSON:
   - HEAD, nhánh;
   - mọi mục của `git status --porcelain=v1 -z -uall` (mã trạng thái, đường dẫn; đường có dấu cách như `typing-mp3/…` phải đúng);
   - với mỗi đường: file thì cỡ và SHA-256; thư mục (submodule như `games/monkeytype`) thì `git -C <đường> rev-parse HEAD` và SHA-256 của `git -C <đường> status --porcelain`; không còn thì `deleted`;
   - danh sách file của `portal/dist` cùng SHA-256;
   - danh sách file trong `portal/node_modules/.vite-temp/` (lúc soạn phiếu: thư mục rỗng).

   Chạy trước mọi việc khác, lưu `227/snap-before.json`.
2. **Gán đường cho phiếu.** Lấy mọi đường đã đổi (status và `git diff --stat`). Gán mỗi đường cho 214, 215, 216 hay 217 theo mục "Nơi làm" và danh sách được ghi của phiếu đó, và theo danh sách file trong báo cáo.
   - Bảng `227/paths.md`: đường, phiếu, phiếu có quyền ghi không, báo cáo có nhận không.
   - Đường nằm trong vùng ghi của một phiếu mà không báo cáo nào nhận: là một phát hiện.
   - Đường ngoài cả bốn phiếu (việc dở của Claude và file của chủ dự án: `shared/game-kit/**`, `scripts/media/**`, `media/media.config.json`, `tools/audio-lab/keys/**`, `games/monkeytype`, `docs/MEDIA_STORAGE.md`, `docs/games/**`, `tools/asset-library/**`, `typing-mp3/**`, file `docs/codex-queue/**` của phiếu khác…): chỉ liệt kê, không đọc kỹ, không kết luận.
3. **Đọc từng phiếu**, đối chiếu từng mục "Việc" và "Cấm" với diff (`git diff -- <đường>`, file mới thì đọc cả file). Tìm lỗi. Trọng tâm:
   - **214:**
     - ba mục `games.json`: `name` đúng Dragonhold, Wordwoven, Last Line; mô tả một câu tiếng Anh 50–110 ký tự, không chữ Việt có dấu, không `\p{Extended_Pictographic}`; không còn trường `icon`; `art.icon`, `art.cover` đúng `/assets/<id>/portal/icon-192.png`, `cover-wide.webp`;
     - sáu mục cũ, **kể cả Tu Tiên**, `deepEqual` với `git show HEAD:portal/public/games.json`; `id`, `path`, `appUrl`, `group` và thứ tự giữ nguyên (tự viết script trong `tmp/codex-227/`);
     - `resolveGameArt`: thử thêm ca biên ngoài test, ví dụ `%2e%2e`, `%2F`, chữ hoa, khoảng trắng, `appUrl` có đường dẫn. Ảnh không bao giờ ra origin khác `appUrl`;
     - `main.ts`: không còn đọc `game.icon`; không đưa trường của `games.json` vào `innerHTML`; `<img>` có `alt`, `width`, `height`, `loading`, `decoding`, ẩn khi lỗi;
     - `styles.css`: không hình vẽ bằng CSS (gradient giả ảnh, khối màu thay biểu tượng);
     - hai script: chỉ đổi nhãn; 0 dòng còn "Rồng Giữ Ải", "Lời Gọi", "Tuyến Cuối"; sáu dòng nhãn Tu Tiên giống HEAD (danh sách ở `214/verification.json`).
   - **215:**
     - hợp đồng tin: tên `typing-game:learning:v1:lookup` và giới hạn 200 khớp kit; mảng 1–200 phần tử kiểm **trước** khi bỏ trùng; id ≤ 200 ký tự sau cắt; chuẩn hóa từ vựng bằng `normalizeVocabularyKey`; trường lạ bị bỏ qua; không thêm `gameId`;
     - danh sách nguồn được trả lời: chỉ khi `event.source` đúng `contentWindow` của iframe đang mở **và** `event.origin` đúng origin của `appUrl` game đang mở. Sai một trong hai, hay chưa mở game: không trả lời, không gọi `store.load`;
     - trả lời chỉ tới khung đã hỏi: `postMessage(…, targetOrigin)` với `targetOrigin` là origin đó, không bao giờ `"*"`, cùng `requestId`;
     - không lộ dữ liệu học: chỉ trả id được hỏi, đúng loại thực thể; khóa nguyên mẫu (`__proto__`, `constructor`, kể cả own key) không ra bản ghi; `recentSamples` không có `userAnswer`, `expectedAnswer`; thông báo lỗi không chứa dữ liệu hồ sơ;
     - chỉ đọc: không ghi kho, không gọi `onApplied`; `flush()` trước `load()`; lỗi đọc kho ra `query-failed`;
     - test đi qua `handleMessage` với sự kiện giả có `source`, `origin`, và khung giả ghi lại từng `postMessage(data, targetOrigin)`. Test nào chỉ gọi thẳng `lookupLearningRecords` thì không chứng minh được đường tin: ghi lại. Phải có ca origin đúng mà `source` là cửa sổ khác;
     - `version: 1` của hồ sơ, công thức độ thuộc, ngày ôn không đổi; sao lưu cũ vẫn nhập được.
   - **216:**
     - cú pháp hai file conf theo bộ kiểm của chính phiếu (`configStructureErrors`, ngoặc cân, mỗi host game đúng một khối `server_name`);
     - tự tính SHA-256 từng khối `server` (theo `server_name`) của HEAD (`git show HEAD:infra/nginx/…`) và của file hiện tại: mọi khối trừ ba khối HTTPS `dragon.`, `td.`, `survival.` giống từng byte. Số `location` của ba khối đó (play: dragon 5 → 3, td 6 → 3, survival 7 → 4; dev: 3 → 1, 4 → 1, 5 → 2; theo `216-report.md`);
     - host Space và portal (`space.`, `typing-game.local`) giữ những gì cần (`validate-space-integration.mjs` đòi `/vocabulary/`, `/shared/typing-texts/`); `tutien.` giữ alias của nó; survival còn đúng một `location /assets/space-typing/models/` kèm chú thích phiếu 205;
     - bộ kiểm báo lỗi khi alias quay lại: chép conf vào `tmp/codex-227/nginx/`, thêm lại `location /vocabulary/ { alias __ROOT_DIR__/shared/vocabulary/; }` vào khối dragon (play) và `/shared/typing-texts/` vào khối td (dev); `node scripts/validate-play-mode.mjs --play-conf …` và `--dev-conf …` phải thoát 1 và nêu đúng host, đường;
     - ba game tự phục vụ từ vựng (chỉ đọc `games/*/public/vocabulary`, `games/*/dist/vocabulary`): pin `18338405eebd9cfdbd6d6bf666ea79361c00a564` trong `vocab-manifest.json`, `dist` khớp `public` (so lại số của `216/vocab-self-serve.json`).
   - **217:**
     - đường: inbox chỉ đọc; mọi đầu ra dưới `--out`; không có đường mặc định trỏ `~/AudioLab` (tìm `AudioLab`, `expanduser`, `Path.home`, `env.WORK`, `env.STAGING` trong `tools/audio-lab/firefly/*.py`); `export.path` và liên kết tượng trưng không thoát ra ngoài;
     - giấy phép: lớp `LicenseRef-Adobe-Firefly-owner` (`policy.py`), `cond: "adobe-model"`, danh sách model khớp từ đầu chuỗi; nhánh `licence_check.py` chỉ cho điều kiện đó; dòng sổ có `raw_redistribution_allowed: false`. So `generator`, `model`, `author` và file `licences/adobe-firefly-owner-2026-10-29.txt` với chuỗi của dự án "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)". Đầu ra `release` (`SOURCES.json`, dòng sổ) có mang chuỗi này, hay một dạng tương đương mà Claude cần xác nhận? Lệch thì ghi một phát hiện để Claude chọn;
     - không mạng: tìm `urllib`, `requests`, `http`, `socket`, `subprocess` trong `firefly/`; ghi mọi chương trình ngoài được gọi;
     - chạy lại ra cùng byte: đọc test của 217 có thật sự so SHA-256 hai lượt không. Không có thì viết một script nhỏ trong `tmp/codex-227/` gọi `firefly.main(argv)` hai lần trên fixture sinh bằng `build/tests/helpers.impact()`, đầu ra trong `tmp/codex-227/`;
     - `launch.py` đúng một dòng thêm; `pytest.ini` chỉ thêm `firefly`; không file âm hay ảnh nào trong `tools/audio-lab/firefly/` hay `docs/codex-queue/217/`.
4. **Chạy lại các lệnh kiểm chỉ đọc**, so với số trong báo cáo. Log vào `227/runs/`:

   | Lệnh | Số báo cáo nói (30/10) |
   |---|---|
   | `pnpm portal:test` | 77/77 trên 3 file (215); trước 215 là 51/51 trên 2 file (214) |
   | `pnpm learning:test`, `pnpm learning:check` | 84/84 trên 13 file; mã 0 (215) |
   | `node docs/codex-queue/215/core-snapshot.mjs > tmp/codex-227/core-now.json` (chỉ in ra stdout) | SHA-256 `f091f364b03c624afd2ab52e7b52113c88fc1e24945a0b73d3a3ac7d46aa182c` (`215/core-hashes.json`) |
   | `node --test scripts/validate-play-mode.test.mjs` | 94/94 (216) |
   | `pnpm validate:play-mode` | mã 0, dòng PASS kết thúc bằng "dragon, td, survival serve their own pinned vocabulary without shared data aliases." |
   | `pnpm validate:space-integration` | mã 0 |
   | Test mới của 217 (lệnh thứ nhất ở "Nơi làm") | 20 qua |
   | Cả bộ Audio Lab (lệnh thứ hai) | 539 qua, 6 lỗi, 10 lỗi thiết lập, 6 bỏ qua; danh sách lỗi giống `217/test-summary.json` mục `after` |
   | `bash -n scripts/game-dir.sh`, `bash -n scripts/bootstrap.sh` (và mọi `.sh` khác bốn phiếu sửa) | mã 0 |
   | `tsc --noEmit` và `vite build` vào `tmp/codex-227/portal-dist` | mã 0 |
   | `git diff --check` trên các file đã theo dõi của bốn phiếu | mã 0 |
   | File mới của bốn phiếu: `git diff --no-index --check /dev/null <file>` | không in dòng nào. Mã 1 là bình thường (file khác `/dev/null`); mã 3 là có lỗi khoảng trắng (điều phối thử 30/10) |

   - Không chạy `docs/codex-queue/215/lookup-timing.mjs`, `217/demo.py`, `214/verify.py`, `214/run-check.py`, `217/run-tests.py` nguyên bản: chúng ghi vào thư mục của phiếu cũ hay `tmp/firefly-ingest/`.
   - Byte gói portal: file `assets/index-*.js` chính và `assets/index-*.css` (214 ghi 609.295 byte `index-CUNiqGGe.js` và 127.854 byte `index-CnQYlBjB.css`, trước 215); tổng byte mọi file `.js` trong `portal-dist`, kể cả worker (215 ghi 4.979.637 sau, CSS 127.854; `215/bundle-bytes.json`). Lệch thì nói lệch do phiếu nào, hay do cách đếm.
5. **Phát hiện.** Mỗi phát hiện một mục, đánh số `227-F1`, `227-F2`…:
   - phiếu; mức; `file:dòng`; ca hỏng cụ thể (đầu vào hay trạng thái → kết quả sai); bằng chứng (lệnh, log, đoạn mã); đề xuất sửa trong một câu. Không sửa.
   - Mức:
     - **chặn**: lỗi bảo mật (dữ liệu học tới origin hay khung khác), build hay test đỏ, ghi ra ngoài vùng được phép, media vào Git, mất dữ liệu;
     - **nặng**: phiếu đòi mà không làm hay làm sai, người chơi hay chủ dự án thấy được;
     - **vừa**: lệch phiếu chưa gây hại ngay; thiếu test cho một ca phiếu đòi; số trong báo cáo không khớp lần chạy lại;
     - **nhẹ**: chú thích, tài liệu, tên.
   - Cuối báo cáo: danh sách việc cần Claude kiểm trên trình duyệt ở `https://typing-game.local`, hay cần chủ dự án chạy với sudo. Ví dụ: bố cục thẻ cổng game ở 1280 và 1920 (214); vào Dragonhold, lookup nhận `query-result`, không `error`, không chờ 2 s (215); `pnpm setup:play` rồi tải `/vocabulary/` của ba host (216); nghe bản 20 s (217).
6. **Mốc cuối.** Chạy lại `snap.mjs`, lưu `227/snap-after.json`; viết `227/snap-delta.json`. Phần chênh chia ba nhóm:
   - của phiếu này (`227-report.md`, `227/`);
   - của làn khác trong lúc chạy: `docs/codex-queue/<n>*` của phiếu khác (213 đang chạy lúc soạn phiếu; 199, 200, 202, 22x), `docs/games/audio/firefly/dragon-hold.*` (213), `docs/games/audio/firefly/typing-defense.*` (221), và commit giấy tờ của điều phối (HEAD tiến). Liệt kê riêng, không tính cho phiếu này;
   - còn lại: phải rỗng. Có thì tìm xem có phải do lệnh của phiếu này không; nếu phải thì là phát hiện mức chặn của chính phiếu, ghi rõ.
7. **Dọn.** Chép log cần cho báo cáo vào `227/` (chỉ TXT, JSON, MD; không ảnh, không âm, không `portal-dist`). In danh sách `tmp/codex-227/` vào báo cáo rồi xóa thư mục đó.

## Cấm

- Ghi ra ngoài ba đường được phép (ngoại lệ duy nhất là thư mục tạm tự xóa của test 216). Gồm cả `portal/dist`, `tmp/firefly-ingest/`, `docs/codex-queue/214/` … `217/`, mọi `node_modules`.
- Sửa bất kỳ file nào, kể cả lỗi rõ ràng. Phiếu này chỉ báo.
- Mọi lệnh git có ghi. Được: `status`, `diff`, `show`, `log`, `rev-parse`, `branch --show-current`, `ls-files`.
- `pnpm install`, `pnpm --dir portal build`, `kit:sync`.
- `nginx` (kể cả `nginx -t`), `sudo`, `scripts/setup-nginx.sh`, `play.sh`, `brew services`.
- Ghi vào `~/AudioLab` (venv chỉ đọc), chạy `tools/audio-lab/run.sh`.
- Dev server, trình duyệt, mạng.
- Ghi vào `games/**` (đọc `games/dragon-hold/src/app/learning.ts` và `games/*/public|dist/vocabulary` thì được). Đụng Tu Tiên.
- Mở hay chạy gì trong việc dở của Claude: `tools/audio-lab/keys/`, `games/.wt-dh-keys`, `.wt-td-keys`, `.wt-ts-typefx`, `.wt-dh-vfx`, `games/monkeytype` (riêng `git status` chỉ đọc của `snap.mjs` thì được).

## Kiểm (ghi số)

1. `snap-before.json` và `snap-after.json`: mọi đường có sẵn lúc đầu giữ nguyên trạng thái và SHA-256, trừ đường của 227. Thay đổi của làn khác liệt kê riêng, không tính cho phiếu này.
2. `portal/dist`: danh sách file và SHA-256 trước, sau giống nhau. `portal/node_modules/.vite-temp/` không có file nào sau build.
3. Bảng chạy lại: lệnh, mã thoát, số qua, lỗi, bỏ qua; so với số báo cáo nói (bảng ở Việc 4). Lệch thì ghi cả hai số.
4. Build portal vào `tmp/`: mã thoát; byte JS và CSS chính so với 214; tổng JS so với 215.
5. Số phát hiện theo mức (chặn, nặng, vừa, nhẹ), mỗi phát hiện có `file:dòng`. Phiếu thiếu báo cáo hay dừng giữa chừng: liệt kê.
6. `tmp/validate-play-mode-test/` không còn sau test 216. `tmp/codex-227/` đã xóa sau khi lưu log vào `227/`.
7. File bị Git bỏ qua (pycache, cache pytest, cache vite) không lộ ra ở `git status`. Ngay trước khi xóa `tmp/codex-227/`, chạy `find portal shared tools/audio-lab scripts infra -path '*/node_modules/.pnpm' -prune -o -newer tmp/codex-227/marker -print` và lưu vào `227/newer.txt`: phải rỗng. Có dòng thì xem có phải do lệnh của phiếu này không; nếu phải thì là phát hiện mức chặn của chính phiếu.

## Báo cáo phải có

- Đầu báo cáo: mỗi phiếu một dòng kết luận (đạt; đạt, có lỗi nhỏ; chưa đạt) và số phát hiện theo mức.
- Bảng gán đường (Việc 2) và danh sách đường ngoài phạm vi.
- Bảng chạy lại (Việc 4), byte gói portal.
- Mọi phát hiện (Việc 5), xếp từ nặng tới nhẹ.
- Việc cần Claude kiểm trên trình duyệt, việc cần chủ dự án chạy sudo.
- HEAD đầu và cuối; bằng chứng mốc (Kiểm 1, 2, 6, 7).

**Xong khi:** bốn phiếu (hay mọi phiếu có báo cáo) được đối chiếu từng mục, các lệnh kiểm được chạy lại có số, mọi phát hiện có `file:dòng` và ca hỏng, bảy mục kiểm có số, không file nào ngoài ba đường được phép bị đổi. Claude dùng báo cáo này khi duyệt và commit 214–217.
