import fs from 'node:fs';
import {im,D,json} from './lib.mjs';
const records=JSON.parse(fs.readFileSync(`${D}/processed.json`)),font='/System/Library/Fonts/Supplemental/Arial.ttf',commands=[];
const panels={'dragon-hold':'ui/frames/panel-large.png','typing-defense':'ui/frames-epic/panel-large.v2.png','typing-survival':'ui/frames-epic/panel-large.png'};
const titles={'dragon-hold':'Dragonhold','typing-defense':'Wordwoven','typing-survival':'Last Line'};
const label={'vol-master':'Master','vol-music':'Music','vol-effects':'Effects','vol-keyboard':'Keyboard sound','vol-keyboard-volume':'Keyboard volume','vol-voice':'Voice','vol-interface':'Interface','hud-settings':'Settings'};
const img=(p,w,h=w)=>['(',p,'-filter','Lanczos','-resize',`${w}x${h}!`,')'];
const crop=(g,w,h)=>{const a=['(','-size',`${w}x${h}`,'xc:none'];for(let x=0;x<w;x+=500){const ww=Math.min(500,w-x);a.push('(',`games/${g}/art-src/${panels[g]}`,'-crop',`${ww}x${h}+200+200`,'+repage',')','-geometry',`+${x}+0`,'-composite');}a.push(')');return a;};
const put=(a,x,y)=>[...a,'-geometry',`+${x}+${y}`,'-composite'];
const txt=(s,x,y,size=16)=>['-font',font,'-pointsize',String(size),'-fill','#f0e6cc','-annotate',`+${x}+${y}`,s];
function save(args,p){commands.push({file:p,args});fs.writeFileSync(p,im([...args,'-quality','94','jpg:-']));}
function get(g,n){return records.find(r=>r.game===g&&r.name===n)?.outputs[0].file||`games/${g}/art-src/ui/quick-settings/selected/${n}.png`;}
function iconPatch(g,n,size,labelled=true){const w=labelled?300:size+16,h=size+16,a=['-size',`${w}x${h}`,'xc:none',...put(crop(g,w,h),0,0),...put(img(get(g,n),size),8,8)];if(labelled)a.push(...txt(label[n],size+18,Math.round(size*.8)+8,Math.round(size*.6)));return im([...a,'png:-']);}
for(const g of ['dragon-hold','typing-defense']){
 const rs=records.filter(r=>r.game===g&&r.type==='icon');let a=['-size','1280x850','xc:#13161a',...txt(titles[g]+' · 244 · icons — 1x specimens',16,26,20)];
 for(let i=0;i<rs.length;i++){const r=rs[i],x=i*320,lo=r.name==='hud-settings'?28:24,hi=r.name==='hud-settings'?40:36;
 a.push(...put(img(r.outputs[0].file,256),x+30,40),...txt(r.name,x+12,315));
 for(const [s,y] of [[hi,345],[lo,420]]){const pp=iconPatch(g,r.name,s);const f=`games/${g}/art-src/_review/244/${r.name}.${s}.1x.png`;fs.writeFileSync(f,pp);a.push(...put(['(',f,')'],x+4,y),...txt(`${s===lo?'720p':'1080p'} · ${s}px · 1x`,x+12,y-8,13));}
 const pp=`games/${g}/art-src/_review/244/${r.name}.${lo}.1x.png`;
 a.push(...put(['(',pp,'-crop',`${lo+16}x${lo+16}+0+0`,'+repage','-filter','point','-resize','400%',')'],x+12,485),...txt('720p ×4 (point)',x+190,505,12));
 // So sánh cặp với master và các icon mới, cùng cỡ thật.
 a.push(...put(crop(g,304,48),x+8,680));const comp=[r.name,'vol-keyboard','vol-keyboard-volume','vol-master'];for(let k=0;k<comp.length;k++)a.push(...put(img(get(g,comp[k]),24),x+20+k*66,692));a.push(...txt('new / keyboard / volume / master',x+12,748,12));
 a.push(...put(crop(g,304,48),x+8,770));const old=`games/${g}/art-src/ui/quick-settings/selected/${r.name}.png`;if(fs.existsSync(old))a.push(...put(img(old,lo),x+22,778));a.push(...put(img(r.outputs[0].file,lo),x+120,778),...txt('old          new',x+12,840,12));
 }
 save(a,`games/${g}/art-src/_review/244-sheet.jpg`);
 // Đủ bảy hàng của bảng Sound, đúng 24 px / nhãn 14 px tại 720p.
 let s=['-size','950x530','xc:#13161a',...txt(titles[g]+' · Sound · 720p / 1080p, 1x',16,28,20)];
 const rows=['vol-master','vol-music','vol-effects','vol-keyboard','vol-keyboard-volume','vol-voice','vol-interface'];
 for(let i=0;i<rows.length;i++){const n=rows[i];for(const [size,x,y] of [[24,20,52+i*42],[36,430,52+i*60]]){const p=`games/${g}/art-src/_review/244/sound-${n}-${size}.png`;fs.writeFileSync(p,iconPatch(g,n,size));s.push(...put(['(',p,')'],x,y));}}
 save(s,`games/${g}/art-src/_review/244-sound-${g}.jpg`);
}
for(const r of records){const rev=`games/${r.game}/art-src/_review/244`,ratio=r.type==='slider'?'620x90':'360x360';let a=['-size',r.type==='slider'?'1280x200':'760x430','xc:#242322',...txt('Bản sinh',12,24),...txt('Bản hậu kỳ',r.type==='slider'?660:392,24)];
 const [bx,by,bw,bh]=r.bbox; a.push(...put(['(',r.src,'-crop',`${bw}x${bh}+${bx}+${by}`,'+repage','-filter','Lanczos','-resize',ratio,')'],10,50),...put(['(',r.outputs[0].file,'-trim','+repage','-filter','Lanczos','-resize',ratio,')'],r.type==='slider'?650:390,50));save(a,`${rev}/${r.name}-compare.jpg`);
}
for(const g of ['dragon-hold','typing-defense','typing-survival']){
 const fill=get(g,'slider-fill'),empty=records.find(r=>r.game===g&&r.name==='slider-empty')?.outputs[0].file||`games/${g}/art-src/ui/quick-settings/sliders/slider-track.png`,thumb=`games/${g}/art-src/ui/quick-settings/sliders/slider-thumb.png`;
 const strips=[];
 for(const [scale,w,h,ts] of [[1,210,10,22],[1.5,315,15,33]]){
 let a=['-size',`${scale===1?1000:1460}x90`,'xc:none',...put(crop(g,scale===1?1000:1460,90),0,0)]; // Tấm 1080 dùng lặp mảnh thật khi chiều rộng vượt ảnh nguồn.
 if(scale===1.5)a=['-size','1460x90','xc:#13161a',...put(crop(g,1000,90),0,0),...put(crop(g,460,90),1000,0)];
 for(let k=0;k<4;k++){const p=[0,.25,.5,1][k],x=20+k*(w+40),y=34,knob=ts/2+p*(w-ts),clip=p===0?0:p===1?w:Math.round(knob);
 a.push(...put(img(empty,w,h),x,y));if(clip)a.push(...put(['(',fill,'-filter','Lanczos','-resize',`${w}x${h}!`,'-crop',`${clip}x${h}+0+0`,'+repage',')'],x,y));a.push(...put(img(thumb,ts),Math.round(x+knob-ts/2),Math.round(y+h/2-ts/2)),...txt(`${Math.round(p*100)}%`,x,79,14));}
 const p=`games/${g}/art-src/_review/244/slider-${scale===1?'720':'1080'}-1x.png`;fs.writeFileSync(p,im([...a,'png:-']));strips.push(p);
 }
 let a=['-size','1500x650','xc:#13161a',...txt(titles[g]+' · slider · 0 / 25 / 50 / 100%',16,28,20),...txt('720p · rail 210×10, thumb box 22px · 1x',16,57),...put(['(',strips[0],')'],12,70),...txt('1080p · rail 315×15, thumb box 33px · 1x',16,187),...put(['(',strips[1],')'],12,200),...txt('720p ×4 (point)',16,320)];
 // Bản phóng đủ bốn mức: mỗi mức là một ô riêng, hai hàng để không thu nhỏ ảnh.
 for(let k=0;k<4;k++)a.push(...put(['(',strips[0],'-crop',`238x46+${8+k*250}+18`,'+repage','-filter','point','-resize','400%',')'],12+(k%2)*740,340+Math.floor(k/2)*200));
 // Tăng bề ngang để bốn ô x4 không đè nhau.
 a[1]='2000x770';for(let i=0;i<a.length;i++)if(typeof a[i]==='string'&&a[i].startsWith('+752+'))a[i]=a[i].replace('+752+','+1012+');
 save(a,`games/${g}/art-src/_review/244-slider-${g}.jpg`);
 let st=['-size','1500x270','xc:#13161a',...txt(titles[g]+' · stretch · 90–435 px, 1x',12,26,20)];let yy=60;for(const [w,h] of [[90,10],[210,10],[290,10],[135,15],[315,15],[435,15]]){st.push(...put(crop(g,600,24),20,yy-5),...put(img(fill,w,h),24,yy),...put(img(empty,w,h),700,yy),...txt(`${w}×${h}`,1250,yy+13,14));yy+=32;}save(st,`games/${g}/art-src/_review/244-slider-stretch-${g}.jpg`);
}

for(const g of ['dragon-hold','typing-defense']){
 let a=['-size','1280x280','xc:#13161a',...txt(titles[g]+' · vùng bảng sáng / tối thật · 720p 1x',16,26,20)];
 const rs=records.filter(r=>r.game===g&&r.type==='icon');
 for(let i=0;i<rs.length;i++){const r=rs[i],size=r.name==='hud-settings'?28:24,x=8+i*320;
  for(const [yy,py] of [[200,55],[700,140]]){a.push(...put(['(',`games/${g}/art-src/${panels[g]}`,'-crop',`304x56+200+${yy}`,'+repage',')'],x,py),...put(img(r.outputs[0].file,size),x+8,py+8),...txt(label[r.name],x+size+18,py+Math.round(size*.8)+8,Math.round(size*.6)),...txt('panel crop (200,'+yy+')',x+8,py+76,12));}
 }
 save(a,`games/${g}/art-src/_review/244-panel-contrast-${g}.jpg`);
}

json(`${D}/review-commands.json`,commands);console.log('Đã dựng tờ kiểm.');
