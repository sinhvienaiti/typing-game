import { SpaceTypingAdminApi } from "../../../api";
import { ProductionPreviewBridge } from "../production-preview-bridge";
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
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Production Preview"),
    el("p", undefined, "Boss painted production renderer + production aura/CombatFx · isolated child runtime"),
  );
  head.append(copy);
  root.append(head);

  const grid = el("div", "stx-grid");
  const boss = field("Boss");
  const source = field("Preview Source");
  source.control.append(new Option("Published · production registry", "published"), new Option("Draft · identity migration preview", "draft"));
  source.control.value = "published" satisfies ProductionPreviewSource;
  const scenario = field("Scenario");
  for (const [value, label] of [["idle", "Idle"], ["phase", "Phase"], ["hit", "Hit"], ["death", "Death"]] as const) {
    scenario.control.append(new Option(label, value));
  }
  grid.append(boss.root, source.root, scenario.root);

  const frameHost = el("div", "st-admin-production-preview-shell");
  const status = el("div", "st-admin-asset-preview-status info", "Loading canonical Boss registry…");
  status.setAttribute("aria-live", "polite");
  root.append(
    grid,
    el("div", "stx-notice info", "Boss art selection is child-owned today. Name/title migration data does not change the visual candidate, so Draft and Published intentionally render the same production Boss asset."),
    frameHost,
    status,
  );

  const studio = createProductionPreviewStudio(frameHost, status);
  let bridge: ProductionPreviewBridge<BossProductionPreviewCandidate, BossProductionPreviewScenario, never> | null = null;
  let disposed = false;
  let bosses: readonly BossPreviewItem[] = [];
  let generation = 0;
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

  const apply = async (): Promise<void> => {
    const active = bridge;
    const candidate = selectedCandidate();
    if (disposed || active === null || candidate === null) return;
    const activeGeneration = ++generation;
    studio.setLifecycle("loading", "Applying Boss candidate in child production runtime…");
    await active.loadCandidate(candidate);
    if (disposed || active !== bridge || activeGeneration !== generation) return;
    await active.setScenario(scenario.control.value as BossProductionPreviewScenario);
    if (disposed || active !== bridge || activeGeneration !== generation) return;
    describeReady();
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
    if (root.isConnected) connectedOnce = true;
    else if (connectedOnce) dispose();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });

  boss.control.addEventListener("change", () => void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error))));
  scenario.control.addEventListener("change", () => void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error))));
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
        await apply();
      },
      replay: async () => {
        await mounted.replay();
        describeReady();
      },
    });
    await apply();
  }).catch((error: unknown) => {
    if (!disposed) studio.setLifecycle("error", error instanceof Error ? error.message : String(error));
  });

  return Object.freeze({ root, dispose });
}
