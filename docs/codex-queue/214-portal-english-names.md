# Phiếu 214 · Cổng game (repo cha) · Tên và mô tả tiếng Anh cho Dragonhold, Wordwoven, Last Line; ảnh thật thay emoji

**Nguồn:**
- `AGENTS.md`, mục "Language, names and art level" (chủ dự án 28/10/2026 tối):
  - "These are English games. Everything the player reads is in English", kể cả tên game;
  - ba game tên **Dragonhold**, **Wordwoven**, **Last Line**;
  - "no emoji"; "Every UI detail carries real art, not text alone".
- `docs/games/NAMES_EN.md`, mục "Luật ngôn ngữ".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Hiện trạng (Claude đã kiểm 30/10):**
- `portal/public/games.json:48-74`: ba thẻ còn tên "Rồng Giữ Ải", "Lời Gọi", "Tuyến Cuối", mô tả tiếng Việt, emoji 🐉 🏮 ☄️ ở trường `icon`.
- `portal/src/main.ts`:
  - kiểu `Game` (49–57) bắt buộc `icon`;
  - emoji in ra bằng chữ ở nút menu (`makeGameButton`, 243–255) và thẻ trang chủ (`renderHome`, 466–490).
- `scripts/game-dir.sh:21-23` và `scripts/bootstrap.sh:142-148, 215-217, 236-242`: nhãn console còn tên Việt.
- Phiếu 176 (ảnh bìa) và 177 (biểu tượng) chỉ làm ảnh trong `art-src`, không gắn vào cổng. Phiếu này làm phần gắn, trước khi có ảnh.

Không trùng 176, 177 (chỉ làm ảnh), 004 (đưa Tu Tiên vào cổng), 105, 105b, 187 (nút về cổng trong Dragonhold).

**Báo cáo:** `docs/codex-queue/214-report.md` (tiếng Việt), thư mục `docs/codex-queue/214/`.

## Nơi làm

- Repo cha `/Users/toandx/htdocs/typing-game`, nhánh `feat/space-typing-admin-uiux`. Làm thẳng trong cây này, không worktree. Mọi lệnh chạy từ gốc repo cha.
- Làn P10, phiếu thứ ba.
- Chỉ được sửa hay tạo:
  - `portal/public/games.json`, `portal/src/main.ts`, `portal/src/styles.css`;
  - file mới `portal/src/game-card.ts`;
  - test mới trong `portal/tests/` và fixture trong `portal/tests/fixtures/`;
  - `scripts/game-dir.sh`, `scripts/bootstrap.sh`;
  - changelog (Việc 8), báo cáo và thư mục `214/`.
- Cây cha đang bẩn vì việc khác (media, docs, `shared/game-kit`). Không đụng các file đó.
- Trước khi làm, chạy `git branch --show-current` và `git status --short -uall -- portal scripts/game-dir.sh scripts/bootstrap.sh`:
  - đúng nhánh và sạch: làm tiếp; lưu đầu ra vào `214/git-before.txt`, và lưu `git status --short -uall` của cả repo vào `214/status-before.txt`;
  - sai nhánh, hay có thay đổi trong các đường dẫn đó (kể cả do phiếu trước trong làn): dừng, ghi vào báo cáo.
  - `docs/changelog/` có file chưa commit của phiếu khác thì không sao: phiếu này chỉ tạo một file mới ở đó.

## Luật chung (phiếu mã)

- Được dùng git chỉ đọc (`status`, `diff`, `show`, `log`).
- Test trước, mã sau. Chú thích tiếng Anh.
- Chữ người chơi thấy là tiếng Anh.
- Sáu mục cũ (Monkeytype, Vocabulary Shooter, Recall Typing, Karaoke Typing, Space Typing, Tu Tiên Thủ Ải) giữ nguyên: tên, mô tả, `icon`, mọi trường.
- `id`, `path`, `appUrl`, `group` và thứ tự của mọi mục giữ nguyên (`scripts/validate-space-integration.mjs` kiểm).

## Việc

