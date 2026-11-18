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
      imageAssetVersionId: "media-version.11111111-2222-3333-4444-555555555555",
      reliefAssetVersionId: "media-version.ship-aegis-relief-v7",
      projectileArchetype: "cosmic",
      statBonus: { shield: 16 },
      visual: { silhouette: "fortress", wingSpan: 1.2, engineCount: 2 },
    },
  },
});

test("B06.1 parent validator accepts child-contract-backed ship overrides", () => {
  assert.equal(validateShipPolicy(validPolicy(), contract.ships).configRevision, "ships-admin-test-v1");
});

test("A5.2 parent validator accepts only canonical Media V2 Ship image versions", () => {
  assert.equal(
    validateShipPolicy(validPolicy(), contract.ships).ships.aegis.imageAssetVersionId,
    "media-version.11111111-2222-3333-4444-555555555555",
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { imageAssetVersionId: "/assets/ship.webp" } } }, contract.ships),
    /canonical Media V2 version id/,
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { imageAssetVersionId: "https:\/\/example.test\/ship.webp" } } }, contract.ships),
    /canonical Media V2 version id/,
  );
});

test("A5.4 parent validator accepts only exact Media V2 Ship relief bundle versions", () => {
  assert.equal(
    validateShipPolicy(validPolicy(), contract.ships).ships.aegis.reliefAssetVersionId,
    "media-version.ship-aegis-relief-v7",
  );
  for (const value of [
    "latest",
    "media.ship-aegis-relief",
    "/assets/ships/aegis/model.json",
    "https://example.test/aegis.glb",
  ]) {
    assert.throws(
      () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { reliefAssetVersionId: value } } }, contract.ships),
      /canonical Media V2 version id/,
    );
  }
});

test("A5.3 parent validator accepts only child-contract production projectile recipes", () => {
  assert.equal(
    validateShipPolicy(validPolicy(), contract.ships).ships.aegis.projectileArchetype,
    "cosmic",
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { projectileArchetype: "invented" } } }, contract.ships),
    /canonical production projectile recipe/,
  );
  assert.throws(
    () => validateShipPolicy({ configRevision: "bad", ships: { vanguard: { projectileArchetype: "/assets/projectile.png" } } }, contract.ships),
    /canonical production projectile recipe/,
  );
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