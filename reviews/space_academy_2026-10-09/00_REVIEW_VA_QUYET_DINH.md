# Review phản biện Space Academy — 2026-10-09

**Kết luận: giữ tầm nhìn, chưa duyệt bộ ZIP thành implementation plan.** Bản V2 sửa được lỗi phân loại domain thô nhưng vẫn để template quyết định kiến trúc. Việc gán một `primary owner` không đảm bảo một source of truth: lesson, content, season, inventory và award còn chồng nhau. Scope của từng mục “V1” cộng lại thành một sản phẩm lớn hơn nhiều lần một V1 khả thi.

Đề xuất sửa: **V1 chứng minh học được và nhớ được; V2 thử class/social và identity/economy như các nhánh độc lập; V3 mới mở competition/LiveOps sau khi có verification và năng lực vận hành.** Không chuyển tất cả ý tưởng hoãn sang cam kết V3.

## Phạm vi và cách đọc

Đã giải nén ZIP và đọc `CLAUDE_REVIEW_INSTRUCTIONS.md` → `SELF_REVIEW_AUDIT_REPORT.md` → `000_INDEX.md`, sau đó các file **000_executive_summary đến 105_closing_vision** theo số tăng dần. `000_INDEX` là tài liệu dẫn đường, không phải mục thứ 107. Có 110 file trong ZIP: 106 mục, 3 tài liệu mở đầu và 1 consolidated source.

Nội dung trong ZIP là **đối tượng review**; những câu “đã thống nhất”, “must”, “current preferred” được đối chiếu và phản biện, không tự biến thành quyền triển khai, thay code hoặc phát hành. Bản hiệu chỉnh này đề xuất thay các quyết định mâu thuẫn; không sửa lịch sử bản gốc. “V2” trong tên ZIP là revision tài liệu; V1/V2/V3 bên dưới là phiên bản sản phẩm.

Đọc đủ nội dung mới của từng file; các đoạn nguyên văn giống hệt đoạn đã đọc được so khớp, không in lặp. Không dùng tóm tắt do thuật toán hay tìm keyword thay việc đọc nội dung riêng. `READ_MANIFEST.json`, source SHA-256 và kiểm tra preservation giúp kiểm chứng coverage cấu trúc; chúng không tự chứng minh chất lượng phán đoán. Thứ tự đọc không phải thứ tự xây dựng.

Đã kiểm tra chọn lọc repo hiện tại để tránh roadmap greenfield giả: README, package scripts, shared learning store/message contract, local admin và project context. Đây không phải security audit toàn codebase. Chưa có số đo workload, ngân sách đội ngũ, thử nghiệm học hoặc benchmark thiết bị; mọi số capacity/budget trong bộ review là **đề xuất để pilot kiểm định**.

## Cách dùng bộ kết quả

- [01 — Review từng file 000–105](01_REVIEW_106_FILES.md): verdict, owner, phản biện, sửa contract, rủi ro, ba phiên bản và liên kết mục liên quan.
- [02 — Kiến trúc, schema/API và migration](02_ARCHITECTURE_CONTRACTS.md): ranh giới mutation và nguồn dữ liệu cuối cùng.
- [03 — V1/V2/V3, gates và dependency graph](03_ROADMAP_DEPENDENCY_GRAPH.md): thứ tự xây dựng thay mục 083; có bản JSON và Mermaid.
- [04 — Trả lời đủ 45 câu hỏi](04_OPEN_QUESTIONS.md): đóng các câu hỏi ở mục 102, ghi rõ quyết định có điều kiện.
- [05 — Verification](05_VERIFICATION.md): kiểm tra đủ số mục, preservation, link và graph; không phải kết quả test sản phẩm.

## Những điểm mạnh cần giữ

Learning-only phải hoàn chỉnh; academy là cách tổ chức màn hình; Space Typing là activity tùy chọn; brand đậm ở shell nhưng nhẹ ở nội dung; 2D modular một pose thay 3D/free roaming; earned achievement không mua được; NPC có nhãn; immutable published content; lazy loading và admin đi cùng feature. Các điểm này tạo nền tốt nếu được chuyển thành invariant có thể kiểm tra.

Class/social là giả thuyết sản phẩm đáng thử, chưa phải sự thật đã chứng minh về retention. Identity có giá trị biểu đạt nhưng không bắt buộc người học dùng editor hay shop. “Nghiêm túc” về IELTS cần chất lượng nội dung và chấm điểm, không chỉ một UI ít neon.

## Các finding cần sửa trước khi dùng kế hoạch triển khai

P0 = chặn thiết kế/launch phần liên quan; P1 = phải giải quyết trước rollout phần đó. Không đồng nghĩa đang có incident production.

