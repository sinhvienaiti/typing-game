import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { buildMultiwozDialogueReviewIntake } from "./multiwoz-review-intake-core.mjs";
import { buildMultiwozDialogueEditorialHandoff } from "./multiwoz-editorial-handoff-core.mjs";
import {
  buildMultiwozDialogueEditorialFinalization,
  writeImmutableEditorialFinalization,
} from "./multiwoz-editorial-finalization-core.mjs";

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

function candidate(sourceId,index=0) {
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
        naturalness:{status:"pending",method:"fixture"},
        cefr:{status:"pending",method:"fixture"},
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

function fixtures() {
  const pin=pinFixture();
  const packet={
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
    recordSet:{recordSetId:"dialogues",records:[candidate("D001.json",1),candidate("D002.json",2)]},
  };
  const intake=buildMultiwozDialogueReviewIntake(packet,pin);
  const handoff=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  return {pin,packet,intake,handoff};
}

function completeChecks(entry,status="pass") {
  for (const name of Object.keys(entry.editorial.checks)) entry.editorial.checks[name]=status;
}

test("finalization blocks pending editorial work and never auto-publishes",()=>{
  const {pin,packet,intake,handoff}=fixtures();
  assert.throws(
    ()=>buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin),
    /still has 2 pending record/,
  );
});

test("finalization turns accepted records into draft authoring data and excludes rejected records",()=>{
  const {pin,packet,intake,handoff}=fixtures();
  handoff.records[0].editorial.disposition="accept";
  handoff.records[0].editorial.cefr="A2";
  completeChecks(handoff.records[0]);
  handoff.records[1].editorial.disposition="reject";
  handoff.records[1].editorial.notes="Dialogue is not suitable for the bounded learning slice.";

  const result=buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin);
  assert.equal(result.authoring.records.length,1);
  assert.equal(result.authoring.records[0].quality.state,"draft");
  assert.equal(result.authoring.records[0].provenance.sources[0].modified,false);
  assert.equal(result.proposal.acceptedCount,1);
  assert.equal(result.proposal.editedCount,0);
  assert.equal(result.proposal.rejectedCount,1);
  assert.equal(result.proposal.batch.state,"draft");
  assert.equal(result.proposal.batch.recordSets[0].expectedCount,1);
  assert.equal(result.proposal.lifecycle.batchRegistration,"ready-for-manifest-registration");
  assert.equal(result.proposal.lifecycle.reviewDecisions,"not-created");
  assert.equal(result.proposal.lifecycle.runtimePublication,"blocked");
  assert.equal(JSON.stringify(result).includes('"published"'),false);
});

test("edited records require a real editorial change and preserve pinned provenance identity",()=>{
  const {pin,packet,intake,handoff}=fixtures();
  handoff.records[0].editorial.disposition="edit";
  handoff.records[0].editorial.cefr="B1";
  completeChecks(handoff.records[0]);
  handoff.records[1].editorial.disposition="reject";
  handoff.records[1].editorial.notes="Rejected during editorial review.";
  assert.throws(
    ()=>buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin),
    /edit disposition must provide an edited scenario or turns/,
  );

  handoff.records[0].editorial.scenario="Booking a hotel for a weekend stay";
  const result=buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin);
  const record=result.authoring.records[0];
  assert.equal(record.scenario,"Booking a hotel for a weekend stay");
  assert.equal(record.cefr,"B1");
  assert.equal(record.provenance.sources[0].modified,true);
  assert.equal(record.provenance.sources[0].snapshot,pin.commit);
  assert.equal(record.provenance.sources[0].sourceId,"D001.json");
});

test("accepted records require completed checks and rejected records require notes",()=>{
  const {pin,packet,intake,handoff}=fixtures();
  handoff.records[0].editorial.disposition="accept";
  handoff.records[0].editorial.cefr="A2";
  completeChecks(handoff.records[0]);
  handoff.records[0].editorial.checks.grammar="pending";
  handoff.records[1].editorial.disposition="reject";
  handoff.records[1].editorial.notes="Not suitable.";
  assert.throws(
    ()=>buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin),
    /editorial check grammar must be pass or not-applicable/,
  );

  handoff.records[0].editorial.checks.grammar="pass";
  handoff.records[1].editorial.notes="";
  assert.throws(
    ()=>buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin),
    /rejection notes must be a non-empty string/,
  );
});

test("finalization outputs are immutable and idempotent",async()=>{
  const {pin,packet,intake,handoff}=fixtures();
  handoff.records[0].editorial.disposition="accept";
  handoff.records[0].editorial.cefr="A2";
  completeChecks(handoff.records[0]);
  handoff.records[1].editorial.disposition="reject";
  handoff.records[1].editorial.notes="Not suitable.";
  const result=buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin);
  const root=await fs.mkdtemp(path.join(os.tmpdir(),"multiwoz-finalization-"));
  try {
    const files={authoringPath:path.join(root,"authoring.json"),proposalPath:path.join(root,"proposal.json")};
    await writeImmutableEditorialFinalization(files,result);
    await writeImmutableEditorialFinalization(files,result);
    const changed=structuredClone(result);
    changed.proposal.lifecycle.runtimePublication="published";
    await assert.rejects(()=>writeImmutableEditorialFinalization(files,changed),/finalization collision/);
  } finally {
    await fs.rm(root,{recursive:true,force:true});
  }
});

test("E11 MultiWOZ editorial finalizer accepts pnpm separator and is syntax-valid",()=>{
  const script=fileURLToPath(new URL("./finalize-multiwoz-e11-dialogue-editorial-handoff.mjs",import.meta.url));
  const syntax=spawnSync(process.execPath,["--check",script],{encoding:"utf8"});
  assert.equal(syntax.status,0,syntax.stderr||syntax.stdout);
  const result=spawnSync(process.execPath,[script,"--","--handoff"],{encoding:"utf8"});
  assert.notEqual(result.status,0);
  assert.match(result.stderr,/--handoff requires a value/);
  assert.doesNotMatch(result.stderr,/Unknown argument: --/);
});
