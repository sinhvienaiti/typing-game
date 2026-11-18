# Phiếu 233 · Kiểm lại độc lập sau sửa 228 và 229

Ngày 30/10/2026 · Mac mini M4/macOS · Chỉ đọc hai cây mã nguồn.

**228 chưa nên commit: F2 sửa thiếu, còn một phát hiện P1 về mẫu nhập từ sao lưu.** F3–F5 sửa đúng trong các ca đã thử; F7 vẫn chưa sửa. **229 commit được trong phạm vi kiểm mã, test và gói của phiếu này**, sau lượt duyệt của Claude. Không có phát hiện mới ở Wordwoven; phần kiểm G7 bằng trình duyệt/server của 224 vẫn dành cho Claude.

Phát hiện mới: **P0 = 0, P1 = 1, P2 = 0**. Không sửa mã hoặc các báo cáo cũ; không chạy Git ghi.

## 1. Điều kiện, mốc và cách chạy

Đủ `228-report.md`, `229-report.md`; đã đọc hai phiếu sửa, báo cáo và các ca gốc trong 227/224. Lúc kiểm đầu, cả `233/`, `233-report.md` và `games/typing-defense/tmp/codex-233/` chưa có. [preflight.json](233/preflight.json) lưu mốc:

| Cây | Nhánh | HEAD |
| --- | --- | --- |
| Repo cha | `feat/space-typing-admin-uiux` | `3c52f79e95a98cfb89f4a5689f8dc58d2e21f74d` |
| `games/.wt-td-codex` | `td-codex` | `f9abfd09987dadd519233c2f38692758d35cefca` |

[before.json](233/before.json) lưu status, **338 SHA-256** nguồn/phụ trợ repo cha trong vùng kiểm và **331 SHA-256** Wordwoven. Bản chép khớp **338/338** và **331/331**: [copy.json](233/copy.json). Số 331 gồm 330 file của mốc sau 229 và ảnh `public/assets/typing-defense/ui/title-dusk.webp` bị Git bỏ qua; không phải thêm mã mới sau 229.

HEAD repo cha đã mới hơn `20ef5e3` mà 228 ghi **trước lúc chụp mốc 233**. Đã kiểm lại nguồn hiện tại với mốc sau 228: **186/186 hash khớp**, nên không lấy HEAD cũ làm bản đang được kiểm. HEAD đầu/cuối 233 giữ nguyên.

- Portal/shared chạy Node test trực tiếp ở repo cha, theo quyền của phiếu. Build portal và test validator chạy trong `tmp/codex-233-portal/`.
- Validator thực tế tạo fixture `tmp/validate-play-mode-test/`, nên chạy bản chép để không ghi ra ngoài vùng cho phép. Không sửa nội dung test.
- Mọi lệnh pnpm của Wordwoven chạy trong `games/typing-defense/tmp/codex-233/tree/`. Chép đủ `public/`; `node_modules` là thư mục thật, **11 symlink** tới phụ thuộc có sẵn, bỏ các mục cache theo 224. `TMPDIR` nằm dưới cây tạm; luôn có `pnpm_config_verify_deps_before_run=false`.
- Không install, sync kit, chạy media, dev server, trình duyệt hoặc mạng; không đọc/sửa cây Tu Tiên. Không chạy build hay test trong worktree gốc.

## 2. Bảng kiểm từng phát hiện

Các dòng Wordwoven tính từ `games/.wt-td-codex`. “Đỏ → xanh” là số test ở lượt tắt sửa rồi trả nguyên byte; mỗi lần đều kiểm hash khôi phục. Log/lệnh ở [parent-mutations.json](233/parent-mutations.json), [td-mutations.json](233/td-mutations.json), [mutation-counts.json](233/mutation-counts.json).

