from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"guard failed for {path}: target not found")
    path.write_text(text.replace(old, new, 1))


# 1) Harden server-side config validation.
store = ROOT / "admin/store.mjs"
replace_once(
    store,
    'export class AdminConflictError extends Error {}\nexport class AdminValidationError extends Error {}\n',
    '''export class AdminConflictError extends Error {}\nexport class AdminValidationError extends Error {}\n\nconst AUDIO_VOLUME_KEYS = ["master", "pronunciation", "music", "ambient", "sfx", "announcer"];\nconst WORLD_ID_PATTERN = /^world-(0[1-9]|[1-4][0-9]|50)$/;\nconst PLAYLIST_SELECTION_MODES = new Set(["shuffle-bag", "ordered"]);\n\nfunction isObject(value) {\n  return value !== null && typeof value === "object" && !Array.isArray(value);\n}\n\nfunction validateAssignment(value, label) {\n  if (value === undefined) return;\n  if (!isObject(value)) throw new AdminValidationError(`${label} must be an object.`);\n  if (value.kind === "inherit") return;\n  if (value.kind !== "replace") {\n    throw new AdminValidationError(`${label}.kind must be inherit or replace.`);\n  }\n  if (!Array.isArray(value.trackIds) || value.trackIds.length === 0) {\n    throw new AdminValidationError(`${label}.trackIds must contain at least one track id.`);\n  }\n  if (value.trackIds.some((id) => typeof id !== "string" || id.trim().length === 0)) {\n    throw new AdminValidationError(`${label}.trackIds must contain non-empty strings.`);\n  }\n  if (new Set(value.trackIds).size !== value.trackIds.length) {\n    throw new AdminValidationError(`${label}.trackIds must not contain duplicates.`);\n  }\n  if (value.selectionMode !== undefined && !PLAYLIST_SELECTION_MODES.has(value.selectionMode)) {\n    throw new AdminValidationError(`${label}.selectionMode must be shuffle-bag or ordered.`);\n  }\n}\n\nfunction validatePolicyEntry(entry, label) {\n  if (!isObject(entry)) throw new AdminValidationError(`${label} must be an object.`);\n  validateAssignment(entry.normal, `${label}.normal`);\n  if (entry.boss !== undefined) {\n    if (!isObject(entry.boss)) throw new AdminValidationError(`${label}.boss must be an object.`);\n    validateAssignment(entry.boss.common, `${label}.boss.common`);\n    validateAssignment(entry.boss.mini, `${label}.boss.mini`);\n    validateAssignment(entry.boss.world, `${label}.boss.world`);\n    validateAssignment(entry.boss.major, `${label}.boss.major`);\n  }\n}\n\nfunction validateWorldMusicPolicy(policy) {\n  if (!isObject(policy)) throw new AdminValidationError("worldMusic.publishedPolicy must be an object.");\n  if (typeof policy.configRevision !== "string" || policy.configRevision.trim().length === 0) {\n    throw new AdminValidationError("worldMusic.publishedPolicy.configRevision is required.");\n  }\n  if (policy.disabledTrackIds !== undefined) {\n    if (!Array.isArray(policy.disabledTrackIds) || policy.disabledTrackIds.some((id) => typeof id !== "string" || id.trim().length === 0)) {\n      throw new AdminValidationError("worldMusic.publishedPolicy.disabledTrackIds must contain non-empty strings.");\n    }\n    if (new Set(policy.disabledTrackIds).size !== policy.disabledTrackIds.length) {\n      throw new AdminValidationError("worldMusic.publishedPolicy.disabledTrackIds must not contain duplicates.");\n    }\n  }\n  if (policy.worlds !== undefined) {\n    if (!isObject(policy.worlds)) throw new AdminValidationError("worldMusic.publishedPolicy.worlds must be an object.");\n    for (const [worldId, entry] of Object.entries(policy.worlds)) {\n      if (!WORLD_ID_PATTERN.test(worldId)) {\n        throw new AdminValidationError(`Unknown World id in published policy: ${worldId}.`);\n      }\n      validatePolicyEntry(entry, `worldMusic.publishedPolicy.worlds.${worldId}`);\n    }\n  }\n  if (policy.global !== undefined) validatePolicyEntry(policy.global, "worldMusic.publishedPolicy.global");\n}\n''',
)
replace_once(
    store,
    '''    if (config.audio === null || typeof config.audio !== "object") {\n      throw new AdminValidationError("audio config is required.");\n    }\n    if (config.worldMusic === null || typeof config.worldMusic !== "object") {\n      throw new AdminValidationError("worldMusic config is required.");\n    }\n    return config;\n''',
    '''    if (!isObject(config.audio)) {\n      throw new AdminValidationError("audio config is required.");\n    }\n    if (typeof config.audio.profileId !== "string" || config.audio.profileId.trim().length === 0) {\n      throw new AdminValidationError("audio.profileId is required.");\n    }\n    if (!isObject(config.audio.defaults)) {\n      throw new AdminValidationError("audio.defaults is required.");\n    }\n    for (const key of AUDIO_VOLUME_KEYS) {\n      const value = config.audio.defaults[key];\n      if (typeof value !== "number" || !Number.isFinite(value) || value < 0 || value > 1) {\n        throw new AdminValidationError(`audio.defaults.${key} must be between 0 and 1.`);\n      }\n    }\n    if (!isObject(config.worldMusic)) {\n      throw new AdminValidationError("worldMusic config is required.");\n    }\n    if (typeof config.worldMusic.policyRevision !== "string" || config.worldMusic.policyRevision.trim().length === 0) {\n      throw new AdminValidationError("worldMusic.policyRevision is required.");\n    }\n    if (config.worldMusic.assignments !== undefined && !isObject(config.worldMusic.assignments)) {\n      throw new AdminValidationError("worldMusic.assignments must be an object when present.");\n    }\n    if (config.worldMusic.publishedPolicy !== undefined) {\n      validateWorldMusicPolicy(config.worldMusic.publishedPolicy);\n      if (config.worldMusic.policyRevision !== config.worldMusic.publishedPolicy.configRevision) {\n        throw new AdminValidationError("worldMusic.policyRevision must match publishedPolicy.configRevision.");\n      }\n    }\n    return config;\n''',
)

