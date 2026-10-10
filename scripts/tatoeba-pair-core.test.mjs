import test from "node:test";
import assert from "node:assert/strict";
import {
  looksLikeLearningPair,
  normalizedPairKey,
  parseTatoebaLinkRow,
  parseTatoebaSentenceRow,
  selectEvenly,
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
