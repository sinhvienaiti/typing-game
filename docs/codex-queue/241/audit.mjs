import fs from 'node:fs';
import {execFileSync as run} from 'node:child_process';
import crypto from 'node:crypto';
const M='/opt/homebrew/bin/magick', out='docs/codex-queue/241';
const games=['dragon-hold','typing-defense','typing-survival'];
const palettes={'dragon-hold':['#2b2118','#f1e3c4'],'typing-defense':['#061e16','#b8aa94','#1f3b33','#e8e1cf'],'typing-survival':['#14181f','#8c96a3']};
const im=a=>run(M,a,{maxBuffer:100*1024*1024});
const dims=p=>im(['identify','-format','%w %h %[channels]',p]).toString().split(' ');
const raw=(p,size)=>im([p,...(size?['-filter','Lanczos','-resize',size+'!']:[]),'-depth','8','rgba:-']);
const col=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)/255);
const Y=c=>.2126*c[0]+.7152*c[1]+.0722*c[2];
const mean=a=>a.reduce((s,x)=>s+x,0)/a.length;
const median=a=>[...a].sort((a,b)=>a-b)[Math.floor(a.length/2)];
const std=a=>Math.sqrt(mean(a.map(x=>(x-mean(a))**2)));
function hue(r,g,b){const mx=Math.max(r,g,b),mn=Math.min(r,g,b),d=mx-mn;let h=0;if(d){h=mx===r?((g-b)/d)%6:mx===g?(b-r)/d+2:(r-g)/d+4;h=(h*60+360)%360;}return [h,mx?d/mx:0];}
function bbox(b,w,h){let x0=w,y0=h,x1=-1,y1=-1;for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(b[(y*w+x)*4+3]>16){x0=Math.min(x0,x);x1=Math.max(x1,x);y0=Math.min(y0,y);y1=Math.max(y1,y);}return [x0,y0,x1-x0+1,y1-y0+1];}
function alphaMetric(p,size,keyHue){const [sw,sh,ch]=dims(p),[w,h]=size?size.split('x').map(Number):[+sw,+sh],b=raw(p,size),integ=new Int32Array((w+1)*(h+1));
 for(let y=0;y<h;y++)for(let x=0;x<w;x++)integ[(y+1)*(w+1)+x+1]=(b[(y*w+x)*4+3]>=128?1:0)+integ[y*(w+1)+x+1]+integ[(y+1)*(w+1)+x]-integ[y*(w+1)+x];
 let partial=0,key=0,visible=0,opaque=0,central=0,centralOpaque=0;
 for(let y=0;y<h;y++)for(let x=0;x<w;x++){const a=b[(y*w+x)*4+3];if(a>0){visible++;const [hh,s]=hue(...b.subarray((y*w+x)*4,(y*w+x)*4+3));if(keyHue!==null&&Math.min(Math.abs(hh-keyHue),360-Math.abs(hh-keyHue))<=15&&s>.5)key++;}if(a===255)opaque++;
  if(x>=Math.ceil(w*.1)&&x<Math.floor(w*.9)){central++;if(a===255)centralOpaque++;}
  if(a>0&&a<255){const x0=Math.max(0,x-3),x1=Math.min(w,x+4),y0=Math.max(0,y-3),y1=Math.min(h,y+4);const n=integ[y1*(w+1)+x1]-integ[y0*(w+1)+x1]-integ[y1*(w+1)+x0]+integ[y0*(w+1)+x0];if(n===0||n===(x1-x0)*(y1-y0))partial++;}}
 const box=bbox(b,w,h);return {file:p,size:[w,h],channels:ch,bboxAlphaGT16:box,coverageLongest:Math.max(box[2],box[3])/Math.max(w,h),centerDeviation:[Math.abs(box[0]+box[2]/2-w/2)/w,Math.abs(box[1]+box[3]/2-h/2)/h],partialOutside3px:partial,keyHuePixels:key,visiblePixels:visible,keyHuePercent:key/visible*100,centralOpaqueFraction:centralOpaque/central,passAlpha:partial===0&&key/visible<=.002};
}
function compositeY(b,i,bg){const a=b[i+3]/255;return Y([0,1,2].map(c=>b[i+c]/255*a+bg[c]*(1-a)));}
function colMeans(p,w,h,bg){const b=raw(p,`${w}x${h}`),c=col(bg),a=[];for(let x=0;x<w;x++){let sum=0;for(let y=0;y<h;y++)sum+=compositeY(b,(y*w+x)*4,c);a.push(sum/h);}return a;}
function endcaps(p,bg){const a=colMeans(p,1024,64,bg),mid=median(a.slice(103,921));let left=null,right=null;const okay=(start)=>a.slice(start,start+16).every(v=>Math.abs(v-mid)<=.03);for(let x=0;x<=1008;x++)if(okay(x)){left=x;break;}for(let x=1008;x>=0;x--)if(okay(x)){right=1024-(x+16);break;}return {background:bg,centralMedian:mid,leftPx:left,rightPx:right,pass:left!==null&&right!==null&&left<=61&&right<=61};}
function readability(track,thumb,scale,bg){const w=210*scale,h=10*scale,s=22*scale,t=raw(track,`${w}x${h}`),k=raw(thumb,`${s}x${s}`),background=col(bg);let ts=0,tn=0,ks=0,kn=0;
 // Rãnh: chỉ các pixel alpha >=128 không bị núm ở vị trí 50% che.
 const kx=Math.round((w-s)/2),ky=Math.round((h-s)/2);
 for(let y=0;y<h;y++)for(let x=0;x<w;x++){const i=(y*w+x)*4;const xx=x-kx,yy=y-ky;const covered=xx>=0&&xx<s&&yy>=0&&yy<s&&k[(yy*s+xx)*4+3]>=128;if(t[i+3]>=128&&!covered){ts+=compositeY(t,i,background);tn++;}}
 for(let i=0;i<k.length;i+=4)if(k[i+3]>=128){ks+=compositeY(k,i,background);kn++;}
 const ty=ts/tn,kyy=ks/kn;return {scale,background:bg,trackMeanLuma:ty,thumbMeanLuma:kyy,panelLuma:Y(background),thumbMinusTrack:kyy-ty,trackMinusPanel:ty-Y(background),trackAbsPanel:Math.abs(ty-Y(background)),passDark:kyy-ty>=.25&&ty-Y(background)>=.12};
}

