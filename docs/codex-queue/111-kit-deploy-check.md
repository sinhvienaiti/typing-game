# Phiếu 111 · Kit · Bộ kiểm gói deploy `check-pack.mjs` (cổng G7)

**Vì sao:** cổng production G7 của map 1 đòi bản build tự đủ: không có đường dẫn sang repo cha, sang game khác hay sang `*.typing-game.local`; đủ file từ vựng và model mà gói trỏ tới; không lọt media riêng tư. Thiết kế ở `docs/games/DEPLOY_INDEPENDENCE.md` §11 (bảng "Kiểm của `deploy:pack`"). Phiếu này viết riêng bộ kiểm, thuần Node, để cả ba game dùng chung qua kit. Claude nối nó vào từng game sau.

**Báo cáo:** `docs/codex-queue/111-report.md`, và thư mục `docs/codex-queue/111/`.

## Luật chung (phiếu mã)

- **cwd và nơi làm:** repo cha `/Users/toandx/htdocs/typing-game`, thư mục `shared/game-kit/tools/deploy/` (mới).
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:**
  - sửa bản chép kit trong game (`games/*/src/kit/**`);
  - chạy `kit:sync`;
  - sửa file ngoài danh sách dưới đây;
  - dev server, trình duyệt; mạng;
  - đụng Tu Tiên.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chỉ dùng thư viện chuẩn của Node.

**Chỉ được ghi:**
- `shared/game-kit/tools/deploy/check-pack.mjs` (mới);
- `shared/game-kit/tools/deploy/check-pack.test.mjs` (mới, `node:test`);
- `shared/game-kit/DRIFT.md`: thêm một mục ngắn. Giữ mọi mục khác, kể cả mục của phiếu 102 và 107;
- báo cáo và `docs/codex-queue/111/`.

## Việc

**1. API:** `checkPack(dir, { gameId, budgets? })` → `{ ok, problems: [{ code, path, detail }], report: { files, bytes, external: [...] } }`.

**2. CLI:** `node shared/game-kit/tools/deploy/check-pack.mjs <thư mục gói> --game <id> [--json]`. Thoát 0 khi đạt, 1 khi có lỗi, 2 khi sai tham số. Không có `--json` thì in mỗi lỗi một dòng.

**3. Kiểm (mỗi kiểm một `code` cố định):**
- `file-too-big`: một file lớn hơn 25 MiB.
- `too-many-files`: từ 20.000 file trở lên.
- `private-media`: có đường chứa `local-assets/`, `art-src/`, `shared/music`, `Dota-Sounds`; hoặc có file `.DS_Store`.
- `foreign-asset`: trong file `.html`, `.js`, `.css`, `.json`, có chuỗi `/assets/<id>/` với `<id>` khác `gameId`, lấy từ danh sách id: `space-typing`, `dragon-hold`, `typing-defense`, `typing-survival`, `immortality-cultivation`.
- `local-host`: có chuỗi `typing-game.local`.
- `parent-path`: có `"../` hay `'../` đứng ngay trước `assets/`, `vocabulary/` hoặc `shared/`.
- `missing-vocabulary`: có `vocabulary/index.json` mà một `levels[].file` trong đó không có file. Có `vocabulary/vocab-manifest.json` thì sha256 từng file phải khớp, lệch thì cũng là lỗi này.
- `missing-attribution`: có thư mục `vocabulary/` mà không có `vocabulary/ATTRIBUTION.md`.
- `missing-model`: mỗi `manifest.json` dưới `assets/<gameId>/models/` có `models` (dạng như kit: mục có `tiers.high.url`, `tiers.medium.url`); url nào trỏ tới file không có trong gói là lỗi. Url tương đối thì tính từ thư mục của manifest.

**4. Báo cáo, không chặn:**
- `report.external`: các nguồn ngoài (`http://` hay `https://` với host bất kỳ), **trừ** `www.w3.org` (chuỗi namespace của SVG và XML) và `typing-game.local` (đã là lỗi), mỗi host một lần kèm số lần gặp;
- `report.bytes`: tổng cỡ;
- `report.files`: số file.

**5. Test** trên thư mục giả tạo trong `os.tmpdir()`, mỗi kiểm một ca đỏ và một ca xanh:
- gói sạch: `index.html`, `assets/index-abc123.js`, `vocabulary/{index.json, levels/001.json, ATTRIBUTION.md, vocab-manifest.json}`, `assets/<id>/models/manifest.json` với hai GLB giả;
- rồi lần lượt làm hỏng từng thứ: thêm `/assets/space-typing/` vào js; thêm `typing-game.local`; xóa một level; đổi một byte level; xóa ATTRIBUTION; xóa một GLB; thêm `art-src/x.png`; thêm `.DS_Store`; một file 26 MiB (tạo bằng `ftruncate`, không ghi dữ liệu thật);
- chuỗi `http://www.w3.org/2000/svg` trong js không phải lỗi và không vào `external`.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `node --test shared/game-kit/tools/deploy/check-pack.test.mjs`: xanh, ghi số ca.
2. `node --check shared/game-kit/tools/deploy/check-pack.mjs`.
3. **Chạy thật, chỉ đọc**, trên ba bản build có sẵn:
   - `games/.wt-ts-codex/dist` với `--game typing-survival`;
   - `games/.wt-dh-codex/dist` với `--game dragon-hold`;
   - `games/typing-defense/dist` với `--game typing-defense`, nếu có.

   Không build lại, không sửa gì trong game. Ghi đầu ra của mỗi lần chạy vào `docs/codex-queue/111/`, kèm nhận xét lỗi nào là thật, lỗi nào là báo nhầm. Có báo nhầm thì sửa luật để hết nhầm, rồi thêm một ca test cho đúng trường hợp đó.
4. **Đột biến:** bỏ kiểm `foreign-asset` thì test của nó phải đỏ; trả lại thì xanh.
5. `git status --short -uall -- shared/game-kit`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** năm mục đạt. Sau đó Claude chạy `kit:sync` vào ba game và nối bộ kiểm vào `deploy:pack`.
