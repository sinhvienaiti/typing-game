import fs from "node:fs/promises";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const reportPath=path.join(root,"content","english","reports","e11-runtime-counts.json");
const reporterPath=path.join(root,"scripts","report-english-content-e11-runtime-counts.mjs");

async function readOptional(filePath) {
  try {
    return await fs.readFile(filePath,"utf8");
  } catch (error) {
    if (error?.code==="ENOENT") return null;
    throw error;
  }
}

function countSummary(text) {
  if (text===null) return {};
  const report=JSON.parse(text);
  return report.counts??{};
}

const committed=await readOptional(reportPath);
let generated=null;
let run;
try {
  run=spawnSync(process.execPath,[reporterPath],{
    cwd:root,
    encoding:"utf8",
  });
  generated=await readOptional(reportPath);
} finally {
  if (committed===null) await fs.rm(reportPath,{force:true});
  else await fs.writeFile(reportPath,committed,"utf8");
}

if (run?.stdout) process.stdout.write(run.stdout);
if (run?.stderr) process.stderr.write(run.stderr);
if (run?.error) throw run.error;

const fresh=committed!==null&&generated!==null&&committed===generated;
console.log(JSON.stringify({
  report:"content/english/reports/e11-runtime-counts.json",
  state:fresh?"fresh":"stale",
  counts:countSummary(generated),
},null,2));

if ((run?.status??1)!==0) {
  process.exitCode=run?.status??1;
} else if (!fresh) {
  console.error("E11 runtime count report is stale; run `pnpm english-content:e11:runtime` and commit the regenerated report.");
  process.exitCode=1;
}
