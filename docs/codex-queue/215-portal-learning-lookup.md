# Phiếu 215 · Cổng game và `shared/learning` · Trả lời tin `typing-game:learning:v1:lookup` (portal đang từ chối, Dragonhold coi từ đã học là từ mới)

**Nguồn:**
- `docs/games/SPLIT_PLAN.md` §9.2, hàng "Truy vấn học": "Thêm `typing-game:learning:v1:lookup` theo danh sách ≤ 200 `entityId`, trả cả `recentSamples`".
- `docs/games/DEPLOY_INDEPENDENCE.md` §7, hàng 6: "portal từ chối tin `lookup` của Rồng". Cách sửa ghi ở đó: "một bộ xử lý `lookup` theo `gameId`. Thêm game không cần sửa portal".
- `docs/games/dragon-lane/01-core-combat-learning.md` §6.8, hàng thứ ba: lookup cần trả `recentSamples` vì §6.3 cần số lần nhớ đúng.
- `docs/games/MAP1_PRODUCTION.md`, DH-04 (cổng G7): chơi qua cổng game thì "cầu học nhận sự kiện".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Hiện trạng (Claude đã đọc mã):**
- Kit gửi lookup: `shared/game-kit/learning/bridge.ts:166-174`, chờ tối đa 2000 ms (`:55`, `:237-240`). Tin là `{ type, requestId, query: { entityType, entityIds } }`. Kit đã chuẩn hóa và bỏ trùng id trước khi gửi.
- Dragonhold gọi lookup khi dựng bộ từ: `games/dragon-hold/src/app/learning.ts:330`, đọc kết quả bằng `parseLookup` (`:170-194`).
- Portal không có nhánh lookup. `shared/learning/message-contract.mjs:57` ném "learning message type is not supported"; `portal/src/learning/bridge.ts:106-119` trả `error` ngay.
- Ghi chú nguồn nói mỗi ải chờ tới 2 s. Theo mã thì portal trả `error` ngay; chờ đủ 2 s chỉ khi origin hai bên lệch. Đường nào cũng ra một kết quả: Dragonhold không có bản ghi của portal, từ đã học ở game khác bị coi là mới.
- Lõi chung chưa lưu mẫu trả lời đúng cho từ vựng. Bản ghi chỉ có `recentMistakes` (câu sai). `recentAnswers` chỉ có ở câu (sentence), không có `activityType`.

**Không trùng:** 105, 105b, 187 (nút và đường về cổng của Dragonhold), 188 (kiểm giấy phép), 207, 208 (nguồn cổng lúc build của Last Line, Wordwoven).

**Báo cáo:** `docs/codex-queue/215-report.md` (tiếng Việt), thư mục `docs/codex-queue/215/`.

## Nơi làm

- Repo cha, chạy từ gốc `/Users/toandx/htdocs/typing-game`. Nhánh lúc viết phiếu: `feat/space-typing-admin-uiux`. Nhánh khác thì ghi lại, không đổi nhánh.
- Chỉ sửa:
  - `shared/learning/core.mjs`, `query.mjs`, `message-contract.mjs`, `profile-backup.mjs`, các `.d.mts` của chúng, test của chúng, `shared/learning/README.md`;
  - `portal/src/learning/bridge.ts`, `portal/tests/learning-bridge.test.mjs` (hay một file test mới trong `portal/tests/`);
  - `docs/changelog/<ngày>-portal-learning-lookup.md` (mới; không sửa `docs/changelog/README.md`, Claude thêm hàng khi commit);
  - báo cáo và thư mục `docs/codex-queue/215/`.
- **Chạy sau phiếu 214** (cùng làn P10, cũng sửa `portal/`). Trước khi làm, chạy `git status --short -uall -- portal shared/learning docs/changelog` và `git branch --show-current`:
  - sạch: làm tiếp;
  - chỉ có file của 214 vì Claude chưa commit (đối chiếu `docs/codex-queue/214-report.md`): làm tiếp, không đụng phần của 214, ghi danh sách vào báo cáo. Trước khi sửa một file mà 214 cũng sửa, chép nó vào `215/before/`;
  - có file lạ khác: dừng, ghi vào báo cáo.
- Được dùng git chỉ đọc. Test trước, mã sau. Chú thích tiếng Anh, ngắn.
- Phiếu này không có chữ người chơi thấy. Thông báo lỗi trong tin trả về là tiếng Anh.

## Đọc trước

