# Phiếu 228 · Sửa các phát hiện kiểm lại 227 của 214–216

Ngày 30/10/2026 · Repo cha · Mac mini M4/macOS · Node v24.22.0.

Hoàn tất **F2–F5** với test đỏ trước mã, test xanh sau mã và đột biến
riêng từng bản sửa. **F7 không sửa** vì log nằm ngoài vùng được ghi của
phiếu này. Claude duyệt trước khi commit; phiên này chỉ dùng Git đọc.

## Điều kiện đầu vào và phạm vi

Đủ `227-report.md`, `214-report.md`, `215-report.md`, `216-report.md`.
Nhánh đúng `feat/space-typing-admin-uiux`; HEAD đầu
`20ef5e30b19cd9afbeb28dabec825b8fec59d665`.
Đối chiếu cả ba phiếu gốc, báo cáo, danh sách file và các ca tái tạo ở
§«Phát hiện, từ nặng tới nhẹ» của 227 trước khi viết test.

[preflight.txt](228/preflight.txt) lưu lệnh/đầu ra nhánh và status hẹp;
[status-before.txt](228/status-before.txt) lưu toàn bộ
`git status --short -uall`. Trong `portal`, `shared/learning`, `infra/nginx`
và hai file validator có **21 file bẩn đã biết, 0 file lạ**. Danh sách
máy đọc được ở [preflight.json](228/preflight.json), đối chiếu danh sách
214/215 và bốn file của 216. File bẩn ngoài các vùng này không phải điều
kiện dừng và không bị sửa bởi 228.

Chỉ sửa **9 file mã/test**, liệt kê ở
[product-files.txt](228/product-files.txt), cộng changelog mới, báo cáo
này và `228/`. [task.diff](228/task.diff) chỉ chứa phần thay đổi của 228,
không trộn diff cũ của 214–216. Bản trước dùng để dựng diff đã được kiểm
SHA-256 khớp mốc đầu của cả chín file; xem
[hashes-before.json](228/hashes-before.json) và `reconstruct-diff.py`.

## Từng phát hiện

| Phát hiện | Test đỏ trước mã | Sửa và dòng hiện tại | Test xanh | Đột biến riêng |
|---|---|---|---|---|
| **F2** | **9/9 đỏ**, mã 1; [f2-red.txt](228/f2-red.txt) | `shared/learning/query.mjs:273`: dựng `recentSamples` bằng đúng năm trường ở `:278`; lookup mặc định `[]` rồi dùng item đã lọc ở `:316`. | **9/9 đạt**, mã 0; [f2-green.txt](228/f2-green.txt) | Bỏ riêng phép chiếu năm trường: **9 đỏ**, mã 1; [f2-mutation.txt](228/f2-mutation.txt). |
| **F3** | **5/5 đỏ**, mã 1; [f3-red.txt](228/f3-red.txt) | `portal/src/learning/bridge.ts:174`, `:198`: chỉ gửi mã `query-failed`. `shared/learning/message-contract.mjs:92` và `.d.mts:56`: cho phép bỏ `message`. | **5/5 đạt**, mã 0; [f3-green.txt](228/f3-green.txt) | Cho hai handler gửi lại `errorText(error)`: **4 đỏ, 1 xanh**, mã 1; [f3-mutation.txt](228/f3-mutation.txt). |
| **F4** | **3 đỏ, 1 xanh sẵn**, mã 1; [f4-red.txt](228/f4-red.txt) | `shared/learning/query.mjs:294`: hàm đầu vào thô parse một lần; hàm nhận kết quả đã parse ở `:303`, khai báo `query.d.mts:19`. Portal dùng hàm đó ở `portal/src/learning/bridge.ts:188`. | **4/4 đạt**, mã 0; [f4-green.txt](228/f4-green.txt) | Cho portal gọi lại hàm parse đầu vào thô: **2 đỏ, 2 xanh**, mã 1; [f4-mutation.txt](228/f4-mutation.txt). |
| **F5** | **16 đỏ, 3 xanh sẵn**, mã 1; [f5-red.txt](228/f5-red.txt) | `portal/src/game-card.ts:30`: giải mã lặp, từ chối dấu phân cách mã hóa ở mỗi lớp; kiểm chuỗi cuối và tiền tố URL đã chuẩn hóa ở `:44`. | **19/19 đạt**, mã 0; [f5-green.txt](228/f5-green.txt) | Bỏ riêng kiểm mới, trở về kiểm URL cũ: **16 đỏ, 3 xanh**, mã 1; [f5-mutation.txt](228/f5-mutation.txt). |

