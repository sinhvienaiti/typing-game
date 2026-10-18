# Kiến trúc và contracts hiệu chỉnh

Các schema/API dưới đây là **thiết kế đích để viết implementation spec**, không phải migration đã chạy hay API đã tồn tại. Mục tiêu là một authority cho từng loại state, giữ đường học hoạt động khi meta hỏng.

## 1. Từ nền hiện có đến kiến trúc đích

Repo hiện tại có portal và các game repo độc lập, shared learning với IndexedDB, contract `typing-game:learning:v1`, parent music, Node local admin. Bằng chứng chọn lọc: [README](../../README.md), [learning bridge](../../shared/learning/message-contract.mjs), [browser store](../../shared/learning/browser-store.mjs), [project context](../../docs/PROJECT_CONTEXT.md), [local admin](../../admin/server.mjs). Local admin hiện bind loopback và có token phát triển; không tái dùng cấu hình đó như auth production.

Giữ portal/game separation. Backend mới bắt đầu bằng **modular monolith + PostgreSQL + object storage**, worker cùng codebase; không Kafka/microservice cho từng file. Chưa đưa Redis vào core learning; chỉ thêm khi presence/cache/workload cho thấy cần. Tách domain là tách quyền ghi và contract, không bắt buộc tách database/network hop.

Published content có thể là artifact trên CDN; DB giữ metadata/version/rights/publication pointer. Private responses, attempts và learner state nằm server. Browser dùng cache/outbox cho trải nghiệm; client không quyết định earned credit, rank hay server progress. Practice local vẫn được, nhưng có nhãn trust và sync status.

Trong monolith, synchronous typed service call đủ cho validation cần tức thì. Một use-case transaction được gọi các owner qua unit-of-work đã định nghĩa, không ghi lén bảng nhau. Reporting dùng read model/view được owner công bố; không cấm tuyệt đối SQL join rồi đổi thành mạng lưới event không cần thiết. Outbox dành cho side effect bền vững sau commit; analytics tách khỏi financial/learning truth.

## 2. Quyền sở hữu cuối cùng

| Owner | Sở hữu state/command | Chỉ đọc/tham chiếu | Không sở hữu |
|---|---|---|---|
| Platform identity/access | account, session, role binding, privacy preference, audit infrastructure | classroom scope | learning level, rank, NPC persona |
| Content | content_item/sense, immutable versions, lesson/course/exam definitions, rights/publication | media asset refs | learner attempts/mastery |
| Learning | lesson_session, checkpoint, accepted attempt/evidence, mastery projection, review queue, course completion | immutable content versions | cosmetic balance, chat, leaderboard |
| Activities | input loop/game state; adapter validation; activity-specific run detail | canonical item/session IDs | shared mastery, academy credits |
| Classroom | cohort/class membership, teacher assignment, class session/phase, assignment, academic term | lessons và learner progress API | lesson source, wallet, human role qua NPC |
| Social | room/messages/friends/invites, ephemeral presence | membership/access policy | class curriculum, assessment score |
| Safety | report cases, enforcement actions, moderator queue, retention policies | scoped evidence | global quyền giáo viên hay runtime content |
| Economy | item catalog, offer/price, wallet/ledger, reward rules/grants, entitlement/ownership, orders | accepted learning evidence, award proofs | grading, avatar asset pixels |
| Avatar | compatible render definitions, loadouts/presets | item entitlement và media manifest | catalog price, inventory copy |
| Competition/Prestige | competition season/ruleset, verification decision, entries, final result revisions, awards | activity/assessment results | all-purpose mastery hoặc campaign scheduler |
| LiveOps | campaign và occurrences, announcements, eligibility config | activity/course/offer refs | academic term, competition result finalization |
| Media/design system | asset files/manifests, generation jobs, cue/tokens/compatibility pipeline | rights approval | currency rules/earned status |
| NPC | labeled presenter templates, optional scoped fact cache | consented learning summary | teacher authority, mastery/wallet mutation |
| Admin | UI/workflows gọi owner; audit views | all allowed owner APIs | bản sao tất cả entity hay universal state database |

