from pathlib import Path
import re,json,hashlib
out=Path('docs/codex-queue/225')
doc=Path('docs/games/ART_DIRECTION_2026-10-28.md').read_text()
specific={
'dragon-hold':[
'A long, straight, perfectly level slider groove for a volume control, shown flat and straight on: a recessed channel of dark forged iron with a faint warm sheen, bordered along both long edges by a thin bright line of hammered warm gold, made to sit on a dark weathered bark-brown panel. The channel is a medium-dark iron tone, clearly lighter than near-black. Short rounded forged-iron end caps, each no longer than 5 percent of the groove length, with one tiny gold stud. The long middle is plain and continuous, with quiet even texture and the same brightness from end to end, so it can be stretched sideways. No fill level, no tick marks, no notches, no knob, no symbols. The groove is about 1400 pixels long and 88 pixels high, centred on a 1536 x 1024 canvas.',
"A round slider knob, shown flat and straight on: a slightly domed disc of hammered warm gold set in a ring of dark forged iron, a small glowing ember-orange enamel centre, fine dragon-scale texture only on the iron ring. Much brighter than the dark iron groove it slides on. A bold, simple round silhouette that still reads as a knob at 22 pixels. The face carries no symbol. Square 1024 x 1024; the knob's diameter is 70 percent of the canvas, exactly centred."],
 'typing-defense':[
'A long, straight, perfectly level slider groove for a volume control, shown flat and straight on: a recessed channel of polished dark jade lacquer, bordered along both long edges by a thin gold-leaf rim, with small bronze cloud-scroll end caps, each no longer than 5 percent of the groove length. The jade channel is a medium-dark tone, clearly lighter than near-black, with quiet lacquer depth. The long middle is plain and continuous, with the same brightness from end to end, so it can be stretched sideways. No fill level, no tick marks, no notches, no knob, no symbols. The groove is about 1400 pixels long and 88 pixels high, centred on a 1536 x 1024 canvas.',
"A round slider knob, shown flat and straight on: a polished pale limestone and gold-leaf disc in a fine bronze bezel, a small dark jade cabochon at the centre, a faint Dong Son sun-star ring engraved on the rim only. Much brighter than the dark jade groove it slides on. A bold, simple round silhouette that still reads as a knob at 22 pixels. The face carries no symbol. Square 1024 x 1024; the knob's diameter is 70 percent of the canvas, exactly centred."],
 'typing-survival':[
'A long, straight, perfectly level slider groove for a volume control, shown flat and straight on: a recessed channel of dark smoked glass over graphite steel, a fine white-gold filigree line along both long edges, and one thin, faint electric-cyan glow line running the full length inside the glass. Short clipped graphite end caps, each no longer than 5 percent of the groove length. The glass reads medium-dark, clearly lighter than near-black. The long middle is plain and continuous, with the same brightness from end to end, so it can be stretched sideways. No fill level, no tick marks, no notches, no glyphs, no knob. The groove is about 1400 pixels long and 88 pixels high, centred on a 1536 x 1024 canvas.',
"A round slider knob, shown flat and straight on: a machined disc of ivory-white ceramic and white-gold, a small smoked-glass lens at the centre, one thin electric-cyan light seam around the lens. Much brighter than the smoked-glass groove it slides on. A bold, simple round silhouette that still reads as a knob at 22 pixels. The face carries no symbol or glyph. Square 1024 x 1024; the knob's diameter is 70 percent of the canvas, exactly centred."]}
sources={'dragon-hold':'ui/parts/keycap.prompt.txt','typing-defense':'ui/parts/card-plate.try1.prompt.txt','typing-survival':'ui/parts/keycap.try1.prompt.txt'}
third={'dragon-hold':'ui/parts/keycap.png','typing-defense':'ui/frames-epic/crest.png','typing-survival':'concepts/b-lightbearer-keyart.png'}
all=[]
for g,parts in specific.items():
 art=Path(f'games/{g}/art-src'); blocks=(art/sources[g]).read_text().strip().split('\n\n'); style=blocks[0];part=blocks[1];bg=blocks[-1]
 assert style in doc
 files=sorted(x for x in (art/'ui/quick-settings').rglob('*') if x.is_file())
 baseline=''.join(hashlib.md5(f.read_bytes()).hexdigest()+' '+str(f)+'\n' for f in files)
 target=out/f'md5-before-{g}.txt'
 if not target.exists():target.write_text(baseline)
 print(g,'KA1',len(files),'files')
 for i,name in enumerate(['slider-track','slider-thumb']):
  pa=part;back=bg
  if i==0:
   pa=pa.replace('The object occupies 70 percent of the canvas long edge with balanced empty margins. ','').replace('The visible object occupies 70% of the longest canvas dimension and is exactly centred. ','')
   if g=='typing-survival':
    back=re.sub(r'Exactly one centered object.*?Empty transparent margins on every side\.', 'Exactly one object, the groove, centred on a 1536 x 1024 canvas, empty transparent margins on every side.',back)
  prompt='\n\n'.join([style,pa,parts[i],'Reference images: match the material finish of this game; reference content is not part of the requested object.',back])
  refs=[str(art/x) for x in ['ui/quick-settings/selected/hud-settings.png','ui/quick-settings/selected/vol-master.png',third[g]]]
  if i:refs.append(str(art/'ui/quick-settings/sliders/slider-track.png'))
  all.append(dict(game=g,name=name,tryNumber=1,status='planned',size='1536x1024' if i==0 else '1024x1024',transparent_background=g=='typing-survival',references=refs,prompt=prompt,changes='Lượt đầu; ghép nguyên văn theo phiếu. Rãnh bỏ câu chiếm 70%; Last Line rãnh đổi câu bố cục nền theo phiếu.' if i==0 else 'Lượt đầu; ghép nguyên văn theo phiếu.'))
(out/'prompts.json').write_text(json.dumps(all,ensure_ascii=False,indent=2)+'\n')
print(all[0]['prompt'])
