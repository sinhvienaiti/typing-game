import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { createDefaultSpaceTypingConfig } from "./default-config.mjs";
import { createStageRuntimeEnvelope } from "./stage-runtime.mjs";
import { AdminValidationError } from "./store.mjs";
import { SpaceTypingRevisionStore } from "./space-typing-store.mjs";

const contract = {
  contractRevision: "space-typing-admin-v1",
  configSchemaVersion: 1,
  worldMusicCatalogSchemaVersion: 1,
  stages: {
    count:1000,
    authorableFields:["enemyBudget","eliteChance","modifierSlots"],
    constraints:{stage:{min:1,max:1000,integer:true},enemyBudget:{minExclusive:0},eliteChance:{min:0,max:1},modifierSlots:{min:0,max:4,integer:true}},
  },
  applyBoundaries: { stagePolicy: "new-session" },
};

async function fixture() {
  const rootDir = await mkdtemp(join(tmpdir(), "typing-game-stage-flow-"));
  let tick = 0;
  const store = new SpaceTypingRevisionStore({ rootDir, contract, now: () => new Date(Date.UTC(2026, 9, 7, 0, 0, tick++)) });
  const seed = createDefaultSpaceTypingConfig(contract);
  seed.content = { stages: seed.content.stages };
  await store.initialize(seed);
  return { store, rootDir };
}

test("B06.6 Stage Draft -> Validate -> Publish -> Runtime -> Rollback is revision isolated", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const seed = await store.getActiveRevision();
  const config = structuredClone(seed.config);
  config.content.stages = { configRevision:"stages-admin-test-v2", stages:[{stage:37,enemyBudget:88,eliteChance:0.33,modifierSlots:3}] };
  const draft = await store.createRevision({ baseRevision: seed.revision, config, message: "Stage gameplay override" });
  const validation = await store.validateRevision(draft.revision);
  assert.equal(validation.valid, true);
  assert.equal(validation.publishable, true);
  let runtime = createStageRuntimeEnvelope(await store.getState(), await store.getRuntimeConfig(), contract);
  assert.equal(runtime.policy.configRevision, "stages-admin-v1");
  assert.deepEqual(runtime.policy.stages, []);
  await store.publish({ revision: draft.revision, expectedActiveRevision: seed.revision });
  runtime = createStageRuntimeEnvelope(await store.getState(), await store.getRuntimeConfig(), contract);
  assert.equal(runtime.activeRevision, draft.revision);
  assert.equal(runtime.applyBoundary, "new-session");
  assert.equal(runtime.policy.stages[0].enemyBudget, 88);
  await store.rollback({ targetRevision: seed.revision, expectedActiveRevision: draft.revision });
  runtime = createStageRuntimeEnvelope(await store.getState(), await store.getRuntimeConfig(), contract);
  assert.equal(runtime.activeRevision, seed.revision);
  assert.deepEqual(runtime.policy.stages, []);
});

test("B06.6 invalid Stage authoring cannot create a revision", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  for (const stages of [
    [{stage:0,enemyBudget:40}],
    [{stage:12,role:"boss"}],
    [{stage:12,enemyBudget:40},{stage:12,enemyBudget:41}],
    [{stage:12,eliteChance:1.1}],
  ]) {
    const config = structuredClone(active.config);
    config.content.stages = { configRevision:"stages-invalid", stages };
    await assert.rejects(store.createRevision({ baseRevision: active.revision, config }), AdminValidationError);
  }
});