Tổng **37 test mới**, lượt đỏ trước mã có **33 lỗi**, **4 xanh sẵn**.
Mỗi nhóm đều được chạy đỏ trước khi sửa mã tương ứng. Đột biến chạy
lần lượt, mỗi lần chỉ tắt một bản sửa; `finally` trả lại file, kiểm byte
và SHA-256. [mutation.json](228/mutation.json) lưu số và hash khôi phục.
Lượt cuối sau khôi phục: **37/37 đạt**, mã 0,
[restored-green.txt](228/restored-green.txt).

### F2 · Mẫu nhập từ sao lưu và mẫu đã lưu

Test `portal/tests/learning-lookup.test.mjs:195` dựng hồ sơ thật bằng
`applyLearningEvents`, thêm `PRIVATE_USER_ANSWER`, `PRIVATE_EXPECTED_ANSWER`
và trường dư vào mẫu, nhập bằng `parseLearningProfileBackup(JSON.stringify(...))`,
rồi đi qua `handleMessage` từ đúng iframe/origin. Kiểm cả `lookup` và
`query`, cả vocabulary/grammar/sentence: tin ra không có các giá trị
riêng tư đó; `recentSamples` chỉ còn đúng năm trường; hồ sơ nguồn không đổi.
Test trực tiếp hồ sơ đã lưu ở `shared/learning/lookup.test.mjs:132` kiểm
cùng ba loại thực thể.

Lọc ở hàm dựng item chung để tin query cũ cũng không chuyển nguyên mẫu
có trường dư. Không cần từ chối bản sao lưu hoặc xóa dữ liệu đã nhập;
`profile-backup.mjs` giữ nguyên. Không đổi `recentMistakes`, `recentAnswers`,
công thức, bộ đếm hay phiên bản hồ sơ.

### F3 · Lỗi đọc kho và hồ sơ hỏng

Test `portal/tests/learning-lookup.test.mjs:215` phủ hai nhánh lookup/query,
với cả `load()` ném `Error('PROFILE_SECRET: unrequested-word / private answer')`
và hồ sơ có `version: 'PRIVATE_PROFILE_VALUE'`. Tin ra chỉ có type,
requestId và `error: { code: "query-failed" }`; không chuyển exception,
giá trị version hoặc hồ sơ. Không đưa chi tiết lỗi vào log mới của portal.
Test hợp đồng ở `shared/learning/lookup.test.mjs:144` kiểm tin chỉ mã và
khả năng giữ thông báo công khai khi caller truyền rõ `message`.

### F4 · NFKC và dấu tổ hợp

Test qua portal ở `portal/tests/learning-lookup.test.mjs:238` có ba id:
`"ﬃ".repeat(100)` (100 → 300 ký tự),
`"ﬃ".repeat(99) + "e\u0301"` (101 → 298 ký tự),
và `"Cafe\u0301"` (dấu tổ hợp → `café`). Hồ sơ thật có bản ghi cho id
đã chuẩn hóa; cả ba đều trả `query-result`, đúng id, đúng một lần đọc kho.
Ca dấu tổ hợp đơn đã xanh trước sửa; hai ca mở rộng tái tạo lỗi 227.
Test shared ở `shared/learning/lookup.test.mjs:151` kiểm kết quả đầu vào
thô/đã parse giống nhau và đầu vào thô 201 ký tự vẫn bị từ chối.

