import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { ShipPolicyValidationError, validateShipPolicy } from "./ship-policy.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = JSON.parse(
  await readFile(resolve(rootDir, "games/space-typing/contracts/space-typing-admin.v1.json"), "utf8"),
);

const validPolicy = () => ({
  configRevision: "ships-admin-test-v1",
  ships: {
    aegis: {
      name: "Aegis Mk II",
      unlockStage: 120,
      statBonus: { shield: 16 },
      visual: { silhouette: "fortress", wingSpan: 1.2, engineCount: 2 },
    },
  },
});

test("B06.1 parent validator accepts child-contract-backed ship overrides", () => {
  assert.equal(validateShipPolicy(validPolicy(), contract.ships).configRevision, "ships-admin-test-v1");
});

test("B06.1 parent validator rejects unknown IDs and player-state fields", () => {
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { unknown: { name: "Nope" } } }, contract.ships),
    ShipPolicyValidationError,
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { selected: true } } }, contract.ships),
    /not authorable/,
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { progress: {} } } }, contract.ships),
    /not authorable/,
  );
});

test("B06.1 parent validator uses the published child ranges", () => {
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { aegis: { unlockStage: 1001 } } }, contract.ships),
    /unlockStage/,
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { aegis: { statBonus: { shield: 101 } } } }, contract.ships),
    /shield/,
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { aegis: { visual: { engineCount: 4 } } } }, contract.ships),
    /engineCount/,
  );
});
