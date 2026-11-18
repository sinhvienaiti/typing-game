# Economy authority, persistence and checks

## Source map

| Concern | Source | Regression anchors |
| --- | --- | --- |
| Currency/pricing | [Credits](../../../../games/space-typing/src/economy/credits.ts), [currencies](../../../../games/space-typing/src/economy/currencies.ts), [wallet rules](../../../../games/space-typing/src/economy/wallet-rules.ts), [prices](../../../../games/space-typing/src/economy/wallet-price.ts) | [Rules](../../../../games/space-typing/tests/wallet-rules.test.ts), [prices](../../../../games/space-typing/tests/wallet-price.test.ts) |
| Warp | [Policy](../../../../games/space-typing/src/economy/warp-charge.ts), [transactions](../../../../games/space-typing/src/persistence/account-transactions.ts), [account state](../../../../games/space-typing/src/persistence/account-state.ts) | [Arithmetic](../../../../games/space-typing/tests/warp-charge.test.ts), [transactions](../../../../games/space-typing/tests/account-transactions.test.ts), [controls](../../../../games/space-typing/tests/warp-controls.test.ts) |
| Online authority/offline gates | [WalletSync](../../../../games/space-typing/src/online/wallet-sync.ts), [cloud wallet](../../../../games/space-typing/cloud/src/wallet.ts), [main integration](../../../../games/space-typing/src/main.ts) | [Sync](../../../../games/space-typing/tests/wallet-sync.test.ts), [cloud transactions](../../../../games/space-typing/tests/cloud-wallet-transactions.test.mjs) |
| Progression/unlocks | [Meta](../../../../games/space-typing/src/progression/meta.ts), [missions](../../../../games/space-typing/src/progression/missions.ts), [characters](../../../../games/space-typing/src/characters/progression.ts), [skills](../../../../games/space-typing/src/skills/progression.ts), [upgrades](../../../../games/space-typing/src/progression/upgrades.ts) | [Meta](../../../../games/space-typing/tests/meta-progression.test.ts), [characters](../../../../games/space-typing/tests/character-progression.test.ts) |
| Shops/stock | [Policy](../../../../games/space-typing/src/shops/policy.ts), [state](../../../../games/space-typing/src/shops/state.ts), [service shop](../../../../games/space-typing/src/shops/service-shop.ts), [admin runtime](../../../../games/space-typing/src/admin/shop-runtime-policy.ts) | [State](../../../../games/space-typing/tests/shop-state.test.ts), [parity](../../../../games/space-typing/tests/shop-policy-parity.test.ts), [revision lifecycle](../../../../games/space-typing/tests/shop-revision-lifecycle.test.ts) |
| Save/migration/rollback | [PlayerSave](../../../../games/space-typing/src/persistence/player-save.ts), [backup](../../../../games/space-typing/src/persistence/backup.ts), [checkpoint](../../../../games/space-typing/src/persistence/checkpoint.ts), [crash recovery](../../../../games/space-typing/src/persistence/crash-recovery.ts) | [Persistence](../../../../games/space-typing/tests/persistence.test.ts), [backup](../../../../games/space-typing/tests/backup.test.ts), [checkpoint](../../../../games/space-typing/tests/checkpoint.test.ts) |
| Rewards/balance | [Credit drops](../../../../games/space-typing/src/rewards/combat-credit-drops.ts), [Warp audit](../../../../games/space-typing/src/balance/warp-economy-audit.ts) | [Rewards](../../../../games/space-typing/tests/campaign-rewards.test.ts), [credit sampling](../../../../games/space-typing/tests/combat-credit-economy-sampling.test.ts), [Warp audit](../../../../games/space-typing/tests/warp-economy-audit.test.ts) |

## Current behavior versus history

[Warp status](../../../../games/space-typing/docs/WARP_CHARGE_IMPLEMENTATION_STATUS.md) describes local safeguards/manual gaps. [Server wallet design/status](../../../../games/space-typing/docs/ONLINE_SERVER_WALLET_DESIGN_2026-10-16.md) records later online phases; opening design prose is historical. Inspect current WalletSync, server policy and session phase to decide authority.

Local persistence has strict transactions, payload-bound receipts, writer/generation fences and bounded history. Online phase 1 shadows; later phases can make server balances/Warp authoritative, require pay-first purchases and prohibit paid offline actions on enrolled devices. UI balances cannot authorize spending.

Currencies include Credits plus Alloy, Star Crystal and Quantum Core. Equipment grade differs from drop probability. [M05 migration](../../../../games/space-typing/docs/M05_GRADE_CURRENCY_MIGRATION.md) is historical context; read `PLAYER_SAVE_VERSION` in source rather than copying its old schema version. Encounter Energy powers abilities; Warp funds deployment.

## Warp contracts to check against current source

Current `warp-v3-1`: Active cap 100 (one per 6 min), Reserve cap 300 (one per 12 min only after Active full), cost 10 per paid deployment. Reserve requires consent. Refuel adds 20 for 8/12/18 Star Crystals, at most three per game day resetting 04:00 UTC+7. Current constants remain authoritative when policy changes.

Prepare assets/input/context before charging. Exact prepared continuation pays once; abandoned/active/crashed attempts follow their recorded state. Quote and persisted mutation must agree. Use bounded regeneration arithmetic; backward clocks cannot mint fuel.

Practice/Smart Review are learning-only overlays. Keep simulated rewards out of Campaign. Expedition/Duel have separate progression and currently zero Warp. Check resurrection, checkpoint and stage-clear settlement before changing reward timing.

For schema changes, provide migration/fixtures, strict current/future validation, backup/import behavior, defaults only for genuinely older saves, and auxiliary-profile/receipt compatibility. Protect canonical accounts from repeat migration grants, stale autosave and rollback through legacy imports. Mutations and receipts commit together; failures cannot grant items or hide unresolved settlement.

## Verification

From platform root:

```sh
pnpm --dir games/space-typing exec vitest run tests/warp-charge.test.ts tests/account-transactions.test.ts tests/wallet-sync.test.ts tests/wallet-price.test.ts tests/persistence.test.ts tests/backup.test.ts
pnpm --dir games/space-typing stamina:audit
```

Select relevant suites. [Game scripts](../../../../games/space-typing/package.json) define audits; inspect the supported Node invocation for cloud `.mjs` tests instead of placing them in Vitest. Formula bounds are not measured human pacing.

Browser checks: duplicate deployment/refuel/purchase; funds; daily reset; prepared resume; quit/defeat/crash; Phoenix; clear/reload; Practice exit; concurrent tabs/writer takeover; offline enrolled wallet; failed/lost response; restore/new generation. Distinguish automated transaction coverage from browser storage/account acceptance.
