import fs from 'node:fs';
import {root,rev,run,rgba,box,matte,measure} from './core.mjs';
const tag=process.argv[2];if(!tag||!/^[a-z0-9-]+$/.test(tag))throw Error('Cần nhãn đầu ra mới: node docs/codex-queue/240/replay.mjs <nhãn>');
const out=rev+'/replay-'+tag;if(fs.existsSync(out))throw Error('Thư mục đã có; dùng nhãn mới');fs.mkdirSync(out);
const jobs=JSON.parse(fs.readFileSync('docs/codex-queue/240/selection.json')),results=[];
for(const j of jobs){const source=`${root}/ui/${j.dir}/${j.name}.png`,n=Number(run(['identify','-format','%w',source]).toString());let r=rgba(source);for(let k=3;k<r.length;k+=4)r[k]=r[k]<=16?0:r[k]>=250?255:r[k];const b=box(r,n);
 const scaled=run(['-size',`${n}x${n}`,'-depth','8','rgba:-','-crop',`${b.w}x${b.h}+${b.x}+${b.y}`,'+repage','-filter','Lanczos','-resize','717x717','-background','none','-gravity','center','-extent','1024x1024','-depth','8','rgba:-'],r),m=matte(scaled,1024),post=out+'/'+j.name+'.post.png';run(['-size','1024x1024','-depth','8','rgba:-','-colorspace','sRGB','PNG32:'+post],m.r);
 fs.copyFileSync(`${root}/ui/${j.dir}/${j.name}.prompt.txt`,post.replace(/\.png$/,'.prompt.txt'));
 const master=out+'/'+j.nameFinal+'.png';if(j.dir==='parts'){const b=box(m.r,1024);run([post,'-crop',`${b.w}x${b.h}+${b.x}+${b.y}`,'+repage','-filter','Lanczos','-resize','233x716!','-gravity','center','-background','none','-extent','1024x1024','-channel','RGB','-evaluate','Multiply','0.944','+channel','PNG32:'+master]);}else fs.copyFileSync(post,master);
 for(const size of [1024,256,128,64]){const p=size===1024?master:out+'/'+j.nameFinal+'.'+size+'.png';if(size!==1024)run([master,'-filter','Lanczos','-resize',`${size}x${size}!`,'-colorspace','sRGB','PNG32:'+p]);fs.copyFileSync(`${root}/ui/${j.dir}/${j.name}.prompt.txt`,p.replace(/\.png$/,'.prompt.txt'));const actual=`${root}/ui/${j.dir}/${j.nameFinal}`+(size===1024?'':'.'+size)+'.png';results.push({file:p,pixelsEqualFinal:rgba(p).equals(rgba(actual)),metrics:measure(rgba(p),size)});}}
fs.writeFileSync(out+'/comparison.json',JSON.stringify(results,null,2));console.log(JSON.stringify({out,files:results.length,pixelsEqualFinal:results.every(x=>x.pixelsEqualFinal)}));
