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


test("rejects invalid audio and World Music policy drafts", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();

  const badAudio = structuredClone(active.config);
  badAudio.audio.defaults.music = 1.5;
  await assert.rejects(
    store.createRevision({ baseRevision: active.revision, config: badAudio }),
    AdminValidationError,
  );

  const badPolicy = structuredClone(active.config);
  badPolicy.worldMusic.policyRevision = "admin-bad-v1";
  badPolicy.worldMusic.publishedPolicy = {
    configRevision: "admin-bad-v1",
    worlds: {
      "world-01": { normal: { kind: "replace", trackIds: [] } },
    },
  };
  await assert.rejects(
    store.createRevision({ baseRevision: active.revision, config: badPolicy }),
    AdminValidationError,
  );
});

test("accepts a canonical published World Music policy as an isolated draft", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const config = structuredClone(active.config);
  config.worldMusic.policyRevision = "admin-world-music-v1";
  config.worldMusic.publishedPolicy = {
    configRevision: "admin-world-music-v1",
    worlds: {
      "world-01": {
        normal: {
          kind: "replace",
          trackIds: ["signal-in-the-void"],
          selectionMode: "ordered",
        },
      },
    },
  };
  const draft = await store.createRevision({
    baseRevision: active.revision,
    config,
    message: "World Music policy draft",
  });
  assert.equal(draft.config.worldMusic.publishedPolicy.configRevision, "admin-world-music-v1");
  assert.equal((await store.getRuntimeConfig()).worldMusic.publishedPolicy, undefined);
});
