#!/usr/bin/env python3
"""Tổng hợp số, kiểm nguyên worktree, dọn riêng bản chép 224 và lập báo cáo."""
from pathlib import Path
import collections, difflib, json, os, re, subprocess, sys, time
sys.path.insert(0,str(Path(__file__).resolve().parent))
import run as R

def read(name):return json.loads((R.OUT/name).read_text())
def log(name):return (R.OUT/name).read_text()
def summary(text):
    text=re.sub(r'\x1b\[[0-9;]*m','',text)
    tests=next((x.strip() for x in reversed(text.splitlines()) if re.match(r'\s*Tests\s',x)), '')
    files=next((x.strip() for x in reversed(text.splitlines()) if re.match(r'\s*Test Files\s',x)), '')
    return {'tests':tests,'files':files}

def prepare():
    baseline=read('before.json')
    source=R.inventory(R.C/'tree',{'node_modules','dist','tmp'})
    restored={'source':R.compare(source['entries'],baseline['entries']), 'fixture_leftovers':sorted(p.name for p in (R.C/'tree/tmp').iterdir())}
    R.save('tree-final.json',restored)
    assert restored['source']=={'same_sha256':329,'changed':[],'added':[],'missing':[]}
    assert not restored['fixture_leftovers']
    chunks=[]
    for p in sorted((R.C/'tree/dist/assets').glob('*.js')):
        text=p.read_text()
        chunks.append({'path':p.relative_to(R.C/'tree/dist').as_posix(),'learning_namespace':text.count('typing-game:learning:v1'),'focus_message':text.count('typing-game:request-focus'),'local_host':text.count('typing-game.local')})
    R.save('chunks.json',{'package':'local','chunks':chunks,'namespace_only_in_learn':all(x['path'].startswith('assets/learn-') for x in chunks if x['learning_namespace']),'entry_namespace':sum(x['learning_namespace'] for x in chunks if x['path'].startswith('assets/index-'))})
    # Lưu diff cả file untracked, không đọc các worktree khác.
    diff=[]
    tracked=set(x.decode() for x in R.git('ls-files','-z').split(b'\0') if x)
    for row in read('paths.json'):
        path=row['path'];old=R.git('show','HEAD:'+path).decode() if path in tracked else ''
        current=(R.WT/path).read_text()
        diff.extend(difflib.unified_diff(old.splitlines(True),current.splitlines(True),fromfile='HEAD/'+path,tofile='td-codex/'+path))
    (R.OUT/'source-diff.log').write_text(''.join(diff))
    growth={}
    for label in ['check-170','check']:
        text=log(label+'.log')
        files={m[1]:int(m[2]) for m in re.finditer(r'^\s*[✓×]\s+(tests/[^\s]+)\s+\((\d+) tests?\)',text,re.M)}
        growth[label]={'summary':summary(text),'files':files,'count_files':len(files),'count_tests':sum(files.values()),'sim_medians_ms':[float(x) for x in re.findall(r'td sim step [^\n]+median ([0-9.]+) ms',text)]}
    growth['new_files']={p:n for p,n in growth['check']['files'].items() if p not in growth['check-170']['files']}
    growth['changed_counts']={p:{'170':growth['check-170']['files'][p],'208':n,'delta':n-growth['check-170']['files'][p]} for p,n in growth['check']['files'].items() if p in growth['check-170']['files'] and n!=growth['check-170']['files'][p]}
    R.save('test-growth.json',growth)
    histories=[]
    for name in ['baseline-flow','tests-before','check-first','cli-timing-1','cli-timing-2','cli-timing-3','check']:
        p=R.OUT.parent/'170'/(name+'.log');text=p.read_text()
        histories.append({'file':str(p.relative_to(R.ROOT)),'sha256':R.sha(p.read_bytes()),**summary(text),'cli_lines':[x.strip() for x in text.splitlines() if 'B9 CLI reads both' in x and ('✓' in x or '×' in x)]})
    R.save('historical-evidence.json',histories)
    after=R.snapshot('after.json')
    started=time.monotonic()
    diffcheck=subprocess.run(['git','-C',str(R.WT),'diff','--check'],cwd=R.ROOT,capture_output=True)
    (R.OUT/'diff-check.log').write_bytes(diffcheck.stdout+diffcheck.stderr)
    R.save('diff-check-run.json',{'command':['git','-C','games/.wt-td-codex','diff','--check'],'exit':diffcheck.returncode,'seconds':round(time.monotonic()-started,4)})
    command=['find','games/.wt-td-codex','-newer','games/typing-defense/tmp/codex-224/marker','-not','-path','*/.git/*']
    newer=subprocess.run(command,cwd=R.ROOT,capture_output=True,text=True)
    paths=newer.stdout.splitlines()
    (R.OUT/'worktree-newer.log').write_text('$ '+' '.join(command)+' | wc -l\n'+newer.stdout+f'count={len(paths)}\nexit={newer.returncode}\n'+newer.stderr)
    integrity={'head':after['head'],'head_unchanged':after['head']==baseline['head']==R.HEAD,'status_unchanged':after['status']==baseline['status']==(R.OUT.parent/'208/status-final.txt').read_text(),'source':R.compare(after['entries'],baseline['entries']),'protected_match_208':after['protected_match_208'],'protected_unchanged':after['protected_sha256']==baseline['protected_sha256'],'node_modules_unchanged':after['node_modules']==baseline['node_modules'],'node_modules_items':len(after['node_modules']['items']),'results_json_files':len(after['node_modules']['vitest_results']),'find_newer_exit':newer.returncode,'find_newer_count':len(paths),'find_newer_paths':paths,'diff_check_exit':diffcheck.returncode}
    R.save('integrity.json',integrity)
    assert integrity['head_unchanged'] and integrity['status_unchanged'] and integrity['node_modules_unchanged'] and integrity['protected_unchanged']
    assert integrity['source']['same_sha256']==329 and not integrity['source']['changed'] and not paths and newer.returncode==0
    return integrity

