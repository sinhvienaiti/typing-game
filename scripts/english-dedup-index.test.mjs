import test from "node:test";
import assert from "node:assert/strict";
import { nearDuplicatePairs, normalizeSentenceKey, tokenJaccard } from "./english-content-core.mjs";

function bruteForce(records, threshold) {
  const pairs=[];
  for (let i=0;i<records.length;i++) for (let j=i+1;j<records.length;j++) {
    if (normalizeSentenceKey(records[i].text)===normalizeSentenceKey(records[j].text)) continue;
    const score=tokenJaccard(records[i].text,records[j].text);
    if (score>=threshold) pairs.push({leftId:records[i].id,rightId:records[j].id,score:Number(score.toFixed(4))});
  }
  return pairs;
}

test("indexed join preserves exact pair values/order, punctuation, repeats, Unicode and empty sets",()=>{
  const records=["a b c d e f g", "g f e d c b a", "a b c d e f", "a a a b c d e f", "A B C D E F!", "", "?!", " ", "café l'été ici", "ici café l'été!", "unrelated other words"].map((text,i)=>({id:String(i),text}));
  for (const threshold of [0,.01,.5,.6,.86,6/7,1]) assert.deepEqual(nearDuplicatePairs(records,threshold),bruteForce(records,threshold));
});

test("indexed join matches brute force over seeded varied-length corpora at threshold boundaries",()=>{
  let seed=72153;
  const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/2**32;};
  for (let run=0;run<12;run++) {
    const records=Array.from({length:90},(_,i)=>({id:`r${i}`,text:Array.from({length:Math.floor(random()*22)},()=>`word${Math.floor(random()*25)}`).join(" ")+(i%3===0?"!":".")}));
    for (const threshold of [.15,.5,2/3,.7,.86,6/7,.9,1]) assert.deepEqual(nearDuplicatePairs(records,threshold),bruteForce(records,threshold));
  }
});

test("large disjoint corpus needs no all-pairs scan and still returns exact result",()=>{
  const records=Array.from({length:20000},(_,i)=>({id:String(i),text:`unique${i} isolated${i} distinct${i} sentence${i} tokens${i}`}));
  assert.deepEqual(nearDuplicatePairs(records),[]);
});

test("rejects invalid similarity thresholds",()=>{
  for (const threshold of [-.1,1.1,NaN,Infinity]) assert.throws(()=>nearDuplicatePairs([],threshold),RangeError);
});
