import { SpaceTypingAdminApi } from "../../api";
import { ProductionPreviewBridge } from "../production-preview-bridge";
import { createProductionPreviewStudio } from "../production-preview-studio";
import {
  worldProductionPreviewAdapter,
  type WorldProductionPreviewCandidate,
  type WorldProductionPreviewScenario,
} from "../adapters/worlds";
import {
  stageProductionPreviewAdapter,
  type StageProductionPreviewCandidate,
  type StageProductionPreviewScenario,
} from "../adapters/stages";

const api = new SpaceTypingAdminApi();

type WorldPreviewItem = Readonly<{
  id: string;
  name: string;
  galaxy: number;
  stageStart: number;
  stageEnd: number;
}>;
type WorldPreviewResponse = Readonly<{
  protocolVersion: 1;
  worlds: readonly WorldPreviewItem[];
}>;

export type ProductionEnvironmentPreviewPanelHandle = Readonly<{
  root: HTMLElement;
  dispose: () => void;
}>;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function selectField(label: string): Readonly<{ root: HTMLElement; control: HTMLSelectElement }> {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("select", "st-admin-select") as HTMLSelectElement;
  control.setAttribute("aria-label", label);
  root.append(control);
  return Object.freeze({ root, control });
}

function sourceField(): Readonly<{ root: HTMLElement; control: HTMLSelectElement }> {
  const source = selectField("Preview Source");
  source.control.append(
    new Option("Published · active runtime", "published"),
    new Option("Draft · current editor context", "draft"),
  );
  source.control.value = "published";
  return source;
}

function mountCleanup(
  root: HTMLElement,
  disposeRuntime: () => void,
): Readonly<{ dispose: () => void; isDisposed: () => boolean }> {
  let disposed = false;
  let connectedOnce = false;
  const observer = new MutationObserver(() => {
    if (disposed) return;
    if (root.isConnected) connectedOnce = true;
    else if (connectedOnce) dispose();
  });
  const dispose = (): void => {
    if (disposed) return;
    disposed = true;
    observer.disconnect();
    disposeRuntime();
  };
  observer.observe(document.documentElement, { childList: true, subtree: true });
  return Object.freeze({ dispose, isDisposed: () => disposed });
}

export function createWorldProductionPreviewPanel(): ProductionEnvironmentPreviewPanelHandle {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Production Environment Preview"),
    el("p", undefined, "Canonical WorldSceneRenderer · authored background layers, ambient FX and production motion"),
  );
  head.append(copy);
  root.append(head);

  const grid = el("div", "stx-grid");
  const world = selectField("World");
  const source = sourceField();
  grid.append(world.root, source.root);
  const frameHost = el("div", "st-admin-production-preview-shell");
  const status = el("div", "st-admin-asset-preview-status info", "Loading canonical World registry…");
  status.setAttribute("aria-live", "polite");
  root.append(
    grid,
    el("div", "stx-notice info", "World roster Draft changes gameplay membership only; they do not own background art today. Draft and Published therefore intentionally use the same canonical production environment instead of a fake Admin renderer."),
    frameHost,
    status,
  );

  const studio = createProductionPreviewStudio(frameHost, status);
  let bridge: ProductionPreviewBridge<WorldProductionPreviewCandidate, WorldProductionPreviewScenario, never> | null = null;
  let worlds: readonly WorldPreviewItem[] = [];
  let generation = 0;
  const cleanup = mountCleanup(root, () => {
    generation += 1;
    bridge?.disposeImmediately();
    bridge = null;
    studio.dispose();
  });

  const apply = async (): Promise<void> => {
    const active = bridge;
    const worldId = world.control.value;
    if (cleanup.isDisposed() || active === null || worldId === "") return;
    const activeGeneration = ++generation;
    studio.setLifecycle("loading", "Applying World in child production renderer…");
    await active.loadCandidate(Object.freeze({ worldId }));
    if (cleanup.isDisposed() || active !== bridge || activeGeneration !== generation) return;
    const item = worlds.find((entry) => entry.id === worldId);
    studio.setLifecycle(
      "ready",
      item ? `${item.name} · Galaxy ${item.galaxy} · Stages ${item.stageStart}–${item.stageEnd} · production environment` : `${worldId} · production environment`,
    );
  };

  world.control.addEventListener("change", () => void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error))));
  source.control.addEventListener("change", () => void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error))));

  void api.requestJson<WorldPreviewResponse>("/api/admin/space-typing/worlds/preview", {
    method: "POST",
    body: JSON.stringify({}),
  }).then(async (payload) => {
    if (cleanup.isDisposed() || payload.protocolVersion !== 1 || !Array.isArray(payload.worlds)) return;
    worlds = payload.worlds;
    world.control.replaceChildren(...worlds.map((item) => new Option(`${item.id} · ${item.name}`, item.id)));
    if (worlds.length === 0) {
      studio.setLifecycle("unsupported", "No canonical Worlds were returned.");
      return;
    }
    const mounted = await ProductionPreviewBridge.mount(studio.frameHost, worldProductionPreviewAdapter);
    if (cleanup.isDisposed()) {
      mounted.disposeImmediately();
      return;
    }
    bridge = mounted;
    await mounted.waitUntilReady();
    if (cleanup.isDisposed() || bridge !== mounted) return;
    studio.bindActions({
      reset: async () => { await mounted.reset(); await apply(); },
      replay: async () => { await mounted.replay(); await apply(); },
    });
    await apply();
  }).catch((error: unknown) => {
    if (!cleanup.isDisposed()) studio.setLifecycle("error", error instanceof Error ? error.message : String(error));
  });

  return Object.freeze({ root, dispose: cleanup.dispose });
}

