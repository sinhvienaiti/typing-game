# Phiếu 224 · Wordwoven · Kiểm lại độc lập 170 + 208

**Kết luận: commit được sau khi sửa các P0–P1 nêu.** Không có P0; có **2 P1** cần sửa ở plugin thay nguồn portal và bộ lọc symlink đứt, cùng **2 P2** về test chưa bắt hồi quy. Bản mã chuẩn hiện tại tái lập đầy đủ **40 file / 414 test xanh**, kit **33/33**, production và demo **0 lỗi**; đây chưa phải chứng nhận G7 trên server/trình duyệt.

Phiếu 224 chỉ kiểm trong bản chép, không sửa mã worktree, không commit. Bằng chứng ở [224/](224/); đường mã bên dưới tính từ `games/.wt-td-codex`. Làn s9; đọc yêu cầu model `gpt-6.1-sol`, mức `xhigh` của phiếu và bảng Chọn model, không tự đổi cấu hình runner. Dùng skill `threejs-qa-release` cho kiểm gói; không mở server/browser hoặc chạy bot ngoài phạm vi được giao.

## 1. Preflight, mốc đầu và bản chép

[preflight.txt](224/preflight.txt): **5/5 điều kiện đạt**. Nhánh `td-codex`, HEAD `f9abfd09987dadd519233c2f38692758d35cefca`; status khớp nguyên văn 208, **28 đường**. Đủ **13** đầu vào bắt buộc; thư mục tạm chưa tồn tại. Node **24.22.0**, pnpm **11.21.0**, có rsync/patch hệ thống.

[before.json](224/before.json): **328** đường Git và hợp với toàn bộ public thành **329** file; file thêm bị ignore là `public/assets/typing-defense/ui/title-dusk.webp`. **37/37** hash bảo vệ khớp 208/after (34 kit, 2 golden, 1 manifest model). Lưu tên/loại/mtime **14** mục node_modules và **1** results.json, cùng danh sách tmp checkout chính và status repo cha.

[copy.json](224/copy.json): `tree` và `tree-170` đều **329/329** SHA-256 khớp, mỗi bản **11** symlink tuyệt đối bên trong node_modules thật. Không symlink `.vite`, `.vite-temp`, workspace state. Tất cả pnpm dùng `pnpm_config_verify_deps_before_run=false`, `TMPDIR` riêng và chỉ cwd trong bản chép; biến portal vắng/trống/có được lưu ở mỗi `*-run.json`. Không install/add/sync/pull.

## 2. Tách 170/208 và kiểm trạng thái 170

[split.log](224/split.log), [split.json](224/split.json): `/usr/bin/patch -R -p1 -E` mã **0**, vá **12 file**, **0** rej/orig; **7/7** file mới 208 bị xóa. `learning.ts`, `vite.config.ts` khớp HEAD; **3/3** file chung khớp 208/before. Nền còn đúng **19 đường: 14 sửa, 5 mới**, trùng Nhóm 170; không tính title-dusk bị ignore. [paths.json](224/paths.json) phân loại đủ **28** đường và số dòng thêm/bớt của từng phiếu: **19 + 12 − 3**.

Nền 170: `pnpm check` mã **0**, **37 file / 380 test / 0 đỏ**, kit **33**, tsc/build qua; golden **6/6**. `deploy:pack` mã **1**, đúng **69 lỗi = 1 local-host + 68 missing-model**; checker local mã **1**, còn **68 missing-model**. Gói **55 file / 1.206.837 byte**, **54/55** SHA-256 trùng inventory 170. Chỉ `.vite/manifest.json` **16.655** thay **15.155** byte: **60 × 25 = 1.500 byte**, tiền tố thật `../../../../.wt-td-codex/`. Đây là khác biệt vị trí bản chép đã dự kiến, không phải hồi quy. [dist-170-comparison.json](224/dist-170-comparison.json), [manifest-paths.json](224/manifest-paths.json).

## Đối chiếu yêu cầu 170, phần Kiểm của 168 và 208

Đường `file:dòng` trong các bảng này tính từ `games/.wt-td-codex`. “Đạt qua hồ sơ” chỉ xác nhận bằng chứng lịch sử đã lưu; phiếu 224 không thể tái tạo thứ tự thao tác hoặc tải máy của phiên cũ.

