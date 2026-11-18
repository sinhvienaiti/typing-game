# Space Typing Admin V2 — Shop Architecture Decision

> Phase: **A4.0 — Shop Architecture Decision**
>
> Status: architecture gate before any A4.1 Shop write UI.
>
> Parent: `sinhvienaiti/typing-game` · `feat/space-typing-admin-uiux`
>
> Audited child source of truth: `sinhvienaiti/space-typing` pinned at `83f80b3d6f640ea1af46e158e25485bc57b31393`.

---

## 1. Executive decision

Space Typing Shop must become administrator-editable **without turning generated player Shop instances into an Admin database**.

The current runtime is policy-driven and deterministic:

- Shop availability depends on Shop type, stage/sector, luck, progression and hidden discovery;
- stock is generated from item/equipment registries and Shop-specific pools;
- equipment grade is rolled from Shop-type/stage rules;
- prices are derived from grade, equipment tier, Shop type and multiple currencies;
- generated `ShopInstance` objects are persisted inside `PlayerSave.shopState`;
- purchase logic consumes the **price already stored on that ShopInstance**;
- Service Shop costs are a separate economy family.

Therefore the canonical V2 owner will be a **published Shop policy**. Admin edits the policy that produces future Shop offers; it does **not** directly edit a player's generated Shop instance, inventory, balance or save.

The required runtime pipeline is:

```text
Admin Shop Editor
  -> immutable parent Admin revision (`economy.shop`)
  -> strict parent + child validation
  -> child preview using the production Shop policy engine
  -> CAS Publish
  -> public runtime Shop policy envelope
  -> child immutable Shop runtime session
  -> production Shop generator/pricing/availability/service resolvers
  -> newly generated ShopInstance in PlayerSave
```

There must be **one Shop generator/pricing engine** shared by production and preview. A second Admin-only generator is forbidden.

---

## 2. Audited current runtime ownership

### 2.1 `src/shops/state.ts`

Current canonical responsibilities:

- `SHOP_TYPES`:
  - `normal`
  - `station`
  - `traveling`
  - `black-market`
  - `hidden`
  - `event`
  - `service`
- four-currency `ShopPrice`:
  - Credits
  - Alloy
  - Star Crystal
  - Quantum Core
- deterministic `shopInstanceSeed()` / `shopInstanceId()`;
- stock generation;
- item/equipment pool selection;
- grade roll;
- item/equipment pricing;
- equipment tier pricing;
- resurrection-item chance;
- availability rules;
- Shop-state sanitization/backward compatibility;
- purchase affordability and stock decrement.

Important persistence fact:

```text
ShopState.version = 1
ShopState.instances[id] = ShopInstance
ShopInstance.stock[*].price = resolved purchase price
```

A Shop price is therefore snapshotted when a Shop instance is generated. `buyShopStockEntry()` charges the persisted entry price; it does not recalculate from current code on every purchase.

### 2.2 Item registry ownership

`src/items/registry.ts` owns:

- item ID;
- name;
- category;
- max stack;
- combat usability;
- icon glyph;
- description;
- grade.

Shop must reference `itemId`; it must not duplicate these fields as a shadow product record.

### 2.3 Equipment registry ownership

`src/equipment/registry.ts` owns:

- equipment ID;
- name;
- slot;
- tier;
- icon glyph;
- description;
- stats;
- perk.

Shop must reference `definitionId`; it must not duplicate Equipment identity/stats/perks.

### 2.4 Service Shop ownership

`src/shops/service-shop.ts` currently owns a separate cost system, including:

- repair pack costs;
- equipment enhancement Credits/Alloy costs;
- equipment evolution costs and required stages;
- affix add/reroll costs;
- dismantle rewards;
- skill upgrade costs;
- attribute upgrade costs;
- other service actions built on progression/equipment state.

Service Shop economics are related to Shop management but are **not ordinary generated stock entries** and must remain a separate sub-policy.

### 2.5 Existing Admin capability

Current parent Shop capability is deliberately `runtime-backed-readonly`.

It correctly exposes runtime evidence but has no safe authoring bridge. It must not be converted into a fake editor by merely enabling form controls.

---

## 3. Non-negotiable ownership rules

