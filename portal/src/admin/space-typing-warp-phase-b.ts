import { isContractRecord, readMainAdminContractSection } from "./space-typing-contract-reader";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

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
function minutes(ms: number): string { return `${Math.round(ms / 60_000)} min / Warp`; }
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((entry) => typeof entry === "string"); }
function numberArray(value: unknown): value is number[] { return Array.isArray(value) && value.every((entry) => typeof entry === "number" && Number.isFinite(entry)); }

function validWarpContract(value: unknown): value is WarpContract {
  if (!isContractRecord(value) || value["mode"] !== "runtime-derived-readonly" || typeof value["policyVersion"] !== "string") return false;
  for (const key of ["runtimeSources", "authorableFields", "runtimeDerivedFields", "sourceFunctions", "transactionFunctions", "codeOwnedPolicyFields"] as const) {
    if (!stringArray(value[key])) return false;
  }
  if (!isContractRecord(value["policy"])) return false;
  const policy = value["policy"];
  for (const key of ["activeCap", "reserveCap", "sortieCost", "activeRegenMs", "reserveRegenMs", "refuelAmount", "dailyRefillLimit"] as const) {
    if (typeof policy[key] !== "number" || !Number.isFinite(policy[key])) return false;
  }
  if (!numberArray(policy["refuelPrices"]) || typeof policy["refuelCurrency"] !== "string" || typeof policy["dailyReset"] !== "string") return false;
  return typeof value["persistenceOwner"] === "string" && typeof value["accountStateOwner"] === "string" && typeof value["sortieCostInvariant"] === "string" && typeof value["auditCommand"] === "string";
}

async function fetchWarpContract(): Promise<WarpContract> {
  return readMainAdminContractSection<WarpContract>("warp", "warp.read", validWarpContract);
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
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    content.replaceChildren(notice("Loading canonical Warp policy…", "info"));
    setAdminStatus(status, "Loading canonical Warp contract…", "loading");
    void fetchWarpContract().then((warp) => {
      if (generation !== loadGeneration) return;
      const policy = warp.policy;
      setAdminStatus(status, `${warp.policyVersion} · ${warp.runtimeSources.length} canonical sources · gameplay-only player mutations · Admin writes closed.`, "success");
      content.replaceChildren();

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

      const boundaries = panel("Admin Boundary", "Unavailable authoring is intentional; policy is code-owned and player mutation is gameplay-only");
      boundaries.append(
        listNotice("Code-owned policy fields", warp.codeOwnedPolicyFields, "warn"),
        notice("Authoring unsupported: no canonical Admin persistence/apply consumer exists for WARP_POLICY, so Save Draft / Publish are intentionally unavailable.", "warn"),
        notice("Player mutation unsupported: live Warp balance, reserve consent and refuel transactions are not Admin capabilities.", "warn"),
        notice("Preview unsupported: Admin does not duplicate reconcile/spend/refuel logic or simulate a player wallet.", "info"),
      );

      content.append(capacity, sortie, refuel, ownership, boundaries);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Stamina / Warp contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Stamina / Warp unavailable",
        fallbackMessage: "The canonical Warp contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
