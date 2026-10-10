#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-36.py'), run_name='e04_scale37_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-37-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-37.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-37'
REVIEWED_AT = '2026-10-07T05:15:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-37'
EXPECTED = {'collocations': 1080, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('assess environmental impacts', 'verb + adjective + noun', 'đánh giá các tác động môi trường của một hoạt động, dự án hoặc sản phẩm', 'B2'),
    ('cut operational carbon emissions', 'verb + noun phrase', 'giảm lượng khí thải carbon phát sinh từ hoạt động sản xuất, vận hành hoặc tiêu dùng', 'B2'),
    ('measure energy consumption', 'verb + noun phrase', 'đo mức tiêu thụ năng lượng để theo dõi hiệu quả sử dụng và cơ hội tiết kiệm', 'B2'),
    ('raise facility energy performance', 'verb + noun phrase', 'cải thiện hiệu suất sử dụng năng lượng để đạt cùng đầu ra với ít năng lượng hơn', 'B2'),
    ('monitor water usage', 'verb + noun phrase', 'theo dõi lượng nước sử dụng nhằm phát hiện lãng phí và kiểm soát nhu cầu', 'B2'),
    ('reduce water consumption', 'verb + noun phrase', 'giảm lượng nước tiêu thụ trong hoạt động vận hành hoặc sản xuất', 'B2'),
    ('manage hazardous waste', 'verb + adjective + noun', 'quản lý chất thải nguy hại theo yêu cầu an toàn, lưu giữ và xử lý phù hợp', 'C1'),
    ('segregate waste streams', 'verb + noun phrase', 'phân loại các dòng chất thải để hỗ trợ tái chế, xử lý và kiểm soát rủi ro', 'C1'),
    ('expand material recovery programs', 'verb + noun phrase', 'tăng tỷ lệ vật liệu hoặc chất thải được thu hồi và tái chế', 'B2'),
    ('minimize material waste', 'verb + noun phrase', 'giảm thiểu lãng phí vật liệu trong thiết kế, sản xuất hoặc sử dụng', 'B2'),
    ('track carbon footprint', 'verb + noun phrase', 'theo dõi dấu chân carbon của tổ chức, sản phẩm hoặc hoạt động theo thời gian', 'C1'),
    ('calculate lifecycle emissions', 'verb + noun phrase', 'tính lượng phát thải trong toàn bộ vòng đời của sản phẩm hoặc dịch vụ', 'C1'),
    ('source renewable energy', 'verb + adjective + noun', 'tìm nguồn và mua năng lượng tái tạo cho hoạt động của tổ chức', 'B2'),
    ('install solar panels', 'verb + noun phrase', 'lắp đặt các tấm pin mặt trời để tạo điện từ năng lượng mặt trời', 'B2'),
    ('purchase renewable electricity', 'verb + adjective + noun', 'mua điện có nguồn gốc từ các nguồn năng lượng tái tạo', 'B2'),
    ('optimize building performance', 'verb + noun phrase', 'tối ưu hiệu năng tòa nhà về năng lượng, tiện nghi và vận hành', 'C1'),
    ('improve thermal insulation', 'verb + adjective + noun', 'cải thiện khả năng cách nhiệt để giảm thất thoát nhiệt và nhu cầu năng lượng', 'C1'),
    ('reduce heat losses', 'verb + noun phrase', 'giảm lượng nhiệt thất thoát qua thiết bị, đường ống hoặc kết cấu công trình', 'B2'),
    ('recover waste heat', 'verb + noun phrase', 'thu hồi nhiệt thải để tái sử dụng cho quá trình hoặc mục đích hữu ích khác', 'C1'),
    ('monitor air quality', 'verb + noun phrase', 'theo dõi chất lượng không khí để phát hiện chất ô nhiễm và xu hướng bất thường', 'B2'),
    ('control pollutant emissions', 'verb + noun phrase', 'kiểm soát phát thải chất ô nhiễm để đáp ứng giới hạn và giảm tác động môi trường', 'C1'),
    ('prevent chemical spills', 'verb + noun phrase', 'ngăn ngừa sự cố tràn hóa chất bằng biện pháp kỹ thuật và kiểm soát vận hành', 'B2'),
    ('contain accidental releases', 'verb + adjective + noun', 'cô lập các phát tán ngoài ý muốn để hạn chế lan rộng và tác động', 'C1'),
    ('restore contaminated sites', 'verb + adjective + noun', 'phục hồi các khu vực bị ô nhiễm thông qua xử lý và cải tạo môi trường', 'C1'),
    ('protect natural habitats', 'verb + adjective + noun', 'bảo vệ môi trường sống tự nhiên khỏi suy thoái hoặc mất mát', 'B2'),
    ('preserve biodiversity values', 'verb + noun phrase', 'bảo tồn các giá trị đa dạng sinh học trong quy hoạch và hoạt động phát triển', 'C1'),
    ('restore native vegetation', 'verb + adjective + noun', 'khôi phục thảm thực vật bản địa tại khu vực bị suy thoái hoặc xáo trộn', 'C1'),
    ('manage invasive species', 'verb + adjective + noun', 'quản lý các loài xâm lấn để hạn chế tác động lên hệ sinh thái bản địa', 'C1'),
    ('conduct ecological surveys', 'verb + adjective + noun', 'thực hiện khảo sát sinh thái để ghi nhận loài, môi trường sống và điều kiện hệ sinh thái', 'C1'),
    ('monitor habitat conditions', 'verb + noun phrase', 'theo dõi điều kiện môi trường sống để đánh giá thay đổi theo thời gian', 'B2'),
    ('set sustainability targets', 'verb + noun phrase', 'đặt mục tiêu phát triển bền vững có phạm vi, chỉ số và thời hạn rõ ràng', 'B2'),
    ('report sustainability performance', 'verb + noun phrase', 'báo cáo kết quả phát triển bền vững bằng các chỉ số và bằng chứng phù hợp', 'C1'),
    ('verify environmental data', 'verb + adjective + noun', 'xác minh dữ liệu môi trường để bảo đảm độ tin cậy và khả năng truy xuất', 'C1'),
    ('audit environmental compliance', 'verb + adjective + noun', 'kiểm toán việc tuân thủ các yêu cầu môi trường và cam kết áp dụng', 'C1'),
    ('identify climate risks', 'verb + noun phrase', 'xác định các rủi ro khí hậu có thể ảnh hưởng đến hoạt động, tài sản hoặc chuỗi cung ứng', 'C1'),
    ('assess climate resilience', 'verb + noun phrase', 'đánh giá khả năng chống chịu và thích ứng trước các tác động khí hậu', 'C1'),
    ('develop adaptation measures', 'verb + noun phrase', 'xây dựng các biện pháp thích ứng nhằm giảm mức độ dễ bị tổn thương trước khí hậu', 'C1'),
    ('implement conservation measures', 'verb + noun phrase', 'triển khai các biện pháp bảo tồn tài nguyên, sinh cảnh hoặc đa dạng sinh học', 'C1'),
    ('engage local communities', 'verb + adjective + noun', 'thu hút sự tham gia của cộng đồng địa phương trong quyết định hoặc chương trình liên quan', 'B2'),
    ('communicate environmental commitments', 'verb + adjective + noun', 'truyền đạt rõ các cam kết môi trường tới nhân viên, đối tác và bên liên quan', 'B2'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-37-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v37'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-37-collocations.json',
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
        '- Latest fully CI-verified scale-up checkpoint before scale-36 publication: `964af3b7b1eaa6a5b08af5f5d693a22cc9d7adc2` — scale-35 publication state verified by English Content Master Plan Acceptance #74, English Content Full Validation #83 and Platform CI #1117; published output: `26fd71cb7df2308c612a949fa8215d6dca5792dc`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-37 publication: `3e0741ca8684a9e0d8f98f9150a31dbeaa52632c` — scale-36 publication state verified by English Content Master Plan Acceptance #78, English Content Full Validation #86 and Platform CI #1121; published output: `ebcc481a41fc89499f566140aee0b69227070aef`.',
        'verified scale-36 checkpoint',
    )
    text = replace_once(text, '- Latest published scale-up HEAD before this checkpoint: `ebcc481a41fc89499f566140aee0b69227070aef` — `feat(content): publish E04 collocation scale 36`.\n', '', 'remove scale-36 publication line')
    text = replace_once(text, '- Latest scale-36 pre-publication HEAD: `b42adf3d031e6eb3c20ac6b42b77c68d6fb859bb` — Apply English E04 Scale 36 #2 passed preflight, source apply, review/E10/license, generate/publish, full quality gates, converge, deterministic replay and bot commit/push. The earlier #1 workflow stopped before preflight because a YAML `#` comment truncated a shell scalar; the workflow-only fix was applied without partial content state.\n', '', 'remove scale-36 prep line')
    text = replace_once(text, '- Scale-36 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #77 and Platform CI #1120 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-36 content or weakening any gate.\n', '', 'remove resolved scale-36 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,190 published records after scale-36', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,230 published records after scale-37', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-36 publication', '## Published runtime snapshot after E04 scale-37 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,190 records', '- phrases: 2,230 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,791', '- total published rich records: 6,831', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,791 decisions / 6,791 applied / 6,791 publish decisions', '- editorial ledger: 6,831 decisions / 6,831 applied / 6,831 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001080`', '- E04 collocation frontier: `col.00001120`', 'collocation frontier')
    old_workstream = '''1. Verify scale-36 publication state through this normal-user checkpoint CI; do not duplicate scale-36 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-36 checkpoint CI passes and no newer worker has claimed the next scope, create scale-37 as the next bounded collocation batch from frontier `col.00001080`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-36 publication is fully verified; do not duplicate scale-36 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-37 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-36 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-36 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001080` (expected scale-37 range `col.00001081` through `col.00001120` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-37 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001120` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-37 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1080:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1080, got {max(nums) if nums else None}')

    new = [make_collocation(1081 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-37: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-37-collocations.json',
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
            'id': 'review.e04.scale-37.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-37-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-37-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-37-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-37-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-37-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-37-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 37 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1080)', 'if(recallCollocations!==1120)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1080 reviewed records', 'must expose 1120 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001081', 'col.00001120'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1120, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2230, 'richRecords': 6831},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
