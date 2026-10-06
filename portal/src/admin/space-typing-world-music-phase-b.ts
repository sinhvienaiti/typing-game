import "./space-typing-world-music-v2.css";
import {
  SpaceTypingAdminApi,
  type PlaylistAssignment,
  type PlaylistSelectionMode,
  type SpaceTypingAdminConfig,
  type WorldMusicPolicy,
  type WorldMusicPolicyEntry,
  type WorldMusicPreview,
  type WorldMusicPreviewState,
} from "./api";

const BASE = "/admin/space-typing";
const api = new SpaceTypingAdminApi();

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type Scope = "global" | "world";
type Slot = "normal" | "boss-common" | "mini" | "world" | "major";

type TrackOption = {
  id: string;
  title: string;
};

const SLOT_LABELS: Readonly<Record<Slot, string>> = {
  normal: "Normal",
  "boss-common": "Boss Common",
  mini: "Mini Boss",
  world: "World Boss",
  major: "Major Boss",
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function btn(label: string, fn: () => void = () => undefined, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", fn);
  return node;
}

function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
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

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `st-admin-info-banner ${tone}`, text);
}

function cloneConfig(config: SpaceTypingAdminConfig): SpaceTypingAdminConfig {
  return structuredClone(config);
}

function clonePolicy(policy: WorldMusicPolicy | undefined, activeRevision: string): WorldMusicPolicy {
  return structuredClone(policy ?? { configRevision: `admin-${activeRevision}`, worlds: {} });
}