| Phiếu / mục | Kết quả | Đối chiếu với nguồn và bằng chứng |
| --- | --- | --- |
| 170 · Việc 1: theo nhãn kit tiếng Anh, không nới test | Đạt | `tests/td-flow.test.ts:67`: giữ số và cấu trúc, đổi chính xác `Balanced`, `Standard`, `Shared flow band`, `Matches human play`, `MISSING DATA`; thêm `Learning stays clear · PASS`. `check-170.log`: 380 xanh. |
| 170 · Việc 2: hai lệnh deploy đúng game, README như 168 | Đạt ở nền 170 | `package.json:13`, `README.md:5`; bản tách khớp ba file `208/before/`. `split.json`, `deploy-170.log`: build rồi checker thật, local chỉ thêm cờ cho phép host nhà. |
| 170 · Việc 3a: tên tải tiếng Anh | Đạt | `src/app/retry.ts:71`; M4 làm 1 test đỏ; trả file thì 5/5 xanh. |
| 170 · Việc 3b: các bộ đọc vẫn nhận tên cũ | Đạt | `scripts/td/b9.ts:11` nhận đường dẫn bất kỳ; `tests/td-b9.test.ts:53` chạy CLI thật với hai mẫu tên, cùng hash. Quét không có bộ lọc tiền tố khác. |
| 170 · Việc 3c: chỉ đổi dòng tên file trong hướng dẫn | Đạt | `docs/td/PLAYTEST_1B.md:32,58`, `docs/td/BUILD_1B.md:547`: đúng ba dòng. Tên cũ trong `BUILD_NOTES.md:1343` là ván lịch sử; các chỗ còn lại là tương thích/test. |
| 170 · Việc 4: gói thật, JSON và phân loại lỗi | Đạt | `pack-170.json`: 1 `local-host` + 68 `missing-model`, đối chiếu báo cáo 170 §4; không coi 95 level từ vựng không ghim là lỗi. |
| 170 · Luật/Cấm: giữ lượt kit có sẵn, không sửa kit/kit cha, không kit:sync | Đạt trong diff | `src/kit/kit-manifest.json:5` ghi commit cha và `parentDirty: true`; 31 module khớp commit, 2 file sinh khớp; 37 hash được bảo toàn. `kit.json`, `before.json`, `after.json`. Không suy ra toàn bộ lịch sử lệnh từ diff. |
| 170 · Luật/Cấm: Git chỉ đọc, không đụng game/worktree khác hoặc Tu Tiên | Đạt trong phạm vi kiểm được | `paths.json`: 19 đường nền 170, không có nguồn game khác. Phiếu 224 chỉ dùng Git đọc. Không chứng minh được lịch sử lệnh của tác giả 170 chỉ bằng ảnh chụp cuối. |
| 170 · Luật/Cấm: không server, trình duyệt, mạng, media vào Git | Đạt trong bằng chứng/diff | 19 đường đều là mã, test, tài liệu; không media mới. Phiếu 224 không mở mạng/server/trình duyệt; G7 thực còn chờ Claude. |
| 170 · Luật: test trước mã, chú thích tiếng Anh | Đạt qua hồ sơ / đạt mã | Hồ sơ 170 ghi 1 đỏ/6 xanh và 9 đỏ/4 xanh trước sửa. `src/app/retry.ts:68`, `scripts/td/b9.ts:6` là chú thích tiếng Anh mới. Không tái hiện thứ tự lịch sử. |
| 170 · Luật: luật chơi và golden không đổi | Đạt | Diff không có `src/sim`, `src/content`, `src/typing`; hash hai golden giữ nguyên, 6 test golden nền 170 xanh. |
| 170 · Kiểm kế thừa 168: pnpm check, verify-kit | Đạt | `check-170.log`: 37 file/380 test, kit 33/33, TypeScript/build qua. |
| 170 · Kiểm kế thừa 168: test thời gian đỏ chạy riêng ba lần | Đạt qua hồ sơ; lượt mới không phát sinh | Lượt 170 cũ có 3/3 xanh trước tăng timeout; lượt 224 nền 170 và cuối đều không đỏ thời gian. Không chạy lại ba lần khi điều kiện không phát sinh. |
| 170 · Kiểm kế thừa 168: status chỉ kit, mã/test/README/changelog cho phép | Đạt | `split.json`: đúng 19 đường, 14 sửa/5 mới; 9 kit + 10 ngoài kit, khớp danh sách 208 §1. |
| 170 · Kiểm thêm: tên mới lúc tải, CLI nhận hai tên | Đạt | `tests/td-b9.test.ts:26,53`, `check-170.log`, M4. DOM giả kiểm thao tác tải; CLI là tiến trình thật. |
| 208 · Trước phiếu: 170 chưa commit thì tiếp tục và tách phần chung | Đạt | `208-report.md` mở đầu nêu rõ; patch ngược sạch 12 file, ba file chung khớp byte `208/before/`; `split.json`, `paths.json`. |
| 208 · Việc 1a: baseline deploy và JSON trên chính dist | Đạt qua hồ sơ, tái lập số | Nền 170 phục dựng cho đúng 69 lỗi; `pack-170.json`, `dist-170.json`. Byte chênh 1.500 do manifest Vite của bản chép, 54/55 hash trùng. |
| 208 · Việc 1b: hash kit, golden, manifest model trước sửa | Đạt | `208/before.json`, `208/after.json` và 37 hash mới khớp; `before.json`, `after.json`. |
| 208 · Việc 2: test trước mã, lưu đỏ/xanh | Đạt qua hồ sơ | `208/tests-before.json` ghi 34 đỏ/8 xanh ở 4 file; lượt cuối 224 414 xanh. Thứ tự phiên cũ không thể kiểm chứng bằng chạy trạng thái cuối. |
| 208 · Việc 3a: VITE_PORTAL_URL là HTTP(S) tuyệt đối, không credentials, sai dừng build | Đạt theo bộ phân tích URL | `src/app/portal.ts:2`, `tests/portal.test.ts:26`, `tests/portal-build.test.ts:52`; probe bổ sung `data/file/ws`, khoảng trắng, credentials rỗng, cổng/query/fragment. Chuẩn hóa URL theo WHATWG được ghi riêng, không gán thành lỗi bảo mật. |
| 208 · Việc 3b: mặc định trống, bị nhúng vẫn giữ queue, không gửi/focus | Đạt | `src/app/learning.ts:8,22,23`; kit `bridge.ts:122,149,177,292`; M2 bắt hồi quy 1 đỏ. Host không parent khiến constructor không xả queue, `sendAttempt` ghi cục bộ, `flushQueue=0`, `requestFocus=false`. |
| 208 · Việc 3c: có biến chỉ gửi/nhận đúng origin | Đạt | `src/app/learning.ts:22`, kit `bridge.ts:248,292`; test thật bridge + host/storage giả kiểm nguồn và `event.source`. Không có danh sách origin hay `*`. |
| 208 · Việc 3d: thay đúng một khai báo trong bộ nhớ, kit đĩa nguyên | Thiếu chặn đường bỏ qua plugin · P1-01 | `vite.config.ts:47,48`: chỉ so chuỗi id; query và cấu hình qua symlink build thành công còn host nhà. Hàm thay có chặn 0/2 nếu được gọi, CRLF qua. Plugin không có guard khi transform chưa chạy. `vite-probes.json`. |
| 208 · Việc 3e: giữ LAZY/chunkOf/manualChunks/port và bridge trong Học | Đạt | `vite.config.ts:11,19,59,83`; `tests/td-chunks.test.ts:57`; build thật có giao thức học trong learn, entry không có. `chunks.json`. |
| 208 · Việc 3f: không thêm nút về portal hay chữ người chơi | Đạt trong diff | `src/app/portal.ts:1` chỉ là helper; `learning.ts` không tạo UI; diff không sửa menu/nút. |
| 208 · Việc 4a: deploy-models.json trống, script mới cạnh game | Đạt | `deploy-models.json:1`, `scripts/deploy/prune.mjs:42`. Probe cwd khác vẫn đọc danh sách cạnh script, không dùng danh sách ở cwd. |
| 208 · Việc 4b: trống bỏ models; chọn giữ mọi tier/metadata, ghi manifest dist | Đạt | `scripts/deploy/prune.mjs:56,63,65,71,82`; `tests/deploy-prune.test.ts:48,57`; query/fragment được bỏ khi xác định file. |
| 208 · Việc 4c: khóa lạ/URL ngoài models dừng trước ghi/xóa | Đạt | `scripts/deploy/prune.mjs:18,25,60,68`; fixture thật chặn `%2e%2e`, `..%2f`, URL tuyệt đối, backslash; trước/sau bằng nhau khi lỗi. `prune-probes.json`. |
| 208 · Việc 4d: chỉ ghi trong dist có index; từ chối symlink mọi cấp | Thiếu với symlink đứt · P1-02 | `scripts/deploy/prune.mjs:8,49`: `existsSync=false` bỏ qua dangling link, rồi vẫn xóa ở `:71,85`. 6/7 ca dangling trả 0 và đổi dist; sentinel ngoài dist 27/27 nguyên. Symlink sống ở 9 vị trí đều bị chặn. |
| 208 · Việc 4e: không models vẫn qua; bỏ .vite; thông báo một dòng | Đạt trên gói hợp lệ | `scripts/deploy/prune.mjs:51,85,86`; mỗi gói bỏ 2 file/39.623 byte; `deploy-*.log`, M3. |
| 208 · Việc 4f: deploy = build → prune → checker; local chỉ thêm allow-local-host | Đạt | `package.json:13,14`; tiến trình package/checker thật trong test, build fixture; deploy thật ba gói đều mã 0. |
| 208 · Việc 4g: build một mình giữ models/.vite và không đổi lệnh | Đạt | `package.json:9` bằng HEAD; `build-only.json` có cả hai manifest; `bundle-budget.mjs` vẫn chạy trước prune. |
| 208 · Việc 5a: README biến, production trống, demo nhà, danh sách/bước lọc | Đạt; còn có thể nói rõ hơn đường đọc danh sách | `README.md:7,12,18,25,27,29`. README đặt file ở gốc game, không nói sai rằng đọc cwd; chưa ghi rõ “cạnh script, độc lập cwd”. Probe xác nhận triển khai đúng. |
| 208 · Việc 5b: lưu ý C13, STARTER/NIGHT_1 cho làn L | Đạt | `README.md:31`, `208-report.md` §5. Không mở làn 1C. |
| 208 · Việc 5c: changelog có số trước/sau | Đạt | `docs/changelog/2026-10-30-deploy-pack.md:6,7`, khớp gói biến trống đã tái lập. |
| 208 · Việc 5d: việc Claude ghi hai lệnh repo cha và tên biến cũ | Đạt qua hồ sơ | `208-report.md` §5 có đúng `build:td`, `dev:td:app`, giữ biến HMR, và ba mục tài liệu `VITE_PORTAL_ORIGINS`; không sửa repo cha thay Claude. |
| 208 · Việc 6a: test URL và hai chế độ bridge | Đạt các ca yêu cầu | `tests/portal.test.ts:26,38,57`; 14 test, M2 đỏ; singleton lười còn hở test P2-02. |
| 208 · Việc 6b: Vite thật, hai chế độ, tmp tự xóa, kit nguyên | Đạt ca chuẩn; thiếu id biến thể | `tests/portal-build.test.ts:28,50,56,59`; JS build được chạy bằng Node thật; kiểm kit trên đĩa; M1 đỏ. Query/symlink chưa được test nên P1-01 lọt. |
| 208 · Việc 6c: lọc trống/một khóa/khóa lạ/không models/public nguyên | Đạt các ca yêu cầu chính | `tests/deploy-prune.test.ts:14,41,44,48,57,65,79`; subprocess script thật; cleanup bằng finally ngay cả khi M3 đỏ. Chặn tổ tiên chưa có test: P2-01. |
| 208 · Việc 6d: deploy fixture chép script/list, missing GLB vẫn qua sau lọc | Đạt | `tests/deploy-pack.test.ts:18,61`; pnpm con chạy package thật, checker thật, build nhỏ giả; không tuyên bố fixture thay Vite build thật. |
| 208 · Cấm 1: Git ghi | Đạt trong bằng chứng phiếu 224; lịch sử tác giả theo hồ sơ | Không commit/add/stash/checkout/reset/apply/worktree/clean; tách bằng `/usr/bin/patch`. `paths.json`, preflight/scope. |
| 208 · Cấm 2: sửa kit/kit cha, kit:sync | Đạt trong diff | 208-only patch không chứa kit; 37/37 hash khớp, module và bản sinh khớp byte. |
| 208 · Cấm 3: sửa public manifest hoặc media; chỉ lọc dist | Đạt | Public manifest thuộc 37 hash; không đường public nào trong 28 đường; fixture public bất biến; `prune-probes.json`. |
| 208 · Cấm 4: nới checker, thêm cờ bỏ qua, tải model | Đạt | Checker kit khớp commit; chỉ local có cờ được chỉ định; 0 GLB/GLTF/BIN ở ba gói, không media mới trong diff. |
| 208 · Cấm 5: server/browser/mạng/media:pull | Đạt trong lượt 224 và hồ sơ 208 | Không chạy các bước này. Một lần CLI tsx của probe bị EPERM ở IPC pipe; đã dùng `node --import tsx`, không mở dev server. Log thử đầu được giữ. |
| 208 · Cấm 6: sửa package/nginx/docs thiết kế repo cha | Đạt trong phạm vi 224 | Chỉ báo cáo/bằng chứng 224; các thay đổi làn khác được tách trong `scope.json`. Phiếu 208 chỉ cung cấp đề xuất ở §5. |
| 208 · Cấm 7: game/worktree khác, đặc biệt 1C/keys, Tu Tiên | Đạt | Chỉ đọc worktree chỉ định, commit kit cha và README kit main được cho phép; không mở các worktree cấm. |
| 208 · Cấm 8: media vào Git | Đạt trong diff | 28 đường không có media; không tạo ảnh/âm, không chép dist vào bằng chứng. |
| 208 · Kiểm 1: pnpm check, file/test/kit, lặp lỗi thời gian nếu có | Đạt | 40/414, kit 33, mã 0; không lỗi thời gian cần lặp. `check.log`. |
| 208 · Kiểm 2: golden hai ván same true | Đạt | 2/2, 19.660 và 5.695 tick, 0 problem/rejected; `golden.log`. |
| 208 · Kiểm 3: hai ngân sách ≤85 kB và cầu học ở chunk Học | Đạt | Nền 170 79,60/81,07; biến vắng 79,60/81,16; biến trống 79,60/81,30. `check-170.log`, `check.log`, `deploy-empty.log`, `chunks.json`. |
| 208 · Kiểm 4: production 0 lỗi, inventory, không models/.vite/local host | Đạt ca chuẩn | Vắng: 53/1.167.486; trống: 53/1.167.750, 53/53 hash trùng 208. Mỗi gói quét 21 file văn bản, 0 host nhà. `scan.json`. |
| 208 · Kiểm 5: local 0 lỗi; production kiểm lại đúng 1 local-host | Đạt | Gói local 53/1.167.801, checker local mã 0; checker production mã 1, chỉ 1 `local-host`. |
| 208 · Kiểm 6: bảng trước/sau và nguyên nhân | Đạt | 69→0, 55→53; 1.206.837→1.167.750 trong bản chép; chênh manifest 1.500 được tách khỏi thay đổi nguồn. `claims.json`. |
| 208 · Kiểm 7: 37 hash và git diff --check | Đạt | `integrity.json`: 37/37, mã 0; toàn bộ 329 hash worktree nguyên. |
| 208 · Kiểm 8: phạm vi 28 đường và hai dòng package riêng | Đạt | 19+12−3=28; không đường lạ, không mất 170; `paths.json`, `split.json`; `package.json:13,14`. |


