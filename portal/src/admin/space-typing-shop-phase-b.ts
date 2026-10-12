import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

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
  head.append(copy);
  root.append(head);
  return root;
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function validateShopManifest(value: unknown): ShopManifest {
  if (!isRecord(value) || value["protocolVersion"] !== 2 || value["mode"] !== "runtime-backed-readonly") {
    throw new Error("Shop capability response does not match the canonical runtime-backed read-only contract.");
  }
  if (
    typeof value["owner"] !== "string" ||
    typeof value["auditedChildSha"] !== "string" ||
    !Array.isArray(value["tabs"]) ||
    !Array.isArray(value["fields"]) ||
    !isRecord(value["capabilities"]) ||
    !isRecord(value["runtime"]) ||
    !Array.isArray(value["evidence"]) ||
    !Array.isArray(value["linkedRuntimeDomains"]) ||
    !isRecord(value["authoring"]) ||
    !isRecord(value["preview"])
  ) {
    throw new Error("Shop capability response is missing required runtime contract sections.");
  }
  const runtime = value["runtime"];
  for (const key of ["sources", "shopTypes", "currencies", "stockKinds", "transactionReasons"] as const) {
    if (!Array.isArray(runtime[key])) throw new Error(`Shop capability response is missing runtime.${key}.`);
  }
  if (typeof runtime["refreshBoundary"] !== "string" || typeof runtime["persistenceOwner"] !== "string") {
    throw new Error("Shop capability response is missing runtime ownership metadata.");
  }
  return value as unknown as ShopManifest;
}

async function fetchShopManifest(): Promise<ShopManifest> {
  const payload = await api.requestJson<unknown>("/api/admin/space-typing/shop/capabilities");
  return validateShopManifest(payload);
}

function tableWrap(table: HTMLElement): HTMLElement {
  const wrap = el("div", "st-admin-table-wrap");
  wrap.append(table);
  return wrap;
}

