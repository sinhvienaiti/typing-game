#!/usr/bin/env python3
"""Mỗi lượt chỉ sửa một file trong tree; finally chép trả từ worktree và kiểm hash."""
from pathlib import Path
import json, re, shutil, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import run as R

def counts(result):
    text=re.sub(r'\x1b\[[0-9;]*m','',(result.stdout+result.stderr).decode())
    lines=[line.strip() for line in text.splitlines() if re.match(r'\s*Tests\s',line)]
    summary=lines[-1] if lines else ''
    def number(word):
        match=re.search(r'(\d+) '+word,summary);return int(match[1]) if match else 0
    return {'failed':number('failed'),'passed':number('passed'),'summary':summary,'exit':result.returncode}

def main():
    plans=[
      ('M1','vite.config.ts','return code.replace(declaration, () => `export const PARENT_ORIGIN = ${JSON.stringify(origin)};`);','return code;', ['tests/portal-build.test.ts'],'Giữ kiểm đúng một khai báo nhưng không thay origin'),
      ('M2','src/app/learning.ts','host: home ? options.host : standaloneHost,','host: options.host,',['tests/portal.test.ts'],'Luôn đưa host nhúng cho kit, kể cả khi biến trống'),
      ('M3','scripts/deploy/prune.mjs','  rmSync(vite, { recursive: true, force: true });','  // Mutation: skip .vite deletion.',['tests/deploy-prune.test.ts','tests/deploy-pack.test.ts'],'Bỏ bước xóa .vite'),
      ('M4','src/app/retry.ts','download: `wordwoven-playtest-','download: `loi-goi-choi-thu-',['tests/td-b9.test.ts'],'Tên tải xuống trở về mẫu cũ'),
      ('M5','scripts/deploy/prune.mjs','if (lstatSync(at).isSymbolicLink())','if (false && lstatSync(at).isSymbolicLink())',['tests/deploy-prune.test.ts'],'Bỏ chặn symlink ở dist và tổ tiên'),
      ('M6','src/app/learning.ts','let bridge: LearningBridge | null = null;','let bridge: LearningBridge | null = createPortalBridge();',['tests/portal.test.ts'],'Khởi tạo singleton ngay lúc import thay vì lười'),
    ]
    rows=[];baseline=json.loads((R.OUT/'before.json').read_text());hashes={e['path']:e['sha256'] for e in baseline['entries']}
    for name,path,old,new,tests,description in plans:
        target=R.C/'tree'/path;source=(R.WT/path).read_bytes()
        assert R.sha(target.read_bytes())==hashes[path]
        original=target.read_text();assert original.count(old)==1,(name,original.count(old))
        row={'id':name,'path':path,'description':description,'tests':tests,'original_sha256':hashes[path]}
        try:
            target.write_text(original.replace(old,new))
            row['mutated_sha256']=R.sha(target.read_bytes())
            row['mutated']=counts(R.run('mutation-'+name,['pnpm','exec','vitest','run',*tests]))
        finally:
            shutil.copyfile(R.WT/path,target)
            row['restored_sha256']=R.sha(target.read_bytes())
            assert row['restored_sha256']==hashes[path]
        row['restored']=counts(R.run('restored-'+name,['pnpm','exec','vitest','run',*tests]))
        rows.append(row);R.save('mutations.json',rows)
        print(name,row['mutated'],row['restored'],flush=True)
    final=[R.entry(R.C/'tree',e['path']) for e in baseline['entries']]
    extra=R.inventory(R.C/'tree',{'node_modules','dist','tmp'})
    R.save('tree-restored.json',{'source':R.compare(final,baseline['entries']),'excluding_generated':R.compare(extra['entries'],baseline['entries']),'fixture_leftovers':sorted(str(p.relative_to(R.C/'tree/tmp')) for p in (R.C/'tree/tmp').iterdir())})

if __name__=='__main__':main()
