import {
  AdminApiError,
  SpaceTypingAdminApi,
  type AdminRevision,
  type AdminRevisionValidation,
  type AdminStatePayload,
} from "./api";

const BASE = "/admin/space-typing";
const api = new SpaceTypingAdminApi();

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type DiffKind = "added" | "removed" | "modified";
type DiffEntry = { kind: DiffKind; path: string; before?: unknown; after?: unknown };

type ValidationState = {
  revision: string;
  result: AdminRevisionValidation;
} | null;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function btn(label: string, onClick: () => void = () => undefined, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

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

function header(eyebrow: string, title: string, description: string, actions: readonly HTMLElement[] = []): HTMLElement {
  const root = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(el("div", "st-admin-eyebrow", eyebrow), el("h1", undefined, title), el("p", undefined, description));
  root.append(copy);
  if (actions.length > 0) {
    const tools = el("div", "st-admin-page-actions");
    tools.append(...actions);
    root.append(tools);
  }
  return root;
}

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `stx-notice ${tone}`, text);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function sameScalar(a: unknown, b: unknown): boolean {
  return Object.is(a, b) || JSON.stringify(a) === JSON.stringify(b);
}

function diffValues(before: unknown, after: unknown, path = ""): DiffEntry[] {
  if (sameScalar(before, after)) return [];
  if (isRecord(before) && isRecord(after)) {
    const keys = [...new Set([...Object.keys(before), ...Object.keys(after)])].sort();
    const result: DiffEntry[] = [];
    for (const key of keys) {
      const nextPath = path ? `${path}.${key}` : key;
      if (!(key in before)) result.push({ kind: "added", path: nextPath, after: after[key] });
      else if (!(key in after)) result.push({ kind: "removed", path: nextPath, before: before[key] });
      else result.push(...diffValues(before[key], after[key], nextPath));
    }
    return result;
  }
  return [{ kind: "modified", path: path || "config", before, after }];
}

function shortValue(value: unknown): string {
  if (value === undefined) return "∅";
  const raw = typeof value === "string" ? value : JSON.stringify(value);
  if (raw.length <= 120) return raw;
  return `${raw.slice(0, 117)}…`;
}

function relationMeta(revision: AdminRevision): { label: string; tone: Tone } {
  if (revision.relation === "active" || revision.active) return { label: "ACTIVE", tone: "good" };
  if (revision.relation === "ancestor") return { label: "PUBLISHED HISTORY", tone: "info" };
  if (revision.publishable) return { label: "FRESH DRAFT", tone: "warn" };
  return { label: "STALE DRAFT", tone: "bad" };
}

function formattedTime(value: string): string {
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? value : date.toLocaleString();
}

function topDomains(diff: readonly DiffEntry[]): string[] {
  return [...new Set(diff.map((entry) => entry.path.split(".")[0] || "config"))].sort();
}

function summarize(diff: readonly DiffEntry[]): { added: number; modified: number; removed: number } {
  return {
    added: diff.filter((entry) => entry.kind === "added").length,
    modified: diff.filter((entry) => entry.kind === "modified").length,
    removed: diff.filter((entry) => entry.kind === "removed").length,
  };
}