# 2) Regression tests for validation.
test_path = ROOT / "admin/store.test.mjs"
test_text = test_path.read_text()
marker = 'test("rejects invalid audio and World Music policy drafts"'
if marker not in test_text:
    test_text += '''\n\ntest("rejects invalid audio and World Music policy drafts", async (t) => {\n  const { store, rootDir } = await fixture();\n  t.after(() => rm(rootDir, { recursive: true, force: true }));\n  const active = await store.getActiveRevision();\n\n  const badAudio = structuredClone(active.config);\n  badAudio.audio.defaults.music = 1.5;\n  await assert.rejects(\n    store.createRevision({ baseRevision: active.revision, config: badAudio }),\n    AdminValidationError,\n  );\n\n  const badPolicy = structuredClone(active.config);\n  badPolicy.worldMusic.policyRevision = "admin-bad-v1";\n  badPolicy.worldMusic.publishedPolicy = {\n    configRevision: "admin-bad-v1",\n    worlds: {\n      "world-01": { normal: { kind: "replace", trackIds: [] } },\n    },\n  };\n  await assert.rejects(\n    store.createRevision({ baseRevision: active.revision, config: badPolicy }),\n    AdminValidationError,\n  );\n});\n\ntest("accepts a canonical published World Music policy as an isolated draft", async (t) => {\n  const { store, rootDir } = await fixture();\n  t.after(() => rm(rootDir, { recursive: true, force: true }));\n  const active = await store.getActiveRevision();\n  const config = structuredClone(active.config);\n  config.worldMusic.policyRevision = "admin-world-music-v1";\n  config.worldMusic.publishedPolicy = {\n    configRevision: "admin-world-music-v1",\n    worlds: {\n      "world-01": {\n        normal: {\n          kind: "replace",\n          trackIds: ["signal-in-the-void"],\n          selectionMode: "ordered",\n        },\n      },\n    },\n  };\n  const draft = await store.createRevision({\n    baseRevision: active.revision,\n    config,\n    message: "World Music policy draft",\n  });\n  assert.equal(draft.config.worldMusic.publishedPolicy.configRevision, "admin-world-music-v1");\n  assert.equal((await store.getRuntimeConfig()).worldMusic.publishedPolicy, undefined);\n});\n'''
    test_path.write_text(test_text)

