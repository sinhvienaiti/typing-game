# Phiếu 197 · Dragonhold · Màn tựa kiêm màn tải (DH-13)

> **Chạy lại (30/10, 10:55, điều phối):** lượt trước dừng vì 195 chưa xong. Lượt này chạy sau 194 và 195 trong cùng làn. File chưa commit của 187, 194, 195 là file đã biết (xem báo cáo của từng phiếu); không sửa phần của chúng. Chỉ chạy khi `194-report.md` và `195-report.md` đều ghi hoàn tất; chưa thì dừng, ghi lý do.

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §1.2 mục 8: "DH-13 · P1 · G5. Không có màn tựa. **Sửa:** màn tựa trên nền cảnh map: tên game, Enter để bắt đầu, ba dòng cách chơi, về cổng game; đi được bằng phím và chuột."
- `docs/games/map1/UI_IMAGERY.md` §2: "Thiếu màn tựa là chỗ hở lớn nhất."
- Chủ dự án 29/10 (`docs/games/IN_GAME_SETTINGS.md` §1): nút bánh răng và nút loa "có ở mọi màn chơi và cả màn tựa".
- Chủ dự án 29/10: giao thêm việc cho Codex.

DH-13 là P1 có tên trong danh sách, nên được làm trong giai đoạn không thêm tính năng (chủ dự án 28/10). MAP1_PRODUCTION giao nó cho làn R của Claude; nay chuyển sang Codex. Camera quay thấp quanh map thật cho màn tựa (phiếu 120) vẫn thuộc làn R2. Phiếu này chỉ chừa móc cho camera đó.

Không trùng: 096, 119, 184 (chỉ vẽ ảnh); 187 (đường về cổng lúc build); 192 (nút Settings và loa); 105, 105b (nút cổng ở màn kết quả).

**Báo cáo:** `docs/codex-queue/197-report.md`, thư mục `docs/codex-queue/197/`.

**Chỉ chạy khi** 194 và 195 đã xong (có `194-report.md` và `195-report.md`). Thiếu một trong hai thì dừng, ghi vào báo cáo.

## Nơi làm

- Worktree `games/.wt-dh-codex`, nhánh `dh-codex`. Làn `s1`, chạy sau 195. cwd của làn là repo cha (`.`); chạy `pnpm` trong thư mục worktree.
- `git status --short -uall` phải sạch, hoặc chỉ còn file của 187, 194, 195 mà Claude chưa commit. Khi đó ghi danh sách vào báo cáo và không sửa phần của chúng ngoài chỗ việc này cần. Có file lạ khác thì dừng.
- **Đọc trước (chỉ đọc):**
  - `src/app/app.ts`: dòng nạp `.dh-boot` (khoảng 205); khối khởi động khoảng 870–910 (`begin`, `learning.buildDeck`, `askPace`).
  - `src/ui/results.ts` 255–275: mẫu nút "Back to portal" (`portalHome`, lớp `is-focused`, focus giữ ở bộ định tuyến phím).
  - `src/app/portal.ts` (`portalHome`, phiếu 187); `src/app/input-router.ts` (`intercept`, `KeyPanel`); `KEYS` trong `src/content/rules.ts`.
  - `194-report.md` (file và cách dùng danh sách chọn ảnh); `195-report.md` (thông báo khi bộ chữ lỗi); `119-report.md` mục 5 và 6; `192-report.md` nếu đã có.
  - Mẫu màn tựa Wordwoven: `games/typing-defense/src/ui/title.ts` 60–80 (thiếu ảnh thì nền phẳng và `console.warn`).
- **Ảnh vào (chỉ đọc, checkout chính):** `games/dragon-hold/art-src/ui/title-epic/`:
  - `title-backdrop.png` (1536 × 1024);
  - `logo.alpha.png`, `logo.512.png`;
  - `emblem.alpha.png`, `emblem.512.png`.
  - `keyart.png`, `poster.png` không dùng ở màn này.

## Việc