export function renderPhaseBHistory(navigate: Navigate): HTMLElement {
  void navigate;
  const page = el("div");
  const activeBadge = badge("ACTIVE · loading", "info");
  const generationBadge = badge("GEN · —", "info");
  const reload = btn("Reload", () => void hydrate(selectedRevisionId));
  page.append(header(
    "System · Immutable Operations · Phase B",
    "History & Publish",
    "Real revision history, config diff, current validation, fresh-draft publish guard and ancestor-only rollback. Every production pointer change uses expected-active CAS.",
    [activeBadge, generationBadge, reload],
  ));

  const status = notice("Loading revision store…", "info");
  const shell = el("div", "stx-editor-shell");
  const listPanel = panel("Revisions", "Immutable revision store");
  const listHost = el("div", "stx-revision-list");
  listPanel.append(listHost);
  const detailPanel = panel("Revision", "Select a revision to inspect");
  const detailHost = el("div", "stx-stack");
  detailPanel.append(detailHost);
  shell.append(listPanel, detailPanel);
  page.append(status, shell);

  let payload: AdminStatePayload | null = null;
  let selectedRevisionId: string | null = null;
  let compareRevisionId: string | null = null;
  let validation: ValidationState = null;

  const setStatus = (message: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = message;
  };

  const revisionById = (id: string | null): AdminRevision | undefined =>
    payload?.history.find((revision) => revision.revision === id);

  const renderList = (): void => {
    listHost.replaceChildren();
    if (payload === null) return;
    for (const revision of payload.history) {
      const meta = relationMeta(revision);
      const item = el("button", `stx-revision${selectedRevisionId === revision.revision ? " active" : ""}`) as HTMLButtonElement;
      item.type = "button";
      item.append(
        el("strong", undefined, revision.revision),
        badge(meta.label, meta.tone),
        el("span", undefined, revision.message || "Untitled revision"),
        el("small", undefined, `${revision.author} · ${formattedTime(revision.createdAt)}`),
      );
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

  const renderDetail = (): void => {
    detailHost.replaceChildren();
    if (payload === null) return;
    const selected = revisionById(selectedRevisionId) ?? payload.active;
    selectedRevisionId = selected.revision;
    const meta = relationMeta(selected);
    const compare = revisionById(compareRevisionId ?? selected.parentRevision);
    const beforeConfig = compare?.config ?? {};
    const diff = diffValues(beforeConfig, selected.config);
    const counts = summarize(diff);
    const domains = topDomains(diff);

    const headline = el("div", "st-admin-page-actions");
    headline.append(
      badge(meta.label, meta.tone),
      badge(`+${counts.added}`, "good"),
      badge(`~${counts.modified}`, "warn"),
      badge(`-${counts.removed}`, "bad"),
    );
    detailHost.append(headline);

    const facts = panel("Revision Metadata", `${selected.revision} · immutable`);
    const factsGrid = el("div", "stx-grid");
    for (const [label, value] of [
      ["Author", selected.author],
      ["Created", formattedTime(selected.createdAt)],
      ["Parent", selected.parentRevision ?? "—"],
      ["Changed Domains", domains.join(", ") || "None"],
    ] as const) {
      const cell = el("div", "stx-stat");
      cell.append(el("span", undefined, label), el("strong", undefined, value));
      factsGrid.append(cell);
    }
    facts.append(factsGrid, notice(selected.message || "No revision message.", "info"));

    const comparePanel = panel("Config Diff", "Compare immutable config snapshots");
    const compareRow = el("div", "st-admin-filterbar");
    const compareSelect = el("select", "st-admin-select") as HTMLSelectElement;
    compareSelect.setAttribute("aria-label", "Compare revision against");
    compareSelect.append(new Option("Empty baseline", ""));
    for (const revision of payload.history) {
      if (revision.revision === selected.revision) continue;
      compareSelect.append(new Option(`${revision.revision} · ${revision.message}`, revision.revision));
    }
    compareSelect.value = compare?.revision ?? "";
    compareSelect.addEventListener("change", () => {
      compareRevisionId = compareSelect.value || null;
      validation = null;
      renderDetail();
    });
    compareRow.append(el("span", undefined, "Compare against"), compareSelect);
    comparePanel.append(compareRow);

    const diffBlock = el("pre", "stx-diff");
    if (diff.length === 0) {
      diffBlock.textContent = "No config differences.";
    } else {
      diffBlock.textContent = diff.slice(0, 200).map((entry) => {
        if (entry.kind === "added") return `+ ${entry.path} = ${shortValue(entry.after)}`;
        if (entry.kind === "removed") return `- ${entry.path} = ${shortValue(entry.before)}`;
        return `~ ${entry.path}\n  - ${shortValue(entry.before)}\n  + ${shortValue(entry.after)}`;
      }).join("\n");
      if (diff.length > 200) diffBlock.textContent += `\n… ${diff.length - 200} more changes`;
    }
    comparePanel.append(diffBlock);

    const gate = panel("Validation & CAS Gate", "Backend-owned eligibility; UI never infers permission to mutate the active pointer");
    const gateStatus = validation?.revision === selected.revision
      ? badge("VALIDATED · PASS", "good")
      : badge("VALIDATION · NOT RUN", "warn");
    const gateCopy = notice(
      selected.publishable
        ? `Fresh draft: parent matches active ${payload.state.activeRevision}. Publish is eligible after validation.`
        : selected.rollbackEligible
          ? `Published ancestor of active ${payload.state.activeRevision}. Rollback is eligible after validation.`
          : selected.active
            ? "This is the active revision. No pointer change is needed."
            : `Stale/non-lineage draft: parent ${selected.parentRevision ?? "—"} does not match active ${payload.state.activeRevision}. Create a fresh reviewed draft instead of overwriting newer changes.`,
      selected.publishable || selected.rollbackEligible ? "info" : selected.active ? "good" : "warn",
    );
    gate.append(gateStatus, gateCopy);

    const actions = el("div", "st-admin-page-actions");
    const validateButton = btn("Validate", () => void validateSelected(validateButton), "st-admin-btn");
    const publishButton = btn("Publish", () => void publishSelected(publishButton), "st-admin-btn primary");
    publishButton.disabled = !selected.publishable;
    publishButton.title = selected.publishable ? "Validate and publish this fresh draft." : "Only a fresh draft based on the current active revision can be published.";
    const rollbackButton = btn("Rollback", () => void rollbackSelected(rollbackButton), "st-admin-btn danger");
    rollbackButton.disabled = !selected.rollbackEligible;
    rollbackButton.title = selected.rollbackEligible ? "Validate and move the active pointer to this published ancestor." : "Rollback is limited to published ancestors of the active revision.";
    actions.append(validateButton, rollbackButton, publishButton);
    gate.append(actions);

    detailHost.append(facts, comparePanel, gate);
  };

  const hydrate = async (preferredRevision: string | null = null): Promise<void> => {
    setStatus("Loading immutable revision history…", "info");
    try {
      payload = await api.getState();
      activeBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
      generationBadge.textContent = `GEN · ${payload.state.generation}`;
      selectedRevisionId = preferredRevision && revisionById(preferredRevision)
        ? preferredRevision
        : selectedRevisionId && revisionById(selectedRevisionId)
          ? selectedRevisionId
          : payload.history.find((revision) => revision.publishable)?.revision ?? payload.state.activeRevision;
      const selected = revisionById(selectedRevisionId) ?? payload.active;
      compareRevisionId = compareRevisionId && revisionById(compareRevisionId)
        ? compareRevisionId
        : selected.parentRevision;
      validation = null;
      renderList();
      renderDetail();
      setStatus(`Loaded ${payload.history.length} immutable revisions. Active pointer is ${payload.state.activeRevision}.`, "good");
    } catch (error: unknown) {
      setStatus(`Admin service unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad");
    }
  };

  const validateSelected = async (button: HTMLButtonElement): Promise<AdminRevisionValidation | null> => {
    if (payload === null || selectedRevisionId === null) return null;
    button.disabled = true;
    setStatus(`Validating ${selectedRevisionId} against current schema…`, "info");
    try {
      const result = await api.validateRevision(selectedRevisionId);
      validation = { revision: selectedRevisionId, result };
      await hydrate(selectedRevisionId);
      validation = { revision: selectedRevisionId, result };
      renderDetail();
      setStatus(`Validation PASS for ${selectedRevisionId}. Backend relation: ${result.relation}.`, "good");
      return result;
    } catch (error: unknown) {
      setStatus(`Validation failed: ${error instanceof Error ? error.message : String(error)}`, "bad");
      return null;
    } finally {
      button.disabled = false;
    }
  };

  const publishSelected = async (button: HTMLButtonElement): Promise<void> => {
    if (payload === null || selectedRevisionId === null) return;
    const revision = selectedRevisionId;
    if (!window.confirm(`Publish ${revision}? This moves the active runtime pointer after validation.`)) return;
    button.disabled = true;
    try {
      const latest = await api.getState();
      if (latest.state.activeRevision !== payload.state.activeRevision) {
        throw new AdminApiError(409, `Active revision changed from ${payload.state.activeRevision} to ${latest.state.activeRevision}. Reload before publishing.`);
      }
      const gate = await api.validateRevision(revision);
      if (!gate.publishable) throw new AdminApiError(409, `Revision ${revision} is no longer a fresh publishable draft.`);
      await api.publish(revision, latest.state.activeRevision);
      await hydrate(revision);
      setStatus(`Published ${revision}. Active pointer advanced by CAS.`, "good");
    } catch (error: unknown) {
      setStatus(`Publish rejected: ${error instanceof Error ? error.message : String(error)}`, "bad");
      await hydrate(revision);
    } finally {
      button.disabled = false;
    }
  };

  const rollbackSelected = async (button: HTMLButtonElement): Promise<void> => {
    if (payload === null || selectedRevisionId === null) return;
    const revision = selectedRevisionId;
    if (!window.confirm(`Rollback active runtime to published ancestor ${revision}?`)) return;
    button.disabled = true;
    try {
      const latest = await api.getState();
      if (latest.state.activeRevision !== payload.state.activeRevision) {
        throw new AdminApiError(409, `Active revision changed from ${payload.state.activeRevision} to ${latest.state.activeRevision}. Reload before rollback.`);
      }
      const gate = await api.validateRevision(revision);
      if (!gate.rollbackEligible) throw new AdminApiError(409, `Revision ${revision} is not a published ancestor of the current active revision.`);
      await api.rollback(revision, latest.state.activeRevision);
      await hydrate(revision);
      setStatus(`Rollback complete. Active pointer now targets ${revision}.`, "good");
    } catch (error: unknown) {
      setStatus(`Rollback rejected: ${error instanceof Error ? error.message : String(error)}`, "bad");
      await hydrate(revision);
    } finally {
      button.disabled = false;
    }
  };

  void hydrate();
  return page;
}
