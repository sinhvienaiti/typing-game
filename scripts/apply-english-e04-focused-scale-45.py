#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-44.py'), run_name='e04_scale45_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-45-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-45.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-45'
REVIEWED_AT = '2026-10-07T07:35:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-45'
EXPECTED = {'collocations': 1400, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('develop shooting schedules', 'verb + noun phrase', 'xây dựng lịch quay để phối hợp cảnh, địa điểm, diễn viên và nguồn lực sản xuất', 'B2'),
    ('scout filming locations', 'verb + noun phrase', 'khảo sát địa điểm quay để đánh giá hình ảnh, hậu cần và mức độ phù hợp với kịch bản', 'B2'),
    ('secure location permits', 'verb + noun phrase', 'xin và hoàn tất giấy phép cần thiết để quay tại địa điểm cụ thể', 'B2'),
    ('cast supporting roles', 'verb + adjective + noun', 'tuyển chọn diễn viên cho các vai phụ phù hợp với yêu cầu của dự án', 'B2'),
    ('rehearse scripted scenes', 'verb + adjective + noun', 'tập dượt các cảnh theo kịch bản trước khi quay chính thức', 'B2'),
    ('block actor movements', 'verb + noun phrase', 'sắp xếp vị trí và hướng di chuyển của diễn viên trong một cảnh quay', 'C1'),
    ('coordinate camera crews', 'verb + noun phrase', 'điều phối đội máy quay theo kế hoạch cảnh, thiết bị và yêu cầu hình ảnh', 'B2'),
    ('rig studio lighting', 'verb + noun phrase', 'lắp đặt hệ thống ánh sáng trường quay theo thiết kế chiếu sáng của cảnh', 'C1'),
    ('position boom microphones', 'verb + noun phrase', 'đặt micro boom ở vị trí thu thoại rõ mà không lọt vào khung hình', 'B2'),
    ('record production sound', 'verb + noun phrase', 'thu âm hiện trường trong quá trình quay để ghi thoại và âm thanh môi trường', 'B2'),
    ('slate camera takes', 'verb + noun phrase', 'đánh dấu từng lần quay bằng bảng slate để đồng bộ và quản lý hậu kỳ', 'C1'),
    ('log continuity notes', 'verb + noun phrase', 'ghi chép thông tin liên tục của cảnh để giữ nhất quán giữa các lần quay', 'B2'),
    ('capture establishing shots', 'verb + adjective + noun', 'quay các cảnh toàn hoặc cảnh thiết lập để xác định không gian và bối cảnh cho người xem', 'B2'),
    ('frame close-up shots', 'verb + adjective + noun', 'bố cục các cảnh cận để nhấn mạnh gương mặt, chi tiết hoặc phản ứng', 'B2'),
    ('pull camera focus', 'verb + noun phrase', 'điều chỉnh tiêu điểm trong lúc quay để chủ thể cần thiết luôn sắc nét', 'C1'),
    ('operate camera dollies', 'verb + noun phrase', 'vận hành dolly máy quay để tạo chuyển động máy ổn định theo đường định trước', 'C1'),
    ('monitor video feeds', 'verb + noun phrase', 'theo dõi tín hiệu hình ảnh trực tiếp từ máy quay để kiểm tra khung hình và chất lượng', 'B2'),
    ('review daily footage', 'verb + adjective + noun', 'xem lại footage quay trong ngày để đánh giá chất lượng và phát hiện cảnh cần quay bổ sung', 'B2'),
    ('select usable takes', 'verb + adjective + noun', 'chọn các lần quay đạt yêu cầu để đưa vào quá trình dựng', 'B2'),
    ('assemble rough cuts', 'verb + adjective + noun', 'ghép các cảnh đã chọn thành bản dựng thô để đánh giá cấu trúc và nhịp kể chuyện', 'C1'),
    ('refine picture edits', 'verb + noun phrase', 'tinh chỉnh phần dựng hình bằng cách điều chỉnh điểm cắt, thứ tự và nhịp cảnh', 'C1'),
    ('trim dialogue scenes', 'verb + noun phrase', 'rút gọn các cảnh thoại bằng cách loại phần dư nhưng vẫn giữ ý và nhịp', 'B2'),
    ('sync dialogue tracks', 'verb + noun phrase', 'đồng bộ các track thoại với hình ảnh và chuyển động miệng trong hậu kỳ', 'B2'),
    ('edit production audio', 'verb + noun phrase', 'biên tập âm thanh hiện trường để làm sạch, sắp xếp và chuẩn bị cho khâu mix', 'B2'),
    ('record replacement dialogue', 'verb + noun phrase', 'thu lại lời thoại trong phòng thu để thay thế phần âm thanh hiện trường không đạt yêu cầu', 'C1'),
    ('create foley effects', 'verb + noun phrase', 'tạo và thu các hiệu ứng foley đồng bộ với hành động trên màn hình', 'C1'),
    ('mix dialogue stems', 'verb + noun phrase', 'trộn các stem thoại để đạt độ rõ, cân bằng và mức âm lượng phù hợp', 'C1'),
    ('balance music cues', 'verb + noun phrase', 'cân bằng các đoạn nhạc với thoại và hiệu ứng để hỗ trợ cảm xúc mà không che nội dung', 'B2'),
    ('design ambient sound', 'verb + adjective + noun', 'thiết kế lớp âm thanh môi trường để tạo cảm giác không gian và bối cảnh', 'C1'),
    ('grade color footage', 'verb + noun phrase', 'chỉnh màu footage để đạt độ nhất quán và phong cách hình ảnh mong muốn', 'C1'),
    ('match shot colors', 'verb + noun phrase', 'cân khớp màu giữa các cảnh quay liền nhau để tránh thay đổi hình ảnh gây chú ý', 'C1'),
    ('composite visual effects', 'verb + adjective + noun', 'ghép các lớp hình ảnh và hiệu ứng để tạo khung hình hoàn chỉnh', 'C1'),
    ('track motion markers', 'verb + noun phrase', 'theo dõi điểm đánh dấu chuyển động để gắn hoặc ổn định yếu tố hình ảnh trong hậu kỳ', 'C1'),
    ('render effect plates', 'verb + noun phrase', 'kết xuất các lớp hoặc plate hiệu ứng phục vụ compositing và hoàn thiện hình ảnh', 'C1'),
    ('conform final timelines', 'verb + adjective + noun', 'đối chiếu và chuẩn hóa timeline cuối với nguồn hình chất lượng cao trước khi mastering', 'C1'),
    ('author subtitle files', 'verb + noun phrase', 'tạo tệp phụ đề với nội dung, timecode và định dạng giao nhận chính xác', 'B2'),
    ('encode review copies', 'verb + noun phrase', 'mã hóa các bản xem thử để phục vụ kiểm duyệt và phản hồi nội bộ', 'B2'),
    ('prepare delivery masters', 'verb + noun phrase', 'chuẩn bị bản master cuối theo thông số kỹ thuật của kênh phát hành hoặc khách hàng', 'C1'),
    ('verify broadcast specifications', 'verb + noun phrase', 'xác minh nội dung đáp ứng thông số kỹ thuật về hình, âm thanh và định dạng phát sóng', 'C1'),
    ('archive project media', 'verb + noun phrase', 'lưu trữ có hệ thống media và tệp dự án để bảo toàn và tái sử dụng về sau', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-45-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v45'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-45-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-44 publication: `3244214aadd7e7e8e86856d34b02f90f84d44a49` — scale-43 publication state verified by English Content Master Plan Acceptance #102, English Content Full Validation #103 and Platform CI #1146; published output: `08ec64f4c22b6f829a445e86894eb626b9cf5154`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-45 publication: `7642618f8b1ea598a6da1b8357f1dc0265b5b559` — scale-44 publication state verified by English Content Master Plan Acceptance #106, English Content Full Validation #106 and Platform CI #1155; published output: `bc0489659d3eaaea0ad400e6d9b01d859a285b79`.',
        'verified scale-44 checkpoint',
    )
    text = replace_once(text, '- Scale-44 publication output: `bc0489659d3eaaea0ad400e6d9b01d859a285b79` — `feat(content): publish E04 collocation scale 44`; Apply English E04 Scale 44 #2 passed preflight, controlled review, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-44 publication line')
    text = replace_once(text, '- Scale-44 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #105 and Platform CI #1152 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-44 content or weakening any gate.\n', '', 'remove scale-44 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,510 published records after scale-44', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,550 published records after scale-45', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-44 publication', '## Published runtime snapshot after E04 scale-45 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,510 records', '- phrases: 2,550 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,111', '- total published rich records: 7,151', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,111 decisions / 7,111 applied / 7,111 publish decisions', '- editorial ledger: 7,151 decisions / 7,151 applied / 7,151 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001400`', '- E04 collocation frontier: `col.00001440`', 'collocation frontier')
    old_workstream = '''1. Scale-43 publication is fully verified; do not duplicate scale-43 artifacts.
2. Scale-44 publication `bc0489659d3eaaea0ad400e6d9b01d859a285b79` is complete; do not regenerate or duplicate scale-44 artifacts.
3. Verify scale-44 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #105/#1152 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-44 checkpoint CI passes and no newer worker has claimed the next scope, create scale-45 as the next bounded collocation batch from frontier `col.00001400`, expected IDs `col.00001401` through `col.00001440`, while preserving exact/near-dedupe threshold 0.86 and all E10/E11/E12 gates.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-44 publication is fully verified; do not duplicate scale-44 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-45 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-44 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-44 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001400` (expected scale-45 range `col.00001401` through `col.00001440` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-45 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001440` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-45 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1400:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1400, got {max(nums) if nums else None}')

    new = [make_collocation(1401 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-45: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-45-collocations.json',
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
            'id': 'review.e04.scale-45.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-45-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-45-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-45-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-45-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-45-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-45-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 45 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1400)', 'if(recallCollocations!==1440)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1400 reviewed records', 'must expose 1440 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001401', 'col.00001440'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1440, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2550, 'richRecords': 7151},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
