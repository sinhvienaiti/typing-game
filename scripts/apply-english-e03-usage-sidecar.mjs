import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeEnglishKey, readJson, stableJson } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const BATCH_ID="e03.usage-reviewed-sidecar";
const SET_ID="reviewed-usages";
const USAGE_PATH="content/english/dictionary/e03-reviewed-usages.json";
const DECISION_PATH="content/english/reviews/decisions.d/e03-usages.json";
const REVIEWED_AT="2026-10-06T09:35:00Z";

async function exists(file){try{await fs.access(file);return true;}catch{return false;}}
async function writeJson(relative,value){const file=path.join(root,relative);await fs.mkdir(path.dirname(file),{recursive:true});await fs.writeFile(file,stableJson(value),"utf8");}
function replaceOnce(text,oldValue,newValue,label){
  const first=text.indexOf(oldValue);
  if(first<0) throw new Error(label+": replacement target missing");
  if(text.indexOf(oldValue,first+oldValue.length)>=0) throw new Error(label+": replacement target is not unique");
  return text.slice(0,first)+newValue+text.slice(first+oldValue.length);
}
function clone(value){return structuredClone(value);}
function decisionKey(batchId,recordSetId,recordId){return batchId+"\u0000"+recordSetId+"\u0000"+recordId;}

const manifestPath="content/english/batches/manifest.json";
const registryPath="content/english/id-registry.json";
const lexemePath="content/english/dictionary/e03-reviewed-lexemes.json";
const sensePath="content/english/dictionary/e03-reviewed-senses.json";
const [manifest,registry,lexemeDoc,senseDoc,sentenceManifest]=await Promise.all([
  readJson(path.join(root,manifestPath)),
  readJson(path.join(root,registryPath)),
  readJson(path.join(root,lexemePath)),
  readJson(path.join(root,sensePath)),
  readJson(path.join(root,"shared/sentences/manifest.json")),
]);
if(manifest.batches?.some(batch=>batch.id===BATCH_ID)) throw new Error(BATCH_ID+" already exists");
if(await exists(path.join(root,USAGE_PATH))) throw new Error(USAGE_PATH+" already exists");
if(await exists(path.join(root,DECISION_PATH))) throw new Error(DECISION_PATH+" already exists");
if(lexemeDoc.records?.length!==300||senseDoc.records?.length!==300) throw new Error("E03 usage sidecar requires exactly 300 reviewed lexemes + 300 reviewed senses");
if((registry.sequences?.usage??0)!==0) throw new Error("usage ID sequence drift: expected 0");
if(Object.keys(registry.entries??{}).some(key=>key.startsWith("usage:"))) throw new Error("usage registry entries already exist");
for(const lexeme of lexemeDoc.records){
  if(!Array.isArray(lexeme.usageRefs)||lexeme.usageRefs.length!==0) throw new Error(lexeme.id+": expected empty usageRefs before E03 sidecar");
}

const publishedExampleIds=new Set();
for(const shard of sentenceManifest.shards??[]){
  if(!String(shard.path).startsWith("examples/")) continue;
  const doc=await readJson(path.join(root,"shared/sentences",shard.path));
  for(const record of doc.records??[]) if(record?.quality?.state==="published") publishedExampleIds.add(record.id);
}
if(publishedExampleIds.size!==1513) throw new Error(`published example drift: expected 1513, got ${publishedExampleIds.size}`);
const sensesByLexeme=new Map();
for(const sense of senseDoc.records??[]){
  if(sensesByLexeme.has(sense.lexemeId)) throw new Error(sense.lexemeId+": multiple primary reviewed senses in controlled E03 pilot");
  if(typeof sense.explanationVi!=="string"||sense.explanationVi.trim()==="") throw new Error(sense.id+": missing reviewed explanationVi");
  if(!Array.isArray(sense.exampleIds)||sense.exampleIds.length===0) throw new Error(sense.id+": missing reviewed exampleIds");
  for(const id of sense.exampleIds) if(!publishedExampleIds.has(id)) throw new Error(sense.id+": example is not in published runtime: "+id);
  sensesByLexeme.set(sense.lexemeId,sense);
}