`product`, `review`, `brand` là trách nhiệm thiết kế/tài liệu; không tự sinh runtime service. `ielts` là curriculum + assessment adapter, chưa cần bounded context database độc lập. Calendar/Reward Center/Codex/Hall of Fame là read models, không authority mới.

## 3. Content và learning data contract

### Canonical content

- `content_items(id, kind, stable_key, sense_id?, status)`; unique key theo namespace và sense. Không dedupe chỉ vì cùng từ.
- `content_versions(id, content_id, version, payload_hash, schema_version, body_ref, rights_review_id, published_at)`; unique `(content_id,version)`. Published immutable; sửa bằng version mới.
- `lesson_versions(id, lesson_id, version, objective_ids, expected_duration_range, status)` và `lesson_steps(lesson_version_id, step_id, ordinal, activity_type, content_version_id, assessment_policy_version)`; unique ordinal và step trong version. Không bắt collaboration trong mọi lesson.
- `course_versions` + course-unit/lesson refs; completion denominator gắn version. `exam_spec_versions` lưu format/rules; `rubric_versions` chấm assessment mở.
- Đáp án/rubric bí mật không nằm trong public payload được prefetch; public exercise và private answer key tách quyền truy cập.
- `rights_reviews` lưu nguồn, quyền sử dụng được duyệt, bằng chứng, attribution, derivative chain và expiry nếu có. Publish kiểm quyền của toàn asset tree. Đây là workflow kiểm quyền, không tự động kết luận pháp lý từ nhãn license.

### Learning execution

- `lesson_sessions(id, user_id, lesson_version_id, mode, status, checkpoint_revision, started_at, completed_at)`.
- `attempts(id, user_id, session_id, step_id, content_version_id, source_activity, client_event_id, payload_hash, trust_tier, received_at, occurred_at_claimed, policy_version, status)`; unique `(user_id,source_activity,client_event_id)` cộng semantic key theo loại bài.
- `attempt_evidence(attempt_id, skill_id, item_or_sense_id, modality, outcome, hints_used, exposure_kind, rubric_version?, assessor_kind)`; one attempt có thể có nhiều evidence, không nhân thành nhiều grant nếu cùng source.
- `mastery_projection(user_id,item_or_sense_id,skill_id,model_version,estimate,uncertainty,evidence_count,last_qualified_at)` và `review_queue(user_id,item_or_sense_id,skill_id,due_at,policy_version)`; index `(user_id,due_at)`.
- `assessment_runs` dùng chung underlying session/attempt IDs. IELTS-specific detail lưu extension theo run: section, exam_spec_version, scoring/rubric refs. Không thêm bộ `ielts_attempts` song song tự tính progress.

**Chốt semantics:** completion = làm đủ bước hợp lệ; accuracy = đúng trên bộ task cụ thể; mastery estimate = suy luận có uncertainty; course level = nhãn curriculum; CEFR proficiency/IELTS band = assessment khác, không derive từ XP/WPM. Nhập từ nhìn thấy là spelling/copy evidence; không tự thành recall/listening evidence. Hints/reveal làm thay đổi evidence weight.

V1 dùng rule-based review tái sử dụng core hiện có, pin algorithm version; thêm delayed recall và giới hạn conclusions. UI nên nói “cần ôn/đã luyện/nhớ qua các lần kiểm tra” thay “mastered” chỉ sau một lần đúng. Recompute model version mới trong shadow projection; không sửa dữ liệu gốc để làm đẹp kết quả. Không reset learning history theo season, nhưng mastery estimate và review priority vẫn có thể thay đổi theo quên kiến thức hoặc evidence mới; “permanent progression” không có nghĩa nhớ vĩnh viễn.

### API tối thiểu

