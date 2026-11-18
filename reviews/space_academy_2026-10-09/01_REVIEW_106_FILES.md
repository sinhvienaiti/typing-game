# Review đủ 106 mục theo thứ tự

Mỗi mục bên dưới là delta hiệu chỉnh so với source. **Keep** = giữ ý chính nhưng vẫn bổ sung contract; **Simplify** = cắt/đổi scope; **Postpone** = giữ làm ứng viên sau gate; **Reject** = bỏ cơ chế hoặc thứ tự đề xuất, không phủ định toàn bộ chủ đề. V2/V3 là gợi ý có điều kiện, không cam kết tất cả.

Đối với mọi runtime feature: authorization phía server; payload/list có giới hạn; retry có idempotency khi ghi state; private data không vào analytics; route nặng lazy-load; mobile/keyboard/mute/reduced-motion là gate. Các rủi ro riêng ghi từng mục dưới đây. Concept/policy/example không sinh DB/API riêng; performance/security áp lên consumer thực thi, không dựng runtime cho tài liệu.

Các “mục liên quan” dùng để truy vết, **không** là hard dependency graph; xem [DAG cuối cùng](03_ROADMAP_DEPENDENCY_GRAPH.md). Schema/API chi tiết dùng chung ở [02](02_ARCHITECTURE_CONTRACTS.md), không nhân bản bảng theo file.

**Tổng verdict:** Keep: 24, Postpone: 31, Reject: 3, Simplify: 48.

## 000 — Executive Summary

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/000_executive_summary.md) — **Simplify**. **Owner:** product (giữ).

**Phản biện:** North star đúng, nhưng khẳng định social là retention mạnh nhất chưa có bằng chứng; loop tuyến tính buộc qua economy/social mâu thuẫn learn-only.

**Sửa scope/schema/API:** Thay bằng loop học khép kín; meta là nhánh tùy chọn. Không schema product.

**Dữ liệu / an toàn / hiệu năng:** Không lấy time-spent thay bằng chứng nhớ bài; Home không chờ meta API.

**V1:** Một cohort học hoàn chỉnh. **V2:** Thử lớp có đối chứng. **V3:** Mở rộng theo bằng chứng.

**Mục liên quan:** [097](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md), [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md).

## 001 — Product Reframing

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/001_product_reframing.md) — **Keep**. **Owner:** product (giữ).

**Phản biện:** Platform-first đúng; cây A1–C2 và mọi kỹ năng là tầm nhìn, không phải backlog V1.

**Sửa scope/schema/API:** Giữ portal shell; game là adapter của canonical attempts; không rewrite toàn bộ game.

**Dữ liệu / an toàn / hiệu năng:** Bridge phải kiểm tra origin/source và compatibility; giữ deep link cũ.

**V1:** Shell và adapter hiện có. **V2:** Thêm track đủ nội dung. **V3:** Mở rộng activity.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [069](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/069_space_typings_role.md).

## 002 — What We Borrow From Online Games — And What We Do Not

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/002_what_we_borrow_from_online_games_and_what_we_do_not.md) — **Simplify**. **Owner:** product (giữ).

**Phản biện:** Quy tắc đạt 2/3 tiêu chí có thể cho qua tính năng hại học nhưng tăng retention và rẻ.

**Sửa scope/schema/API:** Đặt learning safety/accessibility là điều kiện bắt buộc; giá trị và chi phí là bước sau. Không DB.

**Dữ liệu / an toàn / hiệu năng:** Shop scarcity không được vượt gate chống thao túng.

**V1:** Checklist chọn tính năng. **V2:** Đo thử meta nhỏ. **V3:** Chỉ nhân rộng thử nghiệm tốt.

**Mục liên quan:** [003](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/003_core_product_principles.md), [076](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md).

## 003 — Core Product Principles

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/003_core_product_principles.md) — **Keep**. **Owner:** product (giữ).

**Phản biện:** Progressive disclosure tốt nhưng tự suy đoán sở thích để bật competition dễ phá quyền lựa chọn.

**Sửa scope/schema/API:** Dùng opt-in rõ cho social/rank; policy ưu tiên exam và accessibility hơn preset.

**Dữ liệu / an toàn / hiệu năng:** Ẩn UI không thay authorization; không preload feature đã ẩn.

**V1:** Focus và đường học độc lập. **V2:** Disclosure theo lựa chọn. **V3:** Cá nhân hóa có reset.

**Mục liên quan:** [005](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/005_experience_styles.md), [075](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md).

## 004 — Target User Personas

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/004_target_user_personas.md) — **Simplify**. **Owner:** product (giữ).

**Phản biện:** Sáu persona cùng lúc vượt năng lực nội dung/vận hành; teacher/admin không cùng quyền.

**Sửa scope/schema/API:** Chọn adult solo learner làm giả định pilot; teacher pilot ở V2; persona là preference, role là authorization.

**Dữ liệu / an toàn / hiệu năng:** Không suy tuổi/quyền từ persona; tránh thu PII không cần.

**V1:** Một cohort General English. **V2:** Teacher/class và IELTS pilot. **V3:** Cohort mới sau kiểm chứng.

**Mục liên quan:** [023](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/023_core_learning_tracks.md), [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md).

## 005 — Experience Styles

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/005_experience_styles.md) — **Simplify**. **Owner:** product → platform UX; product giữ policy.

**Phản biện:** Ba style cộng preset typing tạo ma trận trạng thái khó dự đoán.

**Sửa scope/schema/API:** Một preference schema versioned; thứ tự OS accessibility > exam policy > user choice > default.

**Dữ liệu / an toàn / hiệu năng:** Không dùng Immersive để bật lại sound/motion bị tắt; cache nhẹ.

**V1:** Focus/Balanced qua token. **V2:** Immersive giới hạn. **V3:** Preset cộng đồng sau moderation.

**Mục liên quan:** [003](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/003_core_product_principles.md), [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md).

## 006 — School / Academy as the Organizing Metaphor

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/006_school_academy_as_the_organizing_metaphor.md) — **Simplify**. **Owner:** classroom → product.

**Phản biện:** Metaphor IA đang kéo theo before/during/after, chat và classroom art dù không có lớp.

**Sửa scope/schema/API:** Chuyển thành guideline tên/route, bỏ runtime class dependencies khỏi mục này.

**Dữ liệu / an toàn / hiệu năng:** Solo không cần membership để học; không tạo campus bundle.

**V1:** Learn/Practice/Profile. **V2:** Class là route tùy chọn. **V3:** Thêm area nếu có nhu cầu.

**Mục liên quan:** [007](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/007_space_academy_areas.md), [085](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/085_core_ux_example_simple_learner.md).

## 007 — Space Academy Areas

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/007_space_academy_areas.md) — **Simplify**. **Owner:** product (giữ).

**Phản biện:** Mười hai khu vực tạo navigation rỗng trước khi có chức năng.

**Sửa scope/schema/API:** Gộp Language/Practice/Simulation vào activity picker; Library là progress view.

**Dữ liệu / an toàn / hiệu năng:** Không render route stub như feature đã có; lazy-load Games.

**V1:** Ba route chính và Games tùy chọn. **V2:** Classes, catalog. **V3:** Events/competition có gate.

**Mục liên quan:** [001](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/001_product_reframing.md), [073](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/073_performance_philosophy.md).

## 008 — Class System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md) — **Postpone**. **Owner:** classroom (giữ).

**Phản biện:** 15–30 người chỉ là giả thuyết; thiếu lifecycle, admission và quyền giáo viên.

**Sửa scope/schema/API:** Class tách course và cohort; membership unique active; join/invite atomic capacity; session pin lesson_version.

**Dữ liệu / an toàn / hiệu năng:** Private roster, thu hồi quyền ngay khi rời lớp; giới hạn participant payload.

**V1:** Không bắt có lớp. **V2:** Pilot 8–12 người rồi thử 15–30. **V3:** Mở rộng khi đủ hỗ trợ.

**Mục liên quan:** [009](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/009_teacher_roles.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md).

## 009 — Teacher Roles

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/009_teacher_roles.md) — **Simplify**. **Owner:** npc → classroom; identity cấp quyền.

**Phản biện:** Role giáo viên người thật đang mang schema relationship NPC, thiếu authority giảng dạy.

**Sửa scope/schema/API:** Teacher assignment là membership role; NPC chỉ persona/presenter, không actor được publish hay xem PII.

**Dữ liệu / an toàn / hiệu năng:** Teacher chỉ xem lớp phụ trách; NPC facts tối thiểu; không tạo 6 bảng NPC cho role.

**V1:** Editor nội bộ và mentor kịch bản. **V2:** Real teacher + NPC gắn nhãn. **V3:** Specialist AI được đánh giá.

**Mục liên quan:** [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md), [010](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/010_npc_ai_philosophy.md).

## 010 — NPC / AI Philosophy

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/010_npc_ai_philosophy.md) — **Simplify**. **Owner:** npc (giữ, adapter tùy chọn).

**Phản biện:** Structured memory vẫn là dữ liệu cá nhân; AI classmates tăng moderation/cost mà chưa chứng minh giá trị.

**Sửa scope/schema/API:** V1 greeting theo template; V2 facts lấy từ learning read API; lưu consent/expiry/source nếu thêm memory.

**Dữ liệu / an toàn / hiệu năng:** Prompt/data isolation; không tự cấp thưởng; budget request; xoá memory/cache theo user.

**V1:** Mentor tĩnh có nhãn. **V2:** Context ngắn có opt-in. **V3:** AI classmates chỉ thử riêng.

**Mục liên quan:** [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md).

