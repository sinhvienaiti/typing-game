import test from "node:test";
import assert from "node:assert/strict";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { runWorldRegistryPreview } from "./world-registry-preview.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = { worlds:{count:50,previewProtocol:{version:1,command:"pnpm worlds:admin-preview"}} };

test("canonical World Admin preview bridge returns gameplay-backed child view", async () => {
  const preview = await runWorldRegistryPreview({
    rootDir,
    contract,
    policy:{configRevision:"worlds-parent-preview",worlds:{"world-01":{enemyRoster:["rainbow-dart"]}}},
  });
  assert.equal(preview.configRevision,"worlds-parent-preview");
  assert.equal(preview.worlds.length,50);
  const world=preview.worlds.find((item)=>item.id==="world-01");
  assert.deepEqual(world.enemyRoster,["rainbow-dart"]);
  assert.equal(world.sampleEnemyId,"rainbow-dart");
  assert.equal(world.galaxy,1);
  assert.equal(world.stageStart,1);
  assert.equal(world.stageEnd,20);
  assert.equal(world.overridden,true);
});