| Command/query | Input chính | Kết quả và invariant |
|---|---|---|
| `POST /v1/lesson-sessions` | lesson_version_id, mode, idempotency key | server xác định user; session pin version, không client tự chọn private answer key |
| `POST /v1/attempts` | session_id, step_id, content_version_id, client_event_id, response/evidence, contract_version | 201 mới / 200 retry cùng payload / 409 cùng key khác payload; trust do server cấp |
| `PATCH /v1/lesson-sessions/{id}/checkpoint` | expected_revision, checkpoint | scope owner; 409 nếu conflict; không last-write-wins làm mất step |
| `POST /v1/lesson-sessions/{id}/complete` | idempotency key | server kiểm required steps; retry trả cùng completion |
| `GET /v1/review-queue?cursor=...` | bounded page | private summary, no toàn history; policy/model version và sync status |
| `POST /v1/content/lessons/{id}/publish` | draft_revision, expected_published_revision | role content publisher; snapshot, rights validation, audit trong transaction |

Session transition: `created → active → completed` hoặc `abandoned`; resume không tạo session mới vô hạn để farm. Practice có thể retry tự do nhưng chỉ evidence đủ điều kiện được tính vào milestone. Invalid/late/untrusted không làm mất quyền xem feedback học tập, chỉ hạn chế state giá trị cao.

Server acceptance means contract/policy checks passed, không chứng minh browser không gian lận. Không đặt answer `correct=true`, `mastery_delta`, `credits` từ client vào authority.

## 4. Event và consistency

Domain event phát sau mutation hợp lệ; envelope đề xuất:

```json
{
  "event_id": "uuid",
  "event_type": "learning.attempt.accepted",
  "schema_version": 1,
  "aggregate_id": "attempt-id",
  "aggregate_revision": 1,
  "occurred_at": "server-instant",
  "correlation_id": "session-id",
  "causation_id": "command-id",
  "payload": {
    "user_id": "internal-id",
    "attempt_id": "attempt-id",
    "content_version_id": "version-id",
    "evidence_policy_version": 1,
    "trust_tier": "server_accepted"
  }
}
```

Tên event không dùng `outbox.event.created` làm business contract. Event public không chứa raw answer/chat/voice hoặc PII thừa. Consumers cần scope phù hợp để resolve reference. Schema event thay đổi có compatibility policy và contract fixtures cho repo cha/con.

Writer transaction ghi state + outbox row. Worker giao ít nhất một lần; consumer transaction ghi `processed_events(consumer,event_id)` unique + side effect. Crash sau commit nhưng trước ack không cấp thưởng lại. Replay giữ event_id; replay projection không tự phát reward mới. Event có sequence per aggregate, consumer xử lý stale/duplicate; không giả định total order toàn hệ thống. Retry có backoff, dead-letter và operator replay có audit. Outbox không tự tạo exactly-once delivery; [AWS nêu cần xử lý idempotent ở consumer](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html).

Immediate learner feedback không đợi Reward/Prestige/Social. API completion trả durable learning receipt; reward UI hiển thị pending nếu worker chưa xong. Projection lag có SLO đề xuất riêng. Nếu Learning và Economy chung DB, vẫn giữ logical ownership; không đưa economy failure vào transaction làm mất attempt.

## 5. Economy tối thiểu khi mở V2

V1 không cần currency. V2 chọn một earned Credit, không đổi tiền, không trade, không crystal/fragment/event token mặc định. Cosmetic thường không hết hạn để tránh biến nghỉ học thành mất quyền lợi.

### Invariants

1. Số Credit là integer, không floating point. `wallet(user_id,currency)` unique; spend không âm.
2. `ledger_transactions` và immutable `ledger_entries`: mỗi transaction cân bằng tổng delta theo currency giữa user account và issuance/sink/reversal account. Issuance không giả vờ là user kiếm từ một ví hữu hạn.
3. Wallet balance là cached projection cập nhật trong cùng transaction ledger. Có reconciliation bằng tổng entries; không dùng Redis balance để authorize mua.
4. `reward_grants` unique `(user_id, source_type, source_id, reward_rule_version, benefit_key)`. Không chỉ unique request ID: gửi request khác vẫn cùng một milestone.
5. `item_entitlements` unique `(user_id,item_id)` cho cosmetic non-consumable; item instance/serial riêng khi thật sự cần scarcity. Avatar không giữ bản sao inventory.
6. Purchase ghi order + debit + entitlement + outbox atomically; entitlement acquisition policy checked server-side. `award_only` không mua được kể cả qua admin chung.
7. Historical ledger không bị edit/delete để sửa sai; correction/reversal transaction có reference và reason. Nếu đã tiêu reward bị revoke, chọn freeze/future-offset/manual review policy rõ; không âm ví bất ngờ hoặc xoá learning progress.

