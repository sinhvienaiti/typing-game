import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { parseShipRegistryPreviewOutput, runShipRegistryPreview } from "./ship-registry-preview.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = JSON.parse(
  await readFile(resolve(rootDir, "games/space-typing/contracts/space-typing-admin.v1.json"), "utf8"),
);

test("Ships preview parser ignores package-manager stdout preamble", () => {
  const payload = parseShipRegistryPreviewOutput(
    "? verifying dependencies...\n{\n  \"protocolVersion\": 1,\n  \"configRevision\": \"x\",\n  \"ships\": []\n}\n",
  );
  assert.equal(payload.protocolVersion, 1);
  assert.equal(payload.configRevision, "x");
  assert.throws(
    () => parseShipRegistryPreviewOutput("verification only, no protocol payload"),
    /payload marker not found/,
  );
});

test("parent Admin invokes the child canonical 11-ship preview protocol", async () => {
  const preview = await runShipRegistryPreview({ rootDir, contract });
  assert.equal(preview.protocolVersion, 1);
  assert.equal(preview.ships.length, 11);
  assert.deepEqual(
    preview.ships.map((ship) => ship.id),
    contract.ships.ids,
  );
  assert.equal(preview.ships[0].assetId, "player-ship-vanguard");
});

test("parent authored overrides are merged by child runtime sources", async () => {
  const preview = await runShipRegistryPreview({
    rootDir,
    contract,
    policy: {
      configRevision: "parent-ships-test-v1",
      ships: {
        aegis: {
          unlockStage: 120,
          statBonus: { shield: 16 },
          visual: { wingSpan: 1.2, engineCount: 2 },
        },
      },
    },
  });
  const aegis = preview.ships.find((ship) => ship.id === "aegis");
  assert.equal(preview.configRevision, "parent-ships-test-v1");
  assert.equal(aegis.unlockStage, 120);
  assert.equal(aegis.statBonus.shield, 16);
  assert.equal(aegis.statBonus.armor, 8);
  assert.equal(aegis.visual.wingSpan, 1.2);
  assert.equal(aegis.overridden, true);
});

test("child canonical preview rejects non-authorable player-state fields", async () => {
  await assert.rejects(
    runShipRegistryPreview({
      rootDir,
      contract,
      policy: {
        configRevision: "invalid-parent-policy",
        ships: { vanguard: { selected: true } },
      },
    }),
    /not authorable/,
  );
});
