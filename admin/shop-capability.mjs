export const SHOP_AUDITED_CHILD_SHA = "6fa13b857990b1f7593b415557a837c505d6fc56";

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

const unavailableReason = "No canonical Shop transaction/catalog owner was found in the pinned Space Typing runtime tree. Authoring stays closed until a real consumer, validation boundary, and persistence owner exist.";

export function createShopCapabilityManifest() {
  return {
    protocolVersion: 1,
    mode: "runtime-audited-readonly",
    owner: "Space Typing runtime audit",
    auditedChildSha: SHOP_AUDITED_CHILD_SHA,
    tabs: SHOP_TABS,
    fields: SHOP_FIELDS.map((name) => ({
      name,
      authorable: false,
      reason: unavailableReason,
    })),
    capabilities: {
      catalogRead: false,
      catalogWrite: false,
      purchaseTransaction: false,
      pricing: false,
      currencies: false,
      limits: false,
      schedules: false,
      bundles: false,
      transactionHistory: false,
      preview: false,
    },
    evidence: [
      { id: "shop-owner", found: false, detail: "No shop/economy/monetization module path in the audited child tree." },
      { id: "purchase-owner", found: false, detail: "No purchase or wallet module path in the audited child tree." },
      { id: "currency-owner", found: false, detail: "No canonical currency module path in the audited child tree." },
      { id: "stamina-owner", found: false, detail: "No stamina module path in the audited child tree." },
    ],
    linkedRuntimeDomains: [
      { id: "ships", label: "Ships", route: "/admin/space-typing/ships", relationship: "runtime-backed content; not proven purchasable" },
      { id: "equipment", label: "Equipment", route: "/admin/space-typing/equipment", relationship: "runtime-backed content; not proven purchasable" },
      { id: "skills", label: "Skills", route: "/admin/space-typing/skills", relationship: "runtime-backed content; not proven purchasable" },
    ],
    authoring: {
      enabled: false,
      applyBoundary: "none",
      persistence: "runtime-audit-manifest",
      reason: unavailableReason,
    },
    preview: {
      available: false,
      reason: "Shop Preview cannot be truthful until a canonical catalog and pricing/purchase consumer exist.",
    },
  };
}
