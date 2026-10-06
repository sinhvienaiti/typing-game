from pathlib import Path

def replace_once(path, old, new):
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match, found {count}: {old[:100]!r}")
    p.write_text(text.replace(old, new, 1))

def replace_all(path, old, new, expected_min=1):
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count < expected_min:
        raise SystemExit(f"{path}: expected at least {expected_min} matches, found {count}: {old[:100]!r}")
    p.write_text(text.replace(old, new))

# API contract mirrors the child B04.2 hierarchy and selected-stage preview input.
replace_once(
    "portal/src/admin/api.ts",
    '''  worlds?: Record<string, WorldMusicPolicyEntry>;
  global?: WorldMusicPolicyEntry;
};''',
    '''  stages?: Record<string, WorldMusicPolicyEntry>;
  worlds?: Record<string, WorldMusicPolicyEntry>;
  galaxies?: Record<string, WorldMusicPolicyEntry>;
  global?: WorldMusicPolicyEntry;
};''',
)
replace_once(
    "portal/src/admin/api.ts",
    '''    /** Additive B04.1 canonical policy. Child v1 currently supports Global + World only. */
    publishedPolicy?: WorldMusicPolicy;''',
    '''    /** Additive B04.2 canonical policy: Global + Galaxy + World + Stage. */
    publishedPolicy?: WorldMusicPolicy;''',
)
replace_once(
    "portal/src/admin/api.ts",
    '''  musicMode: "map" | "random";
  worlds: Array<{''',
    '''  musicMode: "map" | "random";
  stageNumber?: number;
  worlds: Array<{''',
)
replace_once(
    "portal/src/admin/api.ts",
    '''  previewWorldMusic(input: {
    publishedPolicy?: WorldMusicPolicy;
    musicMode?: "map" | "random";
  } = {}): Promise<WorldMusicPreview> {''',
    '''  previewWorldMusic(input: {
    publishedPolicy?: WorldMusicPolicy;
    musicMode?: "map" | "random";
    stageNumber?: number;
  } = {}): Promise<WorldMusicPreview> {''',
)

# Parent bridge validates and forwards selected Stage context to the child CLI.
replace_once(
    "admin/world-music-preview.mjs",
    '''  publishedPolicy,
  musicMode = "map",
  timeoutMs = 10000,''',
    '''  publishedPolicy,
  musicMode = "map",
  stageNumber,
  timeoutMs = 10000,''',
)
replace_once(
    "admin/world-music-preview.mjs",
    '''  if (musicMode !== "map" && musicMode !== "random") {
    throw new WorldMusicPreviewError("musicMode must be map or random.");
  }

  const childDir''',
    '''  if (musicMode !== "map" && musicMode !== "random") {
    throw new WorldMusicPreviewError("musicMode must be map or random.");
  }
  if (
    stageNumber !== undefined &&
    (!Number.isInteger(stageNumber) || stageNumber < 1 || stageNumber > 1000)
  ) {
    throw new WorldMusicPreviewError("stageNumber must be an integer from 1 to 1000.");
  }

  const childDir''',
)
replace_once(
    "admin/world-music-preview.mjs",
    '''      musicMode,
      ...(publishedPolicy === undefined ? {} : { publishedPolicy }),''',
    '''      musicMode,
      ...(stageNumber === undefined ? {} : { stageNumber }),
      ...(publishedPolicy === undefined ? {} : { publishedPolicy }),''',
)
replace_once(
    "admin/server.mjs",
    '''        publishedPolicy,
        musicMode: input.musicMode ?? "map",
      });''',
    '''        publishedPolicy,
        musicMode: input.musicMode ?? "map",
        stageNumber: input.stageNumber,
      });''',
)

