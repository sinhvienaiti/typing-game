import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  buildEnglishReviewDecisionIndex,
  englishContentRecordId,
  englishContentReviewSourceDigest,
  overlayEnglishReviewDecisions,
  readEnglishReviewLedger,
} from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const DEFAULT_OUTPUT=path.join(root,"content","english","review-queues","e11-sentence-gap-next-review.json");
const SENTENCE_TARGETS=new Set([
  "common-mistakes",
  "example-sentences",
  "translation-pairs",
  "cloze-exercises",
  "sentence-transformations",
  "dialogue-examples",
]);
const REVIEWABLE_STATES=new Set(["candidate","draft","validated","reviewed"]);

function parseArgs(argv) {
  const options={perTargetLimit:12,outputPath:DEFAULT_OUTPUT};
  for (let index=0;index<argv.length;index+=1) {
    const arg=argv[index];
    if (arg==="--per-target-limit") {
      options.perTargetLimit=Number.parseInt(argv[index+1]??"",10);
      index+=1;
    } else if (arg==="--output") {
      options.outputPath=path.resolve(root,argv[index+1]??"");
      index+=1;
    } else {
      throw new Error("Unknown argument: "+arg);
    }
  }
  if (!Number.isInteger(options.perTargetLimit)||options.perTargetLimit<1||options.perTargetLimit>50) {
    throw new Error("--per-target-limit must be an integer from 1 to 50");
  }
  return options;
}

async function readJson(relative) {
  return JSON.parse(await fs.readFile(path.join(root,relative),"utf8"));
}

function buildContexts(manifest) {
  const contexts=new Map();
  for (const batch of manifest.batches??[]) {
    for (const set of batch.recordSets??[]) {
      const relative=String(set?.path??"");
      if (!relative) continue;
      const context={
        batchId:String(batch?.id??""),
        recordSetId:String(set?.id??""),
        requiredChecks:[...(set?.requiredChecks??[])],
      };
      const existing=contexts.get(relative);
      if (existing&&(existing.batchId!==context.batchId||existing.recordSetId!==context.recordSetId)) {
        throw new Error(
          "Ambiguous review context for "+relative+": "+existing.batchId+"/"+existing.recordSetId+
          " vs "+context.batchId+"/"+context.recordSetId,
        );
      }
      contexts.set(relative,context);
    }
  }
  return contexts;
}

function recordMatchesTarget(record,targetId) {
  if (targetId==="translation-pairs") return record?.type==="translation";
  if (targetId==="cloze-exercises") return record?.type==="cloze";
  if (targetId==="sentence-transformations") return record?.type==="transformation";
  return true;
}

function incompleteRequiredChecks(record,requiredChecks) {
  return requiredChecks.filter(name=>{
    const status=record?.quality?.checks?.[name]?.status;
    return status!=="pass"&&status!=="not-applicable";
  });
}

function checksWithStatus(record,statuses) {
  return Object.entries(record?.quality?.checks??{})
    .filter(([,check])=>statuses.has(check?.status))
    .map(([name])=>name)
    .sort((left,right)=>left.localeCompare(right,"en"));
}

function decisionKey(context,recordId) {
  return context.batchId+"\u0000"+context.recordSetId+"\u0000"+recordId;
}

function compareCandidates(left,right) {
  return left.source.path.localeCompare(right.source.path,"en")||
    left.recordId.localeCompare(right.recordId,"en");
}

const options=parseArgs(process.argv.slice(2));
const [readiness,manifest,reviewLedger]=await Promise.all([
  readJson("content/english/reports/e11-readiness.json"),
  readJson("content/english/batches/manifest.json"),
  readEnglishReviewLedger(root),
]);
const contexts=buildContexts(manifest);
const decisionIndex=buildEnglishReviewDecisionIndex(reviewLedger);
const underTarget=(readiness.targets??[]).filter(
  target=>SENTENCE_TARGETS.has(target.id)&&Number(target.current)<Number(target.minimum),
);

