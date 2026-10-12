import { isContractRecord, readMainAdminContractSection } from "./space-typing-contract-reader";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type RewardsContract = {
  mode: "runtime-derived-readonly";
  runtimeSources: string[];
  domains: string[];
  authorableFields: string[];
  runtimeDerivedFields: string[];
  performanceRewardIds: string[];
  campaignFunctions: string[];
  combatCredit: {
    modes: string[];
    walletPolicies: Record<string, "real" | "simulated" | "disabled">;
    causes: string[];
    tiers: string[];
    variants: string[];
    sourceFunctions: string[];
    canonicalWalletCommitRequiredForRealModes: boolean;
  };
  equipmentLoot: {
    sources: string[];
    gradeIds: string[];
    equipmentTiers: number[];
    weightTables: string[];
    sourceFunctions: string[];
    mutationHook: string;
  };
  pity: {
    keys: string[];
    counterRange: { min: number; max: number; integer: boolean };
    sourceFunctions: string[];
    mutationHook: string;
  };
  gameplayConsumer: string;
  codeOwnedPolicyFields: string[];
  writeCapability: false;
  previewCapability: false;
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
function listNotice(label: string, values: Array<string | number>, tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.length ? values.join(" · ") : "none exposed"}`, tone);
}
function tableWrap(table: HTMLElement): HTMLElement {
  const wrap = el("div", "st-admin-table-wrap");
  wrap.append(table);
  return wrap;
}
function stringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}
function numberArray(value: unknown): value is number[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "number" && Number.isFinite(entry));
}

function validRewardsContract(value: unknown): value is RewardsContract {
  if (!isContractRecord(value) || value["mode"] !== "runtime-derived-readonly") return false;
  for (const key of ["runtimeSources", "domains", "authorableFields", "runtimeDerivedFields", "performanceRewardIds", "campaignFunctions", "codeOwnedPolicyFields"] as const) {
    if (!stringArray(value[key])) return false;
  }
  if (!isContractRecord(value["combatCredit"]) || !isContractRecord(value["equipmentLoot"]) || !isContractRecord(value["pity"])) return false;
  const credit = value["combatCredit"];
  if (!stringArray(credit["modes"]) || !isContractRecord(credit["walletPolicies"]) || !stringArray(credit["causes"]) || !stringArray(credit["tiers"]) || !stringArray(credit["variants"]) || !stringArray(credit["sourceFunctions"])) return false;
  const loot = value["equipmentLoot"];
  if (!stringArray(loot["sources"]) || !stringArray(loot["gradeIds"]) || !numberArray(loot["equipmentTiers"]) || !stringArray(loot["weightTables"]) || !stringArray(loot["sourceFunctions"]) || typeof loot["mutationHook"] !== "string") return false;
  const pity = value["pity"];
  if (!stringArray(pity["keys"]) || !isContractRecord(pity["counterRange"]) || !stringArray(pity["sourceFunctions"]) || typeof pity["mutationHook"] !== "string") return false;
  return typeof value["gameplayConsumer"] === "string";
}

async function fetchRewardsContract(): Promise<RewardsContract> {
  return readMainAdminContractSection<RewardsContract>("rewards", "rewards.read", validRewardsContract);
}

function walletPolicyTable(rewards: RewardsContract): HTMLElement {
  const root = panel("Combat Credits", "Gameplay-mode wallet policy and canonical drop tiers");
  const table = el("table", "st-admin-table");
  const thead = el("thead");
  const headerRow = el("tr");
  for (const title of ["Mode", "Wallet policy", "Production balance"]) headerRow.append(el("th", undefined, title));
  thead.append(headerRow);
  table.append(thead);
  const tbody = el("tbody");
  for (const mode of rewards.combatCredit.modes) {
    const policy = rewards.combatCredit.walletPolicies[mode] ?? "disabled";
    const row = el("tr");
    row.append(
      el("td", undefined, mode),
      el("td", undefined, policy),
      el("td", undefined, policy === "real" ? "Canonical wallet commit required" : policy === "simulated" ? "Simulation only" : "No reward mutation"),
    );
    tbody.append(row);
  }
  table.append(tbody);
  root.append(
    tableWrap(table),
    listNotice("Kill causes", rewards.combatCredit.causes, "good"),
    listNotice("Crystal tiers", rewards.combatCredit.tiers),
    listNotice("Variants", rewards.combatCredit.variants),
    listNotice("Runtime functions", rewards.combatCredit.sourceFunctions),
  );
  return root;
}

export function renderPhaseBRewards(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Economy · Runtime Contract"),
    el("h1", undefined, "Rewards & Drops"),
    el("p", undefined, "Inspect campaign rewards, combat Credits, equipment loot and pity from the canonical Space Typing runtime. Tuning stays source-owned until gameplay exposes a real authoring/apply seam."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Currencies", () => navigate("/admin/space-typing/currencies")),
    button("Stamina / Warp", () => navigate("/admin/space-typing/warp")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Rewards & Drops contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    content.replaceChildren(notice("Loading runtime reward ownership…", "info"));
    setAdminStatus(status, "Loading canonical Rewards & Drops contract…", "loading");
    void fetchRewardsContract().then((rewards) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, `${rewards.domains.length} runtime domains · ${rewards.runtimeSources.length} canonical sources · writes and Admin preview intentionally closed.`, "success");
      content.replaceChildren();

      const campaign = panel("Campaign Rewards", "Performance badges and sector checkpoint formula owners");
      campaign.append(
        listNotice("Performance reward IDs", rewards.performanceRewardIds, "good"),
        listNotice("Runtime functions", rewards.campaignFunctions),
      );
      content.append(campaign, walletPolicyTable(rewards));

      const loot = panel("Equipment Loot", "Real drop sources, rarity grades, equipment tiers and mutation hook");
      loot.append(
        listNotice("Sources", rewards.equipmentLoot.sources, "good"),
        listNotice("Grades", rewards.equipmentLoot.gradeIds),
        listNotice("Equipment tiers", rewards.equipmentLoot.equipmentTiers),
        listNotice("Code-owned weight tables", rewards.equipmentLoot.weightTables, "warn"),
        listNotice("Runtime functions", rewards.equipmentLoot.sourceFunctions),
        notice(`Gameplay mutation hook: ${rewards.equipmentLoot.mutationHook}`, "good"),
      );
      content.append(loot);

      const pity = panel("Luck Pity", "Persisted gameplay counters are visible, but formula tuning is not an Admin authoring seam");
      pity.append(
        listNotice("Pity keys", rewards.pity.keys, "good"),
        notice(`Counter range: ${String(rewards.pity.counterRange.min)}–${String(rewards.pity.counterRange.max)}${rewards.pity.counterRange.integer ? " · integer" : ""}`),
        listNotice("Runtime functions", rewards.pity.sourceFunctions),
        notice(`Gameplay mutation hook: ${rewards.pity.mutationHook}`, "good"),
      );
      content.append(pity);

      const ownership = panel("Runtime Ownership", "Unavailable authoring is intentional; Admin does not clone reward RNG or formulas");
      ownership.append(
        notice(`Gameplay consumer: ${rewards.gameplayConsumer}`, "good"),
        listNotice("Canonical sources", rewards.runtimeSources),
        listNotice("Code-owned policy fields", rewards.codeOwnedPolicyFields, "warn"),
        notice("Authoring unsupported: the current reward/drop formulas are source-owned and no canonical Admin persistence/apply consumer exists yet.", "warn"),
        notice("Preview unsupported: existing gameplay/test simulation is not promoted into a second Admin reward calculator.", "info"),
      );
      content.append(ownership);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Rewards & Drops contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Rewards & Drops unavailable",
        fallbackMessage: "The canonical Rewards & Drops contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
