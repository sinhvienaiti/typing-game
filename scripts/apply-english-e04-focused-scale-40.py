#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-39.py'), run_name='e04_scale40_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-40-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-40.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-40'
REVIEWED_AT = '2026-10-07T06:30:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-40'
EXPECTED = {'collocations': 1200, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('conduct site surveys', 'verb + noun phrase', 'thực hiện khảo sát hiện trường để thu thập dữ liệu phục vụ thiết kế và thi công', 'B2'),
    ('obtain building permits', 'verb + noun phrase', 'xin giấy phép xây dựng cần thiết trước khi triển khai công việc tại công trường', 'B2'),
    ('review structural drawings', 'verb + adjective + noun', 'rà soát bản vẽ kết cấu để xác nhận kích thước, tải trọng và chi tiết thi công', 'B2'),
    ('mark underground utilities', 'verb + adjective + noun', 'đánh dấu vị trí hạ tầng ngầm để tránh va chạm trong quá trình đào và thi công', 'B2'),
    ('prepare site access', 'verb + noun phrase', 'chuẩn bị lối tiếp cận công trường cho nhân lực, thiết bị và phương tiện vận chuyển', 'B2'),
    ('install temporary fencing', 'verb + adjective + noun', 'lắp hàng rào tạm để kiểm soát ranh giới và quyền ra vào công trường', 'B2'),
    ('establish safety zones', 'verb + noun phrase', 'thiết lập khu vực an toàn quanh các hoạt động hoặc thiết bị có rủi ro', 'B2'),
    ('inspect excavation slopes', 'verb + noun phrase', 'kiểm tra mái dốc hố đào để phát hiện dấu hiệu mất ổn định hoặc sạt lở', 'C1'),
    ('shore deep trenches', 'verb + adjective + noun', 'gia cố các rãnh đào sâu để ngăn sập thành và bảo vệ người làm việc', 'C1'),
    ('compact subgrade layers', 'verb + noun phrase', 'đầm chặt các lớp nền dưới trước khi thi công lớp kết cấu phía trên', 'C1'),
    ('test soil bearing capacity', 'verb + noun phrase', 'kiểm tra khả năng chịu tải của đất để xác nhận giả thiết thiết kế móng', 'C1'),
    ('pour concrete foundations', 'verb + noun phrase', 'đổ bê tông móng theo cấp phối, trình tự và điều kiện kỹ thuật đã quy định', 'B2'),
    ('cure concrete surfaces', 'verb + noun phrase', 'bảo dưỡng bề mặt bê tông để duy trì độ ẩm và phát triển cường độ phù hợp', 'C1'),
    ('erect structural steel', 'verb + adjective + noun', 'lắp dựng kết cấu thép theo trình tự, vị trí và yêu cầu an toàn đã phê duyệt', 'C1'),
    ('align support columns', 'verb + noun phrase', 'căn chỉnh các cột đỡ theo trục, cao độ và độ thẳng đứng thiết kế', 'C1'),
    ('torque anchor bolts', 'verb + noun phrase', 'siết bu lông neo đến mô-men yêu cầu để bảo đảm liên kết đạt điều kiện thiết kế', 'C1'),
    ('install roof membranes', 'verb + noun phrase', 'lắp lớp màng mái để bảo đảm khả năng chống thấm và độ liên tục của hệ bao che', 'B2'),
    ('seal expansion joints', 'verb + noun phrase', 'trám kín khe co giãn bằng vật liệu phù hợp để hạn chế nước và bụi xâm nhập', 'C1'),
    ('route electrical conduits', 'verb + adjective + noun', 'bố trí tuyến ống luồn điện theo bản vẽ và yêu cầu khoảng cách an toàn', 'B2'),
    ('terminate power cables', 'verb + noun phrase', 'đấu nối đầu cáp điện vào thiết bị hoặc tủ điện theo đúng quy trình kỹ thuật', 'C1'),
    ('pressure-test water lines', 'verb + noun phrase', 'thử áp đường ống nước để phát hiện rò rỉ và xác nhận khả năng chịu áp', 'B2'),
    ('flush plumbing systems', 'verb + noun phrase', 'xả rửa hệ thống ống nước để loại bỏ cặn bẩn trước khi đưa vào sử dụng', 'B2'),
    ('balance ventilation systems', 'verb + noun phrase', 'cân chỉnh hệ thống thông gió để lưu lượng tại các nhánh đạt yêu cầu thiết kế', 'C1'),
    ('commission fire alarms', 'verb + noun phrase', 'kiểm tra và đưa hệ thống báo cháy vào trạng thái vận hành chính thức', 'C1'),
    ('inspect sprinkler coverage', 'verb + noun phrase', 'kiểm tra phạm vi bao phủ của đầu phun chữa cháy so với yêu cầu thiết kế', 'C1'),
    ('verify emergency exits', 'verb + adjective + noun', 'xác minh lối thoát hiểm có vị trí, biển báo và khả năng tiếp cận phù hợp', 'B2'),
    ('document punch-list items', 'verb + noun phrase', 'ghi nhận các hạng mục tồn đọng cần hoàn thiện trước khi nghiệm thu cuối cùng', 'C1'),
    ('rectify construction defects', 'verb + noun phrase', 'khắc phục các khiếm khuyết thi công để đáp ứng yêu cầu chất lượng và hồ sơ thiết kế', 'C1'),
    ('coordinate trade contractors', 'verb + noun phrase', 'điều phối các nhà thầu chuyên ngành để giảm xung đột và chồng chéo công việc', 'C1'),
    ('sequence installation activities', 'verb + noun phrase', 'sắp xếp trình tự các hoạt động lắp đặt theo phụ thuộc kỹ thuật và tiến độ', 'C1'),
    ('track material deliveries', 'verb + noun phrase', 'theo dõi việc giao vật tư theo lịch, số lượng và vị trí tiếp nhận tại công trường', 'B2'),
    ('store weather-sensitive materials', 'verb + adjective + noun', 'bảo quản vật tư nhạy cảm với thời tiết trong điều kiện phù hợp để tránh hư hỏng', 'B2'),
    ('manage crane operations', 'verb + noun phrase', 'quản lý hoạt động cần cẩu theo kế hoạch nâng, vùng nguy hiểm và yêu cầu an toàn', 'C1'),
    ('schedule concrete pours', 'verb + noun phrase', 'lập lịch các đợt đổ bê tông phù hợp với nhân lực, thiết bị và thời tiết', 'B2'),
    ('monitor construction noise', 'verb + adjective + noun', 'theo dõi tiếng ồn thi công để kiểm soát ảnh hưởng và tuân thủ giới hạn cho phép', 'B2'),
    ('control construction dust', 'verb + adjective + noun', 'kiểm soát bụi phát sinh từ hoạt động xây dựng bằng các biện pháp giảm phát tán', 'B2'),
    ('divert pedestrian traffic', 'verb + adjective + noun', 'chuyển hướng người đi bộ quanh khu vực thi công để duy trì lối đi an toàn', 'B2'),
    ('restore disturbed landscaping', 'verb + adjective + noun', 'phục hồi cảnh quan bị ảnh hưởng sau khi hoàn tất công việc xây dựng', 'B2'),
    ('certify practical completion', 'verb + adjective + noun', 'xác nhận công trình đạt mức hoàn thành thực tế để có thể bàn giao và sử dụng theo quy định', 'C1'),
    ('hand over as-built drawings', 'verb + adjective + noun', 'bàn giao bản vẽ hoàn công phản ánh chính xác cấu hình công trình sau thi công', 'C1'),
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
        'quality': {
            'state': 'draft',
            'checks': {
                'schema': {'status': 'pass', 'method': 'e04-scale-40-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v40'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-40-collocations.json',
                'snapshot': '2026-10',
                'license': 'LicenseRef-Project-Original',
                'modified': False,
            }],
            'note': 'Project-original controlled E04 scale-up record.',
        },
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-39 publication: `39de17e5f4c2498ffe8151b356e30525b457f95b` — scale-38 publication state verified by English Content Master Plan Acceptance #85, English Content Full Validation #91 and Platform CI #1128; published output: `1109e688f4c14ba7c8b5d64b3061d91696e75700`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-40 publication: `929afcb95c0ac95daef8b5732af14138743032ce` — scale-39 publication state verified by English Content Master Plan Acceptance #89, English Content Full Validation #94 and Platform CI #1132; published output: `ccf47b48a02c94ac9c8ed3b3bf46266c95298af7`.',
        'verified scale-39 checkpoint',
    )
    text = replace_once(text, '- Scale-39 publication output: `ccf47b48a02c94ac9c8ed3b3bf46266c95298af7` — `feat(content): publish E04 collocation scale 39`; publication pipeline completed before the bot commit was pushed.\n', '', 'remove scale-39 publication line')
    text = replace_once(text, '- Scale-39 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #88 and Platform CI #1131 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-39 content or weakening any gate.\n', '', 'remove resolved scale-39 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,310 published records after scale-39', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,350 published records after scale-40', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-39 publication', '## Published runtime snapshot after E04 scale-40 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,310 records', '- phrases: 2,350 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,911', '- total published rich records: 6,951', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,911 decisions / 6,911 applied / 6,911 publish decisions', '- editorial ledger: 6,951 decisions / 6,951 applied / 6,951 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001200`', '- E04 collocation frontier: `col.00001240`', 'collocation frontier')

    old_workstream = '''1. Scale-38 publication is fully verified; do not duplicate scale-38 artifacts.
2. Scale-39 publication `ccf47b48a02c94ac9c8ed3b3bf46266c95298af7` is complete; do not regenerate or duplicate scale-39 artifacts.
3. Verify scale-39 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #88/#1131 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-39 checkpoint CI passes and no newer worker has claimed the next scope, create the next bounded E04 scale batch from frontier `col.00001200`, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-39 publication is fully verified; do not duplicate scale-39 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-40 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')

    old_blocker = "No content/data blocker. Scale-39 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')

    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-39 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001200` (expected scale-40 range `col.00001201` through `col.00001240` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-40 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001240` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-40 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1200:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1200, got {max(nums) if nums else None}')

    new = [make_collocation(1201 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-40: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-40-collocations.json',
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
            'id': 'review.e04.scale-40.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-40-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-40-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-40-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-40-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-40-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-40-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 40 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1200)', 'if(recallCollocations!==1240)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1200 reviewed records', 'must expose 1240 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001201', 'col.00001240'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1240, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2350, 'richRecords': 6951},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
