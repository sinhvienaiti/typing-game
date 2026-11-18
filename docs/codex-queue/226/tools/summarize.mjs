// Phiếu 226. Node thuần; đầu vào bất biến: runs/ và old-runs/. Không chạy sim.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const D=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=n=>fs.readFileSync(path.join(D,n),'utf8');
const bots=['novice','steady','standard','skilled','sloppy','fast'];
const labels={child:'Trẻ em',novice:'Mới',steady:'Chậm chắc',standard:'Chuẩn',skilled:'Khá',sloppy:'Ẩu',fast:'Nhanh','no-type':'Không gõ'};
const modes={balanced:'Cân bằng',relax:'Thư giãn',challenge:'Thử thách'};
const clean=s=>s.replaceAll('**','').trim();
const split=l=>l.trim().slice(1,-1).split('|').map(s=>s.trim());
function tables(text){
 const lines=text.split('\n'),res=[];
 for(let i=0;i<lines.length-1;i++)if(lines[i].startsWith('|')&&/^\|[-:| ]+\|$/.test(lines[i+1])){
  const header=split(lines[i]),rows=[];i+=2;
  while(i<lines.length&&lines[i].startsWith('|'))rows.push(split(lines[i++]));
  res.push({header,rows});i--;
 }
 return res;
}
const table=(text,pred)=>{const t=tables(text).find(t=>pred(t.header));if(!t)throw Error('Không thấy bảng');return t;};
const pct=m=>m<100&&m%10!==0?(m/10).toFixed(1)+' %':Math.round(m/10)+' %';
const milli=(k,n)=>Math.round(k*1000/n);
function infer(s,n){const a=Array.from({length:n+1},(_,k)=>k).filter(k=>pct(milli(k,n))===clean(s));if(a.length!==1)throw Error(`Không duy nhất ${s} / ${n}: ${a}`);return a[0];}
const numbers=s=>[...s.replaceAll(',','.').matchAll(/[-+]?\d+(?:\.\d+)?/g)].map(m=>+m[0]);
function g12(text){return table(text,h=>h[0]==='Cổng').rows.map((r,i)=>({key:r[0]+(i>5?' '+['Thư giãn','Thử thách','Học'][i-6]:''),description:r[1],target:r[2],value:r[3],status:clean(r[4]),...(i===0?{lives:numbers(r[3]),minimum:Math.min(...numbers(r[3])),minimum_seeds:numbers(r[3]).flatMap((v,i)=>v===Math.min(...numbers(r[3]))?[i+1]:[])}:{})}));}
function extract(c){
 const s=read(`runs/${c}-balance160.md`),ts=tables(s);
 const tight=table(s,h=>h[2]?.startsWith('Thắng bộ')).rows;
 const tight6=bots.map(bot=>{
  const r=tight.find(r=>r[0]==='Cân bằng'&&r[1]===bot),w=r[2].split(' / '),ss=r[3].split(' / ');
  const wins=[infer(w[0],80),infer(w[1],80)];wins.push(wins[0]+wins[1]);
  const mil=wins.map((k,i)=>milli(k,i===2?160:80));
  const sPct=ss.map(x=>numbers(x)[0]);
  const winPass=mil[2]>=780&&mil[2]<=880,sPass=sPct[2]>=(bot==='standard'?40:35)&&sPct[2]<=(bot==='standard'?60:65);
  const printPass=!r[5].includes('trượt');
  if(pct(mil[2])!==w[2]||(winPass&&sPass)!==printPass)throw Error('Lệch tái tính '+c+bot);
  return {bot,label:labels[bot],printed_win:w,wins,milli:mil,s_printed:ss,s_percent:sPct,win_pass:winPass,s_pass:sPass,pass:winPass&&sPass,printed_verdict:r[5],upper_to_fail:141-wins[2],lower_to_fail:wins[2]-124,nearest_to_fail:Math.min(141-wins[2],wins[2]-124),recheck:true};
 });
 const gates=ts.filter(t=>t.header[0]==='#'&&t.header[1]==='Cổng').map(t=>t.rows.map(r=>({id:r[0],name:r[1],status:r[2],details:r[3],failures:r[3].split('; ').filter(s=>s.startsWith('✗')),raw:'| '+r.join(' | ')+' |'})));
 if(gates.length!==3)throw Error('Số bảng B: '+gates.length);
 const offPrinted=gates.map(gs=>{const m=gs.find(g=>g.id==='B7').details.match(/standard · tắt nhịp: Thắng ([\d.]+ %), Biên S ([\d.]+ %)/);if(!m)throw Error('Thiếu hàng B7 tắt nhịp');return {win:m[1],s:m[2]};});
 const offWins=[infer(offPrinted[0].win,80),infer(offPrinted[1].win,80)];offWins.push(offWins[0]+offWins[1]);
 const directorOff={printed:offPrinted,wins:offWins,milli:offWins.map((k,i)=>milli(k,i===2?160:80)),pass:offWins[2]>=125&&offWins[2]<=140};
 if(pct(directorOff.milli[2])!==offPrinted[2].win)throw Error('Lệch pct B7');
 const boss=ts.filter(t=>t.header[2]==='Tới boss').at(-1).rows.filter(r=>r[0]==='Cân bằng'&&bots.includes(r[1])).map(r=>({bot:r[1],reached:r[2],retreat:r[3],engage_p50:r[5],lives_lost_peak_p50:r[7],raw:r}));
 const bossLines=s.split('\n').filter(l=>l.startsWith('G3 ('));
 const r2=s.split('\n').find(l=>l.startsWith('R2 gộp:'));
 const wide=s.split('\n').find(l=>l.startsWith('Để so, B1'));
 const challenge=tight.filter(r=>r[0]==='Thử thách').map(r=>{let w=r[2].split(' / '),k=[infer(w[0],80),infer(w[1],80)];return {bot:r[1],printed:w,wins:[...k,k[0]+k[1]],milli:milli(k[0]+k[1],160)};});
 const phases={},phaseOutcomes={};
 for(const m of Object.keys(modes)){
  const p=read(`runs/${c}-pn-${m}.md`),pt=tables(p);
  phases[m]=pt[0].rows.map(r=>({bot:r[1],phase:r[2],duration:r[3],typing:r[4],p:r[5],i:r[6],o:r[7],n:r[8],q:r[9],kills:r[10],lives_lost:r[11],defeats:r[12],raw:r}));
  phaseOutcomes[m]=pt[1].rows.map(r=>({bot:r[1],survived4:r[2],wins5:r[3],s:r[4],n:r[5],raw:r}));
 }
 const night1={};
 for(const n of [40,160])night1[n]=tables(read(`runs/${c}-night1-${n}.md`))[0].rows.map(r=>({bot:r[0],lives_lost:r[7],games_lost_at_least3:+r[8],raw:r}));
 return {tight:tight6,gates,directorOff,boss,bossLines,r2,wide,g12_5:g12(s),g12_20:g12(read(`runs/${c}-g12x20.md`)),phases,phaseOutcomes,night1,challenge};
}
const summary={ticket:226,refs:read('runs/refs.txt').trim().split('\n'),patch_sha256:'66b61fbd73cfefe7533d0c6348822556b4b9c90c54ec37c3ae015553908e11aa',base:extract('base'),pkg:extract('pkg'),commands:JSON.parse(read('runs/commands.json')),win_rechecks:{checked:12,matched:12},known:[]};
// So từng ô; số ván thắng phải khớp chính xác. Các ô pha so toàn bộ, không chỉ các hàng trích báo cáo.
function compare(group,id,a,b,unit='khác',threshold=0){
 const na=numbers(a),nb=numbers(b);let delta=0;
 const shape=na.length===nb.length;
 if(shape&&na.length)delta=Math.max(...na.map((v,i)=>Math.abs(v-nb[i])));
 const exact=clean(a)===clean(b);
 const match=exact||(shape&&na.length>0&&delta<=threshold+1e-9);
 summary.known.push({group,id,old:b,current:a,unit,delta:shape?delta:null,threshold,exact,match});
}
for(const c of ['base','pkg']){
 const old=c==='base'?'r22':'v2',s=read(`old-runs/${old}-balance.md`),oldT=table(s,h=>h[2]?.startsWith('Thắng bộ')).rows;
 for(const bot of bots){
  const r=oldT.find(r=>r[0]==='Cân bằng'&&r[1]===bot),w=r[2].split(' / '),oldK=infer(w[0],40)+infer(w[1],40),cur=summary[c].tight.find(r=>r.bot===bot);
  if(pct(milli(oldK,80))!==w[2])throw Error('Tái tính bảng cũ hỏng');
  compare(c+' M1 1–80',bot+' thắng',String(cur.wins[0]),String(oldK),'ván',0);
  compare(c+' M1 1–80',bot+' S',cur.s_printed[0],r[3].split(' / ')[2],'điểm %',0.5);
 }
 for(const [n,oldName] of [[5,old+'-balance.md'],[20,(c==='base'?'r22':'v1')+'-g12x20.md']]){
  const oldG=g12(read('old-runs/'+oldName));
  for(let i=0;i<oldG.length;i++){
   const a=summary[c]['g12_'+n][i],b=oldG[i],unit=a.key.startsWith('5a')?'giây':a.key.startsWith('5')||a.key==='7'?'điểm %':a.key==='4'?'mạng':'khác',threshold=unit==='giây'||unit==='mạng'?0.05:unit==='điểm %'?0.5:0;
   compare(c+' §12 '+n,a.key,a.value,b.value,unit,threshold);
   compare(c+' §12 '+n,a.key+' kết quả',a.status,b.status);
  }
 }
 for(const m of Object.keys(modes)){
  const oldP=tables(read(`old-runs/${c==='base'?'r22':'v1'}-pn-${m}.md`));
  const phaseCount=summary[c].phases[m].filter(r=>c==='base'||r.phase!=='Đêm 5').length;
  if(phaseCount!==oldP[0].rows.filter(r=>c==='base'||r[2]!=='Đêm 5').length)throw Error('Thiếu hàng pha '+c+m);
  for(const r of summary[c].phases[m]){
   if(c==='pkg'&&r.phase==='Đêm 5')continue;
   const oldRow=oldP[0].rows.find(x=>x[1]===r.bot&&x[2]===r.phase);if(!oldRow)throw Error('Thiếu hàng cũ');
   for(let i=3;i<r.raw.length;i++){
    const unit=i===3?'giây':[4,5,6,7,9].includes(i)?'điểm %':i===11?'mạng':'khác';
    compare(c+' M3 '+m,r.bot+' '+r.phase+' '+oldP[0].header[i],r.raw[i],oldRow[i],unit,unit==='điểm %'?0.5:unit==='giây'||unit==='mạng'?0.05:0);
   }
  }
  if(c==='base')for(const r of summary[c].phaseOutcomes[m]){
   const o=oldP[1].rows.find(x=>x[1]===r.bot);
   for(let i=2;i<r.raw.length;i++)compare(c+' M3 kết ải '+m,r.bot+' '+oldP[1].header[i],r.raw[i],o[i],i<=4?'điểm %':'khác',i<=4?0.5:0);
  }
 }
 const oldN=tables(read('old-runs/'+(c==='base'?'base':'v1')+'-night1.md'))[0];
 if(summary[c].night1[40].length!==oldN.rows.length||summary[c].night1[160].length!==oldN.rows.length)throw Error('Thiếu hàng Đêm 1');
 for(const r of summary[c].night1[40]){
  const o=oldN.rows.find(x=>x[0]===r.bot);
  for(let i=1;i<r.raw.length;i++){
   const unit=i===7?'mạng':[3,4,9,10].includes(i)?'giây':i===11?'điểm %':'khác';
   compare(c+' M4 40',r.bot+' '+oldN.header[i],r.raw[i],o[i],unit,unit==='điểm %'?0.5:unit==='giây'||unit==='mạng'?0.05:0);
  }
 }
}
summary.known_stats={cells:summary.known.length,matched:summary.known.filter(x=>x.match).length,mismatched:summary.known.filter(x=>!x.match).length,exact:summary.known.filter(x=>x.exact).length,max_delta:Object.fromEntries(['giây','điểm %','mạng','ván','khác'].map(u=>[u,Math.max(0,...summary.known.filter(x=>x.unit===u).map(x=>x.delta??0))]))};
const out=[];const emit=s=>out.push(s);const fmt=v=>String(v??'—').replaceAll('|','\\|');
function md(headers,rows){emit('| '+headers.map(fmt).join(' | ')+' |\n|'+headers.map(()=>'---').join('|')+'|\n'+rows.map(r=>'| '+r.map(fmt).join(' | ')+' |').join('\n')+'\n');}
emit('# Phiếu 226 · Bảng số\n');
emit('## Đối chiếu số cũ (đọc trước so base → pkg)\n');
emit(`So ${summary.known_stats.cells} ô: ${summary.known_stats.matched} khớp ngưỡng, ${summary.known_stats.exact} khớp nguyên văn, ${summary.known_stats.mismatched} lệch. Lệch lớn nhất: ${JSON.stringify(summary.known_stats.max_delta)}. Chi tiết từng ô nằm trong summary.json, trường known.\n`);
const groups=[...new Set(summary.known.map(x=>x.group))];md(['Nhóm','Ô so','Khớp','Lệch','Lệch lớn nhất'],groups.map(g=>{let a=summary.known.filter(x=>x.group===g);return[g,a.length,a.filter(x=>x.match).length,a.filter(x=>!x.match).length,Math.max(...a.map(x=>x.delta??0))];}));
for(const x of summary.known.filter(x=>!x.match))emit(`- **Lệch ${x.group}, ${x.id}:** cũ ${x.old}; nay ${x.current}; Δ ${x.delta} ${x.unit}.\n`);
emit('## Dải chặt Cân bằng\n');
emit('Số ván suy duy nhất từ ô in của từng bộ 80 seed, cộng hai bộ rồi tính Math.round(k × 1000 / 160), dùng đúng pct của mã. Mỗi ô ghi ván / tổng, ‰, rồi % in. Biên S giữ ô in bộ 1 / bộ 2 / gộp. Đích gộp thắng 780–880 ‰, tức 125–140/160; S Chuẩn 40–60 %, bot khác 35–65 %. “Cách mép” là số kết quả thắng/thua tối thiểu phải đảo để bắt đầu trượt dải thắng; không áp cho S.\n');
function wf(r,i){return `${r.wins[i]}/${i===2?160:80}; ${r.milli[i]} ‰ (${r.printed_win[i]})`;}
for(const part of [['Thắng bộ 1',0],['Thắng bộ 2',1],['Thắng gộp',2]])md(['Bot',`base · ${part[0]}`,`pkg · ${part[0]}`],bots.map((b,i)=>[labels[b],wf(summary.base.tight[i],part[1]),wf(summary.pkg.tight[i],part[1])]));
md(['Bot','base · S 1 / 2 / gộp','pkg · S 1 / 2 / gộp','base · kết quả; cách mép','pkg · kết quả; cách mép'],bots.map((b,i)=>{let a=summary.base.tight[i],p=summary.pkg.tight[i];const edge=r=>r.win_pass?`${r.pass?'Đạt':'TRƯỢT S'}; dưới ${r.lower_to_fail}, trên ${r.upper_to_fail} ván`:`TRƯỢT thắng; cần ${r.wins[2]>140?r.wins[2]-140:125-r.wins[2]} ván đảo để về dải`;return[labels[b],a.s_printed.join(' / '),p.s_printed.join(' / '),edge(a),edge(p)];}));
emit('Kiểm lại 12/12 ô thắng gộp: số bộ 1 + bộ 2, pct của ‰ gộp và đạt/trượt gồm S đều khớp báo cáo.\n');
emit('## B1–B8, B9\n');
md(['Cổng','base · bộ 1','pkg · bộ 1','base · bộ 2','pkg · bộ 2','base · gộp','pkg · gộp'],Array.from({length:9},(_,i)=>['B'+(i+1),...['base','pkg'].map(c=>summary[c].gates[0][i].status),...['base','pkg'].map(c=>summary[c].gates[1][i].status),...['base','pkg'].map(c=>summary[c].gates[2][i].status)]));
emit('Bộ 1 seed 1–80, bộ 2 seed 81–160 chấm BALANCE §3; gộp chấm đích chặt. B9 **THIẾU SỐ**, cần người thật chơi. Các cổng trượt dưới đây chép nguyên câu số đo trong báo cáo:\n');
for(const c of ['base','pkg'])for(let i=0;i<3;i++)for(const g of summary[c].gates[i].filter(g=>g.status.includes('TRƯỢT'))){emit(`### ${c}, ${['bộ 1','bộ 2','gộp'][i]}, ${g.id}\n`);emit(g.details+'\n');}
md(['base · dải rộng gộp','pkg · dải rộng gộp'],[[summary.base.wide,summary.pkg.wide]]);
emit('B7 có thêm hàng Chuẩn tắt bộ điều nhịp; tái tính số ván từ hai bộ 80 để giải thích cổng trượt cả khi ô gộp in 88 %:\n');
md(['Cây','Thắng bộ 1','Thắng bộ 2','Thắng gộp','Biên S gộp','Đích thắng chặt'],['base','pkg'].map(c=>{const r=summary[c].directorOff;return[c,`${r.wins[0]}/80 (${r.printed[0].win})`,`${r.wins[1]}/80 (${r.printed[1].win})`,`${r.wins[2]}/160; ${r.milli[2]} ‰ (${r.printed[2].win})`,r.printed[2].s,r.pass?'Đạt':'TRƯỢT'];}));
emit('## Boss gộp, Cân bằng\n');
md(['Bot','base · boss rút','pkg · boss rút','base · giao chiến p50 (s)','pkg · giao chiến p50 (s)','base · mạng mất đỉnh p50','pkg · mạng mất đỉnh p50'],bots.map(b=>{let a=summary.base.boss.find(x=>x.bot===b),p=summary.pkg.boss.find(x=>x.bot===b);return[labels[b],a.retreat,p.retreat,a.engage_p50,p.engage_p50,a.lives_lost_peak_p50,p.lives_lost_peak_p50];}));
md(['Cây','G3 / G8 · bộ 1, bộ 2, gộp'],['base','pkg'].map(c=>[c,summary[c].bossLines.at(-1)]));
md(['Cây','R2 gộp · G2, G5, G6 (nguyên dòng)'],['base','pkg'].map(c=>[c,summary[c].r2]));
for(const n of [20,5]){
 emit(`## §12 trên ${n} seed\n`);
 md(['Cổng','Đích','base · số','base · kết quả','pkg · số','pkg · kết quả'],summary.base['g12_'+n].map((a,i)=>{let p=summary.pkg['g12_'+n][i];return[a.key,a.target,a.value,a.status,p.value,p.status];}));
 md(['Cổng 4','base','pkg'],[['Thấp nhất; seed',...['base','pkg'].map(c=>{let r=summary[c]['g12_'+n][0];return r.minimum+' mạng; seed '+r.minimum_seeds.join(', ');})]]);
}
emit('## Đêm 1 · mạng mất · seed 25–48\n');
md(['Chế độ','Bot','base','pkg'],Object.keys(modes).flatMap(m=>summary.base.phases[m].filter(r=>r.phase==='Đêm 1').map(a=>[modes[m],labels[a.bot],a.lives_lost,summary.pkg.phases[m].find(x=>x.bot===a.bot&&x.phase===a.phase).lives_lost])));
emit('## Đêm 1 · Cân bằng · seed 1–40 và 1–160\n');
md(['Seed','Bot','base · mạng mất','pkg · mạng mất','base · ván mất ≥ 3','pkg · ván mất ≥ 3'],[40,160].flatMap(n=>summary.base.night1[n].map((a,i)=>{let p=summary.pkg.night1[n][i];return['1–'+n,labels[a.bot],a.lives_lost,p.lives_lost,a.games_lost_at_least3,p.games_lost_at_least3];})));
emit('## Đêm 3 · Nhàn I · seed 25–48\n');
md(['Chế độ','Bot','base','pkg'],Object.keys(modes).flatMap(m=>summary.base.phases[m].filter(r=>r.phase==='Đêm 3').map(a=>[modes[m],labels[a.bot],a.i,summary.pkg.phases[m].find(x=>x.bot===a.bot&&x.phase===a.phase).i])));
emit('## Kết ải của đầu dò từng pha · seed 25–48\n');
md(['Chế độ','Bot','base · qua 4 đêm / thắng 5 / S','pkg · qua 4 đêm / thắng 5 / S'],Object.keys(modes).flatMap(m=>summary.base.phaseOutcomes[m].map((a,i)=>{let p=summary.pkg.phaseOutcomes[m][i];return[modes[m],labels[a.bot],[a.survived4,a.wins5,a.s].join(' / '),[p.survived4,p.wins5,p.s].join(' / ')];})));
emit('## Thử thách · thắng gộp 160 ván\n');
md(['Bot','base · ván / 160; ‰; % in','pkg · ván / 160; ‰; % in'],summary.base.challenge.map((a,i)=>{let p=summary.pkg.challenge[i];const f=r=>`${r.wins[2]}/160; ${r.milli} ‰; ${r.printed[2]}`;return[labels[a.bot]??a.bot,f(a),f(p)];}));
emit('## Thời gian, luồng, tải\n');
emit('Chạy tuần tự toàn bộ. Mọi lệnh gọi nice -n 15 nhưng sandbox từ chối setpriority ở cả 16 lệnh; không xác nhận được ưu tiên thực nice 15. TMPDIR trong bản chép. Sandbox chặn sysctl và ps; timeline giữ nguyên lỗi sysctl, tải lấy từ uptime, cùng số tải 1 phút. Không kiểm được tiến trình balance.ts của làn khác; phiếu chỉ chạy một lệnh tại mỗi thời điểm. Tải đầu lệnh > 10 dùng 2 luồng, còn lại 4; khói luôn 2, đầu dò luôn 1.\n');
md(['Lệnh','Bắt đầu (+07:00)','Kết thúc','Giây','Luồng','Tải 1 phút','Mã','Seed đúng'],summary.commands.map(r=>[r.tag,r.start,r.end,r.elapsed_seconds,r.threads,r.load1,r.exit,r.headers_valid?'Có':'KHÔNG']));
fs.writeFileSync(path.join(D,'summary.json'),JSON.stringify(summary,null,2)+'\n');
fs.writeFileSync(path.join(D,'summary.md'),out.join('\n'));
console.log(JSON.stringify({known:summary.known_stats,rechecks:summary.win_rechecks,base:summary.base.tight,pkg:summary.pkg.tight},null,2));
