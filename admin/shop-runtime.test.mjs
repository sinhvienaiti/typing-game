import test from "node:test";
import assert from "node:assert/strict";
import {
  SHOP_RUNTIME_APPLY_BOUNDARY,
  createShopRuntimeEnvelope,
} from "./shop-runtime.mjs";

test("Shop runtime envelope publishes only the active Shop policy", () => {
  const policy = { schemaVersion: 1, configRevision: "shop-r2" };
  const envelope = createShopRuntimeEnvelope(
    { activeRevision: "r-active" },
    { economy: { shop: policy } },
  );
  assert.deepEqual(envelope, {
    applyBoundary: SHOP_RUNTIME_APPLY_BOUNDARY,
    activeRevision: "r-active",
    policy,
  });
});

test("Shop runtime envelope keeps migration-safe null policy when no Shop config is published", () => {
  assert.deepEqual(createShopRuntimeEnvelope({ activeRevision: "seed-v1" }, {}), {
    applyBoundary: SHOP_RUNTIME_APPLY_BOUNDARY,
    activeRevision: "seed-v1",
    policy: null,
  });
});

test("Shop runtime envelope never reads a draft-only branch", () => {
  const activePolicy = { schemaVersion: 1, configRevision: "active" };
  const draftPolicy = { schemaVersion: 1, configRevision: "draft" };
  const state = { activeRevision: "r-active", draftRevision: "r-draft" };
  const config = { economy: { shop: activePolicy }, draft: { economy: { shop: draftPolicy } } };
  const envelope = createShopRuntimeEnvelope(state, config);
  assert.equal(envelope.activeRevision, "r-active");
  assert.equal(envelope.policy, activePolicy);
});
