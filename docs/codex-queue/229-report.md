# Phiếu 229 · Wordwoven · Sửa các phát hiện kiểm lại 224

**Đã xử lý đủ P1-01, P1-02, P2-01 và P2-02.** `pnpm check`: **41 file / 439 test xanh**, kit **33/33**, TypeScript/build qua. Production và bản nhà đều **0 lỗi**. Sáu đột biến đều làm test mới đỏ; trả mã thì xanh. Không commit; phần 170/208 chưa commit được giữ nguyên ngoài bốn file cần sửa của phiếu này.

Bằng chứng ở [229/](229/). Các đường `tệp:dòng` bên dưới tính từ `games/.wt-td-codex`. Dùng skill `game-ci-resumable` cho mốc Git/phạm vi và `threejs-qa-release` cho kiểm gói; không chạy phần trình duyệt của skill vì phiếu cấm.

## 1. Điều kiện đầu và phạm vi

- Đủ `224-report.md`, `170-report.md`, `208-report.md`; đã đối chiếu §8 của 224, hai phiếu gốc và báo cáo của chúng.
- Nhánh **`td-codex`**, HEAD **`f9abfd09987dadd519233c2f38692758d35cefca`**, giữ nguyên đến cuối. [Status trước](229/status-before.txt): đúng **28/28 đường** trong `224/paths.json`, không có đường lạ.
- [before.json](229/before.json) lưu status, HEAD và **328 SHA-256** trước sửa. `pnpm check` trước sửa chạy mới, mã **0**, **12,417 s**, **40 file / 414 test**, kit **33/33**, TypeScript/build qua: [log](229/check-before.log), [lệnh](229/check-before-run.json).
- Môi trường: macOS arm64, Node **24.22.0**, pnpm **11.21.0**; log thực tế ghi Vite **7.3.7**, Vitest **3.2.7**. Mọi lệnh pnpm chạy trong worktree, tắt kiểm phụ thuộc trước khi chạy; không install, server, trình duyệt hoặc mạng.

**Phần chênh của 229, đúng sáu đường được phép:**

- Sửa: `vite.config.ts`, `scripts/deploy/prune.mjs`, `tests/deploy-prune.test.ts`, `tests/portal.test.ts`.
- Thêm: `tests/portal-id.test.ts`, `docs/changelog/2026-10-30-fix-224-findings.md`.

`src/app/learning.ts` chỉ được thay tạm cho phép thử M6 và khôi phục đúng byte; không có thay đổi bàn giao. Repo cha chỉ ghi báo cáo này và thư mục `229/`.

## 2. Test đỏ trước mã, bản sửa và test xanh

Viết toàn bộ test mới trước khi sửa mã. [red-P1.log](229/red-P1.log): **19 đỏ / 31 xanh, 3 file**; gồm **7 đỏ portal**, **12 đỏ symlink đứt**, còn **15 test portal xanh**. Sau đó chạy riêng M5/M6 trên mã chưa sửa P1 để tái tạo hai lỗ hổng test, lưu [red-mutations.json](229/red-mutations.json). Mỗi lần thay mã đột biến đều có `finally` khôi phục byte và đối chiếu SHA-256.

