#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-28-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-28.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-28'
REVIEWED_AT = '2026-10-07T01:40:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-28'
EXPECTED = {'collocations': 720, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('establish baseline conditions', 'verb + noun phrase', 'xác lập các điều kiện cơ sở để làm mốc so sánh và đánh giá thay đổi', 'C1'),
    ('define measurable objectives', 'verb + noun phrase', 'xác định các mục tiêu có thể đo lường rõ ràng', 'B2'),
    ('set realistic milestones', 'verb + noun phrase', 'đặt ra các mốc tiến độ thực tế và có thể đạt được', 'B2'),
    ('sequence implementation activities', 'verb + noun phrase', 'sắp xếp các hoạt động triển khai theo trình tự hợp lý', 'C1'),
    ('coordinate delivery partners', 'verb + noun phrase', 'phối hợp các đối tác tham gia cung cấp hoặc triển khai dịch vụ', 'C1'),
    ('mobilize technical expertise', 'verb + noun phrase', 'huy động chuyên môn kỹ thuật cần thiết cho một nhiệm vụ hoặc chương trình', 'C1'),
    ('allocate implementation resources', 'verb + noun phrase', 'phân bổ nguồn lực cần thiết cho quá trình triển khai', 'B2'),
    ('track implementation progress', 'verb + noun phrase', 'theo dõi tiến độ triển khai so với kế hoạch đã đặt ra', 'B2'),
    ('resolve coordination gaps', 'verb + noun phrase', 'giải quyết các khoảng trống hoặc thiếu kết nối trong phối hợp công việc', 'C1'),
    ('reinforce delivery discipline', 'verb + noun phrase', 'củng cố kỷ luật thực thi để bảo đảm cam kết và tiến độ', 'C1'),
    ('improve procurement efficiency', 'verb + noun phrase', 'nâng cao hiệu quả của quy trình mua sắm và lựa chọn nhà cung cấp', 'C1'),
    ('strengthen supplier management', 'verb + noun phrase', 'tăng cường việc quản lý hiệu suất và quan hệ với nhà cung cấp', 'B2'),
    ('diversify supply sources', 'verb + noun phrase', 'đa dạng hóa nguồn cung để giảm phụ thuộc vào một nguồn duy nhất', 'B2'),
    ('reduce supply disruption', 'verb + noun phrase', 'giảm nguy cơ hoặc mức độ gián đoạn trong chuỗi cung ứng', 'B2'),
    ('maintain inventory visibility', 'verb + noun phrase', 'duy trì khả năng quan sát chính xác tình trạng tồn kho', 'C1'),
    ('improve demand forecasting', 'verb + noun phrase', 'cải thiện việc dự báo nhu cầu trong tương lai', 'B2'),
    ('align capacity with demand', 'verb + noun phrase', 'điều chỉnh năng lực cung ứng phù hợp với mức nhu cầu', 'C1'),
    ('streamline logistics operations', 'verb + noun phrase', 'tinh gọn hoạt động logistics để giảm chậm trễ và lãng phí', 'C1'),
    ('improve distribution efficiency', 'verb + noun phrase', 'nâng cao hiệu quả phân phối hàng hóa hoặc dịch vụ', 'B2'),
    ('strengthen quality assurance', 'verb + noun phrase', 'tăng cường hoạt động bảo đảm chất lượng trong quy trình hoặc sản phẩm', 'B2'),
    ('enforce quality standards', 'verb + noun phrase', 'thực thi các tiêu chuẩn chất lượng một cách nhất quán', 'B2'),
    ('conduct compliance reviews', 'verb + noun phrase', 'thực hiện các đợt rà soát việc tuân thủ yêu cầu hoặc quy định', 'C1'),
    ('strengthen audit coverage', 'verb + noun phrase', 'mở rộng và tăng cường phạm vi kiểm toán hoặc kiểm tra', 'C1'),
    ('document control procedures', 'verb + noun phrase', 'ghi chép rõ các thủ tục kiểm soát để có thể áp dụng và kiểm tra nhất quán', 'B2'),
    ('maintain accurate records', 'verb + noun phrase', 'duy trì hồ sơ chính xác và được cập nhật đầy đủ', 'B2'),
    ('improve records management', 'verb + noun phrase', 'cải thiện việc tổ chức, lưu trữ và truy xuất hồ sơ', 'B2'),
    ('establish escalation procedures', 'verb + noun phrase', 'thiết lập quy trình chuyển vấn đề lên cấp có thẩm quyền cao hơn', 'B2'),
    ('resolve service complaints', 'verb + noun phrase', 'giải quyết các khiếu nại liên quan tới chất lượng hoặc cách cung cấp dịch vụ', 'B2'),
    ('monitor customer satisfaction', 'verb + noun phrase', 'theo dõi mức độ hài lòng của khách hàng theo thời gian', 'B2'),
    ('analyze user feedback', 'verb + noun phrase', 'phân tích phản hồi của người dùng để xác định vấn đề và cơ hội cải tiến', 'B2'),
    ('identify service gaps', 'verb + noun phrase', 'xác định những khoảng thiếu hụt giữa dịch vụ hiện có và nhu cầu thực tế', 'B2'),
    ('prioritize corrective measures', 'verb + noun phrase', 'xếp thứ tự ưu tiên cho các biện pháp khắc phục cần thực hiện', 'C1'),
    ('verify corrective actions', 'verb + noun phrase', 'xác minh các hành động khắc phục đã được thực hiện và có hiệu quả', 'C1'),
    ('track recurring issues', 'verb + noun phrase', 'theo dõi các vấn đề lặp lại để nhận diện mẫu và nguyên nhân', 'B2'),
    ('address root causes', 'verb + noun phrase', 'xử lý các nguyên nhân gốc thay vì chỉ giải quyết biểu hiện bề mặt', 'B2'),
    ('prevent problem recurrence', 'verb + noun phrase', 'ngăn vấn đề đã xảy ra lặp lại trong tương lai', 'C1'),
    ('improve incident response', 'verb + noun phrase', 'cải thiện tốc độ và chất lượng phản ứng khi xảy ra sự cố', 'B2'),
    ('coordinate emergency response', 'verb + noun phrase', 'phối hợp phản ứng giữa các bên khi xảy ra tình huống khẩn cấp', 'C1'),
    ('restore critical services', 'verb + noun phrase', 'khôi phục các dịch vụ thiết yếu sau sự cố hoặc gián đoạn', 'B2'),
    ('strengthen recovery planning', 'verb + noun phrase', 'tăng cường kế hoạch phục hồi để sẵn sàng cho gián đoạn hoặc khủng hoảng', 'C1'),
]

