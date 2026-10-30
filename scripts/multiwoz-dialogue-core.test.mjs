import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { stableJson } from "./english-content-core.mjs";
import {
  isLearningDialogue,
  multiwozDialogueSourceKey,
  multiwozDialogueSourceKeyFromRecord,
  normalizeDialogueText,
  parseMultiwozDialogue,
  selectEvenly,
  selectNextMultiwozDialogues,
} from "./multiwoz-dialogue-core.mjs";
import {
  buildMultiwozDialogueReviewIntake,
  writeImmutableReviewIntake,
} from "./multiwoz-review-intake-core.mjs";

function intakePin() {
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

function intakeRecord(sourceId,index=0) {
  const pin=intakePin();
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

function intakePacket() {
  const pin=intakePin();
  const records=[intakeRecord("D001.json",1),intakeRecord("D002.json",2)];
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
    recordSet:{recordSetId:"dialogues",records},
  };
}

test("parses a MultiWOZ 2.2 dialogue into a bounded turn model",()=>{
  const parsed=parseMultiwozDialogue({
    dialogue_id:"D1",
    services:["hotel"],
    turns:[
      {speaker:"USER",utterance:" I need a quiet hotel near the centre for a short weekend stay. "},
      {speaker:"SYSTEM",utterance:"Which price range would you prefer for the hotel, and do you need free parking?"},
      {speaker:"USER",utterance:"I would prefer a moderate price, and free parking would be helpful for our trip."},
      {speaker:"SYSTEM",utterance:"I can help with that and suggest a suitable hotel near the centre."}
    ]
  });
  assert.deepEqual(parsed?.services,["hotel"]);
  assert.equal(parsed?.turns[0]?.utterance,"I need a quiet hotel near the centre for a short weekend stay.");
  assert.equal(isLearningDialogue(parsed),true);
});

test("rejects repeated speakers and long numeric identifiers",()=>{
  assert.equal(isLearningDialogue({
    services:["train"],
    turns:[
      {speaker:"USER",utterance:"I need a train tomorrow morning."},
      {speaker:"USER",utterance:"It should leave after nine o'clock."},
      {speaker:"SYSTEM",utterance:"I can check that route for you."},
      {speaker:"USER",utterance:"Thank you for checking the route."}
    ]
  }),false);
  assert.equal(isLearningDialogue({
    services:["hotel"],
    turns:[
      {speaker:"USER",utterance:"I need a hotel near the centre."},
      {speaker:"SYSTEM",utterance:"Your booking reference is 123456789."},
      {speaker:"USER",utterance:"Thank you for the information."},
      {speaker:"SYSTEM",utterance:"Is there anything else you need?"}
    ]
  }),false);
});

test("normalization and even selection are deterministic",()=>{
  assert.equal(normalizeDialogueText("  Hello   THERE "),"hello there");
  assert.deepEqual(selectEvenly([0,1,2,3,4,5,6,7,8,9],4),[1,3,6,8]);
});

test("MultiWOZ source identity comes from dialogue id and published provenance",()=>{
  assert.equal(multiwozDialogueSourceKey({dialogueId:"PMUL0012.json"}),"PMUL0012.json");
  assert.throws(()=>multiwozDialogueSourceKey({dialogueId:""}),/source identity/);
  const record={
    scenario:"Edited scenario label",
    provenance:{sources:[{dataset:"multiwoz",sourceId:"PMUL0012.json"}]},
  };
  assert.equal(multiwozDialogueSourceKeyFromRecord(record),"PMUL0012.json");
  assert.equal(multiwozDialogueSourceKeyFromRecord({provenance:{sources:[]}}),null);
});

test("next MultiWOZ slices exclude used ids and stay prefix-monotonic",()=>{
  const candidates=[
    {dialogueId:"D050"},
    {dialogueId:"D010"},
    {dialogueId:"D040"},
    {dialogueId:"D020"},
    {dialogueId:"D030"},
    {dialogueId:"D020"},
  ];
  const excludeKeys=new Set(["D020"]);
  const firstTwo=selectNextMultiwozDialogues(candidates,2,{excludeKeys});
  const firstFour=selectNextMultiwozDialogues(candidates,4,{excludeKeys});
  assert.deepEqual(firstTwo.map(multiwozDialogueSourceKey),["D010","D030"]);
  assert.deepEqual(firstFour.map(multiwozDialogueSourceKey),["D010","D030","D040","D050"]);
  assert.deepEqual(firstFour.slice(0,firstTwo.length),firstTwo);
  assert.deepEqual(
    selectNextMultiwozDialogues([...candidates].reverse(),4,{excludeKeys}),
    firstFour,
  );
});

test("E11 MultiWOZ preparer accepts a pnpm-style argument separator",()=>{
  const script=fileURLToPath(new URL("./prepare-multiwoz-e11-dialogue-slice.mjs",import.meta.url));
  const result=spawnSync(process.execPath,[script,"--","--limit=0"],{encoding:"utf8"});
  assert.notEqual(result.status,0);
  assert.match(result.stderr,/--limit must be an integer from 1 to 200/);
  assert.doesNotMatch(result.stderr,/Unknown argument: --/);
});

test("E11 MultiWOZ review-slice preparer stays syntax-valid without requiring local source cache",()=>{
  const script=fileURLToPath(new URL("./prepare-multiwoz-e11-dialogue-slice.mjs",import.meta.url));
  const result=spawnSync(process.execPath,["--check",script],{encoding:"utf8"});
  assert.equal(result.status,0,result.stderr||result.stdout);
});

test("MultiWOZ review intake is deterministic and record-order independent",()=>{
  const pin=intakePin();
  const packet=intakePacket();
  const first=buildMultiwozDialogueReviewIntake(packet,pin);
  const shuffled=structuredClone(packet);
  shuffled.recordSet.records.reverse();
  shuffled.selection.selectedDialogueIds.reverse();
  const second=buildMultiwozDialogueReviewIntake(shuffled,pin);
  assert.equal(stableJson(second),stableJson(first));
  assert.equal(first.candidateCount,2);
  assert.equal(first.lifecycle.batchRegistration,"pending-editorial-authoring");
  assert.equal(first.lifecycle.reviewDecisions,"not-created");
  assert.equal(first.lifecycle.runtimePublication,"blocked");
});

test("MultiWOZ review intake digest changes when learning content changes",()=>{
  const pin=intakePin();
  const packet=intakePacket();
  const first=buildMultiwozDialogueReviewIntake(packet,pin);
  const changed=structuredClone(packet);
  changed.recordSet.records[0].scenario="Changed learning scenario";
  const second=buildMultiwozDialogueReviewIntake(changed,pin);
  assert.notEqual(second.recordSetDigest,first.recordSetDigest);
  assert.notEqual(second.records[0].sourceDigest,first.records[0].sourceDigest);
});

test("MultiWOZ review intake rejects duplicate ids, published state, and wrong provenance",()=>{
  const pin=intakePin();
  const duplicate=intakePacket();
  duplicate.recordSet.records[1].id=duplicate.recordSet.records[0].id;
  assert.throws(()=>buildMultiwozDialogueReviewIntake(duplicate,pin),/duplicate record id/);

  const published=intakePacket();
  published.recordSet.records[0].quality.state="published";
  assert.throws(()=>buildMultiwozDialogueReviewIntake(published,pin),/only accepts quality.state=candidate/);

  const wrongPin=intakePacket();
  wrongPin.recordSet.records[0].provenance.sources[0].snapshot="different-commit";
  assert.throws(()=>buildMultiwozDialogueReviewIntake(wrongPin,pin),/provenance does not match/);
});

test("MultiWOZ review intake output is immutable and idempotent",async()=>{
  const root=await fs.mkdtemp(path.join(os.tmpdir(),"multiwoz-intake-"));
  try {
    const file=path.join(root,"intake.json");
    const intake=buildMultiwozDialogueReviewIntake(intakePacket(),intakePin());
    assert.equal((await writeImmutableReviewIntake(file,intake)).state,"written");
    assert.equal((await writeImmutableReviewIntake(file,intake)).state,"unchanged");
    const changed=structuredClone(intake);
    changed.recordSetDigest="0".repeat(64);
    await assert.rejects(()=>writeImmutableReviewIntake(file,changed),/intake collision/);
  } finally {
    await fs.rm(root,{recursive:true,force:true});
  }
});

test("E11 MultiWOZ intake preparer accepts pnpm separator and stays syntax-valid",()=>{
  const script=fileURLToPath(new URL("./prepare-multiwoz-e11-dialogue-intake.mjs",import.meta.url));
  const syntax=spawnSync(process.execPath,["--check",script],{encoding:"utf8"});
  assert.equal(syntax.status,0,syntax.stderr||syntax.stdout);
  const result=spawnSync(process.execPath,[script,"--","--input"],{encoding:"utf8"});
  assert.notEqual(result.status,0);
  assert.match(result.stderr,/--input requires a value/);
  assert.doesNotMatch(result.stderr,/Unknown argument: --/);
});