# RevisionStore now validates every B04.2 policy scope.
replace_once(
    "admin/store.mjs",
    '''  rejectUnknownKeys(policy, "worldMusic.publishedPolicy", ["configRevision", "disabledTrackIds", "worlds", "global"]);''',
    '''  rejectUnknownKeys(policy, "worldMusic.publishedPolicy", ["configRevision", "disabledTrackIds", "stages", "worlds", "galaxies", "global"]);''',
)
replace_once(
    "admin/store.mjs",
    '''  if (policy.global !== undefined) validateWorldMusicEntry(policy.global, "worldMusic.publishedPolicy.global");
  if (policy.worlds !== undefined) {''',
    '''  if (policy.global !== undefined) validateWorldMusicEntry(policy.global, "worldMusic.publishedPolicy.global");
  if (policy.stages !== undefined) {
    const stages = object(policy.stages, "worldMusic.publishedPolicy.stages");
    for (const [stageId, entry] of Object.entries(stages)) {
      string(stageId, "worldMusic stage id", { max: 4, pattern: /^(?:[1-9]\\d{0,2}|1000)$/ });
      validateWorldMusicEntry(entry, "worldMusic.publishedPolicy.stages." + stageId);
    }
  }
  if (policy.worlds !== undefined) {''',
)
replace_once(
    "admin/store.mjs",
    '''      validateWorldMusicEntry(entry, "worldMusic.publishedPolicy.worlds." + worldId);
    }
  }
}

function validateAudio''',
    '''      validateWorldMusicEntry(entry, "worldMusic.publishedPolicy.worlds." + worldId);
    }
  }
  if (policy.galaxies !== undefined) {
    const galaxies = object(policy.galaxies, "worldMusic.publishedPolicy.galaxies");
    for (const [galaxyId, entry] of Object.entries(galaxies)) {
      string(galaxyId, "worldMusic galaxy id", { max: 2, pattern: /^(?:[1-9]|10)$/ });
      validateWorldMusicEntry(entry, "worldMusic.publishedPolicy.galaxies." + galaxyId);
    }
  }
}

function validateAudio''',
)

