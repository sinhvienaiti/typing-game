import test from "node:test";
import assert from "node:assert/strict";
import { buildMultiwozDialogueReviewIntake } from "./multiwoz-review-intake-core.mjs";
import { buildMultiwozDialogueEditorialHandoff } from "./multiwoz-editorial-handoff-core.mjs";
import { buildMultiwozDialogueEditorialFinalization } from "./multiwoz-editorial-finalization-core.mjs";
import {
  applyMultiwozDialogueEditorialDecisions,
  buildMultiwozEditorialDecisionSet,
  multiwozEditorialDecisionsMatchHandoff,
} from "./multiwoz-editorial-decision-core.mjs";

function fixture() {
  const pin={
    version:"2.2",repository:"budzianowski/multiwoz",commit:"pin",path:"a.json",blobSha1:"a",
    license:"MIT",attribution:"MultiWOZ",additionalFiles:[],
  };
  const candidate={
    schemaVersion:1,id:"dlg.multiwoz.d001.json",scenario:"restaurant service conversation",
    turns:[
      {speaker:"Learner",text:"I need a moderately priced restaurant near the centre."},
      {speaker:"Assistant",text:"What type of food would you like to eat today?"},
      {speaker:"Learner",text:"Italian food would be good. Please recommend a place."},
      {speaker:"Assistant",text:"I can recommend an Italian restaurant in the centre."},
    ],
    quality:{state:"candidate",checks:{schema:{status:"pass"},sourcePin:{status:"pass"},naturalness:{status:"pending"},cefr:{status:"pending"}}},
    provenance:{sources:[{dataset:"multiwoz",sourceId:"D001.json",sourceUrl:"https://github.com/budzianowski/multiwoz/blob/pin/a.json",snapshot:"pin",license:"MIT",attribution:"MultiWOZ",modified:false}]},
  };
  const packet={
    schemaVersion:1,kind:"english-content-review-packet",batchFamily:"e11.dialogue-multiwoz",
    source:{dataset:"multiwoz",version:"2.2",repository:"budzianowski/multiwoz",commit:"pin",observedFiles:[{path:"a.json",blobSha1:"a"}],pinned:true},
    selection:{requestedLimit:1,selectedDialogueIds:["D001.json"]},recordSet:{recordSetId:"dialogues",records:[candidate]},
  };
  const intake=buildMultiwozDialogueReviewIntake(packet,pin);
  const handoff=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  const decisions={
    schemaVersion:1,kind:"english-content-editorial-decisions",decisionSetId:"slice-01",
    handoffId:handoff.handoffId,intakeId:handoff.intakeId,recordSetDigest:handoff.recordSetDigest,
    decisions:[{
      recordId:handoff.records[0].recordId,sourceDigest:handoff.records[0].sourceDigest,disposition:"edit",cefr:"A2",
      scenario:"Choosing an Italian restaurant",
      turns:[
        {speaker:"Learner",text:"I need a moderately priced restaurant near the centre."},
        {speaker:"Assistant",text:"What type of food would you like?"},
        {speaker:"Learner",text:"Italian food would be good. Please recommend a place."},
        {speaker:"Assistant",text:"I can recommend an Italian restaurant in the centre."},
      ],
      checks:{exactDuplicate:"pass",nearDuplicate:"pass",grammar:"pass",naturalness:"pass",cefr:"pass",license:"pass"},
      notes:"Editorial normalization completed.",
    }],
  };
  return {pin,packet,intake,handoff,decisions};
}

test("applies digest-bound editorial decisions without touching candidate snapshots",()=>{
  const {pin,packet,intake,handoff,decisions}=fixture();
  const snapshot=structuredClone(handoff.records[0].candidateSnapshot);
  const result=applyMultiwozDialogueEditorialDecisions(handoff,decisions,packet,intake,pin);
  assert.equal(result.pending,0);
  assert.equal(result.edited,1);
  assert.deepEqual(result.handoff.records[0].candidateSnapshot,snapshot);
  assert.equal(result.handoff.records[0].editorial.cefr,"A2");
  const finalization=buildMultiwozDialogueEditorialFinalization(result.handoff,packet,intake,pin);
  assert.equal(finalization.authoring.records[0].quality.state,"draft");
  assert.equal(finalization.proposal.lifecycle.reviewDecisions,"not-created");
  assert.equal(finalization.proposal.lifecycle.runtimePublication,"blocked");
});

test("rejects stale source digests and incomplete decision coverage",()=>{
  const {pin,packet,intake,handoff,decisions}=fixture();
  const stale=structuredClone(decisions);
  stale.decisions[0].sourceDigest="stale";
  assert.throws(()=>applyMultiwozDialogueEditorialDecisions(handoff,stale,packet,intake,pin),/sourceDigest is stale/);
  const missing=structuredClone(decisions);
  missing.decisions=[];
  assert.throws(()=>applyMultiwozDialogueEditorialDecisions(handoff,missing,packet,intake,pin),/cover every generated handoff record/);
});

test("detects whether a committed decision set is bound to the current generated slice",()=>{
  const {handoff,decisions}=fixture();
  assert.equal(multiwozEditorialDecisionsMatchHandoff(decisions,handoff),true);
  const next=structuredClone(handoff);
  next.recordSetDigest="different";
  assert.equal(multiwozEditorialDecisionsMatchHandoff(decisions,next),false);
});

test("combines deterministic decision shards and rejects metadata drift",()=>{
  const {handoff,decisions}=fixture();
  const manifest={
    schemaVersion:1,kind:"english-content-editorial-decision-manifest",decisionSetId:decisions.decisionSetId,
    handoffId:decisions.handoffId,intakeId:decisions.intakeId,recordSetDigest:decisions.recordSetDigest,totalCount:1,
    shards:[{path:"decisions-001.json",count:1}],
  };
  const shard={...structuredClone(decisions),kind:"english-content-editorial-decision-shard"};
  const merged=buildMultiwozEditorialDecisionSet(manifest,[shard]);
  assert.equal(merged.decisions.length,1);
  assert.equal(multiwozEditorialDecisionsMatchHandoff(merged,handoff),true);
  const drift=structuredClone(shard);
  drift.recordSetDigest="stale";
  assert.throws(()=>buildMultiwozEditorialDecisionSet(manifest,[drift]),/metadata mismatch/);
});
