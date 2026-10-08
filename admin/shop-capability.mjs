export const SHOP_AUDITED_CHILD_SHA = "8128a2a5a7713fff80cd1286b607de6a3e7190f7";

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
      shopTypes: ["normal", "station", "traveling", "black-market", "hidden", "event", "service"],
      currencyIds: ["credits", "alloy", "star-crystal", "quantum-core"],
      priceStateKeys: ["credits", "alloy", "starCrystal", "quantumCore"],
      stockKinds: ["item", "equipment"],
      transactionReasons: ["missing", "sold-out", "currency", "full", "duplicate"],
      refreshBoundary: "sector-instance",
      persistenceOwner: "PlayerSave.shopState",
    },
    evidence: [
      { id: "catalog-owner", found: true, detail: "src/shops/state.ts owns deterministic stock generation and ShopInstance persistence." },
      { id: "purchase-owner", found: true, detail: "buyShopStockEntry validates stock/currency/inventory and applies purchase state." },
      { id: "pricing-owner", found: true, detail: "ShopPrice stores Credits/Alloy plus camelCase Star Crystal/Quantum Core balance keys while the contract exposes canonical hyphenated currency IDs." },
      { id: "availability-owner", found: true, detail: "shopAvailable gates black-market/hidden/event/traveling shops from discovery and luck." },
      { id: "service-owner", found: true, detail: "src/shops/service-shop.ts owns upgrade/repair/evolution/service purchase costs." },
      { id: "authoring-seam", found: false, detail: "No child config contract consumes admin-authored Shop policy yet; write capability stays disabled." },
    ],
    linkedRuntimeDomains: [
      { id: "equipment", label: "Equipment", route: "/admin/space-typing/equipment", relationship: "Shop stock and service upgrades consume runtime equipment definitions/state." },
      { id: "currencies", label: "Currencies", route: "/admin/space-typing/currencies", relationship: "Purchases spend Credits, Alloy, Star Crystal and Quantum Core." },
      { id: "skills", label: "Skills", route: "/admin/space-typing/skills", relationship: "Service Shop can consume upgrade progression state; it is not a separate catalog authoring source." },
    ],
    authoring: {
      enabled: false,
      applyBoundary: "none",
      persistence: "child-runtime-state",
      reason: authoringReason,
    },
    preview: {
      available: false,
      reason: "Runtime generation is real, but the child contract does not expose an admin preview protocol yet. Admin does not reimplement the generator because that would create a second source of truth.",
    },
  };
}
