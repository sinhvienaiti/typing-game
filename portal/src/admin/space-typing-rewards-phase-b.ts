import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
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
type AdminContract = {
  capabilities: string[];
  rewards: RewardsContract;
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function button(label: string, onClick: () => void, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label); node.type = "button"; node.addEventListener("click", onClick); return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div"); copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy); root.append(head); return root;
}
function listNotice(label: string, values: Array<string | number>, tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.join(" · ")}`, tone);
}

async function fetchRewardsContract(): Promise<RewardsContract> {
  const response = await fetch("/api/admin/space-typing/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<AdminContract> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Rewards contract request failed (${response.status})`);
  if (!payload.rewards || !payload.capabilities?.includes("rewards.read")) throw new Error("Pinned child contract does not expose rewards.read.");
  return payload.rewards;
}

function walletPolicyTable(rewards: RewardsContract): HTMLElement {
  const root = panel("Combat Credits", "Gameplay-mode wallet policy and canonical drop tiers");
  const table = el("table", "st-admin-table");
  const thead = el("thead"); const hr = el("tr");
  for (const title of ["Mode", "Wallet policy", "Production balance"]) hr.append(el("th", undefined, title));
  thead.append(hr); table.append(thead);
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
    table,
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
    el("p", undefined, "Inspect campaign rewards, combat Credits, equipment loot and luck pity from the canonical Space Typing runtime. Code-owned tuning stays locked until gameplay exposes a real authoring/apply seam."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Currencies", () => navigate("/admin/space-typing/currencies")),
    button("Stamina / Warp", () => navigate("/admin/space-typing/warp")),
  );
  header.append(copy, actions); page.append(header);

  const status = notice("Loading canonical Rewards & Drops contract…"); page.append(status);
  void (async () => {
    try {
      const rewards = await fetchRewardsContract();
      status.className = "stx-notice good";
      status.textContent = `${rewards.domains.length} runtime domains · ${rewards.runtimeSources.length} canonical sources · writes and Admin preview intentionally closed.`;

      const campaign = panel("Campaign Rewards", "Performance badges and sector checkpoint formula owners");
      campaign.append(
        listNotice("Performance reward IDs", rewards.performanceRewardIds, "good"),
        listNotice("Runtime functions", rewards.campaignFunctions),
      );
      page.append(campaign, walletPolicyTable(rewards));

      const loot = panel("Equipment Loot", "Real drop sources, rarity grades, equipment tiers and mutation hook");
      loot.append(
        listNotice("Sources", rewards.equipmentLoot.sources, "good"),
        listNotice("Grades", rewards.equipmentLoot.gradeIds),
        listNotice("Equipment tiers", rewards.equipmentLoot.equipmentTiers),
        listNotice("Code-owned weight tables", rewards.equipmentLoot.weightTables, "warn"),
        listNotice("Runtime functions", rewards.equipmentLoot.sourceFunctions),
        notice(`Gameplay mutation hook: ${rewards.equipmentLoot.mutationHook}`, "good"),
      );
      page.append(loot);

      const pity = panel("Luck Pity", "Persisted gameplay counters are visible, but their tuning formula is not an Admin authoring seam");
      pity.append(
        listNotice("Pity keys", rewards.pity.keys, "good"),
        notice(`Counter range: ${rewards.pity.counterRange.min}–${rewards.pity.counterRange.max}${rewards.pity.counterRange.integer ? " · integer" : ""}`),
        listNotice("Runtime functions", rewards.pity.sourceFunctions),
        notice(`Gameplay mutation hook: ${rewards.pity.mutationHook}`, "good"),
      );
      page.append(pity);

      const ownership = panel("Runtime Ownership", "No parallel reward calculator or synthetic preview exists in Admin");
      ownership.append(
        notice(`Gameplay consumer: ${rewards.gameplayConsumer}`, "good"),
        listNotice("Canonical sources", rewards.runtimeSources),
        listNotice("Code-owned policy fields", rewards.codeOwnedPolicyFields, "warn"),
        notice("Authoring unsupported: the current reward/drop formulas are source-owned and no canonical Admin persistence/apply consumer exists yet.", "warn"),
        notice("Preview unsupported: Admin does not clone reward RNG/formulas. Existing gameplay/test simulation is not promoted into an authoring preview contract.", "info"),
      );
      page.append(ownership);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Rewards & Drops contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
