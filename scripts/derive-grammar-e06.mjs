import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const sourceDoc=await readJson(path.join(root,"content","english","sentences","pilot-sentences.json"));
const sourceById=new Map(sourceDoc.records.map(item=>[item.id,item]));

const correctionVariants={
  "sent.00000001":["I checks my email every morning.","I am check my email every morning.","I check my emails every mornings."],
  "sent.00000002":["She take the bus to work on weekdays.","She does takes the bus to work on weekdays.","She taking the bus to work on weekdays."],
  "sent.00000003":["We usually eats dinner at home.","We are usually eat dinner at home.","We usually eating dinner at home."],
  "sent.00000004":["I waiting for the train now.","I is waiting for the train now.","I am wait for the train now."],
  "sent.00000005":["They discussing the new schedule.","They is discussing the new schedule.","They are discuss the new schedule."],
  "sent.00000006":["She packing her suitcase at the moment.","She are packing her suitcase at the moment.","She is pack her suitcase at the moment."],
  "sent.00000007":["I has visited Singapore twice.","I have visit Singapore twice.","I have visiting Singapore twice."],
  "sent.00000008":["Has you ever worked with an international team?","Have you ever work with an international team?","Have you ever works with an international team?"],
  "sent.00000009":["She have never missed a flight.","She has never miss a flight.","She has never missing a flight."],
  "sent.00000010":["If it will rain, we will take a taxi.","If it rains, we would take a taxi.","If it rains, we will took a taxi."],
  "sent.00000011":["If you will finish the report today, I will review it tomorrow.","If you finish the report today, I would review it tomorrow.","If you finish the report today, I will reviewed it tomorrow."],
  "sent.00000012":["If the museum will be open, we will visit it after lunch.","If the museum is open, we would visit it after lunch.","If the museum is open, we will visited it after lunch."],
  "sent.00000013":["I has written three emails this morning.","I have wrote three emails this morning.","I have writing three emails this morning."],
  "sent.00000014":["I has been writing emails for two hours.","I have writing emails for two hours.","I have been wrote emails for two hours."],
  "sent.00000015":["She have repaired the printer, so we can use it again.","She has repair the printer, so we can use it again.","She has repairing the printer, so we can use it again."],
  "sent.00000016":["If I have more time, I would learn another language.","If I had more time, I would learned another language.","If I had more time, I will learn another language."],
  "sent.00000017":["If we live closer to the office, we would walk to work.","If we lived closer to the office, we would walked to work.","If we lived closer to the office, we will walk to work."],
  "sent.00000018":["What will you do if your flight were cancelled?","What would you did if your flight were cancelled?","What would you do if your flight were cancel?"],
  "sent.00000019":["If we have left earlier, we would have caught the train.","If we had left earlier, we would caught the train.","If we had left earlier, we would have catch the train."],
  "sent.00000020":["If I have known about the deadline, I would have submitted the form yesterday.","If I had known about the deadline, I would submitted the form yesterday.","If I had known about the deadline, I would have submit the form yesterday."],
  "sent.00000021":["She might avoided the delay if she had checked the route.","She might have avoided the delay if she has checked the route.","She might have avoid the delay if she had checked the route."],
  "sent.00000022":["The new policy expected to reduce waiting times.","The new policy is expect to reduce waiting times.","The new policy are expected to reduce waiting times."],
  "sent.00000023":["The device believed to be safe under normal conditions.","The device is believe to be safe under normal conditions.","The device are believed to be safe under normal conditions."],
  "sent.00000024":["The company reported to have opened a new office.","The company is report to have opened a new office.","The company are reported to have opened a new office."],
  "sent.00000025":["Rarely we see such a clear improvement in one week.","Rarely does we see such a clear improvement in one week.","Rarely do we sees such a clear improvement in one week."],
  "sent.00000026":["Not until the meeting ended I understood the problem.","Not until the meeting ended did I understood the problem.","Not until the meeting ended does I understand the problem."],
  "sent.00000027":["Only then the team realized how serious the error was.","Only then did the team realized how serious the error was.","Only then does the team realize how serious the error was."],
  "sent.00000028":["The rapid expand of the service created new staffing needs.","The rapidly expansion of the service created new staffing needs.","The rapid expansion of the service create new staffing needs."],
  "sent.00000029":["Their decide to postpone the launch reduced the immediate risk.","Their decision to postpone the launch reduce the immediate risk.","Their decision postpone the launch reduced the immediate risk."],
  "sent.00000030":["A careful evaluate of the evidence led to a different conclusion.","A carefully evaluation of the evidence led to a different conclusion.","A careful evaluation of the evidence lead to a different conclusion."],
  "sent.00000031":["With the lights off, they must are asleep.","With the lights off, they must asleep.","With the lights off, they must be sleeps."],
  "sent.00000032":["All visitors must wears a badge.","All visitors must to wear a badge.","All visitors must wearing a badge."],
  "sent.00000033":["You may uses this room after six.","You may to use this room after six.","You may using this room after six."],
  "sent.00000034":["At the end of the corridor stood a narrow wooden doors.","At the end of the corridor was stood a narrow wooden door.","At the end of the corridor stood was a narrow wooden door."],
  "sent.00000035":["Into room walked the last guest.","Into the room did walked the last guest.","Into the room walk the last guest."],
  "sent.00000036":["Most striking were the speed of the recovery.","Most striking did was the speed of the recovery.","Most striking was the speed of the recover."]
};