# 3) Run canonical preview before writing a World Music revision.
server = ROOT / "admin/server.mjs"
replace_once(
    server,
    '''    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {\n      const input = await body(request);\n      const revision = await store.createRevision(input);\n      json(response, 201, revision);\n      return;\n    }\n''',
    '''    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {\n      const input = await body(request);\n      store.validateConfig(input.config);\n      const publishedPolicy = input.config?.worldMusic?.publishedPolicy;\n      if (publishedPolicy !== undefined) {\n        await runWorldMusicPreview({\n          rootDir: root,\n          contract,\n          publishedPolicy,\n          musicMode: "map",\n        });\n      }\n      const revision = await store.createRevision(input);\n      json(response, 201, revision);\n      return;\n    }\n''',
)

# 4) Type the canonical policy in the Portal API.
api = ROOT / "portal/src/admin/api.ts"
replace_once(
    api,
    '''export type SpaceTypingAdminConfig = {\n  contractRevision: string;\n  configSchemaVersion: number;\n  worldMusicCatalogSchemaVersion: number;\n  audio: {\n    profileId: string;\n    defaults: AudioDefaults;\n  };\n  worldMusic: {\n    policyRevision: string;\n    assignments: Record<string, unknown>;\n  };\n};\n''',
    '''export type PlaylistSelectionMode = "shuffle-bag" | "ordered";\n\nexport type PlaylistAssignment =\n  | { kind: "inherit" }\n  | { kind: "replace"; trackIds: string[]; selectionMode?: PlaylistSelectionMode };\n\nexport type WorldMusicPolicyEntry = {\n  normal?: PlaylistAssignment;\n  boss?: {\n    common?: PlaylistAssignment;\n    mini?: PlaylistAssignment;\n    world?: PlaylistAssignment;\n    major?: PlaylistAssignment;\n  };\n};\n\nexport type WorldMusicPolicy = {\n  configRevision: string;\n  disabledTrackIds?: string[];\n  worlds?: Record<string, WorldMusicPolicyEntry>;\n  global?: WorldMusicPolicyEntry;\n};\n\nexport type SpaceTypingAdminConfig = {\n  contractRevision: string;\n  configSchemaVersion: number;\n  worldMusicCatalogSchemaVersion: number;\n  audio: {\n    profileId: string;\n    defaults: AudioDefaults;\n  };\n  worldMusic: {\n    policyRevision: string;\n    assignments?: Record<string, unknown>;\n    publishedPolicy?: WorldMusicPolicy;\n  };\n};\n''',
)
replace_once(
    api,
    '''  previewWorldMusic(input: {\n    publishedPolicy?: unknown;\n    musicMode?: "map" | "random";\n  } = {}): Promise<WorldMusicPreview> {\n''',
    '''  previewWorldMusic(input: {\n    publishedPolicy?: WorldMusicPolicy;\n    musicMode?: "map" | "random";\n  } = {}): Promise<WorldMusicPreview> {\n''',
)