| Phát hiện | Kết luận và vị trí hiện tại | Tái tạo gốc, biến thể bổ sung | Đột biến chạy lại |
| --- | --- | --- | --- |
| **227-F2** | **Sửa thiếu.** Phép chiếu năm trường ở `shared/learning/query.mjs:278` bỏ trường dư trực tiếp, nhưng chưa kiểm kiểu giá trị. | 9 test gốc xanh. Thêm 6 ca đủ 8 mẫu, cả ba loại thực thể × lookup/query: trường dư lồng dưới `extra` bị bỏ đúng. Tuy nhiên **10/10** ca đặt object chứa câu trả lời vào một trong năm trường hợp lệ vẫn gửi object đó; xem P1-233-01. | Bỏ đúng phép chiếu như 228: **9 đỏ → 9 xanh**, khớp 228. |
| **227-F3** | **Sửa đúng** tại `portal/src/learning/bridge.ts:174`, `:198`; chỉ trả mã `query-failed`. | Ca gốc lỗi đọc kho và version riêng tư đều hết. Thêm 6 ca lookup/query ném object không phải Error, Error có cause, thông điệp rất dài: đều chỉ có mã lỗi, đúng requestId/origin. | Trả `errorText(error)` như 228: **4 đỏ/1 xanh → 5 xanh**, khớp. |
| **227-F4** | **Sửa đúng** tại `shared/learning/query.mjs:294`, `:303`, bridge `:188`. | Ca 100 ligature và dấu tổ hợp của 227/228 đều xanh. Thêm id dài đúng 200 trước NFKC, mở rộng đến 600; trim/dedup; 198 ligature kèm dấu tổ hợp; id 201 bị chặn trước đọc kho: **4/4 xanh**. | Cho bridge parse lại: **2 đỏ/2 xanh → 4 xanh**, khớp. |
| **227-F5** | **Sửa đúng** tại `portal/src/game-card.ts:30`, `:44`. | Các đường gốc không còn được nhận. Thêm **27/27** ca từ chối: `%2f`, `%2F`, `%5c`, `%5C`, độ sâu mã hóa 1–6, dấu `\` thô; mỗi ca kiểm icon/cover và ba dạng appUrl. Giữ lựa chọn chặt hơn của 228. | Bỏ đúng kiểm mới: **16 đỏ/3 xanh → 19 xanh**, khớp. |
| **224-P1-01** | **Sửa đúng** tại `vite.config.ts:40`, `:52`, `:64`, `:73`. | 10 test mới của 229 cùng các build query gốc đều xanh. Thêm **6 build Vite thật**: query kèm hash, hai cấp symlink, hai cấp symlink kèm query/hash; mỗi dạng với biến vắng/có URL chứa port/path/query/hash. Thực thi JS đầu ra bằng Node: origin đúng; kit nguyên byte. | Bỏ tách query: **4 đỏ → 8 xanh**; bỏ realpath: **2 đỏ → 8 xanh**; bỏ guard cuối build: **1 đỏ → 1 xanh**. Khớp 229. |
| **224-P1-02** | **Sửa đúng** tại `scripts/deploy/prune.mjs:6`, `:11`, `:52`. | 12 ca gốc link đứt xanh. Thêm **12/12** ca ở assets/game/models/.vite và sâu dưới cây, danh sách rỗng/một khóa, link tương đối trỏ tới đích không tồn tại **ngoài dist**. Mã 1, báo symlink; toàn bộ snapshot, thư mục rỗng, link và sentinel ngoài dist giữ nguyên. | Cho existsSync lọc trước lstat: **12 đỏ → 12 xanh**, khớp. |
| **224-P2-01** | **Đã khép lỗ test** tại `tests/deploy-prune.test.ts:118`; guard `prune.mjs:40` vẫn đúng. | Hai ca dist/tổ tiên gốc xanh; thêm chuỗi tổ tiên qua **hai link tương đối**, từ chối trước thay đổi, snapshot nguyên. | M5 nguyên bản: **2 đỏ → 2 xanh**, khớp. |
| **224-P2-02** | **Đã khép lỗ test** tại `tests/portal.test.ts:82`, `:95`; `src/app/learning.ts:27` vẫn là null. | Test gốc kiểm đúng thời điểm tạo. Thêm **2/2** ca import đồng thời, biến trống/có URL: chưa gọi factory/listener/postMessage khi import; lần dùng đầu mới tạo một bridge; cleanup listener đầy đủ. | M6 nguyên bản: **1 đỏ → 1 xanh**, khớp. |
| **227-F7** | **Chưa sửa**, đúng bàn giao của 228. | Kiểm lại độc lập vẫn có **15 dòng** trailing whitespace; danh sách bên dưới. | Không có bản sửa để tắt; không sửa log cũ. |

Tổng **10/10 đột biến bị bắt**, các lượt khôi phục đều xanh và khớp SHA-256. Ca gốc đã sửa của 228: **37/37 xanh** sau khôi phục. Các biến thể mới: repo cha **43 xanh / 10 đỏ** trong 53 ca; Wordwoven **21/21 xanh**. Mười ca đỏ đều thuộc cùng một phát hiện F2, không phải mười lỗi độc lập.

Bằng chứng bổ sung: [parent-probe.mjs](233/parent-probe.mjs), [parent-variants-final.log](233/parent-variants-final.log), [td-variants.test.ts](233/td-variants.test.ts), [td-variants-final.log](233/td-variants-final.log).

## 3. Phát hiện mới

| Mức / mã | Tệp:dòng | Đầu vào → kết quả sai | Đề xuất sửa và kiểm |
| --- | --- | --- | --- |
| **P1 / P1-233-01 · F2 còn thiếu** | `shared/learning/query.mjs:278`–`:283`; điểm nhận dữ liệu `shared/learning/profile-backup.mjs:48`–`:59`; kiểu hợp đồng `shared/learning/core.d.mts:4`–`:10` | Tạo hồ sơ vocabulary hợp lệ bằng `applyLearningEvents`, thay `recentSamples[0].gameId` bằng `{userAnswer:"PRIVATE_NESTED_USER_ANSWER",expectedAnswer:"PRIVATE_NESTED_EXPECTED_ANSWER"}`. `parseLearningProfileBackup(JSON.stringify(profile))` vẫn nhận. Gửi lookup hoặc query qua `ParentLearningBridge.handleMessage`, đúng iframe/origin → query-result chứa nguyên hai câu trả lời bên trong `recentSamples[0].gameId`. Cả năm trường mẫu đều tái hiện được, hai đường tin mỗi trường: **10/10 đỏ**. | Kiểm kiểu giá trị của cả năm trường, chỉ dựng mẫu đúng hợp đồng với giá trị nguyên thủy. Chặn hoặc bỏ mẫu không hợp lệ ở đường trả dữ liệu để bảo vệ cả hồ sơ đã lưu; có thể bổ sung kiểm riêng recentSamples khi nhập backup. Không chỉ lọc trường dư ở cấp đầu, không đổi chính sách recentMistakes/recentAnswers. Thêm test backup và stored profile với object/array trong từng trường, qua cả lookup/query; ca trên phải hết chứa dữ liệu riêng tư và mẫu trả ra đúng kiểu. |

Đây là dữ liệu JSON được đường nhập hiện tại chấp nhận, không dùng getter/prototype hay vòng tham chiếu. Không chứng minh vượt origin: tin vẫn chỉ gửi đúng iframe được đăng ký. Lỗi là chưa bảo đảm hợp đồng mẫu và chưa ngăn câu trả lời lồng trong giá trị trường đi ra khung game. Phiếu 233 chỉ báo, không sửa.

## 4. Hồi quy và gói

| Kiểm | Số sau sửa trong 228/229 | Đo lại 233 | Kết quả |
| --- | --- | --- | --- |
| Portal, 3 file | 109/109 | **109/109**, mã 0 | Khớp |
| Shared learning, 13 file | 89/89 | **89/89**, mã 0 | Khớp |
| Validator play-mode | 94/94 | **94/94**, mã 0, bản chép | Khớp; tổng ba bộ **292/292** |
| CLI validate-play-mode | PASS | **PASS**, mã 0 | Khớp, không cần nginx |
| Wordwoven `pnpm check` | 41 file / 439 test, kit 33/33 | **41 / 439 / 0 lỗi**, kit **33/33**, tsc/Vite/budget qua | Khớp |
| Golden Wordwoven | 2 ván, 19.660 / 5.695 tick | **2/2 same=true**, đúng tick, 0 problems/rejected | Khớp, SHA giữ nguyên |
| Portal build | 149 file; JS 4.980.038; CSS 127.854 byte | **149 file; JS 4.979.988; CSS 127.854**, tsc/Vite mã 0 | JS **−50 byte**, giải thích giới hạn bên dưới |
| Production Wordwoven, biến vắng | 53 file / 1.167.486 byte / 0 lỗi | **53 / 1.167.486 / 0 lỗi** | **53/53 byte và hash khớp 229** |
| Bản nhà, URL `https://typing-game.local/` | 53 / 1.167.801 / 0 lỗi | **53 / 1.167.801 / 0 lỗi** | **53/53 byte và hash khớp 229** |
| Bộ kiểm production trên bản nhà | 1 lỗi local-host | **Mã 1, đúng 1 lỗi local-host**, 2 chuỗi trong 1 file | Khớp kiểm âm tính |