## 011 — Class Time & Lesson Structure

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/011_class_time_lesson_structure.md) — **Simplify**. **Owner:** classroom (giữ orchestration).

**Phản biện:** 40 phút không phù hợp learner 10–20 phút; session timing đang lẫn lesson pacing.

**Sửa scope/schema/API:** Lesson runner self-paced độc lập; class_session quản lý started_at, phase, revision, instructor command.

**Dữ liệu / an toàn / hiệu năng:** Reconnect lấy snapshot; timeout không tự chấm trượt; timer server khi có assessment.

**V1:** Bài 10–15 phút. **V2:** Lớp 25–40 phút tùy chọn. **V3:** Live/exam template khác.

**Mục liên quan:** [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [015](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/015_before_during_after_class.md).

## 012 — Lesson as a Sequence, Not a Page

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md) — **Keep**. **Owner:** learning → content cho định nghĩa; learning cho execution.

**Phản biện:** Bảng liệt kê không có lesson_versions/step_versions; sequence lại mặc định có collaboration.

**Sửa scope/schema/API:** Content sở hữu lesson_version + ordered steps; learning sở hữu lesson_session/checkpoint/attempt; skip step tùy policy.

**Dữ liệu / an toàn / hiệu năng:** Pin version khi start; không gửi answer key trước đáp án; resume atomic.

**V1:** Runner với read/listen/recall. **V2:** Thêm writing/class wrapper. **V3:** Branching khi đủ dữ liệu.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [071](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/071_content_sources_licensing.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 013 — Weekly Class Structure

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/013_weekly_class_structure.md) — **Postpone**. **Owner:** classroom (giữ).

**Phản biện:** Lịch thứ Hai–Chủ nhật không phải prerequisite cho spaced review; ép lịch làm nợ bài.

**Sửa scope/schema/API:** Weekly template là schedule config, không tạo mastery hay gọi LiveOps để học được.

**Dữ liệu / an toàn / hiệu năng:** Lưu timezone IANA, ngoại lệ/nghỉ và occurrence; không gửi nhắc mặc định.

**V1:** Personal review queue. **V2:** Class weekly template. **V3:** Recurring calendar nâng cao.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [062](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/062_event_calendar.md).

## 014 — Lesson Builder

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/014_lesson_builder.md) — **Simplify**. **Owner:** admin → content; admin là giao diện.

**Phản biện:** Builder thiếu lesson aggregate, nhưng lại đề xuất admin_changes như source of truth.

**Sửa scope/schema/API:** Authoring form + schema validator + preview dùng cùng runner; publish immutable version với expected_revision.

**Dữ liệu / an toàn / hiệu năng:** Content editor không có reward quyền; tránh arbitrary HTML/script; giới hạn asset.

**V1:** Form/import có kiểm định. **V2:** Teacher authoring theo lớp. **V3:** Drag/drop sau nhu cầu thật.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 015 — Before / During / After Class

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/015_before_during_after_class.md) — **Simplify**. **Owner:** classroom (giữ).

**Phản biện:** Mastery +12 không nói đo gì; phase reconnect chưa có state machine cụ thể.

**Sửa scope/schema/API:** State scheduled→running→completed/cancelled, phase_revision; debrief đọc skill evidence thay XP chung.

**Dữ liệu / an toàn / hiệu năng:** Late join không replay reward; phase change kiểm tra expected_revision.

**V1:** Resume/debrief solo. **V2:** Class phase snapshot. **V3:** Đồng bộ nhóm nâng cao.

**Mục liên quan:** [011](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/011_class_time_lesson_structure.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md).

## 016 — Break Time

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/016_break_time.md) — **Postpone**. **Owner:** social → classroom UX; social chỉ cung cấp giao tiếp.

**Phản biện:** Break là thời điểm UX, không phải lý do tạo toàn bộ friendships/messages/challenges.

**Sửa scope/schema/API:** Một link nghỉ/thoát và optional class lounge; không schema break riêng.

**Dữ liệu / an toàn / hiệu năng:** Không lôi learner sang shop bằng countdown; chặn notifications trong focus.

**V1:** Cho nghỉ và kết thúc sạch. **V2:** Lounge đã moderation. **V3:** Mini-activity tùy chọn.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md).

## 017 — Clubs

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/017_clubs.md) — **Postpone**. **Owner:** social (giữ).

**Phản biện:** Clubs thêm vòng membership/moderation cạnh class trước khi có community đủ lớn.

**Sửa scope/schema/API:** Giữ club riêng cohort nhưng tái dùng moderation/room contract; không guild economy.

**Dữ liệu / an toàn / hiệu năng:** Invite abuse, owner bỏ nhóm, archive và roster visibility phải rõ.

**V1:** Không clubs. **V2:** Thử nhóm interest có operator. **V3:** Club tự quản có giới hạn.

**Mục liên quan:** [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 018 — Class Progression

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/018_class_progression.md) — **Postpone**. **Owner:** classroom (giữ projection).

**Phản biện:** XP/rank/theme tạo tiến bộ thứ hai dễ lẫn mastery và gây áp lực đồng đội.

**Sửa scope/schema/API:** Contribution projection từ evidence đủ điều kiện; unique source_attempt, cap/user; rank thuộc prestige.

**Dữ liệu / an toàn / hiệu năng:** Không cộng theo số message; normalized cohort size; roster snapshot.

**V1:** Không class XP. **V2:** Milestone nhóm phi cạnh tranh. **V3:** Rank nếu fairness đạt.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 019 — Attendance & Class Participation

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/019_attendance_class_participation.md) — **Simplify**. **Owner:** classroom (giữ).

**Phản biện:** 20+ người để +10% gây áp lực người vắng dù văn bản nói không phạt.

**Sửa scope/schema/API:** Attendance là private participation record; công nhận async tương đương; bỏ threshold bonus.

**Dữ liệu / an toàn / hiệu năng:** Presence heartbeat không chứng minh học; không công khai người vắng.

**V1:** Không điểm danh bắt buộc. **V2:** Attendance/async completion. **V3:** Chỉ nghiên cứu bonus không ép buộc.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md).

## 020 — Class Competition

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/020_class_competition.md) — **Postpone**. **Owner:** prestige (giữ).

**Phản biện:** Helping/attendance/mastery chưa có thang so sánh; nhóm đông dễ thắng.

**Sửa scope/schema/API:** Chọn một assessment chuẩn, cohort frozen, min participation, normalized score; bỏ helping rank.

**Dữ liệu / an toàn / hiệu năng:** Chống thông đồng và lộ trình độ; bounded snapshot aggregation.

**V1:** Không class competition. **V2:** Goal hợp tác không xếp hạng. **V3:** Competition sau verification.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md).

## 021 — School Terms / Seasons

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/021_school_terms_seasons.md) — **Simplify**. **Owner:** liveops → classroom cho term; liveops cho campaign.

**Phản biện:** seasons và season.finalized bị cả prestige/liveops cùng sở hữu; term không đồng nghĩa contest.

**Sửa scope/schema/API:** academic_terms riêng competition_seasons và campaigns; prestige phát competition.season.finalized duy nhất.

**Dữ liệu / an toàn / hiệu năng:** Không reset mastery; chỉ đóng eligibility window, lưu timezone/snapshot.

**V1:** Course không season. **V2:** Academic term. **V3:** Campaign/competition liên kết ID.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [061](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md).

## 022 — Graduation & Alumni

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/022_graduation_alumni.md) — **Postpone**. **Owner:** classroom (giữ completion).

**Phản biện:** Yearbook vĩnh viễn và alumni graph thiếu visibility/deletion; certificate dễ bị hiểu là chứng nhận năng lực.

**Sửa scope/schema/API:** Course completion do learning xác nhận; class lưu ceremony refs; certificate ghi rõ loại hoàn thành.

**Dữ liệu / an toàn / hiệu năng:** Opt-in photo/history; pseudonymize khi xoá user; không bất biến PII.

**V1:** Progress cá nhân. **V2:** Completion và badge tùy chọn. **V3:** Alumni/yearbook có consent.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md).

## 023 — Core Learning Tracks

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/023_core_learning_tracks.md) — **Simplify**. **Owner:** learning → content curriculum; learning đo evidence.

**Phản biện:** Goal, skill, CEFR, topic và modality trộn thành track ngang hàng.

**Sửa scope/schema/API:** Taxonomy tách goal/skill/topic/claimed_level/activity; CEFR là nhãn nội dung, không chứng nhận từ XP.

**Dữ liệu / an toàn / hiệu năng:** Typing copy không chứng minh listening/recall; khóa một dải trình độ đủ bài.

**V1:** Pilot A2–B1 có kiểm duyệt. **V2:** IELTS/skill bổ sung. **V3:** A1–C2 theo capacity nội dung.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md).

## 024 — IELTS as a First-Class Track

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/024_ielts_as_a_first_class_track.md) — **Postpone**. **Owner:** ielts → learning assessment adapter + content pack.

**Phản biện:** Tách riêng attempts/responses/history dễ tạo mastery kép; nhãn Estimated Band chưa đảm bảo chất lượng chấm.

**Sửa scope/schema/API:** Dùng assessment_run chung với exam_spec_version và rubric_version; IELTS extension lưu mục tiêu và section config.

**Dữ liệu / an toàn / hiệu năng:** Không band từ WPM; answer key kín, autosave, consent audio; AI cost cap.

**V1:** Không hứa IELTS đủ bốn kỹ năng. **V2:** Reading/Listening training đã QA. **V3:** Full mock + W/S khi calibration đạt.

