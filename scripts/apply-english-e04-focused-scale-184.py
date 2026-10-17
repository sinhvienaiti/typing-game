#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'scripts/apply-english-e04-focused-scale-176.py').read_text(encoding='utf-8')
def replace_once(text:str,old:str,new:str,label:str)->str:
    count=text.count(old)
    if count!=1: raise RuntimeError(f'{label}: expected exactly one source match, found {count}')
    return text.replace(old,new,1)
source=source.replace('scale-176','scale-184').replace('scale176','scale184')
source=replace_once(source,"('if(phrasalVerbCount!==710) errors.push(\"published phrasal-verb activity must expose 710 reviewed records\");','if(phrasalVerbCount!==720) errors.push(\"published phrasal-verb activity must expose 720 reviewed records\");','phrasal assertion')","('if(phrasalVerbCount!==790) errors.push(\"published phrasal-verb activity must expose 790 reviewed records\");','if(phrasalVerbCount!==800) errors.push(\"published phrasal-verb activity must expose 800 reviewed records\");','phrasal assertion')",'phrasal smoke transition')
source=replace_once(source,"('if(chunkCount!==780) errors.push(\"published chunk activity must expose 780 reviewed records\");','if(chunkCount!==795) errors.push(\"published chunk activity must expose 795 reviewed records\");','chunk assertion')","('if(chunkCount!==900) errors.push(\"published chunk activity must expose 900 reviewed records\");','if(chunkCount!==915) errors.push(\"published chunk activity must expose 915 reviewed records\");','chunk assertion')",'chunk smoke transition')
source=replace_once(source,"('if(idiomCount!==750) errors.push(\"published idiom activity must expose 750 reviewed records\");','if(idiomCount!==765) errors.push(\"published idiom activity must expose 765 reviewed records\");','idiom assertion')","('if(idiomCount!==870) errors.push(\"published idiom activity must expose 870 reviewed records\");','if(idiomCount!==885) errors.push(\"published idiom activity must expose 885 reviewed records\");','idiom assertion')",'idiom smoke transition')
source=replace_once(source,"'sourceCountsAfter':{'collocations':5000,'verbPatterns':510,'phraseItems':2280}","'sourceCountsAfter':{'collocations':5000,'verbPatterns':510,'phraseItems':2600}",'source count transition')
source=replace_once(source,"'expectedRuntimeAfterPublish':{'phrases':7790,'richRecords':12391}","'expectedRuntimeAfterPublish':{'phrases':8110,'richRecords':12711}",'runtime count transition')
exec(compile(source,str(Path(__file__)),'exec'),{'__name__':'__main__','__file__':__file__})
