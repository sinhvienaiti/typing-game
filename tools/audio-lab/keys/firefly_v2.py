"""Phiếu 218: cắt nguồn Firefly chỉ đọc, gom theo âm sắc, đo bản Vorbis cuối.

Không sinh âm, đổi cao độ, kéo dài hay EQ tạo màu. Bản 189 giữ nguyên.
"""
from __future__ import annotations

import collections
import hashlib
import inspect
import itertools
import json
import math
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal
from scipy.cluster.vq import kmeans2

from build import measure, render
from keys import firefly as ff, firefly_build as old

SR = old.SR
WORK = ff.REPO / 'tmp/keys-firefly'
STAGING = WORK / 'staging-v2/keys-firefly'
EVIDENCE = ff.REPO / 'docs/codex-queue/218'
FAMILIES = [('deep', 'Deep'), ('warm', 'Warm'), ('rounded', 'Rounded'),
            ('solid', 'Solid'), ('crisp', 'Crisp'), ('clear', 'Clear'), ('bright-clack', 'Bright Clack')]
WORDS = ('Velvet Amber Cedar Pebble Slate Silk Copper Walnut Moss Ember Marble Oak '
         'Pearl Stone Linen Maple Birch Rain Brook Reed Quartz Breeze Willow Ash '
         'Satin Clay Flint Crystal Silver Ivory Dune Fern Grove Meadow River '
         'Cove Frost Glade Dawn Drift Cloud Mist Shell Willowcrest Opal Jasper '
         'Topaz Garnet Onyx Coral Bronze Steel Granite Basalt Sand Laurel Aspen '
         'Hazel Acorn Pine Spruce Juniper Olive Almond Chestnut Cinder Glow '
         'Spark Ripple Wave Cascade Dew Snow Ice Winter Spring Summer Autumn '
         'Twilight Moonlight Starlight Sunlight Halo Beam Gleam Glint Shimmer '
         'Chime Echo Whisper Murmur Rustle Patter Cadence Tempo Rhythm Pulse '
         'Orbit Prism Facet Lattice Mosaic Canvas Loom Thread Weave Ribbon').split()
TARGET = -36.0
MIN_DISTANCE = .50
MAX_RADIUS = 1.35
CACHE_VERSION = 1


def guard(src, out, work, evidence):
    source = src.resolve()
    destinations = [p.resolve() for p in (out, work, evidence)]
    for dest in destinations:
        if dest == source or source in dest.parents or dest in source.parents:
            raise ValueError(f'Đầu ra chồng nguồn: {dest}')
    marker = out / '.firefly-builder.json'
    if out.exists() and any(out.iterdir()):
        if not marker.exists() or json.loads(marker.read_text()).get('builder') != 'keys-firefly/218':
            raise ValueError(f'Đầu ra không thuộc phiếu 218: {out}')


def eligible(f):
    """Nhẹ hơn 189 ở attack và rattle; vẫn yêu cầu detector xác nhận tách sạch."""
    return (f['clean'] and not f.get('clip_samples') and 30 <= f['window_ms'] <= 240
            and f['main_ms'] <= 40 and f['attack_ms'] <= 40
            and f['next_press_ms'] >= f['window_ms'] + 2
            and (f['tail']['t60_ms'] is None or f['tail']['t60_ms'] <= 160))


def vector(c):
    """Khoảng cách RMS: 0,25 octave trọng tâm; 3 dB/dải; 0,5 octave dài/tắt."""
    decay = c['features']['tail']['t60_ms']
    return np.array([math.log2(max(c['centroid'], 20))/.25,
                     *[c['bands'][k]/3 for k, *_ in ff.BANDS],
                     math.log2(max(decay if decay is not None else 40, 10))/.5,
                     math.log2(len(c['audio'])/SR*1000)/.5])


def distance(a, b):
    return float(np.sqrt(np.mean((np.asarray(a)-np.asarray(b))**2)))


