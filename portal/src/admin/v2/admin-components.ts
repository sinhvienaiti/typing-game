import type { AdminHelpScope, AdminInfoIconOptions } from "./admin-help";

export type AdminTone = "info" | "good" | "warn" | "bad";

export type AdminPageHeaderOptions = {
  title: string;
  eyebrow?: string;
  subtitle?: string;
  actions?: readonly HTMLElement[];
  help?: Omit<AdminInfoIconOptions, "label">;
  helpScope?: AdminHelpScope;
};

export type AdminValidationMessageOptions = {
  message: string;
  tone?: AdminTone;
  title?: string;
};

export type AdminEmptyStateOptions = {
  title: string;
  message?: string;
  action?: HTMLElement;
};

export type AdminErrorStateOptions = {
  title?: string;
  message: string;
  retry?: () => void;
};

export type AdminSearchInputOptions = {
  label?: string;
  placeholder?: string;
  value?: string;
  onInput?: (value: string) => void;
};

export type AdminDraftBarOptions = {
  title?: string;
  status: string;
  tone?: AdminTone;
  onDiscard?: () => void;
  onSaveDraft?: () => void;
  onPreview?: () => void;
  onReviewChanges?: () => void;
  onPublish?: () => void;
  saving?: boolean;
  publishDisabled?: boolean;
};

export type AdminEntityTableColumn<Row> = {
  key: string;
  label: string;
  render: (row: Row) => string | Node;
  align?: "start" | "center" | "end";
};

export type AdminEntityTableOptions<Row> = {
  columns: readonly AdminEntityTableColumn<Row>[];
  rows: readonly Row[];
  rowKey: (row: Row) => string;
  emptyTitle?: string;
  emptyMessage?: string;
};

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function actionButton(label: string, onClick: (() => void) | undefined, className = "st-admin-btn"): HTMLButtonElement {
  const button = element("button", className, label);
  button.type = "button";
  button.disabled = onClick === undefined;
  if (onClick) button.addEventListener("click", onClick);
  return button;
}

export function createAdminPageHeader(options: AdminPageHeaderOptions): HTMLElement {
  const root = element("header", "st-admin-v2-page-head");
  const copy = element("div", "st-admin-v2-page-head-copy");
  if (options.eyebrow) copy.append(element("div", "st-admin-v2-eyebrow", options.eyebrow));

  const titleRow = element("div", "st-admin-v2-page-title-row");
  titleRow.append(element("h1", undefined, options.title));
  if (options.help && options.helpScope) {
    titleRow.append(options.helpScope.infoIcon({ ...options.help, label: `Help for ${options.title}` }));
  }
  copy.append(titleRow);
  if (options.subtitle) copy.append(element("p", "st-admin-v2-page-subtitle", options.subtitle));
  root.append(copy);

  if (options.actions?.length) {
    const actions = element("div", "st-admin-v2-page-actions");
    actions.append(...options.actions);
    root.append(actions);
  }
  return root;
}

export function createAdminValidationMessage(options: AdminValidationMessageOptions): HTMLElement {
  const tone = options.tone ?? "info";
  const root = element("div", `st-admin-v2-validation ${tone}`);
  root.setAttribute("role", tone === "bad" ? "alert" : "status");
  root.setAttribute("aria-live", tone === "bad" ? "assertive" : "polite");
  if (options.title) root.append(element("strong", undefined, options.title));
  root.append(element("span", undefined, options.message));
  return root;
}

export function createAdminEmptyState(options: AdminEmptyStateOptions): HTMLElement {
  const root = element("section", "st-admin-v2-empty-state");
  root.append(element("div", "st-admin-v2-empty-mark", "◇"), element("h2", undefined, options.title));
  if (options.message) root.append(element("p", undefined, options.message));
  if (options.action) {
    const action = element("div", "st-admin-v2-empty-action");
    action.append(options.action);
    root.append(action);
  }
  return root;
}

