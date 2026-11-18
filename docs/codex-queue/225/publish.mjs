// Chỉ công bố file mới; bản 512 thu thẳng từ bản cắt, núm thu từ bản 1024.
import fs from 'node:fs';
import {execFileSync as run} from 'node:child_process';
const [game,name,attempt,revision='edge']=process.argv.slice(2),M='/opt/homebrew/bin/magick';
if(!['dragon-hold','typing-defense','typing-survival'].includes(game)||!['slider-track','slider-thumb'].includes(name))throw Error('Sai đích');
const tmp=`games/${game}/tmp/codex-225`,base=`games/${game}/art-src/ui/quick-settings/sliders`,tag=`${name}.try${attempt}.${revision}`;
const src=`${tmp}/${tag}.clean.processed.png`,dst=`${base}/${name}.png`;
fs.copyFileSync(src,dst,fs.constants.COPYFILE_EXCL);
const prompt=fs.readFileSync(`${base}/${name}.try${attempt}.prompt.txt`);
fs.writeFileSync(`${base}/${name}.prompt.txt`,prompt,{flag:'wx'});
for(const s of name==='slider-track'?[512]:[256,128,64]){
 const p=`${tmp}/${tag}.${s}.processed.png`;
 if(fs.existsSync(p))throw Error('Giữ file có sẵn '+p);
 const input=name==='slider-track'?`${tmp}/${tag}.crop.png`:dst;
 run(M,[input,'-filter','Lanczos','-resize',name==='slider-track'?'512x32!':`${s}x${s}!`,'-depth','8','-define','png:color-type=6',p]);
 run(process.execPath,['docs/codex-queue/225/repair.mjs',game,name,attempt,revision,String(s)],{stdio:'inherit'});
 fs.copyFileSync(`${tmp}/${tag}.${s}.clean.processed.png`,`${base}/${name}.${s}.png`,fs.constants.COPYFILE_EXCL);
 fs.writeFileSync(`${base}/${name}.${s}.prompt.txt`,prompt,{flag:'wx'});
}
const out='docs/codex-queue/225/selected.json';
const list=fs.existsSync(out)?JSON.parse(fs.readFileSync(out)):[];
list.push({game,name,tryNumber:+attempt,source:`${base}/${name}.try${attempt}.png`,selected:dst,postprocess:`docs/codex-queue/225/postprocess-${game}-${name}.try${attempt}.edge.json`,brightness:revision==='bright8'?1.08:1});
fs.writeFileSync(out,JSON.stringify(list,null,2)+'\n');