const targetPackets=[];
for (const target of underTarget) {
  const candidates=[];
  const blockedSources=[];
  let matchedRecordCount=0;
  let publishedExcludedCount=0;
  let deprecatedExcludedCount=0;
  let existingDecisionExcludedCount=0;

  const sourcePaths=[...new Set((target.sourceCounts??[]).map(source=>String(source?.path??"")).filter(Boolean))];
  for (const relative of sourcePaths) {
    const context=contexts.get(relative);
    if (!context) {
      blockedSources.push({path:relative,reason:"source-is-not-registered-in-batch-manifest"});
      continue;
    }
    const document=await readJson(relative);
    if (!Array.isArray(document?.records)) {
      throw new Error(relative+" must contain records[] for E11 review queue generation");
    }
    const overlaid=overlayEnglishReviewDecisions(document.records,reviewLedger,context);
    for (let index=0;index<document.records.length;index+=1) {
      const sourceRecord=document.records[index];
      if (!recordMatchesTarget(sourceRecord,target.id)) continue;
      matchedRecordCount+=1;
      const currentRecord=overlaid[index];
      const currentState=currentRecord?.quality?.state;
      if (currentState==="published") {
        publishedExcludedCount+=1;
        continue;
      }
      if (currentState==="deprecated") {
        deprecatedExcludedCount+=1;
        continue;
      }
      if (!REVIEWABLE_STATES.has(currentState)) {
        throw new Error(
          target.id+" @ "+relative+": record "+englishContentRecordId(sourceRecord,index)+
          " has non-reviewable quality state "+String(currentState),
        );
      }

      const recordId=englishContentRecordId(sourceRecord,index);
      if (decisionIndex.has(decisionKey(context,recordId))) {
        existingDecisionExcludedCount+=1;
        continue;
      }
      candidates.push({
        targetId:target.id,
        recordId,
        sourceDigest:englishContentReviewSourceDigest(sourceRecord),
        source:{
          path:relative,
          batchId:context.batchId,
          recordSetId:context.recordSetId,
        },
        reviewState:currentState,
        requiredChecks:context.requiredChecks,
        incompleteRequiredChecks:incompleteRequiredChecks(currentRecord,context.requiredChecks),
        pendingChecks:checksWithStatus(currentRecord,new Set(["pending"])),
        failedChecks:checksWithStatus(currentRecord,new Set(["fail"])),
        sourceRecord,
      });
    }
  }

  candidates.sort(compareCandidates);
  const selected=candidates.slice(0,options.perTargetLimit);
  targetPackets.push({
    targetId:target.id,
    current:target.current,
    minimum:target.minimum,
    deficit:Math.max(0,Number(target.minimum)-Number(target.current)),
    sourceCount:sourcePaths.length,
    matchedRecordCount,
    publishedExcludedCount,
    deprecatedExcludedCount,
    existingDecisionExcludedCount,
    availableCandidateCount:candidates.length,
    selectedCount:selected.length,
    blockedSources,
    records:selected,
  });
}

const packet={
  schemaVersion:1,
  kind:"english-content-e11-sentence-review-gap-packet",
  selection:{
    strategy:"e11-source-order-independent-unreviewed-gap-v1",
    perTargetLimit:options.perTargetLimit,
    underTargetCount:targetPackets.length,
    selectedCount:targetPackets.reduce((sum,target)=>sum+target.selectedCount,0),
  },
  safeguards:{
    mutatesReviewLedger:false,
    mutatesSourceRecords:false,
    publishesRecords:false,
    sourceDigestRequired:true,
  },
  targets:targetPackets,
};

await fs.mkdir(path.dirname(options.outputPath),{recursive:true});
await fs.writeFile(options.outputPath,JSON.stringify(packet,null,2)+"\n","utf8");
console.log(
  "E11 sentence review-gap queue:",
  JSON.stringify({
    output:path.relative(root,options.outputPath).replaceAll(path.sep,"/"),
    underTargetCount:packet.selection.underTargetCount,
    selectedCount:packet.selection.selectedCount,
    targets:targetPackets.map(target=>({
      targetId:target.targetId,
      current:target.current,
      minimum:target.minimum,
      availableCandidateCount:target.availableCandidateCount,
      selectedCount:target.selectedCount,
      blockedSourceCount:target.blockedSources.length,
    })),
  }),
);