const transformationPairs=[
["sent.00000001","Rewrite as a negative Present Simple sentence.","I do not check my email every morning."],
["sent.00000002","Rewrite as a Present Simple question.","Does she take the bus to work on weekdays?"],
["sent.00000003","Rewrite as a Present Simple question.","Do we usually eat dinner at home?"],
["sent.00000004","Rewrite as a negative Present Continuous sentence.","I am not waiting for the train now."],
["sent.00000005","Rewrite as a Present Continuous question.","Are they discussing the new schedule?"],
["sent.00000006","Rewrite as a negative Present Continuous sentence.","She is not packing her suitcase at the moment."],
["sent.00000007","Rewrite as a Present Perfect question.","Have I visited Singapore twice?"],
["sent.00000008","Rewrite as an affirmative Present Perfect statement.","You have worked with an international team."],
["sent.00000009","Rewrite as a Present Perfect question using ever.","Has she ever missed a flight?"],
["sent.00000010","Move the result clause before the if-clause without changing the condition.","We will take a taxi if it rains."],
["sent.00000011","Move the result clause before the if-clause without changing the condition.","I will review it tomorrow if you finish the report today."],
["sent.00000012","Move the result clause before the if-clause without changing the condition.","We will visit the museum after lunch if it is open."],
["sent.00000013","Rewrite as a Present Perfect question.","Have I written three emails this morning?"],
["sent.00000014","Rewrite as a negative Present Perfect Continuous sentence.","I have not been writing emails for two hours."],
["sent.00000015","Rewrite as a Present Perfect question.","Has she repaired the printer so we can use it again?"],
["sent.00000016","Move the result clause before the if-clause.","I would learn another language if I had more time."],
["sent.00000017","Move the result clause before the if-clause.","We would walk to work if we lived closer to the office."],
["sent.00000018","Move the if-clause before the question clause.","If your flight were cancelled, what would you do?"],
["sent.00000019","Move the result clause before the if-clause.","We would have caught the train if we had left earlier."],
["sent.00000020","Move the result clause before the if-clause.","I would have submitted the form yesterday if I had known about the deadline."],
["sent.00000021","Move the if-clause before the result clause.","If she had checked the route, she might have avoided the delay."],
["sent.00000022","Rewrite the reporting passive with an impersonal it-clause.","It is expected that the new policy will reduce waiting times."],
["sent.00000023","Rewrite the reporting passive with an impersonal it-clause.","It is believed that the device is safe under normal conditions."],
["sent.00000024","Rewrite the reporting passive with an impersonal it-clause.","It is reported that the company has opened a new office."],
["sent.00000025","Rewrite the inversion in neutral word order.","We rarely see such a clear improvement in one week."],
["sent.00000026","Rewrite the inversion in neutral word order.","I did not understand the problem until the meeting ended."],
["sent.00000027","Rewrite the inversion in neutral word order.","The team realized how serious the error was only then."],
["sent.00000028","Rewrite the nominalisation with a finite verb.","The service expanded rapidly, creating new staffing needs."],
["sent.00000029","Rewrite the nominalisation with a finite verb.","They decided to postpone the launch, which reduced the immediate risk."],
["sent.00000030","Rewrite the nominalisation with a finite verb.","They carefully evaluated the evidence and reached a different conclusion."],
["sent.00000031","Paraphrase the epistemic modal meaning explicitly.","The lights are off, so I am certain that they are asleep."],
["sent.00000032","Paraphrase the obligation meaning without must.","All visitors are required to wear a badge."],
["sent.00000033","Paraphrase the permission meaning without may.","You are allowed to use this room after six."],
["sent.00000034","Rewrite the marked word order in neutral subject-verb order.","A narrow wooden door stood at the end of the corridor."],
["sent.00000035","Rewrite the marked word order in neutral subject-verb order.","The last guest walked into the room."],
["sent.00000036","Rewrite the marked word order in neutral subject-verb order.","The speed of the recovery was most striking."],
["sent.00000001","Replace every morning with an equivalent frequency expression.","I check my email each morning."],
["sent.00000002","Front the time expression while keeping Present Simple.","On weekdays, she takes the bus to work."],
["sent.00000003","Front the place expression while keeping the routine meaning.","At home, we usually eat dinner."],
["sent.00000004","Front the time expression while keeping Present Continuous.","Right now, I am waiting for the train."],
["sent.00000005","Add a natural current-time adverb while keeping Present Continuous.","They are currently discussing the new schedule."],
["sent.00000006","Front the time expression while keeping Present Continuous.","At the moment, she is packing her suitcase."],
["sent.00000007","Rewrite the experience with been while keeping Present Perfect.","I have been to Singapore twice."],
["sent.00000008","Rewrite the experience question with be part of.","Have you ever been part of an international team at work?"],
["sent.00000009","Rewrite never with not ever while keeping Present Perfect.","She has not ever missed a flight."],
["sent.00000010","Contract the result-clause auxiliary.","If it rains, we'll take a taxi."],
["sent.00000011","Contract the result-clause auxiliary.","If you finish the report today, I'll review it tomorrow."],
["sent.00000012","Contract the result-clause auxiliary.","If the museum is open, we'll visit it after lunch."],
["sent.00000013","Use the standard contraction for I have.","I've written three emails this morning."],
["sent.00000014","Use the standard contraction for I have.","I've been writing emails for two hours."]
];

