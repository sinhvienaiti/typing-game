#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-47.py'), run_name='e04_scale48_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-48-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-48.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-48'
REVIEWED_AT = '2026-10-07T08:55:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-48'
EXPECTED = {'collocations': 1520, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('sample raw water', 'verb + adjective + noun', 'lấy mẫu nước thô tại điểm quy định để đánh giá chất lượng nguồn nước trước xử lý', 'B2'),
    ('measure water turbidity', 'verb + noun phrase', 'đo độ đục của nước để theo dõi lượng hạt lơ lửng và hiệu quả xử lý', 'B2'),
    ('adjust coagulant dosage', 'verb + noun phrase', 'điều chỉnh liều chất keo tụ để tối ưu quá trình kết tụ các hạt nhỏ trong nước', 'C1'),
    ('monitor floc formation', 'verb + noun phrase', 'theo dõi sự hình thành bông cặn để đánh giá điều kiện keo tụ và tạo bông', 'C1'),
    ('backwash filter beds', 'verb + noun phrase', 'rửa ngược lớp vật liệu lọc để loại bỏ cặn tích tụ và khôi phục khả năng lọc', 'C1'),
    ('disinfect treated water', 'verb + adjective + noun', 'khử trùng nước đã xử lý để giảm vi sinh vật gây bệnh trước khi cấp cho người dùng', 'B2'),
    ('maintain chlorine residual', 'verb + noun phrase', 'duy trì lượng clo dư phù hợp để bảo vệ chất lượng nước trong mạng lưới phân phối', 'C1'),
    ('calibrate pH probes', 'verb + noun phrase', 'hiệu chuẩn đầu dò pH để các phép đo độ axit hoặc kiềm của nước luôn chính xác', 'B2'),
    ('inspect dosing pumps', 'verb + noun phrase', 'kiểm tra bơm định lượng để bảo đảm hóa chất được cấp ổn định theo lưu lượng yêu cầu', 'B2'),
    ('clean intake screens', 'verb + noun phrase', 'làm sạch lưới chắn tại cửa lấy nước để loại bỏ rác và duy trì dòng chảy vào hệ thống', 'B2'),
    ('flush distribution mains', 'verb + noun phrase', 'xả rửa đường ống chính của mạng cấp nước để loại bỏ cặn và nước tù đọng', 'C1'),
    ('detect pipeline leaks', 'verb + noun phrase', 'phát hiện rò rỉ đường ống để giảm thất thoát nước và ngăn hư hỏng lan rộng', 'B2'),
    ('repair service connections', 'verb + noun phrase', 'sửa chữa các nhánh đấu nối dịch vụ để khôi phục cấp nước an toàn cho khách hàng', 'B2'),
    ('isolate damaged mains', 'verb + adjective + noun', 'cô lập đoạn ống chính bị hỏng để giới hạn mất nước và tạo điều kiện sửa chữa', 'B2'),
    ('restore network pressure', 'verb + noun phrase', 'khôi phục áp lực mạng lưới sau sửa chữa hoặc sự cố để cấp nước trở lại ổn định', 'B2'),
    ('collect compliance samples', 'verb + noun phrase', 'thu thập mẫu kiểm soát tuân thủ theo kế hoạch để chứng minh chất lượng nước đạt yêu cầu', 'C1'),
    ('test microbial indicators', 'verb + adjective + noun', 'kiểm tra các chỉ thị vi sinh để đánh giá nguy cơ nhiễm bẩn sinh học trong nước', 'C1'),
    ('monitor reservoir levels', 'verb + noun phrase', 'theo dõi mực nước hồ chứa để điều phối nguồn cấp và duy trì dự trữ vận hành', 'B2'),
    ('balance network pressure', 'verb + noun phrase', 'cân bằng áp lực giữa các khu vực mạng lưới để hạn chế áp thấp, áp cao và thất thoát', 'C1'),
    ('inspect storage tanks', 'verb + noun phrase', 'kiểm tra bể chứa nước để phát hiện hư hỏng kết cấu, ăn mòn hoặc nguy cơ nhiễm bẩn', 'B2'),
    ('remove sediment buildup', 'verb + noun phrase', 'loại bỏ cặn tích tụ trong bể hoặc đường ống để duy trì dung tích và chất lượng nước', 'B2'),
    ('maintain aeration basins', 'verb + noun phrase', 'bảo trì bể sục khí để quá trình xử lý sinh học nước thải vận hành ổn định', 'C1'),
    ('control sludge age', 'verb + noun phrase', 'kiểm soát tuổi bùn để duy trì quần thể vi sinh phù hợp trong hệ thống bùn hoạt tính', 'C1'),
    ('return activated sludge', 'verb + adjective + noun', 'hoàn lưu bùn hoạt tính từ bể lắng về bể sục khí để duy trì nồng độ sinh khối cần thiết', 'C1'),
    ('waste excess sludge', 'verb + adjective + noun', 'xả bỏ lượng bùn dư để kiểm soát khối lượng chất rắn và tuổi bùn trong quá trình xử lý', 'C1'),
    ('monitor dissolved oxygen', 'verb + adjective + noun', 'theo dõi oxy hòa tan để điều chỉnh sục khí và hỗ trợ hoạt động của vi sinh vật hiếu khí', 'B2'),
    ('measure ammonia levels', 'verb + noun phrase', 'đo nồng độ amoni để đánh giá hiệu quả nitrification và chất lượng nước sau xử lý', 'B2'),
    ('optimize nutrient removal', 'verb + noun phrase', 'tối ưu loại bỏ nitơ và phospho để đáp ứng giới hạn xả thải và giảm phú dưỡng', 'C1'),
    ('dewater sewage sludge', 'verb + noun phrase', 'tách bớt nước khỏi bùn thải để giảm thể tích trước vận chuyển hoặc xử lý tiếp', 'C1'),
    ('digest organic solids', 'verb + adjective + noun', 'phân hủy chất rắn hữu cơ trong bùn để ổn định bùn và giảm lượng vật chất dễ phân hủy', 'C1'),
    ('capture biogas output', 'verb + noun phrase', 'thu hồi khí sinh học tạo ra trong quá trình phân hủy để sử dụng hoặc xử lý an toàn', 'C1'),
    ('inspect clarifier mechanisms', 'verb + noun phrase', 'kiểm tra cơ cấu của bể lắng để bảo đảm gạt bùn và thu nước hoạt động đúng', 'C1'),
    ('clean diffuser membranes', 'verb + noun phrase', 'làm sạch màng phân phối khí để duy trì hiệu suất truyền oxy trong bể sục khí', 'C1'),
    ('prevent sewer overflows', 'verb + noun phrase', 'ngăn tràn nước thải khỏi hệ thống cống bằng vận hành, bảo trì và kiểm soát lưu lượng phù hợp', 'B2'),
    ('inspect lift stations', 'verb + noun phrase', 'kiểm tra trạm bơm nâng nước thải để phát hiện hỏng bơm, tắc nghẽn hoặc lỗi điều khiển', 'B2'),
    ('test backup generators', 'verb + noun phrase', 'kiểm tra máy phát dự phòng để bảo đảm trạm xử lý vẫn vận hành khi mất điện lưới', 'B2'),
    ('clear blocked sewers', 'verb + adjective + noun', 'thông các tuyến cống bị tắc để khôi phục dòng chảy và giảm nguy cơ tràn nước thải', 'B2'),
    ('trace infiltration sources', 'verb + noun phrase', 'xác định nguồn nước ngầm xâm nhập vào hệ thống cống để giảm lưu lượng không mong muốn', 'C1'),
    ('rehabilitate aging pipes', 'verb + adjective + noun', 'phục hồi các đường ống xuống cấp để kéo dài tuổi thọ và giảm sự cố hoặc rò rỉ', 'C1'),
    ('document treatment deviations', 'verb + noun phrase', 'ghi chép các sai lệch trong quá trình xử lý để phục vụ điều tra, khắc phục và báo cáo tuân thủ', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-48-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v48'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-48-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-47 publication: `2acfa2b7b3eff63b4bb1c7931581ea3129910b5e` — scale-46 publication state verified by English Content Master Plan Acceptance #112, English Content Full Validation #110 and Platform CI #1161; published output: `0b469babc616995ec11ea97994b6bfc7528f527a`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-48 publication: `64d77904e3361da2bd51a356c33cb992f04b41db` — scale-47 publication state verified by English Content Master Plan Acceptance #115, English Content Full Validation #112 and Platform CI #1166; published output: `113edd521e847f9b3623d7af08045bc1ff65da26`.',
        'verified scale-47 checkpoint',
    )
    text = replace_once(text, '- Scale-47 publication output: `113edd521e847f9b3623d7af08045bc1ff65da26` — `feat(content): publish E04 collocation scale 47`; Apply English E04 Scale 47 #1 passed preflight, controlled review, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-47 publication line')
    text = replace_once(text, '- Scale-47 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #114 and Platform CI #1163 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-47 content or weakening any gate.\n', '', 'remove scale-47 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,630 published records after scale-47', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,670 published records after scale-48', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-47 publication', '## Published runtime snapshot after E04 scale-48 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,630 records', '- phrases: 2,670 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,231', '- total published rich records: 7,271', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,231 decisions / 7,231 applied / 7,231 publish decisions', '- editorial ledger: 7,271 decisions / 7,271 applied / 7,271 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001520`', '- E04 collocation frontier: `col.00001560`', 'collocation frontier')
    old_workstream = '''1. Scale-46 publication is fully verified; do not duplicate scale-46 artifacts.
2. Scale-47 publication `113edd521e847f9b3623d7af08045bc1ff65da26` is complete; do not regenerate or duplicate scale-47 artifacts.
3. Verify scale-47 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #114/#1163 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-47 checkpoint CI passes and no newer worker has claimed the next scope, create scale-48 as the next bounded collocation batch from frontier `col.00001520`, expected IDs `col.00001521` through `col.00001560`, while preserving exact/near-dedupe threshold 0.86 and all E10/E11/E12 gates.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-47 publication is fully verified; do not duplicate scale-47 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-48 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-47 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-47 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001520` (expected scale-48 range `col.00001521` through `col.00001560` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-48 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001560` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-48 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1520:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1520, got {max(nums) if nums else None}')

    new = [make_collocation(1521 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-48: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-48-collocations.json',
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
            'id': 'review.e04.scale-48.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-48-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-48-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-48-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-48-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-48-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-48-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 48 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1520)', 'if(recallCollocations!==1560)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1520 reviewed records', 'must expose 1560 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001521', 'col.00001560'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1560, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2670, 'richRecords': 7271},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