def source_hashes(src):
    return {str(p.relative_to(src)): old.sha(p) for _, paths in ff.list_sources(src) for p in paths}


def noise_floor(y):
    # Phân vị 10 của các cửa sổ 5 ms: bỏ phần đuôi cú trước khỏi ước lượng nền.
    values=[ff._lvl(y[a:a+240]) for a in range(0,len(y)-239,48)]
    return float(np.percentile(values,10)) if values else ff._lvl(y)


def prepare(data, work):
    """Cache theo hash nguồn + phiên bản mã; xử lý mỗi take đúng một lần."""
    cache = work/'build-v2-cache'
    cache.mkdir(parents=True, exist_ok=True)
    candidates, stats = [], collections.Counter()
    for ti, t in enumerate(data['files']):
        tag = t['provenance']['sha256']
        meta, audio = cache/(tag+'.json'), cache/(tag+'.npz')
        signature = hashlib.sha256((inspect.getsource(prepare)+inspect.getsource(eligible)+inspect.getsource(noise_floor)+inspect.getsource(vector)+inspect.getsource(old.quiet_gate)+inspect.getsource(old.fold_mono)+inspect.getsource(ff.detect)+str(TARGET)).encode()).hexdigest()
        rows = None
        if meta.exists() and audio.exists():
            saved = json.loads(meta.read_text())
            if saved.get('signature') == signature and saved.get('version') == CACHE_VERSION:
                rows = saved['rows']
                with np.load(audio) as clips:
                    for i, c in enumerate(rows):
                        c['audio'] = clips[str(i)].astype(float)
        if rows is None:
            raw, sr = sf.read(t['path'], always_2d=True, dtype='float64')
            if sr != SR:
                raise ValueError('Nguồn không phải 48 kHz')
            m, _, _ = ff.load(Path(t['path']))
            presses, _, _ = ff.detect(m, t['id'])
            lookup = {round(p['onset']/48, 1): p for p in presses}
            filtered = signal.sosfiltfilt(signal.butter(2, 30, 'high', fs=SR, output='sos'), raw, axis=0)
            rows, rejected = [], collections.Counter()
            for f in t['strokes']:
                if not eligible(f):
                    rejected['survey_gate'] += 1
                    continue
                p = lookup.get(f['t_ms'])
                if p is None or not p['clean']:
                    rejected['redetect'] += 1
                    continue
                a, b, onset = p['a'], p['b'], p['onset']
                if np.any(np.abs(raw[a:b]) >= .999):
                    rejected['raw_clip'] += 1
                    continue
                pre = raw[max(0, onset-1440):max(1, onset-144)]
                if len(pre) < 240:
                    rejected['short_pre'] += 1
                    continue
                _, mono = old.fold_mono(raw[a:b], pre)
                channel = filtered.mean(axis=1) if mono['method']=='mid' else filtered[:, 0 if mono['method']=='left' else -1]
                # Nền đo riêng, không coi phần thân đang kêu là nhiễu.
                quiet = pre.mean(axis=1) if mono['method']=='mid' else pre[:, 0 if mono['method']=='left' else -1]
                y, gate = old.quiet_gate(channel[a:b].copy(), float(np.sqrt(np.mean(quiet**2))))
                n_in = min(48, onset-a)
                if n_in > 1:
                    y[:n_in] *= np.sin(np.linspace(0, np.pi/2, n_in))**2
                n_out = min(576, len(y)//5)
                y[-n_out:] *= np.cos(np.linspace(0, np.pi/2, n_out))**2
                y = np.r_[y, np.zeros(960)]
                lm, tp = measure.lufs_m_max(y,SR), measure.true_peak_db(y,SR)
                gain = TARGET-lm
                # Cổng nền nguồn ở mức bàn giao, trước khi lặng hóa.
                post = channel[b:min(p['next']-144,b+1440)]
                floor = max(noise_floor(quiet), noise_floor(post) if len(post)>=480 else -200)+gain
                if floor > -60:
                    rejected['source_floor'] += 1
                    continue
                if tp+gain > -1.8:
                    rejected['crest_headroom'] += 1
                    continue
                if len(y)>12480:
                    rejected['duration'] += 1
                    continue
                freqs, power = ff.psd(y)
                rows.append({'audio': y, 'features': f, 'centroid': ff.centroid(freqs,power),
                             'bands': ff.bands(freqs,power), 'mono': mono, 'gate': gate,
                             'fades': {'fade_in_ms':n_in/48,'fade_out_ms':n_out/48},
                             'cut_samples':[a,b], 'onset_sample':onset, 'lufs':lm, 'tp':tp,
                             'source_floor_at_target_dbfs':floor})
            np.savez_compressed(audio, **{str(i):c['audio'].astype('float32') for i,c in enumerate(rows)})
            old.write_json(meta, {'version':CACHE_VERSION,'signature':signature,
                                 'rows':[{k:v for k,v in c.items() if k!='audio'} for c in rows],
                                 'rejected':dict(rejected)})
        for c in rows:
            c['take'] = t
            c['uid'] = t['id']+':'+str(c['onset_sample'])
            c['v'] = vector(c)
        candidates.extend(rows)
        stats.update(json.loads(meta.read_text())['rejected'])
        if (ti+1)%20==0 or ti+1==len(data['files']):
            print(f'Chuẩn bị {ti+1}/{len(data["files"])} take: {len(candidates)} cú qua cổng',flush=True)
    return candidates, dict(stats)


def unique(pool, n, existing=(), correlate=None):
    chosen = []
    for c in pool:
        if all(c['uid']!=p['uid'] and (correlate(c,p) if correlate else old.corr_max(c['audio'],p['audio'])) <= .94 for p in [*existing,*chosen]):
            chosen.append(c)
        if len(chosen)==n:
            break
    return chosen


def score_set(keys, spaces, maxcorr):
    allc = keys+spaces
    center = np.median([c['v'] for c in keys],axis=0)
    # Mỗi thành phần nằm trong [0,1]; điểm chỉ là ước lượng từ số đo.
    clean = float(np.mean([np.clip(1-max(0,c['features']['attack_ms']-3)/15,0,1) for c in allc]))
    even = float(np.clip(1-np.mean([distance(c['v'],center) for c in keys])/2,0,1))
    repeat = float(np.clip((.95-maxcorr)/.55,0,1))
    noise = float(np.mean([np.clip((-c['source_floor_at_target_dbfs']-60)/20,0,1) for c in allc]))
    tail = float(np.mean([np.clip(1-max(0,(c['features']['tail']['t60_ms'] or 80)-60)/160,0,1) for c in allc]))
    components = dict(cleanliness=clean, consistency=even, repetition=repeat, background=noise, tail=tail)
    score = 10*(.25*clean+.25*even+.20*repeat+.15*noise+.15*tail)
    return round(score,4), components


def propose(candidates):
    """Mỗi take sinh tối đa ba tâm; mỗi bộ lấy từ tối đa tám take gần tâm."""
    correlation_cache={}
    def correlate(a,b):
        pair=tuple(sorted((a['uid'],b['uid'])))
        if pair not in correlation_cache:
            correlation_cache[pair]=old.corr_max(a['audio'],b['audio'])
        return correlation_cache[pair]
    matrix = np.array([c['v'] for c in candidates])
    takes = collections.defaultdict(list)
    for i,c in enumerate(candidates):
        takes[c['take']['path']].append(i)
    seeds=[]
    for path, indices in takes.items():
        ix=[i for i in indices if len(candidates[i]['audio'])<=8640]
        if len(ix)<4:
            continue
        v=matrix[ix]
        seeds.append((np.median(v,axis=0),candidates[ix[0]]['take']['folder'],path))
        if len(ix)>=12:
            means, labels = kmeans2(v,3,iter=15,minit='++',seed=218,missing='warn')
            seeds.extend((np.median(v[labels==j],axis=0), candidates[ix[0]]['take']['folder'],path)
                         for j in range(3) if np.sum(labels==j)>=4)
    # Phủ thêm các sắc thái trong take: thêm tâm thật khi cách mọi tâm đã có ≥0,3.
    for path,indices in takes.items():
        local=[s[0] for s in seeds if s[2]==path]
        ix=[i for i in indices if len(candidates[i]['audio'])<=8640]
        for i in sorted(ix,key=lambda j:candidates[j]['uid']):
            if not local or min(distance(matrix[i],s) for s in local)>=.3:
                local.append(matrix[i])
                seeds.append((matrix[i],candidates[i]['take']['folder'],path))
    print(f'Thử {len(seeds)} tâm từ {len(takes)} take',flush=True)
    proposals, rejects=[],collections.Counter()
    for si,(seed,folder,path) in enumerate(seeds):
        if si%100==0:
            print(f'Tâm {si}/{len(seeds)}: {len(proposals)} bộ ứng viên',flush=True)
        ds=np.sqrt(np.mean((matrix-seed)**2,axis=1))
        near=[i for i in np.argsort(ds) if ds[i]<=MAX_RADIUS
              and abs(np.log2(candidates[i]['centroid']/2**(seed[0]*.25)))<=.65]
        # Ưu tiên cùng thư mục, sau đó take gần nhất; không gom bắc cầu.
        count=collections.Counter(candidates[i]['take']['path'] for i in near if len(candidates[i]['audio'])<=8640)
        same=[p for p in count if candidates[takes[p][0]]['take']['folder']==folder]
        available=same if sum(sorted((count[p] for p in same),reverse=True)[:8])>=80 else list(count)
        paths=sorted(available,key=lambda p:(-count[p],candidates[takes[p][0]]['take']['folder']!=folder,
                                              np.median(ds[takes[p]]),p))[:8]
        pool=[candidates[i] for i in near if candidates[i]['take']['path'] in paths]
        # Dành cú trầm/dài nhất cho cách trước khi chọn phím.
        kp=[c for c in pool if len(c['audio'])<=8640]
        if len(kp)<70:
            rejects['fewer_70_keys']+=1;continue
        medc=float(np.median([c['centroid'] for c in kp]))
        medd=float(np.median([len(c['audio']) for c in kp]))
        sp=[c for c in pool if c['centroid']<medc*.95 and len(c['audio'])>medd*1.05]
        sp.sort(key=lambda c:(not c['features']['space_like'],c['centroid']/medc-len(c['audio'])/medd,c['uid']))
        spaces=unique(sp,8,correlate=correlate)
        if len(spaces)<6:
            rejects['fewer_6_spaces']+=1;continue
        space_ids={c['uid'] for c in spaces}
        kp=[c for c in kp if c['uid'] not in space_ids]
        kp.sort(key=lambda c:(distance(c['v'],seed),-ff.stroke_quality(c['features']),c['uid']))
        chosen=unique(kp,80,spaces,correlate=correlate)
        if len(chosen)<70:
            rejects['unique_keys']+=1;continue
        kc=float(np.median([c['centroid'] for c in chosen]));kd=float(np.median([len(c['audio']) for c in chosen]))
        spaces=[c for c in spaces if c['centroid']<kc*.95 and len(c['audio'])>kd*1.05]
        if len(spaces)<6:
            rejects['space_relative']+=1;continue
        maxcorr=max(correlate(a,b) for a,b in itertools.combinations(chosen+spaces,2))
        score,components=score_set(chosen,spaces,maxcorr)
        if score<6:
            rejects['score_below_6']+=1;continue
        center=np.median([c['v'] for c in chosen],axis=0)
        proposals.append({'keys':chosen,'spaces':spaces,'center':center,'score':score,
                          'score_components':components,'maxcorr':maxcorr,'centroid':kc})
        if (si+1)%50==0:
            print(f'Tâm {si+1}/{len(seeds)}: {len(proposals)} bộ ứng viên',flush=True)
    # Giữ bộ có điểm cao hơn nếu tâm gần trùng; so với TẤT CẢ bộ đã nhận.
    proposals.sort(key=lambda g:(-g['score'],g['centroid'],g['keys'][0]['uid']))
    accepted=[]
    for g in proposals:
        if all(distance(g['center'],p['center'])>=MIN_DISTANCE+.02 for p in accepted):
            accepted.append(g)
        else:
            rejects['near_duplicate']+=1
    return accepted,{'seeds':len(seeds),'qualified_proposals':len(proposals),'rejected':dict(rejects)}


def assign_names(groups, anchors):
    """Gần phổ 189 nhất; id cũ dành cho điểm cao nhất của từng họ."""
    for g in groups:
        # Họ 189 là mốc phổ, không chỉ thứ hạng độ sáng của lô mới.
        g['family_id']=min(anchors,key=lambda k: distance(g['center'][:7],anchors[k]))
    result=[]
    for fid,label in FAMILIES:
        members=sorted([g for g in groups if g['family_id']==fid],key=lambda g:(-g['score'],g['centroid']))
        for i,g in enumerate(members):
            if i>=len(WORDS):
                raise ValueError('Hết từ mô tả')
            g.update(id=fid if i==0 else fid+'-'+WORDS[i].lower(),name=label+' '+WORDS[i],family=label)
            result.append(g)
    return result


def anchors_189():
    root=WORK/'staging/keys-firefly'
    anchors={}
    for fid,_ in FAMILIES:
        man=json.loads((root/fid/'keys-manifest.json').read_text())
        vectors=[]
        for f in man['files']:
            if f['set']!='key':continue
            y,sr=sf.read(root/fid/f['file'])
            hz,p=ff.psd(y)
            vectors.append([math.log2(ff.centroid(hz,p))/.25,*[ff.bands(hz,p)[k]/3 for k,*_ in ff.BANDS]])
        anchors[fid]=np.median(vectors,axis=0)
    return anchors


def build(src=ff.SRC,survey=ff.OUT,out=STAGING,work=WORK,evidence=EVIDENCE,prepare_only=False):
    src,survey,out,work,evidence=map(Path,(src,survey,out,work,evidence))
    guard(src,out,work,evidence)
    data=json.loads((survey/'features.json').read_text())
    if Path(data['source']).resolve()!=src.resolve():raise ValueError('Khảo sát khác nguồn')
    before=source_hashes(src)
    expected={str(Path(t['folder'])/t['file']):t['provenance']['sha256'] for t in data['files']}
    if before!=expected:raise ValueError('Nguồn khác mã băm khảo sát')
    candidates,stats=prepare(data,work)
    old.write_json(evidence/'preparation.json',{'candidates':len(candidates),'rejected':stats,
                   'by_folder':dict(collections.Counter(c['take']['folder'] for c in candidates))})
    if prepare_only:return
    groups,selection=propose(candidates)
    groups=assign_names(groups,anchors_189())
    return deliver(groups,selection,before,src,out,work,evidence)


def deliver(groups,selection,before,src,out,work,evidence):
    """Ghi lựa chọn trước khi encode để có bằng chứng nếu cổng cuối từ chối."""
    old.write_json(evidence/'selection.json',{'selection':selection,'count':len(groups),
        'profiles':[{'id':g['id'],'name':g['name'],'family':g['family'],'score':g['score'],
                     'keys':len(g['keys']),'spaces':len(g['spaces']),
                     'center':g['center'].tolist(),'centroid':g['centroid'],
                     'takes':sorted({c['take']['path'] for c in g['keys']+g['spaces']})} for g in groups]})
    from keys.firefly_v2_delivery import deliver as write_delivery
    return write_delivery(groups,selection,before,src,out,work,evidence)
