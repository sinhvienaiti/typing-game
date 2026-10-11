import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-ranked.v1.json"));
const [rankedSource, authoritySource, serviceSource, querySource, historyAdminSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/ranked.ts"),
  read("games/space-typing/src/duel/authority.ts"),
  read("games/space-typing/server/duel/ranked-service.ts"),
  read("games/space-typing/server/duel/ranked-history-query-service.ts"),
  read("games/space-typing/src/duel/ranked-history-admin.ts"),
  read("portal/src/admin/space-typing-ranked-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const ranked = contract.ranked;
assert.equal(contract.contractRevision, "space-typing-admin-ranked-v1");
assert.equal(contract.capability, "ranked.read");
assert.equal(ranked.mode, "runtime-derived-readonly");
assert.deepEqual(ranked.authorableFields, []);
assert.equal(ranked.writeCapability, false);
assert.equal(ranked.previewCapability, false);
assert.equal(ranked.seasonService, false);
assert.equal(ranked.rewardTableService, false);
assert.equal(ranked.ruleset.id, "ranked-standard-v1");
assert.equal(ranked.rating.base, 1000);
assert.equal(ranked.matchmaking.reconnectGraceMs, 30000);
assert.equal(ranked.history.available, true);
assert.equal(ranked.history.mode, "persisted-authoritative-readonly");
assert.equal(ranked.history.defaultScope, "self");
assert.equal(ranked.history.crossPlayerScope, "authorized-cross-player");
assert.equal(ranked.history.authenticationRequired, true);
assert.equal(ranked.history.crossPlayerAuthorizationRequired, true);
assert.equal(ranked.history.crossPlayerFailClosedWhenUnconfigured, true);
assert.equal(ranked.history.writeCapability, false);

for (const symbol of ["DUEL_RANKED_RULESET", "DUEL_RANKED_BASE_RATING = 1000", "DUEL_RANKED_RECONNECT_GRACE_MS = 30_000"]) {
  assert.ok(rankedSource.includes(symbol), `Ranked runtime evidence missing: ${symbol}`);
}
for (const symbol of ["startRankedMatch", "rankedParticipant", "finishRankedForfeit"]) {
  assert.ok(authoritySource.includes(symbol), `Ranked authority evidence missing: ${symbol}`);
}
assert.match(serviceSource, /DuelRankedService/);
assert.match(historyAdminSource, /DUEL_RANKED_HISTORY_ADMIN_MODE = "read-only"/);
assert.match(historyAdminSource, /canMutate: false/);
for (const symbol of ["UNAUTHENTICATED", "FORBIDDEN", "authorized-cross-player", "authorizeCrossPlayer", "Cross-player Ranked history access is not configured"]) {
  assert.ok(querySource.includes(symbol), `Ranked history authorization evidence missing: ${symbol}`);
}

assert(uiSource.includes("/api/admin/space-typing/ranked/contract"));
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"));
assert(uiSource.includes("HISTORY · AUTHENTICATED"));
assert(uiSource.includes("Fail closed when unconfigured"));
assert(!uiSource.includes("api.createRevision"));
assert(!uiSource.includes("api.publish"));
assert(routerSource.includes("renderPhaseBRanked"));
assert(shellSource.includes("const phaseB = renderPhaseBAdminScreen(path, this.navigate);"));
assert(!shellSource.includes("renderExtendedAdminScreen"));
assert(serverSource.includes("space-typing-admin-ranked.v1.json"));
assert(serverSource.includes("/api/admin/space-typing/ranked/contract"));

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/ranked");
assert.equal(row?.domain, "runtime.ranked");
assert.equal(row?.persistence, "child-duel-server-profile-and-history-store");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log("Space Typing Ranked Admin validation passed: live Ranked policy plus authenticated persisted history are read-only and cross-player access remains fail-closed.");
