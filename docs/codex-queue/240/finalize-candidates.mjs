import fs from 'node:fs';
import {root,rev,run,put,rgba,measure,txt,img} from './core.mjs';
const originals=JSON.parse(fs.readFileSync('docs/codex-queue/240/jobs.json'));
const retry=JSON.parse(fs.readFileSync('docs/codex-queue/240/jobs-retries.json'));
const jobs=[originals[0],retry[1],originals[2],originals[3],retry[0]];
const choices=[];
for (const j of jobs){
 const source=`${rev}/${j.name}.post.png`,base=`${rev}/${j.name}.delivery`;
 if(j.name==='mag-empty.try3')run([source,'-channel','RGB','-evaluate','Multiply','0.944','+channel','-colorspace','sRGB','PNG32:'+base+'.png']);
 else fs.copyFileSync(source,base+'.png',fs.constants.COPYFILE_EXCL);
 const prompt=fs.readFileSync(`${root}/ui/${j.dir}/${j.name}.prompt.txt`);put(base+'.prompt.txt',prompt);
 // Direct Lanczos from the master, preserving alpha rather than filling small details.
 for(const n of [256,128,64]){run([base+'.png','-filter','Lanczos','-resize',`${n}x${n}!`,'-colorspace','sRGB','PNG32:'+base+'.'+n+'.png']);put(base+'.'+n+'.prompt.txt',prompt);}
 const sizes=j.dir==='parts'?[10,15,20,30]:[20,24,30,36];
 const metrics=[1024,256,128,64,...sizes].map(n=>({...measure(rgba(base+(n>=64&&n<1024?'.'+n:'')+'.png',n<64?n:undefined),n)}));
 const a=['-size','1120x720','xc:#232831'];txt(a,`${j.name} · bản sinh | bản giao`,18,12,22);img(a,`${root}/ui/${j.dir}/${j.name}.png`,20,50,400,'#14181f');img(a,base+'.png',560,50,400,'#14181f');txt(a,'Bản sinh: toàn bộ canvas',20,460);txt(a,j.dir==='parts'?'Bản giao: giảm sáng RGB 5,6%; giữ lòng rãnh':'Bản giao: căn vật 70%; giữ màu RGB',560,460);txt(a,'Cỡ thật · than chì #14181f / thép sáng #8c96a3',20,505,18);
 for(let i=0;i<sizes.length;i++){const n=sizes[i],x=20+i*270;txt(a,`${n} px`,x,540);for(let b=0;b<2;b++)img(a,base+'.png',x+10+b*80,575,n,['#14181f','#8c96a3'][b]);}a.push('-quality','96',`${rev}/${j.name}.delivery.before-after.jpg`);run(a);
 const choice={...j,base,nameFinal:j.name.split('.')[0],metrics,brightness:j.dir==='parts'?0.944:1};choices.push(choice);
}
put('docs/codex-queue/240/selection.json',JSON.stringify(choices,null,2)+'\n');
console.log(JSON.stringify(choices.map(j=>({name:j.name,metrics:j.metrics.map(m=>({n:m.n,luma:m.luma,dark:m.deltaDark,semi16:m.semi16,semi127:m.semi127,key:m.keyLeakPct}))})),null,2));