1. **Mốc đầu.**
   - Lấy sáu mục cũ từ `git show HEAD:portal/public/games.json`, ghi vào `portal/tests/fixtures/legacy-games.json` (giữ nguyên thứ tự và giá trị).
   - Chạy `pnpm portal:test`, `pnpm --dir portal build`, `pnpm validate:space-integration`, `pnpm validate:play-mode` trên mã chưa sửa. Lưu log vào `214/before/`.
2. **Tên và mô tả trong `games.json`.**
   - `name`: đúng `Dragonhold`, `Wordwoven`, `Last Line`.
   - `description`: một câu tiếng Anh, 50–110 ký tự, kết thúc bằng dấu chấm. Câu nói người chơi gõ gì, để làm gì, ở thế giới nào.
   - Chỉ dùng danh từ đang có trong game. Đọc nguồn (chỉ đọc, không sửa) và kiểm bằng `grep` trong `games/<id>/src` hay `index.html` của game:
     - Dragonhold: `games/dragon-hold/index.html:6` (meta description đã tiếng Anh); `docs/games/dragon-lane/DESIGN.md` §0–1;
     - Wordwoven: `games/typing-defense/docs/td/TYPING_DEFENSE_DESIGN.md`; `docs/games/ART_DIRECTION_2026-10-28.md` §2.1;
     - Last Line: hướng B "Lightbearer", `ART_DIRECTION_2026-10-28.md` §4.3; phe địch là **Black Hole Horde** (`NAMES_EN.md`). Không có tàu: không viết "ship", "pilot", "fleet".
   - Không chữ Việt, kể cả tên riêng có dấu. Không emoji. Không tên mới chưa có trong game.
   - Báo cáo ghi: câu chọn, số ký tự, nguồn từng danh từ (file:dòng).
3. **Bỏ emoji, thêm trường `art`.**
   - Ba mục mới không còn trường `icon`.
   - Thêm `"art": { "icon": "/assets/<id>/portal/icon-192.png", "cover": "/assets/<id>/portal/cover-wide.webp" }`, với `<id>` là `dragon-hold`, `typing-defense`, `typing-survival`.
   - Đường dẫn tính trên `appUrl` của chính game, ví dụ `https://dragon.typing-game.local/assets/dragon-hold/portal/icon-192.png`. Cổng không chứa ảnh của game.
   - Ảnh chưa có. Claude chép ảnh của 176, 177 vào đó sau khi duyệt, rồi chạy `media:push`. Tới lúc đó ba thẻ không có ảnh. Đó là thiết kế, không phải lỗi.
   - Kiểu `Game` trong `main.ts`: `icon` thành tùy chọn; thêm `art?: { icon?: string; cover?: string }`.
4. **Helper thuần `portal/src/game-card.ts`.**
   - Không import lúc chạy (chỉ `import type`). Không DOM. Không `enum`, không `namespace`. Node 24 phải nạp được file `.ts` này trực tiếp, như `tests/learning-bridge.test.mjs` nạp `bridge.ts`.
   - `resolveGameArt(game)` trả `{ icon: string | null; cover: string | null }`, là URL tuyệt đối. Trả `null` cho từng ảnh khi:
     - không có `art`, hay giá trị không phải chuỗi;
     - đường không bắt đầu bằng `/assets/<id của chính game>/portal/`;
     - đường có `..`, `\`, `//`, `?` hay `#`;
     - URL tính trên `appUrl` có nguồn khác nguồn của `appUrl`.
   - `gameCardModel(game)` trả `{ title, description, glyph, icon, cover }`:
     - `icon`, `cover`: `{ src, alt, width, height }` hay `null`;
     - bìa: `alt` là `"<Name> cover art"`, 1600 × 900;
     - biểu tượng: `alt` là `""` (tên game đứng ngay cạnh), 192 × 192;
     - `glyph`: chuỗi `icon` cũ, chỉ khi mục **không** có `art`. Có `art` thì `glyph` luôn `null`. Không có hình dự phòng bằng chữ, emoji hay ký tự.
   - `hideImageOnError(img, onHide?)`: nghe sự kiện `error` một lần; khi lỗi thì đặt `img.hidden = true` và gọi `onHide` (để ẩn khung bìa). Nhận mọi đối tượng có `addEventListener` và `hidden`, để test bằng đối tượng giả.
