// A17 Shop authority re-audit: f31a2908..22a35dd finalizes only the Admin
// testing-selection capability semantics/tests and legacy player-setting row.
// Shop policy/contracts, generation, pricing, availability, offers, services
// and transaction ownership sources remain unchanged.
export const SHOP_AUDITED_CHILD_SHA = "22a35dd24e25cd9e6881aba350977eb6f42889f2";

export const SHOP_TABS = Object.freeze([
  "Catalog",
  "Pricing",
  "Availability",
  "Offers",
  "Services",
  "Deferred",
]);

export const SHOP_FIELDS = Object.freeze([
  "ID",
  "Item",
  "Category",
  "Price",
  "Original Price",
  "Discount",
  "Stock",
  "Availability",
  "Requirement",
  "Badge / Label",
  "Enabled",
  "Daily Limit",
  "Weekly Limit",
  "Featured",
  "Sort Order",
]);

const fieldModel = Object.freeze({
  "ID": [true, "registry-owned", false, "Stable product identity is owned by the item/equipment registries."],
  "Item": [true, "registry-owned", false, "Name and core identity are owned by the item/equipment registries; Shop policy selects registered IDs."],
  "Category": [true, "registry-owned", false, "Item/equipment category is owned by its registry."],
  "Price": [true, "policy-authorable", true, "Authorable through pricing tables and per-offer overrides."],
  "Original Price": [true, "policy-authorable", true, "Authorable as compare-at price on item/equipment offer overrides."],
  "Discount": [true, "runtime-derived", false, "Discount presentation is derived from Price and Original Price; no independent percentage source is created."],
  "Stock": [true, "policy-authorable", true, "Item stock is authorable per Shop type; generated equipment count is controlled by generation rules."],
  "Availability": [true, "policy-authorable", true, "Authorable through Shop-type availability rules and offer Shop-type scopes."],
  "Requirement": [true, "policy-authorable", true, "Discovery/chance requirements are authorable through canonical availability rules."],
  "Badge / Label": [true, "policy-authorable", true, "Optional offer badge is consumed by the canonical Shop policy."],
  "Enabled": [true, "policy-authorable", true, "Per-offer enabled state is authorable without changing registry identity."],
  "Daily Limit": [false, "unsupported", false, "The current runtime has no daily purchase-limit semantic."],
  "Weekly Limit": [false, "unsupported", false, "The current runtime has no weekly purchase-limit semantic."],
  "Featured": [false, "unsupported", false, "The current runtime has no featured-ranking semantic."],
  "Sort Order": [false, "unsupported", false, "The deterministic generator owns runtime ordering; no independent Admin sort order exists."],
});

export function createShopCapabilityManifest(contract = {}) {
  const authorableSections = Array.isArray(contract.authorableSections) ? [...contract.authorableSections] : [];
  const previewProtocol = contract.previewProtocol ?? {};
  const runtime = contract.runtime ?? {};
  const previewAvailable = previewProtocol.available === true && previewProtocol.version === 1;
  const authoringEnabled = authorableSections.length > 0 && previewAvailable;

  return {
    protocolVersion: 4,
    mode: authoringEnabled ? "runtime-backed-authoring" : "runtime-backed-readonly",
    owner: "Space Typing shops/economy runtime",
    auditedChildSha: SHOP_AUDITED_CHILD_SHA,
    tabs: SHOP_TABS,
    fields: SHOP_FIELDS.map((name) => {
      const [runtimeBacked, source, authorable, reason] = fieldModel[name];
      return { name, runtimeBacked, source, authorable: authoringEnabled && authorable, reason };
    }),
    capabilities: {
      runtimeCatalogGeneration: true,
      purchaseTransaction: true,
      pricing: true,
      currencies: true,
      stockRemaining: true,
      availability: true,
      serviceShop: true,
      catalogWrite: authoringEnabled,
      offerWrite: authoringEnabled,
      servicePricingWrite: authoringEnabled,
      schedules: false,
      bundles: false,
      transactionHistory: false,
      preview: previewAvailable,
    },
    runtime: {
      sources: [
        "src/shops/policy.ts",
        "src/shops/state.ts",
        "src/shops/service-shop.ts",
        "src/economy/credits.ts",
        "src/economy/currencies.ts",
      ],
      shopTypes: Array.isArray(contract?.ids?.shopTypes) ? [...contract.ids.shopTypes] : [],
      currencyIds: ["credits", "alloy", "star-crystal", "quantum-core"],
      priceStateKeys: Array.isArray(contract.currencies) ? [...contract.currencies] : [],
      stockKinds: ["item", "equipment"],
      transactionReasons: ["missing", "sold-out", "currency", "full", "duplicate"],
      refreshBoundary: "sector-instance",
      persistenceOwner: "PlayerSave.shopState",
    },
    evidence: [
      { id: "policy-contract", found: authoringEnabled, detail: "src/shops/policy.ts exposes the validated ShopAdminPolicyV1 authoring contract consumed by runtime materialization." },
      { id: "catalog-owner", found: true, detail: "src/shops/state.ts owns deterministic stock generation and ShopInstance persistence." },
      { id: "purchase-owner", found: true, detail: "buyShopStockEntry validates stock/currency/inventory and applies purchase state." },
      { id: "pricing-owner", found: true, detail: "Shop policy pricing and offer overrides are consumed by the production generator; Admin does not reimplement pricing." },
      { id: "availability-owner", found: true, detail: "shopAvailable consumes canonical policy availability rules and discovery/luck context." },
      { id: "service-owner", found: true, detail: "src/shops/service-shop.ts consumes the canonical services policy for repair/enhancement/evolution/affix/dismantle costs." },
      { id: "preview-seam", found: previewAvailable, detail: previewAvailable ? "The child exports pnpm shop:admin-preview and materializes the same production Shop policy/runtime path." : "No compatible child Shop preview protocol is available." },
    ],
    linkedRuntimeDomains: [
      { id: "equipment", label: "Equipment", route: "/admin/space-typing/equipment", relationship: "Shop generation selects registered equipment IDs and service upgrades consume equipment state." },
      { id: "currencies", label: "Currencies", route: "/admin/space-typing/currencies", relationship: "Pricing spends Credits, Alloy, Star Crystal and Quantum Core." },
      { id: "skills", label: "Skills", route: "/admin/space-typing/skills", relationship: "Progression remains owned by progression/upgrades; Shop only consumes that state." },
    ],
    authoring: {
      enabled: authoringEnabled,
      configNamespace: contract.configNamespace ?? "economy.shop",
      sections: authorableSections,
      applyBoundary: runtime.applyBoundary ?? "none",
      persistence: authoringEnabled ? "admin-revision-store" : "child-runtime-state",
      reason: authoringEnabled
        ? "Drafts persist in the Admin revision store under economy.shop. Publish changes only future sessions and newly resolved Shop instances; existing ShopInstance snapshots do not self-reprice."
        : "Shop authoring remains closed until a canonical validated child policy and production preview protocol are available.",
    },
    preview: {
      available: previewAvailable,
      protocolVersion: previewAvailable ? previewProtocol.version : null,
      command: previewAvailable ? previewProtocol.plannedCommand : null,
      mutation: previewProtocol.mutation === true,
      reason: previewAvailable
        ? "Preview delegates to the pinned child production materializer/generator and never mutates the running game or Admin revision state."
        : "The pinned child contract does not expose a compatible Shop preview protocol.",
    },
    deferredCapabilities: Array.isArray(contract.deferredCapabilities) ? [...contract.deferredCapabilities] : [],
  };
}
