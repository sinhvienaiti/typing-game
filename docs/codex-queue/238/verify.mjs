import fs from 'node:fs';import cp from 'node:child_process';
const root='games/typing-survival/art-src',rev=`${root}/_review/238`;
const before=JSON.parse(fs.readFileSync(`${rev}/md5-before.json`));
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(`${d}/${e.name}`):[`${d}/${e.name}`]);
const paths=['ui/icons','ui/foes'].flatMap(d=>walk(`${root}/${d}`)).sort();
const md5=p=>cp.execFileSync('/sbin/md5',['-r',p],{encoding:'utf8'}).split(' ')[0];
const after=Object.fromEntries(paths.map(p=>[p,md5(p)]));
const added=paths.filter(p=>!before[p]),modified=paths.filter(p=>before[p]&&before[p]!==after[p]),missing=Object.keys(before).filter(p=>!after[p]);
const allowed=new Set([['icons','objective'],['icons','station-crest'],['icons','shard'],['foes','shard']].flatMap(([d,n])=>['.png','.64.png','.128.png','.256.png','.prompt.txt'].map(ext=>`${root}/ui/${d}/${n}${ext}`)));
const unapprovedChanges=modified.filter(p=>!allowed.has(p));
const protectedPaths=Object.keys(before).filter(p=>!allowed.has(p));
const backups=modified.map(p=>({file:p,pass:fs.existsSync(`${rev}/prev/${p.slice(root.length+1)}`)&&md5(`${rev}/prev/${p.slice(root.length+1)}`)===before[p]}));
const finals=[];
for(const [folder,name,attempt] of [['icons','objective',2],['icons','station-crest',3],['icons','shard',2],['foes','shard',2]]){
 const stem=`${root}/ui/${folder}/${name}`;
 const promptMatches=fs.readFileSync(`${stem}.prompt.txt`).equals(fs.readFileSync(`${root}/ui/icons/${name}.try${attempt}.prompt.txt`));
 for(const n of [1024,256,128,64]){
  const ext=n===1024?'':'.'+n,file=stem+ext+'.png';
  const identify=cp.execFileSync('/opt/homebrew/bin/magick',['identify','-format','%w %h %[channels] %[colorspace]',file],{encoding:'utf8'});
  const equalsPost=fs.readFileSync(file).equals(fs.readFileSync(`${rev}/${name}.try${attempt}.post${ext}.png`));
  const metric=JSON.parse(fs.readFileSync(`${rev}/${name}.try${attempt}.metrics.json`)).metrics.find(m=>m.n===n);
  const pass=identify.startsWith(`${n} ${n} srgba`)&&identify.endsWith('sRGB')&&equalsPost&&promptMatches&&metric.semi16===0&&metric.semi127===0&&metric.keyLeakPct<=.2;
  finals.push({file,n,identify,equalsPost,promptMatches,pass});
 }
}
const shardMirror=['','.64','.128','.256'].every(ext=>fs.readFileSync(`${root}/ui/icons/shard${ext}.png`).equals(fs.readFileSync(`${root}/ui/foes/shard${ext}.png`)));
const iou=JSON.parse(fs.readFileSync(`${rev}/iou-delivery.json`));
const summary={before:Object.keys(before).length,after:paths.length,added,modified,missing,unapprovedChanges,protectedCount:protectedPaths.length,protectedUnchanged:protectedPaths.every(p=>after[p]===before[p]),backups,finals,shardMirror,iouPass:iou.pass,pass:!missing.length&&!unapprovedChanges.length&&backups.every(x=>x.pass)&&finals.every(x=>x.pass)&&shardMirror&&iou.pass};
if(process.argv.includes('--save')){for(const [p,s] of [[`${rev}/md5-after.json`,JSON.stringify(after,null,2)+'\n'],[`${rev}/md5-after.txt`,paths.map(p=>`${after[p]} ${p}\n`).join('')],[`${rev}/validation-delivery.json`,JSON.stringify(summary,null,2)+'\n']])fs.writeFileSync(p,s,{flag:'wx'});}
console.log(JSON.stringify({...summary,added:added.length,modified:modified.length,backups:backups.length,finals:finals.length},null,2));if(!summary.pass)process.exitCode=1;