1. **Đưa ảnh 119 vào danh sách chọn của 194.**
   - Bảng `src/ui/ui-art.json` của 194 chỉ có `icons` (ô vuông 64/128/256). Thêm một danh sách mới `art` cạnh `icons`, ba mục `title-backdrop`, `logo`, `emblem`. Mỗi mục: `name`, `alt` (tiếng Anh; logo là "Dragonhold"), `source` (đường tương đối `--art-src`: `ui/title-epic/title-backdrop`, `ui/title-epic/logo.alpha`, `ui/title-epic/emblem.alpha`), `width` ra (backdrop 1536, logo 1024, emblem 512; không phóng to), `accepted`.
   - `accepted` theo đúng quy ước của 194: số phiếu nhận (chuỗi) hay `null`. Cả ba đặt `null`. Claude đổi thành `"119"` khi nhận 119 (logo và huy hiệu còn ngoại lệ sắc khóa, `119-report.md` mục 5).
   - Mở rộng `pnpm prepare-ui-art` của 194: mục `art` có `accepted` khác `null` thì xuất `public/assets/dragon-hold/ui/title/<name>.webp` (thu Lanczos về `width`, giữ alpha, quality 90, alpha-quality 100) và ghi vào cùng `manifest.json`; mục `null` thì bỏ qua, không ghi gì. `--check` kiểm cả mục `art` đã nhận. Thêm test với fixture trong `tmp/`.
   - Lượt chạy thật của phiếu này không xuất ảnh title nào (cả ba `null`). Không chép, cắt, sửa ảnh nguồn. Không đưa ảnh chưa nhận vào `public/`.
   - URL lúc chạy: `/assets/dragon-hold/ui/title/<name>.webp?v=<version>`. Mục `null` thì màn tựa không gửi yêu cầu ảnh nào.
   - Không chờ 184. Nếu bảng đã có mục `loading` của 184 với `accepted` khác `null` thì được dùng làm nền lúc tải.
2. **Màn tựa đứng trước thẻ tốc độ.**
   - Thứ tự mới: màn tựa → Start → thẻ tốc độ (khi chưa có `?wpm=`) → `begin()`. Có `?wpm=` thì Start đi thẳng vào `begin()`.
   - Nền: `title-backdrop`, phủ kín màn, cắt giữa (`object-fit: cover`). Ở màn 16 : 9 đây đúng là bản cắt 119 đã đo.
   - Logo giữa trên, trong vùng 119 đo cho logo: khoảng 25–75 % rộng, 6–30 % cao. Ảnh logo có `alt="Dragonhold"`.
   - Khối menu dưới trái, trong vùng 119 đo cho menu: khoảng 3–35 % rộng, 55–92 % cao. Trong khối: huy hiệu nhỏ, nút Start, dòng gợi ý, ba dòng cách chơi.
   - Dòng gợi ý: lúc tải thì hiện tiến độ (việc 5); tải xong thì "Press Enter to start".
   - Ba dòng cách chơi bằng tiếng Anh, đúng tên đang dùng trong game. Gợi ý:
     - "Type the word over a foe and Hỏa Long breathes fire on it."
     - "Place traps, units and houses on the lanes during breaks."
     - "Keep Hỏa Long standing until the last wave ends."
   - Bỏ dòng `.dh-boot` cũ ("loading words…"); màn tựa thay nó.
3. **Nút về cổng game và chỗ cho hai nút cài đặt.**
   - "Back to portal" chỉ hiện khi `portalHome(import.meta.env.VITE_PORTAL_URL)` khác `null`. Nút trỏ tới đó, `target="_top"`, như màn kết quả.
   - Biến trống thì không có nút và không để lại chỗ trống.
   - Nếu `src/app/quick.ts` của 192 đã có trong `dh-codex`: gắn nút Settings và nút loa ở góc trên phải màn tựa (IN_GAME_SETTINGS §1).
   - Nếu chưa có: chừa ô rỗng `.dh-title__quick` ở góc trên phải và móc `title.quickSlot` (phần tử để 192 gắn vào). Ghi trong báo cáo. Không đặt icon thay thế.
