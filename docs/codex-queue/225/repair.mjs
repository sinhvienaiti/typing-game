// Sửa alpha ở mép; giữ nguyên RGB, giữ nguyên phần vẽ đục trong lòng vật.
import fs from 'node:fs';
import {execFileSync as run} from 'node:child_process';
const [game,name,attempt,revision='edge',sizeTag='']=process.argv.slice(2),M='/opt/homebrew/bin/magick';
if(!['dragon-hold','typing-defense','typing-survival'].includes(game)||!['slider-track','slider-thumb'].includes(name))throw Error('Sai đích');
const tmp=`games/${game}/tmp/codex-225`,tag=`${name}.try${attempt}.${revision}`+(sizeTag?`.${sizeTag}`:''),src=`${tmp}/${tag}.processed.png`,dst=`${tmp}/${tag}.clean.processed.png`;
if(fs.existsSync(dst))throw Error('Giữ file có sẵn '+dst);
const [w,h]=run(M,['identify','-format','%w %h',src]).toString().split(' ').map(Number);
const b=run(M,[src,'-depth','8','rgba:-'],{maxBuffer:100*1024*1024});
const hue=(r,g,b)=>{const mx=Math.max(r,g,b),mn=Math.min(r,g,b),d=mx-mn;let hh=0;if(d){hh=mx===r?((g-b)/d)%6:mx===g?(b-r)/d+2:(r-g)/d+4;hh=(hh*60+360)%360;}return [hh,mx?d/mx:0];};
const changes={clippedNearlyOpaque:0,clippedNearlyClear:0,keyFringe:0,partialOutside3px:0,interiorKey:0};
for(let i=0;i<b.length;i+=4){if(b[i+3]>0&&b[i+3]<=2){b[i+3]=0;changes.clippedNearlyClear++;}else if(b[i+3]>=253&&b[i+3]<255){b[i+3]=255;changes.clippedNearlyOpaque++;}}
const original=Buffer.from(b);
if(game!=='typing-survival')for(let y=0;y<h;y++)for(let x=0;x<w;x++){const i=(y*w+x)*4;if(!b[i+3])continue;const [hh,s]=hue(b[i],b[i+1],b[i+2]);if(Math.abs(hh-300)>15||s<=.5)continue;let outside=false;for(let yy=y-3;yy<=y+3;yy++)for(let xx=x-3;xx<=x+3;xx++)if(xx<0||yy<0||xx>=w||yy>=h||original[(yy*w+xx)*4+3]<128)outside=true;if(!outside){changes.interiorKey++;continue;}b[i+3]=0;changes.keyFringe++;}
// Pixel sắc khóa nằm sâu trong vật được giữ; audit quyết ngưỡng 0,2%.
const mask=Uint8Array.from({length:w*h},(_,i)=>b[i*4+3]>=128?1:0);
for(let y=0;y<h;y++)for(let x=0;x<w;x++){const i=(y*w+x)*4,a=b[i+3];if(a===0||a===255)continue;let has0=false,has1=false;for(let yy=Math.max(0,y-3);yy<=Math.min(h-1,y+3);yy++)for(let xx=Math.max(0,x-3);xx<=Math.min(w-1,x+3);xx++){if(mask[yy*w+xx])has1=true;else has0=true;}if(!(has0&&has1)){b[i+3]=a>=128?255:0;changes.partialOutside3px++;}}
run(M,['-size',`${w}x${h}`,'-depth','8','rgba:-','-define','png:color-type=6',dst],{input:b,maxBuffer:100*1024*1024});
const record={src,dst,changes,policy:'Giữ nguyên mọi RGB; sửa alpha dư khóa ở mép, kẹp alpha gần 0/255 và alpha nằm ngoài dải mép 3 px về phía gần nhất.'};
fs.writeFileSync(`docs/codex-queue/225/repair-${game}-${tag}.json`,JSON.stringify(record,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify(record));
