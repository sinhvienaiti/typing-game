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
const editorialRoot=path.join(root,"content","english","reviews","editorial");
const defaults={
  packetPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-review.json"),
  intakePath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-intake.json"),
  handoffPath:path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-editorial-handoff.json"),
  decisionsPath:null,
  authoringPath:null,
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

export function multiwozEditorialSliceIdentity(decisionManifest) {
  const decisionSetId=String(decisionManifest?.decisionSetId??"");
  const match=/^e11\.dialogue-multiwoz\.reviewed-slice-(\d+)$/.exec(decisionSetId);
  if (!match) {
    throw new TypeError("MultiWOZ editorial decisionSetId must match e11.dialogue-multiwoz.reviewed-slice-<number>");
  }
  const sliceId=match[1];
  return {
    sliceId,
    batchId:"e11.dialogue-multiwoz-reviewed-slice-"+sliceId,
    authoringRelative:"content/english/sentences/e11-multiwoz-dialogue-reviewed-slice-"+sliceId+".json",
  };
}

async function discoverDecisionManifestPath(handoff,explicitPath) {
  if (explicitPath) return explicitPath;
  let entries=[];
  try {
    entries=await fs.readdir(editorialRoot,{withFileTypes:true});
  } catch (error) {
    if (error?.code==="ENOENT") return null;
    throw error;
  }
  const manifests=[];
  for (const entry of entries
    .filter(candidate=>candidate.isDirectory()&&/^multiwoz-e11-dialogue-slice-\d+$/.test(candidate.name))
    .sort((left,right)=>left.name.localeCompare(right.name,"en"))) {
    const manifestPath=path.join(editorialRoot,entry.name,"manifest.json");
    const manifest=await readJson(manifestPath);
    if (
      manifest?.recordSetDigest===handoff.recordSetDigest &&
      manifest?.handoffId===handoff.handoffId &&
      manifest?.intakeId===handoff.intakeId
    ) {
      manifests.push({manifestPath,manifest});
    }
  }
  if (manifests.length>1) {
    throw new Error("Multiple MultiWOZ editorial decision manifests are bound to the current slice");
  }
  return manifests[0]?.manifestPath??null;
}

export async function main(argv=process.argv.slice(2)) {
  const options=parseArgs(argv);
  const [packet,intake,handoff,pin]=await Promise.all([
    readJson(options.packetPath),
    readJson(options.intakePath),
    readJson(options.handoffPath),
    readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json")),
  ]);
  const decisionsPath=await discoverDecisionManifestPath(handoff,options.decisionsPath);
  if (!decisionsPath) {
    console.log("E11 MultiWOZ editorial review:",JSON.stringify({
      state:"decision-set-not-found-for-current-slice",
      currentRecordSetDigest:handoff.recordSetDigest,
      runtimePublication:"blocked",
    }));
    return;
  }
  const decisionManifest=await readJson(decisionsPath);
  const identity=multiwozEditorialSliceIdentity(decisionManifest);
  const expectedDecisionDir="multiwoz-e11-dialogue-slice-"+identity.sliceId;
  if (path.basename(path.dirname(decisionsPath))!==expectedDecisionDir) {
    throw new TypeError("MultiWOZ editorial decision directory does not match decisionSetId slice identity");
  }
  const decisionDir=path.dirname(decisionsPath);
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
  const authoringPath=options.authoringPath??path.join(root,identity.authoringRelative);
  const authoringRelative=path.relative(root,authoringPath).replaceAll(path.sep,"/");

  if (applied.accepted===0&&applied.edited===0) {
    if (applied.rejected!==applied.handoff.records.length) {
      throw new TypeError("Rejection-only MultiWOZ editorial outcome must reject every handoff record");
    }
    await fs.rm(authoringPath,{force:true});
    await fs.rm(options.proposalPath,{force:true});
    console.log("E11 MultiWOZ editorial review:",JSON.stringify({
      state:"finalized-rejections-only",
      decisionSetId:applied.decisionSetId,
      sliceId:identity.sliceId,
      pending:applied.pending,
      accepted:applied.accepted,
      edited:applied.edited,
      rejected:applied.rejected,
      batchRegistration:"not-required",
      reviewDecisions:"complete",
      runtimePublication:"blocked",
    }));
    return;
  }

  const finalization=buildMultiwozDialogueEditorialFinalization(applied.handoff,packet,intake,pin,{
    authoringPath:authoringRelative,
    batchId:identity.batchId,
    proposalId:identity.batchId,
  });
  await fs.mkdir(path.dirname(authoringPath),{recursive:true});
  await fs.mkdir(path.dirname(options.proposalPath),{recursive:true});
  await fs.writeFile(authoringPath,stableJson(finalization.authoring),"utf8");
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
    sliceId:identity.sliceId,
    pending:applied.pending,
    accepted:applied.accepted,
    edited:applied.edited,
    rejected:applied.rejected,
    authoringPath:identity.authoringRelative,
    authoringDigest:validation.authoringDigest,
    batchRegistration:validation.batchRegistration,
    reviewDecisions:validation.reviewDecisions,
    runtimePublication:validation.runtimePublication,
  }));
}

const invoked=process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url);
if (invoked) await main();
