// Read-only CDP analysis. Run from the dh-codex worktree.
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
const source=resolve('../dragon-hold/tmp/map1-audit/feel-35-1280');
const read=n=>JSON.parse(readFileSync(resolve(source,n),'utf8'));
const samples=read('samples.json'), timeline=read('timeline.json'), raw=read('rc-raw.json'), report=read('report.json').result, idle=read('idle.json');
const percentile=(a,q)=>a.length?[...a].sort((a,b)=>a-b)[Math.min(a.length-1,Math.ceil(q*a.length)-1)]:null;
const evalPairs=Object.entries(report.moments).filter(([k])=>/^w\d+-01-warning$/.test(k)).map(([,v])=>v.at-timeline.filter(s=>s.phase==='warning'&&s.wave===v.wave&&s.t<=v.at).at(-1)?.t).filter(x=>x>=0&&x<=100);
const markMs=100, pollMs=evalPairs.map(x=>90+x), waves=[];
for(let w=1;w<=10;w++) {
 const ss=samples.filter(s=>s[1]===2&&s[2]===w), first=ss[0], last=ss.at(-1), start=first[0];
 const end=samples.find(s=>s[0]>last[0])?.[0]??last[0]+100;
 const letters=raw.letters.filter(k=>k.t>=start&&k.t<end), pauses=[];
 const add=(name,at,ms,basis)=>pauses.push({name,startMs:at,endMs:at+ms,ms,basis});
 const sheets=report.sheets.filter(s=>s.name.startsWith(`w${w}-`)), startSheet=sheets.find(s=>s.name.endsWith('start-banner'));
 add('start-banner',report.moments[`w${w}-02-start`].at-startSheet.spanMs,startSheet.spanMs,'sheets.spanMs, neo tại mark start; thiếu thời gian montage');
 for(const [name,m] of Object.entries(report.moments)) {
  if(!name.startsWith(`w${w}-`)||name.endsWith('01-warning'))continue;
  if(m.at!==undefined)add(name,m.at,markMs,'giả định 100 ms/mark; căn chỉnh đồng hồ ±25 ms');
  else if(name.includes('-05-peak-'))add(name,timeline[0].t+Number(name.match(/-(\d+)s$/)?.[1])*1000,markMs,'peak làm tròn giây, sai số ±0,5 s');
 }
 const damage=report.moments[`w${w}-04-first-damage`], hurt=sheets.find(s=>s.name.endsWith('hp-loss'));
 if(hurt&&damage)add('hp-loss',damage.at+markMs,hurt.spanMs,'sheets.spanMs sau mark first-damage');
 const general=sheets.find(s=>s.name.endsWith('general-move'));
 if(general)add('general-move',timeline.find(s=>s.wave===w&&s.general&&Math.hypot(s.general.x,s.general.z)<20)?.t??start,general.spanMs,'sheets.spanMs; mốc từ timeline, sai số một khoảng snapshot');
 for(const sheet of sheets.filter(s=>s.name.includes('-complete-'))) {
  const text=sheet.name.split('-complete-')[1].split('-')[0], at=letters.map(x=>x.key).join('').indexOf(text);
  if(at>=0)add(sheet.name,letters[at+text.length-1].t-120,sheet.spanMs,'neo chữ cuối chuỗi đầu khớp; 120 ms trước + 200 ms sau nằm trong burst');
 }
 const letterBurst=sheets.find(s=>s.name.includes('-letters-'));
 if(letterBurst){const text=letterBurst.name.split('-letters-')[1], at=letters.map(x=>x.key).join('').indexOf(text);if(at>=0){const tail=letters[at+text.length-1].t+200,until=letters[at].t+letterBurst.spanMs;if(until>tail)add(letterBurst.name,tail,until-tail,'chỉ đuôi còn chờ; phím chạy song song');}}
 const ff=report.moments[`w${w}-08-ff-try`];if(ff)add('ff-sleep',ff.at-250,250,'sleep 250 ms, fastForward=false');
 pauses.sort((a,b)=>a.startMs-b.startMs);const union=[];
 for(const p of pauses){const a=Math.max(start,p.startMs),b=Math.min(end,p.endMs);if(b<=a)continue;const prev=union.at(-1);if(prev&&a<=prev[1])prev[1]=Math.max(prev[1],b);else union.push([a,b]);}
 const reactions=[];
 for(let i=0;i<ss.length;i++)if(ss[i][4]>0&&(i===0?samples[samples.indexOf(ss[i])-1]?.[4]===0:ss[i-1][4]===0)) {
  const born=ss[i][0],nextZero=ss.slice(i+1).find(s=>s[4]===0)?.[0]??end,key=letters.find(k=>k.t>=born);
  if(!key){reactions.push({bornMs:born,ms:null,censored:true});continue;}
  const overlaps=pauses.filter(p=>p.startMs<=key.t&&p.endMs>=born).map(p=>p.name);
  reactions.push({bornMs:born,firstKeyMs:key.t,ms:key.t-born,pause:overlaps.length>0,pauses:overlaps});
 }
 const all=reactions.filter(x=>x.ms!==null).map(x=>x.ms),clean=reactions.filter(x=>x.ms!==null&&!x.pause).map(x=>x.ms);
 const tt=timeline.filter(t=>t.wave===w&&t.phase==='wave');
 waves.push({wave:w,startMs:start,endMs:end,seconds:(end-start)/1000,hpStart:first[6],hpMin:Math.min(...ss.map(s=>s[6])),hpDrop:first[6]-Math.min(...ss.map(s=>s[6])),letters:letters.length,lettersPerMinute:letters.length*60000/(end-start),wordsCompleted:null,wordsReason:'Không đo được: words là số từ sống; kills gồm bẫy/kỹ năng; stats.words là tổng 168 lượt chọn, không phải sự kiện hoàn tất.',reaction:{p50:percentile(all,.5),p90:percentile(all,.9),n:all.length,cleanP50:percentile(clean,.5),cleanP90:percentile(clean,.9),cleanN:clean.length,censored:reactions.length-all.length,samples:reactions},pauses,pauseSeconds:union.reduce((s,[a,b])=>s+b-a,0)/1000,nearest:'100% lần chọn tự do theo PICK; khóa và urgent trước',tickRatio:(tt.at(-1).tick-tt[0].tick)/((tt.at(-1).t-tt[0].t)*.06)});
}
const clean=waves.flatMap(w=>w.reaction.samples.filter(s=>s.ms!==null&&!s.pause).map(s=>s.ms));
const out={source,profile:report.profile,sampleCount:samples.length,recordedLetterCount:raw.letters.length,simLetters:report.end.keys,wordAttempts:report.stats.words,reflection:'Kịch bản CDP, không phải người; bỏ rc-raw.hurt.',assumptions:{performanceOffsetMs:0,alignmentErrorMs:25,markMs,evalPairMs:evalPairs,pollMs,pollCaveat:'Không có log mỗi lần hỏi PICK: không nhận diện được phân bố poll chính xác. Dùng 90 ms + proxy hai eval đo tại warning; các eval còn lại chưa tách được.',reactionErrorMs:100,cleanReactionP50:percentile(clean,.5),cleanReactionP90:percentile(clean,.9),startSpanMs:report.sheets.filter(s=>s.name.endsWith('start-banner')).map(s=>s.spanMs),hpLossSpanMs:[0,0,0,0,0,0,1734,1711,1650,0],completeSpanMs:[1112,0,0,0,0,0,0,0,0,1132],generalSpanMs:1160},waves,idleReference:idle};
writeFileSync('tmp/codex-223/browser-waves.json',JSON.stringify(out,null,2)+'\n');
console.log(waves.map(w=>({wave:w.wave,hp:w.hpStart,min:w.hpMin,drop:w.hpDrop,letters:w.letters,cpm:Math.round(w.lettersPerMinute),p50:w.reaction.p50,p90:w.reaction.p90,clean50:w.reaction.cleanP50,n:w.reaction.n,pauses:w.pauseSeconds})));
console.log(out.assumptions);