- `portal/src/learning/bridge.ts` (cả file): kiểm nguồn ở `:70-80`, cách trả query ở `#handleQuery`.
- `shared/learning/message-contract.mjs` và `.d.mts`; `query.mjs` (`queryLearningProfile`, cách dựng một item ở `:284-295`); `core.mjs` (`applyParsedLearningEvent`, `boundedAppendChronological`, `MAX_RECENT_SAMPLES = 8`, `normalizeVocabularyKey`); `profile-backup.mjs` (`validateSamples`, `validateRecord`).
- `portal/tests/learning-bridge.test.mjs`: mẫu khung giả, kho giả, ba origin sai.
- Chỉ đọc, không sửa: `shared/game-kit/learning/bridge.ts`, `contract.ts` (tên tin và `LOOKUP_MAX_IDS = 200`); `games/dragon-hold/src/app/learning.ts:20-30` (`RECALLS`, `isRightRecall`) và `:170-194` (`parseLookup`). Ghi HEAD của `games/dragon-hold` vào báo cáo.

## Việc

1. **Mốc đầu**, trước khi sửa mã:
   - ghi nhánh, HEAD, trạng thái git của các đường dẫn ở mục "Nơi làm"; lưu `git status --short -uall` của cả repo vào `215/status-before.txt` (repo cha đang bẩn vì việc khác);
   - chạy `pnpm learning:test`, `pnpm portal:test`, `pnpm --dir portal build`; lưu số test và kết quả vào `215/baseline.json`;
   - viết `215/core-snapshot.mjs`: áp một dãy cố định 12 sự kiện (ba từ; có `typing-attack`, `meaning-recall`, `listening`, `review-card` có và không có `hintUsed`; có câu sai; một sự kiện đến muộn) lên hồ sơ trống, in bản ghi ra JSON (bỏ trường `recentSamples` nếu có, khóa giữ thứ tự). Chạy trên mã chưa sửa, lưu `215/core-before.json`.
2. **Test trước** (mục "Test" bên dưới). Chạy, ghi số đỏ vào `215/tests-before.json`.
3. **Lõi lưu mẫu gần đây** (`core.mjs`):
   - Mỗi sự kiện, mọi loại thực thể, thêm một mẫu vào `record.recentSamples`: `{ occurredAt, gameId, activityType, result, hintUsed }`. `hintUsed` luôn là boolean.
   - Dùng `boundedAppendChronological`: theo thời gian, giữ 8 mẫu mới nhất.
   - Không lưu `userAnswer`, `expectedAnswer` vào mẫu này.
   - `mastery`, `reviewPriority`, `nextReviewAt`, mọi bộ đếm và các danh sách cũ giữ nguyên từng số. Bản ghi cũ không có trường này vẫn đọc được.
4. **Hợp đồng tin** (`message-contract.mjs`, `.d.mts`):
   - Thêm `LEARNING_LOOKUP_MESSAGE = "typing-game:learning:v1:lookup"` và `LOOKUP_MAX_IDS = 200`, cùng giá trị với kit.
   - `parseLearningMessage` nhận loại lookup, trả `{ type, requestId, lookup }`. `lookup` do `parseLearningLookup(value.query)` dựng.
   - `parseLearningLookup` (để ở `query.mjs`, cạnh `parseLearningQuery`):
     - `query` phải là object thuần; `entityType` là `vocabulary`, `grammar` hay `sentence`, bắt buộc;
     - `entityIds` là mảng chuỗi, độ dài mảng 1–200. Hơn 200 thì lỗi, kể cả khi có id trùng;
     - mỗi id dài tối đa 200 ký tự sau khi cắt khoảng trắng;
     - chuẩn hóa: từ vựng dùng `normalizeVocabularyKey`; loại khác chỉ `trim()`, như kit;
     - bỏ id rỗng, bỏ trùng, giữ thứ tự lần đầu gặp. Không còn id nào thì lỗi;
     - trường lạ trong `query` bị bỏ qua, như `parseLearningQuery`.
   - Tin lookup không mang `gameId`. Không thêm trường mới vào hợp đồng.
