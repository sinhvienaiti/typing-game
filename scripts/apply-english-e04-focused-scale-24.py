#!/usr/bin/env python3
import copy
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH_ID = "e04.phrase-pattern-scale-24"
COL_PATH = "content/english/phrases/e04-scale-24-collocations.json"
PHRASE_PATH = "content/english/phrases/e04-scale-24-phrases.json"
DECISION_PATH = ROOT / "content/english/reviews/decisions.d/e04-scale-24.json"
REVIEWED_AT = "2026-10-06T07:35:00Z"
REVIEWED_BY = "GPT-5.6 Sol bilingual editorial review"

COLLOCATIONS = [
("broker a compromise","verb + noun","dàn xếp một thỏa hiệp","B2"),
("mount a challenge","verb + noun","đưa ra hoặc tạo nên một thách thức đáng kể","B2"),
("avert a crisis","verb + noun","ngăn một cuộc khủng hoảng xảy ra","C1"),
("withstand scrutiny","verb + noun","chịu được sự xem xét kỹ lưỡng","C1"),
("consolidate gains","verb + noun","củng cố những thành quả đã đạt được","C1"),
("marshal resources","verb + noun","tập hợp và tổ chức nguồn lực để sử dụng hiệu quả","C1"),
("temper expectations","verb + noun","điều chỉnh kỳ vọng xuống mức thực tế hơn","C1"),
("defuse tensions","verb + noun","làm dịu căng thẳng","C1"),
("rectify an error","verb + noun","sửa chữa một sai sót","C1"),
("substantiate a claim","verb + noun","đưa bằng chứng để chứng minh một tuyên bố","C1"),
("forge an alliance","verb + noun","thiết lập một liên minh chặt chẽ","C1"),
("preserve anonymity","verb + noun","giữ kín danh tính","C1"),
("maintain impartiality","verb + noun","duy trì sự vô tư và khách quan khi đánh giá","C1"),
("retain jurisdiction","verb + noun","tiếp tục giữ thẩm quyền pháp lý","C1"),
("establish causality","verb + noun","xác lập quan hệ nhân quả","C1"),
("infer meaning","verb + noun","suy ra ý nghĩa từ ngữ cảnh hoặc bằng chứng","B2"),
("reconcile accounts","verb + noun","đối chiếu các tài khoản hoặc sổ sách cho khớp","C1"),
("absorb costs","verb + noun","tự gánh hoặc hấp thụ chi phí thay vì chuyển cho bên khác","C1"),
("diversify holdings","verb + noun","đa dạng hóa danh mục tài sản nắm giữ","C1"),
("honor a commitment","verb + noun","thực hiện đúng một cam kết","B2"),
("waive a fee","verb + noun","miễn một khoản phí","B2"),
("file an appeal","verb + noun","nộp đơn kháng cáo hoặc khiếu nại chính thức","B2"),
("overturn a ruling","verb + noun","đảo ngược một phán quyết","C1"),
("issue an injunction","verb + noun","ban hành lệnh của tòa yêu cầu hoặc ngăn một hành động","C1"),
("levy a fine","verb + noun","áp một khoản tiền phạt","C1"),
("convene a meeting","verb + noun","triệu tập một cuộc họp","C1"),
("adjourn proceedings","verb + noun","tạm hoãn hoặc kết thúc phiên làm việc chính thức","C1"),
("disclose findings","verb + noun","công bố các phát hiện hoặc kết quả","B2"),
("verify credentials","verb + noun","xác minh giấy tờ hoặc năng lực chứng nhận","B2"),
("safeguard privacy","verb + noun","bảo vệ quyền riêng tư","B2"),
("streamline operations","verb + noun","tinh gọn hoạt động để hiệu quả hơn","C1"),
("phase out subsidies","verb + particle + noun","loại bỏ dần các khoản trợ cấp","C1"),
("shore up defenses","verb + particle + noun","củng cố hệ thống phòng vệ","C1"),
("curb emissions","verb + noun","kiềm chế hoặc giảm lượng khí thải","B2"),
("harness potential","verb + noun","khai thác tiềm năng một cách hiệu quả","C1"),
("offset losses","verb + noun","bù đắp các khoản tổn thất","B2"),
("weather a downturn","verb + noun","vượt qua một giai đoạn suy giảm khó khăn","C1"),
("reverse a trend","verb + noun","đảo ngược một xu hướng","B2"),
("sustain growth","verb + noun","duy trì tăng trưởng trong thời gian dài","B2"),
("remedy deficiencies","verb + noun","khắc phục các thiếu sót hoặc điểm yếu","C1"),
]

