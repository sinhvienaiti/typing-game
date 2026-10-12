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
import { renderPhaseBAdminScreen } from "./space-typing-phase-b";
import { adminNavIcon } from "./space-typing-icons";
import { installAdminCommandShortcut, openAdminCommandPalette } from "./space-typing-command";
import { AdminHelpScope } from "./v2/admin-help";

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
};

const ADMIN_BASE = "/admin/space-typing";
const NAV_STATE_KEY = "typing-game:space-admin-collapsed-groups";

const NAV_GROUPS: readonly NavGroup[] = [
  {
    id: "dashboard",
    label: "Dashboard",
    description: "Status, activity and operational signals for Space Typing.",
    items: [
      { label: "Overview", path: ADMIN_BASE, icon: "◫", description: "See current service status and the operational signals available to this Admin." },
      { label: "Analytics", path: `${ADMIN_BASE}/analytics`, icon: "⌁", description: "Review session activity and local profile history that are available today." },
    ],
  },
  {
    id: "audio",
    label: "Audio & Music",
    description: "Manage player audio defaults, music tracks and world or stage assignments.",
    items: [
      { label: "Audio Defaults", path: `${ADMIN_BASE}/audio`, icon: "◖", description: "Set default audio behavior while preserving player-specific preferences." },
      { label: "Music Library", path: `${ADMIN_BASE}/music-library`, icon: "♫", description: "Browse, upload and manage music tracks available to Space Typing." },
      { label: "World / Stage Music", path: `${ADMIN_BASE}/world-music`, icon: "◎", description: "Assign music to global, galaxy, world and stage contexts and preview the result." },
    ],
  },
  {
    id: "content",
    label: "Game Content",
    description: "Manage gameplay content such as ships, equipment, enemies, bosses and stages.",
    items: [
      { label: "Ships", path: `${ADMIN_BASE}/ships`, icon: "△", description: "Manage the fleet and the ship properties currently supported by the game." },
      { label: "Equipment", path: `${ADMIN_BASE}/equipment`, icon: "◇", description: "Manage equipment names, descriptions, stats and supported perks." },
      { label: "Skills", path: `${ADMIN_BASE}/skills`, icon: "ϟ", description: "Manage combat skills and the gameplay-facing values currently supported." },
      { label: "Enemies", path: `${ADMIN_BASE}/enemies`, icon: "✦", description: "Review enemies and tune the gameplay values currently available for management." },
      { label: "Bosses", path: `${ADMIN_BASE}/bosses`, icon: "✹", description: "Review bosses and manage the properties currently available for editing." },
      { label: "Worlds & Stages", path: `${ADMIN_BASE}/stages`, icon: "⌘", description: "Review world structure, stage rosters and supported world or stage settings." },
      { label: "Typing Content", path: `${ADMIN_BASE}/typing-content`, icon: "Aa", description: "Browse the English-learning content used by Space Typing." },
    ],
  },
  {
    id: "economy",
    label: "Economy",
    description: "Review shop, currency, rewards, drops and stamina behavior.",
    items: [
      { label: "Shop", path: `${ADMIN_BASE}/shop`, icon: "▣", description: "Review the current Shop catalog and purchase behavior. Full product editing is being added through Admin V2." },
      { label: "Currencies", path: `${ADMIN_BASE}/currencies`, icon: "◈", description: "Review currencies, limits, acquisition sources and spending uses." },
      { label: "Rewards & Drops", path: `${ADMIN_BASE}/rewards`, icon: "✧", description: "Review campaign rewards, combat credits, loot and drop behavior." },
      { label: "Stamina / Warp", path: `${ADMIN_BASE}/warp`, icon: "⚡", description: "Review Warp stamina, reserve capacity, regeneration and persistence behavior." },
    ],
  },
  {
    id: "live-ops",
    label: "Live Ops",
    description: "Review missions, recurring challenges, expeditions and event behavior.",
    items: [
      { label: "Missions", path: `${ADMIN_BASE}/missions`, icon: "✓", description: "Review progression missions and stage objectives." },
      { label: "Daily / Weekly", path: `${ADMIN_BASE}/daily-weekly`, icon: "◷", description: "Review recurring challenge behavior and which schedules are currently available." },
      { label: "Expedition", path: `${ADMIN_BASE}/expedition`, icon: "↗", description: "Review Expedition rules and saved-run behavior." },
      { label: "Events", path: `${ADMIN_BASE}/events`, icon: "◷", description: "Review event behavior currently supported by Space Typing." },
    ],
  },
  {
    id: "pvp",
    label: "PvP",
    description: "Review Duel, Ranked and alternative competitive modes.",
    items: [
      { label: "Duel Settings", path: `${ADMIN_BASE}/duel`, icon: "⚔", description: "Review Duel rules and settings that currently control a match." },
      { label: "Ranked", path: `${ADMIN_BASE}/ranked`, icon: "♜", description: "Review Ranked rules and the competitive features currently available." },
      { label: "Alternative Modes", path: `${ADMIN_BASE}/alternative-modes`, icon: "⇄", description: "Review alternative PvP modes and their current availability." },
    ],
  },
  {
    id: "visuals",
    label: "Visuals",
    description: "Review backgrounds, visual effects and UI presentation assets.",
    items: [
      { label: "Backgrounds", path: `${ADMIN_BASE}/backgrounds`, icon: "▧", description: "Review game backgrounds, generated visual sets and quality variants." },
      { label: "VFX", path: `${ADMIN_BASE}/vfx`, icon: "✺", description: "Review combat, projectile, skill and boss visual effects." },
      { label: "UI Assets", path: `${ADMIN_BASE}/ui-assets`, icon: "▦", description: "Review HUD and presentation assets currently used by the game." },
    ],
  },
  {
    id: "system",
    label: "System",
    description: "Manage global settings, feature availability and publishing history.",
    items: [
      { label: "General Settings", path: `${ADMIN_BASE}/settings`, icon: "⚙", description: "Manage global game defaults, network behavior and maintenance settings." },
      { label: "Feature Gates", path: `${ADMIN_BASE}/feature-gates`, icon: "⚑", description: "Review features whose availability can be controlled by the game." },
      { label: "History & Publish", path: `${ADMIN_BASE}/history`, icon: "↶", description: "Review drafts and published versions, validate changes, publish or roll back safely." },
    ],
  },
  {
    id: "developer",
    label: "Developer",
    description: "Developer and test tools kept separate from normal game-management workflows.",
    items: [
      { label: "QA Sandbox", path: `${ADMIN_BASE}/qa`, icon: "⌬", description: "Open the isolated Test Lab without changing Campaign progress." },
    ],
  },
];

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

export class SpaceTypingAdmin {
  private readonly help = new AdminHelpScope();

  constructor(private readonly navigate: (path: string) => void) {
    installAdminCommandShortcut(this.navigate);
  }

  render(path: string): HTMLElement {
    this.help.destroy();
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
    return root;
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
      element("p", undefined, "Live Ops · Content · Configuration"),
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
    const item = NAV_GROUPS
      .flatMap((group) => group.items)
      .find((candidate) => candidate.path === path);
    const breadcrumb = element("div", "st-admin-breadcrumb");
    breadcrumb.append(
      document.createTextNode("Space Typing / "),
      element("strong", undefined, item?.label ?? "Admin"),
    );
    bar.append(breadcrumb);
    bar.append(element("div", "st-admin-topbar-spacer"));
    bar.append(
      button(
        "⌘K  Search command…",
        () => openAdminCommandPalette(this.navigate),
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
