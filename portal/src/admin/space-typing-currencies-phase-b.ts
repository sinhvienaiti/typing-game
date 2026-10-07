import { SpaceTypingAdminApi } from "./api";

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

async function fetchCurrencyManifest(): Promise<CurrencyManifest> {
  const response = await fetch("/api/admin/space-typing/currencies/capabilities", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Record<string, unknown>;
  if (!response.ok) throw new Error(typeof payload["message"] === "string" ? payload["message"] : `Currencies capability request failed (${response.status})`);
  return payload as unknown as CurrencyManifest;
}

function currencyTable(manifest: CurrencyManifest): HTMLElement {
  const root = panel("Runtime Currency Definitions", "Canonical economy IDs and hard limits from the pinned game runtime");
  const table = el("table", "st-admin-table");
  const thead = el("thead"); const hr = el("tr");
  for (const title of ["ID", "Name", "Cap", "Precision"]) hr.append(el("th", undefined, title));
  thead.append(hr); table.append(thead);
  const tbody = el("tbody");
  for (const currency of manifest.currencies) {
    const row = el("tr");
    row.append(
      el("td", undefined, currency.id),
      el("td", undefined, currency.name),
      el("td", undefined, currency.cap.toLocaleString()),
      el("td", undefined, String(currency.displayPrecision)),
    );
    tbody.append(row);
  }
  table.append(tbody); root.append(table); return root;
}

function fieldTable(manifest: CurrencyManifest): HTMLElement {
  const root = panel("Master-plan Field Contract", "Unsupported metadata remains explicit instead of becoming fake configuration");
  const table = el("table", "st-admin-table");
  const thead = el("thead"); const hr = el("tr");
  for (const title of ["Field", "Runtime", "Authoring", "Boundary"]) hr.append(el("th", undefined, title));
  thead.append(hr); table.append(thead);
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
  table.append(tbody); root.append(table); return root;
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
  header.append(copy, actions); page.append(header);

  const status = notice("Loading pinned Currencies runtime contract…"); page.append(status);
  void (async () => {
    try {
      const manifest = await fetchCurrencyManifest();
      status.className = "stx-notice good";
      status.textContent = `Child ${manifest.auditedChildSha.slice(0, 12)} · ${manifest.currencies.length} runtime currencies · precision ${manifest.runtime.displayPrecision} · writes intentionally closed.`;
      page.append(currencyTable(manifest), fieldTable(manifest));

      const flow = panel("Economy Flow", "Confirmed runtime owners only");
      flow.append(
        notice(`Sources: ${manifest.runtime.sourceFunctions.join(" · ")}`, "good"),
        notice(`Sinks: ${manifest.runtime.sinkFunctions.join(" · ")}`, "good"),
        notice(manifest.authoring.reason, "warn"),
      );
      page.append(flow);

      const analytics = panel("Economy Analytics", "No synthetic Generated / Spent / Net values");
      analytics.append(
        notice(manifest.analytics.reason, "warn"),
        notice(`Unavailable metrics: ${manifest.analytics.unsupportedMetrics.join(" · ")}`, "info"),
      );
      page.append(analytics);

      const evidence = panel("Runtime Evidence", "Pinned child sources");
      evidence.append(
        notice(manifest.runtime.sources.join(" · "), "good"),
        notice(`Canonical IDs: ${manifest.runtime.currencyIds.join(" · ")}`, "info"),
      );
      page.append(evidence);

      const linked = panel("Related Runtime Domains", "Continue through the real source/sink graph");
      const linkedActions = el("div", "st-admin-page-actions");
      for (const domain of manifest.linkedRuntimeDomains) linkedActions.append(button(`${domain.label} · inspect`, () => navigate(domain.route)));
      linked.append(notice(manifest.linkedRuntimeDomains.map((entry) => `${entry.label}: ${entry.relationship}`).join(" · "), "info"), linkedActions);
      page.append(linked);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Currencies contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
