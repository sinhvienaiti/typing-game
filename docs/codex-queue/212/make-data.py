from pathlib import Path
import json,re,subprocess,math
ROOT=Path(__file__).resolve().parents[3]; OUT=ROOT/'docs/games/audio/firefly'; GAME=ROOT/'games/typing-survival'
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
specs={}
for p in (ROOT/'tools/audio-lab/specs/typing-survival').glob('*.yaml'):
 s=p.read_text(); d=re.search(r'^duration:\n(.*?)(?=^\S)',s,re.M|re.S).group(1); v=re.search(r'^variants:\n(.*?)(?=^\S)',s,re.M|re.S).group(1)
 specs[p.stem]=([None if x=='null' else int(x) for x in re.findall(r'(?:min_ms|max_ms): (\S+)',d)],int(re.search(r'target: (\d+)',v).group(1)))
# id | name | bus | phase | priority | when | sync | voice | English sound description
DATA='''word.load|—|alerts|release|P0|Gõ xong từ và nạp được vào súng.|Vòng ký hiệu đóng quanh súng canh, lóe nạp ngay EV.word.|Lướt lên rồi khóa chắc, ngân thấp.|a luminous glyph ring closing around a floating sentinel gun, a quick energy rise, a crisp loading lock and a compact resolving chord, a short bright attack, then a low ringing body below one kilohertz
word.perfect|—|alerts|release|P0|Từ đạt điều kiện perfect và nạp được.|Vòng vàng trắng khép, áo choàng lóe ở EV.word.|Khóa chắc rồi ngân sáng cao, gọn.|a perfected energy loading gesture, a swift charge rise and a crystalline locking strike, a short bright attack, then a low ringing body below one kilohertz and a delicate bell shimmer above four kilohertz
word.full|—|alerts|release|P0|Gõ xong từ khi bến súng đã đầy.|Viền bến sáng đều tại EV.word, không thêm đạn.|Chạm nhẹ rồi hạ giọng ngay.|a full energy chamber acknowledging a completed glyph ring, a brief bright glass contact followed by a compact low resonant answer below one kilohertz, restrained and dry
streak.up|—|alerts|—|P0|Chuỗi sạch đạt 3, 6, 10, 20 từ.|Số chuỗi nảy và ánh kính mũ tăng ở bậc mới.|Hai nốt liền, nốt sau cao hơn.|two delicate crystalline reward strikes sixty milliseconds apart, A5 then E6, each with a brief bright attack and a fine shimmer above four kilohertz, compact and restrained
 gun.xung|Pulse Gun|guns|release|P0|Mỗi viên Pulse Gun rời nòng.|Sao đầu nòng và viên lam xuất hiện cùng EV.shot.|Căng rất ngắn, bật giòn, thân nặng.|energy cannon shots from a floating sentinel gun, each with a brief loading catch, a bright crystalline crack, a dense plasma punch with weight, a short glassy shimmer settling into a low distant rumble
 gun.xung.tail|Pulse Gun|guns|aftermath|P0|Đầu loạt, mỗi 0,5 s còn bắn và 150 ms sau viên cuối.|Vệt sao chổi tàn, âm vang nối loạt; theo bộ hẹn hiện tại.|Rền thấp tan xa, vào mềm.|diffuse low reports of plasma cannon fire rolling across a vast graphite steel and ancient stone causeway, a gentle onset, a broad dark resonant body below nine hundred hertz and a soft distant decay
 gun.tia.start|Heat Beam|guns|release|P0|Heat Beam bắt đầu cháy.|Lóe mồi ở nòng tại EV.beamStart.|Vo ngắn lên, xé điện rồi ù.|a floating energy emitter igniting a sustained heat beam, a rapid power gathering whine, a forceful arc strike, dense plasma friction over a deep electrical hum, a short low echo
 gun.tia.loop|Heat Beam|guns|travel|P0|Suốt lúc Heat Beam cháy, chỉ khi game đang chạy.|Bám đoạn tia đang quét; dừng theo trạng thái beam.|Giữ ù đều một hơi.|a continuous steady plasma beam texture with a deep fifty five hertz electrical hum, dense low energy friction and fine electrical grains above five kilohertz, constant level and constant timbre throughout, seamless sustained material
 gun.tia.end|Heat Beam|guns|aftermath|P0|Heat Beam ngừng cháy.|Heat Beam tắt tại EV.beamEnd, còn vệt cháy sàn.|Vuốt thấp dần, tắt gọn.|an energy beam extinguishing, a descending electrical release, a contracting plasma body and a low resonant decay below one kilohertz across a wide ancient stone and graphite steel causeway
 gun.tia.pulse|Heat Beam|impacts|impact|P0|Một nhịp Heat Beam có quái trúng.|Lóe cắt trên quái, gom theo khung có tiaHits.|Xẹt rất ngắn, gọn.|tiny concentrated beam contacts biting into cracked black glass, a crisp electrical strike, a tightly compressed sizzling body and a fine high frequency decay above four kilohertz
 gun.tan.fire|Scatter Gun|guns|release|P0|Scatter Gun tung một loạt 7 viên.|Lóe nòng rộng và chùm đạn rời tại EV.volley.|Khóa ngắn rồi bật rộng có lực.|wide energy scatter blasts from a floating sentinel gun, a brief loading catch, a sharp crystalline release, a heavy spreading plasma body and sparkling fragments over a short low causeway echo
 gun.ray.armed|Rail Gun|guns|charge|P0|Rail Gun có băng chờ, chưa vào nhịp nạp.|Đạn sáng lơ lửng ở nòng; vòng điện giữ sẵn.|Ù nhỏ đều, hơi điện rất cao.|a small charged energy capacitor held ready, a quiet continuous hum below four hundred hertz and a faint electric glitter above five kilohertz, constant level and constant timbre throughout, seamless sustained material
 gun.ray.charge|Rail Gun|guns|charge|P0|Rail Gun bắt đầu nạp một phát, 0,15 s.|Vòng điện co về nòng tại EV.charge; không lùi tick bắn.|Rít lên dốc rồi dứt ở đỉnh.|a rail emitter gathering power for a shot, a tightly rising capacitor whine and concentrated electrical tension ending precisely at its peak, a compact preparation gesture
 gun.ray.fire|Rail Gun|guns|release|P0|Rail Gun bắn tia xuyên.|Đầu tia thẳng bật ở nòng tại EV.rail.|Bật đanh, thân nặng rồi ngân xa.|a powerful rail energy discharge from a floating sentinel gun, an extremely sharp crystalline crack, a dense low plasma body, electricity tearing above four kilohertz and a dark resonant tail below one kilohertz
 gun.phao.launch|Star Mortar|guns|release|P0|Star Mortar phóng một quả.|Cầu sáng rời nòng và bắt đầu cung bay tại EV.launch.|Khóa, phóng có lực, rít xa.|a heavy luminous mortar orb launching from a floating sentinel gun, a brief chamber lock, a forceful launch crack with a weighty resonant body, a high ion whistle receding through space and a short low causeway echo
 gun.phao.burst|Star Mortar|impacts|impact|P0|Quả Star Mortar nổ; tiếng riêng thay hit.* trong vùng.|Lóe nổ vùng tại EV.burst; các nổ liền leo nửa cung theo mã.|Nứt giòn rồi nổ nặng, mảnh rơi.|a heavy plasma orb detonating on graphite steel and ancient stone, a sharp crystalline rupture, a deep expansive blast with a dense energy body, black glass fragments scattering and a low rolling spatial decay
 hit.t1|—|impacts|impact|P0|Đòn bậc T1 trúng, gom khoảng 38 ms.|Lóe trúng nhẹ sau cửa sổ gom; không thêm thời gian chờ.|Keng kính gọn, thân nhỏ.|small energy projectiles striking cracked black glass, a bright crisp fracture, a compact solid glass body and a brief high shimmer above four kilohertz, tightly focused impact material
 hit.t2|—|impacts|impact|P0|Đòn bậc T2 hoặc T3 trúng, gom khoảng 38 ms.|Lóe crit hoặc perfect tại mục tiêu; mã giữ mức theo số trúng.|Nứt chắc, thân dày hơn bậc nhẹ.|medium energy impacts on thick cracked black glass, a hard bright fracture and a dense resonant glass body below one kilohertz, a compact high shimmer above four kilohertz, focused impact material
 hit.armour|Armor|impacts|impact|P0|Armor của quái chặn phần lớn đòn, gồm Brute.|Các tia lửa bật khỏi giáp tại EV.hit có FLAG.armour.|Keng chắc bật ra, gọn.|energy projectiles glancing off thick armor, a bright metallic strike with a solid plate body, sparks scattering above four kilohertz and a short low resonance across graphite steel
 hit.sub|—|impacts|impact|P0|Lớp dưới dùng chung từ T2, dành cho phiếu gắn sau.|Ghép đúng đầu trúng T2+ theo cờ bass, không phát riêng.|Hơi trầm nén rất gọn.|low frequency reinforcement layers for a heavy energy impact, a controlled pressure onset, a compact forty to ninety hertz body and a quick natural decay, isolated lower layer material for composite impacts
 hit.tail|—|impacts|aftermath|P0|Lớp đuôi dùng chung theo cờ tail, dành cho phiếu gắn sau.|Bắt theo tiếng trúng đủ bậc; hiện First Shift chỉ có T1–T3.|Ngân trầm lan xa, vào mềm.|low resonant aftermath layers spreading across graphite steel and ancient stone, a soft onset, a dark ringing body below one kilohertz and a spacious fading decay, isolated tail material for composite impacts
 kill.swarm|Swarm|kills|impact|P0|Quái không mang cờ Scout chết, có gom cụm; Brute cũng đi nhánh này.|Kính đen vỡ và nứt cam tắt ở EV.kill; Brute có VFX chết lớn riêng.|Rạn, vỡ vụn, mảnh lăn.|small void creatures of cracked black glass breaking apart, a compressed rupture, crunchy glass fragmentation, a compact low energy collapse and bright shards scattering across ancient stone with a short dark decay
 kill.elite|Scout|kills|impact|P0|Cụm chết có cờ Scout; không phải mọi quái lớn.|Scout vỡ tại EV.kill, mảnh kính và phóng điện.|Vỡ mạnh, điện xé, mảnh rơi.|a medium armored void creature of black glass collapsing, a tense crystalline fracture, a forceful energy rupture with a dense body, electrical discharge and falling glass fragments, a short low spatial decay
 kill.chime|—|kills|aftermath|P0|Lớp nốt của chuỗi hạ, hiện còn nhúng trong kill().|Nốt đi cùng cụm chết; mã đổi cao độ theo chuỗi dưới 1 s.|Một nốt rõ, ngân cao nhẹ.|crystalline reward notes struck at C5 as neutral pitch source material, a brief bright contact, a compact low ringing body and a delicate high shimmer above four kilohertz, consistent pitch across takes
 foe.shot|Scout|alerts|release|P1|Scout bắn cầu plasma về tuyến từ sau giây 12.|Lóe nòng Scout tại EV.foeShot, đạn bắt đầu bay.|Vo lên ngắn rồi xé lao tới.|small hostile plasma shots, a quick rising charge, a sharp energetic release and a rushing compact plasma body moving toward the listener, a short low spatial decay
 foe.shot.down|Scout|impacts|impact|P1|Pulse Gun bắn hạ đạn Scout giữa đường.|Đạn vỡ và tia lửa tại EV.shotDown.|Tách giòn, mảnh nhỏ tan.|small plasma projectiles intercepted in midair, a crisp crystalline fracture, a tiny compressed energy breakup, bright sparks and fine fragments dispersing into a short high decay
 hurt.hull|Armor|alerts|impact|P1|Đạn Scout chạm người chơi.|Giáp Lightbearer lóe khiên lam, áo choàng giật tại EV.playerHit.|Va chắc rồi ngân thấp.|a plasma projectile striking an armored caped guardian's blue energy shield, a sharp glasslike collision, a dense protective resonance, a brief electrical scatter and a low fading rumble
 hurt.breach|Armor|alerts|impact|P1|Quái vượt vạch cuối, làm mất Armor.|Vòng đỏ và giật người tại EV.breach.|Nổ có thân, hai nhịp báo ngắn.|a defensive line breached on an ancient stone and graphite steel causeway, a forceful pressure rupture, a deep resonant structural body and a brief two tone warning, a low rolling decay
 hurt.drain|Armor|alerts|impact|P1|Quái trong vùng gần hút Armor; tối đa một tiếng mỗi 420 ms.|Đốm sáng giáp và luồng hút tại EV.drain.|Rè điện nhỏ, bám rồi tắt.|small parasitic energy arcs draining an armored guardian's protective field, a crisp electrical attachment, a restrained low sizzling body and a fine high crackle fading above four kilohertz
 alarm.surge|—|alerts|—|P1|Đợt dồn bắt đầu, mốc gốc 50 và 115 s có thể được pace dời.|Khớp peak đổi sang dương khi đang play; hướng B quái vật xa ngẩng lên.|Hai lượt lên xuống, trầm và rộng.|a single urgent warning gesture at the edge of a distant black hole, two rising and falling resonant calls over a deep pressure drone, a broad ominous body and a low fading spatial tail
 end.win|—|alerts|—|P1|Giữ đủ 150 s và thắng.|EV.end thắng mở băng rôn trước thẻ kết quả 0,9 s.|Mở hợp âm chắc rồi thả nhẹ.|a single victorious science fiction resolution, a weighty A power chord opening into white gold crystalline overtones, a brief bright crest, a deep relieved body and a spacious low decay
 end.lose|—|alerts|—|P1|Armor cạn, tuyến thua.|EV.end thua mở băng rôn trước thẻ kết quả 0,9 s.|Hạ dần, rạn rồi chìm.|a single defeated energy field collapse, a descending power resonance, cracked black glass settling in several weighted contacts on ancient stone, a deep fading body and a dark spatial decay
 support.repair|Armor|alerts|—|P2|Pace chọn support khi gần thua và director bật.|Vòng xanh từ trên xuống, Armor tăng tại EV.support.|Nâng lên, khép êm, ngân nhẹ.|a restorative green energy ring descending around an armored guardian, a smooth gathering rise, a precise crystalline closure, a warm low resonant body and a soft high shimmer
 star.get|—|ui|—|P2|Kết ải có ít nhất một sao; hiện mã gọi một lần cho cả nhóm.|Khớp settle kết ải có stars.some(Boolean), không đợi từng sao bay.|Một ting sáng, ngân gọn.|a small crystalline reward star arriving, a precise bright contact, a delicate ringing body and a short airy shimmer above four kilohertz
 ui.move|—|ui|—|P2|Đổi mục hoặc giá trị cài đặt.|Nút đổi focus hoặc rê chuột, lóe lam.|Chạm kính rất gọn.|tiny smoked glass interface contacts, a dry precise crystalline tick with a tightly controlled brief resonance
 ui.select|—|ui|—|P2|Chọn mục, nút hoặc súng.|Nút lóe lam, bảng mở bằng đường sáng.|Chạm chắc rồi ù thấp.|smoked glass interface selections, a crisp glass contact, a compact low confirmation resonance and a fine white gold shimmer
 ui.back|—|ui|—|P2|Đóng bảng hoặc quay lại.|Bảng khép, đường sáng rút khi Esc hoặc back.|Chạm thấp hơn chọn, tắt nhẹ.|smoked glass interface closures, a lower gentle crystalline contact, a compact descending low resonance and a soft brief decay'''