4. **Đi bằng phím và chuột.**
   - Phím đi qua bộ định tuyến phím có sẵn (`intercept` hay một `KeyPanel`), như thẻ tốc độ. Không thêm bộ nghe `keydown` thứ hai trên `window`.
   - Bộ định tuyến hiện được tạo sau khi bộ chữ xong. Tạo nó lúc khởi động để màn tựa nhận phím ngay; ghi lại chỗ đã dời.
   - Chỉ dùng action có sẵn trong `KEYS`: `enter`, `escape`, `rotate-left`, `rotate-right`, `tilt-up`, `tilt-down`. Không sửa `src/content/rules.ts`.
   - Mũi tên chuyển focus giữa các nút, đi vòng. Enter bấm nút đang focus.
   - Esc ở màn tựa không rời màn tựa. Bảng của 192 đang mở thì để 192 đóng.
   - Chữ cái không vào sim khi màn tựa mở.
   - Chuột: rê vào nút thì focus nút đó; bấm thì bấm.
   - Focus mặc định là Start. Lúc Start tắt, focus vẫn đứng ở Start.
   - Viền focus rõ ở cả chuột và phím: dày ≥ 2 px, tương phản ≥ 3 : 1 với nền quanh nút.
5. **Tiến độ tải.**
   - Bốn nguồn, đọc từ lời hứa đã có trong `app.ts`: từ vựng (`learning.buildDeck`), model đám đông (`models.ready`), mặt đất (`map.groundBaked`: ô đất và decal trong manifest), hai rồng (`heroes.ready`).
   - Một dòng tiến độ tiếng Anh, ví dụ "Loading 3 of 4 · ground", có `role="status"`; cộng một thanh mảnh.
   - Start chỉ bật khi cả bốn đã xong.
   - Model, mặt đất hay rồng lỗi thì vẫn tính là xong (game đã có cách xử lý riêng) và `console.warn` một lần.
   - Bộ chữ lỗi hay rỗng: hiện thông báo của 195 trên màn tựa; Start giữ tắt; "Back to portal" vẫn dùng được.
6. **Thiếu ảnh.**
   - Ảnh không có trong danh sách, có `accepted: null`, hay lỗi khi tải (`error`): tính là thiếu.
   - Nền thiếu: nền phẳng một màu tối của game, `console.warn` một lần, ghi tên ảnh.
   - Logo thiếu: đặt chữ "Dragonhold" bằng font tiêu đề đang nạp (Cormorant Garamond), như DH-14 cho phép; `console.warn`.
   - Huy hiệu thiếu: ẩn; `console.warn`.
   - Không SVG, canvas, emoji, gradient hay hình CSS thay cho ảnh. Không thêm trang trí CSS mới (viền khắc, rêu).
   - Khung nút: khung vẽ 162 (`button`, `button-active`) chưa nhận và chưa có trong bảng của 194. Dùng nút `.dh-btn` có sẵn của game (như màn kết quả, menu dừng); không thêm kiểu nút mới. Ghi vào báo cáo để phiếu gắn khung 162 thay sau.
7. **Móc cho camera màn tựa của R2.**
   - Màn tựa có `onShow(fn)`, `onHide(fn)` (trả hàm gỡ), `isOpen`, và `setBackdrop("art" | "live")`.
   - `"live"` ẩn tranh nền để thấy cảnh map 3D phía sau. Mặc định `"art"`.
   - `app.ts` chỉ tạo móc, chưa gắn gì. Một dòng chú thích chỉ chỗ R2 gắn camera.
   - Thêm `title` (`"loading" | "ready" | "blocked" | "started"`) vào `handle.state()` để Claude đọc khi kiểm trên trình duyệt.
8. **Bỏ qua màn tựa cho kịch bản.**
   - `?title=0` bỏ qua màn tựa, đi thẳng như hôm nay. Thêm vào `optionsFromUrl`.
   - Thêm `title=0` vào `boot()` của `scripts/visual/scenarios/lib/dh.mjs` và vào các URL `page.goto` viết thẳng trong `scripts/visual/scenarios/*.mjs`.
   - Không chạy các kịch bản đó. Liệt kê trong báo cáo để Claude chạy.
