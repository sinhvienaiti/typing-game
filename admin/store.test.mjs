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
