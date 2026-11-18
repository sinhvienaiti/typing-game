from pathlib import Path
import re, json, collections
root=Path(__file__).resolve().parents[1]
source=next((root/'source').iterdir())
files={int(p.name[:3]):p for p in source.glob('[0-9][0-9][0-9]_*.md') if p.name!='000_INDEX.md'}
rows=[]
for line in (root/'decisions.psv').read_text().splitlines():
 vals=line.split('|')
 assert len(vals)==10,vals[0]
 keys=['id','verdict','owner','critique','correction','risk','v1','v2','v3','related_sections']
 row=dict(zip(keys,vals)); row['id']=int(row['id']); row['related_sections']=[int(s) for s in row['related_sections'].split(',')]
 row['source_file']=str(files[row['id']].relative_to(root)); rows.append(row)
assert [r['id'] for r in rows]==list(range(106))
counts=collections.Counter(r['verdict'] for r in rows)
(root/'DECISIONS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
out=['# Review đủ 106 mục theo thứ tự\n', 'Mỗi mục bên dưới là delta hiệu chỉnh so với source. **Keep** = giữ ý chính nhưng vẫn bổ sung contract; **Simplify** = cắt/đổi scope; **Postpone** = giữ làm ứng viên sau gate; **Reject** = bỏ cơ chế hoặc thứ tự đề xuất, không phủ định toàn bộ chủ đề. V2/V3 là gợi ý có điều kiện, không cam kết tất cả.\n', 'Đối với mọi runtime feature: authorization phía server; payload/list có giới hạn; retry có idempotency khi ghi state; private data không vào analytics; route nặng lazy-load; mobile/keyboard/mute/reduced-motion là gate. Các rủi ro riêng ghi từng mục dưới đây. Concept/policy/example không sinh DB/API riêng; performance/security áp lên consumer thực thi, không dựng runtime cho tài liệu.\n', 'Các “mục liên quan” dùng để truy vết, **không** là hard dependency graph; xem [DAG cuối cùng](03_ROADMAP_DEPENDENCY_GRAPH.md). Schema/API chi tiết dùng chung ở [02](02_ARCHITECTURE_CONTRACTS.md), không nhân bản bảng theo file.\n', '**Tổng verdict:** '+', '.join(f'{k}: {v}' for k,v in sorted(counts.items()))+'.\n']
for r in rows:
 title=files[r['id']].read_text().splitlines()[0].lstrip('# ')
 out+= [f"## {r['id']:03d} — {title.split('. ',1)[1]}\n",f"[Source]({r['source_file']}) — **{r['verdict']}**. **Owner:** {r['owner']}.\n",f"**Phản biện:** {r['critique']}\n",f"**Sửa scope/schema/API:** {r['correction']}\n",f"**Dữ liệu / an toàn / hiệu năng:** {r['risk']}\n",f"**V1:** {r['v1']}. **V2:** {r['v2']}. **V3:** {r['v3']}.\n",'**Mục liên quan:** '+', '.join(f'[S{i:03d}]' for i in r['related_sections'])+'.\n']
(root/'01_REVIEW_106_FILES.md').write_text('\n'.join(out))
# Explicit prerequisite DAG; no domain is converted to a microservice by this list.
spec='''BASE|V1|Baseline repo, contract fixtures, migration inventory||070,069,082
ACCESS|V1|Account, authorization, privacy policy|BASE|030,078
SHELL|V1|Shell, design tokens, budgets, mobile|BASE|003,039,073,074,075
OPS|V1|Audit, publish tooling, support, restore|ACCESS|078,014
CONTENT|V1|Canonical content, rights, versions|OPS|070,071,023
MEDIA|V1|Published learning media + manifest|CONTENT,SHELL|072,040
LESSON|V1|Versioned lesson runner + resume|CONTENT,MEDIA,ACCESS,SHELL|012,025
EVIDENCE|V1|Attempts, skill evidence, review queue|LESSON,ACCESS|027,097
BRIDGE|V1|Adapters and server authority cutover|EVIDENCE,BASE|026,069,070
HOME|V1|Learn-only UX and progress|LESSON,EVIDENCE,BRIDGE|085,028,029
G1|V1|Core learning pilot gate|HOME,OPS,MEDIA,SHELL|083,097
SAFETY|V2|Moderation queue, ACL enforcement, operators|G1,ACCESS,OPS|064,030
CLASS|V2|Cohort, teacher, assignments, async class|G1,LESSON,EVIDENCE,OPS|008,009,011,015,019
CHAT|V2|Private class text room|CLASS,SAFETY|064,065
GCLASS|V2|Class-with-chat pilot gate|CLASS,CHAT,SAFETY|086,096
CALENDAR|V2|Class calendar read model|CLASS|013,062
AVATAR|V2|Single-pose renderer, free preview, compatibility|G1,MEDIA,SHELL|031,032,033,034
SIM|V2|Reward rule core and simulator fixtures|G1,EVIDENCE,OPS|079,043,076
ECON|V2|Credit ledger, grants, catalog, entitlements|SIM,EVIDENCE,ACCESS,OPS|050,043,047,048
SHOP|V2|Fixed-price catalog, purchase, equip, receipt|ECON,AVATAR|035,049,051,052
GECON|V2|Economy and shop launch gate|SIM,ECON,SHOP|079,076,093
IELTS|V2|Curated R/L assessment adapter|G1,CONTENT,LESSON,EVIDENCE,MEDIA|024,023
MENTOR|V2|Scoped optional NPC context and text/voice|G1,EVIDENCE,ACCESS,MEDIA|010,041,095
VERIFY|V3|Competitive challenge, evidence review, appeals|G1,BRIDGE,ACCESS,OPS|077,026
PRESTIGE|V3|Rank rules, season finalization, award revisions|VERIFY,EVIDENCE,OPS|054,055,057,058,059
GPRESTIGE|V3|Verified competition release gate|VERIFY,PRESTIGE|077,087
LIVE|V3|Async campaigns, occurrence jobs, cancellation|G1,OPS,CONTENT,EVIDENCE|061,063,081,099
TOURNAMENT|V3|Tournament format and adjudication|GPRESTIGE,LIVE|060,020
COMMUNITY|V3|Invite-only clubs and study rooms|GCLASS,SAFETY|017,066,067
FULLIELTS|V3|Full mock and calibrated W/S, conditional|IELTS,ACCESS,OPS|024,060'''
nodes=[]; edges=[]
for line in spec.splitlines():
 id,phase,label,deps,refs=line.split('|')
 nodes.append({'id':id,'phase':phase,'label':label,'sections':[int(s) for s in refs.split(',')]})
 for dep in filter(None,deps.split(',')): edges.append({'from':dep,'to':id,'kind':'hard','reason':f'{id} cần capability {dep} trong scope đã chọn'})
conditional=[{'from':'GECON','to':'LIVE','condition':'Campaign cấp currency/item reward'}, {'from':'GPRESTIGE','to':'LIVE','condition':'Campaign trao competitive award'}, {'from':'GCLASS','to':'LIVE','condition':'Campaign gắn lớp có chat'}]
ids={n['id'] for n in nodes}; indeg={i:0 for i in ids}; adj={i:[] for i in ids}
for e in edges:
 assert e['from'] in ids and e['to'] in ids
 indeg[e['to']]+=1; adj[e['from']].append(e['to'])
order=[]; queue=collections.deque(sorted(i for i,d in indeg.items() if not d))
while queue:
 x=queue.popleft();order.append(x)
 for y in adj[x]:
  indeg[y]-=1
  if not indeg[y]:queue.append(y)
assert len(order)==len(nodes),'cycle'
graph={'edge_semantics':'prerequisite -> dependent','nodes':nodes,'edges':edges,'conditional_edges':conditional,'topological_order':order}
(root/'DEPENDENCY_GRAPH.json').write_text(json.dumps(graph,ensure_ascii=False,indent=2)+'\n')
m=['flowchart TD']
for phase in ['V1','V2','V3']:
 m.append(f'  subgraph {phase}["{phase}"]')
 for n in nodes:
  if n['phase']==phase:m.append(f'    {n["id"]}["{n["id"]}: {n["label"]}"]')
 m.append('  end')
for e in edges:m.append(f'  {e["from"]} --> {e["to"]}')
for e in conditional:m.append(f'  {e["from"]} -.->|"{e["condition"]}"| {e["to"]}')
(root/'DEPENDENCY_GRAPH.mmd').write_text('\n'.join(m)+'\n')
block='```mermaid\n'+'\n'.join(m)+'\n```\n\n'
block+='Đồ thị đầy đủ: [JSON](DEPENDENCY_GRAPH.json), [Mermaid](DEPENDENCY_GRAPH.mmd). Một thứ tự topo hợp lệ (các nhánh độc lập có thể đổi chỗ):\n\n`'+' → '.join(order)+'`\n\n'
block+='| Node | Phase | Capability | Hard prerequisites | Mục nguồn |\n|---|---|---|---|---|\n'
for n in nodes:
 deps=[e['from'] for e in edges if e['to']==n['id']]
 block+=f'| {n["id"]} | {n["phase"]} | {n["label"]} | {", ".join(deps) or "—"} | '+', '.join(f'[S{i:03d}]' for i in n['sections'])+' |\n'
p=root/'03_ROADMAP_DEPENDENCY_GRAPH.md'; t=p.read_text(); marker='<!-- GENERATED_GRAPH -->'
if marker in t: t=t.replace(marker, '<!-- GRAPH_START -->\n'+block+'<!-- GRAPH_END -->')
elif '<!-- GRAPH_START -->' in t: t=re.sub(r'<!-- GRAPH_START -->[\s\S]*?<!-- GRAPH_END -->', lambda m: '<!-- GRAPH_START -->\n'+block+'<!-- GRAPH_END -->', t)
p.write_text(t)
for p in root.glob('*.md'):
 def ref(m):
  i=int(m[1]); return f'[{i:03d}]({files[i].relative_to(root)})'
 p.write_text(re.sub(r'\[S(\d{3})\]',ref,p.read_text()))
print(dict(counts));print(f'{len(nodes)} nodes, {len(edges)} hard edges, {len(conditional)} conditional edges; DAG valid')