### R1 — Do not store generated Shop instances in Admin

Forbidden:

```text
Admin revision -> list of player ShopInstance rows
```

Allowed:

```text
Admin revision -> Shop generation/pricing/availability/service policy
PlayerSave -> concrete generated ShopInstance
```

### R2 — Item/Equipment identity stays with its registry

Shop may control whether/where/how an existing Item/Equipment is sold.

Shop does not own:

- Item/Equipment name;
- gameplay description;
- equipment stats/perk/tier;
- generic Item/Equipment icon/media.

If those become editable, the Item/Equipment domain remains the canonical owner and Shop consumes the resolved projection.

### R3 — No Admin-only pricing logic

Preview, runtime generation and production purchase presentation must resolve prices from the same child policy engine.

### R4 — No silent rewrite of existing player Shop instances

Publishing a new policy must not rewrite or re-price an already generated/persisted Shop instance.

### R5 — No fake promotion scheduler

Static merchandising can be added only if the game runtime consumes it.

Time-window scheduling, campaign targeting, Daily/Weekly purchase counters and remote player targeting remain unavailable until real Live Ops/backend capabilities exist.

### R6 — Multi-currency price is canonical

A price is a four-component value, not a single number plus a display currency string.

### R7 — Draft/Publish semantics stay whole-revision CAS

Shop editing follows existing:

```text
Edit -> Save Draft -> Validate -> Preview -> review full change scope -> Publish
```

Publishing Shop changes still activates the complete target Admin revision. The V2 UI must preserve the A0.5 whole-revision warning.

---

## 4. Canonical config namespace

The Shop policy belongs under the economy namespace:

```text
config.economy.shop
```

This is intentionally not `content.shop`:

- Items/Equipment are content definitions;
- Shop is economy behavior over those definitions;
- the migration matrix already identifies the domain as `economy.shop`.

A0.5 change-scope classification must be extended so `economy.shop.*` reports as `economy.shop`, not merely `economy`.

Legacy local revisions without `economy` remain readable. Once `economy.shop` exists, it is strictly validated.

---

## 5. Shop policy model

The first canonical schema is `ShopAdminPolicyV1`.

Conceptual shape:

```ts
type ShopAdminPolicyV1 = {
  schemaVersion: 1;
  configRevision: string;
  generation: ShopGenerationPolicy;
  pricing: ShopPricingPolicy;
  availability: ShopAvailabilityPolicy;
  offers?: ShopOfferOverrides;
  services: ServiceShopPolicy;
};
```

The schema stores policy, not generated stock.

### 5.1 `generation`

`generation` owns the inputs currently embedded in `generateStock()` and `equipmentGradeForShop()`.

Required model:

```ts
type ShopTypeGenerationRule = {
  itemCount: number;
  equipmentCount: number;
  itemStock: number;
  allowedEquipmentTiers: readonly (1 | 2 | 3)[];
  itemPool: readonly ItemId[];
  equipmentPool?: readonly EquipmentId[]; // optional explicit restriction
};

type EquipmentGradeBand = {
  minStage: number;
  weights: Partial<Record<GradeId, number>>;
};
```

Grade bands use one deterministic random roll and normalized weights.

The bundled default must reproduce current semantics, for example hidden Shop stages conceptually resolve to:

```text
< 120     -> Copper 100%
120-349   -> Silver 100%
350-699   -> Silver 60%, Gold 40%
>= 700    -> Silver 60%, Gold 34%, Diamond 6%
```

Equivalent bands must be encoded for every Shop type.

This makes the rule administrator-readable without preserving brittle `if (roll > 0.94)` source logic in the Admin UI.

### 5.2 resurrection / rare-product rules

The current Phoenix Core chance belongs to generation policy, not the Item registry.

Canonical form:

```ts
type RareItemChanceRule = {
  itemId: ItemId;
  shopTypes: readonly ShopType[];
  baseChanceByShopType: Partial<Record<ShopType, number>>;
  luckMultiplierPerPoint: number;
  maxMultiplier: number;
};
```

The bundled policy must reproduce current Phoenix Core behavior.

Legacy Salvage Anchor / Stage Revival Core remain save-schema compatible but are not reintroduced into normal generation unless an explicit future product decision changes that.

