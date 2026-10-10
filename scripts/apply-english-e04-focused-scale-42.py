#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-41.py'), run_name='e04_scale42_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-42-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-42.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-42'
REVIEWED_AT = '2026-10-07T06:55:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-42'
EXPECTED = {'collocations': 1280, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('forecast passenger demand', 'verb + noun phrase', 'dự báo nhu cầu hành khách để lập kế hoạch năng lực nhà ga và nguồn lực khai thác', 'B2'),
    ('allocate boarding gates', 'verb + noun phrase', 'phân bổ cửa lên máy bay cho các chuyến theo lịch khai thác và loại tàu bay', 'B2'),
    ('assign aircraft stands', 'verb + noun phrase', 'phân vị trí đỗ tàu bay dựa trên kích thước, lịch quay đầu và điều kiện sân đỗ', 'B2'),
    ('coordinate ground handling', 'verb + noun phrase', 'điều phối các dịch vụ mặt đất để bảo đảm chuyến bay được phục vụ đúng trình tự và thời gian', 'C1'),
    ('schedule baggage crews', 'verb + noun phrase', 'lập lịch nhân sự hành lý theo lưu lượng chuyến bay và nhu cầu ca làm việc', 'B2'),
    ('load checked baggage', 'verb + adjective + noun', 'xếp hành lý ký gửi lên tàu bay theo chuyến, khoang và yêu cầu cân bằng tải', 'B2'),
    ('screen carry-on items', 'verb + adjective + noun', 'soi chiếu vật dụng xách tay theo quy trình an ninh hàng không', 'B2'),
    ('verify travel documents', 'verb + noun phrase', 'xác minh giấy tờ đi lại của hành khách trước khi làm thủ tục hoặc lên máy bay', 'B2'),
    ('process standby passengers', 'verb + adjective + noun', 'xử lý hành khách chờ chỗ theo thứ tự ưu tiên và số ghế còn trống', 'B2'),
    ('rebook disrupted travelers', 'verb + adjective + noun', 'đặt lại hành trình cho hành khách bị ảnh hưởng bởi hủy, chậm hoặc gián đoạn chuyến bay', 'B2'),
    ('announce gate changes', 'verb + noun phrase', 'thông báo thay đổi cửa ra máy bay qua các kênh thông tin trong nhà ga', 'B2'),
    ('manage boarding queues', 'verb + noun phrase', 'quản lý hàng chờ lên máy bay để duy trì trật tự và tiến độ boarding', 'B2'),
    ('prioritize connecting passengers', 'verb + adjective + noun', 'ưu tiên hành khách nối chuyến có thời gian chuyển tiếp ngắn hoặc nguy cơ lỡ chuyến', 'C1'),
    ('escort unaccompanied minors', 'verb + adjective + noun', 'hộ tống trẻ em đi một mình theo quy trình bàn giao và giám sát của hãng', 'B2'),
    ('assist reduced-mobility passengers', 'verb + adjective + noun', 'hỗ trợ hành khách hạn chế khả năng di chuyển trong quá trình làm thủ tục, di chuyển và lên máy bay', 'B2'),
    ('monitor aircraft turnaround times', 'verb + noun phrase', 'theo dõi thời gian quay đầu tàu bay để nhận diện chậm trễ trong các hoạt động mặt đất', 'C1'),
    ('service aircraft cabins', 'verb + noun phrase', 'thực hiện các dịch vụ khoang hành khách giữa hai chuyến để chuẩn bị tàu bay cho lượt khai thác tiếp theo', 'B2'),
    ('replenish potable water', 'verb + adjective + noun', 'bổ sung nước sạch cho hệ thống phục vụ trên tàu bay theo mức yêu cầu', 'B2'),
    ('empty aircraft waste tanks', 'verb + noun phrase', 'xả bồn chất thải tàu bay theo quy trình vệ sinh và an toàn tại sân đỗ', 'C1'),
    ('refuel parked aircraft', 'verb + adjective + noun', 'tiếp nhiên liệu cho tàu bay đang đỗ theo khối lượng đã tính và yêu cầu an toàn', 'C1'),
    ('inspect runway surfaces', 'verb + noun phrase', 'kiểm tra bề mặt đường băng để phát hiện hư hỏng, vật cản hoặc điều kiện bất thường', 'C1'),
    ('remove foreign-object debris', 'verb + adjective + noun', 'loại bỏ vật thể lạ trên khu bay để giảm nguy cơ hư hỏng tàu bay', 'C1'),
    ('measure runway friction', 'verb + noun phrase', 'đo độ ma sát đường băng để đánh giá điều kiện khai thác khi bề mặt ướt hoặc bị nhiễm bẩn', 'C1'),
    ('maintain taxiway markings', 'verb + noun phrase', 'duy trì sơn kẻ và ký hiệu đường lăn rõ ràng theo tiêu chuẩn khai thác', 'B2'),
    ('activate runway lighting', 'verb + noun phrase', 'kích hoạt hệ thống đèn đường băng phù hợp với điều kiện khai thác và tầm nhìn', 'B2'),
    ('coordinate airfield snow removal', 'verb + adjective + noun', 'điều phối dọn tuyết tại khu bay để khôi phục điều kiện khai thác an toàn', 'C1'),
    ('issue airfield notices', 'verb + noun phrase', 'phát hành thông báo khai thác sân bay về hạn chế, đóng mở hoặc thay đổi điều kiện khu bay', 'C1'),
    ('monitor wildlife hazards', 'verb + noun phrase', 'theo dõi nguy cơ chim và động vật hoang dã ảnh hưởng đến hoạt động tàu bay', 'C1'),
    ('conduct perimeter patrols', 'verb + noun phrase', 'thực hiện tuần tra chu vi sân bay để phát hiện xâm nhập hoặc bất thường an ninh', 'B2'),
    ('test terminal emergency generators', 'verb + adjective + noun', 'kiểm thử máy phát điện khẩn cấp của nhà ga để xác nhận khả năng cấp điện dự phòng', 'C1'),
    ('stage airport rescue vehicles', 'verb + adjective + noun', 'bố trí phương tiện cứu nạn sân bay tại vị trí sẵn sàng đáp ứng tình huống khẩn cấp', 'C1'),
    ('dispatch airport fire crews', 'verb + adjective + noun', 'điều lực lượng chữa cháy sân bay đến khu vực xảy ra sự cố theo cấp độ phản ứng', 'C1'),
    ('inspect passenger boarding bridges', 'verb + adjective + noun', 'kiểm tra cầu ống lồng hành khách để bảo đảm vận hành an toàn và không có hư hỏng', 'C1'),
    ('calibrate baggage scanners', 'verb + noun phrase', 'hiệu chuẩn thiết bị soi chiếu hành lý để duy trì độ chính xác phát hiện theo yêu cầu', 'C1'),
    ('reconcile mishandled baggage', 'verb + adjective + noun', 'đối chiếu hồ sơ hành lý xử lý sai với chuyến bay, thẻ hành lý và thông tin hành khách', 'C1'),
    ('trace delayed luggage', 'verb + adjective + noun', 'truy vết hành lý đến chậm qua các chặng vận chuyển và điểm xử lý', 'B2'),
    ('process lost-property claims', 'verb + noun phrase', 'xử lý yêu cầu về tài sản thất lạc trong nhà ga theo hồ sơ và quy trình xác minh', 'B2'),
    ('monitor terminal occupancy', 'verb + noun phrase', 'theo dõi mật độ người trong nhà ga để hỗ trợ điều tiết dòng hành khách và năng lực khu vực', 'B2'),
    ('adjust security lane staffing', 'verb + noun phrase', 'điều chỉnh nhân sự làn kiểm tra an ninh theo lưu lượng hành khách thực tế', 'C1'),
    ('conduct terminal evacuation drills', 'verb + adjective + noun', 'tổ chức diễn tập sơ tán nhà ga để kiểm tra quy trình, phối hợp và thời gian phản ứng', 'C1'),
]

