import "@fontsource/exo-2/600.css";
import "@fontsource/exo-2/700.css";
import "@fontsource/exo-2/800.css";
import "@fontsource/be-vietnam-pro/400.css";
import "@fontsource/be-vietnam-pro/500.css";
import "@fontsource/be-vietnam-pro/600.css";
import "@fontsource/be-vietnam-pro/700.css";
import "./space-typing-ui.css";
import "./space-typing-phase-b.css";
import { renderPhaseBAdminScreen } from "./space-typing-phase-b";
import { adminNavIcon } from "./space-typing-icons";
import { installAdminCommandShortcut, openAdminCommandPalette } from "./space-typing-command";

type NavItem = {
  label: string;
  path: string;
  icon: string;
};

type NavGroup = {
  label: string;
  items: readonly NavItem[];
};

const ADMIN_BASE = "/admin/space-typing";

const NAV_GROUPS: readonly NavGroup[] = [
  {
    label: "Dashboard",
    items: [
      { label: "Overview", path: ADMIN_BASE, icon: "◫" },
      { label: "Analytics", path: `${ADMIN_BASE}/analytics`, icon: "⌁" },
    ],
  },
  {
    label: "Audio & Music",
    items: [
      { label: "Audio Defaults", path: `${ADMIN_BASE}/audio`, icon: "◖" },
      { label: "Music Library", path: `${ADMIN_BASE}/music-library`, icon: "♫" },
      { label: "World / Stage Music", path: `${ADMIN_BASE}/world-music`, icon: "◎" },
    ],
  },
  {
    label: "Game Content",
    items: [
      { label: "Ships", path: `${ADMIN_BASE}/ships`, icon: "△" },
      { label: "Equipment", path: `${ADMIN_BASE}/equipment`, icon: "◇" },
      { label: "Skills", path: `${ADMIN_BASE}/skills`, icon: "ϟ" },
      { label: "Enemies", path: `${ADMIN_BASE}/enemies`, icon: "✦" },
      { label: "Bosses", path: `${ADMIN_BASE}/bosses`, icon: "✹" },
      { label: "Worlds & Stages", path: `${ADMIN_BASE}/stages`, icon: "⌘" },
      { label: "Typing Content", path: `${ADMIN_BASE}/typing-content`, icon: "Aa" },
    ],
  },
  {
    label: "Economy",
    items: [
      { label: "Shop", path: `${ADMIN_BASE}/shop`, icon: "▣" },
      { label: "Currencies", path: `${ADMIN_BASE}/currencies`, icon: "◈" },
      { label: "Rewards & Drops", path: `${ADMIN_BASE}/rewards`, icon: "✧" },
      { label: "Stamina / Warp", path: `${ADMIN_BASE}/warp`, icon: "⚡" },
    ],
  },
  {
    label: "Live Ops",
    items: [
      { label: "Missions", path: `${ADMIN_BASE}/missions`, icon: "✓" },
      { label: "Daily / Weekly", path: `${ADMIN_BASE}/daily-weekly`, icon: "◷" },
      { label: "Expedition", path: `${ADMIN_BASE}/expedition`, icon: "↗" },
      { label: "Events", path: `${ADMIN_BASE}/events`, icon: "◷" },
    ],
  },
  {
    label: "PvP",
    items: [
      { label: "Duel Settings", path: `${ADMIN_BASE}/duel`, icon: "⚔" },
      { label: "Ranked", path: `${ADMIN_BASE}/ranked`, icon: "♜" },
      { label: "Alternative Modes", path: `${ADMIN_BASE}/alternative-modes`, icon: "⇄" },
    ],
  },
  {
    label: "Visuals",
    items: [
      { label: "Backgrounds", path: `${ADMIN_BASE}/backgrounds`, icon: "▧" },
      { label: "VFX", path: `${ADMIN_BASE}/vfx`, icon: "✺" },
      { label: "UI Assets", path: `${ADMIN_BASE}/ui-assets`, icon: "▦" },
    ],
  },
  {
    label: "System",
    items: [
      { label: "General Settings", path: `${ADMIN_BASE}/settings`, icon: "⚙" },
      { label: "Feature Gates", path: `${ADMIN_BASE}/feature-gates`, icon: "⚑" },
      { label: "History & Publish", path: `${ADMIN_BASE}/history`, icon: "↶" },
    ],
  },
  {
    label: "Developer",
    items: [
      { label: "QA Sandbox", path: `${ADMIN_BASE}/qa`, icon: "⌬" },
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

    const nav = element("nav", "st-admin-nav");
    for (const group of NAV_GROUPS) {
      const wrapper = element("section", "st-admin-nav-group");
      wrapper.append(element("h3", "st-admin-nav-label", group.label));
      for (const item of group.items) {
        const navButton = element(
          "button",
          `st-admin-nav-item${path === item.path ? " active" : ""}`,
        );
        navButton.type = "button";
        navButton.append(
          adminNavIcon(item.icon),
          element("span", "st-admin-nav-text", item.label),
          element("span", "st-admin-nav-phase", "B"),
        );
        navButton.addEventListener("click", () => this.navigate(item.path));
        wrapper.append(navButton);
      }
      nav.append(wrapper);
    }
    aside.append(nav);
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
    bar.append(element("span", "st-admin-revision", "PHASE B · RUNTIME"));
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
