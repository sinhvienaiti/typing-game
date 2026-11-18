# Phiếu 210 · Last Line · Hướng dẫn lần đầu (TS-M1-11, G5)

Hoàn tất phần mã và các kiểm được phép. **296/296 test, 26 file; kit 61/61;
TypeScript và build xanh.** Chờ Claude kiểm trình duyệt ở 1280 và 1920,
đặc biệt hai lần nạp thật, tải lại và bố trí nhãn. Chưa commit hoặc gộp.

## 1. Mốc đầu và phạm vi

Làm ở `games/.wt-ts-codex`, nhánh **ts-codex**. Đã chạy hai lệnh trạng thái
và nhánh trước sửa: [status-before.txt](210/status-before.txt),
[branch-before.txt](210/branch-before.txt). Có đúng **17 đường** chưa commit
của 205/207, khớp hai báo cáo nên tiếp tục:

- `.gitignore`, `README.md`, `vite.config.ts`;
- `src/app/main.ts`, `src/app/learning.ts`, `src/app/portal.ts`;
- `src/view/bolts.ts`, `combat.ts`, `crowd.ts`, `models.ts`, `ship.ts`;
- `docs/changelog/2026-10-30-own-models.md`, `2026-10-30-portal-origin.md`;
- `public/assets/typing-survival/models/manifest.json`;
- `tests/own-models.test.ts`, `portal-build.test.ts`, `portal.test.ts`.

File giao với 205 là `src/app/main.ts`; đã chép nguyên trước khi sửa vào
[before/main.ts](210/before/main.ts). 207 không sửa file thuộc phiếu 210.
Các file có sẵn khác giữ nguyên. Bản vá riêng:
[210-only.patch](210/210-only.patch).

**10 đường của phiếu**, tính từ worktree:

| Đường | Phần thực hiện |
| --- | --- |
| `src/app/guide.ts` (mới) | Bản ghi hướng dẫn, bảng RECOMMENDED, LoadHint và quyết định ưu tiên thông báo; không DOM |
| `src/app/journey.ts` | Chọn sẵn một lần trong trang, con trỏ START, cờ recommended, điều kiện chú thích, ghi started trước host.start |
| `src/view/screens-journey.ts` | Chỉ chèn 3 dòng: import, nhãn riêng, chú thích dưới START |
| `src/view/hud.ts` | Một trường loads; chỉ sửa wordDone và setNotice |
| `src/view/survival.css` | Chỉ chèn quy tắc cạnh notice và thẻ súng; dùng biến theme có sẵn |
| `src/app/main.ts` | Ba vị trí đúng phiếu; diff riêng ở mục 4 |
| `tests/guide.test.ts` (mới) | 31 test Node, gồm render HTML, không dựng DOM/Hud |
| `scripts/visual/scenarios/survival-s1-loadout.mjs` | Đúng một dòng đặt hai cờ true ngay sau xóa survival.stages |
| `scripts/visual/scenarios/survival-s1-first-run.mjs` (mới) | Hồ sơ mới, đo Loadout, chụp, Enter vào thẻ ải rồi một phím vào trận; không tự nạp từ |
| `docs/changelog/2026-10-30-first-run-guide.md` (mới) | Lý do, hành vi, bản ghi, ba chuỗi và số test |

Báo cáo và mọi bằng chứng ở repo cha trong `docs/codex-queue/210*`.
Không sửa kit, sim, content, audio, golden, input hay các file typing đang
thuộc TF2/191; không chạm game khác, worktree khác hoặc Tu Tiên.

## 2. Tám phần việc

1. **Bản ghi:** `survival.guide` là `{ "started": boolean, "hint": boolean }`,
   qua TextStore. Trống/hỏng trả hai cờ false. Có ải đã qua thì hai cờ true,
   kể cả bản ghi hướng dẫn hỏng. Hai thao tác ghi giữ cờ còn lại; lỗi ném
   hoặc trả false không chặn chơi.
2. **Loadout:** chỉ c1-s1 có bảng khuyên dùng `[GUN.xung, GUN.tia]`. Người
   chưa started và chưa có lựa chọn được chọn sẵn, cắt theo số bến; con trỏ
   đặt lên START. Cờ trong Journey ngăn chọn lại sau khi bỏ chọn hết, Esc
   rồi quay lại. Lựa chọn có sẵn giữ nguyên thứ tự; begin ghi started trước
   khi gọi host.start.
3. **Nhãn:** hai nhãn Recommended luôn có ở c1-s1, kể cả người đã started;
   ải khác không có. Phần tử `i.sv-rec` tách khỏi `em` BAY, trên mép trái;
   BAY vẫn ở mép phải. Giữ quy tắc tên súng không xuống dòng. Chưa có bằng
   chứng trình duyệt để kết luận nhãn không đè nhau ở hai độ phân giải.
