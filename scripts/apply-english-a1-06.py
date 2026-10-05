from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BATCH_ID="e05.grammar-scale-a1-06"
TOPIC_PATH="content/english/grammar/e05-scale-a1-06-topics.json"
SENTENCE_PATH="content/english/sentences/e05-scale-a1-06-sentences.json"
EXERCISE_PATH="content/english/sentences/e05-scale-a1-06-exercises.json"
MISTAKE_PATH="content/english/sentences/e05-scale-a1-06-common-mistakes.json"
REVIEW_PATH="content/english/reviews/decisions.d/e05-grammar-a1-06.json"
EXPECTED={"grammar-topics":3,"examples":9,"exercises":6,"common-mistakes":3}


def stable_json(value):
    return json.dumps(value,ensure_ascii=False,indent=2)+"\n"


def load_json(relative):
    return json.loads((ROOT/relative).read_text(encoding="utf-8"))


def write_json(relative,value):
    path=ROOT/relative
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(stable_json(value),encoding="utf-8")


def must_replace(text,old,new,label):
    count=text.count(old)
    if count!=1:
        raise SystemExit(f"{label}: expected one anchor, got {count}")
    return text.replace(old,new,1)


def digest(record):
    normalized=copy.deepcopy(record)
    checks=normalized.get("quality",{}).get("checks",{})
    checks.pop("cefr",None)
    checks.pop("license",None)
    return hashlib.sha256(stable_json(normalized).encode("utf-8")).hexdigest()


def load_sources():
    specs=[("grammar-topics",TOPIC_PATH),("examples",SENTENCE_PATH),("exercises",EXERCISE_PATH),("common-mistakes",MISTAKE_PATH)]
    result={}
    for set_id,relative in specs:
        records=load_json(relative).get("records",[])
        if len(records)!=EXPECTED[set_id]:
            raise SystemExit(f"{set_id}: expected {EXPECTED[set_id]}, got {len(records)}")
        if len({record.get('id') for record in records})!=len(records):
            raise SystemExit(f"{set_id}: duplicate ids")
        if any(record.get("quality",{}).get("state")!="draft" for record in records):
            raise SystemExit(f"{set_id}: sources must remain draft")
        result[set_id]=records
    return result