**Mục liên quan:** [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 025 — Mission-Based Learning Structure

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/025_mission_based_learning_structure.md) — **Simplify**. **Owner:** learning (giữ).

**Phản biện:** Mission narrative có thể che loại bài; mission_steps trùng lesson_steps.

**Sửa scope/schema/API:** Mission là presentation/course assignment trỏ lesson_version; dùng nhãn học rõ cạnh tên sci-fi.

**Dữ liệu / an toàn / hiệu năng:** Không thưởng mỗi bước làm tăng farm; tránh query toàn graph khi mở bài.

**V1:** Một lesson sequence. **V2:** Campaign học nhẹ. **V3:** Narrative nhiều nhánh nếu hữu ích.

**Mục liên quan:** [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [023](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/023_core_learning_tracks.md).

## 026 — Typing Experience

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md) — **Simplify**. **Owner:** typing (giữ adapter).

**Phản biện:** Deep Cockpit trước loop học tăng settings debt; TAB restart chiếm điều hướng accessibility.

**Sửa scope/schema/API:** Giữ input hiện có, settings schema nhỏ; PB keyed ruleset/content/input_mode; shortcut opt-in.

**Dữ liệu / an toàn / hiệu năng:** IME composition không chấm sớm; paste/autocorrect khác ranked; input local không gọi mạng mỗi phím.

**V1:** Minimal + font/mute/IME. **V2:** Preset/theme đã đo. **V3:** Advanced studio khi có nhu cầu.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [075](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 027 — Personalized Learning Intelligence

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md) — **Keep**. **Owner:** learning (giữ).

**Phản biện:** Tỉ lệ đúng và taxonomy lỗi chưa đủ kết luận mastery; copy spelling dễ bị đọc thành recall.

**Sửa scope/schema/API:** Evidence theo item+sense+skill+modality+hints; algorithm_version, due_at, uncertainty; rule-based trước ML.

**Dữ liệu / an toàn / hiệu năng:** Không tự nâng cấp CEFR; tránh vòng lặp chỉ luyện điểm yếu; serialize concurrent updates.

**V1:** Review deterministic và delayed recall. **V2:** Adaptive có holdout. **V3:** ML sau calibration.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md).

## 028 — Knowledge / Codex / Collections

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/028_knowledge_codex_collections.md) — **Simplify**. **Owner:** learning (giữ read model).

**Phản biện:** Word card, event stamp và IELTS medal có ba nguồn sự thật khác nhau.

**Sửa scope/schema/API:** Codex đọc mastery; cosmetic ownership đọc economy; award đọc prestige; discovered khác mastered.

**Dữ liệu / an toàn / hiệu năng:** Denominator snapshot/version; không công khai điểm yếu; paginate cards.

**V1:** Danh sách đã học/cần ôn. **V2:** Collections theo topic. **V3:** Cross-domain showcase.

**Mục liên quan:** [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md).

## 029 — Books as Progress Objects

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/029_books_as_progress_objects.md) — **Simplify**. **Owner:** learning (giữ projection).

**Phản biện:** Book là view đúng, nhưng completion % có thể thay đổi khi curriculum publish.

**Sửa scope/schema/API:** book_view trỏ course_version; completion và retained knowledge hiển thị riêng.

**Dữ liệu / an toàn / hiệu năng:** Không nhân bản progress; upgrade course cần policy; thumbnail nhẹ.

**V1:** Course progress đơn giản. **V2:** Bookshelf theo version. **V3:** Cosmetic book covers.

**Mục liên quan:** [028](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/028_knowledge_codex_collections.md), [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md).

## 030 — User Identity System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md) — **Simplify**. **Owner:** identity (giữ profile; tách authentication foundation).

**Phản biện:** Profile đang được dùng thay nền auth; user_titles/user_badges trùng awards/ownership.

**Sửa scope/schema/API:** Account/session/RBAC là platform; profile chỉ display preferences và showcase refs; field visibility riêng.

**Dữ liệu / an toàn / hiệu năng:** Private default learning target; chống enumeration/XSS; xoá/export; cache theo viewer scope.

**V1:** Account/profile tối thiểu. **V2:** Showcase/class affiliation opt-in. **V3:** Public profile có moderation.

**Mục liên quan:** [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md).

## 031 — Avatar Direction — Current Preferred Decision

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/031_avatar_direction_current_preferred_decision.md) — **Keep**. **Owner:** avatar (giữ direction).

**Phản biện:** 2D một pose phù hợp; không vì quyết định này bắt mọi learner qua editor.

**Sửa scope/schema/API:** Static starter portrait V1; modular renderer là nhánh V2, micro-motion optional.

**Dữ liệu / an toàn / hiệu năng:** Reduced-motion ưu tiên cao nhất; avatar lỗi không chặn học.

**V1:** Portrait + prototype ngoài critical path. **V2:** Modular một pose. **V3:** Motion có budget.

**Mục liên quan:** [033](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/033_avatar_technical_template.md), [039](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/039_visual_audio_brand_spine.md), [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md).

## 032 — 2D Avatar Layer System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/032_2d_avatar_layer_system.md) — **Simplify**. **Owner:** avatar (giữ loadout).

**Phản biện:** Layer list cố định sai trong một số outfit; avatar_items trùng economy items.

**Sửa scope/schema/API:** Economy catalog item_id → avatar render_definition; manifest có occlusion/slot/body_template_version.

**Dữ liệu / an toàn / hiệu năng:** Equip kiểm ownership server; preview không cấp quyền; thumbnail composite.

**V1:** Chưa editor đầy đủ. **V2:** 4–6 slot, whitelist compatibility. **V3:** Thêm slot theo QA.

**Mục liên quan:** [033](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/033_avatar_technical_template.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md).

## 033 — Avatar Technical Template

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/033_avatar_technical_template.md) — **Keep**. **Owner:** avatar cho compatibility; media giữ blob manifest.

**Phản biện:** 1024×1400 là authoring canvas, không delivery size; template thiếu anchor thực tế.

**Sửa scope/schema/API:** Khóa template v1 bằng mẫu đã duyệt; hash, anchor, z_groups, masks, variants, thumbnail refs.

**Dữ liệu / an toàn / hiệu năng:** Validate alpha/dimensions và matrix outfit; tránh texture decode phình RAM.

**V1:** Template + thử art. **V2:** CI manifest/composite. **V3:** Multiple body chỉ sau QA.

**Mục liên quan:** [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md), [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md).

## 034 — Avatar Pose

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/034_avatar_pose.md) — **Simplify**. **Owner:** avatar (giữ).

**Phản biện:** Một pose tốt; các pose Study/Cute tạo nhân chi phí mọi item, không chỉ renderer.

**Sửa scope/schema/API:** pose_id gắn template_version; fallback default nếu item không support; V1 không bán pose.

**Dữ liệu / an toàn / hiệu năng:** Không equip tổ hợp thiếu asset; không tải tất cả poses trước.

**V1:** Một portrait/pose. **V2:** Một modular pose. **V3:** Pose thứ hai khi đủ compatibility.

**Mục liên quan:** [033](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/033_avatar_technical_template.md), [032](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/032_2d_avatar_layer_system.md).

## 035 — Avatar Shop Preview

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/035_avatar_shop_preview.md) — **Postpone**. **Owner:** avatar (giữ preview; economy mua).

**Phản biện:** Preview chung renderer đúng; cache tất cả đã xem có thể tăng memory vô hạn.

**Sửa scope/schema/API:** Local ephemeral loadout, bounded LRU; equip expected_revision; purchase trả ownership receipt riêng.

**Dữ liệu / an toàn / hiệu năng:** Race buy/equip và giá đổi; không persist mỗi hover.

**V1:** Không shop preview bắt buộc. **V2:** Preview/equip nhỏ. **V3:** Set compare/random opt-in.

**Mục liên quan:** [032](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/032_2d_avatar_layer_system.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [051](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md).

## 036 — Cosmetic Content Strategy

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/036_cosmetic_content_strategy.md) — **Simplify**. **Owner:** media (giữ production).

**Phản biện:** Starter inventory 210 asset chưa tính badge/title quá lớn; tổ hợp nhiều cũng là tổ hợp cần QA.

**Sửa scope/schema/API:** Thử 1 body, 3 hair, 3 top, 2 bottom, 2 shoe, 3 accessory và vài frame; không cam kết số launch trước art test.

**Dữ liệu / an toàn / hiệu năng:** Aura không mặc nhiên rẻ trên GPU; rights và variant manifest bắt buộc.

**V1:** Art vertical slice. **V2:** Catalog nhỏ sau compatibility test. **V3:** Tăng theo production throughput.

**Mục liên quan:** [033](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/033_avatar_technical_template.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md).

## 037 — Item Sets

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/037_item_sets.md) — **Postpone**. **Owner:** economy (giữ catalog/entitlement).

**Phản biện:** Set completion bổ sung grant trigger và có thể làm người dùng mua món không muốn.

**Sửa scope/schema/API:** set_version + member item IDs; completion derive từ entitlements; unique set_bonus_grant.

**Dữ liệu / an toàn / hiệu năng:** Không power bonus; không đếm duplicate/revoked item; catalog paginate.

**V1:** Không set economy. **V2:** Một set thử nghiệm. **V3:** Set nhiều mùa khi ổn định.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [051](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md).

## 038 — Cosmetic Rarity

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/038_cosmetic_rarity.md) — **Simplify**. **Owner:** avatar → economy catalog; media trình bày.

**Phản biện:** Common…Mythic, Limited, Prestige đang trộn rarity, availability và earned origin.

**Sửa scope/schema/API:** Tách presentation_tier, acquisition_policy, availability_window; avatar chỉ render style token.

