# 3. Core Product Principles

**Nguồn gốc:** `SPACE_ACADEMY_PRODUCT_VISION_AND_SYSTEM_IDEAS_REVIEW_DRAFT_2026-10-09.md`  
**Loại:** Concept / policy / UX guidance  
**Primary owner/domain:** `product`  
**Secondary integrations:** không có  
**Review status:** Self-reviewed V2 — domain ownership corrected; vẫn là draft cần Claude/architecture review trước implementation.

---

## 1. Mục tiêu

Giữ kiến trúc sản phẩm nhất quán, đơn giản ở bề mặt nhưng đủ chiều sâu cho nhiều persona.

### Điều phải giữ riêng cho mục này

- Khóa nguyên tắc progressive disclosure, focus-first và anti-dark-pattern thành design review checklist.

---

## 2. Ý tưởng gốc đã thống nhất

## 3.1 Depth without complexity at the surface

The product can eventually contain many systems, but users should not see all of them at once.

A beginner should be able to use:

```text
Learn
Practice
Play
Profile
```

without understanding prestige systems, seasonal events, collectibles, advanced rankings, class resources, special shops, etc.

Advanced systems should appear only when relevant.

## 3.2 Progressive disclosure

Examples:

- IELTS appears when the user chooses IELTS as a goal.
- Classroom systems appear after joining a class.
- Social systems expand after users add friends.
- Events become more visible after the learner has basic familiarity.
- Competitive systems become more visible to users who show interest in them.

The interface should **grow with the user** instead of forcing the user to learn the entire product on day one.

## 3.3 Learning must remain readable and calm

The product should have a strong sci-fi / academy identity, but content surfaces must remain comfortable.

Rule:

> **Science-fiction identity at the shell; clarity at the content surface.**

Examples:

- Reading screen → almost like a high-quality e-book.
- Typing screen → minimal and focused.
- IELTS exam → serious and distraction-free.
- Reward, profile, event, class, shop → richer visual personality.

## 3.4 Every feature must earn its visual weight

The most important current action should dominate.

```text
Current learning task     Priority 1
Primary action            Priority 1
Progress                  Priority 2
Rewards                   Priority 3
Social                    Priority 3
Events                    Priority 4 unless active
Shop promotion            Priority 5
```

The shop must never visually overpower the learning task.

## 3.5 Gamification must not become manipulation

Avoid:

- Punishing users for missing a day
- Destroying long streaks after one missed session
- Excessive popups
- Fake scarcity
- Fake player activity
- Rewarding AFK
- Making users feel they must schedule their life around the platform
- Selling status that should represent genuine achievement

Prefer:

- Positive reinforcement
- Optional live bonuses
- Async/replay alternatives
- Clear scarcity rules
- Honest AI/NPC labeling
- Persistent knowledge progression

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

- Mỗi surface có một primary action.
- Progressive disclosure theo persona và maturity.
- Không để game meta lấn learning task.

### UX guardrails chung

- Một primary CTA/màn hình.
- Không dùng badge đỏ/chấm than khắp UI.
- Secondary/meta systems không chiếm visual weight hơn learning task.
- Mobile thiết kế theo mật độ riêng, không chỉ scale desktop.
- Keyboard/focus/contrast/reduced-motion được tính ngay từ đầu.
- Error message phải chỉ cách phục hồi.

---

## 6. Hình ảnh / Art

- Brand nằm ở shell, typography, character, icon và motion language; content surface ưu tiên đọc dễ.

### Asset rules

- Mỗi asset có ID, version/hash, provenance/owner khi cần.
- List dùng thumbnail; full asset chỉ tải khi thực sự cần.
- Template/safe area/crop/alpha/naming được chuẩn hóa.
- Không hard-code file path vào business rules.

---

## 7. Âm thanh

- Chỉ dùng sonic identity ở transition/milestone; không biến navigation thành chuỗi SFX.

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
- Nếu cần runtime state, reuse domain owner: `product` hoặc subsystem được nêu trong Dependencies.
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

- Core shell nhẹ, module nặng route-level lazy-load.
- Không mở realtime/media channel khi feature chưa được dùng.

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

`Core Product Principles` phải phục vụ trực tiếp cho **product**. Các hệ liên quan chỉ tích hợp qua contract, không được khiến file này trở thành một “siêu module” ôm class + reward + avatar + event + typing cùng lúc.

Đây là nguyên tắc quan trọng để giữ sản phẩm **đẹp, dễ hiểu, hiệu năng tốt và có thể mở rộng lâu dài**.