[td-check.log](233/td-check.log), [td-golden.log](233/td-golden.log), [pack-comparison.json](233/pack-comparison.json) giữ số mới. Cả hai gói Wordwoven không còn models/.vite hoặc GLB/GLTF/BIN; chỉ prefix `/assets/typing-defense/`, 0 prefix game khác; `external: []`. Production quét **21 file văn bản, 0 host nhà**. Ngân sách production **79,60 / 81,16 kB gzip**, bản nhà **79,60 / 81,31**, khớp 229, đều dưới 85 kB.

Prune ở bản chép bỏ **2 file / 39.623 byte**, so với **38.123 byte** của 229: chênh **1.500 = 60 × 25**, do đường tương đối trong manifest Vite tới phụ thuộc thật dài hơn, đúng mô tả dựng bản chép của 224. File đó bị bỏ trước kiểm gói; gói cuối khớp hash toàn bộ.

Portal: JS chính **611.289** so với **611.339** của 228; 146/149 mục inventory giữ nguyên byte/hash. Hai JS đổi tên hash và index.html đổi tham chiếu. Đã build thêm với đúng bố cục outDir của 228, vẫn cùng số byte. Đã dựng bản trước 228 bằng chín file có hash cũ khớp mốc: JS chính **610.888 → 611.289**, tổng JS **4.979.587 → 4.979.988**, vẫn tăng đúng **401 byte**; CSS tăng **0**. [portal-delta.json](233/portal-delta.json), [bundle-comparison.json](233/bundle-comparison.json). Nguồn trong mốc sau 228 khớp **186/186**; chưa xác định chính xác nguyên nhân khác 50 byte khi build tại cây sao chép, nên **không ghi là khớp tuyệt đối inventory 228** hoặc suy ra hồi quy chức năng chỉ từ chênh này.

