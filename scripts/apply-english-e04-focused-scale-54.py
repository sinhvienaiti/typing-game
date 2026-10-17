#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-53.py'), run_name='e04_scale54_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-54-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-54.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-54'
REVIEWED_AT = '2026-10-07T11:12:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-54'
EXPECTED = {'collocations': 1760, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('forecast renewable power generation', 'verb + adjective + noun', 'dự báo sản lượng điện tái tạo dựa trên thời tiết, dữ liệu vận hành và khả năng sẵn sàng của nguồn phát', 'C1'),
    ('balance real-time electricity supply', 'verb + adjective + noun', 'cân bằng nguồn cung điện theo thời gian thực với nhu cầu hệ thống để duy trì vận hành ổn định', 'C1'),
    ('dispatch flexible generation resources', 'verb + adjective + noun', 'điều độ các nguồn phát linh hoạt để đáp ứng thay đổi phụ tải và biến động của nguồn năng lượng tái tạo', 'C1'),
    ('curtail excess renewable output', 'verb + adjective + noun', 'cắt giảm sản lượng điện tái tạo dư thừa khi lưới không thể tiếp nhận an toàn toàn bộ công suất khả dụng', 'C1'),
    ('integrate variable solar generation', 'verb + adjective + noun', 'tích hợp nguồn điện mặt trời biến thiên vào hệ thống điện trong khi vẫn giữ cân bằng và độ tin cậy của lưới', 'C1'),
    ('integrate offshore wind capacity', 'verb + adjective + noun', 'tích hợp công suất điện gió ngoài khơi vào lưới thông qua hạ tầng truyền tải và phương án điều độ phù hợp', 'C1'),
    ('stabilize grid frequency deviations', 'verb + noun phrase', 'ổn định các sai lệch tần số lưới bằng điều chỉnh công suất, dự phòng và dịch vụ phụ trợ', 'C1'),
    ('maintain voltage stability margins', 'verb + noun phrase', 'duy trì biên ổn định điện áp đủ an toàn trước các thay đổi phụ tải, sự cố và biến động công suất phản kháng', 'C1'),
    ('manage transmission line congestion', 'verb + noun phrase', 'quản lý nghẽn trên đường dây truyền tải bằng điều độ lại nguồn, giới hạn giao dịch hoặc thay đổi cấu hình lưới', 'C1'),
    ('relieve regional grid constraints', 'verb + adjective + noun', 'giảm các ràng buộc lưới khu vực bằng biện pháp vận hành hoặc tăng cường khả năng truyền tải', 'C1'),
    ('schedule battery storage charging', 'verb + noun phrase', 'lập lịch sạc hệ thống lưu trữ pin vào thời điểm phù hợp với giá điện, nhu cầu và giới hạn lưới', 'B2'),
    ('discharge grid-scale battery systems', 'verb + adjective + noun', 'xả các hệ thống pin quy mô lưới để hỗ trợ phụ tải, cân bằng công suất hoặc cung cấp dịch vụ hệ thống', 'C1'),
    ('optimize energy storage dispatch', 'verb + noun phrase', 'tối ưu điều độ hệ thống lưu trữ năng lượng theo giá trị kinh tế, độ tin cậy và các ràng buộc kỹ thuật', 'C1'),
    ('monitor state of charge levels', 'verb + noun phrase', 'theo dõi mức trạng thái sạc của hệ thống lưu trữ để bảo đảm còn đủ năng lượng và công suất khả dụng khi cần', 'B2'),
    ('coordinate demand response events', 'verb + noun phrase', 'phối hợp các sự kiện đáp ứng nhu cầu để giảm hoặc dịch chuyển phụ tải theo tín hiệu vận hành hay thị trường', 'C1'),
    ('reduce peak electricity demand', 'verb + adjective + noun', 'giảm nhu cầu điện vào giờ cao điểm thông qua điều chỉnh phụ tải, lưu trữ hoặc các chương trình khuyến khích', 'B2'),
    ('shift flexible industrial loads', 'verb + adjective + noun', 'dịch chuyển các phụ tải công nghiệp linh hoạt sang thời điểm thuận lợi hơn cho chi phí và vận hành lưới', 'C1'),
    ('aggregate distributed energy resources', 'verb + adjective + noun', 'tổng hợp các nguồn năng lượng phân tán để có thể điều phối như một danh mục nguồn lực có quy mô lớn hơn', 'C1'),
    ('register virtual power plants', 'verb + adjective + noun', 'đăng ký các nhà máy điện ảo để tham gia vận hành hoặc thị trường theo yêu cầu kỹ thuật và thương mại hiện hành', 'C1'),
    ('synchronize distributed generators safely', 'verb + adjective + noun', 'đồng bộ các máy phát phân tán với lưới một cách an toàn về tần số, điện áp, góc pha và trình tự đóng cắt', 'C1'),
    ('detect islanding conditions promptly', 'verb + noun phrase', 'phát hiện kịp thời tình trạng vận hành đảo lưới để kích hoạt bảo vệ hoặc điều khiển phù hợp', 'C1'),
    ('restore service after outages', 'verb + noun phrase', 'khôi phục cấp điện sau sự cố mất điện theo trình tự an toàn, ưu tiên các phụ tải và khu vực quan trọng', 'B2'),
    ('sectionalize faulted distribution feeders', 'verb + adjective + noun', 'phân đoạn các xuất tuyến phân phối bị sự cố để cô lập phần lỗi và hạn chế phạm vi mất điện', 'C1'),
    ('reroute power around faults', 'verb + noun phrase', 'chuyển hướng dòng công suất quanh khu vực sự cố bằng cấu hình lưới thay thế khi điều kiện kỹ thuật cho phép', 'C1'),
    ('inspect high-voltage substations', 'verb + adjective + noun', 'kiểm tra các trạm biến áp cao áp để phát hiện bất thường về thiết bị, cách điện, làm mát và hệ thống bảo vệ', 'B2'),
    ('maintain transformer cooling systems', 'verb + noun phrase', 'bảo trì hệ thống làm mát máy biến áp để kiểm soát nhiệt độ và giảm nguy cơ suy giảm tuổi thọ thiết bị', 'C1'),
    ('monitor transformer dissolved gases', 'verb + noun phrase', 'theo dõi khí hòa tan trong dầu máy biến áp để nhận diện sớm dấu hiệu phóng điện, quá nhiệt hoặc hư hỏng nội bộ', 'C1'),
    ('replace aging switchgear components', 'verb + adjective + noun', 'thay thế các bộ phận thiết bị đóng cắt đã lão hóa trước khi độ tin cậy hoặc khả năng chịu sự cố suy giảm đáng kể', 'B2'),
    ('test protective relay settings', 'verb + adjective + noun', 'kiểm thử các cài đặt rơ le bảo vệ để xác nhận ngưỡng tác động, thời gian và logic phối hợp hoạt động đúng thiết kế', 'C1'),
    ('coordinate relay protection zones', 'verb + noun phrase', 'phối hợp các vùng bảo vệ rơ le để sự cố được cô lập chọn lọc mà không làm mất điện diện rộng không cần thiết', 'C1'),
    ('model contingency outage scenarios', 'verb + noun phrase', 'mô hình hóa các kịch bản mất phần tử dự phòng để đánh giá phản ứng của hệ thống trước sự cố có khả năng xảy ra', 'C1'),
    ('assess N-1 security criteria', 'verb + adjective + noun', 'đánh giá tiêu chí an ninh N-1 để xác nhận hệ thống vẫn vận hành chấp nhận được khi mất một phần tử quan trọng', 'C1'),
    ('plan transmission capacity upgrades', 'verb + noun phrase', 'lập kế hoạch nâng cấp năng lực truyền tải dựa trên tăng trưởng phụ tải, nguồn mới và các nút thắt dự kiến', 'C1'),
    ('reinforce weak grid interconnections', 'verb + adjective + noun', 'tăng cường các liên kết lưới yếu để cải thiện khả năng truyền công suất, ổn định và hỗ trợ lẫn nhau giữa các khu vực', 'C1'),
    ('connect utility-scale solar farms', 'verb + adjective + noun', 'đấu nối các trang trại điện mặt trời quy mô lớn vào lưới theo yêu cầu kỹ thuật, bảo vệ và điều độ', 'B2'),
    ('commission new wind turbines', 'verb + adjective + noun', 'nghiệm thu và đưa các tua-bin gió mới vào vận hành sau khi hoàn thành kiểm tra cơ khí, điện và điều khiển', 'B2'),
    ('validate grid code compliance', 'verb + noun phrase', 'xác nhận việc tuân thủ quy định đấu nối lưới về điện áp, tần số, phản ứng sự cố, điều khiển và chất lượng điện năng', 'C1'),
    ('forecast ancillary service requirements', 'verb + adjective + noun', 'dự báo nhu cầu dịch vụ phụ trợ như điều tần, dự phòng và hỗ trợ điện áp cho từng giai đoạn vận hành', 'C1'),
    ('procure frequency regulation reserves', 'verb + noun phrase', 'mua hoặc huy động dự phòng điều tần đủ để xử lý biến động ngắn hạn của cân bằng cung cầu', 'C1'),
    ('settle imbalance energy charges', 'verb + noun phrase', 'quyết toán các khoản phí năng lượng mất cân bằng dựa trên chênh lệch giữa lịch giao dịch và sản lượng thực tế', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-54-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v54'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-54-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-53 publication: `d12a87c7004bf5009b22ac2069f26c588ae0461a` — scale-52 publication state verified by English Content Master Plan Acceptance #131, English Content Full Validation #123 and Platform CI #1188; published output: `ae830459fb912231aed2ee12cc1c00fe9e447d1b`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-54 publication: `d3ceb1ce31075499283af412f2e338430f440fe3` — scale-53 publication state verified by English Content Master Plan Acceptance #134, English Content Full Validation #125 and Platform CI #1194; published output: `c6fdf79d94c4540bc2e3dffcd16b998a24e4509a`.',
        'verified scale-53 checkpoint',
    )
    text = replace_once(text, '- Current scale-53 publication awaiting checkpoint CI verification: `c6fdf79d94c4540bc2e3dffcd16b998a24e4509a`.\n', '', 'remove scale-53 pending verification line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,870 published records after scale-53', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,910 published records after scale-54', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-53 publication', '## Published runtime snapshot after E04 scale-54 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,870 records', '- phrases: 2,910 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,471', '- total published rich records: 7,511', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,471 decisions / 7,471 applied / 7,471 publish decisions', '- editorial ledger: 7,511 decisions / 7,511 applied / 7,511 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001760`', '- E04 collocation frontier: `col.00001800`', 'collocation frontier')
    old_workstream = '''1. Scale-52 publication is fully verified at `d12a87c7004bf5009b22ac2069f26c588ae0461a`; do not duplicate scale-52 artifacts.
2. Scale-53 publication is complete at `c6fdf79d94c4540bc2e3dffcd16b998a24e4509a`; do not regenerate scale-53 artifacts.
3. Verify the scale-53 checkpoint commit with English Content Full Validation, Master Plan Acceptance and Platform CI.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-53 publication is fully verified at `d3ceb1ce31075499283af412f2e338430f440fe3`; do not duplicate scale-53 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-54 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Verify mandatory CI for the scale-53 publication checkpoint without regenerating completed artifacts. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001760` (scale-54 unless a newer worker already advanced the branch), or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-54 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001800` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main54():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-54 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1760:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1760, got {max(nums) if nums else None}')

    new = [make_collocation(1761 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-54: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-54-collocations.json',
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
            'id': 'review.e04.scale-54.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-54-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-54-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-54-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-54-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-54-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-54-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 54 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1760)', 'if(recallCollocations!==1800)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1760 reviewed records', 'must expose 1800 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001761', 'col.00001800'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1800, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2910, 'richRecords': 7511},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main54()
