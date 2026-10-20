import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { buildMultiwozDialogueReviewIntake } from "./multiwoz-review-intake-core.mjs";
import { buildMultiwozDialogueEditorialHandoff } from "./multiwoz-editorial-handoff-core.mjs";
import { buildMultiwozDialogueEditorialFinalization } from "./multiwoz-editorial-finalization-core.mjs";
import { registerMultiwozDialogueBatchManifest } from "./multiwoz-batch-registration-core.mjs";
import { parseArgs } from "./register-multiwoz-e11-dialogue-batch.mjs";

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

function candidate(pin) {
  return {
    schemaVersion:1,
    id:"dlg.multiwoz.d001.json",
    scenario:"hotel service conversation",
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
        sourceId:"D001.json",
        sourceUrl:"https://github.com/"+pin.repository+"/blob/"+pin.commit+"/"+pin.path,
        snapshot:pin.commit,
        license:pin.license,
        attribution:pin.attribution,
        modified:false,
      }],
    },
  };
}

function fixture({complete=true}={}) {
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
    selection:{requestedLimit:1,selectedDialogueIds:["D001.json"]},
    recordSet:{recordSetId:"dialogues",records:[candidate(pin)]},
  };
  const intake=buildMultiwozDialogueReviewIntake(packet,pin);
  const handoff=buildMultiwozDialogueEditorialHandoff(packet,intake,pin);
  if (complete) {
    const entry=handoff.records[0];
    entry.editorial.disposition="accept";
    entry.editorial.cefr="A2";
    for (const name of Object.keys(entry.editorial.checks)) entry.editorial.checks[name]="pass";
  }
  const finalization=complete
    ?buildMultiwozDialogueEditorialFinalization(handoff,packet,intake,pin)
    :{authoring:{schemaVersion:1,records:[]},proposal:{batch:{}}};
  return {
    pin,
    packet,
    intake,
    handoff,
    ...finalization,
    manifest:{schemaVersion:1,contentVersion:"2026.10.0",batches:[]},
  };
}

test("registrar appends a validated draft batch and remains idempotent",()=>{
  const data=fixture();
  const first=registerMultiwozDialogueBatchManifest(data);
  assert.equal(first.status,"registered");
  assert.equal(first.manifest.batches.length,1);
  assert.deepEqual(first.manifest.batches[0],data.proposal.batch);
  assert.equal(first.reviewDecisions,"not-created");
  assert.equal(first.runtimePublication,"blocked");
  assert.equal(data.manifest.batches.length,0,"input manifest must not be mutated");

  const second=registerMultiwozDialogueBatchManifest({...data,manifest:first.manifest});
  assert.equal(second.status,"already-registered");
  assert.equal(second.manifest,first.manifest,"idempotent registration returns the existing manifest");
  assert.equal(second.manifest.batches.length,1);
});

test("registrar rejects same batch id with different manifest bytes",()=>{
  const data=fixture();
  const conflicting=structuredClone(data.proposal.batch);
  conflicting.recordSets[0].expectedCount=99;
  data.manifest.batches.push(conflicting);
  assert.throws(
    ()=>registerMultiwozDialogueBatchManifest(data),
    /Batch registration collision/,
  );
});

test("registrar rejects a record-set path already owned by another batch",()=>{
  const data=fixture();
  data.manifest.batches.push({
    id:"e10.other-batch",
    phase:"E10",
    category:"sentences",
    cefr:["A2"],
    state:"draft",
    recordSets:[{
      id:"other",
      path:data.proposal.batch.recordSets[0].path,
      expectedCount:1,
      generated:false,
      allowedQualityStates:["draft"],
      requiredChecks:["schema"],
    }],
    requiredBeforePublish:["schema-review"],
    gameSmokes:[],
  });
  assert.throws(
    ()=>registerMultiwozDialogueBatchManifest(data),
    /path collision/,
  );
});

test("registrar cannot bypass pending editorial handoff",()=>{
  const pending=fixture({complete:false});
  assert.throws(
    ()=>registerMultiwozDialogueBatchManifest(pending),
    /still has 1 pending record/,
  );
});

test("registrar CLI is dry-run by default and accepts pnpm separator",()=>{
  assert.equal(parseArgs([]).write,false);
  assert.equal(parseArgs(["--","--write"]).write,true);
  const script=fileURLToPath(new URL("./register-multiwoz-e11-dialogue-batch.mjs",import.meta.url));
  const syntax=spawnSync(process.execPath,["--check",script],{encoding:"utf8"});
  assert.equal(syntax.status,0,syntax.stderr||syntax.stdout);
  const result=spawnSync(process.execPath,[script,"--","--manifest"],{encoding:"utf8"});
  assert.notEqual(result.status,0);
  assert.match(result.stderr,/--manifest requires a value/);
  assert.doesNotMatch(result.stderr,/Unknown argument: --/);
});