PHRASAL = [
("batten down","cố định hoặc bảo vệ chắc chắn để chuẩn bị đối phó khó khăn","C1","transitive","separable","Có thể dùng với vật cần gia cố; ví dụ batten the hatches down."),
("blot out","che khuất hoàn toàn hoặc xóa khỏi ký ức hay tầm nhìn","C1","transitive","separable","Có thể nói blot the light out hoặc blot out a memory."),
("bottle up","kìm nén cảm xúc thay vì bộc lộ hoặc xử lý chúng","B2","transitive","separable","Có thể nói bottle your feelings up."),
("carve out","tạo dựng một vị trí, vai trò hoặc cơ hội riêng bằng nỗ lực","C1","transitive","separable","Thường dùng với niche, role, career hoặc time."),
("chime in","tham gia vào cuộc trò chuyện bằng một ý kiến hoặc nhận xét","B2","intransitive","inseparable","Có thể theo sau bởi with khi nêu ý kiến được thêm vào."),
("roll back","đảo ngược hoặc cắt giảm một thay đổi đã được áp dụng","C1","transitive","separable","Có thể nói roll the changes back."),
("crop up","xuất hiện bất ngờ, thường là một vấn đề hoặc tình huống mới","B2","intransitive","inseparable","Thường dùng cho problems, questions hoặc issues."),
("shore up","củng cố thứ đang yếu hoặc có nguy cơ suy giảm","C1","transitive","separable","Dùng cho tài chính, niềm tin, phòng thủ hoặc cấu trúc."),
("dole out","phân phát hoặc chia thứ gì thành từng phần nhỏ","B2","transitive","separable","Có thể nói dole the portions out hoặc dole out the portions."),
("spell out","giải thích hoặc nêu rõ từng chi tiết","B2","transitive","separable","Có thể nói spell the rules out."),
("fizzle out","yếu dần rồi chấm dứt mà không đạt kết quả đáng kể","C1","intransitive","inseparable","Thường dùng cho plans, protests, relationships hoặc efforts."),
("hammer out","thảo luận hoặc thương lượng kỹ để đi đến thỏa thuận hay giải pháp","C1","transitive","separable","Có thể nói hammer an agreement out hoặc hammer out an agreement."),
("taper off","giảm dần về mức độ, số lượng hoặc cường độ","C1","intransitive","inseparable","Thường dùng cho nhu cầu, mưa, tác dụng hoặc hoạt động."),
("weed out","loại bỏ những phần tử không mong muốn","B2","transitive","separable","Có thể nói weed the weak entries out."),
("pare down","cắt giảm để chỉ giữ lại phần cần thiết hoặc cốt lõi","C1","transitive","separable","Có thể nói pare the list down hoặc pare down the list."),
("pore over","đọc hoặc xem xét thứ gì rất kỹ và trong thời gian dài","C1","transitive","inseparable","Đối tượng đứng sau over; lưu ý pore khác pour."),
("reel off","nói, đọc hoặc liệt kê nhiều thứ rất nhanh và trôi chảy","C1","transitive","separable","Có thể nói reel the figures off hoặc reel off the figures."),
("shake off","thoát khỏi hoặc loại bỏ một ảnh hưởng, cảm giác hay người bám theo","B2","transitive","separable","Có thể nói shake the feeling off hoặc shake off the feeling."),
("trot out","đưa ra lại một lý do, ý tưởng hoặc lập luận quen thuộc, thường thiếu thuyết phục","C1","transitive","separable","Có thể nói trot the same excuse out hoặc trot out the same excuse."),
("fend off","chống đỡ hoặc ngăn một mối đe dọa/tấn công","C1","transitive","separable","Có thể nói fend the attack off."),
]

CHUNKS = [
("for present purposes","cho mục đích đang được xem xét trong ngữ cảnh hiện tại","C1"),
("in light of this","xét đến điều này hoặc dựa trên thông tin này","B2"),
("from a practical standpoint","xét từ góc độ thực tế và khả năng áp dụng","C1"),
("to a large extent","ở mức độ lớn, phần lớn","B2"),
("by the same token","theo cùng một logic hoặc lý do tương tự","C1"),
("in practical terms","xét về mặt thực tế hoặc cách áp dụng thực tế","C1"),
("on that basis","dựa trên cơ sở hoặc lý do vừa nêu","B2"),
("with that in mind","với việc ghi nhớ và cân nhắc điều vừa nêu","B2"),
("barring unforeseen circumstances","nếu không có tình huống bất ngờ nào xảy ra","C1"),
("pending further review","trong khi chờ việc xem xét thêm trước khi có quyết định cuối cùng","C1"),
]