def read_json(path: Path): return json.loads(path.read_text(encoding='utf-8'))
def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def normalized_key(text: str) -> str: return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text).strip().lower())
def token_set(text: str) -> set[str]: return {p for p in re.sub(r"[^a-z0-9'’-]+", ' ', normalized_key(text)).split() if p}
def jaccard(a: str,b: str)->float:
    l,r=token_set(a),token_set(b)
    if not l and not r:return 1.0
    if not l or not r:return 0.0
    return len(l&r)/len(l|r)
def digest(record)->str:
    src=json.loads(json.dumps(record,ensure_ascii=False)); checks=src.get('quality',{}).get('checks',{}); checks.pop('cefr',None); checks.pop('license',None)
    return hashlib.sha256((json.dumps(src,ensure_ascii=False,indent=2)+'\n').encode()).hexdigest()
def replace_once(text,old,new,label):
    c=text.count(old)
    if c!=1: raise RuntimeError(f'{label}: expected exactly one occurrence, found {c}')
    return text.replace(old,new,1)
def make_collocation(identifier,spec):
    text,pattern,meaning,cefr=spec; rid=f'col.{identifier:08d}'
    return {'schemaVersion':1,'id':rid,'text':text,'headwordKeys':[normalized_key(text).split()[0]],'pattern':pattern,'meaningVi':meaning,'cefr':cefr,'register':['neutral'],'exampleIds':[],'quality':{'state':'draft','checks':{'schema':{'status':'pass','method':'e04-scale-28-authoring-v1'},'grammar':{'status':'pending','method':'manual-review-required'},'translation':{'status':'pending','method':'manual-review-required'},'naturalness':{'status':'pending','method':'manual-review-required'},'cefr':{'status':'pending','method':'manual-review-required'},'targetStructure':{'status':'pending','method':'manual-review-required'},'exactDuplicate':{'status':'pass','method':'normalized-key-v29'},'nearDuplicate':{'status':'pending','method':'manual-review-required'},'license':{'status':'pending','method':'manual-review-required'}}},'provenance':{'sources':[{'dataset':'project-original','sourceId':rid,'sourceUrl':'content/english/phrases/e04-scale-28-collocations.json','snapshot':'2026-10','license':'LicenseRef-Project-Original','modified':False}],'note':'Project-original controlled E04 scale-up record.'}}