### 5.3 `pricing`

Pricing must preserve current deterministic multi-currency economics while allowing administrators to change real prices.

Canonical layers:

1. default Item price by Item grade + Shop type;
2. default Equipment price by Equipment grade + Shop type;
3. Equipment tier adjustment;
4. optional exact product/Shop/grade offer override.

Conceptual shape:

```ts
type ShopPricingPolicy = {
  itemGradePrices: Record<ShopType, Record<GradeId, ShopPrice>>;
  equipmentGradePrices: Record<ShopType, Record<GradeId, ShopPrice>>;
  equipmentTierAdjustments: Record<1 | 2 | 3, EquipmentTierPriceAdjustment>;
};
```

The bundled default is derived from the existing `priceForItem()`, `priceForEquipment()` and `tierPrice()` results.

The Admin UI must not expose formula internals such as `Math.floor(base * 0.75)` as the primary workflow. Administrators edit resolved price tables/offer overrides in currency fields.

### 5.4 `offers`

`offers` is the administrator-friendly per-product override layer.

```ts
type ItemOfferOverride = {
  enabled?: boolean;
  shopTypes?: readonly ShopType[];
  stockByShopType?: Partial<Record<ShopType, number>>;
  priceByShopType?: Partial<Record<ShopType, ShopPrice>>;
  compareAtPriceByShopType?: Partial<Record<ShopType, ShopPrice>>;
  badge?: string | null;
};

type EquipmentOfferOverride = {
  enabled?: boolean;
  shopTypes?: readonly ShopType[];
  priceByShopTypeAndGrade?: Partial<
    Record<ShopType, Partial<Record<GradeId, ShopPrice>>>
  >;
  compareAtPriceByShopTypeAndGrade?: Partial<
    Record<ShopType, Partial<Record<GradeId, ShopPrice>>>
  >;
  badge?: string | null;
};

type ShopOfferOverrides = {
  items?: Partial<Record<ItemId, ItemOfferOverride>>;
  equipment?: Partial<Record<EquipmentId, EquipmentOfferOverride>>;
};
```

Why Equipment needs grade-aware override:

- the Shop sells an Equipment **definition** plus a generated Grade;
- a single Equipment ID can therefore resolve to different prices across generated Grades.

### 5.5 static discount / badge semantics

A4 may support static merchandising only when child runtime/UI consumes the fields:

- `compareAtPrice...` = optional original/compare price;
- `badge` = optional short label such as `SALE`, `LIMITED`, `BEST VALUE`.

Rules:

- actual purchase price remains the resolved `price`;
- `compareAtPrice` never changes affordability/payment;
- discount percentage is derived presentation data, not separately persisted source of truth;
- if a multi-currency vector cannot produce an unambiguous percentage, UI shows compare-at price/badge without inventing a percentage;
- a compare-at value may never be used to charge the player.

This satisfies the administrator need to manage a discount/original-price label without inventing a time scheduler.

### 5.6 deferred offer concepts

These are **not** A4.1 authorable until a real owner exists:

- start/end schedule;
- account/cohort targeting;
- Daily purchase limit;
- Weekly purchase limit;
- cross-device global purchase counters;
- bundle purchase transaction semantics;
- remote player-specific availability;
- analytics-derived recommendation/featured ranking.

Do not show enabled inputs for these concepts.

---

## 6. Availability policy

Current runtime behavior:

- Black Market requires `black-market-signal` discovery;
- Hidden and Event Shop require `echo-rift` discovery;
- Traveling Shop uses deterministic chance based on seed + luck;
- other Shop types are available by default.

Canonical shape:

```ts
type ShopAvailabilityRule =
  | { kind: "always" }
  | { kind: "discovery"; discoveryId: string }
  | {
      kind: "seeded-chance";
      baseChance: number;
      luckPerPoint: number;
      maxChance: number;
    };

type ShopAvailabilityPolicy = Record<ShopType, ShopAvailabilityRule>;
```

Discovery IDs must be validated against a child-owned allowlist/contract. Admin must not type arbitrary runtime discovery strings.

A4.1 may expose these as administrator concepts:

- Always available;
- Requires discovery X;
- Chance to appear + Luck influence.

It must not expose raw source expressions.

---

## 7. Service Shop policy

Service Shop is a sibling sub-policy inside `economy.shop`, not a fake product list.

First architecture shape:

```ts
type ServiceShopPolicy = {
  repairPack: {
    credits: number;
    alloy: number;
  };
  equipmentEnhancement: {
    gradeCreditMultiplier: Record<GradeId, number>;
    gradeAlloyBase: Record<GradeId, number>;
    creditBase: number;
    creditPerEnhancement: number;
    maxEnhancement: number;
  };
  equipmentEvolution: ServiceUpgradeCostRules;
  affixes: ServiceAffixCostRules;
  dismantle: ServiceDismantleRewardRules;
  progression: ServiceProgressionCostRules;
};
```

Important ownership boundary:

- where a cost is already canonically owned by another progression module (`skillUpgradeCost`, `attributeUpgradeCost`), Shop V2 must not silently duplicate the formula;
- either that progression module becomes policy-driven through a shared canonical economy policy, or the field remains read-only in Shop until its owner is migrated.

A4.1 must therefore distinguish:

- **Shop-owned service price** — editable;
- **external progression-owned price** — visible/reference-only until canonical ownership moves.

---

## 8. Runtime apply boundary and PlayerSave compatibility

### 8.1 Published policy session boundary

Child loads the published Shop policy once per page/game session:

```text
/api/runtime/space-typing/shop
  -> ShopRuntimeSession
```

Apply boundary:

```text
new-session + new-shop-instance
```

This is stricter than merely `new-session` because existing persisted instances already contain concrete prices/stock.

### 8.2 Existing Shop instances

When policy revision N+1 is published:

- existing `PlayerSave.shopState.instances` remain untouched;
- purchases from those instances continue using their snapshotted prices;
- a newly generated Shop instance uses policy N+1;
- no background save rewrite occurs;
- no automatic restock/reprice occurs.

This prevents:

- a displayed price changing between opening Shop and purchasing;
- save corruption;
- a Shop reroll caused solely by an Admin publish;
- a rollback unexpectedly rewriting player stock.

### 8.3 Optional trace metadata

Newly generated instances should add an optional backward-compatible field:

```ts
policyRevision?: string;
```

It is diagnostic/provenance only and must not invalidate older v1 saves that lack the field.

If adding it would force a save-schema version bump, defer the field rather than breaking compatibility.

### 8.4 Rollback

Admin rollback changes the policy exposed to **future sessions / future Shop instances**.

It does not mutate existing Shop instances created under the newer policy.

QA may offer an explicitly isolated "generate fresh preview" action. Production Admin must not add a "rewrite all player shops" button because there is no remote player backend and no safe migration owner.

---

## 9. Child runtime architecture

A4 implementation should extract policy logic rather than patching conditions throughout `state.ts`.

Recommended child modules:

```text
src/shops/policy.ts
src/admin/shop-runtime-policy.ts
src/admin/shop-policy-preview.ts
```

### 9.1 `src/shops/policy.ts`

Owns:

- `BUNDLED_SHOP_POLICY` reproducing current behavior;
- strict normalized policy types;
- product eligibility resolution;
- grade-band resolution;
- price resolution;
- availability resolution;
- rare-item chance resolution;
- Shop-owned service-cost resolution.

The production Shop generator calls these pure functions.

### 9.2 `src/admin/shop-runtime-policy.ts`

Follows existing Equipment/Ships/etc. pattern:

```text
fetch /api/runtime/space-typing/shop
validate envelope
materialize immutable ShopRuntimeSession
fallback fail-closed to BUNDLED_SHOP_POLICY
```

Required envelope properties:

```ts
{
  applyBoundary: "new-session+new-shop-instance",
  activeRevision: string | null,
  policy: ShopAdminPolicyV1
}
```

Malformed/unreachable Admin runtime must preserve bundled gameplay, never partially apply a policy.

### 9.3 Production `state.ts`

Refactor these behaviors to accept/use the resolved policy:

- `equipmentGradeForShop`;
- `priceForEquipment`;
- `priceForItem`;
- `tierPrice`;
- `shopEquipmentPool`;
- `generateStock`;
- `resurrectionChance`;
- `shopAvailable`.