Không đổi quy tắc giới hạn: tối đa 200 ký tự **sau trim, trước NFKC**,
đúng 215. `lookupParsedLearningRecords` dành cho kết quả từ
`parseLearningLookup`; cổng tin vẫn kiểm toàn bộ đầu vào trước đọc kho.

### F5 · Giải mã đường ảnh và lựa chọn chặt hơn

18 đường từ chối ở `portal/tests/game-card.test.mjs:200` gồm các tổ hợp
227 đã thử (`%2e%2e/`, `%2E%2E/`, `%2F/`,
`%2e%2e%2F%2e%2e%2Fspace-typing/portal/icon.png`), cùng `%5C`, chữ hoa/thường,
trộn slash/backslash, mã hóa hai lần, trộn độ sâu và mã hóa ba lần.
Có thêm query/fragment mã hóa hai lần và mã phần trăm hỏng. Mỗi ca kiểm
độc lập icon/cover, ở cả ba kiểu appUrl của 227: origin thường, URL có
`/play/session/`, origin viết hoa. Test an toàn ở `:229` giữ được
`a%20b.png`, `%69con.png`, `a%2520b.png`; test cũ giữ đường chuẩn.

227 chưa chốt tác động nginx của ca dấu phân cách mã hóa. Theo yêu cầu
228, **chọn từ chối** mọi `%2F`/`%5C` ở mọi lớp, kể cả `a%2Fb.png` vốn
vẫn nằm trong tiền tố. Giải mã đến ổn định, chặn thành phần không hợp lệ,
kiểm prefix trên chuỗi đã giải mã và URL chuẩn hóa; URL trả về vẫn giữ
đường gốc đã qua kiểm. Không cần chờ xác nhận nginx để áp dụng luật chặt
này. Chưa chạy HTTP/nginx thật, nên không tuyên bố tác động phục vụ file.

### F7 · Không nằm trong vùng ghi

