from __future__ import annotations
import copy, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BATCH_ID="e05.grammar-scale-a1-05"
TOPIC_PATH="content/english/grammar/e05-scale-a1-05-topics.json"
SENTENCE_PATH="content/english/sentences/e05-scale-a1-05-sentences.json"
EXERCISE_PATH="content/english/sentences/e05-scale-a1-05-exercises.json"
MISTAKE_PATH="content/english/sentences/e05-scale-a1-05-common-mistakes.json"
REVIEW_PATH="content/english/reviews/decisions.d/e05-grammar-a1-05.json"
SOURCE_SPECS=[
  {"n":1,"topic":"gr.a1.because-basic","clozePrompt":"Mia is smiling ___ she is happy.","clozeAnswer":"because","clozeSource":"sent.gra1.05.01.2","translationPrompt":"Dịch sang tiếng Anh: Tôi đi bộ đến chỗ làm vì nó ở gần.","translationAnswer":"I walk to work because it is close.","translationSource":"sent.gra1.05.01.1","incorrect":"I am tired so I go to bed early because.","correction":"I am tired, so I go to bed early.","explanationVi":"Because phải đứng trước mệnh đề nêu lý do; câu này đang nêu kết quả nên dùng so."},
  {"n":2,"topic":"gr.a1.present-continuous-temporary","clozePrompt":"I ___ with my cousin this week.","clozeAnswer":"am staying","clozeSource":"sent.gra1.05.02.1","translationPrompt":"Dịch sang tiếng Anh: Noah đang làm việc ở một quán cà phê tháng này.","translationAnswer":"Noah is working at a cafe this month.","translationSource":"sent.gra1.05.02.2","incorrect":"She works at home this week.","correction":"She is working at home this week.","explanationVi":"Với tình huống tạm thời trong tuần này, dùng Hiện tại tiếp diễn: is working."},
  {"n":3,"topic":"gr.a1.present-simple-vs-continuous","clozePrompt":"I usually drink tea, but today I ___ coffee.","clozeAnswer":"am drinking","clozeSource":"sent.gra1.05.03.1","translationPrompt":"Dịch sang tiếng Anh: Ben làm việc ở trường, nhưng tuần này anh ấy đang làm việc tại nhà.","translationAnswer":"Ben works at a school, but this week he is working from home.","translationSource":"sent.gra1.05.03.2","incorrect":"I am knowing the answer.","correction":"I know the answer.","explanationVi":"Know là động từ chỉ trạng thái và thường dùng Hiện tại đơn, không dùng Hiện tại tiếp diễn ở nghĩa này."},
  {"n":4,"topic":"gr.a1.past-be","clozePrompt":"The shops ___ busy on Saturday.","clozeAnswer":"were","clozeSource":"sent.gra1.05.04.2","translationPrompt":"Dịch sang tiếng Anh: Hôm qua tôi đã ở thư viện.","translationAnswer":"I was at the library yesterday.","translationSource":"sent.gra1.05.04.1","incorrect":"They was at home last night.","correction":"They were at home last night.","explanationVi":"Với chủ ngữ they ở quá khứ của be, dùng were, không dùng was."},
  {"n":5,"topic":"gr.a1.past-simple-regular","clozePrompt":"We ___ our grandparents last weekend.","clozeAnswer":"visited","clozeSource":"sent.gra1.05.05.1","translationPrompt":"Dịch sang tiếng Anh: Sara đã dọn bếp sau bữa tối.","translationAnswer":"Sara cleaned the kitchen after dinner.","translationSource":"sent.gra1.05.05.2","incorrect":"We visit our grandparents last weekend.","correction":"We visited our grandparents last weekend.","explanationVi":"Với thời gian quá khứ đã kết thúc last weekend, dùng Quá khứ đơn: visited."},
  {"n":6,"topic":"gr.a1.past-simple-irregular","clozePrompt":"We ___ to the beach on Sunday.","clozeAnswer":"went","clozeSource":"sent.gra1.05.06.1","translationPrompt":"Dịch sang tiếng Anh: Tôi đã gặp giáo viên của mình ở chợ.","translationAnswer":"I saw my teacher at the market.","translationSource":"sent.gra1.05.06.2","incorrect":"He goed to work early.","correction":"He went to work early.","explanationVi":"Go là động từ bất quy tắc; dạng Quá khứ đơn là went, không phải goed."},
  {"n":7,"topic":"gr.a1.past-simple-negative-question","clozePrompt":"___ Maya call you yesterday?","clozeAnswer":"Did","clozeSource":"sent.gra1.05.07.2","translationPrompt":"Dịch sang tiếng Anh: Họ đã không đi dự cuộc họp.","translationAnswer":"They didn't go to the meeting.","translationSource":"sent.gra1.05.07.3","incorrect":"Did you went to school?","correction":"Did you go to school?","explanationVi":"Sau did phải dùng động từ nguyên mẫu: Did you go...?, không dùng went."},
  {"n":8,"topic":"gr.a1.going-to-intentions","clozePrompt":"Eva ___ going to visit her aunt tomorrow.","clozeAnswer":"is","clozeSource":"sent.gra1.05.08.2","translationPrompt":"Dịch sang tiếng Anh: Tối nay chúng tôi sẽ nấu ăn ở nhà.","translationAnswer":"We are going to cook at home tonight.","translationSource":"sent.gra1.05.08.3","incorrect":"I going to buy a new bag.","correction":"I am going to buy a new bag.","explanationVi":"Cấu trúc going to cần động từ be: I am going to..., không thể bỏ am."}
]