Purchase logic continues charging persisted entry price and therefore remains stable for existing instances.

### 9.4 `service-shop.ts`

Only Shop-owned cost helpers should become policy-driven in A4.

Do not move unrelated progression ownership merely to make the Admin screen look complete.

---

## 10. Parent Admin architecture

### 10.1 Revision persistence

Shop draft lives in the existing whole-config immutable revision store:

```text
config.economy.shop
```

No second Shop database and no Shop-specific draft file.

### 10.2 Parent validator

Add:

```text
admin/shop-policy.mjs
```

It validates against child-owned contract metadata:

- known Shop types;
- known Item IDs;
- known Equipment IDs;
- known Grades;
- known Equipment tiers;
- known discovery prerequisites;
- currency amounts/ranges;
- grade weights;
- generation count/stock ranges;
- badge/text lengths;
- allowed authorable keys only.

Unknown fields fail closed.

### 10.3 Runtime envelope

Add:

```text
admin/shop-runtime.mjs
GET /api/runtime/space-typing/shop
```

Runtime endpoint remains read-only/public-to-same-origin like existing Ships/Equipment/Worlds runtime endpoints. Admin mutation endpoints remain token-protected.

### 10.4 Preview bridge

Add:

```text
POST /api/admin/space-typing/shop/preview
```

Preview is authenticated and read-only.

Parent does not simulate Shop rules itself. It invokes child preview logic using the draft policy.

### 10.5 Change-scope domain

Extend A0.5 change-scope mapping:

```text
economy.shop.* -> economy.shop
```

This makes History & Publish explain Shop changes at the correct domain granularity.

---

## 11. Preview / simulation contract

Shop preview must answer an administrator question:

> "With this draft, what would a player actually see in this Shop scenario?"

Input:

```ts
type ShopPreviewScenario = {
  shopType: ShopType;
  stage: number;
  worldKey: string;
  luck: number;
  progression: number;
  discovered: readonly string[];
};
```

Optional future service mode may add a concrete service target, but ordinary stock preview is first.

Output:

```ts
type ShopAdminPreview = {
  protocolVersion: 1;
  configRevision: string;
  scenario: ShopPreviewScenario;
  available: boolean;
  seed: number;
  instanceId: string;
  generatedStock: readonly ShopAdminPreviewOffer[];
  warnings: readonly string[];
};
```

Each offer projects canonical runtime data:

- Item/Equipment display name from its registry;
- Item category or Equipment slot/tier;
- generated Equipment grade;
- quantity;
- exact multi-currency purchase price;
- optional compare-at price;
- optional badge;
- source of price (`default-policy` / `product-override`);
- source of eligibility;
- no raw filesystem/source path in primary preview UI.

Determinism requirement:

Given the same:

- draft policy;
- scenario;
- pinned child runtime;

the preview result must match a newly generated production Shop instance.

---

## 12. A4.1 Administrator workflow

A4.1 should not look like the current Runtime Contract inspector.

Primary Shop screen:

### 12.1 Product list

Projected rows come from Item + Equipment registries joined with Shop policy.

Columns should be administrator concepts:

- Product;
- Type (`Item` / `Equipment`);
- Sold in;
- Price summary;
- Stock rule;
- Badge/compare-at status;
- Enabled;
- Draft status.

Do not put raw source paths, runtime owner strings or child SHA in the primary table.

### 12.2 Product editor

Item product editor may expose:

- enabled in Shop;
- allowed Shop types;
- stock per Shop type;
- exact price override per Shop type;
- compare-at price;
- badge.

Equipment editor may expose:

- enabled in Shop;
- allowed Shop types;
- price overrides by Shop type + generated Grade;
- compare-at price by Shop type + Grade;
- badge.

Canonical Item/Equipment name/stats/icon are shown but linked/read-only unless that owning domain supports editing them.

### 12.3 Rules tabs

Separate policy management from individual products:

- Stock Generation;
- Equipment Grade Chances;
- Shop Availability;
- Default Pricing;
- Service Pricing.

### 12.4 Preview

Administrator chooses scenario controls and sees a generated Shop preview from the child production engine.