rows=[]
for line in DATA.splitlines():
 id,name,bus,phase,pri,when,sync,voice,desc=[x.strip() for x in line.split('|')]
 shape='loop' if id in ['gun.tia.loop','gun.ray.armed'] else 'single' if id in ['alarm.surge','end.win','end.lose'] else 'hits'
 prompt=('An edited sequence of isolated '+desc+', each one followed by a second of silence.' if shape=='hits' else ('A continuous sound recording of '+desc+'.' if shape=='loop' else desc[0].upper()+desc[1:]+'.'))
 limits,n=specs.get(id,([None,None],1))
 basis=['Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6.']
 if id in specs: basis+=['Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/'+id+'.yaml (duration.min_ms/max_ms, variants.target).']
 fallback={'gun.tia.loop':([2000,2000],1),'gun.ray.armed':([2000,2000],1),'word.full':([100,100],1),'streak.up':([260,260],1),'hit.sub':([80,120],1),'hit.tail':([500,700],2),'kill.chime':([240,240],1)}
 if None in limits:
  limits,n=fallback[id]
  basis+=['Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly.']
 if id=='hit.sub': basis+=['Chưa có id phát trong mã. AUDIO_PIPELINE.md §6.3 mục 3, §8.3 ưu tiên hơn ghi chú cũ THEME_SOUND_LIST.md:31; theme-audio.ts:294–307 hiện ghép sub trong flush(), tone 160 ms; trần 120 ms lấy AUDIO_PIPELINE.md:632. Khoảng 80–120 ms là mục tiêu biên tập đề xuất.']
 if id=='hit.tail': basis+=['Chưa có id phát trong mã. AUDIO_PIPELINE.md §6.3 mục 3; THEME_SOUND_LIST.md:31 nói lớp đề xuất; theme-audio.ts:294–307 flush() có thân đuôi 500/700 ms từ T4. Giữ theo yêu cầu phiếu 212 dù c1-s1 hiện không đạt T4.']
 if id=='kill.chime': basis+=['Giữ vì sự kiện nốt hạ vẫn còn ở hướng B. THEME_SOUND_LIST.md §5, AUDIO_PIPELINE.md §6.4/§8.3 yêu cầu tách nốt; theme-audio.ts:315–328 hiện nốt nhúng 240 ms, chưa có id riêng. Mục tiêu biên tập 240 ms, biến thể 1 theo thẻ. Không nhúng nốt vào prompt kill.swarm/elite.']
 if id=='word.full': basis+=['THEME_SOUND_LIST.md:48,57 và type-audio.ts:72–77: 100 ms; biến thể mặc định 1 theo THEME_SOUND_LIST §2, không thuộc nhóm cần 4–6.']
 if id=='streak.up': basis+=['THEME_SOUND_LIST.md:49,58 và type-audio.ts:81–86: cú thứ hai ở 60 ms, ngân 200 ms, tổng 260 ms; biến thể mặc định 1 theo THEME_SOUND_LIST §2.']
 if shape=='loop': basis+=['THEME_SOUND_LIST.md §4/§9: prompt vòng 2 s; gun-audio.ts:74–76: nền duy trì, nhỏ hơn âm khởi đầu; biến thể 1 là mặc định biên tập theo THEME_SOUND_LIST §2.']
 if id=='gun.xung': basis+=['Thẻ còn ghi phát nửa số viên; mã shots.ts:178 và THEME_SOUND_LIST §4 đã phát mỗi viên. Giữ duration thẻ theo phiếu, ingest phải nghe thử lặp 10–11 viên/s.']
 era='kept' if id in ['gun.tia.loop','gun.tia.end','gun.tia.pulse','gun.ray.armed','gun.ray.charge','streak.up','star.get','alarm.surge','hit.sub'] else 'reworded'
 why='Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.' if era=='kept' else 'Cùng sự kiện mã; đổi chất liệu thép/trạm và cơ khí sang năng lượng, kính đen hoặc kính giao diện theo hướng B.'
 special={'hurt.hull':'Thân tàu bị đập đổi thành giáp Lightbearer lóe khiên lam và áo choàng giật.','support.repair':'Khoang sửa cập đổi thành vòng xanh từ trên xuống, vẫn tăng Armor.','word.load':'Băng đạn đóng đổi thành vòng ký hiệu khóa quanh súng canh.','kill.swarm':'Kim loại vỡ đổi thành kính đen vỡ; Brute vẫn dùng cùng nhánh âm hiện tại.','kill.elite':'Máy thép nổ đổi thành Scout kính đen tan cùng phóng điện.','kill.chime':'Thanh thép leo nốt đổi chất âm tinh thể; sự kiện nốt thưởng vẫn còn.'}
 special.update({
 'word.perfect':'Nạp băng kèm điện đổi thành vòng ký hiệu vàng trắng khóa và chuông cao, cùng điều kiện perfect.',
 'word.full':'Chốt băng đạn hụt đổi thành phản hồi vòng năng lượng đã đầy; vẫn không nhận thêm đạn.',
 'gun.xung':'Súng cơ khí thời tàu đổi thành Pulse Gun canh bay: đầu tinh thể, thân plasma, vẫn phát mỗi viên.',
 'gun.xung.tail':'Vang hành lang thép đổi thành dư âm plasma trên đường đắp thép than chì và đá cổ, giữ lịch gọi đuôi.',
 'gun.tia.start':'Máy phát công nghiệp bật đổi thành súng canh gom năng lượng rồi mồi plasma, giữ EV.beamStart.',
 'gun.tan.fire':'Khóa bơm và vỏ đạn cơ khí đổi thành nổ chùm plasma từ súng canh, giữ một âm mỗi volley.',
 'gun.ray.fire':'Nổ súng ray cơ khí đổi thành nhát xả năng lượng xuyên có đuôi ion, giữ EV.rail.',
 'gun.phao.launch':'Đạn trượt vào ống thép đổi thành quả sáng khóa năng lượng và phóng theo cung từ súng canh.',
 'gun.phao.burst':'Nổ mảnh trên sàn thép đổi thành quả plasma phá kính đen trên đường đắp đá cổ, giữ tiếng nổ vùng riêng.',
 'hit.t1':'Keng nhẹ trên vỏ thép đổi thành nứt kính đen nhỏ, vẫn là đầu và thân của bậc T1.',
 'hit.t2':'Keng trên thép dày đổi thành va chạm kính đen dày, vẫn là đầu và thân T2–T3 để ghép sub sau.',
 'hit.armour':'Đòn bị vỏ máy chặn đổi thành đạn năng lượng bật khỏi Armor; vai trò báo bị chặn giữ nguyên.',
 'hit.tail':'Đuôi kim loại trong hành lang đổi thành ngân thấp của thép than chì và đá cổ trên đường đắp rộng.',
 'foe.shot':'Cầu plasma của lính máy đổi bối cảnh thành phát bắn của Scout kính đen, giữ nạp ngắn và tiếng lao tới.',
 'foe.shot.down':'Đạn kim loại vỡ đổi thành cầu plasma bị chặn với tia lửa và mảnh tinh thể, giữ EV.shotDown.',
 'hurt.breach':'Thủng thân trạm đổi thành tuyến phòng thủ bị phá và mất Armor của nhân vật, giữ va chạm kèm báo động.',
 'hurt.drain':'Điện hút trên tấm thép đổi thành hồ quang hút trường bảo vệ quanh giáp nhân vật, vẫn giới hạn mỗi 420 ms.',
 'end.win':'Hợp âm máy kèm xả hơi đổi thành hợp âm năng lượng và âm bội tinh thể vàng trắng, cùng sự kiện thắng.',
 'end.lose':'Máy hạ điện và thép sụp đổi thành trường năng lượng tắt, kính đen lắng trên đá cổ, cùng sự kiện thua.',
 'ui.move':'Rơ-le chọn mục đổi thành chạm kính khói rất ngắn, giữ hành động đổi focus.',
 'ui.select':'Công tắc nặng đổi thành chạm kính khói và cộng hưởng xác nhận thấp, giữ hành động chọn.',
 'ui.back':'Công tắc hạ đổi thành kính khói khép và ngân thấp đi xuống, giữ hành động quay lại.'
 })
 rows.append(dict(id=id,playerName=None if name=='—' else name,when=when,bus=bus,phase=None if phase=='—' else phase,vfxSync=sync,priority=pri,priorityWhy={'P0':'Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.','P1':'Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.','P2':'UI, sao hoặc tiếp tế: nhóm phụ sau P0 và P1.'}[pri],shape=shape,prompt=prompt,targetMs=dict(zip(['min','max'],limits)),variants=n,hitsPerTake=0,takes=0,loop=shape=='loop',voiceHint=voice,inbox=f'~/AudioLab/inbox/firefly/typing-survival/{id}/',era=era,eraNote=special.get(id,why),specCard=f'tools/audio-lab/specs/typing-survival/{id}.yaml' if id in specs else None,basis=basis))
