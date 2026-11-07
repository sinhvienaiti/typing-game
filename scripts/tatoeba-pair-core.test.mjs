import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import {
  looksLikeLearningPair,
  normalizedPairKey,
  parseTatoebaLinkRow,
  parseTatoebaSentenceRow,
  selectEvenly,
  selectNextTatoebaPairs,
  tatoebaPairSourceKey,
  tatoebaPairSourceKeyFromTranslationRecord,
} from "./tatoeba-pair-core.mjs";

test("parses Tatoeba sentence rows with or without explicit language",()=>{
  assert.deepEqual(parseTatoebaSentenceRow("123\teng\tI work at home.","eng"),{
    id:123,text:"I work at home."
  });
  assert.deepEqual(parseTatoebaSentenceRow("456\tTôi làm việc ở nhà.","vie"),{
    id:456,text:"Tôi làm việc ở nhà."
  });
});

test("parses links and rejects malformed ids",()=>{
  assert.deepEqual(parseTatoebaLinkRow("123\t456"),{englishId:123,vietnameseId:456});
  assert.equal(parseTatoebaLinkRow("bad\t456"),null);
});

test("learning-pair filter keeps ordinary sentences and rejects URLs",()=>{
  assert.equal(looksLikeLearningPair("I work at home every Friday.","Tôi làm việc ở nhà vào mỗi thứ Sáu."),true);
  assert.equal(looksLikeLearningPair("See https://example.com now.","Xem liên kết này."),false);
});

test("pair normalization and even selection are deterministic",()=>{
  assert.equal(
    normalizedPairKey("  Hello   world! ","Xin chào thế giới!"),
    "hello world!\u0000xin chào thế giới!"
  );
  assert.deepEqual(selectEvenly([0,1,2,3,4,5,6,7,8,9],4),[1,3,6,8]);
});

test("Tatoeba pair source identity is bound to sentence ids rather than text",()=>{
  const first={englishId:10,vietnameseId:20,englishText:"Same text",vietnameseText:"Cùng chữ"};
  const second={englishId:11,vietnameseId:21,englishText:"Same text",vietnameseText:"Cùng chữ"};
  assert.equal(tatoebaPairSourceKey(first),"10:20");
  assert.equal(tatoebaPairSourceKey(second),"11:21");
  assert.notEqual(tatoebaPairSourceKey(first),tatoebaPairSourceKey(second));
  assert.throws(()=>tatoebaPairSourceKey({englishId:10,vietnameseId:"bad"}),/source identity/);
});

test("reviewed translation provenance yields the same source identity after editorial text changes",()=>{
  const record={
    type:"translation",
    prompt:"Biên tập lại câu tiếng Việt.",
    acceptedAnswers:["Edited English presentation."],
    provenance:{sources:[
      {dataset:"tatoeba",sourceId:"1333"},
      {dataset:"tatoeba",sourceId:"5690"},
    ]},
  };
  assert.equal(tatoebaPairSourceKeyFromTranslationRecord(record),"1333:5690");
  record.prompt="Nội dung trình bày có thể đổi mà source identity không đổi.";
  assert.equal(tatoebaPairSourceKeyFromTranslationRecord(record),"1333:5690");
  assert.equal(tatoebaPairSourceKeyFromTranslationRecord({type:"translation",provenance:{sources:[]}}),null);
  assert.equal(tatoebaPairSourceKeyFromTranslationRecord({type:"cloze"}),null);
});

test("next Tatoeba slices exclude used source ids and are prefix-monotonic",()=>{
  const candidates=[
    {englishId:50,vietnameseId:500},
    {englishId:10,vietnameseId:100},
    {englishId:40,vietnameseId:400},
    {englishId:20,vietnameseId:200},
    {englishId:30,vietnameseId:300},
    {englishId:20,vietnameseId:200},
  ];
  const excludeKeys=new Set(["20:200"]);
  const firstTwo=selectNextTatoebaPairs(candidates,2,{excludeKeys});
  const firstFour=selectNextTatoebaPairs(candidates,4,{excludeKeys});

  assert.deepEqual(firstTwo.map(tatoebaPairSourceKey),["10:100","30:300"]);
  assert.deepEqual(firstFour.map(tatoebaPairSourceKey),["10:100","30:300","40:400","50:500"]);
  assert.deepEqual(firstFour.slice(0,firstTwo.length),firstTwo);
  assert.deepEqual(
    selectNextTatoebaPairs([...candidates].reverse(),4,{excludeKeys}),
    firstFour,
  );
});

test("E11 Tatoeba review-slice preparer stays syntax-valid without requiring local source cache",()=>{
  const script=fileURLToPath(new URL("./prepare-tatoeba-e11-translation-slice.mjs",import.meta.url));
  const result=spawnSync(process.execPath,["--check",script],{encoding:"utf8"});
  assert.equal(result.status,0,result.stderr||result.stdout);
});
