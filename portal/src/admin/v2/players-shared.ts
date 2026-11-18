import { SpaceTypingAdminApi } from "../api";
import "./players.css";

/**
 * Shared bits for the Players and Mail & Gift Codes screens. Both talk to
 * /api/admin/space-typing/accounts/* (admin/account-bridge.mjs), which checks
 * the admin's role and forwards to the Cloudflare Worker/D1 account service.
 */
export const accountsApi = new SpaceTypingAdminApi();
export const ACCOUNTS = "/api/admin/space-typing/accounts";

export type Reward = { credits?: number; alloy?: number; starCrystal?: number; quantumCore?: number; warp?: number; shields?: number };

export const REWARD_FIELDS: readonly { key: keyof Reward; label: string; max: number }[] = [
  { key: "credits", label: "Credits", max: 1_000_000 },
  { key: "alloy", label: "Alloy", max: 100_000 },
  { key: "starCrystal", label: "Star Crystal", max: 5_000 },
  { key: "quantumCore", label: "Quantum Core", max: 50 },
  { key: "warp", label: "Warp", max: 300 },
  { key: "shields", label: "Streak shield", max: 2 },
];

export function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

export function button(label: string, onClick: () => void, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

export function chip(label: string, tone: "info" | "good" | "warn" | "bad" = "info"): HTMLElement {
  return el("span", `st-admin-v2-chip ${tone}`, label);
}

export function panel(title: string, subtitle?: string): { root: HTMLElement; body: HTMLElement } {
  const root = el("section", "st-admin-panel solid stx-panel pl-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  const body = el("div", "pl-panel-body");
  root.append(head, body);
  return { root, body };
}

export function formatTime(value: unknown): string {
  if (typeof value !== "string" && typeof value !== "number") return "—";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "—";
  return date.toLocaleString("vi-VN", { dateStyle: "short", timeStyle: "short" });
}

export function ago(value: unknown): string {
  if (typeof value !== "string" && typeof value !== "number") return "never";
  const ms = Date.now() - new Date(value).getTime();
  if (!Number.isFinite(ms)) return "—";
  const minutes = Math.round(ms / 60_000);
  if (minutes < 1) return "just now";
  if (minutes < 60) return minutes + " min ago";
  const hours = Math.round(minutes / 60);
  if (hours < 48) return hours + " h ago";
  return Math.round(hours / 24) + " days ago";
}

export function rewardText(reward: unknown): string {
  if (reward === null || typeof reward !== "object") return "—";
  const parts = REWARD_FIELDS.flatMap((field) => {
    const amount = (reward as Reward)[field.key];
    return typeof amount === "number" && amount !== 0 ? [(amount > 0 ? "+" : "") + amount.toLocaleString() + " " + field.label] : [];
  });
  return parts.length > 0 ? parts.join(" · ") : "—";
}

/** Number inputs for a reward; read() returns only positive amounts. */
export function rewardInputs(): { root: HTMLElement; read(): Reward; reset(): void } {
  const root = el("div", "pl-reward-grid");
  const inputs = new Map<keyof Reward, HTMLInputElement>();
  for (const field of REWARD_FIELDS) {
    const label = el("label", "pl-field");
    label.append(el("span", undefined, field.label));
    const input = el("input");
    input.type = "number";
    input.min = "0";
    input.max = String(field.max);
    input.step = "1";
    input.placeholder = "0";
    inputs.set(field.key, input);
    label.append(input);
    root.append(label);
  }
  return {
    root,
    read() {
      const reward: Reward = {};
      for (const [key, input] of inputs) {
        const value = Math.floor(Number(input.value));
        if (Number.isFinite(value) && value > 0) reward[key] = value;
      }
      return reward;
    },
    reset() {
      for (const input of inputs.values()) input.value = "";
    },
  };
}

export function textField(label: string, options: { placeholder?: string; maxLength?: number; multiline?: boolean; type?: string } = {}): { root: HTMLElement; input: HTMLInputElement | HTMLTextAreaElement } {
  const root = el("label", "pl-field");
  root.append(el("span", undefined, label));
  const input = options.multiline ? el("textarea") : el("input");
  if (input instanceof HTMLInputElement) input.type = options.type ?? "text";
  if (options.placeholder) input.placeholder = options.placeholder;
  if (options.maxLength) input.maxLength = options.maxLength;
  root.append(input);
  return { root, input };
}

/** "datetime-local" value → ISO string or "". */
export function localToIso(value: string): string {
  if (value.trim() === "") return "";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "" : date.toISOString();
}

export type ApiFailure = { status: number; message: string };

export function failure(error: unknown): ApiFailure {
  const status = typeof (error as { status?: unknown })?.status === "number" ? (error as { status: number }).status : 0;
  const message = error instanceof Error ? error.message : String(error);
  return { status, message };
}

/** The friendly box shown when the account service is not running. */
export function offlineNotice(error: ApiFailure): HTMLElement {
  const box = el("div", "stx-notice " + (error.status === 503 ? "warn" : "bad"));
  if (error.status === 503) {
    box.append(
      el("strong", undefined, "Account service is offline. "),
      document.createTextNode("Start it in games/space-typing with "),
      el("code", undefined, "pnpm account:local"),
      document.createTextNode(" (./play.sh and ./dev.sh start it automatically)."),
    );
  } else if (error.status === 403) {
    box.textContent = "Your Admin role does not have permission for this. " + error.message;
  } else {
    box.textContent = error.message;
  }
  return box;
}

export function getJson<T>(path: string): Promise<T> {
  return accountsApi.requestJson<T>(ACCOUNTS + path);
}

export function postJson<T>(path: string, body: unknown = {}): Promise<T> {
  return accountsApi.requestJson<T>(ACCOUNTS + path, { method: "POST", body: JSON.stringify(body) });
}