5. **Tra bản ghi** (`query.mjs`, `.d.mts`): hàm mới `lookupLearningRecords(profile, lookup, now)`.
   - Tra thẳng bằng `Object.hasOwn` trên bộ sưu tập đúng loại. Không quét cả hồ sơ, không gọi `queryLearningProfile`.
   - Id không có bản ghi thì bỏ khỏi kết quả. Id như `constructor`, `__proto__`, `toString` không bao giờ trả bản ghi.
   - Mỗi item dựng giống item của `queryLearningProfile`: `{ ...record, entityType, entityId, mastery, reviewPriority, status }`, `mastery` và `reviewPriority` tính lại tại `now`. Tách phần dựng item thành một hàm dùng chung; kết quả của `queryLearningProfile` không đổi.
   - Mỗi item luôn có `recentSamples`: mảng của bản ghi, hay `[]` khi bản ghi cũ chưa có.
   - Kết quả: `{ entityType, items }`. `items` theo thứ tự id đã chuẩn hóa của yêu cầu. Đây là dạng `{ items: [...] }` mà `parseLookup` của Dragonhold đọc.
6. **Portal trả lời** (`portal/src/learning/bridge.ts`):
   - Kiểm nguồn y như attempt và query: `event.source` là iframe đang mở, `event.origin` là origin của `appUrl` game đang mở. Sai thì nuốt tin, không trả lời. Chưa mở game thì cũng nuốt.
   - Game được trả lời là game đang mở. Không gắn cứng id game nào: game có trong `portal/public/games.json` thì lookup chạy được.
   - Tin hỏng (sai dạng, hơn 200 id, id quá dài, `entityType` lạ): trả `error` mã `invalid-request`, cùng `requestId`, qua nhánh `catch` sẵn có. `requestId` hỏng thì không trả lời, như hiện nay.
   - Tin hợp lệ: `await this.flush()` trước (để từ vừa gõ có mặt), rồi `store.load()`, rồi `lookupLearningRecords`. Trả `query-result` cùng `requestId`, `result` là kết quả mục 5.
   - Kho lỗi khi đọc: trả `error` mã `query-failed`, cùng `requestId`.
   - Lookup chỉ đọc. Không ghi gì vào hồ sơ, không gọi `onApplied`.
   - Rẽ nhánh theo `message.type`, không theo `"event" in message`. Nhánh attempt và query giữ nguyên hành vi.
7. **Sao lưu hồ sơ** (`profile-backup.mjs`): `recentSamples` là tùy chọn. Có thì dùng `validateSamples` (≤ 8 mẫu, mỗi mẫu là object). Bản sao lưu cũ không có trường này vẫn nhập được.
8. **Tài liệu:**
   - `shared/learning/README.md`: thêm tin lookup (dạng hỏi, dạng trả, giới hạn 200, mã lỗi) và trường `recentSamples`.
   - Changelog `docs/changelog/<ngày>-portal-learning-lookup.md`: đổi gì, vì sao, số test trước và sau.
9. **Danh sách cho Claude** trong báo cáo (Claude sửa, Codex không sửa), kèm số dòng:
   - chú thích "the portal may not answer it yet" ở `shared/game-kit/learning/contract.ts`;
   - chú thích "its lookup may lack recent samples" ở `games/dragon-hold/src/app/learning.ts`;
   - `SPLIT_PLAN.md` §9.2, `DEPLOY_INDEPENDENCE.md` §7 hàng 6, `01-core-combat-learning.md` §6.8.

## Test (viết trước, ghi số đỏ trước khi sửa mã)

Portal (`portal/tests/`), dùng khung giả và kho giả như test hiện có. Kho giả cho lookup giữ một hồ sơ thật dựng bằng `applyLearningEvents`.

1. **Ba game:** `dragon-hold`, `typing-defense`, `typing-survival`, mỗi game từ origin đăng ký trong `games.json`. Đúng một tin gửi đi: `query-result`, cùng `requestId`, `targetOrigin` là origin của `appUrl`.
2. **Sai nguồn:** ba origin sai của test cũ và một cửa sổ lạ. Không tin nào gửi đi; `store.load` không được gọi.
3. **Giới hạn 200:** 200 id thì có kết quả; 201 id thì `error` `invalid-request`, `store.load` không được gọi.
4. **Từ mới vắng mặt:** hồ sơ có `lantern`; hỏi `["Lantern ", "dragon", "constructor"]`. `items` chỉ có `lantern`, `entityId` là `"lantern"`.
5. **Tin hỏng:** `query` không phải object; `entityIds` không phải mảng; phần tử không phải chuỗi; id 201 ký tự; `entityType` lạ; mảng rỗng; mọi id rỗng sau cắt. Mỗi ca một `error` `invalid-request` cùng `requestId`.
6. **Thứ tự ghi rồi đọc:** một attempt rồi một lookup trong cùng nhịp. Kết quả lookup có bản ghi của attempt đó.
7. **Kho lỗi:** `load()` ném lỗi thì trả `error` `query-failed`.
8. **Chỉ đọc:** sau lookup, hồ sơ giữ nguyên (so `structuredClone`), `onApplied` không được gọi.
9. **Khớp `parseLookup`:** viết trong test một bộ đọc chép đúng luật của `parseLookup` và `isRightRecall` (`games/dragon-hold/src/app/learning.ts:20-30`, `:170-194`; ghi HEAD Dragonhold trong chú thích). Không import file của game.
   - Hồ sơ của `lantern`: `typing-attack` đúng; `meaning-recall` đúng, không gợi ý; `review-card` đúng, có `hintUsed`; `listening` đúng; `meaning-recall` sai.
   - Bộ đọc phải ra: `lantern` có `recalls = 2`, `mastery` bằng `calculateMastery` tại `now`, `nextReviewAt` là chuỗi ngày giờ.