**Dữ liệu / an toàn / hiệu năng:** Không màu là tín hiệu duy nhất; tier không tự cấp permission/effect nặng.

**V1:** Không rarity ladder. **V2:** 2–3 presentation tiers. **V3:** Thêm chỉ khi có ý nghĩa.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [039](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/039_visual_audio_brand_spine.md).

## 039 — Visual / Audio Brand Spine

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/039_visual_audio_brand_spine.md) — **Keep**. **Owner:** media → design system; economy giữ business rules.

**Phản biện:** Brand spine ôm economy dễ biến design token thành rule cấp thưởng.

**Sửa scope/schema/API:** Một token/cue registry; profile/component states; catalog chỉ tham chiếu token.

**Dữ liệu / an toàn / hiệu năng:** Contrast và semantic text độc lập màu; không tải registry toàn media.

**V1:** Type/color/focus/sound nhỏ. **V2:** Avatar/class extensions. **V3:** Season skins không fork UI.

**Mục liên quan:** [073](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/073_performance_philosophy.md), [075](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md).

## 040 — Audio Design

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/040_audio_design.md) — **Simplify**. **Owner:** media (giữ audio runtime).

**Phản biện:** Tám mixer group và hover/tab sounds là scope lớn; voice NPC không luôn ưu tiên lesson audio.

**Sửa scope/schema/API:** Ba control đầu: learning, music, effects; priority exam/learning > NPC > music/effects; parent điều phối iframe.

**Dữ liệu / an toàn / hiệu năng:** Audio focus lease có release/timeout; autoplay gesture, mute và caption; không decode toàn thư viện.

**V1:** Reuse parent BGM/ducking. **V2:** Mix profiles theo activity. **V3:** Advanced mixer tùy nhu cầu.

**Mục liên quan:** [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md), [073](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/073_performance_philosophy.md).

## 041 — NPC Voice

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/041_npc_voice.md) — **Simplify**. **Owner:** npc nội dung; media owns voice asset.

**Phản biện:** Dynamic TTS cache theo text không đủ isolation khi text chứa dữ liệu người học.

**Sửa scope/schema/API:** V1 text + ít line QA; cache public chỉ cho generic, private cache theo user/retention cho personalized.

**Dữ liệu / an toàn / hiệu năng:** Voice rights, request cost cap, fallback text; không phát thông tin riêng ở lớp.

**V1:** Text/line tĩnh. **V2:** TTS generic được duyệt. **V3:** Personalized voice opt-in.

**Mục liên quan:** [010](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/010_npc_ai_philosophy.md), [040](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/040_audio_design.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md).

## 042 — VFX Language

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/042_vfx_language.md) — **Simplify**. **Owner:** media (giữ; bỏ self-integration).

**Phản biện:** media integrates media là dependency vô nghĩa; mastery gold ring có thể biến ước lượng thành sự thật.

**Sửa scope/schema/API:** Semantic cue config, không event domain cho animation; trạng thái học do learning trả.

**Dữ liệu / an toàn / hiệu năng:** Reduced motion và non-color feedback; cap concurrent effect và stop hidden tab.

**V1:** Feedback tĩnh/nhẹ. **V2:** Milestone animation nhỏ. **V3:** Signature effect hiếm.

**Mục liên quan:** [039](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/039_visual_audio_brand_spine.md), [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md).

## 043 — Reward System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md) — **Simplify**. **Owner:** economy (giữ optional).

**Phản biện:** Bảy nguồn thưởng trước khi có eligibility tạo double reward và farm dễ.

**Sửa scope/schema/API:** Chỉ accepted evidence/milestone trigger; unique user+source+rule_version+benefit; reward failure không rollback learning.

**Dữ liệu / an toàn / hiệu năng:** Không browser event tự mint; audit/reversal; async có trạng thái pending.

**V1:** Completion feedback phi tiền. **V2:** Một nguồn credit và milestone. **V3:** Thêm nguồn qua simulator.

**Mục liên quan:** [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [079](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/079_reward_simulator.md).

## 044 — Daily Check-In

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/044_daily_check_in.md) — **Reject**. **Owner:** economy (đúng owner, bỏ cơ chế đề xuất).

**Phản biện:** Login→crystal/chest/fragment thưởng mở app, trái meaningful learning và tăng currency sớm.

**Sửa scope/schema/API:** Bỏ daily login payout; nếu hiển thị consistency thì derive từ ngày học đủ điều kiện, không claim endpoint.

**Dữ liệu / an toàn / hiệu năng:** Timezone hopping và streak pressure; không auto-reset động lực khi nghỉ.

**V1:** Không payout đăng nhập. **V2:** Weekly recap tự nguyện. **V3:** Không khôi phục chest ladder mặc định.

**Mục liên quan:** [076](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md), [047](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/047_weekly_rewards.md).

## 045 — Active Session Rewards

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/045_active_session_rewards.md) — **Reject**. **Owner:** economy (đúng owner, bỏ time ladder).

**Phản biện:** 15/30/60 phút active vẫn tối ưu thời gian và script heartbeat, dù không AFK.

**Sửa scope/schema/API:** Bỏ thưởng theo phút; reward theo evidence có cap; duration chỉ giúp pacing và vận hành.

**Dữ liệu / an toàn / hiệu năng:** Không giám sát mỗi phím để chứng minh active; learner chậm không bị thiệt.

**V1:** Không timed payout. **V2:** Qualified evidence rewards. **V3:** Điều chỉnh theo outcome.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md).

## 046 — Daily Activity Meter

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/046_daily_activity_meter.md) — **Postpone**. **Owner:** economy (giữ incentive projection).

**Phản biện:** 100 điểm nhiều mode vẫn thành checklist; bản ví dụ cộng 75 không đủ định nghĩa điều kiện.

**Sửa scope/schema/API:** Nếu thử, nhiều đường learn-only tương đương; derive capped qualified events, không meter balance riêng.

**Dữ liệu / an toàn / hiệu năng:** Cap chung ngăn stack daily/weekly/game; không rewards cho replay event.

**V1:** Personal plan không điểm. **V2:** Thử weekly goal trước. **V3:** Daily meter chỉ sau benefit test.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [047](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/047_weekly_rewards.md), [079](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/079_reward_simulator.md).

## 047 — Weekly Rewards

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/047_weekly_rewards.md) — **Simplify**. **Owner:** economy (giữ).

**Phản biện:** Weekly crystal/chest không cần để giúp học đều; rule snapshot tốt nhưng thiếu period identity.

**Sửa scope/schema/API:** Recap trước; nếu reward thì period_id + timezone frozen + rule_version + semantic grant key.

**Dữ liệu / an toàn / hiệu năng:** DST/timezone changes không tạo hai tuần claim; công nhận nhịp học khác nhau.

**V1:** Recap tiến độ. **V2:** Một bonus deterministic. **V3:** Tối ưu theo cohort, không chest RNG.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md).

## 048 — Long-Term Rewards

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/048_long_term_rewards.md) — **Simplify**. **Owner:** economy owns grant; learning/prestige owns eligibility.

**Phản biện:** Certification, hours, mastered item và PB không cùng loại bằng chứng.

**Sửa scope/schema/API:** milestone_evidence_id tham chiếu nguồn; entitlement chỉ materialize reward, không định nghĩa mastery.

**Dữ liệu / an toàn / hiệu năng:** Grant/revoke từ nguồn đã kiểm tra; không gọi completion là chứng nhận chính thức.

**V1:** Course completion record. **V2:** Cosmetic milestone. **V3:** Achievement nâng cao.

**Mục liên quan:** [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md).

## 049 — Reward Center

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/049_reward_center.md) — **Simplify**. **Owner:** economy (giữ read model).

**Phản biện:** Claim inbox thêm việc phải làm và nguy cơ mất thưởng vì không mở tab.

**Sửa scope/schema/API:** Auto-grant deterministic benefit; inbox là receipt/unread; chỉ choice reward cần claim.

**Dữ liệu / an toàn / hiệu năng:** Claim-all trả từng kết quả idempotent; unread state không quyết định ownership.

**V1:** Không reward inbox. **V2:** Receipt list gọn. **V3:** Choice reward nếu cần.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md).

## 050 — Economy

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md) — **Simplify**. **Owner:** economy (giữ duy nhất ledger/catalog/entitlements).

**Phản biện:** double-entry-ish không phải invariant; Credits/Crystals/token/fragment vượt V1.

**Sửa scope/schema/API:** V2 chỉ earned Credits; integer ledger balanced qua issuance/sink accounts, atomic wallet/order/ownership, semantic dedupe.

**Dữ liệu / an toàn / hiệu năng:** Concurrent spend không âm; audit compensating reversal; không cross-write inventory từ avatar.

**V1:** Không ví cần thiết. **V2:** Một currency đóng, không trade. **V3:** Currency mới chỉ có lý do riêng.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [079](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/079_reward_simulator.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 051 — Shop System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md) — **Postpone**. **Owner:** economy (giữ).

**Phản biện:** Nhiều shop và Honor Store mâu thuẫn prestige không được mua.

**Sửa scope/schema/API:** Một catalog; earned-only award nằm gallery tách purchase; price/version/eligibility server kiểm tra.

**Dữ liệu / an toàn / hiệu năng:** Hai tab mua cùng item, stale price, sold-out phải atomic; không client balance authority.

**V1:** Không shop prerequisite. **V2:** Catalog nhỏ giá cố định. **V3:** Rotation sau simulator.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [035](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/035_avatar_shop_preview.md), [093](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/093_what_must_never_be_sold.md).

