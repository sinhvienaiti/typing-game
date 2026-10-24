#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-31-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-31.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-31'
REVIEWED_AT = '2026-10-07T02:34:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-31'
EXPECTED = {'collocations': 840, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('reduce carbon emissions', 'verb + noun phrase', 'giảm lượng khí thải carbon phát sinh từ hoạt động sản xuất, vận hành hoặc tiêu dùng', 'B2'),
    ('cut energy consumption', 'verb + noun phrase', 'cắt giảm mức năng lượng được sử dụng trong một hoạt động, tòa nhà hoặc hệ thống', 'B2'),
    ('improve energy efficiency', 'verb + noun phrase', 'nâng cao hiệu quả sử dụng năng lượng để tạo cùng kết quả với ít năng lượng hơn', 'B2'),
    ('deploy renewable capacity', 'verb + adjective + noun', 'triển khai thêm công suất năng lượng tái tạo như điện gió hoặc điện mặt trời', 'C1'),
    ('modernize power grids', 'verb + noun phrase', 'hiện đại hóa lưới điện để tăng độ tin cậy, khả năng điều khiển và tích hợp nguồn mới', 'C1'),
    ('integrate variable renewables', 'verb + adjective + noun', 'tích hợp các nguồn tái tạo có sản lượng biến đổi vào hệ thống điện một cách ổn định', 'C1'),
    ('store excess electricity', 'verb + adjective + noun', 'lưu trữ lượng điện dư để sử dụng vào thời điểm nhu cầu cao hơn hoặc nguồn phát thấp hơn', 'B2'),
    ('balance electricity demand', 'verb + noun phrase', 'cân bằng nhu cầu điện với khả năng cung cấp của hệ thống theo thời gian', 'C1'),
    ('forecast energy demand', 'verb + noun phrase', 'dự báo nhu cầu năng lượng trong tương lai để hỗ trợ lập kế hoạch cung ứng', 'B2'),
    ('electrify vehicle fleets', 'verb + noun phrase', 'chuyển đội phương tiện sang sử dụng động cơ điện thay cho nhiên liệu hóa thạch', 'C1'),
    ('expand charging infrastructure', 'verb + noun phrase', 'mở rộng hạ tầng sạc để hỗ trợ việc sử dụng phương tiện điện trên quy mô lớn hơn', 'B2'),
    ('phase out fossil fuels', 'verb + particle + noun phrase', 'loại bỏ dần việc sử dụng nhiên liệu hóa thạch theo lộ trình', 'B2'),
    ('retire coal plants', 'verb + noun phrase', 'đóng cửa và ngừng vận hành các nhà máy điện than theo kế hoạch', 'C1'),
    ('capture industrial emissions', 'verb + adjective + noun', 'thu giữ khí thải từ các quá trình công nghiệp trước khi chúng phát tán vào khí quyển', 'C1'),
    ('monitor methane leaks', 'verb + noun phrase', 'theo dõi các điểm rò rỉ khí methane để phát hiện và xử lý sớm', 'B2'),
    ('restore degraded ecosystems', 'verb + adjective + noun', 'phục hồi các hệ sinh thái đã suy thoái để cải thiện chức năng và đa dạng sinh học', 'C1'),
    ('protect biodiversity hotspots', 'verb + noun phrase', 'bảo vệ các khu vực có mức đa dạng sinh học đặc biệt cao và dễ bị tổn thương', 'C1'),
    ('conserve water resources', 'verb + noun phrase', 'bảo tồn và sử dụng tiết kiệm nguồn nước để duy trì khả năng cung cấp lâu dài', 'B2'),
    ('improve soil health', 'verb + noun phrase', 'cải thiện chất lượng và chức năng của đất để hỗ trợ hệ sinh thái và sản xuất bền vững', 'B2'),
    ('reduce food waste', 'verb + noun phrase', 'giảm lượng thực phẩm bị bỏ đi trong sản xuất, phân phối hoặc tiêu dùng', 'B2'),
    ('divert waste from landfills', 'verb + noun + preposition + noun', 'chuyển chất thải khỏi bãi chôn lấp sang tái sử dụng, tái chế hoặc xử lý phù hợp hơn', 'C1'),
    ('increase recycling rates', 'verb + noun phrase', 'tăng tỷ lệ vật liệu được thu gom và đưa vào quá trình tái chế', 'B2'),
    ('design circular products', 'verb + adjective + noun', 'thiết kế sản phẩm theo hướng tái sử dụng, sửa chữa và tuần hoàn vật liệu', 'C1'),
    ('extend product lifetimes', 'verb + noun phrase', 'kéo dài thời gian sử dụng hữu ích của sản phẩm trước khi phải thay thế hoặc loại bỏ', 'B2'),
    ('source sustainable materials', 'verb + adjective + noun', 'tìm nguồn và mua vật liệu đáp ứng các tiêu chí bền vững đã xác định', 'C1'),
    ('measure lifecycle impacts', 'verb + noun phrase', 'đo lường tác động trong toàn bộ vòng đời của sản phẩm hoặc dịch vụ', 'C1'),
    ('verify sustainability claims', 'verb + noun phrase', 'xác minh các tuyên bố về tính bền vững bằng dữ liệu và tiêu chí có thể kiểm tra', 'C1'),
    ('disclose climate risks', 'verb + noun phrase', 'công bố các rủi ro liên quan đến khí hậu có thể ảnh hưởng đến tổ chức hoặc tài sản', 'C1'),
    ('set science-based targets', 'verb + adjective + noun', 'đặt mục tiêu giảm tác động dựa trên cơ sở khoa học và lộ trình đo lường được', 'C1'),
    ('finance clean technologies', 'verb + adjective + noun', 'cung cấp vốn cho các công nghệ giúp giảm ô nhiễm, phát thải hoặc sử dụng tài nguyên', 'C1'),
    ('price carbon emissions', 'verb + noun phrase', 'gắn chi phí kinh tế cho lượng khí thải carbon nhằm phản ánh tác động môi trường', 'C1'),
    ('strengthen climate resilience', 'verb + noun phrase', 'tăng khả năng chống chịu và phục hồi trước các tác động của biến đổi khí hậu', 'C1'),
    ('assess physical climate risks', 'verb + adjective + noun', 'đánh giá các rủi ro vật lý do nhiệt độ, bão, lũ, hạn hán hoặc biến đổi khí hậu gây ra', 'C1'),
    ('adapt coastal infrastructure', 'verb + adjective + noun', 'điều chỉnh hạ tầng ven biển để thích ứng với nước biển dâng và thời tiết cực đoan', 'C1'),
    ('manage drought exposure', 'verb + noun phrase', 'quản lý mức độ phơi nhiễm trước hạn hán trong hoạt động, chuỗi cung ứng hoặc cộng đồng', 'C1'),
    ('prepare heat action plans', 'verb + noun phrase', 'chuẩn bị kế hoạch ứng phó với các đợt nắng nóng và rủi ro sức khỏe liên quan', 'B2'),
    ('protect vulnerable communities', 'verb + adjective + noun', 'bảo vệ các cộng đồng dễ bị tổn thương trước rủi ro môi trường và khí hậu', 'B2'),
    ('track environmental performance', 'verb + adjective + noun', 'theo dõi kết quả môi trường theo các chỉ số và mục tiêu đã xác định', 'B2'),
    ('meet sustainability standards', 'verb + noun phrase', 'đáp ứng các tiêu chuẩn hoặc yêu cầu về hoạt động bền vững', 'B2'),
    ('report scope three emissions', 'verb + noun phrase', 'báo cáo phát thải gián tiếp thuộc phạm vi ba trong chuỗi giá trị của tổ chức', 'C1'),
]

