import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import {
  gitBlobSha1,
  isLearningDialogue,
  multiwozDialogueSourceKey,
  multiwozDialogueSourceKeyFromRecord,
  normalizeDialogueText,
  parseMultiwozDialogue,
  selectNextMultiwozDialogues,
} from "./multiwoz-dialogue-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const defaultOutput=path.join(root,"content","english","review-queues","multiwoz-e11-dialogue-next-review.json");

function parseArgs(argv) {
  const options={
    limit:24,
    sourceDir:path.join(root,".cache","english-content","multiwoz"),
    outputPath:defaultOutput,
  };
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
    if (flag==="--limit") options.limit=Number.parseInt(takeValue(),10);
    else if (flag==="--source-dir") options.sourceDir=path.resolve(root,takeValue());
    else if (flag==="--output") options.outputPath=path.resolve(root,takeValue());
    else throw new Error("Unknown argument: "+raw);
  }
  if (!Number.isInteger(options.limit)||options.limit<1||options.limit>200) {
    throw new Error("--limit must be an integer from 1 to 200");
  }
  return options;
}

function quality() {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"multiwoz-e11-next-slice-v1"},
      sourcePin:{status:"pass",method:"git-blob-sha1-v1"},
      dialogueStructure:{status:"pass",method:"alternating-4-to-10-turns-v1"},
      identifierSafety:{status:"pass",method:"long-identifier-filter-v1"},
      naturalness:{status:"pending",method:"learning-editor-review-required"},
      cefr:{status:"pending",method:"cefr-review-required"},
    },
  };
}

async function collectUsedDialogueKeys(batchManifest) {
  const paths=new Set();
  for (const batch of batchManifest.batches??[]) {
    for (const set of batch.recordSets??[]) {
      if (typeof set?.path==="string"&&set.path) paths.add(set.path);
    }
  }
  const keys=new Set();
  for (const relative of [...paths].sort((left,right)=>left.localeCompare(right,"en"))) {
    const document=await readJson(path.join(root,relative));
    if (!Array.isArray(document?.records)) continue;
    for (const record of document.records) {
      const key=multiwozDialogueSourceKeyFromRecord(record);
      if (key!==null) keys.add(key);
    }
  }
  return keys;
}

const options=parseArgs(process.argv.slice(2));
const [pin,batchManifest]=await Promise.all([
  readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json")),
  readJson(path.join(root,"content","english","batches","manifest.json")),
]);
const sourceSpecs=[
  {path:pin.path,blobSha1:pin.blobSha1},
  ...(pin.additionalFiles??[]),
];
const observedFiles=[];
const candidates=[];
const seenDialogueText=new Set();
for (const sourceSpec of sourceSpecs) {
  const sourceFile=path.join(options.sourceDir,sourceSpec.path);
  const observedBlobSha1=await gitBlobSha1(sourceFile);
  if (observedBlobSha1!==sourceSpec.blobSha1) {
    throw new Error(
      "MultiWOZ source blob mismatch for "+sourceSpec.path+". Expected "+sourceSpec.blobSha1+", got "+observedBlobSha1,
    );
  }
  observedFiles.push({path:sourceSpec.path,blobSha1:observedBlobSha1});
  const raw=JSON.parse(await fs.readFile(sourceFile,"utf8"));
  if (!Array.isArray(raw)) throw new TypeError("MultiWOZ dialogue file must be an array: "+sourceSpec.path);
  for (const item of raw) {
    const dialogue=parseMultiwozDialogue(item);
    if (dialogue===null||!isLearningDialogue(dialogue)) continue;
    const textKey=dialogue.turns.map(turn=>normalizeDialogueText(turn.utterance)).join("\u0000");
    if (seenDialogueText.has(textKey)) continue;
    seenDialogueText.add(textKey);
    candidates.push({...dialogue,sourcePath:sourceSpec.path});
  }
}

const usedDialogueKeys=await collectUsedDialogueKeys(batchManifest);
const remainingCandidates=candidates.filter(
  dialogue=>!usedDialogueKeys.has(multiwozDialogueSourceKey(dialogue)),
);
const selected=selectNextMultiwozDialogues(
  candidates,
  Math.min(options.limit,remainingCandidates.length),
  {excludeKeys:usedDialogueKeys},
);

if (selected.length===0) {
  await fs.rm(options.outputPath,{force:true});
  console.log("E11 MultiWOZ next dialogue review slice:",JSON.stringify({
    state:"source-exhausted",
    output:path.relative(root,options.outputPath).replaceAll(path.sep,"/"),
    candidateCount:candidates.length,
    usedDialogueCount:usedDialogueKeys.size,
    remainingCandidateCount:0,
    selectedCount:0,
  }));
} else {
  const records=selected.map(dialogue=>({
    schemaVersion:1,
    id:"dlg.multiwoz."+dialogue.dialogueId.toLocaleLowerCase("en-US").replace(/[^a-z0-9._-]+/gu,"-"),
    scenario:dialogue.services.join(" + ")+" service conversation",
    turns:dialogue.turns.map(turn=>({
      speaker:turn.speaker==="USER"?"Learner":"Assistant",
      text:turn.utterance,
    })),
    quality:quality(),
    provenance:{
      sources:[{
        dataset:"multiwoz",
        sourceId:dialogue.dialogueId,
        sourceUrl:"https://github.com/"+pin.repository+"/blob/"+pin.commit+"/"+dialogue.sourcePath,
        snapshot:pin.commit,
        license:pin.license,
        attribution:pin.attribution,
        modified:false,
      }],
      note:"Human-human MultiWOZ 2.2 dialogue selected from the pinned commit for bounded E11 review.",
    },
  }));
  const packet={
    schemaVersion:1,
    kind:"english-content-review-packet",
    batchFamily:"e11.dialogue-multiwoz",
    source:{
      dataset:"multiwoz",
      version:pin.version,
      repository:pin.repository,
      commit:pin.commit,
      observedFiles,
      pinned:true,
    },
    selection:{
      strategy:"dialogue-source-id-order-after-manifest-multiwoz-exclusion-v1",
      requestedLimit:options.limit,
      candidateCount:candidates.length,
      usedDialogueCount:usedDialogueKeys.size,
      remainingCandidateCount:remainingCandidates.length,
      selectedDialogueIds:selected.map(multiwozDialogueSourceKey),
    },
    recordSet:{recordSetId:"dialogues",records},
  };

  await fs.mkdir(path.dirname(options.outputPath),{recursive:true});
  await fs.writeFile(options.outputPath,stableJson(packet),"utf8");
  console.log("E11 MultiWOZ next dialogue review slice:",JSON.stringify({
    state:selected.length<options.limit?"final-partial-slice":"ready",
    output:path.relative(root,options.outputPath).replaceAll(path.sep,"/"),
    candidateCount:candidates.length,
    usedDialogueCount:usedDialogueKeys.size,
    remainingCandidateCount:remainingCandidates.length,
    selectedCount:selected.length,
    selectedDialogueIds:packet.selection.selectedDialogueIds,
  }));
}
