import { buildEnglishActivityDataset } from "./activity-dataset.mjs";

function object(value){
  return value!==null&&typeof value==="object"&&!Array.isArray(value);
}
function text(value,field){
  if(typeof value!=="string"||value.trim()==="") throw new TypeError(field+" is required");
  return value.normalize("NFC").trim().replace(/\s+/g," ");
}
function publishable(record,allowUnpublished){
  if(allowUnpublished===true) return;
  const state=record?.quality?.state;
  if(state!=="published") {
    throw new TypeError("English activity adapter accepts published records only");
  }
}
function firstForm(record){
  for(const key of ["positive","negative","question"]){
    const values=record?.forms?.[key];
    if(Array.isArray(values)){
      const found=values.find(value=>typeof value==="string"&&value.trim()!=="");
      if(found!==undefined) return found;
    }
  }
  return null;
}
function grammarTopicItem(record){
  const answer=firstForm(record);
  if(answer===null) throw new TypeError(record.id+": grammar topic has no playable form");
  return {
    contentId:text(record.id,"grammar id"),
    entityType:"grammar",
    entityId:text(record.id,"grammar id"),
    promptText:text(record.title,"grammar title")+" — "+text(record.objective,"grammar objective"),
    answerText:text(answer,"grammar answer"),
    ...(typeof record.concept?.vi==="string"&&record.concept.vi.trim()!==""
      ?{meaningVi:text(record.concept.vi,"grammar concept.vi")}
      :{}),
  };
}
function exerciseItem(record){
  const answer=Array.isArray(record.acceptedAnswers)
    ?record.acceptedAnswers.find(value=>typeof value==="string"&&value.trim()!=="")
    :undefined;
  if(answer===undefined) throw new TypeError(record.id+": exercise has no accepted answer");
  const sourceId=Array.isArray(record.sourceSentenceIds)
    ?record.sourceSentenceIds.find(value=>typeof value==="string"&&value.trim()!=="")
    :undefined;
  return {
    contentId:text(record.id,"exercise id"),
    entityType:"sentence",
    entityId:sourceId??text(record.id,"exercise id"),
    promptText:text(record.prompt,"exercise prompt"),
    answerText:text(answer,"exercise answer"),
  };
}
export function englishActivityItemsFromRecords(activity,records,options={}){
  if(!Array.isArray(records)||records.length===0) {
    throw new TypeError("English activity records must be a non-empty array");
  }
  const items=[];
  for(const record of records){
    if(!object(record)) throw new TypeError("English activity record must be an object");
    publishable(record,options.allowUnpublished);
    if(activity==="collocation"){
      items.push({
        contentId:text(record.id,"collocation id"),
        entityType:"sentence",
        entityId:text(record.id,"collocation id"),
        promptText:text(record.meaningVi,"collocation meaningVi"),
        answerText:text(record.text,"collocation text"),
        meaningVi:text(record.meaningVi,"collocation meaningVi"),
      });
      continue;
    }
    if(activity==="phrasal-verb"||activity==="chunk"||activity==="idiom"){
      if(record.type!==activity) throw new TypeError(record.id+": phrase type does not match "+activity);
      items.push({
        contentId:text(record.id,"phrase id"),
        entityType:"sentence",
        entityId:text(record.id,"phrase id"),
        promptText:text(record.meaningVi,"phrase meaningVi"),
        answerText:text(record.text,"phrase text"),
        meaningVi:text(record.meaningVi,"phrase meaningVi"),
      });
      continue;
    }
    if(activity==="example-typing"||activity==="listening-typing"){
      if(activity==="listening-typing"&&record.type==="listening-typing"){
        const item=exerciseItem(record);
        items.push({...item,audioText:item.answerText});
        continue;
      }
      const sentenceText=text(record.text,"sentence text");
      items.push({
        contentId:text(record.id,"sentence id"),
        entityType:"sentence",
        entityId:text(record.id,"sentence id"),
        promptText:activity==="listening-typing"?"Listen and type the sentence":sentenceText,
        answerText:sentenceText,
        ...(activity==="listening-typing"?{audioText:sentenceText}:{}),
      });
      continue;
    }
    if(
      activity==="error-correction"&&
      typeof record.id==="string"&&record.id.startsWith("err.")&&
      Array.isArray(record.corrections)
    ){
      const answer=record.corrections.find(value=>typeof value==="string"&&value.trim()!=="");
      if(answer===undefined) throw new TypeError(record.id+": common mistake has no correction");
      items.push({
        contentId:text(record.id,"common mistake id"),
        entityType:"sentence",
        entityId:text(record.id,"common mistake id"),
        promptText:text(record.incorrect,"common mistake incorrect"),
        answerText:text(answer,"common mistake correction"),
        meaningVi:text(record.explanationVi,"common mistake explanationVi"),
      });
      continue;
    }
    if(
      activity==="translation"||
      activity==="contextual-usage"||
      activity==="cloze"||
      activity==="error-correction"||
      activity==="sentence-building"||
      activity==="transformation"
    ){
      const expectedType={
        translation:"translation",
        "contextual-usage":"contextual-usage",
        cloze:"cloze",
        "error-correction":"error-correction",
        "sentence-building":"sentence-building",
        transformation:"transformation",
      }[activity];
      if(record.type!==expectedType) {
        throw new TypeError(record.id+": "+activity+" adapter requires "+expectedType+" exercise");
      }
      items.push(exerciseItem(record));
      continue;
    }
    if(activity==="grammar-topic"){
      if(typeof record.id!=="string"||!record.id.startsWith("gr.")) {
        throw new TypeError("grammar-topic requires a grammar topic");
      }
      items.push(grammarTopicItem(record));
      continue;
    }
    if(activity==="verb-pattern"){
      items.push({
        contentId:text(record.id,"verb pattern id"),
        entityType:"sentence",
        entityId:text(record.id,"verb pattern id"),
        promptText:text(record.explanationVi,"verb pattern explanationVi"),
        answerText:text(record.lemma,"verb pattern lemma")+" · "+text(record.frame,"verb pattern frame"),
        meaningVi:text(record.explanationVi,"verb pattern explanationVi"),
      });
      continue;
    }
    if(activity==="grammar-challenge"){
      if(typeof record.id==="string"&&record.id.startsWith("gr.")){
        items.push(grammarTopicItem(record));
        continue;
      }
      if(record.type==="grammar-typing"){
        const item=exerciseItem(record);
        const grammarId=Array.isArray(record.targetIds)
          ?record.targetIds.find(value=>typeof value==="string"&&value.startsWith("gr."))
          :undefined;
        if(grammarId===undefined) throw new TypeError(record.id+": grammar exercise has no gr.* target");
        items.push({...item,entityType:"grammar",entityId:grammarId});
        continue;
      }
      throw new TypeError("grammar-challenge requires a grammar topic or grammar-typing exercise");
    }
    if(activity==="dialogue"){
      const dialogueId=text(record.id,"dialogue id");
      const scenario=text(record.scenario,"dialogue scenario");
      if(!Array.isArray(record.turns)||record.turns.length<2) {
        throw new TypeError(dialogueId+": dialogue has no turns");
      }
      record.turns.forEach((turn,index)=>{
        if(!object(turn)) throw new TypeError(dialogueId+": invalid dialogue turn");
        const speaker=text(turn.speaker,"dialogue speaker");
        const turnText=text(turn.text,"dialogue turn text");
        items.push({
          contentId:dialogueId+".turn-"+String(index+1).padStart(2,"0"),
          entityType:"sentence",
          entityId:dialogueId,
          promptText:scenario+" · "+speaker,
          answerText:turnText,
          audioText:turnText,
        });
      });
      continue;
    }
    if(activity==="vocabulary"){
      const answer=text(record.en??record.headword,"vocabulary English");
      const meaning=text(record.vi,"vocabulary Vietnamese");
      items.push({
        contentId:text(record.id??answer.toLocaleLowerCase("en-US"),"vocabulary id"),
        entityType:"vocabulary",
        entityId:answer.normalize("NFKC").toLocaleLowerCase("en-US"),
        promptText:meaning,
        answerText:answer,
        meaningVi:meaning,
        ...(typeof record.ipa==="string"&&record.ipa.trim()!==""?{ipa:text(record.ipa,"vocabulary ipa")}:{})
      });
      continue;
    }
    throw new TypeError("No parent record adapter for activity: "+activity);
  }
  if(items.length===0||items.length>100) {
    throw new TypeError("Adapted English activity must contain 1 to 100 items");
  }
  return items;
}
export function buildGameEnglishActivityDataset(
  gameId,
  activity,
  records,
  requestId,
  options={},
){
  const items=englishActivityItemsFromRecords(activity,records,options);
  return buildEnglishActivityDataset(
    gameId,
    activity,
    items,
    requestId,
    options.createdAt,
  );
}