9. **File.**
   - Máy trạng thái thuần (không DOM, không đồng hồ): `src/ui/title-state.ts`.
   - Lớp DOM: `src/ui/title.ts`. Kiểu: `src/ui/styles/title.css`, file mới, nạp từ `title.ts`. Không thêm vào `dh.css` (194 và 192 cũng sửa CSS).
   - Sửa `app.ts` ít nhất có thể: dh-vfx và 192 cũng sửa file này; thứ tự gộp là map-pilot → dh-vfx → dh-codex. Ghi số dòng đổi trong báo cáo.
10. **Test trước, mã sau** (`tests/ui/title-state.test.ts`, `tests/ui/title.test.ts`, cộng một ca cho `optionsFromUrl`):
    - loading → ready khi đủ bốn nguồn; loading → blocked khi bộ chữ lỗi; ready → started đúng một lần;
    - Enter lúc loading hay blocked không bắt đầu; Enter trên Start lúc ready thì bắt đầu; Enter trên "Back to portal" trả lệnh đi cổng;
    - Esc không rời màn tựa; mũi tên đi vòng đúng thứ tự nút;
    - có và không có nút cổng (`vi.stubEnv("VITE_PORTAL_URL", …)`);
    - thiếu ảnh hay `accepted: null`: nền phẳng, chữ logo thay ảnh logo, mỗi ảnh `console.warn` đúng một lần;
    - `onShow`, `onHide` gọi đúng lúc; `?title=0` đọc đúng;
    - dùng stub DOM như `tests/app/pace-card.test.ts`; không test dựa vào thời gian.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy `kit:sync`.
- Sửa `src/view/**` (map-pilot đang giữ một camera màn tựa chưa gộp trong `camera.ts`), `src/sim/**`, `src/content/rules.ts`, `src/ui/styles/dh.css`.
- Dev server, trình duyệt, mạng.
- Chép, cắt, sửa ảnh; đưa ảnh vào Git hay `public/`.
- Âm thanh mới, nhạc màn tựa, hay tính năng ngoài danh sách việc.
- Đụng game khác, worktree khác (nhất là `.wt-dh-vfx`, `.wt-dh-keys`, `.wt-dh-mappilot`, `.wt-dh-models`), Tu Tiên.
- Ghi ra ngoài repo.
- Chữ người chơi thấy phải là tiếng Anh; chỉ tên riêng Hỏa Long, Bạch Long giữ dấu.

## Kiểm (ghi số)

1. `pnpm check` xanh (số test trước và sau). Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Ván vàng: `tests/golden/m0.json` không đổi; test golden xanh.
3. `tests/english-ui.test.ts` xanh. Liệt kê mọi chuỗi mới người chơi thấy.
4. `pnpm deploy:pack` 0 lỗi. Lưu đầu ra JSON vào `197/`.
5. `git status --short -uall`: chỉ file của việc này, cộng `docs/changelog/<ngày>-title-screen.md`. File 187, 194, 195 chưa commit (nếu có) thì nêu tên riêng.
6. `grep` trên `title.ts`, `title-state.ts`, `title.css`: không `<svg`, `canvas`, emoji, `gradient`. Ghi kết quả.
7. Số dòng đổi trong `app.ts`; danh sách kịch bản đã thêm `title=0`.
8. Hướng dẫn cho Claude kiểm trên trình duyệt ở 1280 × 720 và 1920 × 1080: chuột, phím, có và không có `VITE_PORTAL_URL`, ảnh `accepted` là `"119"` (sau khi chạy lại `prepare-ui-art`) và `null`, bộ chữ lỗi.

**Xong khi:** mười mục việc và tám mục kiểm đạt. Claude kiểm trên trình duyệt ở 1280 và 1920, đổi `accepted` khi nhận 119, rồi commit.
