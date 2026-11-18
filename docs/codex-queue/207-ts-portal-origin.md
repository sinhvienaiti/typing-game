# Phiếu 207 · Last Line · Nguồn cổng game là biến build, bản phát hành không còn `typing-game.local`

**Nguồn:**
- Báo cáo 168 §3: `pnpm deploy:pack` báo lỗi `local-host`, và đó là **lỗi thật ở production**. `src/app/learning.ts:18` tạo cầu nối học mà không truyền nguồn. Kit dùng mặc định `https://typing-game.local` (`src/kit/learning/contract.ts:22`; `bridge.ts:115`, gửi tin ở `:292`). Claude đã kiểm lại trên `ts-codex`: đúng.
- `docs/games/DEPLOY_INDEPENDENCE.md` §9 "Nguồn portal là biến build", bước A; bảng Tuyến Cuối, dòng 7.
- `docs/games/MAP1_PRODUCTION.md`, cổng G7 (build tự đứng).
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

Phiếu này là nửa Last Line của việc chung "nguồn cầu nối học". Nửa Wordwoven là phiếu 208. Không trùng 111, 111b (bộ kiểm gói), 168 (lệnh `deploy:pack`), 187 (Dragonhold).

**Mẫu:** phiếu 187 (Dragonhold), `docs/codex-queue/187-report.md` §2. Mã mẫu, chỉ đọc: `games/.wt-dh-codex/vite.config.ts`, `src/app/portal.ts`, `tests/portal-build.test.ts`, `tests/app/portal.test.ts`. Nếu Claude đã gộp 187 thì đọc cùng các file đó ở `games/dragon-hold`.

**Báo cáo:** `docs/codex-queue/207-report.md` (tiếng Việt), thư mục `docs/codex-queue/207/`. Cả hai ở repo cha, không ở trong worktree.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-ts-codex`, nhánh `ts-codex`. Chạy sau phiếu 205 (cùng làn, cùng nhánh). Lệnh git và báo cáo chạy từ gốc repo cha; lệnh `pnpm` chạy trong worktree.
- Trước khi làm, chạy `git -C games/.wt-ts-codex status --short -uall` và `git -C games/.wt-ts-codex branch --show-current`:
  - sạch: làm tiếp;
  - chỉ có file của 205 vì Claude chưa commit (đối chiếu `docs/codex-queue/205-report.md`): làm tiếp, ghi danh sách vào báo cáo. Trước khi sửa một file mà 205 cũng sửa, chép nó vào `207/before/` để Claude tách hai phần;
  - có file khác, hay nhánh không phải `ts-codex`: dừng, ghi vào báo cáo.
- Được dùng git chỉ đọc. Test trước, mã sau. Chú thích tiếng Anh.
- Chữ người chơi thấy là tiếng Anh; phiếu này không đổi chữ nào.
- Luật chơi, ván vàng `tests/golden/s0-trace.json` và mã băm bộ bài `7f073fa2` không đổi.

## Việc

1. **Mốc đầu.**
   - Ghi HEAD và trạng thái git.
   - Chạy `pnpm deploy:pack` trên mã chưa sửa. Rồi chạy `node src/kit/tools/deploy/check-pack.mjs dist --game typing-survival --json` trên chính `dist` đó; lưu JSON thuần vào `207/pack-before.json` (như 187, không trộn log build).
   - Ghi file, offset và ngữ cảnh của mỗi chuỗi `typing-game.local` trong `dist` vào `207/local-host-before.json`.
2. **Biến build `VITE_PORTAL_URL`**, cùng tên và cùng luật với 187. Không dùng `VITE_PORTAL_ORIGINS` như §9 ghi; Claude sửa tài liệu sau.
   - Giá trị là một URL HTTP(S) tuyệt đối. URL sai, sai giao thức hay có user/password thì build dừng, lỗi nói rõ tên biến.
   - **Trống hay không đặt:** cầu nối không gửi `postMessage` nào, kể cả khi game bị nhúng trong iframe. Sự kiện học nằm lại hàng đợi cục bộ: không xả, không xóa.
   - Nguồn rỗng không bao giờ tới `postMessage` (trình duyệt ném lỗi với `""`). 187 dùng một host không có `parent` cho trường hợp này; làm như vậy.
   - **Có giá trị:** cầu nối dùng phần nguồn của URL (`https://portal.example/learn/?x=1` → `https://portal.example`). Hành vi kit hiện có giữ nguyên.
3. **Một chỗ tạo cầu nối.**
   - Theo 187: `portalHome()` và `createPortalBridge()` trong một file mã game (ví dụ `src/app/portal.ts` mới).
   - `src/app/learning.ts` tạo cầu nối qua hàm này; vẫn nhận `host` truyền vào để test.
   - Cầu nối đang được giữ ở mức module (`bridge ??=`). Cho test một cách tạo lại cầu nối; không đổi hành vi lúc chơi.