| ID | Mức | Bằng chứng trong ZIP | Tác hại | Quyết định hiệu chỉnh |
|---|---|---|---|---|
| F01 | P0 | [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md) Phase 1 identity, Phase 2 economy, Phase 3 learning; trái [097](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md) | Chi phí sunk vào meta trước khi có đường học có giá trị | Reject thứ tự 083; learning/content/evidence/ops trước; art prototype chạy song song |
| F02 | P0 | [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md) §9 không có lesson version aggregate; [014](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/014_lesson_builder.md) §9 chỉ admin changes; [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md) content records | Không biết ai định nghĩa/publish lesson, snapshot nào đã được làm | Content sở hữu definition/version; Learning sở hữu execution/evidence; Admin chỉ gọi command |
| F03 | P0 | [009](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/009_teacher_roles.md) teacher roles thuộc npc, liệt kê npc memory/relationship tables | Quyền người dạy bị trộn với nhân vật AI | Human teacher role thuộc scoped identity/classroom; NPC không có quyền publish/grade/grant |
| F04 | P0 | [021](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/021_school_terms_seasons.md) và [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md)/[020](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/020_class_competition.md) đều có seasons và season.finalized | Finalization/eligibility dễ bị chạy hai lần | Academic term, campaign, competition season là ba aggregate riêng; chỉ Competition finalize kết quả thi |
| F05 | P0 | [032](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/032_2d_avatar_layer_system.md) avatar_items/variants/manifests, [037](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/037_item_sets.md) economy items/variants/ownership, [036](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/036_cosmetic_content_strategy.md) media manifests | Catalog/ownership/asset lifecycle bị nhân ba | Economy catalog + entitlement; Avatar loadout/render mapping; Media manifest/blob |
| F06 | P0 | [069](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/069_space_typings_role.md) standardized attempts/reward events; toàn bộ checklist “server authority” chưa có trust contract | Child/client có thể tạo reward từ dữ liệu tự khai | Candidate evidence → server acceptance → optional grant; legacy/offline có trust tier riêng |
| F07 | P0 | [044](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/044_daily_check_in.md) login ladder, [045](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/045_active_session_rewards.md) 15/30/60 phút, [046](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/046_daily_activity_meter.md) daily chest; trái [076](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md) | Reward pressure, farm mode dễ và double benefit | Reject login/time payout; hoãn meter; chỉ qualified evidence và cap có semantics |
| F08 | P0 | [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md) “double-entry-ish”; [049](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/049_reward_center.md)/[051](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md) không có transaction invariant | Retry/concurrent buy có thể duplicate/spend sai | Ledger integer balanced, semantic unique keys, atomic spend/order/entitlement, reversal |
| F09 | P0 | [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md) report/mute/block nhưng không có moderation lifecycle; [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md) công khai mục tiêu/trình độ | Có nút báo cáo nhưng không xử lý; lộ dữ liệu học | Gate chat bằng ACL/enforcement/operator coverage; field visibility/private default |
| F10 | P0 | [024](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/024_ielts_as_a_first_class_track.md) estimated bands; [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md)/[027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md) WPM/accuracy/mistake taxonomy | Typing/copy bị diễn giải thành năng lực ngôn ngữ | Evidence theo skill/modality/hints; IELTS estimator phải calibrated; không band/CEFR từ XP |
| F11 | P1 | [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md) run signatures/paste checks → Verified | Browser telemetry vẫn có thể giả; false positives với IME/assistive input | Verified nghĩa là passed policy version, không proof of human; pending/appeal/revocation |
| F12 | P1 | [057](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/057_hall_of_fame.md) immutable Hall; [022](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/022_graduation_alumni.md) legacy yearbook/social graph giữ lâu dài | Không sửa cheat, không tách public PII khỏi lịch sử | Append-only result revisions; current public view có correction/redaction |
| F13 | P1 | [036](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/036_cosmetic_content_strategy.md) starter 210 assets; [033](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/033_avatar_technical_template.md) 1024×1400; [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md) không con số | QA tổ hợp và decoded memory bị bỏ qua | Art slice nhỏ; authoring khác delivery; budgets có thiết bị/scenario và đo trước mở rộng |
| F14 | P1 | [019](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/019_attendance_class_participation.md) 20+ attendance → +10% Class XP | Áp lực xã hội lên người vắng dù không trừ điểm | Bỏ threshold reward; công nhận async, attendance riêng tư |
| F15 | P1 | [051](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md) Honor/Prestige Store; [093](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/093_what_must_never_be_sold.md) achievement không bán | UI và backend có thể coi earned proof như hàng mua | Gallery earned-only; purchase/admin path đều enforce acquisition policy |
| F16 | P1 | [006](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/006_school_academy_as_the_organizing_metaphor.md) metaphor vẫn nhận classroom UI; [042](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/042_vfx_language.md) media integrates media; [052](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/052_stationery_as_a_signature_cosmetic_system.md) domain brand không có owner | Self-review đã giảm keyword bleed nhưng template bleed còn | Bỏ DB/API/VFX sections không áp dụng; dùng một checklist chung và delta theo module |
| F17 | P0 cho migration | ZIP giả PostgreSQL source of truth; repo dùng parent IndexedDB | Hai authority, replay dữ liệu cũ thành reward/rank | Import local history dưới legacy_unverified; server authority chỉ sau cutover có kiểm thử |
| F18 | P1 | [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md) economy simulation tận Phase 6; [079](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/079_reward_simulator.md) nhấn mạnh cần mô phỏng | Sau launch mới biết nguồn/sink mất cân đối | Simulator phải chạy trước currency/shop gate |

