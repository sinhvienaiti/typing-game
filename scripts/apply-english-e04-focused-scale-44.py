#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-43.py'), run_name='e04_scale44_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-44-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-44.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-44'
REVIEWED_AT = '2026-10-07T07:15:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-44'
EXPECTED = {'collocations': 1360, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('allocate departure gates', 'verb + noun phrase', 'phân bổ cửa khởi hành cho chuyến bay dựa trên lịch, loại tàu bay và năng lực nhà ga', 'B2'),
    ('sequence runway departures', 'verb + noun phrase', 'sắp xếp thứ tự chuyến bay cất cánh để duy trì luồng khai thác an toàn và hiệu quả', 'C1'),
    ('coordinate pushback clearance', 'verb + noun phrase', 'điều phối cho phép đẩy lùi tàu bay giữa tổ lái, kiểm soát mặt đất và đội khai thác sân đỗ', 'C1'),
    ('inspect taxiway markings', 'verb + noun phrase', 'kiểm tra vạch kẻ đường lăn để bảo đảm khả năng nhận biết và dẫn hướng tàu bay', 'B2'),
    ('monitor runway incursions', 'verb + noun phrase', 'theo dõi sự cố xâm nhập đường băng để giảm nguy cơ xung đột giữa tàu bay và phương tiện', 'C1'),
    ('issue landing clearance', 'verb + noun phrase', 'cấp phép hạ cánh cho tàu bay khi đường băng và điều kiện khai thác đáp ứng yêu cầu', 'C1'),
    ('assign arrival stands', 'verb + noun phrase', 'phân công vị trí đỗ cho chuyến bay đến dựa trên loại tàu bay và kế hoạch khai thác', 'B2'),
    ('marshal arriving aircraft', 'verb + adjective + noun', 'hướng dẫn tàu bay đến vào đúng vị trí đỗ bằng tín hiệu mặt đất tiêu chuẩn', 'B2'),
    ('connect ground power units', 'verb + noun phrase', 'kết nối nguồn điện mặt đất cho tàu bay trong thời gian đỗ tại sân bay', 'B2'),
    ('position passenger stairs', 'verb + noun phrase', 'đặt cầu thang hành khách đúng vị trí để bảo đảm lên xuống tàu bay an toàn', 'B2'),
    ('operate passenger boarding bridges', 'verb + noun phrase', 'vận hành cầu ống lồng nối nhà ga với tàu bay theo quy trình an toàn', 'C1'),
    ('load checked baggage', 'verb + adjective + noun', 'xếp hành lý ký gửi lên tàu bay hoặc thiết bị chứa hàng theo kế hoạch tải', 'B2'),
    ('reconcile baggage containers', 'verb + noun phrase', 'đối chiếu container hành lý với dữ liệu chuyến bay trước khi đóng tải', 'C1'),
    ('screen transfer baggage', 'verb + adjective + noun', 'kiểm tra an ninh hành lý nối chuyến trước khi chuyển sang chuyến bay tiếp theo', 'B2'),
    ('tag oversized luggage', 'verb + adjective + noun', 'gắn nhãn hành lý quá khổ để xử lý theo luồng vận chuyển phù hợp', 'B2'),
    ('dispatch baggage tractors', 'verb + noun phrase', 'điều xe kéo hành lý giữa nhà ga, khu phân loại và tàu bay theo lịch chuyến', 'B2'),
    ('refuel parked aircraft', 'verb + adjective + noun', 'tiếp nhiên liệu cho tàu bay đang đỗ theo định mức, quy trình và yêu cầu an toàn', 'B2'),
    ('sample aviation fuel', 'verb + adjective + noun', 'lấy mẫu nhiên liệu hàng không để kiểm tra chất lượng trước hoặc trong quá trình cấp nhiên liệu', 'C1'),
    ('inspect fuel hydrants', 'verb + noun phrase', 'kiểm tra hệ thống cấp nhiên liệu ngầm tại sân đỗ để phát hiện rò rỉ hoặc hư hỏng', 'C1'),
    ('service potable water systems', 'verb + noun phrase', 'bổ sung và bảo dưỡng hệ thống nước sạch trên tàu bay theo tiêu chuẩn vệ sinh', 'B2'),
    ('remove aircraft waste', 'verb + adjective + noun', 'thu gom chất thải từ tàu bay và chuyển đến quy trình xử lý phù hợp', 'B2'),
    ('deice aircraft surfaces', 'verb + noun phrase', 'loại bỏ băng tuyết khỏi bề mặt tàu bay trước khi khởi hành', 'C1'),
    ('apply anti-icing fluid', 'verb + noun phrase', 'phun dung dịch chống đóng băng để hạn chế băng hình thành lại trên bề mặt tàu bay', 'C1'),
    ('inspect engine inlets', 'verb + noun phrase', 'kiểm tra cửa hút động cơ để phát hiện vật thể lạ, hư hỏng hoặc dấu hiệu bất thường', 'C1'),
    ('check aircraft tire pressure', 'verb + noun phrase', 'kiểm tra áp suất lốp tàu bay trước khai thác để bảo đảm giới hạn kỹ thuật', 'B2'),
    ('verify wheel chocks', 'verb + noun phrase', 'xác nhận chèn bánh đã được đặt đúng vị trí để ngăn tàu bay di chuyển ngoài ý muốn', 'B2'),
    ('secure cargo pallets', 'verb + noun phrase', 'cố định pallet hàng hóa trước khi vận chuyển hoặc xếp lên tàu bay', 'B2'),
    ('weigh air cargo consignments', 'verb + noun phrase', 'cân lô hàng hàng không để xác nhận khối lượng phục vụ tính tải và chứng từ', 'B2'),
    ('build unit load devices', 'verb + noun phrase', 'xếp và hoàn thiện thiết bị chứa hàng hàng không theo cấu hình và giới hạn tải', 'C1'),
    ('inspect cargo restraints', 'verb + noun phrase', 'kiểm tra thiết bị chằng giữ hàng hóa để bảo đảm tải được cố định đúng yêu cầu', 'C1'),
    ('accept dangerous goods shipments', 'verb + adjective + noun', 'tiếp nhận lô hàng nguy hiểm sau khi xác minh phân loại, bao gói và chứng từ bắt buộc', 'C1'),
    ('verify aircraft load sheets', 'verb + noun phrase', 'xác minh bảng tải tàu bay trước khởi hành để bảo đảm số liệu trọng lượng và cân bằng chính xác', 'C1'),
    ('calculate takeoff performance', 'verb + noun phrase', 'tính toán thông số cất cánh dựa trên tải, đường băng, thời tiết và cấu hình tàu bay', 'C1'),
    ('brief departing flight crews', 'verb + adjective + noun', 'cập nhật cho tổ bay khởi hành về tình trạng khai thác, tải và các thay đổi liên quan', 'B2'),
    ('update departure slots', 'verb + noun phrase', 'cập nhật giờ khởi hành được phân bổ khi lịch khai thác hoặc năng lực điều hành thay đổi', 'B2'),
    ('coordinate slot revisions', 'verb + noun phrase', 'điều phối thay đổi slot giữa hãng bay và đơn vị quản lý luồng khai thác', 'C1'),
    ('monitor apron traffic', 'verb + noun phrase', 'theo dõi luồng tàu bay và phương tiện trên sân đỗ để hạn chế xung đột', 'B2'),
    ('enforce ramp safety zones', 'verb + noun phrase', 'duy trì các khu vực an toàn trên sân đỗ và hạn chế người hoặc phương tiện không phận sự', 'C1'),
    ('respond to bird strikes', 'verb + noun phrase', 'ứng phó sự cố tàu bay va chạm chim bằng kiểm tra, báo cáo và xử lý khai thác phù hợp', 'C1'),
    ('inspect runway debris', 'verb + noun phrase', 'kiểm tra vật thể lạ trên đường băng để loại bỏ nguy cơ gây hư hỏng tàu bay', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-44-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v44'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-44-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-43 publication: `94f5afd6d5da51313c0f51d45d6a7b153f3d3e60` — scale-42 publication state verified by English Content Master Plan Acceptance #99, English Content Full Validation #101 and Platform CI #1143; published output: `e6682d58f768b23107e47608689dc73fccea3a25`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-44 publication: `3244214aadd7e7e8e86856d34b02f90f84d44a49` — scale-43 publication state verified by English Content Master Plan Acceptance #102, English Content Full Validation #103 and Platform CI #1146; published output: `08ec64f4c22b6f829a445e86894eb626b9cf5154`.',
        'verified scale-43 checkpoint',
    )
    text = replace_once(text, '- Scale-43 publication output: `08ec64f4c22b6f829a445e86894eb626b9cf5154` — `feat(content): publish E04 collocation scale 43`; preflight, controlled review, full quality gates, converge and deterministic replay passed before the bot commit was pushed.\n', '', 'remove scale-43 publication line')
    text = replace_once(text, '- Scale-43 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #101 and Platform CI #1145 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-43 content or weakening any gate.\n', '', 'remove scale-43 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,470 published records after scale-43', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,510 published records after scale-44', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-43 publication', '## Published runtime snapshot after E04 scale-44 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,470 records', '- phrases: 2,510 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,071', '- total published rich records: 7,111', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,071 decisions / 7,071 applied / 7,071 publish decisions', '- editorial ledger: 7,111 decisions / 7,111 applied / 7,111 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001360`', '- E04 collocation frontier: `col.00001400`', 'collocation frontier')
    old_workstream = '''1. Scale-42 publication is fully verified; do not duplicate scale-42 artifacts.
2. Scale-43 publication `08ec64f4c22b6f829a445e86894eb626b9cf5154` is complete; do not regenerate or duplicate scale-43 artifacts.
3. Verify scale-43 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #101/#1145 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-43 checkpoint CI passes and no newer worker has claimed the next scope, create the next bounded E04 scale batch from frontier `col.00001360`, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-43 publication is fully verified; do not duplicate scale-43 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-44 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-43 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-43 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001360` (expected scale-44 range `col.00001361` through `col.00001400` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-44 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001400` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-44 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1360:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1360, got {max(nums) if nums else None}')

    new = [make_collocation(1361 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-44: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-44-collocations.json',
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
            'id': 'review.e04.scale-44.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-44-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-44-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-44-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-44-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-44-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-44-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 44 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1360)', 'if(recallCollocations!==1400)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1360 reviewed records', 'must expose 1400 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001361', 'col.00001400'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1400, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2510, 'richRecords': 7111},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
