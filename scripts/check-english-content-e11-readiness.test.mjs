import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { readEnglishReviewLedger } from "./english-review-core.mjs";
import { readReviewedTatoebaEnglish } from "./english-tatoeba-reviewed.mjs";

const root = fileURLToPath(new URL("../", import.meta.url));
const checkerPath = fileURLToPath(
  new URL("./check-english-content-e11-readiness.mjs", import.meta.url),
);
const reporterPath = fileURLToPath(
  new URL("./report-english-content-e11-readiness.mjs", import.meta.url),
);
const reportPath = fileURLToPath(
  new URL("../content/english/reports/e11-readiness.json", import.meta.url),
);

function runScript(scriptPath) {
  return spawnSync(process.execPath, [scriptPath], {
    cwd: root,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
  });
}

function runChecker() {
  return runScript(checkerPath);
}

test("E11 readiness report freshness checker", async (t) => {
  const original = readFileSync(reportPath, "utf8");

  try {
    const generated = runScript(reporterPath);
    assert.equal(generated.status, 0, generated.stderr || generated.stdout);
    const fresh = readFileSync(reportPath, "utf8");

    await t.test("discovers every English-only batch and counts only its approved records", async () => {
      const manifest = JSON.parse(readFileSync(new URL("../content/english/batches/manifest.json", import.meta.url), "utf8"));
      const ledger = await readEnglishReviewLedger(root);
      const approved = new Set((await readReviewedTatoebaEnglish(root, manifest, ledger))
        .filter(record => record.quality.state === "published").map(record => record.id));
      const target = JSON.parse(fresh).targets.find(row => row.id === "example-sentences");
      for (const batch of manifest.batches.filter(row => /^e11\.tatoeba-english-reviewed-slice-\d+$/u.test(row.id))) {
        const set = batch.recordSets.find(row => row.id === "reviewed-tatoeba-english-examples");
        const records = JSON.parse(readFileSync(new URL("../" + set.path, import.meta.url), "utf8")).records;
        const counts = target.sourceCounts.filter(row => row.path === set.path);
        assert.equal(counts.length, 1, "each registered slice must be counted exactly once");
        assert.equal(counts[0].count, records.filter(row => approved.has(row.id)).length,
          "rejected and pending records must not increase readiness");
      }
    });

    await t.test("accepts a freshly regenerated report", () => {
      const result = runChecker();
      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stdout, /"state":\s*"fresh"/);
      assert.equal(
        readFileSync(reportPath, "utf8"),
        fresh,
        "checker must leave a fresh report unchanged",
      );
    });

    await t.test(
      "rejects a stale report and restores the inspected bytes",
      () => {
        const stale = `${fresh} `;
        writeFileSync(reportPath, stale, "utf8");

        const result = runChecker();
        assert.equal(result.status, 1, result.stderr || result.stdout);
        assert.match(result.stderr, /E11 readiness report is stale/);
        assert.match(result.stderr, /pnpm english-content:e11/);
        assert.equal(
          readFileSync(reportPath, "utf8"),
          stale,
          "checker must restore the report bytes it inspected",
        );
      },
    );
  } finally {
    writeFileSync(reportPath, original, "utf8");
  }
});