| Phát hiện | Test đỏ tái tạo | Bản sửa, vị trí cuối | Test xanh |
| --- | --- | --- | --- |
| **P1-01** | `tests/portal-id.test.ts:11`: build Vite thật với `?v=123`, `?import`, đường contract qua symlink giữ nguyên id và cấu hình qua symlink, ở cả biến vắng/có URL. Trước sửa, **6 ca query/id symlink đỏ** vì còn `typing-game.local`; thêm **1 ca đỏ** khi đồ thị không đi qua contract. [Log đỏ](229/red-P1.log). | `vite.config.ts:40`: bỏ query, chuẩn hóa dấu phân cách, `realpath` id; `:52`–`:53`: canonicalize cả root/contract, không lowercase. `:62` reset dấu đã thay; `:64` so đường thật; `:73` dừng build chưa thay contract. Giữ kiểm đúng một khai báo, `LAZY`, `chunkOf`, `manualChunks`, port 3006. | **10/10** test mới xanh: 8 build biến thể, 1 chặn thiếu transform, 1 CRLF. Chạy JS đầu ra bằng Node và kiểm origin thực, kit contract nguyên byte. Các ca 0/2 khai báo và build chuẩn của `portal-build.test.ts` vẫn xanh trong check toàn bộ. |
| **P1-02** | `tests/deploy-prune.test.ts:103`: **12 đỏ** = 6 vị trí × danh sách trống/một khóa. Vị trí: `assets`, `assets/typing-defense`, `models`, `models/keep/link`, `.vite`, `.vite/link`; hai đường `models` tính dưới `assets/typing-defense`. Mã cũ trả **0** thay vì **1**. | `scripts/deploy/prune.mjs:6`: `lstatSync(..., { throwIfNoEntry: false })`, không dùng `existsSync`; `:11` kiểm symlink trước khi duyệt; `:52` kiểm cả hai tổ tiên; `:60`, `:74` dùng cùng cách đọc mục. Vẫn hoàn tất kiểm trước mọi ghi/xóa. | **12/12** ca symlink đứt xanh; đều mã **1**, báo `symlink`, snapshot nội dung/link của dist và sentinel ngoài dist nguyên. `snapshot` ở `tests/deploy-prune.test.ts:7` dùng `readlinkSync`, không theo link đứt. |
| **P2-01** | `tests/deploy-prune.test.ts:118`: truyền `dist` qua symlink trực tiếp và qua tổ tiên symlink. M5 nguyên bản của 224 làm **2 đỏ**, [log](229/red-mutation-M5.log). | Sửa test/fixture ở `tests/deploy-prune.test.ts:15`, `:38`, `:118`: cho truyền đường đích khác, kiểm mã 1/chẩn đoán, gói thật, sentinel và link không đổi. Giữ guard đúng sẵn có ở `scripts/deploy/prune.mjs:40`. | Trả guard: **2/2 xanh**, [log](229/red-restored-M5.log). Không cần sửa hành vi guard. |
| **P2-02** | `tests/portal.test.ts:82`: reset module/env, bọc hàm tạo bridge thật bằng spy và dùng window giả có listener. M6 nguyên bản của 224 làm **1 đỏ** ngay sau import, [log](229/red-mutation-M6.log). | `tests/portal.test.ts:95`: import chưa tạo bridge/chưa đăng ký listener; lần gọi đầu mới tạo đúng một lần, lần sau cùng object, đúng origin; `:105` dispose mọi bridge đã tạo, kiểm gỡ listener và dọn mock/global/module. `learning.ts:27` giữ `null`. | Trả khởi tạo lười: **1/1 xanh**, [log](229/red-restored-M6.log). Giữ các test bridge thật và gửi/nhận đúng nguồn có sẵn. |

[green-focused.log](229/green-focused.log): **3 file / 50 test xanh**, mã **0**. Ca chỉ nạp cấu hình qua symlink đã xanh trước sửa trên bộ công cụ Mac này; khác kết quả probe của 224. Ca giữ id contract qua symlink thực sự đỏ trước sửa và được phép thử bỏ `realpath` bắt lại, nên không lấy ca cấu hình vốn xanh làm bằng chứng tái tạo lỗi.

## 3. Năm mục kiểm bắt buộc

| # | Lệnh / kiểm | Kết quả mới và bằng chứng |
| --- | --- | --- |
| **1** | `pnpm check` trước/sau | **40/414 → 41/439**, tăng đúng **25 test** (10 portal id, 12 symlink đứt, 2 tổ tiên/dist, 1 singleton). Sau mã **0**, **12,640 s**, kit **33/33**, TypeScript/build qua. [Log sau](229/check-after.log), [lệnh](229/check-after-run.json). Không có lỗi thời gian cần chạy riêng ba lần. |
| **2** | `pnpm deploy:pack` khi biến vắng; `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local` | Cả hai mã **0**, **0 lỗi**, **53 file**. Production **1.167.486 byte**; bản nhà **1.167.801 byte**. [JSON production](229/pack-production.json), [JSON bản nhà](229/pack-local.json), [inventory production](229/dist-production.json), [inventory bản nhà](229/dist-local.json). Cả hai bỏ **2 file / 38.123 byte**, không còn models hoặc `.vite`. Production quét **21 file văn bản**, không còn host nhà. Kiểm production trên bản nhà trả mã **1**, đúng **1 lỗi `local-host`**, không lỗi khác: [JSON kiểm chéo](229/pack-local-production.json). Dựng lại production, **53/53 byte và hash khớp gói production đầu**: [inventory cuối](229/dist-final.json), [JSON cuối](229/pack-final.json). |
| **3** | `pnpm td:golden:check` | Mã **0**, **0,597 s**. Ván thường **19.660 tick**, boss **5.695 tick**; cả hai **`same: true`**, **0 problem/rejected**. [Log](229/golden.log). Hai file golden giữ nguyên SHA-256. |
| **4** | Chạy lại M5/M6 và đột biến P1 | **6/6 bị bắt**, chi tiết mục 4. Mọi lượt đột biến mã **1**, mọi lượt khôi phục mã **0**; hash được kiểm trước khi tiếp tục. [Danh sách phép thay](229/final-mutations.json), [số đỏ](229/mutation-counts.json). |
| **5** | Status sau và phạm vi chênh | [status-after.txt](229/status-after.txt): **30 đường = 28 có sẵn + 2 mới**. So **328 hash trước / 330 hash sau**: chỉ **4 file sửa + 2 file mới** kể trên, không mất file cũ; **37/37 hash bảo vệ** (34 kit, 2 golden, 1 manifest model) khớp. HEAD/nhánh nguyên; `git diff --check` mã **0**. [Xác minh](229/verification.json), [hash sau](229/after.json), [whitespace](229/diff-check.txt). |

