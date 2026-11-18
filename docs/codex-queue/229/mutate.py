from pathlib import Path
import hashlib,json,sys
from run import run,WT,OUT
phase=sys.argv[1]
plans=[
('M5','scripts/deploy/prune.mjs','if (lstatSync(at).isSymbolicLink())','if (false && lstatSync(at).isSymbolicLink())','tests/deploy-prune.test.ts','rejects a linked'),
('M6','src/app/learning.ts','let bridge: LearningBridge | null = null;','let bridge: LearningBridge | null = createPortalBridge();','tests/portal.test.ts','creates one real bridge'),
]
if phase=='final':
    plans += [
    ('P1-01-query','vite.config.ts','const path = id.split("?")[0]!.replace(/\\\\/g, "/");','const path = id.replace(/\\\\/g, "/");','tests/portal-id.test.ts','rewrites the real build through'),
    ('P1-01-realpath','vite.config.ts','return realpathSync(path);','return path;','tests/portal-id.test.ts','rewrites the real build through'),
    ('P1-01-guard','vite.config.ts','if (!error && !transformed)','if (false && !error && !transformed)','tests/portal-id.test.ts','never transforms'),
    ('P1-02','scripts/deploy/prune.mjs','return lstatSync(path, { throwIfNoEntry: false });','return existsSync(path) ? lstatSync(path) : undefined;','tests/deploy-prune.test.ts','rejects dangling'),
    ]
rows=[]
for name,path,old,new,test,pattern in plans:
    target=WT/path;original=target.read_bytes();text=original.decode()
    assert text.count(old)==1,(name,old,text.count(old))
    row={'id':name,'path':path,'old':old,'new':new,'before_sha256':hashlib.sha256(original).hexdigest()}
    try:
        mutated=text.replace(old,new)
        if name=='P1-02': mutated=mutated.replace('import { lstatSync,','import { existsSync, lstatSync,')
        target.write_text(mutated)
        row['mutated_exit']=run(phase+'-mutation-'+name,['pnpm','exec','vitest','run',test,'-t',pattern])
    finally:
        target.write_bytes(original)
        assert hashlib.sha256(target.read_bytes()).hexdigest()==row['before_sha256']
    row['restored_exit']=run(phase+'-restored-'+name,['pnpm','exec','vitest','run',test,'-t',pattern])
    rows.append(row)
    (OUT/(phase+'-mutations.json')).write_text(json.dumps(rows,indent=2)+'\n')
    assert row['mutated_exit']==1 and row['restored_exit']==0,row
