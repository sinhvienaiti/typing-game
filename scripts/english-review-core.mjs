import crypto from "node:crypto";
import { stableJson } from "./english-content-core.mjs";

const STATE_RANK=Object.freeze({
  candidate:0,
  draft:0,
  validated:1,
  reviewed:2,
  published:3,
  deprecated:4,
});

export function englishContentRecordId(record,index=0) {
  const value=record?.id??record?.lexemeId;
  if (typeof value==="string"&&value.trim()!=="") return value;
  return "#"+String(index+1);
}

export function englishContentRecordDigest(record) {
  return crypto.createHash("sha256").update(stableJson(record)).digest("hex");
}

export function buildEnglishReviewDecisionIndex(ledger) {
  const result=new Map();
  for (const decision of ledger?.decisions??[]) {
    const key=decision.batchId+"\u0000"+decision.recordSetId+"\u0000"+decision.recordId;
    if (result.has(key)) throw new TypeError("duplicate review decision target: "+decision.batchId+"/"+decision.recordSetId+"/"+decision.recordId);
    result.set(key,decision);
  }
  return result;
}

function stateRank(value) {
  return Object.hasOwn(STATE_RANK,value)?STATE_RANK[value]:-1;
}

export function applyEnglishReviewDecision(record,decision,options={}) {
  if (!decision) return structuredClone(record);
  const id=englishContentRecordId(record);
  if (id!==decision.recordId) throw new TypeError("review decision recordId mismatch: "+decision.id);
  const digest=englishContentRecordDigest(record);
  if (digest!==decision.sourceDigest) {
    throw new TypeError(decision.id+": sourceDigest is stale; expected "+digest+", got "+decision.sourceDigest);
  }

  const currentState=record?.quality?.state;
  if (stateRank(currentState)<0) throw new TypeError(decision.id+": source record has invalid quality state");
  if (decision.targetState!=="deprecated"&&stateRank(decision.targetState)<stateRank(currentState)) {
    throw new TypeError(decision.id+": review decision cannot move quality state backwards");
  }

  const checks={
    ...(record?.quality?.checks??{}),
    ...structuredClone(decision.checks),
  };
  const requiredChecks=options.requiredChecks??[];
  for (const name of requiredChecks) {
    const status=checks?.[name]?.status;
    if (decision.targetState==="published"&&status!=="pass"&&status!=="not-applicable") {
      throw new TypeError(decision.id+": publication requires completed check "+name);
    }
  }
  if (decision.targetState==="published") {
    for (const [name,check] of Object.entries(checks)) {
      if (check?.status==="pending"||check?.status==="fail") {
        throw new TypeError(decision.id+": publication blocked by "+name+"="+check.status);
      }
    }
  }

  return {
    ...structuredClone(record),
    quality:{
      state:decision.targetState,
      checks,
    },
  };
}

export function overlayEnglishReviewDecisions(records,ledger,context) {
  const index=buildEnglishReviewDecisionIndex(ledger);
  return records.map((record,position)=>{
    const recordId=englishContentRecordId(record,position);
    const key=context.batchId+"\u0000"+context.recordSetId+"\u0000"+recordId;
    return applyEnglishReviewDecision(record,index.get(key),{
      requiredChecks:context.requiredChecks??[],
    });
  });
}