5. **Nối vào `main.ts`.**
   - `renderHome` và `makeGameButton` dựng thẻ và nút qua `gameCardModel`. Không còn chỗ nào đọc `game.icon` trực tiếp.
   - Mỗi `<img>` có `src`, `alt`, `width`, `height`, `loading="lazy"`, `decoding="async"`, và ẩn khi lỗi qua `hideImageOnError`.
   - Bìa lỗi thì ẩn cả khung bìa; thẻ trở về bố cục chữ.
   - Máy chủ trả HTML 200 thay cho 404 thì trình duyệt vẫn báo `error` khi giải mã ảnh. Không cần xử lý thêm.
   - Mục cũ có `glyph` hiện như bây giờ (class `game-icon`, `nav-game-icon`).
   - Menu gọn (`.nav-compact`): ảnh biểu tượng nằm trong span `.nav-game-icon` có sẵn, để luật ẩn hiện cũ vẫn áp dụng. Ảnh lỗi thì span trống; nhãn vẫn thẳng hàng với nút khác.
6. **CSS trong `styles.css`.**
   - Khung bìa ở đầu thẻ, `aspect-ratio: 16 / 9`, `object-fit: cover`, bo góc theo thẻ. Thẻ không nhảy chiều cao khi ảnh đang tải.
   - Biểu tượng 48 px cạnh tiêu đề trong thẻ (thay chỗ `game-icon`); khoảng 1.25em trong menu gọn.
   - Thẻ không có ảnh giữ `min-height` hiện tại; lưới không nhảy.
   - Thêm class mới (ví dụ `.game-cover`, `.game-art-icon`). Chỉ đổi luật của class cũ khi bố cục bìa cần; ghi lý do.
   - Không vẽ hình bằng CSS: không gradient giả ảnh, không khối màu thay biểu tượng.
7. **Nhãn console trong hai script.**
   - `scripts/game-dir.sh:21-23`: `Dragonhold (dragon-hold)`, `Wordwoven (typing-defense)`, `Last Line (typing-survival)`.
   - `scripts/bootstrap.sh`: mọi nhãn "Rồng Giữ Ải", "Lời Gọi", "Tuyến Cuối" thành tên tiếng Anh tương ứng.
   - Nhãn Tu Tiên giữ nguyên. Không đổi logic, đối số hay tên đích (`dragon`, `td`, `survival`).
8. **Changelog** `docs/changelog/<ngày>-portal-english-names.md` (tiếng Việt): đổi gì, vì sao, danh sách file, việc Claude còn phải làm. Không sửa `docs/changelog/README.md`; Claude thêm hàng chỉ mục khi commit (như phiếu 198), để các phiếu cùng làn không đụng nhau ở file đó.

## Test (viết trước, ghi số đỏ trước khi sửa mã)

File mới `portal/tests/game-card.test.mjs`. Chạy bằng `node --test` có sẵn, không thêm gói.

1. `games.json`:
   - ba tên đúng;
   - mỗi mô tả: một câu, 50–110 ký tự, không chữ có dấu tiếng Việt, không ký tự `\p{Extended_Pictographic}`;
   - ba mục không có trường `icon`; `art.icon`, `art.cover` đúng đường ở Việc 3;
   - sáu mục cũ `deepEqual` với `tests/fixtures/legacy-games.json`;
   - danh sách `id` theo thứ tự không đổi.
2. `resolveGameArt`:
   - đường hợp lệ ra đúng URL tuyệt đối;
   - thiếu `art`; giá trị là số;
   - đường của game khác (`/assets/space-typing/portal/a.png`);
   - URL ngoài (`https://evil.example/a.png`, `//evil.example/a.png`);
   - đường có `..`, `\`, `?`, `#`;
   - `appUrl` có đường dẫn hay dấu `/` cuối vẫn ra đúng nguồn.
3. `gameCardModel`:
   - mục có cả `art` và `icon` cũ: `glyph` là `null`;
   - mục cũ không `art`: `glyph` là emoji cũ;
   - ba mục mới: `glyph` là `null`; `alt`, `width`, `height` đúng.
