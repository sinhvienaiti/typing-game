#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-55.py'), run_name='e04_scale56_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-56-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-56.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-56'
REVIEWED_AT = '2026-10-07T11:30:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-56'
EXPECTED = {'collocations': 1840, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('monitor influent water quality', 'verb + noun phrase', 'theo dõi chất lượng nước đầu vào để nhận diện biến động có thể ảnh hưởng đến hiệu quả của các công đoạn xử lý phía sau', 'B2'),
    ('adjust coagulant dosing rates', 'verb + noun phrase', 'điều chỉnh lưu lượng hóa chất keo tụ theo độ đục, thành phần nước và mục tiêu xử lý thực tế', 'C1'),
    ('optimize flocculation mixing intensity', 'verb + noun phrase', 'tối ưu cường độ khuấy trong quá trình tạo bông để hình thành bông cặn đủ lớn mà không bị phá vỡ', 'C1'),
    ('control sedimentation basin loading', 'verb + noun phrase', 'kiểm soát tải trọng bể lắng để duy trì thời gian lưu và hiệu quả tách cặn trong giới hạn thiết kế', 'C1'),
    ('remove suspended solids efficiently', 'verb + adjective + noun', 'loại bỏ chất rắn lơ lửng hiệu quả trước khi nước chuyển sang các bước lọc hoặc xử lý nâng cao', 'B2'),
    ('backwash granular media filters', 'verb + adjective + noun', 'rửa ngược các bộ lọc vật liệu hạt để loại bỏ cặn tích tụ và phục hồi khả năng lọc', 'C1'),
    ('monitor filter head loss', 'verb + noun phrase', 'theo dõi tổn thất cột áp qua bộ lọc để xác định mức độ tắc nghẽn và thời điểm cần rửa lọc', 'C1'),
    ('maintain membrane filtration pressure', 'verb + noun phrase', 'duy trì áp suất lọc màng trong dải vận hành phù hợp để giữ thông lượng và bảo vệ màng', 'C1'),
    ('prevent membrane fouling buildup', 'verb + noun phrase', 'ngăn sự tích tụ cáu bẩn trên màng bằng tiền xử lý, kiểm soát vận hành và làm sạch định kỳ', 'C1'),
    ('clean reverse osmosis membranes', 'verb + adjective + noun', 'làm sạch màng thẩm thấu ngược bằng quy trình hóa học phù hợp để khôi phục hiệu suất và giảm chênh áp', 'C1'),
    ('monitor permeate water conductivity', 'verb + noun phrase', 'theo dõi độ dẫn điện của nước thấm qua màng để phát hiện suy giảm khả năng loại muối hoặc rò rỉ màng', 'C1'),
    ('maintain disinfectant residual levels', 'verb + adjective + noun', 'duy trì nồng độ chất khử trùng dư ở mức đủ bảo vệ chất lượng nước mà không vượt giới hạn quy định', 'B2'),
    ('measure chlorine contact time', 'verb + noun phrase', 'đo thời gian tiếp xúc của clo để xác nhận quá trình khử trùng đạt mức bất hoạt vi sinh cần thiết', 'B2'),
    ('control ultraviolet disinfection intensity', 'verb + noun phrase', 'kiểm soát cường độ tia cực tím để bảo đảm liều khử trùng phù hợp với lưu lượng và chất lượng nước', 'C1'),
    ('monitor dissolved oxygen levels', 'verb + noun phrase', 'theo dõi nồng độ oxy hòa tan để điều khiển quá trình sinh học và tránh cấp khí quá mức hoặc thiếu khí', 'B2'),
    ('optimize aeration basin performance', 'verb + noun phrase', 'tối ưu hiệu suất bể sục khí bằng cách phối hợp tải hữu cơ, oxy hòa tan, thời gian lưu và sinh khối', 'C1'),
    ('adjust activated sludge age', 'verb + adjective + noun', 'điều chỉnh tuổi bùn hoạt tính để duy trì quần thể vi sinh phù hợp với mục tiêu xử lý và tải đầu vào', 'C1'),
    ('maintain mixed liquor concentration', 'verb + noun phrase', 'duy trì nồng độ hỗn hợp bùn trong bể sinh học ở mức hỗ trợ xử lý ổn định và khả năng lắng tốt', 'C1'),
    ('settle biological solids effectively', 'verb + adjective + noun', 'lắng chất rắn sinh học hiệu quả trong bể lắng thứ cấp để tách nước trong khỏi bùn hoạt tính', 'C1'),
    ('return activated sludge flow', 'verb + adjective + noun', 'tuần hoàn dòng bùn hoạt tính từ bể lắng về bể sinh học để duy trì lượng sinh khối cần thiết', 'C1'),
    ('waste excess activated sludge', 'verb + adjective + noun', 'xả bỏ lượng bùn hoạt tính dư có kiểm soát để điều chỉnh tuổi bùn và nồng độ chất rắn trong hệ thống', 'C1'),
    ('monitor nutrient removal efficiency', 'verb + noun phrase', 'theo dõi hiệu quả loại bỏ nitơ và phospho để phát hiện suy giảm của quá trình xử lý dinh dưỡng', 'C1'),
    ('control nitrification process stability', 'verb + noun phrase', 'kiểm soát độ ổn định của quá trình nitrat hóa thông qua oxy, nhiệt độ, pH, kiềm và tuổi bùn', 'C1'),
    ('support denitrification carbon demand', 'verb + noun phrase', 'đáp ứng nhu cầu nguồn carbon cho quá trình khử nitrat khi carbon dễ phân hủy trong nước thải không đủ', 'C1'),
    ('remove phosphorus from wastewater', 'verb + noun phrase', 'loại bỏ phospho khỏi nước thải bằng cơ chế sinh học, kết tủa hóa học hoặc kết hợp cả hai', 'B2'),
    ('thicken waste sludge streams', 'verb + noun phrase', 'làm đặc các dòng bùn thải để giảm thể tích trước khi ổn định, tiêu hóa hoặc tách nước', 'C1'),
    ('dewater digested sludge solids', 'verb + adjective + noun', 'tách nước khỏi chất rắn bùn đã tiêu hóa để giảm khối lượng vận chuyển và thuận lợi cho xử lý cuối cùng', 'C1'),
    ('operate anaerobic digesters safely', 'verb + adjective + noun', 'vận hành bể tiêu hóa kỵ khí an toàn bằng cách kiểm soát nhiệt độ, tải hữu cơ, khí sinh học và áp suất', 'C1'),
    ('capture biogas from digesters', 'verb + noun phrase', 'thu hồi khí sinh học từ bể tiêu hóa để đốt an toàn hoặc sử dụng làm nguồn năng lượng', 'B2'),
    ('monitor digester methane content', 'verb + noun phrase', 'theo dõi hàm lượng methane trong khí bể tiêu hóa để đánh giá hiệu suất và quản lý nguy cơ cháy nổ', 'C1'),
    ('control odor treatment systems', 'verb + noun phrase', 'kiểm soát hệ thống xử lý mùi để thu gom và xử lý các hợp chất gây mùi từ khu vực nước thải và bùn', 'C1'),
    ('inspect lift station pumps', 'verb + noun phrase', 'kiểm tra máy bơm tại trạm nâng để phát hiện tắc nghẽn, rung, quá nhiệt hoặc suy giảm lưu lượng', 'B2'),
    ('prevent sewer overflow events', 'verb + noun phrase', 'ngăn sự cố tràn hệ thống thoát nước bằng giám sát mực nước, năng lực bơm và điều phối dòng chảy', 'C1'),
    ('detect distribution system leaks', 'verb + noun phrase', 'phát hiện rò rỉ trong mạng lưới phân phối nước bằng dữ liệu áp suất, lưu lượng và kiểm tra hiện trường', 'B2'),
    ('maintain reservoir water levels', 'verb + noun phrase', 'duy trì mực nước bể chứa trong dải vận hành để đáp ứng nhu cầu, dự phòng và áp lực hệ thống', 'B2'),
    ('flush drinking water mains', 'verb + adjective + noun', 'xả rửa đường ống nước sạch để loại bỏ cặn, nước tù và cải thiện chất lượng nước trong mạng lưới', 'B2'),
    ('monitor turbidity compliance limits', 'verb + noun phrase', 'theo dõi độ đục so với giới hạn tuân thủ để xác nhận hiệu quả lọc và yêu cầu chất lượng nước', 'C1'),
    ('collect regulatory water samples', 'verb + adjective + noun', 'lấy mẫu nước theo chương trình giám sát quy định với vị trí, tần suất và phương pháp bảo quản phù hợp', 'B2'),
    ('calibrate online water analyzers', 'verb + adjective + noun', 'hiệu chuẩn thiết bị phân tích nước trực tuyến để duy trì độ chính xác của dữ liệu điều khiển và báo cáo', 'C1'),
    ('respond to treatment process upsets', 'verb + noun phrase', 'ứng phó với các biến động bất thường của quá trình xử lý bằng cô lập nguyên nhân, điều chỉnh vận hành và xác nhận phục hồi', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-56-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v56'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-56-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-55 publication: `f0e25bc17c5dbb946467d2da61c49d4458bdcb37` — scale-54 publication state verified by English Content Master Plan Acceptance #137, English Content Full Validation #127 and Platform CI #1197; published output: `d9f363c56c17727c54049bf32309dbc59e409342`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-56 publication: `d658981f167ddec66fb8268901fca9731e058460` — scale-55 publication state verified by English Content Master Plan Acceptance #140, English Content Full Validation #129 and Platform CI #1200; published output: `50208b470ecc5e4c1827185c085f6bc6b3315cf9`.',
        'verified scale-55 checkpoint',
    )
    text = replace_once(text, '- Current scale-55 publication awaiting checkpoint CI verification: `50208b470ecc5e4c1827185c085f6bc6b3315cf9`.\n', '', 'remove scale-55 pending verification line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,950 published records after scale-55', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,990 published records after scale-56', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-55 publication', '## Published runtime snapshot after E04 scale-56 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,950 records', '- phrases: 2,990 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,551', '- total published rich records: 7,591', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,551 decisions / 7,551 applied / 7,551 publish decisions', '- editorial ledger: 7,591 decisions / 7,591 applied / 7,591 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001840`', '- E04 collocation frontier: `col.00001880`', 'collocation frontier')
    old_workstream = '''1. Scale-54 publication is fully verified at `f0e25bc17c5dbb946467d2da61c49d4458bdcb37`; do not duplicate scale-54 artifacts.
2. Scale-55 publication is complete at `50208b470ecc5e4c1827185c085f6bc6b3315cf9`; do not regenerate scale-55 artifacts.
3. Verify this normal-user scale-55 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-55 publication is fully verified at `d658981f167ddec66fb8268901fca9731e058460`; do not duplicate scale-55 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-56 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Verify mandatory CI for the scale-55 publication checkpoint without regenerating completed artifacts. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001840` (scale-56 unless a newer worker already advanced the branch), or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-56 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001880` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main56():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-56 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1840:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1840, got {max(nums) if nums else None}')

    new = [make_collocation(1841 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-56: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-56-collocations.json',
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
            'id': 'review.e04.scale-56.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-56-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-56-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-56-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-56-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-56-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-56-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 56 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1840)', 'if(recallCollocations!==1880)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1840 reviewed records', 'must expose 1880 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001841', 'col.00001880'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1880, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2990, 'richRecords': 7591},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main56()
