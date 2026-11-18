# Phiếu 208 · Wordwoven · Gói triển khai 0 lỗi

**Phần 170 vẫn chưa commit khi bắt đầu.** Worktree `games/.wt-td-codex` ở đúng nhánh `td-codex`, HEAD `f9abfd09987dadd519233c2f38692758d35cefca`; chỉ có đúng 19 đường của 170. Đã làm tiếp và giữ nguyên phần đó, không hoàn tác. Ba file giao nhau được chép trước khi sửa vào [208/before/](208/before/). Không chạy lệnh Git ghi.

Hoàn tất phần mã và kiểm được giao: production **69 → 0 lỗi**, demo nhà **0 lỗi**. `dist` bàn giao là production không cấu hình portal, **53 file / 1.167.750 byte**, không có model, `.vite/` hoặc chuỗi `typing-game.local`. Chờ Claude duyệt rồi commit.

## 1. Hai nhóm file và mốc đầu

Các đường dẫn sau tính từ worktree.

**Nhóm 170 có sẵn, 19 đường:**

- `docs/td/BUILD_1B.md`, `docs/td/PLAYTEST_1B.md`;
- `package.json`, `README.md`, `docs/changelog/2026-10-29-pack-and-kit.md`;
- `scripts/td/b9.ts`, `src/app/retry.ts`;
- `tests/td-b9.test.ts`, `tests/td-flow.test.ts`, `tests/deploy-pack.test.ts`;
- `src/kit/balance/bands.ts`, `gates.ts`, `index.ts`, `pace.ts`, `typist.ts`;
- `src/kit/kit-manifest.json`, `src/kit/tools/cdp-run.mjs`, `src/kit/tools/cdp-port.mjs`, `src/kit/tools/deploy/check-pack.mjs`.

**Nhóm 208, 12 đường:**

- Sửa chung với 170: `package.json`, `README.md`, `tests/deploy-pack.test.ts`.
- Sửa riêng: `src/app/learning.ts`, `vite.config.ts`.
- Tạo mới: `src/app/portal.ts`, `deploy-models.json`, `scripts/deploy/prune.mjs`, `tests/portal.test.ts`, `tests/portal-build.test.ts`, `tests/deploy-prune.test.ts`, `docs/changelog/2026-10-30-deploy-pack.md`.

Repo cha chỉ ghi báo cáo này và `docs/codex-queue/208/`. Các thay đổi của tác nhân khác trong repo cha được giữ nguyên. Không mở `.wt-td-1c` hay sửa worktree game khác; mẫu Dragonhold và báo cáo 187/207 chỉ đọc.

Trước sửa mã, chạy thật `pnpm deploy:pack`: mã **1**, **69 lỗi**, **55 file / 1.205.337 byte**. Sau đó chạy bộ kiểm `--json` trên chính gói đó: [pack-before.json](208/pack-before.json), [log build](208/deploy-pack-before.log). [dist-before.json](208/dist-before.json) có số byte và SHA-256 từng file. [before.json](208/before.json) lưu nhánh, HEAD, status và hash **34 file kit + 2 golden + 1 manifest model**.

Bản chép file chung: [package.json](208/before/package.json), [README.md](208/before/README.md), [deploy-pack.test.ts](208/before/tests/deploy-pack.test.ts). [208-only.patch](208/208-only.patch) tách đúng phần 208 khỏi nền 170 để Claude duyệt/gộp.

## 2. Sáu phần việc

