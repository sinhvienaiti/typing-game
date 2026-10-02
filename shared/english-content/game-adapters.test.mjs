import test from "node:test";
import assert from "node:assert/strict";
import {
  buildGameEnglishActivityDataset,
  englishActivityItemsFromRecords,
} from "./game-adapters.mjs";

const published={state:"published"};

test("adapts published collocations directly for Recall and Shooter",()=>{
  const record={
    id:"col.1",
    text:"make a decision",
    meaningVi:"đưa ra quyết định",
    quality:published,
  };
  const dataset=buildGameEnglishActivityDataset(
    "recall-typing",
    "collocation",
    [record],
    "recall-col",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  assert.deepEqual(dataset.items[0],{
    contentId:"col.1",
    entityType:"sentence",
    entityId:"col.1",
    promptText:"đưa ra quyết định",
    answerText:"make a decision",
    meaningVi:"đưa ra quyết định",
  });
});

test("adapts translation exercises to their stable source sentence id",()=>{
  const dataset=buildGameEnglishActivityDataset(
    "karaoke-typing",
    "translation",
    [{
      id:"ex.translation.1",
      type:"translation",
      prompt:"Tôi đang đợi tàu.",
      acceptedAnswers:["I am waiting for the train."],
      sourceSentenceIds:["sent.1"],
      quality:published,
    }],
    "karaoke-trans",
  );
  assert.equal(dataset.items[0].entityId,"sent.1");
  assert.equal(dataset.items[0].answerText,"I am waiting for the train.");
});

test("adapts grammar topics into Space grammar challenges",()=>{
  const dataset=buildGameEnglishActivityDataset(
    "space-typing",
    "grammar-challenge",
    [{
      id:"gr.b1.second-conditional",
      title:"Second Conditional",
      objective:"Use hypothetical present or future conditions.",
      forms:{positive:["If I had more time, I would learn another language."]},
      quality:published,
    }],
    "space-grammar",
  );
  assert.equal(dataset.items[0].entityType,"grammar");
  assert.equal(dataset.items[0].entityId,"gr.b1.second-conditional");
});

test("flattens a dialogue into bounded Karaoke sentence turns",()=>{
  const items=englishActivityItemsFromRecords("dialogue",[{
    id:"dlg.demo",
    scenario:"hotel booking",
    turns:[
      {speaker:"Learner",text:"I need a room for two nights."},
      {speaker:"Assistant",text:"What price range would you prefer?"},
    ],
    quality:published,
  }]);
  assert.equal(items.length,2);
  assert.equal(items[0].contentId,"dlg.demo.turn-01");
  assert.equal(items[0].entityId,"dlg.demo");
});

test("does not let draft or candidate content enter a runtime activity by default",()=>{
  assert.throws(
    ()=>englishActivityItemsFromRecords("collocation",[{
      id:"col.draft",
      text:"make progress",
      meaningVi:"tiến bộ",
      quality:{state:"draft"},
    }]),
    /published records only/,
  );
  assert.equal(
    englishActivityItemsFromRecords(
      "collocation",
      [{
        id:"col.draft",
        text:"make progress",
        meaningVi:"tiến bộ",
        quality:{state:"draft"},
      }],
      {allowUnpublished:true},
    ).length,
    1,
  );
});
