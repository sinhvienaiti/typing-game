import { SpaceTypingAdminApi } from "../../../api";
import { createImageMediaCandidateTester } from "../../media-candidate-preview";
import {
  ProductionPreviewBridge,
  ProductionPreviewStaleError,
} from "../production-preview-bridge";
import { createProductionPreviewStudio } from "../production-preview-studio";
import {
  bossProductionPreviewAdapter,
  type BossProductionPreviewCandidate,
  type BossProductionPreviewScenario,
} from "../adapters/bosses";
import type { ProductionPreviewSource } from "../preview-contract";

const api = new SpaceTypingAdminApi();

type BossPreviewItem = Readonly<{
  id: string;
  name: string;
  title: string;
  role: string;
  rank: string;
  family: string;
}>;
type BossPreviewResponse = Readonly<{
  protocolVersion: 1;
  bosses: readonly BossPreviewItem[];
}>;

export type BossProductionPreviewPanelHandle = Readonly<{
  root: HTMLElement;
  dispose: () => void;
  selectBoss: (id: string) => void;
}>;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function field(label: string): Readonly<{ root: HTMLElement; control: HTMLSelectElement }> {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("select", "st-admin-select") as HTMLSelectElement;
  control.setAttribute("aria-label", label);
  root.append(control);
  return Object.freeze({ root, control });
}

