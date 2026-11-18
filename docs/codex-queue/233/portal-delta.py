#!/usr/bin/env python3
"""Đo lại riêng chênh byte của 228 trên cùng bản chép."""
from pathlib import Path
import hashlib, json
from run import OUT as O, PARENT_COPY as P, run
scope=json.loads((O/'scope-review.json').read_text())['228']['changed']
original={p:(P/p).read_bytes() for p in scope}
try:
    for p in scope: (P/p).write_bytes((P/'scope228'/p).read_bytes())
    assert run('portal-build-before-228-copy',['pnpm','--dir','portal','build','--configLoader','runner',
        '--outDir','../tmp/portal-before-228','--emptyOutDir'],P)['exit']==0
    d=P/'tmp/portal-before-228'
    before=[{'path':str(p.relative_to(d)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in sorted(d.rglob('*')) if p.is_file()]
finally:
    for p,data in original.items(): (P/p).write_bytes(data)
    assert all((P/p).read_bytes()==data for p,data in original.items())
after=json.loads((O/'portal-dist.json').read_text())['entries']
def summary(entries):
    return {'files':len(entries),'bytes':sum(e['bytes'] for e in entries),
      'js_bytes':sum(e['bytes'] for e in entries if e['path'].endswith('.js')),
      'css_bytes':sum(e['bytes'] for e in entries if e['path'].endswith('.css')),
      'main_js':next(e for e in entries if e['path'].startswith('assets/index-') and e['path'].endswith('.js'))}
a=summary(before);b=summary(after)
result={'before':a,'after':b,'delta_js':b['js_bytes']-a['js_bytes'],'delta_css':b['css_bytes']-a['css_bytes'],
        'all_9_source_files_restored':True}
(O/'portal-delta.json').write_text(json.dumps(result,indent=2)+'\n')
assert result['delta_js']==401 and result['delta_css']==0
print(json.dumps(result))