# Admin editor: unlock all hierarchy scopes and route assignments to canonical maps.
ui = "portal/src/admin/space-typing-world-music-phase-b.ts"
replace_once(ui, 'type Scope = "global" | "world";', 'type Scope = "global" | "galaxy" | "world" | "stage";')
replace_once(
    ui,
    '''  return structuredClone(policy ?? { configRevision: `admin-${activeRevision}`, worlds: {} });''',
    '''  return structuredClone(policy ?? { configRevision: `admin-${activeRevision}`, stages: {}, worlds: {}, galaxies: {} });''',
)
replace_once(
    ui,
    '''function worldEntry(policy: WorldMusicPolicy, worldId: string, create = false): WorldMusicPolicyEntry | undefined {
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
}''',
    '''function rootEntry(
  policy: WorldMusicPolicy,
  scope: Scope,
  worldId: string,
  galaxyId: number,
  stageNumber: number,
  create = false,
): WorldMusicPolicyEntry | undefined {
  if (scope === "global") {
    if (policy.global !== undefined || !create) return policy.global;
    policy.global = {};
    return policy.global;
  }

  const key = scope === "world" ? worldId : String(scope === "galaxy" ? galaxyId : stageNumber);
  const map = scope === "world" ? policy.worlds : scope === "galaxy" ? policy.galaxies : policy.stages;
  const current = map?.[key];
  if (current !== undefined || !create) return current;

  const entry: WorldMusicPolicyEntry = {};
  if (scope === "world") {
    policy.worlds ??= {};
    policy.worlds[key] = entry;
  } else if (scope === "galaxy") {
    policy.galaxies ??= {};
    policy.galaxies[key] = entry;
  } else {
    policy.stages ??= {};
    policy.stages[key] = entry;
  }
  return entry;
}

function readAssignment(
  policy: WorldMusicPolicy,
  scope: Scope,
  worldId: string,
  galaxyId: number,
  stageNumber: number,
  slot: Slot,
): PlaylistAssignment | undefined {
  const root = rootEntry(policy, scope, worldId, galaxyId, stageNumber);
  if (root === undefined) return undefined;
  if (slot === "normal") return root.normal;
  if (slot === "boss-common") return root.boss?.common;
  return root.boss?.[slot];
}

function writeAssignment(
  policy: WorldMusicPolicy,
  scope: Scope,
  worldId: string,
  galaxyId: number,
  stageNumber: number,
  slot: Slot,
  assignment: PlaylistAssignment,
): void {
  const root = rootEntry(policy, scope, worldId, galaxyId, stageNumber, true)!;
  if (slot === "normal") {
    root.normal = assignment;
    return;
  }
  root.boss ??= {};
  if (slot === "boss-common") root.boss.common = assignment;
  else root.boss[slot] = assignment;
}''',
)
replace_once(
    ui,
    '''  collect(policy.global);
  for (const entry of Object.values(policy.worlds ?? {})) collect(entry);''',
    '''  collect(policy.global);
  for (const entry of Object.values(policy.galaxies ?? {})) collect(entry);
  for (const entry of Object.values(policy.worlds ?? {})) collect(entry);
  for (const entry of Object.values(policy.stages ?? {})) collect(entry);''',
)
replace_once(
    ui,
    '''    el("p", undefined, "B04.1 wires the scopes the pinned child resolver really supports today: Global and World. Save Draft creates an immutable revision; Publish applies the policy on the next track/state boundary."),''',
    '''    el("p", undefined, "B04.2 wires the full canonical hierarchy: Global → Galaxy → World → Stage → State. Save Draft creates an immutable revision; Publish remains an explicit review action."),''',
)
replace_once(
    ui,
    '''  actions.append(revisionBadge, badge("GLOBAL + WORLD LIVE", "good"), badge("GALAXY / STAGE BLOCKED", "warn"));''',
    '''  actions.append(revisionBadge, badge("GLOBAL + GALAXY + WORLD + STAGE", "good"), badge("CANONICAL PREVIEW", "info"));''',
)
replace_once(
    ui,
    '''  page.append(notice("Scope safety: the child WorldMusicPolicy v1 has no galaxy/stage keys. Galaxy and Stage authoring stay disabled until the child resolver, preview protocol and runtime consumer are extended together; Admin will not persist JSON that runtime silently ignores.", "warn"));''',
    '''  page.append(notice("B04.2 safety: every editable scope is persisted in the child-owned policy shape and previewed through the same canonical resolver before an immutable draft can be saved.", "info"));''',
)
replace_once(
    ui,
    '''  let scope: Scope = "world";
  let worldId = "world-01";
  let slot: Slot = "normal";

  const scopePanel = panel("Canonical Scope", "Only scopes represented by WorldMusicPolicy v1 can be saved");''',
    '''  let scope: Scope = "world";
  let worldId = "world-01";
  let galaxyId = 1;
  let stageNumber = 1;
  let slot: Slot = "normal";

  const scopePanel = panel("Canonical Scope", "Global → Galaxy → World → Stage; State is selected in the assignment tabs");''',
)
replace_once(
    ui,
    '''  const globalButton = btn("Global");
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
  scopeBody.append(scopeSeg, worldSelect);''',
    '''  const globalButton = btn("Global");
  const galaxyButton = btn("Galaxy");
  const worldButton = btn("World");
  const stageButton = btn("Stage");
  scopeSeg.append(globalButton, galaxyButton, worldButton, stageButton);

  const galaxySelect = el("select", "st-admin-select") as HTMLSelectElement;
  galaxySelect.setAttribute("aria-label", "World Music Galaxy scope");
  for (let index = 1; index <= 10; index += 1) {
    galaxySelect.append(new Option(`Galaxy ${String(index).padStart(2, "0")}`, String(index)));
  }

  const worldSelect = el("select", "st-admin-select") as HTMLSelectElement;
  worldSelect.setAttribute("aria-label", "World Music World scope");
  for (let index = 1; index <= 50; index += 1) {
    const id = `world-${String(index).padStart(2, "0")}`;
    worldSelect.append(new Option(`World ${String(index).padStart(2, "0")}`, id));
  }

  const stageInput = el("input", "st-admin-select") as HTMLInputElement;
  stageInput.type = "number";
  stageInput.min = "1";
  stageInput.max = "1000";
  stageInput.step = "1";
  stageInput.value = "1";
  stageInput.setAttribute("aria-label", "World Music Stage scope");

  scopeBody.append(scopeSeg, galaxySelect, worldSelect, stageInput);''',
)
replace_once(
    ui,
    '''  const updateScopeState = (): void => {
    globalButton.classList.toggle("active", scope === "global");
    worldButton.classList.toggle("active", scope === "world");
    globalButton.setAttribute("aria-pressed", String(scope === "global"));
    worldButton.setAttribute("aria-pressed", String(scope === "world"));
    worldSelect.disabled = scope === "global";
    inheritButton.disabled = scope === "global";
    inheritButton.title = scope === "global" ? "Global has no parent scope to inherit from." : "Use generated/global fallback.";
  };''',
    '''  const syncWorldFromGalaxy = (): void => {
    const representative = preview?.worlds.find((entry) => entry.galaxy === galaxyId);
    const fallbackWorld = Math.min(50, (galaxyId - 1) * 5 + 1);
    worldId = representative?.worldId ?? `world-${String(fallbackWorld).padStart(2, "0")}`;
    worldSelect.value = worldId;
  };

  const syncWorldFromStage = (): void => {
    const owner = preview?.worlds.find((entry) => stageNumber >= entry.stageRange[0] && stageNumber <= entry.stageRange[1]);
    const fallbackWorld = Math.min(50, Math.max(1, Math.ceil(stageNumber / 20)));
    worldId = owner?.worldId ?? `world-${String(fallbackWorld).padStart(2, "0")}`;
    galaxyId = owner?.galaxy ?? Math.min(10, Math.max(1, Math.ceil(fallbackWorld / 5)));
    worldSelect.value = worldId;
    galaxySelect.value = String(galaxyId);
  };

  const updateScopeState = (): void => {
    for (const [value, control] of [
      ["global", globalButton],
      ["galaxy", galaxyButton],
      ["world", worldButton],
      ["stage", stageButton],
    ] as const) {
      control.classList.toggle("active", scope === value);
      control.setAttribute("aria-pressed", String(scope === value));
    }
    galaxySelect.disabled = scope !== "galaxy";
    worldSelect.disabled = scope !== "world";
    stageInput.disabled = scope !== "stage";
    inheritButton.disabled = scope === "global";
    inheritButton.title = scope === "global"
      ? "Global has no parent scope to inherit from."
      : "Inherit from the next broader canonical scope.";
  };''',
)
replace_once(
    ui,
    '''    effectiveBody.append(el("p", undefined, `${scope === "global" ? "Global policy representative preview" : world.name} · ${SLOT_LABELS[slot]}`));''',
    '''    const scopeLabel = scope === "global"
      ? "Global policy representative preview"
      : scope === "galaxy"
        ? `Galaxy ${String(galaxyId).padStart(2, "0")} · ${world.name} representative`
        : scope === "stage"
          ? `Stage ${String(stageNumber).padStart(3, "0")} · ${world.name}`
          : world.name;
    effectiveBody.append(el("p", undefined, `${scopeLabel} · ${SLOT_LABELS[slot]}`));''',
)
replace_all(
    ui,
    "readAssignment(draftPolicy, scope, worldId, slot)",
    "readAssignment(draftPolicy, scope, worldId, galaxyId, stageNumber, slot)",
    expected_min=4,
)
replace_all(
    ui,
    "writeAssignment(draftPolicy, scope, worldId, slot,",
    "writeAssignment(draftPolicy, scope, worldId, galaxyId, stageNumber, slot,",
    expected_min=3,
)
replace_once(
    ui,
    '''    preview = await api.previewWorldMusic({ publishedPolicy: draftPolicy, musicMode: "map" });''',
    '''    preview = await api.previewWorldMusic({
      publishedPolicy: draftPolicy,
      musicMode: "map",
      ...(scope === "stage" ? { stageNumber } : {}),
    });
    if (scope === "stage") syncWorldFromStage();
    if (scope === "galaxy") syncWorldFromGalaxy();''',
)
replace_once(
    ui,
    '''  globalButton.addEventListener("click", () => { scope = "global"; syncEditor(); });
  worldButton.addEventListener("click", () => { scope = "world"; syncEditor(); });
  worldSelect.addEventListener("change", () => { worldId = worldSelect.value; syncEditor(); });''',
    '''  const refreshScopePreview = (): void => {
    void validateDraft().catch((error: unknown) => {
      runtimeStatus.className = "st-admin-info-banner bad";
      runtimeStatus.textContent = `Preview rejected: ${error instanceof Error ? error.message : String(error)}`;
    });
  };
  globalButton.addEventListener("click", () => { scope = "global"; syncEditor(); refreshScopePreview(); });
  galaxyButton.addEventListener("click", () => { scope = "galaxy"; syncWorldFromGalaxy(); syncEditor(); refreshScopePreview(); });
  worldButton.addEventListener("click", () => { scope = "world"; syncEditor(); refreshScopePreview(); });
  stageButton.addEventListener("click", () => { scope = "stage"; syncWorldFromStage(); syncEditor(); refreshScopePreview(); });
  galaxySelect.addEventListener("change", () => {
    galaxyId = Number.parseInt(galaxySelect.value, 10);
    syncWorldFromGalaxy();
    syncEditor();
  });
  worldSelect.addEventListener("change", () => {
    worldId = worldSelect.value;
    const selectedWorld = preview?.worlds.find((entry) => entry.worldId === worldId);
    galaxyId = selectedWorld?.galaxy ?? Math.min(10, Math.max(1, Math.ceil(Number.parseInt(worldId.slice(6), 10) / 5)));
    galaxySelect.value = String(galaxyId);
    syncEditor();
  });
  stageInput.addEventListener("change", () => {
    const next = Number.parseInt(stageInput.value, 10);
    stageNumber = Number.isInteger(next) ? Math.min(1000, Math.max(1, next)) : 1;
    stageInput.value = String(stageNumber);
    syncWorldFromStage();
    syncEditor();
    refreshScopePreview();
  });''',
)
replace_once(
    ui,
    '''  const saveStatus = el("span", undefined, "Save Draft validates and stores Global/World policy only · Publish remains explicit");''',
    '''  const saveStatus = el("span", undefined, "Save Draft validates Global/Galaxy/World/Stage policy · Publish remains explicit");''',
)
replace_once(ui, '''        policyRevision: "phase-b-world-music-v1",''', '''        policyRevision: "phase-b-world-music-b04.2",''')
replace_once(
    ui,
    '''        message: "Admin Phase B · World Music Global/World draft",''',
    '''        message: "Admin Phase B · World Music Global/Galaxy/World/Stage draft",''',
)
replace_once(
    ui,
    '''  saveBar.append(el("strong", undefined, "B04.1 World Music Draft"),''',
    '''  saveBar.append(el("strong", undefined, "B04.2 World Music Draft"),''',
)
replace_once(
    ui,
    '''      ? "Loaded generated/legacy World Music fallback. First B04.1 draft will add an additive publishedPolicy namespace."''',
    '''      ? "Loaded generated/legacy World Music fallback. First B04.2 draft can author Global/Galaxy/World/Stage scopes."''',
)