## 5. Phạm vi của hai phiếu sửa và F7

[scope-review.json](233/scope-review.json) đối chiếu độc lập:

- **228:** 186 hash trước/sau cho **9 file đổi, 177 giữ nguyên**; chín đường trong `task.diff` đúng chín đường đó, đều thuộc vùng được giao. Đảo diff theo tọa độ dòng cho hash cũ **9/9 khớp**; nguồn hiện tại khớp mốc sau **186/186**. Changelog mới đúng đường được phép; báo cáo/bằng chứng chỉ ở 228. Bốn file xuất hiện đồng thời ngoài vùng trong status lịch sử khớp phần đã công khai của 228: ba `203/budget-iteration-{3,4,5}.txt` và `222/attribution.json`; không gán chúng cho diff sửa của 228.
- **229:** mốc **328 → 330** cho đúng **4 file sửa + 2 file mới**, không mất file: `vite.config.ts`, `scripts/deploy/prune.mjs`, `tests/deploy-prune.test.ts`, `tests/portal.test.ts`; thêm `tests/portal-id.test.ts`, `docs/changelog/2026-10-30-fix-224-findings.md`. Cả sáu được phiếu 229 cho phép. Nguồn hiện tại khớp mốc sau **330/330**. Không có thay đổi bàn giao ở `src/app/learning.ts`, kit, sim hoặc golden.

