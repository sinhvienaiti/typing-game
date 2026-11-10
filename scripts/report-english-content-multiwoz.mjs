import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [dialogueDoc,report,pin]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","multiwoz-e06-dialogues.json")),
  readJson(path.join(root,"content","english","review-queues","multiwoz-e06-source-report.json")),
  readJson(path.join(root,"content","english","sources","multiwoz-e06-dialogue.json")),
]);
const records=dialogueDoc.records??[];
const errors=[];
if (records.length!==100) errors.push("MultiWOZ E06 must contain exactly 100 dialogues");
const expectedFiles=[
  {path:pin.path,blobSha1:pin.blobSha1},
  ...(pin.additionalFiles??[]),
];
for (const expected of expectedFiles) {
  const observed=report.observedFiles?.find(item=>item.path===expected.path);
  if (!observed||observed.blobSha1!==expected.blobSha1) {
    errors.push("MultiWOZ observed blob SHA does not match source pin: "+expected.path);
  }
}
const ids=new Set(),dialogueKeys=new Set(),scenarioCounts={};
for (const record of records) {
  if (ids.has(record.id)) errors.push(record.id+": duplicate id");
  ids.add(record.id);
  if (record.quality?.state!=="candidate") errors.push(record.id+": must remain candidate");
  if (record.turns.length<4||record.turns.length>10) errors.push(record.id+": turn count outside 4..10");
  let previous="";
  for (const turn of record.turns) {
    if (turn.speaker===previous) errors.push(record.id+": speakers do not alternate");
    previous=turn.speaker;
  }
  const key=record.turns.map(turn=>turn.text.normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US")).join("\u0000");
  if (dialogueKeys.has(key)) errors.push(record.id+": duplicate normalized dialogue");
  dialogueKeys.add(key);
  scenarioCounts[record.scenario]=(scenarioCounts[record.scenario]??0)+1;
}
console.log(JSON.stringify({
  selectedDialogues:records.length,
  candidateDialogues:report.candidateDialogues,
  observedFiles:report.observedFiles,
  scenarioCounts,
},null,2));
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
