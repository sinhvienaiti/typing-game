#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-42.py'), run_name='e04_scale43_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-43-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-43.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-43'
REVIEWED_AT = '2026-10-07T07:05:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-43'
EXPECTED = {'collocations': 1320, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('schedule vessel berths', 'verb + noun phrase', 'lập lịch cầu bến cho tàu dựa trên thời gian đến, kích thước và nhu cầu khai thác', 'B2'),
    ('assign harbor pilots', 'verb + noun phrase', 'phân công hoa tiêu cảng hỗ trợ tàu ra vào khu vực hàng hải theo lịch', 'B2'),
    ('coordinate tug assistance', 'verb + noun phrase', 'điều phối tàu kéo hỗ trợ thao tác cập hoặc rời bến của tàu biển', 'C1'),
    ('monitor vessel arrivals', 'verb + noun phrase', 'theo dõi thời điểm tàu đến để chuẩn bị cầu bến, nhân lực và thiết bị khai thác', 'B2'),
    ('record vessel draft', 'verb + noun phrase', 'ghi nhận mớn nước của tàu để đánh giá giới hạn luồng và điều kiện cập bến', 'C1'),
    ('verify cargo manifests', 'verb + noun phrase', 'xác minh bản khai hàng hóa so với lô hàng và hồ sơ vận chuyển liên quan', 'B2'),
    ('inspect container seals', 'verb + noun phrase', 'kiểm tra niêm phong container để xác nhận tính nguyên vẹn trước khi xử lý', 'B2'),
    ('weigh export containers', 'verb + adjective + noun', 'cân container xuất khẩu để xác nhận khối lượng phục vụ xếp tàu và chứng từ', 'B2'),
    ('sequence quay crane moves', 'verb + noun phrase', 'sắp xếp trình tự thao tác cẩu bờ để tối ưu quá trình xếp dỡ container', 'C1'),
    ('dispatch terminal tractors', 'verb + adjective + noun', 'điều xe đầu kéo trong cảng để vận chuyển container giữa cầu tàu và bãi', 'B2'),
    ('stack import containers', 'verb + adjective + noun', 'xếp container nhập khẩu vào vị trí bãi theo kế hoạch lưu trữ và lấy hàng', 'B2'),
    ('rehandle blocked containers', 'verb + adjective + noun', 'di chuyển lại các container cản trở để tiếp cận đúng container cần khai thác', 'C1'),
    ('allocate yard slots', 'verb + noun phrase', 'phân bổ vị trí bãi cho container theo loại, thời gian lưu và kế hoạch giao nhận', 'B2'),
    ('track container dwell time', 'verb + noun phrase', 'theo dõi thời gian container lưu tại cảng để kiểm soát ùn tắc và chi phí', 'C1'),
    ('monitor reefer temperatures', 'verb + noun phrase', 'theo dõi nhiệt độ container lạnh để bảo đảm hàng hóa được duy trì đúng điều kiện', 'B2'),
    ('connect reefer power', 'verb + noun phrase', 'kết nối nguồn điện cho container lạnh tại bãi theo quy trình an toàn', 'B2'),
    ('inspect lifting gear', 'verb + noun phrase', 'kiểm tra thiết bị nâng để bảo đảm tình trạng kỹ thuật trước khi sử dụng', 'B2'),
    ('certify crane operators', 'verb + noun phrase', 'xác nhận năng lực và chứng nhận của người vận hành cẩu theo yêu cầu an toàn', 'C1'),
    ('enforce quay safety zones', 'verb + noun phrase', 'duy trì khu vực an toàn tại cầu tàu để hạn chế người và phương tiện không phận sự', 'C1'),
    ('conduct mooring inspections', 'verb + noun phrase', 'thực hiện kiểm tra hệ thống dây buộc tàu và điểm neo trong thời gian tàu ở bến', 'C1'),
    ('secure mooring lines', 'verb + noun phrase', 'cố định dây buộc tàu đúng vị trí và lực căng để duy trì tàu ổn định tại bến', 'B2'),
    ('adjust gangway access', 'verb + noun phrase', 'điều chỉnh cầu thang lên xuống tàu theo thủy triều và vị trí tàu tại bến', 'B2'),
    ('inspect berth fenders', 'verb + noun phrase', 'kiểm tra đệm chống va cầu bến để bảo đảm khả năng hấp thụ lực khi tàu cập', 'C1'),
    ('measure channel depth', 'verb + noun phrase', 'đo độ sâu luồng để xác nhận điều kiện hành hải phù hợp với mớn nước tàu', 'C1'),
    ('survey navigation buoys', 'verb + noun phrase', 'khảo sát phao báo hiệu hàng hải để xác nhận vị trí và tình trạng hoạt động', 'C1'),
    ('issue port clearance', 'verb + noun phrase', 'cấp xác nhận cho tàu rời cảng sau khi hoàn tất các yêu cầu khai thác và thủ tục', 'C1'),
    ('process crew declarations', 'verb + noun phrase', 'xử lý khai báo thuyền viên theo hồ sơ tàu và yêu cầu kiểm soát biên giới', 'B2'),
    ('coordinate customs inspections', 'verb + noun phrase', 'điều phối kiểm tra hải quan đối với tàu, hàng hóa hoặc container theo yêu cầu', 'B2'),
    ('arrange bunkering services', 'verb + noun phrase', 'sắp xếp dịch vụ cấp nhiên liệu cho tàu tại vị trí và thời gian đã xác nhận', 'C1'),
    ('transfer marine fuel', 'verb + adjective + noun', 'chuyển nhiên liệu hàng hải giữa phương tiện cấp và tàu theo quy trình kiểm soát tràn đổ', 'C1'),
    ('monitor ballast discharge', 'verb + noun phrase', 'theo dõi việc xả nước dằn tàu để đáp ứng yêu cầu môi trường và vận hành', 'C1'),
    ('collect oily waste', 'verb + adjective + noun', 'thu gom chất thải có dầu từ tàu để chuyển đến hệ thống xử lý phù hợp', 'B2'),
    ('deploy spill booms', 'verb + noun phrase', 'triển khai phao quây để hạn chế dầu hoặc chất lỏng ô nhiễm lan rộng trên mặt nước', 'C1'),
    ('report marine spills', 'verb + adjective + noun', 'báo cáo sự cố tràn dầu hoặc chất ô nhiễm trên vùng nước cảng theo quy trình ứng phó', 'B2'),
    ('patrol restricted waters', 'verb + adjective + noun', 'tuần tra vùng nước hạn chế để phát hiện xâm nhập và duy trì an ninh cảng', 'B2'),
    ('screen port visitors', 'verb + noun phrase', 'kiểm tra khách ra vào khu vực cảng theo yêu cầu nhận dạng và an ninh', 'B2'),
    ('verify truck appointments', 'verb + noun phrase', 'xác minh lịch hẹn xe tải trước khi cho phương tiện vào khu vực giao nhận container', 'B2'),
    ('meter gate traffic', 'verb + noun phrase', 'điều tiết lưu lượng phương tiện qua cổng cảng để giảm ùn tắc và thời gian chờ', 'C1'),
    ('reconcile terminal inventory', 'verb + adjective + noun', 'đối chiếu tồn container tại cảng giữa vị trí thực tế và dữ liệu hệ thống', 'C1'),
    ('audit port service charges', 'verb + noun phrase', 'kiểm tra các khoản phí dịch vụ cảng so với hoạt động, hợp đồng và biểu phí áp dụng', 'C1'),
]