`docs/codex-queue/216/tests-before.txt:124` cùng 14 dòng khác vẫn có
khoảng trắng cuối dòng. Kiểm chỉ đọc
`git diff --no-index --check /dev/null docs/codex-queue/216/tests-before.txt`
trả **mã 3, 15 thông báo trailing whitespace**;
[f7-read-only.txt](228/f7-read-only.txt) giữ chẩn đoán, bỏ khoảng trắng
cuối dòng trong chính bản chép log mới. Vùng được ghi của 228 chỉ cho
báo cáo và thư mục **228/**, không cho **216/**; vì vậy không sửa log cũ,
không có lượt xanh hay đột biến F7. Claude cần bỏ khoảng trắng trước commit.

## Kiểm bắt buộc và byte gói

Mọi lệnh chạy từ gốc repo. Pnpm dùng
`pnpm_config_verify_deps_before_run=false`, phụ thuộc có sẵn, không cài gói
hay truy cập mạng. `run.py` lưu argv/cwd/mã thoát/thời gian vào JSON cùng
tên với log TXT; TXT bỏ khoảng trắng cuối dòng, không bỏ chẩn đoán.

| Kiểm | Trước | Sau | Bằng chứng trong `228/` |
|---|---:|---:|---|
| Portal, 3 file test | **77/77**, mã 0 | **109/109**, mã 0 | `portal-before.{txt,json}`, `portal-after.{txt,json}` |
| Shared learning, 13 file test | **84/84**, mã 0 | **89/89**, mã 0 | `learning-before.{txt,json}`, `learning-after.{txt,json}` |
| `node --test scripts/validate-play-mode.test.mjs` | **94/94**, mã 0 | **94/94**, mã 0 | `nginx-before.{txt,json}`, `nginx-after.{txt,json}` |
| Build portal gồm TSC và Vite | Mã **0**, 149 file | Mã **0**, 149 file | `build-before.{txt,json}`, `build-after.{txt,json}` |
| `node scripts/validate-play-mode.mjs` | — | **PASS**, mã 0, không cần nginx | `validate-after.{txt,json}` |
| `pnpm learning:check` | — | Mã **0** | `learning-check.{txt,json}` |
| Đột biến F2–F5 | — | **4/4 bị test phát hiện** | `mutation.json`, `f*-mutation.{txt,json}` |

Trước dùng `node --test` trực tiếp ba file `portal/tests`; sau dùng
`pnpm portal:test`, cùng tập ba file. Tổng ba bộ: **255 → 292 test**,
không lỗi/bỏ qua. Không sửa hay chạy test game.

Chạy đúng script build của 214, thêm lựa chọn đầu ra cô lập:

```sh
pnpm --dir portal build --configLoader runner --outDir ../docs/codex-queue/228/build-before --emptyOutDir
pnpm --dir portal build --configLoader runner --outDir ../docs/codex-queue/228/build-after --emptyOutDir
```

`--configLoader runner` tránh sinh `.vite-temp`; hai thư mục build chỉ
nằm trong vùng 228, đã xóa sau khi giữ danh sách byte/SHA-256. Không ghi
`portal/dist`. Test validator tự tạo fixture riêng dưới
`tmp/validate-play-mode-test/` theo test sẵn có và tự dọn; không sửa test
hay giữ fixture ở đó. Không còn thư mục fixture sau kiểm.

| Byte | Trước | Sau | Chênh |
|---|---:|---:|---:|
| JS chính | 610.938 | 611.339 | **+401** |
| Tổng 7 JS, gồm worker/worklet | 4.979.637 | 4.980.038 | **+401** |
| CSS chính/tổng | 127.854 | 127.854 | **0** |

[bundle-bytes.json](228/bundle-bytes.json) có chi tiết bảy JS;
`bundle-before-files.json`, `bundle-after-files.json` giữ số byte/hash
149 file mỗi bản. Cảnh báo chunk >500 kB có ở cả trước/sau, không mở rộng
phiếu sang chia gói. Không giữ bản build hoặc media trong thư mục báo cáo.

## Phạm vi cuối và việc bàn giao

Changelog mới: `docs/changelog/2026-10-30-fix-227.md`.
[status-after.txt](228/status-after.txt) lưu `git status --short -uall`
sau làm; [scope.json](228/scope.json) đối chiếu status và hash vùng kiểm.
Kiểm khoảng trắng mã/test và mọi file mới của 228 ở
[whitespace.json](228/whitespace.json); không đổi nhánh hoặc HEAD.

So với mốc đầu, có bốn file mới ngoài vùng của 228 do công việc đồng
thời: `docs/codex-queue/203/budget-iteration-3.txt`,
`docs/codex-queue/203/budget-iteration-4.txt`,
`docs/codex-queue/203/budget-iteration-5.txt`,
`docs/codex-queue/222/attribution.json`. Không sửa/xóa các file đó để ép
status. Vì vậy chênh status **toàn repo** không chỉ gồm 228; phần do 228
sửa/tạo nằm hoàn toàn trong vùng cho phép. Đối chiếu hash vùng kiểm:
**9 file đổi đúng danh sách, 177 file giữ nguyên**, không có file đổi
ngoài vùng được giao. `scope.json` giữ riêng chênh status của việc đồng
thời để Claude kiểm. Nhánh và HEAD đầu/cuối giống nhau.


F1 (16 lỗi cũ cả bộ Audio Lab) và F6 (nhãn nguồn release 217) **chờ
Claude quyết, không sửa**. F8 không sửa theo chỉ dẫn. Claude còn duyệt
mã/changelog, xử lý F7 ngoài vùng của 228 và kiểm trình duyệt/HTTP ở lượt
được phép trước khi nghiệm thu đầu cuối. Không mở server, browser, mạng,
không cài/reload nginx; không sửa game, Tu Tiên, Audio Lab, media, kit,
chỉ mục changelog hoặc báo cáo cũ. Không tạo ảnh/âm vì phiếu này không có
hạng mục media. Không commit, push, reset, clean hoặc stash.