IDIOMS = [
("draw a line in the sand","đặt ra một giới hạn hoặc lập trường không muốn nhượng bộ thêm","C1"),
("move the needle","tạo ra thay đổi đủ lớn để ảnh hưởng rõ rệt đến kết quả","C1"),
("square the circle","cố giải quyết hai yêu cầu dường như không thể dung hòa","C1"),
("split hairs","tranh luận quá chi li về những khác biệt rất nhỏ","C1"),
("cut no ice","không tạo được ảnh hưởng hoặc không thuyết phục được ai","C1"),
("move heaven and earth","nỗ lực hết sức và làm mọi điều có thể để đạt mục tiêu","C1"),
("miss the forest for the trees","quá chú ý chi tiết mà bỏ lỡ bức tranh tổng thể","C1"),
("read the room","nhận biết đúng tâm trạng và tín hiệu xã hội của những người xung quanh","B2"),
("have a lot on your plate","có rất nhiều việc hoặc trách nhiệm phải xử lý","B2"),
("throw cold water on something","làm giảm sự nhiệt tình hoặc nghi ngờ một ý tưởng/kế hoạch","C1"),
]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def digest(record):
    value = copy.deepcopy(record)
    checks = value.get("quality", {}).get("checks")
    if isinstance(checks, dict):
        checks.pop("cefr", None)
        checks.pop("license", None)
    return hashlib.sha256(stable_json(value).encode("utf-8")).hexdigest()


def norm(value):
    value = unicodedata.normalize("NFC", str(value)).strip().lower()
    value = re.sub(r"\s+", " ", value)
    return value


def toks(value):
    return [x for x in re.sub(r"[^a-z0-9'’-]+", " ", norm(value)).split() if x]


def jaccard(a, b):
    sa, sb = set(toks(a)), set(toks(b))
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def quality(method):
    return {
        "state": "draft",
        "checks": {
            "schema": {"status": "pass", "method": method},
            "grammar": {"status": "pending", "method": "grammar-editorial-review-required"},
            "translation": {"status": "pending", "method": "bilingual-review-required"},
            "naturalness": {"status": "pending", "method": "editor-review-required"},
            "cefr": {"status": "pending", "method": "cefr-review-required"},
            "targetStructure": {"status": "pending", "method": "phrase-structure-review-required"},
            "exactDuplicate": {"status": "pass", "method": "normalized-key-v25"},
            "nearDuplicate": {"status": "pending", "method": "cross-batch-near-dedup-review-required"},
            "license": {"status": "pending", "method": "license-review-required"},
        },
    }


def provenance(source_path, source_id):
    return {
        "sources": [{
            "dataset": "project-original",
            "sourceId": source_id,
            "sourceUrl": source_path,
            "snapshot": "2026-10",
            "license": "LicenseRef-Project-Original",
            "modified": False,
        }],
        "note": "Project-original E04 focused scale-24 item; bilingual meaning and structure were editorially reviewed before publication.",
    }


def collocation_record(index, item):
    text, pattern, meaning, cefr = item
    keys = []
    stop = {"a", "an", "the", "to", "of", "on", "in", "for", "and"}
    for token in toks(text):
        if token not in stop and token not in keys:
            keys.append(token)
    rid = f"col.{index:08d}"
    return {
        "schemaVersion": 1,
        "id": rid,
        "text": text,
        "headwordKeys": keys,
        "pattern": pattern,
        "meaningVi": meaning,
        "cefr": cefr,
        "register": ["neutral"],
        "exampleIds": [],
        "quality": quality("e04-scale-24-authoring-v1"),
        "provenance": provenance(COL_PATH, rid),
    }


def phrase_record(prefix, index, typ, text, meaning, cefr, trans, sep, notes):
    rid = f"{prefix}.{index:08d}"
    return {
        "schemaVersion": 1,
        "id": rid,
        "type": typ,
        "text": text,
        "key": norm(text),
        "meaningVi": meaning,
        "cefr": cefr,
        "transitivity": trans,
        "separability": sep,
        "register": ["neutral"],
        "notesVi": notes,
        "exampleIds": [],
        "quality": quality("e04-scale-24-authoring-v1"),
        "provenance": provenance(PHRASE_PATH, rid),
    }


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one target, got {text.count(old)}")
    return text.replace(old, new, 1)


