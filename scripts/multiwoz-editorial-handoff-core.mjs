import fs from "node:fs/promises";
import path from "node:path";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";
import { stableJson } from "./english-content-core.mjs";
import { buildMultiwozDialogueReviewIntake } from "./multiwoz-review-intake-core.mjs";

const EDITORIAL_CHECKS=Object.freeze([
  "exactDuplicate",
  "nearDuplicate",
  "grammar",
  "naturalness",
  "cefr",
  "license",
]);

function assertIntakeBinding(packet,intake,pin) {
  const expected=buildMultiwozDialogueReviewIntake(packet,pin);
  if (stableJson(expected)!==stableJson(intake)) {
    throw new TypeError("MultiWOZ editorial handoff intake does not match the deterministic packet binding");
  }
  return expected;
}

export function buildMultiwozDialogueEditorialHandoff(packet,intake,pin) {
  const boundIntake=assertIntakeBinding(packet,intake,pin);
  const recordsById=new Map(packet.recordSet.records.map(record=>[record.id,record]));
  const records=boundIntake.records.map(binding=>{
    const record=recordsById.get(binding.recordId);
    if (!record) throw new TypeError(binding.recordId+": candidate record is absent from the review packet");
    const digest=englishContentReviewSourceDigest(record);
    if (digest!==binding.sourceDigest) {
      throw new TypeError(binding.recordId+": candidate source digest changed after intake binding");
    }
    const checks=Object.fromEntries(EDITORIAL_CHECKS.map(name=>[name,"pending"]));
    return {
      recordId:binding.recordId,
      sourceId:binding.sourceId,
      sourceDigest:binding.sourceDigest,
      candidateSnapshot:structuredClone(record),
      editorial:{
        disposition:"pending",
        cefr:null,
        scenario:null,
        turns:null,
        checks,
        notes:"",
      },
    };
  });

  return {
    schemaVersion:1,
    kind:"english-content-editorial-handoff",
    handoffId:"e11.dialogue-multiwoz.next",
    intakeId:boundIntake.intakeId,
    batchFamily:boundIntake.batchFamily,
    recordSetId:boundIntake.recordSetId,
    recordSetDigest:boundIntake.recordSetDigest,
    state:"pending-editorial-authoring",
    editorialChecks:[...EDITORIAL_CHECKS],
    records,
    lifecycle:{
      batchRegistration:"blocked-until-editorial-authoring",
      reviewDecisions:"not-created",
      runtimePublication:"blocked",
    },
  };
}

export function validateMultiwozDialogueEditorialHandoff(handoff,packet,intake,pin) {
  const expected=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  if (handoff?.schemaVersion!==1||handoff?.kind!=="english-content-editorial-handoff") {
    throw new TypeError("MultiWOZ editorial handoff must use schemaVersion 1 and english-content-editorial-handoff kind");
  }
  if (handoff?.intakeId!==expected.intakeId||handoff?.recordSetDigest!==expected.recordSetDigest) {
    throw new TypeError("MultiWOZ editorial handoff is bound to a different intake or record set");
  }
  if (!Array.isArray(handoff?.records)||handoff.records.length!==expected.records.length) {
    throw new TypeError("MultiWOZ editorial handoff record count does not match intake");
  }
  const expectedById=new Map(expected.records.map(record=>[record.recordId,record]));
  const seen=new Set();
  for (const record of handoff.records) {
    const recordId=String(record?.recordId??"");
    if (!recordId||seen.has(recordId)) throw new TypeError("MultiWOZ editorial handoff contains a missing or duplicate record id");
    seen.add(recordId);
    const source=expectedById.get(recordId);
    if (!source) throw new TypeError(recordId+": editorial handoff record is outside the bound intake");
    if (record?.sourceId!==source.sourceId||record?.sourceDigest!==source.sourceDigest) {
      throw new TypeError(recordId+": editorial handoff source identity or digest does not match intake");
    }
    if (englishContentReviewSourceDigest(record?.candidateSnapshot)!==source.sourceDigest) {
      throw new TypeError(recordId+": candidateSnapshot no longer matches the digest-bound candidate");
    }
    const disposition=record?.editorial?.disposition;
    if (!["pending","accept","edit","reject"].includes(disposition)) {
      throw new TypeError(recordId+": unsupported editorial disposition "+String(disposition));
    }
    if (record?.editorial&&Object.hasOwn(record.editorial,"targetState")) {
      throw new TypeError(recordId+": editorial handoff must not contain targetState");
    }
    for (const check of EDITORIAL_CHECKS) {
      const value=record?.editorial?.checks?.[check];
      if (!["pending","pass","not-applicable","fail"].includes(value)) {
        throw new TypeError(recordId+": invalid editorial check "+check+"="+String(value));
      }
    }
  }
  if (seen.size!==expectedById.size) throw new TypeError("MultiWOZ editorial handoff is missing intake records");
  return {
    recordCount:seen.size,
    pending:handoff.records.filter(record=>record.editorial.disposition==="pending").length,
    accepted:handoff.records.filter(record=>record.editorial.disposition==="accept").length,
    edited:handoff.records.filter(record=>record.editorial.disposition==="edit").length,
    rejected:handoff.records.filter(record=>record.editorial.disposition==="reject").length,
  };
}

export async function writeImmutableEditorialHandoff(filePath,handoff) {
  const body=stableJson(handoff);
  try {
    const current=await fs.readFile(filePath,"utf8");
    if (current!==body) {
      throw new Error("Editorial handoff collision at "+filePath+": existing bytes differ from the deterministic handoff");
    }
    return {state:"unchanged",bytes:Buffer.byteLength(body)};
  } catch (error) {
    if (error?.code!=="ENOENT") throw error;
  }
  await fs.mkdir(path.dirname(filePath),{recursive:true});
  await fs.writeFile(filePath,body,"utf8");
  return {state:"written",bytes:Buffer.byteLength(body)};
}
