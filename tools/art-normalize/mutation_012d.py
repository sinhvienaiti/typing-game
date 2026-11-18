#!/usr/bin/env python3
"""Chạy lại 71 mutant của phản biện 012c trên bản sao; ghi rõ mẫu đã hết hiệu lực."""
import ast
import hashlib
from concurrent.futures import ThreadPoolExecutor
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parent
REVIEW=ROOT/'.tmp/review-claude-3'
OUT=Path(os.environ.get('ART_MUTATION_OUT',ROOT/'.tmp/mutation-012d'))


def module(path):
    spec=importlib.util.spec_from_file_location(path.stem+str(time.time_ns()),path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


def collect():
    cases={}
    for filename in ('mutate3.py','mutate3b.py','mutate3c.py'):
        obj=module(REVIEW/'docs-tests'/filename)
        cases.update(obj.M if hasattr(obj,'M') else obj.m3.M)
    tree=ast.parse((REVIEW/'code/mutate3.py').read_text())
    listing=next(ast.literal_eval(stmt.value) for stmt in tree.body if isinstance(stmt,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='M' for t in stmt.targets))
    for name,file,old,new,note in listing:cases[name]={'note':note,'edits':[(file,old,new)]}
    # Retarget exact edits only when the same behavior still exists under a new implementation.
    replacements={
      'A3-strong-key-zero-not-candidate':('normalize.py','if candidate[p] and strong_key(rgb, background) and excess > .7 * max(rgb) and inferred is None:', 'if strong_key(rgb, background) and excess > .7 * max(rgb) and inferred is None:'),
      'D1-row-streak-off-with-reference':('normalize.py','after["criteria"]["row_streak"] = residual <= 5','after["criteria"]["row_streak"] = True'),
      'D2-row-streak-reference-plus30':('normalize.py','after["criteria"]["row_streak"] = residual <= 5','after["criteria"]["row_streak"] = residual <= 30'),
      'D6-row-streak-reference-plus4':('normalize.py','after["criteria"]["row_streak"] = residual <= 5','after["criteria"]["row_streak"] = residual <= 6'),
      'D3-row-streak-left-band-only':('seam_analysis.py','if start<band or start+window>length-band:', 'if start<band:'),
      'M7-edge-matte-loose':('normalize.py','    best=9','    best=400'),
      'M4-hard-cut-no-blend':('normalize.py','radius = max(1, min(3, band//8))','radius = 0.0001'),
      'M5-worst-cut':('seam_analysis.py','k = min(range(len(previous)), key=previous.__getitem__)','k = max(range(len(previous)), key=previous.__getitem__)'),
      'B3-blend-whole-overlap':('normalize.py','radius = max(1, min(3, band//8))','radius = band'),
      'B4-no-cut-search':('seam_analysis.py','k = min(range(len(previous)), key=previous.__getitem__)','k = 0'),
      'F6-partial-not-removed':('normalize.py','                Path(partial).unlink(missing_ok=True)','                pass'),
      'E3-mirror-ratio-0.25':('normalize.py','mirror >= .5*control','mirror >= .25*control'),
    }
    for name,edit in replacements.items():
        cases[name]['retargeted']=True;cases[name]['edits']=[edit]
    cases['M6-row-streak-5px']['retargeted']=True
    cases['M6-row-streak-5px']['edits']=[
        ('seam_analysis.py','window=min(30,max(2,band))','window=min(3,max(2,band))'),
        ('seam_analysis.py','if start<band or start+window>length-band:',
         'if start==0 or start+window==length:')]
    return cases


def one(item):
    name,spec=item
    start=time.monotonic();folder=OUT/name
    if folder.exists():
        # Only interrupted copies under this harness's private output are replaced.
        if (folder/'result.json').exists():raise ValueError('Mutant đã có kết quả.')
        shutil.rmtree(folder)
    folder.mkdir(parents=True,exist_ok=False)
    dst=folder/'art-normalize';shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('.tmp','__pycache__'))
    source_hashes={str(p.relative_to(dst)):hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dst.rglob('*') if p.is_file()}
    missing=[]
    for file,old,new in spec['edits']:
        text=(dst/file).read_text()
        if text.count(old)!=1:missing.append({'file':file,'count':text.count(old),'pattern':old})
    if missing:
        result={'status':'không áp được','missing':missing,**spec}
    else:
        for file,old,new in spec['edits']:
            path=dst/file;path.write_text(path.read_text().replace(old,new))
        env={**os.environ,'ART_MAGICK':'/opt/homebrew/bin/magick','MAGICK_THREAD_LIMIT':'1'}
        try:
            run=subprocess.run(['bash',str(dst/'test.sh')],cwd=folder,env=env,capture_output=True,text=True,timeout=1500)
            (folder/'stdout.txt').write_text(run.stdout);(folder/'stderr.txt').write_text(run.stderr)
            result={'status':'bị bắt' if run.returncode else 'còn sống','exit_code':run.returncode,'seconds':round(time.monotonic()-start,1),'tail':run.stderr[-1000:],**spec}
        except subprocess.TimeoutExpired:
            result={'status':'hết thời gian','seconds':1500,**spec}
    result['source_sha256']=source_hashes
    (folder/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(name,result['status'],flush=True)
    return name,result


if __name__=='__main__':
    import sys
    OUT.mkdir(exist_ok=True)
    # A failing control would label unrelated exceptions as caught mutants.
    baseline=subprocess.run(['bash',str(ROOT/'test.sh')],cwd=OUT,capture_output=True,text=True,
                            env={**os.environ,'ART_MAGICK':'/opt/homebrew/bin/magick','MAGICK_THREAD_LIMIT':'1'})
    (OUT/'baseline.log').write_text(baseline.stdout+baseline.stderr)
    if baseline.returncode:raise SystemExit('Test gốc trượt; không chạy/đếm mutant.')
    cases=collect();wanted=set(sys.argv[1:])
    pending=[item for item in cases.items() if (not wanted or item[0] in wanted) and not (OUT/item[0]/'result.json').exists()]
    with ThreadPoolExecutor(max_workers=3) as pool:results=dict(pool.map(one,pending))
    all_results={p.parent.name:json.loads(p.read_text()) for p in OUT.glob('*/result.json')}
    (OUT/'results.json').write_text(json.dumps(all_results,ensure_ascii=False,indent=2))
