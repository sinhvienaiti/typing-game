// Ticket 234 mutations: switch off one fix step, run both suites, restore bytes.
// Run from the repo root: node docs/codex-queue/234/mutate.mjs
import { createHash } from "node:crypto";
import { spawnSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";

const OUT = "docs/codex-queue/234";
const MUTATIONS = [
  {
    id: "M2-output-types",
    step: "step 2: query/lookup output drops wrongly typed samples",
    file: "shared/learning/query.mjs",
    from: "    if (isLearningSample(projected)) result.push(projected);\n",
    to: "    result.push(projected);\n",
  },
  {
    id: "M3-backup-types",
    step: "step 3: backup import drops wrongly typed samples",
    file: "shared/learning/profile-backup.mjs",
    from: "    record.recentSamples = record.recentSamples.filter(isLearningSample);\n",
    to: "",
  },
];
const SUITES = [
  ["learning", "node", ["--test", "shared/learning/lookup.test.mjs", "shared/learning/profile-backup.test.mjs", "shared/learning/query.test.mjs", "shared/learning/core.test.mjs"]],
  ["portal", "node", ["--test", "portal/tests/learning-bridge.test.mjs", "portal/tests/learning-lookup.test.mjs"]],
];

const sha = (text) => createHash("sha256").update(text).digest("hex");
const count = (log, key) => Number(log.match(new RegExp(`^ℹ ${key} (\\d+)`, "m"))?.[1] ?? NaN);
const failed = (log) => [...log.matchAll(/^✖ (.+?) \([0-9.]+ms\)$/gm)].map((m) => m[1]).filter((name, i, all) => all.indexOf(name) === i && name !== "failing tests:");
const clean = (text) => text.replace(/[ \t]+$/gm, "");

function runSuites(label) {
  const result = {};
  for (const [name, cmd, args] of SUITES) {
    const run = spawnSync(cmd, args, { encoding: "utf8" });
    const log = clean(run.stdout + run.stderr) + `exit: ${run.status}\n`;
    writeFileSync(`${OUT}/${label}-${name}.txt`, log);
    result[name] = { exit: run.status, tests: count(log, "tests"), pass: count(log, "pass"), fail: count(log, "fail"), failed: failed(log) };
  }
  return result;
}

const report = [];
for (const m of MUTATIONS) {
  const original = readFileSync(m.file, "utf8");
  const hash = sha(original);
  if (original.split(m.from).length !== 2) throw new Error(`${m.id}: anchor must occur once`);
  let mutated, restored;
  try {
    writeFileSync(m.file, original.replace(m.from, m.to));
    mutated = runSuites(`${m.id}-mutated`);
  } finally {
    writeFileSync(m.file, original);
  }
  const restoredHash = sha(readFileSync(m.file, "utf8"));
  if (restoredHash !== hash) throw new Error(`${m.id}: restore hash mismatch`);
  restored = runSuites(`${m.id}-restored`);
  report.push({ id: m.id, step: m.step, file: m.file, sha256: hash, restoredSha256: restoredHash, mutated, restored });
}
writeFileSync(`${OUT}/mutation.json`, JSON.stringify(report, null, 2) + "\n");
for (const r of report) {
  console.log(r.id, "mutated", JSON.stringify(Object.fromEntries(Object.entries(r.mutated).map(([k, v]) => [k, `${v.fail} fail / ${v.tests}`]))),
    "restored", JSON.stringify(Object.fromEntries(Object.entries(r.restored).map(([k, v]) => [k, `${v.pass}/${v.tests}`]))), "hash ok");
}
