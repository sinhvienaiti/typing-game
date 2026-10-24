import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type CurrencyField = { name: string; runtimeBacked: boolean; source: "runtime-derived" | "unsupported"; authorable: false; reason: string };
type CurrencyRow = { id: string; name: string; cap: number; displayPrecision: number; icon: null; color: null; enabled: null };
type CurrencyManifest = {
  protocolVersion: 1;
  mode: "runtime-backed-readonly";
  owner: string;
  auditedChildSha: string;
  fields: CurrencyField[];
  currencies: CurrencyRow[];
  capabilities: Record<string, boolean>;
  runtime: { sources: string[]; currencyIds: string[]; sourceFunctions: string[]; sinkFunctions: string[]; cap: number; displayPrecision: number };
  analytics: { available: false; reason: string; unsupportedMetrics: string[] };
  authoring: { enabled: false; reason: string };
  linkedRuntimeDomains: Array<{ id: string; label: string; route: string; relationship: string }>;
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
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function tableWrap(table: HTMLElement): HTMLElement {
  const wrap = el("div", "st-admin-table-wrap");
  wrap.append(table);
  return wrap;
}

function validateCurrencyManifest(value: unknown): CurrencyManifest {
  if (!isRecord(value) || value["protocolVersion"] !== 1 || value["mode"] !== "runtime-backed-readonly") {
    throw new Error("Currencies capability response does not match the canonical runtime-backed read-only contract.");
  }
  if (
    typeof value["owner"] !== "string" ||
    typeof value["auditedChildSha"] !== "string" ||
    !Array.isArray(value["fields"]) ||
    !Array.isArray(value["currencies"]) ||
    !isRecord(value["capabilities"]) ||
    !isRecord(value["runtime"]) ||
    !isRecord(value["analytics"]) ||
    !isRecord(value["authoring"]) ||
    !Array.isArray(value["linkedRuntimeDomains"])
  ) {
    throw new Error("Currencies capability response is missing required runtime contract sections.");
  }
  const runtime = value["runtime"];
  for (const key of ["sources", "currencyIds", "sourceFunctions", "sinkFunctions"] as const) {
    if (!Array.isArray(runtime[key])) throw new Error(`Currencies capability response is missing runtime.${key}.`);
  }
  if (typeof runtime["cap"] !== "number" || typeof runtime["displayPrecision"] !== "number") {
    throw new Error("Currencies capability response is missing numeric runtime limits.");
  }
  const analytics = value["analytics"];
  if (typeof analytics["reason"] !== "string" || !Array.isArray(analytics["unsupportedMetrics"])) {
    throw new Error("Currencies capability response is missing analytics boundary metadata.");
  }
  return value as unknown as CurrencyManifest;
}

async function fetchCurrencyManifest(): Promise<CurrencyManifest> {
  const payload = await api.requestJson<unknown>("/api/admin/space-typing/currencies/capabilities");
  return validateCurrencyManifest(payload);
}

function currencyTable(manifest: CurrencyManifest): HTMLElement {
  const root = panel("Runtime Currency Definitions", "Canonical economy IDs and hard limits from the pinned game runtime");
  if (manifest.currencies.length === 0) {
    root.append(notice("The canonical runtime returned no currency definitions.", "info"));
    return root;
  }
  const table = el("table", "st-admin-table");
  const thead = el("thead");
  const headerRow = el("tr");
  for (const title of ["ID", "Name", "Cap", "Precision"]) headerRow.append(el("th", undefined, title));
  thead.append(headerRow);
  table.append(thead);
  const tbody = el("tbody");
  for (const currency of manifest.currencies) {
    const row = el("tr");
    row.append(
      el("td", undefined, currency.id),
      el("td", undefined, currency.name),
      el("td", undefined, Number.isFinite(currency.cap) ? currency.cap.toLocaleString() : "—"),
      el("td", undefined, Number.isFinite(currency.displayPrecision) ? String(currency.displayPrecision) : "—"),
    );
    tbody.append(row);
  }
  table.append(tbody);
  root.append(tableWrap(table));
  return root;
}

function fieldTable(manifest: CurrencyManifest): HTMLElement {
  const root = panel("Master-plan Field Contract", "Unsupported metadata remains explicit instead of becoming fake configuration");
  if (manifest.fields.length === 0) {
    root.append(notice("No field contract entries were returned.", "info"));
    return root;
  }
  const table = el("table", "st-admin-table");
  const thead = el("thead");
  const headerRow = el("tr");
  for (const title of ["Field", "Runtime", "Authoring", "Boundary"]) headerRow.append(el("th", undefined, title));
  thead.append(headerRow);
  table.append(thead);
  const tbody = el("tbody");
  for (const field of manifest.fields) {
    const row = el("tr");
    row.append(
      el("td", undefined, field.name),
      el("td", undefined, field.runtimeBacked ? "Derived by game" : "Not implemented"),
      el("td", undefined, "Locked"),
      el("td", undefined, field.reason),
    );
    tbody.append(row);
  }
  table.append(tbody);
  root.append(tableWrap(table));
  return root;
}

export function renderPhaseBCurrencies(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Economy · Runtime Contract"),
    el("h1", undefined, "Currencies"),
    el("p", undefined, "Inspect canonical Space Typing currencies, caps, sources and sinks without mutating player balances or inventing economy metadata."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Shop", () => navigate("/admin/space-typing/shop")),
    button("Rewards & Drops", () => navigate("/admin/space-typing/rewards")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading pinned Currencies runtime contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    content.replaceChildren(notice("Loading canonical currency definitions…", "info"));
    setAdminStatus(status, "Loading pinned Currencies runtime contract…", "loading");

    void fetchCurrencyManifest().then((manifest) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(
        status,
        `Child ${manifest.auditedChildSha.slice(0, 12)} · ${manifest.currencies.length} runtime currencies · precision ${manifest.runtime.displayPrecision} · writes intentionally closed.`,
        "success",
      );
      content.replaceChildren(currencyTable(manifest), fieldTable(manifest));

      const flow = panel("Economy Flow", "Confirmed runtime owners only");
      flow.append(
        notice(`Sources: ${manifest.runtime.sourceFunctions.join(" · ") || "none exposed"}`, "good"),
        notice(`Sinks: ${manifest.runtime.sinkFunctions.join(" · ") || "none exposed"}`, "good"),
        notice(manifest.authoring.reason, "warn"),
      );
      content.append(flow);

      const analytics = panel("Economy Analytics", "Unavailable analytics are shown as an intentional product boundary, not fabricated numbers");
      analytics.append(
        notice(manifest.analytics.reason, "warn"),
        notice(`Unavailable metrics: ${manifest.analytics.unsupportedMetrics.join(" · ") || "none listed"}`, "info"),
      );
      content.append(analytics);

      const evidence = panel("Runtime Evidence", "Pinned child sources");
      evidence.append(
        notice(manifest.runtime.sources.join(" · ") || "No source paths were returned", "good"),
        notice(`Canonical IDs: ${manifest.runtime.currencyIds.join(" · ") || "none returned"}`, "info"),
      );
      content.append(evidence);

      const linked = panel("Related Runtime Domains", "Continue through the real source/sink graph");
      const linkedActions = el("div", "st-admin-page-actions");
      for (const domain of manifest.linkedRuntimeDomains) linkedActions.append(button(`${domain.label} · inspect`, () => navigate(domain.route)));
      linked.append(
        notice(manifest.linkedRuntimeDomains.map((entry) => `${entry.label}: ${entry.relationship}`).join(" · ") || "No linked domains were returned.", "info"),
        linkedActions,
      );
      content.append(linked);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Currencies runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Currencies contract unavailable",
        fallbackMessage: "The canonical Currencies runtime contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
