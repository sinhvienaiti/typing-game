---
name: progression-economy
description: Implement or review Space Typing progression, unlocks, currencies, rewards, shop pricing and Warp stamina; use for spending, regeneration, settlement, persistence or economy balance changes.
---

Read [economy and persistence contracts](references/economy-contracts.md). Determine local transactions, server wallet shadowing or authoritative online phase; older local-only design does not describe every current session.

1. Trace domain calculation through validation, transaction/receipt, persistence, runtime adoption and UI. Keep pricing, rewards and regeneration outside UI-only handlers.
2. Preserve currency identities, one-time rewards, stock, quotes and idempotent operation IDs. Charge deployment once after preparation; retries/reconnect cannot charge or reward twice.
3. Check schema version, migration, strict current/future validation, backup restore and generation fences for persisted changes. Preserve data and one authority per account path.
4. Keep Practice/Review/QA overlays and Expedition/Duel economy boundaries. Distinguish encounter Energy from Warp stamina and Credits from expansion currencies.
5. Use production formulas/audits for balance. Verify funds, caps/reset, concurrent tabs, failed storage, lost ACK and offline/online phases before claiming correctness.

Use `admin-runtime-authoring` for prices/unlocks, `space-typing-gameplay` for reward triggers and `space-typing-playtest` for visible purchase/deployment flows. Skill installation itself requires no balance/save changes.
