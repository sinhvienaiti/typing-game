// Release & History (/admin/shared/release): what runs now, where it is kept,
// the draft, every revision with Rollback, and the shared area's audit
// (docs/games/TYPING_FEEL_SERVICE.md §3.11, decision 4). Read only apart from
// Publish and Rollback; the Admin never runs git or a Drive upload.
import { openAdminConfirmDialog } from "../v2/admin-dialog";
import { createAdminEmptyState, createAdminPageHeader, createAdminValidationMessage, type AdminTone } from "../v2/admin-components";
import type { AdminAuditEvent } from "../api";
import { typingFeelApi, typingFeelErrorProblems } from "./api";
import { createTypingFeelReleaseBar, focusTypingFeelNotice, scopeList } from "./release-bar";
import { TYPING_FEEL_PERMISSIONS, TYPING_FEEL_ROUTES } from "./routes";
import { typingFeelSession as session } from "./session";
import type { TypingFeelChangeScope, TypingFeelExportStatus, TypingFeelHistory, TypingFeelHistoryEntry } from "./types";
import { bindSession, button, chip, commandLine, el, formatTime, panel, permissionButton, sessionGate } from "./ui";

const ACTIONS: Readonly<Record<string, string>> = {
  "typing-feel.revision.create": "Saved a draft",
  "typing-feel.publish": "Published to all games",
  "typing-feel.rollback": "Rolled back all games",
  // Add sound set (G7): these change Media V2 only, never a revision or the games.
  "typing-feel.job.format": "Formatted a take",
  "typing-feel.job.accept": "Accepted a new sound set",
  "typing-feel.job.discard": "Discarded a Format job",
};

function relationChip(entry: TypingFeelHistoryEntry): HTMLElement {
  if (entry.relation === "active") return chip("Live", "good");
  if (entry.relation === "ancestor") return chip("Published before", "info");
  if (entry.publication) return chip("Rolled back", "warn");
  if (entry.publishable) return chip("Ready draft", "warn");
  return chip("Old draft", "bad");
}

function auditTone(result: AdminAuditEvent["result"]): AdminTone {
  if (result === "success") return "good";
  if (result === "denied" || result === "error") return "bad";
  return "info";
}

function deploymentRow(label: string, tone: AdminTone, status: string, message: string, command?: string): HTMLElement {
  const row = el("div", "tf-deploy-row");
  const head = el("div", "tf-deploy-head");
  head.append(el("strong", undefined, label), chip(status, tone));
  row.append(head, el("p", undefined, message));
  if (command) row.append(commandLine(command));
  return row;
}

function deploymentRows(status: TypingFeelExportStatus): HTMLElement[] {
  const rows: HTMLElement[] = [];
  rows.push(status.local
    ? deploymentRow("This machine", "good", `Catalogue ${status.local.revision ?? "unknown"}`, `${status.local.sets} sets, published ${formatTime(status.local.publishedAt)} (typing-feel/public/v1/keys/keys-manifest.json).`)
    : deploymentRow("This machine", "bad", "No catalogue", "typing-feel/public/v1/keys/keys-manifest.json is missing; restart the Admin service to export the live revision again."));
  const git = status.git;
  if (git.status === "committed") rows.push(deploymentRow("Git", "good", "Committed", git.message ?? "The published JSON matches Git."));
  else if (git.status === "uncommitted") rows.push(deploymentRow("Git", "warn", "Not committed", `${git.changedFiles ?? 0} JSON ${git.changedFiles === 1 ? "file has" : "files have"} changes Git has not recorded. The Admin never runs git: ask for a commit of typing-feel/public.`));
  else if (git.status === "outside-repository") rows.push(deploymentRow("Git", "info", "Outside Git", git.message ?? "The published folder is not inside this Git checkout."));
  else rows.push(deploymentRow("Git", "warn", "Unknown", git.message ?? "git status could not be read."));
  const drive = status.drive;
  if (drive.status === "listed") rows.push(deploymentRow("Drive", "good", "Listed", `All ${drive.previews ?? 0} sets are in ${drive.lockFile ?? "typing-feel/media.md5"}.`));
  else if (drive.status === "not-backed-up") rows.push(deploymentRow("Drive", "warn", "Not on Drive", `${(drive.previews ?? 0) - (drive.previewsListed ?? 0)} of ${drive.previews ?? 0} sets are not in ${drive.lockFile ?? "the media lock"} yet. Back up by hand:`, drive.backupCommand));
  else if (drive.status === "no-lock-file") rows.push(deploymentRow("Drive", "warn", "Not tracked", drive.message ?? "The sound files are not tracked for Drive yet.", drive.backupCommand));
  else rows.push(deploymentRow("Drive", "warn", "Unknown", drive.message ?? "The media lock could not be read.", drive.backupCommand));
  const online = status.online;
  rows.push(deploymentRow("Online", online.status === "not-configured" ? "info" : "warn", online.status === "not-configured" ? "Not set up" : online.status, online.message ?? "", online.deployCommand));
  return rows;
}