def cleanup():
    # Chỉ thư mục được copy() của phiếu tạo sau preflight.
    assert (R.C/'marker').is_file() and (R.OUT/'copy.json').is_file() and read('integrity.json')['find_newer_count']==0
    p=subprocess.run(['rm','-rf','games/typing-defense/tmp/codex-224'],cwd=R.ROOT,capture_output=True,text=True)
    now=sorted(x.name for x in (R.ROOT/'games/typing-defense/tmp').iterdir());before=read('before.json')['main_tmp']
    R.save('cleanup.json',{'command':['rm','-rf','games/typing-defense/tmp/codex-224'],'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'copy_directory_absent':not R.C.exists(),'main_tmp_before':before,'main_tmp_after':now,'other_added':sorted(set(now)-set(before)),'other_removed':sorted(set(before)-set(now))})
    assert p.returncode==0 and not R.C.exists()

def claims():
    rows=[]
    def add(ticket,check,reported,measured,match,explanation,evidence):
        rows.append({'ticket':ticket,'check':check,'reported':reported,'measured':measured,'match':match,'explanation':explanation,'evidence':evidence})
    history=read('historical-evidence.json')
    for check,reported,index in [('Luồng trước sửa','1 đỏ / 6 xanh',0),('Test mới trước sửa mã','9 đỏ / 4 xanh',1),('Check lần đầu','378 xanh / 2 đỏ; CLI 7,858 s',2)]:
        add('170',check,reported,history[index]['tests'],'khớp hồ sơ','Chỉ đọc lại log lịch sử; không tái hiện trạng thái và tải máy của phiên trước.', 'historical-evidence.json')
    add('170','CLI riêng ba lần trước đổi timeout','3/3 xanh; test 1,834/1,913/2,015 s; cả lệnh 4,075/3,362/3,593 s','Log cũ 3/3 xanh; CLI mới trong check-170 3,485 s','khớp hồ sơ','Không có lỗi thời gian ở lượt mới nên không kích hoạt chạy lặp ba lần. Thời gian cũ không phải số tái đo.', 'historical-evidence.json; check-170.log')
    add('170','Check cuối','37 file / 380 test; mã 0; 24,422 s',f"37/380; mã {read('check-170-run.json')['exit']}; {read('check-170-run.json')['seconds']} s",'khớp','Thời gian thay đổi theo tải máy.', 'check-170.log; check-170-run.json')
    add('170','Kit','33/33','33/33','khớp','34 file kit gồm manifest; verifier kiểm 33 file được manifest liệt kê.', 'check-170.log; kit.json')
    add('170','Golden trong check','6/6; hai hash giữ nguyên','6/6; 2/2 hash giữ nguyên','khớp','Không cập nhật golden.', 'check-170.log; integrity.json')
    add('170','Sim ≤2 ms','0,064 / 0,057 / 0,232 ms',str(read('test-growth.json')['check-170']['sim_medians_ms'])+' ms','đạt ngưỡng','Số mới 0,069/0,053/0,104 ms; không yêu cầu trùng thời gian cũ.', 'check-170.log')
    add('170','Ngân sách hai trang ≤85 kB','79,60 / 81,07 kB','79,60 / 81,07 kB','khớp','Cùng nguồn nền 170.', 'check-170.log')
    add('170','Whitespace và phạm vi','diff --check=0; sim/content/typing sạch','mã 0; 19 đường, 0 ở ba thư mục đó','khớp','14 sửa/5 mới; kit/golden được kiểm hash.', 'diff-check-run.json; split.json; integrity.json')
    add('170','Production','mã 1; 69 lỗi = 1 local-host + 68 missing-model','mã 1; 69 = 1 + 68','khớp','Không báo nhầm về tồn tại model.', 'pack-170.json; deploy-170-run.json')
    add('170','Checker local trên cùng gói','mã 1; 68 missing-model','mã 1; 68 missing-model','khớp','Chỉ local-host được miễn.', 'pack-170-local.json')
    add('170','Inventory','55 file / 1.205.337 byte','55 file / 1.206.837 byte; 54/55 hash trùng','khớp sau giải thích','Chỉ .vite/manifest.json 15.155→16.655 byte: 60 × tiền tố ../../../../.wt-td-codex/ dài 25 = 1.500 byte.', 'dist-170-comparison.json; manifest-paths.json')
    add('170','Thông tin bộ kiểm','95 level không ghim; external 0; GLB thiếu 68','95; external []; 68 missing-model','khớp','95 là thông tin, không thuộc lỗi.', 'pack-170.json')
    add('208','Kiểm 1 · check','40/414; kit 33; mã 0; 12,297 s',f"40/414; kit 33; mã 0; {read('check-run.json')['seconds']} s",'khớp','Thêm 3 file/32 test; deploy-pack thêm 2 test: tổng tăng 34.', 'check.log; test-growth.json')
    add('208','Kiểm 2 · golden','2/2 same=true; 19.660/5.695 tick','2/2; 19.660/5.695; 0 problems/rejected','khớp','Lệnh check không ghi golden.', 'golden.log')
    add('208','Kiểm 3 · ngân sách/chunk','79,60 / 81,30 kB; bridge chỉ trong Học','Vắng 79,60/81,16; trống 79,60/81,30; entry 0 giao thức học','khớp theo biến','Vắng biến gập hằng portalHome(undefined), learn ít hơn 264 byte. Cả hai ≤85.', 'check.log; deploy-empty.log; chunks.json')
    add('208','Kiểm 4 · production','0 lỗi; 53 / 1.167.750; 0 host nhà','Trống: đúng số và 53/53 hash; vắng: 53 / 1.167.486','khớp theo biến','Mỗi gói 21 file văn bản, 0 host nhà; 0 GLB/GLTF/BIN, không models/.vite.', 'pack-empty.json; dist-empty-comparison.json; scan.json')
    add('208','Kiểm 5 · demo/kiểm chéo','demo mã 0, 0 lỗi; production 1 local-host','đúng; demo 53 file / 1.167.801 byte','khớp','Checker production mã 1, chỉ 1 local-host.', 'pack-local.json; pack-local-production.json')
    add('208','Kiểm 6 · trước/sau','69→0; 55→53; 1.205.337→1.167.750 (−37.587)','69→0; 55→53; 1.206.837→1.167.750 (−39.087)','khớp sau giải thích','Lọc bỏ 2 file/39.623 byte, hơn số cũ 1.500 do manifest Vite; JS nguồn tăng 536 byte. Trừ phần đường môi trường thì giảm đúng 37.587.', 'deploy-empty.log; dist-170.json; dist-empty.json')
    add('208','Kiểm 7 · bảo toàn/whitespace','37/37; diff --check=0','37/37; 329/329; mã 0','khớp','Kit, golden và public manifest nguyên byte.', 'integrity.json; kit.json')
    add('208','Kiểm 8 · phạm vi','28 = 19 + 12 − 3; HEAD không đổi','28, đúng 3 dùng chung; 0 đường lạ; HEAD không đổi','khớp','Patch ngược 12 file sạch, 7 file mới xóa đúng, ba bản before khớp.', 'paths.json; split.json; integrity.json')
    R.save('claims.json',rows)
    return rows

def scope():
    # Tạo trước file đầu ra để ảnh status bao gồm toàn bộ đường của chính phiếu.
    for name in ['scope.json','parent-after.txt','verification.json']:
        if not (R.OUT/name).exists() or not (R.OUT/name).stat().st_size:
            (R.OUT/name).write_text('{}\n' if name.endswith('.json') else '')
    report=R.OUT.parent/'224-report.md'
    if not report.exists():report.write_text('Đang tổng hợp phiếu 224.\n')
    p=subprocess.run(['git','--no-optional-locks','status','--porcelain','-uall'],cwd=R.ROOT,capture_output=True,text=True)
    (R.OUT/'parent-after.txt').write_text(p.stdout)
    before=set(log('parent-before.txt').splitlines());after=set(p.stdout.splitlines())
    new=sorted(after-before);removed=sorted(before-after)
    def own(s):return s[3:]=='docs/codex-queue/224-report.md' or s[3:].startswith('docs/codex-queue/224/')
    data={'command':['git','--no-optional-locks','status','--porcelain','-uall'],'exit':p.returncode,'before_lines':len(before),'after_lines':len(after),'new_own':list(filter(own,new)),'new_other':[s for s in new if not own(s)],'removed_other':[s for s in removed if not own(s)],'allowed_own_only':all(own(s) for s in filter(own,new))}
    R.save('scope.json',data)
    return data

def table(headers,rows):
    def cell(s):return str(s).replace('|','\\|').replace('\n',' ')
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(x) for x in row)+' |\n' for row in rows)

