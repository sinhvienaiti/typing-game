import test from "node:test";
import assert from "node:assert/strict";
import { createSchemaValidator, nearDuplicatePairs, normalizeEnglishKey, normalizeSentenceKey, sentenceFingerprint, tokenJaccard } from "./english-content-core.mjs";
test("normalizes English keys compatibly",()=>assert.equal(normalizeEnglishKey("  Take   OFF  "),"take off"));
test("normalizes sentence spacing and punctuation",()=>assert.equal(normalizeSentenceKey(" Hello ,   WORLD! "),"hello, world!"));
test("sentence fingerprint is deterministic",()=>assert.equal(sentenceFingerprint("Hello world."),sentenceFingerprint("  hello   world. ")));
test("near duplicate signal finds similar sentences",()=>{assert.ok(tokenJaccard("I have lived here for five years.","I have lived here for six years.")>0.7);assert.equal(nearDuplicatePairs([{id:"a",text:"I really like this quiet place."},{id:"b",text:"I really like this peaceful place."}],0.6).length,1);});
test("schema validator enforces closed objects",()=>{const schema={$id:"x",type:"object",additionalProperties:false,required:["id"],properties:{id:{type:"string",pattern:"^ok$"}}};const v=createSchemaValidator([schema]);assert.deepEqual(v.validate({id:"ok"},schema),[]);assert.ok(v.validate({id:"bad",extra:true},schema).length>=2);});
