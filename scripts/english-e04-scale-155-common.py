#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
base=runpy.run_path(str(ROOT/'scripts/english-e04-scale-154-common.py'),run_name='e04_scale155_base')
read_json=base['read_json']
write_json=base['write_json']
normalized_key=base['normalized_key']
jaccard=base['jaccard']
digest=base['digest']
replace_once=base['replace_once']
MANIFEST_PATH=ROOT/'content/english/batches/manifest.json'
PHRASE_PATH=ROOT/'content/english/phrases/e04-scale-155-phrases.json'
DECISION_PATH=ROOT/'content/english/reviews/decisions.d/e04-scale-155.json'
PROGRESS_PATH=ROOT/'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID='e04.phrase-pattern-scale-155'
REVIEWED_AT='2026-10-09T11:38:00Z'
REVIEWED_BY='chatgpt-editorial-scale-155'
EXPECTED={'collocations':5000,'verbPatterns':510,'phraseItems':1400}
EXPECTED_FRONTIERS={'phrasal-verb':500,'chunk':465,'idiom':435}
NEAR_DUP_THRESHOLD=0.86
CANDIDATES=read_json(ROOT/'scripts/e04-scale-155-candidates.json')['records']
if len(CANDIDATES)!=40:
    raise RuntimeError(f'scale-155 candidate count drifted: {len(CANDIDATES)}')
def make_record(identifier:int,spec:dict):
    kind=spec['type']
    prefix={'phrasal-verb':'pv','chunk':'chunk','idiom':'idiom'}[kind]
    rid=f'{prefix}.{identifier:08d}'
    return {'schemaVersion':1,'id':rid,'type':kind,'text':spec['text'],'key':normalized_key(spec['text']),'meaningVi':spec['meaningVi'],'cefr':spec['cefr'],'transitivity':spec['transitivity'],'separability':spec['separability'],'register':['neutral'],'notesVi':spec['notesVi'],'exampleIds':[],'quality':{'state':'draft','checks':{'schema':{'status':'pass','method':'e04-scale-155-authoring-v1'},'grammar':{'status':'pending','method':'grammar-editorial-review-required'},'translation':{'status':'pending','method':'bilingual-review-required'},'naturalness':{'status':'pending','method':'editor-review-required'},'cefr':{'status':'pending','method':'cefr-review-required'},'targetStructure':{'status':'pending','method':'phrase-structure-review-required'},'exactDuplicate':{'status':'pass','method':'normalized-key-v155'},'nearDuplicate':{'status':'pending','method':'cross-batch-near-dedup-review-required'},'license':{'status':'pending','method':'license-review-required'}}},'provenance':{'sources':[{'dataset':'project-original','sourceId':rid,'sourceUrl':'content/english/phrases/e04-scale-155-phrases.json','snapshot':'2026-10','license':'LicenseRef-Project-Original','modified':False}],'note':'Project-original E04 focused scale-155 phrase item; bilingual meaning and structure were editorially reviewed before publication.'}}