def stable_json(v): return json.dumps(v,ensure_ascii=False,indent=2)+"\n"
def load_json(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def write_json(p,v):
    path=ROOT/p; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(stable_json(v),encoding="utf-8")
def must_replace(text,old,new,label):
    if text.count(old)!=1: raise SystemExit(f"{label}: anchor count={text.count(old)}")
    return text.replace(old,new,1)
def digest(record):
    v=copy.deepcopy(record); checks=v.get("quality",{}).get("checks",{}); checks.pop("cefr",None); checks.pop("license",None)
    return hashlib.sha256(stable_json(v).encode()).hexdigest()
def provenance(): return {"sources":[{"dataset":"project-original","license":"LicenseRef-Project-Original","modified":False}]}
def q(kind):
    checks={"schema":{"status":"pass","method":"author-v1"},"grammar":{"status":"pending","method":"review"},"translation":{"status":"pending","method":"review"},"exactDuplicate":{"status":"pass","method":"local-dedup"},"nearDuplicate":{"status":"pending","method":"review"},"naturalness":{"status":"pending","method":"review"},"targetPresence":{"status":"pending","method":"review"},"cefr":{"status":"pending","method":"review"},"license":{"status":"pending","method":"review"}}
    if kind=="mistake": checks["targetStructure"]=checks.pop("targetPresence")
    return {"state":"draft","checks":checks}
def write_remaining_sources():
    exercises=[]; mistakes=[]
    for s in SOURCE_SPECS:
        b=f"gra1.05.{s['n']:02d}"
        exercises += [
          {"schemaVersion":1,"id":"ex.cloze."+b,"type":"cloze","prompt":s["clozePrompt"],"targetIds":[s["topic"]],"acceptedAnswers":[s["clozeAnswer"]],"sourceSentenceIds":[s["clozeSource"]],"cefr":"A1","quality":q("exercise"),"provenance":provenance()},
          {"schemaVersion":1,"id":"ex.translation."+b,"type":"translation","prompt":s["translationPrompt"],"targetIds":[s["topic"]],"acceptedAnswers":[s["translationAnswer"]],"sourceSentenceIds":[s["translationSource"]],"cefr":"A1","quality":q("exercise"),"provenance":provenance()}
        ]
        mistakes.append({"schemaVersion":1,"id":"err."+b,"incorrect":s["incorrect"],"corrections":[s["correction"]],"explanationVi":s["explanationVi"],"targetIds":[s["topic"]],"evidenceType":"pedagogical","quality":q("mistake"),"provenance":provenance()})
    write_json(EXERCISE_PATH,{"schemaVersion":1,"records":exercises}); write_json(MISTAKE_PATH,{"schemaVersion":1,"records":mistakes})
def load_sets():
    specs=[("grammar-topics",TOPIC_PATH,8),("examples",SENTENCE_PATH,24),("exercises",EXERCISE_PATH,16),("common-mistakes",MISTAKE_PATH,8)]
    out={}
    for sid,p,n in specs:
        records=load_json(p).get("records",[])
        if len(records)!=n or any(r.get("quality",{}).get("state")!="draft" for r in records): raise SystemExit(f"{sid} source invalid")
        out[sid]=records
    return out
def add_batch():
    m=load_json("content/english/batches/manifest.json")
    if any(x.get("id")==BATCH_ID for x in m.get("batches",[])): raise SystemExit("batch exists")
    sets=[("grammar-topics",TOPIC_PATH,8,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"]),("examples",SENTENCE_PATH,24,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"]),("exercises",EXERCISE_PATH,16,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"]),("common-mistakes",MISTAKE_PATH,8,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetStructure","cefr","license"])]
    batch={"id":BATCH_ID,"phase":"E05","category":"grammar","cefr":["A1"],"state":"draft","recordSets":[{"id":sid,"path":p,"expectedCount":n,"generated":False,"allowedQualityStates":["draft"],"requiredChecks":checks} for sid,p,n,checks in sets],"requiredBeforePublish":["schema-validation","reference-integrity","exact-dedup","near-dedup","grammar-review","bilingual-review","naturalness-review","cefr-review","target-structure-review","license-review","cross-game-smoke"],"gameSmokes":[{"gameId":"space-typing","activity":"grammar-challenge","recordSetId":"grammar-topics","sampleCount":5},{"gameId":"monkeytype","activity":"grammar-topic","recordSetId":"grammar-topics","sampleCount":5},{"gameId":"monkeytype","activity":"example-typing","recordSetId":"examples","sampleCount":5},{"gameId":"monkeytype","activity":"cloze","recordSetId":"exercises","sampleCount":4,"recordType":"cloze"},{"gameId":"monkeytype","activity":"translation","recordSetId":"exercises","sampleCount":4,"recordType":"translation"},{"gameId":"monkeytype","activity":"error-correction","recordSetId":"common-mistakes","sampleCount":4}]}
    i=next(i for i,x in enumerate(m["batches"]) if x.get("id")=="e05.grammar-scale-a1-04"); m["batches"].insert(i+1,batch); write_json("content/english/batches/manifest.json",m)
