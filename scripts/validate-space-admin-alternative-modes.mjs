import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-alternative-modes.v1.json"));
const [authoritySource, duelProtocolSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/authority.ts"), read("games/space-typing/src/duel/protocol.ts"),
  read("portal/src/admin/space-typing-alternative-modes-phase-b.ts"), read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"), read("admin/server.mjs"), read("admin/space-typing-phase-b-map.v1.json"),
]);

const modes = contract.alternativeModes;
assert.equal(contract.contractRevision, "space-typing-admin-alternative-modes-v1");
assert.equal(contract.capability, "alternative-modes.read");
assert.equal(modes.mode, "runtime-backed-readonly");
assert.equal(modes.runtimeOwner, "AlternativeMatchRuntime");
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

const runtimeSources = await Promise.all(modes.runtimeSources.map((path) => read(`games/space-typing/${path}`)));
const combinedRuntime = runtimeSources.join("\n");
for (const token of ["reflex", "word-chain", "AlternativeMatchRuntime", "snapshot-v1"]) assert(combinedRuntime.includes(token), `Expected Alternative Mode runtime evidence missing: ${token}`);
const registrySource = runtimeSources[0];
assert(registrySource.includes('const FRIEND_PRACTICE = ["friend", "practice"] as const'), "Alternative modes must remain scoped to Friend/Practice.");
assert(registrySource.includes("rankedEligible: false"), "Alternative modes must remain fail-closed for Ranked.");
assert(runtimeSources[1].includes("export class AlternativeMatchRuntime"), "Canonical AlternativeMatchRuntime owner is missing.");
assert(runtimeSources[1].includes("static restore("), "Alternative mode reconnect/restore support is missing.");
assert(runtimeSources[1].includes("snapshot(): AlternativeMatchSnapshotV1"), "Alternative mode snapshot persistence is missing.");
assert(authoritySource.includes('mode: "friend" | "ranked" | "practice"'), "Canonical Duel match-mode union changed; re-audit Alternative Modes.");
for (const symbol of ["CREATE_ROOM", "JOIN_ROOM", "QUEUE_RANKED", "INTENT"]) assert(duelProtocolSource.includes(symbol), `Duel protocol evidence missing: ${symbol}`);

// A12 keeps availability/admission administrator-facing while hiding technical ownership evidence under Advanced.
assert(uiSource.includes("/api/admin/space-typing/alternative-modes/contract"), "Alternative Modes UI must read child runtime contract");
assert(uiSource.includes("RUNTIME-BACKED"), "Alternative Modes UI must expose production availability");
assert(uiSource.includes("RANKED FAIL-CLOSED"), "Alternative Modes UI must make Ranked admission closure explicit");
assert(uiSource.includes("Production capability"), "Alternative Modes A12 UI must present each real runtime mode as a capability card");
assert(uiSource.includes("Admission Policy"), "Alternative Modes A12 UI must make match-type admission clear");
assert(uiSource.includes("Advanced runtime ownership details"), "low-level runtime ownership must be progressively disclosed");
assert(!uiSource.includes("api.createRevision"), "Alternative Modes UI must not create synthetic revisions");
assert(!uiSource.includes("api.publish"), "Alternative Modes UI must not publish synthetic mode policy");
assert(!uiSource.includes('type = "range"'), "Alternative Modes UI must not expose prototype tuning sliders");
assert(!uiSource.includes("reactionWindowMs"), "unsupported Reflex tuning must not become a control");
assert(!uiSource.includes("chainRule"), "unsupported Word Chain tuning must not become a control");

assert(routerSource.includes("renderPhaseBAlternativeModes"), "Alternative Modes renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/alternative-modes`"), "Alternative Modes route is not wired into Phase B");
assert(shellSource.includes("const phaseB = renderPhaseBAdminScreen(path, this.navigate);"), "Space Typing shell must invoke Phase B router");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Alternative Modes/mock renderer must remain unreachable");
assert(serverSource.includes("/api/admin/space-typing/alternative-modes/contract"), "Admin server Alternative Modes endpoint is missing");
const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/alternative-modes");
assert.equal(row?.domain, "runtime.alternativeModes");
assert.equal(row?.persistence, "child-duel-alternative-match-snapshot-v1");
assert.equal(row?.applyBoundary, "none");
for (const unsupported of ["reactionWindowMs", "roundDamage", "challengePool", "botReactionMs", "practiceEnabled", "friendRoomEnabled", "rankedEnabled", "beatWindowMs", "penaltyDamage", "lexicon", "chainRule"]) {
  assert(modes.unsupportedAdminMockFields.includes(unsupported), `Alternative Modes unsupported mock field missing: ${unsupported}`);
}

console.log("Space Typing A12 Alternative Modes validation passed: real Friend/Practice capabilities are visible, Ranked stays fail-closed, and unsupported tuning remains closed.");
