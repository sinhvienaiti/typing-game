import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";
import { adminErrorMessage } from "./admin-http";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type ShopType = "normal" | "station" | "traveling" | "black-market" | "hidden" | "event" | "service";
type GradeId = "aluminum" | "copper" | "silver" | "gold" | "diamond";
type Price = { credits: number; alloy: number; starCrystal: number; quantumCore: number };
type GenerationRule = {
  itemPool: string[];
  itemCount: number;
  itemStock: number;
  equipmentCount: number;
  allowedEquipmentTiers: number[];
  equipmentPool?: string[];
};
type AvailabilityRule =
  | { kind: "always" }
  | { kind: "discovery"; discoveryId: string }
  | { kind: "seeded-chance"; baseChance: number; luckPerPoint: number; maxChance: number };
type ItemOffer = {
  enabled?: boolean;
  shopTypes?: ShopType[];
  stockByShopType?: Partial<Record<ShopType, number>>;
  priceByShopType?: Partial<Record<ShopType, Price>>;
  compareAtPriceByShopType?: Partial<Record<ShopType, Price>>;
  badge?: string | null;
};
type EquipmentOffer = {
  enabled?: boolean;
  shopTypes?: ShopType[];
  priceByShopTypeAndGrade?: Partial<Record<ShopType, Partial<Record<GradeId, Price>>>>;
  compareAtPriceByShopTypeAndGrade?: Partial<Record<ShopType, Partial<Record<GradeId, Price>>>>;
  badge?: string | null;
};
type ShopPolicy = {
  schemaVersion: 1;
  configRevision: string;
  generation: {
    shopTypes: Record<ShopType, GenerationRule>;
    equipmentGradeBands: Record<ShopType, Array<{ minStage: number; weights: Partial<Record<GradeId, number>> }>>;
    rareItems: Array<Record<string, unknown>>;
  };
  pricing: {
    itemGradePrices: Record<ShopType, Record<GradeId, Price>>;
    equipmentGradePrices: Record<ShopType, Record<GradeId, Price>>;
    equipmentTierAdjustments: Record<string, { creditsMultiplier: number; alloyMultiplier: number; tier3StarCrystalBonusWhenPriced: number }>;
  };
  availability: Record<ShopType, AvailabilityRule>;
  offers: { items: Record<string, ItemOffer>; equipment: Record<string, EquipmentOffer> };
  services: {
    repairPack: { credits: number; alloy: number };
    equipmentEnhancement: {
      gradeCreditMultiplier: Record<GradeId, number>;
      gradeAlloyBase: Record<GradeId, number>;
      creditBase: number;
      creditPerEnhancement: number;
      maxEnhancement: number;
    };
    equipmentEvolution: Partial<Record<GradeId, { credits: number; alloy: number; starCrystal: number; quantumCore: number; requiredStage: number }>>;
    affixes: Record<string, unknown>;
    dismantle: Record<string, unknown>;
    progressionOwner: string;
  };
};
type ShopAwareConfig = SpaceTypingAdminConfig & { economy?: { shop?: ShopPolicy } };
type ShopField = { name: string; runtimeBacked: boolean; source: "runtime-derived" | "policy-authorable" | "registry-owned" | "unsupported"; authorable: boolean; reason: string };
type ShopManifest = {
  protocolVersion: 4;
  mode: "runtime-backed-authoring" | "runtime-backed-readonly";
  owner: string;
  auditedChildSha: string;
  tabs: string[];
  fields: ShopField[];
  capabilities: Record<string, boolean>;
  runtime: { sources: string[]; shopTypes: ShopType[]; currencyIds: string[]; priceStateKeys: string[]; stockKinds: string[]; transactionReasons: string[]; refreshBoundary: string; persistenceOwner: string };
  authoring: { enabled: boolean; configNamespace: string; sections: string[]; applyBoundary: string; persistence: string; reason: string };
  preview: { available: boolean; protocolVersion: number | null; command: string | null; mutation: boolean; reason: string };
  deferredCapabilities: string[];
};
type ShopContract = {
  schemaVersion: 1;
  configNamespace: "economy.shop";
  ids: { shopTypes: ShopType[]; itemIds: string[]; equipmentIds: string[]; gradeIds: GradeId[]; equipmentTiers: number[]; discoveryIds: string[] };
  currencies: Array<keyof Price>;
  authorableSections: string[];
  constraints: Record<string, { min: number; max: number; integer?: boolean } | number>;
};
type PreviewStock = { kind: "item" | "equipment"; itemId?: string; definitionId?: string; grade?: GradeId; remaining: number; price: Price };
type ShopPreview = {
  protocolVersion: 1;
  kind: "space-typing-shop-runtime-preview";
  runtime: { source: "published"; activeRevision: string; configRevision: string; applyBoundary: string };
  policy: ShopPolicy;
  request: { shopType: ShopType; stage: number; worldKey: string; luck: number; progression: number; discovered: string[] };
  available: boolean;
  instance: { id: string; type: ShopType; worldKey: string; stage: number; sectorStart: number; seed: number; stock: PreviewStock[] };
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function button(label: string, onClick: () => void, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}
function grid(...children: HTMLElement[]): HTMLElement { const root = el("div", "stx-grid"); root.append(...children); return root; }
function isRecord(value: unknown): value is Record<string, unknown> { return value !== null && typeof value === "object" && !Array.isArray(value); }
function fieldLabel(label: string, help: string): HTMLElement {
  const root = el("span");
  root.append(document.createTextNode(label + " "));
  const info = el("span", "st-admin-status info", "ⓘ");
  info.title = help;
  info.setAttribute("aria-label", help);
  root.append(info);
  return root;
}
function numberField(label: string, value: number, help: string, options: { min?: number; max?: number; step?: number } = {}): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-field");
  root.append(fieldLabel(label, help));
  const control = el("input") as HTMLInputElement;
  control.type = "number";
  control.value = String(value);
  if (options.min !== undefined) control.min = String(options.min);
  if (options.max !== undefined) control.max = String(options.max);
  if (options.step !== undefined) control.step = String(options.step);
  root.append(control);
  return { root, control };
}
function textField(label: string, value: string, help: string): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-field"); root.append(fieldLabel(label, help));
  const control = el("input") as HTMLInputElement; control.type = "text"; control.value = value; root.append(control); return { root, control };
}
function selectField<T extends string>(label: string, value: T, values: readonly T[], help: string): { root: HTMLElement; control: HTMLSelectElement } {
  const root = el("label", "stx-field"); root.append(fieldLabel(label, help));
  const control = el("select") as HTMLSelectElement;
  for (const candidate of values) { const option = el("option") as HTMLOptionElement; option.value = candidate; option.textContent = candidate; option.selected = candidate === value; control.append(option); }
  root.append(control); return { root, control };
}
function checkRow(label: string, checked: boolean, help: string): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-toggle-row");
  const copy = el("div"); copy.append(el("strong", undefined, label)); const hint = el("small", undefined, "ⓘ"); hint.title = help; copy.append(hint);
  const control = el("input") as HTMLInputElement; control.type = "checkbox"; control.checked = checked; root.append(copy, control); return { root, control };
}
function emptyPrice(): Price { return { credits: 0, alloy: 0, starCrystal: 0, quantumCore: 0 }; }
function formatPrice(price: Price): string {
  const parts = Object.entries(price).filter(([, value]) => value > 0).map(([key, value]) => `${value} ${key}`);
  return parts.length ? parts.join(" · ") : "Free";
}
function validateShopManifest(value: unknown): ShopManifest {
  if (!isRecord(value) || value["protocolVersion"] !== 4 || !["runtime-backed-authoring", "runtime-backed-readonly"].includes(String(value["mode"]))) throw new Error("Shop capability response does not match protocol v4.");
  if (!isRecord(value["authoring"]) || !isRecord(value["preview"]) || !isRecord(value["runtime"]) || !Array.isArray(value["fields"]) || !Array.isArray(value["tabs"])) throw new Error("Shop capability response is incomplete.");
  return value as unknown as ShopManifest;
}
async function fetchShopManifest(): Promise<ShopManifest> { return validateShopManifest(await api.requestJson<unknown>("/api/admin/space-typing/shop/capabilities")); }
async function fetchShopContract(): Promise<ShopContract> { return api.requestJson<ShopContract>("/api/admin/space-typing/shop/contract"); }
async function previewShop(policy: ShopPolicy | undefined, context: Partial<ShopPreview["request"]> = {}): Promise<ShopPreview> {
  const payload = await api.requestJson<ShopPreview>("/api/admin/space-typing/shop/preview", { method: "POST", body: JSON.stringify({ ...(policy ? { policy } : {}), ...context }) });
  if (payload.protocolVersion !== 1 || payload.kind !== "space-typing-shop-runtime-preview" || !payload.policy || !payload.instance?.stock) throw new Error("Shop preview response does not match the canonical child protocol.");
  return payload;
}

