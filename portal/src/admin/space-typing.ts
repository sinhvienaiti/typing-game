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
import { SpaceTypingAdminApi } from "./api";
import { renderPhaseBAdminScreen } from "./space-typing-phase-b";
import { adminNavIcon } from "./space-typing-icons";
import { installAdminCommandShortcut, openAdminCommandPalette } from "./space-typing-command";
import { AdminHelpScope } from "./v2/admin-help";
import { renderAdminV2Dashboard } from "./v2/dashboard";
import { renderAdminV2DeveloperTools } from "./v2/developer-tools";
import { renderAdminV2MediaLibrary } from "./v2/media-library";

type NavItem = {
  label: string;
  path: string;
  icon: string;
  description: string;
};

type NavGroup = {
  id: string;
  label: string;
  description: string;
  items: readonly NavItem[];
  requiredPermission?: string;
};

const ADMIN_BASE = "/admin/space-typing";
const NAV_STATE_KEY = "typing-game:space-admin-collapsed-groups";
const DEVELOPER_PERMISSION = "developer.runtime-inspect";

const NAV_GROUPS: readonly NavGroup[] = [
  {
    id: "dashboard",
    label: "Dashboard",
    description: "Published state, drafts and administrator activity that need attention now.",
    items: [
      { label: "Overview", path: ADMIN_BASE, icon: "◫", description: "See real Admin state, pending drafts and recent administrator activity." },
    ],
  },
  {
    id: "content",
    label: "Content",
    description: "Manage worlds, stages and learning-content assignments backed by canonical game data.",
    items: [
      { label: "Worlds & Stages", path: `${ADMIN_BASE}/stages`, icon: "⌘", description: "Manage supported world and stage configuration through the revision-backed workflow." },
      { label: "Typing Content", path: `${ADMIN_BASE}/typing-content`, icon: "Aa", description: "Browse canonical English-learning content used by Space Typing without creating a duplicate content database." },
    ],
  },
  {
    id: "gameplay",
    label: "Gameplay",
    description: "Manage revision-backed gameplay entities currently connected to the Space Typing runtime.",
    items: [
      { label: "Ships", path: `${ADMIN_BASE}/ships`, icon: "△", description: "Manage the ship properties currently supported by the canonical runtime." },
      { label: "Equipment", path: `${ADMIN_BASE}/equipment`, icon: "◇", description: "Manage supported equipment definitions, stats and perks." },
      { label: "Skills", path: `${ADMIN_BASE}/skills`, icon: "ϟ", description: "Manage supported combat-skill definitions and parameters." },
      { label: "Enemies", path: `${ADMIN_BASE}/enemies`, icon: "✦", description: "Manage supported enemy admission and projectile policy values." },
      { label: "Bosses", path: `${ADMIN_BASE}/bosses`, icon: "✹", description: "Manage supported boss identity values through the canonical revision workflow." },
    ],
  },
  {
    id: "economy-live-ops",
    label: "Economy & Live Ops",
    description: "Manage canonical Shop merchandising and the Live Ops controls that have real runtime owners.",
    items: [
      { label: "Shop", path: `${ADMIN_BASE}/shop`, icon: "▱", description: "Manage supported Shop offers, pricing and merchandising through the canonical Shop owner." },
      { label: "Live Ops", path: `${ADMIN_BASE}/events`, icon: "⌁", description: "Manage runtime-owned Live Ops controls and see unsupported scheduling or announcements fail closed." },
    ],
  },
  {
    id: "media",
    label: "Media",
    description: "Browse canonical game media, upload Admin-managed assets and keep source-owned runtime media read-only.",
    items: [
      { label: "Media Library", path: `${ADMIN_BASE}/media`, icon: "▧", description: "Browse images, models, music, SFX and Admin uploads, with immutable version history and usage." },
      { label: "Music Library", path: `${ADMIN_BASE}/music-library`, icon: "♫", description: "Browse, upload and manage the legacy authored music capability while it is migrated into Media V2." },
      { label: "SFX", path: `${ADMIN_BASE}/sfx`, icon: "◉", description: "Inspect production sample-backed sound effects and test the exact committed runtime assets without changing game policy." },
      { label: "World / Stage Music", path: `${ADMIN_BASE}/world-music`, icon: "◎", description: "Assign music to global, galaxy, world and stage contexts and preview the canonical result." },
    ],
  },
  {
    id: "system",
    label: "System",
    description: "Manage safe global settings, access review and the revision lifecycle.",
    items: [
      { label: "Audio Defaults", path: `${ADMIN_BASE}/audio`, icon: "◖", description: "Set default audio behavior while preserving player-specific preferences." },
      { label: "General Settings", path: `${ADMIN_BASE}/settings`, icon: "⚙", description: "Manage global game defaults, network behavior and maintenance settings." },
      { label: "Roles & Permissions", path: `${ADMIN_BASE}/roles`, icon: "◈", description: "Review server-enforced role templates, dangerous permissions and this deployment's effective access." },
      { label: "History & Publish", path: `${ADMIN_BASE}/history`, icon: "↶", description: "Review drafts, validate complete change scope, publish or roll back safely." },
    ],
  },
  {
    id: "developer",
    label: "Developer Tools",
    description: "Runtime contracts, capability diagnostics and isolated QA tools separated from normal administrator workflows.",
    requiredPermission: DEVELOPER_PERMISSION,
    items: [
      { label: "Developer Tools", path: `${ADMIN_BASE}/developer-tools`, icon: "⌬", description: "Open permission-gated runtime, economy, Live Ops, PvP, visual and QA diagnostics." },
    ],
  },
];

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
  [`${ADMIN_BASE}/worlds-stages`]: "Stages",
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

