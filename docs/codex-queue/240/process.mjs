import fs from 'node:fs';
import {root,rev,run,put,rgba,box,matte,measure,txt,img} from './core.mjs';
const jobs=[...JSON.parse(fs.readFileSync('docs/codex-queue/240/jobs.json')),...JSON.parse(fs.readFileSync('docs/codex-queue/240/jobs-retries.json')),JSON.parse(fs.readFileSync('docs/codex-queue/240/job-station2.json')),JSON.parse(fs.readFileSync('docs/codex-queue/240/job-station3.json'))];
for (const job of jobs){
 const source=`${root}/ui/${job.dir}/${job.name}.png`,base=`${rev}/${job.name}.post`;
 if(fs.existsSync(`${base}.png`))continue;
 const n=Number(run(['identify','-format','%w',source]).toString()),input=rgba(source);let r=Buffer.from(input),endpoints=0;
 for(let i=3;i<r.length;i+=4){const a=r[i],b=a<=16?0:a>=250?255:a;if(b!==a){r[i]=b;endpoints++;}}
 const b=box(r,n),resized=run(['-size',`${n}x${n}`,'-depth','8','rgba:-','-crop',`${b.w}x${b.h}+${b.x}+${b.y}`,'+repage','-filter','Lanczos','-resize','717x717','-background','none','-gravity','center','-extent','1024x1024','-depth','8','rgba:-'],r);
 const cleaned=matte(resized,1024);run(['-size','1024x1024','-depth','8','rgba:-','-colorspace','sRGB','PNG32:'+`${base}.png`],cleaned.r);
 const prompt=fs.readFileSync(`${root}/ui/${job.dir}/${job.name}.prompt.txt`);put(`${base}.prompt.txt`,prompt);
 const metrics=[{...measure(cleaned.r,1024),matte:cleaned.audit}];
 for(const size of [256,128,64]){const down=rgba(`${base}.png`,size),c=matte(down,size);run(['-size',`${size}x${size}`,'-depth','8','rgba:-','-colorspace','sRGB','PNG32:'+`${base}.${size}.png`],c.r);put(`${base}.${size}.prompt.txt`,prompt);metrics.push({...measure(c.r,size),matte:c.audit});}
 const sizes=job.dir==='parts'?[10,15,20,30]:[20,24,30,36];
 for(const size of sizes)metrics.push(measure(rgba(`${base}.png`,size),size));
 put(`${rev}/${job.name}.metrics.json`,JSON.stringify({name:job.name,source,originalSize:n,endpointPixels:endpoints,sourceBBox:b,metrics},null,2)+'\n');
 const a=['-size','1120x720','xc:#232831'];txt(a,`${job.name} · bản sinh | bản hậu kỳ`,18,12,22);img(a,source,20,50,400,'#14181f');img(a,`${base}.png`,560,50,400,'#14181f');txt(a,'Bản sinh: toàn bộ canvas',20,460);txt(a,'Hậu kỳ: vật 70%, giữ màu RGB',560,460);txt(a,'Cỡ thật · than chì #14181f / thép sáng #8c96a3',20,505,18);
 for(let i=0;i<sizes.length;i++){const size=sizes[i],x=20+i*270;txt(a,`${size} px`,x,540);for(let j=0;j<2;j++)img(a,`${base}.png`,x+10+j*80,575,size,['#14181f','#8c96a3'][j]);}a.push('-quality','96',`${rev}/${job.name}.before-after.jpg`);run(a);
 console.log(JSON.stringify({name:job.name,metrics:metrics.map(x=>({n:x.n,box:x.bbox,dark:x.deltaDark,luma:x.luma,semi16:x.semi16,semi127:x.semi127,matte:x.matte}))}));
}
