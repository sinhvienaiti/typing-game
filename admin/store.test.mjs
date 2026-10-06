import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { AdminConflictError, AdminValidationError, RevisionStore } from "./store.mjs";
import { createDefaultSpaceTypingConfig } from "./default-config.mjs";

const contract = {
  contractRevision: "space-typing-admin-v1",
  configSchemaVersion: 1,
  worldMusicCatalogSchemaVersion: 1,
};

async function fixture() {
  const rootDir = await mkdtemp(join(tmpdir(), "typing-game-admin-"));
  let tick = 0;
  const store = new RevisionStore({
    rootDir,
    contract,
    now: () => new Date(Date.UTC(2026, 9, 5, 12, 0, tick++)),
  });
  await store.initialize(createDefaultSpaceTypingConfig(contract));
  return { store, rootDir };
}

test("default config seeds additive Phase B system and feature flag namespaces", () => {
  const config = createDefaultSpaceTypingConfig(contract);
  assert.equal(config.system.gameDefaults.defaultMode, "campaign");
  assert.equal(config.system.network.minimumVersion, "0.1.0");
  assert.equal(config.system.maintenance.enabled, false);
  assert.equal(config.featureFlags["stamina"].risk, "economy");
  assert.equal(config.featureFlags["new-boss-renderer"].rolloutPercent, 25);
});

test("draft revisions stay isolated from runtime until CAS publish", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const activeBefore = await store.getActiveRevision();
  const config = structuredClone(activeBefore.config);
  config.audio.defaults.music = 0.18;

  const draft = await store.createRevision({
    baseRevision: activeBefore.revision,
    config,
    message: "Lower default music under pronunciation",
  });

  assert.equal((await store.getRuntimeConfig()).audio.defaults.music, 0.26);
  await store.publish({
    revision: draft.revision,
    expectedActiveRevision: activeBefore.revision,
  });
  assert.equal((await store.getRuntimeConfig()).audio.defaults.music, 0.18);
});

test("Phase B system changes stay isolated until publish", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const active = await store.getActiveRevision();
  const config = structuredClone(active.config);
  config.system.maintenance.enabled = true;
  config.system.maintenance.message = "Phase B maintenance test";
  config.featureFlags["new-boss-renderer"].rolloutPercent = 50;

  const draft = await store.createRevision({
    baseRevision: active.revision,
    config,
    message: "Phase B system draft",
  });

  assert.equal((await store.getRuntimeConfig()).system.maintenance.enabled, false);
  assert.equal((await store.getRuntimeConfig()).featureFlags["new-boss-renderer"].rolloutPercent, 25);

  await store.publish({ revision: draft.revision, expectedActiveRevision: active.revision });
  const runtime = await store.getRuntimeConfig();
  assert.equal(runtime.system.maintenance.enabled, true);
  assert.equal(runtime.system.maintenance.message, "Phase B maintenance test");
  assert.equal(runtime.featureFlags["new-boss-renderer"].rolloutPercent, 50);
});

test("Phase B validation rejects unsafe malformed system and feature flag drafts", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const active = await store.getActiveRevision();

  const badRollout = structuredClone(active.config);
  badRollout.featureFlags["pvp-reflex"].rolloutPercent = 101;
  await assert.rejects(
    store.createRevision({ baseRevision: active.revision, config: badRollout }),
    AdminValidationError,
  );

  const badVersion = structuredClone(active.config);
  badVersion.system.network.minimumVersion = "latest";
  await assert.rejects(
    store.createRevision({ baseRevision: active.revision, config: badVersion }),
    AdminValidationError,
  );

  const badMaintenance = structuredClone(active.config);
  badMaintenance.system.maintenance.message = "x".repeat(501);
  await assert.rejects(
    store.createRevision({ baseRevision: active.revision, config: badMaintenance }),
    AdminValidationError,
  );
});

test("pre-Phase-B v1 revisions remain valid when additive namespaces are absent", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const active = await store.getActiveRevision();
  const legacy = structuredClone(active.config);
  delete legacy.system;
  delete legacy.featureFlags;

  const draft = await store.createRevision({
    baseRevision: active.revision,
    config: legacy,
    message: "Legacy v1 compatibility",
  });
  assert.equal(draft.config.system, undefined);
  assert.equal(draft.config.featureFlags, undefined);
});

test("publish rejects stale expected active revisions", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const active = await store.getActiveRevision();
  const first = await store.createRevision({
    baseRevision: active.revision,
    config: active.config,
    message: "First draft",
  });
  const second = await store.createRevision({
    baseRevision: active.revision,
    config: active.config,
    message: "Second draft",
  });

  await store.publish({
    revision: first.revision,
    expectedActiveRevision: active.revision,
  });
  await assert.rejects(
    store.publish({
      revision: second.revision,
      expectedActiveRevision: active.revision,
    }),
    AdminConflictError,
  );
});

