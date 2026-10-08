export const CURRENCIES_AUDITED_CHILD_SHA = "8128a2a5a7713fff80cd1286b607de6a3e7190f7";

export const CURRENCY_FIELDS = Object.freeze([
  "ID",
  "Name",
  "Icon",
  "Cap",
  "Display Precision",
  "Color",
  "Enabled",
]);

const RUNTIME_IDS = Object.freeze(["credits", "alloy", "star-crystal", "quantum-core"]);
const RUNTIME_NAMES = Object.freeze({
  credits: "Credits",
  alloy: "Alloy",
  "star-crystal": "Star Crystal",
  "quantum-core": "Quantum Core",
});
const BALANCE_KEYS = Object.freeze({
  credits: "credits",
  alloy: "alloy",
  "star-crystal": "starCrystal",
  "quantum-core": "quantumCore",
});
const MAX_BALANCE = 999_999_999;
const runtimeFieldNames = new Set(["ID", "Name", "Cap", "Display Precision"]);
const runtimeReason = "Derived from the pinned Space Typing economy runtime. The Admin surface is reference-only and does not mutate player balances or source-owned economy rules.";
const unsupportedReason = "The pinned runtime has no canonical metadata owner for this master-plan field. Admin keeps it visible as unsupported instead of inventing data.";

export function createCurrencyCapabilityManifest() {
  return {
    protocolVersion: 1,
    mode: "runtime-backed-readonly",
    owner: "Space Typing economy runtime",
    auditedChildSha: CURRENCIES_AUDITED_CHILD_SHA,
    fields: CURRENCY_FIELDS.map((name) => ({
      name,
      runtimeBacked: runtimeFieldNames.has(name),
      source: runtimeFieldNames.has(name) ? "runtime-derived" : "unsupported",
      authorable: false,
      reason: runtimeFieldNames.has(name) ? runtimeReason : unsupportedReason,
    })),
    currencies: RUNTIME_IDS.map((id) => ({
      id,
      name: RUNTIME_NAMES[id],
      balanceKey: BALANCE_KEYS[id],
      cap: MAX_BALANCE,
      displayPrecision: 0,
      icon: null,
      color: null,
      enabled: null,
    })),
    capabilities: {
      currencyDefinitions: true,
      hardCaps: true,
      stageClearGeneration: true,
      shopSpending: true,
      balanceAuthoring: false,
      definitionAuthoring: false,
      transactionLedger: false,
      analytics: false,
    },
    runtime: {
      sources: ["src/economy/credits.ts", "src/economy/currencies.ts", "src/shops/state.ts"],
      currencyIds: [...RUNTIME_IDS],
      balanceKeys: { ...BALANCE_KEYS },
      sourceFunctions: ["stageClearCreditReward", "stageClearExpansionCurrencyReward"],
      sinkFunctions: ["buyShopStockEntry"],
      cap: MAX_BALANCE,
      displayPrecision: 0,
    },
    analytics: {
      available: false,
      reason: "The runtime stores balances but does not expose a canonical transaction ledger, so Generated / Spent / Net / Top Sources / Top Sinks cannot be reported truthfully.",
      unsupportedMetrics: ["Generated", "Spent", "Net", "Top Sources", "Top Sinks"],
    },
    authoring: {
      enabled: false,
      reason: "Currency balances are player save-state and currency rules are child-runtime source-owned. No admin-config consumer exists for currency definitions or balances.",
    },
    linkedRuntimeDomains: [
      { id: "shop", label: "Shop", route: "/admin/space-typing/shop", relationship: "buyShopStockEntry is a confirmed sink for the four runtime currency IDs." },
      { id: "rewards", label: "Rewards & Drops", route: "/admin/space-typing/rewards", relationship: "Campaign, combat-credit and loot generation are now audited through the canonical Rewards runtime contract." },
    ],
  };
}
