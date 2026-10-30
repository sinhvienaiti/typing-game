"""Dựng danh sách từ bản chụp nguồn đã đọc; chỉ ghi trong phạm vi phiếu 213."""
from pathlib import Path
import json, re, subprocess, hashlib

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'docs/codex-queue/213'
DEST = ROOT / 'docs/games/audio/firefly'
snap = json.loads((OUT / 'source-snapshot.json').read_text())
def save(p, obj): p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
def scalar(s):
    s=s.strip()
    if len(s)>1 and s[0]==s[-1] and s[0] in "\"'":
        return json.loads(s) if s[0]=='"' else s[1:-1].replace("''", "'")
    return s
def card(p):
    s=p.read_text()
    def get(pattern):
        m=re.search(pattern,s,re.M)
        if not m: raise ValueError((p,pattern))
        return scalar(m[1])
    return dict(id=p.stem, when=get(r'^when: (.*)$'), purpose=get(r'^purpose: (.*)$'),
                prompt=get(r'^  text: (.*)$'), min=int(get(r'^  min_ms: (\d+)$')),
                max=int(get(r'^  max_ms: (\d+)$')), variants=int(get(r'^variants:\s*\n  target: (\d+)$')),
                mode=get(r'^  mode: (.*)$'), channels=get(r'^  channels: (.*)$'), path=str(p.relative_to(ROOT)))
specs={p.stem:card(p) for p in (ROOT/'tools/audio-lab/specs/dragon-hold').glob('*.yaml') if not p.stem.startswith('music.')}
catalog={}
for i,l in enumerate(snap['main:src/audio/catalog.ts'].splitlines(),1):
    m=re.search(r'"([^"]+)": def\("([^"]+)", (\d), ([\d_]+),.*',l)
    if m: catalog[m[1]]=dict(bus=m[2], priority=int(m[3]), lengthMs=int(m[4].replace('_','')), loop='loop: true' in l, line=i)
assert len(catalog)==83
save(OUT/'spec-evidence.json',specs)

def refs(branch, file, needles):
    lines=snap[branch+':'+file].splitlines()
    return [f'{branch}:games/dragon-hold/{file}:{i}' for i,l in enumerate(lines,1) if any(n in l for n in needles)]
direct={}
for id in catalog:
    sources=[]
    for b in ['main','dh-vfx']:
        for f in ['src/audio/map-events.ts','src/audio/index.ts']:
            # Only callsites, not id declarations or import comments.
            for i,l in enumerate(snap[b+':'+f].splitlines(),1):
                if '"'+id+'"' in l and any(x in l for x in ['this.push(', 'this.at(', 'const id:', '? "', 'engine.bed(', 'engine.play(']):
                    sources.append(f'{b}:games/dragon-hold/{f}:{i}')
    direct[id]=sources
dynamic={
 'impact.multi':['this.push("impact.multi"'],
 'fire.impact.a':['this.at(id, event.x, event.z, listener, { variant'],
 'fire.impact.b':['this.at(id, event.x, event.z, listener, { variant'],
 'fire.impact.c':['this.at(id, event.x, event.z, listener, { variant'],
 'dragon.breath':['event.skill === "breath"','if (id) this.push(id)'],
 'dragon.skyfire.cast':['event.skill === "breath"','if (id) this.push(id)'],
 'dragon.roar':['event.skill === "breath"','if (id) this.push(id)'],
 'dragon.inferno':['event.skill === "breath"','if (id) this.push(id)'],
 'dragon.low':['return "dragon.low"'], 'dragon.heartbeat':['return "dragon.heartbeat"'],
}
for id in catalog:
    if id.startswith('enemy.') and id!='enemy.quadruped.howl':
        slot=id.rsplit('.',1)[1]
        dynamic[id]=[{'spawn':'this.at(CLASS_SETS[voice.cls].spawn','windup':'this.at(CLASS_SETS[voice.cls].windup','attack':'this.at(id, event.x, event.z, listener, { rate','shoot':'this.at(id, event.x, event.z, listener, { rate','charge':'this.at(id, event.x, event.z, listener, { rate','hit':'this.at(CLASS_SETS[voice.cls].hit','death':'this.at(CLASS_SETS[cls].death'}.get(slot,'NEVER')]
    if id.startswith('general.g01.'):
        slot=id.rsplit('.',1)[1]
        dynamic[id]=[{'horn':'this.at(set.horn','attack':'this.at(id, event.x, event.z, listener, { rate','skill':'this.at(set.skill','aura':'event.on ? set.aura','death':'this.at(set.death'}[slot]]
    if id.startswith('trap.'):
        dynamic[id]=['this.push(placeSound(event.item))' if id.endswith('.arm') else 'this.at(sounds.trigger']
