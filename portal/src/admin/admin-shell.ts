import "@fontsource/exo-2/600.css";
import "@fontsource/exo-2/700.css";
import "@fontsource/exo-2/800.css";
import "@fontsource/be-vietnam-pro/400.css";
import "@fontsource/be-vietnam-pro/500.css";
import "@fontsource/be-vietnam-pro/600.css";
import "@fontsource/be-vietnam-pro/700.css";
import "./space-typing-ui.css";
import "./space-typing-phase-b.css";
import "./space-typing-remediation.css";
import "./v2/admin-v2.css";
import "./admin-shell.css";
import { SpaceTypingAdminApi } from "./api";
import { adminNavIcon } from "./space-typing-icons";
import { installAdminCommandShortcut, openAdminCommandPalette } from "./space-typing-command";
import { AdminHelpScope } from "./v2/admin-help";

import { ADMIN_AREAS, ADMINISTRATION, areaForPath, isAdministrationPath, renderAdministrationPage } from "./areas/registry";
import type { AdminArea } from "./areas/types";
import { getAdminStatus } from "./shared-overview";
const ALL_NAV_GROUPS = [...ADMIN_AREAS.flatMap((area) => area.navGroups), ADMINISTRATION];
const ADMIN_BASE = "/admin/space-typing";
const NAV_STATE_KEY = "typing-game:space-admin-collapsed-groups";
const AREA_STATE_KEY = "typing-game:admin-last-area";
const DEVELOPER_PERMISSION = "developer.runtime-inspect";

/** Pages reached from inside a section that should keep its nav item lit. */
const NAV_ALIASES: Readonly<Record<string, string>> = {
  [`${ADMIN_BASE}/worlds-stages`]: `${ADMIN_BASE}/stages`,
};

const LEGACY_ROUTE_LABELS: Readonly<Record<string, string>> = {
  [`${ADMIN_BASE}/analytics`]: "Analytics / Telemetry",
  [`${ADMIN_BASE}/shop`]: "Shop",
  [`${ADMIN_BASE}/currencies`]: "Currencies",
  [`${ADMIN_BASE}/rewards`]: "Rewards & Drops",
  [`${ADMIN_BASE}/warp`]: "Stamina / Warp",
  [`${ADMIN_BASE}/missions`]: "Missions",
  [`${ADMIN_BASE}/daily-weekly`]: "Daily / Weekly",
  [`${ADMIN_BASE}/expedition`]: "Expedition",
  [`${ADMIN_BASE}/events`]: "Live Ops",
  [`${ADMIN_BASE}/duel`]: "Duel Settings",
  [`${ADMIN_BASE}/ranked`]: "Ranked",
  [`${ADMIN_BASE}/alternative-modes`]: "Alternative Modes",
  [`${ADMIN_BASE}/backgrounds`]: "Backgrounds",
  [`${ADMIN_BASE}/vfx`]: "VFX",
  [`${ADMIN_BASE}/ui-assets`]: "UI Assets",
  [`${ADMIN_BASE}/feature-gates`]: "Feature Gates",
  [`${ADMIN_BASE}/qa`]: "QA Sandbox",
  [`${ADMIN_BASE}/worlds-stages`]: "Worlds & Stages · Stage overrides",
  [`${ADMIN_BASE}/players`]: "Players",
  [`${ADMIN_BASE}/liveops-mail`]: "Mail & Gift Codes",
  [`${ADMIN_BASE}/chat`]: "Chat Moderation",
  [`${ADMIN_BASE}/feedback`]: "Feedback",
  [`${ADMIN_BASE}/roles`]: "Roles & Permissions",
};

