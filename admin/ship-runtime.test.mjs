import test from "node:test";
import assert from "node:assert/strict";
import {
  createShipRuntimeEnvelope,
  SHIP_RUNTIME_APPLY_BOUNDARY,
} from "./ship-runtime.mjs";

test("Ships runtime exposes only the active published policy at the new-session boundary", () => {
  const envelope = createShipRuntimeEnvelope(
    { activeRevision: "rev-active" },
    {
      content: {
        ships: {
          configRevision: "ships-admin-v2",
          ships: {
            vanguard: { name: "Admin Vanguard" },
          },
        },
      },
    },
  );

  assert.equal(envelope.applyBoundary, SHIP_RUNTIME_APPLY_BOUNDARY);
  assert.equal(envelope.activeRevision, "rev-active");
  assert.deepEqual(envelope.policy, {
    configRevision: "ships-admin-v2",
    ships: {
      vanguard: { name: "Admin Vanguard" },
    },
  });
});

test("Ships runtime falls back to bundled child registry when no policy was published", () => {
  const envelope = createShipRuntimeEnvelope(
    { activeRevision: "seed-v1" },
    { content: {} },
  );

  assert.equal(envelope.applyBoundary, "new-session");
  assert.equal(envelope.activeRevision, "seed-v1");
  assert.equal(envelope.policy, null);
});
