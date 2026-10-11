import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-alternative-modes.v1.json"));
const [authoritySource, duelProtocolSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/authority.ts"),
  read("games/space-typing/src/duel/protocol.ts"),
  read("portal/src/admin/space-typing-alternative-modes-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const modes = contract.alternativeModes;
assert.equal(contract.contractRevision, "space-typing-admin-alternative-modes-v1");
assert.equal(contract.capability, "alternative-modes.read");
assert.deepEqual(contract.route, { id: "alternative-modes", path: "/admin/space-typing/alternative-modes", label: "Alternative Modes" });
assert.equal(modes.mode, "runtime-backed-readonly");
assert.equal(modes.runtimeOwner, "AlternativeMatchRuntime");
assert.deepEqual(modes.runtimeSources, [
  "src/duel/alternative-modes.ts",
  "src/duel/alternative-match-runtime.ts",
  "src/duel/alternative-protocol.ts",
  "server/duel/alternative-service.ts",
  "server/duel/alternative-coordinator.ts",
]);
assert.deepEqual(modes.supportedDuelMatchModes, ["friend", "ranked", "practice"]);
assert.deepEqual(modes.requestedPrototypeModes, ["reflex", "word-chain"]);
assert.deepEqual(modes.runtimeImplementations, { reflex: true, "word-chain": true });
assert.deepEqual(modes.implementations, [
  { id: "reflex", available: true, supportedMatchTypes: ["friend", "practice"], rankedEligible: false, persistence: "snapshot-v1", reconnect: true },
  { id: "word-chain", available: true, supportedMatchTypes: ["friend", "practice"], rankedEligible: false, persistence: "snapshot-v1", reconnect: true },
]);
assert.deepEqual(modes.authorableFields, []);
assert.equal(modes.writeCapability, false);
assert.equal(modes.previewCapability, false);
assert.equal(modes.rankedAdmissionCapability, false);
assert.equal(modes.persistenceOwner, "AlternativeMatchRuntime snapshot-v1");
assert.equal(modes.applyBoundary, "none");

const runtimeSources = await Promise.all(modes.runtimeSources.map((path) => read(`games/space-typing/${path}`)));
const combinedRuntime = runtimeSources.join("\n");
for (const token of ["reflex", "word-chain", "AlternativeMatchRuntime", "snapshot-v1"]) {
  assert(combinedRuntime.includes(token), `Expected canonical Alternative Mode runtime evidence missing: ${token}`);
}
const registrySource = runtimeSources[0];
assert(registrySource.includes('const FRIEND_PRACTICE = ["friend", "practice"] as const'), "Alternative modes must remain scoped to Friend/Practice.");
assert(registrySource.includes("rankedEligible: false"), "Alternative modes must remain fail-closed for Ranked.");
assert(registrySource.includes('runtimeOwner: "AlternativeMatchRuntime"'), "Alternative mode runtime owner changed; re-audit required.");
const runtimeSource = runtimeSources[1];
assert(runtimeSource.includes("export class AlternativeMatchRuntime"), "Canonical AlternativeMatchRuntime owner is missing.");
assert(runtimeSource.includes("static restore("), "Alternative mode reconnect/restore support is missing.");
assert(runtimeSource.includes("snapshot(): AlternativeMatchSnapshotV1"), "Alternative mode snapshot persistence is missing.");
const alternativeProtocolSource = runtimeSources[2];
assert(alternativeProtocolSource.includes('type: "MODE_INPUT"'), "Alternative mode wire input is missing.");
assert(alternativeProtocolSource.includes('mode: "reflex"'), "Reflex protocol support is missing.");
assert(alternativeProtocolSource.includes('mode: "word-chain"'), "Word Chain protocol support is missing.");
assert(authoritySource.includes('mode: "friend" | "ranked" | "practice"'), "Canonical Duel match-mode union changed; re-audit Alternative Modes.");
for (const symbol of ["CREATE_ROOM", "JOIN_ROOM", "QUEUE_RANKED", "INTENT"]) assert(duelProtocolSource.includes(symbol), `Duel protocol evidence missing: ${symbol}`);

assert(uiSource.includes("/api/admin/space-typing/alternative-modes/contract"), "Alternative Modes UI must read the child runtime contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Alternative Modes UI must expose runtime-backed read-only ownership");
assert(uiSource.includes("RANKED FAIL-CLOSED"), "Alternative Modes UI must make Ranked admission closure explicit");
assert(uiSource.includes("AlternativeMatchRuntime"), "Alternative Modes UI must expose the canonical runtime owner");
assert(!uiSource.includes("api.createRevision"), "Alternative Modes UI must not create synthetic revisions");
assert(!uiSource.includes("api.publish"), "Alternative Modes UI must not publish synthetic mode policy");
assert(!uiSource.includes('type = "range"'), "Alternative Modes read-only screen must not expose prototype tuning sliders");

assert(routerSource.includes("renderPhaseBAlternativeModes"), "Alternative Modes renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/alternative-modes`"), "Alternative Modes route is not wired into Phase B");
const phaseBCall = "const phaseB = renderPhaseBAdminScreen(path, this.navigate);";
assert(shellSource.includes(phaseBCall), "Space Typing shell must invoke the Phase B router");
assert(shellSource.includes("if (phaseB !== null) return phaseB;"), "Space Typing shell must return the canonical Phase B renderer");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Alternative Modes/mock renderer must not remain reachable from the production shell");
assert(shellSource.includes("return this.renderUnknown(path);"), "Unknown Admin routes must terminate at the explicit unknown-route guard");
assert(serverSource.includes("space-typing-admin-alternative-modes.v1.json"), "Admin server must load Alternative Modes contract from pinned child");
assert(serverSource.includes("/api/admin/space-typing/alternative-modes/contract"), "Admin server Alternative Modes endpoint is missing");

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/alternative-modes");
assert.equal(row?.domain, "runtime.alternativeModes");
assert.equal(row?.persistence, "child-duel-alternative-match-snapshot-v1");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

for (const unsupported of [
  "reactionWindowMs", "roundDamage", "challengePool", "botReactionMs",
  "practiceEnabled", "friendRoomEnabled", "rankedEnabled", "beatWindowMs",
  "penaltyDamage", "lexicon", "chainRule",
]) assert(modes.unsupportedAdminMockFields.includes(unsupported), `Alternative Modes unsupported mock field missing: ${unsupported}`);

console.log("Space Typing Alternative Modes Admin validation passed: Reflex/Word Chain are runtime-backed for Friend/Practice, Ranked remains fail-closed, and Admin authoring stays closed.");
