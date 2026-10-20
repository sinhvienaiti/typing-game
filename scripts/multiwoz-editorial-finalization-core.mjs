import fs from "node:fs/promises";
import path from "node:path";
import { englishContentRecordDigest } from "./english-review-core.mjs";
import { stableJson } from "./english-content-core.mjs";
import { validateMultiwozDialogueEditorialHandoff } from "./multiwoz-editorial-handoff-core.mjs";

const EDITORIAL_CHECKS=Object.freeze([
  "exactDuplicate",
  "nearDuplicate",
  "grammar",
  "naturalness",
  "cefr",
  "license",
]);
const REQUIRED_CHECKS=Object.freeze([
  "schema",
  "sourcePin",
  "dialogueStructure",
  "identifierSafety",
  "exactDuplicate",
  "nearDuplicate",
  "grammar",
  "translation",
  "naturalness",
  "targetStructure",
  "cefr",
  "license",
]);
const REQUIRED_BEFORE_PUBLISH=Object.freeze([
  "source-pin",
  "dialogue-structure-review",
  "identifier-safety-review",
  "dedupe-review",
  "grammar-review",
  "naturalness-review",
  "cefr-review",
  "license-review",
]);
const ALLOWED_CEFR=new Set(["A2","B1"]);

function requireText(value,label) {
  if (typeof value!=="string"||value.trim()==="") throw new TypeError(label+" must be a non-empty string");
  return value.trim();
}

function normalizeTurns(value,label) {
  if (!Array.isArray(value)||value.length<4||value.length>10) {
    throw new TypeError(label+" must contain 4 to 10 turns");
  }
  const turns=value.map((turn,index)=>({
    speaker:requireText(turn?.speaker,label+"["+index+"] speaker"),
    text:requireText(turn?.text,label+"["+index+"] text"),
  }));
  for (let index=0;index<turns.length;index++) {
    const expected=index%2===0?"Learner":"Assistant";
    if (turns[index].speaker!==expected) {
      throw new TypeError(label+" must alternate Learner/Assistant from the first turn");
    }
  }
  return turns;
}

function completedEditorialChecks(entry) {
  const result={};
  for (const name of EDITORIAL_CHECKS) {
    const status=entry?.editorial?.checks?.[name];
    if (status!=="pass"&&status!=="not-applicable") {
      throw new TypeError(entry.recordId+": editorial check "+name+" must be pass or not-applicable before finalization");
    }
    result[name]={status,method:"e11-multiwoz-editorial-finalization-v1"};
  }
  return result;
}

function authoringRecord(entry) {
  const disposition=entry.editorial.disposition;
  if (disposition==="reject") {
    requireText(entry.editorial.notes,entry.recordId+" rejection notes");
    return null;
  }
  if (disposition!=="accept"&&disposition!=="edit") {
    throw new TypeError(entry.recordId+": editorial disposition must be accept, edit, or reject before finalization");
  }
  const candidate=structuredClone(entry.candidateSnapshot);
  const cefr=requireText(entry.editorial.cefr,entry.recordId+" editorial cefr");
  if (!ALLOWED_CEFR.has(cefr)) throw new TypeError(entry.recordId+": editorial cefr must be A2 or B1");
  const scenario=entry.editorial.scenario===null
    ?requireText(candidate.scenario,entry.recordId+" candidate scenario")
    :requireText(entry.editorial.scenario,entry.recordId+" editorial scenario");
  const turns=normalizeTurns(
    entry.editorial.turns===null?candidate.turns:entry.editorial.turns,
    entry.recordId+" turns",
  );
  if (disposition==="edit"&&entry.editorial.scenario===null&&entry.editorial.turns===null) {
    throw new TypeError(entry.recordId+": edit disposition must provide an edited scenario or turns");
  }
  const editorialChecks=completedEditorialChecks(entry);
  const provenance=structuredClone(candidate.provenance);
  if (!Array.isArray(provenance?.sources)||provenance.sources.length!==1) {
    throw new TypeError(entry.recordId+": finalized record requires exactly one provenance source");
  }
  if (disposition==="edit") provenance.sources[0].modified=true;
  provenance.note=disposition==="edit"
    ?"Editorially normalized from the pinned MultiWOZ 2.2 dialogue during the E11 controlled review intake; immutable source identity is retained."
    :"Accepted from the pinned MultiWOZ 2.2 E11 controlled review intake without dialogue-text modification; immutable source identity is retained.";

  return {
    schemaVersion:1,
    id:requireText(candidate.id,entry.recordId+" candidate id"),
    scenario,
    cefr,
    turns,
    quality:{
      state:"draft",
      checks:{
        schema:{status:"pass",method:"e11-multiwoz-editorial-finalization-v1"},
        sourcePin:{status:"pass",method:"multiwoz-git-blob-pin-v1"},
        dialogueStructure:{status:"pass",method:"editorial-alternating-dialogue-v1"},
        identifierSafety:{status:"pass",method:"editorial-identifier-safety-v1"},
        exactDuplicate:editorialChecks.exactDuplicate,
        nearDuplicate:editorialChecks.nearDuplicate,
        grammar:editorialChecks.grammar,
        translation:{status:"not-applicable",method:"english-only-dialogue"},
        naturalness:editorialChecks.naturalness,
        targetStructure:{status:"not-applicable",method:"dialogue-free-production"},
        cefr:editorialChecks.cefr,
        license:editorialChecks.license,
      },
    },
    provenance,
  };
}