const reviewBase="content/english/reviews/decisions.json";
const reviewDir=path.join(root,"content/english/reviews/decisions.d");
const reviewPaths=[reviewBase];
for(const name of (await fs.readdir(reviewDir)).filter(name=>name.endsWith(".json")).sort((a,b)=>a.localeCompare(b,"en"))) reviewPaths.push("content/english/reviews/decisions.d/"+name);
const reviewDocs=new Map();
const reviewIndex=new Map();
for(const relative of reviewPaths){
  const doc=await readJson(path.join(root,relative));
  reviewDocs.set(relative,doc);
  for(const decision of doc.decisions??[]){
    const key=decisionKey(decision.batchId,decision.recordSetId,decision.recordId);
    if(reviewIndex.has(key)) throw new Error("duplicate review decision target: "+key);
    reviewIndex.set(key,{relative,decision});
  }
}

const usages=[];
const newDecisions=[];
const changedReviewFiles=new Set();
const sortedLexemes=[...lexemeDoc.records].sort((a,b)=>a.id.localeCompare(b.id,"en"));
for(const lexeme of sortedLexemes){
  const sense=sensesByLexeme.get(lexeme.id);
  if(!sense) throw new Error(lexeme.id+": reviewed primary sense missing");
  const next=(registry.sequences.usage??0)+1;
  registry.sequences.usage=next;
  const usageId="usage."+String(next).padStart(8,"0");
  const registryKey="usage:"+normalizeEnglishKey(lexeme.id);
  if(registry.entries[registryKey]) throw new Error("usage stable key already allocated: "+registryKey);
  registry.entries[registryKey]=usageId;
  lexeme.usageRefs=[usageId];

  const provenance=clone(sense.provenance);
  const derivationNote="Usage sidecar deterministically reuses the already-reviewed primary-sense Vietnamese explanation, register and example links; no new prose or third-party text was introduced.";
  provenance.note=(String(provenance.note??"").trim()+" "+derivationNote).trim();
  const usage={
    schemaVersion:1,
    id:usageId,
    targetId:lexeme.id,
    explanationVi:sense.explanationVi,
    ...(Array.isArray(sense.register)&&sense.register.length?{register:[...sense.register]}:{}),
    exampleIds:[...sense.exampleIds],
    quality:{
      state:"draft",
      checks:{
        schema:{status:"pass",method:"e03-usage-derived-reviewed-sense-v1"},
        referenceIntegrity:{status:"pending",method:"reference-review-required"},
        senseAlignment:{status:"pending",method:"sense-alignment-review-required"},
        naturalness:{status:"pending",method:"editor-review-required"},
        targetPresence:{status:"pending",method:"target-presence-review-required"},
        license:{status:"pending",method:"license-review-required"},
      },
    },
    provenance,
  };
  usages.push(usage);

  const lexDecisionTarget=reviewIndex.get(decisionKey("e03.lexical-reviewed-slice","reviewed-lexemes",lexeme.id));
  if(!lexDecisionTarget) throw new Error(lexeme.id+": E03 lexeme review decision missing");
  lexDecisionTarget.decision.sourceDigest=englishContentReviewSourceDigest(lexeme);
  lexDecisionTarget.decision.checks={...(lexDecisionTarget.decision.checks??{}),usageLink:{status:"pass",method:"e03-reviewed-usage-sidecar-link-v1"}};
  const lexNote="Stable usageRefs link added to the deterministic reviewed-sense usage sidecar.";
  if(!String(lexDecisionTarget.decision.note??"").includes(lexNote)) lexDecisionTarget.decision.note=(String(lexDecisionTarget.decision.note??"").trim()+" "+lexNote).trim();
  changedReviewFiles.add(lexDecisionTarget.relative);

  newDecisions.push({
    id:"review.e03.usage."+usageId.replaceAll(".","-"),
    batchId:BATCH_ID,
    recordSetId:SET_ID,
    recordId:usageId,
    sourceDigest:englishContentReviewSourceDigest(usage),
    targetState:"published",
    checks:{
      referenceIntegrity:{status:"pass",method:"e03-usage-target-example-integrity-v1"},
      senseAlignment:{status:"pass",method:"inherited-reviewed-primary-sense-v1"},
      naturalness:{status:"pass",method:"inherited-reviewed-sense-v1"},
      targetPresence:{status:"pass",method:"e03-usage-target-lexeme-check-v1"},
      license:{status:"pass",method:"inherited-reviewed-sense-provenance-v1"},
    },
    reviewedAt:REVIEWED_AT,
    reviewedBy:"Deterministic E03 reviewed-sense derivation",
    note:"This usage record introduces no new prose. explanationVi, register and exampleIds are copied from the already-reviewed primary sense; targetId and stable usage ID are deterministic graph links.",
  });
}
if(usages.length!==300||newDecisions.length!==300||registry.sequences.usage!==300) throw new Error("E03 usage sidecar allocation count mismatch");