for id,needles in dynamic.items():
    for b in ['main','dh-vfx']:direct[id]+=refs(b,'src/audio/map-events.ts',needles)
for id in catalog:
    if id.endswith('.march'):
        for b in ['main','dh-vfx']:direct[id]+=refs(b,'src/audio/index.ts',['engine.bed(CLASS_SETS[cls].march'])
    if id.startswith('ui.') or id.startswith('learn.'):
        for b in ['main','dh-vfx']:direct[id]+=refs(b,'src/audio/index.ts',['id: `ui.${sound}`' if id.startswith('ui.') else 'id: `learn.${sound}`'])
    if id in ['dragon.low','dragon.heartbeat']:
        for b in ['main','dh-vfx']:direct[id]+=refs(b,'src/audio/index.ts',['if (alarmCue) engine.play'])
    if id=='house.herb.place':
        for b in ['main','dh-vfx']:direct[id]+=refs(b,'src/audio/map-events.ts',['this.push(placeSound(event.item))'])
    direct[id]=sorted(set(direct[id]))
assert [id for id,rs in direct.items() if not rs]==['enemy.quadruped.howl']

names={'moss-grunt':'Moss Grunt','moss-archer':'Moss Archer','tusk-boar':'Tusk Boar','blight-wolf':'Blight Wolf','thorn-wasp':'Thorn Wasp','thorn-ant':'Thorn Ant','moss-banner':'Moss Bannerman'}
classes={'moss-grunt':'biped','moss-archer':'biped','tusk-boar':'quadruped','blight-wolf':'quadruped','thorn-wasp':'flyer','thorn-ant':'swarm','moss-banner':'biped'}
own={}
for foe in names:
    for slot in ['spawn','move','attack','hit','death']:
        id=('general.' if foe=='moss-banner' else 'enemy.')+foe+'.'+slot
        fallback='enemy.'+classes[foe]+'.'+('march' if slot=='move' else 'shoot' if slot=='attack' and foe=='moss-archer' else 'charge' if slot=='attack' and foe=='tusk-boar' else slot)
        if foe=='moss-banner' and slot in ['spawn','attack','death']:fallback='general.g01.'+{'spawn':'horn','attack':'attack','death':'death'}[slot]
        needles={'spawn':['file: foeSfx(event.foe)?.spawn'], 'move':['foeSfx(entry.lead)?.move'], 'attack':['file: foeSfx(this.foes.get(event.source.serial) ?? "")?.attack'], 'hit':['const own = foeSfx','file: foeSfx(this.foes.get(target.serial) ?? "")?.hit'], 'death':['file: foeSfx(fold.foe)?.death']}[slot]
        calls=refs('dh-vfx','src/audio/index.ts' if slot=='move' else 'src/audio/map-events.ts',needles)
        acceptedOnly=foe=='moss-banner' and slot in ['spawn','death']
        if acceptedOnly:calls=[]
        own[id]=dict(foe=foe,slot=slot,fallback=fallback,sources=calls,acceptedOnly=acceptedOnly)

fired=[]
for id,rs in direct.items():
    if rs:fired.append(dict(id=id,branches=['main','dh-vfx'],sources=rs,status='routed',condition=specs[id]['when']))
for id,x in own.items():
    if not x['acceptedOnly']:fired.append(dict(id=id,branches=['dh-vfx'],sources=x['sources'],status='file-conditional',condition='Có file riêng; move chọn loài dẫn đầu của lớp khi khởi tạo bed.',fallback=x['fallback']))
save(OUT/'fired-ids.json',dict(stage='L2-cau',sourceCommits={b:subprocess.check_output(['git','-C',str(ROOT/'games/dragon-hold'),'rev-parse','--short',b],text=True).strip() for b in ['main','dh-vfx']},ids=fired,manifestOnly=[dict(id=id,reason='G01 trả về sớm trước đường spawn/death lớp; manifest nhận nhưng chưa gọi riêng.',sources=refs('dh-vfx','src/audio/catalog.ts',['export function foeSfx','return { spawn:','export const FOE_SFX_IDS'])) for id,x in own.items() if x['acceptedOnly']],scope=dict(foes=list(names),carry=['spikes','pine-bomb','net-launcher','moss-warden','herb-hut','small-potion'],skills=['breath','skyfire','roar','inferno']),foeSfxTotal=35,foeSfxOutsideMap=0))