# 5) Add a dedicated structured World Music editor module.
editor = ROOT / "portal/src/admin/world-music-editor.ts"
editor.write_text(r'''import {
  SpaceTypingAdminApi,
  type AdminStatePayload,
  type PlaylistAssignment,
  type PlaylistSelectionMode,
  type SpaceTypingAdminConfig,
  type WorldMusicPolicy,
  type WorldMusicPolicyEntry,
  type WorldMusicPreview,
} from "./api";

type AssignmentSlot = "normal" | "boss-common" | "mini" | "world" | "major";
type PreviewStateName = "normal" | "mini" | "world" | "major";

const SLOTS: readonly AssignmentSlot[] = ["normal", "boss-common", "mini", "world", "major"];
const STYLE_ID = "space-typing-world-music-editor-v1";

function ensureStyles(): void {
  if (document.getElementById(STYLE_ID) !== null) return;
  const style = document.createElement("style");
  style.id = STYLE_ID;
  style.textContent = `
    .st-wm-editor{margin:16px 0;padding:16px;border:1px solid rgba(93,217,255,.18);border-radius:14px;background:rgba(6,21,35,.72)}
    .st-wm-editor-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.st-wm-field{display:grid;gap:6px}.st-wm-field.full{grid-column:1/-1}.st-wm-field label{font-size:12px;font-weight:800;color:#abd9ec}.st-wm-field input,.st-wm-field select,.st-wm-field textarea{box-sizing:border-box;width:100%;border:1px solid rgba(117,210,255,.2);border-radius:9px;background:#07111d;color:#dff7ff;padding:9px 10px}.st-wm-field textarea{min-height:72px;resize:vertical;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}.st-wm-raw{margin-top:14px}.st-wm-raw summary{cursor:pointer;color:#9de9ff;font-weight:700}.st-wm-raw textarea{width:100%;min-height:210px;margin-top:10px;box-sizing:border-box;background:#050b13;color:#caeefe;border:1px solid rgba(117,210,255,.18);border-radius:10px;padding:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}.st-wm-preview{margin-top:18px}.st-wm-warning{color:#ffd18a}@media(max-width:900px){.st-wm-editor-grid{grid-template-columns:1fr}}
  `;
  document.head.append(style);
}

function button(label: string, onClick: () => void, className = "st-admin-action"): HTMLButtonElement {
  const element = document.createElement("button");
  element.type = "button";
  element.className = className;
  element.textContent = label;
  element.addEventListener("click", onClick);
  return element;
}

function field(labelText: string, control: HTMLElement, full = false): HTMLElement {
  const wrapper = document.createElement("div");
  wrapper.className = `st-wm-field${full ? " full" : ""}`;
  const label = document.createElement("label");
  label.textContent = labelText;
  wrapper.append(label, control);
  return wrapper;
}

function select(values: readonly string[]): HTMLSelectElement {
  const element = document.createElement("select");
  for (const value of values) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    element.append(option);
  }
  return element;
}

function stateForSlot(slot: AssignmentSlot): PreviewStateName {
  if (slot === "normal") return "normal";
  if (slot === "mini") return "mini";
  if (slot === "major") return "major";
  return "world";
}

function getAssignment(policy: WorldMusicPolicy, worldId: string, slot: AssignmentSlot): PlaylistAssignment | undefined {
  const entry = policy.worlds?.[worldId];
  if (slot === "normal") return entry?.normal;
  if (slot === "boss-common") return entry?.boss?.common;
  return entry?.boss?.[slot];
}

function setAssignment(policy: WorldMusicPolicy, worldId: string, slot: AssignmentSlot, assignment: PlaylistAssignment): void {
  policy.worlds ??= {};
  const entry: WorldMusicPolicyEntry = policy.worlds[worldId] ?? {};
  policy.worlds[worldId] = entry;
  if (slot === "normal") {
    entry.normal = assignment;
    return;
  }
  entry.boss ??= {};
  if (slot === "boss-common") entry.boss.common = assignment;
  else entry.boss[slot] = assignment;
}

function parseTrackIds(value: string): string[] {
  return [...new Set(value.split(/[\s,]+/).map((item) => item.trim()).filter(Boolean))];
}

function createDraftPolicy(state: AdminStatePayload, preview: WorldMusicPreview): WorldMusicPolicy {
  const existing = state.active.config.worldMusic.publishedPolicy;
  if (existing !== undefined) return structuredClone(existing);
  return {
    configRevision: `admin-world-music-${state.state.generation + 1}`,
    worlds: {},
  };
}

function renderPreviewCards(preview: WorldMusicPreview): HTMLElement {
  const list = document.createElement("div");
  list.className = "st-galaxy-list st-wm-preview";
  const galaxies = [...new Set(preview.worlds.map((world) => world.galaxy))];
  for (const galaxy of galaxies) {
    const section = document.createElement("section");
    section.className = "st-galaxy";
    const title = document.createElement("h3");
    title.textContent = `Galaxy ${String(galaxy).padStart(2, "0")}`;
    const worlds = document.createElement("div");
    worlds.className = "st-world-grid";
    for (const world of preview.worlds.filter((item) => item.galaxy === galaxy)) {
      const card = document.createElement("div");
      card.className = "st-world";
      const strong = document.createElement("strong");
      strong.textContent = `${world.worldId} · ${world.name}`;
      const range = document.createElement("small");
      range.textContent = `Stages ${world.stageRange[0]}–${world.stageRange[1]} · normal ${world.states.normal.trackCount} · boss ${world.states.world.trackCount}`;
      const badges = document.createElement("div");
      badges.className = "st-world-badges";
      for (const badge of [...new Set([...world.states.normal.badges, ...world.states.world.badges])]) {
        const chip = document.createElement("span");
        chip.className = "st-badge";
        chip.textContent = badge;
        badges.append(chip);
      }
      const source = document.createElement("div");
      source.className = "st-world-source";
      source.textContent = `normal: ${world.states.normal.resolvedFrom} · boss: ${world.states.world.resolvedFrom}`;
      source.title = [...world.states.normal.fallbackTrace, ...world.states.world.fallbackTrace].join("\n");
      card.append(strong, range, badges, source);
      worlds.append(card);
    }
    section.append(title, worlds);
    list.append(section);
  }
  return list;
}

function hasSilenceFailSafe(preview: WorldMusicPreview): boolean {
  return preview.worlds.some((world) =>
    Object.values(world.states).some((state) => state.badges.includes("EMPTY / SILENCE FAIL-SAFE")),
  );
}

export function renderWorldMusicEditor(options: {
  panel: HTMLElement;
  state: AdminStatePayload;
  preview: WorldMusicPreview;
  api: SpaceTypingAdminApi;
  navigate: (path: string) => void;
  header: HTMLElement;
}): void {
  ensureStyles();
  const { panel, state, api, navigate, header } = options;
  let currentPreview = options.preview;
  let policy = createDraftPolicy(state, currentPreview);
  const config: SpaceTypingAdminConfig = structuredClone(state.active.config);

  panel.replaceChildren(header);
  const note = document.createElement("div");
  note.className = "st-admin-note";
  const updateNote = (): void => {
    note.textContent = `Preview ${currentPreview.configRevision} · manifest ${currentPreview.manifestRevision} · mode ${currentPreview.musicMode} · active revision ${state.state.activeRevision}`;
  };
  updateNote();
  panel.append(note);

  const editor = document.createElement("section");
  editor.className = "st-wm-editor";
  const grid = document.createElement("div");
  grid.className = "st-wm-editor-grid";

  const revisionInput = document.createElement("input");
  revisionInput.value = policy.configRevision;
  const modeInput = select(["map", "random"]);
  modeInput.value = currentPreview.musicMode;
  const worldInput = select(currentPreview.worlds.map((world) => world.worldId));
  const slotInput = select(SLOTS);
  const assignmentInput = select(["inherit", "replace"]);
  const selectionInput = select(["ordered", "shuffle-bag"]);
  const tracksInput = document.createElement("textarea");
  tracksInput.placeholder = "track-id-1, track-id-2";

  grid.append(
    field("Policy revision", revisionInput),
    field("Preview mode", modeInput),
    field("World", worldInput),
    field("Assignment slot", slotInput),
    field("Assignment", assignmentInput),
    field("Selection", selectionInput),
    field("Track IDs (comma / whitespace separated)", tracksInput, true),
  );
  editor.append(grid);

  const status = document.createElement("div");
  const raw = document.createElement("details");
  raw.className = "st-wm-raw";
  const rawSummary = document.createElement("summary");
  rawSummary.textContent = "Advanced canonical policy JSON";
  const rawText = document.createElement("textarea");
  raw.append(rawSummary, rawText);

  const syncRaw = (): void => {
    rawText.value = `${JSON.stringify(policy, null, 2)}\n`;
  };
  const loadControls = (): void => {
    revisionInput.value = policy.configRevision;
    const assignment = getAssignment(policy, worldInput.value, slotInput.value as AssignmentSlot) ?? { kind: "inherit" };
    assignmentInput.value = assignment.kind;
    if (assignment.kind === "replace") {
      tracksInput.value = assignment.trackIds.join(", ");
      selectionInput.value = assignment.selectionMode ?? "shuffle-bag";
    } else {
      tracksInput.value = "";
      selectionInput.value = "ordered";
    }
    tracksInput.disabled = assignmentInput.value === "inherit";
    selectionInput.disabled = assignmentInput.value === "inherit";
    syncRaw();
  };
  const applyControls = (): void => {
    const revision = revisionInput.value.trim();
    if (revision.length === 0) throw new Error("Policy revision is required.");
    policy.configRevision = revision;
    const slot = slotInput.value as AssignmentSlot;
    if (assignmentInput.value === "inherit") {
      setAssignment(policy, worldInput.value, slot, { kind: "inherit" });
    } else {
      const trackIds = parseTrackIds(tracksInput.value);
      if (trackIds.length === 0) throw new Error("Replace requires at least one track id.");
      setAssignment(policy, worldInput.value, slot, {
        kind: "replace",
        trackIds,
        selectionMode: selectionInput.value as PlaylistSelectionMode,
      });
    }
    syncRaw();
  };

  worldInput.addEventListener("change", loadControls);
  slotInput.addEventListener("change", loadControls);
  assignmentInput.addEventListener("change", () => {
    const inherit = assignmentInput.value === "inherit";
    tracksInput.disabled = inherit;
    selectionInput.disabled = inherit;
  });

  const actions = document.createElement("div");
  actions.className = "st-admin-actions";
  const apply = button("Apply assignment to draft", () => {
    try {
      applyControls();
      status.className = "st-admin-success";
      status.textContent = "Assignment applied to the in-memory draft. Runtime is unchanged.";
    } catch (error) {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid assignment.";
    }
  });
  const useResolved = button("Use resolved tracks", () => {
    const world = currentPreview.worlds.find((item) => item.worldId === worldInput.value);
    const stateName = stateForSlot(slotInput.value as AssignmentSlot);
    tracksInput.value = world?.states[stateName].trackIds.join(", ") ?? "";
    assignmentInput.value = "replace";
    tracksInput.disabled = false;
    selectionInput.disabled = false;
  });
  const previewButton = button("Preview draft", () => {
    previewButton.disabled = true;
    status.className = "st-admin-note";
    status.textContent = "Running canonical child resolver…";
    try {
      applyControls();
    } catch (error) {
      previewButton.disabled = false;
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid draft.";
      return;
    }
    void api.previewWorldMusic({
      publishedPolicy: policy,
      musicMode: modeInput.value as "map" | "random",
    }).then((next) => {
      currentPreview = next;
      updateNote();
      previewHost.replaceChildren(renderPreviewCards(currentPreview));
      status.className = hasSilenceFailSafe(next) ? "st-admin-error" : "st-admin-success";
      status.textContent = hasSilenceFailSafe(next)
        ? "Preview contains EMPTY / SILENCE FAIL-SAFE. Fix the draft before publishing."
        : "Canonical preview passed. Review badges/traces before saving the draft.";
    }).catch((error: unknown) => {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Preview failed.";
    }).finally(() => {
      previewButton.disabled = false;
    });
  }, "st-admin-action primary");
  const save = button("Save immutable draft", () => {
    save.disabled = true;
    status.className = "st-admin-note";
    status.textContent = "Validating draft through canonical resolver…";
    try {
      applyControls();
    } catch (error) {
      save.disabled = false;
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid draft.";
      return;
    }
    void api.previewWorldMusic({ publishedPolicy: policy, musicMode: "map" })
      .then((validated) => {
        if (hasSilenceFailSafe(validated)) {
          throw new Error("Draft contains EMPTY / SILENCE FAIL-SAFE and was not saved.");
        }
        config.worldMusic.policyRevision = policy.configRevision;
        config.worldMusic.assignments = {};
        config.worldMusic.publishedPolicy = structuredClone(policy);
        return api.createRevision({
          baseRevision: state.state.activeRevision,
          config,
          message: `Update World Music policy ${policy.configRevision}`,
        });
      })
      .then((revision) => {
        status.className = "st-admin-success";
        status.textContent = `Draft ${revision.revision} saved. Runtime stays on ${state.state.activeRevision} until Publish.`;
      })
      .catch((error: unknown) => {
        status.className = "st-admin-error";
        status.textContent = error instanceof Error ? error.message : "Could not save World Music draft.";
      })
      .finally(() => {
        save.disabled = false;
      });
  }, "st-admin-action primary");
  const loadRaw = button("Load advanced JSON into draft", () => {
    try {
      const parsed = JSON.parse(rawText.value) as WorldMusicPolicy;
      if (typeof parsed.configRevision !== "string" || parsed.configRevision.trim().length === 0) {
        throw new Error("Advanced policy JSON needs configRevision.");
      }
      policy = structuredClone(parsed);
      loadControls();
      status.className = "st-admin-success";
      status.textContent = "Advanced JSON loaded into the in-memory draft. Preview it before saving.";
    } catch (error) {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid policy JSON.";
    }
  });
  const reset = button("Reset Admin overrides", () => {
    policy = { configRevision: revisionInput.value.trim() || `admin-world-music-${state.state.generation + 1}`, worlds: {} };
    loadControls();
    status.className = "st-admin-note";
    status.textContent = "Admin overrides cleared in the draft. Generated/legacy fallback remains available after preview.";
  });
  actions.append(apply, useResolved, previewButton, save, button("History / Publish", () => navigate("/admin/space-typing/history")), reset);
  editor.append(actions, status, raw);
  panel.append(editor);

  const previewHost = document.createElement("div");
  previewHost.append(renderPreviewCards(currentPreview));
  panel.append(previewHost);
  loadControls();
  actions.append(loadRaw);
}
''')