excluded=[]
def ex(id,reason,first,basis): excluded.append(dict(id=id,reason=reason,firstStage=first,basis=basis))
for id in ['key.ok','key.bad']: ex(id,'Tiếng phím do bộ Firefly 189–191 phụ trách, không làm trùng.', 's0',['typing-feel.ts:120–129; theme-audio.ts:222–230; chapter-1.ts:39–53.'])
for id in ['music.calm','music.surge']: ex(id,'Nhạc là stem 96 BPM La thứ theo AUDIO_PIPELINE §8.3, không phải SFX.', 's0',['theme-audio.ts:131–151,434–443; main.ts:651.'])
for id,line,stage,reason in [('leader.horn',91,'c1-s2','Cần Pack Leader, chỉ objective hunt đưa vào.'),('leader.down',96,'c1-s2','Cần tiến độ hunt tăng sau khi hạ Pack Leader.'),('rift.warn',104,'c1-s3','Cần telegraph Rift; First Shift hazard null.'),('rift.open',107,'c1-s3','Cần Rift mở; First Shift hazard null.'),('shield.hit',84,'c1-s4','Cần Shield Guard; First Shift chỉ có brute pack.'),('shield.break',86,'c1-s4','Cần Shield Guard; First Shift chỉ có brute pack.'),('foe.split',89,None,'Cần Splitter; chưa có ải nào trong CHAPTER_1 hoặc Trial khai báo splitter pack.'),('hit.t4',None,None,'Không đạt T4: combat.ts chỉ truyền T1–T3 vào audio.hit; chưa có ải đầu tiên phát được trong mã hiện tại.')]:
 ex(id,reason,stage,[f'gunfx.ts:{line}; chapter-1.ts:39–105; stage-s0.ts:52–70; spawn.ts:24–25,180–184.' if line else 'combat.ts:179–198; theme-audio.ts:294–306; src/kit/feedback/tiers.ts:34–39.'])
