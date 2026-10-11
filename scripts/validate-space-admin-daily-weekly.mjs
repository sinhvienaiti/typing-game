import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const DAILY_WEEKLY_AUDITED_CHILD_SHA = "5cc2de2f0a88400ae6531dc05b67b033196126ca";
const readChild = (path) => readFile(resolve(childRoot, path), "utf8");
const contract = JSON.parse(await readChild("contracts/space-typing-admin-daily-weekly.v1.json"));
const [challengeSource, weeklyRuntimeSource, weeklyAdminSource, page, router, server, phaseMapSource] = await Promise.all([
  readChild("src/expansion-v2/challenge.ts"),
  readChild("src/expansion-v2/weekly-challenge-runtime.ts"),
  readChild("src/expansion-v2/weekly-challenge-admin.ts"),
  readFile(resolve(root, "portal/src/admin/space-typing-daily-weekly-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
]);
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, DAILY_WEEKLY_AUDITED_CHILD_SHA, `Daily / Weekly audit is stale: audited=${DAILY_WEEKLY_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit current challenge runtime before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-daily-weekly-v1");
assert.equal(contract.capability, "daily-weekly.read");
assert.equal(contract.liveOps.mode, "runtime-readonly");
assert.equal(contract.liveOps.daily.available, true);
assert.equal(contract.liveOps.daily.challengeKind, "daily");
assert.equal(contract.liveOps.daily.seedPolicy, "hash(dayKey|rulesetVersion)");
assert.equal(contract.liveOps.weekly.available, true);
assert.equal(contract.liveOps.weekly.challengeKind, "weekly");
assert.equal(contract.liveOps.weekly.adminMode, "read-only");
assert.equal(contract.liveOps.weekly.seedOverrideCapability, false);
assert.equal(contract.liveOps.weekly.schedulerControlCapability, false);
assert.equal(contract.liveOps.weekly.rewardAuthoringCapability, false);
assert.equal(contract.liveOps.adminWriteCapability, false);
assert.equal(contract.liveOps.publishCapability, false);

for (const symbol of ["weeklyChallengeWeekKey", "weeklySeed", "weeklyChallengeIdentityKey"]) {
  assert.ok(challengeSource.includes(symbol), `Weekly canonical identity evidence missing: ${symbol}`);
}
for (const symbol of ["weeklyChallengeBindingStatus", "weeklyChallengeResumeStatus", "weeklyChallengeRewardEligible", "weeklyChallengeLeaderboardEligible"]) {
  assert.ok(weeklyRuntimeSource.includes(symbol), `Weekly runtime evidence missing: ${symbol}`);
}
assert.match(weeklyAdminSource, /WEEKLY_CHALLENGE_ADMIN_MODE = "read-only"/);
assert.match(weeklyAdminSource, /canMutate: false/);

assert.match(server, /space-typing-admin-daily-weekly\.v1\.json/);
assert.match(server, /\/api\/admin\/space-typing\/daily-weekly\/contract/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(!server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/daily-weekly/`), `Daily / Weekly Admin service must not expose a fake ${method} mutation endpoint`);
}

assert.match(router, /renderPhaseBDailyWeekly/);
assert.match(page, /WEEKLY · RUNTIME-BACKED/);
assert.match(page, /Weekly Challenge/);
assert.match(page, /No synthetic live-ops authoring/);
assert.doesNotMatch(page, /WEEKLY · NOT IMPLEMENTED|weekly has no canonical runtime/i);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|method:\s*["'](?:POST|PUT|PATCH|DELETE)["']/);

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/daily-weekly");
assert.ok(row, "Daily / Weekly Phase B map row is required");
assert.equal(row.domain, "liveOps.dailyWeekly");
assert.equal(row.persistence, "child-expansion-v2-profile-browser-local");
assert.equal(row.applyBoundary, "none");
assert.equal(row.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log(`Space Typing Admin Daily / Weekly mapping: PASS (${childHead.slice(0, 12)} · Daily + Weekly canonical read-only runtime).`);
