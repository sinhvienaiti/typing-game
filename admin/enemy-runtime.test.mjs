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
    { content: { enemies: { configRevision: "enemies-admin-test", projectileMode: "off", enemies: { "rainbow-dart": { minStage: 25 } } } } },
    contract,
  );
  assert.deepEqual(envelope, {
    protocolVersion: 1,
    activeRevision: "r8",
    applyBoundary: "new-session",
    policy: {
      configRevision: "enemies-admin-test",
      projectileMode: "off",
      enemies: { "rainbow-dart": { minStage: 25 } },
    },
  });
});

test("uses the safe adaptive Enemy policy for revisions without Enemy config", () => {
  const envelope = createEnemyRuntimeEnvelope({ activeRevision: "legacy" }, {}, contract);
  assert.equal(envelope.policy.configRevision, "enemies-admin-v1");
  assert.equal(envelope.policy.projectileMode, "auto");
  assert.deepEqual(envelope.policy.enemies, {});
});

test("normalizes older Enemy revisions to Admin-owned adaptive projectiles", () => {
  const envelope = createEnemyRuntimeEnvelope(
    { activeRevision: "legacy-enemies" },
    { content: { enemies: { configRevision: "enemies-admin-v1", enemies: { "rainbow-scout": { minStage: 5 } } } } },
    contract,
  );
  assert.equal(envelope.policy.projectileMode, "auto");
  assert.deepEqual(envelope.policy.enemies, { "rainbow-scout": { minStage: 5 } });
});