function normalize(value) {
  return String(value).normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US");
}
function selectEvenly(items,limit) {
  if (items.length<limit) throw new Error("Need "+limit+" candidates, got "+items.length);
  if (items.length===limit) return [...items];
  const selected=[];
  const used=new Set();
  for (let index=0;index<limit;index++) {
    let position=Math.floor(((index+0.5)*items.length)/limit);
    position=Math.min(items.length-1,Math.max(0,position));
    while (used.has(position)&&position+1<items.length) position++;
    while (used.has(position)&&position>0) position--;
    used.add(position);
    selected.push(items[position]);
  }
  return selected;
}
function quality(kind) {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"e06-grammar-recipe-v1"},
      sourceLink:{status:"pass",method:"pilot-sentence-id-v1"},
      targetStructure:{status:"pending",method:"grammar-editor-review-required"},
      naturalness:{status:"pending",method:"editor-review-required"},
      semanticEquivalence:{
        status:kind==="transformation"?"pending":"not-applicable",
        method:kind==="transformation"?"independent-review-required":"correction-task",
      },
    },
  };
}
function provenance(sourceId,recipeId) {
  return {
    sources:[{
      dataset:"project-original",
      sourceId:sourceId+":"+recipeId,
      sourceUrl:"content/english/sentences/pilot-sentences.json",
      snapshot:"2026-10",
      license:"LicenseRef-Project-Original",
      modified:true,
    }],
    note:"Deterministic E06 grammar pilot recipe derived from an authored pilot sentence; publication requires independent grammar review.",
  };
}

