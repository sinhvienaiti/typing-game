# Phiếu 227 · Kiểm lại độc lập 214–217 trước khi Claude duyệt

Ngày 30/10/2026 · Repo cha · Nhánh `feat/space-typing-admin-uiux` · Chỉ đọc mã nguồn.

| Phiếu | Kết luận | Chặn | Nặng | Vừa | Nhẹ |
|---|---|---:|---:|---:|---:|
| 214 · Thẻ cổng game | Đạt, có lỗi nhỏ; ca đường ảnh mã hóa cần Claude xác nhận | 0 | 0 | 1 | 0 |
| 215 · Tra cứu học | **Chưa đạt**: mẫu nhập từ sao lưu có thể mang câu trả lời; hai ca lỗi còn lại | 0 | 1 | 2 | 0 |
| 216 · Alias nginx | Đạt, có lỗi nhỏ ở log; mã và cấu hình qua kiểm lại | 0 | 0 | 0 | 1 |
| 217 · Nhận âm Firefly | **Chưa đạt cổng cả bộ Audio Lab**; 20 test mới qua, không thêm lỗi so với báo cáo cũ; cần chốt nhãn nguồn | 1 | 0 | 1 | 1 |
| **Tổng** | **8 phát hiện**; chặn ở 217 là lỗi cũ/môi trường, không phải hồi quy được chứng minh của 217 | **1** | **1** | **4** | **2** |

Không sửa lỗi, không commit/push. Không phiếu nào thiếu báo cáo hoặc còn dừng ở lượt hiện hành. Hai lượt 215 cũ đã dừng; lượt thứ ba đã hoàn tất. Chưa nghiệm thu bằng trình duyệt, nginx thật hoặc nghe WAV thật.

## Điều kiện chạy, phạm vi và cách đối chiếu

[preflight.txt](227/preflight.txt) ghi cả năm điều. Điều 5 được kiểm đầu tiên: cả hai thư mục đều chưa có, mã 0; ngay sau đó tạo `tmp/codex-227/marker`, viết/chạy script chụp mốc rồi mới đọc phiếu và chạy các kiểm khác. Bốn `last.md` hiện hành đều có. Mỗi phiếu còn đường nguồn chưa commit, nên dùng diff **HEAD → cây làm việc**; không cần thay bằng diff một commit cũ. `scripts/validate-play-mode.test.mjs` cũng là file mới chưa theo dõi; lệnh status hẹp trong đề bài không nêu file này.

Mọi lệnh Git chạy với `GIT_OPTIONAL_LOCKS=0`; mọi lệnh pnpm có `pnpm_config_verify_deps_before_run=false`. Không cài gói, không mạng, không browser/dev server, không chạy nginx/sudo, không mở `tools/audio-lab/keys/**` hoặc các worktree bị cấm. Chỉ đọc mục Tu Tiên trong registry/hai script và khối nginx để so với HEAD; không đụng repo hoặc tài liệu Tu Tiên. Dùng skill `game-ci-resumable` để giữ mốc và việc đồng thời; phiếu 227 quyết định giới hạn lệnh.

### Gán đường

Bảng đầy đủ từng đường, quyền ghi và báo cáo nhận nằm ở [paths.md](227/paths.md), dữ liệu máy ở [paths.json](227/paths.json), stat ở [diff-stat.txt](227/diff-stat.txt), diff nguồn ở [product-diff.txt](227/product-diff.txt).

| Nhóm tại mốc đầu | Số đường |
|---|---:|
| Toàn bộ `status --porcelain=v1 -z -uall` | 1.312 |
| Thuộc vùng được giao của 214–217 và có báo cáo nhận | 159 |
| Trong vùng được giao nhưng không báo cáo nào nhận | **0** |
| Ngoài bốn phiếu, chỉ liệt kê | 1.153 |
| File sản phẩm nguồn/test của bốn phiếu | 36: 21 đã theo dõi, 15 mới |

Danh sách ngoài phạm vi đầy đủ ở phần riêng trong `paths.md`: việc của Claude/chủ dự án trong `shared/game-kit/**`, `scripts/media/**`, `media/media.config.json`, `tools/audio-lab/keys/**`, `games/monkeytype`, `tools/asset-library/**`, `typing-mp3/**`, `docs/MEDIA_STORAGE.md`, `docs/games/**`, các phiếu khác và các phiếu gốc. Không dùng danh sách này để kết luận chất lượng của làn khác. Những đoạn tài liệu nguồn được đề bài chỉ định được đọc đúng phần cần đối chiếu.

## Chạy lại và đối chiếu số

Mỗi log trong [runs/](227/runs/) có argv/cwd, môi trường và mã thoát; JSON cùng tên có thời gian. Số dưới đây lấy từ lần chạy này, không chép số cũ làm kết quả.