# 6) Delegate World Music rendering to the structured editor without touching other Admin pages.
ui = ROOT / "portal/src/admin/space-typing.ts"
ui_text = ui.read_text()
import_line = 'import { renderWorldMusicEditor } from "./world-music-editor";\n'
if import_line not in ui_text:
    anchor = 'import contractJson from "./contracts/space-typing-admin.v1.json";\n'
    if anchor not in ui_text:
      raise SystemExit("guard failed: admin UI import anchor missing")
    ui_text = ui_text.replace(anchor, anchor + import_line, 1)
start = ui_text.find('  private renderWorldMusic(\n')
end = ui_text.find('\n  private renderHistory(', start)
if start < 0 or end < 0:
    raise SystemExit("guard failed: renderWorldMusic block missing")
replacement = '''  private renderWorldMusic(\n    panel: HTMLElement,\n    state: AdminStatePayload,\n    preview: WorldMusicPreview,\n  ): void {\n    renderWorldMusicEditor({\n      panel,\n      state,\n      preview,\n      api: this.api,\n      navigate: this.navigate,\n      header: this.renderHeader(\n        "World Music",\n        "Edit a canonical published policy, preview through the child resolver, then save an immutable draft.",\n      ),\n    });\n  }\n'''
ui.write_text(ui_text[:start] + replacement + ui_text[end:])