## 052 — Stationery as a Signature Cosmetic System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/052_stationery_as_a_signature_cosmetic_system.md) — **Simplify**. **Owner:** economy entitlement; design system render.

**Phản biện:** Caret/highlighter/ink cosmetic có thể làm giảm khả năng đọc; brand không được định nghĩa domain.

**Sửa scope/schema/API:** Theme tokens có contract theo surface; free accessible defaults; cosmetic item trỏ token bundle.

**Dữ liệu / an toàn / hiệu năng:** Contrast/motion audit trước publish; không cosmetic đổi grading/hints.

**V1:** Một theme đọc rõ. **V2:** Stationery nhỏ. **V3:** Bộ cosmetic rộng nếu hữu ích.

**Mục liên quan:** [039](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/039_visual_audio_brand_spine.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [075](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md).

## 053 — Limited & Seasonal Items

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/053_limited_seasonal_items.md) — **Postpone**. **Owner:** economy (giữ availability).

**Phản biện:** permanent/seasonal/may_return/never_return không loại trừ nhau; quantity scarcity thiếu allocation.

**Sửa scope/schema/API:** Tách recurrence_policy, window, eligibility, supply_cap; serial mint dưới transaction; lời hứa exclusivity versioned.

**Dữ liệu / an toàn / hiệu năng:** Không đếm ngược giả; timezone rõ; hủy/revoke không tái dùng serial lịch sử.

**V1:** Không limited shop. **V2:** Season skin có return policy. **V3:** Capped supply khi vận hành đủ.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [061](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 054 — Prestige System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md) — **Postpone**. **Owner:** prestige (giữ award/competition).

**Phản biện:** Prestige đang bao trùm mastery, completion và participation dễ lẫn “verified”.

**Sửa scope/schema/API:** Award_definition có evidence_type và verification_policy; competition riêng learning progress.

**Dữ liệu / an toàn / hiệu năng:** Award chỉ sau adjudication; appeal/revoke có revision; không bảng mastery thứ hai.

**V1:** Private completion/PB. **V2:** Achievement không competitive. **V3:** Competitive prestige verified.

**Mục liên quan:** [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md).

## 055 — Ranking Center

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/055_ranking_center.md) — **Postpone**. **Owner:** prestige (giữ projection).

**Phản biện:** 10 chiều ×14 loại rank phân mảnh cohort và xếp hạng thang chưa calibrated.

**Sửa scope/schema/API:** Bắt đầu 1 ruleset typing opt-in; ruleset_hash/input_mode/content_version/period; không global English score.

**Dữ liệu / an toàn / hiệu năng:** Min cohort, ties, pseudonym/privacy; snapshot/query bounded.

**V1:** Private PB. **V2:** Private challenge results. **V3:** Một board verified rồi mở rộng.

**Mục liên quan:** [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md), [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md).

## 056 — Personal Best & Improvement Prestige

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/056_personal_best_improvement_prestige.md) — **Simplify**. **Owner:** prestige → typing/learning owns PB; prestige reads verified awards.

**Phản biện:** PB không cần prestige subsystem; Most Improved dễ sandbag baseline.

**Sửa scope/schema/API:** PB keyed comparable ruleset; learning improvement từ delayed assessments; nhiều lần đo baseline.

**Dữ liệu / an toàn / hiệu năng:** Không so WPM khác duration/input; private mặc định; không replay PB reward.

**V1:** Private PB. **V2:** Progress milestones. **V3:** Most Improved có eligibility rõ.

**Mục liên quan:** [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md).

## 057 — Hall of Fame

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/057_hall_of_fame.md) — **Postpone**. **Owner:** prestige (giữ).

**Phản biện:** Immutable Hall of Fame tuyệt đối cản sửa cheat, khiếu nại và xoá dữ liệu cá nhân.

**Sửa scope/schema/API:** Final result revisions append-only; public view latest effective revision; profile ref có thể ẩn/pseudonymize.

**Dữ liệu / an toàn / hiệu năng:** Không khóa PII vĩnh viễn; CDN purge khi correction; kiểm chứng trước publish.

**V1:** Không Hall. **V2:** Không cần cho pilot class. **V3:** History sau season verified.

**Mục liên quan:** [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 058 — Exclusive Prestige Cosmetics

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/058_exclusive_prestige_cosmetics.md) — **Postpone**. **Owner:** prestige eligibility; economy entitlement; avatar renderer.

**Phản biện:** Prestige không nên tự tạo inventory riêng; non-tradeable chưa đủ chặn admin/shop mint.

**Sửa scope/schema/API:** Award-issued entitlement có grant_reason + source_award; catalog acquisition_policy=award_only.

**Dữ liệu / an toàn / hiệu năng:** Purchase path và admin grant reject nếu thiếu valid award; revoke loadout fallback.

**V1:** Không prestige cosmetic. **V2:** Completion badge rõ loại. **V3:** Exclusive award visual.

**Mục liên quan:** [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [032](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/032_2d_avatar_layer_system.md).

## 059 — Item Provenance

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/059_item_provenance.md) — **Simplify**. **Owner:** prestige → economy entitlement provenance.

**Phản biện:** Provenance cần cho item thường lẫn prestige; hiện không có owner chung.

**Sửa scope/schema/API:** ownership_origin(source_type, source_id, acquired_at, policy_version); prestige bổ sung evidence ref.

**Dữ liệu / an toàn / hiệu năng:** Serial có unique constraint; public view giấu actor/private evidence.

**V1:** Provenance nội dung trước. **V2:** Item receipt đơn giản. **V3:** Serial/season khi cần.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md).

## 060 — Tournaments & Exams

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/060_tournaments_exams.md) — **Postpone**. **Owner:** prestige tournament; learning assessment.

**Phản biện:** Tournament và exam là hai lifecycle khác nhau; bracket 256 chưa có người dùng đủ.

**Sửa scope/schema/API:** Tách assessment_run khỏi competition_entry; tournament tham chiếu verified result, không own đáp án.

**Dữ liệu / an toàn / hiệu năng:** Fairness/ties/disconnect và appeals trước bracket; không streaming/spectator V1.

**V1:** Learning assessment nhỏ. **V2:** Timed practice. **V3:** Tournament sau đủ participants/ops.

**Mục liên quan:** [024](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/024_ielts_as_a_first_class_track.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md).

## 061 — Scheduled Events

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md) — **Postpone**. **Owner:** liveops (giữ campaign).

**Phản biện:** Lịch dày mỗi tối là nghĩa vụ và tạo vận hành liên tục.

**Sửa scope/schema/API:** Một campaign async có occurrence IDs; phần live không có lợi thế mastery hoặc reward thiết yếu.

**Dữ liệu / an toàn / hiệu năng:** Dedup scheduled jobs; cancel policy; UTC instant + timezone recurrence; quiet hours.

**V1:** Không LiveOps runtime. **V2:** Một thử nghiệm async. **V3:** Live nhiều slot nếu đủ demand.

**Mục liên quan:** [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [062](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/062_event_calendar.md).

## 062 — Event Calendar

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/062_event_calendar.md) — **Simplify**. **Owner:** liveops → calendar read model; source owner giữ schedule.

**Phản biện:** Calendar không nên sở hữu cả class/club/event schedule.

**Sửa scope/schema/API:** Unified DTO {source_type, source_id, occurrence_id, start,end,tz,revision}; source commands riêng.

**Dữ liệu / an toàn / hiệu năng:** Filter quyền trước cache; DST/ICS nếu thêm cần test; window pagination.

**V1:** Review due trong Home. **V2:** Class calendar. **V3:** Aggregate events/club.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [061](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md).

## 063 — School Events

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/063_school_events.md) — **Postpone**. **Owner:** liveops (giữ).

**Phản biện:** Festival nhiều activity tạo content/event QA lớn trước khi loop học tốt.

**Sửa scope/schema/API:** Bundle published activity IDs, không viết game engine cho từng event.

**Dữ liệu / an toàn / hiệu năng:** Licensing/expiry từng asset; hoạt động async tương đương; preload riêng route.

**V1:** Không festival. **V2:** Một theme course tùy chọn. **V3:** Festival reuse activity đủ ổn.

**Mục liên quan:** [061](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md), [068](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/068_group_activities_mini_games.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md).

## 064 — Social System

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md) — **Postpone**. **Owner:** social (giữ chat/friends); platform safety là prerequisite.

**Phản biện:** Report/mute/block mới là nút, thiếu moderator queue, enforcement và retention.

**Sửa scope/schema/API:** Text class room có ACL; report case lifecycle, block policy, rate limits, deletion/takedown; chưa DM/file.

**Dữ liệu / an toàn / hiệu năng:** Server kiểm membership mỗi send/read/reconnect; operator coverage; tên hiển thị cũng UGC.

**V1:** Không user chat công khai. **V2:** Private class text đã moderation. **V3:** Friends/clubs sau safety gate.

**Mục liên quan:** [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md), [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md).

## 065 — Social Presence

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/065_social_presence.md) — **Postpone**. **Owner:** social (giữ ephemeral).

**Phản biện:** Online count không được trở thành attendance truth; opt-out phải áp cả aggregate nhỏ.

**Sửa scope/schema/API:** TTL presence theo room, approximate; authorised subscribers; không ghi heartbeat DB.

**Dữ liệu / an toàn / hiệu năng:** Không expose last_seen rộng; hide small cohort inference; multi-tab aggregate.

**V1:** Không presence. **V2:** Polling/TTL cho class. **V3:** Realtime khi latency cần.

**Mục liên quan:** [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md), [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md).

## 066 — Study Rooms

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/066_study_rooms.md) — **Postpone**. **Owner:** social (giữ room).

