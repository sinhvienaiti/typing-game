import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type WarpContract = {
  mode: "runtime-derived-readonly";
  policyVersion: string;
  runtimeSources: string[];
  authorableFields: string[];
  runtimeDerivedFields: string[];
  policy: {
    activeCap: number;
    reserveCap: number;
    sortieCost: number;
    activeRegenMs: number;
    reserveRegenMs: number;
    refuelAmount: number;
    refuelPrices: number[];
    refuelCurrency: string;
    dailyRefillLimit: number;
    dailyReset: string;
  };
  sourceFunctions: string[];
  transactionFunctions: string[];
  persistenceOwner: string;
  accountStateOwner: string;
  sortieCostInvariant: string;
  auditCommand: string;
  codeOwnedPolicyFields: string[];
  playerMutationCapability: "gameplay-only";
  writeCapability: false;
  previewCapability: false;
};
type AdminContract = { capabilities: string[]; warp: WarpContract };

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
  return notice(`${label}: ${values.join(" · ")}`, tone);
}
function minutes(ms: number): string {
  return `${Math.round(ms / 60_000)} min / Warp`;
}
async function fetchWarpContract(): Promise<WarpContract> {
  const response = await fetch("/api/admin/space-typing/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<AdminContract> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Warp contract request failed (${response.status})`);
  if (!payload.warp || !payload.capabilities?.includes("warp.read")) throw new Error("Pinned child contract does not expose warp.read.");
  return payload.warp;
}

export function renderPhaseBWarp(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Economy · Runtime Contract"),
    el("h1", undefined, "Stamina / Warp"),
    el("p", undefined, "Inspect the canonical Warp stamina policy and persistence ownership. Player balances, reserve consent and refuels remain gameplay transactions; policy tuning stays source-owned until a real Admin authoring/apply seam exists."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Rewards & Drops", () => navigate("/admin/space-typing/rewards")),
    button("Missions", () => navigate("/admin/space-typing/missions")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Warp contract…");
  page.append(status);
  void (async () => {
    try {
      const warp = await fetchWarpContract();
      const policy = warp.policy;
      status.className = "stx-notice good";
      status.textContent = `${warp.policyVersion} · ${warp.runtimeSources.length} canonical sources · gameplay-only player mutations · Admin writes closed.`;

      const capacity = panel("Capacity & Regeneration", "Canonical WARP_POLICY values used by gameplay");
      capacity.append(
        notice(`Active capacity: ${policy.activeCap} Warp`, "good"),
        notice(`Reserve capacity: ${policy.reserveCap} Warp`, "good"),
        notice(`Active regeneration: ${minutes(policy.activeRegenMs)}`),
        notice(`Reserve regeneration: ${minutes(policy.reserveRegenMs)}`),
        notice(`Policy version: ${warp.policyVersion}`),
      );

      const sortie = panel("Sortie Admission", "Warp spending is owned by the canonical account transaction path");
      sortie.append(
        notice(`Sortie cost: ${policy.sortieCost} Warp`, "good"),
        notice(`Invariant: ${warp.sortieCostInvariant}`),
        notice(`Account state owner: ${warp.accountStateOwner}`),
        notice("Reserve consent and sortie spending are gameplay/player-state operations. Admin exposes no spend or consent action.", "warn"),
      );

      const refuel = panel("Refuel Policy", "Reference values only — this screen cannot mutate a player wallet");
      refuel.append(
        notice(`Refuel amount: +${policy.refuelAmount} Warp`, "good"),
        listNotice(`Prices (${policy.refuelCurrency})`, policy.refuelPrices),
        notice(`Daily refill limit: ${policy.dailyRefillLimit}`),
        notice(`Daily reset: ${policy.dailyReset}`),
        notice("Refuel execution remains in the gameplay account transaction, where Star Crystal spending and quote validation are applied atomically.", "warn"),
      );

      const ownership = panel("Canonical State & Ownership", "Admin reads the runtime contract instead of cloning stamina logic");
      ownership.append(
        notice(`Persistence owner: ${warp.persistenceOwner}`, "good"),
        listNotice("Persisted/runtime fields", warp.runtimeDerivedFields),
        listNotice("Warp functions", warp.sourceFunctions),
        listNotice("Account transaction functions", warp.transactionFunctions),
        listNotice("Canonical sources", warp.runtimeSources),
        notice(`Runtime audit: ${warp.auditCommand}`, "good"),
      );

      const boundaries = panel("Admin Boundary", "Policy is code-owned and player mutation is gameplay-only");
      boundaries.append(
        listNotice("Code-owned policy fields", warp.codeOwnedPolicyFields, "warn"),
        notice("Authoring unsupported: no canonical Admin persistence/apply consumer exists for WARP_POLICY, so Save Draft / Publish are intentionally unavailable.", "warn"),
        notice("Player mutation unsupported: live Warp balance, reserve consent and refuel transactions are not Admin capabilities.", "warn"),
        notice("Preview unsupported: Admin does not duplicate reconcile/spend/refuel logic or simulate a player wallet.", "info"),
      );

      page.append(capacity, sortie, refuel, ownership, boundaries);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Stamina / Warp contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
