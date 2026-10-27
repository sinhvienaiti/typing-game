import "./dashboard.css";
import {
  type AdminActor,
  type AdminAuditEvent,
  type AdminStatePayload,
  SpaceTypingAdminApi,
} from "../api";
import { adminErrorMessage } from "../admin-http";
import type { AdminHelpScope } from "./admin-help";
import {
  createAdminCardGrid,
  createAdminEmptyState,
  createAdminErrorState,
  createAdminPageHeader,
  createAdminSkeleton,
  createAdminStatusChip,
} from "./admin-components";

const BASE = "/admin/space-typing";

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function navButton(label: string, path: string, navigate: (path: string) => void): HTMLButtonElement {
  const button = element("button", "st-admin-btn", label);
  button.type = "button";
  button.addEventListener("click", () => navigate(path));
  return button;
}

function formatDateTime(value: string): string {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "Unknown";
  return new Intl.DateTimeFormat(undefined, {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(date);
}

function humanAction(event: AdminAuditEvent): string {
  const action = event.action;
  if (action === "revision.create") return "Saved a draft";
  if (action === "revision.publish") return "Published changes";
  if (action === "revision.rollback") return "Rolled back a published version";
  if (action === "media.music.upload") return "Uploaded a music track";
  if (action === "media.music.delete") return "Removed an Admin-uploaded music track";
  return action.replaceAll(".", " ");
}

function metricCard(label: string, value: string, detail: string, tone: "info" | "good" | "warn" | "bad" = "info"): HTMLElement {
  const card = element("article", "st-admin-v2-dashboard-metric");
  card.append(createAdminStatusChip(label, tone), element("strong", "st-admin-v2-dashboard-value", value), element("span", "st-admin-v2-dashboard-detail", detail));
  return card;
}

function actionCard(title: string, message: string, action: HTMLElement): HTMLElement {
  const card = element("article", "st-admin-v2-dashboard-action");
  card.append(element("h3", undefined, title), element("p", undefined, message), action);
  return card;
}

function activityList(events: AdminAuditEvent[]): HTMLElement {
  const successful = events.filter((event) => event.result === "success").slice(0, 6);
  if (successful.length === 0) {
    return createAdminEmptyState({
      title: "No recorded admin activity yet",
      message: "Activity appears here after successful draft, publish, rollback or Admin-managed media changes.",
    });
  }

  const list = element("div", "st-admin-v2-activity-list");
  for (const event of successful) {
    const row = element("article", "st-admin-v2-activity-row");
    const copy = element("div");
    copy.append(
      element("strong", undefined, humanAction(event)),
      element("span", undefined, event.actor?.actorDisplayName || event.actor?.actorId || "Admin"),
    );
    row.append(copy, element("time", undefined, formatDateTime(event.timestamp)));
    list.append(row);
  }
  return list;
}

function renderDashboardData(
  body: HTMLElement,
  state: AdminStatePayload,
  actor: AdminActor,
  trackCount: number,
  auditEvents: AdminAuditEvent[],
  navigate: (path: string) => void,
): void {
  const drafts = state.history.filter((revision) => revision.relation === "draft");
  const publishableDrafts = drafts.filter((revision) => revision.publishable === true);
  const staleDrafts = drafts.filter((revision) => revision.publishable !== true);
  const maintenance = state.active.config.system?.maintenance.enabled === true;

  const metrics = createAdminCardGrid(
    metricCard("Live version", `#${state.state.generation}`, `Published ${formatDateTime(state.state.updatedAt)}`, "good"),
    metricCard("Drafts", String(drafts.length), `${publishableDrafts.length} ready to review`, drafts.length > 0 ? "warn" : "good"),
    metricCard("Music", String(trackCount), "Tracks in the canonical music catalog", "info"),
    metricCard("Signed in", actor.actorDisplayName || actor.actorId, actor.role.replaceAll("-", " "), "info"),
  );

  const needs = element("section", "st-admin-v2-dashboard-section");
  needs.append(element("h2", undefined, "Needs attention"));
  const attention = element("div", "st-admin-v2-dashboard-attention");

  if (publishableDrafts.length > 0) {
    attention.append(actionCard(
      `${publishableDrafts.length} ${publishableDrafts.length === 1 ? "draft is" : "drafts are"} ready for review`,
      "Review the complete change scope before publishing. Publishing activates the full target revision, not only the screen you last edited.",
      navButton("Review drafts", `${BASE}/history`, navigate),
    ));
  }
  if (staleDrafts.length > 0) {
    attention.append(actionCard(
      `${staleDrafts.length} older ${staleDrafts.length === 1 ? "draft needs" : "drafts need"} attention`,
      "These drafts are no longer based on the active version and cannot be published directly. Re-open the relevant workflow and create a fresh draft from the current live version.",
      navButton("Open history", `${BASE}/history`, navigate),
    ));
  }
  if (maintenance) {
    attention.append(actionCard(
      "Maintenance mode is enabled",
      "Players may see the configured maintenance state. Review General Settings before the next release or live session.",
      navButton("Review settings", `${BASE}/settings`, navigate),
    ));
  }
  if (attention.childElementCount === 0) {
    attention.append(createAdminEmptyState({
      title: "No immediate action detected",
      message: "Available Admin state has no publishable/stale drafts and maintenance mode is off.",
    }));
  }
  needs.append(attention);

  const activity = element("section", "st-admin-v2-dashboard-section");
  activity.append(element("h2", undefined, "Recent admin activity"), activityList(auditEvents));

  const quick = element("section", "st-admin-v2-dashboard-section");
  quick.append(element("h2", undefined, "Quick actions"));
  const quickActions = element("div", "st-admin-v2-dashboard-quick");
  quickActions.append(
    navButton("History & Publish", `${BASE}/history`, navigate),
    navButton("Music Library", `${BASE}/music-library`, navigate),
    navButton("General Settings", `${BASE}/settings`, navigate),
  );
  quick.append(quickActions);

  body.replaceChildren(metrics, needs, activity, quick);
}

export function renderAdminV2Dashboard(navigate: (path: string) => void, helpScope: AdminHelpScope): HTMLElement {
  const root = element("section", "st-admin-v2-dashboard");
  root.append(createAdminPageHeader({
    eyebrow: "Command Center",
    title: "Dashboard",
    subtitle: "Live administrator state from the revision store, audit log and canonical music catalog — no placeholder metrics.",
    helpScope,
    help: {
      title: "Dashboard data",
      content: "This dashboard only shows signals backed by Admin data that exists today. Future Live Ops, player and commerce metrics will appear only after their canonical services exist.",
    },
  }));

  const body = element("div", "st-admin-v2-dashboard-body");
  body.append(createAdminSkeleton(6));
  root.append(body);

  requestAnimationFrame(async () => {
    const api = new SpaceTypingAdminApi();
    try {
      const [state, actor, music] = await Promise.all([
        api.getState(),
        api.getActor(),
        api.getMusicCatalogSummary(),
      ]);
      if (!root.isConnected) return;

      let auditEvents: AdminAuditEvent[] = [];
      if (actor.permissions.includes("audit.read")) {
        try {
          auditEvents = (await api.getAudit(12)).events;
        } catch {
          // Dashboard remains useful when optional activity history is temporarily unavailable.
        }
      }
      if (!root.isConnected) return;
      renderDashboardData(body, state, actor, music.tracks.length, auditEvents, navigate);
    } catch (error) {
      if (!root.isConnected) return;
      body.replaceChildren(createAdminErrorState({
        title: "Dashboard unavailable",
        message: adminErrorMessage(error, "Unable to load the current Admin state."),
        retry: () => navigate(BASE),
      }));
    }
  });

  return root;
}