**Phản biện:** Study room không voice/video vẫn cần ACL, scheduling và abuse response.

**Sửa scope/schema/API:** Reuse room membership; activity independently executable; room closure/host transfer policy.

**Dữ liệu / an toàn / hiệu năng:** Không public discovery trước moderation; limit room/fanout; degrade về solo.

**V1:** Solo study đầy đủ. **V2:** Invite-only room thử nghiệm. **V3:** Discovery sau safety/scale.

**Mục liên quan:** [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md), [065](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/065_social_presence.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md).

## 067 — Friend Challenges

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/067_friend_challenges.md) — **Postpone**. **Owner:** social owns invite; activity owns score.

**Phản biện:** Async tiết kiệm hạ tầng nhưng cùng đề chưa chắc công bằng nếu xem đáp án trước.

**Sửa scope/schema/API:** Challenge snapshot rules/content/seed/deadline/attempt_limit; result_refs từ adapter; reveal sau cả hai hoặc deadline.

**Dữ liệu / an toàn / hiệu năng:** Invite/block/rate limits; no coin wagering; không grade client totals.

**V1:** Private PB. **V2:** Async friend challenge giới hạn. **V3:** Ranked challenge verified.

**Mục liên quan:** [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md), [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 068 — Group Activities / Mini-Games

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/068_group_activities_mini_games.md) — **Postpone**. **Owner:** learning → activities; learning owns evidence.

**Phản biện:** Nhiều minigame trùng learning core; game score không là mastery.

**Sửa scope/schema/API:** Activity capability registry, objective/evidence contract; nhóm là wrapper, không engine chung bắt buộc.

**Dữ liệu / an toàn / hiệu năng:** One completion per item; no duplicate XP; load theo route.

**V1:** Reuse activity hiện có. **V2:** Một activity hợp tác. **V3:** Game mới qua learning evaluation.

**Mục liên quan:** [069](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/069_space_typings_role.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md).

## 069 — Space Typing’s Role

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/069_space_typings_role.md) — **Keep**. **Owner:** typing → activities/space-typing adapter.

**Phản biện:** Shared IDs đúng; “phát reward events” dễ cho game quyền mint và repetition bị gọi mastery.

**Sửa scope/schema/API:** Game gửi candidate evidence, server learning validate; economy chỉ consume accepted event. Combat progression độc lập.

**Dữ liệu / an toàn / hiệu năng:** Không import game currency thành academy credit; giữ adapter/version handshake.

**V1:** Tích hợp hiện có + contract migration. **V2:** Learning-context launch nâng cấp. **V3:** Thêm mode nếu hiệu quả.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [073](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/073_performance_philosophy.md).

## 070 — Content & Learning Data Foundation

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md) — **Keep**. **Owner:** content_ops → content canonical registry; learning owns learner state.

**Phản biện:** Rich records đang vừa ở content_records vừa learning_items; compact ABI thiếu sense/version mapping.

**Sửa scope/schema/API:** Một content_id+sense_id+immutable_version; ABI là export adapter; lesson/assessment reference canonical registry.

**Dữ liệu / an toàn / hiệu năng:** Dedupe không gộp khác nghĩa; block/takedown có cache invalidation; migration giữ legacy IDs.

**V1:** Registry/publish và adapter. **V2:** Content authoring mở rộng. **V3:** Search riêng khi đo cần.

**Mục liên quan:** [071](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/071_content_sources_licensing.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 071 — Content Sources & Licensing

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/071_content_sources_licensing.md) — **Keep**. **Owner:** content_ops (giữ rights review).

**Phản biện:** License allowlist chưa đủ provenance của adaptation, audio và từng derivative.

**Sửa scope/schema/API:** Asset/content có source, rights_basis, evidence_ref, attribution, derivative_chain, review_status; publish gate.

**Dữ liệu / an toàn / hiệu năng:** Không coi AI-generated tự động có quyền; block unknown theo policy nội bộ; takedown phủ CDN.

**V1:** Rights trước publish. **V2:** Batch review/expiry queue. **V3:** Mở rộng nguồn đã kiểm định.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md).

## 072 — Media Production Strategy

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md) — **Simplify**. **Owner:** media (giữ assets/jobs); content_ops kiểm rights.

**Phản biện:** Hai accent, timing, dynamic generation và search là nhiều pipeline chưa cần cùng lúc.

**Sửa scope/schema/API:** Một locale ưu tiên; deterministic job key input_hash+voice+locale+model_version; manifest/CDN và retry.

**Dữ liệu / an toàn / hiệu năng:** Private audio signed access; không cache PII public; validate MIME/duration; codec fallback test device.

**V1:** Audio chuẩn ít, pre-generated. **V2:** Hai accent/timing có giá trị. **V3:** On-demand có cost/quality gate.

**Mục liên quan:** [071](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/071_content_sources_licensing.md), [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md).

## 073 — Performance Philosophy

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/073_performance_philosophy.md) — **Keep**. **Owner:** platform (giữ).

**Phản biện:** Singleton audio toàn app không trực tiếp áp dụng nhiều iframe; lazy loading chưa có gate đo.

**Sửa scope/schema/API:** Parent audio focus contract + child lifecycle pause/dispose; core route không phụ thuộc game load.

**Dữ liệu / an toàn / hiệu năng:** Unload iframe/subscription; trace route payload và memory sau nhiều switch.

**V1:** CI budget + lifecycle. **V2:** Realtime đo theo demand. **V3:** Scale theo bottleneck.

**Mục liên quan:** [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md), [040](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/040_audio_design.md).

## 074 — Asset Performance Budgets

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md) — **Simplify**. **Owner:** platform (giữ engineering policy).

**Phản biện:** Gọi “budgets” nhưng không có số; còn tạo outbox.event.created như business event.

**Sửa scope/schema/API:** Dùng budget proposal có thiết bị/network/scenario; outbox là hạ tầng không event domain cho UI.

**Dữ liệu / an toàn / hiệu năng:** Đo decoded memory và p95 latency; payload caps; fail build trên budget đã ratify.

**V1:** Khóa budget provisional rồi đo. **V2:** RUM cohort mobile. **V3:** Điều chỉnh bằng evidence.

**Mục liên quan:** [073](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/073_performance_philosophy.md), [072](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/072_media_production_strategy.md).

## 075 — Mobile as a First-Class Experience

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md) — **Keep**. **Owner:** platform UX (giữ).

**Phản biện:** Voice/chat/shop trên mobile chưa đảm bảo lesson input/autosave/accessibility.

**Sửa scope/schema/API:** Responsive runner trước; keyboard/IME/touch contract; static avatar fallback; core parity dù meta tắt.

**Dữ liệu / an toàn / hiệu năng:** Background audio và offline resume; không xếp soft keyboard cùng physical keyboard ranked.

**V1:** Read/listen/review đủ trên mobile. **V2:** Class/text interaction. **V3:** Rich mode tùy khả năng.

**Mục liên quan:** [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md), [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md).

## 076 — Reward / Economy Anti-Patterns to Avoid

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md) — **Keep**. **Owner:** economy policy (giữ).

**Phản biện:** Anti-pattern đúng nhưng 044–046 và 050 vi phạm ngay trong cùng bộ tài liệu.

**Sửa scope/schema/API:** Biến policy thành gate: no login/time payout, no purchasable evidence, no required game route.

**Dữ liệu / an toàn / hiệu năng:** Test stacking/caps; accessible defaults không bị khóa cosmetic; không dùng expiry ép học.

**V1:** Loại reward pressure. **V2:** Audit economy nhỏ. **V3:** Review mọi campaign.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [044](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/044_daily_check_in.md), [045](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/045_active_session_rewards.md).

## 077 — Prestige Integrity

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md) — **Keep**. **Owner:** prestige policy; activity verifier thực thi.

**Phản biện:** Client run signature, paste detection không chứng minh con người; Verified dễ hứa quá mức.

**Sửa scope/schema/API:** Server-issued run nonce/rules/content, replay checks, evidence trust tier, review/appeal; signed challenge không ký sự thật input.

**Dữ liệu / an toàn / hiệu năng:** Chấp nhận browser không chống bot tuyệt đối; raw keystrokes bounded/retention; IME không mặc định cheat.

**V1:** Phân loại trust, private results. **V2:** Verification thử kín. **V3:** Public rank sau false-positive audit.

**Mục liên quan:** [026](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/026_typing_experience.md), [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 078 — Admin / Game Master / Learning Operations Console

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md) — **Simplify**. **Owner:** admin → application surface; domain giữ mutation.

**Phản biện:** Admin_changes/approval_requests không thay business state; universal console quá lớn.

**Sửa scope/schema/API:** V1 content preview/publish, user access, audit, job errors, takedown; command handler owner validate.

**Dữ liệu / an toàn / hiệu năng:** Role scope, audit actor/reason, secrets server-side; local token hiện tại không là auth production.

**V1:** Ops tối thiểu từ đầu. **V2:** Class/moderation/economy tools cùng feature. **V3:** LiveOps/appeals đầy đủ.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [030](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/030_user_identity_system.md).

## 079 — Reward Simulator

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/079_reward_simulator.md) — **Keep**. **Owner:** admin → economy model; admin chỉ chạy scenario.

**Phản biện:** Đặt simulation ở Phase 6 sau khi economy chạy là quá muộn.

**Sửa scope/schema/API:** Pure deterministic simulator dùng cùng reward function/version, seed, replay fixtures; không production credentials.

**Dữ liệu / an toàn / hiệu năng:** Burst/retry/timezone/farm/sink exhaustion; percentile và worst-case; không chỉ mean.