function normalizedAdminPath(path: string): string {
  if (path === `${ADMIN_BASE}/flags`) return `${ADMIN_BASE}/feature-gates`;
  return path;
}

function readCollapsedGroups(): Set<string> {
  try {
    const raw = localStorage.getItem(NAV_STATE_KEY);
    if (raw === null) return new Set(NAV_GROUPS.map((group) => group.id));
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
  const primary = NAV_GROUPS.flatMap((group) => group.items).find((item) => item.path === path);
  return primary?.label ?? LEGACY_ROUTE_LABELS[path] ?? "Admin";
}

export class SpaceTypingAdmin {
  private readonly help = new AdminHelpScope();
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
    const root = element("main", "st-admin");
    const shell = element("div", "st-admin-shell");
    shell.append(this.renderSidebar(canonicalPath));

    const main = element("div", "st-admin-main");
    main.append(this.renderTopbar(canonicalPath));
    const content = element("div", "st-admin-content");
    content.append(this.renderPage(canonicalPath));
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

  private renderSidebar(path: string): HTMLElement {
    const aside = element("aside", "st-admin-sidebar");
    const brand = element("div", "st-admin-brand");
    const mark = element("div", "st-admin-brand-mark");
    mark.append(
      element("span", "st-admin-brand-logo", "ST"),
      element("span", undefined, "Space Typing"),
    );
    brand.append(
      mark,
      element("h2", undefined, "Command Center"),
      element("p", undefined, "Game Management"),
    );
    const env = element("div", "st-admin-env-row");
    env.append(
      element("span", "st-admin-env", "LOCAL"),
      element("span", "st-admin-status good", "SERVICE CONNECTED"),
    );
    brand.append(env);
    aside.append(brand);

    const collapsed = readCollapsedGroups();
    const activeGroup = NAV_GROUPS.find((group) => group.items.some((item) => item.path === path));
    if (activeGroup) collapsed.delete(activeGroup.id);
    writeCollapsedGroups(collapsed);

    const nav = element("nav", "st-admin-nav");
    nav.setAttribute("aria-label", "Space Typing Admin sections");
    let activeButton: HTMLButtonElement | null = null;

    for (const group of NAV_GROUPS) {
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
          `st-admin-nav-item${path === item.path ? " active" : ""}`,
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

  private renderTopbar(path: string): HTMLElement {
    const bar = element("div", "st-admin-topbar");
    const breadcrumb = element("div", "st-admin-breadcrumb");
    breadcrumb.append(
      document.createTextNode("Space Typing / "),
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
      element("span", "st-admin-revision", "LOCAL ADMIN · CONNECTED"),
      this.help.infoIcon({
        title: "Local Admin",
        content: "Connected to the local Space Typing Admin service. Saved drafts do not affect the active game until an explicit publish succeeds.",
        placement: "bottom",
        interaction: "popover",
        label: "About the local Admin connection",
      }),
    );
    bar.append(localAdmin);
    bar.append(statusBadge("READY", "good"));
    return bar;
  }

  private renderPage(path: string): HTMLElement {
    if (path === ADMIN_BASE) return renderAdminV2Dashboard(this.navigate, this.help);
    if (path === `${ADMIN_BASE}/media`) return renderAdminV2MediaLibrary(this.help);
    if (path === `${ADMIN_BASE}/developer-tools`) return renderAdminV2DeveloperTools(this.navigate, this.help);
    const phaseB = renderPhaseBAdminScreen(path, this.navigate);
    if (phaseB !== null) return phaseB;
    return this.renderUnknown(path);
  }

  private renderUnknown(path: string): HTMLElement {
    const page = element("div");
    const panel = element("section", "st-admin-panel solid");
    panel.append(
      element("div", "st-admin-eyebrow", "Navigation"),
      element("h1", undefined, "Screen not found"),
      element("p", undefined, `This Admin URL is not registered. Use the sidebar or Search command to open a supported Space Typing screen. Requested path: ${path}.`),
      button("Back to Overview", () => this.navigate(ADMIN_BASE), "st-admin-btn primary"),
    );
    page.append(panel);
    return page;
  }
}