retired=[dict(id='gun.xung.loop',reason='Nền cơ khí liên thanh thời tàu không còn sự kiện âm riêng trong hướng B: Pulse Gun phát từng viên và có đuôi riêng, không có lệnh loop này.',basis=['gun-audio.ts:37,44–58; shots.ts:178–181,431; thẻ gun.xung.loop.yaml là đề xuất cũ.'])]
a=dict(fileSeconds=12,silenceMs=1000,maxHitsPerTake=8,usableFraction=0.75,p0ReserveTakes=1,note='12 s theo lô 189; 75% cú dùng được là giả định biên tập chưa đo, chỉnh sau lượt đầu. Số lượt là kế hoạch, không phải bảo đảm chất lượng hay credit.')
for r in rows:
 h=min(a['maxHitsPerTake'],math.floor(a['fileSeconds']*1000/(r['targetMs']['max']+a['silenceMs']))) if r['shape']=='hits' else 1
 r['hitsPerTake']=h;r['takes']=math.ceil(r['variants']/(h*a['usableFraction']))+(a['p0ReserveTakes'] if r['priority']=='P0' else 0)
listdata=dict(game='typing-survival',stage='c1-s1',direction='B · Lightbearer',sourceCommits={'main':subprocess.check_output(['git','-C',str(GAME),'rev-parse','HEAD'],text=True).strip()},assumptions=a,rows=rows,excluded=excluded,retired=retired,totals=dict(rows=len(rows),takes=sum(r['takes'] for r in rows),byPriority={p:sum(r['takes'] for r in rows if r['priority']==p) for p in ['P0','P1','P2']}))
evidence=json.loads((ROOT/'docs/codex-queue/212/source-evidence.json').read_text())
for r in [*rows,*excluded,*retired]:
 r['basis'] += [evidence[r['id']]['calls'],evidence[r['id']]['condition']]