**V1:** Chưa cần khi chưa currency. **V2:** Bắt buộc trước credit launch. **V3:** Stochastic scenarios từ dữ liệu thật.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md).

## 080 — Lesson Simulator

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/080_lesson_simulator.md) — **Simplify**. **Owner:** admin → content preview + learning runner.

**Phản biện:** Simulator chỉ cộng phút không kiểm tra thực tế đọc/nghe/chuyển task.

**Sửa scope/schema/API:** Reuse published runner preview; duration interval theo text/audio/transition/hints; không giả learner mastery.

**Dữ liệu / an toàn / hiệu năng:** Không ghi practice giả vào production; audio load budget tính vào cold path.

**V1:** Estimate + preview. **V2:** Teacher timing từ quan sát. **V3:** Adaptive estimator sau calibration.

**Mục liên quan:** [014](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/014_lesson_builder.md), [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md).

## 081 — LiveOps Admin

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/081_liveops_admin.md) — **Postpone**. **Owner:** admin → liveops application surface.

**Phản biện:** Event Builder đang sở hữu class schedule/exam/shop cùng lúc, dẫn tới owner chồng.

**Sửa scope/schema/API:** Shared form/version/audit components; source-specific validators/commands; không universal workflow engine.

**Dữ liệu / an toàn / hiệu năng:** Publish expected_revision; cancel không xoá lịch sử; privilege tách reward/calendar.

**V1:** Content ops đủ. **V2:** Schedule admin cho class. **V3:** Campaign editor và jobs audit.

**Mục liên quan:** [061](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md), [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md).

## 082 — Proposed Master Plan Document Split

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/082_proposed_master_plan_document_split.md) — **Simplify**. **Owner:** product (giữ docs).

**Phản biện:** 9 master plan bỏ qua migration, safety và content/assessment như deliverable riêng.

**Sửa scope/schema/API:** Giữ 106 mục làm traceability; gom ADR/contracts theo owner; thêm migration/safety/verification docs.

**Dữ liệu / an toàn / hiệu năng:** Một định nghĩa invariant tránh 106 checklist drift; không tạo microservice theo file.

**V1:** Core contracts/roadmap. **V2:** Owner specs theo feature. **V3:** ADR khi tách service.

**Mục liên quan:** [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md), [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md).

## 083 — Recommended Build Order

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md) — **Reject**. **Owner:** product (giữ owner, thay thứ tự).

**Phản biện:** Phase 1 avatar/shop, Phase 2 economy, Phase 3 learning trái learning-first; simulator tận Phase 6.

**Sửa scope/schema/API:** Thay bằng baseline→content/auth/ops→learning→pilot gate→nhánh class hoặc identity/economy→verified liveops.

**Dữ liệu / an toàn / hiệu năng:** Không làm migration big bang; rollback ở từng slice; compatibility tests trước integration.

**V1:** Learning vertical slice. **V2:** Class/economy độc lập có gates. **V3:** Competition/LiveOps.

**Mục liên quan:** [097](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md), [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [079](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/079_reward_simulator.md).

## 084 — Important Non-Goals / Current Rejections

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/084_important_non_goals_current_rejections.md) — **Keep**. **Owner:** product (giữ).

**Phản biện:** Non-goals hợp lý nhưng không nên ngầm biến thành V3 backlog.

**Sửa scope/schema/API:** Giữ 3D/free roam/power economy/trade ngoài roadmap cả ba phiên bản; đổi cần ADR và lý do riêng.

**Dữ liệu / an toàn / hiệu năng:** Không xoá game hiện có chỉ vì có combat; giữ boundary combat/learning.

**V1:** Enforce non-goals. **V2:** Giữ nguyên. **V3:** Giữ nguyên trừ quyết định mới.

**Mục liên quan:** [001](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/001_product_reframing.md), [069](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/069_space_typings_role.md).

## 085 — Core UX Example — Simple Learner

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/085_core_ux_example_simple_learner.md) — **Keep**. **Owner:** product (giữ acceptance scenario).

**Phản biện:** Simple learner là bài test quan trọng nhất; progress 68% thiếu denominator.

**Sửa scope/schema/API:** Acceptance: start→answer→feedback→resume→review không gọi social/economy; progress gắn course_version.

**Dữ liệu / an toàn / hiệu năng:** Test meta API down, slow network, mute/reduced-motion và mobile.

**V1:** Release gate V1. **V2:** Regression mọi feature. **V3:** Tiếp tục gate bắt buộc.

**Mục liên quan:** [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [075](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md).

## 086 — Core UX Example — Social Learner

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/086_core_ux_example_social_learner.md) — **Postpone**. **Owner:** product (giữ scenario).

**Phản biện:** PB classmates/feed online tiết lộ hoạt động nếu auto-public.

**Sửa scope/schema/API:** Composition view đọc projections có visibility; không lưu social persona state riêng.

**Dữ liệu / an toàn / hiệu năng:** Block/mute xuyên feed/challenge; Home không fanout mọi class.

**V1:** Không feed. **V2:** Class view opt-in. **V3:** Friends/activity feed có cap.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md), [065](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/065_social_presence.md).

## 087 — Core UX Example — Competitive User

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/087_core_ux_example_competitive_user.md) — **Postpone**. **Owner:** product (giữ scenario).

**Phản biện:** Ranked IELTS và English mastery chưa có comparable assessment; không phải toggle UI đủ.

**Sửa scope/schema/API:** Scenario chỉ enabled khi ruleset/verification/appeal đã đạt; học riêng vẫn hoạt động.

**Dữ liệu / an toàn / hiệu năng:** Không mix casual/unverified; hiển thị policy và pending; load ranking on demand.

**V1:** PB private. **V2:** Challenge thử kín. **V3:** Verified ranked experience.

**Mục liên quan:** [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [077](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/077_prestige_integrity.md).

## 088 — Core UX Example — Cosmetic / Collector User

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/088_core_ux_example_cosmetic_collector_user.md) — **Postpone**. **Owner:** product (giữ scenario).

**Phản biện:** Collector loop xoay quanh limited token/shop rotation dễ biến retention thành FOMO.

**Sửa scope/schema/API:** Bắt đầu earned cosmetic không thời hạn; catalog view chỉ đọc economy, không own progress.

**Dữ liệu / an toàn / hiệu năng:** Không reward cho mua; budget asset và no dark patterns; accessible default miễn phí.

**V1:** Free starter identity. **V2:** Catalog thường và receipt. **V3:** Collections theo evidence.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [051](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md), [076](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md).

## 089 — Core UX Example — Teacher

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/089_core_ux_example_teacher.md) — **Simplify**. **Owner:** product UX; classroom/content ownership.

**Phản biện:** Teacher flow bỏ qua quyền publish, cancellation và version thay đổi sau giao bài.

**Sửa scope/schema/API:** Teacher chọn approved lesson hoặc tạo draft; publisher duyệt; assignment pin version, follow-up từ learning.

**Dữ liệu / an toàn / hiệu năng:** Không export toàn learner corpus; class ACL và audit; preview không mutate progress.

**V1:** Internal editor flow. **V2:** Pilot teacher đầy đủ scope. **V3:** Delegated authoring có policy.

**Mục liên quan:** [014](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/014_lesson_builder.md), [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 090 — Brand Direction

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/090_brand_direction.md) — **Keep**. **Owner:** media/design system (giữ).

**Phản biện:** Brand thesis tốt; typography/audio/asset consistency đáng giá hơn thêm hệ meta.

**Sửa scope/schema/API:** Gộp bible với 039; một bộ tokens/components/character art direction, không schema brand riêng.

**Dữ liệu / an toàn / hiệu năng:** Contrast, localization và loading placeholders; không tải neon/VFX trên reading.

**V1:** Design system nhỏ hoàn chỉnh. **V2:** Avatar/class kit. **V3:** Season variant cùng components.

**Mục liên quan:** [039](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/039_visual_audio_brand_spine.md), [074](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/074_asset_performance_budgets.md).

## 091 — Why “Academic Objects” Matter

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/091_why_academic_objects_matter.md) — **Simplify**. **Owner:** economy → product/design policy.

**Phản biện:** Academic objects là ngôn ngữ thiết kế; không cần domain economy để có notebook UI.

**Sửa scope/schema/API:** Tách decorative certificate khỏi proof of completion; functional study tools luôn sẵn.

**Dữ liệu / an toàn / hiệu năng:** Không bán accessibility/hints cơ bản; cosmetic không đổi grading.

**V1:** UI học có brand. **V2:** Stationery token pack. **V3:** Collector extensions.

**Mục liên quan:** [052](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/052_stationery_as_a_signature_cosmetic_system.md), [093](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/093_what_must_never_be_sold.md).

## 092 — Recognition & Status

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/092_recognition_status.md) — **Simplify**. **Owner:** prestige → product recognition policy.

**Phản biện:** Recognition đa trục hợp lý nhưng helping/reputation dễ farm hoặc thiên vị.

**Sửa scope/schema/API:** Personal milestone/private feedback trước; public award có evidence và consent; không universal score.

**Dữ liệu / an toàn / hiệu năng:** Bỏ ranking helping nếu không đo đáng tin; avoid shame cho người học chậm.

**V1:** Private progress. **V2:** Class acknowledgments có lựa chọn. **V3:** Award sau verification.

**Mục liên quan:** [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md).

## 093 — What Must Never Be Sold

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/093_what_must_never_be_sold.md) — **Keep**. **Owner:** prestige policy + economy enforcement.

**Phản biện:** “Không bán” mới là lời hứa nếu catalog/admin vẫn mint mọi item.

