import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root=fileURLToPath(new URL("../",import.meta.url));
const checkerPath=fileURLToPath(new URL("./check-english-content-e11-readiness.mjs",import.meta.url));
const reportPath=fileURLToPath(new URL("../content/english/reports/e11-readiness.json",import.meta.url));

function runChecker() {
  return spawnSync(process.execPath,[checkerPath],{
    cwd:root,
    encoding:"utf8",
    stdio:["ignore","pipe","pipe"],
  });
}

test("E11 readiness report freshness checker",async t=>{
  const original=readFileSync(reportPath,"utf8");
  try {
    await t.test("accepts the committed report when it matches fresh output",()=>{
      const result=runChecker();
      assert.equal(result.status,0,result.stderr||result.stdout);
      assert.match(result.stdout,/\[english-content:e11:check\].*"state":"fresh"/);
      assert.equal(readFileSync(reportPath,"utf8"),original,"checker must leave a fresh committed report unchanged");
    });

    await t.test("rejects a stale committed report and restores the pre-check bytes",()=>{
      const stale=original+" ";
      writeFileSync(reportPath,stale,"utf8");

      const result=runChecker();
      assert.equal(result.status,1,result.stderr||result.stdout);
      assert.match(result.stderr,/E11 readiness report is stale/);
      assert.match(result.stderr,/npm run english-content:e11/);
      assert.equal(readFileSync(reportPath,"utf8"),stale,"checker must restore the report bytes it inspected");
    });
  } finally {
    writeFileSync(reportPath,original,"utf8");
  }
});