fire=['fire.cast','fire.impact.a','fire.impact.b','fire.impact.c','impact.multi','dragon.breath','dragon.skyfire.cast','dragon.skyfire.impact','dragon.inferno']
groups=['Lửa','Rồng (khác lửa)','Quái','G01','Bẫy và phe ta','Báo nguy và mốc trận','UI và học','Nền']
def group(id):
    if id in fire:return groups[0]
    if id in ['dragon.low','dragon.heartbeat'] or id.startswith(('warn.','wave.','stinger.')):return groups[5]
    if id.startswith('dragon.'):return groups[1]
    if id.startswith('general.'):return groups[3]
    if id.startswith('enemy.') or id=='kill.chime':return groups[2]
    if id.startswith(('trap.','unit.','house.')):return groups[4]
    if id.startswith('amb.'):return groups[7]
    return groups[6]

display={'dragon.breath':'Fire Breath','dragon.skyfire.cast':'Sky Fire','dragon.skyfire.impact':'Sky Fire / Inferno','dragon.roar':'Dragon Roar','dragon.inferno':'Inferno','dragon.potion':'Small Potion'}
for id in catalog:
    if id.startswith('trap.'):display[id]={'spikes':'Spikes','pine-bomb':'Pine Bomb','net':'Net Launcher'}[id.split('.')[1]]
    if id.startswith('unit.warden'):display[id]='Grove Warden'
    if id.startswith('house.herb'):display[id]='Herb Hut'
    if id.startswith('general.g01'):display[id]='Moss Bannerman'
def label(id):
    if id in display:return display[id]
    if id in own:return names[own[id]['foe']]
    return id.replace('.',' ').replace('-',' ').title()

