import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { createDefaultSpaceTypingConfig } from "./default-config.mjs";
import { createBossRuntimeEnvelope } from "./boss-runtime.mjs";
import { AdminValidationError } from "./store.mjs";
import { SpaceTypingRevisionStore } from "./space-typing-store.mjs";

const bossIds = ["void-emperor"];
const contract = {
  contractRevision: "space-typing-admin-v1",
  configSchemaVersion: 1,
  worldMusicCatalogSchemaVersion: 1,
  bosses: { ids: bossIds, authorableFields: ["name", "title"], constraints: { nameMax: 100, titleMax: 160 } },
  applyBoundaries: { bossPolicy: "new-session" },
};

async function fixture() {
  const rootDir = await mkdtemp(join(tmpdir(), "typing-game-boss-flow-"));
  let tick = 0;
  const store = new SpaceTypingRevisionStore({ rootDir, contract, now: () => new Date(Date.UTC(2026, 9, 7, 0, 0, tick++)) });
  await store.initialize(createDefaultSpaceTypingConfig(contract));
  return { store, rootDir };
}

test("B06.5 Draft -> Validate -> Publish -> Runtime -> Rollback is revision isolated", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const seed = await store.getActiveRevision();
  const config = structuredClone(seed.config);
  config.content.bosses = { configRevision: "bosses-admin-test-v2", bosses: { "void-emperor": { name: "Abyss Regent", title: "Sovereign of Silence" } } };
  const draft = await store.createRevision({ baseRevision: seed.revision, config, message: "Boss identity override" });
  const validation = await store.validateRevision(draft.revision);
  assert.equal(validation.valid, true);
  assert.equal(validation.publishable, true);
  let runtime = createBossRuntimeEnvelope(await store.getState(), await store.getRuntimeConfig(), contract);
  assert.equal(runtime.policy.configRevision, "bosses-admin-v1");
  assert.deepEqual(runtime.policy.bosses, {});
  await store.publish({ revision: draft.revision, expectedActiveRevision: seed.revision });
  runtime = createBossRuntimeEnvelope(await store.getState(), await store.getRuntimeConfig(), contract);
  assert.equal(runtime.activeRevision, draft.revision);
  assert.equal(runtime.applyBoundary, "new-session");
  assert.equal(runtime.policy.bosses["void-emperor"].name, "Abyss Regent");
  await store.rollback({ targetRevision: seed.revision, expectedActiveRevision: draft.revision });
  runtime = createBossRuntimeEnvelope(await store.getState(), await store.getRuntimeConfig(), contract);
  assert.equal(runtime.activeRevision, seed.revision);
  assert.deepEqual(runtime.policy.bosses, {});
});

test("B06.5 invalid Boss authoring cannot create a revision", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  for (const bosses of [
    { unknown: { name: "Nope" } },
    { "void-emperor": { hp: 999999 } },
    { "void-emperor": { name: "x".repeat(101) } },
  ]) {
    const config = structuredClone(active.config);
    config.content.bosses = { configRevision: "bosses-invalid", bosses };
    await assert.rejects(store.createRevision({ baseRevision: active.revision, config }), AdminValidationError);
  }
});
