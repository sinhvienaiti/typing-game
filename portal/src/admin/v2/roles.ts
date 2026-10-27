import { SpaceTypingAdminApi, type AdminActor } from "../api";
import type { AdminHelpScope } from "./admin-help";

type PermissionDefinition = Readonly<{ id: string; label: string; group: string; dangerous: boolean }>;
type RoleTemplate = Readonly<{ id: string; label: string; description: string; permissions: readonly string[] }>;
type RoleAwareActor = AdminActor & Readonly<{
  roleKnown?: boolean;
  permissionOverrides?: readonly Readonly<{ operation: "add" | "remove"; permission: string }>[];
  permissionCatalog?: readonly PermissionDefinition[];
  roleTemplates?: readonly RoleTemplate[];
  roleAssignmentOwner?: string;
}>;

const api = new SpaceTypingAdminApi();

type Tone = "good" | "warn" | "bad" | "info";
function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
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
function permissionLabel(permission: string, catalog: readonly PermissionDefinition[]): string {
  return catalog.find((entry) => entry.id === permission)?.label ?? permission;
}

export function renderAdminV2Roles(help?: AdminHelpScope): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "System · Access Control"),
    el("h1", undefined, "Roles & Permissions"),
    el("p", undefined, "Review server-enforced role templates and the effective permissions of this Admin service. Role assignment stays deployment-owned because there is no canonical player/account administration backend."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("SERVER ENFORCED", "good"), badge("DEPLOYMENT ASSIGNED", "info"));
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading effective access…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  void api.getActor().then((rawActor) => {
    const actor = rawActor as RoleAwareActor;
    const catalog = actor.permissionCatalog ?? [];
    const templates = actor.roleTemplates ?? [];
    const current = templates.find((entry) => entry.id === actor.role);
    const effective = new Set(actor.permissions);
    status.className = `stx-notice ${actor.roleKnown === false ? "warn" : "good"}`;
    status.textContent = actor.roleKnown === false
      ? `Current deployment role “${actor.role}” is unknown; effective permissions fail closed.`
      : `${actor.actorDisplayName} · ${current?.label ?? actor.role} · ${actor.permissions.length} effective permissions.`;

    const currentPanel = panel("Current Access", "Effective permissions enforced by the Admin service");
    const currentHead = el("div", "st-admin-page-actions");
    currentHead.append(badge(current?.label ?? actor.role, actor.roleKnown === false ? "warn" : "good"));
    if ((actor.permissionOverrides?.length ?? 0) > 0) currentHead.append(badge("DEPLOYMENT OVERRIDES", "warn"));
    currentPanel.append(currentHead);
    const currentGrid = el("div", "stx-grid");
    for (const permission of catalog) {
      const granted = effective.has(permission.id);
      const row = el("div", "stx-toggle-row");
      const text = el("div");
      text.append(el("strong", undefined, permission.label));
      text.append(el("small", undefined, permission.group));
      row.append(text, badge(granted ? "ALLOWED" : "DENIED", granted ? (permission.dangerous ? "warn" : "good") : "info"));
      if (permission.dangerous) row.title = "Sensitive permission: publishing, destructive media operations, rollback, or Developer Tools can affect production or expose technical internals.";
      currentGrid.append(row);
    }
    currentPanel.append(currentGrid);
    if ((actor.permissionOverrides?.length ?? 0) > 0) {
      currentPanel.append(notice(`Deployment overrides: ${actor.permissionOverrides!.map((entry) => `${entry.operation === "add" ? "+" : "−"}${permissionLabel(entry.permission, catalog)}`).join(" · ")}`, "warn"));
    }

    const templatesPanel = panel("Role Templates", "Compare the permission sets available to the local Admin deployment");
    const selector = el("select", "st-admin-select") as HTMLSelectElement;
    selector.setAttribute("aria-label", "Role template");
    for (const template of templates) selector.append(new Option(template.label, template.id));
    selector.value = actor.role;
    const roleDescription = notice("", "info");
    const rolePermissions = el("div", "stx-grid");
    const renderTemplate = (): void => {
      const template = templates.find((entry) => entry.id === selector.value) ?? templates[0];
      if (!template) {
        roleDescription.textContent = "No role templates are exposed by the server.";
        rolePermissions.replaceChildren();
        return;
      }
      roleDescription.textContent = template.description;
      const allowed = new Set(template.permissions);
      rolePermissions.replaceChildren(...catalog.map((permission) => {
        const row = el("div", "stx-toggle-row");
        const text = el("div");
        text.append(el("strong", undefined, permission.label), el("small", undefined, permission.group));
        row.append(text, badge(allowed.has(permission.id) ? "IN TEMPLATE" : "NOT INCLUDED", allowed.has(permission.id) ? (permission.dangerous ? "warn" : "good") : "info"));
        return row;
      }));
    };
    selector.addEventListener("change", renderTemplate);
    templatesPanel.append(selector, roleDescription, rolePermissions);
    renderTemplate();

    const assignment = panel("Assignment & Overrides", "Server-side ownership prevents browser privilege escalation");
    assignment.append(
      notice("Role assignment belongs to the local deployment, not to a fake user database. `TYPING_GAME_ADMIN_ROLE` selects the service role; unknown roles fail closed.", "info"),
      notice("Granular deployment overrides can add/remove known permissions with `TYPING_GAME_ADMIN_PERMISSION_OVERRIDES`. Request headers can identify the actor for audit, but cannot choose the role or permissions.", "good"),
    );
    if (help) {
      const info = help.infoIcon({
        title: "Why assignments are not editable here",
        content: "This Admin currently has a local deployment identity, not a canonical multi-user account backend. Editing fake users or role assignments in browser state would create a security model that production does not consume.",
        placement: "left",
        interaction: "popover",
        label: "About role assignment ownership",
      });
      assignment.querySelector(".st-admin-panel-head")?.append(info);
    }
    content.replaceChildren(currentPanel, templatesPanel, assignment);
  }).catch((error: unknown) => {
    status.className = "stx-notice bad";
    status.textContent = error instanceof Error ? error.message : String(error);
    content.replaceChildren(notice("Effective access could not be loaded from the Admin service.", "bad"));
  });

  return page;
}
