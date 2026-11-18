import fs from 'node:fs';
import {root,rev,run,put,rgba,txt,img,measure} from './core.mjs';
const jobs=JSON.parse(fs.readFileSync('docs/codex-queue/240/selection.json'));
const selected=Object.fromEntries(jobs.map(j=>[j.name.split('.')[0],`${j.base}.png`]));
const p=n=>selected[n]||`${root}/ui/${n.startsWith('mag-')?'parts':'icons'}/${n}.png`;
function tile(a,path,x,y,size,bg,w=150,h=70,zoom=1){a.push('(','-size',`${w}x${h}`,'xc:'+bg,'(',path,'-filter','Lanczos','-resize',`${size}x${size}!`,...(zoom!==1?['-filter','point','-resize',`${size*zoom}x${size*zoom}!`]:[]),')','-gravity','center','-composite',')','-gravity','NorthWest','-geometry',`+${x}+${y}`,'-composite');}
for(const zoom of [1,8]){
 const a=['-size','1580x1780','xc:#272e37'];txt(a,`240 · Last Line · ${zoom===1?'Cỡ thật':'Cỡ nhỏ phóng nearest 8× để kiểm nét'}`,20,12,24);
 jobs.forEach((j,i)=>{const x=20+i*310;tile(a,`${j.base}.png`,x,55,256,'#14181f',290,270);txt(a,j.name,x,330,17);});
 txt(a,'Icon 20 / 24 / 30 / 36 px · nền than chì và thép sáng',20,375,20);
 for(let i=0;i<4;i++){const x=20+i*310,n=jobs[i].name;for(let r=0;r<4;r++){const size=[20,24,30,36][r],y=415+r*100;txt(a,`${size}px`,x,y,14);for(let b=0;b<2;b++)tile(a,`${jobs[i].base}.png`,x+b*145,y+18,size,['#14181f','#8c96a3'][b],140,75,zoom===1?1:4);}}
 txt(a,'So cặp · shake / reduced-motion | mag-empty / mag-full | station-crest / chapter-crest',20,830,20);
 const pairs=[['shake','reduced-motion'],['mag-empty','mag-full'],['station-crest','chapter-crest']];
 pairs.forEach((pair,i)=>{const x=20+i*510;txt(a,pair.join(' / '),x,865,17);for(let r=0;r<2;r++){const size=[20,30][r],y=895+r*105;txt(a,`${size}px`,x,y,14);for(let b=0;b<2;b++)for(let k=0;k<2;k++)tile(a,p(pair[k]),x+b*245+k*115,y+18,size,['#14181f','#8c96a3'][b],110,80,zoom===1?1:2);}});
 txt(a,'Ô đạn 10 / 15 px · rỗng mới | đầy đã nhận | rỗng cũ',20,1135,20);
 for(let r=0;r<2;r++)for(let b=0;b<2;b++)for(let k=0;k<3;k++){const size=[10,15][r],x=20+(b*3+k)*250,y=1170+r*110;tile(a,k===0?p('mag-empty'):k===1?p('mag-full'):`${rev}/prev/ui/parts/mag-empty.png`,x,y,size,['#14181f','#8c96a3'][b],240,80,zoom);txt(a,`${['mới','đầy','cũ'][k]} · ${size}px`,x,y+80,14);}
 txt(a,'Đối chiếu bộ cũ và HUD thương mại · cùng cao 96 px',20,1455,20);
 for(const [i,n] of ['gun-xung','gun-tia','gun-tan','gun-ray'].entries()){img(a,root+'/ui/icons/'+n+'.norm.256.png',20+i*190,1500,96,'#14181f');txt(a,n,20+i*190,1610,15);}
 a.push('(',root+'/_review/153/resume-20261031/owner-hud-crop.png','-resize','120x96!',')','-gravity','NorthWest','-geometry','+800+1500','-composite');txt(a,'HUD chủ dự án',790,1610,15);
 img(a,root+'/ui/frames-epic/panel-large.alpha.png',1030,1500,96,'#14181f');txt(a,'127 · khung',1030,1610,15);
 a.push('(',root+'/ui/screens-epic/briefing-bg.png','-resize','171x96!',')','-gravity','NorthWest','-geometry','+1250+1500','-composite');txt(a,'121 · Lightbearer',1250,1610,15);
 txt(a,'Bản chọn: shake c2-try1; reduced-motion c2-try2; stat-evenness try2; station-crest c2-try3; mag-empty try3.',20,1670,17);
 txt(a,'Bản thu giữ Lanczos trực tiếp, xem ngoại lệ alpha trong báo cáo; chờ Claude chấm lại từ 8.',20,1710,17);
 a.push('-quality','96',`${root}/_review/240-${zoom===1?'sheet-small':'sheet-nearest'}.jpg`);run(a);
}
const pair={};for(const size of [10,15,20,30]){const e=measure(rgba(p('mag-empty'),size),size),f=measure(rgba(p('mag-full'),size),size);pair[size]={empty:e.luma,full:f.luma,delta:f.luma-e.luma};}
const groups={settings:['sfx','music','shake','reduced-motion','read-aloud','pace-director.v2','quality','stat-wpm.v2','stat-new-word','stat-evenness','rift'],parts:['keycap','keycap-active','led-on','led-off','mag-empty','mag-full','arrow'],stage:['objective','hazard','learning-rule','equipment','warning','new-badge','station-crest','chapter-crest','load-guns','back','shard']};
const ious={};for(const [g,names] of Object.entries(groups)){const masks=Object.fromEntries(names.map(n=>[n,rgba(selected[n]||`${root}/ui/${g==='parts'?'parts':'icons'}/${n}.png`,32)]));ious[g]=[];for(let i=0;i<names.length;i++)for(let j=i+1;j<names.length;j++){const aa=masks[names[i]],bb=masks[names[j]],v={a:names[i],b:names[j]};for(const t of [16,127]){let inter=0,union=0;for(let k=3;k<aa.length;k+=4){const a=aa[k]>t,b=bb[k]>t;if(a&&b)inter++;if(a||b)union++;}v['iou'+t]=inter/union;}ious[g].push(v);}}
fs.writeFileSync(`${rev}/comparison.json`,JSON.stringify({pair,ious},null,2));
console.log(JSON.stringify({pair,ious:Object.fromEntries(Object.entries(ious).map(([g,v])=>[g,v.sort((a,b)=>b.iou127-a.iou127).slice(0,5)]))},null,2));
