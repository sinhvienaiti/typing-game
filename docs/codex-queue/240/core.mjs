import fs from 'node:fs';
import cp from 'node:child_process';
const root='games/typing-survival/art-src',rev=`${root}/_review/240`,M='/opt/homebrew/bin/magick';
const run=(a,input)=>cp.execFileSync(M,a,{input,maxBuffer:80*1024*1024});
const put=(p,s)=>fs.writeFileSync(p,s,{flag:'wx'});
const rgba=(p,n)=>run([p,...(n?['-filter','Lanczos','-resize',`${n}x${n}!`]:[]),'-depth','8','rgba:-']);
function box(r,w,t=16){let x0=w,y0=w,x1=-1,y1=-1;for(let y=0;y<w;y++)for(let x=0;x<w;x++)if(r[4*(y*w+x)+3]>t){x0=Math.min(x,x0);y0=Math.min(y,y0);x1=Math.max(x,x1);y1=Math.max(y,y1);}return{x:x0,y:y0,w:x1-x0+1,h:y1-y0+1};}
const offsets=[];for(let dy=-3;dy<=3;dy++)for(let dx=-3;dx<=3;dx++)if(dx*dx+dy*dy<=9)offsets.push([dx,dy]);
function edge(r,n,x,y,t){const inside=r[4*(y*n+x)+3]>t;return offsets.some(([dx,dy])=>{const xx=x+dx,yy=y+dy;return xx<0||yy<0||xx>=n||yy>=n||((r[4*(yy*n+xx)+3]>t)!==inside)});}
function matte(input,n){let r=Buffer.from(input),steps=0,maxDelta=0;for(let pass=0;pass<12;pass++){const out=Buffer.from(r);let changes=0;for(let y=0;y<n;y++)for(let x=0;x<n;x++){const k=4*(y*n+x)+3,a=r[k];if(a===0||a===255)continue;if([16,127].some(t=>!edge(r,n,x,y,t))){const b=a>127?255:0;out[k]=b;changes++;maxDelta=Math.max(maxDelta,Math.abs(a-b));}}r=out;steps+=changes;if(!changes)break;if(pass===11)throw Error('Matte convergence');}let rgbChanged=0,alphaChanged=0;for(let k=0;k<r.length;k+=4){if(r[k]!==input[k]||r[k+1]!==input[k+1]||r[k+2]!==input[k+2])rgbChanged++;if(r[k+3]!==input[k+3])alphaChanged++;}return {r,audit:{steps,maxDelta,rgbChanged,alphaChanged}};}
function measure(r,n){let weight=0,sum=0,semi16=0,semi127=0,key=0,nonzero=0;for(let y=0;y<n;y++)for(let x=0;x<n;x++){const k=4*(y*n+x),a=r[k+3];if(!a)continue;nonzero++;sum+=(.2126*r[k]+.7152*r[k+1]+.0722*r[k+2])*a/255;weight+=a;const R=r[k]/255,G=r[k+1]/255,B=r[k+2]/255,mx=Math.max(R,G,B),mn=Math.min(R,G,B),d=mx-mn;let hue=0;if(d){hue=mx===R?60*((G-B)/d%6):mx===G?60*((B-R)/d+2):60*((R-G)/d+4);if(hue<0)hue+=360;}if(mx&&d/mx>.5&&Math.abs(hue-300)<=15)key++;if(a===255)continue;if(!edge(r,n,x,y,16))semi16++;if(!edge(r,n,x,y,127))semi127++;}
const luma=sum/weight,b=box(r,n);return {n,bbox:b,longestPct:100*Math.max(b.w,b.h)/n,offsetPct:[100*Math.abs(b.x+b.w/2-n/2)/n,100*Math.abs(b.y+b.h/2-n/2)/n],semi16,semi127,keyLeakPct:100*key/nonzero,luma,deltaDark:Math.abs(luma-(.2126*20+.7152*24+.0722*31)/255),deltaLight:Math.abs(luma-(.2126*140+.7152*150+.0722*163)/255),deltaActualDark:Math.abs(luma-(.2126*17+.7152*22+.0722*29)/255)};}
function txt(a,s,x,y,size=16){a.push('-font','/System/Library/Fonts/Supplemental/Arial.ttf','-pointsize',String(size),'-fill','#edf2f5','-gravity','NorthWest','-annotate',`+${x}+${y}`,s);}
function img(a,p,x,y,n,bg){a.push('(',p,'-filter','Lanczos','-resize',`${n}x${n}!`,'-background',bg,'-alpha','remove','-alpha','off',')','-gravity','NorthWest','-geometry',`+${x}+${y}`,'-composite');}

export {root,rev,M,run,put,rgba,box,matte,measure,txt,img};