export function createStageProductionPreviewPanel(): ProductionEnvironmentPreviewPanelHandle {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Production Stage Preview"),
    el("p", undefined, "Stage → worldForStage → WorldSceneRenderer · isolated production mapping"),
  );
  head.append(copy);
  root.append(head);

  const grid = el("div", "stx-grid");
  const stageRoot = el("label", "stx-field");
  stageRoot.append(el("span", undefined, "Stage"));
  const stage = el("input") as HTMLInputElement;
  stage.type = "number";
  stage.min = "1";
  stage.max = "1000";
  stage.step = "1";
  stage.value = "1";
  stage.setAttribute("aria-label", "Stage");
  stageRoot.append(stage);
  const source = sourceField();
  grid.append(stageRoot, source.root);
  const frameHost = el("div", "st-admin-production-preview-shell");
  const status = el("div", "st-admin-asset-preview-status info", "Starting child production Stage preview…");
  status.setAttribute("aria-live", "polite");
  root.append(
    grid,
    el("div", "stx-notice info", "Stage budget/elite/modifier Draft fields affect encounter composition, not the World environment renderer. This preview shows the exact production environment selected by the canonical stage mapping and does not fabricate combat waves."),
    frameHost,
    status,
  );

  const studio = createProductionPreviewStudio(frameHost, status);
  let bridge: ProductionPreviewBridge<StageProductionPreviewCandidate, StageProductionPreviewScenario, never> | null = null;
  let generation = 0;
  const cleanup = mountCleanup(root, () => {
    generation += 1;
    bridge?.disposeImmediately();
    bridge = null;
    studio.dispose();
  });

  const apply = async (): Promise<void> => {
    const active = bridge;
    const value = Number(stage.value);
    if (cleanup.isDisposed() || active === null) return;
    if (!Number.isSafeInteger(value) || value < 1 || value > 1000) {
      studio.setLifecycle("error", "Stage must be an integer from 1 to 1000.");
      return;
    }
    const activeGeneration = ++generation;
    studio.setLifecycle("loading", `Resolving Stage ${value} in child runtime…`);
    await active.loadCandidate(Object.freeze({ stage: value }));
    if (cleanup.isDisposed() || active !== bridge || activeGeneration !== generation) return;
    studio.setLifecycle("ready", `Stage ${value} · canonical world mapping · production environment`);
  };

  stage.addEventListener("change", () => void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error))));
  source.control.addEventListener("change", () => void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error))));

  void ProductionPreviewBridge.mount(studio.frameHost, stageProductionPreviewAdapter).then(async (mounted) => {
    if (cleanup.isDisposed()) {
      mounted.disposeImmediately();
      return;
    }
    bridge = mounted;
    await mounted.waitUntilReady();
    if (cleanup.isDisposed() || bridge !== mounted) return;
    studio.bindActions({
      reset: async () => { stage.value = "1"; await mounted.reset(); await apply(); },
      replay: async () => { await mounted.replay(); await apply(); },
    });
    await apply();
  }).catch((error: unknown) => {
    if (!cleanup.isDisposed()) studio.setLifecycle("error", error instanceof Error ? error.message : String(error));
  });

  return Object.freeze({ root, dispose: cleanup.dispose });
}
