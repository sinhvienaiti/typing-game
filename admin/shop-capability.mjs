export const SHOP_AUDITED_CHILD_SHA = "83f80b3d6f640ea1af46e158e25485bc57b31393";

export const SHOP_TABS = Object.freeze([
  "Catalog",
  "Featured",
  "Daily",
  "Weekly",
  "Bundles",
  "History",
]);

export const SHOP_FIELDS = Object.freeze([
  "ID",
  "Item",
  "Category",
  "Price",
  "Currency",
  "Original Price",
  "Discount",
  "Purchase Limit",
  "Daily Limit",
  "Weekly Limit",
  "Availability",
  "Requirement",
  "Featured",
  "Sort Order",
  "Enabled",
]);

const runtimeFieldNames = new Set([
  "ID",
  "Item",
  "Category",
  "Price",
  "Currency",
  "Purchase Limit",
  "Availability",
  "Requirement",
  "Enabled",
]);

const runtimeReason = "Derived by the pinned Space Typing Shop runtime. It is inspectable here but not authorable because the current gameplay policy is source-owned and purchase state persists in PlayerSave.";
const unsupportedReason = "The current Space Typing Shop runtime has no native concept for this master-plan field. Admin keeps the field visible but locked instead of fabricating behavior.";
const authoringReason = "Shop generation/pricing rules are source-owned in the child runtime and transaction state persists in PlayerSave. No canonical admin-config consumer exists yet, so Shop authoring remains closed.";

export function createShopCapabilityManifest() {
  return {
    protocolVersion: 3,
    mode: "runtime-backed-readonly",
    owner: "Space Typing shops/economy runtime",
    auditedChildSha: SHOP_AUDITED_CHILD_SHA,
    tabs: SHOP_TABS,
    fields: SHOP_FIELDS.map((name) => ({
      name,
      runtimeBacked: runtimeFieldNames.has(name),
      source: runtimeFieldNames.has(name) ? "runtime-derived" : "unsupported",
      authorable: false,
      reason: runtimeFieldNames.has(name) ? runtimeReason : unsupportedReason,
    })),
    capabilities: {
      runtimeCatalogGeneration: true,
      purchaseTransaction: true,
      pricing: true,
      currencies: true,
      stockRemaining: true,
      availability: true,
      serviceShop: true,
      catalogWrite: false,
      schedules: false,
      bundles: false,
      transactionHistory: false,
      preview: false,
    },
    runtime: {
      sources: [
        "src/shops/state.ts",
        "src/shops/service-shop.ts",
        "src/economy/credits.ts",
        "src/economy/currencies.ts",
      ],
      persistence: "PlayerSave + session-scoped shop stock",
      currencyIds: ["credits", "alloy", "star-crystal", "quantum-core"],
      priceStateKeys: ["credits", "alloy", "starCrystal", "quantumCore"],
      serviceShopOwner: "src/shops/service-shop.ts",
      purchaseOwner: "src/shops/state.ts::buyShopStockEntry",
    },
    authoring: {
      enabled: false,
      applyBoundary: "none",
      reason: authoringReason,
    },
  };
}
