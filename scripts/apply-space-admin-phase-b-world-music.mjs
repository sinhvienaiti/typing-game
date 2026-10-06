import fs from "node:fs";

function replaceRequired(file, before, after, label) {
  const source = fs.readFileSync(file, "utf8");
  if (!source.includes(before)) throw new Error(`Missing ${label} anchor in ${file}`);
  fs.writeFileSync(file, source.replace(before, after));
}

const storePath = "admin/store.mjs";
let store = fs.readFileSync(storePath, "utf8");
const worldMusicValidation = `function rejectUnknownKeys(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) throw new AdminValidationError(path + "." + key + " is not supported by the current canonical schema.");
  }
}

function validateTrackIds(value, path, { allowEmpty = true } = {}) {
  if (!Array.isArray(value)) throw new AdminValidationError(path + " must be an array.");
  if (!allowEmpty && value.length === 0) throw new AdminValidationError(path + " must contain at least one track id.");
  const seen = new Set();
  for (const [index, id] of value.entries()) {
    string(id, path + "[" + index + "]", { max: 160, pattern: /^[a-z0-9][a-z0-9._-]*$/ });
    if (seen.has(id)) throw new AdminValidationError(path + " contains duplicate track id " + id + ".");
    seen.add(id);
  }
}

function validatePlaylistAssignment(value, path) {
  object(value, path);
  rejectUnknownKeys(value, path, ["kind", "trackIds", "selectionMode"]);
  enumValue(value.kind, path + ".kind", ["inherit", "replace"]);
  if (value.kind === "inherit") {
    if (value.trackIds !== undefined || value.selectionMode !== undefined) {
      throw new AdminValidationError(path + " inherit assignments cannot include trackIds/selectionMode.");
    }
    return;
  }
  validateTrackIds(value.trackIds, path + ".trackIds", { allowEmpty: false });
  if (value.selectionMode !== undefined) {
    enumValue(value.selectionMode, path + ".selectionMode", ["shuffle-bag", "ordered"]);
  }
}

function validateWorldMusicEntry(value, path) {
  object(value, path);
  rejectUnknownKeys(value, path, ["normal", "boss"]);
  if (value.normal !== undefined) validatePlaylistAssignment(value.normal, path + ".normal");
  if (value.boss !== undefined) {
    const boss = object(value.boss, path + ".boss");
    rejectUnknownKeys(boss, path + ".boss", ["common", "mini", "world", "major"]);
    for (const key of ["common", "mini", "world", "major"]) {
      if (boss[key] !== undefined) validatePlaylistAssignment(boss[key], path + ".boss." + key);
    }
  }
}

function validateWorldMusic(worldMusic) {
  object(worldMusic, "worldMusic");
  string(worldMusic.policyRevision, "worldMusic.policyRevision", { max: 120, pattern: /^[a-z0-9][a-z0-9._-]*$/ });
  object(worldMusic.assignments, "worldMusic.assignments");
  if (worldMusic.publishedPolicy === undefined) return;
  const policy = object(worldMusic.publishedPolicy, "worldMusic.publishedPolicy");
  rejectUnknownKeys(policy, "worldMusic.publishedPolicy", ["configRevision", "disabledTrackIds", "worlds", "global"]);
  string(policy.configRevision, "worldMusic.publishedPolicy.configRevision", { max: 160, pattern: /^[a-zA-Z0-9][a-zA-Z0-9._-]*$/ });
  if (policy.disabledTrackIds !== undefined) validateTrackIds(policy.disabledTrackIds, "worldMusic.publishedPolicy.disabledTrackIds");
  if (policy.global !== undefined) validateWorldMusicEntry(policy.global, "worldMusic.publishedPolicy.global");
  if (policy.worlds !== undefined) {
    const worlds = object(policy.worlds, "worldMusic.publishedPolicy.worlds");
    for (const [worldId, entry] of Object.entries(worlds)) {
      string(worldId, "worldMusic world id", { max: 8, pattern: /^world-(?:0[1-9]|[1-4]\\d|50)$/ });
      validateWorldMusicEntry(entry, "worldMusic.publishedPolicy.worlds." + worldId);
    }
  }
}

`;
const validatorAnchor = "function validateAudio(audio) {";
if (!store.includes(validatorAnchor)) throw new Error("Missing World Music validation insertion anchor");
store = store.replace(validatorAnchor, worldMusicValidation + validatorAnchor);
store = store.replace(
  '    if (config.worldMusic === null || typeof config.worldMusic !== "object") {\n      throw new AdminValidationError("worldMusic config is required.");\n    }',
  '    validateWorldMusic(config.worldMusic);',
);
fs.writeFileSync(storePath, store);

