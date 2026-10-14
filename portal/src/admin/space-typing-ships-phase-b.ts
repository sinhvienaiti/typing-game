import "./space-typing-asset-preview.css";
import {
  SpaceTypingAdminApi,
  type CoreStatKey,
  type ShipAdminOverride,
  type ShipAdminPolicy,
  type ShipAdminPreview,
  type ShipAdminPreviewItem,
  type ShipVisualProfile,
  type SpaceTypingAdminConfig,
} from "./api";
import { adminErrorMessage } from "./admin-http";
import {
  SpaceTypingAssetPreviewBridge,
  type SpaceTypingAssetPreviewScenario,
  type SpaceTypingAssetPreviewSource,
} from "./space-typing-asset-preview";
import { isSpaceTypingReliefMediaVersionCompatible } from "./space-typing-relief-media";
import { AdminHelpScope, createAdminFieldShell } from "./v2/admin-help";
import { openAdminMediaAssetPicker } from "./v2/asset-picker";
import {
  createAssetTuningCapabilityState,
  createAssetTuningScalarControl,
  createAssetTuningStudio,
} from "./v2/asset-tuning-studio";

const api = new SpaceTypingAdminApi();
const CORE_STATS: readonly CoreStatKey[] = [
  "hull",
  "shield",
  "firepower",
  "armor",
  "energy",
  "reactor",
  "focus",
  "ward",
  "luck",
  "salvage",
];
const SILHOUETTES = ["spear", "fortress", "arc", "phantom", "crown", "blade"] as const;
const PROJECTILE_ARCHETYPES = [
  "spear",
  "heavy",
  "electric",
  "shadow",
  "star",
  "barrage",
  "mystic",
  "guard",
  "slash",
  "radiant",
  "cosmic",
] as const;
const BASIC_COLOR_KEYS = ["primary", "secondary", "accent"] as const;
const ADVANCED_COLOR_KEYS = ["core", "engine", "glow"] as const;
const TEXT_FIELDS = [
  ["name", "Name"],
  ["role", "Role"],
  ["summary", "Summary"],
  ["passiveName", "Passive Name"],
  ["activeName", "Active Name"],
  ["ultimateName", "Ultimate Name"],
] as const;

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type ShipId = string;
type VisualColorKey = (typeof BASIC_COLOR_KEYS)[number] | (typeof ADVANCED_COLOR_KEYS)[number];
type ProjectileArchetype = (typeof PROJECTILE_ARCHETYPES)[number];
type PreviewSurface = "2d" | "relief";

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function button(label: string, onClick: () => void, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `stx-notice ${tone}`, text);
}

function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}

function field(label: string, value: string, options?: readonly string[], type: "text" | "number" = "text"): { root: HTMLElement; control: HTMLInputElement | HTMLSelectElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  let control: HTMLInputElement | HTMLSelectElement;
  if (options) {
    const select = el("select", "st-admin-select") as HTMLSelectElement;
    for (const option of options) select.append(new Option(option, option));
    select.value = value;
    control = select;
  } else {
    const input = el("input") as HTMLInputElement;
    input.type = type;
    input.value = value;
    control = input;
  }
  control.setAttribute("aria-label", label);
  root.append(control);
  return { root, control };
}

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}

function cloneConfig(config: SpaceTypingAdminConfig): SpaceTypingAdminConfig {
  return structuredClone(config);
}

