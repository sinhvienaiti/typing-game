import fs from 'node:fs';
import {im,dim,raw,box,clean,png,hsv,json,D} from './lib.mjs';
const jobs=JSON.parse(fs.readFileSync(`${D}/prompts.json`)),selection=[16,17,2,13,14,5,18,15,19,9,21,11];
const records=[];
for(const ji of selection){console.log('Traitement',ji); const j=jobs[ji],src=j.output,[w,h]=dim(src),rev=`games/${j.game}/art-src/_review/244`;fs.mkdirSync(rev,{recursive:true});
 const b=raw(src);let keyRemoved=0;
 if(j.type==='icon')for(let i=0;i<b.length;i+=4){const [hu,s]=hsv(b[i],b[i+1],b[i+2]);if(Math.abs(hu-300)<=30&&s>.35){b[i+3]=0;keyRemoved++;}}
 const bounds=box(b,w,h),[x,y,cw,ch]=bounds;
 const source=png(b,w,h);let pw,ph;
 if(j.type==='icon'){const long=Math.max(cw,ch);pw=ph=Math.ceil(long/.70);}
 else{ph=Math.max(ch,Math.ceil(cw/16));pw=ph*16;}
 const brightness=(ji===13?1.06:ji===16?1.10:1);
 const padded=im(['png:-',...(brightness!==1?['-channel','RGB','-evaluate','Multiply',String(brightness),'+channel']:[]),'-crop',`${cw}x${ch}+${x}+${y}`,'+repage','-background','none','-gravity','center','-extent',`${pw}x${ph}`,'png:-'],source);
 const prefix=`${rev}/${j.name}-try${j.attempt||1}${brightness!==1?'.bright'+brightness:''}`;
 const outputs=[];
 for(const s of (j.type==='icon'?[1024,256,128,64]:[1024,512])){
  console.log('Taille',s); const oh=j.type==='icon'?s:s/16;
  const rb=im(['png:-','-filter','Lanczos','-resize',`${s}x${oh}!`,'-depth','8','rgba:-'],padded);const repair=clean(rb,s,oh);
  const dest=`${prefix}${s===1024?'':'.'+s}.processed.png`;
  if(!fs.existsSync(dest))fs.writeFileSync(dest,png(rb,s,oh));
  outputs.push({file:dest,size:[s,oh],scaleX:s/pw,scaleY:oh/ph,alphaRepair:repair});
 }
 records.push({job:ji,game:j.game,name:j.name,type:j.type,src,size:[w,h],bbox:bounds,padded:[pw,ph],keyRemoved,brightness,outputs});
}
json(`${D}/processed.json`,records);console.log(records.map(r=>({name:r.game+'/'+r.name,bbox:r.bbox,padded:r.padded})));