1. **Mốc đầu:** đã lưu gói, JSON bộ kiểm, inventory và hash trước mã như mục 1. Đọc đủ 69 phát hiện của 170; baseline hiện tại khớp số đó.
2. **Test trước mã:** thêm test portal, Vite thật, lọc model và ca đóng gói manifest có GLB thiếu. Trên mã cũ: **34 đỏ / 8 xanh, 4 file** ([JSON](208/tests-before.json), [log](208/tests-before.log)). Lượt liên quan đầu sau sửa: **42/42 xanh** ([JSON](208/tests-after.json), [log](208/tests-after.log)); kiểm toàn bộ sau cùng ở mục 3.
3. **Nguồn portal lúc build:** `portalHome()` trong `src/app/portal.ts` nhận URL HTTP(S) tuyệt đối không có thông tin đăng nhập, mặc định `null`; URL sai dừng build với lỗi nêu `VITE_PORTAL_URL`. `createPortalBridge()` trong `learning.ts` dùng phần nguồn. Khi biến trống, luôn đưa kit host không có parent, kể cả host giả đang nhúng: giữ sự kiện cũ/mới trong hàng đợi, không gửi tin, không xả/xóa hàng đợi, `requestFocus()` trả `false`. Có biến thì gửi đúng nguồn, bỏ tin từ nguồn khác. Singleton vẫn khởi tạo lười. Plugin `wordwoven-portal-origin` thay đúng một khai báo `PARENT_ORIGIN` trong bộ nhớ; 0 hoặc 2 khai báo làm build dừng. Thay bằng callback để giữ nguyên ký tự `$&`. Kit trên đĩa nguyên byte; giữ `LAZY`, `chunkOf`, `manualChunks`, `port: 3006`. Không thêm nút về portal hoặc chữ người chơi thấy.
4. **Danh sách model và lọc:** `deploy-models.json` chứa `{ "models": [] }` cho `a2-days`. `prune.mjs <dist>` từ chối thư mục thiếu `index.html`; đọc danh sách cạnh script, chỉ ghi/xóa trong gói được truyền. Danh sách trống bỏ toàn bộ `models/`; có khóa giữ mọi tier theo URL đã bỏ query, giữ metadata và ghi manifest gói chỉ còn khóa chọn. Khóa lạ, URL ra ngoài hoặc symlink đều dừng trước ghi/xóa; không có model vẫn qua và dọn `.vite/`. In một dòng số file/byte bỏ và khóa giữ. Hai lệnh deploy chạy lọc sau build, trước bộ kiểm. Lệnh `build` giữ nguyên; không tải model hoặc nới bộ kiểm.
5. **Tài liệu:** README ghi cách dùng biến, production trống, demo nhà, danh sách model, bước lọc và lưu ý C13 cho làn L. Changelog tiếng Việt có số trước/sau. Không sửa tài liệu repo cha thuộc `docs/games/**`.
6. **Test xanh:** **42 test liên quan**, gồm URL trống/hợp lệ có đường dẫn/sai/credentials/giao thức khác; giữ hàng đợi khi bị nhúng; đúng nguồn gửi/nhận; Vite thật ở hai chế độ và demo nhà, chạy JS sinh ra trong Node; kiểm fallback, hash kit và khai báo 0/2; lọc trống/một khóa/khóa lạ/URL thoát/symlink/không model/thiếu index và bảo toàn `public/` fixture. Hai lệnh deploy được chạy với build giả có manifest trỏ GLB thiếu: đều mã 0 sau lọc, không còn model hoặc `.vite/`. Fixture trong `tmp/` tự xóa; **0 thư mục fixture còn lại**.

Lượt `pnpm check` đầu có **412 xanh / 2 đỏ** ở kiểm biên: nơi gọi kit chuyển sang `portal.ts`, và chuỗi import trong fixture bị bộ quét hiểu là ra ngoài repo ([log](208/check-first.log)). Đã đưa `createPortalBridge()` về `learning.ts` và tạo import fixture bằng đường tính từ root. Không sửa hoặc nới `boundary.test.ts`; lượt cuối toàn bộ xanh. Không có test thời gian đỏ nên không cần chạy riêng ba lần.

## 3. Tám mục kiểm

| # | Kiểm | Kết quả và bằng chứng |
| --- | --- | --- |
| 1 | `pnpm check` | Mã **0**, **12,297 s**, **40 file / 414 test xanh**, kit **33/33**; TypeScript và build qua. [Log](208/check.log), [lệnh](208/check-run.json). |
| 2 | `pnpm td:golden:check` | Mã **0**, **0,653 s**; ván thường **19.660 tick**, boss **5.695 tick**, cả hai **`same: true`**, 0 problem/rejected. [Log](208/golden.log). |
| 3 | Ngân sách trang | `/`: **79,60 → 79,60 kB gzip**; `/?title=0`: **81,07 → 81,30 kB**. Cả hai ≤ 85 kB; còn **5,40 / 3,70 kB**. Build thường vẫn có manifest model và `.vite`; giao thức cầu học có trong chunk Học `learn-8MpvuGcr.js`, không có trong entry `index-DMJ9g847.js`. [Bằng chứng build thường](208/build-only.json). |
| 4 | Production `pnpm deploy:pack` | Mã **0**, **2,290 s**, **0 lỗi**; **53 file / 1.167.750 byte**. Không còn `assets/typing-defense/models/` hoặc `.vite/`. Quét **21 file HTML/JS/CSS/JSON: 0 chuỗi `typing-game.local`**. [JSON kiểm](208/pack-after.json), [inventory có SHA-256](208/dist-after.json), [log](208/deploy-pack-after.log). |
| 5 | Demo nhà và kiểm chéo | `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local`: mã **0**, **2,522 s**, **0 lỗi** ([JSON](208/pack-local.json)). Kiểm production trên chính gói demo: mã **1**, đúng **1 `local-host`**, 0 lỗi khác ([JSON](208/pack-local-production.json)). Sau đó dựng lại production: mã **0**, **2,639 s**, inventory trùng từng byte/hash với gói ở mục 4 ([dist-final.json](208/dist-final.json), [pack-final.json](208/pack-final.json)). |
| 6 | Bảng trước/sau | **69 → 0 lỗi**, **55 → 53 file**, **1.205.337 → 1.167.750 byte**, giảm ròng **37.587 byte**. Chi tiết nguyên nhân ở bảng dưới. |
| 7 | Bảo toàn và whitespace | **37/37 hash khớp**: 34 file `src/kit/**` gồm manifest kit, 2 golden, 1 manifest model trong `public`. `git diff --check` mã **0**. [Hash sau](208/after.json), [xác minh](208/verification.json), [diff check](208/diff-check.txt). |
| 8 | Phạm vi cuối | HEAD không đổi; **28 đường = 19 của 170 + 9 mới của 208**, 3 đường dùng chung; 0 đường lạ, 0 đường 170 bị mất. [Status đầy đủ](208/status-final.txt), [phân nhóm và kiểm phạm vi](208/verification.json), [hai dòng package thay đổi](208/package-changes.json). |

