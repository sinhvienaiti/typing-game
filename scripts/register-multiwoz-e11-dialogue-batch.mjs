import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { registerMultiwozDialogueBatchManifest } from "./multiwoz-batch-registration-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const defaults={
  packetPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-review.json"),
  intakePath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-intake.json"),
  handoffPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-editorial-handoff.json"),
  authoringPath:path.join(root,"content","english","sentences","e11-multiwoz-dialogue-reviewed-slice-01.json"),
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

export async function main(argv=process.argv.slice(2)) {
  const options=parseArgs(argv);
  const [manifest,packet,intake,handoff,authoring,proposal,pin]=await Promise.all([
    readJson(options.manifestPath),
    readJson(options.packetPath),
    readJson(options.intakePath),
    readJson(options.handoffPath),
    readJson(options.authoringPath),
    readJson(options.proposalPath),
    readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json")),
  ]);
  const result=registerMultiwozDialogueBatchManifest({
    manifest,
    authoring,
    proposal,
    handoff,
    packet,
    intake,
    pin,
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
    authoringDigest:result.authoringDigest,
    reviewDecisions:result.reviewDecisions,
    runtimePublication:result.runtimePublication,
    manifest:path.relative(root,options.manifestPath).replaceAll(path.sep,"/"),
    wrote,
  }));
}

const invoked=process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url);
if (invoked) await main();
