#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'scripts/apply-english-e04-focused-scale-176.py').read_text(encoding='utf-8')
def replace_once(text:str,old:str,new:str,label:str)->str:
    count=text.count(old)
    if count!=1: raise RuntimeError(f'{label}: expected exactly one source match, found {count}')
    return text.replace(old,new,1)
source=source.replace('scale-176','scale-201').replace('scale176','scale201')
source=replace_once(source,"('if(phrasalVerbCount!==710) errors.push(\"published phrasal-verb activity must expose 710 reviewed records\");','if(phrasalVerbCount!==720) errors.push(\"published phrasal-verb activity must expose 720 reviewed records\");','phrasal assertion')","('if(phrasalVerbCount!==960) errors.push(\"published phrasal-verb activity must expose 960 reviewed records\");','if(phrasalVerbCount!==970) errors.push(\"published phrasal-verb activity must expose 970 reviewed records\");','phrasal assertion')",'phrasal smoke transition')
source=replace_once(source,"('if(chunkCount!==780) errors.push(\"published chunk activity must expose 780 reviewed records\");','if(chunkCount!==795) errors.push(\"published chunk activity must expose 795 reviewed records\");','chunk assertion')","('if(chunkCount!==1155) errors.push(\"published chunk activity must expose 1155 reviewed records\");','if(chunkCount!==1170) errors.push(\"published chunk activity must expose 1170 reviewed records\");','chunk assertion')",'chunk smoke transition')
source=replace_once(source,"('if(idiomCount!==750) errors.push(\"published idiom activity must expose 750 reviewed records\");','if(idiomCount!==765) errors.push(\"published idiom activity must expose 765 reviewed records\");','idiom assertion')","('if(idiomCount!==1125) errors.push(\"published idiom activity must expose 1125 reviewed records\");','if(idiomCount!==1140) errors.push(\"published idiom activity must expose 1140 reviewed records\");','idiom assertion')",'idiom smoke transition')
source=replace_once(source,"'sourceCountsAfter':{'collocations':5000,'verbPatterns':510,'phraseItems':2280}","'sourceCountsAfter':{'collocations':5000,'verbPatterns':510,'phraseItems':3280}",'source count transition')
source=replace_once(source,"'expectedRuntimeAfterPublish':{'phrases':7790,'richRecords':12391}","'expectedRuntimeAfterPublish':{'phrases':8790,'richRecords':13391}",'runtime count transition')
exec(compile(source,str(Path(__file__)),'exec'),{'__name__':'__main__','__file__':__file__})