export function createAdminErrorState(options: AdminErrorStateOptions): HTMLElement {
  const root = element("section", "st-admin-v2-error-state");
  root.setAttribute("role", "alert");
  root.append(element("div", "st-admin-v2-error-mark", "!"), element("h2", undefined, options.title ?? "Unable to load"), element("p", undefined, options.message));
  if (options.retry) root.append(actionButton("Retry", options.retry, "st-admin-btn primary"));
  return root;
}

export function createAdminSkeleton(lines = 4): HTMLElement {
  const root = element("div", "st-admin-v2-skeleton");
  root.setAttribute("aria-label", "Loading");
  root.setAttribute("aria-busy", "true");
  for (let index = 0; index < Math.max(1, Math.min(12, lines)); index += 1) {
    root.append(element("span", "st-admin-v2-skeleton-line"));
  }
  return root;
}

export function createAdminSearchInput(options: AdminSearchInputOptions = {}): HTMLInputElement {
  const input = element("input", "st-admin-v2-search");
  input.type = "search";
  input.value = options.value ?? "";
  input.placeholder = options.placeholder ?? "Search…";
  input.setAttribute("aria-label", options.label ?? "Search");
  if (options.onInput) input.addEventListener("input", () => options.onInput?.(input.value));
  return input;
}

export function createAdminFilterBar(...children: HTMLElement[]): HTMLElement {
  const root = element("div", "st-admin-v2-filter-bar");
  root.append(...children);
  return root;
}

export function createAdminStatusChip(label: string, tone: AdminTone = "info"): HTMLElement {
  return element("span", `st-admin-v2-chip ${tone}`, label);
}

export function createAdminDraftBar(options: AdminDraftBarOptions): HTMLElement {
  const root = element("div", `st-admin-v2-draft-bar ${options.tone ?? "info"}`);
  const copy = element("div", "st-admin-v2-draft-copy");
  copy.append(element("strong", undefined, options.title ?? "Draft changes"), element("span", undefined, options.status));
  root.append(copy);

  const actions = element("div", "st-admin-v2-draft-actions");
  if (options.onDiscard) actions.append(actionButton("Discard", options.onDiscard));
  if (options.onPreview) actions.append(actionButton("Preview", options.onPreview));
  if (options.onReviewChanges) actions.append(actionButton("Review Changes", options.onReviewChanges));
  if (options.onSaveDraft) {
    const save = actionButton(options.saving ? "Saving…" : "Save Draft", options.onSaveDraft, "st-admin-btn primary");
    save.disabled = Boolean(options.saving);
    actions.append(save);
  }
  if (options.onPublish) {
    const publish = actionButton("Publish", options.onPublish, "st-admin-btn st-admin-v2-publish");
    publish.disabled = Boolean(options.publishDisabled);
    actions.append(publish);
  }
  root.append(actions);
  return root;
}

export function createAdminEntityTable<Row>(options: AdminEntityTableOptions<Row>): HTMLElement {
  if (options.rows.length === 0) {
    return createAdminEmptyState({
      title: options.emptyTitle ?? "No items yet",
      message: options.emptyMessage,
    });
  }

  const wrap = element("div", "st-admin-v2-table-wrap");
  const table = element("table", "st-admin-v2-table");
  const thead = element("thead");
  const headerRow = element("tr");
  for (const column of options.columns) {
    const th = element("th", column.align ? `align-${column.align}` : undefined, column.label);
    th.scope = "col";
    headerRow.append(th);
  }
  thead.append(headerRow);
  table.append(thead);

  const tbody = element("tbody");
  for (const row of options.rows) {
    const tr = element("tr");
    tr.dataset.entityKey = options.rowKey(row);
    for (const column of options.columns) {
      const td = element("td", column.align ? `align-${column.align}` : undefined);
      const rendered = column.render(row);
      if (typeof rendered === "string") td.textContent = rendered;
      else td.append(rendered);
      tr.append(td);
    }
    tbody.append(tr);
  }
  table.append(tbody);
  wrap.append(table);
  return wrap;
}