| Lệnh | Báo cáo cũ | Lần 227 | Mã | Bằng chứng |
|---|---|---|---:|---|
| `pnpm portal:test` | 77/77, 3 file sau 215; 51/51 sau 214 | **77/77**, 3 file, 0 lỗi/bỏ qua | 0 | [portal-test.txt](227/runs/portal-test.txt) |
| `pnpm learning:test` | 84/84, 13 file | **84/84**, 13 file, 0 lỗi/bỏ qua | 0 | [learning-test.txt](227/runs/learning-test.txt) |
| `pnpm learning:check` | 0 | Qua | 0 | [learning-check.txt](227/runs/learning-check.txt) |
| `node docs/codex-queue/215/core-snapshot.mjs > tmp/codex-227/core-now.json` | `f091f364…` | Khớp trọn SHA-256 và từng byte của cả before/after cũ | 0 | [core-snapshot.json](227/runs/core-snapshot.json), [core-now.json](227/core-now.json) |
| `node --test scripts/validate-play-mode.test.mjs` | 94/94 | **94/94**, 0 lỗi/bỏ qua | 0 | [test-216.txt](227/runs/test-216.txt) |
| `pnpm validate:play-mode` | 0, PASS mới | Qua; đúng câu kết yêu cầu | 0 | [play-mode.txt](227/runs/play-mode.txt) |
| `pnpm validate:space-integration` | 0 | Qua | 0 | [space-integration.txt](227/runs/space-integration.txt) |
| Python `-I tmp/codex-227/run-tests-217.py firefly build/tests/test_build_firefly_licence.py` | 20 qua | **20 qua**, 0 lỗi/bỏ qua | 0 | [audio-new.txt](227/runs/audio-new.txt) |
| Python `-I tmp/codex-227/run-tests-217.py` | 539 qua, 6 lỗi, 10 lỗi thiết lập, 6 bỏ qua | **Đúng cả bốn số; đúng cả 16 tên lỗi** | **1** | [audio-all.txt](227/runs/audio-all.txt), [audio-summary.json](227/audio-summary.json) |
| `bash -n scripts/game-dir.sh` | 0 | Qua | 0 | [game-dir-syntax.txt](227/runs/game-dir-syntax.txt) |
| `bash -n scripts/bootstrap.sh` | 0 | Qua; đây là hai `.sh` duy nhất bốn phiếu đổi | 0 | [bootstrap-syntax.txt](227/runs/bootstrap-syntax.txt) |
| `cd portal; ./node_modules/.bin/tsc --noEmit` | 0 | Qua | 0 | [tsc.txt](227/runs/tsc.txt) |
| `cd portal; ./node_modules/.bin/vite build --configLoader runner --outDir ../tmp/codex-227/portal-dist --emptyOutDir` | 0 | Qua, 149 file; cảnh báo chunk lớn vẫn có | 0 | [vite.txt](227/runs/vite.txt) |
| Git diff check 21 file sản phẩm đã theo dõi | 0 | 0 dòng lỗi | 0 | [whitespace.json](227/runs/whitespace.json) |
| Git no-index check 15 file sản phẩm mới | Không in dòng nào | **15/15** không in dòng nào | 1 mỗi file, bình thường | [whitespace.json](227/runs/whitespace.json) |
| Git no-index check **mọi** file mới của bốn phiếu ở status đầu | Không in dòng nào theo yêu cầu 227 | **133/138** sạch; 5 log có tổng 125 dòng khoảng trắng lỗi | 133 mã 1; **5 mã 3** | [whitespace-all-new.json](227/runs/whitespace-all-new.json); F7, F8 |
| `node tmp/codex-227/audit-214-215.mjs` | Kiểm bổ sung | 6 mục cũ deepEqual, 25 ca ảnh, 9 ca cầu tin | 0 | [audit-214-215.txt](227/runs/audit-214-215.txt), [audit-214.json](227/audit-214.json), [audit-215.json](227/audit-215.json) |
| `python3 tmp/codex-227/audit-216.py` | Kiểm độc lập | Khối server, hash từ vựng, hai fixture CLI đúng | 0 | [audit-216.txt](227/runs/audit-216.txt) |
| Import `configStructureErrors`/`sharedDataAliases` | Không lỗi | 2 conf: 0 lỗi cấu trúc, 0 alias bị cấm ở 6 khối game | 0 | [nginx-validator.json](227/nginx-validator.json) |
| `python3 tmp/codex-227/audit-217.py` | Kiểm bổ sung | 0 media trong hai vùng cấm; kiểm nguồn release và quét mã | 0 | [audit-217.txt](227/runs/audit-217.txt), [audit-217.json](227/audit-217.json) |

Wrapper Audio Lab được chép bằng đúng hai phép thay trong đề bài và đọc lại trước chạy: `parents[2]` ra gốc repo; `root` là `tmp/codex-227/audiolab`; pycache, matplotlib, numba, pytest và basetemp cùng nằm dưới đó. Không chạy wrapper gốc, `run.sh`, demo/verify của phiếu cũ hoặc lệnh đo thời gian cũ. Bản wrapper và các script kiểm bổ sung được giữ dưới dạng TXT trong `227/` để chạy lại sau khi Claude xem xét.