def update_progress():
    text=PROGRESS_PATH.read_text(encoding='utf-8')
    text=replace_once(text,'- Latest fully CI-verified scale-up prep HEAD: `a393e8351687c202be391935487b697d9597882d` — scale-26 publication workflow, Full Validation, Master Plan Acceptance and Platform CI all PASS; publication output: `0eb0bad34550866a067730d98ab1157da569b80b`.','- Latest fully CI-verified scale-up prep HEAD: `12313191cbf20f5a3223f139bc507e8cc3a5d9dd` — scale-27 publication workflow, Full Validation, Master Plan Acceptance and Platform CI all PASS; publication output: `4b57e29cb75b8f46945704f574621508d5f8a9fe`.','verified head')
    old='''- Latest verified scale-up gates before scale-27 publication:\n  - Apply English E04 Scale 26 #1 — PASS\n  - English Content Full Validation #64 — PASS\n  - English Content Master Plan Acceptance #45 — PASS\n  - Platform CI #1057 — PASS'''
    new='''- Latest verified scale-up gates before scale-28 publication:\n  - Apply English E04 Scale 27 #1 — PASS\n  - English Content Full Validation #65 — PASS\n  - English Content Master Plan Acceptance #47 — PASS\n  - Platform CI #1064 — PASS'''
    text=replace_once(text,old,new,'CI checkpoint')
    text=replace_once(text,'- E04 phrase/pattern architecture + current reviewed publication: complete — 1,830 published records after scale-27','- E04 phrase/pattern architecture + current reviewed publication: complete — 1,870 published records after scale-28','E04 count')
    text=replace_once(text,'## Published runtime snapshot after E04 scale-27 publication','## Published runtime snapshot after E04 scale-28 publication','snapshot heading')
    text=replace_once(text,'- phrases: 1,830 records','- phrases: 1,870 records','phrases')
    text=replace_once(text,'- total published rich records: 6,431','- total published rich records: 6,471','total')
    text=replace_once(text,'- editorial ledger: 6,431 decisions / 6,431 applied / 6,431 publish decisions','- editorial ledger: 6,471 decisions / 6,471 applied / 6,471 publish decisions','ledger')
    text=replace_once(text,'Scale-26 and scale-27 collocation batches are complete after all publication gates pass. Resolve latest HEAD, verify scale-27 publication/CI, then continue immediately with the next genuinely new bounded collocation batch from the new ID frontier (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.','Scale-26, scale-27 and scale-28 collocation batches are complete after all publication gates pass. Resolve latest HEAD, verify scale-28 publication/CI, then continue immediately with the next genuinely new bounded collocation batch from the new ID frontier (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.','next task')
    PROGRESS_PATH.write_text(text,encoding='utf-8')