function fieldTable(manifest: ShopManifest): HTMLElement {
  const root = panel("Item Config Contract", "Master-plan fields mapped to the current gameplay runtime");
  const table = el("table", "st-admin-table");
  const thead = el("thead");
  const headerRow = el("tr");
  for (const title of ["Field", "Runtime source", "Authoring", "Boundary"]) headerRow.append(el("th", undefined, title));
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

function renderTab(host: HTMLElement, tab: string, manifest: ShopManifest): void {
  host.replaceChildren();
  if (tab === "Catalog") {
    const summary = panel("Runtime Catalog", "Game-owned generation and transactions; Admin is a reference/control-plane view only");
    summary.append(
      notice(`Shop types: ${manifest.runtime.shopTypes.join(" · ") || "none exposed"}`, "good"),
      notice(`Currencies: ${manifest.runtime.currencies.join(" · ") || "none exposed"}`, "good"),
      notice(`Stock: ${manifest.runtime.stockKinds.join(" + ") || "none exposed"} · refresh ${manifest.runtime.refreshBoundary} · persistence ${manifest.runtime.persistenceOwner}`, "info"),
      notice(manifest.authoring.reason, "warn"),
    );
    host.append(summary, fieldTable(manifest));
    return;
  }

  const scope = panel(`${tab} · Capability`, "This tab documents the verified runtime boundary; unavailable authoring is intentional, not a failed service state");
  if (tab === "Featured") {
    scope.append(notice("The current Shop generator has no Featured flag or featured rotation. This tab is intentionally non-authorable.", "warn"));
  } else if (tab === "Daily" || tab === "Weekly") {
    scope.append(notice(`The runtime has sector-instance stock, not ${tab.toLowerCase()} reset/limit semantics. No schedule is fabricated in Admin.`, "warn"));
  } else if (tab === "Bundles") {
    scope.append(notice("The current transaction model buys one stock entry at a time; no native bundle entity exists.", "warn"));
  } else if (tab === "History") {
    scope.append(notice("Shop state stores remaining stock, not a canonical purchase ledger. Admin revision history is not presented as transaction history.", "warn"));
  } else {
    scope.append(notice("This capability has no separate canonical authoring model in the pinned runtime.", "info"));
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
    el("p", undefined, "Inspect the real Space Typing Shop transaction model, runtime stock and economy boundaries without creating a second pricing or catalog source of truth."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Currencies", () => navigate("/admin/space-typing/currencies")),
    button("History", () => navigate("/admin/space-typing/history")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading pinned Shop runtime contract…");
  status.setAttribute("aria-live", "polite");
  const tabBar = el("div", "st-admin-page-actions");
  tabBar.setAttribute("role", "tablist");
  const content = el("div");
  const detailsHost = el("div");
  page.append(status, tabBar, content, detailsHost);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    tabBar.replaceChildren();
    content.replaceChildren(notice("Loading runtime Shop contract…", "info"));
    detailsHost.replaceChildren();
    setAdminStatus(status, "Loading pinned Shop runtime contract…", "loading");

    void fetchShopManifest().then((manifest) => {
      if (generation !== loadGeneration) return;
      const runtimeCount = manifest.fields.filter((field) => field.runtimeBacked).length;
      const unsupportedCount = manifest.fields.length - runtimeCount;
      setAdminStatus(status, `Child ${manifest.auditedChildSha.slice(0, 12)} · ${runtimeCount} runtime-derived fields · ${unsupportedCount} intentionally unsupported fields · writes closed.`, "success");

      const availableTabs = manifest.tabs.length > 0 ? manifest.tabs : ["Catalog"];
      let activeTab = availableTabs[0];
      const renderTabs = (): void => {
        tabBar.replaceChildren();
        for (const tab of availableTabs) {
          const control = button(tab, () => {
            activeTab = tab;
            renderTabs();
            renderTab(content, activeTab, manifest);
          }, activeTab === tab ? "st-admin-btn primary" : "st-admin-btn");
          control.setAttribute("role", "tab");
          control.setAttribute("aria-selected", String(activeTab === tab));
          tabBar.append(control);
        }
      };
      renderTabs();
      renderTab(content, activeTab, manifest);

      const capabilities = panel("Runtime Capabilities", "Positive evidence is shown only where the pinned game actually owns the behavior");
      for (const [name, enabled] of Object.entries(manifest.capabilities)) {
        capabilities.append(notice(`${name}: ${enabled ? "available" : "not exposed"}`, enabled ? "good" : "info"));
      }
      const evidence = panel("Runtime Evidence", manifest.runtime.sources.join(" · ") || "No runtime source paths were returned");
      for (const item of manifest.evidence) {
        evidence.append(notice(`${item.id}: ${item.found ? "FOUND" : "not exposed"} · ${item.detail}`, item.found ? "good" : "info"));
      }
      const linked = panel("Related Runtime Domains", "Follow the real content/economy owners rather than duplicating them in Shop");
      const linkedActions = el("div", "st-admin-page-actions");
      for (const domain of manifest.linkedRuntimeDomains) linkedActions.append(button(`${domain.label} · inspect`, () => navigate(domain.route)));
      linked.append(notice(manifest.linkedRuntimeDomains.map((entry) => `${entry.label}: ${entry.relationship}`).join(" · ") || "No linked domains were returned.", "info"), linkedActions);
      const preview = panel("Shop Preview", "Preview remains closed until the child exports a protocol for the same deterministic generator");
      preview.append(notice(manifest.preview.reason, "warn"));
      detailsHost.append(capabilities, evidence, linked, preview);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Shop runtime contract is unavailable.", "error");
      tabBar.replaceChildren();
      detailsHost.replaceChildren();
      renderAdminFailureState(content, {
        title: "Shop contract unavailable",
        fallbackMessage: "The canonical Shop runtime contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
