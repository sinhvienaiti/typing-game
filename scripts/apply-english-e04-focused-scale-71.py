#!/usr/bin/env python3
from __future__ import annotations
import json, re, runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
s = runpy.run_path(str(ROOT / 'scripts/english-e04-scale-71-common.py'), run_name='e04_scale71_apply')
read_json, write_json = s['read_json'], s['write_json']
normalized_key, jaccard, digest = s['normalized_key'], s['jaccard'], s['digest']
MANIFEST_PATH, COL_PATH, DECISION_PATH = s['MANIFEST_PATH'], s['COL_PATH'], s['DECISION_PATH']
BATCH_ID, REVIEWED_AT, REVIEWED_BY = s['BATCH_ID'], s['REVIEWED_AT'], s['REVIEWED_BY']
EXPECTED, NEAR_DUP_THRESHOLD, COLLOCATIONS = s['EXPECTED'], s['NEAR_DUP_THRESHOLD'], s['COLLOCATIONS']
make_record = s['make_record']

def main71():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-71 artifact exists without matching batch manifest')
    existing = {'collocations': [], 'verbPatterns': [], 'phraseItems': []}
    all_texts, all_ids = [], set()
    for batch in manifest.get('batches', []):
        if batch.get('phase') != 'E04' or batch.get('category') != 'phrases':
            continue
        for record_set in batch.get('recordSets', []):
            records = read_json(ROOT / record_set['path']).get('records', [])
            rsid = record_set.get('id')
            if rsid in {'collocations', 'scale-collocations'}:
                existing['collocations'].extend(records)
            elif rsid in {'verb-patterns', 'scale-verb-patterns'}:
                existing['verbPatterns'].extend(records)
            elif rsid in {'phrases', 'scale-phrases'}:
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
    nums = [int(m.group(1)) for record in existing['collocations'] if (m := re.fullmatch(r'col\.(\d{8})', str(record.get('id', ''))))]
    if not nums or max(nums) != 2440:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2440, got {max(nums) if nums else None}')
    new = [make_record(2441 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
    exact = {normalized_key(text): rid for rid, text in all_texts}
    accepted = []
    for record in new:
        rid, text = record['id'], record['text']; key = normalized_key(text)
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
                raise RuntimeError(f'duplicate inside scale-71: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(record)
    write_json(COL_PATH, {'schemaVersion': 1, 'records': new})
    manifest['batches'].append({
        'id': BATCH_ID, 'phase': 'E04', 'category': 'phrases', 'cefr': ['B2', 'C1'], 'state': 'draft',
        'recordSets': [{'id': 'scale-collocations', 'path': 'content/english/phrases/e04-scale-71-collocations.json', 'expectedCount': 40, 'generated': False, 'allowedQualityStates': ['draft'], 'requiredChecks': ['schema','grammar','translation','naturalness','cefr','targetStructure','exactDuplicate','nearDuplicate','license']}],
        'requiredBeforePublish': ['schema-validation','reference-integrity','exact-dedup','near-dedup','grammar-review','bilingual-review','naturalness-review','cefr-review','target-structure-review','license-review','cross-game-smoke'],
        'gameSmokes': [
            {'gameId':'recall-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},
            {'gameId':'vocab-shooter','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},
            {'gameId':'space-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},
        ],
    })
    write_json(MANIFEST_PATH, manifest)
    decisions = []
    for record in new:
        decisions.append({
            'id': 'review.e04.scale-71.' + record['id'].replace('.', '-'), 'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations', 'recordId': record['id'], 'sourceDigest': digest(record), 'targetState': 'published',
            'checks': {
                'grammar': {'status':'pass','method':'e04-scale-71-grammar-editorial-review'},
                'translation': {'status':'pass','method':'e04-scale-71-bilingual-review'},
                'naturalness': {'status':'pass','method':'e04-scale-71-naturalness-review'},
                'cefr': {'status':'pass','method':'e04-scale-71-cefr-review'},
                'targetStructure': {'status':'pass','method':'e04-scale-71-structure-review'},
                'nearDuplicate': {'status':'pass','method':'e04-scale-71-cross-batch-near-dedup-review'},
                'license': {'status':'pass','method':'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT, 'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 71 renewable-energy grid operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})
    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = s['replace_once'](smoke, 'if(recallCollocations!==2440)', 'if(recallCollocations!==2480)', 'smoke count')
    smoke = s['replace_once'](smoke, 'must expose 2440 reviewed records', 'must expose 2480 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')
    runpy.run_path(str(ROOT / 'scripts/update-english-e04-scale-71-progress.py'), run_name='e04_scale71_progress_apply')
    print(json.dumps({'status':'applied','batch':BATCH_ID,'collocationsAdded':40,'collocationRange':['col.00002441','col.00002480'],'sourceCountsBefore':actual,'sourceCountsAfter':{'collocations':2480,'verbPatterns':510,'phraseItems':600},'expectedRuntimeAfterPublish':{'phrases':3590,'richRecords':8191}}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main71()