# Parent persistence tests: all four scopes are canonical; malformed ids still reject.
store_test = "admin/store.test.mjs"
replace_once(
    store_test,
    'test("B04.1 World Music canonical Global/World draft stays isolated until publish", async (t) => {',
    'test("B04.2 World Music canonical all-scope draft stays isolated until publish", async (t) => {',
)
replace_once(
    store_test,
    '''    global: { normal: { kind: "replace", trackIds: ["signal-in-the-void"], selectionMode: "ordered" } },
    worlds: { "world-01": { boss: { world: { kind: "replace", trackIds: ["world-01-boss-battle-theme-a"] } } } },
  };''',
    '''    global: { normal: { kind: "replace", trackIds: ["signal-in-the-void"], selectionMode: "ordered" } },
    galaxies: { "2": { normal: { kind: "replace", trackIds: ["signal-in-the-void"] } } },
    worlds: { "world-06": { boss: { world: { kind: "replace", trackIds: ["world-01-boss-battle-theme-a"] } } } },
    stages: { "101": { normal: { kind: "replace", trackIds: ["signal-in-the-void"], selectionMode: "ordered" } } },
  };''',
)
replace_once(
    store_test,
    '''  assert.deepEqual(runtime.worldMusic.publishedPolicy.global.normal.trackIds, ["signal-in-the-void"]);
});

test("B04.1 rejects unsupported Stage/Galaxy policy and unsafe replacement playlists", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const unsupportedStage = structuredClone(active.config);
  unsupportedStage.worldMusic.publishedPolicy = { configRevision: "bad-stage", stages: { "1": {} } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: unsupportedStage }), AdminValidationError);
  const unsupportedGalaxy = structuredClone(active.config);
  unsupportedGalaxy.worldMusic.publishedPolicy = { configRevision: "bad-galaxy", galaxies: { "1": {} } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: unsupportedGalaxy }), AdminValidationError);
  const emptyReplace = structuredClone(active.config);
  emptyReplace.worldMusic.publishedPolicy = { configRevision: "bad-empty", worlds: { "world-01": { normal: { kind: "replace", trackIds: [] } } } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: emptyReplace }), AdminValidationError);
  const badWorld = structuredClone(active.config);
  badWorld.worldMusic.publishedPolicy = { configRevision: "bad-world", worlds: { "world-51": { normal: { kind: "inherit" } } } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badWorld }), AdminValidationError);
});''',
    '''  assert.deepEqual(runtime.worldMusic.publishedPolicy.global.normal.trackIds, ["signal-in-the-void"]);
  assert.deepEqual(runtime.worldMusic.publishedPolicy.galaxies["2"].normal.trackIds, ["signal-in-the-void"]);
  assert.deepEqual(runtime.worldMusic.publishedPolicy.stages["101"].normal.trackIds, ["signal-in-the-void"]);
});

test("B04.2 rejects malformed scope ids and unsafe replacement playlists", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();

  const badStage = structuredClone(active.config);
  badStage.worldMusic.publishedPolicy = { configRevision: "bad-stage", stages: { "0": {} } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badStage }), AdminValidationError);

  const badGalaxy = structuredClone(active.config);
  badGalaxy.worldMusic.publishedPolicy = { configRevision: "bad-galaxy", galaxies: { "11": {} } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badGalaxy }), AdminValidationError);

  const emptyReplace = structuredClone(active.config);
  emptyReplace.worldMusic.publishedPolicy = { configRevision: "bad-empty", worlds: { "world-01": { normal: { kind: "replace", trackIds: [] } } } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: emptyReplace }), AdminValidationError);

  const badWorld = structuredClone(active.config);
  badWorld.worldMusic.publishedPolicy = { configRevision: "bad-world", worlds: { "world-51": { normal: { kind: "inherit" } } } };
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badWorld }), AdminValidationError);
});''',
)