const correctionCandidates=[];
for (const [sourceId,wrongVariants] of Object.entries(correctionVariants)) {
  const source=sourceById.get(sourceId);
  if (!source) throw new Error("Unknown correction source sentence "+sourceId);
  const grammarId=source.grammarIds?.[0];
  if (!grammarId) throw new Error(sourceId+" has no grammar target");
  wrongVariants.forEach((wrong,index)=>{
    if (normalize(wrong)===normalize(source.text)) {
      throw new Error(sourceId+" correction "+(index+1)+" does not change the source");
    }
    correctionCandidates.push({
      schemaVersion:1,
      id:"ex.correction.e06."+sourceId.slice(5)+"."+String(index+1).padStart(2,"0"),
      type:"error-correction",
      prompt:wrong,
      targetIds:[grammarId],
      acceptedAnswers:[source.text],
      sourceSentenceIds:[source.id],
      cefr:source.cefr,
      quality:quality("correction"),
      provenance:provenance(source.id,"correction-"+String(index+1)),
    });
  });
}
const corrections=selectEvenly(correctionCandidates,100);

const transformationCandidates=[];
for (const [sourceId,instruction,alternative] of transformationPairs) {
  const source=sourceById.get(sourceId);
  if (!source) throw new Error("Unknown transformation source sentence "+sourceId);
  const grammarId=source.grammarIds?.[0];
  if (!grammarId) throw new Error(sourceId+" has no grammar target");
  if (normalize(alternative)===normalize(source.text)) {
    throw new Error(sourceId+" transformation alternative equals source");
  }
  const pairIndex=transformationCandidates.length/2+1;
  transformationCandidates.push({
    schemaVersion:1,
    id:"ex.transformation.e06."+String(pairIndex).padStart(3,"0")+".a",
    type:"transformation",
    prompt:instruction+"\nSource: "+source.text,
    targetIds:[grammarId],
    acceptedAnswers:[alternative],
    sourceSentenceIds:[source.id],
    cefr:source.cefr,
    quality:quality("transformation"),
    provenance:provenance(source.id,"transformation-forward-"+String(pairIndex)),
  });
  transformationCandidates.push({
    schemaVersion:1,
    id:"ex.transformation.e06."+String(pairIndex).padStart(3,"0")+".b",
    type:"transformation",
    prompt:"Rewrite this alternative back into the pilot target form ("+grammarId+").\nSource: "+alternative,
    targetIds:[grammarId],
    acceptedAnswers:[source.text],
    sourceSentenceIds:[source.id],
    cefr:source.cefr,
    quality:quality("transformation"),
    provenance:provenance(source.id,"transformation-reverse-"+String(pairIndex)),
  });
}
if (transformationCandidates.length!==100) {
  throw new Error("Expected exactly 100 transformation candidates, got "+transformationCandidates.length);
}

const outDir=path.join(root,"content","english","review-queues");
await fs.mkdir(outDir,{recursive:true});
await Promise.all([
  fs.writeFile(
    path.join(outDir,"grammar-e06-corrections.json"),
    stableJson({schemaVersion:1,records:corrections}),
    "utf8",
  ),
  fs.writeFile(
    path.join(outDir,"grammar-e06-transformations.json"),
    stableJson({schemaVersion:1,records:transformationCandidates}),
    "utf8",
  ),
]);
console.log("E06 grammar candidates:",JSON.stringify({
  correctionPool:correctionCandidates.length,
  corrections:corrections.length,
  transformationPairs:transformationPairs.length,
  transformations:transformationCandidates.length,
}));
