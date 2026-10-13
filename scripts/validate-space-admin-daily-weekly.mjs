import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const DAILY_WEEKLY_AUDITED_CHILD_SHA = "dbd7348daf23a7e8ef3d804c23205e22f82407f1";
const readChild = (path) => readFile(resolve(childRoot, path), "utf8");
const contract = JSON.parse(await readChild("contracts/space-typing-admin-daily-weekly.v1.json"));
const [page, router, server, phaseMapSource, weeklyRuntime, weeklyAdmin, challengeSource] = await Promise.all([
  readFile(resolve(root, "portal/src/admin/space-typing-daily-weekly-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readChild("src/expansion-v2/weekly-challenge-runtime.ts"),
  readChild("src/expansion-v2/weekly-challenge-admin.ts"),
  readChild("src/expansion-v2/challenge.ts"),
]);
const phaseMap = JSON.parse(phaseMapSource);
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, DAILY_WEEKLY_AUDITED_CHILD_SHA, `Daily / Weekly audit is stale: audited=${DAILY_WEEKLY_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit fixed challenge runtime before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-daily-weekly-v1");
assert.equal(contract.capability, "daily-weekly.read");
assert.equal(contract.route.path, "/admin/space-typing/daily-weekly");
assert.equal(contract.liveOps.mode, "runtime-readonly");

const daily = contract.liveOps.daily;
assert.equal(daily.available, true);
assert.equal(daily.challengeKind, "daily");
assert.equal(daily.cadence, "utc-day");
assert.equal(daily.dayKeyFormat, "YYYY-MM-DD");
assert.equal(daily.seedPolicy, "hash(dayKey|rulesetVersion)");
assert.equal(daily.personalBest, true);
assert.equal(daily.personalGhost, true);
assert.equal(daily.remoteScheduler, false);
assert.equal(daily.remoteLeaderboard, false);
assert.equal(daily.adminMode, "read-only");
assert.equal(daily.writeCapability, false);

const weekly = contract.liveOps.weekly;
assert.equal(weekly.available, true);
assert.equal(weekly.challengeKind, "weekly");
assert.equal(weekly.cadence, "utc-iso-week");
assert.equal(weekly.weekKeyFormat, "YYYY-Www");
assert.equal(weekly.weekKeyOwner, "weeklyChallengeWeekKey(date)");
assert.equal(weekly.seedPolicy, "hash(weekly|weekKey|rulesetVersion)");
assert.equal(weekly.seedOwner, "weeklySeed(weekKey, rulesetVersion)");
assert.equal(weekly.personalBest, true);
assert.equal(weekly.personalGhost, true);
assert.equal(weekly.adminMode, "read-only");
assert.equal(weekly.remoteScheduler, false);
assert.equal(weekly.remoteLeaderboard, false);
assert.equal(weekly.writeCapability, false);
assert.equal(weekly.schedulerControlCapability, false);
assert.equal(weekly.rewardAuthoringCapability, false);
assert.equal(weekly.seedOverrideCapability, false);
assert.deepEqual(weekly.readableState, [
  "weekKey",
  "seed",
  "identityKey",
  "resumeStatus",
  "rewardClaimed",
  "personalBest",
  "ghostPointCount",
  "leaderboardEligible",
]);

assert.equal(contract.liveOps.adminWriteCapability, false);
assert.equal(contract.liveOps.scheduleAuthoringCapability, false);
assert.equal(contract.liveOps.rewardAuthoringCapability, false);
assert.equal(contract.liveOps.publishCapability, false);
assert.equal(contract.liveOps.applyBoundary, "none");

for (const source of contract.liveOps.runtimeSources) {
  const content = await readChild(source);
  assert.ok(content.length > 0, `Daily / Weekly runtime source is empty: ${source}`);
}
assert.match(challengeSource, /export function weeklyChallengeWeekKey/);
assert.match(challengeSource, /export function weeklySeed/);
assert.match(challengeSource, /export function weeklyChallengeIdentity/);
assert.match(weeklyRuntime, /export function weeklyChallengeRunBinding/);
assert.match(weeklyRuntime, /export function weeklyChallengeResumeStatus/);
assert.match(weeklyRuntime, /export function settleWeeklyChallengeProfile/);
assert.match(weeklyRuntime, /export function buildWeeklyChallengeAdminSnapshot/);
assert.match(weeklyAdmin, /WEEKLY_CHALLENGE_ADMIN_MODE = "read-only"/);
assert.match(weeklyAdmin, /canMutate:\s*false/);
assert.match(challengeSource, /daily/);

for (const unsupported of [
  "creating or editing Daily or Weekly schedules",
  "changing deterministic Daily or Weekly seeds",
  "editing player Personal Best or Personal Ghost records",
  "claiming a remote leaderboard or scheduler backend",
  "authoring or publishing Weekly rewards",
  "mutating browser-local player challenge progress",
]) {
  assert.ok(contract.liveOps.unsupportedAdminOperations.includes(unsupported), `Daily / Weekly unsupported boundary missing: ${unsupported}`);
}

assert.match(server, /space-typing-admin-daily-weekly\.v1\.json/);
assert.match(server, /request\.method==="GET"&&url\.pathname==="\/api\/admin\/space-typing\/daily-weekly\/contract"/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(
    !server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/daily-weekly/`),
    `Daily / Weekly Admin service must not expose a fake ${method} mutation endpoint`,
  );
}

assert.match(router, /renderPhaseBDailyWeekly/);
assert.match(router, /\$\{BASE\}\/daily-weekly`\) return renderPhaseBDailyWeekly\(\)/);
assert.match(page, /\/api\/admin\/space-typing\/daily-weekly\/contract/);
assert.match(page, /DAILY · RUNTIME-BACKED/);
assert.match(page, /WEEKLY · RUNTIME-BACKED/);
assert.match(page, /No synthetic live-ops authoring/);
assert.match(page, /No remote scheduler or remote leaderboard/);
assert.match(page, /weekly\.readableState/);
assert.doesNotMatch(page, /WEEKLY · NOT IMPLEMENTED/);
assert.doesNotMatch(page, /Weekly has no canonical runtime implementation/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|method:\s*["'](?:POST|PUT|PATCH|DELETE)["']/);

const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/daily-weekly");
assert.ok(row, "Daily / Weekly Phase B map row is required");
assert.equal(row.domain, "liveOps.dailyWeekly");
assert.equal(row.persistence, "child-expansion-v2-profile-browser-local");
assert.equal(row.applyBoundary, "none");
assert.equal(row.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log(`Space Typing Admin Daily / Weekly mapping: PASS (${childHead.slice(0, 12)} · Daily + Weekly canonical deterministic runtimes, browser-local state, Admin read-only).`);
