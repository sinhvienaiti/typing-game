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

function lifecycleTone(status: ProductionPreviewLifecycle): "info" | "good" | "bad" | "warn" {
  if (status === "ready") return "good";
  if (status === "error") return "bad";
  if (status === "unsupported") return "warn";
  return "info";
}

/** Shared production-preview host chrome. Domain pages retain ownership of persisted fields. */
export function createProductionPreviewStudio(
  host: HTMLElement,
  statusHost: HTMLElement,
): ProductionPreviewStudioHandle {
  const root = element("div", "st-admin-production-preview");
  const frameHost = element("div", "st-admin-production-preview-frame-host");
  const actionsHost = element("div", "st-admin-production-preview-actions");
  const resetButton = element("button", "st-admin-btn", "Reset");
  const replayButton = element("button", "st-admin-btn", "Replay");
  const fullscreenButton = element("button", "st-admin-btn", "Fullscreen");
  resetButton.type = "button";
  replayButton.type = "button";
  fullscreenButton.type = "button";
  actionsHost.append(resetButton, replayButton, fullscreenButton);
  root.append(frameHost, actionsHost);
  host.replaceChildren(root);

  let disposed = false;
  let actions: ProductionPreviewStudioActions | null = null;

  const run = (action: "reset" | "replay"): void => {
    if (disposed || actions === null) return;
    resetButton.disabled = true;
    replayButton.disabled = true;
    Promise.resolve(actions[action]()).catch((error: unknown) => {
      const message = error instanceof Error ? error.message : String(error);
      statusHost.className = "st-admin-asset-preview-status bad";
      statusHost.textContent = message;
    }).finally(() => {
      if (disposed) return;
      resetButton.disabled = false;
      replayButton.disabled = false;
    });
  };

  resetButton.addEventListener("click", () => run("reset"));
  replayButton.addEventListener("click", () => run("replay"));
  fullscreenButton.addEventListener("click", () => {
    if (disposed) return;
    if (root.requestFullscreen === undefined) {
      statusHost.className = "st-admin-asset-preview-status warn";
      statusHost.textContent = "Fullscreen preview is not supported by this browser.";
      return;
    }
    void root.requestFullscreen().catch((error: unknown) => {
      statusHost.className = "st-admin-asset-preview-status bad";
      statusHost.textContent = error instanceof Error ? error.message : String(error);
    });
  });

  return Object.freeze({
    frameHost,
    setLifecycle: (status, message): void => {
      if (disposed) return;
      statusHost.className = `st-admin-asset-preview-status ${lifecycleTone(status)}`;
      statusHost.textContent = message;
    },
    bindActions: (nextActions): void => {
      actions = nextActions;
      resetButton.disabled = false;
      replayButton.disabled = false;
    },
    dispose: (): void => {
      if (disposed) return;
      disposed = true;
      actions = null;
      root.remove();
    },
  });
}