export function createBossProductionPreviewPanel(): BossProductionPreviewPanelHandle {
  const root = el("section", "st-admin-panel solid stx-panel st-admin-boss-preview-primary");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Production Preview"),
    el("p", undefined, "Boss painted production renderer + production aura/CombatFx · isolated child runtime"),
  );
  head.append(copy);
  root.append(head);

  const grid = el("div", "stx-grid st-admin-runtime-preview-grid");
  const boss = field("Boss");
  const source = field("Preview Source");
  source.control.append(new Option("Published · production registry", "published"), new Option("Draft · identity migration preview", "draft"));
  source.control.value = "published" satisfies ProductionPreviewSource;
  const scenario = field("Scenario");
  for (const [value, label] of [["idle", "Idle"], ["phase", "Phase"], ["hit", "Hit"], ["death", "Death"]] as const) {
    scenario.control.append(new Option(label, value));
  }
  grid.append(boss.root, source.root, scenario.root);

  const mediaTester = createImageMediaCandidateTester({
    title: "Boss image test candidate",
    description: "Choose an exact Media V2 image for visual QA only. Production Boss art remains canonical until Boss media binding is migrated into production authority.",
  });
  const frameHost = el("div", "st-admin-production-preview-shell st-admin-production-preview-shell--hero");
  const status = el("div", "st-admin-asset-preview-status info", "Loading canonical Boss registry…");
  status.setAttribute("aria-live", "polite");
  const mediaTools = el("details", "st-admin-preview-media-tools");
  const mediaSummary = el("summary", undefined, "Media candidate · preview only");
  mediaTools.append(mediaSummary, mediaTester.root);

  root.append(
    grid,
    el("div", "stx-notice info", "Current production Boss art renders at full size below. Media replacement is a secondary QA tool and stays collapsed until needed."),
    frameHost,
    status,
    mediaTools,
  );

  const studio = createProductionPreviewStudio(frameHost, status);
  let bridge: ProductionPreviewBridge<BossProductionPreviewCandidate, BossProductionPreviewScenario, never> | null = null;
  let disposed = false;
  let bosses: readonly BossPreviewItem[] = [];
  let pendingSelectionId: string | null = null;
  let generation = 0;
  let latestCandidate: Promise<unknown> = Promise.resolve();
  let connectedOnce = false;

  const selectedCandidate = (): BossProductionPreviewCandidate | null => {
    const id = boss.control.value;
    return id === "" ? null : Object.freeze({ bossId: id });
  };

  const describeReady = (): void => {
    const item = bosses.find((entry) => entry.id === boss.control.value);
    if (!item) return;
    studio.setLifecycle("ready", `${item.name}, ${item.title} · ${item.rank} · production Boss renderer`);
  };

  const reportError = (error: unknown): void => {
    if (disposed || error instanceof ProductionPreviewStaleError) return;
    studio.setLifecycle("error", error instanceof Error ? error.message : String(error));
  };

  const loadSelectedBoss = async (): Promise<void> => {
    const active = bridge;
    const candidate = selectedCandidate();
    if (disposed || active === null || candidate === null) return;
    const activeGeneration = ++generation;
    studio.setLifecycle("loading", "Applying Boss candidate in child production runtime…");
    const operation = active.loadCandidate(candidate);
    latestCandidate = operation;
    await operation;
    if (disposed || active !== bridge || activeGeneration !== generation) return;
    await active.setScenario(scenario.control.value as BossProductionPreviewScenario);
    if (disposed || active !== bridge || activeGeneration !== generation) return;
    describeReady();
  };

  const applyScenario = async (): Promise<void> => {
    const active = bridge;
    if (disposed || active === null) return;
    const activeGeneration = ++generation;
    studio.setLifecycle("loading", `Switching Boss scenario to ${scenario.control.value}…`);
    await latestCandidate;
    if (disposed || active !== bridge || activeGeneration !== generation) return;
    await active.setScenario(scenario.control.value as BossProductionPreviewScenario);
    if (disposed || active !== bridge || activeGeneration !== generation) return;
    describeReady();
  };

  const selectBoss = (id: string): void => {
    pendingSelectionId = id;
    if (disposed || bosses.length === 0) return;
    if (!bosses.some((item) => item.id === id)) return;
    pendingSelectionId = null;
    boss.control.value = id;
    void loadSelectedBoss().catch(reportError);
    root.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };

  const dispose = (): void => {
    if (disposed) return;
    disposed = true;
    generation += 1;
    bridge?.disposeImmediately();
    bridge = null;
    mediaTester.dispose();
    studio.dispose();
    observer.disconnect();
  };

  const observer = new MutationObserver(() => {
    if (disposed) return;
    if (root.isConnected) connectedOnce = true;
    else if (connectedOnce) dispose();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });

  boss.control.addEventListener("change", () => {
    pendingSelectionId = null;
    void loadSelectedBoss().catch(reportError);
  });
  scenario.control.addEventListener("change", () => void applyScenario().catch(reportError));
  source.control.addEventListener("change", describeReady);

  void api.requestJson<BossPreviewResponse>("/api/admin/space-typing/bosses/preview", {
    method: "POST",
    body: JSON.stringify({}),
  }).then(async (payload) => {
    if (disposed || payload.protocolVersion !== 1 || !Array.isArray(payload.bosses)) return;
    bosses = payload.bosses;
    boss.control.replaceChildren(...bosses.map((item) => new Option(`${item.name} · ${item.rank}`, item.id)));
    if (bosses.length === 0) {
      studio.setLifecycle("unsupported", "No canonical Boss identities were returned.");
      return;
    }
    const requested = pendingSelectionId;
    if (requested !== null && bosses.some((item) => item.id === requested)) {
      boss.control.value = requested;
      pendingSelectionId = null;
    }
    const mounted = await ProductionPreviewBridge.mount(studio.frameHost, bossProductionPreviewAdapter);
    if (disposed) {
      mounted.disposeImmediately();
      return;
    }
    bridge = mounted;
    await mounted.waitUntilReady();
    if (disposed || mounted !== bridge) return;
    studio.bindActions({
      reset: async () => {
        scenario.control.value = "idle";
        await mounted.reset();
        await loadSelectedBoss();
      },
      replay: async () => {
        await mounted.replay();
        describeReady();
      },
    });
    await loadSelectedBoss();
  }).catch(reportError);

  return Object.freeze({ root, dispose, selectBoss });
}
