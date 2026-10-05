import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const childPath = new URL(
  "../games/space-typing/contracts/space-typing-admin.v1.json",
  import.meta.url,
);
const snapshotPath = new URL(
  "../portal/src/admin/contracts/space-typing-admin.v1.json",
  import.meta.url,
);

const [child, snapshot] = await Promise.all([
  readFile(childPath, "utf8").then(JSON.parse),
  readFile(snapshotPath, "utf8").then(JSON.parse),
]);

assert.equal(child.contractRevision, "space-typing-admin-v2");
assert.equal(child.schemaVersion, 1);
assert.equal(child.gameId, "space-typing");
assert.deepEqual(snapshot, child);
assert.equal(child.qa.protocolVersion, 1);
assert.equal(child.qa.productionAllowed, false);
assert.equal(child.qa.persistenceTarget, "qa-sandbox");
assert.equal(child.qa.rewardEligibility, "none");
assert.ok(child.capabilities.includes("qa.session.issue"));
assert.ok(child.routes.some((route) => route.id === "qa-session"));

console.log(
  `Space Typing Admin contract OK: ${child.contractRevision} · ${child.worldMusic.worldCount} Worlds · QA sandbox v${child.qa.protocolVersion}`,
);
