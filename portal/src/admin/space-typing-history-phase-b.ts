import {
  AdminApiError,
  SpaceTypingAdminApi,
  type AdminAuditEvent,
  type AdminRevision,
  type AdminRevisionValidation,
  type AdminStatePayload,
} from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type DiffKind = "added" | "removed" | "modified";
type DiffEntry = { kind: DiffKind; path: string; before?: unknown; after?: unknown };
type ValidationState = { revision: string; result: AdminRevisionValidation } | null;

const DOMAIN_LABELS: Readonly<Record<string, string>> = Object.freeze({
  audio: "Audio Defaults",
  worldMusic: "World / Stage Music",
  system: "General Settings",
  featureFlags: "Feature Gates",
  ships: "Ships",
  equipment: "Equipment",
  skills: "Skills",
  enemies: "Enemies",
  bosses: "Bosses",
  worlds: "Worlds",
  stages: "Stages",
  shop: "Shop",
  currencies: "Currencies",
  rewards: "Rewards",
});

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function btn(label: string, onClick: () => void = () => undefined, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label) as HTMLButtonElement;
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
function header(actions: readonly HTMLElement[]): HTMLElement {
  const root = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "System · Change History"),
    el("h1", undefined, "History & Publish"),
    el("p", undefined, "Review who changed what, compare administrator-facing values, validate the exact publication scope, then publish or roll back safely."),
  );
  const tools = el("div", "st-admin-page-actions");
  tools.append(...actions);
  root.append(copy, tools);
  return root;
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function validateState(value: unknown): AdminStatePayload {
  if (!isRecord(value) || !isRecord(value["state"]) || !isRecord(value["active"]) || !Array.isArray(value["history"])) {
    throw new Error("Revision history response is missing the canonical state envelope.");
  }
  const state = value["state"];
  const active = value["active"];
  if (typeof state["activeRevision"] !== "string" || typeof state["generation"] !== "number" || typeof active["revision"] !== "string" || !isRecord(active["config"]) || active["revision"] !== state["activeRevision"]) {
    throw new Error("Revision history response contains an inconsistent active pointer.");
  }
  return value as unknown as AdminStatePayload;
}
function sameValue(left: unknown, right: unknown): boolean {
  return Object.is(left, right) || JSON.stringify(left) === JSON.stringify(right);
}
function diffValues(before: unknown, after: unknown, path = ""): DiffEntry[] {
  if (sameValue(before, after)) return [];
  if (isRecord(before) && isRecord(after)) {
    const result: DiffEntry[] = [];
    for (const key of [...new Set([...Object.keys(before), ...Object.keys(after)])].sort()) {
      const nextPath = path ? `${path}.${key}` : key;
      if (!(key in before)) result.push({ kind: "added", path: nextPath, after: after[key] });
      else if (!(key in after)) result.push({ kind: "removed", path: nextPath, before: before[key] });
      else result.push(...diffValues(before[key], after[key], nextPath));
    }
    return result;
  }
  return [{ kind: "modified", path: path || "config", before, after }];
}
function formattedTime(value: string): string {
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? value : date.toLocaleString();
}
function humanize(segment: string): string {
  return segment
    .replace(/([a-z0-9])([A-Z])/g, "$1 $2")
    .replace(/[-_]/g, " ")
    .replace(/^./, (value) => value.toUpperCase());
}
function businessPath(path: string): { domain: string; entity: string; field: string } {
  const parts = path.split(".");
  if (parts[0] === "content" && parts.length > 1) parts.shift();
  const domainKey = parts.shift() ?? "config";
  const domain = DOMAIN_LABELS[domainKey] ?? humanize(domainKey);
  let entity = "Configuration";
  if (parts.length > 1 && ["ships", "equipment", "skills", "enemies", "bosses", "worlds", "stages", "products", "offers"].includes(parts[0] ?? "")) {
    parts.shift();
    entity = parts.shift() ?? "Configuration";
  } else if (parts.length > 1 && /^[a-z0-9-]+$/i.test(parts[0] ?? "")) {
    entity = parts.shift() ?? "Configuration";
  }
  return { domain, entity: humanize(entity), field: parts.map(humanize).join(" › ") || "Value" };
}
function friendlyValue(value: unknown): string {
  if (value === undefined) return "Not set";
  if (value === null) return "None";
  if (typeof value === "boolean") return value ? "Enabled" : "Disabled";
  if (typeof value === "string" || typeof value === "number") return String(value);
  if (Array.isArray(value)) return value.length === 0 ? "None" : value.map(friendlyValue).join(", ");
  const raw = JSON.stringify(value);
  return raw.length > 100 ? `${raw.slice(0, 97)}…` : raw;
}
function relationMeta(revision: AdminRevision): { label: string; tone: Tone } {
  if (revision.relation === "active" || revision.active) return { label: "PUBLISHED", tone: "good" };
  if (revision.relation === "ancestor") return { label: "PUBLISHED HISTORY", tone: "info" };
  if (revision.publishable) return { label: "READY DRAFT", tone: "warn" };
  return { label: "STALE DRAFT", tone: "bad" };
}
function actionLabel(event: AdminAuditEvent): string {
  const labels: Record<string, string> = {
    "revision.create": "created a draft",
    "revision.publish": "published changes",
    "revision.rollback": "rolled back production",
    "media.upload": "uploaded media",
    "media.delete": "retired media",
  };
  return labels[event.action] ?? humanize(event.action.replace(/\./g, " "));
}
function auditTone(result: AdminAuditEvent["result"]): Tone {
  if (result === "success") return "good";
  if (result === "denied" || result === "error") return "bad";
  return "info";
}

