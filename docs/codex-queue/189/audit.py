"""Kiểm độc lập đầu ra phiếu 189; không dựng lại, không sửa media hay nguồn.

bash tools/audio-lab/run.sh docs/codex-queue/189/audit.py [--staging DIR]
"""
import argparse
import itertools
import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf

from keys import firefly_build as fb

ap=argparse.ArgumentParser()
ap.add_argument('--staging',type=Path,default=fb.WORK/'staging/keys-firefly')
a=ap.parse_args()
out=a.staging
root=json.loads((out/'keys-manifest.json').read_text())
rows=[];audio={'wav':[],'ogg':[]};families={};mono=[];limiting=[]
for p in root['profiles']:
    m=json.loads((out/p['manifest']).read_text())
    stats=[]
    for f in m['files']:
        for ext in ('wav','ogg'):
            file=out/p['id']/(Path(f['file']).stem+'.'+ext)
            y,sr=sf.read(file)
            info=sf.info(file)
            assert sr==48000 and info.channels==1
            if ext=='wav': assert info.subtype=='PCM_24'
            assert fb.sha(file)==f['sha256'][ext]
            met=fb.audio_metrics(y,f['gate']['muted_intervals_samples'])
            assert met==f['metrics'][ext],(file,met,f['metrics'][ext])
            assert met['duration_ms'] <= (180 if f['set']=='key' else 260)
            assert met['true_peak_dbtp']<=-1 and met['background_dbfs']<=-70
            assert abs(met['lufs_m_max']-m['loudness']['target'])<=.5
            row={'profile':p['id'],'file':file.name,'set':f['set'],**met}
            rows.append(row);stats.append(row);audio[ext].append((str(file),y))
            if ext=='wav': limiting.append((met['lufs_m_max']-met['true_peak_dbtp']-1.65,str(file)))
        mono.append(f['mono'])
    yy,sr=sf.read(out/p['preview']);prev=fb.audio_metrics(yy)
    assert len(yy)==48000 and sr==48000 and prev['background_dbfs']<=-70
    assert [e['set'] for e in m['preview_schedule']['events']]==['key']*6+['space']
    assert max(e['end_s'] for e in m['preview_schedule']['events'])<=.995
    source_counts={}
    for f in m['files']:
        folder=f['source']['directory'];source_counts[folder]=source_counts.get(folder,0)+1
    families[p['id']]={'name':p['name'],'order':p['order'],'source_counts':source_counts,
                       **m['family'],'preview':prev,
                       'wav_spread_db':max(r['lufs_m_max'] for r in stats if r['file'].endswith('.wav'))-min(r['lufs_m_max'] for r in stats if r['file'].endswith('.wav')),
                       'key_duration_ms':[min(r['duration_ms'] for r in stats if r['set']=='key'),max(r['duration_ms'] for r in stats if r['set']=='key')],
                       'space_duration_ms':[min(r['duration_ms'] for r in stats if r['set']=='space'),max(r['duration_ms'] for r in stats if r['set']=='space')]}
pairs={}
for ext,items in audio.items():
    corr,pair=max((fb.corr_max(x,y),[px,py]) for (px,x),(py,y) in itertools.combinations(items,2))
    assert corr<=.95
    pairs[ext]={'max':corr,'pair':pair}
listen=[]
for file in sorted((fb.WORK/'listen').glob('*.mp3')):
    probe=json.loads(subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(file)],capture_output=True,text=True,check=True).stdout)
    stream=probe['streams'][0]
    raw=subprocess.run(['ffmpeg','-v','error','-i',str(file),'-ar','48000','-ac','1','-f','f32le','pipe:1'],capture_output=True,check=True).stdout
    seconds=len(raw)/(4*48000)
    expected=4*len(root['profiles']) if file.name=='so-sanh-cac-bo.mp3' else 10
    assert abs(seconds-expected)<=.001 and int(stream['bit_rate'])==192000
    listen.append({'file':str(file),'seconds_decoded':seconds,'bit_rate':int(stream['bit_rate']),'sha256':fb.sha(file)})
repeat=json.loads((fb.EVIDENCE/'repeat-before.json').read_text())
changed=[p for p,s in repeat.items() if fb.sha(Path(p))!=s]
assert not changed,changed
summary={'profiles':families,'cue_count':len(audio['wav']),'per_format_correlation':pairs,
         'metrics_ranges':{k:[min(r[k] for r in rows),max(r[k] for r in rows)] for k in ['duration_ms','head_ms','lufs_m_max','true_peak_dbtp','background_dbfs']},
         'mono_methods':{method:sum(r['method']==method for r in mono) for method in ['mid','left','right','mono']},
         'mono_fold_loss_range_db':[min(r['fold_loss_db'] for r in mono),max(r['fold_loss_db'] for r in mono)],
         'limiting_cue':min(limiting),'listen':listen,
         'repeat_media_count':len(repeat),'repeat_changed_count':len(changed)}
fb.write_json(fb.EVIDENCE/'audit.json',summary)
lines=['# Phiếu 189 · Số đo từng file','','Đo lại từ WAV và OGG giải mã; LUFS-M cửa sổ 400 ms, thêm lặng tới đủ cửa sổ. Đỉnh thật lấy mẫu gấp 4. Nền là giá trị lớn nhất của RMS 5 ms cuối và lõi các khoảng lặng ≥10 ms (bỏ 3 ms mỗi mép). −200 là lặng dưới sàn số đo.','','| Bộ | File | Dài (ms) | Trước tiếng (ms) | LUFS-M max | dBTP | Nền (dBFS) |','|---|---|---:|---:|---:|---:|---:|']
for r in rows:
    lines.append(f"| {r['profile']} | {r['file']} | {r['duration_ms']:.2f} | {r['head_ms']:.3f} | {r['lufs_m_max']:.3f} | {r['true_peak_dbtp']:.3f} | {r['background_dbfs']:.3f} |")
(fb.EVIDENCE/'file-metrics.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'files':len(rows),'mp3':len(listen),'repeat_changed':len(changed),'max_correlation':pairs},ensure_ascii=False))