export function renderPhaseBShop(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading");
  const dirtyBadge = badge("CLEAN", "good");
  const previewBadge = badge("PREVIEW · pending");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Economy · Shop Control Plane · A4.1"),
    el("h1", undefined, "Shop"),
    el("p", undefined, "Manage canonical Shop generation, prices, stock, availability, offer labels and service costs. Draft preview delegates to the same production Shop engine used by gameplay."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(dirtyBadge, previewBadge, revisionBadge, button("Currencies", () => navigate("/admin/space-typing/currencies")), button("History", () => navigate("/admin/space-typing/history")));
  header.append(copy, actions); page.append(header);

  const status = notice("Loading active Shop policy and production preview…"); status.setAttribute("aria-live", "polite");
  const tabs = el("div", "st-admin-page-actions"); tabs.setAttribute("role", "tablist");
  const content = el("div");
  const previewHost = el("div");
  page.append(status, tabs, content, previewHost);

  let manifest: ShopManifest | null = null;
  let contract: ShopContract | null = null;
  let policy: ShopPolicy | null = null;
  let bundledPolicy: ShopPolicy | null = null;
  let baselinePolicy = "";
  let validatedPolicy: string | null = null;
  let latestPreview: ShopPreview | null = null;
  let loadedActiveRevision: string | null = null;
  let draftRevision: string | null = null;
  let activeTab = "Catalog";
  let selectedShopType: ShopType = "normal";
  let selectedGrade: GradeId = "aluminum";
  let selectedOfferKind: "item" | "equipment" = "item";
  let selectedOfferId = "";
  let loadGeneration = 0;
  const previewContext: Partial<ShopPreview["request"]> = { shopType: "normal", stage: 1, worldKey: "admin-preview", luck: 0, progression: 0, discovered: [] };
  let saveButton: HTMLButtonElement;
  let publishButton: HTMLButtonElement;
  let saveStatus: HTMLElement;

  const policyHash = (): string => policy ? JSON.stringify(policy) : "";
  const refreshBadges = (): void => {
    const dirty = policy !== null && policyHash() !== baselinePolicy;
    dirtyBadge.textContent = dirty ? "DIRTY" : "CLEAN"; dirtyBadge.className = `st-admin-status ${dirty ? "warn" : "good"}`;
    const valid = policy !== null && validatedPolicy === policyHash();
    previewBadge.textContent = valid ? "PREVIEW · VALID" : "PREVIEW · pending"; previewBadge.className = `st-admin-status ${valid ? "good" : "info"}`;
    if (publishButton) publishButton.disabled = draftRevision === null;
  };
  const markDirty = (): void => { validatedPolicy = null; latestPreview = null; draftRevision = null; refreshBadges(); renderPreviewPanel(); };
  const bindNumber = (field: { control: HTMLInputElement }, apply: (value: number) => void): void => field.control.addEventListener("input", () => { apply(Number(field.control.value)); markDirty(); });
  const bindText = (field: { control: HTMLInputElement }, apply: (value: string) => void): void => field.control.addEventListener("input", () => { apply(field.control.value); markDirty(); });

  const priceEditor = (title: string, price: Price, onChange: () => void): HTMLElement => {
    const root = panel(title);
    const fields = (["credits", "alloy", "starCrystal", "quantumCore"] as const).map((currency) => numberField(currency, price[currency], `Amount charged in ${currency}. Runtime/server validation enforces non-negative integer currency amounts.`, { min: 0, step: 1 }));
    for (const [index, currency] of (["credits", "alloy", "starCrystal", "quantumCore"] as const).entries()) {
      fields[index].control.addEventListener("input", () => { price[currency] = Number(fields[index].control.value); onChange(); markDirty(); });
    }
    root.append(grid(...fields.map((field) => field.root))); return root;
  };

  const renderCatalog = (): void => {
    if (!policy || !contract) return;
    const root = panel("Catalog generation", "Administrator-facing controls backed by ShopAdminPolicyV1");
    const type = selectField("Shop type", selectedShopType, contract.ids.shopTypes, "Choose which runtime Shop family to configure.");
    type.control.addEventListener("change", () => { selectedShopType = type.control.value as ShopType; previewContext.shopType = selectedShopType; renderActiveTab(); renderPreviewPanel(); });
    const rule = policy.generation.shopTypes[selectedShopType];
    const itemCount = numberField("Item slots", rule.itemCount, "Number of item entries generated for a new Shop instance.", { min: 0, max: 50, step: 1 });
    const itemStock = numberField("Stock per item", rule.itemStock, "Starting remaining stock for generated item entries.", { min: 0, max: 99, step: 1 });
    const equipmentCount = numberField("Equipment slots", rule.equipmentCount, "Number of equipment entries generated for a new Shop instance.", { min: 0, max: 50, step: 1 });
    bindNumber(itemCount, (value) => { rule.itemCount = value; }); bindNumber(itemStock, (value) => { rule.itemStock = value; }); bindNumber(equipmentCount, (value) => { rule.equipmentCount = value; });
    root.append(grid(type.root, itemCount.root, itemStock.root, equipmentCount.root));

    const pools = panel("Item pool", "Registered products only · hover ⓘ for field intent");
    for (const itemId of contract.ids.itemIds) {
      const control = checkRow(itemId, rule.itemPool.includes(itemId), "Include this registered item in deterministic generation for the selected Shop type.");
      control.control.addEventListener("change", () => { rule.itemPool = control.control.checked ? [...new Set([...rule.itemPool, itemId])] : rule.itemPool.filter((id) => id !== itemId); markDirty(); });
      pools.append(control.root);
    }
    const tiers = panel("Equipment tiers");
    for (const tier of contract.ids.equipmentTiers) {
      const control = checkRow(`Tier ${tier}`, rule.allowedEquipmentTiers.includes(tier), "Allow this canonical equipment tier in generated stock.");
      control.control.addEventListener("change", () => { rule.allowedEquipmentTiers = control.control.checked ? [...new Set([...rule.allowedEquipmentTiers, tier])].sort() : rule.allowedEquipmentTiers.filter((value) => value !== tier); markDirty(); }); tiers.append(control.root);
    }
    content.append(root, grid(pools, tiers));
  };

  const renderPricing = (): void => {
    if (!policy || !contract) return;
    const selector = panel("Base pricing selector");
    const type = selectField("Shop type", selectedShopType, contract.ids.shopTypes, "Pricing table applied before per-product offer overrides.");
    const grade = selectField("Grade", selectedGrade, contract.ids.gradeIds, "Select equipment/item grade price band.");
    type.control.addEventListener("change", () => { selectedShopType = type.control.value as ShopType; previewContext.shopType = selectedShopType; renderActiveTab(); });
    grade.control.addEventListener("change", () => { selectedGrade = grade.control.value as GradeId; renderActiveTab(); });
    selector.append(grid(type.root, grade.root));
    const itemPrice = policy.pricing.itemGradePrices[selectedShopType][selectedGrade];
    const equipmentPrice = policy.pricing.equipmentGradePrices[selectedShopType][selectedGrade];
    content.append(selector, grid(priceEditor("Item base price", itemPrice, () => {}), priceEditor("Equipment base price", equipmentPrice, () => {})));

    const tiers = panel("Equipment tier multipliers");
    for (const tier of contract.ids.equipmentTiers) {
      const adjustment = policy.pricing.equipmentTierAdjustments[String(tier)];
      if (!adjustment) continue;
      const credits = numberField(`Tier ${tier} credits ×`, adjustment.creditsMultiplier, "Multiplier applied to base credits price.", { min: 0, step: 0.05 });
      const alloy = numberField(`Tier ${tier} alloy ×`, adjustment.alloyMultiplier, "Multiplier applied to base alloy price.", { min: 0, step: 0.05 });
      const crystal = numberField(`Tier ${tier} crystal bonus`, adjustment.tier3StarCrystalBonusWhenPriced, "Additional Star Crystal amount when the tier is priced in crystals.", { min: 0, step: 1 });
      bindNumber(credits, (value) => { adjustment.creditsMultiplier = value; }); bindNumber(alloy, (value) => { adjustment.alloyMultiplier = value; }); bindNumber(crystal, (value) => { adjustment.tier3StarCrystalBonusWhenPriced = value; });
      tiers.append(grid(credits.root, alloy.root, crystal.root));
    }
    content.append(tiers);
  };

  const renderAvailability = (): void => {
    if (!policy || !contract) return;
    const root = panel("Shop availability", "Configure the production shopAvailable rule for each Shop type");
    const type = selectField("Shop type", selectedShopType, contract.ids.shopTypes, "Runtime Shop family whose availability rule is being edited.");
    type.control.addEventListener("change", () => { selectedShopType = type.control.value as ShopType; previewContext.shopType = selectedShopType; renderActiveTab(); });
    let rule = policy.availability[selectedShopType];
    const kind = selectField("Rule", rule.kind, ["always", "discovery", "seeded-chance"] as const, "Always, discovery-gated, or deterministic chance influenced by luck.");
    kind.control.addEventListener("change", () => {
      const next = kind.control.value as AvailabilityRule["kind"];
      policy!.availability[selectedShopType] = next === "always" ? { kind: "always" } : next === "discovery" ? { kind: "discovery", discoveryId: contract!.ids.discoveryIds[0] } : { kind: "seeded-chance", baseChance: 0.25, luckPerPoint: 0.001, maxChance: 0.5 };
      markDirty(); renderActiveTab();
    });
    root.append(grid(type.root, kind.root)); rule = policy.availability[selectedShopType];
    if (rule.kind === "discovery") {
      const discovery = selectField("Discovery requirement", rule.discoveryId, contract.ids.discoveryIds, "Canonical hidden-content discovery required before this Shop can appear.");
      discovery.control.addEventListener("change", () => { (policy!.availability[selectedShopType] as Extract<AvailabilityRule, {kind:"discovery"}>).discoveryId = discovery.control.value; markDirty(); }); root.append(discovery.root);
    } else if (rule.kind === "seeded-chance") {
      const base = numberField("Base chance", rule.baseChance, "Base deterministic appearance chance from 0 to 1.", { min: 0, max: 1, step: 0.01 });
      const luck = numberField("Luck per point", rule.luckPerPoint, "Chance added per luck point.", { min: 0, max: 1, step: 0.0005 });
      const max = numberField("Maximum chance", rule.maxChance, "Hard upper bound after luck adjustment.", { min: 0, max: 1, step: 0.01 });
      bindNumber(base, (value) => { (policy!.availability[selectedShopType] as Extract<AvailabilityRule,{kind:"seeded-chance"}>).baseChance = value; });
      bindNumber(luck, (value) => { (policy!.availability[selectedShopType] as Extract<AvailabilityRule,{kind:"seeded-chance"}>).luckPerPoint = value; });
      bindNumber(max, (value) => { (policy!.availability[selectedShopType] as Extract<AvailabilityRule,{kind:"seeded-chance"}>).maxChance = value; }); root.append(grid(base.root, luck.root, max.root));
    }
    content.append(root);
  };

  const renderOffers = (): void => {
    if (!policy || !contract) return;
    const root = panel("Product offer override", "Manage visibility, Shop scope, stock, price, compare-at price and label without changing registry identity");
    const kind = selectField("Product kind", selectedOfferKind, ["item", "equipment"] as const, "Item or equipment registry product.");
    const ids = selectedOfferKind === "item" ? contract.ids.itemIds : contract.ids.equipmentIds;
    if (!ids.includes(selectedOfferId)) selectedOfferId = ids[0] ?? "";
    const product = selectField("Product", selectedOfferId, ids, "Stable registry ID. Rename/art changes belong to the owning registry screen, not Shop.");
    const type = selectField("Shop type", selectedShopType, contract.ids.shopTypes, "Shop type whose per-offer values are being edited.");
    const grade = selectField("Grade", selectedGrade, contract.ids.gradeIds, "Grade used for equipment offer price overrides.");
    kind.control.addEventListener("change", () => { selectedOfferKind = kind.control.value as "item"|"equipment"; selectedOfferId = ""; renderActiveTab(); });
    product.control.addEventListener("change", () => { selectedOfferId = product.control.value; renderActiveTab(); });
    type.control.addEventListener("change", () => { selectedShopType = type.control.value as ShopType; previewContext.shopType = selectedShopType; renderActiveTab(); });
    grade.control.addEventListener("change", () => { selectedGrade = grade.control.value as GradeId; renderActiveTab(); });
    root.append(grid(kind.root, product.root, type.root, ...(selectedOfferKind === "equipment" ? [grade.root] : [])));
    if (!selectedOfferId) { root.append(notice("No registered product IDs are available.", "warn")); content.append(root); return; }

    const map = selectedOfferKind === "item" ? policy.offers.items : policy.offers.equipment;
    const existing = map[selectedOfferId];
    if (!existing) {
      root.append(notice("No override yet. Runtime uses generation/base-pricing defaults.", "info"), button("Create Override", () => {
        if (selectedOfferKind === "item") policy!.offers.items[selectedOfferId] = { enabled: true, shopTypes: [...contract!.ids.shopTypes], stockByShopType: {}, priceByShopType: {}, compareAtPriceByShopType: {}, badge: null };
        else policy!.offers.equipment[selectedOfferId] = { enabled: true, shopTypes: [...contract!.ids.shopTypes], priceByShopTypeAndGrade: {}, compareAtPriceByShopTypeAndGrade: {}, badge: null };
        markDirty(); renderActiveTab();
      }, "st-admin-btn primary")); content.append(root); return;
    }

    const enabled = checkRow("Enabled", existing.enabled !== false, "Disable this offer without deleting the registered item/equipment definition."); enabled.control.addEventListener("change", () => { existing.enabled = enabled.control.checked; markDirty(); });
    const badgeField = textField("Badge / label", existing.badge ?? "", "Optional short Shop label such as SALE, NEW or EVENT. Length is validated by the server contract."); bindText(badgeField, (value) => { existing.badge = value.trim() ? value : null; });
    root.append(enabled.root, badgeField.root);
    const scopes = panel("Available in Shop types");
    for (const shopType of contract.ids.shopTypes) {
      const scope = checkRow(shopType, existing.shopTypes?.includes(shopType) ?? true, "Limit this product override to selected Shop types.");
      scope.control.addEventListener("change", () => { const current = existing.shopTypes ?? [...contract!.ids.shopTypes]; existing.shopTypes = scope.control.checked ? [...new Set([...current, shopType])] : current.filter((value) => value !== shopType); markDirty(); }); scopes.append(scope.root);
    }
    root.append(scopes);

    if (selectedOfferKind === "item") {
      const offer = existing as ItemOffer; offer.stockByShopType ??= {}; offer.priceByShopType ??= {}; offer.compareAtPriceByShopType ??= {};
      const stock = numberField("Stock override", offer.stockByShopType[selectedShopType] ?? policy.generation.shopTypes[selectedShopType].itemStock, "Starting stock for this item in the selected Shop type.", { min: 0, max: 99, step: 1 });
      bindNumber(stock, (value) => { offer.stockByShopType![selectedShopType] = value; }); root.append(stock.root);
      offer.priceByShopType[selectedShopType] ??= structuredClone(policy.pricing.itemGradePrices[selectedShopType]["aluminum"]);
      offer.compareAtPriceByShopType[selectedShopType] ??= structuredClone(offer.priceByShopType[selectedShopType]!);
      root.append(grid(priceEditor("Offer price", offer.priceByShopType[selectedShopType]!, () => {}), priceEditor("Original / compare-at price", offer.compareAtPriceByShopType[selectedShopType]!, () => {})));
    } else {
      const offer = existing as EquipmentOffer; offer.priceByShopTypeAndGrade ??= {}; offer.compareAtPriceByShopTypeAndGrade ??= {}; offer.priceByShopTypeAndGrade[selectedShopType] ??= {}; offer.compareAtPriceByShopTypeAndGrade[selectedShopType] ??= {};
      offer.priceByShopTypeAndGrade[selectedShopType]![selectedGrade] ??= structuredClone(policy.pricing.equipmentGradePrices[selectedShopType][selectedGrade]);
      offer.compareAtPriceByShopTypeAndGrade[selectedShopType]![selectedGrade] ??= structuredClone(offer.priceByShopTypeAndGrade[selectedShopType]![selectedGrade]!);
      root.append(grid(priceEditor("Offer price", offer.priceByShopTypeAndGrade[selectedShopType]![selectedGrade]!, () => {}), priceEditor("Original / compare-at price", offer.compareAtPriceByShopTypeAndGrade[selectedShopType]![selectedGrade]!, () => {})));
    }
    root.append(button("Remove Override", () => { delete map[selectedOfferId]; markDirty(); renderActiveTab(); })); content.append(root);
  };

  const renderServices = (): void => {
    if (!policy || !contract) return;
    const services = policy.services;
    const repair = panel("Repair service");
    const credits = numberField("Repair credits", services.repairPack.credits, "Credits charged for the repair pack service.", { min: 0, step: 1 });
    const alloy = numberField("Repair alloy", services.repairPack.alloy, "Alloy charged for the repair pack service.", { min: 0, step: 1 });
    bindNumber(credits, (value) => { services.repairPack.credits = value; }); bindNumber(alloy, (value) => { services.repairPack.alloy = value; }); repair.append(grid(credits.root, alloy.root));
    const enhancement = panel("Equipment enhancement");
    const base = numberField("Credit base", services.equipmentEnhancement.creditBase, "Base credits before enhancement-level scaling.", { min: 0, step: 1 });
    const per = numberField("Credits / enhancement", services.equipmentEnhancement.creditPerEnhancement, "Additional credits per current enhancement level.", { min: 0, step: 1 });
    const max = numberField("Maximum enhancement", services.equipmentEnhancement.maxEnhancement, "Maximum enhancement level accepted by the service policy.", { min: 0, step: 1 });
    bindNumber(base, (value) => { services.equipmentEnhancement.creditBase = value; }); bindNumber(per, (value) => { services.equipmentEnhancement.creditPerEnhancement = value; }); bindNumber(max, (value) => { services.equipmentEnhancement.maxEnhancement = value; }); enhancement.append(grid(base.root, per.root, max.root));
    const evolution = panel("Evolution cost");
    const grade = selectField("Target grade", selectedGrade, contract.ids.gradeIds, "Select canonical grade evolution cost to edit."); grade.control.addEventListener("change", () => { selectedGrade = grade.control.value as GradeId; renderActiveTab(); }); evolution.append(grade.root);
    const cost = services.equipmentEvolution[selectedGrade];
    if (cost) {
      for (const [label, key] of [["Credits", "credits"], ["Alloy", "alloy"], ["Star Crystal", "starCrystal"], ["Quantum Core", "quantumCore"], ["Required stage", "requiredStage"]] as const) {
        const field = numberField(label, cost[key], `Canonical ${label.toLowerCase()} requirement for evolution to ${selectedGrade}.`, { min: 0, step: 1 }); bindNumber(field, (value) => { cost[key] = value; }); evolution.append(field.root);
      }
    } else evolution.append(notice(`No evolution rule is defined for ${selectedGrade}; Admin does not invent one.`, "info"));
    content.append(grid(repair, enhancement), evolution);
  };

  const renderDeferred = (): void => {
    if (!manifest) return;
    const root = panel("Deferred capabilities", "Visible so administrators know what is intentionally not implemented");
    for (const capability of manifest.deferredCapabilities) { const row = notice(capability, "info"); row.title = "Locked because the production Shop runtime has no canonical consumer for this capability yet."; root.append(row); }
    content.append(root);
  };

  const renderActiveTab = (): void => {
    content.replaceChildren();
    if (!policy || !contract || !manifest) { content.append(notice("Shop authoring is not ready.", "warn")); return; }
    if (activeTab === "Catalog") renderCatalog();
    else if (activeTab === "Pricing") renderPricing();
    else if (activeTab === "Availability") renderAvailability();
    else if (activeTab === "Offers") renderOffers();
    else if (activeTab === "Services") renderServices();
    else renderDeferred();
  };

  const runPreview = async (): Promise<void> => {
    if (!policy) return;
    setAdminStatus(status, "Running production Shop preview…", "loading");
    try {
      latestPreview = await previewShop(policy, previewContext);
      validatedPolicy = policyHash(); refreshBadges(); renderPreviewPanel();
      setAdminStatus(status, `Preview accepted · ${latestPreview.runtime.configRevision} · ${latestPreview.instance.stock.length} stock entries · ${latestPreview.available ? "available" : "availability rule blocked"}.`, "success");
    } catch (error: unknown) {
      validatedPolicy = null; latestPreview = null; refreshBadges(); renderPreviewPanel(); setAdminStatus(status, adminErrorMessage(error, "Shop preview failed."), "error");
    }
  };

  function renderPreviewPanel(): void {
    previewHost.replaceChildren();
    if (!contract || !policy) return;
    const root = panel("Production preview", "Same materializer, availability resolver, deterministic generator and pricing path as gameplay");
    const type = selectField("Shop type", (previewContext.shopType ?? selectedShopType) as ShopType, contract.ids.shopTypes, "Shop family to resolve in preview.");
    const stage = numberField("Stage", Number(previewContext.stage ?? 1), "Campaign stage used by generation/grade/availability logic.", { min: 1, max: 1000, step: 1 });
    const world = textField("World key", String(previewContext.worldKey ?? "admin-preview"), "Stable world key used by the deterministic Shop seed.");
    const luck = numberField("Luck", Number(previewContext.luck ?? 0), "Player luck context used by rare-item and chance-based availability logic.", { min: 0, max: 100, step: 1 });
    const progression = numberField("Progression", Number(previewContext.progression ?? 0), "Progression context fed to the production generator.", { min: 0, step: 1 });
    type.control.addEventListener("change", () => { previewContext.shopType = type.control.value as ShopType; validatedPolicy = null; renderPreviewPanel(); });
    stage.control.addEventListener("input", () => { previewContext.stage = Number(stage.control.value); validatedPolicy = null; });
    world.control.addEventListener("input", () => { previewContext.worldKey = world.control.value; validatedPolicy = null; });
    luck.control.addEventListener("input", () => { previewContext.luck = Number(luck.control.value); validatedPolicy = null; });
    progression.control.addEventListener("input", () => { previewContext.progression = Number(progression.control.value); validatedPolicy = null; });
    root.append(grid(type.root, stage.root, world.root, luck.root, progression.root));
    const discoveries = el("div", "st-admin-page-actions");
    for (const id of contract.ids.discoveryIds) {
      const control = checkRow(id, (previewContext.discovered ?? []).includes(id), "Simulate this canonical discovery in preview context only.");
      control.control.addEventListener("change", () => { const current = previewContext.discovered ?? []; previewContext.discovered = control.control.checked ? [...new Set([...current, id])] : current.filter((value) => value !== id); validatedPolicy = null; }); discoveries.append(control.root);
    }
    root.append(discoveries, button("Validate Preview", () => { void runPreview(); }, "st-admin-btn primary"));
    if (latestPreview) {
      root.append(notice(`${latestPreview.instance.id} · seed ${latestPreview.instance.seed} · sector ${latestPreview.instance.sectorStart} · ${latestPreview.available ? "AVAILABLE" : "BLOCKED BY AVAILABILITY"}`, latestPreview.available ? "good" : "warn"));
      const table = el("table", "st-admin-table"); const head = el("tr"); for (const label of ["Kind", "Product", "Grade", "Stock", "Price"]) head.append(el("th", undefined, label)); const thead = el("thead"); thead.append(head); table.append(thead); const body = el("tbody");
      for (const stock of latestPreview.instance.stock) { const row = el("tr"); row.append(el("td", undefined, stock.kind), el("td", undefined, stock.itemId ?? stock.definitionId ?? "—"), el("td", undefined, stock.grade ?? "—"), el("td", undefined, String(stock.remaining)), el("td", undefined, formatPrice(stock.price))); body.append(row); }
      table.append(body); const wrap = el("div", "st-admin-table-wrap"); wrap.append(table); root.append(wrap);
    } else root.append(notice("Edit freely, then validate to see the generated Shop instance. Preview does not mutate runtime or revision state.", "info"));
    previewHost.append(root);
  }

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  saveStatus = el("span", undefined, "Load the active Shop policy before saving");
  saveButton = button("Save Draft", () => {
    void (async () => {
      if (!policy || !loadedActiveRevision) return;
      saveButton.disabled = true; publishButton.disabled = true; saveStatus.textContent = "Validating production preview…";
      try {
        const nextPolicy = structuredClone(policy);
        nextPolicy.configRevision = `shop-admin-${Date.now().toString(36)}`;
        const preview = await previewShop(nextPolicy, previewContext);
        const state = await api.getState();
        if (state.state.activeRevision !== loadedActiveRevision) throw new Error(`Active revision changed from ${loadedActiveRevision} to ${state.state.activeRevision}. Reload before saving.`);
        const config = structuredClone(state.active.config) as ShopAwareConfig; config.economy ??= {}; config.economy.shop = nextPolicy;
        const revision = await api.createRevision({ baseRevision: state.active.revision, config, message: `A4.1 Shop policy draft · ${nextPolicy.configRevision}` });
        await api.validateRevision(revision.revision);
        policy = nextPolicy; latestPreview = preview; validatedPolicy = JSON.stringify(policy); baselinePolicy = JSON.stringify(policy); draftRevision = revision.revision;
        refreshBadges(); renderActiveTab(); renderPreviewPanel(); saveStatus.textContent = `Draft ${revision.revision} validated · runtime unchanged`; setAdminStatus(status, "Draft saved and validated. Publish when ready; existing ShopInstance snapshots will not self-reprice.", "success");
      } catch (error: unknown) { saveStatus.textContent = `Draft rejected · ${adminErrorMessage(error, "Shop draft could not be saved.")}`; setAdminStatus(status, saveStatus.textContent, "error"); }
      finally { saveButton.disabled = false; refreshBadges(); }
    })();
  }, "st-admin-btn primary"); saveButton.disabled = true;
  publishButton = button("Publish Draft", () => {
    void (async () => {
      if (!draftRevision || !loadedActiveRevision) return;
      publishButton.disabled = true; saveStatus.textContent = `Validating ${draftRevision} before publish…`;
      try {
        const validation = await api.validateRevision(draftRevision); if (!validation.publishable) throw new Error(`Revision ${draftRevision} is not publishable from the current active revision.`);
        await api.publish(draftRevision, loadedActiveRevision); saveStatus.textContent = `Published ${draftRevision} · applies to new sessions + new Shop instances`; setAdminStatus(status, "Shop policy published. Existing persisted Shop instances keep their original prices/stock; new instances use the new policy.", "success"); load();
      } catch (error: unknown) { saveStatus.textContent = `Publish rejected · ${adminErrorMessage(error, "Shop draft could not be published.")}`; setAdminStatus(status, saveStatus.textContent, "error"); publishButton.disabled = false; }
    })();
  }); publishButton.disabled = true;
  saveBar.append(el("strong", undefined, "A4.1 Shop Draft"), saveStatus, el("div", "grow"), button("Discard", () => load()), button("History", () => navigate("/admin/space-typing/history")), publishButton, saveButton); page.append(saveBar);

  const renderTabs = (): void => {
    tabs.replaceChildren(); if (!manifest) return;
    for (const tab of manifest.tabs) { const control = button(tab, () => { activeTab = tab; renderTabs(); renderActiveTab(); }, activeTab === tab ? "st-admin-btn primary" : "st-admin-btn"); control.setAttribute("role", "tab"); control.setAttribute("aria-selected", String(activeTab === tab)); tabs.append(control); }
  };

  function load(): void {
    const generation = ++loadGeneration; manifest = null; contract = null; policy = null; bundledPolicy = null; latestPreview = null; validatedPolicy = null; loadedActiveRevision = null; draftRevision = null; tabs.replaceChildren(); content.replaceChildren(notice("Loading Shop Admin contracts…")); previewHost.replaceChildren(); saveButton.disabled = true; publishButton.disabled = true; saveStatus.textContent = "Load the active Shop policy before saving"; revisionBadge.textContent = "ACTIVE · loading"; revisionBadge.className = "st-admin-status info"; setAdminStatus(status, "Loading active revision, Shop contract and bundled production policy…", "loading");
    void Promise.all([fetchShopManifest(), fetchShopContract(), api.getState(), previewShop(undefined)]).then(async ([nextManifest, nextContract, state, bundled]) => {
      if (generation !== loadGeneration) return;
      if (!nextManifest.authoring.enabled || !nextManifest.preview.available) throw new Error("Pinned child Shop contract has not opened canonical authoring + preview.");
      manifest = nextManifest; contract = nextContract; bundledPolicy = structuredClone(bundled.policy); loadedActiveRevision = state.state.activeRevision;
      const activePolicy = (state.active.config as ShopAwareConfig).economy?.shop; policy = structuredClone(activePolicy ?? bundled.policy); selectedShopType = nextContract.ids.shopTypes[0] ?? "normal"; selectedGrade = nextContract.ids.gradeIds[0] ?? "aluminum"; selectedOfferId = nextContract.ids.itemIds[0] ?? ""; previewContext.shopType = selectedShopType;
      const effective = await previewShop(policy, previewContext); if (generation !== loadGeneration) return; latestPreview = effective; validatedPolicy = JSON.stringify(policy); baselinePolicy = JSON.stringify(policy);
      revisionBadge.textContent = `ACTIVE · ${state.state.activeRevision}`; revisionBadge.className = "st-admin-status good"; saveButton.disabled = false; saveStatus.textContent = activePolicy ? `Active ${policy.configRevision} · revision-backed` : "Bundled defaults loaded · first Save Draft will initialize economy.shop";
      renderTabs(); renderActiveTab(); renderPreviewPanel(); refreshBadges(); setAdminStatus(status, `Child ${nextManifest.auditedChildSha.slice(0, 12)} · authoring ${nextManifest.authoring.sections.join(" / ")} · apply ${nextManifest.authoring.applyBoundary}.`, activePolicy ? "success" : "warning");
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return; saveButton.disabled = true; publishButton.disabled = true; revisionBadge.textContent = "ACTIVE · unavailable"; revisionBadge.className = "st-admin-status bad"; tabs.replaceChildren(); previewHost.replaceChildren(); setAdminStatus(status, "Shop Admin service is unavailable.", "error"); renderAdminFailureState(content, { title: "Shop Admin unavailable", fallbackMessage: "The canonical Shop authoring/preview bridge could not be loaded.", error, onRetry: load });
    });
  }

  load(); return page;
}
