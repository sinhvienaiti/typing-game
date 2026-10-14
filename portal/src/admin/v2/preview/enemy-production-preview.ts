import { ProductionPreviewBridge } from "./production-preview-bridge";
import { createProductionPreviewStudio } from "./production-preview-studio";
import {
  enemyProductionPreviewAdapter,
  type EnemyProductionPreviewCandidate,
  type EnemyProductionPreviewScenario,
} from "./adapters/enemies";
import type { ProductionPreviewSource } from "./preview-contract";

export type EnemyProductionPreviewPanelHandle = Readonly<{
  root: HTMLElement;
  dispose: () => void;
}>;

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function selectField<T extends string>(
  label: string,
  value: T,
  options: readonly Readonly<{ value: T; label: string }>[]
): Readonly<{ root: HTMLElement; control: HTMLSelectElement }> {
  const root = element("label", "stx-field");
  root.append(element("span", undefined, label));
  const control = element("select", "st-admin-select") as HTMLSelectElement;
  control.setAttribute("aria-label", label);
  for (const option of options) control.append(new Option(option.label, option.value));
  control.value = value;
  root.append(control);
  return Object.freeze({ root, control });
}

function panel(title: string, subtitle: string): HTMLElement {
  const root = element("section", "st-admin-panel solid stx-panel");
  const head = element("div", "st-admin-panel-head");
  const copy = element("div");
  copy.append(element("h2", undefined, title), element("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}

/**
 * Administrator-facing Enemy preview chrome. Rendering stays in the child
 * production runtime; this module owns only source/scenario controls and the
 * isolated preview bridge lifecycle.
 */
export function createEnemyProductionPreviewPanel(definitionId: string): EnemyProductionPreviewPanelHandle {
  const root = panel(
    "Production Preview",
    "Exact child production Enemy renderer · isolated preview state · no progression mutation",
  );
  const controls = element("div", "stx-grid");
  const source = selectField<ProductionPreviewSource>("Preview Source", "published", [
    { value: "published", label: "Published · production registry" },
    { value: "draft", label: "Draft · current Admin candidate" },
  ]);
  const scenario = selectField<EnemyProductionPreviewScenario>("Scenario", "idle", [
    { value: "idle", label: "Idle" },
    { value: "hit", label: "Hit" },
    { value: "death", label: "Death" },
  ]);
  controls.append(source.root, scenario.root);

  const previewHost = element("div", "st-admin-production-preview-shell");
  const previewStatus = element(
    "div",
    "st-admin-asset-preview-status info",
    "Connecting to child production preview…",
  );
  previewStatus.setAttribute("aria-live", "polite");
  root.append(
    controls,
    element(
      "div",
      "stx-notice info",
      "Enemy identity/visuals are currently child-owned. Draft and Published therefore render the same canonical definition until per-Enemy visual overrides gain a production consumer.",
    ),
    previewHost,
    previewStatus,
  );

  const studio = createProductionPreviewStudio(previewHost, previewStatus);
  const candidate: EnemyProductionPreviewCandidate = Object.freeze({ definitionId });
  let bridge: ProductionPreviewBridge<EnemyProductionPreviewCandidate, EnemyProductionPreviewScenario, never> | null = null;
  let disposed = false;
  let generation = 0;
  let wasConnected = false;

  const updateSourceStatus = (): void => {
    if (disposed || bridge === null) return;
    if (source.control.value === "draft") {
      studio.setLifecycle(
        "ready",
        "Draft selected · no draft visual override exists yet, so the child renders the canonical production Enemy definition.",
      );
    } else {
      studio.setLifecycle("ready", "Published production Enemy definition is rendering in the isolated child runtime.");
    }
  };

  const load = async (nextScenario: EnemyProductionPreviewScenario): Promise<void> => {
    const activeBridge = bridge;
    if (disposed || activeBridge === null) return;
    await activeBridge.loadCandidate(candidate);
    if (disposed || activeBridge !== bridge) return;
    await activeBridge.setScenario(nextScenario);
  };

  const dispose = (): void => {
    if (disposed) return;
    disposed = true;
    generation += 1;
    bridge?.disposeImmediately();
    bridge = null;
    studio.dispose();
    observer.disconnect();
  };

  const observer = new MutationObserver(() => {
    if (disposed) return;
    if (root.isConnected) {
      wasConnected = true;
      return;
    }
    if (wasConnected) dispose();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });

  source.control.addEventListener("change", updateSourceStatus);
  scenario.control.addEventListener("change", () => {
    if (disposed || bridge === null) return;
    const next = scenario.control.value as EnemyProductionPreviewScenario;
    studio.setLifecycle("loading", `Applying ${next} scenario in child production runtime…`);
    void bridge.setScenario(next).then(
      () => updateSourceStatus(),
      (error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error)),
    );
  });

  const mountGeneration = ++generation;
  studio.setLifecycle("loading", "Connecting to isolated child production preview…");
  void ProductionPreviewBridge.mount(studio.frameHost, enemyProductionPreviewAdapter).then(async (mounted) => {
    if (disposed || mountGeneration !== generation) {
      mounted.disposeImmediately();
      return;
    }
    bridge = mounted;
    await mounted.waitUntilReady();
    if (disposed || mounted !== bridge) return;
    await load("idle");
    if (disposed || mounted !== bridge) return;
    studio.bindActions({
      reset: async () => {
        scenario.control.value = "idle";
        await mounted.reset();
        if (disposed || mounted !== bridge) return;
        await mounted.loadCandidate(candidate);
        if (disposed || mounted !== bridge) return;
        await mounted.setScenario("idle");
        updateSourceStatus();
      },
      replay: async () => {
        await mounted.replay();
        updateSourceStatus();
      },
    });
    updateSourceStatus();
  }).catch((error: unknown) => {
    if (disposed || mountGeneration !== generation) return;
    studio.setLifecycle("error", error instanceof Error ? error.message : String(error));
  });

  return Object.freeze({ root, dispose });
}