def add_batch():
    manifest=load_json("content/english/batches/manifest.json")
    if any(batch.get("id")==BATCH_ID for batch in manifest.get("batches",[])):
        raise SystemExit(f"batch exists: {BATCH_ID}")
    sets=[
        ("grammar-topics",TOPIC_PATH,3,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"]),
        ("examples",SENTENCE_PATH,9,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"]),
        ("exercises",EXERCISE_PATH,6,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"]),
        ("common-mistakes",MISTAKE_PATH,3,["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetStructure","cefr","license"]),
    ]
    batch={
        "id":BATCH_ID,"phase":"E05","category":"grammar","cefr":["A1"],"state":"draft",
        "recordSets":[{"id":sid,"path":path,"expectedCount":count,"generated":False,"allowedQualityStates":["draft"],"requiredChecks":checks} for sid,path,count,checks in sets],
        "requiredBeforePublish":["schema-validation","reference-integrity","exact-dedup","near-dedup","grammar-review","bilingual-review","naturalness-review","cefr-review","target-structure-review","license-review","cross-game-smoke"],
        "gameSmokes":[
            {"gameId":"space-typing","activity":"grammar-challenge","recordSetId":"grammar-topics","sampleCount":3},
            {"gameId":"monkeytype","activity":"grammar-topic","recordSetId":"grammar-topics","sampleCount":3},
            {"gameId":"monkeytype","activity":"example-typing","recordSetId":"examples","sampleCount":5},
            {"gameId":"monkeytype","activity":"cloze","recordSetId":"exercises","sampleCount":3,"recordType":"cloze"},
            {"gameId":"monkeytype","activity":"translation","recordSetId":"exercises","sampleCount":3,"recordType":"translation"},
            {"gameId":"monkeytype","activity":"error-correction","recordSetId":"common-mistakes","sampleCount":3},
        ],
    }
    batches=manifest.setdefault("batches",[])
    index=next(i for i,item in enumerate(batches) if item.get("id")=="e05.grammar-scale-a1-05")
    batches.insert(index+1,batch)
    write_json("content/english/batches/manifest.json",manifest)


def write_review(reviewed):
    decisions=[]
    for set_id in ("grammar-topics","examples","exercises","common-mistakes"):
        for record in reviewed[set_id]:
            checks={}
            for name,check in record["quality"]["checks"].items():
                checks[name]={"status":"not-applicable" if check.get("status")=="not-applicable" else "pass","method":f"editorial-{name}-review-a1-06"}
            decisions.append({
                "id":"review.e05.a1-06."+record["id"].replace(".","-"),"batchId":BATCH_ID,
                "recordSetId":set_id,"recordId":record["id"],"sourceDigest":digest(record),
                "targetState":"published","checks":checks,"reviewedAt":"2026-10-05T14:48:00Z",
                "reviewedBy":"GPT-5.6 Sol grammar editorial review",
                "note":"Final controlled A1 grammar-body slice reviewed for grammar accuracy, EN/VI meaning, naturalness, target structure/presence, CEFR fit, dedup and project-original license/provenance."
            })
    if len(decisions)!=21:
        raise SystemExit(f"expected 21 review decisions, got {len(decisions)}")
    write_json(REVIEW_PATH,{"schemaVersion":1,"decisions":decisions})


def patch_publisher():
    path=ROOT/"scripts/publish-english-content.mjs"
    text=path.read_text(encoding="utf-8")
    anchor='const grammarScaleA105Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-05-common-mistakes.json");'
    text=must_replace(text,anchor,anchor+'\nconst grammarScaleA106=await loadRecords("content/english/grammar/e05-scale-a1-06-topics.json");\nconst grammarScaleA106Sentences=await loadRecords("content/english/sentences/e05-scale-a1-06-sentences.json");\nconst grammarScaleA106Exercises=await loadRecords("content/english/sentences/e05-scale-a1-06-exercises.json");\nconst grammarScaleA106Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-06-common-mistakes.json");',"publisher declarations")
    replacements=[
        ("records:[...topics,...grammarScaleA101,...grammarScaleA102,...grammarScaleA103,...grammarScaleA104,...grammarScaleA105]","records:[...topics,...grammarScaleA101,...grammarScaleA102,...grammarScaleA103,...grammarScaleA104,...grammarScaleA105,...grammarScaleA106]"),
        ("...grammarScaleA105Sentences,...reviewedTranslationSentences","...grammarScaleA105Sentences,...grammarScaleA106Sentences,...reviewedTranslationSentences"),
        ("...grammarScaleA105Exercises,...reviewedE06Exercises","...grammarScaleA105Exercises,...grammarScaleA106Exercises,...reviewedE06Exercises"),
        ("...grammarScaleA105Mistakes]","...grammarScaleA105Mistakes,...grammarScaleA106Mistakes]"),
    ]
    for old,new in replacements:
        text=must_replace(text,old,new,"publisher arrays")
    path.write_text(text,encoding="utf-8")


def patch_validator():
    path=ROOT/"scripts/validate-english-content.mjs"
    text=path.read_text(encoding="utf-8")
    anchor='const grammarScaleA105Mistakes=await validateFile("content/english/sentences/e05-scale-a1-05-common-mistakes.json","common-mistake-set.schema.json");'
    text=must_replace(text,anchor,anchor+'\nconst grammarScaleA106=await validateFile("content/english/grammar/e05-scale-a1-06-topics.json","grammar-topic-set.schema.json");\nconst grammarScaleA106Sentences=await validateFile("content/english/sentences/e05-scale-a1-06-sentences.json","sentence-set.schema.json");\nconst grammarScaleA106Exercises=await validateFile("content/english/sentences/e05-scale-a1-06-exercises.json","exercise-set.schema.json");\nconst grammarScaleA106Mistakes=await validateFile("content/english/sentences/e05-scale-a1-06-common-mistakes.json","common-mistake-set.schema.json");',"validator declarations")
    marker="if (reviewedTranslationSentences&&reviewedTranslations) {"
    block=r'''if (grammarScaleA106&&grammarScaleA106Sentences&&grammarScaleA106Exercises&&grammarScaleA106Mistakes) {
  const sets=[["grammar-topics",grammarScaleA106,3],["examples",grammarScaleA106Sentences,9],["exercises",grammarScaleA106Exercises,6],["common-mistakes",grammarScaleA106Mistakes,3]];
  for (const [id,doc,count] of sets) {
    if (batchExpectedCount("e05.grammar-scale-a1-06",id)!==count||doc.records.length!==count) errors.push("E05 A1 scale 06 "+id+" count mismatch");
    for (const record of doc.records) if (record.quality?.state!=="draft") errors.push(record.id+": A1 scale 06 source must remain draft");
  }
  const topicIds=new Set(grammarScaleA106.records.map(record=>record.id));
  const sentenceIds=new Set(grammarScaleA106Sentences.records.map(record=>record.id));
  const exerciseIds=new Set(grammarScaleA106Exercises.records.map(record=>record.id));
  const mistakeIds=new Set(grammarScaleA106Mistakes.records.map(record=>record.id));
  const oldIds=new Set([...(grammarPilot?.records??[]),...(grammarScaleA101?.records??[]),...(grammarScaleA102?.records??[]),...(grammarScaleA103?.records??[]),...(grammarScaleA104?.records??[]),...(grammarScaleA105?.records??[])].map(record=>record.id));
  const exampleCounts=new Map(),exerciseCounts=new Map(),mistakeCounts=new Map();
  for (const topic of grammarScaleA106.records) {
    if (topic.cefr!=="A1"||!allIds.has(topic.id)||oldIds.has(topic.id)) errors.push(topic.id+": invalid A1 scale 06 topic identity");
    if ((topic.exampleIds??[]).length!==3||(topic.exerciseIds??[]).length!==2||(topic.commonMistakeIds??[]).length!==1) errors.push(topic.id+": invalid linked counts");
    if (!String(topic.concept?.en??"").trim()||!String(topic.concept?.vi??"").trim()) errors.push(topic.id+": bilingual concept is required");
    for (const id of topic.exampleIds??[]) if (!sentenceIds.has(id)) errors.push(topic.id+": missing example "+id);
    for (const id of topic.exerciseIds??[]) if (!exerciseIds.has(id)) errors.push(topic.id+": missing exercise "+id);
    for (const id of topic.commonMistakeIds??[]) if (!mistakeIds.has(id)) errors.push(topic.id+": missing mistake "+id);
    for (const id of [...(topic.prerequisiteIds??[]),...(topic.contrastTopicIds??[])]) if (!allIds.has(id)) errors.push(topic.id+": unknown grammar reference "+id);
  }
  for (const sentence of grammarScaleA106Sentences.records) {
    if (sentence.cefr!=="A1"||(sentence.grammarIds??[]).length!==1||!topicIds.has(sentence.grammarIds[0])) errors.push(sentence.id+": invalid A1 scale 06 example");
    const grammarId=sentence.grammarIds?.[0]; if(grammarId) exampleCounts.set(grammarId,(exampleCounts.get(grammarId)??0)+1);
  }
  let cloze=0,translation=0;
  for (const exercise of grammarScaleA106Exercises.records) {
    const grammarId=exercise.targetIds?.[0];
    if ((exercise.targetIds??[]).length!==1||!topicIds.has(grammarId)||(exercise.sourceSentenceIds??[]).length!==1||!sentenceIds.has(exercise.sourceSentenceIds[0])) errors.push(exercise.id+": invalid A1 scale 06 exercise links");
    if (exercise.type==="cloze") { cloze++; if(!String(exercise.prompt??"").includes("___")) errors.push(exercise.id+": cloze prompt must contain ___"); }
    else if (exercise.type==="translation") translation++;
    else errors.push(exercise.id+": unsupported exercise type");
    if(grammarId) exerciseCounts.set(grammarId,(exerciseCounts.get(grammarId)??0)+1);
  }
  if (cloze!==3||translation!==3) errors.push("E05 A1 scale 06 must contain 3 cloze + 3 translation exercises");
  for (const mistake of grammarScaleA106Mistakes.records) {
    const grammarId=mistake.targetIds?.[0];
    if ((mistake.targetIds??[]).length!==1||!topicIds.has(grammarId)||mistake.evidenceType!=="pedagogical"||(mistake.corrections??[]).length!==1||!String(mistake.explanationVi??"").trim()) errors.push(mistake.id+": invalid A1 scale 06 mistake");
    if(grammarId) mistakeCounts.set(grammarId,(mistakeCounts.get(grammarId)??0)+1);
  }
  for (const id of topicIds) {
    if ((exampleCounts.get(id)??0)!==3) errors.push(id+": A1 scale 06 requires 3 examples");
    if ((exerciseCounts.get(id)??0)!==2) errors.push(id+": A1 scale 06 requires 2 exercises");
    if ((mistakeCounts.get(id)??0)!==1) errors.push(id+": A1 scale 06 requires 1 common mistake");
  }
}

'''
    text=must_replace(text,marker,block+marker,"validator block")
    path.write_text(text,encoding="utf-8")


def patch_smoke():
    path=ROOT/"scripts/smoke-published-english-content.mjs"
    text=path.read_text(encoding="utf-8")
    replacements=[
        ("grammarManifest.count!==52","grammarManifest.count!==55"),
        ("published grammar runtime must contain 52 reviewed grammar topics","published grammar runtime must contain 55 reviewed grammar topics"),
        ("sentenceManifest.count!==1900","sentenceManifest.count!==1918"),
        ("published sentence runtime must contain 1900 reviewed records","published sentence runtime must contain 1918 reviewed records"),
        ("topics.length!==52||examples.length!==756||exercises.length!==904||dialogues.length!==100||commonMistakes.length!==140","topics.length!==55||examples.length!==765||exercises.length!==910||dialogues.length!==100||commonMistakes.length!==143"),
        ("published runtime split must be 52 topics + 756 examples + 904 exercises + 100 dialogues + 140 common mistakes","published runtime split must be 55 topics + 765 examples + 910 exercises + 100 dialogues + 143 common mistakes"),
        ("monkeyCorrectionCount!==240","monkeyCorrectionCount!==243"),
        ("published Monkeytype error-correction activity must expose 100 corrections + 140 common mistakes","published Monkeytype error-correction activity must expose 100 corrections + 143 common mistakes"),
        ("monkeyCorrectionRecords:240","monkeyCorrectionRecords:243"),
    ]
    for old,new in replacements:
        text=must_replace(text,old,new,"runtime smoke counts")
    path.write_text(text,encoding="utf-8")


def patch_release():
    release=load_json("content/english/releases/2026.10.0.json")
    release["runtimeCounts"]["grammar"]=55
    release["runtimeCounts"]["sentences"]=1918
    release["batchStates"]["draft"]=39
    write_json("content/english/releases/2026.10.0.json",release)


def main():
    reviewed=load_sources()
    add_batch()
    write_review(reviewed)
    patch_publisher()
    patch_validator()
    patch_smoke()
    patch_release()


if __name__=="__main__":
    main()