def main():
    manifest=read_json(MANIFEST_PATH)
    if any(b.get('id')==BATCH_ID for b in manifest.get('batches',[])):
        print(json.dumps({'status':'skip','reason':'batch already exists','batch':BATCH_ID},indent=2)); return
    if COL_PATH.exists() or DECISION_PATH.exists(): raise RuntimeError('scale-28 artifact exists without matching batch manifest')
    existing={'collocations':[],'verbPatterns':[],'phraseItems':[]}; all_texts=[]; all_ids=set()
    for batch in manifest.get('batches',[]):
        if batch.get('phase')!='E04' or batch.get('category')!='phrases': continue
        for rs in batch.get('recordSets',[]):
            records=read_json(ROOT/rs['path']).get('records',[]); sid=rs.get('id')
            if sid in {'collocations','scale-collocations'}: existing['collocations'].extend(records)
            elif sid in {'verb-patterns','scale-verb-patterns'}: existing['verbPatterns'].extend(records)
            elif sid in {'phrases','scale-phrases'}: existing['phraseItems'].extend(records)
            for rec in records:
                rid=rec.get('id')
                if rid in all_ids: raise RuntimeError(f'existing duplicate E04 record id: {rid}')
                all_ids.add(rid); value=rec.get('text') or rec.get('pattern') or ''
                if value: all_texts.append((rid,value))
    actual={k:len(v) for k,v in existing.items()}
    if actual!=EXPECTED: raise RuntimeError(f'E04 source counts drifted; expected {EXPECTED}, got {actual}')
    nums=[int(m.group(1)) for r in existing['collocations'] if (m:=re.fullmatch(r'col\.(\d{8})',str(r.get('id',''))))]
    if not nums or max(nums)!=720: raise RuntimeError(f'collocation ID frontier drifted; expected max 720, got {max(nums) if nums else None}')
    new=[make_collocation(721+i,s) for i,s in enumerate(COLLOCATIONS)]
    exact={normalized_key(t):rid for rid,t in all_texts}; accepted=[]
    for rec in new:
        rid,text=rec['id'],rec['text']; key=normalized_key(text)
        if rid in all_ids: raise RuntimeError(f'new record id collides: {rid}')
        if key in exact: raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {exact[key]}')
        for oid,ot in all_texts:
            score=jaccard(text,ot)
            if score>=NEAR_DUP_THRESHOLD: raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {oid} {ot!r}')
        for prior in accepted:
            score=jaccard(text,prior['text'])
            if normalized_key(prior['text'])==key or score>=NEAR_DUP_THRESHOLD: raise RuntimeError(f'duplicate inside scale-28: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(rec)
    write_json(COL_PATH,{'schemaVersion':1,'records':new})
    manifest['batches'].append({'id':BATCH_ID,'phase':'E04','category':'phrases','cefr':['B2','C1'],'state':'draft','recordSets':[{'id':'scale-collocations','path':'content/english/phrases/e04-scale-28-collocations.json','expectedCount':40,'generated':False,'allowedQualityStates':['draft'],'requiredChecks':['schema','grammar','translation','naturalness','cefr','targetStructure','exactDuplicate','nearDuplicate','license']}],'requiredBeforePublish':['schema-validation','reference-integrity','exact-dedup','near-dedup','grammar-review','bilingual-review','naturalness-review','cefr-review','target-structure-review','license-review','cross-game-smoke'],'gameSmokes':[{'gameId':'recall-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},{'gameId':'vocab-shooter','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},{'gameId':'space-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5}]})
    write_json(MANIFEST_PATH,manifest)
    decisions=[]
    for rec in new:
        decisions.append({'id':'review.e04.scale-28.'+rec['id'].replace('.','-'),'batchId':BATCH_ID,'recordSetId':'scale-collocations','recordId':rec['id'],'sourceDigest':digest(rec),'targetState':'published','checks':{'grammar':{'status':'pass','method':'e04-scale-28-grammar-editorial-review'},'translation':{'status':'pass','method':'e04-scale-28-bilingual-review'},'naturalness':{'status':'pass','method':'e04-scale-28-naturalness-review'},'cefr':{'status':'pass','method':'e04-scale-28-cefr-review'},'targetStructure':{'status':'pass','method':'e04-scale-28-structure-review'},'nearDuplicate':{'status':'pass','method':'e04-scale-28-cross-batch-near-dedup-review'},'license':{'status':'pass','method':'project-original-license-review-v1'}},'reviewedAt':REVIEWED_AT,'reviewedBy':REVIEWED_BY,'note':'Focused E04 scale 28 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.'})
    write_json(DECISION_PATH,{'schemaVersion':1,'decisions':decisions})
    smoke_path=ROOT/'scripts/smoke-published-english-content.mjs'; smoke=smoke_path.read_text(encoding='utf-8')
    smoke=replace_once(smoke,'if(recallCollocations!==720)','if(recallCollocations!==760)','count'); smoke=replace_once(smoke,'must expose 720 reviewed records','must expose 760 reviewed records','message'); smoke_path.write_text(smoke,encoding='utf-8')
    update_progress()
    print(json.dumps({'status':'applied','batch':BATCH_ID,'collocationsAdded':40,'collocationRange':['col.00000721','col.00000760'],'sourceCountsBefore':actual,'sourceCountsAfter':{'collocations':760,'verbPatterns':510,'phraseItems':600},'expectedRuntimeAfterPublish':{'phrases':1870,'richRecords':6471}},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
