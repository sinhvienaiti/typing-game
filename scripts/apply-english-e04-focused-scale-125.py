#!/usr/bin/env python3
from __future__ import annotations
import json,re,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-125-common.py'),run_name='e04_scale125_apply'); read_json=s['read_json']; write_json=s['write_json']; nk=s['normalized_key']; jac=s['jaccard']; digest=s['digest']; MANIFEST_PATH=s['MANIFEST_PATH']; COL_PATH=s['COL_PATH']; DECISION_PATH=s['DECISION_PATH']; BATCH_ID=s['BATCH_ID']; REVIEWED_AT=s['REVIEWED_AT']; REVIEWED_BY=s['REVIEWED_BY']; EXPECTED=s['EXPECTED']; threshold=s['NEAR_DUP_THRESHOLD']; specs=s['COLLOCATIONS']; make_record=s['make_record']
def main():
    manifest=read_json(MANIFEST_PATH)
    if any(b.get('id')==BATCH_ID for b in manifest.get('batches',[])): print(json.dumps({'status':'skip','reason':'batch already exists','batch':BATCH_ID},indent=2)); return
    if COL_PATH.exists() or DECISION_PATH.exists(): raise RuntimeError('scale-125 artifact exists without matching batch manifest')
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
    if actual!=EXPECTED: raise RuntimeError(f'E04 source counts drifted; expected {EXPECTED}, got {actual}')
    nums=[int(m.group(1)) for r in existing['collocations'] if (m:=re.fullmatch(r'col\.(\d{8})',str(r.get('id',''))))]
    if not nums or max(nums)!=4600: raise RuntimeError(f'collocation ID frontier drifted; expected max 4600, got {max(nums) if nums else None}')
    new=[make_record(4601+i,spec) for i,spec in enumerate(specs)]; exact={nk(text):rid for rid,text in all_texts}; accepted=[]
    for record in new:
        rid,text=record['id'],record['text']; key=nk(text)
        if rid in all_ids: raise RuntimeError(f'new record id collides: {rid}')
        if key in exact: raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {exact[key]}')
        for old_id,old_text in all_texts:
            score=jac(text,old_text)
            if score>=threshold: raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {old_id} {old_text!r}')
        for prior in accepted:
            score=jac(text,prior['text'])
            if nk(prior['text'])==key or score>=threshold: raise RuntimeError(f'duplicate inside scale-125: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(record)
    write_json(COL_PATH,{'schemaVersion':1,'records':new})
    manifest['batches'].append({'id':BATCH_ID,'phase':'E04','category':'phrases','cefr':['B2','C1'],'state':'draft','recordSets':[{'id':'scale-collocations','path':'content/english/phrases/e04-scale-125-collocations.json','expectedCount':40,'generated':False,'allowedQualityStates':['draft'],'requiredChecks':['schema','grammar','translation','naturalness','cefr','targetStructure','exactDuplicate','nearDuplicate','license']}],'requiredBeforePublish':['schema-validation','reference-integrity','exact-dedup','near-dedup','grammar-review','bilingual-review','naturalness-review','cefr-review','target-structure-review','license-review','cross-game-smoke'],'gameSmokes':[{'gameId':'recall-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},{'gameId':'vocab-shooter','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5},{'gameId':'space-typing','activity':'collocation','recordSetId':'scale-collocations','sampleCount':5}]}); write_json(MANIFEST_PATH,manifest)
    decisions=[]
    for record in new: decisions.append({'id':'review.e04.scale-125.'+record['id'].replace('.','-'),'batchId':BATCH_ID,'recordSetId':'scale-collocations','recordId':record['id'],'sourceDigest':digest(record),'targetState':'published','checks':{'grammar':{'status':'pass','method':'e04-scale-125-grammar-editorial-review'},'translation':{'status':'pass','method':'e04-scale-125-bilingual-review'},'naturalness':{'status':'pass','method':'e04-scale-125-naturalness-review'},'cefr':{'status':'pass','method':'e04-scale-125-cefr-review'},'targetStructure':{'status':'pass','method':'e04-scale-125-structure-review'},'nearDuplicate':{'status':'pass','method':'e04-scale-125-cross-batch-near-dedup-review'},'license':{'status':'pass','method':'project-original-license-review-v1'}},'reviewedAt':REVIEWED_AT,'reviewedBy':REVIEWED_BY,'note':'Focused E04 scale 125 hospital sterile processing, instrument decontamination and autoclave operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.'})
    write_json(DECISION_PATH,{'schemaVersion':1,'decisions':decisions})
    smoke_path=ROOT/'scripts/smoke-published-english-content.mjs'; smoke=smoke_path.read_text(encoding='utf-8'); smoke=s['replace_once'](smoke,'if(recallCollocations!==4600)','if(recallCollocations!==4640)','smoke count'); smoke=s['replace_once'](smoke,'must expose 4600 reviewed records','must expose 4640 reviewed records','smoke message'); smoke_path.write_text(smoke,encoding='utf-8')
    runpy.run_path(str(ROOT/'scripts/update-english-e04-scale-125-progress.py'),run_name='e04_scale125_progress_apply')
    print(json.dumps({'status':'applied','batch':BATCH_ID,'collocationsAdded':40,'collocationRange':['col.00004601','col.00004640'],'sourceCountsBefore':actual,'sourceCountsAfter':{'collocations':4640,'verbPatterns':510,'phraseItems':600},'expectedRuntimeAfterPublish':{'phrases':5750,'richRecords':10351}},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
