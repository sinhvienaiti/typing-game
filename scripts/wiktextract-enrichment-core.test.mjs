import test from "node:test";
import assert from "node:assert/strict";
import {
  parseWiktextractForms,
  parseWiktextractIpa,
  parseWiktextractSenses,
} from "./wiktextract-enrichment-core.mjs";

test("parses forms and preserves usage tags",()=>{
  assert.deepEqual(parseWiktextractForms({
    forms:[
      {form:"went",tags:["past"]},
      {form:"gone",tags:["past","participle"]},
      {form:"gone",tags:["past","participle"]},
      {form:"-"}
    ]
  }),[
    {form:"went",tags:["past"]},
    {form:"gone",tags:["past","participle"]}
  ]);
});

test("parses sense labels examples and IPA defensively",()=>{
  assert.deepEqual(parseWiktextractSenses({
    senses:[{
      glosses:["To move from one place to another."],
      tags:["intransitive"],
      raw_tags:["informal"],
      examples:[{text:"We go home at six."}]
    }]
  }),[{
    sourceSenseIndex:0,
    glossesEn:["To move from one place to another."],
    tags:["intransitive","informal"],
    examples:["We go home at six."]
  }]);
  assert.deepEqual(parseWiktextractIpa({sounds:[{ipa:"/ɡəʊ/"},{ipa:"/ɡoʊ/"}]}),["/ɡəʊ/","/ɡoʊ/"]);
});