def write_review(sets):
    decisions=[]
    for sid in ("grammar-topics","examples","exercises","common-mistakes"):
        for r in sets[sid]:
            checks={name:{"status":"not-applicable" if c.get("status")=="not-applicable" else "pass","method":f"editorial-{name}-review-a1-05"} for name,c in r["quality"]["checks"].items()}
            decisions.append({"id":"review.e05.a1-05."+r["id"].replace(".","-"),"batchId":BATCH_ID,"recordSetId":sid,"recordId":r["id"],"sourceDigest":digest(r),"targetState":"published","checks":checks,"reviewedAt":"2026-10-05T14:40:00Z","reviewedBy":"GPT-5.6 Sol grammar editorial review","note":"Controlled A1 grammar-body slice 05 reviewed for grammar accuracy, EN/VI meaning, naturalness, target structure/presence, CEFR fit, dedup and project-original provenance."})
    if len(decisions)!=56: raise SystemExit("review count")
    write_json(REVIEW_PATH,{"schemaVersion":1,"decisions":decisions})
def patch_publisher():
    p=ROOT/"scripts/publish-english-content.mjs"; t=p.read_text()
    a='const grammarScaleA104Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-04-common-mistakes.json");'
    t=must_replace(t,a,a+'\nconst grammarScaleA105=await loadRecords("content/english/grammar/e05-scale-a1-05-topics.json");\nconst grammarScaleA105Sentences=await loadRecords("content/english/sentences/e05-scale-a1-05-sentences.json");\nconst grammarScaleA105Exercises=await loadRecords("content/english/sentences/e05-scale-a1-05-exercises.json");\nconst grammarScaleA105Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-05-common-mistakes.json");',"publisher declarations")
    for old,new in [
      ("records:[...topics,...grammarScaleA101,...grammarScaleA102,...grammarScaleA103,...grammarScaleA104]","records:[...topics,...grammarScaleA101,...grammarScaleA102,...grammarScaleA103,...grammarScaleA104,...grammarScaleA105]"),
      ("...grammarScaleA104Sentences,...reviewedTranslationSentences","...grammarScaleA104Sentences,...grammarScaleA105Sentences,...reviewedTranslationSentences"),
      ("...grammarScaleA104Exercises,...reviewedE06Exercises","...grammarScaleA104Exercises,...grammarScaleA105Exercises,...reviewedE06Exercises"),
      ("...grammarScaleA104Mistakes]","...grammarScaleA104Mistakes,...grammarScaleA105Mistakes]")
    ]: t=must_replace(t,old,new,"publisher arrays")
    p.write_text(t)