export function buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin,{authoringPath}={}) {
  const validation=validateMultiwozDialogueEditorialHandoff(handoff,packet,intake,pin);
  if (validation.pending!==0) {
    throw new TypeError("MultiWOZ editorial handoff still has "+validation.pending+" pending record(s)");
  }
  const normalizedPath=requireText(
    authoringPath??"content/english/sentences/e11-multiwoz-dialogue-reviewed-slice-01.json",
    "authoringPath",
  ).replaceAll(path.sep,"/");
  if (!normalizedPath.startsWith("content/english/sentences/")) {
    throw new TypeError("authoringPath must stay under content/english/sentences/");
  }

  const records=[];
  const rejected=[];
  for (const entry of handoff.records) {
    const record=authoringRecord(entry);
    if (record===null) rejected.push({recordId:entry.recordId,notes:entry.editorial.notes.trim()});
    else records.push(record);
  }
  records.sort((left,right)=>left.id.localeCompare(right.id,"en"));
  rejected.sort((left,right)=>left.recordId.localeCompare(right.recordId,"en"));
  if (records.length===0) throw new TypeError("MultiWOZ editorial finalization has no accepted or edited records");

  const authoring={schemaVersion:1,records};
  const batch={
    id:"e11.dialogue-multiwoz-reviewed-slice-01",
    phase:"E11",
    category:"sentences",
    cefr:["A2","B1"],
    state:"draft",
    recordSets:[{
      id:"reviewed-dialogues",
      path:normalizedPath,
      expectedCount:records.length,
      generated:false,
      allowedQualityStates:["draft"],
      requiredChecks:[...REQUIRED_CHECKS],
    }],
    requiredBeforePublish:[...REQUIRED_BEFORE_PUBLISH],
    gameSmokes:[{
      gameId:"karaoke-typing",
      activity:"dialogue",
      recordSetId:"reviewed-dialogues",
      sampleCount:Math.min(3,records.length),
    }],
  };
  const proposal={
    schemaVersion:1,
    kind:"english-content-batch-registration-proposal",
    proposalId:"e11.dialogue-multiwoz-reviewed-slice-01",
    handoffId:handoff.handoffId,
    intakeId:handoff.intakeId,
    recordSetDigest:handoff.recordSetDigest,
    authoringPath:normalizedPath,
    authoringDigest:englishContentRecordDigest(authoring),
    acceptedCount:validation.accepted,
    editedCount:validation.edited,
    rejectedCount:validation.rejected,
    rejected,
    batch,
    lifecycle:{
      batchRegistration:"ready-for-manifest-registration",
      reviewDecisions:"not-created",
      runtimePublication:"blocked",
    },
  };
  return {authoring,proposal};
}

export async function writeImmutableEditorialFinalization({authoringPath,proposalPath},finalization) {
  const outputs=[
    [authoringPath,stableJson(finalization.authoring)],
    [proposalPath,stableJson(finalization.proposal)],
  ];
  for (const [filePath,body] of outputs) {
    try {
      const current=await fs.readFile(filePath,"utf8");
      if (current!==body) throw new Error("Editorial finalization collision at "+filePath+": existing bytes differ");
    } catch (error) {
      if (error?.code!=="ENOENT") throw error;
      await fs.mkdir(path.dirname(filePath),{recursive:true});
      await fs.writeFile(filePath,body,"utf8");
    }
  }
  return {
    authoringBytes:Buffer.byteLength(outputs[0][1]),
    proposalBytes:Buffer.byteLength(outputs[1][1]),
  };
}