4. **Thay fallback của kit lúc build.** Bài học 187: chỉ truyền `parentOrigin` ở nơi gọi vẫn để chuỗi kit trong bundle.
   - Plugin trong `vite.config.ts`, `enforce: "pre"`, chỉ xử lý `src/kit/learning/contract.ts`.
   - Thay khai báo `export const PARENT_ORIGIN = …;` bằng nguồn của `VITE_PORTAL_URL`, hay `""` khi biến trống.
   - Đọc biến bằng `loadEnv` của Vite theo `mode`.
   - Số khai báo khác đúng một: build dừng (`this.error`), không bỏ qua.
   - Phép thay chạy trong bộ nhớ. File kit trên đĩa giữ nguyên byte; `verify-kit` vẫn qua.
   - Nếu 205 đã sửa `vite.config.ts`, giữ nguyên phần của 205.
5. **README** của game:
   - bản phát hành: `pnpm deploy:pack`, không đặt biến;
   - bản demo nhà: `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local`;
   - biến đang có trong môi trường thì tắt rõ: `VITE_PORTAL_URL= pnpm deploy:pack`;
   - `--allow-local-host` không tự đặt biến;
   - bỏ câu "Bản production còn bị chặn bởi nguồn portal …".
6. **Changelog** `docs/changelog/<ngày>-portal-origin.md` trong game: đổi gì, vì sao, số đo trước và sau.
7. **Chỗ repo cha cần đặt biến** (chỉ đọc, Claude sửa). Liệt kê trong báo cáo, kèm số dòng:
   - `package.json`: `build:survival`, `build:local`, `dev:survival:app`;
   - `play.sh`: mục Tuyến Cuối.

   Không đặt biến ở đó thì Play và dev ở máy nhà giữ sự kiện học trong hàng đợi, không gửi về portal.

## Test (viết trước, ghi số đỏ trước khi sửa mã)

1. `portalHome`: trống, chỉ khoảng trắng, URL hợp lệ có đường dẫn và query, chuỗi không phải URL, `ftp:`, URL có user/password.
2. Biến trống, host giả **có** `parent`: `reportWord` không gọi `postMessage`. Hàng đợi có đủ sự kiện, `gameId` là `typing-survival`.
3. Biến có giá trị, host giả có `parent`: `postMessage` nhận đúng `https://portal.example`, không phải `typing-game.local`.
4. Test build, như `tests/portal-build.test.ts` của 187: Vite build trong bộ nhớ (`write: false`), chạy JS sinh ra trong Node.
   - Không đặt biến: không có chuỗi `typing-game.local`; `parentOrigin` của cầu nối là `""`.
   - Đặt biến: `parentOrigin` là nguồn của biến.
   - `contract.ts` trên đĩa giữ nguyên byte.
5. Hàm thay khai báo: 0 hay 2 khai báo thì báo lỗi; đúng 1 thì thay đúng.
6. `tests/learning.test.ts` hiện có vẫn xanh.
7. Fixture ở `tmp/` của game, tự xóa sau test. Dùng `vi.stubEnv`, gỡ sau mỗi test.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy `kit:sync`.
- Dev server, trình duyệt, mạng.
- Tạo file `.env*` đặt `VITE_PORTAL_URL`.
- Nới hay sửa bộ kiểm gói `check-pack.mjs` để làm xanh.
- Thêm nút "Back to portal": Last Line không có nút đó. Phiếu này chỉ đổi cầu nối học.
- Làm bắt tay `hello`/`ack` (§9 bước B): đó là việc kit riêng.
- Sửa `src/app/main.ts`, `src/app/input.ts`, `src/view/type-fx.ts`, `src/audio/**`: phiếu 191 đang sửa các file đó ở `.wt-ts-typefx`.
- Sửa repo cha (`package.json`, `play.sh`, `docs/games/**`).
- Đụng game khác, worktree khác (`.wt-ts-typefx`, `.wt-dh-*`, `.wt-td-*`), Tu Tiên. Tạo media.

## Kiểm (ghi số)

1. `pnpm deploy:pack`, không cờ, không biến: **0 lỗi `local-host`**.
   - Có 205 trong cây: **0 lỗi tổng**.
   - 205 chưa vào cây: chỉ còn lỗi `foreign-asset` cũ; ghi rõ.
   - JSON bộ kiểm lưu `207/pack-after.json`.
2. Quét mọi file HTML, JS, CSS, JSON trong `dist` của mục 1: **0** chuỗi `typing-game.local`. Lưu `207/production-bundle.json` (file, byte, SHA-256).
3. `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local` vẫn đạt: có 205 thì 0 lỗi; chưa có thì chỉ lỗi `foreign-asset` cũ. JSON lưu `207/pack-local.json`.
4. Dựng lại bản production không biến, để `dist` bàn giao là bản phát hành. Ghi số file và byte của `dist` trước và sau.
5. `pnpm check` xanh: số file test, số test, số file `verify-kit`. Ván vàng `s0-trace` giữ SHA-256. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
6. Test liên quan: số đỏ trước sửa, số xanh sau sửa; log trong `207/`.
7. `git status --short -uall`: chỉ file của việc này (mã, test, README, changelog), cộng file 205 nếu Claude chưa commit. `git diff --check` mã 0.

**Xong khi:** bảy việc và bảy mục kiểm đạt, có số trong báo cáo. Claude duyệt rồi commit; sửa script repo cha và §9; gộp với 191 (khác file, thứ tự gộp ghi trong báo cáo).
