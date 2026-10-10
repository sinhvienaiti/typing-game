#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-181-common.py'),run_name='e04_scale181_preflight')
manifest=s['read_json'](s['MANIFEST_PATH']); nk=s['normalized_key']; jac=s['jaccard']; threshold=s['NEAR_DUP_THRESHOLD']; candidates=s['CANDIDATES']; existing=[]; ids=set()
for batch in manifest.get('batches',[]):
    if batch.get('phase')!='E04' or batch.get('category')!='phrases': continue
    for rs in batch.get('recordSets',[]):
        for record in s['read_json'](ROOT/rs['path']).get('records',[]):
            rid=record.get('id')
            if rid in ids: raise RuntimeError(f'existing duplicate E04 record id: {rid}')
            ids.add(rid); value=record.get('text') or record.get('pattern') or ''
            if value: existing.append((rid,value))
exact_map={}
for rid,text in existing: exact_map.setdefault(nk(text),[]).append(rid)
conflicts=[]
for spec in candidates:
    text=spec['text']; key=nk(text); exact=exact_map.get(key,[]); near=[]
    for old_id,old_text in existing:
        score=jac(text,old_text)
        if score>=threshold and nk(old_text)!=key: near.append({'id':old_id,'text':old_text,'score':round(score,3)})
    if exact or near: conflicts.append({'type':spec['type'],'text':text,'exactIds':exact,'near':near})
for left in range(len(candidates)):
    for right in range(left+1,len(candidates)):
        score=jac(candidates[left]['text'],candidates[right]['text'])
        if nk(candidates[left]['text'])==nk(candidates[right]['text']) or score>=threshold:
            conflicts.append({'text':candidates[left]['text'],'insideBatchNear':{'text':candidates[right]['text'],'score':round(score,3)}})
print(json.dumps({'candidateCount':len(candidates),'existingE04Texts':len(existing),'threshold':threshold,'conflictCount':len(conflicts),'conflicts':conflicts},ensure_ascii=False,indent=2))
if conflicts: raise SystemExit(1)
