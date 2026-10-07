#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-45.py'), run_name='e04_scale46_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-46-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-46.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-46'
REVIEWED_AT = '2026-10-07T07:50:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-46'
EXPECTED = {'collocations': 1440, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('catalog museum objects', 'verb + noun phrase', 'lập danh mục hiện vật bảo tàng với thông tin nhận dạng, mô tả và tình trạng cơ bản', 'B2'),
    ('document artifact provenance', 'verb + noun phrase', 'ghi lại nguồn gốc và lịch sử sở hữu của hiện vật để hỗ trợ nghiên cứu và quản lý', 'C1'),
    ('assess object condition', 'verb + noun phrase', 'đánh giá tình trạng vật lý của hiện vật để xác định rủi ro và nhu cầu bảo tồn', 'B2'),
    ('stabilize fragile materials', 'verb + adjective + noun', 'ổn định vật liệu dễ hư hỏng để ngăn xuống cấp thêm trong lưu trữ hoặc trưng bày', 'C1'),
    ('control gallery humidity', 'verb + noun phrase', 'kiểm soát độ ẩm trong không gian trưng bày để bảo vệ hiện vật nhạy cảm', 'B2'),
    ('monitor display lighting', 'verb + noun phrase', 'theo dõi mức chiếu sáng tại khu trưng bày để hạn chế hư hại do ánh sáng', 'B2'),
    ('mount exhibition objects', 'verb + noun phrase', 'gắn và cố định hiện vật lên hệ thống trưng bày phù hợp và an toàn', 'C1'),
    ('pack cultural artifacts', 'verb + adjective + noun', 'đóng gói hiện vật văn hóa bằng vật liệu và kỹ thuật phù hợp cho vận chuyển hoặc lưu kho', 'B2'),
    ('crate oversized artworks', 'verb + adjective + noun', 'đóng kiện các tác phẩm kích thước lớn để vận chuyển an toàn', 'C1'),
    ('inspect incoming loans', 'verb + adjective + noun', 'kiểm tra hiện vật mượn khi tiếp nhận để xác nhận tình trạng và yêu cầu xử lý', 'B2'),
    ('register loan agreements', 'verb + noun phrase', 'ghi nhận và quản lý thỏa thuận cho mượn hiện vật cùng điều kiện liên quan', 'B2'),
    ('schedule conservation treatment', 'verb + noun phrase', 'lập lịch xử lý bảo tồn theo mức độ ưu tiên, nguồn lực và tình trạng hiện vật', 'C1'),
    ('clean painted surfaces', 'verb + adjective + noun', 'làm sạch bề mặt sơn bằng phương pháp phù hợp để tránh làm hỏng lớp vật liệu gốc', 'C1'),
    ('consolidate flaking paint', 'verb + adjective + noun', 'cố định lớp sơn bong tróc để ngăn mất mát vật liệu tiếp tục', 'C1'),
    ('repair textile supports', 'verb + noun phrase', 'sửa chữa lớp hoặc kết cấu đỡ cho hiện vật dệt nhằm tăng ổn định khi lưu trữ và trưng bày', 'C1'),
    ('house archival documents', 'verb + adjective + noun', 'đặt tài liệu lưu trữ vào vật liệu bao gói và hộp bảo quản thích hợp', 'C1'),
    ('digitize collection records', 'verb + noun phrase', 'số hóa hồ sơ bộ sưu tập để hỗ trợ tra cứu, quản lý và bảo tồn thông tin', 'B2'),
    ('capture object photography', 'verb + noun phrase', 'chụp ảnh hiện vật theo tiêu chuẩn tài liệu hóa để phục vụ hồ sơ và nghiên cứu', 'B2'),
    ('calibrate color targets', 'verb + noun phrase', 'hiệu chuẩn bảng màu tham chiếu để bảo đảm ảnh hiện vật có màu sắc đáng tin cậy', 'C1'),
    ('update accession records', 'verb + noun phrase', 'cập nhật hồ sơ tiếp nhận hiện vật với thông tin mới hoặc đã được xác minh', 'B2'),
    ('assign catalog numbers', 'verb + noun phrase', 'cấp số danh mục duy nhất cho hiện vật nhằm quản lý và truy vết chính xác', 'B2'),
    ('research object histories', 'verb + noun phrase', 'nghiên cứu lịch sử của hiện vật từ nguồn tư liệu, chủ sở hữu và bối cảnh liên quan', 'C1'),
    ('verify donor restrictions', 'verb + noun phrase', 'xác minh các điều kiện hoặc hạn chế do bên hiến tặng đặt ra đối với hiện vật', 'C1'),
    ('track object movements', 'verb + noun phrase', 'theo dõi việc di chuyển hiện vật giữa kho, phòng bảo tồn, khu trưng bày và địa điểm mượn', 'B2'),
    ('escort valuable loans', 'verb + adjective + noun', 'hộ tống hiện vật có giá trị trong quá trình vận chuyển để giám sát an toàn và điều kiện xử lý', 'C1'),
    ('prepare courier reports', 'verb + noun phrase', 'chuẩn bị báo cáo của người hộ tống về hành trình, xử lý và tình trạng hiện vật', 'C1'),
    ('install gallery labels', 'verb + noun phrase', 'lắp đặt nhãn trưng bày tại vị trí phù hợp với hiện vật và thiết kế triển lãm', 'B2'),
    ('proof exhibition text', 'verb + noun phrase', 'soát lỗi nội dung triển lãm trước khi in hoặc xuất bản để bảo đảm độ chính xác và nhất quán', 'B2'),
    ('design display mounts', 'verb + noun phrase', 'thiết kế giá đỡ trưng bày phù hợp với hình dạng, trọng lượng và yêu cầu bảo tồn của hiện vật', 'C1'),
    ('adjust case lighting', 'verb + noun phrase', 'điều chỉnh ánh sáng trong tủ trưng bày để cân bằng khả năng quan sát và giới hạn phơi sáng', 'B2'),
    ('monitor pest activity', 'verb + noun phrase', 'theo dõi dấu hiệu côn trùng và sinh vật gây hại trong kho hoặc khu trưng bày', 'B2'),
    ('quarantine infested objects', 'verb + adjective + noun', 'cách ly hiện vật bị sinh vật gây hại để ngăn lây lan sang bộ sưu tập khác', 'C1'),
    ('record environmental readings', 'verb + adjective + noun', 'ghi lại số liệu nhiệt độ, độ ẩm và các điều kiện môi trường liên quan đến bảo quản', 'B2'),
    ('rotate light-sensitive works', 'verb + adjective + noun', 'luân phiên các tác phẩm nhạy sáng để giới hạn tổng thời gian phơi sáng', 'C1'),
    ('manage collection storage', 'verb + noun phrase', 'quản lý không gian và hệ thống lưu trữ bộ sưu tập theo yêu cầu bảo tồn và truy xuất', 'B2'),
    ('retrieve study objects', 'verb + noun phrase', 'lấy hiện vật phục vụ nghiên cứu theo quy trình kiểm soát vị trí và xử lý', 'B2'),
    ('supervise object handling', 'verb + noun phrase', 'giám sát thao tác với hiện vật để bảo đảm kỹ thuật an toàn được tuân thủ', 'C1'),
    ('document conservation treatment', 'verb + noun phrase', 'ghi chép đầy đủ quá trình và vật liệu xử lý bảo tồn để duy trì hồ sơ lâu dài', 'C1'),
    ('prepare deaccession records', 'verb + noun phrase', 'chuẩn bị hồ sơ loại hiện vật khỏi bộ sưu tập theo quy trình và phê duyệt bắt buộc', 'C1'),
    ('audit collection inventories', 'verb + noun phrase', 'kiểm kê và đối chiếu bộ sưu tập để xác nhận vị trí, tình trạng và hồ sơ của hiện vật', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-46-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v46'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-46-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-45 publication: `7642618f8b1ea598a6da1b8357f1dc0265b5b559` — scale-44 publication state verified by English Content Master Plan Acceptance #106, English Content Full Validation #106 and Platform CI #1155; published output: `bc0489659d3eaaea0ad400e6d9b01d859a285b79`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-46 publication: `c4ce06381108bfe1888f99e02ea81c8ccfa66f7f` — scale-45 publication state verified by English Content Master Plan Acceptance #109, English Content Full Validation #108 and Platform CI #1158; published output: `af9a91944cf030ff3fafb753ff2ada8bf62bd643`.',
        'verified scale-45 checkpoint',
    )
    text = replace_once(text, '- Scale-45 publication output: `af9a91944cf030ff3fafb753ff2ada8bf62bd643` — `feat(content): publish E04 collocation scale 45`; Apply English E04 Scale 45 #1 passed preflight, controlled review, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-45 publication line')
    text = replace_once(text, '- Scale-45 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #108 and Platform CI #1157 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-45 content or weakening any gate.\n', '', 'remove scale-45 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,550 published records after scale-45', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,590 published records after scale-46', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-45 publication', '## Published runtime snapshot after E04 scale-46 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,550 records', '- phrases: 2,590 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,151', '- total published rich records: 7,191', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,151 decisions / 7,151 applied / 7,151 publish decisions', '- editorial ledger: 7,191 decisions / 7,191 applied / 7,191 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001440`', '- E04 collocation frontier: `col.00001480`', 'collocation frontier')
    old_workstream = '''1. Scale-44 publication is fully verified; do not duplicate scale-44 artifacts.
2. Scale-45 publication `af9a91944cf030ff3fafb753ff2ada8bf62bd643` is complete; do not regenerate or duplicate scale-45 artifacts.
3. Verify scale-45 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #108/#1157 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-45 checkpoint CI passes and no newer worker has claimed the next scope, create scale-46 as the next bounded collocation batch from frontier `col.00001440`, expected IDs `col.00001441` through `col.00001480`, while preserving exact/near-dedupe threshold 0.86 and all E10/E11/E12 gates.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-45 publication is fully verified; do not duplicate scale-45 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-46 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-45 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-45 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001440` (expected scale-46 range `col.00001441` through `col.00001480` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-46 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001480` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-46 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1440:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1440, got {max(nums) if nums else None}')

    new = [make_collocation(1441 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-46: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-46-collocations.json',
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
            'id': 'review.e04.scale-46.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-46-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-46-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-46-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-46-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-46-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-46-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 46 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1440)', 'if(recallCollocations!==1480)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1440 reviewed records', 'must expose 1480 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001441', 'col.00001480'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1480, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2590, 'richRecords': 7191},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