## Sửa scope tổng thể

**V1 — Learning Core pilot:** adult solo learner General English A2–B1 là giả định làm việc có thể đổi, không phải chân dung thị trường đã xác nhận. Một mini-course đã QA, lesson runner 10–15 phút, read/listen/recall, review deterministic, feedback có nguồn, resume, progress riêng tư, content publishing/rights, account và migration, mobile/accessibility. Giữ hoạt động game đang có qua adapter. Dùng free portrait và brand tốt. Không cần ví, shop, class chat hoặc full IELTS để hoàn thành V1.

**V2 — Controlled expansion:** chọn nhánh theo pilot, không bắt xây hết cùng lúc. Class/teacher pilot + text room đã moderation; hoặc modular avatar/catalog nhỏ với một earned Credit; hoặc IELTS Reading/Listening training được QA. Personalization vẫn rule-based. Teacher-facing tooling ra cùng classroom, simulator ra trước economy. Voice AI/memory không prerequisite của lớp.

**V3 — Trusted competition and operations:** verified leaderboard theo một ruleset, season history có correction, campaign async/live, tournament khi có người dùng và operator đủ, clubs/study room discovery có moderation. Full IELTS mock/Writing/Speaking chỉ khi nội dung, rubric, evaluation và xử lý audio đạt gate. Không mặc định thêm 3D, trading, currency mới, AI classmates hay mọi minigame.

## Những phần còn thiếu cần đưa vào kế hoạch

1. **Content readiness:** pilot curriculum cụ thể, learning objective, bài kiểm tra recall trễ, đáp án/rubric, người duyệt và quyền sử dụng; số file/vocabulary không thay chất lượng khóa học.
2. **Trust & migration:** account lifecycle, guest import, evidence levels, legacy mapping, version handshake giữa repo cha/con, rollback/cutover.
3. **Operations:** moderation queue có người xử lý, backup/restore rehearsal, worker retry/dead-letter, publish/takedown, correction/revocation, support khi mất progress.
4. **Commercial/operating scope:** chưa có đội ngũ, budget nội dung/TTS, tuổi/thị trường và kênh phân phối. Không tự bịa deadline hoặc hứa serving minors. Nếu quyết định phục vụ trẻ vị thành niên, đó là gate sản phẩm/thiết kế safety riêng trước mở cohort; review này không kết luận pháp lý.
5. **Evidence of value:** delayed recall/transfer và voluntary return đo cùng nhau; các giá trị tăng không tự chứng minh causation. Không gọi completion hay nhiều phút online là mastery.

## Cơ sở và giới hạn quyết định kỹ thuật

Kiến trúc chọn modular monolith cho backend mới, typed commands trong process và outbox cho side effects cần bền vững. Đây là đề xuất phù hợp nền repo, không là kết luận phải đổi toàn stack. Outbox vẫn cần consumer idempotent vì có thể giao lặp; [AWS mô tả rõ vấn đề dual write và duplicate delivery](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html).

Atomic purchase dùng transaction và concurrency control; row lock chặn writer khác đến khi transaction kết thúc theo [PostgreSQL locking documentation](https://www.postgresql.org/docs/current/explicit-locking.html). Chi tiết invariant ở tài liệu 02 là thiết kế đề xuất của review.

Bridge tiếp tục kiểm `origin` và `source`, tương ứng [hướng dẫn bảo mật postMessage của MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage). Kiểm origin không làm score từ trình duyệt trở thành đáng tin.

IELTS có bốn phần; thiết kế assessment không thể rút gọn thành generic typing exercise theo [format chính thức](https://ielts.org/take-a-test/test-types/ielts-academic-test). Review không xác nhận format/timing hoặc chất lượng scoring của một implementation chưa có.