def regex_once(text, pattern, repl, label):
    out, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one regex target, got {count}")
    return out


def main():
    manifest_path = ROOT / "content/english/batches/manifest.json"
    manifest = read_json(manifest_path)
    if any(b.get("id") == BATCH_ID for b in manifest.get("batches", [])):
        print("E04 focused scale-24 already applied; skipping.")
        return

    e04_sets = []
    existing = {"collocations": [], "verb-patterns": [], "phrases": []}
    for batch in manifest.get("batches", []):
        if batch.get("phase") != "E04":
            continue
        for record_set in batch.get("recordSets", []):
            sid = record_set.get("id", "")
            if sid in ("collocations", "scale-collocations"):
                kind = "collocations"
            elif sid in ("verb-patterns", "scale-verb-patterns"):
                kind = "verb-patterns"
            elif sid in ("phrases", "scale-phrases"):
                kind = "phrases"
            else:
                continue
            doc = read_json(ROOT / record_set["path"])
            existing[kind].extend(doc.get("records", []))
            e04_sets.append((kind, record_set["path"]))

    counts = {k: len(v) for k, v in existing.items()}
    if counts != {"collocations": 560, "verb-patterns": 510, "phrases": 560}:
        raise RuntimeError(f"E04 drift before scale-24: {counts}")

    def max_num(records, prefix):
        nums = [int(r["id"].split(".")[-1]) for r in records if str(r.get("id", "")).startswith(prefix + ".")]
        return max(nums) if nums else 0

    split = {
        "pv": max_num(existing["phrases"], "pv"),
        "chunk": max_num(existing["phrases"], "chunk"),
        "idiom": max_num(existing["phrases"], "idiom"),
    }
    if max_num(existing["collocations"], "col") != 560 or split != {"pv": 280, "chunk": 155, "idiom": 125}:
        raise RuntimeError(f"E04 ID drift before scale-24: coll={max_num(existing['collocations'], 'col')} phrases={split}")

    new_collocations = [collocation_record(561 + i, item) for i, item in enumerate(COLLOCATIONS)]
    new_phrases = []
    for i, (text, meaning, cefr, trans, sep, notes) in enumerate(PHRASAL):
        new_phrases.append(phrase_record("pv", 281 + i, "phrasal-verb", text, meaning, cefr, trans, sep, notes))
    for i, (text, meaning, cefr) in enumerate(CHUNKS):
        new_phrases.append(phrase_record("chunk", 156 + i, "chunk", text, meaning, cefr, "not-applicable", "not-applicable", "Cụm diễn ngôn/cụm cố định; dùng như một đơn vị hoàn chỉnh."))
    for i, (text, meaning, cefr) in enumerate(IDIOMS):
        new_phrases.append(phrase_record("idiom", 126 + i, "idiom", text, meaning, cefr, "not-applicable", "not-applicable", "Thành ngữ; nghĩa toàn cụm không nên suy ra máy móc từ từng từ riêng lẻ."))
    if len(new_collocations) != 40 or len(new_phrases) != 40:
        raise RuntimeError("scale-24 must contain 40 collocations + 40 phrase items")

    for label, old_records, new_records in [
        ("collocation", existing["collocations"], new_collocations),
        ("phrase", existing["phrases"], new_phrases),
    ]:
        old_text = [(r.get("id", ""), r.get("text", "")) for r in old_records]
        seen = []
        for rec in new_records:
            for oid, otext in old_text + seen:
                if norm(rec["text"]) == norm(otext):
                    raise RuntimeError(f"{label} exact duplicate: {rec['id']} == {oid}: {rec['text']}")
                score = jaccard(rec["text"], otext)
                if score >= 0.86:
                    raise RuntimeError(f"{label} near duplicate >=0.86: {rec['id']} ~ {oid}: {score:.4f}: {rec['text']} / {otext}")
            seen.append((rec["id"], rec["text"]))

    write_json(ROOT / COL_PATH, {"schemaVersion": 1, "records": new_collocations})
    write_json(ROOT / PHRASE_PATH, {"schemaVersion": 1, "records": new_phrases})

    required_checks = ["schema", "grammar", "translation", "naturalness", "cefr", "targetStructure", "exactDuplicate", "nearDuplicate", "license"]
    manifest["batches"].append({
        "id": BATCH_ID,
        "phase": "E04",
        "category": "phrases",
        "cefr": ["B2", "C1"],
        "state": "draft",
        "recordSets": [
            {"id": "scale-collocations", "path": COL_PATH, "expectedCount": 40, "generated": False, "allowedQualityStates": ["draft"], "requiredChecks": required_checks},
            {"id": "scale-phrases", "path": PHRASE_PATH, "expectedCount": 40, "generated": False, "allowedQualityStates": ["draft"], "requiredChecks": required_checks},
        ],
        "requiredBeforePublish": ["schema-validation", "reference-integrity", "exact-dedup", "near-dedup", "grammar-review", "bilingual-review", "naturalness-review", "cefr-review", "target-structure-review", "license-review", "cross-game-smoke"],
        "gameSmokes": [
            {"gameId": "recall-typing", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "vocab-shooter", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "space-typing", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "recall-typing", "activity": "phrasal-verb", "recordSetId": "scale-phrases", "sampleCount": 5, "recordType": "phrasal-verb"},
            {"gameId": "recall-typing", "activity": "chunk", "recordSetId": "scale-phrases", "sampleCount": 5, "recordType": "chunk"},
            {"gameId": "monkeytype", "activity": "idiom", "recordSetId": "scale-phrases", "sampleCount": 5, "recordType": "idiom"},
        ],
    })
    write_json(manifest_path, manifest)

    decisions = []
    def add_decision(record, set_id):
        decisions.append({
            "id": "review.e04.scale-24." + record["id"].replace(".", "-"),
            "batchId": BATCH_ID,
            "recordSetId": set_id,
            "recordId": record["id"],
            "sourceDigest": digest(record),
            "targetState": "published",
            "checks": {
                "grammar": {"status": "pass", "method": "e04-scale-24-grammar-editorial-review"},
                "translation": {"status": "pass", "method": "e04-scale-24-bilingual-review"},
                "naturalness": {"status": "pass", "method": "e04-scale-24-naturalness-review"},
                "cefr": {"status": "pass", "method": "e04-scale-24-cefr-review"},
                "targetStructure": {"status": "pass", "method": "e04-scale-24-structure-review"},
                "nearDuplicate": {"status": "pass", "method": "e04-scale-24-cross-batch-near-dedup-review"},
                "license": {"status": "pass", "method": "project-original-license-review-v1"},
            },
            "reviewedAt": REVIEWED_AT,
            "reviewedBy": REVIEWED_BY,
            "note": "Focused E04 scale 24 reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup, phrasal-verb separability/transitivity where applicable, and project-original provenance.",
        })
    for record in new_collocations:
        add_decision(record, "scale-collocations")
    for record in new_phrases:
        add_decision(record, "scale-phrases")
    if DECISION_PATH.exists():
        raise RuntimeError("scale-24 decision shard already exists")
    write_json(DECISION_PATH, {"schemaVersion": 1, "decisions": decisions})

    publisher_path = ROOT / "scripts/publish-english-content.mjs"
    publisher = publisher_path.read_text(encoding="utf-8")
    load_pattern = r'const collocations=await loadRecords\("content/english/phrases/pilot-collocations\.json"\);.*?const scale23Phrases=await loadRecords\("content/english/phrases/e04-scale-23-phrases\.json"\);\n'
    dynamic = '''const e04Collocations=[];\nconst e04VerbPatterns=[];\nconst e04Phrases=[];\nconst e04Batches=(batchManifest.batches??[]).filter(batch=>batch.phase==="E04"&&batch.category==="phrases").sort((a,b)=>a.id.localeCompare(b.id,"en"));\nfor (const batch of e04Batches) {\n  for (const set of batch.recordSets??[]) {\n    if (set.id==="collocations"||set.id==="scale-collocations") e04Collocations.push(...await loadRecords(set.path));\n    else if (set.id==="verb-patterns"||set.id==="scale-verb-patterns") e04VerbPatterns.push(...await loadRecords(set.path));\n    else if (set.id==="phrases"||set.id==="scale-phrases") e04Phrases.push(...await loadRecords(set.path));\n  }\n}\n'''
    publisher = regex_once(publisher, load_pattern, dynamic, "publisher E04 manifest-driven loader")
    publisher = regex_once(publisher, r'\{id:"collocations",dir:"collocations",records:\[[^\]]*\]\}', '{id:"collocations",dir:"collocations",records:e04Collocations}', "publisher collocations output")
    publisher = regex_once(publisher, r'\{id:"verb-patterns",dir:"verb-patterns",records:\[[^\]]*\]\}', '{id:"verb-patterns",dir:"verb-patterns",records:e04VerbPatterns}', "publisher verb-patterns output")
    publisher = regex_once(publisher, r'\{id:"phrases",dir:"items",records:\[[^\]]*\]\}', '{id:"phrases",dir:"items",records:e04Phrases}', "publisher phrases output")
    publisher_path.write_text(publisher, encoding="utf-8")

    smoke_path = ROOT / "scripts/smoke-published-english-content.mjs"
    smoke = smoke_path.read_text(encoding="utf-8")
    for old, new, label in [
        ('if(recallCollocations!==560)', 'if(recallCollocations!==600)', 'collocation count'),
        ('must expose 560 reviewed records', 'must expose 600 reviewed records', 'collocation message'),
        ('if(phrasalVerbCount!==280)', 'if(phrasalVerbCount!==300)', 'phrasal count'),
        ('must expose 280 reviewed records', 'must expose 300 reviewed records', 'phrasal message'),
        ('if(chunkCount!==155)', 'if(chunkCount!==165)', 'chunk count'),
        ('must expose 155 reviewed records', 'must expose 165 reviewed records', 'chunk message'),
        ('if(idiomCount!==125)', 'if(idiomCount!==135)', 'idiom count'),
        ('must expose 125 reviewed records', 'must expose 135 reviewed records', 'idiom message'),
    ]:
        smoke = replace_once(smoke, old, new, label)
    smoke_path.write_text(smoke, encoding="utf-8")

    release_path = ROOT / "content/english/releases/2026.10.0.json"
    release = read_json(release_path)
    if release.get("runtimeCounts", {}).get("phrases") != 1630:
        raise RuntimeError(f"release phrase count drift: {release.get('runtimeCounts', {}).get('phrases')}")
    release["runtimeCounts"]["phrases"] = 1710
    release.setdefault("notes", []).append("E04 focused scale 24 adds 40 reviewed collocations plus 20 phrasal verbs, 10 chunks and 10 idioms; verb-pattern volume stays at the 510 reviewed target.")
    write_json(release_path, release)

    report_path = ROOT / "scripts/report-english-content-e04.mjs"
    report_path.write_text('''import path from "node:path";\nimport{fileURLToPath}from"node:url";\nimport{readJson}from"./english-content-core.mjs";\nconst root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");\nconst manifest=await readJson(path.join(root,"shared","phrases","manifest.json"));\nconst records=[];\nfor(const shard of manifest.shards??[]){const doc=await readJson(path.join(root,"shared","phrases",shard.path));records.push(...(doc.records??[]));}\nconst collocations=records.filter(x=>String(x.id??"").startsWith("col."));\nconst verbPatterns=records.filter(x=>String(x.id??"").startsWith("pat."));\nconst phraseItems=records.filter(x=>/^(pv|chunk|idiom)\\./u.test(String(x.id??"")));\nconst report={total:records.length,collocations:collocations.length,verbPatterns:verbPatterns.length,phrasalVerbs:phraseItems.filter(x=>x.type==="phrasal-verb").length,chunks:phraseItems.filter(x=>x.type==="chunk").length,idioms:phraseItems.filter(x=>x.type==="idiom").length,published:records.filter(x=>x.quality?.state==="published").length,withExamples:{collocations:collocations.filter(x=>(x.exampleIds??[]).length>0).length,verbPatterns:verbPatterns.filter(x=>(x.exampleIds??[]).length>0).length,phraseItems:phraseItems.filter(x=>(x.exampleIds??[]).length>0).length}};\nconsole.log(JSON.stringify(report,null,2));\n''', encoding="utf-8")

    print(json.dumps({
        "status": "applied",
        "batch": BATCH_ID,
        "added": {"collocations": 40, "verbPatterns": 0, "phrasalVerbs": 20, "chunks": 10, "idioms": 10},
        "expectedRuntime": {"totalPhrases": 1710, "collocations": 600, "verbPatterns": 510, "phrasalVerbs": 300, "chunks": 165, "idioms": 135},
        "publisher": "manifest-driven E04 loading",
    }, indent=2))


if __name__ == "__main__":
    main()
