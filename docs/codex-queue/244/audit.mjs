import fs from 'node:fs';
import {im,raw,box,mask,iou,lum,hsv,json,D} from './lib.mjs';
const records=JSON.parse(fs.readFileSync(`${D}/processed.json`));
const panels={'dragon-hold':'ui/frames/panel-large.png','typing-defense':'ui/frames-epic/panel-large.v2.png','typing-survival':'ui/frames-epic/panel-large.png'};
function alphaAudit(p,w,h){const b=raw(p),m=mask(b,127);let partial=0,key=0,vis=0;for(let y=0;y<h;y++)for(let x=0;x<w;x++){const i=(y*w+x)*4,a=b[i+3];if(a){vis++;const [hu,s]=hsv(b[i],b[i+1],b[i+2]);if(Math.abs(hu-300)<=15&&s>.5)key++;}if(a>0&&a<255){let v0=false,v1=false;for(let yy=Math.max(0,y-3);yy<=Math.min(h-1,y+3);yy++)for(let xx=Math.max(0,x-3);xx<=Math.min(w-1,x+3);xx++){if(m[yy*w+xx])v1=true;else v0=true;}if(!(v0&&v1))partial++;}}
 return {size:[w,h],bbox:box(b,w,h),partialOutside3px:partial,keyHuePercent:key/vis*100};}
function opening(m,w,h){let e=new Uint8Array(m.length),d=new Uint8Array(m.length);for(let y=0;y<h-1;y++)for(let x=0;x<w-1;x++)e[y*w+x]=m[y*w+x]&&m[y*w+x+1]&&m[(y+1)*w+x]&&m[(y+1)*w+x+1];for(let y=0;y<h;y++)for(let x=0;x<w;x++){for(let yy=Math.max(0,y-1);yy<=y;yy++)for(let xx=Math.max(0,x-1);xx<=x;xx++)if(e[yy*w+xx])d[y*w+x]=1;}return d;}
function mean(b,w,h,x0,x1,y0,y1){let sum=0,n=0;for(let y=y0;y<y1;y++)for(let x=x0;x<x1;x++){const i=(y*w+x)*4;if(b[i+3]>=128){sum+=lum(b[i],b[i+1],b[i+2]);n++;}}return sum/n;}
const report={icons:[],sliders:[],pairs:[],sliderPairs:[]};
for(const r of records){const p=r.outputs[0].file;if(r.type==='icon'){
 const s=r.name==='hud-settings'?28:24,hi=r.name==='hud-settings'?40:36,b=raw(p,s),m=mask(b,128),bb=box(b,s,s,128),opened=opening(m,s,s),count=m.reduce((a,v)=>a+v,0);const panel=`games/${r.game}/art-src/${panels[r.game]}`;
 // Vùng lòng bảng thật tại x=256,y=256. Không tô màu hoặc vẽ lại mảnh nền.
 const patch=im([panel,'-crop',`${s}x${s}+208+208`,'+repage','-depth','8','rgba:-']);let fg=0,bg=0,n=0;for(let i=0;i<m.length;i++)if(m[i]){const j=i*4,a=b[j+3]/255;fg+=lum(b[j]*a+patch[j]*(1-a),b[j+1]*a+patch[j+1]*(1-a),b[j+2]*a+patch[j+2]*(1-a));bg+=lum(patch[j],patch[j+1],patch[j+2]);n++;}
 report.icons.push({game:r.game,name:r.name,job:r.job,size720:s,size1080:hi,source:p,alpha:r.outputs.map(o=>alphaAudit(o.file,...o.size)),openingRetention:opened.reduce((a,v)=>a+v,0)/count,coverage:count/(bb[2]*bb[3]),contrastOnPanel:fg/n-bg/n,panelMeanLuma:bg/n,objectMeanLuma:fg/n});
 }else{
 const b=raw(p),track=`games/${r.game}/art-src/ui/quick-settings/sliders/slider-track.png`,old=raw(track),bb=box(b,1024,64),ob=box(old,1024,64);
 const stretches=[];for(const [w,h] of [[90,10],[210,10],[290,10],[135,15],[315,15],[435,15]]){const rb=raw(p,w,h),col=[];for(let x=Math.ceil(w*.1);x<Math.floor(w*.9);x++){let su=0;for(let y=0;y<h;y++){let i=(y*w+x)*4;su+=lum(rb[i],rb[i+1],rb[i+2])*rb[i+3]/255;}col.push(su/h);}const avg=col.reduce((a,v)=>a+v,0)/col.length,sd=Math.sqrt(col.reduce((a,v)=>a+(v-avg)**2,0)/col.length);stretches.push({size:[w,h],columnStddev:sd});}
 report.sliders.push({game:r.game,name:r.name,job:r.job,source:p,alpha:r.outputs.map(o=>alphaAudit(o.file,...o.size)),iouToTrack:iou(mask(b),mask(old)),bbox:bb,trackBbox:ob,endOffset:[Math.abs(bb[0]-ob[0]),Math.abs(bb[0]+bb[2]-ob[0]-ob[2])],channelRegion:[103,921,20,44],channelLuma:mean(b,1024,64,103,921,20,44),trackChannelLuma:mean(old,1024,64,103,921,20,44),stretches});
 }}
for(const g of ['dragon-hold','typing-defense']){
 const icons=report.icons.filter(r=>r.game===g);const all=new Map(icons.map(r=>[r.name,r.source]));for(const n of ['vol-master','vol-music','vol-effects','vol-voice'])if(!all.has(n))all.set(n,`games/${g}/art-src/ui/quick-settings/selected/${n}.png`);
 const names=[...all.keys()];for(let a=0;a<names.length;a++)for(let b=a+1;b<names.length;b++)for(const s of [24,32])report.pairs.push({game:g,a:names[a],b:names[b],size:s,iou:iou(mask(raw(all.get(names[a]),s)),mask(raw(all.get(names[b]),s)))});
}
for(const g of ['dragon-hold','typing-defense','typing-survival']){const fill=report.sliders.find(r=>r.game===g&&r.name==='slider-fill'),empty=report.sliders.find(r=>r.game===g&&r.name==='slider-empty');report.sliderPairs.push({game:g,lumaDelta:fill.channelLuma-(empty?empty.channelLuma:fill.trackChannelLuma),iouFillEmpty:empty?iou(mask(raw(fill.source)),mask(raw(empty.source))):fill.iouToTrack});}
json(`${D}/metrics.json`,report);console.log(JSON.stringify(report,null,2));
