import "./space-typing-command.css";

const BASE = "/admin/space-typing";
const RESULTS_ID = "space-admin-command-results";
const STATUS_ID = "space-admin-command-status";

type Navigate = (path: string) => void;
export type AdminCommandOptions = { includeDeveloperTools?: boolean };

const PRIMARY_COMMANDS = [
  ["Overview", BASE, "Dashboard"],
  ["Shop", `${BASE}/shop`, "Economy & Live Ops"],
  ["Live Ops", `${BASE}/events`, "Economy & Live Ops"],
  ["Audio Defaults", `${BASE}/audio`, "System"], ["Media Library", `${BASE}/media`, "Media"], ["Music Library", `${BASE}/music-library`, "Media"], ["SFX", `${BASE}/sfx`, "Media"], ["World / Stage Music", `${BASE}/world-music`, "Media"],
  ["Ships", `${BASE}/ships`, "Gameplay"], ["Equipment", `${BASE}/equipment`, "Gameplay"], ["Skills", `${BASE}/skills`, "Gameplay"], ["Enemies", `${BASE}/enemies`, "Gameplay"], ["Bosses", `${BASE}/bosses`, "Gameplay"], ["Worlds & Stages", `${BASE}/stages`, "Content"], ["Typing Content", `${BASE}/typing-content`, "Content"],
  ["General Settings", `${BASE}/settings`, "System"], ["Roles & Permissions", `${BASE}/roles`, "System"], ["History & Publish", `${BASE}/history`, "System"],
] as const;

const DEVELOPER_COMMANDS = [
  ["Developer Tools", `${BASE}/developer-tools`, "Developer Tools"],
  ["Analytics", `${BASE}/analytics`, "Developer Tools · Runtime"],
  ["Currencies", `${BASE}/currencies`, "Developer Tools · Runtime"], ["Rewards & Drops", `${BASE}/rewards`, "Developer Tools · Runtime"], ["Stamina / Warp", `${BASE}/warp`, "Developer Tools · Runtime"], ["Expedition", `${BASE}/expedition`, "Developer Tools · Runtime"],
  ["Missions", `${BASE}/missions`, "Developer Tools · Contracts"], ["Daily / Weekly", `${BASE}/daily-weekly`, "Developer Tools · Contracts"], ["Feature Gates", `${BASE}/feature-gates`, "Developer Tools · Validation"],
  ["Duel Settings", `${BASE}/duel`, "Developer Tools · PvP"], ["Ranked", `${BASE}/ranked`, "Developer Tools · PvP"], ["Alternative Modes", `${BASE}/alternative-modes`, "Developer Tools · PvP"],
  ["Backgrounds", `${BASE}/backgrounds`, "Developer Tools · Assets"], ["VFX", `${BASE}/vfx`, "Developer Tools · Assets"], ["UI Assets", `${BASE}/ui-assets`, "Developer Tools · Assets"],
  ["QA Sandbox", `${BASE}/qa`, "Developer Tools · QA"],
] as const;

let current: HTMLElement | null = null;
let currentCleanup: (() => void) | null = null;
let previousFocus: HTMLElement | null = null;

export function closeAdminCommandPalette(): void {
  const focusTarget = previousFocus;
  currentCleanup?.();
  currentCleanup = null;
  current?.remove();
  current = null;
  previousFocus = null;
  focusTarget?.focus();
}

