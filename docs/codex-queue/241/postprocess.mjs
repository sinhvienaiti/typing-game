// Chỉ cắt hộp bao alpha >16, thêm đệm trong suốt, co đều Lanczos và sửa alpha mép.
import fs from 'node:fs';
import {execFileSync as run} from 'node:child_process';
const M='/opt/homebrew/bin/magick',base='games/dragon-hold/art-src/ui/quick-settings/sliders',review='games/dragon-hold/art-src/_review/241';
const attempt=process.argv[2]||'1',stem=`slider-track.c2-try${attempt}`,src=`${base}/${stem}.png`;
const im=(a,input)=>run(M,a,{input,maxBuffer:100*1024*1024});
const [w,h]=im(['identify','-format','%w %h',src]).toString().split(' ').map(Number),b=im([src,'-depth','8','rgba:-']);
let x0=w,y0=h,x1=-1,y1=-1;
for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(b[(y*w+x)*4+3]>16){x0=Math.min(x0,x);x1=Math.max(x1,x);y0=Math.min(y0,y);y1=Math.max(y1,y);}
const cw=x1-x0+1,ch=y1-y0+1,padH=Math.max(ch,Math.ceil(cw/16)),padW=16*padH;
const crop=`${review}/${stem}.crop.png`,padded=`${review}/${stem}.padded.png`;
im([src,'-crop',`${cw}x${ch}+${x0}+${y0}`,'+repage',crop]);
im([crop,'-background','none','-gravity','center','-extent',`${padW}x${padH}`,'-define','png:color-type=6',padded]);
const opaqueThreshold=attempt==='3'?250:253;
const record={src,sourceSize:[w,h],bboxAlphaGT16:[x0,y0,cw,ch],bboxRatio:cw/ch,paddedSize:[padW,padH],paddingTotal:[padW-cw,padH-ch],brightnessMultiplier:1,alphaNearlyOpaqueThreshold:opaqueThreshold,outputs:[]};
for(const [ow,oh,suffix] of [[1024,64,'processed'],[512,32,'512.processed']]){
 const dst=`${base}/${stem}.${suffix}.png`;
 const rb=im([padded,'-filter','Lanczos','-resize',`${ow}x${oh}!`,'-depth','8','rgba:-']);
 const changes={nearlyClear:0,nearlyOpaque:0,partialOutside3px:0,keyFringe:0};
 for(let i=0;i<rb.length;i+=4){if(rb[i+3]>0&&rb[i+3]<=2){rb[i+3]=0;changes.nearlyClear++;}else if(rb[i+3]>=opaqueThreshold&&rb[i+3]<255){rb[i+3]=255;changes.nearlyOpaque++;}}
 const mask=Uint8Array.from({length:ow*oh},(_,i)=>rb[i*4+3]>=128?1:0);
 for(let y=0;y<oh;y++)for(let x=0;x<ow;x++){
  const i=(y*ow+x)*4,a=rb[i+3];if(!a)continue;
  let has0=false,has1=false;
  for(let yy=y-3;yy<=y+3;yy++)for(let xx=x-3;xx<=x+3;xx++){
   if(xx<0||yy<0||xx>=ow||yy>=oh)continue;
   if(mask[yy*ow+xx])has1=true;else has0=true;
  }
  // Không sửa RGB; chỉ kẹp alpha lẻ ngoài dải mép 3 px.
  if(a<255&&!(has0&&has1)){rb[i+3]=a>=128?255:0;changes.partialOutside3px++;}
 }
 im(['-size',`${ow}x${oh}`,'-depth','8','rgba:-','-define','png:color-type=6',dst],rb);
 const prompt=fs.readFileSync(`${base}/${stem}.prompt.txt`,'utf8');
 fs.writeFileSync(dst.replace(/\.png$/,'.prompt.txt'),prompt);
 record.outputs.push({file:dst,size:[ow,oh],scaleX:ow/padW,scaleY:oh/padH,equalScale:ow/padW===oh/padH,alphaRepair:changes});
}
fs.writeFileSync(`docs/codex-queue/241/postprocess-try${attempt}.json`,JSON.stringify(record,null,2)+'\n');
console.log(JSON.stringify(record,null,2));