manifest.batches.push({
  id:BATCH_ID,
  phase:"E03",
  category:"dictionary",
  cefr:["A1","A2","B1","B2"],
  state:"draft",
  recordSets:[{
    id:SET_ID,
    path:USAGE_PATH,
    expectedCount:300,
    generated:false,
    allowedQualityStates:["draft"],
    requiredChecks:["schema","referenceIntegrity","senseAlignment","naturalness","targetPresence","license"],
  }],
  requiredBeforePublish:["schema-validation","reference-integrity","sense-alignment","naturalness-review","target-presence-review","license-review"],
  gameSmokes:[],
});

await writeJson(lexemePath,lexemeDoc);
await writeJson(registryPath,registry);
await writeJson(manifestPath,manifest);
await writeJson(USAGE_PATH,{schemaVersion:1,records:usages});
await writeJson(DECISION_PATH,{schemaVersion:1,decisions:newDecisions});
for(const relative of changedReviewFiles) await writeJson(relative,reviewDocs.get(relative));

const usageSetSchema={
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "$id":"https://typing-game.local/schemas/english-content/usage-set.schema.json",
  title:"usage-set",
  type:"object",
  additionalProperties:false,
  required:["schemaVersion","records"],
  properties:{
    schemaVersion:{const:1},
    records:{type:"array",items:{"$ref":"https://typing-game.local/schemas/english-content/usage.schema.json"}},
  },
};
await writeJson("shared/schemas/english-content/usage-set.schema.json",usageSetSchema);

// Extend schema/source validation with the new controlled sidecar.
const validatorPath=path.join(root,"scripts/validate-english-content.mjs");
let validator=await fs.readFile(validatorPath,"utf8");
validator=replaceOnce(validator,'"usage.schema.json","collocation.schema.json"','"usage.schema.json","usage-set.schema.json","collocation.schema.json"',"validator schema catalog");
validator=replaceOnce(validator,'const reviewedSenses=await validateFile("content/english/dictionary/e03-reviewed-senses.json","sense-set.schema.json");','const reviewedSenses=await validateFile("content/english/dictionary/e03-reviewed-senses.json","sense-set.schema.json");\nconst reviewedUsages=await validateFile("content/english/dictionary/e03-reviewed-usages.json","usage-set.schema.json");',"validator usage source");
validator=replaceOnce(validator,'const pilotSentenceIds=new Set((sentencePilot?.records??[]).map(item=>item.id));',`if (reviewedLexemes&&reviewedUsages) {
  const expectedReviewedUsages=batchExpectedCount("e03.usage-reviewed-sidecar","reviewed-usages");
  if (expectedReviewedUsages!==300||reviewedUsages.records.length!==300) errors.push("E03 reviewed usage sidecar must contain exactly 300 controlled records");
  const lexemeIds=new Set(reviewedLexemes.records.map(item=>item.id));
  const usageIds=new Set(reviewedUsages.records.map(item=>item.id));
  for (const usage of reviewedUsages.records) {
    if (usage.quality?.state!=="draft") errors.push(usage.id+": E03 usage source must remain draft; publication is ledger-overlay only");
    if (!lexemeIds.has(usage.targetId)) errors.push(usage.id+": unknown usage target "+usage.targetId);
    if (!usage.explanationVi||!Array.isArray(usage.exampleIds)||usage.exampleIds.length===0) errors.push(usage.id+": usage requires reviewed explanationVi + exampleIds");
  }
  for (const lexeme of reviewedLexemes.records) {
    if (!Array.isArray(lexeme.usageRefs)||lexeme.usageRefs.length!==1) errors.push(lexeme.id+": reviewed lexeme must expose exactly one usageRef");
    for (const id of lexeme.usageRefs??[]) if (!usageIds.has(id)) errors.push(lexeme.id+": unknown reviewed usage "+id);
  }
}
const pilotSentenceIds=new Set((sentencePilot?.records??[]).map(item=>item.id));`,"validator usage contract");
await fs.writeFile(validatorPath,validator,"utf8");