SHA-256 snapshot lõi: `f091f364b03c624afd2ab52e7b52113c88fc1e24945a0b73d3a3ac7d46aa182c`.

### Byte gói portal

| Cách đếm | Sau 214 | Sau 215 / mốc ngoài repo trong đề bài | Lần 227 |
|---|---:|---:|---:|
| JS chính `assets/index-*.js` | 609.295 (`index-CUNiqGGe.js`) | 610.938 | **610.938** (`index-vST_2eXZ.js`) |
| CSS chính | 127.854 | 127.854 | **127.854** (`index-CnQYlBjB.css`) |
| Tổng mọi `.js`, gồm worker/worklet | 4.977.994 ở baseline 215 | 4.979.637 | **4.979.637** |

JS chính/tổng tăng đúng **1.643 byte** do phần lookup của 215; CSS tăng **0**. So với sau 215 không lệch byte nào. [bundle-bytes.json](227/bundle-bytes.json) liệt kê đủ 7 file JS, gồm worker Vosk 4.330.680 byte; không nhầm JS chính với tổng gói.

## Đối chiếu từng phiếu

### 214 · Tên, ảnh, DOM, CSS và script

- `portal/public/games.json:50`, `:63`, `:76`: đúng Dragonhold, Wordwoven, Last Line; mô tả **90/85/99** ký tự, ASCII, một câu kết dấu chấm, 0 ký tự Extended_Pictographic, không còn `icon`, đủ hai đường `art` đúng. So trực tiếp HEAD xác nhận **6/6** mục cũ (kể cả Tu Tiên) và fixture deepEqual; mọi id/path/appUrl/group/thứ tự giữ nguyên. Bằng chứng: `audit-214.json`.
- Helper thuần, không import runtime/DOM/enum/namespace; glyph của mục có `art` luôn null; icon/bìa đủ metadata; listener error một lần (`portal/src/game-card.ts:46`, `:65`). 25 ca bổ sung gồm `%2e%2e`, `%2F`, chữ hoa, khoảng trắng/tab/newline, appUrl có đường dẫn. **Mọi URL không null đều cùng origin appUrl**; F5 ghi riêng giới hạn kiểm tiền tố sau giải mã.
- `portal/src/main.ts:245` đặt alt/width/height/loading/decoding, gắn error trước src; `:258`, `:490` dùng model; `:500` ẩn khung bìa khi lỗi. **0** chỗ đọc `game.icon`. Ba `innerHTML` ở `:485`, `:562`, `:612` đều là hằng chuỗi, không ghép trường registry.
- Diff CSS chỉ thêm 10 dòng tại `portal/src/styles.css:49`: khung 16:9, cover, icon48px/menu1,25em, luật hidden. Không thêm tranh gradient/khối màu thay ảnh. Gradient nền có sẵn ở HEAD không phải thay đổi 214; không nhận xét ngoài phạm vi. Hiệu ứng chiều cao/lưới khi tải/lỗi vẫn cần browser.
- Hai script **chỉ thay nhãn**: thay ba tên cũ trong HEAD cho kết quả giống file hiện tại từng byte. Số tên Việt cũ **0**; **6/6** dòng nhãn Tu Tiên giống HEAD và danh sách `214/verification.json`. Changelog/danh sách ảnh bàn giao đã có. Không sinh hoặc chép ảnh; trạng thái ba thẻ chưa có ảnh được chính phiếu 214 cho phép.

### 215 · Hợp đồng tin và hồ sơ