export function renderTypingFeelRelease(navigate: (path: string) => void): HTMLElement {
  const page = el("div", "tf-page tf-release");
  let history: TypingFeelHistory | null = null;
  let historyError: string | null = null;
  let deployment: TypingFeelExportStatus | null = null;
  let deploymentError: string | null = null;
  let draftScope: { revision: string; scope: TypingFeelChangeScope | null; error: string | null } | null = null;
  let loadedFor: string | null = null;

  const refreshDetails = (force = false): void => {
    const ready = session.ready;
    if (!ready) return;
    const key = `${ready.state.activeRevision}:${ready.state.generation}:${ready.history.length}`;
    if (!force && loadedFor === key) return;
    loadedFor = key;
    typingFeelApi.history().then((value) => {
      history = value;
      historyError = null;
      render();
    }).catch((error: unknown) => {
      historyError = typingFeelErrorProblems(error).join(" ");
      render();
    });
    typingFeelApi.exportStatus().then((value) => {
      deployment = value;
      deploymentError = null;
      render();
    }).catch((error: unknown) => {
      deploymentError = typingFeelErrorProblems(error).join(" ");
      render();
    });
  };

  const reload = button("Reload", () => {
    void session.load().then(() => refreshDetails(true));
  });
  page.append(createAdminPageHeader({
    eyebrow: "All games · Typing Feel",
    title: "Release & History",
    subtitle: "What every game reads now, where it is kept, the draft waiting for review, and every published revision with Rollback.",
    actions: [reload],
  }));
  const body = el("div", "tf-body");
  page.append(body, createTypingFeelReleaseBar(session, "release", navigate));

  const confirmRollback = (target: TypingFeelHistoryEntry, trigger: HTMLElement): void => {
    const ready = session.ready;
    if (!ready) return;
    const detail = el("div", "tf-dialog-detail");
    detail.append(chip("Affects all games", "warn"), el("p", "tf-hint", "Loading what changes…"));
    openAdminConfirmDialog({
      eyebrow: "All games · Typing Feel",
      title: `Roll back all games to ${target.revision}?`,
      message: `Every game goes back to ${target.revision}${target.publication ? ` (catalogue ${target.publication.catalogueRevision})` : ""} on its next load, replacing live revision ${ready.state.activeRevision}. The current revision stays in History and can be published again.`,
      detail,
      tone: "danger",
      confirmLabel: "Roll back all games",
      returnFocus: trigger,
      onConfirm: async () => {
        await session.rollback(target.revision);
        refreshDetails(true);
        focusTypingFeelNotice(page);
      },
    });
    typingFeelApi.rollbackChangeScope(target.revision).then((scope) => {
      detail.replaceChildren(chip("Affects all games", "warn"), scopeList(scope));
    }).catch((error: unknown) => {
      detail.replaceChildren(chip("Affects all games", "warn"), el("p", "tf-hint", `What changes could not be listed: ${typingFeelErrorProblems(error).join(" ")}`));
    });
  };

  const render = (): void => {
    const gate = sessionGate(session, () => void session.load());
    if (gate) {
      body.replaceChildren(gate);
      return;
    }
    refreshDetails();
    const ready = session.ready!;
    const active = ready.active;
    const content = el("div", "tf-release-layout");

    const live = panel("Live now", "The revision every game reads on its next load.");
    const facts = el("dl", "tf-facts");
    const fact = (term: string, value: string) => {
      const item = el("div");
      item.append(el("dt", undefined, term), el("dd", undefined, value));
      facts.append(item);
    };
    const shownSets = active.config.keyboard.sets.filter((set) => set.enabled).length;
    const defaultName = active.config.keyboard.sets.find((set) => set.id === active.config.keyboard.defaultSet)?.name ?? active.config.keyboard.defaultSet;
    fact("Revision", active.revision);
    fact("Catalogue", active.publication ? `${active.publication.catalogueRevision} · published ${formatTime(active.publication.publishedAt)}` : "Not exported yet");
    fact("Sound sets", `${shownSets} shown · ${active.config.keyboard.sets.length - shownSets} hidden`);
    fact("Default", defaultName);
    const effects = active.config.effects.defaults;
    fact("Typing effects", `${effects.style} · ${effects.intensity} · ${effects.size} · ${Math.round(effects.volume * 100)}%`);
    fact("Changed", `${formatTime(ready.state.updatedAt)} (generation ${ready.state.generation})`);
    live.body.append(facts);
    const startup = ready.startup;
    if (startup?.status === "error") {
      const problems = Array.isArray(startup["problems"]) ? (startup["problems"] as unknown[]).map(String).join(" ") : "See the Admin server log.";
      live.body.append(createAdminValidationMessage({ tone: "bad", title: "Start-up check failed", message: `The published catalogue was left as it is. ${problems}` }));
    }
    if (!ready.local.matchesActive) {
      live.body.append(createAdminValidationMessage({ tone: "warn", title: "Catalogue on disk differs", message: `typing-feel/public says ${ready.local.catalogue?.revision ?? "nothing"}; the live revision is ${active.publication?.catalogueRevision ?? active.revision}. Restart the Admin service to export it again.` }));
    }

    const deploy = panel("Where it is kept", "Decision 4: the catalogue goes to Git, the sounds to Drive. The Admin only reads this.");
    if (deployment) deploy.body.append(...deploymentRows(deployment));
    else if (deploymentError) deploy.body.append(createAdminValidationMessage({ tone: "bad", message: deploymentError }));
    else deploy.body.append(el("p", "tf-hint", "Reading Git and Drive status…"));

    const top = el("div", "tf-release-top");
    top.append(live.root, deploy.root);
    content.append(top);

    const draftPanel = panel("Draft", "The newest draft saved on top of the live revision since it went live. Older drafts stay in History.");
    const source = session.source;
    const draft = ready.draft;
    if (session.dirty) {
      draftPanel.body.append(createAdminValidationMessage({ tone: "warn", title: "Unsaved edits", message: `${session.changeSummary.parts.join(", ")} changed in this tab and not saved yet. Save draft in the bar below, or discard them.` }));
    }
    if (source && source.relation === "draft" && source.revision !== draft?.revision) {
      draftPanel.body.append(createAdminValidationMessage({ tone: "info", message: `The working copy is ${source.revision}${source.publication ? ", a rolled-back revision" : ""}.` }));
    }
    if (!draft) {
      draftPanel.body.append(createAdminEmptyState({ title: "No draft waiting", message: "Edit Keyboard Sounds or Typing Effects, then Save draft. The draft appears here for review." }));
    } else {
      const head = el("div", "tf-draft-head");
      const copy = el("div");
      copy.append(el("strong", undefined, draft.revision), el("span", undefined, `${draft.message} · ${draft.author} · ${formatTime(draft.createdAt)}`));
      head.append(copy, chip("Affects all games", "warn"));
      draftPanel.body.append(head);
      if (draftScope?.revision !== draft.revision) {
        draftScope = { revision: draft.revision, scope: null, error: null };
        const wanted = draft.revision;
        typingFeelApi.changeScope(wanted).then((scope) => {
          if (draftScope?.revision !== wanted) return;
          draftScope = { revision: wanted, scope, error: null };
          render();
        }).catch((error: unknown) => {
          if (draftScope?.revision !== wanted) return;
          draftScope = { revision: wanted, scope: null, error: typingFeelErrorProblems(error).join(" ") };
          render();
        });
      }
      if (draftScope.scope) draftPanel.body.append(scopeList(draftScope.scope));
      else if (draftScope.error) draftPanel.body.append(createAdminValidationMessage({ tone: "bad", message: draftScope.error }));
      else draftPanel.body.append(el("p", "tf-hint", "Listing what changes…"));
      const actions = el("div", "tf-row-actions");
      if (source?.revision !== draft.revision && !session.dirty) actions.append(button("Use as working copy", () => void session.load({ sourceRevision: draft.revision }), "st-admin-btn tf-mini"));
      actions.append(button("Open Keyboard Sounds", () => navigate(TYPING_FEEL_ROUTES.keyboardSounds), "st-admin-btn tf-mini"), button("Open Typing Effects", () => navigate(TYPING_FEEL_ROUTES.typingEffects), "st-admin-btn tf-mini"));
      draftPanel.body.append(actions, el("p", "tf-hint", "Review and Publish run from the bar below."));
    }
    content.append(draftPanel.root);

    const revisions = panel("History", "Newest first. Rollback restores an earlier published revision for every game.");
    const list = el("ol", "tf-history");
    const entries = history?.history ?? ready.history;
    for (const entry of entries) {
      const row = el("li", `tf-history-row ${entry.relation ?? ""}`.trim());
      const main = el("div", "tf-history-main");
      const titleRow = el("div", "tf-history-title");
      titleRow.append(el("strong", undefined, entry.revision), relationChip(entry));
      if (entry.revision === source?.revision && entry.relation !== "active") titleRow.append(chip("Working copy", "info"));
      main.append(titleRow, el("span", undefined, entry.message));
      const meta = [`${entry.author} · ${formatTime(entry.createdAt)}`];
      if (entry.publication) meta.push(`catalogue ${entry.publication.catalogueRevision}, first published ${formatTime(entry.publication.publishedAt)}`);
      if (entry.parentRevision) meta.push(`based on ${entry.parentRevision}`);
      main.append(el("small", undefined, meta.join(" · ")));
      row.append(main);
      const actions = el("div", "tf-row-actions");
      if (entry.rollbackEligible) {
        const rollback = permissionButton("Roll back to this", TYPING_FEEL_PERMISSIONS.rollback, ready.permissions.rollback, () => confirmRollback(entry, rollback), "st-admin-btn tf-mini danger");
        rollback.disabled = session.busy !== null;
        actions.append(rollback);
      } else if (entry.relation === "draft" && entry.publishable && entry.revision !== source?.revision && !session.dirty) {
        // Only a role that can publish is offered to publish again; any role may load a revision to review it.
        const again = Boolean(entry.publication) && ready.permissions.publish;
        const use = button(again ? "Use to publish again" : "Use as working copy", () => void session.load({ sourceRevision: entry.revision }), "st-admin-btn tf-mini");
        use.title = again
          ? "Load this rolled-back revision into the bar, then Review and Publish it again."
          : ready.permissions.publish ? "Load this draft into the bar to review and publish it." : "Load this revision into the bar to review it.";
        actions.append(use);
      }
      row.append(actions);
      list.append(row);
    }
    revisions.body.append(list);
    if (historyError) revisions.body.append(createAdminValidationMessage({ tone: "bad", message: historyError }));
    if (!ready.permissions.rollback) revisions.body.append(el("p", "tf-hint", "Rollback needs shared.publish; your role can only read the history."));

    const activity = panel("Activity", "Typing Feel actions from the shared audit log.");
    if (!history) activity.body.append(el("p", "tf-hint", historyError ? "Activity unavailable." : "Loading activity…"));
    else if (history.eventsHidden || history.events === null) activity.body.append(createAdminValidationMessage({ tone: "info", message: "Reading the audit log needs audit.read." }));
    else {
      const events = history.events.filter((event) => event.result !== "attempt").slice(0, 30);
      if (events.length === 0) activity.body.append(createAdminEmptyState({ title: "No Typing Feel activity yet", message: "Saved drafts, publishes and rollbacks appear here." }));
      const log = el("ol", "tf-activity");
      for (const event of events) {
        const row = el("li");
        const copy = el("div");
        copy.append(el("strong", undefined, ACTIONS[event.action] ?? event.action), el("span", undefined, `${event.actor?.actorDisplayName || event.actor?.actorId || "Admin"}${event.entityId ? ` · ${event.entityId}` : ""}${event.error ? ` · ${event.error}` : ""}`));
        row.append(copy, chip(event.result, auditTone(event.result)), el("time", undefined, formatTime(event.timestamp)));
        log.append(row);
      }
      activity.body.append(log);
    }
    const bottom = el("div", "tf-release-bottom");
    bottom.append(revisions.root, activity.root);
    content.append(bottom);
    body.replaceChildren(content);
  };

  bindSession(page, session, render);
  render();
  void session.load();
  return page;
}