// Publish usage records as a first-class dictionary sidecar group.
const publisherPath=path.join(root,"scripts/publish-english-content.mjs");
let publisher=await fs.readFile(publisherPath,"utf8");
publisher=replaceOnce(publisher,'const senses=await loadRecords("content/english/dictionary/e03-reviewed-senses.json");','const senses=await loadRecords("content/english/dictionary/e03-reviewed-senses.json");\nconst usages=await loadRecords("content/english/dictionary/e03-reviewed-usages.json");',"publisher usage load");
publisher=replaceOnce(publisher,'{id:"senses",dir:"senses",records:senses}\n]}));','{id:"senses",dir:"senses",records:senses},\n  {id:"usages",dir:"usages",records:usages}\n]}));',"publisher usage group");
await fs.writeFile(publisherPath,publisher,"utf8");

// Strengthen runtime smoke to verify all three dictionary graph layers and references.
const smokePath=path.join(root,"scripts/smoke-published-english-content.mjs");
let smoke=await fs.readFile(smokePath,"utf8");
smoke=replaceOnce(smoke,'const senses=dictionaryRecords.filter(record=>String(record.id??"").startsWith("sense."));','const senses=dictionaryRecords.filter(record=>String(record.id??"").startsWith("sense."));\nconst usages=dictionaryRecords.filter(record=>String(record.id??"").startsWith("usage."));',"smoke usage split");
smoke=replaceOnce(smoke,'if (dictionaryManifest.count!==600) errors.push("published dictionary runtime must contain 600 E03 records");\nif (lexemes.length!==300||senses.length!==300) errors.push("published E03 runtime split must be 300 lexemes + 300 senses");','if (dictionaryManifest.count!==900) errors.push("published dictionary runtime must contain 900 E03 records");\nif (lexemes.length!==300||senses.length!==300||usages.length!==300) errors.push("published E03 runtime split must be 300 lexemes + 300 senses + 300 usages");',"smoke dictionary counts");
smoke=replaceOnce(smoke,'for (const record of [...lexemes,...senses]) {','for (const record of [...lexemes,...senses,...usages]) {',"smoke published usage quality");
smoke=replaceOnce(smoke,'const senseIds=new Set(senses.map(record=>record.id));','const senseIds=new Set(senses.map(record=>record.id));\nconst usageIds=new Set(usages.map(record=>record.id));',"smoke usage ids");
smoke=replaceOnce(smoke,'for (const id of lexeme.senseIds??[]) if (!senseIds.has(id)) errors.push(lexeme.id+": missing runtime sense "+id);','for (const id of lexeme.senseIds??[]) if (!senseIds.has(id)) errors.push(lexeme.id+": missing runtime sense "+id);\n  if (!Array.isArray(lexeme.usageRefs)||lexeme.usageRefs.length!==1) errors.push(lexeme.id+": published lexeme must expose exactly one usageRef");\n  for (const id of lexeme.usageRefs??[]) if (!usageIds.has(id)) errors.push(lexeme.id+": missing runtime usage "+id);',"smoke lexeme usage refs");
smoke=replaceOnce(smoke,'const exerciseIds=new Set(exercises.map(record=>record.id));',`for (const usage of usages) {
  if (!lexemes.some(lexeme=>lexeme.id===usage.targetId)) errors.push(usage.id+": unknown runtime usage target "+usage.targetId);
  if (!usage.explanationVi||!Array.isArray(usage.exampleIds)||usage.exampleIds.length===0) errors.push(usage.id+": runtime usage requires explanationVi + exampleIds");
  for (const id of usage.exampleIds??[]) if (!exampleIds.has(id)) errors.push(usage.id+": missing runtime example "+id);
}
const exerciseIds=new Set(exercises.map(record=>record.id));`,"smoke usage integrity");
smoke=replaceOnce(smoke,'dictionarySenses:senses.length,','dictionarySenses:senses.length,\n  dictionaryUsages:usages.length,',"smoke report usage count");
await fs.writeFile(smokePath,smoke,"utf8");

