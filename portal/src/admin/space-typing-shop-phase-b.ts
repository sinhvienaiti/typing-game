import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type ShopManifest = {
  protocolVersion: 1;
  mode: "runtime-audited-readonly";
  owner: string;
  auditedChildSha: string;
  tabs: string[];
  fields: Array<{ name: string; authorable: false; reason: string }>;
  capabilities: Record<string, boolean>;
  evidence: Array<{ id: string; found: boolean; detail: string }>;
  linkedRuntimeDomains: Array<{ id: string; label: string; route: string; relationship: string }>;
  authoring: { enabled: false; applyBoundary: "none"; persistence: "runtime-audit-manifest"; reason: string };
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
  if (!response.ok) throw new Error(typeof payload["message"] === "string" ? payload["message"] : `Shop capability audit failed (${response.status})`);
  return payload as unknown as ShopManifest;
}

function renderUnavailableTab(host: HTMLElement, tab: string, manifest: ShopManifest) {
  host.replaceChildren();
  const scope = panel(`${tab} · Runtime boundary`, "Master-plan surface retained without fabricating commerce data");
  scope.append(
    notice(manifest.authoring.reason, "warn"),
    notice(`Apply boundary: ${manifest.authoring.applyBoundary} · Persistence: ${manifest.authoring.persistence}`, "info"),
  );
  if (tab === "Catalog") {
    const fields = panel("Item Config Contract", "All 15 master-plan fields are visible, but none are writable until a real consumer exists");
    const table = el("table", "st-admin-table");
    const thead = el("thead"); const hr = el("tr");
    for (const title of ["Field", "Runtime-backed", "Authorable", "Reason"]) hr.append(el("th", undefined, title));
    thead.append(hr); table.append(thead);
    const tbody = el("tbody");
    for (const field of manifest.fields) {
      const row = el("tr");
      row.append(el("td", undefined, field.name), el("td", undefined, "No"), el("td", undefined, "Locked"), el("td", undefined, field.reason));
      tbody.append(row);
    }
    table.append(tbody); fields.append(table); host.append(scope, fields);
    return;
  }
  if (tab === "History") {
    scope.append(notice("No canonical Shop transaction-history source exists in the audited runtime tree. Revision history is not presented as purchase history.", "info"));
  } else {
    scope.append(notice(`${tab} configuration remains unavailable because catalog, pricing, currency, purchase-limit and schedule consumers are not runtime-backed yet.`, "info"));
  }
  host.append(scope);
}

export function renderPhaseBShop(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Economy · Runtime Ownership Audit"),
    el("h1", undefined, "Shop"),
    el("p", undefined, "The complete Shop UX contract is present, but authoring is deliberately locked until Space Typing has a canonical catalog, pricing/currency model and purchase transaction owner."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME AUDIT · READ ONLY", "warn"), button("Currencies", () => navigate("/admin/space-typing/currencies")), button("History", () => navigate("/admin/space-typing/history")));
  header.append(copy, actions); page.append(header);

  const status = notice("Auditing pinned runtime ownership…");
  const tabBar = el("div", "st-admin-page-actions");
  const content = el("div");
  page.append(status, tabBar, content);

  void (async () => {
    try {
      const manifest = await fetchShopManifest();
      status.className = "stx-notice good";
      status.textContent = `Audit pinned to child ${manifest.auditedChildSha.slice(0, 12)} · no Shop transaction owner found · fake commerce authoring prevented.`;
      let activeTab = manifest.tabs[0] ?? "Catalog";
      const renderTabs = () => {
        tabBar.replaceChildren();
        for (const tab of manifest.tabs) {
          tabBar.append(button(tab, () => { activeTab = tab; renderTabs(); renderUnavailableTab(content, activeTab, manifest); }, activeTab === tab ? "st-admin-btn primary" : "st-admin-btn"));
        }
      };
      renderTabs(); renderUnavailableTab(content, activeTab, manifest);

      const audit = panel("Runtime Evidence", "Negative evidence is explicit and tied to the pinned child SHA");
      for (const item of manifest.evidence) audit.append(notice(`${item.id}: ${item.found ? "FOUND" : "not found"} · ${item.detail}`, item.found ? "good" : "info"));
      const linked = panel("Runtime-backed Content", "These domains exist, but are not silently treated as merchandise");
      const linkedActions = el("div", "st-admin-page-actions");
      for (const domain of manifest.linkedRuntimeDomains) linkedActions.append(button(`${domain.label} · inspect`, () => navigate(domain.route)));
      linked.append(notice(manifest.linkedRuntimeDomains.map((entry) => `${entry.label}: ${entry.relationship}`).join(" · "), "info"), linkedActions);
      const preview = panel("Shop Preview", "Preview stays closed until it can render the same canonical data the game would consume");
      preview.append(notice(manifest.preview.reason, "warn"));
      page.append(audit, linked, preview);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Shop audit unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();

  return page;
}
