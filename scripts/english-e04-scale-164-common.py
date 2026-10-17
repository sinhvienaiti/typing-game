#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
base=runpy.run_path(str(ROOT/'scripts/english-e04-scale-163-common.py'),run_name='e04_scale164_base')
read_json=base['read_json']; write_json=base['write_json']; normalized_key=base['normalized_key']; jaccard=base['jaccard']; digest=base['digest']; replace_once=base['replace_once']
MANIFEST_PATH=ROOT/'content/english/batches/manifest.json'
PHRASE_PATH=ROOT/'content/english/phrases/e04-scale-164-phrases.json'
DECISION_PATH=ROOT/'content/english/reviews/decisions.d/e04-scale-164.json'
PROGRESS_PATH=ROOT/'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID='e04.phrase-pattern-scale-164'
REVIEWED_AT='2026-10-10T01:38:00Z'
REVIEWED_BY='chatgpt-editorial-scale-164'
EXPECTED={'collocations':5000,'verbPatterns':510,'phraseItems':1760}
EXPECTED_FRONTIERS={'phrasal-verb':590,'chunk':600,'idiom':570}
NEAR_DUP_THRESHOLD=0.86
_base_candidates=read_json(ROOT/'scripts/e04-scale-164-candidates.json')['records']
_replacements=read_json(ROOT/'scripts/e04-scale-164-candidate-replacements.json').get('replacements',{})
CANDIDATES=[_replacements.get(spec['text'],spec) for spec in _base_candidates]
if len(CANDIDATES)!=40: raise RuntimeError(f'scale-164 candidate count drifted: {len(CANDIDATES)}')
if len({spec['text'] for spec in CANDIDATES})!=40: raise RuntimeError('scale-164 replacement overlay produced duplicate candidate text')
def make_record(identifier:int,spec:dict):
    kind=spec['type']; prefix={'phrasal-verb':'pv','chunk':'chunk','idiom':'idiom'}[kind]; rid=f'{prefix}.{identifier:08d}'
    return {'schemaVersion':1,'id':rid,'type':kind,'text':spec['text'],'key':normalized_key(spec['text']),'meaningVi':spec['meaningVi'],'cefr':spec['cefr'],'transitivity':spec['transitivity'],'separability':spec['separability'],'register':['neutral'],'notesVi':spec['notesVi'],'exampleIds':[],'quality':{'state':'draft','checks':{'schema':{'status':'pass','method':'e04-scale-164-authoring-v1'},'grammar':{'status':'pending','method':'grammar-editorial-review-required'},'translation':{'status':'pending','method':'bilingual-review-required'},'naturalness':{'status':'pending','method':'editor-review-required'},'cefr':{'status':'pending','method':'cefr-review-required'},'targetStructure':{'status':'pending','method':'phrase-structure-review-required'},'exactDuplicate':{'status':'pass','method':'normalized-key-v164'},'nearDuplicate':{'status':'pending','method':'cross-batch-near-dedup-review-required'},'license':{'status':'pending','method':'license-review-required'}}},'provenance':{'sources':[{'dataset':'project-original','sourceId':rid,'sourceUrl':'content/english/phrases/e04-scale-164-phrases.json','snapshot':'2026-10','license':'LicenseRef-Project-Original','modified':False}],'note':'Project-original E04 focused scale-164 phrase item; bilingual meaning and structure were editorially reviewed before publication.'}}