- Hằng tên lookup và giới hạn **200** khớp `shared/game-kit/learning/contract.ts:7`, `:23`; kit gửi `{type,requestId,query}` tại `shared/game-kit/learning/bridge.ts:166`. Parser kiểm độ dài **mảng trước bỏ trùng**, trim≤200, chuẩn hóa vocabulary, loại khác chỉ trim, bỏ trường lạ; không thêm gameId (`shared/learning/query.mjs:64`, `message-contract.mjs:61`). F4 là ca Unicode không được xử lý nhất quán qua hai lần parse.
- `portal/src/learning/bridge.ts:77`–`:86` kiểm đồng thời iframe, source và origin trước đọc kho. Ca đúng origin nhưng **cửa sổ lạ**, sai origin nhưng đúng cửa sổ, chưa mở game: **0 load, 0 reply**. `:267` dùng targetOrigin cụ thể; không có `"*"`. Ba game đăng ký được kiểm qua handleMessage; requestId giữ nguyên.
- `shared/learning/query.mjs:295` dùng `Object.hasOwn`, tra đúng collection/id, chặn cả own prototype keys; không quét hồ sơ. `:273` dựng query item chung. 29 test shared có các ca gọi thẳng hàm: chúng chứng minh parser/lõi/sao lưu, **không tự chứng minh đường tin**. 26 test mới ở `portal/tests/learning-lookup.test.mjs` có khung giả và handleMessage; ca `stranger` đúng origin ở `:64` kiểm cửa sổ lạ. Không thiếu ca này.
- Handler mới `portal/src/learning/bridge.ts:190` thực hiện flush→load→lookup; test attempt cùng nhịp ra ack rồi query-result; lookup đơn **0 write, 0 callback**, hồ sơ giữ nguyên. Kho đọc lỗi ra query-failed. F2/F3 ghi các giới hạn giữ kín dữ liệu.
- Lõi thêm đúng năm trường mẫu tại `shared/learning/core.mjs:291`, giữ tám mẫu theo thời gian cho cả ba entity; mẫu sinh từ sự kiện không có hai trường câu trả lời. Version vẫn **1**; công thức/đếm/ngày ôn ngoài trường mới khớp snapshot 12 sự kiện từng byte. Sao lưu cũ không có mẫu vẫn nhập được; giới hạn tám/object qua test. F2 chỉ ra sao lưu có mẫu dư trường vẫn được nhận.
- Bộ đọc trong test chép đúng `RECALLS`, `isRightRecall` và `parseLookup` của Dragonhold (`games/dragon-hold/src/app/learning.ts:20`, `:170`): ra **2** recalls. HEAD Dragonhold đọc lại là `1f1de484afd5092f5967454fab5f4e6edd3189c9`, khớp báo cáo 215. README/changelog và danh sách chú thích/tài liệu Claude cần sửa đã có. Không chạy lại lookup-timing vì 227 cấm script đó; không coi 0,1875 ms cũ là số mới đo.

### 216 · Bảo toàn nginx và dữ liệu tự phục vụ

Script độc lập quét ký tự, bỏ comment/chuỗi/escape, lấy từng khối server rồi băm trực tiếp HEAD và hiện tại; không lấy SHA trong báo cáo cũ làm kết quả. [nginx-blocks.json](227/nginx-blocks.json): **22 khối**, 11 mỗi conf, **16/16** khối ngoài ba host giữ nguyên SHA-256/từng byte; chỉ sáu khối HTTPS được giao đổi. Kiểm của chính phiếu cũng cho **0 lỗi cấu trúc**, ngoặc cân và đúng một server_name mỗi host game.

| Mode | Dragon | TD | Survival | Server |
|---|---:|---:|---:|---:|
| Play, location HEAD → nay | **5 → 3** | **6 → 3** | **7 → 4** | **11 → 11** |
| Dev, location HEAD → nay | **3 → 1** | **4 → 1** | **5 → 2** | **11 → 11** |

Space/portal giữ route mà `scripts/validate-space-integration.mjs:135`–`:145` đòi; tutien nguyên byte. Survival giữ **1** route model mỗi conf cùng chú thích ticket205. Sáu khối game có **0** route dữ liệu/đích shared bị cấm. So diff validator với HEAD: giữ các kiểm cũ và thông báo; chỉ thu hẹp vòng bắt buộc dữ liệu còn tutien, thêm cấu trúc/CLI và kiểm alias mới; main chỉ chạy khi gọi trực tiếp.

Hai bản chép conf dưới tmp được thêm alias thật rồi chạy CLI: play/dragon `/vocabulary/` và dev/td `/shared/typing-texts/` đều **mã 1**, stderr đúng host, đường, dòng; [nginx-injected-play.txt](227/runs/nginx-injected-play.txt), [nginx-injected-dev.txt](227/runs/nginx-injected-dev.txt). Không gọi nginx thật.

[vocab-self-serve.json](227/vocab-self-serve.json): ba pin cùng `18338405eebd9cfdbd6d6bf666ea79361c00a564`; hash mọi file manifest và dist/public đều khớp. Dragon **102 nguồn/103 public/103 dist**; TD **7/8/8**; Survival **5/6/6**; **0** file thiếu/thừa/lệch. Số khớp `216/vocab-self-serve.json`. Không quét lại src/dist-JS hoặc vite config của game: 227 chỉ cho đọc file learning Dragonhold và các thư mục vocabulary; kết luận 0 typing-texts/Vite của 216 **chưa được tái chứng minh** trong lượt này. Cần Claude kiểm nguồn đó nếu muốn đóng cả phần dev/self-serve end-to-end.

Changelog nháp đúng chỗ `216/changelog.md`; hai rủi ro cũ vẫn còn: cấu hình đang cài phải được setup lại; file vocabulary thiếu có thể nhận HTML200 qua SPA fallback. Chưa có bằng chứng HTTP để đóng G7.

### 217 · Cô lập đường, giấy phép, test lặp và media