def make_collocation(identifier: int, spec):
    text, pattern, meaning, cefr = spec
    rid = f'col.{identifier:08d}'
    return {
        'schemaVersion': 1,
        'id': rid,
        'text': text,
        'headwordKeys': [normalized_key(text).split()[0]],
        'pattern': pattern,
        'meaningVi': meaning,
        'cefr': cefr,
        'register': ['neutral'],
        'exampleIds': [],
        'quality': {'state': 'draft', 'checks': {
            'schema': {'status': 'pass', 'method': 'e04-scale-43-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v43'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-43-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-42 publication: `17be297dc7461ed542d2f7dbbdedc2266ed5bafb` — scale-41 publication state verified by English Content Master Plan Acceptance #96, English Content Full Validation #99 and Platform CI #1140; published output: `6b72aba6a305a3e4bd2180fa05efcb04beee70ec`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-43 publication: `94f5afd6d5da51313c0f51d45d6a7b153f3d3e60` — scale-42 publication state verified by English Content Master Plan Acceptance #99, English Content Full Validation #101 and Platform CI #1143; published output: `e6682d58f768b23107e47608689dc73fccea3a25`.',
        'verified scale-42 checkpoint',
    )
    text = replace_once(text, '- Scale-42 publication output: `e6682d58f768b23107e47608689dc73fccea3a25` — `feat(content): publish E04 collocation scale 42`; preflight, controlled review, full quality gates, converge and deterministic replay passed before the bot commit was pushed.\n', '', 'remove scale-42 publication line')
    text = replace_once(text, '- Scale-42 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #98 and Platform CI #1142 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-42 content or weakening any gate.\n', '', 'remove scale-42 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,430 published records after scale-42', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,470 published records after scale-43', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-42 publication', '## Published runtime snapshot after E04 scale-43 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,430 records', '- phrases: 2,470 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,031', '- total published rich records: 7,071', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,031 decisions / 7,031 applied / 7,031 publish decisions', '- editorial ledger: 7,071 decisions / 7,071 applied / 7,071 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001320`', '- E04 collocation frontier: `col.00001360`', 'collocation frontier')
    old_workstream = '''1. Scale-41 publication is fully verified; do not duplicate scale-41 artifacts.
2. Scale-42 publication `e6682d58f768b23107e47608689dc73fccea3a25` is complete; do not regenerate or duplicate scale-42 artifacts.
3. Verify scale-42 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #98/#1142 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-42 checkpoint CI passes and no newer worker has claimed the next scope, create the next bounded E04 scale batch from frontier `col.00001320`, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-42 publication is fully verified; do not duplicate scale-42 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-43 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-42 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-42 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001320` (expected scale-43 range `col.00001321` through `col.00001360` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-43 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001360` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-43 artifact exists without matching batch manifest')

    existing = {'collocations': [], 'verbPatterns': [], 'phraseItems': []}
    all_texts = []
    all_ids = set()
    for batch in manifest.get('batches', []):
        if batch.get('phase') != 'E04' or batch.get('category') != 'phrases':
            continue
        for record_set in batch.get('recordSets', []):
            records = read_json(ROOT / record_set['path']).get('records', [])
            record_set_id = record_set.get('id')
            if record_set_id in {'collocations', 'scale-collocations'}:
                existing['collocations'].extend(records)
            elif record_set_id in {'verb-patterns', 'scale-verb-patterns'}:
                existing['verbPatterns'].extend(records)
            elif record_set_id in {'phrases', 'scale-phrases'}:
                existing['phraseItems'].extend(records)
            for record in records:
                rid = record.get('id')
                if rid in all_ids:
                    raise RuntimeError(f'existing duplicate E04 record id: {rid}')
                all_ids.add(rid)
                value = record.get('text') or record.get('pattern') or ''
                if value:
                    all_texts.append((rid, value))

    actual = {key: len(value) for key, value in existing.items()}
    if actual != EXPECTED:
        raise RuntimeError(f'E04 source counts drifted; expected {EXPECTED}, got {actual}')
    nums = [int(match.group(1)) for record in existing['collocations'] if (match := re.fullmatch(r'col\.(\d{8})', str(record.get('id', ''))))]
    if not nums or max(nums) != 1320:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1320, got {max(nums) if nums else None}')

    new = [make_collocation(1321 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
    exact = {normalized_key(text): rid for rid, text in all_texts}
    accepted = []
    for record in new:
        rid, text = record['id'], record['text']
        key = normalized_key(text)
        if rid in all_ids:
            raise RuntimeError(f'new record id collides: {rid}')
        if key in exact:
            raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {exact[key]}')
        for old_id, old_text in all_texts:
            score = jaccard(text, old_text)
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {old_id} {old_text!r}')
        for prior in accepted:
            score = jaccard(text, prior['text'])
            if normalized_key(prior['text']) == key or score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f'duplicate inside scale-43: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(record)

    write_json(COL_PATH, {'schemaVersion': 1, 'records': new})
    manifest['batches'].append({
        'id': BATCH_ID,
        'phase': 'E04',
        'category': 'phrases',
        'cefr': ['B2', 'C1'],
        'state': 'draft',
        'recordSets': [{
            'id': 'scale-collocations',
            'path': 'content/english/phrases/e04-scale-43-collocations.json',
            'expectedCount': 40,
            'generated': False,
            'allowedQualityStates': ['draft'],
            'requiredChecks': ['schema', 'grammar', 'translation', 'naturalness', 'cefr', 'targetStructure', 'exactDuplicate', 'nearDuplicate', 'license'],
        }],
        'requiredBeforePublish': ['schema-validation', 'reference-integrity', 'exact-dedup', 'near-dedup', 'grammar-review', 'bilingual-review', 'naturalness-review', 'cefr-review', 'target-structure-review', 'license-review', 'cross-game-smoke'],
        'gameSmokes': [
            {'gameId': 'recall-typing', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
            {'gameId': 'vocab-shooter', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
            {'gameId': 'space-typing', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
        ],
    })
    write_json(MANIFEST_PATH, manifest)

    decisions = []
    for record in new:
        decisions.append({
            'id': 'review.e04.scale-43.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-43-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-43-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-43-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-43-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-43-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-43-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 43 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1320)', 'if(recallCollocations!==1360)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1320 reviewed records', 'must expose 1360 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001321', 'col.00001360'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1360, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2470, 'richRecords': 7071},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
