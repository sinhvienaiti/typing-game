import test from "node:test";
import assert from "node:assert/strict";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
  loadPublishedEnglishActivityRecords,
} from "./activity-source.mjs";

const published={state:"published"};
function fakeLoader(groups){
  return {
    async loadDataset(dataset,{prefix}={}){
      return groups[dataset+":"+String(prefix??"")]??[];
    },
  };
}

test("loads only published records for the requested exercise type",async()=>{
  const loader=fakeLoader({
    "sentences:exercises-":[
      {id:"ex.cloze.1",type:"cloze",quality:published},
      {id:"ex.translation.1",type:"translation",quality:published},
      {id:"ex.translation.draft",type:"translation",quality:{state:"draft"}},
    ],
  });
  const records=await loadPublishedEnglishActivityRecords(loader,"translation",{limit:10});
  assert.deepEqual(records.map(record=>record.id),["ex.translation.1"]);
  assert.equal(await countPublishedEnglishActivityRecords(loader,"translation"),1);
});

test("builds a bounded Karaoke translation dataset from published runtime records",async()=>{
  const loader=fakeLoader({
    "sentences:exercises-":[{
      id:"ex.translation.1",
      type:"translation",
      prompt:"Tôi đang đợi tàu.",
      acceptedAnswers:["I am waiting for the train."],
      sourceSentenceIds:["sent.1"],
      quality:published,
    }],
  });
  const dataset=await buildPublishedGameEnglishActivityDataset(
    loader,
    "karaoke-typing",
    "karaoke",
    "translation",
    "karaoke-runtime-1",
    {limit:20,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  assert.equal(dataset.items.length,1);
  assert.equal(dataset.items[0].entityId,"sent.1");
});

test("builds Space grammar challenge from published topics",async()=>{
  const loader=fakeLoader({
    "grammar:topics-":[{
      id:"gr.a1.present-simple-routines",
      title:"Present Simple",
      objective:"Describe repeated routines.",
      forms:{positive:["I work at home."]},
      quality:published,
    }],
  });
  const dataset=await buildPublishedGameEnglishActivityDataset(
    loader,
    "space-typing",
    "space",
    "grammar-challenge",
    "space-runtime-1",
  );
  assert.equal(dataset.items[0].entityType,"grammar");
  assert.equal(dataset.items[0].entityId,"gr.a1.present-simple-routines");
});

test("refuses unsupported game/activity combinations",async()=>{
  const loader=fakeLoader({"sentences:exercises-":[]});
  await assert.rejects(
    buildPublishedGameEnglishActivityDataset(
      loader,
      "vocab-shooter",
      "shooter",
      "translation",
      "bad-runtime",
    ),
    /not supported/,
  );
});
