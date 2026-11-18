"""Bàn giao OGG và bảng kiểm phiếu 218; không chứa WAV trung gian."""
from __future__ import annotations

import collections
import csv
import itertools
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal

from build import render
from keys import firefly_v2 as v, firefly_build as old


def write_csv(path, rows, fields=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fields or list(rows[0]),extrasaction='ignore')
        writer.writeheader();writer.writerows(rows)


def deliver(groups,selection,before,src,out,work,evidence):
    if not groups:
        old.write_json(evidence/'verification.json',{'status':'insufficient-source','profiles':0,'selection':selection})
        raise ValueError('Không có bộ nào đủ 70+6 và điểm 6; không dựng bộ rỗng')
    out.mkdir(parents=True,exist_ok=True)
    listen=work/'listen-v2'
    marker=listen/'.firefly-builder.json'
    if listen.exists() and any(listen.iterdir()) and (not marker.exists() or json.loads(marker.read_text()).get('builder')!='keys-firefly/218'):
        raise ValueError('Thư mục nghe không thuộc phiếu 218')
    listen.mkdir(parents=True,exist_ok=True)
    old.write_json(out/'.firefly-builder.json',{'builder':'keys-firefly/218'})
    old.write_json(marker,{'builder':'keys-firefly/218'})
    profiles=[];rows=[];setrows=[];previews=[];comp=collections.defaultdict(list)
    reuse=collections.Counter();pairs=[]
    for order,g in enumerate(groups):
        dest=out/g['id'];dest.mkdir(parents=True,exist_ok=True)
        files=[];sets={'key':[],'space':[]};metsets={'key':[],'space':[]}
        for part,pool in [('key',g['keys']),('space',g['spaces'])]:
            for i,c in enumerate(pool,1):
                # Bộ đọc hiện hành có \\d{2}; tối đa 80 phím nên dùng hai chữ số.
                stem=f'{part}-{i:02d}'
                y=c['audio']*10**((v.TARGET-c['lufs'])/20)
                path=dest/(stem+'.ogg')
                path.write_bytes(render.encode_ogg(y[:,None],v.SR,.6))
                runtime,sr=sf.read(path,dtype='float64')
                met=old.audio_metrics(runtime,c['gate']['muted_intervals_samples'])
                if (sr!=v.SR or runtime.ndim!=1 or met['duration_ms']>(180 if part=='key' else 260)
                    or met['true_peak_dbtp']>-1 or met['background_dbfs']>-60
                    or abs(met['lufs_m_max']-v.TARGET)>.75):
                    raise ValueError(f'{g["id"]}/{stem}: OGG không qua cổng: {met}')
                t=c['take']
                source={'directory':t['folder'],'original_file':t['file'],
                        'sha256':t['provenance']['sha256'],'c2pa_manifest':t['provenance']['c2pa_manifest'],
                        'cut_start_s':c['cut_samples'][0]/v.SR,'cut_end_s':c['cut_samples'][1]/v.SR,
                        'cut_samples':c['cut_samples'],'onset_s':c['onset_sample']/v.SR,
                        'space_like_measured':bool(c['features']['space_like']),
                        'borrowed_for_space':bool(part=='space' and not c['features']['space_like']),
                        'background_at_target_before_gate_dbfs':c['source_floor_at_target_dbfs'],
                        'tail_t60_ms':c['features']['tail']['t60_ms'],'licence':old.LICENCE}
                files.append({'file':path.name,'set':part,'metrics':met,'source':source,
                              'mono':c['mono'],'gate':c['gate'],'sha256':old.sha(path),
                              'processing':{'hpf_hz':30,'hpf_order':2,'hpf_zero_phase':True,
                                            **c['fades'],'silence_pad_ms':20,'gain_db':v.TARGET-c['lufs']}})
                rows.append({'profile':g['id'],'file':path.name,'set':part,
                             **{k:val for k,val in met.items() if k!='quiet_windows'},
                             'source_background_dbfs':c['source_floor_at_target_dbfs'],
                             'source_tail_t60_ms':c['features']['tail']['t60_ms'],
                             'source_uid':c['uid']})
                reuse[c['uid']]+=1
                sets[part].append(runtime);metsets[part].append(met)
        waves=sets['key']+sets['space']
        corr,pair=max((old.corr_max(a,b),(i,j)) for (i,a),(j,b) in itertools.combinations(enumerate(waves),2))
        levels=[f['metrics']['lufs_m_max'] for f in files]
        spread=max(levels)-min(levels)
        if corr>.95 or spread>1.5:raise ValueError(f'{g["id"]}: tương quan {corr}, lệch {spread}')
        kc=float(np.median([m['centroid_hz'] for m in metsets['key']]))
        kd=float(np.median([m['duration_ms'] for m in metsets['key']]))
        if any(m['centroid_hz']>=kc or m['duration_ms']<=kd for m in metsets['space']):
            raise ValueError(f'{g["id"]}: phím cách không trầm và dài hơn')
        # Tâm cuối lấy từ phổ OGG; độ tắt lấy số đo nguồn, độ dài lấy OGG.
        vectors=[]
        for c,y in zip(g['keys'],sets['key']):
            hz,power=v.ff.psd(y)
            vectors.append(v.vector(dict(c,audio=y,centroid=v.ff.centroid(hz,power),bands=v.ff.bands(hz,power))))
        center=np.median(vectors,axis=0)
        preview,schedule=old.phrase(sets)
        if [e['set'] for e in schedule['events']]!=['key']*6+['space']:
            raise ValueError('Preview không đủ 6 phím + 1 cách')
        (dest/'preview.ogg').write_bytes(render.encode_ogg(preview[:,None],v.SR,.6))
        y,sr=sf.read(dest/'preview.ogg')
        pm=old.audio_metrics(y)
        if abs(pm['duration_ms']-1000)>10 or pm['true_peak_dbtp']>-1 or pm['background_dbfs']>-60:
            raise ValueError(f'{g["id"]}: preview vượt cổng')
        compare,_=old.phrase(sets,2.)
        comp[g['family_id']].append(compare)
        measurement={'max_pair_correlation':corr,'max_pair':[files[i]['file'] for i in pair],
                     'lufs_spread_db':spread,'key_centroid_median_hz':kc,'key_duration_median_ms':kd,
                     'min_space_duration_ratio':min(m['duration_ms']/kd for m in metsets['space']),
                     'max_space_centroid_ratio':max(m['centroid_hz']/kc for m in metsets['space']),
                     'timbre_center':center.tolist(),
                     'source_takes':len({c['take']['path'] for c in g['keys']+g['spaces']}),
                     'space_like_measured':sum(c['features']['space_like'] for c in g['spaces']),
                     'space_borrowed':sum(not c['features']['space_like'] for c in g['spaces'])}
        manifest={'schema':'typing-keys-firefly/2','id':g['id'],'name':g['name'],
                  'family':g['family'],'score':g['score'],'score_components':g['score_components'],
                  'status':'owner-approved-source','licence':old.LICENCE,
                  'files':files,'preview':'preview.ogg','preview_metrics':pm,'preview_schedule':schedule,
                  'source_directories':sorted({c['take']['folder'] for c in g['keys']+g['spaces']}),
                  'measurements':measurement,'space_note':'Nguồn không ghi phím vật lý. Nhãn space-like là nhận dạng bằng số đo; các cú khác là mượn trầm/dài trong cùng bộ.',
                  'loudness':{'metric':'LUFS-M max, 400 ms zero-padded','target':v.TARGET},
                  'format':{'runtime':'OGG Vorbis 48 kHz mono quality 0.6'}}
        want={part:[f['file'] for f in files if f['set']==part] for part in ('key','space')}
        if old.kit_files(manifest)!=want:raise ValueError('Manifest không đọc đủ bằng luật kit')
        old.write_json(dest/'keys-manifest.json',manifest)
        profiles.append({k:val for k,val in dict(id=g['id'],name=g['name'],family=g['family'],score=g['score'],
                        manifest=f'{g["id"]}/keys-manifest.json',preview=f'{g["id"]}/preview.ogg',order=order).items()})
        setrows.append({'id':g['id'],'name':g['name'],'family':g['family'],'score':g['score'],
                        'keys':len(sets['key']),'spaces':len(sets['space']),
                        **measurement,'timbre_center':center.tolist()})
        previews.append({'id':g['id'],**{k:val for k,val in pm.items() if k!='quiet_windows'}})
        g['final_center']=center
        print(f'{order+1}/{len(groups)} {g["name"]}: {len(sets["key"])}+{len(sets["space"])}, điểm {g["score"]:.2f}, corr {corr:.4f}',flush=True)
    # Codec không được khiến hai tâm vượt qua ranh giới gần trùng.
    for a,b in itertools.combinations(groups,2):
        d=v.distance(a['final_center'],b['final_center'])
        pairs.append({'a':a['id'],'b':b['id'],'distance':d})
        if d<v.MIN_DISTANCE:raise ValueError(f'Tâm OGG gần trùng: {a["id"]}/{b["id"]}: {d}')
    listen_rows=[]
    for fid,label in v.FAMILIES:
        if not comp[fid]:continue
        path=listen/f'so-sanh-{fid}.mp3'
        old.mp3(np.concatenate(comp[fid]),path)
        y,sr=sf.read(path)
        expected=len(comp[fid])*2
        if abs(len(y)/sr-expected)>.01:raise ValueError('Bài nghe sai thời lượng')
        listen_rows.append({'family':label,'file':str(path.relative_to(ff_repo())),
                            'profiles':len(comp[fid]),'seconds':len(y)/sr,'bytes':path.stat().st_size})
    root={'schema':'typing-keys-firefly/catalogue-2','profiles':profiles,'status':'owner-approved-source',
          'builder':'keys-firefly/218','filename_note':'Hai chữ số để tương thích keyboardFiles hiện tại; mỗi bộ tối đa 80 phím.'}
    old.write_json(out/'keys-manifest.json',root)
    after=v.source_hashes(src)
    if before!=after:raise ValueError('Nguồn thay đổi trong khi dựng')
    size=sum(p.stat().st_size for p in out.rglob('*') if p.is_file())
    audio_size=sum(p.stat().st_size for p in out.rglob('*.ogg'))
    counts=[len(g['keys']) for g in groups];spaces=[len(g['spaces']) for g in groups]
    result={'status':'measured-pass','profiles':len(groups),'requested_profiles':80,
            'shortfall':max(0,80-len(groups)),'target_lufs_m_max':v.TARGET,
            'families':dict(collections.Counter(g['family'] for g in groups)),
            'scores':{'min':min(g['score'] for g in groups),'median':float(np.median([g['score'] for g in groups])),
                      'max':max(g['score'] for g in groups),
                      'histogram':dict(collections.Counter(str(int(g['score']))+'–'+str(int(g['score'])+1) for g in groups))},
            'key_counts':{'min':min(counts),'median':float(np.median(counts)),'max':max(counts)},
            'space_counts':{'min':min(spaces),'median':float(np.median(spaces)),'max':max(spaces)},
            'file_count':len(rows),'unique_source_strokes':len(reuse),'max_stroke_reuse_across_profiles':max(reuse.values()),
            'source_files':len(before),'source_hashes_unchanged':before==after,
            'source_root':str(src),'staging':str(out),'selection':selection,
            'worst':{'key_duration_ms':max(r['duration_ms'] for r in rows if r['set']=='key'),
                     'space_duration_ms':max(r['duration_ms'] for r in rows if r['set']=='space'),
                     'head_ms_max':max(r['head_ms'] for r in rows),'head_ms_min':min(r['head_ms'] for r in rows),
                     'lufs_m_max_min':min(r['lufs_m_max'] for r in rows),'lufs_m_max_max':max(r['lufs_m_max'] for r in rows),
                     'true_peak_dbtp':max(r['true_peak_dbtp'] for r in rows),
                     'background_dbfs':max(r['background_dbfs'] for r in rows),
                     'source_background_dbfs':max(r['source_background_dbfs'] for r in rows),
                     'lufs_spread_db':max(r['lufs_spread_db'] for r in setrows),
                     'max_pair_correlation':max(r['max_pair_correlation'] for r in setrows),
                     'min_timbre_distance':min(p['distance'] for p in pairs) if pairs else None},
            'preview_ms':{'min':min(r['duration_ms'] for r in previews),'max':max(r['duration_ms'] for r in previews)},
            'bytes':{'staging_total':size,'ogg':audio_size,'listen_mp3':sum(r['bytes'] for r in listen_rows)},
            'listen':listen_rows,'descriptive_words':v.WORDS,
            'acceptance':'Đạt số đo, chưa được chủ dự án nghe duyệt. Điểm là ước lượng, không phải điểm nghe.'}
    old.write_json(evidence/'verification.json',result)
    old.write_json(evidence/'source-hashes.json',before)
    old.write_json(evidence/'profiles.json',root)
    write_csv(evidence/'file-metrics.csv',rows)
    write_csv(evidence/'set-metrics.csv',setrows)
    write_csv(evidence/'preview-metrics.csv',previews)
    if pairs:write_csv(evidence/'timbre-distances.csv',pairs)
    old.write_json(evidence/'source-reuse.json',dict(sorted(reuse.items())))
    return result


def ff_repo():
    return v.ff.REPO