**Sửa scope/schema/API:** acquisition_policy enforced cùng code cho purchase/admin/reward; award_only cần source_award verified.

**Dữ liệu / an toàn / hiệu năng:** Test forged request, direct admin grant, revoked award; không bán lookalike gây nhầm.

**V1:** Giữ policy. **V2:** Enforce trước shop. **V3:** Audit mọi prestige release.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [054](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/054_prestige_system.md), [078](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/078_admin_game_master_learning_operations_console.md).

## 094 — What Can Be Purchased With Earned Credits

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/094_what_can_be_purchased_with_earned_credits.md) — **Simplify**. **Owner:** economy (giữ).

**Phản biện:** Danh sách pose/emote/VFX vượt catalog nhỏ và dễ bán tính năng accessibility.

**Sửa scope/schema/API:** Earned Credits chỉ cosmetic; stable price/item_version, free baseline đủ đọc/học.

**Dữ liệu / an toàn / hiệu năng:** Không link spend vào mastery; no negative wallet; asset downgrade khi yếu.

**V1:** Không credit store. **V2:** Một catalog ít item. **V3:** Thêm theo QA/usage.

**Mục liên quan:** [050](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/050_economy.md), [051](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/051_shop_system.md), [075](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/075_mobile_as_a_first_class_experience.md).

## 095 — “Living Even When Alone” Principle

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/095_living_even_when_alone_principle.md) — **Simplify**. **Owner:** npc → product UX; npc presenter.

**Phản biện:** “Alive” không cần upcoming event/class nếu learner solo chưa tham gia.

**Sửa scope/schema/API:** Greeting có nhãn và next review thật; không sinh recent human activity giả.

**Dữ liệu / an toàn / hiệu năng:** Không lưu relationship score V1; no polling NPC schedules; text fallback.

**V1:** Daily plan + mentor tĩnh. **V2:** Context rõ nguồn. **V3:** NPC phong phú sau evaluation.

**Mục liên quan:** [010](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/010_npc_ai_philosophy.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md).

## 096 — Social Retention Principle

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/096_social_retention_principle.md) — **Postpone**. **Owner:** social → product hypothesis.

**Phản biện:** “Strongest loop” là giả thuyết, không lý do xây cả network trước learning.

**Sửa scope/schema/API:** Pilot class so với solo trên delayed learning, voluntary return và moderation load; không schema retention.

**Dữ liệu / an toàn / hiệu năng:** Tránh spam invite/notification; phân biệt selection bias với causal effect.

**V1:** Không phụ thuộc social. **V2:** Class pilot có tiêu chí. **V3:** Mở rộng khi lợi ích rõ.

**Mục liên quan:** [008](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/008_class_system.md), [064](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/064_social_system.md), [097](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md).

## 097 — Learning Retention Principle

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md) — **Keep**. **Owner:** learning (giữ).

**Phản biện:** Đây phải là dependency spine, hiện bị đặt sau economy trong build order.

**Sửa scope/schema/API:** Goal→lesson→feedback→due review→evidence progress; mọi nhánh meta tháo được.

**Dữ liệu / an toàn / hiệu năng:** Tắt economy/social/game mà vẫn học/resume được; bảo toàn lịch sử khi migration.

**V1:** Core release gate. **V2:** Mở rộng content. **V3:** Giữ gate mọi phiên bản.

**Mục liên quan:** [012](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/012_lesson_as_a_sequence_not_a_page.md), [027](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/027_personalized_learning_intelligence.md), [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md).

## 098 — Reward Retention Principle

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/098_reward_retention_principle.md) — **Simplify**. **Owner:** economy policy (giữ).

**Phản biện:** Learn→earn→buy không phù hợp mọi persona; recognition không phải điều kiện quay lại.

**Sửa scope/schema/API:** Giữ tùy chọn, đo tác động lên delayed recall; không hành động mua để unlock core.

**Dữ liệu / an toàn / hiệu năng:** Không notification pressure; cap reward stacking; không mutate learning qua wallet.

**V1:** Không reward dependency. **V2:** Earned identity thử nhỏ. **V3:** Tối ưu nếu outcome không giảm.

**Mục liên quan:** [043](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/043_reward_system.md), [076](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md).

## 099 — Event Retention Principle

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/099_event_retention_principle.md) — **Postpone**. **Owner:** liveops policy (giữ).

**Phản biện:** Async/replay “khi hợp lý” chưa bảo đảm learner không mất tiến độ thiết yếu.

**Sửa scope/schema/API:** Core content/review luôn truy cập; event chỉ presentation/challenge thêm; reward eligibility rõ.

**Dữ liệu / an toàn / hiệu năng:** Expiry không xoá mastery; time zone fairness và opt-in reminder.

**V1:** Không event loop. **V2:** Async trial. **V3:** Live event có điều kiện.

**Mục liên quan:** [061](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/061_scheduled_events.md), [076](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/076_reward_economy_anti_patterns_to_avoid.md).

## 100 — Final Design Thesis

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/100_final_design_thesis.md) — **Keep**. **Owner:** product (giữ).

**Phản biện:** Tầm nhìn tám kiểu người dùng không phải acceptance checklist launch.

**Sửa scope/schema/API:** Đổi thesis thành staged strategy và lựa chọn cohort; không schema riêng.

**Dữ liệu / an toàn / hiệu năng:** Không chứng minh giá trị bằng số feature; học độc lập là gate.

**V1:** Solo value rõ. **V2:** Một–hai nhánh mở rộng. **V3:** Nhiều persona khi đủ capacity.

**Mục liên quan:** [004](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/004_target_user_personas.md), [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md).

## 101 — Product Philosophy Statements to Preserve

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/101_product_philosophy_statements_to_preserve.md) — **Simplify**. **Owner:** product (giữ).

**Phản biện:** Giữ philosophy nhưng “class must have shared progression” quá mạnh cho pilot.

**Sửa scope/schema/API:** Phân loại invariant (learning/privacy) và hypothesis (class progression/retention); mỗi câu có test/gate.

**Dữ liệu / an toàn / hiệu năng:** Không nhân PR checklist 106 lần; owner quyết exceptions có ADR.

**V1:** 5–7 invariant chung. **V2:** Bổ sung bằng evidence. **V3:** Loại câu không còn đúng.

**Mục liên quan:** [003](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/003_core_product_principles.md), [018](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/018_class_progression.md), [096](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/096_social_retention_principle.md).

## 102 — Open Questions for Claude Review

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/102_open_questions_for_claude_review.md) — **Keep**. **Owner:** review (giữ non-runtime).

**Phản biện:** 45 câu hỏi cần quyết định cụ thể; không coi câu hỏi là yêu cầu xây feature.

**Sửa scope/schema/API:** Trả lời 45 câu trong 04_OPEN_QUESTIONS; owner/phase gắn roadmap, unknown ghi rõ.

**Dữ liệu / an toàn / hiệu năng:** Không runtime schema/API; không giả số đã benchmark hoặc đo retention.

**V1:** Chốt defaults có thể đảo. **V2:** Đánh giá pilot. **V3:** Đánh giá scale.

**Mục liên quan:** [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md), [103](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/103_suggested_review_output_from_claude.md).

## 103 — Suggested Review Output From Claude

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/103_suggested_review_output_from_claude.md) — **Keep**. **Owner:** review (giữ non-runtime).

**Phản biện:** Output yêu cầu đầy đủ, nhưng dài không thay tính truy vết/khả thi.

**Sửa scope/schema/API:** Cung cấp 106 quyết định, finding register, contracts, phases và DAG kiểm tra được.

**Dữ liệu / an toàn / hiệu năng:** Không tuyên bố implementation pass chỉ vì docs đủ; archive hash giữ source.

**V1:** Bộ review này. **V2:** Update decision log. **V3:** ADR tiếp theo.

**Mục liên quan:** [102](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/102_open_questions_for_claude_review.md), [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md).

## 104 — Current Direction to Treat as Most Important

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/104_current_direction_to_treat_as_most_important.md) — **Simplify**. **Owner:** product (giữ).

**Phản biện:** Dòng “Ưu tiên hiện tại” class/social+identity/reward che mất prerequisite learning/content.

**Sửa scope/schema/API:** Ưu tiên: content/evidence/ops/mobile trước; brand prototype song song; class/economy qua gate.

**Dữ liệu / an toàn / hiệu năng:** Không đồng nhất ưu tiên chiến lược với dependency build; migration có trust tiers.

**V1:** Core trước meta. **V2:** Class + identity nhỏ. **V3:** Prestige/events khi đủ tin cậy.

**Mục liên quan:** [083](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/083_recommended_build_order.md), [070](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/070_content_learning_data_foundation.md), [097](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md).

## 105 — Closing Vision

[Source](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/105_closing_vision.md) — **Keep**. **Owner:** product (giữ).

**Phản biện:** Vision tốt nhưng ham muốn limited frame chưa chứng minh học tốt hơn.

**Sửa scope/schema/API:** Success là bằng chứng nhớ/vận dụng, voluntary return, trust và performance; numbers là giả thuyết trước pilot.

**Dữ liệu / an toàn / hiệu năng:** Không tối ưu time-spent hay vanity unlock; không hứa outcome chưa đo.

**V1:** Chứng minh loop học. **V2:** Chứng minh lợi ích cộng đồng. **V3:** Mở rộng có kiểm soát.

**Mục liên quan:** [097](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/097_learning_retention_principle.md), [096](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/096_social_retention_principle.md), [098](source/space_academy_detailed_plans_reviewed_v2_2026-10-09/098_reward_retention_principle.md).