const apiPath = "portal/src/admin/api.ts";
let api = fs.readFileSync(apiPath, "utf8");
const typeAnchor = 'export type GeneralSettingsConfig = {';
const worldTypes = `export type PlaylistSelectionMode = "shuffle-bag" | "ordered";
export type PlaylistAssignment =
  | { kind: "inherit" }
  | { kind: "replace"; trackIds: string[]; selectionMode?: PlaylistSelectionMode };
export type WorldMusicBossPolicy = {
  common?: PlaylistAssignment;
  mini?: PlaylistAssignment;
  world?: PlaylistAssignment;
  major?: PlaylistAssignment;
};
export type WorldMusicPolicyEntry = {
  normal?: PlaylistAssignment;
  boss?: WorldMusicBossPolicy;
};
export type WorldMusicPolicy = {
  configRevision: string;
  disabledTrackIds?: string[];
  worlds?: Record<string, WorldMusicPolicyEntry>;
  global?: WorldMusicPolicyEntry;
};

`;
if (!api.includes(typeAnchor)) throw new Error("Missing API World Music type insertion anchor");
api = api.replace(typeAnchor, worldTypes + typeAnchor);
api = api.replace(
  '  worldMusic: {\n    policyRevision: string;\n    assignments: Record<string, unknown>;\n  };',
  '  worldMusic: {\n    policyRevision: string;\n    assignments: Record<string, unknown>;\n    /** Additive B04.1 canonical policy. Child v1 currently supports Global + World only. */\n    publishedPolicy?: WorldMusicPolicy;\n  };',
);
api = api.replace(
  '  previewWorldMusic(input: {\n    publishedPolicy?: unknown;\n    musicMode?: "map" | "random";\n  } = {}): Promise<WorldMusicPreview> {',
  '  previewWorldMusic(input: {\n    publishedPolicy?: WorldMusicPolicy;\n    musicMode?: "map" | "random";\n  } = {}): Promise<WorldMusicPreview> {',
);
fs.writeFileSync(apiPath, api);

const phaseBPath = "portal/src/admin/space-typing-phase-b.ts";
let phaseB = fs.readFileSync(phaseBPath, "utf8");
phaseB = phaseB.replace(
  'import { renderPhaseBAudio } from "./space-typing-audio-phase-b";\n',
  'import { renderPhaseBAudio } from "./space-typing-audio-phase-b";\nimport { renderPhaseBWorldMusic } from "./space-typing-world-music-phase-b";\n',
);
phaseB = phaseB.replace(
  '  if (path === `${BASE}/audio`) return renderPhaseBAudio(navigate);\n',
  '  if (path === `${BASE}/audio`) return renderPhaseBAudio(navigate);\n  if (path === `${BASE}/world-music`) return renderPhaseBWorldMusic(navigate);\n',
);
fs.writeFileSync(phaseBPath, phaseB);

const mapPath = "admin/space-typing-phase-b-map.v1.json";
const map = JSON.parse(fs.readFileSync(mapPath, "utf8"));
for (const entry of map.screens) {
  if (entry.route === "/admin/space-typing/world-music") entry.status = "phase-b-ui-wired-global-world";
}
fs.writeFileSync(mapPath, `${JSON.stringify(map, null, 2)}\n`);