special={
 'amb.forest':'Seamless wind through tall pines in a deep mountain pass, soft gusts and low granite-cliff reflections, 6 s.',
 'learn.wrong':'Gentle low falling wooden note, a warm reflective answer cue with a brief soft resonance, 380 ms.',
 'type.miss':'Soft muted wooden knock, gentle error tick with a tiny dry woody body, immediate attack, 60 ms.',
 'warn.strike':'Two clear high woodblock knocks, an urgent restrained alert with a short wooden resonance, 260 ms.',
 'dragon.low':'Low two-note warning horn over a soft low war-drum pulse, urgent restrained tone, 900 ms.',
 'fire.cast':'The fire dragon releases a fireball: a large throat rasp layered with sharp pressurised flame ignition at 0 ms, roaring flame body to 200 ms, dense receding flight rush to 350 ms, low valley echo to 750 ms. Match the mouth flash within 17 ms. Energy at 1-4 kHz falls 15 dB within 100 ms; the tail sits below 1 kHz.',
 'fire.impact.a':'Fireball contact: sharp flame rupture at 0 ms, rolling fire body to 300 ms, ember crackle and scattered debris, low pine-valley echo to 600 ms. Match the first contact flash within 17 ms; smoke rises from 133-233 ms. Energy at 1-4 kHz falls 15 dB within 100 ms; the tail sits below 1 kHz.',
 'fire.impact.b':'Darker fireball contact: deep flame rupture at 0 ms, rolling fire body to 320 ms, dry ember crackles and wooden splinters, low pine-valley echo to 640 ms. Match the first contact flash within 17 ms; smoke rises from 133-233 ms. Energy at 1-4 kHz falls 15 dB within 100 ms; the tail sits below 1 kHz.',
 'fire.impact.c':'Heavy fireball contact: a weighty flame explosion at 0 ms, rolling fire body to 450 ms, embers and debris flung wide, low mountain-valley echo to 1000 ms. Match the contact flash within 17 ms; smoke rises from 133-233 ms. Energy at 1-4 kHz falls 15 dB within 100 ms; the tail sits below 1 kHz.',
 'impact.multi':'Layer beneath a fireball striking several targets: weighted flame ruptures at 0 ms and across 45 ms, broad fire body to 400 ms, scattered ember crackles and debris, low forest-valley echo to 700 ms. Align the first attack with the gathered contact flashes within 17 ms. Energy at 1-4 kHz falls 15 dB within 100 ms; the tail sits below 1 kHz.',
 'dragon.skyfire.cast':'The fire dragon charges and launches a huge fireball across a mountain pass: deep intake and throat rumble from 0 to 200 ms, forceful flame ignition at 200 ms, rising then descending fire roar and rushing air to 800 ms, low valley tail to 900 ms. Match the mouth release at 200 ms within 17 ms; ease the flight into the separate impact at 800 ms.',
 'dragon.skyfire.impact':'A huge fireball hits the ground: cracking blast at 0 ms, deep earth-shaking body under roaring fire to 670 ms, rocks and embers scattering from 33 ms, rolling low valley echo to 1800 ms. Match the contact flash within 17 ms. Ground flames rise from 100-233 ms; smoke rolls from 367-567 ms. The same blast marks the final strike of Inferno.',
 'dragon.breath':'The fire dragon exhales a broad flame jet: immediate deep throat intake layered into forceful ignition at 0 ms, pressurised rolling flame and crackle through 700 ms, dying embers and low granite-valley echo to 1650 ms. Match the mouth emitter onset within 17 ms.',
 'dragon.inferno':'The fire dragon unleashes Inferno: immediate deep inhale layered into a giant pressurised fire release at 0 ms, wide blazing roar with a low choir swell to 1600 ms, ember crackle and deep mountain-valley echo to 2400 ms. Match the fire crown onset within 17 ms; this sound marks the opening of a ten-second skill.',
}
clipmeta=json.loads((OUT/'clip-metadata.json').read_text())['flipbooks']
def clip(id,phase,start,length,note):return dict(clip=id,phase=phase,startMs=round(start),lengthMs=round(length),syncNote=note)
def impact_clips(strong=False):
    out=[]
    for id in ['impact-burst','fire-burst','impact-big']:
        fps=clipmeta.get(id,{}).get('fps',24)
        frame,last,rate=(20,23,.75) if id=='impact-big' else (11,19,1.8) if strong else (10,20,2)
        ms=(last+1-frame)/fps/rate*1000
        n=f'dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. {"Mạnh" if strong else "Thường"}: frame={frame}, until={last}, rate={rate}, fps={fps}; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo.'
        if id=='fire-burst':n+=' Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp.'
        out += [clip(id,'I',0,ms,n),clip(id,'I',1000*2/60,ms/1.15,n+' Khối phụ trễ 2 khung, rate ×1,15.')]
    out += [clip('smoke-mask','F',1000*8/60,1100,'fx.ts:1602–1607; life=1,1 s, rate=2,6, fps=8; khói thay thế smoke-roll, fadeIn=100 ms. Đuôi thấp đi cùng khói; không kéo dài âm quá catalog.'),clip('smoke-roll','F',1000*14/60,1000,'fx.ts:1602–1607; dự phòng khi chưa có smoke-mask; life=1 s, rate=2,6, fps=8; fadeIn=100 ms. Đuôi thấp đi cùng khói.')]
    return out
clips={id:[] for id in fire}
clips['fire.cast']=[clip('muzzle-flash','R',0,1000*4/60,'fx.ts:1196–1198; frame=6, rate=1, fps=24, life=4/60 s; đòn mạnh life=5/60 s (83 ms). Khè và bắt lửa cùng mốc R trong 17 ms; không thêm gồng sau phím cuối.'),clip('fireball-head','T',1000/60,1000*11/60,'fx.ts:1376,2104,2121–2127; ONE_FRAME=0,1 ms được vẽ lại suốt đường bay; out=0 ở tuổi ≤1/60, hiện từ khung kế tiếp (khoảng 17–33 ms). Đây là cửa sổ danh định 12 tick=200 ms; thời gian thực theo min(0,2; max(0,12; distance/18)), catch-up tối đa 60 ms, worldDt và chờ hit. Vân lặp frame=time×24+from.x, không chạy từ frame 0 mỗi đạn.'),clip('flame-trail','T',0,1000*(12+8)/60,'fx.ts:1411–1418,2114,2087–2100; ribbon đọc pool trực tiếp, frame=floor(time×12)%16; 200 ms bay danh định + 8/60 s đuôi=333 ms, không phải độ dài atlas 1333 ms. Chuyển động âm bám đường bay, không thêm cú nổ khi nối vòng.'),clip('impact-burst','I',0,50,'fx.ts:1223–1224: clip pha I theo bảng nguồn được tái dùng làm lóe R ngay tại miệng, không phải mục tiêu; frame=0, until=4, rate=6,5, life=3/60 s. Bắt lửa trùng khung đầu trong 17 ms.')]
for id in ['fire.impact.a','fire.impact.b','fire.impact.c','impact.multi']:
    clips[id]=impact_clips(False)
    if id in ['fire.impact.c','impact.multi']:clips[id]+=impact_clips(True)[:6]
    if id=='impact.multi':
        for c in clips[id]:c['syncNote']+=' Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit.'
