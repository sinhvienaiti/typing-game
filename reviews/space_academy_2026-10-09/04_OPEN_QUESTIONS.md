# Trả lời 45 câu hỏi mở của mục 102

Đây là các quyết định đề xuất cho roadmap; các giả thuyết về hiệu quả học, class size và chi phí phải được kiểm chứng qua pilot. “V2/V3” dưới đây là phiên bản sản phẩm, không revision ZIP.

## Product — câu 1–5

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 1 | Space Academy có đúng mental model? | **Giữ làm brand/IA.** Course, Learn, Practice phải dễ hiểu không cần biết lore. Academy không bắt user nhập học lớp hay di chuyển trong campus. |
| 2 | Có metaphor tốt hơn? | Dùng tên thao tác phổ thông làm primary labels, academy làm lớp biểu đạt: “Bài học”, “Ôn tập”, “Lớp”, “Hồ sơ”. Không cần rebrand “universe” lớn hơn để giải bài toán navigation. Kiểm thử hiểu nhãn trước đầu tư thêm area. |
| 3 | Hệ nào còn phức tạp? | Currency ladder, daily/weekly/time rewards chồng nhau, multi-shop, nhiều rarity, AI classmates/memory, nhiều leaderboard, art catalog 210 món và universal admin. Cắt ở nguồn; ẩn bằng progressive disclosure không làm giảm chi phí backend/QA. |
| 4 | Thiếu hệ gì? | Canonical lesson/content version; evidence semantics; account/migration; scoped authorization; moderation operations; deletion/takedown; correction/revocation; durable worker/restore; đánh giá learning. Bổ sung capability tối thiểu, không dựng thêm mười service. |
| 5 | Hoãn gì? | V2: classroom/chat, modular avatar/economy, IELTS training tùy gate. V3 hoặc xa hơn: public rankings, LiveOps/tournaments, discovery rooms, calibrated W/S. 3D/trading/power economy và login/time payout không nằm trong roadmap được khuyến nghị. |

