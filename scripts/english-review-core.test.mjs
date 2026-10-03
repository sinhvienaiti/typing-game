import test from "node:test";
import assert from "node:assert/strict";
import {
  applyEnglishReviewDecision,
  englishContentRecordDigest,
  overlayEnglishReviewDecisions,
} from "./english-review-core.mjs";

function sourceRecord() {
  return {
    schemaVersion:1,
    id:"sent.demo",
    text:"I work at home.",
    quality:{
      state:"candidate",
      checks:{
        schema:{status:"pass",method:"fixture"},
        naturalness:{status:"pending",method:"editor-review-required"},
      },
    },
  };
}

test("review overlay is digest-bound and can complete a record",()=>{
  const record=sourceRecord();
  const decision={
    id:"review.sent-demo",
    recordId:"sent.demo",
    sourceDigest:englishContentRecordDigest(record),
    targetState:"reviewed",
    checks:{
      naturalness:{status:"pass",method:"editor-v1"},
    },
  };
  const result=applyEnglishReviewDecision(record,decision);
  assert.equal(result.quality.state,"reviewed");
  assert.equal(result.quality.checks.naturalness.status,"pass");
  assert.equal(record.quality.state,"candidate");
});

test("stale decisions fail instead of applying to changed content",()=>{
  const record=sourceRecord();
  assert.throws(
    ()=>applyEnglishReviewDecision(record,{
      id:"review.stale",
      recordId:"sent.demo",
      sourceDigest:"0".repeat(64),
      targetState:"reviewed",
      checks:{naturalness:{status:"pass",method:"editor-v1"}},
    }),
    /sourceDigest is stale/,
  );
});

test("publication rejects unfinished checks",()=>{
  const record=sourceRecord();
  assert.throws(
    ()=>applyEnglishReviewDecision(record,{
      id:"review.publish",
      recordId:"sent.demo",
      sourceDigest:englishContentRecordDigest(record),
      targetState:"published",
      checks:{schema:{status:"pass",method:"fixture"}},
    },{requiredChecks:["schema","naturalness"]}),
    /completed check naturalness/,
  );
});

test("ledger targets one batch record without mutating peers",()=>{
  const first=sourceRecord();
  const second={...sourceRecord(),id:"sent.other"};
  const ledger={decisions:[{
    id:"review.one",
    batchId:"e06.demo",
    recordSetId:"examples",
    recordId:"sent.demo",
    sourceDigest:englishContentRecordDigest(first),
    targetState:"validated",
    checks:{naturalness:{status:"pass",method:"editor-v1"}},
  }]};
  const result=overlayEnglishReviewDecisions([first,second],ledger,{
    batchId:"e06.demo",
    recordSetId:"examples",
    requiredChecks:["naturalness"],
  });
  assert.equal(result[0].quality.state,"validated");
  assert.equal(result[1].quality.state,"candidate");
});