## 3. Bảng đối chiếu số

Chép đầy đủ từ [claims.json](224/claims.json). Những hàng “khớp hồ sơ” chỉ đọc lại log cũ và hash bằng chứng, không gọi đó là lượt test mới; tải máy và thời gian lịch sử không thể tái hiện bằng mã cuối.

| Phiếu | Kiểm | Phiếu báo | Đo/đối chiếu lại | Khớp | Giải thích | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- |
| 170 | Luồng trước sửa | 1 đỏ / 6 xanh | Tests  1 failed \| 6 passed (7) | khớp hồ sơ | Chỉ đọc lại log lịch sử; không tái hiện trạng thái và tải máy của phiên trước. | historical-evidence.json |
| 170 | Test mới trước sửa mã | 9 đỏ / 4 xanh | Tests  9 failed \| 4 passed (13) | khớp hồ sơ | Chỉ đọc lại log lịch sử; không tái hiện trạng thái và tải máy của phiên trước. | historical-evidence.json |
| 170 | Check lần đầu | 378 xanh / 2 đỏ; CLI 7,858 s | Tests  2 failed \| 378 passed (380) | khớp hồ sơ | Chỉ đọc lại log lịch sử; không tái hiện trạng thái và tải máy của phiên trước. | historical-evidence.json |
| 170 | CLI riêng ba lần trước đổi timeout | 3/3 xanh; test 1,834/1,913/2,015 s; cả lệnh 4,075/3,362/3,593 s | Log cũ 3/3 xanh; CLI mới trong check-170 3,485 s | khớp hồ sơ | Không có lỗi thời gian ở lượt mới nên không kích hoạt chạy lặp ba lần. Thời gian cũ không phải số tái đo. | historical-evidence.json; check-170.log |
| 170 | Check cuối | 37 file / 380 test; mã 0; 24,422 s | 37/380; mã 0; 17.4121 s | khớp | Thời gian thay đổi theo tải máy. | check-170.log; check-170-run.json |
| 170 | Kit | 33/33 | 33/33 | khớp | 34 file kit gồm manifest; verifier kiểm 33 file được manifest liệt kê. | check-170.log; kit.json |
| 170 | Golden trong check | 6/6; hai hash giữ nguyên | 6/6; 2/2 hash giữ nguyên | khớp | Không cập nhật golden. | check-170.log; integrity.json |
| 170 | Sim ≤2 ms | 0,064 / 0,057 / 0,232 ms | [0.069, 0.053, 0.104] ms | đạt ngưỡng | Số mới 0,069/0,053/0,104 ms; không yêu cầu trùng thời gian cũ. | check-170.log |
| 170 | Ngân sách hai trang ≤85 kB | 79,60 / 81,07 kB | 79,60 / 81,07 kB | khớp | Cùng nguồn nền 170. | check-170.log |
| 170 | Whitespace và phạm vi | diff --check=0; sim/content/typing sạch | mã 0; 19 đường, 0 ở ba thư mục đó | khớp | 14 sửa/5 mới; kit/golden được kiểm hash. | diff-check-run.json; split.json; integrity.json |
| 170 | Production | mã 1; 69 lỗi = 1 local-host + 68 missing-model | mã 1; 69 = 1 + 68 | khớp | Không báo nhầm về tồn tại model. | pack-170.json; deploy-170-run.json |
| 170 | Checker local trên cùng gói | mã 1; 68 missing-model | mã 1; 68 missing-model | khớp | Chỉ local-host được miễn. | pack-170-local.json |
| 170 | Inventory | 55 file / 1.205.337 byte | 55 file / 1.206.837 byte; 54/55 hash trùng | khớp sau giải thích | Chỉ .vite/manifest.json 15.155→16.655 byte: 60 × tiền tố ../../../../.wt-td-codex/ dài 25 = 1.500 byte. | dist-170-comparison.json; manifest-paths.json |
| 170 | Thông tin bộ kiểm | 95 level không ghim; external 0; GLB thiếu 68 | 95; external []; 68 missing-model | khớp | 95 là thông tin, không thuộc lỗi. | pack-170.json |
| 208 | Kiểm 1 · check | 40/414; kit 33; mã 0; 12,297 s | 40/414; kit 33; mã 0; 18.3881 s | khớp | Thêm 3 file/32 test; deploy-pack thêm 2 test: tổng tăng 34. | check.log; test-growth.json |
| 208 | Kiểm 2 · golden | 2/2 same=true; 19.660/5.695 tick | 2/2; 19.660/5.695; 0 problems/rejected | khớp | Lệnh check không ghi golden. | golden.log |
| 208 | Kiểm 3 · ngân sách/chunk | 79,60 / 81,30 kB; bridge chỉ trong Học | Vắng 79,60/81,16; trống 79,60/81,30; entry 0 giao thức học | khớp theo biến | Vắng biến gập hằng portalHome(undefined), learn ít hơn 264 byte. Cả hai ≤85. | check.log; deploy-empty.log; chunks.json |
| 208 | Kiểm 4 · production | 0 lỗi; 53 / 1.167.750; 0 host nhà | Trống: đúng số và 53/53 hash; vắng: 53 / 1.167.486 | khớp theo biến | Mỗi gói 21 file văn bản, 0 host nhà; 0 GLB/GLTF/BIN, không models/.vite. | pack-empty.json; dist-empty-comparison.json; scan.json |
| 208 | Kiểm 5 · demo/kiểm chéo | demo mã 0, 0 lỗi; production 1 local-host | đúng; demo 53 file / 1.167.801 byte | khớp | Checker production mã 1, chỉ 1 local-host. | pack-local.json; pack-local-production.json |
| 208 | Kiểm 6 · trước/sau | 69→0; 55→53; 1.205.337→1.167.750 (−37.587) | 69→0; 55→53; 1.206.837→1.167.750 (−39.087) | khớp sau giải thích | Lọc bỏ 2 file/39.623 byte, hơn số cũ 1.500 do manifest Vite; JS nguồn tăng 536 byte. Trừ phần đường môi trường thì giảm đúng 37.587. | deploy-empty.log; dist-170.json; dist-empty.json |
| 208 | Kiểm 7 · bảo toàn/whitespace | 37/37; diff --check=0 | 37/37; 329/329; mã 0 | khớp | Kit, golden và public manifest nguyên byte. | integrity.json; kit.json |
| 208 | Kiểm 8 · phạm vi | 28 = 19 + 12 − 3; HEAD không đổi | 28, đúng 3 dùng chung; 0 đường lạ; HEAD không đổi | khớp | Patch ngược 12 file sạch, 7 file mới xóa đúng, ba bản before khớp. | paths.json; split.json; integrity.json |