clips['dragon.skyfire.cast']=[clip('charge-orb','A',0,200,'skyfire.ts:346–349; ONE_FRAME vẽ lại frame=time×24; A f0–f11, dài 200 ms trong cửa sổ sim 800 ms. Gầm gồng bắt đầu ở cast, không dời tick.'),clip('fireball-head','T',200,600,'skyfire.ts:39–42,485–492; ONE_FRAME vẽ lại frame=time×24, R tại f12=200 ms, I tại f48=800 ms. Tiếng bắt lửa phải trùng R trong 17 ms. R dùng cone/flare mã ở :427–433; không gọi muzzle-flash.'),clip('flame-trail','T',200,733,'skyfire.ts:477 và fx.ts:1411–1418; frame=floor(time×12)%16; T=600 ms, tail=8/60 s sau I (:675–679), tổng 733 ms. Âm cast 900 ms chồng 100 ms với âm impact ở 800 ms; đuôi ribbon kết thúc khoảng 933 ms.')]
sky=[]
for id in ['impact-big','fire-burst','impact-burst']:
    first,last,rate=(16,23,1) if id=='impact-big' else (9,23,1.6)
    fps=clipmeta.get(id,{}).get('fps',24);ms=(last+1-first)/(fps*rate)*1000
    n=f'Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame={first}, until={last}, rate={rate}, fps={fps}. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này.'
    if id=='fire-burst':n+=' Metadata dự phòng chưa có, ms dự toán theo 24 fps; tính lại khi nạp.'
    sky+=[clip(id,'I',0,ms,n),clip(id,'I',1000*2/60,ms/1.2,n+' Khối phụ thứ nhất, rate ×1,2.'),clip(id,'I',1000*4/60,ms/1.2,n+' Khối phụ thứ hai, rate ×1,2.')]
sky += [clip('embers','I',1000*2/60,30/(12*2.4)*1000,'skyfire.ts:565–566; frames=30, start=0, fps=12, rate=2,4, không life riêng → 1042 ms. Đá/than bắt đầu f2, đuôi rơi nằm trong 1800 ms âm.')]
for start in [22,28]:sky.append(clip('smoke-column','F',start/60*1000,2300,'skyfire.ts:625–630; life=2,3 s, rate=1,7, fps=8; pha F suy từ vai trò khói trong mã vì tools/vfx-flipbook/dragon-hold.json chưa khai báo smoke-column. Âm tắt ở 1800 ms dù hình khói còn; không kéo file dài ra.'))
sky.append(clip('smoke-mask','F',26/60*1000,1300,'skyfire.ts:632; khi có smoke-column, billow giữa: life=1,3 s, rate=2,2, fps=8. Đuôi nổ thấp lùi cùng khói.'))
for id in ['smoke-mask','smoke-roll']:
    for start in [26,30,34]:sky.append(clip(id,'F',start/60*1000,1150,'skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói.'))
sky.append(clip('ground-fire','F',100,3200,'skyfire.ts:648–661; chỉ điểm khô, trễ ngẫu nhiên 6–14/60 s (100–233 ms), life ngẫu nhiên 2000–3200 ms; lengthMs ghi cực đại; frame ngẫu nhiên 0–30, fps=24, loop=true. Đuôi lách tách trong âm 1800 ms; hình cháy lâu hơn âm, không tự thêm loop âm.'))
clips['dragon.skyfire.impact']=sky

