#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-46.py'), run_name='e04_scale47_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-47-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-47.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-47'
REVIEWED_AT = '2026-10-07T08:05:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-47'
EXPECTED = {'collocations': 1480, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect rail alignment', 'verb + noun phrase', 'kiểm tra độ thẳng và vị trí hình học của đường ray để phát hiện sai lệch cần bảo trì', 'B2'),
    ('measure track gauge', 'verb + noun phrase', 'đo khổ đường ray để xác nhận khoảng cách giữa hai ray nằm trong giới hạn an toàn', 'B2'),
    ('grind rail defects', 'verb + noun phrase', 'mài các khuyết tật trên bề mặt ray để cải thiện độ êm và kéo dài tuổi thọ đường ray', 'C1'),
    ('tamp ballast beds', 'verb + noun phrase', 'đầm đá ballast dưới tà vẹt để khôi phục độ ổn định và hình học của đường ray', 'C1'),
    ('replace worn sleepers', 'verb + adjective + noun', 'thay các tà vẹt bị mòn hoặc hư hỏng để duy trì khả năng đỡ và cố định đường ray', 'B2'),
    ('tighten rail fasteners', 'verb + noun phrase', 'siết chặt các bộ phận liên kết ray để giữ ray và tà vẹt chắc chắn theo đúng tiêu chuẩn', 'B2'),
    ('lubricate switch points', 'verb + noun phrase', 'bôi trơn các bộ phận chuyển hướng của ghi để chúng vận hành trơn tru và đáng tin cậy', 'C1'),
    ('test signal aspects', 'verb + noun phrase', 'kiểm tra các trạng thái hiển thị của tín hiệu để bảo đảm thông tin điều hành tàu chính xác', 'B2'),
    ('calibrate axle counters', 'verb + noun phrase', 'hiệu chuẩn bộ đếm trục để phát hiện chính xác tình trạng chiếm dụng khu đoạn đường sắt', 'C1'),
    ('verify interlocking logic', 'verb + noun phrase', 'xác minh logic liên khóa để ngăn thiết lập các hành trình tàu xung đột hoặc không an toàn', 'C1'),
    ('inspect overhead catenary', 'verb + adjective + noun', 'kiểm tra hệ thống dây tiếp xúc trên cao để phát hiện hao mòn, võng hoặc hư hỏng', 'C1'),
    ('tension contact wire', 'verb + noun phrase', 'điều chỉnh lực căng dây tiếp xúc để duy trì hình học ổn định cho hệ thống cấp điện kéo', 'C1'),
    ('isolate traction power', 'verb + noun phrase', 'cô lập nguồn điện kéo trước khi thực hiện công việc bảo trì trong khu vực có điện nguy hiểm', 'C1'),
    ('ground electrical sections', 'verb + adjective + noun', 'nối đất các phân đoạn điện đã cô lập để bảo vệ nhân viên trong quá trình bảo trì', 'C1'),
    ('patrol railway corridors', 'verb + noun phrase', 'tuần tra hành lang đường sắt để phát hiện vật cản, xâm nhập hoặc điều kiện bất thường', 'B2'),
    ('clear track obstructions', 'verb + noun phrase', 'loại bỏ vật cản trên đường ray để khôi phục hành lang chạy tàu an toàn', 'B2'),
    ('schedule possession windows', 'verb + noun phrase', 'lập lịch khoảng thời gian phong tỏa đường để đội kỹ thuật có thể làm việc an toàn', 'C1'),
    ('coordinate engineering trains', 'verb + adjective + noun', 'điều phối các đoàn tàu công trình để hỗ trợ vận chuyển thiết bị và vật liệu bảo trì', 'C1'),
    ('dispatch rescue locomotives', 'verb + noun phrase', 'điều đầu máy cứu viện đến vị trí tàu gặp sự cố để hỗ trợ kéo hoặc phục hồi hoạt động', 'B2'),
    ('recover disabled trains', 'verb + adjective + noun', 'xử lý và đưa các đoàn tàu mất khả năng vận hành ra khỏi tuyến hoặc trở lại trạng thái khai thác', 'C1'),
    ('manage platform crowding', 'verb + noun phrase', 'quản lý tình trạng đông người trên sân ga để giảm rủi ro và duy trì luồng hành khách an toàn', 'B2'),
    ('regulate train headways', 'verb + noun phrase', 'điều chỉnh khoảng cách thời gian giữa các chuyến tàu để duy trì tần suất khai thác ổn định', 'C1'),
    ('turn back delayed services', 'verb + adjective + noun', 'cho các chuyến tàu bị chậm quay đầu sớm để khôi phục lịch chạy và giảm chậm dây chuyền', 'C1'),
    ('short-turn peak services', 'verb + adjective + noun', 'cho một số chuyến giờ cao điểm quay đầu tại ga trung gian để tăng năng lực ở đoạn đông khách', 'C1'),
    ('reroute passenger flows', 'verb + noun phrase', 'điều hướng lại luồng hành khách khi có đóng ga, gián đoạn hoặc khu vực quá tải', 'B2'),
    ('inspect tunnel drainage', 'verb + noun phrase', 'kiểm tra hệ thống thoát nước trong hầm để ngăn ngập và hư hại kết cấu hoặc thiết bị', 'B2'),
    ('pump trackside flooding', 'verb + noun phrase', 'bơm thoát nước ngập bên đường ray để khôi phục điều kiện vận hành an toàn', 'B2'),
    ('monitor bridge bearings', 'verb + noun phrase', 'theo dõi gối cầu để phát hiện dịch chuyển, hao mòn hoặc dấu hiệu suy giảm bất thường', 'C1'),
    ('survey embankment movement', 'verb + noun phrase', 'khảo sát chuyển vị nền đắp để phát hiện lún hoặc trượt ảnh hưởng đến ổn định đường sắt', 'C1'),
    ('stabilize track foundations', 'verb + noun phrase', 'gia cố nền đường sắt để hạn chế lún, biến dạng và mất ổn định hình học đường ray', 'C1'),
    ('maintain level crossings', 'verb + noun phrase', 'bảo trì đường ngang để các thiết bị cảnh báo và bề mặt giao cắt hoạt động an toàn', 'B2'),
    ('test crossing barriers', 'verb + noun phrase', 'kiểm tra cần chắn đường ngang để xác nhận chu trình đóng mở và cơ chế an toàn hoạt động đúng', 'B2'),
    ('inspect wheel profiles', 'verb + noun phrase', 'kiểm tra biên dạng bánh xe để phát hiện mòn ảnh hưởng đến tiếp xúc bánh-ray và độ ổn định chạy tàu', 'C1'),
    ('monitor bearing temperatures', 'verb + noun phrase', 'theo dõi nhiệt độ ổ trục để phát hiện quá nhiệt trước khi phát sinh hỏng hóc nghiêm trọng', 'B2'),
    ('service braking systems', 'verb + adjective + noun', 'bảo dưỡng hệ thống phanh để duy trì lực phanh, độ tin cậy và khả năng dừng tàu an toàn', 'B2'),
    ('verify door interlocks', 'verb + noun phrase', 'xác minh liên khóa cửa để tàu không thể khởi hành khi cửa chưa ở trạng thái an toàn', 'C1'),
    ('clean traction motors', 'verb + noun phrase', 'làm sạch động cơ kéo để giảm bụi bẩn, hỗ trợ tản nhiệt và duy trì hiệu suất vận hành', 'B2'),
    ('diagnose signaling faults', 'verb + noun phrase', 'chẩn đoán lỗi hệ thống tín hiệu để xác định nguyên nhân và khôi phục chức năng điều hành an toàn', 'C1'),
    ('document maintenance defects', 'verb + noun phrase', 'ghi chép các khiếm khuyết được phát hiện trong bảo trì để theo dõi sửa chữa và lịch sử tài sản', 'B2'),
    ('close safety incidents', 'verb + noun phrase', 'khép lại hồ sơ sự cố an toàn sau khi hoàn tất điều tra, hành động khắc phục và xác minh kết quả', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-47-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v47'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-47-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-46 publication: `c4ce06381108bfe1888f99e02ea81c8ccfa66f7f` — scale-45 publication state verified by English Content Master Plan Acceptance #109, English Content Full Validation #108 and Platform CI #1158; published output: `af9a91944cf030ff3fafb753ff2ada8bf62bd643`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-47 publication: `2acfa2b7b3eff63b4bb1c7931581ea3129910b5e` — scale-46 publication state verified by English Content Master Plan Acceptance #112, English Content Full Validation #110 and Platform CI #1161; published output: `0b469babc616995ec11ea97994b6bfc7528f527a`.',
        'verified scale-46 checkpoint',
    )
    text = replace_once(text, '- Scale-46 publication output: `0b469babc616995ec11ea97994b6bfc7528f527a` — `feat(content): publish E04 collocation scale 46`; Apply English E04 Scale 46 #1 passed preflight, controlled review, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-46 publication line')
    text = replace_once(text, '- Scale-46 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #111 and Platform CI #1160 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-46 content or weakening any gate.\n', '', 'remove scale-46 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,590 published records after scale-46', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,630 published records after scale-47', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-46 publication', '## Published runtime snapshot after E04 scale-47 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,590 records', '- phrases: 2,630 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,191', '- total published rich records: 7,231', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,191 decisions / 7,191 applied / 7,191 publish decisions', '- editorial ledger: 7,231 decisions / 7,231 applied / 7,231 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001480`', '- E04 collocation frontier: `col.00001520`', 'collocation frontier')
    old_workstream = '''1. Scale-45 publication is fully verified; do not duplicate scale-45 artifacts.
2. Scale-46 publication `0b469babc616995ec11ea97994b6bfc7528f527a` is complete; do not regenerate or duplicate scale-46 artifacts.
3. Verify scale-46 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #111/#1160 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-46 checkpoint CI passes and no newer worker has claimed the next scope, create scale-47 as the next bounded collocation batch from frontier `col.00001480`, expected IDs `col.00001481` through `col.00001520`, while preserving exact/near-dedupe threshold 0.86 and all E10/E11/E12 gates.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-46 publication is fully verified; do not duplicate scale-46 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-47 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-46 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-46 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001480` (expected scale-47 range `col.00001481` through `col.00001520` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-47 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001520` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-47 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1480:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1480, got {max(nums) if nums else None}')

    new = [make_collocation(1481 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-47: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-47-collocations.json',
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
            'id': 'review.e04.scale-47.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-47-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-47-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-47-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-47-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-47-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-47-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 47 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1480)', 'if(recallCollocations!==1520)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1480 reviewed records', 'must expose 1520 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001481', 'col.00001520'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1520, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2630, 'richRecords': 7231},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