`37/380 → 40/414` được đếm trực tiếp từ log: `portal.test.ts` **14**, `portal-build.test.ts` **7**, `deploy-prune.test.ts` **11** = **3 file / 32 test**; `deploy-pack.test.ts` **8→10**, tăng **2**. Tổng tăng **34**, không mất test cũ. [test-growth.json](224/test-growth.json). Lượt mới không có lỗi thời gian ngoài các lỗi cố ý gây bằng đột biến, nên không có file nào phải chạy riêng ba lần.

## 4. Các gói và quét

| Gói / chế độ checker | Mã checker | Số lỗi | Theo code | File | Byte |
| --- | --- | --- | --- | --- | --- |
| 170 | 1 | 69 | {'local-host': 1, 'missing-model': 68} | 55 | 1.206.837 |
| 170-local | 1 | 68 | {'missing-model': 68} | 55 | 1.206.837 |
| absent | 0 | 0 | 0 | 53 | 1.167.486 |
| empty | 0 | 0 | 0 | 53 | 1.167.750 |
| local | 0 | 0 | 0 | 53 | 1.167.801 |
| local-production | 1 | 1 | {'local-host': 1} | 53 | 1.167.801 |


Ba lệnh deploy (vắng/trống/local) đều mã **0**, lần lượt **3,6282 / 3,6171 / 3,765 s**; riêng nền 170 mã **1** sau build. JSON và inventory lưu ở `pack-*.json`, `dist-*.json`, lệnh/env/mã/giây ở `*-run.json`. Gói biến trống **53/53 hash và byte trùng** 208/dist-final. Gói biến vắng ít hơn **264 byte**, chỉ learn **8.273** thay **8.537** byte; Vite gập hằng cho `portalHome(undefined)`, đúng nguyên nhân phiếu đã nêu. Tên chunk thay đổi theo hash của nội dung và tham chiếu import.

