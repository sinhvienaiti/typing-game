import "./space-typing-command.css";

const BASE = "/admin/space-typing";

type Navigate = (path: string) => void;

const COMMANDS = [
  ["Overview", BASE, "Dashboard"], ["Analytics", `${BASE}/analytics`, "Dashboard"],
  ["Audio Defaults", `${BASE}/audio`, "Audio & Music"], ["Music Library", `${BASE}/music-library`, "Audio & Music"], ["World / Stage Music", `${BASE}/world-music`, "Audio & Music"],
  ["Ships", `${BASE}/ships`, "Game Content"], ["Equipment", `${BASE}/equipment`, "Game Content"], ["Skills", `${BASE}/skills`, "Game Content"], ["Enemies", `${BASE}/enemies`, "Game Content"], ["Bosses", `${BASE}/bosses`, "Game Content"], ["Worlds & Stages", `${BASE}/stages`, "Game Content"], ["Typing Content", `${BASE}/typing-content`, "Game Content"],
  ["Shop", `${BASE}/shop`, "Economy"], ["Currencies", `${BASE}/currencies`, "Economy"], ["Rewards & Drops", `${BASE}/rewards`, "Economy"], ["Stamina / Warp", `${BASE}/warp`, "Economy"],
  ["Missions", `${BASE}/missions`, "Live Ops"], ["Daily / Weekly", `${BASE}/daily-weekly`, "Live Ops"], ["Expedition", `${BASE}/expedition`, "Live Ops"], ["Events", `${BASE}/events`, "Live Ops"],
  ["Duel Settings", `${BASE}/duel`, "PvP"], ["Ranked", `${BASE}/ranked`, "PvP"], ["Alternative Modes", `${BASE}/alternative-modes`, "PvP"],
  ["Backgrounds", `${BASE}/backgrounds`, "Visuals"], ["VFX", `${BASE}/vfx`, "Visuals"], ["UI Assets", `${BASE}/ui-assets`, "Visuals"],
  ["General Settings", `${BASE}/settings`, "System"], ["Feature Flags", `${BASE}/flags`, "System"], ["History & Publish", `${BASE}/history`, "System"], ["QA Sandbox", `${BASE}/qa`, "Developer"],
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

export function openAdminCommandPalette(navigate: Navigate): void {
  closeAdminCommandPalette();
  previousFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;
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
  const key = document.createElement("kbd");
  key.textContent = "ESC";
  head.append(input, key);
  const results = document.createElement("div");
  results.className = "stx-command-results";
  const render = () => {
    const query = input.value.trim().toLowerCase();
    results.replaceChildren();
    for (const [label, path, group] of COMMANDS.filter(([label, , group]) => `${label} ${group}`.toLowerCase().includes(query)).slice(0, 12)) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "stx-command-result";
      const copy = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = label;
      const small = document.createElement("small");
      small.textContent = group;
      copy.append(strong, small);
      const arrow = document.createElement("span");
      arrow.textContent = "→";
      button.append(copy, arrow);
      button.addEventListener("click", () => { closeAdminCommandPalette(); navigate(path); });
      results.append(button);
    }
    if (!results.children.length) {
      const empty = document.createElement("div");
      empty.className = "stx-command-empty";
      empty.textContent = "No matching Admin screen.";
      results.append(empty);
    }
  };
  input.addEventListener("input", render);
  overlay.addEventListener("mousedown", (event) => { if (event.target === overlay) closeAdminCommandPalette(); });
  const onKey = (event: KeyboardEvent) => {
    if (event.key === "Escape") {
      closeAdminCommandPalette();
      return;
    }
    if (event.key === "Tab") {
      const focusables: HTMLElement[] = [input, ...Array.from(results.querySelectorAll<HTMLButtonElement>("button:not([disabled])"))];
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
  palette.append(head, results);
  overlay.append(palette);
  document.body.append(overlay);
  current = overlay;
  render();
  window.requestAnimationFrame(() => input.focus());
}

export function installAdminCommandShortcut(navigate: Navigate): () => void {
  const listener = (event: KeyboardEvent) => {
    if (!location.pathname.startsWith(BASE)) return;
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openAdminCommandPalette(navigate);
    }
  };
  document.addEventListener("keydown", listener);
  return () => document.removeEventListener("keydown", listener);
}