# End-to-end parent -> child preview coverage for Stage and Galaxy.
preview_test = Path("admin/world-music-preview.test.mjs")
preview_text = preview_test.read_text()
marker = 'test("B04.2 parent preview forwards Stage and resolves Galaxy fallback", async () => {'
if marker not in preview_text:
    preview_text += '''

test("B04.2 parent preview forwards Stage and resolves Galaxy fallback", async () => {
  const stagePreview = await runWorldMusicPreview({
    rootDir,
    contract,
    stageNumber: 101,
    publishedPolicy: {
      configRevision: "parent-stage-test-v1",
      stages: {
        "101": {
          normal: {
            kind: "replace",
            trackIds: ["signal-in-the-void"],
            selectionMode: "ordered",
          },
        },
      },
    },
  });
  assert.equal(stagePreview.stageNumber, 101);
  const world06Stage = stagePreview.worlds.find((world) => world.worldId === "world-06");
  assert.equal(world06Stage.states.normal.resolvedFrom, "stage-101.published.normal");
  assert.ok(world06Stage.states.normal.badges.includes("STAGE OVERRIDE"));

  const galaxyPreview = await runWorldMusicPreview({
    rootDir,
    contract,
    publishedPolicy: {
      configRevision: "parent-galaxy-test-v1",
      galaxies: {
        "2": {
          normal: {
            kind: "replace",
            trackIds: ["signal-in-the-void"],
            selectionMode: "ordered",
          },
        },
      },
    },
  });
  const world06Galaxy = galaxyPreview.worlds.find((world) => world.worldId === "world-06");
  assert.equal(world06Galaxy.states.normal.resolvedFrom, "galaxy-2.published.normal");
  assert.ok(world06Galaxy.states.normal.badges.includes("GALAXY FALLBACK"));
});
'''
    preview_test.write_text(preview_text)