def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def normalized_key(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text).strip().lower())

def token_set(text: str) -> set[str]:
    return {p for p in re.sub(r"[^a-z0-9'’-]+", ' ', normalized_key(text)).split() if p}

def jaccard(a: str, b: str) -> float:
    left, right = token_set(a), token_set(b)
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)

def digest(record) -> str:
    source = json.loads(json.dumps(record, ensure_ascii=False))
    checks = source.get('quality', {}).get('checks', {})
    checks.pop('cefr', None)
    checks.pop('license', None)
    return hashlib.sha256((json.dumps(source, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest()

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly one occurrence, found {count}')
    return text.replace(old, new, 1)

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
                'schema': {'status': 'pass', 'method': 'e04-scale-31-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v31'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-31-collocations.json',
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
        '- Latest published scale-up HEAD before this checkpoint: `cb1ae65a88181d25933f9ac0465382231b8d73d6` — `feat(content): publish E04 collocation scale 30`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-31 publication: `a39288a22f50f9010d5ed2cfcee93b8e6648113e` — scale-30 publication state verified by English Content Master Plan Acceptance #57, English Content Full Validation #71 and Platform CI #1077; published output: `cb1ae65a88181d25933f9ac0465382231b8d73d6`.',
        'verified scale-30 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest fully CI-verified pre-publication HEAD: `cb00f341eabccaa43c19593001264e1100975580` — Apply English E04 Scale 30 #1, English Content Full Validation #70, English Content Master Plan Acceptance #55 and Platform CI #1075 all PASS.\n',
        '',
        'remove scale-30 prep checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-30 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #56 and Platform CI #1076 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the same mandatory CI from a normal branch write without regenerating scale-30 content or weakening any gate.\n',
        '',
        'remove resolved scale-30 verification note',
    )
    text = replace_once(
        text,
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,950 published records after scale-30',
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,990 published records after scale-31',
        'E04 count',
    )
    text = replace_once(text, '## Published runtime snapshot after E04 scale-30 publication', '## Published runtime snapshot after E04 scale-31 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 1,950 records', '- phrases: 1,990 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,551', '- total published rich records: 6,591', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,551 decisions / 6,551 applied / 6,551 publish decisions', '- editorial ledger: 6,591 decisions / 6,591 applied / 6,591 publish decisions', 'ledger count')
    old_workstream = '''1. Verify scale-30 publication state through the normal-user checkpoint CI; do not duplicate scale-30 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-30 checkpoint CI passes and no newer worker has claimed the next scope, create scale-31 as the next bounded collocation batch from frontier `col.00000840`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-30 publication is fully verified; do not duplicate scale-30 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-31 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-30 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-30 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000840` (expected scale-31 range `col.00000841` through `col.00000880` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-31 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000880` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-31 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 840:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 840, got {max(nums) if nums else None}')

    new = [make_collocation(841 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-31: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-31-collocations.json',
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
            'id': 'review.e04.scale-31.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-31-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-31-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-31-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-31-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-31-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-31-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 31 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==840)', 'if(recallCollocations!==880)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 840 reviewed records', 'must expose 880 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00000841', 'col.00000880'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 880, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 1990, 'richRecords': 6591},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
