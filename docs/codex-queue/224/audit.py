#!/usr/bin/env python3
"""Kiểm kit và trường hợp biên; ghi fixture trong bản chép, tự dọn bằng finally."""
from pathlib import Path
import sys, json, subprocess, shutil, os, tempfile, re
sys.path.insert(0,str(Path(__file__).resolve().parent))
import run as R

def kit():
    commit='1b1fe6cfacdc81a55d13af202da0f42023455313'
    base=R.C/'tree/src/kit'
    manifest=json.loads((base/'kit-manifest.json').read_text())
    modules=[]
    for path in manifest['files']:
        if path in ['README.md','verify-kit.mjs']:continue
        p=subprocess.run(['git','show',commit+':shared/game-kit/'+path],cwd=R.ROOT,capture_output=True)
        modules.append({'path':path,'git_exit':p.returncode,'match':p.returncode==0 and p.stdout==(base/path).read_bytes(),'expected_sha256':R.sha(p.stdout),'actual_sha256':R.sha((base/path).read_bytes())})
    probe='''import {readFileSync} from 'node:fs';
import {VERIFY_SOURCE} from REPLACE_URL;
const source=readFileSync(REPLACE_PATH,'utf8');
const expr=source.match(/const README_TEXT = ([\\s\\S]*?);\\n\\nexport const VERIFY_SOURCE/)[1];
const generated=Function('MANIFEST_FILE','VERIFY_FILE','return '+expr)('kit-manifest.json','verify-kit.mjs');
console.log(JSON.stringify({verify:Buffer.from(VERIFY_SOURCE).equals(readFileSync('src/kit/verify-kit.mjs')),readme:Buffer.from(generated).equals(readFileSync('src/kit/README.md'))}));'''
    script=R.ROOT/'scripts/sync-game-kit.mjs'
    probe=probe.replace('REPLACE_URL',json.dumps(script.as_uri())).replace('REPLACE_PATH',json.dumps(str(script)))
    result=R.run('kit-generator',['node','--input-type=module','--eval',probe])
    generated=json.loads(result.stdout)
    report={'parentCommit':manifest['parentCommit'],'parentDirty':manifest['parentDirty'],'modules':modules,'matched_modules':sum(x['match'] for x in modules),'generated':generated,'readme_matches_main_checkout':(base/'README.md').read_bytes()==(R.ROOT/'games/typing-defense/src/kit/README.md').read_bytes()}
    R.save('kit.json',report)
    print('kit',report['matched_modules'],generated)

def snap(base):
    out={}
    for here,dirs,files in os.walk(base,followlinks=False):
        for name in dirs+files:
            p=Path(here)/name; rel=p.relative_to(base).as_posix()
            if p.is_symlink():out[rel]={'symlink':str(p.readlink())}
            elif p.is_file():out[rel]=R.sha(p.read_bytes())
    return out

def prune():
    cases=[]
    prefix='/assets/typing-defense/models/'
    urls=[('encoded-dotdot',prefix+'%2e%2e/escape.glb'),('backslash',prefix+'keep\\x.glb'),('query',prefix+'keep/high.glb?v=hash'),('fragment',prefix+'keep/high.glb#hash'),('absolute','https://portal.example'+prefix+'keep/high.glb'),('double-encoding',prefix+'%252e%252e/escape.glb')]
    plans=[('symlink-'+p,{'symlink':p}) for p in ['dist','ancestor','assets','game','models','models-deep','vite','vite-deep','index']]
    plans += [('dangling-'+p,{'symlink':p,'dangling':True}) for p in ['assets','game','models','models-deep','vite','vite-deep','index']]
    plans += [(name,{'url':url,'keys':['keep']}) for name,url in urls]
    plans += [('duplicate-keys',{'keys':['keep','keep']}),('non-string',{'keys':['keep',42]}),('missing-models-array',{'list':{}}),('manifest-no-models',{'manifest':{},'keys':['keep']}),('list-relative-script',{'keys':['keep']})]
    for name,options in plans:
        temp=Path(tempfile.mkdtemp(prefix='audit-prune-',dir=R.C/'tree/tmp'))
        try:
            dist=temp/'real/dist';models=dist/'assets/typing-defense/models';vite=dist/'.vite'
            (models/'keep').mkdir(parents=True);vite.mkdir()
            (dist/'index.html').write_text('game');(dist/'keep.txt').write_text('keep')
            (models/'keep/high.glb').write_text('high');(models/'discard.glb').write_text('discard');(vite/'manifest.json').write_text('{}')
            (models/'manifest.json').write_text(json.dumps(options.get('manifest',{'version':1,'models':{'keep':{'tiers':{'high':{'url':options.get('url',prefix+'keep/high.glb?v=hash')}}}}})))
            (temp/'scripts/deploy').mkdir(parents=True)
            shutil.copyfile(R.WT/'scripts/deploy/prune.mjs',temp/'scripts/deploy/prune.mjs')
            (temp/'deploy-models.json').write_text(json.dumps(options.get('list',{'models':options.get('keys',[])})))
            # Nếu script đọc cwd thay vì cạnh script thì ca này phải hỏng.
            (temp/'real/deploy-models.json').write_text('{"models":["wrong-cwd"]}')
            outside=temp/'outside';outside.mkdir();(outside/'sentinel').write_text('outside-unchanged')
            target=dist
            where=options.get('symlink')
            if where=='ancestor':
                (temp/'alias').symlink_to(temp/'real');target=temp/'alias/dist'
            elif where=='dist':
                (temp/'alias-dist').symlink_to(dist);target=temp/'alias-dist'
            elif where:
                path={'assets':dist/'assets','game':dist/'assets/typing-defense','models':models,'models-deep':models/'keep/link','vite':vite,'vite-deep':vite/'link','index':dist/'index.html'}[where]
                if path.is_dir():shutil.rmtree(path)
                elif path.exists():path.unlink()
                path.symlink_to(outside/('missing' if options.get('dangling') else 'sentinel') if where=='index' else outside/'missing' if options.get('dangling') else outside)
            before=snap(dist);outside_before=snap(outside)
            result=subprocess.run(['node',str(temp/'scripts/deploy/prune.mjs'),str(target)],cwd=R.C/'tree',capture_output=True,text=True)
            cases.append({'case':name,'options':options,'exit':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'dist_unchanged':snap(dist)==before,'outside_unchanged':snap(outside)==outside_before,'dist_after':snap(dist)})
        finally:shutil.rmtree(temp)
    R.save('prune-probes.json',cases)
    print('prune cases',len(cases),'unexpected symlink successes',[x['case'] for x in cases if ('symlink' in x['case'] or 'dangling' in x['case']) and x['exit']==0])

def vite():
    dest=R.C/'tree/tmp/audit-probe.mts';shutil.copyfile(R.OUT/'probe.mts',dest)
    try:
        p=R.run('vite-probes',['node','--import','tsx','tmp/audit-probe.mts'])
        line=next(x for x in p.stdout.decode().splitlines() if x.startswith('AUDIT_JSON='))
        R.save('vite-probes.json',json.loads(line[len('AUDIT_JSON='):]))
    finally:dest.unlink()

if __name__=='__main__':
    kit();prune();vite()
