import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { runWorldMusicPreview } from "./world-music-preview.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = JSON.parse(
  await readFile(resolve(rootDir, "games/space-typing/contracts/space-typing-admin.v1.json"), "utf8"),
);

test("parent Admin invokes the child canonical World Music preview protocol", async () => {
  const preview = await runWorldMusicPreview({ rootDir, contract });
  assert.equal(preview.protocolVersion, 1);
  assert.equal(preview.worlds.length, 50);

  const world10 = preview.worlds.find((world) => world.worldId === "world-10");
  assert.equal(world10.states.world.resolvedFrom, "world-10.generated.world");
  assert.deepEqual(world10.states.world.trackIds, ["world-10-boss-battle-theme-b"]);

  const world11 = preview.worlds.find((world) => world.worldId === "world-11");
  assert.equal(world11.states.normal.resolvedFrom, "world-11.legacy.normal");
  assert.ok(world11.states.normal.badges.includes("LEGACY FALLBACK"));
});

test("published Admin policy is previewed by the same child resolver", async () => {
  const preview = await runWorldMusicPreview({
    rootDir,
    contract,
    publishedPolicy: {
      configRevision: "parent-admin-test-v1",
      worlds: {
        "world-01": {
          normal: {
            kind: "replace",
            trackIds: ["signal-in-the-void"],
            selectionMode: "ordered",
          },
        },
      },
    },
  });
  const world01 = preview.worlds.find((world) => world.worldId === "world-01");
  assert.equal(preview.configRevision, "parent-admin-test-v1");
  assert.equal(world01.states.normal.resolvedFrom, "world-01.published.normal");
  assert.deepEqual(world01.states.normal.badges, ["REPLACED"]);
});