### 12.5 Lifecycle

Use existing A1/A0.5 primitives:

```text
Edit -> Save Draft -> Validate -> Preview -> History/change scope -> Publish
```

---

## 13. Validation rules

At minimum:

- all counts/stocks are integers in safe configured ranges;
- all currency amounts are non-negative integers and bounded;
- no all-zero actual price unless explicitly allowed as a free offer;
- grade weights are finite/non-negative and each active band has total weight > 0;
- stage bands are ordered/non-overlapping;
- referenced Item/Equipment IDs exist in child contract;
- Equipment grade/tier keys are valid;
- Shop type keys are valid;
- discovery IDs come from allowlist;
- badges are short plain text with a defined max length;
- unknown keys rejected;
- duplicate pool IDs rejected;
- disabled products cannot be required as guaranteed generated entries;
- compare-at data never changes charge price;
- static offer overrides cannot introduce schedule/account targeting fields;
- runtime envelope malformed -> bundled fallback, not partial merge.

---

## 14. What A4.0 explicitly rejects

### Rejected: one static row = one live Shop stock row

Why: actual stock is generated per Shop instance and persisted per player.

### Rejected: Admin writes directly to `PlayerSave.shopState`

Why: there is no remote player backend; it would also violate deterministic/save ownership.

### Rejected: duplicate Item/Equipment names/icons/descriptions inside Shop config

Why: creates shadow models and drift.

### Rejected: price formula reimplementation in Portal

Why: preview would diverge from gameplay.

### Rejected: change all existing saved Shop prices on Publish

Why: mid-instance repricing and save mutation are unsafe.

### Rejected: generic `discountPercent` plus separately editable final price

Why: creates two competing sources of truth.

### Rejected: fake scheduled promotion fields

Why: there is no production scheduler/targeting backend yet.

### Rejected: Shop Media upload/path field

Why: generic Item/Equipment artwork belongs to its owning domain + Media V2. Shop may eventually select a Shop-specific promotional asset only after the runtime actually consumes that field.

---

## 15. Implementation slices after this architecture gate

### A4.0-S1 — child policy core + contract

- introduce bundled `ShopAdminPolicyV1` that reproduces current behavior;
- child contract exposes IDs/types/grades/constraints;
- unit tests prove bundled policy parity for representative scenarios.

### A4.0-S2 — refactor production generator to shared policy engine

- no behavioral change under bundled policy;
- existing Shop save/purchase tests stay green;
- add deterministic parity snapshots.

### A4.0-S3 — child runtime materializer + parent runtime envelope

- optional `economy.shop` config;
- strict validation;
- bundled fallback;
- `GET /api/runtime/space-typing/shop`;
- new-session/new-shop-instance apply boundary.

### A4.0-S4 — preview bridge

- child production-engine preview;
- parent authenticated endpoint;
- scenario/determinism tests;
- no player-save mutation.

### A4.0-S5 — revision lifecycle smoke

- draft isolated;
- preview uses draft policy;
- runtime stays active policy until Publish;
- Publish changes future runtime Shop policy;
- rollback restores prior policy for future sessions/instances;
- existing persisted ShopInstance remains unchanged.

### A4.1 — Shop administrator UI

Only after S1-S5 are green:

- product list/editor;
- pricing/stock/availability rules;
- static compare-at/badge capability that is actually consumed by child UI;
- service pricing for Shop-owned services;
- scenario preview;
- draft lifecycle;
- manual acceptance.

---

## 16. A4.0 exit criteria

A4.0 is not complete until all of the following are true:

- architecture document is accepted as the implementation source of truth;
- bundled policy is machine-readable and reproduces current runtime behavior;
- production Shop generator/pricing/availability consumes the shared policy engine;
- no second Shop generator exists in parent/Portal;
- strict parent/child validators exist;
- runtime envelope exists with fail-closed bundled fallback;
- preview uses the same production engine;
- existing ShopInstance persistence behavior is explicitly preserved;
- service-cost ownership is not silently duplicated;
- Admin revision lifecycle tests prove draft/publish/rollback behavior;
- CI keeps existing Shop/player-save tests green;
- no A4.1 editor is enabled before these conditions are met.