### Purchase contract và concurrency

`POST /v1/purchases` nhận `offer_id, offer_version, quantity=1, idempotency_key`; user/cost/currency/eligibility tính server. Lưu request payload hash; duplicate cùng key cùng body trả receipt cũ; khác body trả 409. Với giá đã đổi, trả stale-offer và giá mới để người dùng xác nhận lại, không im lặng dùng giá mới.

Trong transaction: lock wallet; validate balance/offer/ownership; reserve capped stock nếu có; ghi debit/order/ownership; commit. Dùng ordering nhất quán khi cần nhiều lock; bounded retry serialization/deadlock. Đừng chỉ “kiểm balance rồi update” ở hai query không được bảo vệ. `FOR UPDATE` khóa row đối với writer khác theo [PostgreSQL docs](https://www.postgresql.org/docs/current/explicit-locking.html); ứng dụng vẫn phải thiết kế unique constraints và idempotency đầy đủ.

Claim-all chỉ cho benefit không cần lựa chọn; tốt hơn auto-grant và Reward Center là receipt list. Choice reward có claim transaction riêng, một lựa chọn duy nhất. Local daily period dùng timezone đã chốt, period_id ổn định, không cho timezone hop mint lại.

### Cân bằng economy

Không chốt tỷ lệ earning bằng cảm giác. Mô hình thử: vài qualified goals/tuần, giá item = số tuần trải nghiệm có ý nghĩa × earning percentile mục tiêu. Báo cáo P10/P50/P90 time-to-first-item, max earn, source mix, source/sink và catalog exhaustion; so solo với class/game path. Offline/legacy không mint. Cap toàn benefit window ngăn stacking daily+weekly+event trên cùng evidence.

Simulator dùng cùng evaluator production dưới input fixtures, không credentials production; kiểm replay/duplicate/burst/absence/timezone/farm và người học chậm. Không tăng giá hoặc làm mất tiền chỉ để tạo sink; khi catalog cạn, chấp nhận người dùng không cần chi mỗi tuần.

## 6. Classroom, teacher, NPC và social

Class là cohort theo curriculum, không bản sao course; `class_memberships(class_id,user_id,role,status,joined_at,left_at)` và teacher binding có lifecycle. Capacity là config và join atomic; V2 bắt đầu pilot 8–12 người như một giả thuyết vận hành, rồi thử dải 15–30 của nguồn. Không chốt kích thước bằng lập luận “chat sẽ đọc được”.

`class_sessions` pin lesson_version, timezone/schedule occurrence và revision. Instructor phase command cần expected_revision; reconnect đọc current snapshot, không chỉ replay WebSocket stream. Late join/async learner giữ được individual progress. Attendance không suy từ online count; không bonus khi đủ người gây pressure.

Human teacher là authenticated actor với class scope. Mentor NPC là presenter: bản tĩnh hoặc AI có nhãn, không tự đọc tất cả dữ liệu, không có identity role của giáo viên. V1 không memory DB. Khi thêm memory: mục đích rõ, ít facts, provenance/expiry/consent, xem/xoá được, không lưu raw conversation mặc định. NPC response không gọi mutation grade/reward; generated feedback phải tách khỏi official scoring.

Social V2 chỉ private class text nếu có đội vận hành. Trước mở: server room ACL cho read/send/reconnect, block semantics theo surface, mute notifications, report queue, moderator decisions, rate limit, audit, retention/takedown, appeal và handling giáo viên bị report. Membership revoke phải ngừng truy cập ngay cả khi subscription còn mở. Không public DM, upload/video hay public room discovery trong pilot.

Presence là ephemeral TTL và approximate; opt-out; không DB heartbeat hoặc attendance authority. WebSocket chỉ khi measured latency/fanout cần; polling hoặc SSE đủ cho một số classroom update. Synchronous lesson runner không phụ thuộc social transport.

## 7. Assessment, competition và history

Casual practice, exam simulation và ranked competition có policy riêng trên common attempt substrate. Leaderboard key chứa activity/ruleset/content pool/input modality/time window, không so WPM 15s với 60s hay keyboard vật lý với IME/mobile tùy tiện.

Competitive run: server-issued run ID, nonce, content/rules version, eligibility, expiry; submit evidence bounded; server tính score có thể tính lại. Paste/automation/timing chỉ là signals. Token/signature chứng minh server cấp challenge, không chứng minh người dùng gõ thật. `unverified → pending_review → verified/rejected` và appeal/correction. Chỉ verified thuộc đúng policy vào serious ranking; giữ practice result cho user khi bị unverified.

Season thuộc Competition: `open → closed → verifying → finalized`; finalization cutoff và tie policy chốt trước mở season. Historical result append-only với correction revision, award revocation event khi cần. Hall of Fame đọc latest effective result; tên/ảnh public có thể ẩn hoặc pseudonymize độc lập lịch sử kết quả.

IELTS training có hints, simulation không hints; cùng content IDs nhưng policy khác. AI writing/speaking có rubric/model version và human evaluation set; estimated band vẫn cần calibration/error reporting. Chưa đạt thì trả feedback định tính và từ chối báo số giả chính xác. Official test có bốn kỹ năng theo [IELTS](https://ielts.org/take-a-test/test-types/ielts-academic-test); practice product không tự là chứng nhận.

## 8. Avatar, brand và media

Giữ 2D một pose. V1 free portrait; prototype modular để khóa art compatibility, không đặt editor trên critical path. V2 renderer DOM/CSS layers cho một preview, static composite thumbnail trong list; đây là lựa chọn đơn giản cần đo, không khẳng định nhanh nhất. Chỉ đổi Canvas/Pixi nếu profiling chứng minh bottleneck; Rive/Spine cần đánh giá pipeline/license ở thời điểm chọn, không tự thêm dependency.

Avatar manifest tối thiểu: `template_version`, `body_variant`, `pose_id`, `logical_slot`, `render_parts[{z_group,asset_hash,anchor,mask_ref}]`, `occludes`, `compatible_tags`, `thumbnail_ref`. Logical slot không đồng nhất một ảnh: tóc/áo có thể nhiều lớp trước/sau. Media sở hữu hash/blob; Economy item_id; Avatar render mapping và loadout. Equip validate entitlement + compatibility + expected_loadout_revision; preview local, cache LRU có giới hạn.

Canvas 1024×1400 là master authoring, không gửi từng layer cỡ đó tới mọi profile card. Pipeline: source art → rights/provenance → template validator → compatibility fixture composite → human QA → optimize sizes → hashed manifest → publish. Test ảnh trong suốt, anchor/mask/clip, nhiều nền, outfit pairs và full set fixture, visual fallback khi thiếu asset. Không giả “nhiều combination” đồng nghĩa production rẻ.

Audio: parent coordinator giữ focus/ducking; child lease và release khi dispose; exam/learning ưu tiên NPC và music. Generic voice cache public theo text+voice+locale+model version; personalized audio private có TTL. Có gesture fallback, mute groups, caption/text alternative và codec/device tests. Không preload toàn BGM/cue library.

## 9. Budget đề xuất để pilot khóa lại

Các số sau là **acceptance targets đề xuất**, không số đo repo, không tiêu chuẩn bắt buộc toàn ngành. Baseline ít nhất một Android RAM 4 GB/tầm trung thấp, một iPhone Safari đại diện và desktop; cold cache, 4 Mbps/150 ms giả lập cùng một lượt real-device. Performance tests cần tách đã tải font/audio và cold start.

| Surface | Budget ban đầu đề xuất | Cách kiểm |
|---|---|---|
| Core learn entry | JS ≤250 KiB gzip, CSS ≤50 KiB gzip; tổng trước first usable ≤800 KiB | network waterfall; không avatar catalog/game/social chunks |
| Trải nghiệm học | p75 LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 | lab trước pilot, RUM khi đủ mẫu; không hứa đạt trước đo |
| API first page/write ack | p95 ≤400 ms dưới tải pilot đã định nghĩa; async score có trạng thái riêng | load scenario và p95, không cộng generation time vào request đồng bộ |
| Typing feedback | p95 committed input→paint ≤50 ms trên thiết bị thử | trace interaction/IME; không server roundtrip mỗi phím |
| Avatar thumbnail | 128–256 px theo DPR; mục tiêu ≤30 KiB mỗi thumbnail | decoded memory + scroll frame time, không full layers trong list |
| Full avatar preview | ≤8 render layers, ≤600 KiB transferred, ≤24 MiB decoded texture/memory delta | warm/cold preview; vượt thì giảm layer/resolution trước đổi engine |
| Learning audio | chỉ preload clip cần kế tiếp; mục tiêu ≤500 KiB trước bước audio đầu | streaming long audio; transcript fallback |
| Lifecycle | không có memory tăng đơn điệu sau 20 lần mở/đóng route; background pause | heap/subscription/audio leak observation, không lấy một snapshot đơn |
| Payload | attempts batch tối đa 100 events/256 KiB, list mặc định 20–50 items | server cap, reject oversized; tune bằng actual payload |

Budget vượt → giảm scope, không chỉ thêm “lazy-load” vào checklist. Reduced motion do OS/user luôn thắng preset; [MDN mô tả media query nhận lựa chọn hệ điều hành](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion). Accessibility không chỉ motion: keyboard focus, contrast, screen reader labels, timed-task alternatives, non-color feedback đều là release gate.

## 10. Migration và rollout an toàn

1. **Inventory/read-only audit:** version từng child adapter, canonical keys/legacy IDs, IndexedDB schema, local admin contracts và production requirements. Chốt fixtures trước đổi contract.
2. **Backup + content mapping:** export local profile, mapping compact ABI → content/sense/version. Unknown mapping giữ quarantine, không đoán/gộp sai nghĩa. Không xóa local history.
3. **Backend core có auth:** server content/session/attempt APIs; guest/local vẫn dùng được theo policy. Account liên kết qua authenticated flow, không user_id do child tự nhận.
4. **Shadow ingestion:** ingest mới dưới feature flag; server validate và so projections, không dual authority. Chỉ một nguồn hiển thị chính; divergence có báo cáo. Local import `legacy_unverified`, không chuyển aggregate thành raw attempts giả.
5. **Authority cutover theo cohort:** server giữ progress authority; browser outbox retry cùng event ID. Offline attempts dùng cho private practice theo policy, không competitive/wallet grant. Đổi thiết bị đăng nhập lấy server state.
6. **Compatibility/cutover failure:** parent thương lượng version/capability với child; không support thì chuyển local practice có nhãn. Giữ old local profile backup; rollback UI/API version phải reconcile những server writes đã accepted, không replay mint.
7. **Hardening:** retry/out-of-order/multiple tabs/refresh test; restore DB/object metadata; content takedown; account export/delete và job retries; theo dõi outbox lag, accepted/rejected, duplicate rate và divergence.

Exact `targetOrigin`, `event.origin`, `event.source` và active child context là cần thiết theo [MDN postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage); giữ những check hiện có. Account auth/token production không gửi vào arbitrary game message. Client proof vẫn untrusted dù bridge hợp lệ.

Privacy retention được chốt bằng policy trước rollout: ví dụ pilot có thể chọn raw free-text/evidence chi tiết 30 ngày và aggregate lâu hơn; đây là đề xuất cần mục đích cụ thể, không thời hạn pháp lý. Đừng gửi raw keystrokes/audio/chat vào analytics. Xoá user phải xử lý facts, assets/cache và public projections; audit record chỉ giữ dữ liệu tối thiểu cần thiết theo policy đã duyệt.
