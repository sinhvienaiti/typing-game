import test from "node:test";
import assert from "node:assert/strict";
import { buildMultiwozDialogueReviewIntake } from "../../scripts/multiwoz-review-intake-core.mjs";
import {
  multiwozDialogueRecordId,
  selectNextMultiwozDialogues,
} from "../../scripts/multiwoz-dialogue-core.mjs";

function pin() {
  return {
    version:"2.2",
    repository:"budzianowski/multiwoz",
    commit:"fe0c8e65cfcd8462bd33c86e35f21addc84ca82b",
    path:"data/MultiWOZ_2.2/train/dialogues_001.json",
    blobSha1:"1ab08d377750e83493095b0eb1249df81a99ba21",
    license:"MIT",
    attribution:"MultiWOZ 2.2 · Paweł Budzianowski and contributors",
  };
}

function record(sourceId) {
  const sourcePin=pin();
  return {
    schemaVersion:1,
    id:"dlg.multiwoz."+sourceId.toLocaleLowerCase("en-US"),
    scenario:"hotel service conversation",
    turns:[
      {speaker:"Learner",text:"I need a quiet hotel near the centre for a short weekend stay."},
      {speaker:"Assistant",text:"Which price range would you prefer, and do you need free parking?"},
      {speaker:"Learner",text:"I would prefer a moderate price, and free parking would be helpful."},
      {speaker:"Assistant",text:"I can help with that and suggest a suitable hotel near the centre."},
    ],
    quality:{state:"candidate",checks:{sourcePin:{status:"pass",method:"fixture"}}},
    provenance:{sources:[{
      dataset:"multiwoz",
      sourceId,
      sourceUrl:"https://github.com/"+sourcePin.repository+"/blob/"+sourcePin.commit+"/"+sourcePin.path,
      snapshot:sourcePin.commit,
      license:sourcePin.license,
      attribution:sourcePin.attribution,
      modified:false,
    }]},
  };
}

function packet(requestedLimit=3) {
  const sourcePin=pin();
  const records=[record("D001.json"),record("D002.json")];
  return {
    schemaVersion:1,
    kind:"english-content-review-packet",
    batchFamily:"e11.dialogue-multiwoz",
    source:{
      dataset:"multiwoz",
      version:sourcePin.version,
      repository:sourcePin.repository,
      commit:sourcePin.commit,
      observedFiles:[{path:sourcePin.path,blobSha1:sourcePin.blobSha1}],
      pinned:true,
    },
    selection:{
      requestedLimit,
      selectedDialogueIds:records.map(item=>item.provenance.sources[0].sourceId),
    },
    recordSet:{recordSetId:"dialogues",records},
  };
}

test("MultiWOZ selector returns a deterministic final partial remainder",()=>{
  const candidates=[
    {dialogueId:"D003.json"},
    {dialogueId:"D001.json"},
    {dialogueId:"D002.json"},
  ];
  const selected=selectNextMultiwozDialogues(candidates,24,{excludeKeys:new Set(["D001.json"])});
  assert.deepEqual(selected.map(item=>item.dialogueId),["D002.json","D003.json"]);
});

test("MultiWOZ selector stays deterministic after editorial-reject prefiltering",()=>{
  const candidates=[
    {dialogueId:"D004.json"},
    {dialogueId:"D002.json"},
    {dialogueId:"D003.json"},
    {dialogueId:"D001.json"},
  ];
  const rejectedRecordIds=new Set(["dlg.multiwoz.d002.json"]);
  const eligible=candidates.filter(item=>!rejectedRecordIds.has(multiwozDialogueRecordId(item)));
  const selected=selectNextMultiwozDialogues(eligible,2,{excludeKeys:new Set(["D001.json"])});
  assert.deepEqual(selected.map(item=>item.dialogueId),["D003.json","D004.json"]);
  const reversedEligible=[...candidates].reverse()
    .filter(item=>!rejectedRecordIds.has(multiwozDialogueRecordId(item)));
  assert.deepEqual(
    selectNextMultiwozDialogues(reversedEligible,2,{excludeKeys:new Set(["D001.json"])}),
    selected,
  );
});

test("MultiWOZ intake accepts a deterministic final partial slice",()=>{
  const intake=buildMultiwozDialogueReviewIntake(packet(3),pin());
  assert.equal(intake.candidateCount,2);
  assert.equal(intake.records.length,2);
});

test("MultiWOZ intake still rejects a slice larger than requestedLimit",()=>{
  assert.throws(
    ()=>buildMultiwozDialogueReviewIntake(packet(1),pin()),
    /record count must not exceed selection\.requestedLimit/,
  );
});