| Gói | File văn bản | Chuỗi host nhà | Prefix / số lần | GLB/GLTF/BIN | Có .vite | Có models |
| --- | --- | --- | --- | --- | --- | --- |
| absent | 21 | 0 | {'/assets/typing-defense/': 1} | {'.glb': 0, '.gltf': 0, '.bin': 0} | False | False |
| empty | 21 | 0 | {'/assets/typing-defense/': 1} | {'.glb': 0, '.gltf': 0, '.bin': 0} | False | False |
| local | 21 | 2 | {'/assets/typing-defense/': 1} | {'.glb': 0, '.gltf': 0, '.bin': 0} | False | False |


[scan.json](224/scan.json) có số host nhà theo **từng file**, kể cả số 0, và mọi prefix khác nhau. Prefix game khác **0** trong cả ba gói. Local có **2 chuỗi** host trong một learn chunk, bộ kiểm báo **1 lỗi theo file**, đúng kỳ vọng. Mọi lượt prune bỏ **2 file / 39.623 byte**, hơn số 208 **1.500** vì 60 đường trong manifest Vite; file đó bị bỏ trước checker. Không lưu dist hoặc media trong thư mục bằng chứng.

`pnpm build` thường vẫn giữ model manifest và `.vite`: [build-only.json](224/build-only.json). Giao thức học chỉ ở learn chunk, entry có **0** chuỗi namespace học: [chunks.json](224/chunks.json); test chunk còn giữ LAZY/chunkOf/manualChunks và port 3006.

## 5. Đọc kỹ URL, bridge, plugin và prune

`portalHome`: undefined/rỗng/toàn khoảng trắng → null; bỏ khoảng trắng hai đầu; space trong hostname bị từ chối, space ở path thành `%20`. `user@` và `:pass@` bị từ chối. `https://@host/` và `https://:@host/` được URL parser chuẩn hóa thành không credentials; tab/newline giữa URL bị URL parser bỏ, `https:host` chuẩn hóa thành HTTPS. Đây là cách parse URL hiện có, không có thông tin đăng nhập bị gửi. Nếu muốn cú pháp chặt hơn thì cần quyết định/test riêng, không tự coi các chuẩn hóa này là P0/P1.

`javascript:`, `data:`, `file:`, `ftp:`, `ws:`, URL tương đối và protocol-relative đều bị từ chối. Cổng/query/fragment giữ trong href; bridge dùng `.origin`, giữ cổng khác mặc định và bỏ đường/query/fragment. `http:` production được nhận **đúng yêu cầu HTTP(S) của 208**, không có quy tắc HTTPS-only trong phiếu. Khuyến nghị vận hành dùng HTTPS khi portal thật dùng HTTPS; không tự thêm rào cản mới.

Bridge trống dùng `standaloneHost.parent=null`: constructor kit không flush, sendAttempt nối queue, flushQueue=0, requestFocus=false, không đăng ký listener thật. Với portal đã cấu hình, chỉ origin đó được postMessage và chỉ đúng parent+origin được nhận. Kit vẫn **xóa queue ngay sau gửi**, không chờ ack (`src/kit/learning/bridge.ts:149`); đây là hành vi kit có sẵn được 208 giữ, cần Claude kiểm rủi ro mất sự kiện nếu parent chưa sẵn sàng. Phiếu này không mở rộng thành sửa kit. Singleton nguồn hiện tại thực sự lười; test chưa chứng minh được thời điểm tạo (P2-02).

