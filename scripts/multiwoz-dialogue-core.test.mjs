import test from "node:test";
import assert from "node:assert/strict";
import {
  isLearningDialogue,
  multiwozDialogueSourceKey,
  multiwozDialogueSourceKeyFromRecord,
  normalizeDialogueText,
  parseMultiwozDialogue,
  selectEvenly,
  selectNextMultiwozDialogues,
} from "./multiwoz-dialogue-core.mjs";

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
