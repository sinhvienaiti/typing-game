# 102. Open Questions for Claude Review

**Nguồn gốc:** `SPACE_ACADEMY_PRODUCT_VISION_AND_SYSTEM_IDEAS_REVIEW_DRAFT_2026-10-09.md`  
**Loại:** Concept / policy / UX guidance  
**Primary owner/domain:** `review`  
**Secondary integrations:** không có  
**Review status:** Self-reviewed V2 — domain ownership corrected; vẫn là draft cần Claude/architecture review trước implementation.

---

## 1. Mục tiêu

Tài liệu review không phải runtime feature; mục tiêu là buộc reviewer phản biện scope, kiến trúc, UX, performance và learning quality.

### Điều phải giữ riêng cho mục này

- Reviewer phải trả lời bằng Keep/Simplify/Postpone/Reject, không chỉ comment chung.

---

## 2. Ý tưởng gốc đã thống nhất

The reviewer should challenge the plan rather than simply approve it.

## Product

1. Is “Space Academy” the right primary mental model?
2. Are there better organizing metaphors that preserve the same strengths?
3. Which systems are still unnecessarily complex?
4. Which systems are missing?
5. Which features should be explicitly postponed?

## Learning

6. Does the class/lesson structure support serious learning outcomes?
7. Where could gamification damage learning quality?
8. Is the IELTS approach sufficiently separated from casual gamification?
9. How should CEFR and topic tracks coexist?

## Social

10. Is the class size assumption reasonable?
11. How should real teachers, AI teachers, and self-study classes coexist?
12. How should users be matched into classes?
13. How can class social bonds form without becoming noisy or unsafe?
14. Which chat functions belong in V1?

## NPC / AI

15. What is the best technical model for contextual NPC memory?
16. How do we keep NPCs natural without pretending they are human?
17. What content/moderation boundaries are needed?
18. Which NPC roles create real user value?

## Rewards / Economy

19. Are Credits + Crystals + contextual tokens enough?
20. What should the earning/spending ratios look like?
21. How can inflation be prevented?
22. Which reward systems should be V1 vs later?
23. How do we prevent grinding from replacing learning?

## Prestige

24. Which rankings are meaningful and fair?
25. How should verified competitive results work?
26. What prestige items should be permanently exclusive?
27. How should Hall of Fame/history be designed?

## Avatar / Cosmetics

28. Is layered 2D the right long-term choice?
29. Should the implementation use DOM/CSS, Canvas, PixiJS, Rive, Spine, or another renderer?
30. How should outfit masking/layer standards work?
31. What asset resolution/file size budgets should be enforced?
32. How can artists efficiently create hundreds of compatible items?

## Audio / Visual

33. What should the core art direction be?
34. How do we make it feel premium rather than “educational website with sci-fi skin”?
35. What audio identity is distinctive enough to be memorable?
36. What effects should be intentionally restrained?

## Architecture / Performance

37. Which modules should be separately lazy-loaded?
38. Which data should be real-time?
39. Which social features require WebSocket infrastructure?
40. What initial performance budgets should be locked?
41. What should mobile degrade gracefully?

## Admin

42. Which admin functions are essential to avoid hard-coded LiveOps?
43. How should Lesson Builder and Event Builder share components?
44. How should reward/economy simulation be implemented?
45. What audit/versioning is needed for class/reward/event configuration?

---

---

## 3. Phạm vi V1 đề xuất

### Core

- Chỉ triển khai behavior trực tiếp phục vụ mục tiêu của mục này.
- Server là authority cho progress, reward, ownership, ranking hoặc permission có giá trị.
- Client tối ưu presentation, optimistic feedback và cache; không tự quyết định state giá trị cao.
- Data/config có lifecycle thì dùng version rõ ràng.
- Có empty/loading/error/retry state.

### Không đưa vào V1 nếu chưa có bằng chứng

- Realtime chỉ để “trông hiện đại”.
- Animation/VFX phức tạp không giúp comprehension/identity.
- Schema riêng cho state có thể derive an toàn.
- Integration chéo bằng cách query thẳng bảng của module khác.
- Feature phụ chỉ vì game online khác có.