| Nhóm | Trước | Sau | Vì sao hết lỗi |
| --- | ---: | ---: | --- |
| `local-host` | 1 | 0 | Portal mặc định trống; nguồn mặc định trong kit được thay trong bộ nhớ khi Vite biên dịch. |
| `missing-model` | 68 | 0 | Nhánh 2D không dùng model; danh sách trống bỏ manifest/model khỏi gói sau build. Không tải GLB để làm xanh. |
| Tổng | **69** | **0** | Bộ kiểm kit giữ nguyên byte và các điều kiện kiểm giữ nguyên. |

Bước lọc thực tế bỏ **2 file / 38.123 byte** (manifest model và manifest Vite). Mã JS mới tăng **536 byte**, nên gói giảm ròng 37.587 byte. Mốc này không có 19,8 MB GLB thừa như khảo sát cũ: toàn bộ 68 GLB trong manifest đã thiếu từ baseline. `vocabularyNotShipped: 95` vẫn là thông tin của gói ghim level 1–5, không phải lỗi; `external: []` trước/sau.

Hai dòng `package.json` của game sau 208, để gộp riêng với `td-1c` và `td-keys`:

```json
"deploy:pack": "pnpm build && node scripts/deploy/prune.mjs dist && node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense",
"deploy:pack:local": "pnpm build && node scripts/deploy/prune.mjs dist && node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense --allow-local-host"
```

## 4. Phần không làm

Không sửa luật chơi, golden, kit, `public/` hay media; không chạy `kit:sync`, `media:pull`, dev server, trình duyệt hoặc mạng. Không chạy build/test của game khác. Không sửa package/nginx/tài liệu thiết kế của repo cha hoặc Tu Tiên. Không thêm ảnh/âm thanh; không có capture cần dọn. Phiếu chứng minh gói tĩnh và hành vi bằng fixture/JS Vite, chưa chứng nhận G7 bằng server và trình duyệt vì phiếu cấm các bước đó.

Giữ nguyên cơ chế xả hàng đợi hiện có của kit khi **đã cấu hình portal**; bắt tay `hello` và chỉ xóa sau `ack` thuộc phần kit riêng trong tài liệu triển khai độc lập, không thuộc phiếu này.

## 5. Việc của Claude

1. Duyệt phần 208 bằng `208-only.patch`, đối chiếu bản `before/` để tách ba file giao 170; sau đó commit. File `deploy-models.json` và các nguồn mới đang là untracked vì phiếu cấm mọi lệnh Git ghi.
2. Ở **C13**, làn L (`td-1c`) điền `deploy-models.json` từ **`STARTER` và `NIGHT_1`** trong `scripts/td/media-budget.mjs` của làn đó. Phiếu 208 không mở hay sửa `.wt-td-1c`.
3. Repo cha cần truyền **`VITE_PORTAL_URL=https://typing-game.local/`** cho `build:td` và `dev:td:app` để cổng nhà tiếp tục nhận focus và sự kiện học. Đề xuất thay đúng hai giá trị script sau, giữ các biến HMR hiện tại:

```json
"build:td": "bash scripts/game-dir.sh require typing-defense && VITE_PORTAL_URL=https://typing-game.local/ pnpm --dir games/typing-defense build",
"dev:td:app": "bash scripts/game-dir.sh require typing-defense && cd games/typing-defense && VITE_PORTAL_URL=https://typing-game.local/ DEV_HOST=127.0.0.1 DEV_ALLOWED_HOSTS=td.typing-game.local DEV_HMR_HOST=td.typing-game.local DEV_HMR_PROTOCOL=wss DEV_HMR_CLIENT_PORT=443 pnpm dev"
```

4. Cập nhật những chỗ còn dùng tên cũ **`VITE_PORTAL_ORIGINS`**: `docs/games/DEPLOY_INDEPENDENCE.md` **§9, §11** và `docs/games/MAP1_PRODUCTION.md` **§2.2 A9**. Thống nhất `VITE_PORTAL_URL`, mặc định production trống, thay vì danh sách nguồn và mặc định nguồn nhà của tài liệu cũ. Các file repo cha này được giữ nguyên theo phạm vi phiếu.