function assertStableActiveRevision(loadedActiveRevision: string | null, currentActiveRevision: string): void {
  if (loadedActiveRevision === null) {
    throw new Error("Active revision has not finished loading. Reload this screen before saving.");
  }
  if (loadedActiveRevision !== currentActiveRevision) {
    throw new Error(`Active revision changed from ${loadedActiveRevision} to ${currentActiveRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
  }
}

function worldEntry(policy: WorldMusicPolicy, worldId: string, create = false): WorldMusicPolicyEntry | undefined {
  const current = policy.worlds?.[worldId];
  if (current !== undefined || !create) return current;
  policy.worlds ??= {};
  const entry: WorldMusicPolicyEntry = {};
  policy.worlds[worldId] = entry;
  return entry;
}

function rootEntry(policy: WorldMusicPolicy, scope: Scope, worldId: string, create = false): WorldMusicPolicyEntry | undefined {
  if (scope === "global") {
    if (policy.global !== undefined || !create) return policy.global;
    policy.global = {};
    return policy.global;
  }
  return worldEntry(policy, worldId, create);
}

function readAssignment(policy: WorldMusicPolicy, scope: Scope, worldId: string, slot: Slot): PlaylistAssignment | undefined {
  const root = rootEntry(policy, scope, worldId);
  if (root === undefined) return undefined;
  if (slot === "normal") return root.normal;
  if (slot === "boss-common") return root.boss?.common;
  return root.boss?.[slot];
}

function writeAssignment(policy: WorldMusicPolicy, scope: Scope, worldId: string, slot: Slot, assignment: PlaylistAssignment): void {
  const root = rootEntry(policy, scope, worldId, true)!;
  if (slot === "normal") {
    root.normal = assignment;
    return;
  }
  root.boss ??= {};
  if (slot === "boss-common") root.boss.common = assignment;
  else root.boss[slot] = assignment;
}

function selectedPreviewStates(slot: Slot): readonly WorldMusicPreviewState[] {
  if (slot === "boss-common") return ["mini", "world", "major"];
  if (slot === "normal") return ["normal"];
  return [slot];
}

function previewTracks(preview: WorldMusicPreview | null, policy: WorldMusicPolicy): TrackOption[] {
  const tracks = new Map<string, string>();
  if (preview !== null) {
    for (const world of preview.worlds) {
      for (const state of Object.values(world.states)) {
        for (const track of state.tracks) tracks.set(track.id, track.title);
      }
    }
  }
  const collect = (entry: WorldMusicPolicyEntry | undefined): void => {
    if (entry === undefined) return;
    const assignments = [entry.normal, entry.boss?.common, entry.boss?.mini, entry.boss?.world, entry.boss?.major];
    for (const assignment of assignments) {
      if (assignment?.kind !== "replace") continue;
      for (const id of assignment.trackIds) if (!tracks.has(id)) tracks.set(id, id);
    }
  };
  collect(policy.global);
  for (const entry of Object.values(policy.worlds ?? {})) collect(entry);
  return [...tracks.entries()].map(([id, title]) => ({ id, title })).sort((a, b) => a.title.localeCompare(b.title));
}

export function renderPhaseBWorldMusic(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Audio & Music · Canonical Policy · Phase B"),
    el("h1", undefined, "World / Stage Music"),
    el("p", undefined, "B04.1 wires the scopes the pinned child resolver really supports today: Global and World. Save Draft creates an immutable revision; Publish applies the policy on the next track/state boundary."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(revisionBadge, badge("GLOBAL + WORLD LIVE", "good"), badge("GALAXY / STAGE BLOCKED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const runtimeStatus = notice("Loading active World Music policy and canonical child preview…", "info");
  page.append(runtimeStatus);
  page.append(notice("Scope safety: the child WorldMusicPolicy v1 has no galaxy/stage keys. Galaxy and Stage authoring stay disabled until the child resolver, preview protocol and runtime consumer are extended together; Admin will not persist JSON that runtime silently ignores.", "warn"));

  let loadedActiveRevision: string | null = null;
  let draftPolicy: WorldMusicPolicy = { configRevision: "loading", worlds: {} };
  let preview: WorldMusicPreview | null = null;
  let scope: Scope = "world";
  let worldId = "world-01";
  let slot: Slot = "normal";

  const scopePanel = panel("Canonical Scope", "Only scopes represented by WorldMusicPolicy v1 can be saved");
  const scopeBody = el("div", "st-admin-panel-pad");
  const scopeSeg = el("div", "st-admin-seg");
  const globalButton = btn("Global");
  const worldButton = btn("World");
  const galaxyButton = btn("Galaxy · blocked");
  const stageButton = btn("Stage · blocked");
  galaxyButton.disabled = true;
  stageButton.disabled = true;
  galaxyButton.title = "Blocked until the child resolver consumes galaxy policy.";
  stageButton.title = "Blocked until the child resolver consumes stage policy.";
  scopeSeg.append(globalButton, worldButton, galaxyButton, stageButton);

  const worldSelect = el("select", "st-admin-select") as HTMLSelectElement;
  worldSelect.setAttribute("aria-label", "World Music World scope");
  for (let index = 1; index <= 50; index += 1) {
    const id = `world-${String(index).padStart(2, "0")}`;
    worldSelect.append(new Option(`World ${String(index).padStart(2, "0")}`, id));
  }
  scopeBody.append(scopeSeg, worldSelect);
  scopePanel.append(scopeBody);

  const editor = panel("Assignment Editor", "Canonical multi-file playlist · inherit or replace");
  const tabs = el("div", "st-admin-state-tabs");
  const slotButtons = new Map<Slot, HTMLButtonElement>();
  for (const value of Object.keys(SLOT_LABELS) as Slot[]) {
    const control = btn(SLOT_LABELS[value]);
    control.setAttribute("aria-pressed", "false");
    slotButtons.set(value, control);
    tabs.append(control);
  }
  editor.append(tabs);

  const assignmentHead = el("div", "stx-music-assignment-head");
  const assignmentSeg = el("div", "st-admin-seg");
  const inheritButton = btn("Inherit");
  const replaceButton = btn("Replace");
  assignmentSeg.append(inheritButton, replaceButton);
  const selectionMode = el("select", "st-admin-select") as HTMLSelectElement;
  selectionMode.setAttribute("aria-label", "Playlist selection strategy");
  selectionMode.append(new Option("Shuffle Bag", "shuffle-bag"), new Option("Ordered", "ordered"));
  assignmentHead.append(el("span", "st-admin-chip", "Assignment"), assignmentSeg, el("div", "grow"), selectionMode);
  editor.append(assignmentHead);
  const trackPicker = el("div", "stx-music-track-picker");
  editor.append(trackPicker);

  const effective = panel("Canonical Effective Preview", "Resolved by the same child code path used by runtime");
  const effectiveBody = el("div", "st-admin-panel-pad");
  effective.append(effectiveBody);

  const layout = el("div", "stx-world-music-v2");
  layout.append(scopePanel, editor, effective);
  page.append(layout);

  const updateScopeState = (): void => {
    globalButton.classList.toggle("active", scope === "global");
    worldButton.classList.toggle("active", scope === "world");
    globalButton.setAttribute("aria-pressed", String(scope === "global"));
    worldButton.setAttribute("aria-pressed", String(scope === "world"));
    worldSelect.disabled = scope === "global";
    inheritButton.disabled = scope === "global";
    inheritButton.title = scope === "global" ? "Global has no parent scope to inherit from." : "Use generated/global fallback.";
  };

  const renderEffective = (): void => {
    effectiveBody.replaceChildren();
    if (preview === null) {
      effectiveBody.append(notice("Preview not loaded yet.", "info"));
      return;
    }
    const world = preview.worlds.find((entry) => entry.worldId === worldId) ?? preview.worlds[0];
    if (world === undefined) {
      effectiveBody.append(notice("No world preview returned by child resolver.", "bad"));
      return;
    }
    effectiveBody.append(el("p", undefined, `${scope === "global" ? "Global policy representative preview" : world.name} · ${SLOT_LABELS[slot]}`));
    for (const stateName of selectedPreviewStates(slot)) {
      const statePreview = world.states[stateName];
      const row = el("div", "stx-effective-source");
      row.append(
        badge(stateName.toUpperCase(), statePreview.badges.includes("REPLACED") ? "good" : "info"),
        el("span", undefined, `${statePreview.resolvedFrom} · ${statePreview.selectionMode} · ${statePreview.trackCount} track(s)`),
      );
      effectiveBody.append(row);
      const list = el("div", "stx-effective-tracks");
      for (const [index, track] of statePreview.tracks.entries()) {
        const trackRow = el("div", "stx-effective-track");
        trackRow.append(el("span", "st-admin-track-num", String(index + 1)), el("div"));
        (trackRow.lastElementChild as HTMLElement).append(el("strong", undefined, track.title), el("small", undefined, track.id));
        list.append(trackRow);
      }
      if (statePreview.tracks.length === 0) list.append(notice("EMPTY / SILENCE FAIL-SAFE", "bad"));
      effectiveBody.append(list);
      const fallback = el("div", "stx-fallback");
      fallback.append(el("span", undefined, "Fallback chain"), el("code", undefined, statePreview.fallbackTrace.join(" → ")));
      effectiveBody.append(fallback);
    }
  };

  const syncEditor = (): void => {
    updateScopeState();
    for (const [value, control] of slotButtons) {
      control.classList.toggle("active", slot === value);
      control.setAttribute("aria-pressed", String(slot === value));
    }
    let assignment = readAssignment(draftPolicy, scope, worldId, slot);
    if (scope === "global" && assignment?.kind !== "replace") assignment = undefined;
    const kind = assignment?.kind ?? (scope === "global" ? "replace" : "inherit");
    inheritButton.classList.toggle("active", kind === "inherit");
    replaceButton.classList.toggle("active", kind === "replace");
    inheritButton.setAttribute("aria-pressed", String(kind === "inherit"));
    replaceButton.setAttribute("aria-pressed", String(kind === "replace"));
    selectionMode.disabled = kind !== "replace";
    selectionMode.value = assignment?.kind === "replace" ? assignment.selectionMode ?? "shuffle-bag" : "shuffle-bag";

    const selected = new Set(assignment?.kind === "replace" ? assignment.trackIds : []);
    const options = previewTracks(preview, draftPolicy);
    trackPicker.replaceChildren();
    if (options.length === 0) {
      trackPicker.append(notice("No canonical tracks are available from the preview yet.", "warn"));
    }
    for (const option of options) {
      const row = el("label", "stx-music-track");
      const input = el("input") as HTMLInputElement;
      input.type = "checkbox";
      input.checked = selected.has(option.id);
      input.disabled = kind !== "replace";
      const copy = el("span");
      copy.append(el("strong", undefined, option.title), el("small", undefined, option.id));
      input.addEventListener("change", () => {
        const current = readAssignment(draftPolicy, scope, worldId, slot);
        const ids = new Set(current?.kind === "replace" ? current.trackIds : []);
        if (input.checked) ids.add(option.id); else ids.delete(option.id);
        writeAssignment(draftPolicy, scope, worldId, slot, {
          kind: "replace",
          trackIds: [...ids],
          selectionMode: selectionMode.value as PlaylistSelectionMode,
        });
        syncEditor();
      });
      row.append(input, copy, badge(input.checked ? "SELECTED" : "AVAILABLE", input.checked ? "good" : "info"));
      trackPicker.append(row);
    }
    renderEffective();
  };

  const validateDraft = async (): Promise<void> => {
    runtimeStatus.className = "st-admin-info-banner info";
    runtimeStatus.textContent = "Validating draft through child canonical World Music resolver…";
    preview = await api.previewWorldMusic({ publishedPolicy: draftPolicy, musicMode: "map" });
    runtimeStatus.className = "st-admin-info-banner good";
    runtimeStatus.textContent = `Canonical preview OK · ${preview.configRevision} · ${preview.worlds.length} worlds · runtime unchanged`;
    syncEditor();
  };

  globalButton.addEventListener("click", () => { scope = "global"; syncEditor(); });
  worldButton.addEventListener("click", () => { scope = "world"; syncEditor(); });
  worldSelect.addEventListener("change", () => { worldId = worldSelect.value; syncEditor(); });
  for (const [value, control] of slotButtons) control.addEventListener("click", () => { slot = value; syncEditor(); });
  inheritButton.addEventListener("click", () => {
    if (scope === "global") return;
    writeAssignment(draftPolicy, scope, worldId, slot, { kind: "inherit" });
    syncEditor();
  });
  replaceButton.addEventListener("click", () => {
    const current = readAssignment(draftPolicy, scope, worldId, slot);
    writeAssignment(draftPolicy, scope, worldId, slot, {
      kind: "replace",
      trackIds: current?.kind === "replace" ? [...current.trackIds] : [],
      selectionMode: current?.kind === "replace" ? current.selectionMode ?? "shuffle-bag" : "shuffle-bag",
    });
    syncEditor();
  });
  selectionMode.addEventListener("change", () => {
    const current = readAssignment(draftPolicy, scope, worldId, slot);
    if (current?.kind !== "replace") return;
    writeAssignment(draftPolicy, scope, worldId, slot, { ...current, selectionMode: selectionMode.value as PlaylistSelectionMode });
  });

  const saveBar = el("div", "st-admin-sticky-save");
  const saveStatus = el("span", undefined, "Save Draft validates and stores Global/World policy only · Publish remains explicit");
  const validateButton = btn("Validate Draft", () => void validateDraft().catch((error: unknown) => {
    runtimeStatus.className = "st-admin-info-banner bad";
    runtimeStatus.textContent = `Preview rejected: ${error instanceof Error ? error.message : String(error)}`;
  }));
  const saveButton = btn("Save Draft", () => void (async () => {
    saveButton.disabled = true;
    saveStatus.textContent = "Validating canonical policy before immutable draft…";
    try {
      await validateDraft();
      const payload = await api.getState();
      assertStableActiveRevision(loadedActiveRevision, payload.state.activeRevision);
      const config = cloneConfig(payload.active.config);
      draftPolicy.configRevision = `admin-${payload.active.revision}-${Date.now().toString(36)}`;
      config.worldMusic = {
        ...config.worldMusic,
        policyRevision: "phase-b-world-music-v1",
        publishedPolicy: structuredClone(draftPolicy),
      };
      const revision = await api.createRevision({
        baseRevision: payload.active.revision,
        config,
        message: "Admin Phase B · World Music Global/World draft",
      });
      saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
      runtimeStatus.className = "st-admin-info-banner good";
      runtimeStatus.textContent = `World Music draft ${revision.revision} created. Publish is still required; active playback remains on ${payload.state.activeRevision}.`;
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : String(error);
      saveStatus.textContent = `Draft rejected · ${message}`;
      runtimeStatus.className = "st-admin-info-banner bad";
      runtimeStatus.textContent = `Validation/save failed: ${message}`;
    } finally {
      saveButton.disabled = false;
    }
  })(), "st-admin-btn primary");
  saveBar.append(el("strong", undefined, "B04.1 World Music Draft"), saveStatus, el("div", "grow"), btn("Discard", () => navigate(`${BASE}/world-music`)), validateButton, saveButton);
  page.append(saveBar);

  void api.getState().then(async (payload) => {
    loadedActiveRevision = payload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
    draftPolicy = clonePolicy(payload.active.config.worldMusic.publishedPolicy, payload.state.activeRevision);
    preview = await api.previewWorldMusic({ publishedPolicy: payload.active.config.worldMusic.publishedPolicy, musicMode: "map" });
    runtimeStatus.className = "st-admin-info-banner good";
    runtimeStatus.textContent = payload.active.config.worldMusic.publishedPolicy === undefined
      ? "Loaded generated/legacy World Music fallback. First B04.1 draft will add an additive publishedPolicy namespace."
      : `Loaded active published World Music policy · ${payload.active.config.worldMusic.publishedPolicy.configRevision}`;
    syncEditor();
  }).catch((error: unknown) => {
    runtimeStatus.className = "st-admin-info-banner bad";
    runtimeStatus.textContent = `Admin/preview service unavailable: ${error instanceof Error ? error.message : String(error)}`;
  });

  updateScopeState();
  syncEditor();
  return page;
}
