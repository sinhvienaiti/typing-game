// Tờ so sánh và tờ xem dựng từ ảnh thật, không sinh/vẽ lại nội dung tài sản.
import fs from 'node:fs';
import {execFileSync as run} from 'node:child_process';
const M='/opt/homebrew/bin/magick',font='/System/Library/Fonts/Supplemental/Arial.ttf';
const im=a=>run(M,a,{maxBuffer:100*1024*1024});
const onlyNew=p=>{if(fs.existsSync(p))throw Error('Giữ file có sẵn '+p);};
const selected=JSON.parse(fs.readFileSync('docs/codex-queue/225/selected.json'));
const commands=[];
const writeImage=(p,args)=>{if(!fs.existsSync(p))im([...args,p]);commands.push({output:p,args:[M,...args,p]});};
const writeText=(p,text)=>{if(!fs.existsSync(p))fs.writeFileSync(p,text,{flag:'wx'});};
const label=(text,x,y,size=16)=>['-font',font,'-pointsize',String(size),'-fill','#eeeeee','-gravity','NorthWest','-annotate',`+${x}+${y}`,text];
for(const item of selected){const g=item.game,n=item.name,track=n==='slider-track',tmp=`games/${g}/tmp/codex-225`,height=track?760:1120;
 const before=`${tmp}/${n}.before-panel.png`,after=`${tmp}/${n}.after-panel.png`;
 writeImage(before,[item.source,'-filter','Lanczos','-resize',track?'1024x683':'1024x1024','-background','#20242b','-alpha','remove','-gravity','center','-extent',`1080x${height}`,...label(`Bản sinh · ${g} · lượt ${item.tryNumber}`,24,18,22)]);
 writeImage(after,[item.selected,'-background','#20242b','-alpha','remove','-gravity','center','-extent',`1080x${height}`,...label(`Bản hậu kỳ · ${track?'1024 × 64':'1024 × 1024'}`,24,18,22)]);
 const dst=`games/${g}/art-src/_review/225-${n}-compare.jpg`;
 writeImage(dst,[before,after,'+append','-quality','94']);
 writeText(dst.replace('.jpg','.prompt.txt'),`Tờ so sánh hậu kỳ, không gọi sinh ảnh. Chạy từ gốc repo: node docs/codex-queue/225/review.mjs\nNguồn sinh: ${item.source}\nNguồn hậu kỳ: ${item.selected}\nHai ô có cùng khổ 1080 × ${height}; giữ nguyên tỉ lệ tranh ở mỗi ô.\n`);
}
const configs=[['dragon-hold','Dragonhold','#2b2118','#f1e3c4'],['typing-defense','Wordwoven','#061e16','#b8aa94'],['typing-survival','Last Line','#14181f','#8c96a3']];
function bar(g,scale,pos,bg,kit=false){const w=210*scale,h=10*scale,s=22*scale,W=w+30,H=Math.max(56,Math.ceil(s+20)),x=15,y=Math.floor((H-h)/2),kx=x+Math.round((w-s)*pos/100),ky=Math.round(y+h/2-s/2),tmp=`games/${g}/tmp/codex-225`,base=`games/${g}/art-src/ui/quick-settings/sliders`,tag=`${scale}-${pos}-${bg.slice(1)}-${kit?'kit':'clear'}`;
 const tr=`${tmp}/bar-track-${tag}.png`,th=`${tmp}/bar-thumb-${tag}.png`,dst=`${tmp}/bar-${tag}.png`;
 writeImage(tr,[`${base}/slider-track.png`,'-filter','Lanczos','-resize',`${w}x${h}!`]);
 writeImage(th,[`${base}/slider-thumb.png`,'-filter','Lanczos','-resize',`${s}x${s}!`]);
 const a=['-size',`${W}x${H}`,`xc:${bg}`];
 if(kit)a.push('(','-size',`${w}x${h}`,'xc:#4A505C',')','-geometry',`+${x}+${y}`,'-compose','Over','-composite');
 a.push(tr,'-geometry',`+${x}+${y}`,'-compose','Over','-composite');
 if(kit)a.push('(','-size',`${s}x${s}`,'xc:#F3F4F6',')','-geometry',`+${kx}+${ky}`,'-compose','Over','-composite');
 a.push(th,'-geometry',`+${kx}+${ky}`,'-compose','Over','-composite');
 writeImage(dst,a);return dst;
}
const rows=[];
for(const [g,title,dark,light] of configs){const tmp=`games/${g}/tmp/codex-225`,a=['-size','2810x350','xc:#15191f',...label(title,20,10,26)];
 const place=(p,x,y)=>a.push(p,'-geometry',`+${x}+${y}`,'-compose','Over','-composite');
 let x=20;
 for(const [scale,bg,name] of [[1,dark,'720p · tối'],[1,light,'720p · sáng'],[1.5,dark,'1080p · tối'],[1.5,light,'1080p · sáng']]){
  for(const [i,pos] of [0,50,100].entries()){place(bar(g,scale,pos,bg),x,55+i*78);a.push(...label(`${name} · ${pos}%`,x+12,112+i*78,14));}
  x+=scale===1?255:360;
 }
 const icon=`games/${g}/art-src/ui/quick-settings/selected/vol-master.png`;
 for(const [i,s] of [20,28].entries()){const p=`${tmp}/vol-master-${s}-sheet.png`;writeImage(p,[icon,'-filter','Lanczos','-resize',`${s}x${s}!`,'-background',dark,'-alpha','remove','-gravity','center','-extent','95x74']);place(p,x,55+i*105);a.push(...label(`vol-master ${s}px`,x,136+i*105,12));}
 x+=110;
 const hud=`${tmp}/owner-hud.png`;writeImage(hud,['games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp','-crop','369x234+1005+476','+repage','-filter','Lanczos','-resize','347x220!']);place(hud,x,55);a.push(...label('Mảnh HUD tham chiếu chủ dự án',x,282,14));x+=365;
 const mid=bar(g,1,50,dark),zoom=`${tmp}/bar-point3.png`;if(!fs.existsSync(zoom))writeImage(zoom,[mid,'-filter','point','-resize','300%']);place(zoom,x,65);a.push(...label('720p · 50% · phóng ×3 · point',x,242,16));x+=740;
 place(bar(g,1,50,dark,true),x,65);a.push(...label('kit hôm nay · 720p · 50%',x,130,16),...label('#4A505C dưới rãnh',x,160,14),...label('#F3F4F6 dưới ô núm 22px',x,183,14));
 const row=`${tmp}/review-row.png`;writeImage(row,a);rows.push(row);
}
const sheet='games/typing-defense/art-src/_review/225-sheet.jpg';writeImage(sheet,[...rows,'-append','-quality','94']);
writeText(sheet.replace('.jpg','.prompt.txt'),'Tờ xem kỹ thuật; không gọi sinh ảnh.\nLệnh dựng từ repo cha: node docs/codex-queue/225/review.mjs\nFont: '+font+'\nMỗi hàng: 720p/1080p ở 0,50,100%, nền tối/sáng; vol-master 20/28px; HUD chủ dự án cao 220px; phóng point ×3; mô phỏng hai màu nền kit hiện tại.\nLệnh ImageMagick chi tiết: docs/codex-queue/225/review-commands.json\n');
writeText('docs/codex-queue/225/review-commands.json',JSON.stringify(commands,null,2)+'\n');