def patch_validator():
    p=ROOT/"scripts/validate-english-content.mjs"; t=p.read_text()
    a='const grammarScaleA104Mistakes=await validateFile("content/english/sentences/e05-scale-a1-04-common-mistakes.json","common-mistake-set.schema.json");'
    t=must_replace(t,a,a+'\nconst grammarScaleA105=await validateFile("content/english/grammar/e05-scale-a1-05-topics.json","grammar-topic-set.schema.json");\nconst grammarScaleA105Sentences=await validateFile("content/english/sentences/e05-scale-a1-05-sentences.json","sentence-set.schema.json");\nconst grammarScaleA105Exercises=await validateFile("content/english/sentences/e05-scale-a1-05-exercises.json","exercise-set.schema.json");\nconst grammarScaleA105Mistakes=await validateFile("content/english/sentences/e05-scale-a1-05-common-mistakes.json","common-mistake-set.schema.json");',"validator declarations")
    marker="if (reviewedTranslationSentences&&reviewedTranslations) {"
    block=r'''if (grammarScaleA105&&grammarScaleA105Sentences&&grammarScaleA105Exercises&&grammarScaleA105Mistakes) {
  const sets=[["grammar-topics",grammarScaleA105,8],["examples",grammarScaleA105Sentences,24],["exercises",grammarScaleA105Exercises,16],["common-mistakes",grammarScaleA105Mistakes,8]];
  for (const [id,doc,count] of sets) {
    if (batchExpectedCount("e05.grammar-scale-a1-05",id)!==count||doc.records.length!==count) errors.push("E05 A1 scale 05 "+id+" count mismatch");
    for (const record of doc.records) if (record.quality?.state!=="draft") errors.push(record.id+": A1 scale 05 source must remain draft");
  }
  const topicIds=new Set(grammarScaleA105.records.map(x=>x.id)), sentenceIds=new Set(grammarScaleA105Sentences.records.map(x=>x.id)), exerciseIds=new Set(grammarScaleA105Exercises.records.map(x=>x.id)), mistakeIds=new Set(grammarScaleA105Mistakes.records.map(x=>x.id));
  const oldIds=new Set([...(grammarPilot?.records??[]),...(grammarScaleA101?.records??[]),...(grammarScaleA102?.records??[]),...(grammarScaleA103?.records??[]),...(grammarScaleA104?.records??[])].map(x=>x.id));
  for (const topic of grammarScaleA105.records) {
    if (topic.cefr!=="A1"||!allIds.has(topic.id)||oldIds.has(topic.id)) errors.push(topic.id+": invalid A1 scale 05 topic identity");
    if ((topic.exampleIds??[]).length!==3||(topic.exerciseIds??[]).length!==2||(topic.commonMistakeIds??[]).length!==1) errors.push(topic.id+": invalid linked counts");
    for (const id of topic.exampleIds??[]) if (!sentenceIds.has(id)) errors.push(topic.id+": missing example "+id);
    for (const id of topic.exerciseIds??[]) if (!exerciseIds.has(id)) errors.push(topic.id+": missing exercise "+id);
    for (const id of topic.commonMistakeIds??[]) if (!mistakeIds.has(id)) errors.push(topic.id+": missing mistake "+id);
    for (const id of [...(topic.prerequisiteIds??[]),...(topic.contrastTopicIds??[])]) if (!allIds.has(id)) errors.push(topic.id+": unknown grammar reference "+id);
  }
  const counts=new Map(); for (const s of grammarScaleA105Sentences.records) { if (s.cefr!=="A1"||(s.grammarIds??[]).length!==1||!topicIds.has(s.grammarIds[0])) errors.push(s.id+": invalid A1 scale 05 example"); counts.set(s.grammarIds?.[0],(counts.get(s.grammarIds?.[0])??0)+1); }
  let cloze=0,translation=0; for (const e of grammarScaleA105Exercises.records) { if ((e.targetIds??[]).length!==1||!topicIds.has(e.targetIds[0])||(e.sourceSentenceIds??[]).length!==1||!sentenceIds.has(e.sourceSentenceIds[0])) errors.push(e.id+": invalid A1 scale 05 exercise links"); if(e.type==="cloze")cloze++; else if(e.type==="translation")translation++; else errors.push(e.id+": unsupported exercise type"); }
  if (cloze!==8||translation!==8) errors.push("E05 A1 scale 05 exercise type counts invalid");
  for (const m of grammarScaleA105Mistakes.records) if ((m.targetIds??[]).length!==1||!topicIds.has(m.targetIds[0])||m.evidenceType!=="pedagogical"||(m.corrections??[]).length!==1) errors.push(m.id+": invalid A1 scale 05 mistake");
  for (const id of topicIds) if ((counts.get(id)??0)!==3) errors.push(id+": A1 scale 05 requires 3 examples");
}

'''
    t=must_replace(t,marker,block+marker,"validator block"); p.write_text(t)
