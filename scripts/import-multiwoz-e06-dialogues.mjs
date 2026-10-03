import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import {
  gitBlobSha1,
  isLearningDialogue,
  normalizeDialogueText,
  parseMultiwozDialogue,
  selectEvenly,
} from "./multiwoz-dialogue-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).filter(value=>value.startsWith("--")).map(raw=>{
  const split=raw.indexOf("=");
  return split<0?[raw,"true"]:[raw.slice(0,split),raw.slice(split+1)];
}));
const pin=await readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json"));
const sourceDir=path.resolve(root,args.get("--source-dir")??".cache/english-content/multiwoz");
const sourceSpecs=[
  {path:pin.path,blobSha1:pin.blobSha1},
  ...(pin.additionalFiles??[]),
];
const output=path.resolve(root,args.get("--output")??"content/english/review-queues/multiwoz-e06-dialogues.json");
const reportOutput=path.resolve(root,args.get("--report")??"content/english/review-queues/multiwoz-e06-source-report.json");
const observedFiles=[];
const candidates=[];
const seenDialogueText=new Set();
for (const sourceSpec of sourceSpecs) {
  const sourceFile=path.join(sourceDir,sourceSpec.path);
  const observedBlobSha1=await gitBlobSha1(sourceFile);
  if (observedBlobSha1!==sourceSpec.blobSha1) {
    throw new Error("MultiWOZ source blob mismatch for "+sourceSpec.path+". Expected "+sourceSpec.blobSha1+", got "+observedBlobSha1);
  }
  observedFiles.push({path:sourceSpec.path,blobSha1:observedBlobSha1});
  const raw=JSON.parse(await fs.readFile(sourceFile,"utf8"));
  if (!Array.isArray(raw)) throw new TypeError("MultiWOZ dialogue file must be an array: "+sourceSpec.path);
  for (const item of raw) {
    const dialogue=parseMultiwozDialogue(item);
    if (dialogue===null||!isLearningDialogue(dialogue)) continue;
    const key=dialogue.turns.map(turn=>normalizeDialogueText(turn.utterance)).join("\u0000");
    if (seenDialogueText.has(key)) continue;
    seenDialogueText.add(key);
    candidates.push({...dialogue,sourcePath:sourceSpec.path});
  }
}
candidates.sort((a,b)=>a.dialogueId.localeCompare(b.dialogueId));
const selected=selectEvenly(candidates,100);

function quality() {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"multiwoz-e06-import-v1"},
      sourcePin:{status:"pass",method:"git-blob-sha1-v1"},
      dialogueStructure:{status:"pass",method:"alternating-4-to-10-turns-v1"},
      identifierSafety:{status:"pass",method:"long-identifier-filter-v1"},
      naturalness:{status:"pending",method:"learning-editor-review-required"},
      cefr:{status:"pending",method:"cefr-review-required"},
    },
  };
}

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
    note:"Human-human MultiWOZ 2.2 dialogue selected deterministically for the E06 learning-content pilot.",
  },
}));

await fs.mkdir(path.dirname(output),{recursive:true});
await Promise.all([
  fs.writeFile(output,stableJson({schemaVersion:1,records}),"utf8"),
  fs.writeFile(reportOutput,stableJson({
    schemaVersion:1,
    source:"multiwoz",
    version:pin.version,
    commit:pin.commit,
    observedFiles,
    candidateDialogues:candidates.length,
    selectedDialogues:records.length,
  }),"utf8"),
]);
console.log("MultiWOZ E06 dialogue pilot:",JSON.stringify({
  candidateDialogues:candidates.length,
  selectedDialogues:records.length,
  observedFiles,
}));