4. **START:** đúng chuỗi ở mục 5; chỉ hiện khi chưa started và ready, ngay
   dưới nút, dùng sv-note và quy tắc không xuống dòng. Chờ Claude xác nhận
   vừa một dòng ở 1280 × 720.
5. **Gợi ý:** Hud.loads chỉ tăng khi full là false. LoadHint trả lời nhắc
   trong mode play trước lần nạp thứ hai, sau đó lưu hint một lần trong
   trang và ẩn; trang sau đọc cờ đã lưu. Áp dụng cả Trial lẫn ải 1. Thứ tự
   thông báo: IME → danh sách từ ngoại tuyến → gợi ý. setNotice mặc định
   warn vẫn nhận lời gọi một tham số; hint có lớp is-hint, viền xanh và bỏ
   ký tự bàn phím bằng content: none.
6. **Esc:** không sửa listener thẻ ải hoặc test cũ. 22/22 test intro-key
   xanh; Journey vẫn giữ bộ súng và thứ tự khi tải lại Loadout.
7. **Kịch bản:** hai file qua node --check, không chạy trình duyệt. File
   mới xóa hai bản ghi và lựa chọn phiên còn sót, tải lại để khởi tạo
   LoadHint mới, ghi picked/cursor/ready/số nhãn/chú thích, chụp Loadout;
   vào trận ghi chữ/lớp/trạng thái ẩn của notice và chụp. Ảnh mặc định vào
   `tmp/visual` của game khi Claude chạy từ gốc worktree. Không sinh ảnh
   trong lượt này nên không có raw frame cần prune.
8. **Changelog:** đã viết bằng tiếng Việt, đầy đủ số trước/sau và lý do
   TS-M1-11/G5; đường ở bảng trên.

## 3. Bảy mục kiểm

| # | Kiểm và số đo | Bằng chứng |
| --- | --- | --- |
| 1 | Trước mã: pnpm check mã 0, **265 test / 25 file**, kit **61/61**, TypeScript/Vite đạt. Sau mã: mã 0, **296 test / 26 file**, kit **61/61**, TypeScript/Vite đạt. Không có test thời gian đỏ nên không cần chạy riêng ba lần. | [Trước](210/check-before.log), [sau cuối](210/check-final.log) |
| 2 | Test mới trước mã: **26 đỏ / 5 xanh**, 31 test/1 file. Sau mã: **31/31 xanh**; cộng Esc **22** và English UI **5** là **58/58**, 3 file. Đột biến bỏ chọn sẵn: **3 đỏ / 28 xanh**; bỏ lưu hint: **2 đỏ / 29 xanh**; trả mã: **58/58 xanh**. | [Đỏ](210/test-red.log), [xanh](210/test-green.log), [bỏ chọn sẵn](210/mutation-preselect.log), [bỏ lưu](210/mutation-hint-save.log), [trả mã](210/test-restored.log), [mã thoát](210/mutation-exits.json) |
| 3 | Golden trước/sau cùng SHA-256 **42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea**. Chapter-hashes mỗi lần **152 dòng**, diff mã 0, rỗng. Test vocab-pin giữ bộ bài **7f073fa2**; golden **18/18** xanh trong check. | [Golden trước](210/golden-before.txt), [sau](210/golden-after.txt), [chương trước](210/chapter-before.txt), [sau](210/chapter-after.txt), [diff rỗng](210/chapter-diff.txt) |
| 4 | Git diff numstat main.ts: **5 thêm, 3 xóa = 8**, gồm cả 205. Riêng 210 **3 thêm, 1 xóa**, đúng ba vị trí. Đoạn listener VM không đổi; tests/intro-key.test.ts không đổi. | [Numstat](210/main-numstat.txt), [toàn diff](210/main-all.diff), [riêng 210](210/main-210.diff), [xác minh](210/verification.json) |
| 5 | Chỉ **3 chuỗi** người chơi thấy được thêm, đều tiếng Anh, liệt kê ở mục 5. tests/english-ui.test.ts **5/5 xanh**. Hai câu cảnh báo có sẵn chỉ chuyển sang hàm thuần, nội dung giữ nguyên. | [Test liên quan](210/test-restored.log) |
| 6 | node --check cả hai kịch bản mã **0**; không chạy kịch bản. | [Loadout](210/survival-s1-loadout.mjs.check.log), [first-run](210/survival-s1-first-run.mjs.check.log) |
| 7 | Cuối **26 đường** = 17 đường nền + 10 đường phiếu, trùng main.ts. **0 đường ngoài phạm vi**; screens-journey và CSS chỉ thêm dòng; git diff --check mã **0**. | [Status cuối](210/status-final.txt), [diff-check](210/diff-check.txt), [xác minh](210/verification.json), [script kiểm](210/verify.py) |