10. Test attempt và query hiện có vẫn xanh, không sửa.

Lõi (`shared/learning/*.test.mjs`):

11. `parseLearningMessage` nhận lookup; giá trị tên tin và giới hạn 200 khớp kit. Test đọc `shared/game-kit/learning/contract.ts` dạng văn bản và so hai hằng số, không import kit.
12. `parseLearningLookup`: chuẩn hóa, bỏ trùng, giữ thứ tự, các ca lỗi của test 5.
13. `lookupLearningRecords`: thứ tự theo yêu cầu, id vắng mặt bị bỏ, khóa nguyên mẫu (`__proto__`…) không ra bản ghi, bản ghi cũ không có `recentSamples` thì trả `[]`.
14. Lõi: `recentSamples` đúng năm trường, theo thời gian, tối đa 8, sự kiện đến muộn chen đúng chỗ; không có `userAnswer`.
15. Sao lưu: nhận bản ghi có `recentSamples` ≤ 8; từ chối 9 mẫu hay mẫu không phải object; bản cũ không có trường vẫn nhập được.
16. Test của `review-session`, `mixed-review`, `adaptive-mix` và các `*-review-dataset` xanh, không sửa.

## Cấm

- Mọi lệnh git có ghi.
- Sửa `games/**` (mọi repo game, mọi worktree `.wt-*`), `shared/game-kit/**`, chạy `kit:sync`.
- Sửa Smart Review và Space: `portal/src/review/**`, `portal/src/main.ts`, `shared/learning/review-session.mjs`, `mixed-review.mjs`, `adaptive-mix.mjs`, `*-review-dataset.mjs`, `games/space-typing/**`.
- Sửa `portal/public/games.json`, `docs/games/**`.
- Đổi công thức độ thuộc, độ ưu tiên, ngày ôn; đổi phiên bản hồ sơ (`version: 1` giữ nguyên).
- Thêm trường `gameId` hay trường mới khác vào tin lookup.
- Dev server, trình duyệt, mạng. Đụng Tu Tiên. Tạo media.

## Kiểm (ghi số)

1. `pnpm learning:test`: số file, số test, số đạt; trước và sau. `pnpm learning:check` xanh.
2. `pnpm portal:test`: số test, số đạt; trước và sau.
3. `pnpm --dir portal build` xanh (`tsc` và `vite build`). `portal/dist` nằm ngoài Git; không đưa vào báo cáo.
4. Số đỏ trước sửa và số xanh sau sửa của các test mới; log ở `215/`.
5. Chạy lại `215/core-snapshot.mjs` sau khi sửa, lưu `215/core-after.json`. Hai file phải giống hệt từng byte; ghi SHA-256 cả hai.
6. Đo lookup 200 id trên hồ sơ 5.000 từ (Node, trung vị 20 lần). Ghi số ms vào `215/lookup-timing.json`. Mục tiêu dưới 20 ms; vượt thì ghi lý do, không tối ưu thêm.
7. `git status --short -uall` sau khi làm, lưu `215/status-after.txt`: phần chênh so với `215/status-before.txt` chỉ là các đường dẫn ở mục "Nơi làm". File của 214 chưa commit đã có trong `status-before.txt`; liệt kê riêng trong báo cáo. `git diff --check` trên các file phiếu này sửa: mã 0.

**Xong khi:** chín việc và bảy mục kiểm đạt, có số trong báo cáo. Claude duyệt rồi commit, sửa các chú thích và tài liệu ở việc 9, build lại portal, rồi kiểm một lần trong trình duyệt (`https://typing-game.local`, vào Dragonhold): tin lookup nhận `query-result`, không `error`, không chờ 2 s, và từ đã học ở game khác không còn là từ mới.
