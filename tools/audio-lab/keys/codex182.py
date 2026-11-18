"""Phiếu 182: dựng lại tiếng phím cục bộ, không tải âm hay ghi vào thư mục nguồn.

Chạy bằng venv Audio Lab, từ repo cha:
  MPLCONFIGDIR=tmp/keys-codex/cache PYTHONDONTWRITEBYTECODE=1 \
    ~/AudioLab/.venv/bin/python -B tools/audio-lab/keys/codex182.py build

Các cổng kỹ thuật chỉ xác nhận vệ sinh/định dạng, không xác nhận chất liệu hay mức 9.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import re
import subprocess
from pathlib import Path

import numpy as np
import pyloudnorm as pyln
import soundfile as sf
import soxr
from scipy import ndimage, signal

SR = 48000
REPO = Path(__file__).resolve().parents[3]
OUT = REPO / 'tmp/keys-codex'
DOC = REPO / 'docs/codex-queue/182'
SOURCE = Path('/Users/toandx/AudioLab/work/_keys')
# Các hướng dưới đây là mục tiêu xử lý, không phải lời khẳng định về bàn phím nguồn.
PROFILES = {
    'creamy': dict(name='Creamy Linear', source='creamy', body=3., harsh=-4., shelf=-15., lp=6800., hz=260.),
    'thock': dict(name='Deep Thock', source='thock', body=4., harsh=-5., shelf=-18., lp=6200., hz=230.),
    'marbly': dict(name='Marbly', source='creamy', body=2., harsh=-2., shelf=-12., lp=7600., hz=340.),
    # Giữ nguồn tuyến tính: switch clicky không phải clack của keycap ABS dày.
    'clack': dict(name='Clean Clack', source='creamy', body=2., harsh=-1., shelf=-9., lp=9000., hz=300.),
    'dome': dict(name='Soft Dome', source='dome', body=2., harsh=-6., shelf=-20., lp=5600., hz=300.),
}
BAD_FLAGS = {'hf_hiss', 'phasey_swirl', 'noise_floor', 'pitch_wobble', 'decoder_comb'}


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def db(x):
    # Sàn hiển thị hữu hạn để JSON hợp chuẩn; -180 nghĩa là dưới sàn đo.
    return float(20 * np.log10(max(float(x), 1e-9)))


def momentary(x):
    z = np.pad(np.asarray(x), (SR // 2, SR // 2))
    for f in pyln.Meter(SR)._filters.values():
        z = signal.lfilter(f.b, f.a, z)
    n = int(.4 * SR)
    c = np.r_[0., np.cumsum(z * z)]
    return float(-.691 + 10 * np.log10(max(np.max(c[n:] - c[:-n]) / n, 1e-20)))


def peak(x):
    return db(np.max(np.abs(signal.resample_poly(x, 8, 1))))


def bell(hz, gain, q=.8):
    A = 10 ** (gain / 40)
    w = 2 * np.pi * hz / SR
    a = np.sin(w) / (2 * q)
    return signal.tf2sos([1+a*A, -2*np.cos(w), 1-a*A], [1+a/A, -2*np.cos(w), 1-a/A])


def shelf(hz, gain):
    A = 10 ** (gain / 40)
    w = 2 * np.pi * hz / SR
    c, s = np.cos(w), np.sin(w)
    a = s / np.sqrt(2)
    z = 2 * np.sqrt(A) * a
    b = [A*((A+1)+(A-1)*c+z), -2*A*((A-1)+(A+1)*c), A*((A+1)+(A-1)*c-z)]
    d = [(A+1)-(A-1)*c+z, 2*((A-1)-(A+1)*c), (A+1)-(A-1)*c-z]
    return signal.tf2sos(b, d)


def runs(mask):
    d = np.diff(np.r_[False, mask, False].astype(int))
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


def clean_stroke(x, profile, release_sample=None):
    """HPF/EQ nhân quả + expander, không đảo pha, chorus, pitch hay thêm lớp âm.

    Không dùng mặt nạ STFT biến thiên: tránh tiếng chim/rung phổ khi gate mạnh.
    Hạ dải trên bằng shelf và LPF, giữ phần thân thật có sẵn trong nguồn.
    Đóng những khoảng lặng có bằng chứng >=4 ms; fade 1 ms giữ nhấn/nhả.
    """
    p = PROFILES[profile]
    x = np.asarray(x, dtype=float)
    if not len(x) or np.max(np.abs(x)) < 1e-10:
        raise ValueError('Nguồn lặng')
    y = signal.sosfilt(signal.butter(2, 65, 'highpass', fs=SR, output='sos'), x)
    y = signal.sosfilt(bell(p['hz'], p['body']), y)
    y = signal.sosfilt(bell(1700, p['harsh'], .9), y)
    y = signal.sosfilt(shelf(3400, p['shelf']), y)
    y = signal.sosfilt(signal.butter(3, p['lp'], fs=SR, output='sos'), y)
    env = np.sqrt(ndimage.uniform_filter1d(y*y, 96, mode='constant'))
    rel = 20*np.log10(np.maximum(env, 1e-12) / max(env.max(), 1e-12))
    gain = 10 ** (np.clip((rel + 30) * 2, -60, 0) / 20)
    gain = ndimage.gaussian_filter1d(gain, 12)
    protected = np.zeros(len(y), dtype=bool)
    if release_sample is not None:
        # Upstroke nhỏ hơn bottom-out: không nhầm nó với nền để gate mất.
        a = max(0, int(release_sample)-96)
        b = min(len(y), int(release_sample)+1680)
        protected[a:b] = True
        protect_gain = ndimage.gaussian_filter1d(protected.astype(float),24)
        gain = np.maximum(gain, protect_gain)
    y *= gain
    quiet = []
    # Giữ nguyên các khoảng lặng tự nhiên, không lấy một khoảng có tiếng làm nền.
    for a, b in runs((rel < -38) & ~protected):
        if b-a >= 192:
            a1, b1 = a+48, b-48
            if b1 <= a1:
                continue
            y[a:a1] *= np.linspace(1, 0, a1-a)
            y[a1:b1] = 0
            y[b1:b] *= np.linspace(0, 1, b-b1)
            quiet.append([int(a1), int(b1)])
    # Bản cắt nguồn đã có fade đuôi; thêm ramp chỉ ở 8 ms cuối và 3 ms lặng.
    n = min(len(y), 528)
    y[-n:-144] *= np.linspace(1, 0, n-144)
    y[-144:] = 0
    # Cắt lượng trễ do lọc, chỉ trước ngưỡng -40 dB, giữ 0,5 ms pre-roll.
    active = np.flatnonzero(np.abs(y) >= np.max(np.abs(y)) * .01)
    if not len(active):
        raise ValueError('Nguồn lặng')
    trim = max(0, int(active[0])-24)
    y = y[trim:]
    quiet = [[max(0,a-trim), b-trim] for a,b in quiet if b-trim > 0]
    quiet.append([len(y)-144, len(y)])
    y[:12] *= np.linspace(0, 1, 12)
    y *= 10 ** ((-27 - momentary(y)) / 20)
    return y, {'trim_samples': trim, 'quiet_windows_samples': quiet,
               'chain': 'HPF 65 Hz bậc 2; bell thân; bell 1,7 kHz; shelf 3,4 kHz; LPF bậc 3; expander 1:3; gate lặng có fade 1 ms; fade đuôi; gain tới −27 LUFS-M',
               'parameters': p}


def spectrum(x):
    # PSD Welch cùng cửa sổ/FFT, trung bình công suất; không chuẩn hóa riêng từng phổ.
    return signal.welch(x, SR, nperseg=min(1024, len(x)), nfft=4096)


def measures(x, quiet):
    f, P = spectrum(x)
    low = P[(f >= 150) & (f < 400)].sum()
    hi = P[(f >= 4000) & (f < 8000)].sum()
    rms1 = np.sqrt(np.mean(np.pad(x, (0, (-len(x)) % 48)).reshape(-1,48)**2, axis=1))
    main = int(np.flatnonzero(rms1 >= rms1.max() * .5)[0])
    on = int(np.flatnonzero(np.abs(x) >= np.abs(x).max() * .01)[0])
    edge_floor = max([db(np.sqrt(np.mean(x[a:b]**2))) for a,b in quiet if b>a] or [-180.])
    # Vorbis trải đuôi của transient qua biên block: đo nền ở giữa khoảng lặng
    # >=25 ms, gạt 10 ms mỗi biên. Giữ riêng mức sát biên, không giấu nó.
    # 3 ms cuối là đoạn lặng thực được fade trước đó; không thêm padding khi đo.
    windows = [[a+480,b-480] for a,b in quiet if b-a>=1200]
    windows.append([len(x)-144,len(x)])
    floor = max(db(np.sqrt(np.mean(x[a:b]**2))) for a,b in windows)
    return dict(duration_ms=len(x)/48, head_ms=on/48, main_ms=float(main), lufs_m_max=momentary(x),
                true_peak_dbtp=peak(x), noise_floor_dbfs=floor, quiet_edge_residual_dbfs=edge_floor,
                noise_windows_count=len(windows), noise_window_samples=sum(b-a for a,b in windows),
                high4k8k_vs_body150_400_db=float(10*np.log10(max(hi,1e-20)/max(low,1e-20))),
                centroid_hz=float(np.sum(f*P)/max(P.sum(),1e-20)))


def correlation(a,b):
    """Tương quan tuyệt đối lớn nhất, cả file, cho phép trượt tối đa ±5 ms.

    Chuẩn năng lượng toàn file tránh cặp giống nhau qua cổng chỉ nhờ dịch đầu.
    """
    c = signal.correlate(a,b,mode='full',method='fft')
    center = len(b)-1
    c = c[max(0,center-240):center+241]
    return float(np.max(np.abs(c))/max(np.linalg.norm(a)*np.linalg.norm(b),1e-20))


def recover_event(take, raw_sr, stroke, seconds):
    """Khôi phục đúng đoạn của cùng sự kiện trước fade đuôi cũ, giữ thêm đuôi cú đơn."""
    take=np.asarray(take)
    mono=take.mean(axis=1) if take.ndim==2 else take.copy()
    mono=signal.sosfiltfilt(signal.butter(2,30,'highpass',fs=raw_sr,output='sos'),mono)
    mono=soxr.resample(mono,raw_sr,SR,quality='VHQ')
    a=max(0,stroke['onset']-48)
    b=min(len(mono),stroke['press_end']+(1920 if seconds==1 else 0))
    if b-a>int(.26*SR):
        raise ValueError('Sự kiện vượt 260 ms; không cắt tiếng hoặc ghép nhả')
    return mono[a:b].copy(),(stroke['release_onset']-a)/48,a,b


def candidates(profile):
    p = PROFILES[profile]
    rows, rejected = [], []
    for procpath in sorted((SOURCE/p['source']).glob('r*/strokes/*.proc.json')):
        proc = json.loads(procpath.read_text())
        stem = proc['stem']
        critic = procpath.parent.parent/'critic'/f'{stem}.json'
        if not critic.exists():
            continue
        cj = json.loads(critic.read_text())
        flags = {v['id'] for v in cj.get('flags',[]) if v.get('layer') == 'L1b'}
        if (proc['stroke']['kind'] != 'press+release' or cj.get('verdict') != 'PASS'
                or proc.get('raw_qa',{}).get('verdict') != 'PASS' or flags & BAD_FLAGS):
            continue
        path = Path(proc['path'])
        rawpath = procpath.parent.parent/'raw'/f"{proc['take']}.json"
        raw = json.loads(rawpath.read_text())
        x, sr = sf.read(path)
        if sr != SR or x.ndim != 1:
            continue
        st = proc['stroke']
        rel_ms = (st['release_onset']-st['onset'])/48 + proc['render']['pre_roll_ms'] - proc['render'].get('tightened_ms',0)
        recovery = None
        if profile=='dome' and proc['part']=='space':
            # Fade đuôi cũ bắt đầu trước upstroke và đã hạ nó 20–37 dB.
            # Khôi phục cả sự kiện từ float raw, không ghép nhả của phím khác.
            raw_audio=Path(raw['files']['f32']['path'])
            take,raw_sr=sf.read(raw_audio,always_2d=True)
            try:
                x,rel_ms,a,b=recover_event(take,raw_sr,st,proc['seconds'])
            except ValueError:
                continue
            recovery=dict(raw_audio=str(raw_audio),sha256=sha(raw_audio),start_sample_48k=a,end_sample_48k=b,
                          note='Cả nhấn và nhả từ cùng đoạn float raw; bỏ fade đuôi cũ, không ghép âm.')
        y, cleanup = clean_stroke(x, profile, release_sample=round(rel_ms*48))
        if recovery:
            cleanup['raw_recovery']=recovery
        m = measures(y, cleanup['quiet_windows_samples'])
        why = []
        if m['head_ms'] > 2 or m['main_ms'] > 15:
            why.append('đầu tiếng/tiếng chính chậm')
        if m['true_peak_dbtp'] > -1.25:
            why.append('đỉnh thật sát trần')
        if m['noise_floor_dbfs'] > -70:
            why.append('nền giữa thành phần cao')
        if profile=='dome' and proc['part']=='space' and m['centroid_hz']<400:
            why.append('phím cách quá thiên trầm')
        if why:
            rejected.append({'source':str(path),'why':why,'metrics':m})
            continue
        # Vẫn phải còn tiếng nhả riêng ở chỗ metadata chỉ ra, sau khi rút hold.
        release = int(rel_ms*48)-cleanup['trim_samples']
        if release < 18*48 or release+240 > len(y):
            continue
        release_rms = np.sqrt(np.mean(y[release:release+480]**2))
        if db(release_rms) < -55:
            continue
        # Chọn sau vòng encode/decode: Vorbis có thể đổi cân đầu tiếng.
        buf=io.BytesIO()
        sf.write(buf,y,SR,format='OGG',subtype='VORBIS',compression_level=.4)
        data=subprocess.run(['ffmpeg','-nostdin','-v','error','-i','pipe:0','-f','f64le','-ar',str(SR),'-ac','1','-'],input=buf.getvalue(),capture_output=True,check=True).stdout
        z=np.frombuffer(data,dtype='<f8')
        om=measures(z,cleanup['quiet_windows_samples'])
        if om['main_ms']>15 or om['head_ms']>2 or om['true_peak_dbtp']>-1 or om['noise_floor_dbfs']>-70 or abs(om['lufs_m_max']+27)>.5:
            rejected.append({'source':str(path),'why':['OGG giải mã trượt cổng'],'metrics':om})
            continue
        if release+480>len(z) or db(np.sqrt(np.mean(z[release:release+480]**2))) < -55:
            continue
        row = dict(stem=stem, part=proc['part'], take=proc['take'], path=str(path), proc=str(procpath),
                   source_sha256=sha(path), source_record=str(rawpath), source_record_sha256=sha(rawpath),
                   prompt=raw['prompt'], seed=raw['seed'], model=raw['model'], licence=raw['licence'],
                   original_flags=sorted(flags), release_ms=release/48, release_rms_dbfs=db(release_rms),
                   cleanup=cleanup, metrics=m, before=measures(x, [[len(x)-144,len(x)]]), audio=y,
                   Q=float((cj.get('L3',{}).get('scores') or {}).get('PQ') or 0))
        rows.append(row)
    return rows, rejected


def select(rows, part, n, used):
    pool = [r for r in rows if r['part']==part and r['source_sha256'] not in used]
    if len(pool) < n:
        raise RuntimeError(f'{part}: chỉ {len(pool)} ứng viên qua cổng, cần {n}')
    # Cùng take được ưu tiên, nhưng nguồn AI cũ không có đủ mọi take cho 13 cú.
    # Chọn nhóm compact nhất về log-spectrum, centroid và độ dài; không tạo biến thể bằng dịch âm.
    feats = []
    for r in pool:
        f,P = spectrum(r['audio'])
        bands = np.geomspace(100,10000,25)
        v = np.array([10*np.log10(P[(f>=a)&(f<b)].sum()+1e-20) for a,b in zip(bands,bands[1:])])
        feats.append(v-v.mean())
    feat = np.array(feats)
    D = np.sqrt(np.mean((feat[:,None]-feat[None,:])**2,axis=2))
    best = None
    for med in range(len(pool)):
        chosen = [med]
        order = sorted(range(len(pool)), key=lambda i: D[med,i] - .35*(pool[i]['take']==pool[med]['take']) - .03*pool[i]['Q'])
        for i in order:
            if i in chosen:
                continue
            if all(correlation(pool[i]['audio'],pool[j]['audio']) <= .95 for j in chosen):
                chosen.append(i)
            if len(chosen)==n:
                break
        if len(chosen) != n:
            continue
        score = np.mean(D[np.ix_(chosen,chosen)]) + .2*len({pool[i]['take'] for i in chosen})
        if best is None or score < best[0]:
            best = (score,chosen)
    if best is None:
        raise RuntimeError('Không chọn được bộ không trùng')
    selected = [pool[i] for i in best[1]]
    used.update(r['source_sha256'] for r in selected)
    return selected


def encode(src, dst, args):
    subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',str(src),*args,str(dst)],check=True)


def decoded(path):
    b = subprocess.check_output(['ffmpeg','-nostdin','-v','error','-i',str(path),'-f','f64le','-ar',str(SR),'-ac','1','-'])
    return np.frombuffer(b,dtype='<f8').copy()


def schedule(seconds, mode='alternating'):
    """Nhịp chung cho mọi hồ sơ, 5 ký tự/từ; luân phiên khối 5 s ở 60/100 WPM."""
    rng = np.random.default_rng(182)
    text = 'the quick brown fox jumps over the lazy dog '
    out, t, k = [], .12, 0
    while t < seconds-.28:
        wpm = (60 if int(t//5)%2==0 else 100) if mode=='alternating' else int(mode)
        out.append(dict(t=t,part='space' if text[k%len(text)]==' ' else 'key',wpm=wpm))
        t += 60/(5*wpm)*rng.uniform(.85,1.15)
        k += 1
    return out


def phrase(sets, seconds, mode='alternating'):
    rng = np.random.default_rng(183)
    orders, cursors, last = {}, {}, {}
    out = np.zeros(round(seconds*SR))
    events = []
    for event in schedule(seconds, mode):
        part = event['part']
        if part not in orders or cursors[part]>=len(orders[part]):
            order = rng.permutation(len(sets[part])).tolist()
            if order[0]==last.get(part):
                order[0],order[1]=order[1],order[0]
            orders[part],cursors[part]=order,0
        idx=orders[part][cursors[part]]
        cursors[part]+=1
        last[part]=idx
        rate=float(rng.uniform(.97,1.03))
        gain=(.6 if part=='space' else .55)*float(rng.uniform(.92,1.08))
        src=sets[part][idx]
        # Nội suy tuyến tính giống thay tốc độ phát, không pitch-shifter xoáy pha.
        y=np.interp(np.arange(0,len(src)-1,rate),np.arange(len(src)),src)*gain
        a=round(event['t']*SR)
        b=min(len(out),a+len(y))
        out[a:b]+=y[:b-a]
        events.append(event|dict(variant=idx+1,rate=rate,gain=gain))
    return out,events


def average_spectrum(paths):
    spectra=[]
    for path in paths:
        x,sr=sf.read(path)
        assert sr==SR
        f,P=spectrum(x)
        spectra.append(P)
    return f,np.mean(spectra,axis=0)


def plot_spectra():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    font=FontProperties(fname='/System/Library/Fonts/Supplemental/Arial.ttf')
    fig,axes=plt.subplots(5,2,figsize=(13,15),sharex=True,sharey=True)
    old=json.loads((SOURCE/'master.json').read_text())
    old_ids=['creamy','thock','spring','clicky','dome']
    specdata={}
    for row,((pid,p),oldid) in enumerate(zip(PROFILES.items(),old_ids)):
        before=[Path(old['profiles'][oldid]['sets']['top']['dir'])/r['master'] for r in old['profiles'][oldid]['sets']['top']['files']]
        after=sorted((OUT/pid).glob('key-*.wav'))+sorted((OUT/pid).glob('space-*.wav'))
        f,A=average_spectrum(before);_,B=average_spectrum(after)
        specdata[pid]={'hz':f.tolist(),'old_id':oldid,'old_psd':A.tolist(),'new_psd':B.tolist()}
        for col,(P,color,label) in enumerate([(A,'#b45c4e',f'Claude bị trả: {oldid}'),(B,'#157a79',f'Codex tái xử lý: {pid}')]):
            ax=axes[row,col]
            ax.semilogx(f,10*np.log10(P+1e-20),c=color,lw=1)
            ax.axvspan(150,400,color='#3aa66c',alpha=.12)
            ax.axvspan(4000,8000,color='#eaa03d',alpha=.15)
            ax.set_xlim(65,16000);ax.set_ylim(-125,-30)
            ax.grid(alpha=.2);ax.set_title(label,fontproperties=font)
            ax.set_ylabel('dBFS/Hz · PSD Welch',fontproperties=font)
    for ax in axes[-1]:ax.set_xlabel('Hz',fontproperties=font)
    fig.suptitle('Cùng thang tuyệt đối · 13 cú/hồ sơ · 48 kHz · thân 150–400 Hz (xanh), dải xì 4–8 kHz (cam)\nMarbly thay vị trí Spring: khác họ âm, không phải A/B cùng bàn phím; phổ không chứng minh chất liệu hay mức 9',fontproperties=font,fontsize=13)
    fig.tight_layout(rect=(0,0,1,.95));fig.savefig(DOC/'spectra.png',dpi=145);plt.close(fig)
    dump(DOC/'spectra-data.json',specdata)
    (DOC/'spectra.prompt.txt').write_text('Ảnh số liệu, không dùng image_gen: vẽ bằng plot_spectra() trong tools/audio-lab/keys/codex182.py; 5 hàng × 2 cột, PSD Welch tuyệt đối trung bình 13 cú gõ, cửa sổ Hann 1024, FFT 4096, cùng trục −125…−30 dBFS/Hz; trái đủ năm hồ sơ Claude bị trả, phải đủ năm ứng viên Codex; tô 150–400 Hz và 4–8 kHz; phông Arial macOS. Marbly nằm cạnh Spring là hồ sơ bị thay thế, không cùng họ; Clean Clack cạnh Clicky bị trả.\n')


def build():
    OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
    used=set();allmetrics=[];summary={};comparison=[];decisions={}
    for pid,p in PROFILES.items():
        rows,rejected=candidates(pid)
        selected=select(rows,'key',10,used)+select(rows,'space',3,used)
        directory=OUT/pid;directory.mkdir(exist_ok=True)
        manifest={'schema':'keys-codex182/1','id':pid,'name':p['name'],'status':'candidate-reprocessed-not-owner-approved',
                  'quality_9_accepted':False,'actual_aluminium_recording':False,
                  'format':{'sample_rate':SR,'channels':1,'master':'WAV PCM_24','runtime':'Vorbis q=0.6 (libsndfile compression_level=0.4)'},
                  'source_notice':'Nguồn AI cũ; chỉ tái xử lý. Không xác nhận vật liệu, plate hay keycap thật. Không phải CC0.',
                  'files':[]}
        sets={'key':[],'space':[]};counts={'key':0,'space':0}
        for r in selected:
            part=r['part'];counts[part]+=1
            stem=f'{part}-{counts[part]:02}'
            wav=directory/f'{stem}.wav';ogg=directory/f'{stem}.ogg'
            sf.write(wav,r['audio'],SR,subtype='PCM_24')
            sf.write(ogg,r['audio'],SR,format='OGG',subtype='VORBIS',compression_level=.4)
            x,_=sf.read(wav);z=decoded(ogg)
            metrics=measures(x,r['cleanup']['quiet_windows_samples'])
            om=measures(z,r['cleanup']['quiet_windows_samples'])
            source={k:v for k,v in r.items() if k not in {'audio','metrics','before'}}
            entry=dict(file=ogg.name,master=wav.name,duration_ms=metrics['duration_ms'],lufs_m_max=metrics['lufs_m_max'],
                       sha256={'wav':sha(wav),'ogg':sha(ogg)},source=source,licence=r['model']['licence'],metrics=metrics,runtime_metrics=om)
            manifest['files'].append(entry);sets[part].append(x)
            allmetrics.append({'profile':pid,'file':wav.name,**metrics,'ogg_lufs_m_max':om['lufs_m_max'],
                               'ogg_true_peak_dbtp':om['true_peak_dbtp'],'ogg_head_ms':om['head_ms'],
                               'ogg_noise_floor_dbfs':om['noise_floor_dbfs'],'ogg_quiet_edge_residual_dbfs':om['quiet_edge_residual_dbfs'],'release_ms':r['release_ms'],
                               'release_rms_dbfs':r['release_rms_dbfs'],'source':r['path']})
            # Prompt nguồn giữ nguyên; không nhận prompt cũ là prompt mới đã sinh.
            (directory/f'{stem}.prompt.txt').write_text(r['prompt']+'\n')
        correlations=[{'a':a['master'],'b':b['master'],'max_abs_corr_lag5ms':correlation(sf.read(directory/a['master'])[0],sf.read(directory/b['master'])[0])} for a,b in itertools.combinations(manifest['files'],2)]
        lufs=[r['metrics']['lufs_m_max'] for r in manifest['files']]
        render,_=phrase(sets,20)
        ref60,ev60=phrase(sets,20,'60')
        target=-25.
        # Cân một gain duy nhất mỗi hồ sơ, đo ở 60 WPM và giữ gain đó khi sang 100.
        integrated=pyln.Meter(SR).integrated_loudness(np.column_stack([ref60,ref60]))
        gain=10**((target-integrated)/20)
        manifest['listen_gain_db']=db(gain)
        listen=OUT/'listen';listen.mkdir(exist_ok=True)
        for label,mix,seconds in [('20s',render,20)]:
            temp=listen/f'{pid}-{label}.wav'
            sf.write(temp,np.column_stack([mix,mix])*gain,SR,subtype='PCM_24')
            encode(temp,listen/f'{pid}-{label}.mp3',['-c:a','libmp3lame','-b:a','192k','-ar',str(SR),'-ac','2'])
        short,events=phrase(sets,6,'60');comparison.append(short*gain)
        _,events20=phrase(sets,20)
        dump(listen/f'{pid}-schedule.json',{'gain_db':db(gain),'kit_gain':{'key':.55,'space':.6},'events':events20,
                                            'reference60_events':ev60,'true_peak_dbtp':peak(render*gain)})
        dump(directory/'keys-manifest.json',manifest)
        summary[pid]={'candidate_pool':len(rows),'selected':len(selected),'takes':sorted({r['take'] for r in selected}),
                      'lufs_spread_db':max(lufs)-min(lufs),'max_abs_waveform_corr_lag5ms':max(r['max_abs_corr_lag5ms'] for r in correlations),
                      'reference60_stereo_lufs_i':float(integrated+db(gain)),
                      'listening_gain_db':db(gain),'correlations':correlations}
        decisions[pid]={'pool':len(rows),'rejected_after_processing':rejected,'selection':'compact log-spectrum, same-take preference; unique source events across all five profiles'}
        print(pid,'pool',len(rows),'selected',len(selected),'corr',summary[pid]['max_abs_waveform_corr_lag5ms'],flush=True)
    comp=np.concatenate(comparison)
    sf.write(OUT/'listen/so-sanh-5-ban-phim.wav',np.column_stack([comp,comp]),SR,subtype='PCM_24')
    encode(OUT/'listen/so-sanh-5-ban-phim.wav',OUT/'listen/so-sanh-5-ban-phim.mp3',['-c:a','libmp3lame','-b:a','192k','-ar',str(SR),'-ac','2'])
    dump(DOC/'measurements.json',allmetrics);dump(DOC/'summary.json',summary);dump(DOC/'selection.json',decisions)
    with (DOC/'measurements.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(allmetrics[0]));w.writeheader();w.writerows(allmetrics)
    dump(OUT/'keys-manifest.json',{'profiles':[{'id':pid,'name':p['name'],'manifest':f'{pid}/keys-manifest.json'} for pid,p in PROFILES.items()],
                                  'status':'candidate-reprocessed-not-owner-approved'})
    plot_spectra()


def verify():
    """Đọc lại file giao, không tin số đo lưu lúc build; ffmpeg độc lập kiểm chéo."""
    failures=[];audits=[]
    for pid in PROFILES:
        directory=OUT/pid
        man=json.loads((directory/'keys-manifest.json').read_text())
        assert len(man['files'])==13
        levels=[];waves=[]
        for entry in man['files']:
            wav=directory/entry['master'];ogg=directory/entry['file']
            info=sf.info(wav);x,_=sf.read(wav)
            assert info.samplerate==SR and info.channels==1 and info.subtype=='PCM_24'
            oi=sf.info(ogg)
            assert oi.samplerate==SR and oi.channels==1 and oi.subtype=='VORBIS'
            assert sha(wav)==entry['sha256']['wav'] and sha(ogg)==entry['sha256']['ogg']
            m=measures(x,entry['source']['cleanup']['quiet_windows_samples']);levels.append(m['lufs_m_max']);waves.append(x)
            cap=260 if wav.name.startswith('space') else 180
            if not (m['duration_ms']<=cap and m['head_ms']<=2 and m['main_ms']<=15 and m['true_peak_dbtp']<=-1 and m['noise_floor_dbfs']<=-70 and abs(m['lufs_m_max']+27)<=.15):
                failures.append({'file':str(wav),'metrics':m})
            # Đệm trước/sau để ebur128 đo được cửa sổ 400 ms của cú gõ ngắn.
            cmd=['ffmpeg','-nostdin','-hide_banner','-i',str(wav),'-af','adelay=400,apad=pad_dur=0.4,ebur128=peak=true','-f','null','-']
            proc=subprocess.run(cmd,capture_output=True,text=True,check=True)
            momentary_ffmpeg=max(float(v) for v in re.findall(r'\bM:\s*(-?\d+\.?\d*)',proc.stderr))
            true_peak_ffmpeg=float(re.findall(r'Peak:\s*(-?\d+\.?\d*) dBFS',proc.stderr)[-1])
            audits.append({'file':str(wav),'lufs_m_max':momentary_ffmpeg,'true_peak_dbtp':true_peak_ffmpeg,'ffmpeg_log':proc.stderr})
            if abs(momentary_ffmpeg+27)>.2 or true_peak_ffmpeg>-1:
                failures.append({'file':str(wav),'why':'ffmpeg độc lập trượt cổng','M':momentary_ffmpeg,'TP':true_peak_ffmpeg})
            om=measures(decoded(ogg),entry['source']['cleanup']['quiet_windows_samples'])
            if om['true_peak_dbtp']>-1 or om['head_ms']>2 or om['main_ms']>15 or om['noise_floor_dbfs']>-70 or abs(om['lufs_m_max']+27)>.5:
                failures.append({'file':str(ogg),'metrics':om})
        if max(levels)-min(levels)>1 or max(correlation(a,b) for a,b in itertools.combinations(waves,2))>.95:
            failures.append({'profile':pid,'why':'độ đều hoặc tương quan'})
    listening=[]
    for path in sorted((OUT/'listen').glob('*.mp3')):
        info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(path)]))
        stream=info['streams'][0];duration=float(info['format']['duration']);expected=30 if path.name.startswith('so-sanh') else 20
        proc=subprocess.run(['ffmpeg','-nostdin','-hide_banner','-i',str(path),'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True,check=True)
        integrated=float(re.findall(r'I:\s*(-?\d+\.?\d*) LUFS',proc.stderr)[-1])
        tp=float(re.findall(r'Peak:\s*(-?\d+\.?\d*) dBFS',proc.stderr)[-1])
        listening.append({'file':path.name,'probe':info,'lufs_i':integrated,'true_peak_dbtp':tp,'ffmpeg_log':proc.stderr})
        if abs(duration-expected)>.06 or stream['channels']!=2 or stream['sample_rate']!='48000' or int(stream['bit_rate'])!=192000:
            failures.append({'file':str(path),'why':'định dạng/nghe'})
    dump(DOC/'ffmpeg-audit.json',audits);dump(DOC/'listening-audit.json',listening)
    dump(DOC/'verification.json',{'status':'PASS' if not failures else 'FAIL','files':65,'ogg_files':65,'listening_mp3':6,'failures':failures,
                                 'notice':'Chỉ cổng kỹ thuật phiếu 182; chưa chấm L1–L6/mức 9, chưa nghe bằng tai.'})
    print('Verification:',len(failures),'failures')
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','verify'])
    args=parser.parse_args()
    {'build':build,'verify':verify}[args.command]()