def report(rows):
    integrity=read('integrity.json');cleanup=read('cleanup.json');scope_data=read('scope.json');findings=read('findings.json');mutations=read('mutations.json')
    packs=[]
    for name in ['170','170-local','absent','empty','local','local-production']:
        p=read('pack-'+name+'.json');codes=dict(collections.Counter(x['code'] for x in p['problems']))
        packs.append([name,read('pack-'+name+'-run.json')['exit'],len(p['problems']),codes or '0',p['report']['files'],f"{p['report']['bytes']:,}".replace(',','.')])
    scans=read('scan.json')
    deploy_seconds=' / '.join(str(read('deploy-'+label+'-run.json')['seconds']).replace('.',',') for label in ['absent','empty','local'])
    scanrows=[[label,d['text_files'],sum(d['local_host'].values()),d['asset_prefixes'],d['model_extensions'],d['has_vite'],d['has_models']] for label,d in scans.items()]
    claims_table=table(['Phiếu','Kiểm','Phiếu báo','Đo/đối chiếu lại','Khớp','Giải thích','Bằng chứng'],[[r['ticket'],r['check'],r['reported'],r['measured'],r['match'],r['explanation'],r['evidence']] for r in rows])
    mutation_table=table(['Mã','Sửa một file','Test','Khi sửa: đỏ/xanh','Trả lại: đỏ/xanh','Hash trả lại'],[[r['id'],r['path']+': '+r['description'],', '.join(r['tests']),f"{r['mutated']['failed']}/{r['mutated']['passed']}",f"{r['restored']['failed']}/{r['restored']['passed']}",'khớp' if r['restored_sha256']==r['original_sha256'] else 'SAI'] for r in mutations])
    findings_table=table(['Mức / mã','file:dòng','Đầu vào → kết quả sai','Sửa đề xuất và test','Bằng chứng / giới hạn'],[[r['severity']+' / '+r['id'],r['location'],r['scenario'],r['proposal']+' '+r['test'],r['evidence']+' '+r.get('limit','')] for r in findings])
    scopes='\n'.join(scope_data['new_other']+scope_data['removed_other']) or '(không có)'
    checks=[
      [1,'Worktree nguyên',f"329/329 hash; 37/37 hash bảo vệ; HEAD/status khớp; find -newer={integrity['find_newer_count']}; {integrity['node_modules_items']} mục node_modules + {integrity['results_json_files']} results.json không đổi",'Đạt'],
      [2,'Bản chép','329/329 ở cả hai bản; mỗi bản 11 symlink, node_modules là thư mục thật','Đạt'],
      [3,'pnpm check cuối','40 file / 414 xanh / 0 đỏ; kit 33; tsc/build qua; 79,60 / 81,16 kB khi biến vắng','Đạt'],
      [4,'Golden','2/2 same=true; 19.660 / 5.695 tick; 0 problems/rejected','Đạt'],
      [5,'Gói/quét','Cả ba deploy mã 0; hai production 0 host nhà/GLB/models/.vite; local kiểm production đúng 1 local-host; 0 prefix game khác','Đạt ca chuẩn'],
      [6,'Tách 170/208','patch mã 0/12 file; 19 đường=14 sửa+5 mới; 3 before khớp; 37/380; 69 lỗi; 55 file; 54/55 hash; 1.206.837 byte (+1.500)','Đạt'],
      [7,'Kit','31/31 module commit cha; README và verifier sinh khớp; verifier 33/33','Đạt'],
      [8,'Đột biến','4/4 bắt buộc đỏ rồi xanh; 2/2 bổ sung vẫn xanh, đã ghi P2; 329/329 nguồn trả lại','Đạt kiểm bắt buộc; phát hiện 2 hở test'],
      [9,'Phát hiện','P0=0; P1=2; P2=2; P3=0; mỗi dòng có file:dòng, kịch bản, đề xuất/test','Đã ghi'],
      [10,'Dọn/phạm vi',f"Bản chép không còn; tmp thêm {len(cleanup['other_added'])}/mất {len(cleanup['other_removed'])} mục khác; {len(scope_data['new_own'])} dòng mới của 224 đều trong hai đường cho phép; thay đổi khác tách riêng",'Đạt'],
    ]
    text=f'''# Phiếu 224 · Wordwoven · Kiểm lại độc lập 170 + 208

**Kết luận: commit được sau khi sửa các P0–P1 nêu.** Không có P0; có **2 P1** cần sửa ở plugin thay nguồn portal và bộ lọc symlink đứt, cùng **2 P2** về test chưa bắt hồi quy. Bản mã chuẩn hiện tại tái lập đầy đủ **40 file / 414 test xanh**, kit **33/33**, production và demo **0 lỗi**; đây chưa phải chứng nhận G7 trên server/trình duyệt.

Phiếu 224 chỉ kiểm trong bản chép, không sửa mã worktree, không commit. Bằng chứng ở [224/](224/); đường mã bên dưới tính từ `games/.wt-td-codex`. Làn s9; đọc yêu cầu model `gpt-6.1-sol`, mức `xhigh` của phiếu và bảng Chọn model, không tự đổi cấu hình runner. Dùng skill `threejs-qa-release` cho kiểm gói; không mở server/browser hoặc chạy bot ngoài phạm vi được giao.

## 1. Preflight, mốc đầu và bản chép

[preflight.txt](224/preflight.txt): **5/5 điều kiện đạt**. Nhánh `td-codex`, HEAD `f9abfd09987dadd519233c2f38692758d35cefca`; status khớp nguyên văn 208, **28 đường**. Đủ **13** đầu vào bắt buộc; thư mục tạm chưa tồn tại. Node **24.22.0**, pnpm **11.21.0**, có rsync/patch hệ thống.

[before.json](224/before.json): **328** đường Git và hợp với toàn bộ public thành **329** file; file thêm bị ignore là `public/assets/typing-defense/ui/title-dusk.webp`. **37/37** hash bảo vệ khớp 208/after (34 kit, 2 golden, 1 manifest model). Lưu tên/loại/mtime **14** mục node_modules và **1** results.json, cùng danh sách tmp checkout chính và status repo cha.

[copy.json](224/copy.json): `tree` và `tree-170` đều **329/329** SHA-256 khớp, mỗi bản **11** symlink tuyệt đối bên trong node_modules thật. Không symlink `.vite`, `.vite-temp`, workspace state. Tất cả pnpm dùng `pnpm_config_verify_deps_before_run=false`, `TMPDIR` riêng và chỉ cwd trong bản chép; biến portal vắng/trống/có được lưu ở mỗi `*-run.json`. Không install/add/sync/pull.

## 2. Tách 170/208 và kiểm trạng thái 170

[split.log](224/split.log), [split.json](224/split.json): `/usr/bin/patch -R -p1 -E` mã **0**, vá **12 file**, **0** rej/orig; **7/7** file mới 208 bị xóa. `learning.ts`, `vite.config.ts` khớp HEAD; **3/3** file chung khớp 208/before. Nền còn đúng **19 đường: 14 sửa, 5 mới**, trùng Nhóm 170; không tính title-dusk bị ignore. [paths.json](224/paths.json) phân loại đủ **28** đường và số dòng thêm/bớt của từng phiếu: **19 + 12 − 3**.

Nền 170: `pnpm check` mã **0**, **37 file / 380 test / 0 đỏ**, kit **33**, tsc/build qua; golden **6/6**. `deploy:pack` mã **1**, đúng **69 lỗi = 1 local-host + 68 missing-model**; checker local mã **1**, còn **68 missing-model**. Gói **55 file / 1.206.837 byte**, **54/55** SHA-256 trùng inventory 170. Chỉ `.vite/manifest.json` **16.655** thay **15.155** byte: **60 × 25 = 1.500 byte**, tiền tố thật `../../../../.wt-td-codex/`. Đây là khác biệt vị trí bản chép đã dự kiến, không phải hồi quy. [dist-170-comparison.json](224/dist-170-comparison.json), [manifest-paths.json](224/manifest-paths.json).

{(R.OUT/'requirements.md').read_text()}

## 3. Bảng đối chiếu số

Chép đầy đủ từ [claims.json](224/claims.json). Những hàng “khớp hồ sơ” chỉ đọc lại log cũ và hash bằng chứng, không gọi đó là lượt test mới; tải máy và thời gian lịch sử không thể tái hiện bằng mã cuối.

{claims_table}

`37/380 → 40/414` được đếm trực tiếp từ log: `portal.test.ts` **14**, `portal-build.test.ts` **7**, `deploy-prune.test.ts` **11** = **3 file / 32 test**; `deploy-pack.test.ts` **8→10**, tăng **2**. Tổng tăng **34**, không mất test cũ. [test-growth.json](224/test-growth.json). Lượt mới không có lỗi thời gian ngoài các lỗi cố ý gây bằng đột biến, nên không có file nào phải chạy riêng ba lần.

## 4. Các gói và quét

{table(['Gói / chế độ checker','Mã checker','Số lỗi','Theo code','File','Byte'],packs)}

Ba lệnh deploy (vắng/trống/local) đều mã **0**, lần lượt **{deploy_seconds} s**; riêng nền 170 mã **1** sau build. JSON và inventory lưu ở `pack-*.json`, `dist-*.json`, lệnh/env/mã/giây ở `*-run.json`. Gói biến trống **53/53 hash và byte trùng** 208/dist-final. Gói biến vắng ít hơn **264 byte**, chỉ learn **8.273** thay **8.537** byte; Vite gập hằng cho `portalHome(undefined)`, đúng nguyên nhân phiếu đã nêu. Tên chunk thay đổi theo hash của nội dung và tham chiếu import.

{table(['Gói','File văn bản','Chuỗi host nhà','Prefix / số lần','GLB/GLTF/BIN','Có .vite','Có models'],scanrows)}

[scan.json](224/scan.json) có số host nhà theo **từng file**, kể cả số 0, và mọi prefix khác nhau. Prefix game khác **0** trong cả ba gói. Local có **2 chuỗi** host trong một learn chunk, bộ kiểm báo **1 lỗi theo file**, đúng kỳ vọng. Mọi lượt prune bỏ **2 file / 39.623 byte**, hơn số 208 **1.500** vì 60 đường trong manifest Vite; file đó bị bỏ trước checker. Không lưu dist hoặc media trong thư mục bằng chứng.

`pnpm build` thường vẫn giữ model manifest và `.vite`: [build-only.json](224/build-only.json). Giao thức học chỉ ở learn chunk, entry có **0** chuỗi namespace học: [chunks.json](224/chunks.json); test chunk còn giữ LAZY/chunkOf/manualChunks và port 3006.

## 5. Đọc kỹ URL, bridge, plugin và prune

`portalHome`: undefined/rỗng/toàn khoảng trắng → null; bỏ khoảng trắng hai đầu; space trong hostname bị từ chối, space ở path thành `%20`. `user@` và `:pass@` bị từ chối. `https://@host/` và `https://:@host/` được URL parser chuẩn hóa thành không credentials; tab/newline giữa URL bị URL parser bỏ, `https:host` chuẩn hóa thành HTTPS. Đây là cách parse URL hiện có, không có thông tin đăng nhập bị gửi. Nếu muốn cú pháp chặt hơn thì cần quyết định/test riêng, không tự coi các chuẩn hóa này là P0/P1.

`javascript:`, `data:`, `file:`, `ftp:`, `ws:`, URL tương đối và protocol-relative đều bị từ chối. Cổng/query/fragment giữ trong href; bridge dùng `.origin`, giữ cổng khác mặc định và bỏ đường/query/fragment. `http:` production được nhận **đúng yêu cầu HTTP(S) của 208**, không có quy tắc HTTPS-only trong phiếu. Khuyến nghị vận hành dùng HTTPS khi portal thật dùng HTTPS; không tự thêm rào cản mới.

Bridge trống dùng `standaloneHost.parent=null`: constructor kit không flush, sendAttempt nối queue, flushQueue=0, requestFocus=false, không đăng ký listener thật. Với portal đã cấu hình, chỉ origin đó được postMessage và chỉ đúng parent+origin được nhận. Kit vẫn **xóa queue ngay sau gửi**, không chờ ack (`src/kit/learning/bridge.ts:149`); đây là hành vi kit có sẵn được 208 giữ, cần Claude kiểm rủi ro mất sự kiện nếu parent chưa sẵn sàng. Phiếu này không mở rộng thành sửa kit. Singleton nguồn hiện tại thực sự lười; test chưa chứng minh được thời điểm tạo (P2-02).

Plugin chỉ nhận đúng chuỗi id canonical. Probe Vite thật chứng minh `?v=`, `?import`, config qua symlink đều build xanh nhưng còn mặc định host nhà; synthetic id khác hoa/thường cũng không khớp. Không suy ra mọi import khác hoa/thường trên mọi filesystem đều build được. Không có guard khi contract chưa transform. Hàm replace riêng chặn 0/2 khai báo, giữ `$&` theo callback, và **CRLF qua/giữ CRLF**. Plugin cũng được đăng ký khi command=serve (chỉ kiểm config, không chạy dev). `.env.production` trong bản chép được load: có thể đặt origin khi process env vắng; process env `VITE_PORTAL_URL=''` ghi đè thành trống. [vite-probes.json](224/vite-probes.json).

Prune: URL `%2e%2e`, backslash, double encoding và URL tuyệt đối đều bị chặn trước xóa; query và fragment bỏ khi tìm file; duplicate keys được dedupe; phần tử không phải chuỗi và list thiếu models bị từ chối. Manifest không có models, khi chọn khóa, trả “Unknown model key” trước xóa; danh sách trống không cần đọc manifest để bỏ cây model. Danh sách đọc cạnh script, không phải cwd; README chỉ rõ file ở gốc game nhưng có thể thêm một câu về điều này. **27 probe**, sentinel ngoài dist **27/27 nguyên**; symlink sống **9/9 bị chặn**, dangling **6/7 bị bỏ sót**, index dangling bị chặn. [prune-probes.json](224/prune-probes.json). Các kiểm ngữ nghĩa của đường hợp lệ nằm trước lần ghi/xóa đầu; lỗi dangling là ngoại lệ đã tái hiện, không diễn giải thành đã xóa ngoài dist.

## 6. Kit và chất lượng test

[kit.json](224/kit.json): **31/31** file module bằng byte với `git show 1b1fe6cfacdc81a55d13af202da0f42023455313:shared/game-kit/<path>`; **0 khác**. README bằng byte README kit checkout chính và template sinh; verify-kit bằng byte export `VERIFY_SOURCE`. Import script sync không gọi main (guard gọi trực tiếp); không sync. Manifest ghi đúng commit cha, **parentDirty=true**. Verifier kiểm **33/33**, cộng manifest thành **34** file kit.

Portal test dùng bridge thật với host/storage giả; build test dùng cấu hình Vite thật và thực thi JS đầu ra bằng Node. Prune/check-pack là subprocess thật. Deploy fixture dùng build nhỏ giả để chứng minh chuỗi lệnh/chặn lỗi, được bổ sung bằng ba deploy thật. Test tải file dùng DOM/clipboard giả nhưng kiểm Blob, click, revoke, nội dung; B9 chạy CLI thật và so replay hash. `td-flow` giữ các khẳng định số và nhãn kit; không nới sang kiểm tồn tại chung chung.

Fixture của các file được hỏi đều dọn bằng finally, kể cả khi test đỏ trong M1–M4: cuối **0 fixture sót**. Timeout CLI **20 s** ở test B9 được chặn thêm bằng `spawnSync timeout=15 s`, không biến treo vô hạn thành xanh; không nới ngưỡng sim. Test prune subprocess chưa đặt timeout riêng, nên nếu chính script treo đồng bộ thì timeout Vitest không ngắt được `spawnSync`; hiện không có lỗi treo được quan sát, có thể bổ sung timeout tiến trình khi sửa test. Lần thử dùng `tsx` CLI của probe bị EPERM khi mở IPC pipe; đã đổi sang `node --import tsx`, giữ log thử đầu. Một lỗi script đo template thiếu biến `VERIFY_FILE` cũng được sửa trong script bằng chứng và giữ log; hai lỗi công cụ đo này không phải lỗi game.

## 7. Đột biến

{mutation_table}

[mutations.json](224/mutations.json) lưu test, mã thoát, số đỏ/xanh và hash từng lần. **4/4 đột biến bắt buộc bị bắt**, đúng số Claude từng thử; hai bổ sung M5/M6 lọt và được ghi P2. Sau mỗi lần đều chép lại từ worktree, xác minh SHA-256 rồi chạy lại cùng test. Cuối cùng **329/329** nguồn khớp mốc, không thêm nguồn khác khi bỏ generated `node_modules/dist/tmp`: [tree-final.json](224/tree-final.json).

## 8. Phát hiện

**P0: 0; P1: 2; P2: 2; P3: 0.** P1 cần xử lý trước khi nhận G7 và đề xuất sửa trước commit. P2 là hồi quy có thể lọt test, mã gốc tương ứng hiện đang đúng.

{findings_table}

## Cần trình duyệt của Claude

- Nhúng gói có `VITE_PORTAL_URL=https://typing-game.local/`: phím đầu tới game, requestFocus và sự kiện học tới portal; nhận nhạc/dataset từ đúng parent/origin, bỏ nguồn khác. Kiểm parent đã sẵn sàng trước khi bridge xả queue.
- Mở riêng không portal, rồi tải lại: queue giữ và không có tin ra ngoài; nhúng bản production không cấu hình cũng phải giữ queue.
- Gói production trên server tĩnh: đúng MIME/cache/base path, không 404, không request tới host khác hoặc repo cha; từ vựng ghim tải độc lập và không tải model thừa.
- Chơi tới màn kết, tải JSON có tên wordwoven-playtest; B9 nhận cả tên cũ/mới. Kiểm focus và vòng đời chunk Học trong trình duyệt thật. Phiếu này không chụp ảnh, không mở server/browser/mạng.

## 9. Dọn, bảo toàn và phạm vi

[integrity.json](224/integrity.json): trước/sau status khớp 208/status-final và HEAD nguyên; **329/329** hash bằng nhau; **37/37** hash bảo vệ; **14** mục node_modules và mtime **1** results.json không đổi. Lệnh find trước dọn ra **0** dòng: [worktree-newer.log](224/worktree-newer.log). `git diff --check` mã **0**. Không chạy node/pnpm với cwd worktree.

[cleanup.json](224/cleanup.json): `rm -rf games/typing-defense/tmp/codex-224` mã **0**, thư mục đã mất. Danh sách tmp checkout chính {'bằng mốc đầu' if not cleanup['other_added'] and not cleanup['other_removed'] else 'có thay đổi làn khác được liệt kê trong cleanup.json'}; thêm **{len(cleanup['other_added'])}**, mất **{len(cleanup['other_removed'])}** mục khác. Mục khác thêm: `{cleanup['other_added']}`; mất: `{cleanup['other_removed']}`. `codex-226` đã có trước và biến mất trong phiên; phiếu 224 không sửa hoặc xóa thư mục đó, không tính là lỗi của 224.

[scope.json](224/scope.json), [parent-before.txt](224/parent-before.txt), [parent-after.txt](224/parent-after.txt): status repo cha **{scope_data['before_lines']}→{scope_data['after_lines']}** dòng. **{len(scope_data['new_own'])}** dòng mới của phiếu chỉ thuộc `docs/codex-queue/224-report.md` và `docs/codex-queue/224/…`. Các dòng khác xuất hiện/biến mất trong phiên được liệt kê riêng dưới đây; không sửa hoặc dọn chúng:

```text
{scopes}
```

{table(['Kiểm','Nội dung','Số đo','Kết quả'],checks)}

## Việc của Claude

1. Đọc P1-01/P1-02 và bổ sung ca test tái hiện trước; sửa plugin canonicalize/guard và lstat cho symlink đứt. Nên sửa luôn hai lỗ test P2-01/P2-02. Chạy check và ba gói lại sau sửa; không lấy inventory 224 làm số cho mã đã đổi.
2. Duyệt/commit **170 trước**, theo nền 19 đường và ba file `208/before/`; sau đó **208** theo `208/208-only.patch`, kèm các sửa P1 của phần 208. Phiếu 224 không thay lượt duyệt/commit của Claude và không chạy Git ghi.
3. C13 của làn L điền deploy-models từ STARTER/NIGHT_1 khi game dùng model. Repo cha truyền `VITE_PORTAL_URL=https://typing-game.local/` cho build:td và dev:td:app theo đúng hai dòng ở 208-report §5; sửa các mục tài liệu còn ghi VITE_PORTAL_ORIGINS. README có thể nói rõ danh sách model được đọc cạnh script, độc lập cwd, và `.env*` cũng tham gia Vite loadEnv.
4. Chạy các bước ở “Cần trình duyệt của Claude”, rồi cổng G7 trên server tĩnh. Chủ dự án cần xem hai kịch bản P1 và xác nhận focus/sự kiện học/queue trên portal thật; số kiểm tĩnh xanh chưa thay phần đó.

Script chạy lại từ gốc repo cha và thứ tự lệnh ở [224/README.md](224/README.md). Không tạo ảnh/âm; không sửa lỗi nguồn, không sửa các phiếu/bằng chứng 168/170/208 hoặc file làn.
'''
    (R.OUT.parent/'224-report.md').write_text(text)

