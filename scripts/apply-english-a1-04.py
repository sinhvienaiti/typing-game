from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH_ID = "e05.grammar-scale-a1-04"
TOPIC_PATH = "content/english/grammar/e05-scale-a1-04-topics.json"
SENTENCE_PATH = "content/english/sentences/e05-scale-a1-04-sentences.json"
EXERCISE_PATH = "content/english/sentences/e05-scale-a1-04-exercises.json"
MISTAKE_PATH = "content/english/sentences/e05-scale-a1-04-common-mistakes.json"
REVIEW_PATH = "content/english/reviews/decisions.d/e05-grammar-a1-04.json"
EXPECTED_COUNTS = {"grammar-topics": 8, "examples": 24, "exercises": 16, "common-mistakes": 8}
REVIEWED_DIGESTS = {
  "grammar-topics": {
    "gr.a1.likes-gerund-noun": "6413f184d571ad3ae4ade90aa2085c4f07c86a265f22eda38b6fe6f83be68f32",
    "gr.a1.want-need-infinitive": "b1e1c225460a48cd6d9d25c9bdfcd905defaff9c14f7d1f28e41f79450bd171b",
    "gr.a1.time-prepositions": "8d7e5103f2215a9a718f628477b7fb2a32b18026c46bc4c64fb463e3d097bfcf",
    "gr.a1.place-prepositions": "13fc0cc16706e2953f3370923c913d0d17a2f535b3728cc9d23fcfe9a303369c",
    "gr.a1.movement-prepositions": "9119a3a47cd16a15aa275d662139492160849f468368536b2062afee8f52b275",
    "gr.a1.adjective-position": "1935ebd6fd06e0eb3cd61db150bcf4cbe8481119cad320b377a0f313530c8cc9",
    "gr.a1.degree-very-really": "ac74f9820704130851eb1b38d54b10a50f7e856faac7e63a7eaa777269e59727",
    "gr.a1.coordinators": "201cf4bdb1d0dd73af853b19fc03d9e5ae959c510e240a6edc83fa7bce1536ae"
  },
  "examples": {
    "sent.gra1.04.01.1": "30dae41d4fa366f2db72699e04f7a674739635ea87dad73cb7385d2862a024b0",
    "sent.gra1.04.01.2": "008ba6db0b60a5572b245886cdfaf72164a9e019094401d83ca83e072f0d8065",
    "sent.gra1.04.01.3": "aa46b49b170d481c393f5bc8bcc65f4b1762c9b7d8cfe040b3912fb963cce6ff",
    "sent.gra1.04.02.1": "99a71bdac3e7f1073851279c53054613968693365be3a38f9cb2222ff2bd28f8",
    "sent.gra1.04.02.2": "b4ce41a9d4159f31198e44fce43294742883304052ae5178190394c3277430c1",
    "sent.gra1.04.02.3": "76b66882eb3d71b62ee46946329e55344e056e12c97561701741045486b1724f",
    "sent.gra1.04.03.1": "fe13b1504f6917a5375dc5adbdb470cd2130419ed579d6b62a80279ba42de204",
    "sent.gra1.04.03.2": "cfeb962010c22369144252e60361dbd0716c48c18f59005abbb0afdd6a8d596d",
    "sent.gra1.04.03.3": "bd05227587b15967af2b0726766bf62c49666d034fef2f49b0c15318468bb81b",
    "sent.gra1.04.04.1": "ad4967d5837a14ebbf377a26ada0292f3a0b5147c6328ce655e55833081fad3c",
    "sent.gra1.04.04.2": "17b2994b6c4fce6655c319bd89d0eb7db4c6c532642ced900fd7102522122861",
    "sent.gra1.04.04.3": "bd580a9d08bcd80c3a564865c53f8b2dc18b3cde956f4125bce2a5b5a47db77e",
    "sent.gra1.04.05.1": "46ea1e1e3db702ce5a0b77f425c42cf2c3d14b03c8adfa9770d249b32c041f51",
    "sent.gra1.04.05.2": "1f928fc89e90eaa18b3481804608575b0d9e9900e880789120834113b0523b64",
    "sent.gra1.04.05.3": "584f719bb5d86ae31e8172505041a6599a4ae86b06c63f1473dc0abf091ef31b",
    "sent.gra1.04.06.1": "6fed19e5f642760a5116f71cd16d45db7ad28f264860562901d310d675edbe88",
    "sent.gra1.04.06.2": "a69babff46ecc6b7c64c4fe9a06fac08f0d8c79d74a9fccf686d8c2cb83eb030",
    "sent.gra1.04.06.3": "b98a6c0c557ac4945defccf34449a85a18dc69ce264792777e1c3b96c83a15cc",
    "sent.gra1.04.07.1": "3f83a06e57a3e1928df29a08c67b11e1b606286510483581eb3813aaf422ba2a",
    "sent.gra1.04.07.2": "a03b983e58301642c72fc3db02258194c33a5fd4da9e0b4eb982e4c219b16b93",
    "sent.gra1.04.07.3": "c0a1747b49618018c13da7d5d04778232ed89905d77dcd9b328a10821899d8c0",
    "sent.gra1.04.08.1": "287195798b51042a7dba109ec89ed52eb8044acf2d43eb47498aba92dbbd0fe0",
    "sent.gra1.04.08.2": "174e57ef8eb40f9610028699982d921a1d4ef8165ac599ea661fb2881826341c",
    "sent.gra1.04.08.3": "1840bcf4b2fa01fbc3f8e4ca75cb991ee0caa8e3e12a2b14de0f155ae62885f0"
  },
  "exercises": {
    "ex.cloze.gra1.04.01": "7fbbb64526fccbf1cda27153114bf0b5f8bad701f6f1b34934703e1ad571e650",
    "ex.translation.gra1.04.01": "74d715953282ed1b61aa2182b4992f22d701b50131a96bbbf8133827570786ef",
    "ex.cloze.gra1.04.02": "7a4e77ca84262cfc79dcb0585be0ed4585a06ed664ea19fb6895e961914822d1",
    "ex.translation.gra1.04.02": "63ecfc92116b11cca4d66ef05d1bbfaf39bd5d8b16ad63bde38e3ba86e3622dd",
    "ex.cloze.gra1.04.03": "df9d80c1ac467a9f5b9c38d20f3eb27d12000b5aa6d83b22ee062ad3703aa03b",
    "ex.translation.gra1.04.03": "ab33187fc46bb8263f6aaa14619403417070461153e7e64b12336d68feabf230",
    "ex.cloze.gra1.04.04": "a3a404a0a92b0e878945558bf9a01ae12c78665eb4d4b5796028866279a74500",
    "ex.translation.gra1.04.04": "4a6c865a138b60cfe6c298981190cfa75f8ba1b745cf29d8424c49d8af049004",
    "ex.cloze.gra1.04.05": "52f57692f0a9c01bc15e9d61e8baa1cd983601734957125802116cfc91f2b13a",
    "ex.translation.gra1.04.05": "ad00023858cb2b1552f411cbe76efeac8646a9aefea6e59c468a6f69c79bb452",
    "ex.cloze.gra1.04.06": "242f5432445882273020e13f6d99a23aa266a11621863f558fb01ff0f34ca146",
    "ex.translation.gra1.04.06": "e31cf41478af0325858d99e2f2cda447b73c19cbe2a8d04b55ed2579ce72e200",
    "ex.cloze.gra1.04.07": "cf3074940d0e3ff2b11ab6292407840967e63af2bc0b2291f491ed774b7941e2",
    "ex.translation.gra1.04.07": "1917993ff3462a129e84821a2e066b17e5d40259a3f0158200c29ed455eeaf30",
    "ex.cloze.gra1.04.08": "25b0707b260b46dc432b1708e6f56ac372b0c4cd2ab73bc39ef4e4c35be0f094",
    "ex.translation.gra1.04.08": "53cdd1295b316f9d69c95801c6d38e249dd1a18bda310e2579d14fc2c429a7ef"
  },
  "common-mistakes": {
    "err.gra1.04.01": "d4cc6a94d3800c3a685d16bd8eb46e86d28d3e1b163960f6b09b77386e097895",
    "err.gra1.04.02": "0b94c5f422bb02928226b7429257fbcff9f0b121797419fb465168a25151f76e",
    "err.gra1.04.03": "70de95b0d68ea7f949103d53a0ccb77d1f2b1a70fe86e21b3b1aa9e119715982",
    "err.gra1.04.04": "fb5f0b7aaa3959581453433192a663a56a043b07218984eb67cc07da8b731832",
    "err.gra1.04.05": "382e892b996068e08bad43a9e423d18a8dc4626dbcae53bf9b5673bdc6f8a1d4",
    "err.gra1.04.06": "54921da6aa996403e8da8d39c6d134d6621348b17eac26da3c5822de2810cfca",
    "err.gra1.04.07": "b5c16ba46252d40ad5e5e4f0b5eb66ae9ee965391a118071b50ae9e36ba2fe3a",
    "err.gra1.04.08": "c937a85402068147330cbaf7053096159288182559612c76f0ecef470bdb9727"
  }
}


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def load_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def write_json(relative, value):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(stable_json(value), encoding="utf-8")


