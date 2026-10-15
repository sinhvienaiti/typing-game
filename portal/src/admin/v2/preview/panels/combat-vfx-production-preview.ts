import { SpaceTypingAdminApi, type ShipAdminPreviewItem } from "../../api";
import { ProductionPreviewBridge } from "../production-preview-bridge";
import { createProductionPreviewStudio } from "../production-preview-studio";
import {
  shipProductionPreviewAdapter,
  type ShipProductionPreviewCandidate,
  type ShipProductionPreviewScenario,
} from "../adapters/ships";

const api = new SpaceTypingAdminApi();

export type CombatVfxProductionPreviewPanelHandle = Readonly<{
  root: HTMLElement;
  dispose: () => void;
}>;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function mountCleanup(root: HTMLElement, disposeRuntime: () => void): Readonly<{ dispose: () => void; isDisposed: () => boolean }> {
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

function candidateFor(ship: ShipAdminPreviewItem): ShipProductionPreviewCandidate {
  return Object.freeze({
    characterId: ship.id,
    visual: structuredClone(ship.visual) as Readonly<Record<string, unknown>>,
    ...(ship.imageAssetVersionId === undefined ? {} : { imageAssetVersionId: ship.imageAssetVersionId }),
    ...(ship.projectileArchetype === undefined ? {} : { projectileArchetype: ship.projectileArchetype }),
  });
}

export function createCombatVfxProductionPreviewPanel(): CombatVfxProductionPreviewPanelHandle {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Production Combat Preview"),
    el("p", undefined, "Representative Ship fire context · production muzzle, projectile flight, impact and SFX"),
  );
  head.append(copy);
  root.append(head);

  const selector = el("label", "stx-field");
  selector.append(el("span", undefined, "Ship / projectile context"));
  const shipSelect = el("select", "st-admin-select") as HTMLSelectElement;
  shipSelect.setAttribute("aria-label", "Ship / projectile context");
  selector.append(shipSelect);

  const grid = el("div", "stx-grid");
  grid.append(selector);
  const frameHost = el("div", "st-admin-production-preview-shell");
  const status = el("div", "st-admin-asset-preview-status info", "Loading canonical Ship projectile contexts…");
  status.setAttribute("aria-live", "polite");
  root.append(
    grid,
    el("div", "stx-notice info", "This is a read-only production preview. VFX tuning remains code-owned: Admin reuses the same Ship renderer, PlayerShotSystem and impact/audio path used by gameplay instead of maintaining a second effects engine."),
    frameHost,
    status,
  );

  const studio = createProductionPreviewStudio(frameHost, status);
  let bridge: ProductionPreviewBridge<ShipProductionPreviewCandidate, ShipProductionPreviewScenario, Readonly<Record<string, unknown>>> | null = null;
  let ships: readonly ShipAdminPreviewItem[] = [];
  let generation = 0;
  const cleanup = mountCleanup(root, () => {
    generation += 1;
    bridge?.disposeImmediately();
    bridge = null;
    studio.dispose();
  });

  const apply = async (): Promise<void> => {
    const active = bridge;
    const ship = ships.find((entry) => entry.id === shipSelect.value);
    if (cleanup.isDisposed() || active === null || ship === undefined) return;
    const activeGeneration = ++generation;
    studio.setLifecycle("loading", `Loading ${ship.name} production fire context…`);
    await active.loadCandidate(candidateFor(ship));
    if (cleanup.isDisposed() || active !== bridge || activeGeneration !== generation) return;
    await active.setScenario("fire");
    if (cleanup.isDisposed() || active !== bridge || activeGeneration !== generation) return;
    studio.setLifecycle(
      "ready",
      `${ship.name} · ${ship.projectileArchetype ?? "canonical projectile"} · muzzle → flight → impact · production runtime`,
    );
  };

  shipSelect.addEventListener("change", () => {
    void apply().catch((error: unknown) => studio.setLifecycle("error", error instanceof Error ? error.message : String(error)));
  });

  void api.previewShips().then(async (payload) => {
    if (cleanup.isDisposed() || payload.protocolVersion !== 1) return;
    ships = payload.ships;
    shipSelect.replaceChildren(...ships.map((ship) => new Option(`${ship.name} · ${ship.projectileArchetype ?? "canonical"}`, ship.id)));
    if (ships.length === 0) {
      studio.setLifecycle("unsupported", "No canonical Ship projectile contexts were returned.");
      return;
    }
    const mounted = await ProductionPreviewBridge.mount(studio.frameHost, shipProductionPreviewAdapter);
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