---

## 4. User flow

```text
DISCOVER
  ↓
UNDERSTAND
  ↓
ACT
  ↓
FEEDBACK
  ↓
CONTINUE / RETURN
```

1. **Discover:** user hiểu feature là gì mà không đọc tutorial dài.
2. **Understand:** rule, cost, reward hoặc learning objective minh bạch.
3. **Act:** primary action ít bước.
4. **Feedback:** kết quả rõ, pending/failed/retry nếu async.
5. **Continue:** CTA hợp logic hoặc kết thúc sạch, không ép sang Shop/Event.

---

## 5. UI/UX

- Không áp dụng UI runtime.

### UX guardrails chung

- Một primary CTA/màn hình.
- Không dùng badge đỏ/chấm than khắp UI.
- Secondary/meta systems không chiếm visual weight hơn learning task.
- Mobile thiết kế theo mật độ riêng, không chỉ scale desktop.
- Keyboard/focus/contrast/reduced-motion được tính ngay từ đầu.
- Error message phải chỉ cách phục hồi.

---

## 6. Hình ảnh / Art

- Không áp dụng asset runtime.

### Asset rules

- Mỗi asset có ID, version/hash, provenance/owner khi cần.
- List dùng thumbnail; full asset chỉ tải khi thực sự cần.
- Template/safe area/crop/alpha/naming được chuẩn hóa.
- Không hard-code file path vào business rules.

---

## 7. Âm thanh

- Không áp dụng audio runtime.

### Audio guardrails

- Voice/pronunciation > music > cosmetic SFX về priority.
- Có mute/volume theo group khi domain có audio.
- Notification cue có cooldown.
- Không autoplay audio dài chỉ vì mở screen.
- Mobile autoplay restriction phải có user gesture fallback.

---

## 8. Motion / VFX

- Animation mặc định dùng transform/opacity khi đủ.
- Reduced-motion có fallback tĩnh.
- Effect hiếm mới fullscreen.
- Dừng effect off-screen/hidden tab.
- Quality tier giảm blur/shadow/particles trên thiết bị yếu.
- Motion phải giải thích state hoặc tạo cảm xúc có chủ đích; nếu chỉ trang trí và tốn GPU thì bỏ.

---

## 9. Database / Data ownership

- Không tạo schema/database riêng chỉ vì tài liệu này là một principle/example.
- Nếu cần runtime state, reuse domain owner: `review` hoặc subsystem được nêu trong Dependencies.
- Tránh duplicate source of truth chỉ để phục vụ một view/example.

### Data rules

- PostgreSQL là transactional source of truth.
- Redis chỉ cache/realtime/ranking khi có use case rõ.
- Media nằm object storage/CDN.
- Mutation có thể retry phải idempotent.
- JSONB cho config mở rộng; field query thường xuyên nên thành column/index.
- Historical result đã finalize không sửa tùy tiện.
- Mọi timestamp business quan trọng dùng server time; timezone chỉ dùng để resolve user-facing calendar/day boundary.

---

## 10. API / Domain events

- Tài liệu này không cần tạo event riêng; dùng event của subsystem owner.

### Contract rules

- Không query DB cross-module trực tiếp nếu có thể dùng service/domain contract.
- Mutation validate authorization + eligibility phía server.
- Cursor pagination cho collection lớn.
- API list trả summary DTO, không full aggregate.
- Event payload có stable IDs + schema version.

---

## 11. Tích hợp với subsystem khác

- Không có integration bắt buộc ngoài platform contracts chung.

**Nguyên tắc:** secondary integration không đồng nghĩa nhập toàn bộ UI/DB của domain đó vào file này. Đây là lỗi đã được sửa so với bản generated đầu tiên.

---

## 12. Admin / Configuration

