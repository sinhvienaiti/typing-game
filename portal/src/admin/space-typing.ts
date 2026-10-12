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
import { renderPhaseBAdminScreen } from "./space-typing-phase-b";
import { adminNavIcon } from "./space-typing-icons";
import { installAdminCommandShortcut, openAdminCommandPalette } from "./space-typing-command";

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
    description: "Operational status and local-profile analytics.",
    items: [
      { label: "Overview", path: ADMIN_BASE, icon: "◫", description: "See runtime ownership, available operational signals and service status." },
      { label: "Analytics", path: `${ADMIN_BASE}/analytics`, icon: "⌁", description: "Inspect session telemetry and persisted local-profile history." },
    ],
  },
  {
    id: "audio",
    label: "Audio & Music",
    description: "Player defaults, authored tracks and world/stage music policy.",
    items: [
      { label: "Audio Defaults", path: `${ADMIN_BASE}/audio`, icon: "◖", description: "Edit child-backed player audio defaults without overwriting player preferences." },
      { label: "Music Library", path: `${ADMIN_BASE}/music-library`, icon: "♫", description: "Upload Admin-owned tracks and rebuild the canonical runtime catalog." },
      { label: "World / Stage Music", path: `${ADMIN_BASE}/world-music`, icon: "◎", description: "Author Global, Galaxy, World and Stage playlist assignments with canonical preview." },
    ],
  },
  {
    id: "content",
    label: "Game Content",
    description: "Canonical gameplay registries and supported overrides.",
    items: [
      { label: "Ships", path: `${ADMIN_BASE}/ships`, icon: "△", description: "Inspect the canonical fleet and author supported ship metadata/stat/visual overrides." },
      { label: "Equipment", path: `${ADMIN_BASE}/equipment`, icon: "◇", description: "Inspect equipment definitions and author supported name, description, stat and perk overrides." },
      { label: "Skills", path: `${ADMIN_BASE}/skills`, icon: "ϟ", description: "Inspect combat skills and author supported gameplay-facing fields." },
      { label: "Enemies", path: `${ADMIN_BASE}/enemies`, icon: "✦", description: "Inspect enemy identities and tune only the verified admission boundary." },
      { label: "Bosses", path: `${ADMIN_BASE}/bosses`, icon: "✹", description: "Inspect canonical bosses and author the supported identity fields." },
      { label: "Worlds & Stages", path: `${ADMIN_BASE}/stages`, icon: "⌘", description: "Inspect world structure, enemy rosters and supported stage overrides." },
      { label: "Typing Content", path: `${ADMIN_BASE}/typing-content`, icon: "Aa", description: "Browse canonical English-learning content consumed by Space Typing." },
    ],
  },
  {
    id: "economy",
    label: "Economy",
    description: "Read canonical transaction, currency, reward and stamina boundaries.",
    items: [
      { label: "Shop", path: `${ADMIN_BASE}/shop`, icon: "▣", description: "Inspect the real Shop transaction/catalog model without creating a second pricing source." },
      { label: "Currencies", path: `${ADMIN_BASE}/currencies`, icon: "◈", description: "Inspect currencies, caps, sources and sinks owned by gameplay." },
      { label: "Rewards & Drops", path: `${ADMIN_BASE}/rewards`, icon: "✧", description: "Inspect campaign rewards, combat credits, loot and luck ownership." },
      { label: "Stamina / Warp", path: `${ADMIN_BASE}/warp`, icon: "⚡", description: "Inspect Warp stamina, reserve, regeneration and persistence rules." },
    ],
  },
  {
    id: "live-ops",
    label: "Live Ops",
    description: "Runtime-owned missions, challenges, expeditions and event systems.",
    items: [
      { label: "Missions", path: `${ADMIN_BASE}/missions`, icon: "✓", description: "Inspect progression missions and per-stage objective ownership." },
      { label: "Daily / Weekly", path: `${ADMIN_BASE}/daily-weekly`, icon: "◷", description: "Inspect Daily runtime behavior and explicit Weekly capability boundaries." },
      { label: "Expedition", path: `${ADMIN_BASE}/expedition`, icon: "↗", description: "Inspect deterministic Expedition rules and browser-owned save boundaries." },
      { label: "Events", path: `${ADMIN_BASE}/events`, icon: "◷", description: "Inspect gameplay event systems; no remote calendar service is fabricated." },
    ],
  },
  {
    id: "pvp",
    label: "PvP",
    description: "Duel, Ranked and alternative mode ownership diagnostics.",
    items: [
      { label: "Duel Settings", path: `${ADMIN_BASE}/duel`, icon: "⚔", description: "Inspect room-owner Duel settings and runtime authority boundaries." },
      { label: "Ranked", path: `${ADMIN_BASE}/ranked`, icon: "♜", description: "Inspect Ranked runtime rules and fail-closed season/Admin authority." },
      { label: "Alternative Modes", path: `${ADMIN_BASE}/alternative-modes`, icon: "⇄", description: "Inspect supported alternative PvP modes and unavailable admissions." },
    ],
  },
  {
    id: "visuals",
    label: "Visuals",
    description: "Production background, VFX and UI asset ownership.",
    items: [
      { label: "Backgrounds", path: `${ADMIN_BASE}/backgrounds`, icon: "▧", description: "Inspect production BGV compositions, generated kits and quality budgets." },
      { label: "VFX", path: `${ADMIN_BASE}/vfx`, icon: "✺", description: "Inspect production combat/projectile/skill/boss VFX ownership and quality tiers." },
      { label: "UI Assets", path: `${ADMIN_BASE}/ui-assets`, icon: "▦", description: "Inspect HUD and presentation ownership without a fake asset CRUD layer." },
    ],
  },
  {
    id: "system",
    label: "System",
    description: "Revision-backed configuration, runtime gates and publishing.",
    items: [
      { label: "General Settings", path: `${ADMIN_BASE}/settings`, icon: "⚙", description: "Edit revision-backed defaults, network behavior and maintenance state." },
      { label: "Feature Gates", path: `${ADMIN_BASE}/feature-gates`, icon: "⚑", description: "Inspect feature gates actually consumed by the runtime." },
      { label: "History & Publish", path: `${ADMIN_BASE}/history`, icon: "↶", description: "Review immutable revisions, validate, publish and perform eligible rollback." },
    ],
  },
  {
    id: "developer",
    label: "Developer",
    description: "Isolated developer/test surfaces that never mutate Campaign progression.",
    items: [
      { label: "QA Sandbox", path: `${ADMIN_BASE}/qa`, icon: "⌬", description: "Launch the isolated production Test Lab without writing Campaign progress." },
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
  constructor(private readonly navigate: (path: string) => void) {
    installAdminCommandShortcut(this.navigate);
  }

  render(path: string): HTMLElement {
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
      element("span", "st-admin-mock-badge", "PHASE B · RUNTIME INTEGRATED"),
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
      groupButton.title = group.description;
      const groupCopy = element("span", "st-admin-nav-group-copy");
      groupCopy.append(
        element("strong", undefined, group.label),
        element("small", undefined, group.description),
      );
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
        navButton.title = `${item.label} — ${item.description}`;
        navButton.setAttribute("aria-label", `${item.label}. ${item.description}`);
        const navCopy = element("span", "st-admin-nav-copy");
        navCopy.append(
          element("span", "st-admin-nav-text", item.label),
          element("small", "st-admin-nav-description", item.description),
        );
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
    const runtime = element("span", "st-admin-revision", "LOCAL ADMIN · RUNTIME");
    runtime.title = "This Admin surface is connected to the local Space Typing runtime service.";
    bar.append(runtime);
    bar.append(statusBadge("LOCAL", "good"));
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
      element("div", "st-admin-eyebrow", "Admin Route"),
      element("h1", undefined, "Unknown Admin screen"),
      element("p", undefined, `No registered Phase B screen exists for ${path}.`),
      button("Back to Overview", () => this.navigate(ADMIN_BASE), "st-admin-btn primary"),
    );
    page.append(panel);
    return page;
  }
}
