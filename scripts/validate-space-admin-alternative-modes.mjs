import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-alternative-modes.v1.json"));
const [registrySource, runtimeSource, protocolSource, serviceSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/alternative-modes.ts"),
  read("games/space-typing/src/duel/alternative-match-runtime.ts"),
  read("games/space-typing/src/duel/alternative-protocol.ts"),
  read("games/space-typing/server/duel/alternative-service.ts"),
  read("portal/src/admin/space-typing-alternative-modes-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const modes = contract.alternativeModes;
assert.equal(contract.contractRevision, "space-typing-admin-alternative-modes-v1");
assert.equal(contract.capability, "alternative-modes.read");
assert.equal(modes.mode, "runtime-backed-readonly");
assert.deepEqual(modes.runtimeImplementations, { reflex: true, "word-chain": true });
assert.deepEqual(modes.authorableFields, []);
assert.equal(modes.writeCapability, false);
assert.equal(modes.previewCapability, false);
assert.equal(modes.rankedAdmissionCapability, false);
assert.equal(modes.applyBoundary, "none");
assert.deepEqual(modes.implementations.map((entry) => entry.id), ["reflex", "word-chain"]);
for (const entry of modes.implementations) {
  assert.equal(entry.available, true);
  assert.deepEqual(entry.supportedMatchTypes, ["friend", "practice"]);
  assert.equal(entry.rankedEligible, false);
  assert.equal(entry.persistence, "snapshot-v1");
  assert.equal(entry.reconnect, true);
}

for (const symbol of ["ALTERNATIVE_MODE_REGISTRY", 'reflex:', '"word-chain":', "AlternativeMatchRuntime", 'rankedEligible: false']) {
  assert.ok(`${registrySource}\n${runtimeSource}`.includes(symbol), `Alternative Mode runtime evidence missing: ${symbol}`);
}
assert.match(registrySource, /supportedMatchTypes:\s*FRIEND_PRACTICE/);
assert.match(registrySource, /does not support.*ranked remains fail-closed/i);
assert.match(protocolSource, /AlternativeModeId/);
assert.match(serviceSource, /Alternative/);

assert(uiSource.includes("/api/admin/space-typing/alternative-modes/contract"));
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"));
assert(uiSource.includes("RANKED · FAIL CLOSED"));
assert(!uiSource.includes("REFLEX / WORD CHAIN NOT CONNECTED"));
assert(!uiSource.includes("api.createRevision"));
assert(!uiSource.includes("api.publish"));
assert(!uiSource.includes('type = "range"'));

assert(routerSource.includes("renderPhaseBAlternativeModes"));
assert(routerSource.includes("`${BASE}/alternative-modes`"));
assert(shellSource.includes("const phaseB = renderPhaseBAdminScreen(path, this.navigate);"));
assert(shellSource.includes("if (phaseB !== null) return phaseB;"));
assert(!shellSource.includes("renderExtendedAdminScreen"));
assert(serverSource.includes("space-typing-admin-alternative-modes.v1.json"));
assert(serverSource.includes("/api/admin/space-typing/alternative-modes/contract"));

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/alternative-modes");
assert.equal(row?.domain, "runtime.alternativeModes");
assert.equal(row?.persistence, "child-duel-alternative-snapshot-v1");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log("Space Typing Alternative Modes Admin validation passed: Reflex/Word Chain are real Friend/Practice runtimes, Ranked remains fail-closed, and Admin authoring remains closed.");
