#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-120-common.py'),run_name='e04_scale120_preflight'); manifest=s['read_json'](s['MANIFEST_PATH']); nk=s['normalized_key']; jac=s['jaccard']; threshold=s['NEAR_DUP_THRESHOLD']; candidates=s['COLLOCATIONS']; existing=[]; ids=set()
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
for index,spec in enumerate(candidates,start=4401):
    text=spec[0]; key=nk(text); exact=exact_map.get(key,[]); near=[]
    for old_id,old_text in existing:
        score=jac(text,old_text)
        if score>=threshold and nk(old_text)!=key: near.append({'id':old_id,'text':old_text,'score':round(score,3)})
    if exact or near: conflicts.append({'candidateId':f'col.{index:08d}','text':text,'exactIds':exact,'near':near})
for left in range(len(candidates)):
    for right in range(left+1,len(candidates)):
        score=jac(candidates[left][0],candidates[right][0])
        if score>=threshold: conflicts.append({'candidateId':f'col.{4401+left:08d}','text':candidates[left][0],'insideBatchNear':{'candidateId':f'col.{4401+right:08d}','text':candidates[right][0],'score':round(score,3)}})
print(json.dumps({'candidateCount':len(candidates),'existingE04Texts':len(existing),'threshold':threshold,'conflictCount':len(conflicts),'conflicts':conflicts},ensure_ascii=False,indent=2))
if conflicts: raise SystemExit(1)
