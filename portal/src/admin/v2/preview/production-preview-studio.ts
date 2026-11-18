import "./production-preview-a16.css";
import type {
  ProductionPreviewLifecycle,
  ProductionPreviewStudioActions,
} from "./preview-contract";

export type ProductionPreviewStudioHandle = Readonly<{
  frameHost: HTMLElement;
  setLifecycle: (status: ProductionPreviewLifecycle, message: string) => void;
  bindActions: (actions: ProductionPreviewStudioActions) => void;
  dispose: () => void;
}>;

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}
function lifecycleTone(status: ProductionPreviewLifecycle): "info" | "good" | "bad" | "warn" {
  if (status === "ready") return "good";
  if (status === "error") return "bad";
  if (status === "unsupported") return "warn";
  return "info";
}

/** Shared production-preview host chrome. Domain pages retain ownership of persisted fields. */
export function createProductionPreviewStudio(host: HTMLElement, statusHost: HTMLElement): ProductionPreviewStudioHandle {
  const root = element("div", "st-admin-production-preview");
  root.tabIndex = 0;
  root.setAttribute("role", "region");
  root.setAttribute("aria-label", "Production preview");
  const frameHost = element("div", "st-admin-production-preview-frame-host");
  frameHost.setAttribute("aria-label", "Production renderer viewport");
  const actionsHost = element("div", "st-admin-production-preview-actions");
  const resetButton = element("button", "st-admin-btn", "Reset") as HTMLButtonElement;
  const replayButton = element("button", "st-admin-btn", "Replay") as HTMLButtonElement;
  const fullscreenButton = element("button", "st-admin-btn", "Fullscreen") as HTMLButtonElement;
  for (const button of [resetButton, replayButton, fullscreenButton]) button.type = "button";
  resetButton.disabled = true;
  replayButton.disabled = true;
  resetButton.setAttribute("aria-label", "Reset production preview");
  replayButton.setAttribute("aria-label", "Replay production preview scenario");
  fullscreenButton.setAttribute("aria-label", "Open production preview fullscreen");
  resetButton.title = "Reset preview (R when preview has focus)";
  replayButton.title = "Replay scenario (Space when preview has focus)";
  fullscreenButton.title = "Toggle fullscreen (F when preview has focus)";
  statusHost.setAttribute("aria-live", "polite");
  statusHost.setAttribute("aria-atomic", "true");
  actionsHost.append(resetButton, replayButton, fullscreenButton);
  root.append(frameHost, actionsHost);
  host.replaceChildren(root);

  let disposed = false;
  let actions: ProductionPreviewStudioActions | null = null;
  let actionGeneration = 0;
  let actionPending = false;

  const run = (action: "reset" | "replay"): void => {
    if (disposed || actions === null || actionPending) return;
    const current = ++actionGeneration;
    const currentActions = actions;
    actionPending = true;
    resetButton.disabled = true;
    replayButton.disabled = true;
    Promise.resolve().then(() => currentActions[action]()).catch((error: unknown) => {
      if (disposed || current !== actionGeneration) return;
      statusHost.className = "st-admin-asset-preview-status bad";
      statusHost.textContent = error instanceof Error ? error.message : String(error);
    }).finally(() => {
      if (disposed || current !== actionGeneration) return;
      actionPending = false;
      resetButton.disabled = false;
      replayButton.disabled = false;
    });
  };

  const toggleFullscreen = (): void => {
    if (disposed) return;
    if (document.fullscreenElement === root) {
      void document.exitFullscreen().catch(() => undefined);
      return;
    }
    if (root.requestFullscreen === undefined) {
      statusHost.className = "st-admin-asset-preview-status warn";
      statusHost.textContent = "Fullscreen preview is not supported by this browser.";
      return;
    }
    void root.requestFullscreen().catch((error: unknown) => {
      if (disposed) return;
      statusHost.className = "st-admin-asset-preview-status bad";
      statusHost.textContent = error instanceof Error ? error.message : String(error);
    });
  };
  const onFullscreenChange = (): void => {
    if (disposed) return;
    const active = document.fullscreenElement === root;
    fullscreenButton.textContent = active ? "Exit Fullscreen" : "Fullscreen";
    fullscreenButton.setAttribute("aria-label", active ? "Exit production preview fullscreen" : "Open production preview fullscreen");
    fullscreenButton.setAttribute("aria-pressed", String(active));
  };
  const onKeyDown = (event: KeyboardEvent): void => {
    if (event.target !== root || event.altKey || event.ctrlKey || event.metaKey) return;
    if (event.key.toLowerCase() === "r") {
      event.preventDefault();
      run("reset");
    } else if (event.key === " ") {
      event.preventDefault();
      run("replay");
    } else if (event.key.toLowerCase() === "f") {
      event.preventDefault();
      toggleFullscreen();
    }
  };

  resetButton.addEventListener("click", () => run("reset"));
  replayButton.addEventListener("click", () => run("replay"));
  fullscreenButton.addEventListener("click", toggleFullscreen);
  document.addEventListener("fullscreenchange", onFullscreenChange);
  root.addEventListener("keydown", onKeyDown);

  return Object.freeze({
    frameHost,
    setLifecycle: (status, message): void => {
      if (disposed) return;
      statusHost.className = `st-admin-asset-preview-status ${lifecycleTone(status)}`;
      statusHost.textContent = message;
      root.setAttribute("aria-busy", String(status === "loading"));
    },
    bindActions: (nextActions): void => {
      if (disposed) return;
      actions = nextActions;
      if (!actionPending) {
        resetButton.disabled = false;
        replayButton.disabled = false;
      }
    },
    dispose: (): void => {
      if (disposed) return;
      disposed = true;
      actionGeneration += 1;
      actions = null;
      document.removeEventListener("fullscreenchange", onFullscreenChange);
      root.removeEventListener("keydown", onKeyDown);
      if (document.fullscreenElement === root) void document.exitFullscreen().catch(() => undefined);
      root.remove();
    },
  });
}