# Machine-readable mapping and docs now report B04.2 all-scope support.
replace_once(
    "admin/space-typing-phase-b-map.v1.json",
    '"status": "phase-b-ui-wired-global-world"',
    '"status": "phase-b-ui-wired-all-scopes"',
)
mapping = "portal/src/admin/SPACE_TYPING_PHASE_B_MAPPING.md"
replace_once(
    mapping,
    '''## B04.1 — World Music canonical scopes

The Phase A editor exposed All → Galaxy → World → Stage, but the pinned child `WorldMusicPolicy` v1 only models `global` and `worlds`. B04.1 therefore wires only Global + World to real immutable revisions. Every draft is previewed through the child `music:admin-preview` resolver before save. Galaxy/Stage controls are blocked instead of persisting ignored JSON. B04.2 is the explicit child-contract expansion needed before those scopes can become writable.''',
    '''## B04.1 — World Music canonical scopes

B04.1 wired Global + World to real immutable revisions while Galaxy/Stage stayed blocked until the child contract could consume those scopes.

## B04.2 — Galaxy + Stage canonical scopes

The pinned child now models `stages`, `worlds`, `galaxies`, and `global`, with effective precedence Stage → World → Galaxy → Global (plus the explicit legacy World migration fallback). The parent editor can author all four scopes, persists only validated numeric Galaxy/Stage ids, forwards the selected Stage to the child preview protocol, and still saves immutable drafts without direct Publish. Random-normal playback keeps its legacy global/random-library semantics; map/boss preview uses the hierarchical resolver.''',
)
replace_once(
    mapping,
    '''4. **B04 — World Music**: **B04.1 implemented** for canonical Global + World policy drafts, child preview validation, stale-active protection, and next-track/state apply boundary. Galaxy/Stage remain intentionally blocked because child WorldMusicPolicy v1 does not consume those scopes; B04.2 must extend child resolver + preview + runtime before enabling them.''',
    '''4. **B04 — World Music**: **B04.1 + B04.2 implemented** for canonical Global + Galaxy + World + Stage policy drafts, child preview validation, effective fallback trace, stale-active protection, and next-track/state apply boundary. Production changes still require explicit History / Publish review.''',
)

