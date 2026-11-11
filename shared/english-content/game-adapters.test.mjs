import test from "node:test";
import assert from "node:assert/strict";
import {
  buildGameEnglishActivityDataset,
  englishActivityItemsFromRecords,
  hasVerifiedTargetAttribution,
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

test("adapts Monkeytype grammar-topic and cloze smoke records",()=>{
  const grammar=buildGameEnglishActivityDataset(
    "monkeytype",
    "grammar-topic",
    [{
      id:"gr.a1.present-simple-routines",
      title:"Present Simple",
      objective:"Describe repeated routines.",
      forms:{positive:["I work at home."]},
      quality:published,
    }],
    "monkey-grammar",
  );
  assert.equal(grammar.items[0].entityType,"grammar");
  assert.equal(grammar.items[0].entityId,"gr.a1.present-simple-routines");

  const cloze=buildGameEnglishActivityDataset(
    "monkeytype",
    "cloze",
    [{
      id:"ex.cloze.1",
      type:"cloze",
      prompt:"She ___ the bus every morning.",
      acceptedAnswers:["takes"],
      sourceSentenceIds:["sent.1"],
      quality:published,
    }],
    "monkey-cloze",
  );
  assert.equal(cloze.items[0].entityType,"sentence");
  assert.equal(cloze.items[0].entityId,"sent.1");
  assert.equal(cloze.items[0].answerText,"takes");
});

test("adapts Monkeytype verb patterns and idioms without inventing mastery entity types",()=>{
  const pattern=buildGameEnglishActivityDataset(
    "monkeytype",
    "verb-pattern",
    [{
      id:"pat.1",
      lemma:"want",
      frame:"verb + to-infinitive",
      explanationVi:"Dùng want + to V để diễn tả điều muốn làm.",
      quality:published,
    }],
    "monkey-pattern",
  );
  assert.equal(pattern.items[0].entityType,"sentence");
  assert.match(pattern.items[0].answerText,/want/);

  const idiom=buildGameEnglishActivityDataset(
    "monkeytype",
    "idiom",
    [{
      id:"idiom.1",
      type:"idiom",
      text:"break the ice",
      meaningVi:"phá tan sự ngượng ngùng ban đầu",
      quality:published,
    }],
    "monkey-idiom",
  );
  assert.equal(idiom.items[0].entityType,"sentence");
  assert.equal(idiom.items[0].answerText,"break the ice");
});

test("preserves multi-answer alternatives and guards unverified rotational E11 targets",()=>{
  const dataset=buildGameEnglishActivityDataset(
    "monkeytype",
    "transformation",
    [{
      id:"ex.transformation.e11.01.004",
      type:"transformation",
      prompt:"Rewrite as a negative sentence.\nSource: If it rains, we will take a taxi.",
      targetIds:["gr.a2.first-conditional"],
      acceptedAnswers:[
        "If it rains, we will not take a taxi.",
        "If it rains, we won't take a taxi.",
      ],
      sourceSentenceIds:["sent.tatoeba.9999"],
      cefr:"A2",
      quality:published,
    }],
    "monkey-multi",
    {includeGrading:true},
  );
  assert.equal(dataset.items[0].answerText,"If it rains, we will not take a taxi.");
  assert.deepEqual(dataset.items[0].acceptedAnswers,[
    "If it rains, we will not take a taxi.",
    "If it rains, we won't take a taxi.",
  ]);
  assert.equal(dataset.items[0].targetConfidence,"unverified-rotational");
  assert.equal(hasVerifiedTargetAttribution({id:"ex.cloze.gra1.01.02",sourceSentenceIds:["sent.gra1.01.02.2"]}),true);
  assert.equal(hasVerifiedTargetAttribution({id:"ex.cloze.e11.01.020",sourceSentenceIds:["sent.tatoeba.123"]}),false);
});
