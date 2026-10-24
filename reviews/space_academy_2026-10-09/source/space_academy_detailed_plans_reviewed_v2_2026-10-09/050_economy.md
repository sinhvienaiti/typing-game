# 50. Economy

**Nguồn gốc:** `SPACE_ACADEMY_PRODUCT_VISION_AND_SYSTEM_IDEAS_REVIEW_DRAFT_2026-10-09.md`  
**Loại:** Subsystem detailed design  
**Primary owner/domain:** `economy`  
**Secondary integrations:** platform  
**Review status:** Self-reviewed V2 — domain ownership corrected; vẫn là draft cần Claude/architecture review trước implementation.

---

## 1. Mục tiêu

Tạo reward/economy dễ hiểu, audit được, chống double grant và không khuyến khích grind vô nghĩa.

### Điều phải giữ riêng cho mục này

- Giữ public-facing currency ít; contextual resource chỉ hiển thị trong feature.
- Ledger double-entry-ish/auditable là bắt buộc.

---

## 2. Ý tưởng gốc đã thống nhất

The economy should remain understandable.

A simple public-facing currency model is preferred.

## Credits

Common currency.

Earned from:

- Learning
- Practice
- Class activities
- Games
- Events

Used for:

- Avatar cosmetics
- Frames
- Backgrounds
- Stationery skins
- Themes
- Small customization

## Crystals

Rarer.

Earned from:

- Higher mastery
- Weekly milestones
- Events
- Achievements
- Limited activities

Used for:

- Rare cosmetics
- Premium-looking themes
- Limited visuals

## Event Token

Appears only when an event is active.

## Context-specific resources

Class resources, crafting-like fragments, etc. should appear only inside the relevant system instead of cluttering the main UI.

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

- Chỉ hiển thị ít currency chính.
- Reward nhỏ gom Reward Center; rare reward mới ceremony.
- Shop minh bạch giá, owned-state, thời gian và exclusivity.

### UX guardrails chung

- Một primary CTA/màn hình.
- Không dùng badge đỏ/chấm than khắp UI.
- Secondary/meta systems không chiếm visual weight hơn learning task.
- Mobile thiết kế theo mật độ riêng, không chỉ scale desktop.
- Keyboard/focus/contrast/reduced-motion được tính ngay từ đầu.
- Error message phải chỉ cách phục hồi.

---

## 6. Hình ảnh / Art

- Item/rarity presentation nhất quán; prestige không dùng cùng visual với đồ mua thường.

### Asset rules

- Mỗi asset có ID, version/hash, provenance/owner khi cần.
- List dùng thumbnail; full asset chỉ tải khi thực sự cần.
- Template/safe area/crop/alpha/naming được chuẩn hóa.
- Không hard-code file path vào business rules.

---

## 7. Âm thanh

- Claim/buy cue ngắn theo rarity; không spam với micro-credit.

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

- `currencies`, `wallets`, `wallet_ledger`, `items`, `item_variants`, `item_ownership`, `shops`, `shop_slots`, `shop_rotations`, `reward_definitions`, `reward_grants`, `purchase_orders`.

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

- `reward.granted`
- `wallet.changed`
- `purchase.completed`
- `item.acquired`

### Contract rules

- Không query DB cross-module trực tiếp nếu có thể dùng service/domain contract.
- Mutation validate authorization + eligibility phía server.
- Cursor pagination cho collection lớn.
- API list trả summary DTO, không full aggregate.
- Event payload có stable IDs + schema version.

---

## 11. Tích hợp với subsystem khác

- **platform**: tích hợp qua events/contracts; không copy schema/UI của domain này vào module `economy`.

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

- Ledger PostgreSQL là source of truth; balance có thể cache.
- Catalog CDN + pagination; không tải toàn shop.
- Grant/purchase idempotent.

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

`Economy` phải phục vụ trực tiếp cho **economy**. Các hệ liên quan chỉ tích hợp qua contract, không được khiến file này trở thành một “siêu module” ôm class + reward + avatar + event + typing cùng lúc.

Đây là nguyên tắc quan trọng để giữ sản phẩm **đẹp, dễ hiểu, hiệu năng tốt và có thể mở rộng lâu dài**.