dump(OUT/'typing-survival.json',listdata)
# Narrow JSON Schema subset, checked without dependencies by check.mjs.
S=lambda nullable=False: {'type':['string','null'] if nullable else 'string',**({} if nullable else {'minLength':1})}
I=lambda minimum=0:dict(type='integer',minimum=minimum)
def obj(props,required=None):return dict(type='object',properties=props,required=list(props) if required is None else required,additionalProperties=False)
def arr(items): return dict(type='array',items=items)
phase={'enum':['charge','release','travel','impact','aftermath',None]}
rowprops={k:S(k in ['playerName','voiceHint','specCard']) for k in ['id','playerName','when','bus','vfxSync','priorityWhy','prompt','voiceHint','inbox','eraNote','specCard']}
rowprops.update(phase=phase,priority={'enum':['P0','P1','P2']},shape={'enum':['hits','single','loop']},targetMs=obj({'min':I(1),'max':I(1)}),variants=I(1),hitsPerTake=I(1),takes=I(1),loop={'type':'boolean'},era={'enum':['kept','reworded']},basis=arr(S()))
required=list(rowprops)
rowprops.update(branchOnly=S(True),clips=arr(obj({'clip':S(),'phase':{'enum':['A','R','T','I','F']},'startMs':I(),'lengthMs':I(1),'syncNote':S()})),clipsWhy=S(True))
rowprops['hitsPerTake']['maximum']=8
props=dict(game=S(),stage=S(),direction=S(),assumptions=obj({'fileSeconds':dict(type='number',exclusiveMinimum=0),'silenceMs':I(),'maxHitsPerTake':I(1),'usableFraction':dict(type='number',exclusiveMinimum=0,maximum=1),'p0ReserveTakes':I(),'note':S()}),rows=arr(obj(rowprops,required)),excluded=arr(obj({'id':S(),'reason':S(),'firstStage':S(True),'basis':arr(S())})),retired=arr(obj({'id':S(),'reason':S(),'basis':arr(S())})),totals=obj({'rows':I(),'takes':I(),'byPriority':obj({p:I() for p in ['P0','P1','P2']})}))
props['assumptions']['properties']['maxHitsPerTake']['maximum']=8
req=list(props);props['sourceCommits']=dict(type='object',additionalProperties=dict(type='string',pattern='^[0-9a-f]{7,40}$'))
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','title':'Danh sách Adobe Firefly SFX dùng chung ba game',**obj(props,req)}
dump(OUT/'schema.json',schema)
md=['# Last Line · First Shift (`c1-s1`) · danh sách âm Firefly hướng B','',f"**{len(rows)} hàng · {listdata['totals']['takes']} lượt dự kiến** (P0 {listdata['totals']['byPriority']['P0']}, P1 {listdata['totals']['byPriority']['P1']}, P2 {listdata['totals']['byPriority']['P2']}). Công thức và giả định ở [README](README.md).",'', '150 s; không hiểm họa; Scout từ 12 s; Brute từ 80 s; hai đợt dồn gốc 50/115 s; chọn 2 trong 5 súng nên cả 5 được tính. Đây là danh sách sản xuất, chưa tạo hay nghe âm. `hit.sub`, `hit.tail`, `kill.chime` là lớp dành cho bước gắn sau; `hit.tail` chưa có tình huống T4 trong ải này.','', '| Id | Tên trong game | Ưu tiên | Lượt |','|---|---|---|---|']
for r in rows:md.append(f"| `{r['id']}` | {r['playerName'] or '—'} | {r['priority']} | {r['takes']} |")
for r in rows:
 md+=['',f"## `{r['id']}`",'',f"- Tên: {r['playerName'] or '—'}; ưu tiên **{r['priority']}**. {r['priorityWhy']}",f"- Khi nào: {r['when']}",f"- Pha: {r['phase'] or 'null (ngoài đòn)'}; khớp VFX: {r['vfxSync']}",f"- Độ dài phần cắt: {r['targetMs']['min']}–{r['targetMs']['max']} ms; dạng `{r['shape']}`; {r['variants']} biến thể; {r['hitsPerTake']} cú/lượt; **{r['takes']} lượt**.",f"- Thư mục nhận: `{r['inbox']}`",f"- Gợi ý diễn bằng giọng: {r['voiceHint']}",f"- Thời kỳ: `{r['era']}`. {r['eraNote']}",'','```text',r['prompt'],'```','','Căn cứ: '+' '.join(r['basis'])]
for title,key in [('Loại trừ','excluded'),('Id cũ dừng sản xuất','retired')]:
 md+=['',f'## {title}','','| Id | Lý do | Ải đầu tiên |','|---|---|---|']
 for x in listdata[key]:md.append(f"| `{x['id']}` | {x['reason']} | {x.get('firstStage') or 'Chưa có trong mã hiện tại'} |")
(OUT/'typing-survival.md').write_text('\n'.join(md)+'\n')
print(listdata['totals'])