rows=[]
for id in list(catalog)+list(own):
    if id in ['type.key','enemy.quadruped.howl']:continue
    x=own.get(id);base=x['fallback'] if x else id;c=catalog[base];sp=specs[base]
    loop=c['loop']; shape='loop' if loop else 'single' if c['lengthMs']>1200 else 'hits'
    pri='P0' if id in fire or id=='kill.chime' or (id.startswith('enemy.') and id.endswith(('.attack','.hit','.death'))) else 'P2' if group(id) in [groups[6],groups[7]] else 'P1'
    prompt=special.get(id,sp['prompt'].rstrip('.'))
    if x:
        creature={'moss-grunt':'small moss goblin in bark armour','moss-archer':'small moss archer with a thorn bow','tusk-boar':'heavy tusked boar','blight-wolf':'lean blighted wolf','thorn-wasp':'large thorn wasp','thorn-ant':'cluster of tiny thorn ants','moss-banner':'large moss captain carrying a wooden war banner'}[x['foe']]
        action={'spawn':'arriving with a short creature call and moving foliage','move':'moving steadily over forest ground','attack':'drawing back and delivering a forceful strike','hit':'recoiling at contact with a short pain call and rustling body','death':'giving a last cry, collapsing and scattering natural fragments'}[x['slot']]
        if x['slot']=='move' and x['foe']=='thorn-wasp':action='flying steadily with a textured wing buzz'
        if x['slot']=='attack' and x['foe']=='moss-archer':action='drawing a creaking bow, releasing the string and sending a thorn arrow through the air'
        if x['slot']=='attack' and x['foe']=='tusk-boar':action='driving its hooves forward into a weighty tusk charge, scattering dirt'
        if x['slot']=='attack' and x['foe']=='blight-wolf':action='lunging with a breath into a strong jaw snap and a short snarl'
        if x['slot']=='attack' and x['foe']=='thorn-wasp':action='tensing its wings, rushing forward and striking with its stinger'
        if x['slot']=='attack' and x['foe']=='thorn-ant':action='skittering forward and biting with many small sharp mandibles'
        if x['slot']=='move':prompt=f'A {creature} {action}, natural layered movement texture with steady density, {c["lengthMs"]} ms, seamless continuous loop in a pine mountain pass.'
        else:prompt=f'A {creature} {action}, clear attack and textured natural body, brief low pine-valley echo, {c["lengthMs"]} ms. Material and movement character: '+sp['prompt'].rstrip('.')+'.'
    if loop:
        if not prompt.endswith('.'):prompt+='.'
        if 'seamless' not in prompt.lower():prompt+=' Seamless continuous loop with steady density.'
    elif shape=='hits':prompt='An edited Foley sequence of isolated takes: '+prompt.rstrip('.')+'. One second of silence follows each complete take.'
    else:prompt='One complete isolated sound event: '+prompt.rstrip('.')+'.'
    when=sp['when']
    for old,new in {'Bình Máu Nhỏ':'Small Potion','Vệ Binh Rêu':'Grove Warden','Nhà Thuốc Lá':'Herb Hut','Lều Thuốc Nam':'Herb Hut','Gai Chông':'Spikes','Bom Hạt Thông':'Pine Bomb','Lưới Phóng':'Net Launcher','Phun Lửa':'Fire Breath','Thiên Hỏa':'Sky Fire','Long Hống':'Dragon Roar','Long Nộ':'Rage','Viêm Đế':'Inferno','Thẻ Ôn':'Review Card','Học trước':'Learn Ahead','Từ Khẩn':'Urgent Word','Ong Gai':'Thorn Wasp','Kiến Gai':'Thorn Ant','Hoàn hảo':'Perfect','Hoàn Hảo':'Perfect','Chớp':'Flash','Ấn Phá':'Seal Break'}.items():
        when=when.replace(old,new)
    if id=='dragon.skyfire.impact':
        when='Sky Fire chạm đất. Mapper cũng nhận Inferno stage=impact, nhưng sim hiện chỉ emit stage=end ở finale; nhánh âm finale chưa nối.'
    basis=[f'main:games/dragon-hold/src/audio/catalog.ts:{c["line"]}; lengthMs={c["lengthMs"]}; bus={c["bus"]}; loop={str(loop).lower()}; id nguồn={base}.',f'{sp["path"]}: duration.min_ms={sp["min"]}; max_ms={sp["max"]}; variants.target={sp["variants"]}; playback.mode={sp["mode"]}; playback.channels={sp["channels"]}.', 'games/dragon-hold/src/content/data/stages.ts:18–31; L2-cau, carry và bốn heroSkills.']
    if id=='dragon.skyfire.impact':
        basis+=['main và dh-vfx:games/dragon-hold/src/sim/combat.ts:829–834: infernoFinale emit stage=end; map-events.ts nhánh skill chỉ phát skyfire.impact khi stage=impact. Đây là lệch hiện trạng cần làn ráp xử lý, phiếu 213 không sửa mã.']
    if x:
        when=f'{names[x["foe"]]} · '+{'spawn':'xuất hiện','move':'vòng chuyển động khi loài dẫn đầu lớp','attack':'ra đòn','hit':'trúng đòn chữ đầu cửa sổ 45 ms hoặc đòn Grove Warden','death':'chết, gộp cùng lớp mỗi khung'}[x['slot']]+'.'
        if x['acceptedOnly']:when+=' Chưa có điểm phát riêng; chỉ manifest nhận, sự kiện hiện dùng '+base+'.'
        basis+=x['sources']+refs('dh-vfx','src/audio/catalog.ts',['export function foeSfx','return { spawn:','export const FOE_SFX_IDS'])
        basis+=['Chưa có thẻ riêng hoặc lengthMs riêng cho id này. Kế thừa nguyên số thẻ và catalog của '+base+'; không phải số riêng đã được thiết kế.','dh-vfx:games/dragon-hold/src/audio/engine.ts:60–91,105–125; có file riêng thì thay âm lớp; thiếu file giữ lớp. Hit đòn chữ fileOnly=true: thiếu file thì im lớp giọng riêng, fire.impact vẫn phát. Move chỉ chọn lúc bed được tạo, không đổi loài giữa bed đang chạy.']
    else:basis+=direct[id]
    why=None if clips.get(id) else ('Fire Breath dùng emitter breath 700 ms tại dh-vfx:fx.ts:1702–1708; không gọi flipbook.' if id=='dragon.breath' else 'Inferno dùng emitter inferno trong 10000 ms tại dh-vfx:fx.ts:1785–1787; âm mở 2400 ms. Finale bomb tại :2725 dùng lớp mã, không gọi flipbook.' if id=='dragon.inferno' else 'Không có cặp clip Firefly cho sự kiện này trong phạm vi ghép lửa của phiếu 213.')
    voice='Diễn một lần theo thứ tự chuẩn bị ngắn → phát → thân → đuôi; giữ đúng cỡ sinh vật và không thêm thời gian chờ.'
    if id=='fire.cast':voice='Khè-bùng ngay 0 ms; gầm tới 200 ms; vút xa tới 350 ms; vang thấp tới 750 ms. Phần A đã nằm trong lúc gõ.'
    elif id=='dragon.skyfire.cast':voice='Hít-gồng 0–200 ms; KHÈ ở 200 ms; vút lên rồi lao xuống tới 800 ms; đuôi tới 900 ms. Âm chạm riêng bắt đầu ở 800 ms.'
    elif id=='dragon.skyfire.impact':voice='NỔ ngay 0 ms; thân lửa tới khoảng 670 ms, than/đá từ 33 ms; vang thấp tắt ở 1800 ms. Khi dùng cho Inferno, chỉ bắt nhịp finale emitter.'
    elif id in fire:voice=f'Nhấn đầu hành động ngay 0 ms; giữ thân có chất liệu rồi hạ đuôi vang trước {c["lengthMs"]} ms; theo các mốc clip bên dưới.'
    phase='charge' if id=='dragon.skyfire.cast' else 'release' if id in ['fire.cast','dragon.breath','dragon.inferno','dragon.roar'] else 'impact' if id in fire or id.endswith(('.hit','.attack','.trigger')) else 'aftermath' if id.endswith(('.death','.down')) else None
    row=dict(id=id,playerName=label(id),when=when,bus=c['bus'],vfxSync='; '.join(dict.fromkeys(q['syncNote'] for q in clips.get(id,[]))) or why,priority=pri,priorityWhy='Ưu tiên sản xuất của README 212: đòn chữ/trúng/chết và lửa P0, tín hiệu trận P1, thao tác và nền P2; khác mức ưu tiên runtime trong catalog.',prompt=prompt,voiceHint=voice,inbox=f'~/AudioLab/inbox/firefly/dragon-hold/{id}/',era='kept',eraNote='Giữ hành động và chất liệu của thẻ; diễn lại theo ải núi, thung lũng thông và Q6, dùng Adobe Firefly Generate Sound Effects.',specCard=None if x else sp['path'],phase=phase,shape=shape,targetMs=dict(min=sp['min'],max=sp['max']),variants=sp['variants'],hitsPerTake=1,takes=1,loop=loop,basis=basis,branchOnly='dh-vfx' if x else None,clips=clips.get(id,[]),clipsWhy=why)
    rows.append(row)
