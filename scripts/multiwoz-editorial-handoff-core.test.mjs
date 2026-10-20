import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { stableJson } from "./english-content-core.mjs";
import { buildMultiwozDialogueReviewIntake } from "./multiwoz-review-intake-core.mjs";
import {
  buildMultiwozDialogueEditorialHandoff,
  validateMultiwozDialogueEditorialHandoff,
  writeImmutableEditorialHandoff,
} from "./multiwoz-editorial-handoff-core.mjs";

function pinFixture() {
  return {
    version:"2.2",
    repository:"budzianowski/multiwoz",
    commit:"fe0c8e65cfcd8462bd33c86e35f21addc84ca82b",
    path:"data/MultiWOZ_2.2/train/dialogues_001.json",
    blobSha1:"1ab08d377750e83493095b0eb1249df81a99ba21",
    license:"MIT",
    attribution:"MultiWOZ 2.2 · Paweł Budzianowski and contributors",
    additionalFiles:[{
      path:"data/MultiWOZ_2.2/train/dialogues_002.json",
      blobSha1:"d182eae43341a44ebe3807ed61e829d73dc34a84",
    }],
  };
}

function recordFixture(sourceId,index=0) {
  const pin=pinFixture();
  return {
    schemaVersion:1,
    id:"dlg.multiwoz."+sourceId.toLocaleLowerCase("en-US"),
    scenario:"hotel service conversation "+String(index),
    turns:[
      {speaker:"Learner",text:"I need a quiet hotel near the centre for a short weekend stay."},
      {speaker:"Assistant",text:"Which price range would you prefer, and do you need free parking?"},
      {speaker:"Learner",text:"I would prefer a moderate price, and free parking would be helpful."},
      {speaker:"Assistant",text:"I can help with that and suggest a suitable hotel near the centre."},
    ],
    quality:{
      state:"candidate",
      checks:{
        schema:{status:"pass",method:"fixture"},
        sourcePin:{status:"pass",method:"fixture"},
        naturalness:{status:"pending",method:"editor-review-required"},
        cefr:{status:"pending",method:"cefr-review-required"},
      },
    },
    provenance:{
      sources:[{
        dataset:"multiwoz",
        sourceId,
        sourceUrl:"https://github.com/"+pin.repository+"/blob/"+pin.commit+"/"+pin.path,
        snapshot:pin.commit,
        license:pin.license,
        attribution:pin.attribution,
        modified:false,
      }],
    },
  };
}

function packetFixture() {
  const pin=pinFixture();
  return {
    schemaVersion:1,
    kind:"english-content-review-packet",
    batchFamily:"e11.dialogue-multiwoz",
    source:{
      dataset:"multiwoz",
      version:pin.version,
      repository:pin.repository,
      commit:pin.commit,
      observedFiles:[
        {path:pin.path,blobSha1:pin.blobSha1},
        ...pin.additionalFiles,
      ],
      pinned:true,
    },
    selection:{requestedLimit:2,selectedDialogueIds:["D001.json","D002.json"]},
    recordSet:{
      recordSetId:"dialogues",
      records:[recordFixture("D001.json",1),recordFixture("D002.json",2)],
    },
  };
}

function boundFixtures() {
  const pin=pinFixture();
  const packet=packetFixture();
  const intake=buildMultiwozDialogueReviewIntake(packet,pin);
  return {pin,packet,intake};
}

test("MultiWOZ editorial handoff is deterministic, pending-only, and intake-bound",()=>{
  const {pin,packet,intake}=boundFixtures();
  const first=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  const shuffled=structuredClone(packet);
  shuffled.recordSet.records.reverse();
  const second=buildMultiwozDialogueEditorialHandoff(shuffled,intake,pin);
  assert.equal(stableJson(second),stableJson(first));
  assert.equal(first.recordSetDigest,intake.recordSetDigest);
  assert.equal(first.lifecycle.batchRegistration,"blocked-until-editorial-authoring");
  assert.equal(first.lifecycle.reviewDecisions,"not-created");
  assert.equal(first.lifecycle.runtimePublication,"blocked");
  assert.equal(first.records.every(record=>record.editorial.disposition==="pending"),true);
  assert.equal(stableJson(first).includes("targetState"),false);
  assert.equal(stableJson(first).includes('"published"'),false);
  assert.deepEqual(validateMultiwozDialogueEditorialHandoff(first,packet,intake,pin),{
    recordCount:2,
    pending:2,
    accepted:0,
    edited:0,
    rejected:0,
  });
});

test("MultiWOZ editorial handoff rejects intake drift and candidate snapshot edits",()=>{
  const {pin,packet,intake}=boundFixtures();
  const wrongIntake=structuredClone(intake);
  wrongIntake.recordSetDigest="0".repeat(64);
  assert.throws(
    ()=>buildMultiwozDialogueEditorialHandoff(packet,wrongIntake,pin),
    /intake does not match/,
  );

  const handoff=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  handoff.records[0].candidateSnapshot.scenario="Changed after binding";
  assert.throws(
    ()=>validateMultiwozDialogueEditorialHandoff(handoff,packet,intake,pin),
    /candidateSnapshot no longer matches/,
  );
});

test("MultiWOZ editorial handoff allows explicit editorial states but never targetState",()=>{
  const {pin,packet,intake}=boundFixtures();
  const handoff=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  handoff.records[0].editorial.disposition="accept";
  handoff.records[0].editorial.cefr="B1";
  handoff.records[0].editorial.checks.grammar="pass";
  const validation=validateMultiwozDialogueEditorialHandoff(handoff,packet,intake,pin);
  assert.equal(validation.accepted,1);
  assert.equal(validation.pending,1);

  handoff.records[0].editorial.targetState="published";
  assert.throws(
    ()=>validateMultiwozDialogueEditorialHandoff(handoff,packet,intake,pin),
    /must not contain targetState/,
  );
});

test("MultiWOZ editorial handoff output is immutable and idempotent",async()=>{
  const {pin,packet,intake}=boundFixtures();
  const root=await fs.mkdtemp(path.join(os.tmpdir(),"multiwoz-handoff-"));
  try {
    const file=path.join(root,"handoff.json");
    const handoff=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
    assert.equal((await writeImmutableEditorialHandoff(file,handoff)).state,"written");
    assert.equal((await writeImmutableEditorialHandoff(file,handoff)).state,"unchanged");
    const changed=structuredClone(handoff);
    changed.records[0].editorial.notes="different bytes";
    await assert.rejects(()=>writeImmutableEditorialHandoff(file,changed),/handoff collision/);
  } finally {
    await fs.rm(root,{recursive:true,force:true});
  }
});

test("E11 MultiWOZ editorial handoff preparer accepts pnpm separator and is syntax-valid",()=>{
  const script=fileURLToPath(new URL("./prepare-multiwoz-e11-dialogue-editorial-handoff.mjs",import.meta.url));
  const syntax=spawnSync(process.execPath,["--check",script],{encoding:"utf8"});
  assert.equal(syntax.status,0,syntax.stderr||syntax.stdout);
  const result=spawnSync(process.execPath,[script,"--","--packet"],{encoding:"utf8"});
  assert.notEqual(result.status,0);
  assert.match(result.stderr,/--packet requires a value/);
  assert.doesNotMatch(result.stderr,/Unknown argument: --/);
});
