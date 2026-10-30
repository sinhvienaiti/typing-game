# Phiếu 210 · Last Line · Hướng dẫn lần đầu: chọn sẵn Pulse Gun và Heat Beam, chú thích START, gợi ý nạp súng trong trận đầu (TS-M1-11)

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §3.2 mục 8: "TS-M1-11 · P1 · G5. Lần đầu không có hướng dẫn. Sửa: chọn sẵn Pulse Gun + Heat Beam kèm nhãn "Khuyên dùng"; nút "BẮT ĐẦU" kèm chú thích; gợi ý "Gõ từ trên bến để nạp súng" trong trận đầu, tắt sau 2 lần nạp." Bảng cổng §3.1, G5: "Lần đầu không có hướng dẫn".
- Luật ngôn ngữ 28/10 (`AGENTS.md`): mọi chữ người chơi thấy là tiếng Anh. Ba chữ ở trên thành "Recommended", một dòng chú thích dưới START, và "Type a word on a bay to load its gun".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi". Việc này trước thuộc làn T của Claude; nay giao Codex.

Chưa có mã nào làm việc này (đã quét). Không trùng 104 (ba nhãn nhỏ), 104b (Esc ở thẻ ải), 130 (đổi chữ sang tiếng Anh).

**Báo cáo:** `docs/codex-queue/210-report.md` (tiếng Việt), thư mục `docs/codex-queue/210/`. Cả hai ở repo cha, không ở trong worktree.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-ts-codex`, nhánh `ts-codex`. Làn Codex `s1` (một làn), cwd `.`; chạy sau 205 và 207 (cùng nhánh). Lệnh git và báo cáo chạy từ gốc repo cha; lệnh `pnpm` chạy trong worktree.
- Trước khi làm, chạy `git -C games/.wt-ts-codex status --short -uall` và `git -C games/.wt-ts-codex branch --show-current`:
  - sạch: làm tiếp;
  - chỉ có file của 205 hay 207 vì Claude chưa commit (đối chiếu `docs/codex-queue/205-report.md`, `207-report.md`): làm tiếp, ghi danh sách vào báo cáo. Trước khi sửa một file mà 205 hay 207 cũng sửa, chép nó vào `210/before/` để Claude tách các phần;
  - có file khác, hay nhánh không phải `ts-codex`: dừng, ghi vào báo cáo.
- Được dùng git chỉ đọc. Test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn.
- Luật chơi không đổi. Ván vàng `tests/golden/s0-trace.json`, 152 mã băm chương và mã băm bộ bài `7f073fa2` giữ nguyên.

**Chỉ được ghi** (đường dẫn tính từ worktree):
- `src/app/guide.ts` (mới; hàm thuần, không DOM);
- `src/app/journey.ts`;
- `src/view/screens-journey.ts`: chỉ chèn dòng mới, không viết lại hay định dạng lại dòng cũ (phiếu 206 sửa cùng file ở `.wt-ts-art`; Claude gộp theo thứ tự);
- `src/view/hud.ts`: chỉ `wordDone()` và `setNotice()`, cộng một trường;
- `src/view/survival.css`: chèn quy tắc mới cạnh `.sv-notice` (dòng 59–60) và cạnh thẻ súng (dòng 233–245); không sửa dòng cũ;
- `src/app/main.ts`: tối đa 8 dòng đổi, chỉ ba chỗ ở việc 5;
- test mới trong `tests/`;
- `scripts/visual/scenarios/survival-s1-loadout.mjs` (một dòng) và `scripts/visual/scenarios/survival-s1-first-run.mjs` (mới);
- `docs/changelog/<ngày>-first-run-guide.md` (mới, tiếng Việt);
- báo cáo và `210/` ở repo cha.

## Đọc trước

- `src/app/journey.ts`: `Journey.loadout()`, `cards()`, `begin()`, `picked`, `cursor`, `ready`; `loadProgress()`, `STAGES_KEY`. Kiểu `TextStore` ở `src/app/skill.ts`.
- `src/view/screens-journey.ts`: thẻ súng (khoảng dòng 90–100) và nút START (dòng 106).
- `src/view/hud.ts`: `wordDone()` (khoảng dòng 219) và `setNotice()` (khoảng dòng 245). `src/view/typing-feel.ts` gọi `wordDone(..., full)`: `full` là `false` khi từ thật sự nạp súng.
- `src/app/main.ts`: dòng `hud.setNotice(...)` trong `update()` (khoảng dòng 635); listener Esc ở thẻ ải (khoảng dòng 560–571, phiếu 104b).
- `tests/intro-key.test.ts`: test này chạy thật đoạn `main.ts` từ `for (const type of ["pointerdown", "keydown"])` tới `installAutoPause(window` trong VM. Thêm tên mới vào đoạn đó là test vỡ.
- `src/view/survival.css`: `.sv-notice` là ô cảnh báo viền đỏ, có ký tự `⌨` ở `::before`; nhãn `BAY n` của thẻ súng là `em` nằm trên mép phải.

## Việc

1. **Bản ghi hướng dẫn** trong `src/app/guide.ts`. Tên hàm là gợi ý; đổi được nếu hợp mã hơn.
   - Khóa `survival.guide` ở `localStorage`, qua `TextStore` như `survival.stages`. JSON `{ "started": boolean, "hint": boolean }`.
   - `loadGuide(store)`: không có hay hỏng thì cả hai `false`. Người chơi đã qua ải nào (`loadProgress(store).passed` không rỗng) thì cả hai `true`: người chơi cũ không thấy hướng dẫn.
   - `markStarted(store)`, `markHintDone(store)`: gộp vào bản ghi, không xóa trường kia. `setItem` trả `false` hay ném lỗi thì không vỡ.
   - `RECOMMENDED`: chỉ `c1-s1` → `[GUN.xung, GUN.tia]` (Pulse Gun, Heat Beam). Đặt trong `guide.ts`, không trong `src/content/**`.
2. **Chọn sẵn ở lần đầu.**
   - `Journey.loadout()`: nếu `started` là `false`, `picked` rỗng và ải có trong `RECOMMENDED`, thì chọn sẵn hai súng đó theo đúng thứ tự, cắt theo số bến của ải.
   - Khi chọn sẵn, con trỏ đặt lên START: một Enter là vào thẻ ải.
   - Mỗi trang chọn sẵn nhiều nhất một lần. Người chơi bỏ chọn hết, Esc, rồi quay lại: màn trống, không chọn lại.
   - `picked` đã có (nút Next ở màn kết quả, Esc từ thẻ ải của 104b): giữ nguyên bộ súng và thứ tự.
   - `Journey.begin()` gọi `markStarted` trước `host.start`.
3. **Nhãn "Recommended".**
   - `CardView` thêm `recommended: boolean`. Đúng với Pulse Gun và Heat Beam ở `c1-s1`, mọi lúc: đây là lời khuyên của ải, không chỉ của lần đầu. Ải khác: không nhãn.
   - Thẻ có một phần tử riêng, ví dụ `<i class="sv-rec">Recommended</i>`. Không đặt trong `em` của nhãn `BAY n`.
   - CSS: nhãn nằm trên mép trái của thẻ, đối xứng với nhãn bến. Không đè nhãn bến; tên súng không xuống dòng.
   - Chỉ dùng biến màu có sẵn trong `theme.css`. Không icon vẽ bằng CSS, SVG hay emoji.
   - Nhãn chỉ là chữ, nằm trên thẻ súng sẽ có icon thật của phiếu 206. Nếu cần ảnh đế riêng cho nhãn, Claude mở phiếu ảnh sau; ghi vào báo cáo, không vẽ thay ở đây.
4. **Chú thích START**, một dòng, đúng chuỗi:
   - "Press Enter to start. Guns fire on their own; type words to load them."
   - Chỉ hiện khi `started` là `false` và bộ súng đã đủ (`ready`). Đã từng bắt đầu một ải thì không hiện.
   - Đặt ngay dưới nút START, dùng lớp `.sv-note` có sẵn. Không xuống dòng ở 1280 × 720.
5. **Gợi ý trong trận đầu**, đúng chuỗi: "Type a word on a bay to load its gun".
   - `Hud`: trường `loads` đếm lần nạp thật trong trang, tăng trong `wordDone()` khi `full` là `false`. Mỗi trận là một lần tải trang, nên không cần đặt lại.
   - Lớp thuần, ví dụ `LoadHint(store)`: trả chuỗi gợi ý khi `hint` là `false`, đang chơi (`mode === "play"`) và `loads < 2`.
   - Khi `loads` chạm 2: gọi `markHintDone` đúng một lần, từ đó trả `""`. Trang sau không hiện nữa.
   - Hiện ở trận đầu, dù là Trial (`s0`) hay ải 1. Không hiện ở thẻ ải, lúc tạm dừng, màn kết quả.
   - Dùng ô thông báo có sẵn (`.sv-notice`, trên dòng chữ). Thứ tự ưu tiên: bàn phím không phải tiếng Anh > danh sách từ ngoại tuyến > gợi ý. Tách quyết định này ra hàm thuần, ví dụ `noticeFor(ime, offline, hint)` trả `{ text, kind }`.
   - `setNotice(value, kind = "warn")`: kiểu `"hint"` thêm lớp `is-hint`. Lời gọi cũ chỉ một tham số vẫn chạy (nhánh `ts-typefx` gọi như vậy).
   - CSS `.sv-notice.is-hint`: không viền đỏ cảnh báo; `::before` là `none` (bỏ ký tự `⌨`); chỉ dùng biến màu có sẵn.
   - Chỉ chữ, chưa icon. Icon bàn phím của phiếu 149 do Claude gắn sau khi nhận.
   - `main.ts`: một import, một dòng tạo `LoadHint`, và dòng `setNotice` trong `update()`. Tối đa 8 dòng đổi. Không chỗ nào nằm trong đoạn `tests/intro-key.test.ts` chạy.
6. **Esc của 104b giữ đúng.** Thẻ ải → Esc → nạp súng, đúng ải, đúng bộ súng và thứ tự, kể cả ở lần đầu. `tests/intro-key.test.ts` không sửa và vẫn xanh.
7. **Kịch bản trình duyệt.** Codex viết, không chạy; Claude chạy.
   - `survival-s1-loadout.mjs`: thêm một dòng đặt `survival.guide` thành `{"started":true,"hint":true}` ngay sau dòng xóa `survival.stages`. Phím 1 và 3 vẫn chọn đúng hai súng như cũ.
   - `survival-s1-first-run.mjs` mới, theo mẫu `survival-s1-loadout.mjs`:
     - xóa `survival.stages` và `survival.guide`;
     - vào nạp súng của ải 1; ghi `picked`, `cursor`, số `.sv-rec`, chữ chú thích START; chụp;
     - Enter → thẻ ải → một phím vào trận; ghi chữ và lớp của `.sv-notice`; chụp;
     - không gõ từ (Claude gõ tay hai lần nạp);
     - ảnh vào `tmp/` của game.
   - Hai file qua `node --check`.
   - Báo cáo liệt kê các kịch bản khác có thể thấy gợi ý ở khung đầu trận khi hồ sơ trình duyệt mới. Không sửa chúng.
8. **Changelog** `docs/changelog/<ngày>-first-run-guide.md`: làm gì, vì sao (TS-M1-11, G5), bản ghi `survival.guide`, ba chuỗi tiếng Anh, số test trước và sau.

## Test (viết trước, ghi số đỏ trước khi sửa mã)

1. `loadGuide`: kho trống; JSON hỏng; đã qua ải → cả hai `true`. `markStarted` rồi `markHintDone`: giữ trường kia. `setItem` ném lỗi: không vỡ.
2. Chọn sẵn qua `Journey` với host giả:
   - lần đầu ở `c1-s1` → `picked` là `[xung, tia]`, `cursor` ở START, `ready` đúng;
   - `started` đúng → trống;
   - ải `c1-s2` → trống;
   - `picked` có sẵn → giữ nguyên thứ tự;
   - bỏ chọn hết, Esc, quay lại → trống;
   - `begin()` ghi `started`.
3. `cards()`: `recommended` đúng cho hai súng ở `c1-s1`; sai cho ba súng kia, và cho mọi súng ở ải khác.
4. HTML của `renderJourney`:
   - lần đầu: 2 `sv-rec`, 1 chú thích đúng chuỗi;
   - sau `started`: không chú thích, vẫn 2 nhãn ở ải 1;
   - ải 2: không nhãn;
   - `sv-rec` không nằm trong `em`;
   - chưa đủ súng: không chú thích.
5. `LoadHint`:
   - `loads` 0 và 1 → chuỗi gợi ý;
   - `loads` 2 → `""`, `setItem` của `survival.guide` gọi đúng một lần;
   - không đang chơi → `""`;
   - `hint` sẵn `true` → `""` từ đầu;
   - `LoadHint` mới trên cùng kho sau khi xong → `""`.
6. `noticeFor`: IME thắng ngoại tuyến; ngoại tuyến thắng gợi ý; không gì → `""`; kiểu `"hint"` chỉ khi chữ là gợi ý.
7. `tests/english-ui.test.ts` vẫn xanh.
8. **Đột biến:** cho chọn sẵn không làm gì thì test 2 đỏ; cho `LoadHint` không bao giờ lưu thì test 5 đỏ; trả lại thì xanh. Ghi số.

Môi trường test là `node`, không DOM. `Hud` không test trực tiếp; Claude kiểm phần đếm trên trình duyệt.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy `kit:sync`.
- Sửa `src/sim/**`, `src/content/**`, `src/audio/**`, golden.
- Sửa `src/app/input.ts`, `src/view/strip.ts`, `src/view/typing-feel.ts`, `src/view/type-fx.ts`: TF2 và phiếu 191 đang sửa các file này ở `.wt-ts-typefx`.
- Sửa `main.ts` ngoài ba chỗ ở việc 5, hay sửa trong đoạn `tests/intro-key.test.ts` chạy.
- Dev server, trình duyệt, mạng. Tạo media. Icon vẽ bằng CSS, SVG hay emoji.
- Chữ tiếng Việt trong chữ người chơi thấy.
- Đụng game khác, worktree khác (`.wt-ts-typefx`, `.wt-ts-vfx`, `.wt-ts-art` nếu có, `.wt-dh-*`, `.wt-td-*`), repo cha ngoài báo cáo và `210/`, Tu Tiên.

## Kiểm (ghi số)

1. `pnpm check` xanh: số file test và số test trước và sau, số file `verify-kit`, build đạt. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Test mới: số đỏ trước sửa, số xanh sau sửa; log trong `210/`.
3. SHA-256 của `tests/golden/s0-trace.json` trước và sau giống nhau. `node --import tsx scripts/chapter-hashes.ts` trước và sau: `diff` rỗng (152 dòng).
4. `git -C games/.wt-ts-codex diff --numstat -- src/app/main.ts`: ≤ 8 dòng; chép các dòng đổi vào báo cáo. `tests/intro-key.test.ts` không đổi.
5. Danh sách mọi chuỗi người chơi thấy mới hay đổi (ba chuỗi ở trên); test chữ tiếng Anh xanh.
6. `node --check` cho hai file kịch bản.
7. `git status --short -uall`: chỉ file trong "Chỉ được ghi", cộng file 205/207 nếu Claude chưa commit (ghi rõ). `git diff --check` mã 0.

**Xong khi:** tám việc và bảy mục kiểm đạt, có số trong báo cáo. Sau đó Claude kiểm trên trình duyệt ở 1280 và 1920 bằng hồ sơ mới:
- nạp súng ải 1 chọn sẵn hai súng, hai nhãn, chú thích, con trỏ ở START;
- vào trận thấy gợi ý; nạp hai lần thì gợi ý tắt; tải lại không thấy nữa;
- Esc ở thẻ ải về nạp súng, giữ bộ súng.

Rồi Claude commit, gộp theo thứ tự 205 → 207 → 210, cùng 206 (`.wt-ts-art`) và 191 (`.wt-ts-typefx`).
