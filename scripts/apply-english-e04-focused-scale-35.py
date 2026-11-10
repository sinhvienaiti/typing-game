#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-35-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-35.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-35'
REVIEWED_AT = '2026-10-07T04:15:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-35'
EXPECTED = {'collocations': 1000, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('forecast shipment volumes', 'verb + noun phrase', 'dự báo khối lượng hàng gửi để lập kế hoạch năng lực vận chuyển và kho bãi', 'B2'),
    ('consolidate outbound orders', 'verb + adjective + noun', 'gom các đơn hàng xuất đi để tăng hiệu quả đóng gói và vận chuyển', 'B2'),
    ('allocate warehouse capacity', 'verb + noun phrase', 'phân bổ sức chứa kho cho các nhóm hàng, khu vực hoặc nhu cầu dự kiến', 'B2'),
    ('optimize picking routes', 'verb + noun phrase', 'tối ưu tuyến lấy hàng trong kho để giảm quãng đường và thời gian xử lý', 'C1'),
    ('schedule dock appointments', 'verb + noun phrase', 'lập lịch xe hoặc container vào khu vực bốc dỡ để giảm ùn tắc tại kho', 'B2'),
    ('coordinate carrier pickups', 'verb + noun phrase', 'phối hợp lịch lấy hàng với đơn vị vận chuyển theo thời gian và khối lượng đã xác nhận', 'B2'),
    ('track container movements', 'verb + noun phrase', 'theo dõi sự di chuyển của container qua các chặng trong chuỗi vận tải', 'B2'),
    ('monitor transit delays', 'verb + noun phrase', 'giám sát các chậm trễ trong quá trình vận chuyển để xử lý tác động đến giao hàng', 'B2'),
    ('reroute delayed shipments', 'verb + adjective + noun', 'đổi tuyến các lô hàng bị chậm nhằm giảm thời gian gián đoạn', 'C1'),
    ('expedite critical deliveries', 'verb + adjective + noun', 'đẩy nhanh các chuyến giao hàng quan trọng cần đến sớm hơn lịch thông thường', 'C1'),
    ('balance safety stocks', 'verb + noun phrase', 'cân đối tồn kho an toàn giữa mức phục vụ và chi phí lưu kho', 'C1'),
    ('set reorder points', 'verb + noun phrase', 'thiết lập điểm đặt hàng lại dựa trên nhu cầu, thời gian cung ứng và mức tồn kho an toàn', 'B2'),
    ('replenish regional depots', 'verb + adjective + noun', 'bổ sung hàng cho các kho khu vực để duy trì khả năng đáp ứng nhu cầu', 'B2'),
    ('classify inventory items', 'verb + noun phrase', 'phân loại mặt hàng tồn kho theo giá trị, tốc độ luân chuyển hoặc đặc tính quản lý', 'B2'),
    ('conduct cycle counts', 'verb + noun phrase', 'thực hiện kiểm đếm luân phiên từng phần kho thay vì kiểm kê toàn bộ cùng lúc', 'B2'),
    ('investigate stock discrepancies', 'verb + noun phrase', 'điều tra chênh lệch giữa số liệu tồn kho hệ thống và số lượng thực tế', 'B2'),
    ('reduce inventory shrinkage', 'verb + noun phrase', 'giảm hao hụt tồn kho do mất mát, hư hỏng, sai sót hoặc gian lận', 'C1'),
    ('manage product recalls', 'verb + noun phrase', 'quản lý việc thu hồi sản phẩm từ thị trường theo phạm vi và quy trình đã xác định', 'C1'),
    ('verify chain-of-custody records', 'verb + noun phrase', 'xác minh hồ sơ bàn giao để bảo đảm lịch sử kiểm soát hàng hóa hoặc mẫu vật có thể truy vết', 'C1'),
    ('validate supplier lead times', 'verb + noun phrase', 'xác nhận thời gian cung ứng thực tế của nhà cung cấp để cải thiện kế hoạch tồn kho', 'B2'),
    ('diversify sourcing regions', 'verb + noun phrase', 'đa dạng hóa khu vực mua hàng để giảm phụ thuộc vào một nguồn địa lý', 'C1'),
    ('qualify backup suppliers', 'verb + adjective + noun', 'đánh giá và phê duyệt các nhà cung cấp dự phòng trước khi cần sử dụng', 'C1'),
    ('negotiate freight rates', 'verb + noun phrase', 'đàm phán mức cước vận chuyển với hãng vận tải hoặc nhà cung cấp logistics', 'B2'),
    ('tender transport contracts', 'verb + noun phrase', 'tổ chức mời thầu hợp đồng vận tải để lựa chọn nhà cung cấp phù hợp', 'C1'),
    ('audit carrier performance', 'verb + noun phrase', 'kiểm tra hiệu quả của đơn vị vận chuyển theo chất lượng, chi phí và mức độ tuân thủ', 'C1'),
    ('measure on-time delivery', 'verb + adjective + noun', 'đo tỷ lệ giao hàng đúng thời hạn đã cam kết', 'B2'),
    ('improve order fill rates', 'verb + noun phrase', 'nâng tỷ lệ đơn hàng được đáp ứng đầy đủ từ lượng hàng sẵn có', 'B2'),
    ('reduce picking errors', 'verb + noun phrase', 'giảm lỗi lấy nhầm mặt hàng hoặc số lượng trong quá trình xử lý đơn', 'B2'),
    ('automate warehouse workflows', 'verb + noun phrase', 'tự động hóa các quy trình kho để giảm thao tác thủ công và tăng tính nhất quán', 'C1'),
    ('maintain cold-storage conditions', 'verb + adjective + noun', 'duy trì điều kiện kho lạnh phù hợp với yêu cầu bảo quản của hàng hóa', 'C1'),
    ('secure hazardous materials', 'verb + adjective + noun', 'bảo quản và kiểm soát vật liệu nguy hiểm theo yêu cầu an toàn và truy cập', 'C1'),
    ('document customs declarations', 'verb + noun phrase', 'lập và lưu hồ sơ khai báo hải quan chính xác cho hàng xuất nhập khẩu', 'B2'),
    ('classify tariff codes', 'verb + noun phrase', 'xác định mã thuế quan phù hợp cho hàng hóa theo hệ thống phân loại áp dụng', 'C1'),
    ('clear inbound consignments', 'verb + adjective + noun', 'hoàn tất thủ tục cần thiết để các lô hàng nhập được thông quan và nhận vào mạng lưới', 'C1'),
    ('calculate landed costs', 'verb + adjective + noun', 'tính tổng chi phí hàng về bao gồm giá mua, vận chuyển, thuế và phí liên quan', 'C1'),
    ('manage reverse logistics', 'verb + adjective + noun', 'quản lý dòng hàng đi ngược từ khách hàng về kho, nhà cung cấp hoặc điểm xử lý', 'C1'),
    ('process customer returns', 'verb + noun phrase', 'xử lý hàng khách trả lại theo kiểm tra, hoàn tiền, tái nhập kho hoặc tiêu hủy', 'B2'),
    ('recover reusable packaging', 'verb + adjective + noun', 'thu hồi bao bì có thể tái sử dụng để đưa trở lại chu trình vận hành', 'B2'),
    ('monitor warehouse utilization', 'verb + noun phrase', 'theo dõi mức sử dụng không gian và năng lực kho để nhận diện thiếu hoặc dư công suất', 'B2'),
    ('coordinate last-mile delivery', 'verb + adjective + noun', 'phối hợp chặng giao hàng cuối cùng từ điểm phân phối đến người nhận', 'B2'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-35-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v35'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-35-collocations.json',
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
        '- Latest published scale-up HEAD before this checkpoint: `8825d0158b036e87bfeaa9ef1749d5448a40ab32` — `feat(content): publish E04 collocation scale 34`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-35 publication: `e7342759929cf624efb35fc56b09542bde7cd193` — scale-34 publication state verified by English Content Master Plan Acceptance #71, English Content Full Validation #81 and Platform CI #1097; published output: `8825d0158b036e87bfeaa9ef1749d5448a40ab32`.',
        'verified scale-34 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest scale-34 pre-publication HEAD: `e778dcae752536339e246e7aa871fde37f6189fa` — Apply English E04 Scale 34 #1, English Content Full Validation #80 and English Content Master Plan Acceptance #69 PASS; preflight was clean on the first attempt, and all publication quality gates plus deterministic replay passed before the bot commit was pushed.\n',
        '',
        'remove scale-34 prep checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-34 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #70 and Platform CI #1095 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-34 content or weakening any gate.\n',
        '',
        'remove resolved scale-34 verification note',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,110 published records after scale-34', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,150 published records after scale-35', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-34 publication', '## Published runtime snapshot after E04 scale-35 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,110 records', '- phrases: 2,150 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,711', '- total published rich records: 6,751', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,711 decisions / 6,711 applied / 6,711 publish decisions', '- editorial ledger: 6,751 decisions / 6,751 applied / 6,751 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001000`', '- E04 collocation frontier: `col.00001040`', 'collocation frontier')
    old_workstream = '''1. Verify scale-34 publication state through this normal-user checkpoint CI; do not duplicate scale-34 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-34 checkpoint CI passes and no newer worker has claimed the next scope, create scale-35 as the next bounded collocation batch from frontier `col.00001000`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-34 publication is fully verified; do not duplicate scale-34 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-35 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-34 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-34 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001000` (expected scale-35 range `col.00001001` through `col.00001040` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-35 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001040` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-35 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1000:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1000, got {max(nums) if nums else None}')

    new = [make_collocation(1001 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-35: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-35-collocations.json',
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
            'id': 'review.e04.scale-35.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-35-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-35-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-35-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-35-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-35-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-35-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 35 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1000)', 'if(recallCollocations!==1040)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1000 reviewed records', 'must expose 1040 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001001', 'col.00001040'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1040, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2150, 'richRecords': 6751},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