test("rollback is a CAS pointer change to an immutable prior revision", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const seed = await store.getActiveRevision();
  const changedConfig = structuredClone(seed.config);
  changedConfig.audio.defaults.sfx = 0.4;
  const changed = await store.createRevision({
    baseRevision: seed.revision,
    config: changedConfig,
  });
  await store.publish({
    revision: changed.revision,
    expectedActiveRevision: seed.revision,
  });
  await store.rollback({
    targetRevision: seed.revision,
    expectedActiveRevision: changed.revision,
  });
  assert.equal((await store.getState()).activeRevision, seed.revision);
  assert.equal((await store.getRevision(changed.revision)).config.audio.defaults.sfx, 0.4);
});

test("contract/schema drift is rejected before a revision is written", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const active = await store.getActiveRevision();
  const incompatible = structuredClone(active.config);
  incompatible.contractRevision = "space-typing-admin-v2";

  await assert.rejects(
    store.createRevision({
      baseRevision: active.revision,
      config: incompatible,
    }),
    AdminValidationError,
  );
});


test("B03 default audio profile matches runtime-backed gain fields", () => {
  const config = createDefaultSpaceTypingConfig(contract);
  assert.equal(config.audio.defaults.credit, 1);
  assert.deepEqual(config.audio.defaults.categories, {
    typing: 1,
    combat: 1,
    warnings: 1,
    ui: 1,
    rewards: 1,
  });
});

test("B03 audio draft stays isolated until publish and preserves legacy compatibility", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const config = structuredClone(active.config);
  config.audio.defaults.music = 0.2;
  config.audio.defaults.credit = 1.25;
  config.audio.defaults.categories.typing = 0.75;
  const draft = await store.createRevision({ baseRevision: active.revision, config, message: "B03 audio draft" });
  assert.equal((await store.getRuntimeConfig()).audio.defaults.music, 0.26);
  await store.publish({ revision: draft.revision, expectedActiveRevision: active.revision });
  const runtime = await store.getRuntimeConfig();
  assert.equal(runtime.audio.defaults.music, 0.2);
  assert.equal(runtime.audio.defaults.credit, 1.25);
  assert.equal(runtime.audio.defaults.categories.typing, 0.75);

  const legacy = structuredClone(runtime);
  delete legacy.audio.defaults.credit;
  delete legacy.audio.defaults.categories;
  const legacyDraft = await store.createRevision({ baseRevision: draft.revision, config: legacy, message: "Legacy audio compatibility" });
  assert.equal(legacyDraft.config.audio.defaults.credit, undefined);
});

test("B03 audio validation rejects out-of-range gain and category defaults", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const badCredit = structuredClone(active.config);
  badCredit.audio.defaults.credit = 2.01;
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badCredit }), AdminValidationError);
  const badCategory = structuredClone(active.config);
  badCategory.audio.defaults.categories.combat = 1.01;
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badCategory }), AdminValidationError);
  const badMaster = structuredClone(active.config);
  badMaster.audio.defaults.master = -0.01;
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badMaster }), AdminValidationError);
});


test("B04.2 World Music canonical all-scope draft stays isolated until publish", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const config = structuredClone(active.config);
  config.worldMusic.publishedPolicy = {
    configRevision: "admin-world-music-test-v1",
    global: { normal: { kind: "replace", trackIds: ["signal-in-the-void"], selectionMode: "ordered" } },
    galaxies: { "2": { normal: { kind: "replace", trackIds: ["signal-in-the-void"] } } },
    worlds: { "world-06": { boss: { world: { kind: "replace", trackIds: ["world-01-boss-battle-theme-a"] } } } },
    stages: { "101": { normal: { kind: "replace", trackIds: ["signal-in-the-void"], selectionMode: "ordered" } } },
  };
  const draft = await store.createRevision({ baseRevision: active.revision, config, message: "B04.1 world music draft" });
  assert.equal((await store.getRuntimeConfig()).worldMusic.publishedPolicy, undefined);
  await store.publish({ revision: draft.revision, expectedActiveRevision: active.revision });
  const runtime = await store.getRuntimeConfig();
  assert.equal(runtime.worldMusic.publishedPolicy.configRevision, "admin-world-music-test-v1");
  assert.deepEqual(runtime.worldMusic.publishedPolicy.global.normal.trackIds, ["signal-in-the-void"]);
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
});
