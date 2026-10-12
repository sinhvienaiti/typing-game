import { SpaceTypingAdminApi } from "./api";
import { adminErrorMessage } from "./admin-http";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

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
type CatalogTabState = { status: string; source: string; consumers?: string[]; note?: string };
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
  tabs: { bossText: CatalogTabState; recall: CatalogTabState; objectives: CatalogTabState } & Record<string, CatalogTabState>;
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
  input.setAttribute("aria-label", label);
  root.append(input);
  return { root, input };
}
function selectField(label: string, options: Array<[string, string]>): { root: HTMLElement; select: HTMLSelectElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const select = el("select", "st-admin-select") as HTMLSelectElement;
  select.setAttribute("aria-label", label);
  for (const [value, text] of options) {
    const option = el("option", undefined, text) as HTMLOptionElement;
    option.value = value;
    select.append(option);
  }
  root.append(select);
  return { root, select };
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function validateCatalogPayload(value: unknown, expectedKind: CatalogKind): CatalogPayload {
  if (!isRecord(value)) throw new Error("Typing Content catalog response is not an object.");
  if (value["protocolVersion"] !== 1 || value["mode"] !== "canonical-readonly" || value["kind"] !== expectedKind) {
    throw new Error("Typing Content catalog response does not match the canonical read-only protocol.");
  }
  if (typeof value["owner"] !== "string" || !Array.isArray(value["items"]) || !isRecord(value["canonicalTotals"]) || !isRecord(value["tabs"])) {
    throw new Error("Typing Content catalog response is missing canonical catalog metadata.");
  }
  const totals = value["canonicalTotals"];
  for (const key of ["vocabulary", "vocabularyLevels", "typingText", "typingTextLevels"] as const) {
    if (typeof totals[key] !== "number" || !Number.isFinite(totals[key])) {
      throw new Error(`Typing Content catalog response is missing canonicalTotals.${key}.`);
    }
  }
  for (const key of ["bossText", "recall", "objectives"] as const) {
    if (!isRecord(value["tabs"][key]) || typeof value["tabs"][key]["status"] !== "string" || typeof value["tabs"][key]["source"] !== "string") {
      throw new Error(`Typing Content catalog response is missing tabs.${key}.`);
    }
  }
  if (typeof value["total"] !== "number" || typeof value["offset"] !== "number" || typeof value["limit"] !== "number") {
    throw new Error("Typing Content catalog pagination metadata is invalid.");
  }
  return value as unknown as CatalogPayload;
}

async function fetchCatalog(params: URLSearchParams): Promise<CatalogPayload> {
  const expectedKind = params.get("kind") === "typing-text" ? "typing-text" : "vocabulary";
  const payload = await api.requestJson<unknown>(`/api/admin/space-typing/typing-content/catalog?${params.toString()}`);
  return validateCatalogPayload(payload, expectedKind);
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
    el("p", undefined, "Browse the canonical English Learning Content System used by Space Typing. This surface is read-only: vocabulary and typing-text records stay owned by the shared learning pipeline."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("CANONICAL · READ ONLY", "good"),
    button("Worlds & Stages", () => navigate("/admin/space-typing/stages")),
    button("History", () => navigate("/admin/space-typing/history")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical catalog…");
  status.setAttribute("aria-live", "polite");
  page.append(status);

  const tabBar = el("div", "st-admin-page-actions");
  tabBar.setAttribute("role", "tablist");
  const content = el("div");
  page.append(tabBar, content);

  let activeTab: TabId = "vocabulary";
  let offset = 0;
  const limit = 50;
  let lastMetadata: CatalogPayload | null = null;
  let renderGeneration = 0;

  const renderTabs = (): void => {
    tabBar.replaceChildren();
    for (const [id, label] of tabs) {
      const control = button(label, () => {
        activeTab = id;
        offset = 0;
        renderTabs();
        void renderContent();
      }, activeTab === id ? "st-admin-btn primary" : "st-admin-btn");
      control.setAttribute("role", "tab");
      control.setAttribute("aria-selected", String(activeTab === id));
      tabBar.append(control);
    }
  };

  const renderDerivedTab = (title: string, state: CatalogTabState, details: string[]): void => {
    content.replaceChildren();
    const info = panel(title, "Consumer/reference status — no duplicate content records are created here");
    info.append(notice(`Status: ${state.status} · Source: ${state.source}`, state.status === "gameplay-owned" ? "warn" : "info"));
    if (state.note) info.append(notice(state.note, "info"));
    for (const detail of details) info.append(notice(detail, "info"));
    content.append(info);
  };

  const renderCatalog = async (kind: CatalogKind): Promise<void> => {
    const generation = ++renderGeneration;
    content.replaceChildren();
    const filters = panel("Catalog Filters", "Search and filter the canonical source; editing stays in the owning content pipeline");
    const filterGrid = el("div", "stx-grid");
    const search = inputField("Search", kind === "vocabulary" ? "ID, word, meaning, IPA…" : "ID, topic, text, target word…");
    const cefr = selectField("CEFR", [["", "All"], ["Foundation", "Foundation"], ["A1", "A1"], ["A2", "A2"], ["B1", "B1"], ["B2", "B2"], ["C1", "C1"], ["C2", "C2"], ["Advanced", "Advanced"]]);
    const topic = inputField("Topic / skill focus", "topic contains…");
    const level = inputField("Learning Level", "1–100");
    level.input.type = "number";
    level.input.min = "1";
    level.input.max = "100";
    const usedByOptions: Array<[string, string]> = kind === "vocabulary"
      ? [["", "All consumers"], ["combat", "Combat"], ["recall", "Recall"], ["smart-review", "Smart Review"]]
      : [["", "All consumers"], ["special-stage-typing", "Special Stage Typing"]];
    const usedBy = selectField("Stage / mode usage", usedByOptions);
    const source = selectField("Source", [["", "Canonical source"], [kind === "vocabulary" ? "shared/vocabulary" : "shared/typing-texts", kind === "vocabulary" ? "shared/vocabulary" : "shared/typing-texts"]]);
    const controls = [search.input, cefr.select, topic.input, level.input, usedBy.select, source.select];
    filterGrid.append(search.root, cefr.root, topic.root, level.root, usedBy.root, source.root);
    const filterActions = el("div", "st-admin-page-actions");
    filters.append(filterGrid, filterActions);

    const tablePanel = panel(kind === "vocabulary" ? "Vocabulary Catalog" : "Typing Text Catalog", "Content IDs remain owned by the shared English-learning pipeline");
    const tableHost = el("div");
    const detailHost = el("div");
    tablePanel.append(tableHost, detailHost);
    content.append(filters, tablePanel);

    const load = async (resetOffset = false): Promise<void> => {
      if (resetOffset) offset = 0;
      const params = new URLSearchParams({ kind, offset: String(offset), limit: String(limit) });
      if (search.input.value.trim()) params.set("q", search.input.value.trim());
      if (cefr.select.value) params.set("cefr", cefr.select.value);
      if (topic.input.value.trim()) params.set("topic", topic.input.value.trim());
      if (level.input.value) params.set("level", level.input.value);
      if (usedBy.select.value) params.set("usedBy", usedBy.select.value);
      if (source.select.value) params.set("source", source.select.value);

      controls.forEach((control) => { control.disabled = true; });
      setAdminStatus(status, "Reading canonical shared catalog…", "loading");
      tableHost.replaceChildren(notice("Loading catalog rows…", "info"));
      detailHost.replaceChildren();
      try {
        const result = await fetchCatalog(params);
        if (generation !== renderGeneration || activeTab !== kind) return;
        lastMetadata = result;
        const totalKind = kind === "vocabulary"
          ? `${result.canonicalTotals.vocabulary.toLocaleString()} words / ${result.canonicalTotals.vocabularyLevels} levels`
          : `${result.canonicalTotals.typingText.toLocaleString()} passages / ${result.canonicalTotals.typingTextLevels} levels`;
        setAdminStatus(status, `${result.owner} · ${totalKind} · ${result.total.toLocaleString()} matching · source remains read-only.`, "success");
        tableHost.replaceChildren();

        if (result.items.length === 0) {
          tableHost.append(notice("No canonical content matches the current filters. Change a filter and try again.", "info"));
        } else {
          const wrap = el("div", "st-admin-table-wrap");
          const table = el("table", "st-admin-table");
          const head = el("thead");
          const headerRow = el("tr");
          for (const title of ["Content ID", "Title / Word", "Type", "CEFR", "Topic", "Difficulty", "Length", "Used By", "Status", ""]) headerRow.append(el("th", undefined, title));
          head.append(headerRow);
          table.append(head);
          const tbody = el("tbody");
          for (const item of result.items) {
            const row = el("tr");
            row.append(
              el("td", undefined, item.id),
              el("td", undefined, item.title),
              el("td", undefined, item.type),
              el("td", undefined, item.cefr),
              el("td", undefined, Array.isArray(item.topics) ? item.topics.join(", ") || "—" : "—"),
              el("td", undefined, item.difficulty),
              el("td", undefined, String(item.length)),
              el("td", undefined, Array.isArray(item.usedBy) ? item.usedBy.join(", ") : "—"),
              el("td", undefined, item.status),
            );
            const inspectCell = el("td");
            inspectCell.append(button("Inspect", () => {
              detailHost.replaceChildren();
              const detail = panel(`${item.id} · ${item.title}`, `${item.source} · Level ${item.level} · canonical owner`);
              if (item.type === "vocabulary") {
                detail.append(
                  notice(`IPA: ${item.ipa ?? "—"}`, "info"),
                  notice(`Meaning: ${item.meaning ?? "—"}`, "info"),
                  notice(`Topics: ${Array.isArray(item.topics) ? item.topics.join(", ") || "unclassified" : "unclassified"}`, "info"),
                );
              } else {
                detail.append(
                  notice(`Style: ${item.style ?? "—"} · Setting: ${item.setting ?? "—"} · Tone: ${item.tone ?? "—"}`, "info"),
                  notice(`Target words: ${Array.isArray(item.targetWords) ? item.targetWords.join(", ") : "—"}`, "info"),
                  notice(item.excerpt ? `${item.excerpt}…` : "No excerpt", "info"),
                );
              }
              detail.append(notice("Editing is intentionally disabled here. Update content through the owning English Learning Content System pipeline; this catalog then reflects the canonical result.", "warn"));
              detailHost.append(detail);
            }));
            row.append(inspectCell);
            tbody.append(row);
          }
          table.append(tbody);
          wrap.append(table);
          tableHost.append(wrap);
        }

        const previous = button("Previous", () => {
          offset = Math.max(0, offset - limit);
          void load(false);
        });
        previous.disabled = offset === 0;
        const next = button("Next", () => {
          if (offset + limit < result.total) {
            offset += limit;
            void load(false);
          }
        });
        next.disabled = offset + limit >= result.total;
        filterActions.replaceChildren(
          button("Apply Filters", () => { void load(true); }, "st-admin-btn primary"),
          previous,
          badge(`${result.total === 0 ? 0 : offset + 1}–${Math.min(offset + limit, result.total)} / ${result.total}`),
          next,
        );
      } catch (error: unknown) {
        if (generation !== renderGeneration) return;
        setAdminStatus(status, "Typing Content is unavailable.", "error");
        renderAdminFailureState(tableHost, {
          title: "Canonical content unavailable",
          fallbackMessage: "The Typing Content catalog could not be verified. Check the local Admin runtime and try again.",
          error,
          onRetry: () => { void load(false); },
        });
      } finally {
        if (generation === renderGeneration) controls.forEach((control) => { control.disabled = false; });
      }
    };

    search.input.addEventListener("keydown", (event) => { if (event.key === "Enter") void load(true); });
    topic.input.addEventListener("keydown", (event) => { if (event.key === "Enter") void load(true); });
    filterActions.append(button("Apply Filters", () => { void load(true); }, "st-admin-btn primary"));
    await load(false);
  };

  const renderContent = async (): Promise<void> => {
    if (activeTab === "vocabulary") { await renderCatalog("vocabulary"); return; }
    if (activeTab === "typing-text") { await renderCatalog("typing-text"); return; }
    const generation = ++renderGeneration;
    if (!lastMetadata) {
      setAdminStatus(status, "Loading canonical consumer metadata…", "loading");
      try {
        lastMetadata = await fetchCatalog(new URLSearchParams({ kind: "vocabulary", limit: "1" }));
      } catch (error: unknown) {
        if (generation !== renderGeneration) return;
        setAdminStatus(status, "Typing Content is unavailable.", "error");
        renderAdminFailureState(content, {
          title: "Consumer metadata unavailable",
          fallbackMessage: "The canonical Typing Content metadata could not be loaded. Check the local Admin runtime and try again.",
          error,
          onRetry: () => { void renderContent(); },
        });
        return;
      }
    }
    if (generation !== renderGeneration || !lastMetadata) return;
    setAdminStatus(status, "Canonical consumer boundary verified; no duplicate Admin dataset is created.", "success");
    if (activeTab === "boss-text") renderDerivedTab("Boss Text", lastMetadata.tabs.bossText, ["Boss typing mechanics currently consume the canonical vocabulary pool and mechanic rules.", "No standalone boss passage corpus was found in the verified runtime path, so authoring stays closed until such a consumer exists."]);
    if (activeTab === "recall") renderDerivedTab("Recall", lastMetadata.tabs.recall, ["Recall accepts canonical VocabularyEntry records and preserves their IDs.", "Shared review datasets also resolve exact vocabulary entity IDs; Vocabulary remains the single source of truth."]);
    if (activeTab === "objectives") renderDerivedTab("Objectives", lastMetadata.tabs.objectives, ["The current objective system is stage/gameplay logic under events/objectives.", "It is not an English-learning content catalog, so this Admin screen does not misrepresent gameplay objectives as authorable learning records."]);
  };

  renderTabs();
  void renderContent().catch((error: unknown) => {
    setAdminStatus(status, adminErrorMessage(error, "Typing Content could not be rendered."), "error");
  });
  return page;
}