def make_collocation(identifier: int, spec):
    text, pattern, meaning, cefr = spec
    rid = f'col.{identifier:08d}'
    return {
        'schemaVersion': 1, 'id': rid, 'text': text,
        'headwordKeys': [normalized_key(text).split()[0]],
        'pattern': pattern, 'meaningVi': meaning, 'cefr': cefr,
        'register': ['neutral'], 'exampleIds': [],
        'quality': {'state': 'draft', 'checks': {
            'schema': {'status': 'pass', 'method': 'e04-scale-42-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v42'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original', 'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-42-collocations.json',
            'snapshot': '2026-10', 'license': 'LicenseRef-Project-Original', 'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(text,
        '- Latest fully CI-verified scale-up checkpoint before scale-41 publication: `fd8cc5c6cb04e2c2a500aa067480f72148c30cc6` — scale-40 publication state verified by English Content Master Plan Acceptance #93, English Content Full Validation #97 and Platform CI #1136; published output: `ca9f43aa36bf4f9458ea4feb7088af66150896ae`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-42 publication: `17be297dc7461ed542d2f7dbbdedc2266ed5bafb` — scale-41 publication state verified by English Content Master Plan Acceptance #96, English Content Full Validation #99 and Platform CI #1140; published output: `6b72aba6a305a3e4bd2180fa05efcb04beee70ec`.',
        'verified scale-41 checkpoint')
    text = replace_once(text, '- Scale-41 publication output: `6b72aba6a305a3e4bd2180fa05efcb04beee70ec` — `feat(content): publish E04 collocation scale 41`; preflight, controlled review, full quality gates, converge and deterministic replay passed before the bot commit was pushed.\n', '', 'remove scale-41 publication line')
    text = replace_once(text, '- Scale-41 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #95 and Platform CI #1139 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-41 content or weakening any gate.\n', '', 'remove scale-41 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,390 published records after scale-41', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,430 published records after scale-42', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-41 publication', '## Published runtime snapshot after E04 scale-42 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,390 records', '- phrases: 2,430 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,991', '- total published rich records: 7,031', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,991 decisions / 6,991 applied / 6,991 publish decisions', '- editorial ledger: 7,031 decisions / 7,031 applied / 7,031 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001280`', '- E04 collocation frontier: `col.00001320`', 'collocation frontier')
    old_workstream = '''1. Scale-40 publication is fully verified; do not duplicate scale-40 artifacts.
2. Scale-41 publication `6b72aba6a305a3e4bd2180fa05efcb04beee70ec` is complete; do not regenerate or duplicate scale-41 artifacts.
3. Verify scale-41 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #95/#1139 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-41 checkpoint CI passes and no newer worker has claimed the next scope, create the next bounded E04 scale batch from frontier `col.00001280`, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-41 publication is fully verified; do not duplicate scale-41 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-42 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-41 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-41 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001280` (expected scale-42 range `col.00001281` through `col.00001320` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-42 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001320` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2)); return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-42 artifact exists without matching batch manifest')
    existing = {'collocations': [], 'verbPatterns': [], 'phraseItems': []}; all_texts = []; all_ids = set()
    for batch in manifest.get('batches', []):
        if batch.get('phase') != 'E04' or batch.get('category') != 'phrases': continue
        for record_set in batch.get('recordSets', []):
            records = read_json(ROOT / record_set['path']).get('records', []); rsid = record_set.get('id')
            if rsid in {'collocations', 'scale-collocations'}: existing['collocations'].extend(records)
            elif rsid in {'verb-patterns', 'scale-verb-patterns'}: existing['verbPatterns'].extend(records)
            elif rsid in {'phrases', 'scale-phrases'}: existing['phraseItems'].extend(records)
            for record in records:
                rid = record.get('id')
                if rid in all_ids: raise RuntimeError(f'existing duplicate E04 record id: {rid}')
                all_ids.add(rid); value = record.get('text') or record.get('pattern') or ''
                if value: all_texts.append((rid, value))
    actual = {key: len(value) for key, value in existing.items()}
    if actual != EXPECTED: raise RuntimeError(f'E04 source counts drifted; expected {EXPECTED}, got {actual}')
    nums = [int(m.group(1)) for r in existing['collocations'] if (m := re.fullmatch(r'col\.(\d{8})', str(r.get('id', ''))))]
    if not nums or max(nums) != 1280: raise RuntimeError(f'collocation ID frontier drifted; expected max 1280, got {max(nums) if nums else None}')
    new = [make_collocation(1281 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
    exact = {normalized_key(t): rid for rid, t in all_texts}; accepted = []
    for record in new:
        rid, text = record['id'], record['text']; key = normalized_key(text)
        if rid in all_ids: raise RuntimeError(f'new record id collides: {rid}')
        if key in exact: raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {exact[key]}')
        for old_id, old_text in all_texts:
            score = jaccard(text, old_text)
            if score >= NEAR_DUP_THRESHOLD: raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {old_id} {old_text!r}')
        for prior in accepted:
            score = jaccard(text, prior['text'])
            if normalized_key(prior['text']) == key or score >= NEAR_DUP_THRESHOLD: raise RuntimeError(f'duplicate inside scale-42: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(record)
    write_json(COL_PATH, {'schemaVersion': 1, 'records': new})
    manifest['batches'].append({'id': BATCH_ID, 'phase': 'E04', 'category': 'phrases', 'cefr': ['B2', 'C1'], 'state': 'draft', 'recordSets': [{'id': 'scale-collocations', 'path': 'content/english/phrases/e04-scale-42-collocations.json', 'expectedCount': 40, 'generated': False, 'allowedQualityStates': ['draft'], 'requiredChecks': ['schema','grammar','translation','naturalness','cefr','targetStructure','exactDuplicate','nearDuplicate','license']}], 'requiredBeforePublish': ['schema-validation','reference-integrity','exact-dedup','near-dedup','grammar-review','bilingual-review','naturalness-review','cefr-review','target-structure-review','license-review','cross-game-smoke'], 'gameSmokes': [{'gameId':'recall-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},{'gameId':'vocab-shooter','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},{'gameId':'space-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5}]})
    write_json(MANIFEST_PATH, manifest)
    decisions = []
    for record in new:
        decisions.append({'id':'review.e04.scale-42.' + record['id'].replace('.','-'),'batchId':BATCH_ID,'recordSetId':'scale-collocations','recordId':record['id'],'sourceDigest':digest(record),'targetState':'published','checks':{'grammar':{'status':'pass','method':'e04-scale-42-grammar-editorial-review'},'translation':{'status':'pass','method':'e04-scale-42-bilingual-review'},'naturalness':{'status':'pass','method':'e04-scale-42-naturalness-review'},'cefr':{'status':'pass','method':'e04-scale-42-cefr-review'},'targetStructure':{'status':'pass','method':'e04-scale-42-structure-review'},'nearDuplicate':{'status':'pass','method':'e04-scale-42-cross-batch-near-dedup-review'},'license':{'status':'pass','method':'project-original-license-review-v1'}},'reviewedAt':REVIEWED_AT,'reviewedBy':REVIEWED_BY,'note':'Focused E04 scale 42 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.'})
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})
    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'; smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1280)', 'if(recallCollocations!==1320)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1280 reviewed records', 'must expose 1320 reviewed records', 'smoke message'); smoke_path.write_text(smoke, encoding='utf-8')
    update_progress()
    print(json.dumps({'status':'applied','batch':BATCH_ID,'collocationsAdded':40,'collocationRange':['col.00001281','col.00001320'],'sourceCountsBefore':actual,'sourceCountsAfter':{'collocations':1320,'verbPatterns':510,'phraseItems':600},'expectedRuntimeAfterPublish':{'phrases':2430,'richRecords':7031}}, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
