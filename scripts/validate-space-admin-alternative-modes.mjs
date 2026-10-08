import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-alternative-modes.v1.json"));
const [protocolSource, roomSource, roomUiSource, authoritySource, localMatchSource, gameSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/protocol.ts"),
  read("games/space-typing/src/duel/room.ts"),
  read("games/space-typing/src/duel/room-ui.ts"),
  read("games/space-typing/src/duel/authority.ts"),
  read("games/space-typing/src/duel/local-match.ts"),
  read("games/space-typing/src/Game.ts"),
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
assert.equal(modes.mode, "runtime-absence-diagnostic");
assert.deepEqual(modes.supportedDuelMatchModes, ["friend", "ranked", "practice"]);
assert.deepEqual(modes.requestedPrototypeModes, ["reflex", "word-chain"]);
assert.deepEqual(modes.runtimeImplementations, { reflex: false, "word-chain": false });
assert.deepEqual(modes.authorableFields, []);
assert.equal(modes.writeCapability, false);
assert.equal(modes.previewCapability, false);
assert.equal(modes.rankedAdmissionCapability, false);
assert.equal(modes.persistenceOwner, "none");
assert.equal(modes.applyBoundary, "none");

const canonicalRuntime = [protocolSource, roomSource, roomUiSource, authoritySource, localMatchSource, gameSource].join("\n").toLowerCase();
for (const token of ["reflex", "word-chain", "word chain"]) {
  assert(!canonicalRuntime.includes(token), `Unexpected Alternative Mode runtime evidence found: ${token}`);
}
assert(authoritySource.includes('mode: "friend" | "ranked" | "practice"'), "Canonical Duel match-mode union changed; re-audit Alternative Modes.");
for (const symbol of ["CREATE_ROOM", "JOIN_ROOM", "QUEUE_RANKED", "INTENT"]) assert(protocolSource.includes(symbol), `Duel protocol evidence missing: ${symbol}`);

assert(uiSource.includes("/api/admin/space-typing/alternative-modes/contract"), "Alternative Modes UI must read the child diagnostic contract");
assert(uiSource.includes("RUNTIME AUDIT · READ ONLY"), "Alternative Modes UI must expose read-only audit ownership");
assert(uiSource.includes("REFLEX / WORD CHAIN NOT CONNECTED"), "Alternative Modes UI must expose missing runtime integration");
assert(!uiSource.includes("api.createRevision"), "Alternative Modes UI must not create synthetic revisions");
assert(!uiSource.includes("api.publish"), "Alternative Modes UI must not publish synthetic mode policy");
assert(!uiSource.includes('type = "range"'), "Alternative Modes diagnostic must not expose prototype tuning sliders");

assert(routerSource.includes("renderPhaseBAlternativeModes"), "Alternative Modes renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/alternative-modes`"), "Alternative Modes route is not wired into Phase B");
const phaseBCall = "const phaseB = renderPhaseBAdminScreen(path, this.navigate);";
assert(shellSource.includes(phaseBCall), "Space Typing shell must invoke the Phase B router");
assert(shellSource.includes("if (phaseB !== null) return phaseB;"), "Space Typing shell must return the canonical Phase B renderer");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Alternative Modes/mock renderer must not remain reachable from the production shell");
assert(shellSource.includes("return this.renderUnknown(path);"), "Unknown Admin routes must terminate at the explicit unknown-route guard");
assert(serverSource.includes("space-typing-admin-alternative-modes.v1.json"), "Admin server must load Alternative Modes diagnostic from pinned child");
assert(serverSource.includes("/api/admin/space-typing/alternative-modes/contract"), "Admin server Alternative Modes endpoint is missing");

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/alternative-modes");
assert.equal(row?.domain, "runtime.alternativeModes");
assert.equal(row?.persistence, "none");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-absence-diagnostic");

for (const unsupported of [
  "reactionWindowMs", "roundDamage", "challengePool", "botReactionMs",
  "practiceEnabled", "friendRoomEnabled", "rankedEnabled", "beatWindowMs",
  "penaltyDamage", "lexicon", "chainRule",
]) assert(modes.unsupportedAdminMockFields.includes(unsupported), `Alternative Modes unsupported mock field missing: ${unsupported}`);

console.log("Space Typing Alternative Modes Admin validation passed: Reflex/Word Chain remain explicit runtime-absent diagnostics and no legacy mock authoring route is reachable.");