# Validator must fail if the parent ever regresses back to blocked Stage/Galaxy UI.
validator = "scripts/validate-space-admin-phase-b.mjs"
replace_once(
    validator,
    'assert.equal(worldMusic?.status, "phase-b-ui-wired-global-world");',
    'assert.equal(worldMusic?.status, "phase-b-ui-wired-all-scopes");',
)
replace_once(
    validator,
    '''assert.match(worldMusicPhaseB, /B04\\.1 World Music Draft/);''',
    '''assert.match(worldMusicPhaseB, /B04\\.2 World Music Draft/);''',
)
replace_once(
    validator,
    '''assert.match(worldMusicPhaseB, /GALAXY \\/ STAGE BLOCKED/);
assert.match(worldMusicPhaseB, /WorldMusicPolicy v1 has no galaxy\\/stage keys/);''',
    '''assert.doesNotMatch(worldMusicPhaseB, /GALAXY \\/ STAGE BLOCKED/);
assert.match(worldMusicPhaseB, /type Scope = "global" \\| "galaxy" \\| "world" \\| "stage"/);
assert.match(worldMusicPhaseB, /policy\\.galaxies/);
assert.match(worldMusicPhaseB, /policy\\.stages/);
assert.match(worldMusicPhaseB, /stageNumber/);''',
)
replace_once(
    validator,
    '''console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B04.1 revision-backed domains ready).`);''',
    '''console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B04.2 revision-backed domains ready).`);''',
)

print("B04.2 parent exact-string patch applied.")
