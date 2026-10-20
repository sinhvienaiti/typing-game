import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import {
  applyMultiwozDialogueEditorialDecisions,
  buildMultiwozEditorialDecisionSet,
  multiwozEditorialDecisionsMatchHandoff,
} from "./multiwoz-editorial-decision-core.mjs";
import { buildMultiwozDialogueEditorialFinalization } from "./multiwoz-editorial-finalization-core.mjs";
import { validateMultiwozDialogueEditorialFinalizationOutputs } from "./multiwoz-editorial-finalization-validation-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const defaults={
  packetPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-review.json"),
  intakePath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-intake.json"),
  handoffPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-editorial-handoff.json"),
  decisionsPath:path.join(root,"content","english","reviews","editorial","multiwoz-e11-dialogue-slice-01","manifest.json"),
  authoringPath:path.join(root,"content","english","sentences","e11-multiwoz-dialogue-reviewed-slice-01.json"),
  proposalPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-batch-proposal.json"),
};

function parseArgs(argv) {
  const options={...defaults};
  for (let index=0;index<argv.length;index++) {
    const raw=argv[index];
    if (raw==="--") continue;
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
    else if (flag==="--decisions") options.decisionsPath=path.resolve(root,takeValue());
    else if (flag==="--authoring-output") options.authoringPath=path.resolve(root,takeValue());
    else if (flag==="--proposal-output") options.proposalPath=path.resolve(root,takeValue());
    else throw new Error("Unknown argument: "+raw);
  }
  return options;
}

export async function main(argv=process.argv.slice(2)) {
  const options=parseArgs(argv);
  const [packet,intake,handoff,decisionManifest,pin]=await Promise.all([
    readJson(options.packetPath),
    readJson(options.intakePath),
    readJson(options.handoffPath),
    readJson(options.decisionsPath),
    readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json")),
  ]);
  const decisionDir=path.dirname(options.decisionsPath);
  const decisionShards=await Promise.all((decisionManifest.shards??[]).map(spec=>readJson(path.join(decisionDir,spec.path))));
  const decisions=buildMultiwozEditorialDecisionSet(decisionManifest,decisionShards);
  if (!multiwozEditorialDecisionsMatchHandoff(decisions,handoff)) {
    console.log("E11 MultiWOZ editorial review:",JSON.stringify({
      state:"decision-set-not-bound-to-current-slice",
      decisionSetId:decisions.decisionSetId,
      currentRecordSetDigest:handoff.recordSetDigest,
      decisionRecordSetDigest:decisions.recordSetDigest,
      runtimePublication:"blocked",
    }));
    return;
  }

  const applied=applyMultiwozDialogueEditorialDecisions(handoff,decisions,packet,intake,pin);
  await fs.writeFile(options.handoffPath,stableJson(applied.handoff),"utf8");
  const authoringRelative=path.relative(root,options.authoringPath).replaceAll(path.sep,"/");
  const finalization=buildMultiwozDialogueEditorialFinalization(applied.handoff,packet,intake,pin,{
    authoringPath:authoringRelative,
  });
  await fs.mkdir(path.dirname(options.authoringPath),{recursive:true});
  await fs.mkdir(path.dirname(options.proposalPath),{recursive:true});
  await fs.writeFile(options.authoringPath,stableJson(finalization.authoring),"utf8");
  await fs.writeFile(options.proposalPath,stableJson(finalization.proposal),"utf8");
  const validation=validateMultiwozDialogueEditorialFinalizationOutputs({
    authoring:finalization.authoring,
    proposal:finalization.proposal,
    handoff:applied.handoff,
    packet,
    intake,
    pin,
  });
  console.log("E11 MultiWOZ editorial review:",JSON.stringify({
    state:"finalized-draft",
    decisionSetId:applied.decisionSetId,
    pending:applied.pending,
    accepted:applied.accepted,
    edited:applied.edited,
    rejected:applied.rejected,
    authoringDigest:validation.authoringDigest,
    batchRegistration:validation.batchRegistration,
    reviewDecisions:validation.reviewDecisions,
    runtimePublication:validation.runtimePublication,
  }));
}

const invoked=process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url);
if (invoked) await main();
