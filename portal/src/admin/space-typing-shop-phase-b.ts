import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type ShopField = { name: string; runtimeBacked: boolean; source: "runtime-derived" | "unsupported"; authorable: false; reason: string };
type ShopManifest = {
  protocolVersion: 2;
  mode: "runtime-backed-readonly";
  owner: string;
  auditedChildSha: string;
  tabs: string[];
  fields: ShopField[];
  capabilities: Record<string, boolean>;
  runtime: {
    sources: string[];
    shopTypes: string[];
    currencies: string[];
    stockKinds: string[];
    transactionReasons: string[];
    refreshBoundary: string;
    persistenceOwner: string;
  };
  evidence: Array<{ id: string; found: boolean; detail: string }>;
  linkedRuntimeDomains: Array<{ id: string; label: string; route: string; relationship: string }>;
  authoring: { enabled: false; applyBoundary: "none"; persistence: "child-runtime-state"; reason: string };
  preview: { available: false; reason: string };
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
  head.append(copy); root.append(head); return root;
}

async function fetchShopManifest(): Promise<ShopManifest> {
  const response = await fetch("/api/admin/space-typing/shop/capabilities", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Record<string, unknown>;
  if (!response.ok) throw new Error(typeof payload["message"] === "string" ? payload["message"] : `Shop capability request failed (${response.status})`);
  return payload as unknown as ShopManifest;
}

function fieldTable(manifest: ShopManifest): HTMLElement {
  const root = panel("Item Config Contract", "15 master-plan fields mapped to the current gameplay runtime");
  const table = el("table", "st-admin-table");
  const thead = el("thead"); const hr = el("tr");
  for (const title of ["Field", "Runtime source", "Authoring", "Boundary"]) hr.append(el("th", undefined, title));
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

function renderTab(host: HTMLElement, tab: string, manifest: ShopManifest) {
  host.replaceChildren();
  if (tab === "Catalog") {
    const summary = panel("Runtime Catalog", "Game-owned generation and transactions; Admin is a reference/control-plane view only");
    summary.append(
      notice(`Shop types: ${manifest.runtime.shopTypes.join(" · ")}`, "good"),
      notice(`Currencies: ${manifest.runtime.currencies.join(" · ")}`, "good"),
      notice(`Stock: ${manifest.runtime.stockKinds.join(" + ")} · refresh ${manifest.runtime.refreshBoundary} · persistence ${manifest.runtime.persistenceOwner}`, "info"),
      notice(manifest.authoring.reason, "warn"),
    );
    host.append(summary, fieldTable(manifest));
    return;
  }

  const scope = panel(`${tab} · Capability`, "Master-plan tab retained, but only runtime-native behavior is claimed");
  if (tab === "Featured") {
    scope.append(notice("The current Shop generator has no Featured flag or featured rotation. This tab is intentionally non-authorable.", "warn"));
  } else if (tab === "Daily" || tab === "Weekly") {
    scope.append(notice(`The runtime has sector-instance stock, not ${tab.toLowerCase()} reset/limit semantics. No schedule is fabricated in Admin.`, "warn"));
  } else if (tab === "Bundles") {
    scope.append(notice("The current transaction model buys one stock entry at a time; no native bundle entity exists.", "warn"));
  } else if (tab === "History") {
    scope.append(notice("Shop state stores remaining stock, not a canonical purchase ledger. Admin revision history is not presented as transaction history.", "warn"));
  }
  host.append(scope);
}

export function renderPhaseBShop(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Economy · Runtime Contract"),
    el("h1", undefined, "Shop"),
    el("p", undefined, "Inspect the real Space Typing Shop transaction model without creating a second pricing/catalog source of truth."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), button("Currencies", () => navigate("/admin/space-typing/currencies")), button("History", () => navigate("/admin/space-typing/history")));
  header.append(copy, actions); page.append(header);

  const status = notice("Loading pinned Shop runtime contract…");
  const tabBar = el("div", "st-admin-page-actions");
  const content = el("div");
  page.append(status, tabBar, content);

  void (async () => {
    try {
      const manifest = await fetchShopManifest();
      const runtimeCount = manifest.fields.filter((field) => field.runtimeBacked).length;
      const unsupportedCount = manifest.fields.length - runtimeCount;
      status.className = "stx-notice good";
      status.textContent = `Child ${manifest.auditedChildSha.slice(0, 12)} · ${runtimeCount} runtime-derived fields · ${unsupportedCount} unsupported fields · writes intentionally closed.`;
      let activeTab = manifest.tabs[0] ?? "Catalog";
      const renderTabs = () => {
        tabBar.replaceChildren();
        for (const tab of manifest.tabs) {
          tabBar.append(button(tab, () => { activeTab = tab; renderTabs(); renderTab(content, activeTab, manifest); }, activeTab === tab ? "st-admin-btn primary" : "st-admin-btn"));
        }
      };
      renderTabs(); renderTab(content, activeTab, manifest);

      const capabilities = panel("Runtime Capabilities", "Positive evidence is shown only where the pinned game actually owns the behavior");
      for (const [name, enabled] of Object.entries(manifest.capabilities)) {
        capabilities.append(notice(`${name}: ${enabled ? "available" : "not exposed"}`, enabled ? "good" : "info"));
      }
      const evidence = panel("Runtime Evidence", manifest.runtime.sources.join(" · "));
      for (const item of manifest.evidence) evidence.append(notice(`${item.id}: ${item.found ? "FOUND" : "not exposed"} · ${item.detail}`, item.found ? "good" : "info"));
      const linked = panel("Related Runtime Domains", "Follow the actual content/economy owners rather than duplicating them in Shop");
      const linkedActions = el("div", "st-admin-page-actions");
      for (const domain of manifest.linkedRuntimeDomains) linkedActions.append(button(`${domain.label} · inspect`, () => navigate(domain.route)));
      linked.append(notice(manifest.linkedRuntimeDomains.map((entry) => `${entry.label}: ${entry.relationship}`).join(" · "), "info"), linkedActions);
      const preview = panel("Shop Preview", "Preview remains closed until the child exports a preview protocol for the same deterministic generator");
      preview.append(notice(manifest.preview.reason, "warn"));
      page.append(capabilities, evidence, linked, preview);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Shop contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();

  return page;
}
