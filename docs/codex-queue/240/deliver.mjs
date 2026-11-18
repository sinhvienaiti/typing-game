import fs from 'node:fs';import crypto from 'node:crypto';
import {root,rev,run,txt,img} from './core.mjs';
const jobs=JSON.parse(fs.readFileSync('docs/codex-queue/240/selection.json'));
const before=JSON.parse(fs.readFileSync(rev+'/md5-before.json'));
const md5=p=>crypto.createHash('md5').update(fs.readFileSync(p)).digest('hex');
const targets=[];
for(const j of jobs)for(const ext of ['.png','.256.png','.128.png','.64.png','.prompt.txt','.256.prompt.txt','.128.prompt.txt','.64.prompt.txt']){
 const target=`${root}/ui/${j.dir}/${j.nameFinal}${ext}`;
 if(fs.existsSync(target)&&md5(target)!==before[target])throw Error('File changed concurrently: '+target);
 targets.push({source:j.base+ext,target});
}
// Back up every existing final before writing any final.
for(const {target} of targets)if(fs.existsSync(target)){
 const backup=rev+'/prev/'+target.slice(root.length+1);fs.mkdirSync(backup.slice(0,backup.lastIndexOf('/')),{recursive:true});fs.copyFileSync(target,backup,fs.constants.COPYFILE_EXCL);if(md5(backup)!==before[target])throw Error('Backup mismatch');
}
for(const {source,target} of targets)fs.copyFileSync(source,target);
fs.writeFileSync(rev+'/delivery-targets.json',JSON.stringify(targets,null,2)+'\n',{flag:'wx'});
for(const j of jobs){
 const a=['-size','1120x720','xc:#232831'];txt(a,`${j.name} · bản sinh | bản chốt`,18,12,22);img(a,`${root}/ui/${j.dir}/${j.name}.png`,20,50,400,'#14181f');img(a,`${root}/ui/${j.dir}/${j.nameFinal}.png`,560,50,400,'#14181f');txt(a,'Bản sinh: toàn bộ canvas',20,460);txt(a,j.dir==='parts'?'Căn vỏ theo mag-full; giảm sáng toàn ảnh 5,6%':'Vật 70%; giữ màu RGB; bản thu Lanczos trực tiếp',560,460);txt(a,'Cỡ thật · than chì #14181f / thép sáng #8c96a3',20,505,18);
 const sizes=j.dir==='parts'?[10,15,20,30]:[20,24,30,36];for(let i=0;i<sizes.length;i++){const n=sizes[i],x=20+i*270;txt(a,`${n} px`,x,540);for(let b=0;b<2;b++)img(a,`${root}/ui/${j.dir}/${j.nameFinal}.png`,x+10+b*80,575,n,['#14181f','#8c96a3'][b]);}a.push('-quality','96',`${rev}/${j.nameFinal}-before-after.jpg`);run(a);
}
console.log('Delivered '+targets.length+' files; backups verified before replacement.');
