import fs from 'node:fs';import {im,D,json} from './lib.mjs';
const rs=JSON.parse(fs.readFileSync(`${D}/processed.json`)),jobs=JSON.parse(fs.readFileSync(`${D}/prompts.json`)),files=[];
function write(p,b){if(fs.existsSync(p)){if(fs.readFileSync(p).equals(Buffer.from(b)))return;throw new Error('Giữ file đã có: '+p);}fs.writeFileSync(p,b,{flag:'wx'});files.push(p);}
for(const r of rs){const base=`games/${r.game}/art-src/ui/quick-settings`,name=r.name+(r.type==='icon'&&r.name!=='vol-keyboard-volume'?'.r2':''),dir=r.type==='icon'?`${base}/selected`:`${base}/sliders`,prompt=jobs[r.job].prompt;
 for(const o of r.outputs){const s=o.size[0],dest=`${dir}/${name}${s===1024?'':'.'+s}.png`;write(dest,fs.readFileSync(o.file));write(dest.replace(/\.png$/,'.prompt.txt'),prompt);}
}
json(`${D}/delivered.json`,rs.map(r=>({game:r.game,name:r.name,job:r.job,source:r.src,status:r.type==='slider'&&r.game!=='dragon-hold'?'chưa đạt — giữ bản tốt nhất sau 3 lượt':'chờ Claude chấm lại',files:r.outputs.map(o=>{const s=o.size[0];return `games/${r.game}/art-src/ui/quick-settings/${r.type==='icon'?'selected':'sliders'}/${r.name}${r.type==='icon'&&r.name!=='vol-keyboard-volume'?'.r2':''}${s===1024?'':'.'+s}.png`;})})));
fs.writeFileSync(`${D}/identify.txt`,im(['identify','-format','%f %wx%h %[channels]\n',...JSON.parse(fs.readFileSync(`${D}/delivered.json`)).flatMap(r=>r.files)]));console.log('Đã chép bản chọn, giữ nguyên file cũ.');
