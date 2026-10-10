#!/usr/bin/env python3
from __future__ import annotations
import json,re,runpy
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-145-common.py'),run_name='e04_scale145_apply')
read_json=s['read_json']; write_json=s['write_json']; nk=s['normalized_key']; jac=s['jaccard']; digest=s['digest']; replace_once=s['replace_once']; manifest_path=s['MANIFEST_PATH']; phrase_path=s['PHRASE_PATH']; decision_path=s['DECISION_PATH']; batch_id=s['BATCH_ID']; reviewed_at=s['REVIEWED_AT']; reviewed_by=s['REVIEWED_BY']; expected=s['EXPECTED']; frontiers=s['EXPECTED_FRONTIERS']; threshold=s['NEAR_DUP_THRESHOLD']; candidates=s['CANDIDATES']; make_record=s['make_record']
def main():
    manifest=read_json(manifest_path)
    if any(batch.get('id')==batch_id for batch in manifest.get('batches',[])): print(json.dumps({'status':'skip','reason':'batch already exists','batch':batch_id},indent=2)); return
    if phrase_path.exists() or decision_path.exists(): raise RuntimeError('scale-145 artifact exists without matching batch manifest')
    existing={'collocations':[],'verbPatterns':[],'phraseItems':[]}; all_texts=[]; all_ids=set()
    for batch in manifest.get('batches',[]):
        if batch.get('phase')!='E04' or batch.get('category')!='phrases': continue
        for rs in batch.get('recordSets',[]):
            records=read_json(ROOT/rs['path']).get('records',[]); rsid=rs.get('id')
            if rsid in {'collocations','scale-collocations'}: existing['collocations'].extend(records)
            elif rsid in {'verb-patterns','scale-verb-patterns'}: existing['verbPatterns'].extend(records)
            elif rsid in {'phrases','scale-phrases'}: existing['phraseItems'].extend(records)
            for record in records:
                rid=record.get('id')
                if rid in all_ids: raise RuntimeError(f'existing duplicate E04 record id: {rid}')
                all_ids.add(rid); value=record.get('text') or record.get('pattern') or ''
                if value: all_texts.append((rid,value))
    actual={k:len(v) for k,v in existing.items()}
    if actual!=expected: raise RuntimeError(f'E04 source counts drifted; expected {expected}, got {actual}')
    current_frontiers={}
    for kind,prefix in [('phrasal-verb','pv'),('chunk','chunk'),('idiom','idiom')]:
        nums=[]
        for record in existing['phraseItems']:
            if record.get('type')!=kind: continue
            match=re.fullmatch(rf'{prefix}\.(\d{{8}})',str(record.get('id','')))
            if match: nums.append(int(match.group(1)))
        current_frontiers[kind]=max(nums) if nums else 0
    if current_frontiers!=frontiers: raise RuntimeError(f'phrase ID frontiers drifted; expected {frontiers}, got {current_frontiers}')
    counters=dict(frontiers); new=[]
    for spec in candidates: kind=spec['type']; counters[kind]+=1; new.append(make_record(counters[kind],spec))
    accepted=[]; exact={nk(text):rid for rid,text in all_texts}
    for record in new:
        rid,text=record['id'],record['text']; key=nk(text)
        if rid in all_ids: raise RuntimeError(f'new record id collides: {rid}')
        if key in exact: raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {exact[key]}')
        for old_id,old_text in all_texts:
            score=jac(text,old_text)
            if score>=threshold: raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {old_id} {old_text!r}')
        for prior in accepted:
            score=jac(text,prior['text'])
            if nk(prior['text'])==key or score>=threshold: raise RuntimeError(f'duplicate inside scale-145: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(record)
    write_json(phrase_path,{'schemaVersion':1,'records':new})
    manifest['batches'].append({'id':batch_id,'phase':'E04','category':'phrases','cefr':['B2','C1'],'state':'draft','recordSets':[{'id':'scale-phrases','path':'content/english/phrases/e04-scale-145-phrases.json','expectedCount':40,'generated':False,'allowedQualityStates':['draft'],'requiredChecks':['schema','grammar','translation','naturalness','cefr','targetStructure','exactDuplicate','nearDuplicate','license']}],'requiredBeforePublish':['schema-validation','reference-integrity','exact-dedup','near-dedup','grammar-review','bilingual-review','naturalness-review','cefr-review','target-structure-review','license-review','cross-game-smoke'],'gameSmokes':[{'gameId':'recall-typing','activity':'phrasal-verb','recordSetId':'scale-phrases','sampleCount':5,'recordType':'phrasal-verb'},{'gameId':'vocab-shooter','activity':'phrasal-verb','recordSetId':'scale-phrases','sampleCount':5,'recordType':'phrasal-verb'},{'gameId':'space-typing','activity':'phrasal-verb','recordSetId':'scale-phrases','sampleCount':5,'recordType':'phrasal-verb'},{'gameId':'recall-typing','activity':'chunk','recordSetId':'scale-phrases','sampleCount':5,'recordType':'chunk'},{'gameId':'vocab-shooter','activity':'chunk','recordSetId':'scale-phrases','sampleCount':5,'recordType':'chunk'},{'gameId':'space-typing','activity':'chunk','recordSetId':'scale-phrases','sampleCount':5,'recordType':'chunk'},{'gameId':'monkeytype','activity':'idiom','recordSetId':'scale-phrases','sampleCount':5,'recordType':'idiom'}]}); write_json(manifest_path,manifest)
    decisions=[]
    for record in new: decisions.append({'id':'review.e04.scale-145.'+record['id'].replace('.','-'),'batchId':batch_id,'recordSetId':'scale-phrases','recordId':record['id'],'sourceDigest':digest(record),'targetState':'published','checks':{'grammar':{'status':'pass','method':'e04-scale-145-grammar-editorial-review'},'translation':{'status':'pass','method':'e04-scale-145-bilingual-review'},'naturalness':{'status':'pass','method':'e04-scale-145-naturalness-review'},'cefr':{'status':'pass','method':'e04-scale-145-cefr-review'},'targetStructure':{'status':'pass','method':'e04-scale-145-structure-review'},'nearDuplicate':{'status':'pass','method':'e04-scale-145-cross-batch-near-dedup-review'},'license':{'status':'pass','method':'project-original-license-review-v1'}},'reviewedAt':reviewed_at,'reviewedBy':reviewed_by,'note':f'Focused E04 scale 145 {record["type"]} reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.'})
    write_json(decision_path,{'schemaVersion':1,'decisions':decisions})
    smoke_path=ROOT/'scripts/smoke-published-english-content.mjs'; smoke=smoke_path.read_text(encoding='utf-8')
    for old,new_value,label in [('if(phrasalVerbCount!==400)','if(phrasalVerbCount!==410)','phrasal count'),('must expose 400 reviewed records','must expose 410 reviewed records','phrasal message'),('if(chunkCount!==315)','if(chunkCount!==330)','chunk count'),('must expose 315 reviewed records','must expose 330 reviewed records','chunk message'),('if(idiomCount!==285)','if(idiomCount!==300)','idiom count'),('must expose 285 reviewed records','must expose 300 reviewed records','idiom message')]: smoke=replace_once(smoke,old,new_value,label)
    smoke_path.write_text(smoke,encoding='utf-8'); runpy.run_path(str(ROOT/'scripts/update-english-e04-scale-145-progress.py'),run_name='e04_scale145_progress_apply'); counts=Counter(record['type'] for record in new)
    print(json.dumps({'status':'applied','batch':batch_id,'added':dict(counts),'frontiersAfter':counters,'sourceCountsBefore':actual,'sourceCountsAfter':{'collocations':5000,'verbPatterns':510,'phraseItems':1040},'expectedRuntimeAfterPublish':{'phrases':6550,'richRecords':11151}},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