Plugin chỉ nhận đúng chuỗi id canonical. Probe Vite thật chứng minh `?v=`, `?import`, config qua symlink đều build xanh nhưng còn mặc định host nhà; synthetic id khác hoa/thường cũng không khớp. Không suy ra mọi import khác hoa/thường trên mọi filesystem đều build được. Không có guard khi contract chưa transform. Hàm replace riêng chặn 0/2 khai báo, giữ `$&` theo callback, và **CRLF qua/giữ CRLF**. Plugin cũng được đăng ký khi command=serve (chỉ kiểm config, không chạy dev). `.env.production` trong bản chép được load: có thể đặt origin khi process env vắng; process env `VITE_PORTAL_URL=''` ghi đè thành trống. [vite-probes.json](224/vite-probes.json).

Prune: URL `%2e%2e`, backslash, double encoding và URL tuyệt đối đều bị chặn trước xóa; query và fragment bỏ khi tìm file; duplicate keys được dedupe; phần tử không phải chuỗi và list thiếu models bị từ chối. Manifest không có models, khi chọn khóa, trả “Unknown model key” trước xóa; danh sách trống không cần đọc manifest để bỏ cây model. Danh sách đọc cạnh script, không phải cwd; README chỉ rõ file ở gốc game nhưng có thể thêm một câu về điều này. **27 probe**, sentinel ngoài dist **27/27 nguyên**; symlink sống **9/9 bị chặn**, dangling **6/7 bị bỏ sót**, index dangling bị chặn. [prune-probes.json](224/prune-probes.json). Các kiểm ngữ nghĩa của đường hợp lệ nằm trước lần ghi/xóa đầu; lỗi dangling là ngoại lệ đã tái hiện, không diễn giải thành đã xóa ngoài dist.

## 6. Kit và chất lượng test

[kit.json](224/kit.json): **31/31** file module bằng byte với `git show 1b1fe6cfacdc81a55d13af202da0f42023455313:shared/game-kit/<path>`; **0 khác**. README bằng byte README kit checkout chính và template sinh; verify-kit bằng byte export `VERIFY_SOURCE`. Import script sync không gọi main (guard gọi trực tiếp); không sync. Manifest ghi đúng commit cha, **parentDirty=true**. Verifier kiểm **33/33**, cộng manifest thành **34** file kit.

Portal test dùng bridge thật với host/storage giả; build test dùng cấu hình Vite thật và thực thi JS đầu ra bằng Node. Prune/check-pack là subprocess thật. Deploy fixture dùng build nhỏ giả để chứng minh chuỗi lệnh/chặn lỗi, được bổ sung bằng ba deploy thật. Test tải file dùng DOM/clipboard giả nhưng kiểm Blob, click, revoke, nội dung; B9 chạy CLI thật và so replay hash. `td-flow` giữ các khẳng định số và nhãn kit; không nới sang kiểm tồn tại chung chung.

Fixture của các file được hỏi đều dọn bằng finally, kể cả khi test đỏ trong M1–M4: cuối **0 fixture sót**. Timeout CLI **20 s** ở test B9 được chặn thêm bằng `spawnSync timeout=15 s`, không biến treo vô hạn thành xanh; không nới ngưỡng sim. Test prune subprocess chưa đặt timeout riêng, nên nếu chính script treo đồng bộ thì timeout Vitest không ngắt được `spawnSync`; hiện không có lỗi treo được quan sát, có thể bổ sung timeout tiến trình khi sửa test. Lần thử dùng `tsx` CLI của probe bị EPERM khi mở IPC pipe; đã đổi sang `node --import tsx`, giữ log thử đầu. Một lỗi script đo template thiếu biến `VERIFY_FILE` cũng được sửa trong script bằng chứng và giữ log; hai lỗi công cụ đo này không phải lỗi game.

## 7. Đột biến

| Mã | Sửa một file | Test | Khi sửa: đỏ/xanh | Trả lại: đỏ/xanh | Hash trả lại |
| --- | --- | --- | --- | --- | --- |
| M1 | vite.config.ts: Giữ kiểm đúng một khai báo nhưng không thay origin | tests/portal-build.test.ts | 3/4 | 0/7 | khớp |
| M2 | src/app/learning.ts: Luôn đưa host nhúng cho kit, kể cả khi biến trống | tests/portal.test.ts | 1/13 | 0/14 | khớp |
| M3 | scripts/deploy/prune.mjs: Bỏ bước xóa .vite | tests/deploy-prune.test.ts, tests/deploy-pack.test.ts | 5/16 | 0/21 | khớp |
| M4 | src/app/retry.ts: Tên tải xuống trở về mẫu cũ | tests/td-b9.test.ts | 1/4 | 0/5 | khớp |
| M5 | scripts/deploy/prune.mjs: Bỏ chặn symlink ở dist và tổ tiên | tests/deploy-prune.test.ts | 0/11 | 0/11 | khớp |
| M6 | src/app/learning.ts: Khởi tạo singleton ngay lúc import thay vì lười | tests/portal.test.ts | 0/14 | 0/14 | khớp |


[mutations.json](224/mutations.json) lưu test, mã thoát, số đỏ/xanh và hash từng lần. **4/4 đột biến bắt buộc bị bắt**, đúng số Claude từng thử; hai bổ sung M5/M6 lọt và được ghi P2. Sau mỗi lần đều chép lại từ worktree, xác minh SHA-256 rồi chạy lại cùng test. Cuối cùng **329/329** nguồn khớp mốc, không thêm nguồn khác khi bỏ generated `node_modules/dist/tmp`: [tree-final.json](224/tree-final.json).

## 8. Phát hiện

**P0: 0; P1: 2; P2: 2; P3: 0.** P1 cần xử lý trước khi nhận G7 và đề xuất sửa trước commit. P2 là hồi quy có thể lọt test, mã gốc tương ứng hiện đang đúng.

