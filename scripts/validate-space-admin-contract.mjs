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

assert.equal(child.contractRevision, "space-typing-admin-v1");
assert.equal(child.schemaVersion, 1);
assert.equal(child.gameId, "space-typing");
assert.deepEqual(snapshot, child);

console.log(
  `Space Typing Admin contract OK: ${child.contractRevision} · ${child.worldMusic.worldCount} Worlds`,
);
