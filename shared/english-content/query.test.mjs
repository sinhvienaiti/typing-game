import test from "node:test";
import assert from "node:assert/strict";
import { createEnglishContentClient, parseEnglishCurriculumLevel, parseEnglishTopicCatalog } from "./query.mjs";

const catalog={schemaVersion:1,topics:[
  {id:"gr.a1.present-simple-routines",cefr:"A1",title:"Present Simple: habits and routines",objective:"Describe repeated everyday actions and routines."},
  {id:"gr.a2.first-conditional",cefr:"A2",title:"First Conditional",objective:"Describe realistic future conditions and likely results."}
]};
test("parses a topic catalog",()=>assert.equal(parseEnglishTopicCatalog(catalog).topics.length,2));
test("rejects duplicate catalog ids",()=>assert.throws(()=>parseEnglishTopicCatalog({schemaVersion:1,topics:[catalog.topics[0],catalog.topics[0]]})));
test("parses curriculum level and rejects duplicate refs",()=>{
  assert.equal(parseEnglishCurriculumLevel({schemaVersion:1,cefr:"A1",topicIds:["gr.a1.present-simple-routines"]},"A1").topicIds.length,1);
  assert.throws(()=>parseEnglishCurriculumLevel({schemaVersion:1,cefr:"A1",topicIds:["x","x"]},"A1"));
});
test("client fetches bounded curriculum data and searches",async()=>{
  const calls=[];
  const fetcher=async input=>{
    calls.push(input);
    const body=input.endsWith("topic-catalog.json")?catalog:{schemaVersion:1,cefr:"A1",topicIds:["gr.a1.present-simple-routines"]};
    return {ok:true,status:200,json:async()=>body};
  };
  const client=createEnglishContentClient({fetcher,baseUrl:"https://typing-game.local/english-content/"});
  assert.equal((await client.getGrammarTopic("gr.a2.first-conditional")).cefr,"A2");
  assert.equal((await client.listGrammarTopics({search:"routines"})).length,1);
  assert.equal((await client.listCurriculumTopics("A1")).length,1);
  assert.equal(calls.filter(call=>call.endsWith("topic-catalog.json")).length,1);
});
