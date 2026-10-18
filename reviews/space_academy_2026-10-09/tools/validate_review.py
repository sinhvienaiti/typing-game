from pathlib import Path
from collections import Counter, deque
import hashlib, json, re, zipfile
root=Path(__file__).resolve().parents[1]
source=next((root/'source').iterdir())
archive=Path('/Users/jokerit/Downloads/SPACE_ACADEMY_DETAILED_PLANS_REVIEWED_V2_2026-10-09.zip')
files={int(p.name[:3]):p for p in source.glob('[0-9][0-9][0-9]_*.md') if p.name!='000_INDEX.md'}
assert sorted(files)==list(range(106))
checks=[]
checks.append('PASS — đúng 106 source sections, liên tục 000–105; index không tính như section.')
with zipfile.ZipFile(archive) as z:
 members=[n for n in z.namelist() if not n.endswith('/')]
 assert len(members)==110
 for n in members:
  assert (root/'source'/n).read_bytes()==z.read(n),n
checks.append('PASS — 110 source files giữ nguyên byte so với ZIP gốc.')
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(source.iterdir()) if p.is_file()}
(root/'SOURCE_HASHES.json').write_text(json.dumps({'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':hashes},indent=2)+'\n')
original=(source/'SPACE_ACADEMY_PRODUCT_VISION_AND_SYSTEM_IDEAS_REVIEW_DRAFT_2026-10-09.md').read_text()
sections=list(re.finditer(r'^# (\d+)\. .+$',original,re.M))
assert len(sections)==106
normalize=lambda t: re.sub(r'\s+',' ',re.sub(r'^---\s*$','',t,flags=re.M)).strip()
for i,m in enumerate(sections):
 body=original[m.end():sections[i+1].start() if i+1<len(sections) else len(original)]
 embed=files[int(m[1])].read_text().split('## 2. Ý tưởng gốc đã thống nhất',1)[1].split('## 3. Phạm vi V1 đề xuất',1)[0]
 assert normalize(body)==normalize(embed),m[1]
checks.append('PASS — 106/106 phần ý tưởng gốc tương đương consolidated source sau chuẩn hóa whitespace/separator; không phát hiện mất nội dung nguồn.')
rows=json.loads((root/'DECISIONS.json').read_text())
assert [r['id'] for r in rows]==list(range(106))
for r in rows:
 assert r['verdict'] in {'Keep','Simplify','Postpone','Reject'}
 assert all(r[k] for k in ['owner','critique','correction','risk','v1','v2','v3','source_file'])
 assert all(n in files for n in r['related_sections'])
 assert (root/r['source_file']).is_file()
headings=re.findall(r'^## (\d{3}) —', (root/'01_REVIEW_106_FILES.md').read_text(),re.M)
assert list(map(int,headings))==list(range(106))
checks.append('PASS — 106 review entries đúng thứ tự; mỗi mục đủ verdict, owner, phản biện, contract, rủi ro, V1/V2/V3 và reference.')
qs=list(map(int,re.findall(r'^\| (\d+) \|',(root/'04_OPEN_QUESTIONS.md').read_text(),re.M)))
assert qs==list(range(1,46))
checks.append('PASS — trả lời đủ 45/45 câu hỏi, đúng thứ tự mục 102.')
g=json.loads((root/'DEPENDENCY_GRAPH.json').read_text());ids={n['id'] for n in g['nodes']};assert len(ids)==len(g['nodes'])
def topo(edges):
 degree={n:0 for n in ids};adj={n:[] for n in ids}
 for e in edges:
  assert e['from'] in ids and e['to'] in ids
  degree[e['to']]+=1;adj[e['from']].append(e['to'])
 q=deque(n for n,d in degree.items() if d==0);out=[]
 while q:
  n=q.popleft();out.append(n)
  for m in adj[n]:
   degree[m]-=1
   if degree[m]==0:q.append(m)
 assert len(out)==len(ids),'dependency cycle'
 return out
order=topo(g['edges']);topo(g['edges']+g['conditional_edges'])
index={n:i for i,n in enumerate(g['topological_order'])}; assert set(index)==ids
assert all(index[e['from']]<index[e['to']] for e in g['edges'])
phase={n['id']:int(n['phase'][1:]) for n in g['nodes']}
assert all(phase[e['from']]<=phase[e['to']] for e in g['edges'])
for n in g['nodes']:assert all(s in files for s in n['sections'])
checks.append(f'PASS — {len(ids)} graph nodes, {len(g["edges"])} hard edges, {len(g["conditional_edges"])} conditional edges; không chu trình kể cả bật cả conditional; không phase phụ thuộc phase tương lai.')
# Every review-relative markdown file link must resolve; no network requests.
(root/'05_VERIFICATION.md').touch(exist_ok=True)
links=0
for p in root.glob('*.md'):
 assert not re.search(r'\[S\d{3}\]',p.read_text()),f'unexpanded reference {p}'
 assert p.read_text().count('```')%2==0,f'unbalanced fence {p}'
 for match in re.finditer(r'\]\(([^)]+)\)',p.read_text()):
  target=match[1]
  if target.startswith(('https://','http://','#','mailto:')):continue
  path=target.split('#')[0]
  if path:assert (p.parent/path).exists(),(p.name,path)
  links+=1
checks.append(f'PASS — {links} liên kết nội bộ của review resolve; code fences cân bằng, không placeholder source chưa thay.')
counts=Counter(r['verdict'] for r in rows)
report='# Verification của bộ review\n\nNgày: 2026-10-09. Kiểm tra tài liệu/artifact, **không phải** test implementation sản phẩm.\n\n'
report+='\n'.join('- '+c for c in checks)+'\n\n'
report+='## Verdict\n\n'+', '.join(f'**{k}: {counts[k]}**' for k in ['Keep','Simplify','Postpone','Reject'])+'.\n\n'
report+='## Đối chiếu self-review V2\n\nStructural completeness và source preservation được xác nhận lại độc lập bằng script. Tuy nhiên việc đủ section, có primary owner và giữ source không chứng minh kiến trúc đúng. 18 finding trong tài liệu 00 cho thấy template bleed, duplicate authority, missing contracts và scope contradictions còn tồn tại.\n\n'
report+='## Giới hạn kiểm chứng\n\nKhông benchmark app, không chạy migration, không thực hiện penetration test, không thử hiệu quả học hay economy trên người dùng. Graph đã kiểm tra cấu trúc DAG và reference; Mermaid source chưa được render bằng browser trong tác vụ này. Đánh giá nội dung là review thủ công; checksum/coverage không thay thế semantic review. Số budget/capacity và cohort là đề xuất cần pilot. Không code sản phẩm nào bị sửa trong tác vụ review.\n\n'
report+='## Tái kiểm tra\n\n```sh\npython3 reviews/space_academy_2026-10-09/tools/validate_review.py\n```\n\nScript dùng đường dẫn ZIP gốc để so byte; khi chuyển máy, cập nhật đường dẫn archive hoặc dùng SOURCE_HASHES.json để đối chiếu file. DECISIONS.json là structured review; decisions.psv là input để sinh file-by-file. DEPENDENCY_GRAPH.json/Mermaid là graph cuối.\n'
(root/'05_VERIFICATION.md').write_text(report)
print('\n'.join(checks));print(dict(counts))
