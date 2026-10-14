import {
  ProductionPreviewBridge,
  resolveSpaceTypingProductionPreviewTarget,
} from "./v2/preview/production-preview-bridge";
import {
  shipProductionPreviewAdapter,
  type ShipProductionPreviewCandidate,
  type ShipProductionPreviewScenario,
  type ShipProductionPreviewSource,
} from "./v2/preview/adapters/ships";

export type SpaceTypingAssetPreviewScenario = ShipProductionPreviewScenario;
export type SpaceTypingAssetPreviewSource = ShipProductionPreviewSource;
export type SpaceTypingShipPreviewCandidate = ShipProductionPreviewCandidate;

export const resolveSpaceTypingAssetPreviewTarget = resolveSpaceTypingProductionPreviewTarget;

/**
 * Compatibility facade for the existing Ships page. The shared A10.5
 * ProductionPreviewBridge now owns isolation, security, stale cancellation and
 * lifecycle; this facade keeps A5 callers source-compatible.
 */
export class SpaceTypingAssetPreviewBridge {
  private constructor(
    private readonly bridge: ProductionPreviewBridge<
      ShipProductionPreviewCandidate,
      ShipProductionPreviewScenario,
      Readonly<Record<string, unknown>>
    >,
  ) {}

  static async mount(host: HTMLElement): Promise<SpaceTypingAssetPreviewBridge> {
    const bridge = await ProductionPreviewBridge.mount(host, shipProductionPreviewAdapter);
    return new SpaceTypingAssetPreviewBridge(bridge);
  }

  get iframe(): HTMLIFrameElement {
    return this.bridge.iframe;
  }

  get origin(): string {
    return this.bridge.origin;
  }

  get previewSessionId(): string {
    return this.bridge.previewSessionId;
  }

  async waitUntilReady(): Promise<void> {
    return this.bridge.waitUntilReady();
  }

  loadShip(candidate: ShipProductionPreviewCandidate): Promise<unknown> {
    return this.bridge.loadCandidate(candidate);
  }

  async setScenario(scenario: ShipProductionPreviewScenario): Promise<unknown> {
    return this.bridge.setScenario(scenario);
  }

  async setTuning(visual: Readonly<Record<string, unknown>>): Promise<unknown> {
    return this.bridge.setTuning(visual);
  }

  async setPaused(paused: boolean): Promise<unknown> {
    return this.bridge.setPaused(paused);
  }

  async reset(): Promise<unknown> {
    return this.bridge.reset();
  }

  async replay(): Promise<void> {
    return this.bridge.replay();
  }

  async dispose(): Promise<void> {
    return this.bridge.dispose();
  }

  disposeImmediately(): void {
    this.bridge.disposeImmediately();
  }
}
