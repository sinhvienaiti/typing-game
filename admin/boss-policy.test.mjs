import test from "node:test";
import assert from "node:assert/strict";
import { BossPolicyValidationError, validateBossPolicy } from "./boss-policy.mjs";

const contract = { ids: ["tyrant-g01", "warden-rainbow"], authorableFields: ["name", "title"], constraints: { nameMax: 100, titleMax: 160 } };

test("accepts canonical Boss identity overrides", () => {
  assert.equal(validateBossPolicy({ configRevision:"bosses-test", bosses:{ "tyrant-g01":{ name:"Nova", title:"The First" } } }, contract).configRevision, "bosses-test");
});

test("accepts empty Boss overrides", () => assert.doesNotThrow(() => validateBossPolicy({ configRevision:"bosses-test", bosses:{} }, contract)));

test("rejects unknown IDs and unsupported combat fields", () => {
  assert.throws(() => validateBossPolicy({ configRevision:"bosses-test", bosses:{ unknown:{name:"X"} } }, contract), BossPolicyValidationError);
  assert.throws(() => validateBossPolicy({ configRevision:"bosses-test", bosses:{ "tyrant-g01":{hp:999} } }, contract), /not authorable/);
});

test("rejects blank and oversized identity text", () => {
  assert.throws(() => validateBossPolicy({ configRevision:"bosses-test", bosses:{ "tyrant-g01":{name:" "} } }, contract), /non-empty/);
  assert.throws(() => validateBossPolicy({ configRevision:"bosses-test", bosses:{ "tyrant-g01":{title:"x".repeat(161)} } }, contract), /160/);
});