| Mức / mã | file:dòng | Đầu vào → kết quả sai | Sửa đề xuất và test | Bằng chứng / giới hạn |
| --- | --- | --- | --- | --- |
| P1 / P1-01 | vite.config.ts:48 | VITE_PORTAL_URL vắng, import src/kit/learning/contract.ts?v=123 hoặc ?import (hoặc nạp vite.config.ts qua symlink) → Vite build mã 0, chunk vẫn export https://typing-game.local; plugin không báo việc transform bị bỏ qua. | Chuẩn hóa id trước so sánh: bỏ query, chuẩn hóa dấu phân cách và canonicalize đường thật của cả hai phía; tránh lowercase mù trên filesystem phân biệt hoa thường. Theo dõi contract đã được thay trong lượt build và dừng rõ nếu gói game không đi qua phép thay mong đợi. Giữ kit trên đĩa nguyên. Thêm Vite build thật với ?v=, ?import, cấu hình qua symlink; khẳng định origin rỗng/cấu hình đúng và thiếu transform làm build dừng. Giữ các ca 0/2 declaration và CRLF. | vite-probes.json: realBuilds.queryV, queryImport, symlinkConfig đều success=true/localHost=true; canonical localHost=false. Đồ thị không đi qua contract cũng build thành công; plugin chỉ có transform, không guard kết thúc. Build chuẩn hiện tại và ba deploy gốc đều đạt; deploy checker production vẫn bắt local-host nếu nó lọt ra gói. Đây là lỗ của bảo đảm build/plugin, chưa phải chứng cứ gói chuẩn hiện tại hỏng. |
| P1 / P1-02 | scripts/deploy/prune.mjs:8 | Đặt symlink đứt ở assets, assets/typing-defense, models, models/keep/link, .vite hoặc .vite/link → existsSync=false khiến script bỏ qua symlink, trả 0 và vẫn xóa file/thư mục khác; trái bảo đảm từ chối symlink trước mọi thay đổi. Cùng mẫu sai ở dòng 49. | Dùng lstatSync(path, { throwIfNoEntry: false }) hoặc lstat với catch chỉ ENOENT; kiểm isSymbolicLink trước quyết định đường không tồn tại, áp dụng cả assets/game ancestors. Hoàn tất kế hoạch và kiểm mọi nhánh trước ghi/xóa. Thêm dangling symlink ở models/.vite và sâu dưới chúng, cả assets và game; khẳng định mã 1, chẩn đoán symlink, dist và sentinel ngoài dist giữ nguyên. | prune-probes.json: 6 ca dangling trả 0 và dist_unchanged=false; ví dụ dangling-models-deep vẫn xóa models/. Sentinel ngoài dist không đổi trong cả 27 ca. Chưa thấy ghi/xóa ra ngoài dist trong probe; lỗi đã đo là bỏ sót từ chối symlink và tiếp tục thay đổi gói. |
| P2 / P2-01 | tests/deploy-prune.test.ts:94 | M5 vô hiệu hóa riêng chặn symlink ở dist/tổ tiên trong prune.mjs:37 → cả 11 test deploy-prune vẫn xanh, dù script cho phép dist qua symlink tổ tiên và có thể sửa đích ngoài đường truyền theo cú pháp. | Mở rộng fixture để gọi script qua dist symlink và một tổ tiên symlink tới thư mục sentinel; khẳng định từ chối trước thay đổi. M5 phải làm ít nhất một test mới đỏ; khi trả guard thì tất cả xanh. | mutations.json: M5 mutated 0 đỏ/11 xanh; restored 0 đỏ/11 xanh. Probe mã gốc chặn dist/ancestor đúng, nên đây là hở test, không phải lỗi đang có của guard này.  |
| P2 / P2-02 | tests/portal.test.ts:77 | M6 đổi learning.ts:27 thành createPortalBridge() ngay khi import → 14 test portal vẫn xanh. Test tên lazy singleton chỉ kiểm cùng object và parentOrigin, không kiểm thời điểm tạo. | Kiểm import module chưa đăng ký listener/chưa tạo bridge, lần gọi learningBridge đầu mới tạo một lần; reset module/env và kiểm cleanup để không phụ thuộc thứ tự test. M6 phải làm test thời điểm khởi tạo đỏ; giữ test bridge thật và gửi/nhận đúng origin hiện có. | mutations.json: M6 mutated 0 đỏ/14 xanh; restored 0 đỏ/14 xanh. Mã gốc hiện tại dùng null và ??=, thực sự lười.  |


## Cần trình duyệt của Claude

- Nhúng gói có `VITE_PORTAL_URL=https://typing-game.local/`: phím đầu tới game, requestFocus và sự kiện học tới portal; nhận nhạc/dataset từ đúng parent/origin, bỏ nguồn khác. Kiểm parent đã sẵn sàng trước khi bridge xả queue.
- Mở riêng không portal, rồi tải lại: queue giữ và không có tin ra ngoài; nhúng bản production không cấu hình cũng phải giữ queue.
- Gói production trên server tĩnh: đúng MIME/cache/base path, không 404, không request tới host khác hoặc repo cha; từ vựng ghim tải độc lập và không tải model thừa.
- Chơi tới màn kết, tải JSON có tên wordwoven-playtest; B9 nhận cả tên cũ/mới. Kiểm focus và vòng đời chunk Học trong trình duyệt thật. Phiếu này không chụp ảnh, không mở server/browser/mạng.

## 9. Dọn, bảo toàn và phạm vi

[integrity.json](224/integrity.json): trước/sau status khớp 208/status-final và HEAD nguyên; **329/329** hash bằng nhau; **37/37** hash bảo vệ; **14** mục node_modules và mtime **1** results.json không đổi. Lệnh find trước dọn ra **0** dòng: [worktree-newer.log](224/worktree-newer.log). `git diff --check` mã **0**. Không chạy node/pnpm với cwd worktree.

[cleanup.json](224/cleanup.json): `rm -rf games/typing-defense/tmp/codex-224` mã **0**, thư mục đã mất. Danh sách tmp checkout chính có thay đổi làn khác được liệt kê trong cleanup.json; thêm **0**, mất **1** mục khác. Mục khác thêm: `[]`; mất: `['codex-226']`. `codex-226` đã có trước và biến mất trong phiên; phiếu 224 không sửa hoặc xóa thư mục đó, không tính là lỗi của 224.

[scope.json](224/scope.json), [parent-before.txt](224/parent-before.txt), [parent-after.txt](224/parent-after.txt): status repo cha **1414→1555** dòng. **79** dòng mới của phiếu chỉ thuộc `docs/codex-queue/224-report.md` và `docs/codex-queue/224/…`. Các dòng khác xuất hiện/biến mất trong phiên được liệt kê riêng dưới đây; không sửa hoặc dọn chúng:

