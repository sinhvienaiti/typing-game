#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-49-impl.py'), run_name='e04_scale50_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-50-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-50.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-50'
REVIEWED_AT = '2026-10-07T09:40:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-50'
EXPECTED = {'collocations': 1600, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('assess supplier production capacity', 'verb + noun phrase', 'đánh giá năng lực sản xuất của nhà cung cấp để xác định khả năng đáp ứng sản lượng và lịch giao hàng', 'C1'),
    ('compare supplier bid packages', 'verb + noun phrase', 'so sánh các bộ hồ sơ chào thầu của nhà cung cấp theo giá, điều kiện, phạm vi và tiêu chí kỹ thuật', 'C1'),
    ('issue blanket purchase orders', 'verb + adjective + noun', 'phát hành đơn mua hàng khung cho nhu cầu lặp lại trong một khoảng thời gian hoặc hạn mức đã phê duyệt', 'C1'),
    ('approve emergency purchase requisitions', 'verb + adjective + noun', 'phê duyệt yêu cầu mua hàng khẩn cấp khi nhu cầu vận hành không thể chờ chu kỳ mua sắm thông thường', 'C1'),
    ('negotiate index-linked pricing', 'verb + adjective + noun', 'đàm phán cơ chế giá gắn với chỉ số tham chiếu để điều chỉnh giá minh bạch theo biến động thị trường', 'C1'),
    ('qualify alternate material suppliers', 'verb + adjective + noun', 'thẩm định nhà cung cấp vật liệu thay thế để giảm phụ thuộc và duy trì nguồn cung khi có gián đoạn', 'C1'),
    ('review supplier financial stability', 'verb + noun phrase', 'xem xét mức độ ổn định tài chính của nhà cung cấp trước khi giao hợp đồng hoặc tăng mức phụ thuộc', 'C1'),
    ('audit subcontractor performance', 'verb + noun phrase', 'kiểm tra hiệu quả thực hiện của nhà thầu phụ theo nghĩa vụ chất lượng, giao hàng và tuân thủ đã thống nhất', 'C1'),
    ('track component procurement lead times', 'verb + noun phrase', 'theo dõi thời gian dẫn mua sắm linh kiện để lập kế hoạch đặt hàng và giảm nguy cơ thiếu vật tư', 'C1'),
    ('forecast raw-material requirements', 'verb + adjective + noun', 'dự báo nhu cầu nguyên vật liệu dựa trên kế hoạch sản xuất, tồn kho và nhu cầu dự kiến', 'B2'),
    ('consolidate regional purchasing volumes', 'verb + adjective + noun', 'gộp khối lượng mua của nhiều khu vực để tăng sức mua và giảm chi phí giao dịch', 'C1'),
    ('set safety-stock reorder thresholds', 'verb + noun phrase', 'thiết lập ngưỡng đặt hàng lại có tính đến tồn kho an toàn để hạn chế rủi ro thiếu hàng', 'C1'),
    ('expedite shortage-critical orders', 'verb + adjective + noun', 'thúc đẩy các đơn hàng then chốt đang thiếu để rút ngắn thời gian giao và bảo vệ kế hoạch vận hành', 'C1'),
    ('confirm supplier capacity allocations', 'verb + noun phrase', 'xác nhận phần công suất nhà cung cấp dành cho doanh nghiệp trong giai đoạn nhu cầu cao hoặc nguồn cung hạn chế', 'C1'),
    ('resolve three-way-match exceptions', 'verb + adjective + noun', 'xử lý ngoại lệ đối chiếu ba bên giữa đơn mua hàng, biên nhận và hóa đơn trước khi thanh toán', 'C1'),
    ('match supplier invoices to receipts', 'verb + noun phrase', 'đối chiếu hóa đơn nhà cung cấp với chứng từ nhận hàng để xác minh số lượng và điều kiện thanh toán', 'B2'),
    ('verify contracted freight surcharges', 'verb + adjective + noun', 'xác minh các khoản phụ phí vận chuyển theo hợp đồng trước khi chấp nhận chi phí hoặc thanh toán', 'C1'),
    ('maintain quarterly supplier scorecards', 'verb + adjective + noun', 'duy trì bảng điểm nhà cung cấp theo quý để theo dõi chất lượng, giao hàng, chi phí và mức độ hợp tác', 'C1'),
    ('assess single-source supply risks', 'verb + adjective + noun', 'đánh giá rủi ro nguồn cung khi một vật tư hoặc dịch vụ phụ thuộc vào duy nhất một nhà cung cấp', 'C1'),
    ('diversify critical component sources', 'verb + adjective + noun', 'đa dạng hóa nguồn cung cho linh kiện quan trọng để giảm tác động của sự cố tại một nhà cung cấp', 'C1'),
    ('maintain approved supplier registers', 'verb + adjective + noun', 'duy trì danh sách nhà cung cấp được phê duyệt cùng trạng thái thẩm định và phạm vi hàng hóa hoặc dịch vụ', 'C1'),
    ('conduct supplier process audits', 'verb + noun phrase', 'thực hiện đánh giá quy trình tại nhà cung cấp để xác minh khả năng kiểm soát chất lượng và tuân thủ', 'C1'),
    ('request sealed competitive bids', 'verb + adjective + noun', 'yêu cầu hồ sơ chào giá cạnh tranh được niêm phong để hỗ trợ quy trình lựa chọn minh bạch và công bằng', 'C1'),
    ('evaluate technical tender submissions', 'verb + adjective + noun', 'đánh giá hồ sơ kỹ thuật trong gói thầu theo yêu cầu chức năng, chất lượng và tiêu chí bắt buộc', 'C1'),
    ('award multi-year supply contracts', 'verb + adjective + noun', 'trao hợp đồng cung ứng nhiều năm cho nhà cung cấp được lựa chọn theo quy trình phê duyệt', 'C1'),
    ('renew master supply agreements', 'verb + adjective + noun', 'gia hạn thỏa thuận cung ứng tổng thể khi điều khoản thương mại và hiệu suất vẫn đáp ứng yêu cầu', 'C1'),
    ('enforce contractual service levels', 'verb + adjective + noun', 'thực thi các mức dịch vụ đã cam kết trong hợp đồng và xử lý trường hợp không đạt chỉ tiêu', 'C1'),
    ('review milestone payment schedules', 'verb + noun phrase', 'xem xét lịch thanh toán theo mốc để bảo đảm khoản chi gắn với kết quả hoặc giai đoạn được chấp nhận', 'C1'),
    ('validate supplier tax documentation', 'verb + noun phrase', 'xác thực hồ sơ thuế của nhà cung cấp trước khi kích hoạt thanh toán hoặc cập nhật dữ liệu nhà cung cấp', 'C1'),
    ('control tail-spend purchases', 'verb + adjective + noun', 'kiểm soát các khoản mua nhỏ và phân tán ngoài nhóm chi tiêu chính để giảm mua ngoài quy trình và chi phí ẩn', 'C1'),
    ('analyze category spending patterns', 'verb + noun phrase', 'phân tích mô hình chi tiêu theo nhóm hàng để nhận diện xu hướng, phân mảnh và cơ hội tối ưu mua sắm', 'C1'),
    ('identify landed-cost savings', 'verb + adjective + noun', 'xác định cơ hội tiết kiệm dựa trên tổng chi phí hàng đến nơi gồm giá mua, vận chuyển, thuế và phụ phí', 'C1'),
    ('negotiate tiered volume rebates', 'verb + adjective + noun', 'đàm phán mức hoàn chiết khấu theo bậc sản lượng để phản ánh quy mô mua thực tế', 'C1'),
    ('document supplier selection rationale', 'verb + noun phrase', 'ghi lại căn cứ lựa chọn nhà cung cấp để bảo đảm quyết định có thể kiểm tra và giải trình', 'C1'),
    ('screen suppliers against sanctions', 'verb + noun phrase', 'sàng lọc nhà cung cấp theo danh sách trừng phạt áp dụng trước khi phê duyệt hoặc tiếp tục giao dịch', 'C1'),
    ('verify supplier compliance certificates', 'verb + noun phrase', 'xác minh chứng nhận tuân thủ của nhà cung cấp còn hiệu lực và phù hợp với phạm vi hàng hóa hoặc dịch vụ', 'C1'),
    ('monitor commodity price indexes', 'verb + noun phrase', 'theo dõi chỉ số giá hàng hóa để hỗ trợ dự báo chi phí và các điều khoản điều chỉnh giá', 'C1'),
    ('coordinate supplier portal onboarding', 'verb + noun phrase', 'phối hợp đưa nhà cung cấp vào cổng giao dịch để hoàn tất tài khoản, dữ liệu và quy trình sử dụng hệ thống', 'C1'),
    ('approve vendor-master data changes', 'verb + noun phrase', 'phê duyệt thay đổi dữ liệu gốc nhà cung cấp sau khi xác minh thông tin và quyền yêu cầu cập nhật', 'C1'),
    ('close fully received purchase orders', 'verb + adjective + noun', 'đóng các đơn mua hàng đã nhận đủ và xử lý xong nghĩa vụ còn lại để tránh cam kết mở không cần thiết', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-50-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v50'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-50-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-49 verification: `1da7f8a848925a3c9843b9015e82ddfe05ca4a36` — scale-48 publication state verified by English Content Master Plan Acceptance #118, English Content Full Validation #114 and Platform CI #1170; published output: `c4c6a387cd1a5fbc062352b18b73b078826384c4`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-50 publication: `e528b4eb8d467c472b77bca241c0ce6e738fd452` — scale-49 publication state verified by English Content Master Plan Acceptance #122, English Content Full Validation #117 and Platform CI #1174; published output: `2534d8a44ab77144615a820ef3ceabf2c70ded88`.',
        'verified scale-49 checkpoint',
    )
    text = replace_once(text, '- Scale-49 publication commit: `2534d8a44ab77144615a820ef3ceabf2c70ded88` — E04 collocation scale-49 published after replacing the single conflicting `col.00001598` candidate with `assess returned merchandise`; published frontier is `col.00001600`.\n', '', 'remove scale-49 publication line')
    text = replace_once(text, '- Scale-49 verification state: publication is complete, but the normal-user checkpoint verification is still required. Bot-triggered English Content Master Plan Acceptance #121 and Platform CI #1173 ended `action_required` before jobs ran, matching the known bot-publication pattern; do not regenerate scale-49.\n', '', 'remove scale-49 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,710 published records after scale-49', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,750 published records after scale-50', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-49 publication', '## Published runtime snapshot after E04 scale-50 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,710 records', '- phrases: 2,750 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,311', '- total published rich records: 7,351', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,311 decisions / 7,311 applied / 7,311 publish decisions', '- editorial ledger: 7,351 decisions / 7,351 applied / 7,351 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001600`', '- E04 collocation frontier: `col.00001640`', 'collocation frontier')
    old_workstream = '''1. Scale-48 publication is fully verified; do not duplicate scale-48 artifacts.
2. Scale-49 source/application/publication is complete at `2534d8a44ab77144615a820ef3ceabf2c70ded88`; do not regenerate or republish it.
3. Verify this normal-user checkpoint with all three mandatory workflows: English Content Master Plan Acceptance, English Content Full Validation and Platform CI. Scale-49 is not fully verified until all three PASS on the checkpoint.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. After scale-49 is fully verified, re-resolve HEAD and recalculate deficits. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-49 publication is fully verified at `e528b4eb8d467c472b77bca241c0ce6e738fd452`; do not duplicate scale-49 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-50 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Scale-49 publication is complete at `2534d8a44ab77144615a820ef3ceabf2c70ded88`. Verify this normal-user checkpoint until English Content Master Plan Acceptance, English Content Full Validation and Platform CI all PASS. Do not create a second CI-refresh checkpoint. Once all three pass, mark scale-49 fully verified in the next real-state progress update associated with subsequent bounded work, then continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001600` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-50 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001640` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main50():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-50 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1600:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1600, got {max(nums) if nums else None}')

    new = [make_collocation(1601 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-50: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-50-collocations.json',
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
            'id': 'review.e04.scale-50.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-50-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-50-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-50-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-50-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-50-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-50-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 50 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1600)', 'if(recallCollocations!==1640)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1600 reviewed records', 'must expose 1640 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001601', 'col.00001640'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1640, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2750, 'richRecords': 7351},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main50()