function mergeShip(base: ShipAdminPreviewItem, override?: ShipAdminOverride): ShipAdminPreviewItem {
  return {
    ...base,
    ...(override ?? {}),
    id: base.id,
    assetId: base.assetId,
    statBonus: { ...base.statBonus, ...(override?.statBonus ?? {}) },
    visual: { ...base.visual, ...(override?.visual ?? {}) },
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
}

function policyFrom(config: SpaceTypingAdminConfig): ShipAdminPolicy {
  return structuredClone(config.content?.ships ?? { configRevision: "ships-admin-v1", ships: {} });
}

function previewVisual(ship: ShipAdminPreviewItem): Readonly<Record<string, unknown>> {
  return structuredClone(ship.visual) as unknown as Readonly<Record<string, unknown>>;
}

function projectileArchetypeFor(ship: ShipAdminPreviewItem): ProjectileArchetype | undefined {
  const value = ship.projectileArchetype;
  return typeof value === "string" && PROJECTILE_ARCHETYPES.includes(value as ProjectileArchetype)
    ? value as ProjectileArchetype
    : undefined;
}

function colorLabel(key: VisualColorKey): string {
  const labels: Record<VisualColorKey, string> = {
    primary: "Primary",
    secondary: "Secondary",
    accent: "Accent",
    core: "Core",
    engine: "Engine",
    glow: "Glow",
  };
  return labels[key];
}

export function renderPhaseBShips(navigate: Navigate): HTMLElement {
  const page = el("div");
  const helpScope = new AdminHelpScope();
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Runtime-backed Registry · B06.1"),
    el("h1", undefined, "Ships"),
    el("p", undefined, "Manage canonical Ship metadata, combat bonuses and production-backed presentation. Visual tuning uses the shared A5 Asset Tuning Studio."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child ship registry…", "info");
  status.setAttribute("aria-live", "polite");

  const studio = createAssetTuningStudio({
    helpScope,
    title: "Ship Appearance",
    basicLabel: "Basic",
    sources: [
      { id: "draft", label: "Draft", help: "Current in-memory candidate, including unsaved visual edits." },
      { id: "published", label: "Published", help: "Active revision materialized separately from the Draft candidate." },
    ],
    activeSource: "draft",
    scenarios: [
      { id: "idle", label: "Idle", help: "Production idle presentation. Scenario state is not persisted." },
      { id: "move", label: "Move", help: "Production movement presentation. Scenario state is not persisted." },
      { id: "fire", label: "Fire", help: "Production Ship projectile path. This does not create a Weapon Admin entity." },
    ],
    activeScenario: "idle",
    onSourceChange: (source) => selectPreviewSource(source as SpaceTypingAssetPreviewSource),
    onScenarioChange: (scenario) => selectPreviewScenario(scenario as SpaceTypingAssetPreviewScenario),
  });
  const previewHost = studio.previewHost;
  const previewStatus = studio.previewStatus;

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Fleet", "11 child-owned ship IDs · IDs and asset IDs are immutable");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Ship Configuration", "Metadata and combat policy stay separate from presentation tuning.");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, studio.root, body);

  let loadedActiveRevision: string | null = null;
  let bundled: ShipAdminPreview | null = null;
  let publishedPreview: ShipAdminPreview | null = null;
  let selectedId: ShipId = "vanguard";
  let policy: ShipAdminPolicy = { configRevision: "ships-admin-v1", ships: {} };
  let serviceReady = false;
  let loadGeneration = 0;
  let previewSource: SpaceTypingAssetPreviewSource = "draft";
  let previewScenario: SpaceTypingAssetPreviewScenario = "idle";
  let previewSurface: PreviewSurface = "2d";
  let previewGeneration = 0;
  let previewBridge: SpaceTypingAssetPreviewBridge | null = null;
  let previewBridgePromise: Promise<SpaceTypingAssetPreviewBridge> | null = null;

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const setPreviewStatus = (text: string, tone: Tone = "info"): void => {
    previewStatus.className = `st-admin-asset-preview-status ${tone}`;
    previewStatus.textContent = text;
  };

  const overrideFor = (id: ShipId): ShipAdminOverride => {
    policy.ships ??= {};
    policy.ships[id] ??= {};
    return policy.ships[id];
  };

  const pruneEmptyOverride = (id: ShipId): void => {
    const override = policy.ships?.[id];
    if (override !== undefined && Object.keys(override).length === 0) delete policy.ships?.[id];
  };

  const baseShip = (id: ShipId): ShipAdminPreviewItem | undefined =>
    bundled?.ships.find((ship) => ship.id === id);

  const effectiveShip = (id: ShipId): ShipAdminPreviewItem | undefined => {
    const base = baseShip(id);
    if (!base) return publishedPreview?.ships.find((ship) => ship.id === id);
    return mergeShip(base, policy.ships?.[id]);
  };

  const previewShip = (): ShipAdminPreviewItem | undefined =>
    previewSource === "published"
      ? publishedPreview?.ships.find((ship) => ship.id === selectedId)
      : effectiveShip(selectedId);

  function refreshPreviewControls(): void {
    studio.setSource(previewSource);
    studio.setScenario(previewScenario);
  }

  async function ensurePreviewBridge(): Promise<SpaceTypingAssetPreviewBridge> {
    if (previewBridge !== null) return previewBridge;
    if (previewBridgePromise !== null) return previewBridgePromise;
    setPreviewStatus("Connecting to isolated child production preview…", "info");
    const mountPromise = SpaceTypingAssetPreviewBridge.mount(previewHost).then(async (bridge) => {
      if (!page.isConnected) {
        bridge.disposeImmediately();
        throw new Error("Ships page was closed before preview became ready.");
      }
      previewBridge = bridge;
      await bridge.waitUntilReady();
      return bridge;
    }).catch((error: unknown) => {
      if (previewBridge?.iframe.isConnected === false) previewBridge = null;
      previewBridgePromise = null;
      throw error;
    });
    previewBridgePromise = mountPromise;
    return mountPromise;
  }

  function syncPreview(): void {
    const generation = ++previewGeneration;
    refreshPreviewControls();
    if (!serviceReady) {
      setPreviewStatus("Waiting for active revision and canonical ship registry…", "info");
      return;
    }
    const ship = previewShip();
    if (ship === undefined) {
      setPreviewStatus(`No ${previewSource} preview candidate exists for ${selectedId}.`, "warn");
      return;
    }
    const surfaceLabel = previewSurface === "relief" ? "3D relief" : "2D";
    setPreviewStatus(`Loading ${previewSource} · ${ship.id} · ${surfaceLabel} · ${previewScenario} through production renderer…`, "info");
    void ensurePreviewBridge().then(async (bridge) => {
      if (generation !== previewGeneration || !page.isConnected) return;
      const projectileArchetype = projectileArchetypeFor(ship);
      await bridge.loadShip({
        characterId: ship.id,
        visual: previewVisual(ship),
        ...(ship.imageAssetVersionId === undefined ? {} : { imageAssetVersionId: ship.imageAssetVersionId }),
        ...(previewSurface === "relief"
          ? { reliefAssetVersionId: ship.reliefAssetVersionId ?? null }
          : {}),
        ...(projectileArchetype === undefined ? {} : { projectileArchetype }),
      });
      if (generation !== previewGeneration || !page.isConnected) return;
      await bridge.setScenario(previewScenario);
      if (generation !== previewGeneration || !page.isConnected) return;
      setPreviewStatus(`${previewSource === "draft" ? "Draft" : "Published"} · ${ship.id} · ${surfaceLabel} · ${previewScenario} · production renderer`, "good");
    }).catch((error: unknown) => {
      if (generation !== previewGeneration || !page.isConnected) return;
      setPreviewStatus(error instanceof Error ? error.message : String(error), "bad");
    });
  }

  function selectPreviewSource(source: SpaceTypingAssetPreviewSource): void {
    if (previewSource === source) return;
    previewSource = source;
    syncPreview();
  }

  function selectPreviewScenario(scenario: SpaceTypingAssetPreviewScenario): void {
    if (previewScenario === scenario) return;
    previewScenario = scenario;
    const generation = ++previewGeneration;
    refreshPreviewControls();
    const bridge = previewBridge;
    if (bridge === null) {
      syncPreview();
      return;
    }
    setPreviewStatus(`Switching to ${scenario} production scenario…`, "info");
    void bridge.setScenario(scenario).then(() => {
      if (generation !== previewGeneration || !page.isConnected) return;
      const ship = previewShip();
      setPreviewStatus(`${previewSource === "draft" ? "Draft" : "Published"} · ${ship?.id ?? selectedId} · ${previewSurface === "relief" ? "3D relief" : "2D"} · ${scenario} · production renderer`, "good");
    }).catch((error: unknown) => {
      if (generation !== previewGeneration || !page.isConnected) return;
      setPreviewStatus(error instanceof Error ? error.message : String(error), "bad");
    });
  }

  const renderList = (): void => {
    listHost.replaceChildren();
    const ships = bundled?.ships ?? publishedPreview?.ships ?? [];
    if (ships.length === 0) {
      listHost.append(notice(serviceReady ? "No canonical ships were returned by the preview." : "Load the canonical ship registry to browse the fleet.", serviceReady ? "warn" : "info"));
      return;
    }
    for (const ship of ships) {
      const current = effectiveShip(ship.id) ?? ship;
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(el("strong", undefined, current.name), el("small", undefined, `${ship.id} · ${current.assetId} · stage ${current.unlockStage}`));
      const actions = el("div");
      if (policy.ships?.[ship.id] && Object.keys(policy.ships[ship.id]).length > 0) actions.append(badge("OVERRIDE", "warn"));
      const select = button(selectedId === ship.id ? "Editing" : "Edit", () => {
        selectedId = ship.id;
        renderList();
        renderEditor();
        renderStudioSettings();
        syncPreview();
      }, selectedId === ship.id ? "st-admin-btn primary" : "st-admin-btn");
      select.disabled = !serviceReady;
      actions.append(select);
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const bindText = (control: HTMLInputElement | HTMLSelectElement, key: keyof ShipAdminOverride): void => {
    control.addEventListener("input", () => {
      (overrideFor(selectedId) as Record<string, unknown>)[key] = control.value;
      renderList();
    });
  };

  const setVisualColor = (key: VisualColorKey, value: string): void => {
    const override = overrideFor(selectedId);
    override.visual ??= {};
    override.visual[key] = value;
    syncPreview();
  };

  const createVisualColorField = (key: VisualColorKey, ship: ShipAdminPreviewItem): HTMLElement => {
    const input = el("input") as HTMLInputElement;
    input.type = "text";
    input.value = ship.visual[key];
    input.spellcheck = false;
    input.addEventListener("input", () => setVisualColor(key, input.value));
    return createAdminFieldShell(helpScope, {
      label: colorLabel(key),
      control: input,
    });
  };

  const renderStudioSettings = (): void => {
    studio.basicHost.replaceChildren();
    studio.advancedHost.replaceChildren();
    const ship = effectiveShip(selectedId);
    if (!serviceReady || !ship) {
      studio.basicHost.append(notice(serviceReady ? "No ship is available for tuning." : "Load the canonical fleet before tuning presentation.", serviceReady ? "warn" : "info"));
      studio.advancedHost.append(notice("Capability state will appear after the canonical fleet loads.", "info"));
      return;
    }

    const baseline = baseShip(selectedId) ?? ship;
    const imageActions = el("div", "st-admin-page-actions");
    const chooseImage = button(ship.imageAssetVersionId ? "Change image" : "Choose image", () => {
      openAdminMediaAssetPicker({
        title: `Choose image for ${ship.name}`,
        message: "Select an image from the Media Library. The exact immutable version is stored in this Ship draft.",
        allowedKinds: ["image"],
        selectedAssetVersionId: ship.imageAssetVersionId ?? null,
        returnFocus: chooseImage,
        onSelect: ({ version }) => {
          overrideFor(selectedId).imageAssetVersionId = version.assetVersionId;
          previewSurface = "2d";
          renderList();
          renderStudioSettings();
          syncPreview();
          setStatus(`${selectedId} now uses Media V2 image ${version.assetVersionId}. Save Draft to persist this assignment.`, "good");
        },
      });
    });
    imageActions.append(chooseImage, button("Preview 2D", () => {
      previewSurface = "2d";
      syncPreview();
    }));
    if (ship.imageAssetVersionId !== undefined) {
      imageActions.append(button("Clear", () => {
        const override = policy.ships?.[selectedId];
        if (override !== undefined) {
          delete override.imageAssetVersionId;
          pruneEmptyOverride(selectedId);
        }
        previewSurface = "2d";
        renderList();
        renderStudioSettings();
        syncPreview();
        setStatus(`${selectedId} image override cleared. The bundled production image is restored for this Draft.`, "good");
      }));
    }
    studio.basicHost.append(createAdminFieldShell(helpScope, {
      label: "Ship Image",
      control: imageActions,
      help: {
        title: "Ship Image",
        content: "Choose an image through Media V2. The Draft stores the exact immutable asset version; Clear restores the bundled production image.",
      },
      stateMessage: ship.imageAssetVersionId === undefined
        ? "Bundled production image"
        : `Exact version · ${ship.imageAssetVersionId}`,
      stateTone: ship.imageAssetVersionId === undefined ? "info" : "good",
    }));

    const reliefActions = el("div", "st-admin-page-actions");
    const chooseRelief = button(ship.reliefAssetVersionId ? "Change 3D bundle" : "Choose 3D bundle", () => {
      openAdminMediaAssetPicker({
        title: `Choose 3D relief bundle for ${ship.name}`,
        message: "Only compatible immutable Space Typing relief bundles are shown.",
        allowedKinds: ["model"],
        selectedAssetVersionId: ship.reliefAssetVersionId ?? null,
        returnFocus: chooseRelief,
        isVersionCompatible: isSpaceTypingReliefMediaVersionCompatible,
        incompatibleEmptyMessage: "A relief bundle needs model, color, emissive and height components with immutable hashes.",
        onSelect: ({ version }) => {
          overrideFor(selectedId).reliefAssetVersionId = version.assetVersionId;
          previewSurface = "relief";
          renderList();
          renderStudioSettings();
          syncPreview();
          setStatus(`${selectedId} now uses exact 3D relief bundle ${version.assetVersionId}. Save Draft to persist this assignment.`, "good");
        },
      });
    });
    reliefActions.append(chooseRelief, button("Preview 3D", () => {
      previewSurface = "relief";
      syncPreview();
    }));
    if (ship.reliefAssetVersionId !== undefined) {
      reliefActions.append(button("Use bundled default", () => {
        const override = policy.ships?.[selectedId];
        if (override !== undefined) {
          delete override.reliefAssetVersionId;
          pruneEmptyOverride(selectedId);
        }
        previewSurface = "relief";
        renderList();
        renderStudioSettings();
        syncPreview();
        setStatus(`${selectedId} 3D relief override cleared. The bundled production hull is restored for this Draft.`, "good");
      }));
    }
    studio.basicHost.append(createAdminFieldShell(helpScope, {
      label: "3D Relief Bundle",
      control: reliefActions,
      help: {
        title: "3D Relief Bundle",
        content: "Choose one exact Media V2 relief bundle. Uploading Media does not change gameplay until the Ship draft is published.",
      },
      stateMessage: ship.reliefAssetVersionId === undefined
        ? "Bundled production hull"
        : `Exact version · ${ship.reliefAssetVersionId}`,
      stateTone: ship.reliefAssetVersionId === undefined ? "info" : "good",
    }));

    const effectiveProjectile = projectileArchetypeFor(ship);
    const baselineProjectile = projectileArchetypeFor(baseline);
    if (effectiveProjectile !== undefined && baselineProjectile !== undefined) {
      const projectile = el("select", "st-admin-select") as HTMLSelectElement;
      for (const recipe of PROJECTILE_ARCHETYPES) projectile.append(new Option(recipe, recipe));
      projectile.value = effectiveProjectile;
      projectile.addEventListener("change", () => {
        const next = projectile.value as ProjectileArchetype;
        const override = overrideFor(selectedId);
        if (next === baselineProjectile) {
          delete override.projectileArchetype;
          pruneEmptyOverride(selectedId);
        } else {
          override.projectileArchetype = next;
        }
        renderList();
        renderStudioSettings();
        syncPreview();
        setStatus(`${selectedId} projectile recipe set to ${next}. Fire preview uses the production PlayerShotSystem; Save Draft to persist this binding.`, "good");
      });
      studio.basicHost.append(createAdminFieldShell(helpScope, {
        label: "Projectile Recipe",
        control: projectile,
        help: {
          title: "Projectile Recipe",
          content: "Binds this Ship to one existing production projectile recipe. Muzzle, trail, sprite and motion remain recipe-owned.",
        },
        stateMessage: effectiveProjectile === baselineProjectile
          ? `Bundled production recipe · ${effectiveProjectile}`
          : `Draft override · ${effectiveProjectile} · applies on a new session`,
        stateTone: effectiveProjectile === baselineProjectile ? "info" : "good",
      }));
    } else {
      studio.basicHost.append(createAssetTuningCapabilityState({
        label: "Projectile recipe binding",
        status: "REQUIRES CANONICAL MIGRATION",
        description: "The canonical child preview did not expose a production projectile recipe for this Ship.",
      }));
    }

    const silhouette = el("select", "st-admin-select") as HTMLSelectElement;
    for (const option of SILHOUETTES) silhouette.append(new Option(option, option));
    silhouette.value = ship.visual.silhouette;
    silhouette.addEventListener("change", () => {
      const override = overrideFor(selectedId);
      override.visual ??= {};
      override.visual.silhouette = silhouette.value as ShipVisualProfile["silhouette"];
      syncPreview();
    });
    studio.basicHost.append(createAdminFieldShell(helpScope, {
      label: "Silhouette",
      control: silhouette,
    }));

    for (const key of BASIC_COLOR_KEYS) studio.basicHost.append(createVisualColorField(key, ship));

    studio.basicHost.append(
      createAssetTuningScalarControl(helpScope, {
        label: "Wing Span",
        value: ship.visual.wingSpan,
        defaultValue: baseline.visual.wingSpan,
        min: 0.5,
        max: 2,
        step: 0.01,
        stateMessage: "Production-backed Ship visual field · applies on a new session",
        onChange: (value) => {
          const override = overrideFor(selectedId);
          override.visual ??= {};
          override.visual.wingSpan = value;
          syncPreview();
        },
      }),
      createAssetTuningScalarControl(helpScope, {
        label: "Body Length",
        value: ship.visual.bodyLength,
        defaultValue: baseline.visual.bodyLength,
        min: 0.5,
        max: 2,
        step: 0.01,
        stateMessage: "Production-backed Ship visual field · applies on a new session",
        onChange: (value) => {
          const override = overrideFor(selectedId);
          override.visual ??= {};
          override.visual.bodyLength = value;
          syncPreview();
        },
      }),
    );

    const engines = el("select", "st-admin-select") as HTMLSelectElement;
    for (const count of [1, 2, 3] as const) engines.append(new Option(String(count), String(count)));
    engines.value = String(ship.visual.engineCount);
    engines.addEventListener("change", () => {
      const override = overrideFor(selectedId);
      override.visual ??= {};
      override.visual.engineCount = Number(engines.value) as 1 | 2 | 3;
      syncPreview();
    });
    studio.basicHost.append(createAdminFieldShell(helpScope, {
      label: "Engine Count",
      control: engines,
    }));

    for (const key of ADVANCED_COLOR_KEYS) studio.advancedHost.append(createVisualColorField(key, ship));

    const capabilityTitle = el("strong", undefined, "Capability boundaries");
    studio.advancedHost.append(
      capabilityTitle,
      createAssetTuningCapabilityState({
        label: "Per-Ship 2D Media assignment",
        status: "AVAILABLE",
        description: "Basic stores one exact immutable Media V2 image version.",
      }),
      createAssetTuningCapabilityState({
        label: "Per-Ship 3D relief bundle assignment",
        status: "AVAILABLE",
        description: "Basic stores one exact immutable compatible Media V2 relief bundle and previews it through production Ship3D.",
      }),
      createAssetTuningCapabilityState({
        label: "3D anchors / material / lighting",
        status: "READ-ONLY REFERENCE",
        description: "Model anchors and production renderer material/lighting remain owned by the relief bundle and runtime.",
      }),
      createAssetTuningCapabilityState({
        label: "Projectile recipe binding",
        status: "AVAILABLE",
        description: "Basic binds a Ship to one existing production PlayerShot recipe. Fire preview executes the same child PlayerShotSystem path.",
      }),
      createAssetTuningCapabilityState({
        label: "Projectile muzzle / trail / sprite internals",
        status: "READ-ONLY REFERENCE",
        description: "These are owned by the selected production recipe and are not independent writable Admin fields.",
      }),
      createAssetTuningCapabilityState({
        label: "Projectile launch / impact SFX",
        status: "REQUIRES CANONICAL MIGRATION",
        description: "Production audio identities exist, but persisted bindings plus a production-backed Admin audio scenario do not yet form a complete authoring chain.",
      }),
      createAssetTuningCapabilityState({
        label: "Persistent 3D scale / orientation / pivot",
        status: "REQUIRES CANONICAL MIGRATION",
        description: "Those values are still runtime-owned and have no canonical persisted Ship field.",
      }),
      createAssetTuningCapabilityState({
        label: "Semantic 3D animation clips",
        status: "DEFERRED / UNSUPPORTED",
        description: "Idle, attack, cast, recoil/recover, wing, cloth and hand/weapon clip bindings are not canonical runtime fields.",
      }),
      createAssetTuningCapabilityState({
        label: "Current VFX / SFX",
        status: "READ-ONLY REFERENCE",
        description: "Production effects and semantic/sample audio remain owned by their current runtime systems.",
      }),
      createAssetTuningCapabilityState({
        label: "Miss presentation / Weapon Admin entity",
        status: "DEFERRED / UNSUPPORTED",
        description: "Normal Ship projectiles have no canonical per-Ship miss presentation, and production has no first-class writable Weapon domain.",
      }),
      createAssetTuningCapabilityState({
        label: "Arbitrary / animated GLB",
        status: "DEFERRED / UNSUPPORTED",
        description: "Production relief uses its typed bundle; no canonical arbitrary GLB/GLTF loader exists.",
      }),
    );
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const ship = effectiveShip(selectedId);
    if (!serviceReady || !ship) {
      editorHost.append(notice(serviceReady ? "No ship is available for editing." : "Load the active revision and canonical ship preview before editing overrides.", serviceReady ? "warn" : "info"));
      return;
    }

    const identity = el("div", "stx-notice info", `ID ${ship.id} · asset ${ship.assetId} · apply boundary: new session`);
    editorHost.append(identity);

    const metadata = panel("Identity & Discovery", "`unlockStage` updates discovery/progression metadata only; it does not prevent selecting the ship.");
    const metaFields: HTMLElement[] = [];
    for (const [key, label] of TEXT_FIELDS) {
      const item = field(label, String(ship[key]));
      bindText(item.control, key);
      metaFields.push(item.root);
    }
    const unlock = field("Unlock / Discovery Stage", String(ship.unlockStage), undefined, "number");
    (unlock.control as HTMLInputElement).min = "1";
    (unlock.control as HTMLInputElement).max = "1000";
    unlock.control.addEventListener("input", () => {
      overrideFor(selectedId).unlockStage = Number(unlock.control.value);
      renderList();
    });
    metadata.append(grid(metaFields[0], unlock.root, metaFields[1]), grid(metaFields[2], metaFields[3], metaFields[4]), metaFields[5]);

    const stats = panel("Combat Stat Bonuses", "Child `characterStatBonus()` keys · allowed range -100..100");
    const statFields: HTMLElement[] = [];
    for (const key of CORE_STATS) {
      const item = field(key, String(ship.statBonus[key] ?? 0), undefined, "number");
      const input = item.control as HTMLInputElement;
      input.min = "-100";
      input.max = "100";
      input.step = "0.1";
      input.addEventListener("input", () => {
        const override = overrideFor(selectedId);
        override.statBonus ??= {};
        override.statBonus[key] = Number(input.value);
      });
      statFields.push(item.root);
    }
    for (let index = 0; index < statFields.length; index += 3) stats.append(grid(...statFields.slice(index, index + 3)));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Ship Override", () => {
        if (policy.ships) delete policy.ships[selectedId];
        renderList();
        renderEditor();
        renderStudioSettings();
        syncPreview();
        setStatus(`${selectedId} reset to bundled child runtime values. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Draft", () => {
        setStatus("Validating current Draft ship overrides against the canonical child policy…", "info");
        void api.previewShips({ policy }).then((validatedDraft) => {
          renderList();
          renderEditor();
          renderStudioSettings();
          syncPreview();
          setStatus(`Child canonical policy accepted Draft ${validatedDraft.configRevision} with ${validatedDraft.ships.length} ships. Published preview remains the active revision.`, "good");
        }).catch((error: unknown) => setStatus(adminErrorMessage(error, "The Draft ship policy could not be validated. Check the local Admin runtime and try again."), "bad"));
      }, "st-admin-btn primary"),
    );
    editorHost.append(metadata, stats, actions);
  };

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Load the active revision before saving a ship draft");
  const save = button("Save Draft", () => {
    void (async () => {
      if (!serviceReady) return;
      save.disabled = true;
      saveStatus.textContent = "Validating against child runtime…";
      try {
        const payload = await api.getState();
        if (loadedActiveRevision === null || loadedActiveRevision !== payload.state.activeRevision) {
          throw new Error(`Active revision changed from ${loadedActiveRevision ?? "not-loaded"} to ${payload.state.activeRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
        }
        await api.previewShips({ policy });
        const config = cloneConfig(payload.active.config);
        config.content = { ...(config.content ?? {}), ships: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin A5 · Ship asset tuning draft",
        });
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child policy + server validation. Published preview still reflects active ${loadedActiveRevision}; publish from History to change runtime policy. Gameplay apply boundary is a new session.`, "good");
      } catch (error: unknown) {
        const message = adminErrorMessage(error, "The Ships draft could not be saved. Check the local Admin runtime and try again.");
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = !serviceReady;
      }
    })();
  }, "st-admin-btn primary");
  save.disabled = true;
  saveBar.append(el("strong", undefined, "Ships Draft"), saveStatus, el("div", "grow"), button("Discard", () => navigate(location.pathname)), save);
  studio.lifecycleHost.append(saveBar);

  const load = (): void => {
    const generation = ++loadGeneration;
    ++previewGeneration;
    serviceReady = false;
    loadedActiveRevision = null;
    bundled = null;
    publishedPreview = null;
    previewSurface = "2d";
    revisionBadge.className = "st-admin-status info";
    revisionBadge.textContent = "ACTIVE · loading";
    setStatus("Loading active revision and canonical child ship registry…", "info");
    setPreviewStatus("Waiting for active revision and canonical ship registry…", "info");
    saveStatus.textContent = "Load the active revision before saving a ship draft";
    save.disabled = true;
    renderList();
    renderEditor();
    renderStudioSettings();

    void Promise.all([api.getState(), api.previewShips()]).then(async ([statePayload, bundledPreview]) => {
      const nextPolicy = policyFrom(statePayload.active.config);
      const nextPublishedPreview = await api.previewShips({ policy: nextPolicy });
      if (generation !== loadGeneration) return;
      loadedActiveRevision = statePayload.state.activeRevision;
      bundled = bundledPreview;
      policy = nextPolicy;
      publishedPreview = nextPublishedPreview;
      serviceReady = true;
      selectedId = publishedPreview.ships[0]?.id ?? "vanguard";
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
      saveStatus.textContent = "Revision-backed · no direct runtime mutation";
      save.disabled = false;
      renderList();
      renderEditor();
      renderStudioSettings();
      syncPreview();
      setStatus(
        statePayload.active.config.content?.ships
          ? `Loaded active Ships policy ${policy.configRevision}. Draft is isolated until History / Publish; Published preview is pinned to active ${statePayload.state.activeRevision}.`
          : "Active revision predates B06.1 Ships policy; bundled child registry is shown until the first draft is saved.",
        statePayload.active.config.content?.ships ? "good" : "warn",
      );
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      ++previewGeneration;
      serviceReady = false;
      loadedActiveRevision = null;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      save.disabled = true;
      setPreviewStatus("Preview is disabled until the canonical fleet is available.", "bad");
      studio.basicHost.replaceChildren(notice("Presentation tuning is disabled until the canonical fleet is available.", "bad"));
      studio.advancedHost.replaceChildren(notice("Capability state is unavailable until the canonical fleet loads.", "warn"));
      listHost.replaceChildren(notice("The canonical fleet could not be loaded. Retry after the local Admin service is available.", "bad"));
      editorHost.replaceChildren(notice("Ship overrides are disabled until the active revision and canonical preview are loaded.", "warn"));
      status.className = "stx-notice bad";
      status.replaceChildren(document.createTextNode(adminErrorMessage(error, "The Ships Admin service is unavailable. Check the local runtime and try again.")), document.createTextNode(" "), button("Retry", load));
    });
  };

  const lifecycleObserver = new MutationObserver(() => {
    if (page.isConnected) return;
    lifecycleObserver.disconnect();
    ++previewGeneration;
    previewBridge?.disposeImmediately();
    previewBridge = null;
    previewBridgePromise = null;
  });
  queueMicrotask(() => {
    if (page.isConnected) {
      lifecycleObserver.observe(document.body, { childList: true, subtree: true });
    } else {
      previewBridge?.disposeImmediately();
      previewBridge = null;
      previewBridgePromise = null;
    }
  });

  helpScope.observeRoot(page);
  refreshPreviewControls();
  load();
  return page;
}