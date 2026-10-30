import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { validateEnglishContentBatchContracts } from "./english-batch-contract-core.mjs";
import { registerMultiwozDialogueBatchManifest } from "./multiwoz-batch-registration-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const defaults={
  packetPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-review.json"),
  intakePath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-intake.json"),
  handoffPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-editorial-handoff.json"),
  authoringPath:null,
  proposalPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-batch-proposal.json"),
  manifestPath:path.join(root,"content","english","batches","manifest.json"),
  write:false,
};

export function parseArgs(argv) {
  const options={...defaults};
  for (let index=0;index<argv.length;index++) {
    const raw=argv[index];
    if (raw==="--") continue;
    if (raw==="--write") {
      options.write=true;
      continue;
    }
    const equal=raw.indexOf("=");
    const flag=equal<0?raw:raw.slice(0,equal);
    const inlineValue=equal<0?null:raw.slice(equal+1);
    const takeValue=()=>{
      if (inlineValue!==null) return inlineValue;
      const value=argv[index+1];
      if (!value||value.startsWith("--")) throw new Error(flag+" requires a value");
      index++;
      return value;
    };
    if (flag==="--packet") options.packetPath=path.resolve(root,takeValue());
    else if (flag==="--intake") options.intakePath=path.resolve(root,takeValue());
    else if (flag==="--handoff") options.handoffPath=path.resolve(root,takeValue());
    else if (flag==="--authoring") options.authoringPath=path.resolve(root,takeValue());
    else if (flag==="--proposal") options.proposalPath=path.resolve(root,takeValue());
    else if (flag==="--manifest") options.manifestPath=path.resolve(root,takeValue());
    else throw new Error("Unknown argument: "+raw);
  }
  return options;
}

function resolveAuthoringPath(proposal,overridePath) {
  const proposed=proposal?.authoringPath;
  if (overridePath) return overridePath;
  if (typeof proposed!=="string"||proposed.trim()==="") {
    throw new TypeError("proposal authoringPath must be a non-empty string");
  }
  const resolved=path.resolve(root,proposed);
  const relative=path.relative(root,resolved).replaceAll(path.sep,"/");
  if (!relative.startsWith("content/english/sentences/")||relative.includes("../")) {
    throw new TypeError("proposal authoringPath must stay under content/english/sentences/");
  }
  return resolved;
}

export async function validateProspectiveRegistration({manifest,authoring,proposal}) {
  const schemaDir=path.join(root,"shared","schemas","english-content");
  const [commonSchema,batchSchema]=await Promise.all([
    readJson(path.join(schemaDir,"common.schema.json")),
    readJson(path.join(schemaDir,"batch-manifest.schema.json")),
  ]);
  const proposedAuthoringPath=proposal.authoringPath;
  const {errors,report}=await validateEnglishContentBatchContracts({
    manifest,
    commonSchema,
    batchSchema,
    loadRecordSet:(recordPath)=>recordPath===proposedAuthoringPath
      ?authoring
      :readJson(path.join(root,recordPath)),
  });
  if (errors.length) {
    throw new Error("Prospective E10 batch contract validation failed:\n"+errors.join("\n"));
  }
  return report;
}

export async function main(argv=process.argv.slice(2)) {
  const options=parseArgs(argv);
  const [manifest,packet,intake,handoff,proposal,pin]=await Promise.all([
    readJson(options.manifestPath),
    readJson(options.packetPath),
    readJson(options.intakePath),
    readJson(options.handoffPath),
    readJson(options.proposalPath),
    readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json")),
  ]);
  const authoringPath=resolveAuthoringPath(proposal,options.authoringPath);
  const authoring=await readJson(authoringPath);
  const result=registerMultiwozDialogueBatchManifest({
    manifest,
    authoring,
    proposal,
    handoff,
    packet,
    intake,
    pin,
  });
  const contractReport=await validateProspectiveRegistration({
    manifest:result.manifest,
    authoring,
    proposal,
  });

  let wrote=false;
  if (options.write&&result.status==="registered") {
    const nextBytes=JSON.stringify(result.manifest,null,2)+"\n";
    await fs.writeFile(options.manifestPath,nextBytes,"utf8");
    wrote=true;
  }

  console.log("E11 MultiWOZ batch registration:",JSON.stringify({
    mode:options.write?"write":"dry-run",
    status:result.status,
    batchId:result.batchId,
    recordCount:result.recordCount,
    authoringPath:path.relative(root,authoringPath).replaceAll(path.sep,"/"),
    authoringDigest:result.authoringDigest,
    reviewDecisions:result.reviewDecisions,
    runtimePublication:result.runtimePublication,
    e10ContractRecords:contractReport.totals.records,
    manifest:path.relative(root,options.manifestPath).replaceAll(path.sep,"/"),
    wrote,
  }));
}

const invoked=process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url);
if (invoked) await main();