// Make usage graph completeness a mandatory acceptance contract, not a warning-only metric.
const auditPath=path.join(root,"scripts/audit-english-content-master-plan.mjs");
let audit=await fs.readFile(auditPath,"utf8");
audit=replaceOnce(audit,'const senses=dictionary.groups.senses??[];','const senses=dictionary.groups.senses??[];\nconst usages=dictionary.groups.usages??[];',"audit usages group");
audit=replaceOnce(audit,'const senseIds=new Set(senses.map(record=>record.id));','const senseIds=new Set(senses.map(record=>record.id));\nconst usageIds=new Set(usages.map(record=>record.id));\nconst exampleIds=new Set(examples.map(record=>record.id));',"audit usage ids");
audit=replaceOnce(audit,'const lexemesWithoutUsageRefs=lexemes.filter(record=>!Array.isArray(record.usageRefs)||record.usageRefs.length===0);','const lexemesWithoutUsageRefs=lexemes.filter(record=>!Array.isArray(record.usageRefs)||record.usageRefs.length===0);\nconst lexemesWithBrokenUsageRefs=lexemes.filter(record=>(record.usageRefs??[]).some(id=>!usageIds.has(id)));\nconst usagesWithBrokenTargets=usages.filter(record=>!lexemeIds.has(record.targetId));\nconst usagesWithoutExamples=usages.filter(record=>!Array.isArray(record.exampleIds)||record.exampleIds.length===0||record.exampleIds.some(id=>!exampleIds.has(id)));',"audit usage integrity metrics");
audit=replaceOnce(audit,'addCheck(errors,sensesWithoutExamples.length===0,"E03 has senses without reviewed example links: "+sensesWithoutExamples.length);',`addCheck(errors,sensesWithoutExamples.length===0,"E03 has senses without reviewed example links: "+sensesWithoutExamples.length);
addCheck(errors,usages.length===300,"E03 requires exactly 300 published usage sidecars; got "+usages.length);
addCheck(errors,lexemesWithoutUsageRefs.length===0,"E03 has lexemes without usageRefs: "+lexemesWithoutUsageRefs.length);
addCheck(errors,lexemesWithBrokenUsageRefs.length===0,"E03 has broken lexeme usageRefs: "+lexemesWithBrokenUsageRefs.length);
addCheck(errors,usagesWithBrokenTargets.length===0,"E03 has usage records with broken targetId: "+usagesWithBrokenTargets.length);
addCheck(errors,usagesWithoutExamples.length===0,"E03 has usage records with missing/broken exampleIds: "+usagesWithoutExamples.length);`,"audit usage acceptance");
audit=replaceOnce(audit,'senses:senses.length,\n    lexemesWithoutSenses:','senses:senses.length,\n    usages:usages.length,\n    lexemesWithoutSenses:',"audit report usages");
audit=replaceOnce(audit,'lexemesWithoutUsageRefs:lexemesWithoutUsageRefs.length,\n    sensesWithoutExamples:','lexemesWithoutUsageRefs:lexemesWithoutUsageRefs.length,\n    lexemesWithBrokenUsageRefs:lexemesWithBrokenUsageRefs.length,\n    usagesWithBrokenTargets:usagesWithBrokenTargets.length,\n    usagesWithoutExamples:usagesWithoutExamples.length,\n    sensesWithoutExamples:',"audit report usage integrity");
await fs.writeFile(auditPath,audit,"utf8");

console.log(JSON.stringify({
  status:"applied",
  batch:BATCH_ID,
  usages:usages.length,
  lexemeUsageRefs:lexemeDoc.records.filter(record=>record.usageRefs?.length===1).length,
  registryUsageSequence:registry.sequences.usage,
  expectedDictionaryRuntime:900,
  prosePolicy:"reuse-reviewed-primary-sense-fields-only",
},null,2));