def verify():
    import ast
    report_path=R.OUT.parent/'224-report.md';text=report_path.read_text()
    json_files=list(R.OUT.glob('*.json'))
    for p in json_files:json.loads(p.read_text())
    for p in R.OUT.glob('*.py'):ast.parse(p.read_text())
    links=re.findall(r'\]\((224/[^)]+)\)',text)
    missing=[link for link in links if not (R.OUT.parent/link).exists()]
    forbidden=[str(p.relative_to(R.OUT)) for p in R.OUT.rglob('*') if p.is_file() and p.suffix.lower() in ['.png','.jpg','.jpeg','.webp','.glb','.gltf','.bin']]
    result={'json_files_parsed':len(json_files),'python_scripts_parsed':len(list(R.OUT.glob('*.py'))),'report_local_links_checked':len(links),'missing_links':missing,'forbidden_artifacts':forbidden,'copy_directory_absent':not R.C.exists(),'findings_by_level':dict(collections.Counter(x['severity'] for x in read('findings.json'))),'claims_rows':len(read('claims.json')),'scope_own_rows':len(read('scope.json')['new_own'])}
    assert not missing and not forbidden and not R.C.exists()
    assert read('test-growth.json')['check']['count_tests']==414
    assert read('integrity.json')['find_newer_count']==0
    R.save('verification.json',result)

if __name__=='__main__':
    if sys.argv[1:]==['--report-only']:
        scope();report(read('claims.json'));verify()
        print('Đã cập nhật báo cáo từ bằng chứng, không chạy lại build/test hoặc dọn.')
    elif not sys.argv[1:]:
        prepare();rows=claims();cleanup();scope();report(rows);verify()
        print('Đã kiểm nguyên worktree, xóa bản chép và viết 224-report.md.')
    else:raise SystemExit('Dùng finish.py [--report-only]')
