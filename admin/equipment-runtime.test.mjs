import test from "node:test";
import assert from "node:assert/strict";
import {
  createEquipmentRuntimeEnvelope,
  EQUIPMENT_RUNTIME_APPLY_BOUNDARY,
} from "./equipment-runtime.mjs";

test("Equipment runtime exposes only the active published policy at the new-session boundary", () => {
  const envelope = createEquipmentRuntimeEnvelope(
    { activeRevision: "rev-active" },
    {
      content: {
        equipment: {
          configRevision: "equipment-admin-v2",
          equipment: {
            "arc-projector-mk2": { name: "Admin Arc" },
          },
        },
      },
    },
  );

  assert.equal(envelope.applyBoundary, EQUIPMENT_RUNTIME_APPLY_BOUNDARY);
  assert.equal(envelope.activeRevision, "rev-active");
  assert.deepEqual(envelope.policy, {
    configRevision: "equipment-admin-v2",
    equipment: {
      "arc-projector-mk2": { name: "Admin Arc" },
    },
  });
});

test("Equipment runtime falls back to bundled child registry when no policy was published", () => {
  const envelope = createEquipmentRuntimeEnvelope(
    { activeRevision: "seed-v1" },
    { content: {} },
  );

  assert.equal(envelope.applyBoundary, "new-session");
  assert.equal(envelope.activeRevision, "seed-v1");
  assert.equal(envelope.policy, null);
});