export function renderPhaseBHistory(navigate: Navigate): HTMLElement {
  void navigate;
  const page = el("div");
  const activeBadge = badge("Published · loading", "info");
  const reload = btn("Reload", () => void hydrate(selectedRevisionId));
  page.append(header([activeBadge, reload]));

  const status = notice("Loading change history…");
  status.setAttribute("aria-live", "polite");
  const failureHost = el("div");
  const activityPanel = panel("Administrator Activity", "Recent attributed actions from the server audit log");
  const activityHost = el("div", "stx-stack");
  activityPanel.append(activityHost);

  const editor = el("div", "stx-editor-shell");
  const listPanel = panel("Versions", "Drafts and published versions");
  const listHost = el("div", "stx-revision-list");
  listPanel.append(listHost);
  const detailPanel = panel("Review Changes", "Select a version to review exactly what changed");
  const detailHost = el("div", "stx-stack");
  detailPanel.append(detailHost);
  editor.append(listPanel, detailPanel);
  page.append(status, failureHost, activityPanel, editor);

  let payload: AdminStatePayload | null = null;
  let selectedRevisionId: string | null = null;
  let compareRevisionId: string | null = null;
  let validation: ValidationState = null;
  let generation = 0;

  const revisionById = (id: string | null): AdminRevision | undefined => payload?.history.find((revision) => revision.revision === id);
  const setStatus = (message: string, tone: Tone = "info"): void => {
    setAdminStatus(status, message, tone === "good" ? "success" : tone === "bad" ? "error" : tone === "warn" ? "warning" : "info");
  };

  const renderActivity = (events: readonly AdminAuditEvent[] | null): void => {
    activityHost.replaceChildren();
    if (events === null) {
      activityHost.append(notice("Audit history is restricted for this role. Revision review and server-enforced publish permissions remain available according to the effective role.", "warn"));
      return;
    }
    const visible = events.filter((event) => event.result !== "attempt").slice(0, 12);
    if (visible.length === 0) {
      activityHost.append(notice("No attributed administrator actions have been recorded yet."));
      return;
    }
    for (const event of visible) {
      const row = el("div", "stx-toggle-row");
      const copy = el("div");
      const actor = event.actor?.actorDisplayName ?? "Unknown actor";
      copy.append(
        el("strong", undefined, `${actor} ${actionLabel(event)}`),
        el("small", undefined, `${formattedTime(event.timestamp)} · ${humanize(event.domain)}${event.entityId ? ` · ${event.entityId}` : ""}`),
      );
      row.append(copy, badge(event.result.toUpperCase(), auditTone(event.result)));
      if (event.error) row.append(notice(event.error, "bad"));
      activityHost.append(row);
    }
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    if (!payload) return;
    for (const revision of payload.history) {
      const meta = relationMeta(revision);
      const item = el("button", `stx-revision${selectedRevisionId === revision.revision ? " active" : ""}`) as HTMLButtonElement;
      item.type = "button";
      item.append(
        el("strong", undefined, revision.message || "Untitled change"),
        badge(meta.label, meta.tone),
        el("span", undefined, revision.author || "Unknown author"),
        el("small", undefined, formattedTime(revision.createdAt)),
      );
      item.title = `Revision ${revision.revision}`;
      item.addEventListener("click", () => {
        selectedRevisionId = revision.revision;
        compareRevisionId = revision.parentRevision;
        validation = null;
        renderList();
        renderDetail();
      });
      listHost.append(item);
    }
  };

  const renderHumanDiff = (diff: readonly DiffEntry[]): HTMLElement => {
    const host = el("div", "stx-stack");
    if (diff.length === 0) {
      host.append(notice("No administrator-visible changes between these versions.", "good"));
      return host;
    }
    const grouped = new Map<string, DiffEntry[]>();
    for (const entry of diff) {
      const key = businessPath(entry.path).domain;
      grouped.set(key, [...(grouped.get(key) ?? []), entry]);
    }
    for (const [domain, entries] of grouped) {
      const group = panel(domain, `${entries.length} change${entries.length === 1 ? "" : "s"}`);
      for (const entry of entries.slice(0, 50)) {
        const info = businessPath(entry.path);
        const row = el("div", "stx-toggle-row");
        const copy = el("div");
        copy.append(el("strong", undefined, `${info.entity} · ${info.field}`));
        if (entry.kind === "added") copy.append(el("small", undefined, `Added: ${friendlyValue(entry.after)}`));
        else if (entry.kind === "removed") copy.append(el("small", undefined, `Removed: ${friendlyValue(entry.before)}`));
        else copy.append(el("small", undefined, `${friendlyValue(entry.before)} → ${friendlyValue(entry.after)}`));
        row.append(copy, badge(entry.kind.toUpperCase(), entry.kind === "added" ? "good" : entry.kind === "removed" ? "bad" : "warn"));
        group.append(row);
      }
      if (entries.length > 50) group.append(notice(`${entries.length - 50} additional changes are available in Advanced raw diff.`));
      host.append(group);
    }
    return host;
  };

  const renderDetail = (): void => {
    detailHost.replaceChildren();
    if (!payload) return;
    const selected = revisionById(selectedRevisionId) ?? payload.active;
    selectedRevisionId = selected.revision;
    const compare = revisionById(compareRevisionId ?? selected.parentRevision);
    const diff = diffValues(compare?.config ?? {}, selected.config);
    const meta = relationMeta(selected);

    const summary = panel(selected.message || "Untitled change", `${selected.author} · ${formattedTime(selected.createdAt)}`);
    const summaryActions = el("div", "st-admin-page-actions");
    summaryActions.append(badge(meta.label, meta.tone), badge(`${diff.length} CHANGES`, diff.length ? "warn" : "good"));
    summary.append(summaryActions);

    const compareBar = el("div", "st-admin-filterbar");
    const compareSelect = el("select", "st-admin-select") as HTMLSelectElement;
    compareSelect.setAttribute("aria-label", "Compare version against");
    compareSelect.append(new Option("Empty baseline", ""));
    for (const revision of payload.history) {
      if (revision.revision !== selected.revision) compareSelect.append(new Option(revision.message || formattedTime(revision.createdAt), revision.revision));
    }
    compareSelect.value = compare?.revision ?? "";
    compareSelect.addEventListener("change", () => {
      compareRevisionId = compareSelect.value || null;
      validation = null;
      renderDetail();
    });
    compareBar.append(el("span", undefined, "Compare against"), compareSelect);
    summary.append(compareBar, renderHumanDiff(diff));

    const raw = el("details", "st-admin-panel solid stx-panel");
    raw.append(el("summary", undefined, "Advanced · raw revision and path diff"));
    const pre = el("pre", "stx-diff");
    pre.textContent = diff.length === 0 ? "No raw differences." : diff.slice(0, 200).map((entry) => {
      if (entry.kind === "added") return `+ ${entry.path} = ${friendlyValue(entry.after)}`;
      if (entry.kind === "removed") return `- ${entry.path} = ${friendlyValue(entry.before)}`;
      return `~ ${entry.path}\n  - ${friendlyValue(entry.before)}\n  + ${friendlyValue(entry.after)}`;
    }).join("\n");
    raw.append(
      notice(`Revision: ${selected.revision} · Parent: ${selected.parentRevision ?? "none"} · Active: ${payload.state.activeRevision}`),
      pre,
    );

    const operation = panel("Publish Safety", "Server validation and compare-and-swap protect the active version");
    const eligible = selected.publishable || selected.rollbackEligible;
    operation.append(
      validation?.revision === selected.revision ? badge("VALIDATED", "good") : badge("VALIDATION REQUIRED", eligible ? "warn" : "info"),
      notice(
        selected.publishable
          ? "This draft is based on the current published version and can be published after validation."
          : selected.rollbackEligible
            ? "This is a previously published ancestor and can be selected as a rollback target after validation."
            : selected.active
              ? "This version is currently published."
              : "This draft is stale or outside the current published lineage. Create a fresh draft instead of overwriting newer work.",
        selected.publishable || selected.rollbackEligible ? "info" : selected.active ? "good" : "warn",
      ),
    );
    const actions = el("div", "st-admin-page-actions");
    const validateButton = btn("Validate", () => void validateSelected(validateButton));
    const rollbackButton = btn("Roll Back", () => void rollbackSelected(rollbackButton), "st-admin-btn danger");
    rollbackButton.disabled = !selected.rollbackEligible;
    const publishButton = btn("Publish", () => void publishSelected(publishButton), "st-admin-btn primary");
    publishButton.disabled = !selected.publishable;
    actions.append(validateButton, rollbackButton, publishButton);
    operation.append(actions);
    detailHost.append(summary, operation, raw);
  };

  const hydrate = async (preferredRevision: string | null = null): Promise<void> => {
    const current = ++generation;
    reload.disabled = true;
    validation = null;
    failureHost.replaceChildren();
    setStatus("Loading versions and attributed administrator activity…");
    try {
      const [state, audit] = await Promise.all([
        api.getState().then(validateState),
        api.getAudit(100).then((result) => result.events).catch(() => null),
      ]);
      if (current !== generation) return;
      payload = state;
      activeBadge.textContent = `Published · ${state.active.message || formattedTime(state.active.createdAt)}`;
      activeBadge.className = "st-admin-status good";
      selectedRevisionId = preferredRevision && revisionById(preferredRevision)
        ? preferredRevision
        : selectedRevisionId && revisionById(selectedRevisionId)
          ? selectedRevisionId
          : state.history.find((revision) => revision.publishable)?.revision ?? state.state.activeRevision;
      const selected = revisionById(selectedRevisionId) ?? state.active;
      compareRevisionId = compareRevisionId && revisionById(compareRevisionId) ? compareRevisionId : selected.parentRevision;
      renderActivity(audit);
      renderList();
      renderDetail();
      setStatus(`Loaded ${state.history.length} versions. Current published version is ${state.active.message || state.state.activeRevision}.`, "good");
    } catch (error: unknown) {
      if (current !== generation) return;
      payload = null;
      listHost.replaceChildren();
      detailHost.replaceChildren();
      activityHost.replaceChildren();
      activeBadge.textContent = "Published · unavailable";
      activeBadge.className = "st-admin-status bad";
      setStatus("History unavailable. Publish and rollback are closed.", "bad");
      renderAdminFailureState(failureHost, {
        title: "History & Publish unavailable",
        fallbackMessage: "The authoritative revision store could not be loaded. No production pointer action is available.",
        error,
        onRetry: () => void hydrate(preferredRevision),
      });
    } finally {
      if (current === generation) reload.disabled = false;
    }
  };

  const validateSelected = async (button: HTMLButtonElement): Promise<AdminRevisionValidation | null> => {
    if (!payload || !selectedRevisionId) return null;
    const revision = selectedRevisionId;
    button.disabled = true;
    setStatus(`Validating “${revisionById(revision)?.message || revision}”…`);
    try {
      const result = await api.validateRevision(revision);
      validation = { revision, result };
      renderDetail();
      setStatus("Validation passed. Publication eligibility was confirmed by the server.", "good");
      return result;
    } catch (error: unknown) {
      setStatus(`Validation failed: ${error instanceof Error ? error.message : "The version could not be validated."}`, "bad");
      return null;
    } finally {
      button.disabled = false;
    }
  };

  const publishSelected = async (button: HTMLButtonElement): Promise<void> => {
    if (!payload || !selectedRevisionId) return;
    const baseline = payload;
    const revision = selectedRevisionId;
    const title = revisionById(revision)?.message || revision;
    if (!window.confirm(`Publish “${title}”? This activates every reviewed change in this version.`)) return;
    button.disabled = true;
    try {
      const latest = validateState(await api.getState());
      if (latest.state.activeRevision !== baseline.state.activeRevision) throw new AdminApiError(409, "The published version changed while you were reviewing. Reload before publishing.");
      const gate = await api.validateRevision(revision);
      if (!gate.publishable) throw new AdminApiError(409, "This draft is no longer based on the current published version.");
      await api.publish(revision, latest.state.activeRevision);
      await hydrate(revision);
      setStatus(`Published “${title}” safely.`, "good");
    } catch (error: unknown) {
      setStatus(`Publish rejected: ${error instanceof Error ? error.message : "The publish request was rejected."}`, "bad");
      await hydrate(revision);
    } finally {
      button.disabled = false;
    }
  };

  const rollbackSelected = async (button: HTMLButtonElement): Promise<void> => {
    if (!payload || !selectedRevisionId) return;
    const baseline = payload;
    const revision = selectedRevisionId;
    const title = revisionById(revision)?.message || revision;
    if (!window.confirm(`Roll back production to “${title}”? The server will verify that it is a published ancestor first.`)) return;
    button.disabled = true;
    try {
      const latest = validateState(await api.getState());
      if (latest.state.activeRevision !== baseline.state.activeRevision) throw new AdminApiError(409, "The published version changed while you were reviewing. Reload before rolling back.");
      const gate = await api.validateRevision(revision);
      if (!gate.rollbackEligible) throw new AdminApiError(409, "This version is not an eligible published rollback target.");
      await api.rollback(revision, latest.state.activeRevision);
      await hydrate(revision);
      setStatus(`Production rolled back to “${title}” safely.`, "good");
    } catch (error: unknown) {
      setStatus(`Rollback rejected: ${error instanceof Error ? error.message : "The rollback request was rejected."}`, "bad");
      await hydrate(revision);
    } finally {
      button.disabled = false;
    }
  };

  void hydrate();
  return page;
}
