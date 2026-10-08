import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type TabId = "vocabulary" | "typing-text" | "boss-text" | "recall" | "objectives";
type CatalogKind = "vocabulary" | "typing-text";
type CatalogItem = {
  id: string;
  title: string;
  type: CatalogKind;
  cefr: string;
  topics: string[];
  difficulty: string;
  length: number;
  usedBy: string[];
  status: string;
  source: string;
  level: number;
  meaning?: string;
  ipa?: string;
  style?: string;
  setting?: string;
  tone?: string;
  targetWords?: string[];
  excerpt?: string;
};
type CatalogPayload = {
  protocolVersion: 1;
  mode: "canonical-readonly";
  owner: string;
  kind: CatalogKind;
  total: number;
  offset: number;
  limit: number;
  items: CatalogItem[];
  canonicalTotals: { vocabulary: number; vocabularyLevels: number; typingText: number; typingTextLevels: number };
  tabs: Record<string, { status: string; source: string; consumers?: string[]; note?: string }>;
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
function inputField(label: string, placeholder = ""): { root: HTMLElement; input: HTMLInputElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const input = el("input") as HTMLInputElement;
  input.placeholder = placeholder;
  root.append(input);
  return { root, input };
}
function selectField(label: string, options: Array<[string, string]>): { root: HTMLElement; select: HTMLSelectElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const select = el("select") as HTMLSelectElement;
  for (const [value, text] of options) { const option = el("option", undefined, text) as HTMLOptionElement; option.value = value; select.append(option); }
  root.append(select);
  return { root, select };
}

async function fetchCatalog(params: URLSearchParams): Promise<CatalogPayload> {
  const response = await fetch(`/api/admin/space-typing/typing-content/catalog?${params.toString()}`, {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Record<string, unknown>;
  if (!response.ok) throw new Error(typeof payload["message"] === "string" ? payload["message"] : `Typing Content catalog failed (${response.status})`);
  return payload as unknown as CatalogPayload;
}

const tabs: Array<[TabId, string]> = [
  ["vocabulary", "Vocabulary"],
  ["typing-text", "Typing Text"],
  ["boss-text", "Boss Text"],
  ["recall", "Recall"],
  ["objectives", "Objectives"],
];

export function renderPhaseBTypingContent(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Canonical Learning Catalog"),
    el("h1", undefined, "Typing Content"),
    el("p", undefined, "Read-only Space Typing view over the canonical English Learning Content System. This screen never forks vocabulary or typing-text records into Admin revisions."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("CANONICAL · READ ONLY", "good"), button("Worlds & Stages", () => navigate("/admin/space-typing/stages")), button("History", () => navigate("/admin/space-typing/history")));
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical catalog…");
  page.append(status);

  const tabBar = el("div", "st-admin-page-actions");
  const content = el("div");
  page.append(tabBar, content);

  let activeTab: TabId = "vocabulary";
  let offset = 0;
  const limit = 50;
  let lastMetadata: CatalogPayload | null = null;

  const renderTabs = () => {
    tabBar.replaceChildren();
    for (const [id, label] of tabs) {
      tabBar.append(button(label, () => { activeTab = id; offset = 0; renderTabs(); void renderContent(); }, activeTab === id ? "st-admin-btn primary" : "st-admin-btn"));
    }
  };

  const renderDerivedTab = (title: string, state: { status: string; source: string; note?: string }, details: string[]) => {
    content.replaceChildren();
    const info = panel(title, "Consumer/reference status — no duplicate content records are created here");
    info.append(notice(`Status: ${state.status} · Source: ${state.source}`, state.status === "gameplay-owned" ? "warn" : "info"));
    if (state.note) info.append(notice(state.note, "info"));
    for (const detail of details) info.append(notice(detail, "info"));
    content.append(info);
  };

  const renderCatalog = async (kind: CatalogKind) => {
    content.replaceChildren();
    const filters = panel("Catalog Filters", "Search first · canonical source · no direct authoring");
    const filterGrid = el("div", "stx-grid");
    const search = inputField("Search", kind === "vocabulary" ? "ID, word, meaning, IPA…" : "ID, topic, text, target word…");
    const cefr = selectField("CEFR", [["", "All"], ["Foundation", "Foundation"], ["A1", "A1"], ["A2", "A2"], ["B1", "B1"], ["B2", "B2"], ["C1", "C1"], ["C2", "C2"], ["Advanced", "Advanced"]]);
    const topic = inputField("Topic / skill focus", "topic contains…");
    const level = inputField("Learning Level", "1–100");
    level.input.type = "number"; level.input.min = "1"; level.input.max = "100";
    const usedByOptions: Array<[string, string]> = kind === "vocabulary"
      ? [["", "All consumers"], ["combat", "Combat"], ["recall", "Recall"], ["smart-review", "Smart Review"]]
      : [["", "All consumers"], ["special-stage-typing", "Special Stage Typing"]];
    const usedBy = selectField("Stage / mode usage", usedByOptions);
    const source = selectField("Source", [["", "Canonical source"], [kind === "vocabulary" ? "shared/vocabulary" : "shared/typing-texts", kind === "vocabulary" ? "shared/vocabulary" : "shared/typing-texts"]]);
    filterGrid.append(search.root, cefr.root, topic.root, level.root, usedBy.root, source.root);
    const filterActions = el("div", "st-admin-page-actions");
    filters.append(filterGrid, filterActions);

    const tablePanel = panel(kind === "vocabulary" ? "Vocabulary Catalog" : "Typing Text Catalog", "Content IDs remain owned by the shared English-learning pipeline");
    const tableHost = el("div");
    const detailHost = el("div");
    tablePanel.append(tableHost, detailHost);
    content.append(filters, tablePanel);

    const load = async (resetOffset = false) => {
      if (resetOffset) offset = 0;
      const params = new URLSearchParams({ kind, offset: String(offset), limit: String(limit) });
      if (search.input.value.trim()) params.set("q", search.input.value.trim());
      if (cefr.select.value) params.set("cefr", cefr.select.value);
      if (topic.input.value.trim()) params.set("topic", topic.input.value.trim());
      if (level.input.value) params.set("level", level.input.value);
      if (usedBy.select.value) params.set("usedBy", usedBy.select.value);
      if (source.select.value) params.set("source", source.select.value);
      status.className = "stx-notice info"; status.textContent = "Reading canonical shared catalog…";
      try {
        const result = await fetchCatalog(params);
        lastMetadata = result;
        const totalKind = kind === "vocabulary" ? `${result.canonicalTotals.vocabulary.toLocaleString()} words / ${result.canonicalTotals.vocabularyLevels} levels` : `${result.canonicalTotals.typingText.toLocaleString()} passages / ${result.canonicalTotals.typingTextLevels} levels`;
        status.className = "stx-notice good";
        status.textContent = `${result.owner} · ${totalKind} · ${result.total.toLocaleString()} matching · source remains read-only.`;
        tableHost.replaceChildren();
        const table = el("table", "st-admin-table");
        const head = el("thead"); const hr = el("tr");
        for (const title of ["Content ID", "Title / Word", "Type", "CEFR", "Topic", "Difficulty", "Length", "Used By", "Status", ""]) hr.append(el("th", undefined, title));
        head.append(hr); table.append(head);
        const tbody = el("tbody");
        for (const item of result.items) {
          const row = el("tr");
          row.append(
            el("td", undefined, item.id), el("td", undefined, item.title), el("td", undefined, item.type), el("td", undefined, item.cefr),
            el("td", undefined, item.topics.join(", ") || "—"), el("td", undefined, item.difficulty), el("td", undefined, String(item.length)),
            el("td", undefined, item.usedBy.join(", ")), el("td", undefined, item.status),
          );
          const inspectCell = el("td");
          inspectCell.append(button("Inspect", () => {
            detailHost.replaceChildren();
            const detail = panel(`${item.id} · ${item.title}`, `${item.source} · Level ${item.level} · canonical owner`);
            if (item.type === "vocabulary") {
              detail.append(notice(`IPA: ${item.ipa ?? "—"}`, "info"), notice(`Meaning: ${item.meaning ?? "—"}`, "info"), notice(`Topics: ${item.topics.join(", ") || "unclassified"}`, "info"));
            } else {
              detail.append(notice(`Style: ${item.style ?? "—"} · Setting: ${item.setting ?? "—"} · Tone: ${item.tone ?? "—"}`, "info"), notice(`Target words: ${(item.targetWords ?? []).join(", ")}`, "info"), notice(item.excerpt ? `${item.excerpt}…` : "No excerpt", "info"));
            }
            detail.append(notice("Editing is intentionally disabled here. Update content through the owning English Learning Content System pipeline, then this catalog reflects the canonical result.", "warn"));
            detailHost.append(detail);
          }));
          row.append(inspectCell); tbody.append(row);
        }
        table.append(tbody); tableHost.append(table);
        filterActions.replaceChildren(
          button("Apply Filters", () => { void load(true); }, "st-admin-btn primary"),
          button("Previous", () => { offset = Math.max(0, offset - limit); void load(false); }),
          badge(`${result.total === 0 ? 0 : offset + 1}–${Math.min(offset + limit, result.total)} / ${result.total}`),
          button("Next", () => { if (offset + limit < result.total) { offset += limit; void load(false); } }),
        );
      } catch (error: unknown) {
        status.className = "stx-notice bad";
        status.textContent = `Typing Content unavailable: ${error instanceof Error ? error.message : String(error)}`;
      }
    };
    search.input.addEventListener("keydown", (event) => { if (event.key === "Enter") void load(true); });
    topic.input.addEventListener("keydown", (event) => { if (event.key === "Enter") void load(true); });
    filterActions.append(button("Apply Filters", () => { void load(true); }, "st-admin-btn primary"));
    await load(false);
  };

  const renderContent = async () => {
    if (activeTab === "vocabulary") { await renderCatalog("vocabulary"); return; }
    if (activeTab === "typing-text") { await renderCatalog("typing-text"); return; }
    if (!lastMetadata) {
      try { lastMetadata = await fetchCatalog(new URLSearchParams({ kind: "vocabulary", limit: "1" })); }
      catch (error: unknown) { status.className = "stx-notice bad"; status.textContent = `Typing Content unavailable: ${error instanceof Error ? error.message : String(error)}`; return; }
    }
    status.className = "stx-notice good"; status.textContent = "Canonical consumer boundary verified; no duplicate Admin dataset is created.";
    if (activeTab === "boss-text") renderDerivedTab("Boss Text", lastMetadata.tabs.bossText, ["Boss typing mechanics currently consume the canonical vocabulary pool and mechanic rules.", "No standalone boss passage corpus was found in the verified runtime path, so authoring stays closed until such a consumer exists."]);
    if (activeTab === "recall") renderDerivedTab("Recall", lastMetadata.tabs.recall, ["Recall accepts canonical VocabularyEntry records and preserves their IDs.", "Shared review datasets also resolve exact vocabulary entity IDs; Vocabulary remains the single source of truth."]);
    if (activeTab === "objectives") renderDerivedTab("Objectives", lastMetadata.tabs.objectives, ["The current objective system is stage/gameplay logic under events/objectives.", "It is not an English-learning content catalog, so this Admin screen does not misrepresent gameplay objectives as authorable learning records."]);
  };

  renderTabs();
  void renderContent();
  return page;
}
