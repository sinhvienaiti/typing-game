import { stableJson } from "./english-content-core.mjs";
import { validateMultiwozDialogueEditorialHandoff } from "./multiwoz-editorial-handoff-core.mjs";

const CHECKS=Object.freeze([
  "exactDuplicate",
  "nearDuplicate",
  "grammar",
  "naturalness",
  "cefr",
  "license",
]);
const DISPOSITIONS=new Set(["accept","edit","reject"]);
const CHECK_STATES=new Set(["pass","not-applicable","fail"]);
const SHA256_PATTERN=/^[0-9a-f]{64}$/;

function requireText(value,label) {
  if (typeof value!=="string"||value.trim()==="") throw new TypeError(label+" must be a non-empty string");
  return value.trim();
}

function assertDecisionSetMetadata(decisions,handoff) {
  if (decisions?.schemaVersion!==1||decisions?.kind!=="english-content-editorial-decisions") {
    throw new TypeError("MultiWOZ editorial decisions must use schemaVersion 1 and english-content-editorial-decisions kind");
  }
  requireText(decisions?.decisionSetId,"MultiWOZ editorial decisionSetId");
  if (decisions?.handoffId!==handoff.handoffId||decisions?.intakeId!==handoff.intakeId) {
    throw new TypeError("MultiWOZ editorial decisions are bound to a different handoff or intake");
  }
  if (decisions?.recordSetDigest!==handoff.recordSetDigest) {
    throw new TypeError("MultiWOZ editorial decisions recordSetDigest does not match the generated handoff");
  }
  if (!Array.isArray(decisions?.decisions)) throw new TypeError("MultiWOZ editorial decisions must contain decisions[]");
}

function normalizeTurns(value,label) {
  if (value===null) return null;
  if (!Array.isArray(value)||value.length<4||value.length>10) throw new TypeError(label+" must contain 4 to 10 turns");
  return value.map((turn,index)=>({
    speaker:requireText(turn?.speaker,label+"["+index+"] speaker"),
    text:requireText(turn?.text,label+"["+index+"] text"),
  }));
}

function normalizeDecision(decision,source) {
  const recordId=requireText(decision?.recordId,"MultiWOZ editorial decision recordId");
  if (recordId!==source.recordId) throw new TypeError(recordId+": editorial decision recordId does not match the bound handoff entry");
  const sourceDigest=requireText(decision?.sourceDigest,recordId+" editorial decision sourceDigest");
  if (!SHA256_PATTERN.test(sourceDigest)) {
    throw new TypeError(recordId+": editorial decision sourceDigest is stale or malformed; expected 64 lowercase hex characters");
  }
  if (sourceDigest!==source.sourceDigest) throw new TypeError(recordId+": editorial decision sourceDigest is stale");
  const disposition=decision?.disposition;
  if (!DISPOSITIONS.has(disposition)) throw new TypeError(recordId+": editorial decision must be accept, edit, or reject");
  const checks={};
  for (const name of CHECKS) {
    const state=decision?.checks?.[name];
    if (!CHECK_STATES.has(state)) throw new TypeError(recordId+": invalid editorial decision check "+name+"="+String(state));
    checks[name]=state;
  }
  return {
    disposition,
    cefr:decision?.cefr===null?null:requireText(decision?.cefr,recordId+" editorial cefr"),
    scenario:decision?.scenario===null?null:requireText(decision?.scenario,recordId+" editorial scenario"),
    turns:normalizeTurns(decision?.turns,recordId+" editorial turns"),
    checks,
    notes:typeof decision?.notes==="string"?decision.notes.trim():"",
  };
}

export function buildMultiwozEditorialDecisionSet(manifest,shards) {
  if (manifest?.schemaVersion!==1||manifest?.kind!=="english-content-editorial-decision-manifest") {
    throw new TypeError("MultiWOZ editorial decision manifest must use schemaVersion 1 and english-content-editorial-decision-manifest kind");
  }
  if (!Array.isArray(manifest?.shards)||manifest.shards.length===0) {
    throw new TypeError("MultiWOZ editorial decision manifest must contain shards[]");
  }
  if (!Array.isArray(shards)||shards.length!==manifest.shards.length) {
    throw new TypeError("MultiWOZ editorial decision shard count does not match manifest");
  }
  const decisions=[];
  for (let index=0;index<manifest.shards.length;index++) {
    const spec=manifest.shards[index];
    const shard=shards[index];
    if (shard?.schemaVersion!==1||shard?.kind!=="english-content-editorial-decision-shard") {
      throw new TypeError("MultiWOZ editorial decision shard must use schemaVersion 1 and english-content-editorial-decision-shard kind");
    }
    for (const name of ["decisionSetId","handoffId","intakeId","recordSetDigest"]) {
      if (shard?.[name]!==manifest?.[name]) throw new TypeError("MultiWOZ editorial decision shard metadata mismatch for "+name);
    }
    if (!Array.isArray(shard?.decisions)||shard.decisions.length!==spec?.count) {
      throw new TypeError("MultiWOZ editorial decision shard count mismatch for "+String(spec?.path));
    }
    decisions.push(...shard.decisions);
  }
  if (!Number.isInteger(manifest.totalCount)||decisions.length!==manifest.totalCount) {
    throw new TypeError("MultiWOZ editorial decision totalCount does not match shard decisions");
  }
  return {
    schemaVersion:1,
    kind:"english-content-editorial-decisions",
    decisionSetId:manifest.decisionSetId,
    handoffId:manifest.handoffId,
    intakeId:manifest.intakeId,
    recordSetDigest:manifest.recordSetDigest,
    decisions,
  };
}

export function applyMultiwozDialogueEditorialDecisions(handoff,decisions,packet,intake,pin) {
  validateMultiwozDialogueEditorialHandoff(handoff,packet,intake,pin);
  assertDecisionSetMetadata(decisions,handoff);
  const decisionById=new Map();
  for (const decision of decisions.decisions) {
    const recordId=requireText(decision?.recordId,"MultiWOZ editorial decision recordId");
    if (decisionById.has(recordId)) throw new TypeError("Duplicate MultiWOZ editorial decision for "+recordId);
    decisionById.set(recordId,decision);
  }
  if (decisionById.size!==handoff.records.length) {
    throw new TypeError("MultiWOZ editorial decisions must cover every generated handoff record");
  }

  const next=structuredClone(handoff);
  for (const entry of next.records) {
    const decision=decisionById.get(entry.recordId);
    if (!decision) throw new TypeError("Missing MultiWOZ editorial decision for "+entry.recordId);
    entry.editorial=normalizeDecision(decision,entry);
  }
  const validation=validateMultiwozDialogueEditorialHandoff(next,packet,intake,pin);
  if (validation.pending!==0) throw new TypeError("Applied MultiWOZ editorial decisions must leave zero pending records");
  return {
    handoff:next,
    decisionSetId:decisions.decisionSetId,
    ...validation,
  };
}

export function multiwozEditorialDecisionsMatchHandoff(decisions,handoff) {
  return decisions?.schemaVersion===1&&
    decisions?.kind==="english-content-editorial-decisions"&&
    decisions?.handoffId===handoff?.handoffId&&
    decisions?.intakeId===handoff?.intakeId&&
    decisions?.recordSetDigest===handoff?.recordSetDigest;
}

export function stableEditorialDecisions(value) {
  return stableJson(value);
}
