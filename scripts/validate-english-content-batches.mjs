import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import { validateEnglishContentBatchContracts } from "./english-batch-contract-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const schemaDir=path.join(root,"shared","schemas","english-content");
const [commonSchema,batchSchema,manifest]=await Promise.all([
  readJson(path.join(schemaDir,"common.schema.json")),
  readJson(path.join(schemaDir,"batch-manifest.schema.json")),
  readJson(path.join(root,"content","english","batches","manifest.json")),
]);
const {errors,report}=await validateEnglishContentBatchContracts({
  manifest,
  commonSchema,
  batchSchema,
  loadRecordSet:(recordPath)=>readJson(path.join(root,recordPath)),
});

await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(
  path.join(root,"content","english","reports","e10-batch-report.json"),
  stableJson(report),
  "utf8",
);
console.log(JSON.stringify(report,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
