// Ghép tờ duyệt từ ảnh thật; không vẽ lại tài sản, không mở game.
import fs from 'node:fs';
import {execFileSync as run} from 'node:child_process';
const M='/opt/homebrew/bin/magick',font='/System/Library/Fonts/Supplemental/Arial.ttf',base='games/dragon-hold/art-src/ui/quick-settings/sliders',out='games/dragon-hold/art-src/_review/241',commands=[];
const im=a=>run(M,a,{maxBuffer:100*1024*1024});
const label=(s,x,y,size=18,color='#eee9df')=>['-font',font,'-pointsize',String(size),'-fill',color,'-gravity','NorthWest','-annotate',`+${x}+${y}`,s];
function save(p,a,prompt){im([...a,p]);commands.push({output:p,args:[M,...a,p]});fs.writeFileSync(p.replace(/\.(jpg|png)$/,'.prompt.txt'),prompt+'\nLệnh chính xác: docs/codex-queue/241/review-commands.json\nChạy: node docs/codex-queue/241/review.mjs\n');}
function place(a,src,x,y,opts=[]){a.push('(',src,...opts,')','-geometry',`+${x}+${y}`,'-compose','Over','-composite');}
function bar(scale,pos,bg,kit=false){const w=210*scale,h=10*scale,s=22*scale,x=15,y=Math.round((60-h)/2),kx=x+Math.round((w-s)*pos/100),ky=Math.round(y+h/2-s/2),a=['-size',`${w+30}x60`,`xc:${bg}`];
if(kit)place(a,'xc:#4A505C',x,y,['-resize',`${w}x${h}!`]);
place(a,`${base}/slider-track.png`,x,y,['-filter','Lanczos','-resize',`${w}x${h}!`]);
if(kit)place(a,'xc:#F3F4F6',kx,ky,['-resize',`${s}x${s}!`]);
place(a,`${base}/slider-thumb.png`,kx,ky,['-filter','Lanczos','-resize',`${s}x${s}!`]);return a;}
for(let n=1;n<=3;n++){
const stem=`slider-track.c2-try${n}`,a=['-size','2160x260','xc:#20242b',...label(`Lượt ${n} · bản sinh (cắt hộp bao, giữ tỉ lệ)`,24,16,24),...label('Bản hậu kỳ · 1024 × 64 · co x = co y',1104,16,24)];
place(a,`${out}/${stem}.crop.png`,28,85,['-filter','Lanczos','-resize','1024x150']);
place(a,`${base}/${stem}.processed.png`,1108,85);
const p=JSON.parse(fs.readFileSync(`docs/codex-queue/241/postprocess-try${n}.json`));a.push(...label(`Hộp bao: ${p.bboxAlphaGT16.join(', ')} · tỉ lệ ${p.bboxRatio.toFixed(4)}:1`,24,205),...label(`Đệm ${p.paddedSize.join(' × ')} · hệ số ${p.outputs[0].scaleX.toFixed(9)} / ${p.outputs[0].scaleY.toFixed(9)}`,1104,205));
save(`${out}/try${n}-compare.jpg`,a,`Tờ so sánh bản sinh | bản hậu kỳ cùng ô 1080×260; ảnh gốc giữ tỉ lệ, không chỉnh RGB. Prompt sinh: ${base}/${stem}.prompt.txt`);
}
const a=['-size','1800x1090','xc:#15191f',...label('DRAGONHOLD · Phiếu 241 · lượt 3 · CHƯA ĐẠT Kiểm 4 (trái 69 px > 61 px)',20,15,26)];
for(const [i,[scale,bg,name]] of [[1,'#2b2118','720p · tối'],[1,'#f1e3c4','720p · sáng'],[1.5,'#2b2118','1080p · tối'],[1.5,'#f1e3c4','1080p · sáng']].entries()){
 const x=20+i*445;a.push(...label(name,x,65,22));for(const [j,pos] of [0,50,100].entries()){
 a.push('(',...bar(scale,pos,bg),')','-geometry',`+${x}+${105+j*95}`,'-compose','Over','-composite',...label(`${pos}% · rãnh ${210*scale}×${10*scale}, ô núm ${22*scale}px`,x,168+j*95,16));}}
a.push(...label('Rãnh 1024 × 64 và núm đã nhận (thu 128 px, giữ đúng lề)',20,410,20));place(a,`${base}/slider-track.png`,20,455);place(a,`${base}/slider-thumb.png`,1100,427,['-resize','128x128']);
a.push(...label('720p · 50% · phóng ×3 · point',20,555,20),'(',...bar(1,50,'#2b2118'),'-filter','point','-resize','300%',')','-geometry','+20+590','-compose','Over','-composite');
a.push(...label('Kit hôm nay · 720p · 50%',790,555,20),'(',...bar(1,50,'#2b2118',true),')','-geometry','+790+590','-compose','Over','-composite',...label('#4A505C dưới rãnh; #F3F4F6 dưới ô núm',790,660,16));
const icon='games/dragon-hold/art-src/ui/quick-settings/selected/vol-master.png';place(a,icon,790,710,['-resize','20x20']);place(a,icon,850,706,['-resize','28x28']);a.push(...label('vol-master 20 / 28 px · cùng bộ',790,750,16));
place(a,'games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp',1380,555,['-crop','369x234+1005+476','+repage','-resize','347x220!']);a.push(...label('HUD thương mại · tham chiếu chủ dự án',1380,785,16));
a.push(...label('Kiểm kéo giãn · 720p: 90 / 210 / 290 × 10 px',20,815,20));for(const [i,w] of [90,210,290].entries())place(a,`${base}/slider-track.png`,20+i*340,860,['-filter','Lanczos','-resize',`${w}x10!`]);
a.push(...label('Kiểm kéo giãn · 1080p: 135 / 315 / 435 × 15 px',20,910,20));for(const [i,w] of [135,315,435].entries())place(a,`${base}/slider-track.png`,20+i*470,955,['-filter','Lanczos','-resize',`${w}x15!`]);
a.push(...label('Núm và toàn bộ ảnh đã nhận giữ nguyên. Mức 0/50/100% chỉ đổi vị trí núm; rãnh không có phần đã đầy.',20,1030,18));
save(`${out}/241-sheet.jpg`,a,'Tờ xem kỹ thuật dùng bản chọn lượt 3, núm Dragonhold đã nhận, 0/50/100% ở 720p và 1080p, hai nền #2b2118 / #f1e3c4; phóng point ×3; kit hiện tại; icon bộ 180; mảnh HUD tham chiếu. Font Arial theo phiếu. Không gọi công cụ sinh ảnh.');
fs.writeFileSync('docs/codex-queue/241/review-commands.json',JSON.stringify(commands,null,2)+'\n');
console.log('Đã ghép 3 tờ so sánh và 241-sheet.jpg.');
