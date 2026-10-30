from pathlib import Path
import json
P=Path(__file__).resolve().parent; R=P.parents[2]; G='games/typing-survival/src/'
data=json.loads((R/'docs/games/audio/firefly/typing-survival.json').read_text()); allrows={x['id']:x for k in ['rows','excluded','retired'] for x in data[k]}
calls={
'key.ok':'view/typing-feel.ts:120; audio/theme-audio.ts:222', 'key.bad':'view/typing-feel.ts:129; audio/theme-audio.ts:228',
'word.load':'view/typing-feel.ts:140–146; audio/theme-audio.ts:234–238', 'word.perfect':'view/typing-feel.ts:140–146; audio/theme-audio.ts:234–238', 'word.full':'view/typing-feel.ts:140–146; audio/type-audio.ts:72–77', 'streak.up':'view/typing-feel.ts:160–162; audio/type-audio.ts:81–86',
'gun.xung':'view/shots.ts:178; audio/theme-audio.ts:248–250', 'gun.xung.tail':'view/shots.ts:181,431; audio/theme-audio.ts:254–256',
'gun.tia.start':'view/combat.ts:261–266; audio/theme-audio.ts:260–267', 'gun.tia.end':'view/combat.ts:269–271; audio/theme-audio.ts:270–271', 'gun.tia.loop':'view/beams.ts:172–184; audio/theme-audio.ts:206–214', 'gun.tia.pulse':'view/combat.ts:193,294; audio/theme-audio.ts:275–280',
'gun.tan.fire':'view/gunfx.ts:71–72', 'gun.ray.armed':'view/beams.ts:163–165; audio/gun-audio.ts:76', 'gun.ray.charge':'view/gunfx.ts:73–74', 'gun.ray.fire':'view/gunfx.ts:75–76', 'gun.phao.launch':'view/gunfx.ts:77–78', 'gun.phao.burst':'view/gunfx.ts:79–82; view/combat.ts:197–198',
'hit.t1':'view/combat.ts:185–198; audio/theme-audio.ts:294–303', 'hit.t2':'view/combat.ts:185–198; audio/theme-audio.ts:294–303', 'hit.t4':'view/combat.ts:186,198; audio/theme-audio.ts:298; kit/feedback/tiers.ts:38–39', 'hit.armour':'view/combat.ts:185–190; audio/theme-audio.ts:82',
'kill.swarm':'view/combat.ts:351–366; audio/theme-audio.ts:319', 'kill.elite':'view/combat.ts:351–366; audio/theme-audio.ts:319', 'foe.shot':'view/combat.ts:233–235; audio/theme-audio.ts:336', 'foe.shot.down':'view/combat.ts:237–240; audio/theme-audio.ts:344',
'hurt.hull':'view/combat.ts:223–228; audio/theme-audio.ts:352–365', 'hurt.breach':'view/combat.ts:213–218; audio/theme-audio.ts:352–360', 'hurt.drain':'view/combat.ts:245–250; audio/theme-audio.ts:372–378', 'support.repair':'view/combat.ts:253–258; sim/pace.ts:229–233',
'alarm.surge':'app/main.ts:649; audio/theme-audio.ts:392–399', 'end.win':'view/combat.ts:283–285; audio/theme-audio.ts:403–409', 'end.lose':'view/combat.ts:283–285; audio/theme-audio.ts:403–415',
'ui.move':'app/main.ts:393,472,502; app/journey.ts:222,235', 'ui.select':'app/main.ts:416,579; app/journey.ts:205,261', 'ui.back':'app/main.ts:398,483; app/journey.ts:200,267', 'star.get':'app/main.ts:182–186', 'music.calm':'audio/theme-audio.ts:131–151', 'music.surge':'app/main.ts:651; audio/theme-audio.ts:434–443',
'leader.horn':'view/gunfx.ts:90–91', 'leader.down':'view/gunfx.ts:92–96', 'rift.warn':'view/gunfx.ts:101–104', 'rift.open':'view/gunfx.ts:105–107', 'shield.hit':'view/gunfx.ts:83–84', 'shield.break':'view/gunfx.ts:85–87', 'foe.split':'view/gunfx.ts:88–89; sim/projectiles.ts:51',
'hit.sub':'audio/theme-audio.ts:294–303', 'hit.tail':'audio/theme-audio.ts:294–307', 'kill.chime':'audio/theme-audio.ts:315–328', 'gun.xung.loop':'audio/gun-audio.ts:37; view/shots.ts:178–181,431'
}
base='content/chapter-1.ts:39–53'
conditions={}
for id in calls:
 cond='Trong ải; '+base
 if id.startswith('gun.') and id!='gun.xung.loop': cond='Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; '+base
 if id.startswith('word.') or id in ['key.ok','key.bad','streak.up']: cond='Gõ trong bất kỳ bến súng nào; '+base
 if id=='word.full':cond='Từ vẫn hoàn tất khi bến đã đầy: view/typing-feel.ts:140–146; '+base
 if id in ['hit.t1','hit.t2']:cond='Đòn thường/crit/perfect có T1–T3; '+base
 if id=='hit.armour':cond='Brute Armor 4 từ 80 s; content/foes.ts:46; content/chapter-1.ts:49; affix giáp còn có ở sim/pace.ts:244–250'
 if id=='kill.swarm':cond='Swarm và Brute không mang cờ Scout; content/foes.ts:44,46; '+base
 if id=='kill.elite':cond='Cụm có Scout từ 12 s, không lấy kích cỡ làm cờ; content/chapter-1.ts:48; view/combat.ts:337,351,366'
 if id in ['foe.shot','foe.shot.down','hurt.hull']:cond='Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5'
 if id in ['hurt.drain','hurt.breach','end.lose']:cond='Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145'
 if id=='support.repair':cond='Director bật và chọn support khi nguy; content/chapter-1.ts:52; content/stage-rules.ts:103; sim/pace.ts:97–98,229–233'
 if id=='alarm.surge':cond='Hai surge gốc 50/115 s; content/chapter-1.ts:47; pace có thể dời, sim/pace.ts:223–225'
 if id=='end.win':cond='Giữ đủ 150 s; content/chapter-1.ts:42'
 if id=='star.get':cond='Ải khác s0 và stars.some(Boolean); app/main.ts:182–186; content/chapter-1.ts:39–42'
 if id.startswith('ui.'):cond='Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416'
 if id=='leader.horn' or id=='leader.down':cond='Ngoài ải; đầu tiên c1-s2, objective hunt; content/chapter-1.ts:57–60; c1-s1 chỉ hold, :42'
 if id.startswith('rift.'):cond='Ngoài ải; đầu tiên c1-s3; content/chapter-1.ts:74–78; c1-s1 hazard null, :43'
 if id.startswith('shield.'):cond='Ngoài ải; đầu tiên c1-s4; content/chapter-1.ts:91–101; c1-s1 chỉ brute, :49'
 if id=='foe.split':cond='Ngoài ải; chưa có ải đầu tiên trong mã; content/chapter-1.ts:36–107 và content/stage-s0.ts:67 không có splitter pack; sim/spawn.ts:180–184 bỏ loại thiếu cấu hình'
 if id=='hit.t4':cond='Ngoài mọi ải hiện tại: chỉ một nơi gọi audio.hit, view/combat.ts:186,198, t tối đa 3; tail cần T4, kit/feedback/tiers.ts:38–39; quái lớn chết không gọi audio.hit'
 if id in ['music.calm','music.surge']:cond='Có thể phát trong/ngoài trận nhưng loại khỏi SFX; app/main.ts:651; '+base
 if id in ['hit.sub','hit.tail','kill.chime']:cond='Lớp dự kiến tách file, chưa có id riêng trong SOUND_IDS. AUDIO_PIPELINE §6.3 mục 3 / §8.3; '+('T4 chưa đạt trong ải.' if id=='hit.tail' else 'Sự kiện nền tảng có trong ải.')
 if id=='gun.xung.loop':cond='Không còn sự kiện loop cơ khí riêng; per-shot và tail thay thế trong hướng B.'
 conditions[id]=cond
out={id:dict(calls='; '.join(G+s.strip() for s in calls[id].split(';')),condition=conditions[id]) for id in calls}
(P/'source-evidence.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