function element<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  className?: string,
  text?: string,
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function button(
  label: string,
  onClick: () => void,
  className = "st-admin-btn",
): HTMLButtonElement {
  const node = element("button", className, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function statusBadge(
  label: string,
  tone: "good" | "warn" | "bad" | "info" = "info",
): HTMLElement {
  return element("span", `st-admin-status ${tone}`, label);
}

export const ADMIN_ROUTE_REDIRECTS: Readonly<Record<string, string>> = {
  "/admin": "/admin/shared",
  "/admin/space-typing/media": "/admin/media",
  "/admin/space-typing/roles": "/admin/roles",
  "/admin/space-typing/typing-content": "/admin/shared/learning-content",
};

export function normalizedAdminPath(path: string): string {
  path = path.replace(/\/+$/, "") || "/";
  const redirected = ADMIN_ROUTE_REDIRECTS[path];
  if (redirected) return redirected;
  if (path === `${ADMIN_BASE}/flags`) return `${ADMIN_BASE}/feature-gates`;
  return path;
}

function readCollapsedGroups(): Set<string> {
  try {
    const raw = localStorage.getItem(NAV_STATE_KEY);
    if (raw === null) return new Set(ALL_NAV_GROUPS.map((group) => group.id));
    const parsed = JSON.parse(raw) as unknown;
    if (!Array.isArray(parsed)) return new Set();
    return new Set(parsed.filter((value): value is string => typeof value === "string"));
  } catch {
    return new Set();
  }
}

function writeCollapsedGroups(groups: Set<string>): void {
  try {
    localStorage.setItem(NAV_STATE_KEY, JSON.stringify([...groups]));
  } catch {
    // Navigation remains fully usable even when local storage is unavailable.
  }
}

function routeLabel(path: string): string {
  const primary = ALL_NAV_GROUPS.flatMap((group) => group.items).find((item) => item.path === path);
  return primary?.label ?? LEGACY_ROUTE_LABELS[path] ?? "Admin";
}

type AreaStorage = Pick<Storage, "getItem" | "setItem">;

/**
 * Administration pages (Media Library, Roles) belong to every area, so they keep
 * the area the user came from. The last area also lives in sessionStorage so a
 * reload keeps it; a fresh tab or direct load starts in All games.
 */
export class AdminAreaMemory {
  private lastAreaId: string | null;

  constructor(private readonly storage: () => AreaStorage = () => sessionStorage) {
    try {
      this.lastAreaId = this.storage().getItem(AREA_STATE_KEY);
    } catch {
      this.lastAreaId = null;
    }
  }

  /** An old /admin/space-typing/media or /roles link came from Space, so its page keeps that area. */
  remember(areaId: string): void {
    this.lastAreaId = areaId;
    try {
      this.storage().setItem(AREA_STATE_KEY, areaId);
    } catch {
      // The in-memory field still keeps the area for this page session.
    }
  }

  areaFor(path: string): AdminArea {
    const area = areaForPath(path, this.lastAreaId);
    if (!isAdministrationPath(path) && area.id !== this.lastAreaId) {
      this.lastAreaId = area.id;
      try {
        this.storage().setItem(AREA_STATE_KEY, area.id);
      } catch {
        // The in-memory field still keeps the area for this page session.
      }
    }
    return area;
  }
}

export class TypingGameAdmin {
  private readonly help = new AdminHelpScope();
  private readonly areas = new AdminAreaMemory();
  private developerToolsAllowed = false;
  private renderGeneration = 0;

  constructor(private readonly navigate: (path: string) => void) {
    installAdminCommandShortcut(this.navigate, () => ({ includeDeveloperTools: this.developerToolsAllowed }));
  }

  render(path: string): HTMLElement {
    this.help.destroy();
    this.developerToolsAllowed = false;
    const generation = ++this.renderGeneration;
    const canonicalPath = normalizedAdminPath(path);
    if (canonicalPath !== path) history.replaceState({}, "", canonicalPath + location.search + location.hash);
    document.title = `Typing Game Admin · ${routeLabel(canonicalPath)}`;
    if (canonicalPath !== path && path.startsWith(`${ADMIN_BASE}/`) && isAdministrationPath(canonicalPath)) this.areas.remember("space-typing");
    const area = this.areas.areaFor(canonicalPath);
    const root = element("main", "st-admin");
    const shell = element("div", "st-admin-shell");
    shell.append(this.renderSidebar(canonicalPath, area));

    const main = element("div", "st-admin-main");
    main.append(this.renderTopbar(canonicalPath, area));
    const content = element("div", "st-admin-content");
    content.append(this.renderPage(canonicalPath, area));
    main.append(content);

    shell.append(main);
    root.append(shell);
    this.help.observeRoot(root);
    void this.hydratePermissions(root, generation);
    return root;
  }

  private async hydratePermissions(root: HTMLElement, generation: number): Promise<void> {
    try {
      const actor = await new SpaceTypingAdminApi().getActor();
      if (generation !== this.renderGeneration || !root.isConnected) return;
      this.developerToolsAllowed = actor.permissions.includes(DEVELOPER_PERMISSION);
    } catch {
      if (generation !== this.renderGeneration || !root.isConnected) return;
      this.developerToolsAllowed = false;
    }

    for (const node of root.querySelectorAll<HTMLElement>(`[data-admin-permission="${DEVELOPER_PERMISSION}"]`)) {
      node.hidden = !this.developerToolsAllowed;
    }
  }

  private renderSidebar(path: string, area: AdminArea): HTMLElement {
    const aside = element("aside", "st-admin-sidebar");
    const brand = element("div", "st-admin-brand");
    const mark = element("div", "st-admin-brand-mark");
    mark.append(
      element("span", "st-admin-brand-logo", "TG"),
      element("span", undefined, "Typing Game"),
    );
    brand.append(
      mark,
      element("h2", undefined, "Typing Game Admin"),
      element("p", undefined, "Game Management"),
    );
    const env = element("div", "st-admin-env-row");
    env.append(
      element("span", "st-admin-env", "LOCAL"),
      element("span", "st-admin-status good", "LOCAL SERVICE"),
    );
    brand.append(env);
    aside.append(brand);

    const selector = element("div", "st-admin-area-selector");
    selector.setAttribute("role", "group");
    selector.setAttribute("aria-label", "Admin area");
    for (const entry of ADMIN_AREAS) {
      const choice = button(entry.label, () => this.navigate(entry.base), `st-admin-btn${area.id === entry.id ? " primary" : ""}`);
      choice.setAttribute("aria-pressed", String(area.id === entry.id));
      selector.append(choice);
    }
    aside.append(selector);
    const groups = [...area.navGroups, ADMINISTRATION];
    const collapsed = readCollapsedGroups();
    const activeGroup = groups.find((group) => group.items.some((item) => item.path === path));
    if (activeGroup) collapsed.delete(activeGroup.id);
    writeCollapsedGroups(collapsed);

    const nav = element("nav", "st-admin-nav");
    nav.setAttribute("aria-label", "Typing Game Admin sections");
    let activeButton: HTMLButtonElement | null = null;

    for (const group of groups) {
      const wrapper = element("section", "st-admin-nav-group");
      if (group.requiredPermission) {
        wrapper.dataset.adminPermission = group.requiredPermission;
        wrapper.hidden = true;
      }
      const groupButton = element("button", "st-admin-nav-group-toggle");
      groupButton.type = "button";
      groupButton.setAttribute("aria-label", `Toggle ${group.label}`);
      this.help.tooltip(groupButton, {
        title: group.label,
        content: group.description,
        placement: "right",
        interaction: "hover-focus",
      });
      const groupCopy = element("span", "st-admin-nav-group-copy");
      groupCopy.append(element("strong", undefined, group.label));
      const chevron = element("span", "st-admin-nav-chevron", "⌄");
      chevron.setAttribute("aria-hidden", "true");
      groupButton.append(groupCopy, chevron);

      const groupItems = element("div", "st-admin-nav-group-items");
      const groupItemsId = `space-admin-nav-${group.id}`;
      groupItems.id = groupItemsId;
      groupButton.setAttribute("aria-controls", groupItemsId);
      const initiallyExpanded = !collapsed.has(group.id);
      groupButton.setAttribute("aria-expanded", String(initiallyExpanded));
      groupItems.hidden = !initiallyExpanded;

      groupButton.addEventListener("click", () => {
        const expanded = groupButton.getAttribute("aria-expanded") === "true";
        groupButton.setAttribute("aria-expanded", String(!expanded));
        groupItems.hidden = expanded;
        if (expanded) collapsed.add(group.id); else collapsed.delete(group.id);
        writeCollapsedGroups(collapsed);
      });

      for (const item of group.items) {
        const navButton = element(
          "button",
          `st-admin-nav-item${path === item.path || NAV_ALIASES[path] === item.path ? " active" : ""}`,
        );
        navButton.type = "button";
        navButton.setAttribute("aria-label", item.label);
        this.help.tooltip(navButton, {
          title: item.label,
          content: item.description,
          placement: "right",
          interaction: "hover-focus",
        });
        const navCopy = element("span", "st-admin-nav-copy");
        navCopy.append(element("span", "st-admin-nav-text", item.label));
        navButton.append(adminNavIcon(item.icon), navCopy);
        navButton.addEventListener("click", () => this.navigate(item.path));
        groupItems.append(navButton);
        if (path === item.path) activeButton = navButton;
      }

      wrapper.append(groupButton, groupItems);
      nav.append(wrapper);
    }
    aside.append(nav);

    if (activeButton !== null) {
      queueMicrotask(() => activeButton?.scrollIntoView({ block: "nearest" }));
    }
    return aside;
  }

  private renderTopbar(path: string, area: AdminArea): HTMLElement {
    const bar = element("div", "st-admin-topbar");
    const breadcrumb = element("div", "st-admin-breadcrumb");
    breadcrumb.append(
      document.createTextNode(`${isAdministrationPath(path) ? "Administration" : area.label} / `),
      element("strong", undefined, routeLabel(path)),
    );
    bar.append(breadcrumb);
    bar.append(element("div", "st-admin-topbar-spacer"));
    bar.append(
      button(
        "⌘K  Search command…",
        () => openAdminCommandPalette(this.navigate, { includeDeveloperTools: this.developerToolsAllowed }),
        "st-admin-command",
      ),
    );

    const localAdmin = element("span", "st-admin-v2-topbar-help");
    localAdmin.append(
      element("span", "st-admin-revision", "LOCAL ADMIN"),
      this.help.infoIcon({
        title: "Local Admin",
        content: "Uses the local Typing Game Admin service. Saved drafts do not affect the active game until an explicit publish succeeds.",
        placement: "bottom",
        interaction: "popover",
        label: "About the local Admin connection",
      }),
    );
    bar.append(localAdmin);
    bar.append(statusBadge("READY", "good"));
    return bar;
  }

  private renderPage(path: string, area: AdminArea): HTMLElement {
    const context = { navigate: this.navigate, help: this.help };
    const administration = renderAdministrationPage(path, context);
    if (administration) return administration;
    if (area.id !== "space-typing") return area.renderPage(path, context) ?? this.renderUnknown(path);
    const host = element("div");
    host.append(element("p", "st-admin-notice", "Checking Space Typing availability…"));
    const renderSpacePage = () => host.replaceChildren(area.renderPage(path, context) ?? this.renderUnknown(path));
    void getAdminStatus().then((status) => {
      if (!host.isConnected) return;
      if (status.spaceStatus === "failed") {
        host.replaceChildren(element("h1", undefined, "Space Typing failed to start — see the Admin server log"));
        return;
      }
      if (!status.spaceAvailable) {
        host.replaceChildren(element("h1", undefined, "Space Typing is not checked out"));
        return;
      }
      renderSpacePage();
    }).catch(() => {
      // Without the probe, render the page anyway: its own API calls report their errors.
      if (host.isConnected) renderSpacePage();
    });
    return host;
  }

  private renderUnknown(path: string): HTMLElement {
    const page = element("div");
    const panel = element("section", "st-admin-panel solid");
    panel.append(
      element("div", "st-admin-eyebrow", "Navigation"),
      element("h1", undefined, "Screen not found"),
      element("p", undefined, `This Admin URL is not registered. Use the sidebar or Search command to open a supported Admin screen. Requested path: ${path}.`),
      button("Back to Overview", () => this.navigate("/admin/shared"), "st-admin-btn primary"),
    );
    page.append(panel);
    return page;
  }
}