const attempt=process.argv[2]||'1',base='games/dragon-hold/art-src/ui/quick-settings/sliders',track=attempt==='final'?`${base}/slider-track.png`:`${base}/slider-track.c2-try${attempt}.processed.png`,small=attempt==='final'?`${base}/slider-track.512.png`:`${base}/slider-track.c2-try${attempt}.512.processed.png`,thumb=`${base}/slider-thumb.png`;
const images=[alphaMetric(track,null,300),alphaMetric(small,null,300)];
const stretch=[[90,10],[210,10],[290,10],[135,15],[315,15],[435,15]].map(([w,h])=>{const c=colMeans(track,w,h,'#2b2118'),v=std(c.slice(Math.ceil(.1*w),Math.floor(.9*w)));return {size:[w,h],centralColumnLumaStd:v,pass:v<=.05};});
const ends=endcaps(track,'#2b2118'),read=['#2b2118','#f1e3c4'].flatMap(bg=>[1,1.5].map(s=>readability(track,thumb,s,bg)));
const before=JSON.parse(fs.readFileSync(`${out}/sha256-before.json`,'utf8')),hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const allowed=['slider-track.png','slider-track.512.png','slider-track.prompt.txt'].map(n=>base+'/'+n),changed=Object.keys(before).filter(p=>!fs.existsSync(p)||hash(p)!==before[p]);
const result={attempt,track,thumb,alpha:images,stretch,endcaps:ends,readability:read,checks:{KA1:{changed,allowed,pass:changed.every(p=>allowed.includes(p))},dimensions:images.every((x,i)=>x.size.join('x')===(i?'512x32':'1024x64')&&x.channels==='srgba'),alpha:images.every(x=>x.passAlpha)&&images[0].centralOpaqueFraction>=.9,stretch:stretch.every(x=>x.pass)&&ends.pass,readability:read.filter(x=>x.background==='#2b2118').every(x=>x.passDark)}};
result.pass=Object.values(result.checks).every(x=>typeof x==='boolean'?x:x.pass);
fs.writeFileSync(`${out}/metrics-try${attempt}.json`,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