```text
?? docs/codex-queue/203/200-diff-before.json
?? docs/codex-queue/203/before.txt
?? docs/codex-queue/203/status-before.txt
?? docs/codex-queue/203/targeted.txt
?? docs/codex-queue/203/tests-first.txt
?? docs/codex-queue/220-report.md
?? docs/codex-queue/220/evidence/four-stage-repro.json
?? docs/codex-queue/220/evidence/parent-status-after.txt
?? docs/codex-queue/220/evidence/parent-status-changes.json
?? docs/codex-queue/220/evidence/summary-first-sha256.json
?? docs/codex-queue/220/evidence/summary-repro.json
?? docs/codex-queue/220/evidence/worktree-status-after.txt
?? docs/codex-queue/220/logs/summarize-before-last.txt
?? docs/codex-queue/220/logs/summarize-final.txt
?? docs/codex-queue/220/logs/summarize-repeat.txt
?? docs/codex-queue/220/logs/verification-before-cleanup.txt
?? docs/codex-queue/220/logs/verification-final.txt
?? docs/codex-queue/220/runs/x-f4-s1.err
?? docs/codex-queue/220/runs/x-f4-s1.json
?? docs/codex-queue/220/runs/x-f4-s1.md
?? docs/codex-queue/220/runs/x-f4-s101.err
?? docs/codex-queue/220/runs/x-f4-s101.json
?? docs/codex-queue/220/runs/x-f4-s101.md
?? docs/codex-queue/220/verification.json
?? docs/codex-queue/226-report.md
?? docs/codex-queue/226/cleanup-check.txt
?? docs/codex-queue/226/delete-list.txt
?? docs/codex-queue/226/execution-checks.json
?? docs/codex-queue/226/git-after.txt
?? docs/codex-queue/226/git-final.txt
?? docs/codex-queue/226/git-parent-after.txt
?? docs/codex-queue/226/patch-log.txt
?? docs/codex-queue/226/runs.sha256
?? docs/codex-queue/226/runs/base-balance160.err
?? docs/codex-queue/226/runs/base-balance160.md
?? docs/codex-queue/226/runs/base-g12x20.err
?? docs/codex-queue/226/runs/base-g12x20.md
?? docs/codex-queue/226/runs/base-night1-160.md
?? docs/codex-queue/226/runs/base-night1-40.md
?? docs/codex-queue/226/runs/base-pn-balanced.md
?? docs/codex-queue/226/runs/base-pn-challenge.md
?? docs/codex-queue/226/runs/base-pn-relax.md
?? docs/codex-queue/226/runs/base-smoke.err
?? docs/codex-queue/226/runs/base-smoke.md
?? docs/codex-queue/226/runs/commands.json
?? docs/codex-queue/226/runs/pkg-balance160.err
?? docs/codex-queue/226/runs/pkg-balance160.md
?? docs/codex-queue/226/runs/pkg-g12x20.err
?? docs/codex-queue/226/runs/pkg-g12x20.md
?? docs/codex-queue/226/runs/pkg-night1-160.md
?? docs/codex-queue/226/runs/pkg-night1-40.md
?? docs/codex-queue/226/runs/pkg-pn-balanced.md
?? docs/codex-queue/226/runs/pkg-pn-challenge.md
?? docs/codex-queue/226/runs/pkg-pn-relax.md
?? docs/codex-queue/226/runs/pkg-smoke.err
?? docs/codex-queue/226/runs/pkg-smoke.md
?? docs/codex-queue/226/runs/refs.txt
?? docs/codex-queue/226/runs/timeline.txt
?? docs/codex-queue/226/summary-repro.json
?? docs/codex-queue/226/summary.json
?? docs/codex-queue/226/summary.md
?? docs/codex-queue/226/tools/report.py
```

| Kiểm | Nội dung | Số đo | Kết quả |
| --- | --- | --- | --- |
| 1 | Worktree nguyên | 329/329 hash; 37/37 hash bảo vệ; HEAD/status khớp; find -newer=0; 14 mục node_modules + 1 results.json không đổi | Đạt |
| 2 | Bản chép | 329/329 ở cả hai bản; mỗi bản 11 symlink, node_modules là thư mục thật | Đạt |
| 3 | pnpm check cuối | 40 file / 414 xanh / 0 đỏ; kit 33; tsc/build qua; 79,60 / 81,16 kB khi biến vắng | Đạt |
| 4 | Golden | 2/2 same=true; 19.660 / 5.695 tick; 0 problems/rejected | Đạt |
| 5 | Gói/quét | Cả ba deploy mã 0; hai production 0 host nhà/GLB/models/.vite; local kiểm production đúng 1 local-host; 0 prefix game khác | Đạt ca chuẩn |
| 6 | Tách 170/208 | patch mã 0/12 file; 19 đường=14 sửa+5 mới; 3 before khớp; 37/380; 69 lỗi; 55 file; 54/55 hash; 1.206.837 byte (+1.500) | Đạt |
| 7 | Kit | 31/31 module commit cha; README và verifier sinh khớp; verifier 33/33 | Đạt |
| 8 | Đột biến | 4/4 bắt buộc đỏ rồi xanh; 2/2 bổ sung vẫn xanh, đã ghi P2; 329/329 nguồn trả lại | Đạt kiểm bắt buộc; phát hiện 2 hở test |
| 9 | Phát hiện | P0=0; P1=2; P2=2; P3=0; mỗi dòng có file:dòng, kịch bản, đề xuất/test | Đã ghi |
| 10 | Dọn/phạm vi | Bản chép không còn; tmp thêm 0/mất 1 mục khác; 79 dòng mới của 224 đều trong hai đường cho phép; thay đổi khác tách riêng | Đạt |


## Việc của Claude

1. Đọc P1-01/P1-02 và bổ sung ca test tái hiện trước; sửa plugin canonicalize/guard và lstat cho symlink đứt. Nên sửa luôn hai lỗ test P2-01/P2-02. Chạy check và ba gói lại sau sửa; không lấy inventory 224 làm số cho mã đã đổi.
2. Duyệt/commit **170 trước**, theo nền 19 đường và ba file `208/before/`; sau đó **208** theo `208/208-only.patch`, kèm các sửa P1 của phần 208. Phiếu 224 không thay lượt duyệt/commit của Claude và không chạy Git ghi.
3. C13 của làn L điền deploy-models từ STARTER/NIGHT_1 khi game dùng model. Repo cha truyền `VITE_PORTAL_URL=https://typing-game.local/` cho build:td và dev:td:app theo đúng hai dòng ở 208-report §5; sửa các mục tài liệu còn ghi VITE_PORTAL_ORIGINS. README có thể nói rõ danh sách model được đọc cạnh script, độc lập cwd, và `.env*` cũng tham gia Vite loadEnv.
4. Chạy các bước ở “Cần trình duyệt của Claude”, rồi cổng G7 trên server tĩnh. Chủ dự án cần xem hai kịch bản P1 và xác nhận focus/sự kiện học/queue trên portal thật; số kiểm tĩnh xanh chưa thay phần đó.

Script chạy lại từ gốc repo cha và thứ tự lệnh ở [224/README.md](224/README.md). Không tạo ảnh/âm; không sửa lỗi nguồn, không sửa các phiếu/bằng chứng 168/170/208 hoặc file làn.