- `tools/audio-lab/firefly/cli.py:78`–`:98` bắt buộc inbox/out, resolve hai gốc, không cho chứa nhau và chặn symlink trong out; `pipeline.py:38` ràng buộc đường đã resolve dưới out; `:177` chặn export tuyệt đối/`.`/`..`; status json/listen cũng đi qua under. Test mới có ca export traversal và symlink về inbox, ba lệnh không ghi thư mục env giả. **Không có mặc định AudioLab/Path.home/env.WORK/env.STAGING** trong firefly/*.py; bốn expanduser đều áp dụng tham số người dùng. Quét đầy đủ ở `audit-217.json`.
- **0** kết quả trực tiếp cho urllib/requests/http/socket/subprocess trong firefly/*.py; không có chương trình ngoài được gọi trực tiếp ở các file mới. Có import `mp3`, `corr_max` từ keys.firefly_build (`pipeline.py:16`, `listening.py:12`). **Chưa chắc** toàn bộ danh sách chương trình ngoài qua helper đó: 227 cấm mở keys; Claude cần kiểm helper/encoder trước khi khẳng định cả chuỗi không gọi tiến trình/mạng. Không suy từ quét file mới thành bảo đảm cho mọi dependency.
- `policy.py:23` đúng lớp, cond adobe-model, attribution false; `:37`–`:41` fullmatch họ Adobe từ đầu đến cuối. `licence_check.py:221` chỉ thêm nhánh điều kiện mới, chặn model thiếu/đối tác và raw redistribution true. Dòng sổ đủ generator/model/author/derivedFrom/prompt khi có, false raw redistribution và true ai_input_allowed; file ghi chú nguồn/copies được giữ nguyên byte qua release. **Chưa xác nhận điều khoản pháp lý mới**, không mạng; đó là việc Claude đã được bàn giao. F6 ghi sự khác nhau giữa nhãn nguồn dự án và output SOURCES.
- Test `tools/audio-lab/firefly/tests/test_firefly.py:114`–`:117` thật sự băm master+OGG trước/sau hai ingest rồi so cả dictionary, đồng thời so inbox hash/mtime. Test này nằm trong **20/20** chạy lại; fixture có bốn biến thể ⇒ **8 file âm** được so. Demo cũ 10/10 là hai id với năm biến thể; không nhầm với số file của ca test. Vì test đã so SHA thật, **không cần viết/chạy thêm script dựng âm lặp**.
- 20 test còn kiểm cắt nguyên mẫu, overlap, gate raw/final, recipe cycle, mức/đỉnh/độ dài, sequence/context20s/cache, status; render→release→licence-check dùng cây tạm và qua. `launch.py` diff **đúng 1 dòng thêm**; pytest.ini **chỉ thêm firefly**. **0 file âm/ảnh** trong firefly và 217/. README/changelog có; chưa nhận/nghe/gắn âm thật, chưa đổi gameplay/ngưỡng L1, không nhân take bằng đổi cao độ.

## Phát hiện, từ nặng tới nhẹ

### 227-F1 · 217 · Chặn cổng cả bộ: 16 lỗi cũ vẫn đỏ

**Vị trí:** `docs/codex-queue/217/test-summary.json:26`; log mới `docs/codex-queue/227/runs/audio-all.txt:583` và `:599`.

**Ca hỏng:** chạy đúng wrapper cô lập được chỉ định → mã **1**, 6 failed +10 errors, dù 539 passed. Ba lỗi env do home/venv cô lập; Board không mở được socket (`PermissionError` ở log dòng63/522); hai Specs vẫn lỗi. [audio-summary.json](227/audio-summary.json) chứng minh **tập 16 tên lỗi giống hệt**, không có lỗi mới, không giảm số qua so với sau217. Đây là **chặn nghiệm thu cả bộ**, không phải kết luận 217 gây hồi quy; không yêu cầu sửa mã làn khác trong 227.

**Đề xuất:** Claude chạy lại cổng Audio Lab ở môi trường hỗ trợ các kiểm đó và xử lý/theo dõi lỗi Specs hiện hữu trước khi ghi cả bộ xanh.

### 227-F2 · 215 · Nặng: recentSamples từ sao lưu chuyển nguyên câu trả lời ra iframe

**Vị trí:** `shared/learning/query.mjs:299`, `shared/learning/profile-backup.mjs:130` (validateSamples ở `:48` chỉ kiểm object và độ dài).

**Ca hỏng:** tạo hồ sơ hợp lệ của lantern, thêm `userAnswer` và `expectedAnswer` vào mẫu → `parseLearningProfileBackup(JSON.stringify(profile))` **nhận** → gửi lookup qua **handleMessage** từ đúng iframe/origin → query-result vẫn chứa cả `PRIVATE_USER_ANSWER` và `PRIVATE_EXPECTED_ANSWER` trong recentSamples. `core` sinh mẫu sạch không bảo vệ được hồ sơ được nhập/lưu từ trước. Không chứng minh gửi sang origin khác, nhưng vi phạm yêu cầu 227 giữ hai trường này khỏi recentSamples.

**Bằng chứng:** `node tmp/codex-227/audit-214-215.mjs`, mã0; ca `accepted backup contains answer fields in recentSamples` trong [audit-215.json](227/audit-215.json) và log một dòng [audit-214-215.txt](227/runs/audit-214-215.txt).

**Đề xuất:** dựng recentSamples khi trả lookup bằng đúng năm trường cho phép và kiểm/loại trường dư ở đường nhập sao lưu.

### 227-F3 · 215 · Vừa: query-failed chuyển tiếp nội dung lỗi/hồ sơ

**Vị trí:** `portal/src/learning/bridge.ts:202`, hàm errorText ở `:51`; `shared/learning/core.mjs:227` đưa giá trị version vào lỗi.

**Ca hỏng:** store.load ném `Error('PROFILE_SECRET: unrequested-word / private answer')` → thông báo nguyên chuỗi tới khung hỏi; hồ sơ lỗi có `version: 'PRIVATE_PROFILE_VALUE'` cũng trả `unsupported learning profile version: PRIVATE_PROFILE_VALUE`. Chỉ cắt 300 ký tự ở makeLearningError không phải lọc dữ liệu. Đây là ca kho/hồ sơ hỏng, chưa chứng minh lỗi IndexedDB thông thường tự chứa câu trả lời; ca fixture chứng minh **không có bảo đảm** thông báo lỗi sạch dữ liệu.

**Bằng chứng:** cùng lệnh mã0; hai ca `storage error includes profile data`, `stored profile version is echoed in query-failed` trong `audit-215.json`. Origin vẫn đúng; không nâng thành lỗi vượt origin.

**Đề xuất:** trả thông báo query-failed cố định, chỉ ghi chi tiết nội bộ ở portal.

### 227-F4 · 215 · Vừa: parse hai lần làm id NFKC hợp lệ thành lỗi kho

**Vị trí:** `shared/learning/query.mjs:89`–`:92`, `:291`; `portal/src/learning/bridge.ts:192`.

**Ca hỏng:** id `"ﬃ".repeat(100)` có 100 ký tự sau trim, được parser hợp đồng nhận và NFKC thành 300 ký tự; hồ sơ thật dựng bằng applyLearningEvents cũng có bản ghi đó. Handler load kho rồi lookupLearningRecords **parse lại** chuỗi đã chuẩn hóa, từ chối vì dài 300 và trả **query-failed** thay vì kết quả. Không có lỗi đọc kho. Đây là ca biên Unicode, chưa thấy trong từ vựng hiện hành.

**Bằng chứng:** cùng lệnh mã0, ca `100 ligatures expand to 300 characters on second parse` trong `audit-215.json`, lỗi `entityId is too long`.

**Đề xuất:** thống nhất giới hạn trước/sau NFKC và bảo đảm dữ liệu đã parse không bị kiểm lại theo quy tắc khác; thêm ca Unicode mở rộng qua handleMessage.

### 227-F5 · 214 · Vừa: tổ hợp dấu phân cách mã hóa vượt kiểm tiền tố sau giải mã

**Vị trí:** `portal/src/game-card.ts:26`, `:33`.

**Ca hỏng tại helper:** `/assets/dragon-hold/portal/%2e%2e%2F%2e%2e%2Fspace-typing/portal/icon.png` được resolveGameArt nhận nguyên URL. Giải mã pathname rồi chuẩn hóa cho `/assets/space-typing/portal/icon.png`, ngoài tiền tố riêng của game. `%2e%2e/` đơn lẻ đã bị chặn; `%2F` làm lọt tổ hợp này. **Origin vẫn đúng** trong cả 25 ca; đây không phải lỗi tải ảnh sang origin ngoài.

**Bằng chứng:** cùng lệnh mã0; `artCases` trong [audit-214.json](227/audit-214.json) ghi input/result/decodedNormalizedPath ở ba kiểu appUrl. **Chưa chắc** nginx đang cài phục vụ đường đã giải mã ra sao, vì 227 cấm nginx/browser/mạng; Claude cần kiểm request thật để chốt tác động. Registry hiện tại có đường ảnh chuẩn, chưa có đầu vào gây hỏng này.

**Đề xuất:** từ chối dấu phân cách/dot segment mã hóa hoặc kiểm tiền tố an toàn sau một quy tắc giải mã được chốt, kèm test tổ hợp `%2e%2e%2F`.

### 227-F6 · 217 · Vừa: nhãn nguồn release cần Claude chốt tính tương đương

**Vị trí:** `tools/audio-lab/firefly/pipeline.py:143`–`:144`, `:183`; nguồn build hiện hữu `tools/audio-lab/build/sources.py:253`, `tools/audio-lab/build/render.py:302`; chuẩn dự án `docs/games/audio/firefly/README.md:7`.

**Ca khác chuẩn:** ingest→release fixture qua test mới tạo dòng sổ có generator=`Adobe Firefly Generate Sound Effects`, model=`Adobe Firefly Audio Model`, author=`project owner`, raw_redistribution_allowed=false; **không có nguyên chuỗi** `Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)`. File giấy phép diễn đạt đủ ý bằng nhiều dòng. SOURCES.json của release chỉ có kind=file/licence/ledgerKey, **models=[]**, **aiSteps=[]** và không có generator/model/author trong layer. Đọc SOURCES cùng dòng sổ theo ledgerKey vẫn có thể khôi phục nguồn; **chưa chắc** Claude chấp nhận dạng tách trường này là tương đương câu chuẩn và có chấp nhận models rỗng không.

**Bằng chứng:** `python3 tmp/codex-227/audit-217.py`, mã0; [audit-217.json](227/audit-217.json) giữ bốn dòng sổ, bốn record SOURCES và `licenceCopyMatches:true` từ cây release tạm của test. Không phải kết luận pháp lý.

**Đề xuất:** Claude xác nhận bằng văn bản dạng tách trường là đủ hoặc bổ sung nhãn chuẩn và metadata model/generation vào output trước nhận âm thật.

### 227-F7 · 216 · Nhẹ: log đỏ cũ có khoảng trắng cuối dòng

**Vị trí:** `docs/codex-queue/216/tests-before.txt:124` (cùng 14 dòng khác).

**Ca hỏng:** `GIT_OPTIONAL_LOCKS=0 git diff --no-index --check /dev/null docs/codex-queue/216/tests-before.txt` → **mã 3**, 15 dòng `trailing whitespace`; 4 file mã của216 vẫn sạch. **Bằng chứng:** `runs/whitespace-all-new.json` ghi đúng argv, mã, mọi dòng lỗi. Đây là khác biệt giữa check file nguồn và check mọi file mới.

**Đề xuất:** Claude bỏ khoảng trắng cuối dòng trong bản log văn bản trước commit, giữ nguyên nội dung chẩn đoán.

### 227-F8 · 217 · Nhẹ: bốn log cũ có khoảng trắng cuối dòng

**Vị trí:** `docs/codex-queue/217/demo.txt:95`, `217/tests-after.txt:31`, `217/tests-before.txt:31`, `217/tests-context-red.txt:17` (đều dưới docs/codex-queue).

**Ca hỏng:** cùng lệnh no-index cho từng file → **mã 3**; lần lượt **1/53/53/3**, tổng 110 dòng `trailing whitespace`. 15 file sản phẩm mới của cả bốn phiếu đều sạch; không có lỗi khoảng trắng trong mã217. **Bằng chứng:** `runs/whitespace-all-new.json`.

**Đề xuất:** Claude chuẩn hóa khoảng trắng cuối dòng trong bốn log trước commit mà không bỏ thông báo lỗi.

## Claude và chủ dự án cần kiểm tiếp

| Người | Việc cần làm |
|---|---|
| Claude · 214 | Ở `https://typing-game.local`, kiểm thẻ/menu 1280 và 1920 khi chưa có ảnh, khi có ảnh176/177 và khi ảnh lỗi; xác nhận 16:9, 48 px, menu gọn, nhãn/khung không lệch. Kiểm F5 bằng request ảnh mã hóa; không coi mock Node là bằng chứng HTTP. |
| Claude · 215 | Sau khi xử lý F2–F4, vào Dragonhold qua cổng: lookup nhận query-result cùng requestId, không error/timeout 2 s; từ đã học ở game khác có bản ghi; sai source/origin vẫn im. Sửa các chú thích/tài liệu cũ theo danh sách215-report. |
| Chủ dự án · 216 | Dùng tài khoản thường chạy `pnpm setup:play` (hoặc `pnpm setup:dev`), script tự hỏi sudo cho kiểm/reload. **Không chạy cả script dưới sudo trên macOS.** Sau áp dụng kiểm vocabulary của dragon/td/survival trả JSON của bản ghim; kiểm route/file thiếu, Content-Type và fallback200 để đóng G7. 227 chưa chạy các lệnh này. |
| Claude · 216 | Kiểm lại src/dist-JS và Vite của ba game trong lượt được phép đọc chúng; xem hướng dẫn sudo cũ và việc bỏ model alias sau 205. Không mở lại Tu Tiên trong lượt227. |
| Claude · 217 | Giải quyết cổng cả bộ F1 trong môi trường phù hợp; xác nhận lớp/allowlist Adobe, ai_input_allowed chỉ chấm cục bộ, bản lưu điều khoản có ngày/URL và nhãn F6. Kiểm chương trình ngoài của helper MP3 trong keys khi được phép. |
| Chủ dự án/điều phối · 217 | Nhận WAV thật, chạy ingest rồi nghe bản 20 s ở cả context/sequence, kiểm các pha hành động theo Q6, clipping/đuôi/gap/biến thể; nghe duyệt rồi mới gắn game. Fixture kỹ thuật không chứng minh thẩm mỹ hoặc quyền phát hành. |

## Mốc cuối, bảy mục kiểm và dọn

HEAD đầu và cuối đều **`52005e3fb37424fcd8212670dd8eec728559ff6a`**; nhánh không đổi. **0 commit chen giữa**, nên không có danh sách diff commit cần bổ sung. Script chụp mốc lưu tại [snap.mjs.txt](227/audit-sources/snap.mjs.txt); lệnh `node tmp/codex-227/snap.mjs docs/codex-queue/227/snap-after.json` mã **0**.

| Mục kiểm | Số và kết luận | Bằng chứng |
|---|---|---|
| 1. Giữ cây ban đầu | **1.312** đường đầu; **1.306/1.306** đường ngoài thay đổi làn khác giữ nguyên cả status và hash. **6** đường cũ của làn khác đổi; **0** đường nguồn 214–217 đổi bởi 227. Status tại mốc sau **1.409** mục. | [snap-before.json](227/snap-before.json), [snap-after.json](227/snap-after.json), [snap-delta.json](227/snap-delta.json) |
| 2. Build cô lập | `portal/dist`: **149/149** file, tên và SHA-256 giống trước/sau. `.vite-temp`: **0 → 0** file. | Hai snapshot và portalDistUnchanged=true trong delta |
| 3. Chạy lại | Portal 77/77, Learning 84/84, nginx 94/94; 20 test 217 mới qua. Audio cả bộ 539/6/10/6 đúng số cũ; **0 tên lỗi mới**. Các mã ở bảng chạy lại; whitespace log là phần khác số/không đạt tiêu chí. | `runs/`, `audio-summary.json` |
| 4. Build/byte | TSC 0, Vite 0; JS chính 610.938, CSS 127.854, tổng JS 4.979.637 byte. Không đổi so sau 215. | `bundle-bytes.json`, `runs/tsc.txt`, `runs/vite.txt` |
| 5. Phát hiện | **1 chặn cũ, 1 nặng, 4 vừa, 2 nhẹ**; đủ file:dòng, ca hỏng, lệnh/mã/log. **0 phiếu thiếu hoặc dừng hiện hành**. | F1–F8; `preflight.txt` |
| 6. Dọn | `tmp/validate-play-mode-test/` **không còn**. `tmp/codex-227/` được xóa sau lưu log; xác nhận máy ở `cleanup.json`. | [cleanup.json](227/cleanup.json) |
| 7. File bị ignore/cache | Lệnh find đúng đề bài sau cùng cho **0 dòng**; không có cache mới ngoài tmp bị Git che. Các file mới sau mốc thuộc 227 hoặc phiếu 220/226, không có pycache/pytest/vite cache ở status ngoài vùng tạm. | [newer.txt](227/newer.txt), `snap-delta.json` |

Chênh mốc được chia ba nhóm: **60** đường của 227 tại thời điểm chụp; **43** đường của làn khác (**6** đổi sẵn có, **37** mới), toàn bộ dưới `docs/codex-queue/220/` và `226/`; nhóm **còn lại=0**. Từng đường và hash trước/sau có trong `snap-delta.json`; không đọc kỹ hoặc kết luận chất lượng phần của hai làn đó. Sáu đường cũ thay đổi là:

- `docs/codex-queue/220/evidence/wave-C.json`
- `docs/codex-queue/220/logs/wave-C.txt`
- `docs/codex-queue/220/summary.md`
- `docs/codex-queue/220/tools/summarize.mjs`
- `docs/codex-queue/220/tools/verify.py`
- `docs/codex-queue/220/tools/write-report.py`

Danh sách tạm trước xóa: **4.565 file, 209.679.070 byte**. [tmp-inventory.txt](227/tmp-inventory.txt) in đầy đủ từng đường và byte; [tmp-summary.json](227/tmp-summary.json) có tổng theo thư mục. Các mục ngay dưới gốc tạm:

- `audiolab/`: 4.405 file, 159.885.829 byte; cache/fixture/đầu ra thử, xóa toàn bộ.
- `portal-dist/`: 149 file, 49.747.552 byte; xóa toàn bộ, không chép vào docs.
- `nginx/`: 2 conf fixture, 18.316 byte; xóa sau lưu log CLI.
- `audit-214-215.mjs`, `audit-216.py`, `audit-217.py`, `paths.py`, `run-commands.py`, `run-tests-217.py`, `snap.mjs`: 7 script, bản nguồn TXT giữ ở `227/audit-sources/`.
- `core-now.json`: 4.606 byte, đã giữ bản JSON trong 227; `marker`: 0 byte.

Chỉ giữ TXT/JSON/MD trong 227; **0 ảnh, 0 âm, 0 portal-dist** được giữ ở đó. Snapshot sau được chụp trước thao tác dọn; các file delta/cleanup và lần hoàn thiện báo cáo phát sinh sau snapshot đều nằm trong vùng 227. Không còn việc mã nguồn nào được thực hiện sau mốc này.