rows.sort(key=lambda r:(groups.index(group(r['id'])),fire.index(r['id']) if r['id'] in fire else 100, list(catalog).index(r['id']) if r['id'] in catalog else 1000+list(own).index(r['id'])))
ex=[dict(id='type.key',reason='Tiếng phím thuộc bộ Firefly 189–192; charge-orb lúc gõ đi cùng type.key, không tạo âm mới ở 213.',firstStage='L2-cau',basis=direct['type.key']),dict(id='enemy.quadruped.howl',reason='Catalog dành sẵn; mapper không gọi id này, kể cả khi nội dung Blight Wolf có pack-howl.',firstStage=None,basis=['games/dragon-hold/src/audio/catalog.ts:115','games/dragon-hold/src/audio/map-events.ts:198–343; move/status/grade bỏ qua, skill chỉ định tuyến hero.'])]
for id in ['music.forest','music.wave','music.surge','music.general']:
    ex.append(dict(id=id,reason='Nhạc và mọi lớp cùng tên trong music.ts đi theo AUDIO_PIPELINE §8.1: VSCO-2-CE/VCSL, không tạo SFX Firefly.',firstStage='L2-cau',basis=['games/dragon-hold/src/audio/music.ts:17,174','docs/games/AUDIO_PIPELINE.md:606']))