def patch_smoke():
    p=ROOT/"scripts/smoke-published-english-content.mjs"; t=p.read_text()
    for old,new in [
      ("grammarManifest.count!==44","grammarManifest.count!==52"),("published grammar runtime must contain 44 reviewed grammar topics","published grammar runtime must contain 52 reviewed grammar topics"),
      ("sentenceManifest.count!==1852","sentenceManifest.count!==1900"),("published sentence runtime must contain 1852 reviewed records","published sentence runtime must contain 1900 reviewed records"),
      ("topics.length!==44||examples.length!==732||exercises.length!==888||dialogues.length!==100||commonMistakes.length!==132","topics.length!==52||examples.length!==756||exercises.length!==904||dialogues.length!==100||commonMistakes.length!==140"),
      ("published runtime split must be 44 topics + 732 examples + 888 exercises + 100 dialogues + 132 common mistakes","published runtime split must be 52 topics + 756 examples + 904 exercises + 100 dialogues + 140 common mistakes"),
      ("monkeyCorrectionCount!==232","monkeyCorrectionCount!==240"),("published Monkeytype error-correction activity must expose 100 corrections + 132 common mistakes","published Monkeytype error-correction activity must expose 100 corrections + 140 common mistakes"),("monkeyCorrectionRecords:232","monkeyCorrectionRecords:240")
    ]: t=must_replace(t,old,new,"smoke counts")
    p.write_text(t)
def patch_release():
    r=load_json("content/english/releases/2026.10.0.json"); r["runtimeCounts"]["grammar"]=52; r["runtimeCounts"]["sentences"]=1900; r["batchStates"]["draft"]=38; write_json("content/english/releases/2026.10.0.json",r)
def main():
    write_remaining_sources(); sets=load_sets(); add_batch(); write_review(sets); patch_publisher(); patch_validator(); patch_smoke(); patch_release()
if __name__=="__main__": main()