Ngân sách production giữ **79,60 / 81,16 kB gzip**, bản nhà **79,60 / 81,31 kB**, đều ≤85 kB. Số byte production khớp ca **biến vắng** của 224; mốc **1.167.750 byte** trong 208 là ca biến trống, không dùng làm mốc cho biến vắng. Giữ nguyên thông tin **95 level từ vựng không ghim**, không coi là lỗi; `external: []` ở cả hai gói.

## 4. Đột biến sau sửa

Các lệnh đều có dạng `pnpm exec vitest run <tệp> -t <tên ca>`; đầy đủ argv/cwd/env/mã thoát/thời gian nằm trong từng `final-*-run.json`. Dùng riêng các ca mới để xác nhận chúng bắt hồi quy, không dựa vào test cũ.

| Đột biến | Phần bị bỏ hoặc thay | Test mới đỏ | Sau khôi phục |
| --- | --- | ---: | ---: |
| **M5** | Vô hiệu riêng guard symlink ở dist/tổ tiên, đúng phép thay của 224 | **2** | **2 xanh** |
| **M6** | `let bridge = createPortalBridge()` ngay khi import, đúng phép thay của 224 | **1** | **1 xanh** |
| **P1-01-query** | Bỏ tách `?` trước `realpath` | **4** | **8 xanh** |
| **P1-01-realpath** | Trả đường cú pháp thay đường thật | **2** | **8 xanh** |
| **P1-01-guard** | Bỏ chặn build chưa thay contract | **1** | **1 xanh** |
| **P1-02** | Cho `existsSync` lọc trước `lstat`, bỏ sót link đứt | **12** | **12 xanh** |

Ở hai đột biến chuẩn hóa id, build dừng tại guard chưa transform, khiến các ca yêu cầu build thành công đỏ. Đây là bằng chứng test bắt mất chức năng; guard vẫn ngăn chunk có origin cũ lọt qua. Tất cả phép thay đã được hoàn trả; build production cuối chạy sau đột biến.

## 5. Phần không làm và chủ dự án cần xem

- Chờ **Claude kiểm trình duyệt theo mục “Cần trình duyệt của Claude” của 224**: iframe/focus/học/nhạc, queue khi tải lại, MIME/cache/request độc lập, tải JSON chơi thử và vòng đời chunk Học. Phiếu 229 cấm server/trình duyệt/mạng, nên không chứng nhận G7 thực tế.
- Chủ dự án/Claude xem sáu file của 229 và báo cáo này cùng phần 170/208 trước khi quyết định commit. Phiếu không chạy lệnh Git ghi; không sửa các việc repo cha và làn khác đã giao cho Claude.
- Không sửa kit, sim, luật chơi, golden, public, kit cha hoặc Tu Tiên. Không sinh ảnh/âm thanh vì phiếu chỉ sửa mã/test đóng gói; không có capture cần dọn. Fixture mới tự xóa trong `finally`, cuối phiên **0 thư mục `portal-id-*` / `deploy-prune-*` còn lại**.

Các script tái lập và log chỉ ở `229/`: `run.py` chạy lệnh có ghi cwd/env; `mutate.py` thay tạm và trả byte; `release.py` kiểm hai gói và dựng trả production; `verify.py` đối chiếu hash/phạm vi. Mỗi script đột biến dùng chuỗi đích duy nhất và dừng nếu nguồn khác; không dùng để chép đè công việc mới hơn.