- Chỉ config những gì operator/teacher thật sự cần thay đổi thường xuyên.
- Live config: `draft → preview → publish`.
- Có audit actor/time/reason.
- Economy/prestige/reward config cần permission cao hơn.
- Không để admin sửa thẳng historical result đã finalized.
- Config có thời hạn phải có start/end/timezone policy rõ.

---

## 13. Performance

- Không áp dụng performance runtime; reviewer phải kiểm tra budgets trong các file subsystem.

### Budget guardrails

- Feature không thuộc Home critical path thì code-split/lazy-load.
- Không giữ realtime subscription khi user rời context.
- List media responsive theo viewport.
- Tránh long task do animation/large JSON.
- Đo trên thiết bị yếu đại diện, không chỉ máy dev.
- Theo dõi p95 API, asset failure, interaction latency, memory growth.

---

## 14. Security / Abuse / Safety

- Không tin client score/time/balance/eligibility.
- Rate limit các action spam-able.
- Reward/purchase/prestige cần audit/idempotency khi phù hợp.
- Social feature phải có moderation primitives tương ứng.
- PII tối thiểu.
- AI/NPC không giả làm người thật.
- Nếu target minors, cần privacy/safety review riêng trước launch.

---

## 15. Analytics / KPI

Không tối ưu chỉ theo **time spent**.

Đo tối thiểu:

- Primary-action completion
- Return rate theo persona
- Abandon/error rate
- Time-to-primary-action
- Feature load time
- Learning outcome/mistake reduction nếu liên quan học
- Healthy engagement: opt-out/mute/notification-dismiss khi liên quan social/reward
- Economy source/sink hoặc rank integrity nếu thuộc domain đó

---

## 16. Testing / Acceptance

### Functional

- Happy path.
- Empty/loading/error/retry.
- Refresh/reconnect.
- Concurrent/double-click.
- Mobile/touch.
- Keyboard/accessibility.
- Reduced-motion/mute.
- Permission/eligibility.
- Version compatibility.

### Data

- Không duplicate grant/progress khi retry.
- Migration forward/rollback plan.
- Index query chính được kiểm tra.
- Audit trail cho state giá trị cao.

### Performance

- Route chunk/media không vượt budget đã khóa.
- Không memory leak sau nhiều navigation.
- Network slow/offline có graceful behavior khi hợp lý.

---

## 17. Rollout

### A. Prototype
Validate UX/art/content bằng fixture, chưa xây backend quá sâu.

### B. Foundation
Schema/API tối thiểu + analytics + basic admin.

### C. Production V1
Real data + mobile + error/retry + performance budget.

### D. Enrichment
Chỉ thêm live/social/VFX/cosmetic depth khi core metrics chứng minh có giá trị.

---

## 18. Claude review checklist

Claude nên đánh dấu **Keep / Simplify / Postpone / Reject** và trả lời:

1. Scope này có quá lớn không?
2. Primary owner/domain đã đúng chưa?
3. Có duplicate source of truth không?
4. DB có over-normalized hoặc quá generic không?
5. UI có đủ đơn giản với casual learner không?
6. Visual/audio có lấn learning không?
7. Performance web/mobile có hợp lý không?
8. Có FOMO/dark pattern/cheat vector không?
9. V1 có thể cắt thêm gì?
10. Dependency nào nên chuyển sang event/contract?

---

## 19. Definition of Done

Chỉ coi là hoàn thành khi:

- Functional + integration tests pass.
- Analytics hoạt động.
- Mobile/accessibility smoke pass.
- Performance budget pass.
- Data ownership và idempotency rõ.
- Admin/config path được test nếu có.
- Không còn hidden dependency vào module khác.
- Documentation/ADR cập nhật.

---

## 20. Kết luận

`Open Questions for Claude Review` phải phục vụ trực tiếp cho **review**. Các hệ liên quan chỉ tích hợp qua contract, không được khiến file này trở thành một “siêu module” ôm class + reward + avatar + event + typing cùng lúc.

Đây là nguyên tắc quan trọng để giữ sản phẩm **đẹp, dễ hiểu, hiệu năng tốt và có thể mở rộng lâu dài**.
