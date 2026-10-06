import test from "node:test";
import assert from "node:assert/strict";
import { createEnemyRuntimeEnvelope } from "./enemy-runtime.mjs";

const contract = {
  enemies: {
    ids: ["rainbow-scout", "rainbow-dart"],
    authorableFields: ["minStage"],
    constraints: {
      minStage: { min: 1, max: 1000, integer: true },
    },
  },
  applyBoundaries: { enemyPolicy: "new-session" },
};

test("builds a published Enemy runtime envelope", () => {
  const envelope = createEnemyRuntimeEnvelope(
    { activeRevision: "r8" },
    { content: { enemies: { configRevision: "enemies-admin-test", enemies: { "rainbow-dart": { minStage: 25 } } } } },
    contract,
  );
  assert.deepEqual(envelope, {
    protocolVersion: 1,
    activeRevision: "r8",
    applyBoundary: "new-session",
    policy: {
      configRevision: "enemies-admin-test",
      enemies: { "rainbow-dart": { minStage: 25 } },
    },
  });
});

test("uses the safe empty Enemy policy for legacy revisions", () => {
  const envelope = createEnemyRuntimeEnvelope({ activeRevision: "legacy" }, {}, contract);
  assert.equal(envelope.policy.configRevision, "enemies-admin-v1");
  assert.deepEqual(envelope.policy.enemies, {});
});