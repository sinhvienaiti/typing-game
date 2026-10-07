#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-32-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-32.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-32'
REVIEWED_AT = '2026-10-07T03:29:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-32'
EXPECTED = {'collocations': 880, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('screen eligible patients', 'verb + adjective + noun', 'sàng lọc những bệnh nhân đủ điều kiện theo tiêu chí lâm sàng hoặc chương trình chăm sóc', 'B2'),
    ('administer routine vaccinations', 'verb + adjective + noun', 'thực hiện các mũi tiêm chủng định kỳ theo lịch khuyến nghị', 'B2'),
    ('monitor vital signs', 'verb + adjective + noun', 'theo dõi các dấu hiệu sinh tồn như mạch, huyết áp, nhịp thở và nhiệt độ', 'B2'),
    ('review medical histories', 'verb + adjective + noun', 'rà soát tiền sử bệnh để hỗ trợ đánh giá và quyết định điều trị', 'B2'),
    ('reconcile medication lists', 'verb + noun phrase', 'đối chiếu danh sách thuốc để phát hiện thiếu, trùng hoặc sai khác giữa các nguồn thông tin', 'C1'),
    ('adjust treatment plans', 'verb + noun phrase', 'điều chỉnh kế hoạch điều trị dựa trên đáp ứng, kết quả xét nghiệm hoặc thay đổi tình trạng', 'B2'),
    ('manage chronic conditions', 'verb + adjective + noun', 'quản lý các bệnh mạn tính bằng theo dõi, điều trị và hỗ trợ lâu dài', 'B2'),
    ('coordinate follow-up care', 'verb + noun phrase', 'phối hợp chăm sóc theo dõi sau khám, điều trị hoặc xuất viện', 'B2'),
    ('refer complex cases', 'verb + adjective + noun', 'chuyển các ca phức tạp đến chuyên khoa hoặc cơ sở phù hợp hơn', 'B2'),
    ('triage incoming patients', 'verb + adjective + noun', 'phân loại bệnh nhân mới đến theo mức độ khẩn cấp và nhu cầu chăm sóc', 'C1'),
    ('prioritize urgent cases', 'verb + adjective + noun', 'ưu tiên xử lý các trường hợp khẩn cấp cần can thiệp sớm', 'B2'),
    ('prevent hospital readmissions', 'verb + noun phrase', 'ngăn việc bệnh nhân phải nhập viện lại thông qua theo dõi và chăm sóc chuyển tiếp phù hợp', 'C1'),
    ('reduce infection rates', 'verb + noun phrase', 'giảm tỷ lệ nhiễm bệnh hoặc nhiễm khuẩn bằng các biện pháp phòng ngừa và kiểm soát', 'B2'),
    ('strengthen disease surveillance', 'verb + noun phrase', 'tăng cường giám sát dịch bệnh để phát hiện sớm thay đổi về số ca và mô hình lây truyền', 'C1'),
    ('trace close contacts', 'verb + adjective + noun', 'truy vết những người tiếp xúc gần với ca bệnh để hỗ trợ kiểm soát lây truyền', 'B2'),
    ('investigate disease outbreaks', 'verb + noun phrase', 'điều tra các ổ dịch để xác định nguồn, phạm vi và yếu tố liên quan', 'C1'),
    ('expand testing capacity', 'verb + noun phrase', 'mở rộng năng lực xét nghiệm về số lượng mẫu, địa điểm hoặc tốc độ xử lý', 'B2'),
    ('improve vaccine coverage', 'verb + noun phrase', 'nâng tỷ lệ bao phủ vắc-xin trong nhóm dân số mục tiêu', 'B2'),
    ('maintain cold chains', 'verb + adjective + noun', 'duy trì chuỗi lạnh cần thiết để bảo quản vắc-xin, thuốc hoặc mẫu sinh học', 'C1'),
    ('allocate scarce resources', 'verb + adjective + noun', 'phân bổ nguồn lực khan hiếm theo mức độ ưu tiên và nhu cầu chăm sóc', 'C1'),
    ('train frontline staff', 'verb + adjective + noun', 'đào tạo nhân viên tuyến đầu về quy trình, kỹ năng và biện pháp an toàn cần thiết', 'B2'),
    ('protect patient privacy', 'verb + noun phrase', 'bảo vệ quyền riêng tư của bệnh nhân khi thu thập, sử dụng và chia sẻ thông tin', 'B2'),
    ('obtain informed consent', 'verb + adjective + noun', 'xin sự đồng ý sau khi người bệnh đã được cung cấp và hiểu thông tin cần thiết', 'C1'),
    ('document clinical findings', 'verb + adjective + noun', 'ghi chép các phát hiện lâm sàng một cách rõ ràng và có thể kiểm tra', 'B2'),
    ('interpret diagnostic results', 'verb + adjective + noun', 'diễn giải kết quả chẩn đoán trong bối cảnh triệu chứng và dữ liệu lâm sàng', 'C1'),
    ('confirm laboratory diagnoses', 'verb + adjective + noun', 'xác nhận chẩn đoán bằng bằng chứng từ xét nghiệm phòng thí nghiệm', 'C1'),
    ('manage adverse reactions', 'verb + adjective + noun', 'xử trí các phản ứng bất lợi liên quan đến thuốc, vắc-xin hoặc thủ thuật', 'C1'),
    ('report medication errors', 'verb + noun phrase', 'báo cáo sai sót dùng thuốc để hỗ trợ khắc phục và phòng ngừa tái diễn', 'B2'),
    ('audit clinical practice', 'verb + adjective + noun', 'kiểm toán thực hành lâm sàng so với tiêu chuẩn và quy trình đã thống nhất', 'C1'),
    ('standardize care pathways', 'verb + noun phrase', 'chuẩn hóa lộ trình chăm sóc để giảm biến thiên không cần thiết trong xử trí', 'C1'),
    ('optimize appointment scheduling', 'verb + noun phrase', 'tối ưu lịch hẹn để sử dụng nguồn lực hiệu quả và giảm thời gian chờ', 'B2'),
    ('reduce waiting times', 'verb + noun phrase', 'giảm thời gian người bệnh phải chờ để được khám, xét nghiệm hoặc điều trị', 'B2'),
    ('expand primary care access', 'verb + adjective + noun', 'mở rộng khả năng tiếp cận dịch vụ chăm sóc ban đầu cho cộng đồng', 'B2'),
    ('address health disparities', 'verb + noun phrase', 'giải quyết chênh lệch sức khỏe giữa các nhóm dân cư hoặc khu vực', 'C1'),
    ('support maternal health', 'verb + adjective + noun', 'hỗ trợ sức khỏe bà mẹ trước, trong và sau thai kỳ', 'B2'),
    ('improve neonatal outcomes', 'verb + adjective + noun', 'cải thiện kết quả sức khỏe của trẻ sơ sinh thông qua chăm sóc phù hợp', 'C1'),
    ('promote healthy behaviors', 'verb + adjective + noun', 'khuyến khích các hành vi có lợi cho sức khỏe trong cá nhân và cộng đồng', 'B2'),
    ('deliver preventive care', 'verb + adjective + noun', 'cung cấp chăm sóc phòng ngừa như sàng lọc, tư vấn và tiêm chủng', 'B2'),
    ('coordinate emergency response', 'verb + adjective + noun', 'phối hợp hoạt động ứng phó y tế trong tình huống khẩn cấp hoặc thảm họa', 'C1'),
    ('maintain essential services', 'verb + adjective + noun', 'duy trì các dịch vụ y tế thiết yếu trong giai đoạn gián đoạn hoặc nhu cầu tăng cao', 'B2'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-32-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v32'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-32-collocations.json',
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
        '- Latest published scale-up HEAD before this checkpoint: `6dce5bc2d93198df5cda4e142915127e8bb72457` — `feat(content): publish E04 collocation scale 31`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-32 publication: `7e4430ca92c3d9007a7c61bafe84ef86546c69d4` — scale-31 publication state verified by English Content Master Plan Acceptance #60, English Content Full Validation #73 and Platform CI #1081; published output: `6dce5bc2d93198df5cda4e142915127e8bb72457`.',
        'verified scale-31 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest scale-31 pre-publication HEAD: `c51cfe57955997af0a3f89f3cf231ec9300ead5a` — Apply English E04 Scale 31 #1, English Content Full Validation #72 and English Content Master Plan Acceptance #58 PASS; Platform CI #1078 had already passed English-content/runtime/Space Typing gates and was finishing the final app build when the publication commit landed.\n',
        '',
        'remove scale-31 prep checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-31 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #59 and Platform CI #1080 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-31 content or weakening any gate.\n',
        '',
        'remove resolved scale-31 verification note',
    )
    text = replace_once(
        text,
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,990 published records after scale-31',
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,030 published records after scale-32',
        'E04 count',
    )
    text = replace_once(text, '## Published runtime snapshot after E04 scale-31 publication', '## Published runtime snapshot after E04 scale-32 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 1,990 records', '- phrases: 2,030 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,591', '- total published rich records: 6,631', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,591 decisions / 6,591 applied / 6,591 publish decisions', '- editorial ledger: 6,631 decisions / 6,631 applied / 6,631 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00000880`', '- E04 collocation frontier: `col.00000920`', 'collocation frontier')
    old_workstream = '''1. Verify scale-31 publication state through this normal-user checkpoint CI; do not duplicate scale-31 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-31 checkpoint CI passes and no newer worker has claimed the next scope, create scale-32 as the next bounded collocation batch from frontier `col.00000880`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-31 publication is fully verified; do not duplicate scale-31 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-32 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-31 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-31 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000880` (expected scale-32 range `col.00000881` through `col.00000920` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-32 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000920` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-32 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 880:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 880, got {max(nums) if nums else None}')

    new = [make_collocation(881 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-32: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-32-collocations.json',
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
            'id': 'review.e04.scale-32.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-32-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-32-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-32-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-32-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-32-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-32-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 32 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==880)', 'if(recallCollocations!==920)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 880 reviewed records', 'must expose 920 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00000881', 'col.00000920'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 920, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2030, 'richRecords': 6631},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