4. `hideImageOnError` với đối tượng giả: chưa lỗi thì `hidden` là false; phát `error` thì `hidden` là true và `onHide` chạy đúng một lần.
5. Quét chữ `portal/src/main.ts`: không còn `game.icon`.
6. `tests/learning-bridge.test.mjs` hiện có vẫn xanh.

## Cấm

- Mọi lệnh git có ghi.
- Sửa `media/media.config.json` và `scripts/media/**` (phần sửa chưa commit của phiếu 171).
- Sửa `portal/src/admin/**`, `shared/**`, `package.json` gốc, `portal/package.json`, `play.sh`, `dev.sh`, `infra/**`, `.gitmodules`.
- Ghi vào `games/**` (mọi repo game, mọi worktree). Tu Tiên, kể cả mục của nó trong `games.json`.
- Tạo, chép hay sửa ảnh; ảnh tạm; hình vẽ bằng SVG, canvas hay CSS; emoji hay ký tự thay biểu tượng.
- Thêm gói npm (không `jsdom`, không `happy-dom`).
- Dev server, trình duyệt, mạng.
- Đổi nhãn nhóm menu (`main.ts:73-77`: "Luyện gõ", "Game chiến đấu", "Khác") và nhãn thương hiệu (`main.ts:108`, "⌨ typing games"). Đó không phải thẻ của ba game. Đề xuất nhãn tiếng Anh trong báo cáo để Claude quyết.

## Kiểm (ghi số)

1. `pnpm portal:test`: số test đỏ trước khi sửa mã, số qua và số lỗi sau khi sửa. Log trong `214/`.
2. `pnpm --dir portal build`: mã thoát 0. Byte của file JS và CSS chính trước và sau.
3. `pnpm validate:space-integration` và `pnpm validate:play-mode`: qua. Log trong `214/`.
4. `bash -n scripts/game-dir.sh` và `bash -n scripts/bootstrap.sh`: mã 0. Số dòng còn "Rồng Giữ Ải", "Lời Gọi", "Tuyến Cuối" trong hai script: 0. Nhãn Tu Tiên còn nguyên.
5. `git diff -- portal/public/games.json`: chỉ ba mục mới đổi. Lưu vào `214/games-json.diff`.
6. Emoji còn lại: trong `games.json` (sáu mục cũ) và trong `portal/src/main.ts` (ví dụ `⌨` ở nhãn thương hiệu), mỗi chỗ một dòng file:dòng.
7. Tên Việt cũ ngoài phạm vi phiếu: liệt kê file:dòng trong `play.sh`, `dev.sh` cho Claude sửa.
8. `git status --short -uall` của cả repo sau khi làm, lưu `214/status-after.txt`, so với `214/status-before.txt`: phần chênh chỉ là các đường ở mục "Nơi làm" (cộng báo cáo và `214/`). Báo cáo ghi **đúng** danh sách đường dẫn phiếu này sửa hay tạo. `git diff --check` trên các file đó: không lỗi.

## Báo cáo phải có

- Ba câu mô tả, số ký tự, nguồn danh từ.
- Bảng cho Claude: ảnh của 176, 177 → đường đích trong repo game:
  - `games/<id>/art-src/ui/app-icon/` bản 192 → `games/<id>/public/assets/<id>/portal/icon-192.png`;
  - `games/<id>/art-src/ui/cover/cover-wide.png` → `games/<id>/public/assets/<id>/portal/cover-wide.webp`.
  - Ghi rằng Last Line chưa có thư mục `public/assets/typing-survival/`.
- Đề xuất nhãn tiếng Anh cho ba nhóm menu và nhãn thương hiệu.
- Rủi ro: ba thẻ chưa có ảnh tới khi 176, 177 được nhận và `media:push`; nhánh cha chưa push.

**Xong khi:** tám việc và tám mục kiểm đạt, có số trong báo cáo. Claude duyệt, kiểm bố cục trang chủ cổng ở 1280 và 1920 (khi chưa có ảnh, và khi có ảnh của 176, 177), rồi commit.