export function openAdminCommandPalette(navigate: Navigate, options: AdminCommandOptions = {}): void {
  closeAdminCommandPalette();
  previousFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;
  const commands = options.includeDeveloperTools
    ? [...PRIMARY_COMMANDS, ...DEVELOPER_COMMANDS]
    : [...PRIMARY_COMMANDS];
  const overlay = document.createElement("div");
  overlay.className = "stx-command-overlay";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-modal", "true");
  overlay.setAttribute("aria-label", "Admin command search");
  const palette = document.createElement("section");
  palette.className = "stx-command-palette";
  const head = document.createElement("div");
  head.className = "stx-command-head";
  const input = document.createElement("input");
  input.type = "search";
  input.placeholder = "Search screens, settings, content…";
  input.setAttribute("aria-label", "Search Admin commands");
  input.setAttribute("aria-controls", RESULTS_ID);
  input.setAttribute("aria-describedby", STATUS_ID);
  const key = document.createElement("kbd");
  key.textContent = "ESC";
  head.append(input, key);
  const results = document.createElement("div");
  results.className = "stx-command-results";
  results.id = RESULTS_ID;
  const status = document.createElement("div");
  status.id = STATUS_ID;
  status.className = "stx-command-status";
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.setAttribute("aria-atomic", "true");
  const resultButtons = (): HTMLButtonElement[] => Array.from(results.querySelectorAll<HTMLButtonElement>("button.stx-command-result:not([disabled])"));
  const render = () => {
    const query = input.value.trim().toLowerCase();
    const matches = commands.filter(([label, , group]) => `${label} ${group}`.toLowerCase().includes(query)).slice(0, 12);
    results.replaceChildren();
    for (const [label, path, group] of matches) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "stx-command-result";
      button.setAttribute("aria-label", `${label}, ${group}`);
      const copy = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = label;
      const small = document.createElement("small");
      small.textContent = group;
      copy.append(strong, small);
      const arrow = document.createElement("span");
      arrow.textContent = "→";
      arrow.setAttribute("aria-hidden", "true");
      button.append(copy, arrow);
      button.addEventListener("click", () => { closeAdminCommandPalette(); navigate(path); });
      results.append(button);
    }
    if (matches.length === 0) {
      const empty = document.createElement("div");
      empty.className = "stx-command-empty";
      empty.textContent = "No matching Admin screen.";
      results.append(empty);
      status.textContent = "No matching Admin screen.";
    } else {
      status.textContent = `${matches.length} matching Admin ${matches.length === 1 ? "screen" : "screens"}. Use the arrow keys to move through results.`;
    }
  };
  input.addEventListener("input", render);
  overlay.addEventListener("mousedown", (event) => { if (event.target === overlay) closeAdminCommandPalette(); });
  const onKey = (event: KeyboardEvent) => {
    if (event.key === "Escape") {
      closeAdminCommandPalette();
      return;
    }
    const buttons = resultButtons();
    const activeIndex = buttons.findIndex((button) => button === document.activeElement);
    if (event.key === "ArrowDown" && buttons.length > 0) {
      event.preventDefault();
      buttons[activeIndex >= 0 ? (activeIndex + 1) % buttons.length : 0]?.focus();
      return;
    }
    if (event.key === "ArrowUp" && buttons.length > 0) {
      event.preventDefault();
      buttons[activeIndex >= 0 ? (activeIndex - 1 + buttons.length) % buttons.length : buttons.length - 1]?.focus();
      return;
    }
    if (event.key === "Home" && activeIndex >= 0 && buttons.length > 0) {
      event.preventDefault();
      buttons[0]?.focus();
      return;
    }
    if (event.key === "End" && activeIndex >= 0 && buttons.length > 0) {
      event.preventDefault();
      buttons[buttons.length - 1]?.focus();
      return;
    }
    if (event.key === "Tab") {
      const focusables: HTMLElement[] = [input, ...buttons];
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (first === undefined || last === undefined) return;
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  };
  document.addEventListener("keydown", onKey);
  currentCleanup = () => document.removeEventListener("keydown", onKey);
  palette.append(head, results, status);
  overlay.append(palette);
  document.body.append(overlay);
  current = overlay;
  render();
  window.requestAnimationFrame(() => input.focus());
}

export function installAdminCommandShortcut(
  navigate: Navigate,
  getOptions: () => AdminCommandOptions = () => ({}),
): () => void {
  const listener = (event: KeyboardEvent) => {
    if (!location.pathname.startsWith(BASE)) return;
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openAdminCommandPalette(navigate, getOptions());
    }
  };
  document.addEventListener("keydown", listener);
  return () => document.removeEventListener("keydown", listener);
}