def must_replace(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one anchor, got {count}: {old[:140]!r}")
    return text.replace(old, new, 1)


def source_digest(record):
    normalized = copy.deepcopy(record)
    checks = normalized.get("quality", {}).get("checks", {})
    checks.pop("cefr", None)
    checks.pop("license", None)
    return hashlib.sha256(stable_json(normalized).encode("utf-8")).hexdigest()


def load_and_lock_reviewed_sources():
    specs = [("grammar-topics", TOPIC_PATH), ("examples", SENTENCE_PATH), ("exercises", EXERCISE_PATH), ("common-mistakes", MISTAKE_PATH)]
    result = {}
    for record_set_id, relative in specs:
        records = load_json(relative).get("records", [])
        expected = EXPECTED_COUNTS[record_set_id]
        if len(records) != expected:
            raise SystemExit(f"{record_set_id}: expected {expected} reviewed records, got {len(records)}")
        locked = REVIEWED_DIGESTS[record_set_id]
        ids = [record.get("id") for record in records]
        if set(ids) != set(locked):
            raise SystemExit(f"{record_set_id}: reviewed record IDs drifted; missing={sorted(set(locked)-set(ids))}, extra={sorted(set(ids)-set(locked))}")
        for record in records:
            digest = source_digest(record)
            if digest != locked[record["id"]]:
                raise SystemExit(f"{record_set_id}/{record['id']}: source digest changed after editorial review; expected {locked[record['id']]}, got {digest}")
            if record.get("quality", {}).get("state") != "draft":
                raise SystemExit(f"{record['id']}: authoring source must remain draft")
        result[record_set_id] = records
    return result


def add_batch_manifest():
    manifest = load_json("content/english/batches/manifest.json")
    if any(batch.get("id") == BATCH_ID for batch in manifest.get("batches", [])):
        raise SystemExit(f"batch already exists: {BATCH_ID}")
    record_sets = [
        ("grammar-topics", TOPIC_PATH, 8, ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"]),
        ("examples", SENTENCE_PATH, 24, ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"]),
        ("exercises", EXERCISE_PATH, 16, ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"]),
        ("common-mistakes", MISTAKE_PATH, 8, ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetStructure", "cefr", "license"]),
    ]
    batch = {
        "id": BATCH_ID, "phase": "E05", "category": "grammar", "cefr": ["A1"], "state": "draft",
        "recordSets": [{"id": sid, "path": path, "expectedCount": count, "generated": False, "allowedQualityStates": ["draft"], "requiredChecks": checks} for sid,path,count,checks in record_sets],
        "requiredBeforePublish": ["schema-validation", "reference-integrity", "exact-dedup", "near-dedup", "grammar-review", "bilingual-review", "naturalness-review", "cefr-review", "target-structure-review", "license-review", "cross-game-smoke"],
        "gameSmokes": [
            {"gameId":"space-typing","activity":"grammar-challenge","recordSetId":"grammar-topics","sampleCount":5},
            {"gameId":"monkeytype","activity":"grammar-topic","recordSetId":"grammar-topics","sampleCount":5},
            {"gameId":"monkeytype","activity":"example-typing","recordSetId":"examples","sampleCount":5},
            {"gameId":"monkeytype","activity":"cloze","recordSetId":"exercises","sampleCount":4,"recordType":"cloze"},
            {"gameId":"monkeytype","activity":"translation","recordSetId":"exercises","sampleCount":4,"recordType":"translation"},
            {"gameId":"monkeytype","activity":"error-correction","recordSetId":"common-mistakes","sampleCount":4},
        ],
    }
    batches = manifest.setdefault("batches", [])
    idx = next(i for i,item in enumerate(batches) if item.get("id") == "e05.grammar-scale-a1-03")
    batches.insert(idx + 1, batch)
    write_json("content/english/batches/manifest.json", manifest)


def write_review_ledger(reviewed):
    decisions=[]
    for set_id in ("grammar-topics","examples","exercises","common-mistakes"):
        for record in reviewed[set_id]:
            checks={}
            for name, check in record["quality"]["checks"].items():
                status="not-applicable" if check.get("status")=="not-applicable" else "pass"
                checks[name]={"status":status,"method":f"editorial-{name}-review-a1-04"}
            decisions.append({
                "id":"review.e05.a1-04."+record["id"].replace(".","-"), "batchId":BATCH_ID, "recordSetId":set_id, "recordId":record["id"],
                "sourceDigest":REVIEWED_DIGESTS[set_id][record["id"]], "targetState":"published", "checks":checks,
                "reviewedAt":"2026-10-05T09:10:00Z", "reviewedBy":"GPT-5.6 Sol grammar editorial review",
                "note":"Controlled A1 grammar-body slice 04 reviewed for grammar accuracy, EN/VI meaning, naturalness, target structure/presence, CEFR fit, exact/near dedup and project-original license/provenance. Near-similar examples were retained only when their grammar target and pedagogical function were distinct."
            })
    if len(decisions)!=56: raise SystemExit(f"expected 56 review decisions, got {len(decisions)}")
    write_json(REVIEW_PATH,{"schemaVersion":1,"decisions":decisions})


def patch_publisher():
    path=ROOT/"scripts/publish-english-content.mjs"; text=path.read_text(encoding="utf-8")
    anchor='const grammarScaleA103Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-03-common-mistakes.json");'
    text=must_replace(text,anchor,anchor+'\nconst grammarScaleA104=await loadRecords("content/english/grammar/e05-scale-a1-04-topics.json");'+'\nconst grammarScaleA104Sentences=await loadRecords("content/english/sentences/e05-scale-a1-04-sentences.json");'+'\nconst grammarScaleA104Exercises=await loadRecords("content/english/sentences/e05-scale-a1-04-exercises.json");'+'\nconst grammarScaleA104Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-04-common-mistakes.json");',"publisher A1-04 declarations")
    text=must_replace(text,"records:[...topics,...grammarScaleA101,...grammarScaleA102,...grammarScaleA103]","records:[...topics,...grammarScaleA101,...grammarScaleA102,...grammarScaleA103,...grammarScaleA104]","publisher grammar")
    text=must_replace(text,"records:[...sentences,...grammarScaleA101Sentences,...grammarScaleA102Sentences,...grammarScaleA103Sentences,...reviewedTranslationSentences,...reviewedTypingTextSentences]","records:[...sentences,...grammarScaleA101Sentences,...grammarScaleA102Sentences,...grammarScaleA103Sentences,...grammarScaleA104Sentences,...reviewedTranslationSentences,...reviewedTypingTextSentences]","publisher examples")
    text=must_replace(text,"records:[...exercises,...grammarScaleA101Exercises,...grammarScaleA102Exercises,...grammarScaleA103Exercises,...reviewedE06Exercises,...reviewedTranslations,...reviewedCloze]","records:[...exercises,...grammarScaleA101Exercises,...grammarScaleA102Exercises,...grammarScaleA103Exercises,...grammarScaleA104Exercises,...reviewedE06Exercises,...reviewedTranslations,...reviewedCloze]","publisher exercises")
    text=must_replace(text,"records:[...reviewedCommonMistakes,...grammarScaleA101Mistakes,...grammarScaleA102Mistakes,...grammarScaleA103Mistakes]","records:[...reviewedCommonMistakes,...grammarScaleA101Mistakes,...grammarScaleA102Mistakes,...grammarScaleA103Mistakes,...grammarScaleA104Mistakes]","publisher mistakes")
    path.write_text(text,encoding="utf-8")


def patch_validator():
    path=ROOT/"scripts/validate-english-content.mjs"; text=path.read_text(encoding="utf-8")
    anchor='const grammarScaleA103Mistakes=await validateFile("content/english/sentences/e05-scale-a1-03-common-mistakes.json","common-mistake-set.schema.json");'
    text=must_replace(text,anchor,anchor+'\nconst grammarScaleA104=await validateFile("content/english/grammar/e05-scale-a1-04-topics.json","grammar-topic-set.schema.json");'+'\nconst grammarScaleA104Sentences=await validateFile("content/english/sentences/e05-scale-a1-04-sentences.json","sentence-set.schema.json");'+'\nconst grammarScaleA104Exercises=await validateFile("content/english/sentences/e05-scale-a1-04-exercises.json","exercise-set.schema.json");'+'\nconst grammarScaleA104Mistakes=await validateFile("content/english/sentences/e05-scale-a1-04-common-mistakes.json","common-mistake-set.schema.json");',"validator A1-04 declarations")
    marker="if (reviewedTranslationSentences&&reviewedTranslations) {"
    block=r'''if (grammarScaleA104&&grammarScaleA104Sentences&&grammarScaleA104Exercises&&grammarScaleA104Mistakes) {
  const expectedTopics=batchExpectedCount("e05.grammar-scale-a1-04","grammar-topics");
  const expectedExamples=batchExpectedCount("e05.grammar-scale-a1-04","examples");
  const expectedExercises=batchExpectedCount("e05.grammar-scale-a1-04","exercises");
  const expectedMistakes=batchExpectedCount("e05.grammar-scale-a1-04","common-mistakes");
  if (expectedTopics!==8||grammarScaleA104.records.length!==expectedTopics) errors.push("E05 A1 grammar scale 04 must contain 8 topics");
  if (expectedExamples!==24||grammarScaleA104Sentences.records.length!==expectedExamples) errors.push("E05 A1 grammar scale 04 must contain 24 examples");
  if (expectedExercises!==16||grammarScaleA104Exercises.records.length!==expectedExercises) errors.push("E05 A1 grammar scale 04 must contain 16 exercises");
  if (expectedMistakes!==8||grammarScaleA104Mistakes.records.length!==expectedMistakes) errors.push("E05 A1 grammar scale 04 must contain 8 common mistakes");
  const topicIds=new Set(grammarScaleA104.records.map(record=>record.id));
  const sentenceIds=new Set(grammarScaleA104Sentences.records.map(record=>record.id));
  const exerciseIds=new Set(grammarScaleA104Exercises.records.map(record=>record.id));
  const mistakeIds=new Set(grammarScaleA104Mistakes.records.map(record=>record.id));
  const existingTopicIds=new Set([...(grammarPilot?.records??[]),...(grammarScaleA101?.records??[]),...(grammarScaleA102?.records??[]),...(grammarScaleA103?.records??[])].map(record=>record.id));
  const normalizedSentenceText=new Set([...(sentencePilot?.records??[]),...(grammarScaleA101Sentences?.records??[]),...(grammarScaleA102Sentences?.records??[]),...(grammarScaleA103Sentences?.records??[])].map(record=>String(record.text??"").normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US")));
  const normalize=value=>String(value??"").normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US");
  const sentenceById=new Map(grammarScaleA104Sentences.records.map(record=>[record.id,record]));
  const exampleCounts=new Map(),exerciseCounts=new Map(),mistakeCounts=new Map();
  for (const topic of grammarScaleA104.records) {
    if (topic.quality?.state!=="draft") errors.push(topic.id+": E05 A1 scale topic must remain draft; publication is ledger-overlay only");
    if (topic.cefr!=="A1") errors.push(topic.id+": E05 A1 scale topic must be A1");
    if (!allIds.has(topic.id)) errors.push(topic.id+": E05 A1 scale topic is absent from the 300-topic catalog");
    if (existingTopicIds.has(topic.id)) errors.push(topic.id+": E05 A1 scale 04 topic duplicates an already-authored grammar body");
    if (!String(topic.concept?.en??"").trim()||!String(topic.concept?.vi??"").trim()) errors.push(topic.id+": bilingual concept is required");
    if ((topic.formulae??[]).length===0||(topic.whenToUse??[]).length===0) errors.push(topic.id+": formulae and whenToUse are required");
    if ((topic.exampleIds??[]).length!==3) errors.push(topic.id+": exactly 3 linked examples are required");
    if ((topic.exerciseIds??[]).length!==2) errors.push(topic.id+": exactly 2 linked exercises are required");
    if ((topic.commonMistakeIds??[]).length!==1) errors.push(topic.id+": exactly 1 linked common mistake is required");
    for (const id of topic.exampleIds??[]) if (!sentenceIds.has(id)) errors.push(topic.id+": missing A1 scale example "+id);
    for (const id of topic.exerciseIds??[]) if (!exerciseIds.has(id)) errors.push(topic.id+": missing A1 scale exercise "+id);
    for (const id of topic.commonMistakeIds??[]) if (!mistakeIds.has(id)) errors.push(topic.id+": missing A1 scale common mistake "+id);
    for (const id of [...(topic.prerequisiteIds??[]),...(topic.contrastTopicIds??[])]) if (!allIds.has(id)) errors.push(topic.id+": unknown grammar reference "+id);
  }
  for (const sentence of grammarScaleA104Sentences.records) {
    if (sentence.quality?.state!=="draft") errors.push(sentence.id+": E05 A1 scale example must remain draft");
    if (sentence.cefr!=="A1") errors.push(sentence.id+": E05 A1 scale example must be A1");
    if ((sentence.grammarIds??[]).length!==1||!topicIds.has(sentence.grammarIds[0])) errors.push(sentence.id+": example must target exactly one A1 scale topic");
    const key=normalize(sentence.text);
    if (normalizedSentenceText.has(key)) errors.push(sentence.id+": exact duplicate of an earlier grammar example");
    normalizedSentenceText.add(key);
    const grammarId=sentence.grammarIds?.[0];
    if (grammarId) exampleCounts.set(grammarId,(exampleCounts.get(grammarId)??0)+1);
  }
  let clozeCount=0,translationCount=0;
  for (const exercise of grammarScaleA104Exercises.records) {
    if (exercise.quality?.state!=="draft") errors.push(exercise.id+": E05 A1 scale exercise must remain draft");
    if (exercise.cefr!=="A1") errors.push(exercise.id+": E05 A1 scale exercise must be A1");
    if ((exercise.targetIds??[]).length!==1||!topicIds.has(exercise.targetIds[0])) errors.push(exercise.id+": exercise must target exactly one A1 scale topic");
    if ((exercise.sourceSentenceIds??[]).length!==1||!sentenceIds.has(exercise.sourceSentenceIds[0])) errors.push(exercise.id+": exercise must link exactly one A1 scale example");
    const source=sentenceById.get(exercise.sourceSentenceIds?.[0]);
    if (exercise.type==="cloze") {
      clozeCount++;
      if (!String(exercise.prompt??"").includes("___")) errors.push(exercise.id+": cloze prompt must contain ___");
      const answer=exercise.acceptedAnswers?.[0];
      const barePrompt=String(exercise.prompt??"").replace(/\s+\([^)]*\)\s*$/u,"");
      const restored=barePrompt.replace("___",String(answer??""));
      if (source&&normalize(restored)!==normalize(source.text)) errors.push(exercise.id+": cloze prompt + canonical answer must reconstruct its linked source sentence");
    } else if (exercise.type==="translation") {
      translationCount++;
      if (source&&normalize(exercise.acceptedAnswers?.[0])!==normalize(source.text)) errors.push(exercise.id+": translation canonical answer must equal its linked source sentence");
    } else errors.push(exercise.id+": A1 scale supports cloze/translation only");
    const grammarId=exercise.targetIds?.[0];
    if (grammarId) exerciseCounts.set(grammarId,(exerciseCounts.get(grammarId)??0)+1);
  }
  for (const mistake of grammarScaleA104Mistakes.records) {
    if (mistake.quality?.state!=="draft") errors.push(mistake.id+": E05 A1 scale common mistake must remain draft");
    if ((mistake.targetIds??[]).length!==1||!topicIds.has(mistake.targetIds[0])) errors.push(mistake.id+": common mistake must target exactly one A1 scale topic");
    if (mistake.evidenceType!=="pedagogical") errors.push(mistake.id+": common mistake must use pedagogical evidence");
    if ((mistake.corrections??[]).length!==1||!String(mistake.explanationVi??"").trim()) errors.push(mistake.id+": exactly one canonical correction and a Vietnamese explanation are required");
    const grammarId=mistake.targetIds?.[0];
    if (grammarId) mistakeCounts.set(grammarId,(mistakeCounts.get(grammarId)??0)+1);
  }
  if (clozeCount!==8||translationCount!==8) errors.push("E05 A1 scale 04 must contain 8 cloze + 8 translation exercises");
  for (const id of topicIds) {
    if ((exampleCounts.get(id)??0)!==3) errors.push(id+": E05 A1 scale requires 3 examples");
    if ((exerciseCounts.get(id)??0)!==2) errors.push(id+": E05 A1 scale requires 2 exercises");
    if ((mistakeCounts.get(id)??0)!==1) errors.push(id+": E05 A1 scale requires 1 common mistake");
  }
}

'''
    text=must_replace(text,marker,block+marker,"validator A1-04 block")
    path.write_text(text,encoding="utf-8")


def patch_smoke():
    path=ROOT/"scripts/smoke-published-english-content.mjs"; text=path.read_text(encoding="utf-8")
    replacements=[
        ("grammarManifest.count!==36","grammarManifest.count!==44"),
        ("published grammar runtime must contain 36 reviewed grammar topics","published grammar runtime must contain 44 reviewed grammar topics"),
        ("sentenceManifest.count!==1804","sentenceManifest.count!==1852"),
        ("published sentence runtime must contain 1804 reviewed records","published sentence runtime must contain 1852 reviewed records"),
        ("topics.length!==36||examples.length!==708||exercises.length!==872||dialogues.length!==100||commonMistakes.length!==124","topics.length!==44||examples.length!==732||exercises.length!==888||dialogues.length!==100||commonMistakes.length!==132"),
        ("published runtime split must be 36 topics + 708 examples + 872 exercises + 100 dialogues + 124 common mistakes","published runtime split must be 44 topics + 732 examples + 888 exercises + 100 dialogues + 132 common mistakes"),
        ("monkeyCorrectionCount!==224","monkeyCorrectionCount!==232"),
        ("published Monkeytype error-correction activity must expose 100 corrections + 124 common mistakes","published Monkeytype error-correction activity must expose 100 corrections + 132 common mistakes"),
        ("monkeyCorrectionRecords:224","monkeyCorrectionRecords:232"),
    ]
    for old,new in replacements: text=must_replace(text,old,new,"runtime smoke counts")
    path.write_text(text,encoding="utf-8")


def patch_e11_report():
    path=ROOT/"scripts/report-english-content-e11-readiness.mjs"; text=path.read_text(encoding="utf-8")
    text=must_replace(text,'const pendingGrammarReview=[await buildGrammarReviewPacket("a1-04")];','const pendingGrammarReview=[];',"E11 pending A1-04 packet")
    path.write_text(text,encoding="utf-8")


def patch_release_and_docs():
    release=load_json("content/english/releases/2026.10.0.json")
    release["runtimeCounts"]["grammar"]=44; release["runtimeCounts"]["sentences"]=1852; release["batchStates"]["draft"]=44
    write_json("content/english/releases/2026.10.0.json",release)
    path=ROOT/"docs/ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md"; text=path.read_text(encoding="utf-8")
    replacements=[
        ("Pilot status: **THIRD CONTROLLED A1 BODY SLICE PUBLISHED LOCALLY; CONTINUING REVIEWED SCALE-UP**.","Pilot status: **FOURTH CONTROLLED A1 BODY SLICE PUBLISHED LOCALLY; CONTINUING REVIEWED SCALE-UP**."),
        ("- The E05 grammar-body review ledger now overlays **240 digest-bound accepted records** and promotes only those reviewed records at publication time.","- The E05 grammar-body review ledger now overlays **296 digest-bound accepted records** and promotes only those reviewed records at publication time."),
        ("- Published E05 runtime now contains **36 rich grammar topics**: the original 12-topic cross-CEFR pilot plus three controlled A1 body slices with 24 additional topics. Grammar-linked authoring now includes **108 controlled example sentences, 72 exercises and 24 linked common mistakes**.","- Published E05 runtime now contains **44 rich grammar topics**: the original 12-topic cross-CEFR pilot plus four controlled A1 body slices with 32 additional topics. Grammar-linked authoring now includes **132 controlled example sentences, 88 exercises and 32 linked common mistakes**."),
        ("A1 slice 03 adds Present Simple negatives/questions/wh-questions, frequency adverbs, can for ability, can for permission/requests, imperatives and object pronouns. Every scale topic","A1 slice 03 adds Present Simple negatives/questions/wh-questions, frequency adverbs, can for ability, can for permission/requests, imperatives and object pronouns. A1 slice 04 adds likes/dislikes with nouns and -ing forms, want/need + to-infinitive, time/place/movement prepositions, adjective position, very/really and basic coordinators. Every scale topic"),
        ("- The original 72 publication decisions remain intact. The three A1 scale slices add **168 digest-bound publication decisions** (24 topics + 72 examples + 48 exercises + 24 mistakes) with grammar, bilingual/naturalness, target, CEFR, dedup and license/provenance checks completed.","- The original 72 publication decisions remain intact. The four A1 scale slices add **224 digest-bound publication decisions** (32 topics + 96 examples + 64 exercises + 32 mistakes) with grammar, bilingual/naturalness, target, CEFR, dedup and license/provenance checks completed."),
        ("- The full 300-topic framework remains the curriculum/taxonomy; **36/300 topics now have reviewed rich runtime bodies**.","- The full 300-topic framework remains the curriculum/taxonomy; **44/300 topics now have reviewed rich runtime bodies**."),
        ("Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **36 topics**; `shared/sentences` contains **1,804 records** = **708 examples + 872 exercises + 100 dialogues + 124 reviewed common mistakes**;","Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **44 topics**; `shared/sentences` contains **1,852 records** = **732 examples + 888 exercises + 100 dialogues + 132 reviewed common mistakes**;"),
        ("The current controlled E03-E06 manifest plus the first two E05 A1 scale slices accounts for **6,398 authoring/candidate records: 3,200 candidate + 3,198 draft**.","The active controlled manifest now accounts for **4,128 checked-in draft authoring/source records across 37 batches**; superseded transient candidate batches are intentionally retired from the active manifest."),
        ("- grammar topics: **300/300 framework entries**, with **28/300 reviewed rich topic bodies** currently published;","- grammar topics: **300/300 framework entries**, with **44/300 reviewed rich topic bodies** currently published;"),
        ("- common mistakes: **116 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 16 reviewed A1 grammar-scale mistakes;","- common mistakes: **132 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 32 reviewed A1 grammar-scale mistakes;"),
        ("- example sentences: candidate/source pipeline remains far below 100,000; current published runtime contains **684 examples** (84 E05 grammar-linked + 300 typing-text + 300 Tatoeba);","- example sentences: candidate/source pipeline remains far below 100,000; current published runtime contains **732 examples** (132 E05 grammar-linked + 300 typing-text + 300 Tatoeba);"),
        ("- continue grammar-body promotion in small reviewed CEFR slices; the first two A1 scale slices add 16 rich topics and 96 linked sentence-domain records, while E03, E04, E05 and E06 publication still uses digest-bound `draft → published` overlays;","- continue grammar-body promotion in small reviewed CEFR slices; the first four A1 scale slices add 32 rich topics and 192 linked sentence-domain records, while E03, E04, E05 and E06 publication still uses digest-bound `draft → published` overlays;"),
    ]
    for old,new in replacements: text=must_replace(text,old,new,"master plan checkpoint")
    path.write_text(text,encoding="utf-8")


def main():
    reviewed=load_and_lock_reviewed_sources(); add_batch_manifest(); write_review_ledger(reviewed); patch_publisher(); patch_validator(); patch_smoke(); patch_e11_report(); patch_release_and_docs()


if __name__=="__main__": main()
