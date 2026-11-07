import test from "node:test";
import assert from "node:assert/strict";
import {
  ENGLISH_ACTIVITY_DATASET_MESSAGE,
  buildEnglishActivityDataset,
  parseEnglishActivityDataset,
} from "./activity-dataset.mjs";

test("builds Recall phrase activity without pretending it is vocabulary",()=>{
  const dataset=buildEnglishActivityDataset(
    "recall-typing",
    "collocation",
    [{
      contentId:"col.make-decision",
      promptText:"đưa ra quyết định",
      answerText:"make a decision",
      meaningVi:"đưa ra quyết định",
    }],
    "recall-col-1",
    "2026-10-03T00:00:00.000Z",
  );
  assert.equal(dataset.type,ENGLISH_ACTIVITY_DATASET_MESSAGE);
  assert.deepEqual(dataset.items[0],{
    contentId:"col.make-decision",
    entityType:"sentence",
    entityId:"col.make-decision",
    promptText:"đưa ra quyết định",
    answerText:"make a decision",
    meaningVi:"đưa ra quyết định",
  });
});

test("maps Space grammar challenge to grammar mastery id",()=>{
  const dataset=buildEnglishActivityDataset(
    "space-typing",
    "grammar-challenge",
    [{
      contentId:"gr.b1.second-conditional",
      promptText:"Complete the hypothetical sentence",
      answerText:"If I had more time, I would learn another language.",
    }],
    "space-grammar-1",
  );
  assert.equal(dataset.items[0].entityType,"grammar");
  assert.equal(dataset.items[0].entityId,"gr.b1.second-conditional");
});

test("maps vocabulary answers to canonical vocabulary keys",()=>{
  const dataset=buildEnglishActivityDataset(
    "vocab-shooter",
    "vocabulary",
    [{contentId:"lex.en.airport",promptText:"sân bay",answerText:" Airport "}],
    "shooter-vocab-1",
  );
  assert.equal(dataset.items[0].entityType,"vocabulary");
  assert.equal(dataset.items[0].entityId,"airport");
});

test("rejects activities that do not fit the target game",()=>{
  assert.throws(
    ()=>buildEnglishActivityDataset(
      "vocab-shooter",
      "translation",
      [{contentId:"sent.1",promptText:"Xin chào",answerText:"Hello"}],
      "bad-activity",
    ),
    /not supported/,
  );
});

test("parser rejects grammar items without stable gr ids",()=>{
  assert.throws(
    ()=>parseEnglishActivityDataset({
      version:1,
      type:ENGLISH_ACTIVITY_DATASET_MESSAGE,
      requestId:"bad-grammar",
      createdAt:"2026-10-03T00:00:00.000Z",
      gameId:"space-typing",
      activity:"grammar-challenge",
      items:[{
        contentId:"challenge.1",
        entityType:"grammar",
        entityId:"challenge.1",
        promptText:"Choose the form",
        answerText:"would go",
      }],
    }),
    /gr\.\*/,
  );
});
