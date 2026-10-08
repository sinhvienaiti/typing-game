import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const DAILY_WEEKLY_AUDITED_CHILD_SHA = "8128a2a5a7713fff80cd1286b607de6a3e7190f7";
const contract = JSON.parse(await readFile(resolve(childRoot, "contracts/space-typing-admin-daily-weekly.v1.json"), "utf8"));
const page = await readFile(resolve(root, "portal/src/admin/space-typing-daily-weekly-phase-b.ts"), "utf8");
const router = await readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8");
const server = await readFile(resolve(root, "admin/server.mjs"), "utf8");
const phaseMap = JSON.parse(await readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"));
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, DAILY_WEEKLY_AUDITED_CHILD_SHA, `Daily / Weekly audit is stale: audited=${DAILY_WEEKLY_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit fixed challenge runtime before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-daily-weekly-v1");
assert.equal(contract.capability, "daily-weekly.read");
assert.equal(contract.route.path, "/admin/space-typing/daily-weekly");
assert.equal(contract.liveOps.mode, "runtime-partial-readonly");
assert.equal(contract.liveOps.daily.available, true);
assert.equal(contract.liveOps.daily.challengeKind, "daily");
assert.equal(contract.liveOps.daily.cadence, "utc-day");
assert.equal(contract.liveOps.daily.seedPolicy, "hash(dayKey|rulesetVersion)");
assert.equal(contract.liveOps.daily.personalBest, true);
assert.equal(contract.liveOps.daily.personalGhost, true);
assert.equal(contract.liveOps.daily.remoteScheduler, false);
assert.equal(contract.liveOps.daily.remoteLeaderboard, false);
assert.equal(contract.liveOps.weekly.available, false);
assert.match(contract.liveOps.weekly.reason, /No canonical weekly challenge identity/i);
assert.equal(contract.liveOps.adminWriteCapability, false);
assert.equal(contract.liveOps.scheduleAuthoringCapability, false);
assert.equal(contract.liveOps.rewardAuthoringCapability, false);
assert.equal(contract.liveOps.publishCapability, false);
assert.equal(contract.liveOps.applyBoundary, "none");

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
assert.match(page, /WEEKLY · NOT IMPLEMENTED/);
assert.match(page, /No synthetic live-ops authoring/);
assert.match(page, /No remote scheduler or remote leaderboard/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|method:\s*["'](?:POST|PUT|PATCH|DELETE)["']/);

const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/daily-weekly");
assert.ok(row, "Daily / Weekly Phase B map row is required");
assert.equal(row.domain, "liveOps.dailyWeekly");
assert.equal(row.persistence, "child-expansion-v2-profile-browser-local");
assert.equal(row.applyBoundary, "none");
assert.equal(row.status, "phase-b-ui-wired-runtime-partial-readonly");

console.log(`Space Typing Admin Daily / Weekly mapping: PASS (${childHead.slice(0, 12)} · Daily canonical UTC challenge + Weekly explicit absence).`);
