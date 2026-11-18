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
