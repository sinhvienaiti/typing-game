import test from "node:test";
import assert from "node:assert/strict";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { runStageConfigPreview } from "./stage-config-preview.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = {
  stages: {
    count: 1000,
    previewProtocol: { version:1, command:"pnpm stages:admin-preview" },
  },
};

test("canonical Stage Admin preview bridge returns the pinned child runtime view", async () => {
  const preview = await runStageConfigPreview({
    rootDir,
    contract,
    policy: { configRevision:"stages-parent-preview", stages:[{stage:37,enemyBudget:88,eliteChance:0.33,modifierSlots:3}] },
  });
  assert.equal(preview.configRevision, "stages-parent-preview");
  assert.equal(preview.stages.length, 1000);
  const stage = preview.stages.find((item) => item.stage === 37);
  assert.equal(stage.enemyBudget, 88);
  assert.equal(stage.eliteChance, 0.33);
  assert.equal(stage.modifierSlots, 3);
  assert.equal(stage.pacingBudget, 88);
  assert.equal(stage.overridden, true);
});