const testsPath = "admin/store.test.mjs";
let tests = fs.readFileSync(testsPath, "utf8");
tests += `

test("B04.1 World Music canonical Global/World draft stays isolated until publish", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const config = structuredClone(active.config);
  config.worldMusic.publishedPolicy = {
    configRevision: "admin-world-music-test-v1",
    global: { normal: { kind: "replace", trackIds: ["signal-in-the-void"], selectionMode: "ordered" } },
    worlds: { "world-01": { boss: { world: { kind: "replace", trackIds: ["world-01-boss-battle-theme-a"] } } } },
  };
  const draft = await store.createRevision({ baseRevision: active.revision, config, message: "B04.1 world music draft" });
  assert.equal((await store.getRuntimeConfig()).worldMusic.publishedPolicy, undefined);
  await store.publish({ revision: draft.revision, expectedActiveRevision: active.revision });
  const runtime = await store.getRuntimeConfig();
  assert.equal(runtime.worldMusic.publishedPolicy.configRevision, "admin-world-music-test-v1");
  assert.deepEqual(runtime.worldMusic.publishedPolicy.global.normal.trackIds, ["signal-in-the-void"]);
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
});
`;
fs.writeFileSync(testsPath, tests);

const validatorPath = "scripts/validate-space-admin-phase-b.mjs";
let validator = fs.readFileSync(validatorPath, "utf8");
validator = validator.replace(
  'const audioPhaseB = await readFile(new URL("portal/src/admin/space-typing-audio-phase-b.ts", root), "utf8");',
  'const audioPhaseB = await readFile(new URL("portal/src/admin/space-typing-audio-phase-b.ts", root), "utf8");\nconst worldMusicPhaseB = await readFile(new URL("portal/src/admin/space-typing-world-music-phase-b.ts", root), "utf8");',
);
validator = validator.replace(
  'const settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");',
  'const worldMusic = map.screens.find((entry) => entry.route === "/admin/space-typing/world-music");\nconst settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");',
);
validator = validator.replace(
  'assert.equal(settings?.domain, "system");',
  'assert.equal(worldMusic?.domain, "worldMusic");\nassert.equal(worldMusic?.status, "phase-b-ui-wired-global-world");\nassert.equal(worldMusic?.applyBoundary, "next-track-or-state");\nassert.equal(settings?.domain, "system");',
);
validator = validator.replace(
  'assert.match(audioPhaseB, /assertStableActiveRevision/);',
  'assert.match(audioPhaseB, /assertStableActiveRevision/);\nassert.match(phaseB, /renderPhaseBWorldMusic/);\nassert.match(worldMusicPhaseB, /B04\\.1 World Music Draft/);\nassert.match(worldMusicPhaseB, /api\\.previewWorldMusic/);\nassert.match(worldMusicPhaseB, /api\\.createRevision/);\nassert.doesNotMatch(worldMusicPhaseB, /api\\.publish/);\nassert.match(worldMusicPhaseB, /GALAXY \\/ STAGE BLOCKED/);\nassert.match(worldMusicPhaseB, /WorldMusicPolicy v1 has no galaxy\\/stage keys/);\nassert.match(worldMusicPhaseB, /assertStableActiveRevision/);',
);
validator = validator.replace(
  'console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B03 revision-backed domains ready).`);',
  'console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B04.1 revision-backed domains ready).`);',
);
fs.writeFileSync(validatorPath, validator);

const docPath = "portal/src/admin/SPACE_TYPING_PHASE_B_MAPPING.md";
let doc = fs.readFileSync(docPath, "utf8");
doc = doc.replace(
  '4. **B04 — World Music**: map Stage-level editor data into authored policy drafts and canonical preview validation; keep runtime apply at next-track/state.',
  '4. **B04 — World Music**: **B04.1 implemented** for canonical Global + World policy drafts, child preview validation, stale-active protection, and next-track/state apply boundary. Galaxy/Stage remain intentionally blocked because child WorldMusicPolicy v1 does not consume those scopes; B04.2 must extend child resolver + preview + runtime before enabling them.',
);
doc = doc.replace(
  '## Apply boundaries',
  '## B04.1 — World Music canonical scopes\n\nThe Phase A editor exposed All → Galaxy → World → Stage, but the pinned child `WorldMusicPolicy` v1 only models `global` and `worlds`. B04.1 therefore wires only Global + World to real immutable revisions. Every draft is previewed through the child `music:admin-preview` resolver before save. Galaxy/Stage controls are blocked instead of persisting ignored JSON. B04.2 is the explicit child-contract expansion needed before those scopes can become writable.\n\n## Apply boundaries',
);
fs.writeFileSync(docPath, doc);
