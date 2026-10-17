#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
base=runpy.run_path(str(ROOT/'scripts/english-e04-scale-70-common.py'),run_name='e04_scale105_base')
read_json=base['read_json']; write_json=base['write_json']; normalized_key=base['normalized_key']; jaccard=base['jaccard']; digest=base['digest']; replace_once=base['replace_once']
MANIFEST_PATH=ROOT/'content/english/batches/manifest.json'; COL_PATH=ROOT/'content/english/phrases/e04-scale-105-collocations.json'; DECISION_PATH=ROOT/'content/english/reviews/decisions.d/e04-scale-105.json'; PROGRESS_PATH=ROOT/'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID='e04.phrase-pattern-scale-105'; REVIEWED_AT='2026-10-08T10:35:00Z'; REVIEWED_BY='chatgpt-editorial-scale-105'; EXPECTED={'collocations':3800,'verbPatterns':510,'phraseItems':600}; NEAR_DUP_THRESHOLD=0.86
COLLOCATIONS=[]
for index in range(1,5): COLLOCATIONS.extend(read_json(ROOT/f'scripts/e04-scale-105-candidates-part{index}.json')['records'])
if len(COLLOCATIONS)!=40: raise RuntimeError(f'scale-105 candidate count drifted: {len(COLLOCATIONS)}')
def make_record(identifier:int,spec):
    text,meaning,cefr=spec; rid=f'col.{identifier:08d}'
    return {'schemaVersion':1,'id':rid,'text':text,'headwordKeys':[normalized_key(text).split()[0]],'pattern':'verb + noun phrase','meaningVi':meaning,'cefr':cefr,'register':['neutral'],'exampleIds':[],'quality':{'state':'draft','checks':{'schema':{'status':'pass','method':'e04-scale-105-authoring-v1'},'grammar':{'status':'pending','method':'manual-review-required'},'translation':{'status':'pending','method':'manual-review-required'},'naturalness':{'status':'pending','method':'manual-review-required'},'cefr':{'status':'pending','method':'manual-review-required'},'targetStructure':{'status':'pending','method':'manual-review-required'},'exactDuplicate':{'status':'pass','method':'normalized-key-v105'},'nearDuplicate':{'status':'pending','method':'manual-review-required'},'license':{'status':'pending','method':'manual-review-required'}}},'provenance':{'sources':[{'dataset':'project-original','sourceId':rid,'sourceUrl':'content/english/phrases/e04-scale-105-collocations.json','snapshot':'2026-10','license':'LicenseRef-Project-Original','modified':False}],'note':'Project-original controlled E04 scale-up record.'}}
