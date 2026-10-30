// Small DOM helpers shared by the three Typing Feel pages.
import "./typing-feel.css";
import { createAdminEmptyState, createAdminErrorState, createAdminStatusChip, type AdminTone } from "../v2/admin-components";
import type { TypingFeelSession } from "./session";

export function el<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

export function button(label: string, onClick: () => void, className = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", className, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

/**
 * A button that carries data-admin-permission (§3.13). It is hidden when the
 * role lacks the permission; the server checks every permission again (P09).
 */
export function permissionButton(label: string, permission: string, allowed: boolean, onClick: () => void, className = "st-admin-btn"): HTMLButtonElement {
  const node = button(label, onClick, className);
  node.dataset["adminPermission"] = permission;
  node.hidden = !allowed;
  return node;
}

export function chip(label: string, tone: AdminTone = "info"): HTMLElement {
  return createAdminStatusChip(label, tone);
}

export function panel(title: string, subtitle?: string, className = ""): { root: HTMLElement; body: HTMLElement; head: HTMLElement } {
  const root = el("section", `st-admin-panel solid tf-panel ${className}`.trim());
  const head = el("div", "st-admin-panel-head");
  const copy = el("div", "grow");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  const body = el("div", "tf-panel-body");
  root.append(head, body);
  return { root, body, head };
}

export function formatTime(value: string | null | undefined): string {
  if (!value) return "Unknown time";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? value : date.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

export function title(value: string): string {
  return value.replace(/[-_]/g, " ").replace(/\b\w/g, (letter) => letter.toUpperCase());
}

export function commandLine(command: string): HTMLElement {
  const code = el("code", "tf-command", command);
  code.tabIndex = 0;
  code.title = "Run this in a terminal at the project root.";
  return code;
}

/**
 * What every Typing Feel page shows before it can edit: loading, Typing Feel
 * off (503), the store not imported yet, or the state unreadable. Returns null
 * when the session is ready.
 */
export function sessionGate(session: TypingFeelSession, retry: () => void): HTMLElement | null {
  if (session.phase === "loading") {
    const host = el("div", "tf-loading");
    host.append(el("p", "st-admin-notice", "Loading Typing Feel…"));
    return host;
  }
  if (session.phase === "unavailable") {
    return createAdminErrorState({ title: "Typing Feel is off on this Admin service", message: session.failure ?? "The Admin service reports Typing Feel as unavailable. See the Admin server log.", retry });
  }
  if (session.phase === "error") {
    return createAdminErrorState({ title: "Typing Feel could not be loaded", message: session.failure ?? "Check the local Admin service, then retry.", retry });
  }
  if (session.phase === "not-imported" && session.state && !session.state.initialized) {
    const commands = el("div", "tf-setup");
    commands.append(
      el("p", undefined, "Run this once on the home Mac, from the project root. It records today's sound sets as the first revision; the games' catalogue does not change:"),
      commandLine(session.state.setup.importCommand),
      el("p", undefined, "On a fresh clone without the Audio Lab staging folder, restore from the catalogue in Git instead:"),
      commandLine(session.state.setup.restoreCommand),
    );
    return createAdminEmptyState({ title: "Typing Feel is not imported yet", message: "Keyboard Sounds, Typing Effects and Release & History open after the one-off import. Until then nothing here can change the games.", action: commands });
  }
  return null;
}

/** Marks a control so a re-render can give focus back to its replacement. */
export function focusKey<T extends HTMLElement>(node: T, key: string): T {
  node.dataset["focusKey"] = key;
  return node;
}

/** Marks a container (a set card, a family row) so focus can fall back to it when its control is disabled or gone. */
export function focusGroup<T extends HTMLElement>(node: T, group: string): T {
  node.dataset["focusGroup"] = group;
  return node;
}

function usable(node: HTMLElement | null | undefined): node is HTMLElement {
  return Boolean(node) && !node!.hidden && !(node as HTMLButtonElement).disabled;
}

/**
 * Pages re-render after every edit; this keeps keyboard focus on the control the
 * user was on (for example a card's Move down, or the volume slider), so arrow
 * keys and Tab keep working. When that control is now disabled (Set default, a
 * move to the first or last place) focus goes to the opposite move button, else
 * to its card or row, which announces the new state; never to the page body.
 */
export function keepFocus(root: HTMLElement, render: () => void): void {
  const active = document.activeElement;
  const inside = active instanceof HTMLElement && root.contains(active);
  const key = inside ? active.dataset["focusKey"] ?? null : null;
  const group = inside ? active.closest<HTMLElement>("[data-focus-group]")?.dataset["focusGroup"] ?? null : null;
  render();
  if (!key && !group) return;
  const byKey = (wanted: string) => [...root.querySelectorAll<HTMLElement>("[data-focus-key]")].find((node) => node.dataset["focusKey"] === wanted) ?? null;
  const next = key ? byKey(key) : null;
  if (usable(next)) {
    next.focus({ preventScroll: true });
    return;
  }
  const move = key ? /^(.*):(up|down)$/.exec(key) : null;
  const opposite = move ? byKey(`${move[1]}:${move[2] === "up" ? "down" : "up"}`) : null;
  if (usable(opposite)) {
    opposite.focus({ preventScroll: true });
    return;
  }
  const container = group ? [...root.querySelectorAll<HTMLElement>("[data-focus-group]")].find((node) => node.dataset["focusGroup"] === group) : null;
  if (container) {
    if (!container.hasAttribute("tabindex")) container.tabIndex = -1;
    container.focus({ preventScroll: true });
  }
}

/** Re-renders `render` on every session change while `root` stays in the page. */
export function bindSession(root: HTMLElement, session: TypingFeelSession, render: () => void): void {
  // The shell attaches the page right after renderPage returns, so an emit in
  // that same task may still see it detached; after that, detached means gone.
  let settled = false;
  setTimeout(() => {
    settled = true;
  }, 0);
  const unsubscribe = session.subscribe(() => {
    if (!root.isConnected) {
      if (settled) unsubscribe();
      return;
    }
    render();
  });
}
