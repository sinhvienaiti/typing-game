#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'scripts/english-e04-scale-196-common.py').read_text(encoding='utf-8')
def replace_once(text,old,new,label):
    count=text.count(old)
    if count!=1: raise RuntimeError(f'{label}: expected exactly one source match, found {count}')
    return text.replace(old,new,1)
source=source.replace('scale-196','scale-197').replace('scale196','scale197').replace('v196','v197')
source=replace_once(source,"EXPECTED={'collocations':5000,'verbPatterns':510,'phraseItems':3040}; EXPECTED_FRONTIERS={'phrasal-verb':910,'chunk':1080,'idiom':1050}; NEAR_DUP_THRESHOLD=0.86","EXPECTED={'collocations':5000,'verbPatterns':510,'phraseItems':3080}; EXPECTED_FRONTIERS={'phrasal-verb':920,'chunk':1095,'idiom':1065}; NEAR_DUP_THRESHOLD=0.86",'scale-197 source/frontier expectations')
source=replace_once(source,"REVIEWED_AT='2026-10-11T07:00:00Z'","REVIEWED_AT='2026-10-11T07:55:00Z'",'scale-197 review timestamp')
exec(compile(source,str(Path(__file__)),'exec'),globals())
