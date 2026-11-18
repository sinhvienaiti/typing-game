import json, glob, os, re, collections
import sys
# Usage: python3 tools/agent-usage/usage.py <session-transcript-dir-without-.jsonl> <start-UTC e.g. 2026-11-03T17:00:00>
# Effective tokens = input + 0.1 cache reads + 2 cache writes + 5 output. Groups: main-thread tool kinds; subagents by
# role (browser assistants when >25 % of their calls drive the browser, critics, authors, captures, other work).
P=sys.argv[1]
START=sys.argv[2] if len(sys.argv)>2 else '2026-11-03T17:00:00'
def eff(u):
    return (u.get('input_tokens',0) + 0.1*u.get('cache_read_input_tokens',0) + 2*u.get('cache_creation_input_tokens',0) + 5*u.get('output_tokens',0))
def scan(path):
    seen=set(); calls=[]
    for l in open(path, errors='ignore'):
        try: d=json.loads(l)
        except: continue
        if d.get('type')!='assistant': continue
        t=d.get('timestamp','')
        if t < START: continue
        m=d.get('message',{}); u=m.get('usage')
        if not u: continue
        mid=m.get('id') or d.get('requestId')
        tools=[c.get('name') for c in m.get('content',[]) if isinstance(c,dict) and c.get('type')=='tool_use']
        if mid in seen:
            # merge tool names into last call with same id
            for c in calls:
                if c['id']==mid: c['tools']+=tools
            continue
        seen.add(mid)
        calls.append({'id':mid,'t':t,'u':u,'tools':tools})
    return calls
def cat_tool(names):
    if not names: return 'trả lời / suy nghĩ (không gọi công cụ)'
    n=names[0]
    if n.startswith('mcp__Claude_Browser__'): return 'trình duyệt (ChatGPT, Gemini, Firefly, lab)'
    if n.startswith('mcp__claude-in-chrome__'): return 'Claude in Chrome'
    if n in ('WebSearch','WebFetch'): return 'tra cứu web'
    if n in ('Read','Write','Edit','NotebookEdit'): return 'đọc/sửa file'
    if n=='Bash': return 'lệnh Bash (chạy test, ffmpeg, git, đo)'
    if n in ('Agent','Workflow','SendMessage','TaskStop','Monitor','ReadNotifications'): return 'điều phối agent'
    if n.startswith('mcp__ccd_turn__') or n.startswith('mcp__ccd'): return 'cập nhật danh sách việc / báo cáo'
    if n in ('SendUserFile','AskUserQuestion'): return 'gửi file / hỏi anh'
    if n.startswith('mcp__'): return 'connector khác'
    return 'khác ('+n+')'
out={}
# main thread
main=scan(P+'.jsonl')
mt=collections.Counter(); ninstr=0
for c in main:
    u=c['u']
    instr=0.1*min(u.get('cache_read_input_tokens',0), 45000)  # system prompt + tools ~45k re-read each call
    mt['main: đọc lại hướng dẫn hệ thống mỗi lượt']+=instr
    mt['main: '+cat_tool(c['tools'])]+=eff(u)-instr
print('main calls', len(main))
# subagents
agents=[]
for f in glob.glob(P+'/subagents/**/agent-*.jsonl', recursive=True):
    meta=f[:-6]+'.meta.json'
    desc=''
    try: desc=json.load(open(meta)).get('description','')
    except: pass
    calls=scan(f)
    if not calls: continue
    e=sum(eff(c['u']) for c in calls)
    br=sum(1 for c in calls for n in c['tools'] if n and n.startswith('mcp__Claude_Browser__'))
    tot=sum(len(c['tools']) for c in calls)
    agents.append((e, desc, len(calls), br, tot, f.split('/subagents/')[1]))
agents.sort(reverse=True)
def stage(desc, br, tot):
    d=desc.lower()
    if tot and br/tot > 0.25: return 'sub: làm việc trên trình duyệt (ChatGPT/Gemini/Firefly)'
    if re.match(r'^(critic|fix)\d|critic|ticket critic|design critic|ticket-1 critic', d): return 'sub: phản biện phiếu (critic + sửa)'
    if d.startswith('author') or d.startswith('analysis') or 'draft' in d or 'ticket' in d or 'plan' in d: return 'sub: viết lời giải / phân tích'
    if tot and br/tot > 0.25: return 'sub: làm việc trên trình duyệt (ChatGPT/Gemini/Firefly)'
    if any(k in d for k in ('demo','checks','video','capture','measure','judge','review:','sheet','parity')): return 'sub: quay, đo, kiểm, video cho anh'
    return 'sub: làm thật bằng agent Claude (dựng mã hộp xám, Blender, âm, ảnh, audit)'
st=collections.Counter(); cnt=collections.Counter()
for e,desc,n,br,tot,f in agents:
    s=stage(desc,br,tot); st[s]+=e; cnt[s]+=1
total=sum(mt.values())+sum(st.values())
print('TOTAL effective (M):', round(total/1e6,1), ' subagents:', len(agents))
rows=sorted(list(mt.items())+list(st.items()), key=lambda x:-x[1])
for k,v in rows:
    extra=f' ({cnt[k]} agent)' if k in cnt else ''
    print(f'{v/total*100:5.1f}%  {v/1e6:7.1f}M  {k}{extra}')
print('\nTop 15 agents:')
for e,desc,n,br,tot,f in agents[:15]:
    print(f'{e/1e6:6.1f}M  calls={n:4d} browser={br:3d}/{tot:4d}  {desc[:70]}')

