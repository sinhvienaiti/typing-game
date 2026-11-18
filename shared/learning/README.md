# Shared Learning Core

This folder owns the parent-platform learning contract and deterministic learning calculations.

## Versioning

- Learning Event: v1
- Learning Profile: v1
- IndexedDB database: `typingGameLearning`
- object store: `state`
- canonical profile key: `profile`
- recent mistake/answer bound: 8 samples per item

Child games must emit learning attempts. They must not independently calculate a competing canonical mastery score.

## Vocabulary identity

Vocabulary IDs use the same canonical rule as the shared vocabulary library:

```text
NFKC
-> trim
-> collapse whitespace
-> lowercase
```

EN/VI/IPA stay in `shared/vocabulary`; learning records store only the normalized key and aggregate history.

## Profile entities

The profile has three maps:

- `vocabulary`
- `grammar`
- `sentences`

Common aggregates include attempts, correct/wrong counts, hint/replay counts, average response time, correct streak, last-seen/correct/wrong timestamps, mastery, review priority, next-review time and source games.

Grammar/sentence records also keep bounded error classifications. Sentence records keep bounded recent answers.

Mỗi sự kiện ở cả ba loại thực thể còn thêm một mẫu vào `recentSamples`:
`{ occurredAt, gameId, activityType, result, hintUsed }`. `hintUsed` luôn là
boolean; mẫu không chứa `userAnswer` hay `expectedAnswer`. Danh sách theo
thời gian, giữ tối đa tám mẫu mới nhất, kể cả khi sự kiện đến muộn.
Bản ghi và bản sao lưu v1 cũ không có trường này vẫn đọc/nhập được;
lookup trả `[]` cho bản ghi cũ. Không dựng lại các mẫu lịch sử bị thiếu.

## Mastery v1

Mastery is deterministic and clamped to 0-100. It is a learning-strength indicator, not a literal percentage of knowledge.

Weights:

- correctness: 55
- correct streak: 20
- response speed: 10
- independence from hints/replays: 10
- recent successful recall: 5

## Review priority v1

Review priority is deterministic and clamped to 0-100.

Signals:

- low mastery: up to 55
- accumulated failures: up to 20
- staleness since successful recall: up to 15
- slow response: up to 5
- hint/replay dependence: up to 5

Initial next-review intervals are intentionally simple and deterministic:

- mastery 0-39: due now
- 40-69: +1 day
- 70-89: +3 days
- 90-100: +7 days

Later milestones may evolve the formula only through an explicit profile/event versioned migration.

## Persistence

`browser-store.mjs` persists the canonical parent profile in IndexedDB.

Writes are serialized so concurrent parent operations do not overwrite one another. Learning is recorded per completed attempt/event, not per physical keystroke.

L02 adds the cross-origin messaging bridge and batching/query API.

## Verification

Run:

```bash
pnpm learning:check
pnpm learning:test
```

The tests cover event validation, vocabulary key normalization, deterministic aggregates, bounded history, grammar error classification, sentence answer history and review-priority ordering.

## Cross-origin bridge

The Portal is the only canonical Shared Learning owner.

Child games communicate through the versioned namespace:

```text
typing-game:learning:v1:attempt
typing-game:learning:v1:query
typing-game:learning:v1:lookup

typing-game:learning:v1:ack
typing-game:learning:v1:query-result
typing-game:learning:v1:error
```

The Portal accepts a request only when:

- the sender is the currently mounted iframe;
- the origin exactly matches that game's registry `appUrl` origin;
- the message passes the shared schema parser;
- Attempt `gameId` matches the active game.

Attempt persistence is batched (maximum 32 per write, short debounce) and serialized through the parent IndexedDB store. Query requests flush older pending attempts first so review reads do not miss acknowledged learning work.

Current query contract supports:

- `entityType`: vocabulary / grammar / sentence;
- `page`;
- `pageSize`: 10 / 25 / 50 / 100;
- `search`;
- filters for status, source game, mastery range, due-only and last-mistake date range;
- deterministic sorts including Smart Priority, mastery, mistakes, recency, review age, response speed, attempts and A-Z/Z-A.

Child-specific adapters are added only in their integration milestones. L02 defines and validates the parent transport; it does not duplicate Smart Review logic in children.

### Tra bản ghi theo danh sách id

Mọi game đang mở trong iframe, có nguồn khớp `appUrl` trong registry, có
thể gửi lookup. Tin không mang `gameId`; portal dùng game đang mở để kiểm
nguồn, giống attempt và query.

```json
{
  "type": "typing-game:learning:v1:lookup",
  "requestId": "lookup-1",
  "query": {
    "entityType": "vocabulary",
    "entityIds": ["Lantern ", "dragon"]
  }
}
```

`entityType` bắt buộc là `vocabulary`, `grammar` hoặc `sentence`.
`entityIds` chứa 1–200 chuỗi **trước khi bỏ trùng**; mỗi chuỗi tối đa
200 ký tự sau `trim()`. Từ vựng chuẩn hóa theo quy tắc NFKC ở trên;
grammar/sentence chỉ `trim()`. Bỏ id rỗng và trùng, giữ thứ tự lần đầu;
danh sách còn rỗng là lỗi. Các trường lạ trong `query` được bỏ qua.

Portal ghi hết attempt đang chờ trước khi đọc hồ sơ. Tra cứu dùng khóa
trực tiếp, bỏ id chưa có và các khóa nguyên mẫu như `constructor`,
`__proto__`, `toString`. Tin trả có cùng `requestId` và dạng sau
(`items` là mảng item đầy đủ, ví dụ rỗng khi chưa học từ nào):

```json
{
  "type": "typing-game:learning:v1:query-result",
  "requestId": "lookup-1",
  "result": { "entityType": "vocabulary", "items": [] }
}
```

Mỗi item gồm các trường bản ghi, `entityType`, `entityId`, `mastery`,
`reviewPriority`, `status` và luôn có `recentSamples`. Điểm được tính
lại tại thời điểm tra cứu; ngày ôn và các bộ đếm giữ nguyên. Thứ tự item
theo id yêu cầu đã chuẩn hóa. Lookup chỉ đọc hồ sơ, không gọi `onApplied`.

Tin hỏng nhận `typing-game:learning:v1:error` với cùng `requestId`,
`error: { code: "invalid-request", message: "..." }`. Kho lỗi khi đọc
nhận cùng dạng với mã `query-failed`. Thông báo lỗi là tiếng Anh.
`requestId` hỏng, sai cửa sổ/nguồn hoặc chưa mở game thì không trả lời.

## Smart Review Dashboard

The parent Portal exposes `/review` as the canonical Smart Review inspection screen.

It queries the local parent profile with bounded pagination and supports:

- Words / Grammar / Sentences;
- quick and advanced profile filters;
- Topic / Word type / Level / Grammar curriculum filters;
- URL-persisted search/sort/filter/page state;
- responsive desktop/mobile presentation;
- item details and Why Review explanations.

Vocabulary rows resolve EN/VI/IPA lazily from the existing shared vocabulary levels. The learning database stores only the canonical vocabulary key and learning history.

## Review Planner and Session Core

`review-session.mjs` is the single parent Smart Review planner.

It owns review-set semantics, ordering, capability matching, item limits, source filters and the canonical At Risk rule. The Portal uses it from `/review/build` and persists the current plan in parent session storage for `/review/session`.

Child games do not implement their own Smart Review planner. Their later adapters only consume parent-selected review material and emit normal Learning Events back to the parent.