unregistered=['enemy.'+foe+'.skill' for foe in ['moss-archer','blight-wolf','tusk-boar','thorn-wasp']]+['general.moss-banner.skill','trap.place','trap.spikes.stab','trap.pine-bomb.blast','trap.net.shoot','trap.net.wrap','house.place','house.down','unit.place','unit.warden.hit','unit.down','item.potion.drink','buy.heart','buy.scale']
for id in unregistered:
    ex.append(dict(id=id,reason='Nhãn show.sounds của content không thuộc catalog hoặc FOE_SFX_IDS; mapper dùng id đã ánh xạ, không phát nhãn này.',firstStage=None,basis=['games/dragon-hold/src/content/data/enemies.ts:32–37,99,131,162,194' if id.startswith('enemy.') else 'games/dragon-hold/src/content/data/generals.ts:44' if id.startswith('general.') else 'games/dragon-hold/src/content/data/our-side.ts:60–215']))
assumptions=dict(fileSeconds=12,silenceMs=1000,maxHitsPerTake=8,usableFraction=.75,p0ReserveTakes=1,note='Theo README 212: 12 s/file quan sát ở lô phím, tỷ lệ dùng được 75% chưa đo, một lượt là một file kết quả dự kiến; không suy ra credit hay thao tác. Không đổi độ dài và số biến thể của thẻ. Id riêng chưa có thẻ dùng nguyên số của thẻ lớp được ghi trong basis.')
commits=json.loads((OUT/'fired-ids.json').read_text())['sourceCommits']
data=dict(game='dragon-hold',stage='L2-cau',direction='Dragonhold: ải núi hùng vĩ, sông xiết và cầu đá cũ, rừng thông, vách hoa cương, rồng trưởng thành; chất lửa thật, gầm 60–250 Hz, vang thung lũng thấp theo AUDIO_PIPELINE §8.1, Q6 và ART_DIRECTION §3.',assumptions=assumptions,sourceCommits=commits,rows=rows,excluded=ex,retired=[],totals=dict(rows=len(rows),takes=0,byPriority=dict(P0=0,P1=0,P2=0)))
save(DEST/'dragon-hold.json',data)
save(OUT/'groups.json',{g:[r['id'] for r in rows if group(r['id'])==g] for g in groups})
save(OUT/'source-evidence.json',dict(sourceCommits=commits,catalog=catalog,own=own,metadata=dict(path='games/dragon-hold/public/assets/dragon-hold/vfx/firefly/manifest.json',sha256=hashlib.sha256((OUT/'clip-metadata.json').read_bytes()).hexdigest(),note='Metadata media hiện có ở checkout chính, ngoài Git; không thuộc commit, sao chụp để tái tính fps. fire-burst chưa có metadata; smoke-column chưa có trong cấu hình công cụ.'),unregistered=unregistered))
print(f'Dựng {len(rows)} hàng; bước tiếp: node docs/codex-queue/213/render.mjs để tính lượt bằng hàm 212 và chép Markdown.')