Kiểm phạm vi lịch sử dựa trên snapshot và diff đã lưu; không thể suy từ status đơn thuần tác nhân nào ghi file ngoài vùng. Phần mã thay của cả hai phiếu đều khớp danh sách cho phép.

**F7 để Claude sửa trước commit log:** `docs/codex-queue/216/tests-before.txt` dòng **124, 134, 136, 137, 139, 1208, 1210, 1229, 1231, 1250, 1252, 1271, 1273, 1292, 1294**. `git diff --no-index --check` mã **3**, đúng **15** thông báo. [f7.json](233/f7.json), [f7-read-only.log](233/f7-read-only.log). Đường 216 không được 228 hoặc 233 sửa, nên giữ nguyên.

## 6. Bảo toàn, dọn và bàn giao

[integrity.json](233/integrity.json), hai cặp `parent-status-{before,after}.txt` / `td-status-{before,after}.txt`:

- Repo cha: **338/338** hash giữ nguyên; HEAD/nhánh giữ nguyên. Status toàn repo **1.842 → 1.996 dòng**, không giống hệt: thêm **75 dòng** đầu ra 233; ngoài ra thêm **86**, mất **7** dòng bằng chứng đồng thời ở các làn **223, 230, 231**. Danh sách đầy đủ ở `integrity.json`; không có nguồn portal/shared/validator/nginx thay đổi. Không sửa/xóa việc làn khác để ép status. Vì vậy điều “không có thay đổi mới” đạt cho nguồn được kiểm và phần do 233 làm, **không đạt nếu hiểu là toàn bộ status repo phải bằng nhau**.
- Worktree: **331/331** hash giữ nguyên; status **30 → 30 đường**, giống hệt; HEAD/nhánh giữ nguyên; **37/37** file kit/golden/manifest được bảo vệ giữ nguyên. **14** mục node_modules và mtime results.json không đổi; **0** mục mới hơn marker. Bản chép được trả về cùng hash nguồn trước dọn.
- `git diff --check` nguồn repo cha và worktree đều mã **0**. F7 là log chưa theo dõi nên được kiểm riêng bên trên.
- [cleanup.json](233/cleanup.json): đã xóa đúng `tmp/codex-233-portal/` và `games/typing-defense/tmp/codex-233/`, xác nhận không còn; không dọn thư mục của tác nhân khác. Trong tmp của game có thêm **`codex-231`** của làn khác, không có mục khác mất. Không lưu dist/media vào báo cáo; không có capture cần prune.

Các lỗi lần chạy đầu do cách dựng bằng chứng được giữ log: bản chép portal thiếu nguồn import kiểu từ Space Typing, validator thiếu `play.sh`; bổ sung đúng file từ cây gốc rồi chạy xanh. Probe F4 đầu dùng uppercase làm ligature nở vượt giới hạn đầu vào, đã đổi sang biến thể trim/dedup hợp lệ. Probe Wordwoven đầu thiếu ngoặc đóng, đã sửa script kiểm và chạy **21/21**. BSD patch đảo diff không có ngữ cảnh chỉ khớp **8/9** do thứ tự hai hunk sát nhau; bộ đảo theo tọa độ kiểm lại **9/9** hash gốc. Không tính các lỗi dựng công cụ đo này là lỗi sản phẩm; kết luận dùng log `*-final` hoặc `*-retry` đã ghi ở trên.

**Claude cần xem:** P1-233-01 và sửa F2 trước khi nhận 228; bỏ khoảng trắng F7 khi đưa log vào commit. Với 229, duyệt sáu file trên rồi quyết định commit cùng chuỗi 170/208; giữ các bước iframe/focus/học/queue, MIME/cache/request độc lập và tải JSON chơi thử trong mục “Cần trình duyệt của Claude” của 224. Phiếu này không chứng nhận các bước trình duyệt đó. F1/F6 của 227 vẫn ngoài phạm vi, không được suy là đã giải quyết.

Không làm ảnh/âm, vì phiếu chỉ kiểm mã/test/gói. Không sửa mã, game docs, Audio Lab, media, kit hoặc Tu Tiên; không commit/push/reset/clean/stash.