## Learning — câu 6–9

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 6 | Lesson/class có giúp học nghiêm túc? | Có tiềm năng, nhưng 40 phút và nhiều phase không tự tạo hiệu quả. Mỗi lesson cần objective → practice → feedback → delayed retrieval; lesson runner phải self-paced độc lập. Class chỉ là orchestration trên cùng version. |
| 7 | Gamification hại ở đâu? | Reward theo phút/login, thi tốc độ trong task cần suy nghĩ, thưởng chép từ như nhớ nghĩa, checklist 100 điểm và bonus đủ người. Bỏ time/login payout, tách evidence theo modality/hints, không thưởng replay và giữ async parity. |
| 8 | IELTS đủ tách khỏi game chưa? | UI định hướng đúng, data/assessment chưa đủ. Dùng exam_spec/rubric version, answer protection, autosave/timer policy; training khác simulation. Bốn kỹ năng của IELTS là phạm vi assessment riêng theo [format chính thức](https://ielts.org/take-a-test/test-types/ielts-academic-test). Không numeric band nếu chưa có evaluation/calibration. |
| 9 | CEFR và topics cùng tồn tại thế nào? | Goal là mục đích; topic là nội dung; skill là năng lực; CEFR label là curriculum difficulty; activity là cách luyện. Một lesson có topic+claimed level+objectives; mastery theo evidence item/skill. Không có “CEFR level tăng vì mua/xài đồ hoặc WPM cao”. |

## Social — câu 10–14

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 10 | Class size 15–30 hợp lý? | Là giả thuyết hợp lý để thử, chưa phải sizing yêu cầu. Pilot 8–12 người với teacher/operator rõ, sau đó thử dải gốc; đánh giá learning, scheduling coverage, teacher effort, moderation load. Không suy sức chứa hạ tầng từ số này. |
| 11 | Real teacher, AI và self-study cùng tồn tại? | Human teacher có account/role binding lớp; NPC là presenter có nhãn; self-study không cần class. Course/lesson chung, class_session chỉ thêm schedule/phase. AI không tự có quyền xem học sinh, chấm chính thức hay publish. |
| 12 | Match vào lớp? | V2 user chọn từ danh sách nhỏ theo goal, timezone/lịch khả dụng, ngôn ngữ và assessment level phù hợp; invite/waitlist có capacity. Chưa cần recommendation ML. Cho đổi/rời lớp; không public chi tiết điểm đầu vào. |
| 13 | Gắn kết mà không ồn/nguy hiểm? | Nhóm nhỏ, hoạt động async có mục tiêu, room ACL, quiet hours, opt-in feed, moderation queue có người xử lý. Không public ranking người vắng, không presence làm bằng chứng attendance, không broadcast weak skills. |
| 14 | Chat nào V1? | V1 sản phẩm mới **không user chat**. Giai đoạn V2 có class text room mới là V1 của chat module; gọi tên rõ để tránh scope creep. Chưa DM/upload/voice/video; nếu chưa có moderator thì classroom chạy không chat. |

## NPC / AI — câu 15–18

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 15 | Memory model tốt nhất? | V1 không có persistent NPC memory. V2 scoped summary từ Learning API, ưu tiên derive thay copy. Chỉ lưu facts cần thiết với source/consent/expiry khi lợi ích rõ; user xem/xoá được. Không vector store/raw-chat archive mặc định. |
| 16 | Tự nhiên mà không giả người? | Nhãn AI/NPC luôn nhìn thấy; greeting và biểu cảm có ngữ cảnh thật; timestamp/source rõ cho class activity. Không giả attendance, human online count, lời mời từ người không tồn tại hoặc đưa AI vào leaderboard người thật. |
| 17 | Boundary nội dung/moderation? | NPC không thực thi lệnh trong content hoặc lời học sinh, không tool quyền grant/grade/publish. Input giới hạn, facts scoped, output moderation và report/correction, không tiết lộ dữ liệu bạn học. Cost/time limit + text fallback và dữ liệu học không dùng ngoài mục đích đã công bố. |
| 18 | NPC role nào có giá trị? | Một mentor giới thiệu objective/next review và feedback dựa facts. Chỉ thêm specialist khi đánh giá cho thấy trợ giúp cụ thể tốt hơn template. Hoãn AI classmates, relationship meter và daily schedule simulation. |

## Economy — câu 19–23

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 19 | Credits + Crystals + tokens đủ? | Đã quá nhiều cho lần đầu. V1 không ví; V2 một earned Credit là đủ thử cosmetic loop. Token/crystal chỉ xem lại khi có công dụng không thể giải bằng eligibility/catalog; không tạo để có “độ sâu”. |
| 20 | Tỷ lệ earning/spending? | Chưa có dữ liệu để chốt tỷ lệ thật. Simulator nhận số qualified goals/tuần và giá; so time-to-item P10/P50/P90, solo/class, người học chậm và catalog exhaustion. Giá có thể đặt theo số tuần học mục tiêu như giả thuyết, rồi điều chỉnh trước launch. |
| 21 | Ngăn inflation? | Cap qualified sources, semantic dedupe, theo dõi nguồn/sink, deterministic grant; không login/AFK/time faucet. Non-consumable catalog hữu hạn sẽ bão hòa, không ép người học mua mãi hoặc tăng giá bí mật để sửa. Credits đóng không trade là lựa chọn giảm phạm vi, không bảo đảm tự cân bằng. |
| 22 | Reward V1 và sau đó? | V1 feedback/course progress/private milestone. V2 deterministic cosmetic grant, một nguồn Credit, optional weekly bonus đã simulate, receipt auto-grant. V3 event reward khi infrastructure và healthy engagement gate đạt. Reject daily login chest và mốc active minutes. |
| 23 | Chống grind thay learning? | Reward accepted evidence với đúng skill và giới hạn repeat, không game score/client duration. Debrief học trước reward. Delayed recall/transfer và learner control là guardrail; cap không tự chứng minh còn học tốt nên vẫn phải pilot. |

## Prestige — câu 24–27

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 24 | Ranking nào công bằng? | V1 private PB theo comparable ruleset. V3 một board typing opt-in có input modality/content/rules/timing cố định. Không generic English mastery, helping hoặc IELTS estimate board trước calibration. Ties, minimum cohort và visibility phải rõ. |
| 25 | Competitive Verified thế nào? | Server challenge/run ID/rules version; bounded evidence; verifier và suspicious review; pending/verified/rejected + appeal. Browser signals không proof of human. Hiển thị “đã qua kiểm tra theo policy X”, không quảng bá chống gian lận tuyệt đối. |
| 26 | Item nào permanently exclusive? | Chỉ historical proof thật như season champion có policy được công bố và finalized result; non-tradeable, award-only, có revoke khi fraud/correction. Shop cosmetics thường ưu tiên may-return. Không hứa “never return” cho hàng trang trí chỉ để tạo áp lực. |
| 27 | Hall/history? | Result snapshots có revision, amendment và actor/reason; public projection lấy latest valid result. Ẩn/pseudonymize profile riêng khỏi record. Không overwrite lịch sử âm thầm, nhưng cũng không dùng immutable để chặn correction hoặc deletion policy. |

## Avatar — câu 28–32

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 28 | 2D layered có đúng? | Đúng với nhu cầu profile/shop/class portrait, một pose và micro-motion. Không cần đi lại. Static thumbnail và portrait hoàn toàn đủ V1; modular production là nhánh V2, không gate learning. |
| 29 | DOM/CSS, Canvas, Pixi, Rive, Spine? | Bắt đầu prototype DOM/CSS cho một preview và composite thumbnails cho list. Chỉ đổi renderer khi profile thực tế cho thấy layer/mask/frame-time không đạt. Engine animation/licensing/pipeline phải được kiểm tra tại thời điểm chọn; chưa có bằng chứng cần Rive/Spine/Pixi cho V1. |
| 30 | Masks/layers standards? | template_version/body_variant/pose_id, fixed anchors, logical slots → nhiều render parts, z_groups/masks/occludes/compatibility tags. Item catalog và asset manifest tách owner; visual QA ảnh tổ hợp trước publish. Không dùng danh sách z-order bất biến cho mọi outfit. |
| 31 | Resolution/size? | 1024×1400 là master. Đề xuất thumbnails 128–256 px, ≤30 KiB; preview ≤8 render layers, ≤600 KiB transfer và ≤24 MiB decoded delta; đo lại trên thiết bị đại diện theo tài liệu 02. Không khẳng định budget này đã đạt hoặc là chuẩn ngành. |
| 32 | Hàng trăm items tương thích? | Đừng bắt đầu hàng trăm. Một art slice có fixture combos, auto-check canvas/alpha/anchor/manifest và human clipping QA; variant tooling; publish thumbnail/composite. Production throughput/cost per accepted item quyết định tăng catalog, không phép nhân số combination. |

## Audio / Visual — câu 33–36

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 33 | Art direction? | Modern academy, stylized 2D có silhouette rõ, typography và contrast cao; sci-fi ở shell, learning surface yên. Gộp 039/090 thành bible/tokens, tránh hai nguồn style khác nhau. |
| 34 | Làm premium thế nào? | Chất lượng đọc/nghe, spacing, consistency, input feedback nhanh, illustration ít nhưng tốt, state loading/error/resume tử tế. Không tăng số animation/currency để tạo cảm giác có chiều sâu. |
| 35 | Audio identity gì? | Một motif ngắn ở milestone, ít cue consistent; lesson/voice thật rõ. Reuse parent music/ducking hiện có với audio focus contract; generic pre-generated lines có QA. Không autoplay greeting dài hoặc hover/tab SFX khắp nơi. |
| 36 | Hiệu ứng nào hạn chế? | Fullscreen reveal, particles/aura, parallax/blur, simultaneous avatar idle và keyboard sounds. Exam không decorative effects; offscreen/hidden dừng; reduced-motion user/OS thắng style preset. |

## Architecture / performance — câu 37–41

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 37 | Module nào lazy-load? | Tất cả game engines/combat, editor/avatar full assets, shop catalog, class chat history, event visuals, admin, ranking. Shell/next lesson chỉ tải payload cần cho thao tác đầu. Route split phải kiểm waterfall thay chỉ nhìn cấu trúc thư mục. |
| 38 | Data nào realtime? | Chỉ current class phase/presence/chat và live contest khi feature bật. Mastery/receipt/codex cập nhật sau durable write hoặc invalidation/poll, không cần global WebSocket. Content published cache theo version. |
| 39 | Social gì cần WebSocket? | Text room/presence quy mô hoặc latency yêu cầu có thể dùng WebSocket; small class có thể polling/SSE theo nhu cầu. Async challenges/calendar không bắt buộc. Membership revoke, reconnect snapshot, connection cap phải đi cùng transport. |
| 40 | Budgets nào khóa? | Proposal ở 02: shell JS 250 KiB gzip/CSS 50 KiB, total 800 KiB trước usable, API p95 400 ms, input→paint p95 50 ms, device/network scenario và decoded avatar limits. Chạy baseline trước ratify; vượt thì cắt payload/scope. |
| 41 | Mobile degrade gì? | Static avatar, ít VFX, thumbnails, không background animation. Không degrade khả năng đọc/nghe/ôn, resume, input accessibility. Soft keyboard/IME có policy riêng trong competition; không coi lack of desktop typing là lack of English ability. |

## Admin — câu 42–45

| # | Câu hỏi | Kết luận và hành động |
|---|---|---|
| 42 | Admin essential? | V1: content review/preview/publish/takedown, user access/privacy actions, audit, failed jobs/support, backup/restore. Class admin/moderation đến cùng class; economy simulator/reversal đến trước shop; event editor tới cùng LiveOps. Không dashboard giả cho capability chưa có. |
| 43 | Lesson/Event Builder share gì? | Form controls, schema-validation UI, version diff, media picker, permission/audit component. Lesson semantic validation ở Content, event recurrence/eligibility ở LiveOps. Không chung một generic workflow engine/super-table chỉ vì cả hai có publish. |
| 44 | Simulator economy? | Pure evaluator cùng rule version với production, deterministic seeds và scenario fixtures; offline outputs có percentile/worst-case. Không production wallet credentials. Kiểm retry/cap/absence/timezone/source stacking, giá/catalog exhaustion trước ra Credit. |
| 45 | Audit/version config? | Entity owner giữ draft revision/published immutable version và optimistic concurrency. Audit actor/time/reason/input hash; schedule occurrence/rule snapshot pinned; action privilege theo scope. Rollback pointer chỉ cho future sessions; historical correction bằng revision/reversal, không edit finalized result. |

## Unknown còn lại và default đã dùng

Chưa có số người dùng, tuổi/thị trường launch, staffing teacher/moderator, cost ceiling AI/media, target device thực tế hoặc learning evaluation dataset. Review dùng adult pilot, một course, một backend module set, no public chat V1 và no currency V1 để có lộ trình thực thi cụ thể. Khi những dữ kiện này thay đổi, cập nhật scope/gate có chủ đích; không cần đổi invariant ownership, evidence trust và learn-only path.