Build còn cảnh báo chunk trên 500 kB giống nền; không mở rộng sang tối ưu.

## 4. Các dòng main.ts của riêng 210

Thêm import và tạo LoadHint ngoài đoạn listener mà intro-key chạy:

```ts
import { LoadHint, noticeFor } from "./guide";
const loadHint = new LoadHint(safeLocalStorage);
```

Thay đúng dòng setNotice trong update:

```ts
// Before
hud.setNotice(imeNotice.on(now) ? "Switch to an English keyboard" : vocab.source === "fallback" ? "Offline word list (server words unavailable)" : "");
// After (one source line)
const notice = noticeFor(imeNotice.on(now), vocab.source === "fallback", loadHint.text(mode, hud.loads)); hud.setNotice(notice.text, notice.kind);
```

Giữ nguyên hai dòng của 205: truyền tier vào crowd/ship.load và truyền
world.header.kit.guns vào Combat. Bản before và bản vá riêng giúp Claude
tách theo thứ tự **205 → 207 → 210**, rồi đối chiếu 206 và 191.

## 5. Toàn bộ chữ người chơi thấy mới

- `Recommended`
- `Press Enter to start. Guns fire on their own; type words to load them.`
- `Type a word on a bay to load its gun`

Không thêm icon hoặc ảnh đế; nhãn hiện là chữ theo phiếu. Chờ icon thật
của 206 và icon bàn phím 149 do Claude gắn sau; nếu cần ảnh đế riêng thì
Claude mở phiếu ảnh, không vẽ thay bằng CSS/SVG/emoji ở đây.

## 6. Kịch bản khác có thể gặp gợi ý đầu trận

Theo mã nguồn, khi hồ sơ trình duyệt mới, chưa có cờ hint hay ải đã qua,
chưa nạp đủ hai lần và không có cảnh báo ưu tiên, các kịch bản sau có thể
thấy gợi ý trong những khung đầu trận:

- `survival-s0-balance.mjs`, `survival-s0-boot.mjs`,
  `survival-s0-fight.mjs`, `survival-s0-frames.mjs`,
  `survival-s0-keys.mjs`, `survival-s0-menu.mjs`, `survival-s0-perf.mjs`;
- `survival-s1-guns.mjs`, `survival-s1-hazards.mjs`,
  `survival-s1-latency.mjs`, `survival-s1-perf.mjs`,
  `survival-s1-stage.mjs`;
- `survival-feel.mjs`, `survival-feel-guns.mjs`,
  `survival-feel-ship.mjs`, `survival-vfx-pair.mjs`.

Hai thư viện s0-lib/s1-lib dùng autostart nên các kịch bản gọi chúng cũng
chịu điều kiện trên; đây là suy luận source, chưa phải quan sát chạy.
Không sửa chúng. Kịch bản menu cũng mở Trial trước khi tạm dừng, nên có
thể hiện lời nhắc trong quãng chơi đó. Loadout cũ đã thêm đúng một dòng
theo phiếu, nhưng vẫn
có assertion tiếng Việt từ trước (Hành trình/Trận thử/ẢI…); Claude cần
đối chiếu kết quả với đợt ngôn ngữ 130, không quy lỗi đó cho chọn sẵn.

## 7. Phần bỏ qua và cần chủ dự án/Claude xem

- Không chạy dev server, trình duyệt, mạng, tạo media, kit:sync hay Git ghi
  theo lệnh cấm. Không có ảnh/prompt/audio phát sinh. Build/test chỉ chạy
  đúng worktree này bằng các lệnh phiếu yêu cầu; không chạy game khác.
- Chưa đo cảm quan, độ vừa chữ, lớp đếm Hud thật hoặc hai lần nạp bằng tay;
  Node không dựng Hud theo phiếu. Không tuyên bố G5 đã được duyệt hình ảnh.
- Claude chạy first-run ở **1280 × 720** và **1920 × 1080** với hồ sơ mới:
  kiểm hai súng đúng thứ tự, hai nhãn tách BAY, chú thích một dòng và con
  trỏ START; Enter vào thẻ ải, Esc trở về giữ bộ súng; vào trận thấy hint,
  nạp thật hai lần thì tắt, tải lại vẫn tắt. Kiểm cả Trial. Nếu đang dùng
  từ ngoại tuyến, notice phải hiện cảnh báo ngoại tuyến thay hint đúng
  ưu tiên; cần nguồn từ hoạt động để chụp lời nhắc trong kịch bản mới.
- Chủ dự án duyệt chữ/nhãn và Claude duyệt trình duyệt trước khi commit,
  gộp cùng 206 (`.wt-ts-art`) và 191 (`.wt-ts-typefx`). Phiếu này không
  sửa hoặc giải quyết xung đột trong hai worktree đó.
