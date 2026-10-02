import test from "node:test";
import assert from "node:assert/strict";
import {
  isLearningDialogue,
  normalizeDialogueText,
  parseMultiwozDialogue,
  selectEvenly,
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
  assert.equal(parsed?.turns[0]?.utterance,"I need a quiet hotel.");
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
