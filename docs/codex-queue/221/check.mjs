import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { validateList, calculateTakes, calculateTotals } from '../212/check.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../..');
const read = p => readFileSync(resolve(root,p),'utf8');
const git = (...args) => execFileSync('git',['-C',resolve(root,'games/typing-defense'),...args],{encoding:'utf8'}).trim();
const literals = s => [...s.matchAll(/"([^"\n]+)"/g)].map(m=>m[1]);
const same = (a,b) => JSON.stringify(a)===JSON.stringify(b);
const negative = /\b(?:no|not|without|never|neither|nor|avoid|exclude|excluding|except|cannot|can't|don't|doesn't|isn't|aren't|won't)\b/i;
const banned = /\b(?:pop|puff|balloon|thud|thump|toy|cartoon|retro|8-bit|chiptune|temple\s+bell|monk\w*|chant\w*|wooden\s+fish|shakuhachi|taiko|erhu|dizi|laser\w*|synth\w*|electronic\w*)\b/i;
const proper = /\b(?:Moc\s+Tinh|Draconis|Cham|Phay|Gach|Ba\s+Cu\s+Muc|Thu\s+Dong|Wordwoven)\b/i;
const busOf = id => /^(key|word|chain|call)-/.test(id)?'typing':id.startsWith('ui-')||id==='day-countdown'?'ui':'world';

function sources() {
  const sm=git('show','td-1c:src/view/sound-map.ts');
  const am=git('show','td-1c:src/view/audio-min.ts');
  const body=sm.match(/export const SOUND_IDS\s*=\s*\{([\s\S]*?)\}\s*as const/)?.[1];
  if(!body)throw new Error('Không đọc được SOUND_IDS');
  const codeIds=literals(body);
  // Chỉ đọc literal, không eval/import TypeScript. play(id) từ event/ring được phủ qua sound-map.
  const direct=[...am.matchAll(/this\.play\("([^"\n]+)"\s*,/g)].map(m=>m[1]);
  const ui=literals(am.match(/export type UiSound\s*=([^;]+);/)?.[1]??'').map(id=>'ui-'+id);
  const extraIds=[...new Set([...direct,...ui])].filter(id=>!codeIds.includes(id));
  const specs=Object.fromEntries(readdirSync(resolve(root,'tools/audio-lab/specs/typing-defense')).filter(n=>n.endsWith('.yaml')).map(n=>{
    const path='tools/audio-lab/specs/typing-defense/'+n,s=read(path);
    const number=(section,field)=>{
      const block=s.match(new RegExp(`^${section}:\\s*\\n((?:[ \\t].*\\n|\\n)*)`,'m'))?.[1];
      const v=block?.match(new RegExp(`^  ${field}: (\\d+(?:\\.\\d+)?|null)$`,'m'))?.[1];
      return v===undefined||v==='null'?null:Number(v);
    };
    return [n.slice(0,-5),{path,min:number('duration','min_ms'),max:number('duration','max_ms'),variants:number('variants','target')}];
  }));
  return {codeIds,extraIds,direct,ui,specs,commits:{'td-1c':git('rev-parse','td-1c'),'a2-days':git('rev-parse','a2-days')}};
}

/** Kiểm riêng Wordwoven: id chỉ có thẻ cũng được phép excluded, không dùng audit của 212. */
export function checkList(list,schema,fired,src,md) {
  const out=Object.fromEntries(['missing','unknown','duplicates','schemaErrors','firedErrors','map1Errors','calculationErrors','loopErrors','inboxErrors','specErrors','asciiPromptErrors','asciiNameErrors','properNameErrors','bannedErrors','negativeErrors','gongErrors','markdownErrors','busErrors','sourceCommitErrors','basisErrors'].map(k=>[k,[]]));
  out.schemaErrors.push(...validateList(list,schema));
  if(out.schemaErrors.length)return out;
  const all=[...list.rows,...list.excluded,...list.retired];
  const union=new Set([...src.codeIds,...src.extraIds,...fired.map(x=>x.id),...Object.keys(src.specs)]);
  const counts=new Map();
  for(const r of all)counts.set(r.id,(counts.get(r.id)??0)+1);
  for(const id of union)if(!counts.has(id))out.missing.push(id);
  for(const [id,n]of counts){if(n>1)out.duplicates.push(`${id}: ${n}`);if(!union.has(id))out.unknown.push(id);}
  const mustFire=new Set([...src.codeIds,...src.extraIds]);
  for(const id of mustFire)if(fired.filter(x=>x.id===id).length!==1)out.firedErrors.push(`${id}: cần đúng một fired entry`);
  for(const f of fired){
    if(!mustFire.has(f.id))out.firedErrors.push(`${f.id}: fired id không có trong mã/âm gọi thêm`);
    if(typeof f.map1!=='boolean'||!f.trigger||!f.sourceEvent||!f.map1Basis||f.bus!==busOf(f.id))out.firedErrors.push(`${f.id}: thiếu căn cứ/trigger/event hoặc bus sai`);
    if(f.map1&&f.firstStage!=='w1-silverfall')out.firedErrors.push(`${f.id}: firstStage sai`);
    if(!f.map1&&list.rows.some(r=>r.id===f.id))out.map1Errors.push(`${f.id}: map1=false mà có row`);
    // Mục 6 bắt buộc key-right ở excluded, dù mục 1 yêu cầu map1 giữ đúng khả năng phát.
    // Ngoại lệ nguồn duy nhất, công khai trong output/report; không âm thầm đổi fired.map1.
    if(f.map1&&f.id==='key-right') {
      if(!list.excluded.some(e=>e.id==='key-right'&&/189.*193/.test(e.reason)))out.map1Errors.push('key-right: mục 6 yêu cầu excluded bộ 189–193');
    } else if(f.map1&&!list.rows.some(r=>r.id===f.id))out.map1Errors.push(`${f.id}: map1=true phải có row`);
  }
  for(const r of list.rows){
    if(!fired.some(f=>f.id===r.id&&f.map1))out.map1Errors.push(`${r.id}: row không được fired map1 hỗ trợ`);
    if(/[^\x00-\x7f]/.test(r.prompt))out.asciiPromptErrors.push(r.id);
    if(r.playerName!==null&&/[^\x00-\x7f]/.test(r.playerName))out.asciiNameErrors.push(r.id);
    if(proper.test(r.prompt))out.properNameErrors.push(`${r.id}: ${r.prompt.match(proper)[0]}`);
    if(banned.test(r.prompt))out.bannedErrors.push(`${r.id}: ${r.prompt.match(banned)[0]}`);
    if(negative.test(r.prompt))out.negativeErrors.push(`${r.id}: ${r.prompt.match(negative)[0]}`);
    if(/\bgong\b/i.test(r.prompt)&&!r.eraNote.includes('gong:'))out.gongErrors.push(r.id);
    if(r.loop!==(r.shape==='loop'))out.loopErrors.push(r.id);
    if(r.inbox!==`~/AudioLab/inbox/firefly/typing-defense/${r.id}/`)out.inboxErrors.push(r.id);
    if(r.bus!==busOf(r.id))out.busErrors.push(r.id);
    if(r.targetMs.min>r.targetMs.max)out.schemaErrors.push(`${r.id}: min > max`);
    if(r.specCard!==null){
      const c=src.specs[r.id];
      if(!c||c.path!==r.specCard)out.specErrors.push(`${r.id}: thẻ không đúng đường dẫn`);
      else {
        for(const k of ['min','max'])if(c[k]!==null&&c[k]!==r.targetMs[k])out.specErrors.push(`${r.id}: targetMs.${k}`);
        if(c.variants!==null&&c.variants!==r.variants)out.specErrors.push(`${r.id}: variants`);
      }
    }else{
      if(src.specs[r.id])out.specErrors.push(`${r.id}: có thẻ nhưng specCard=null`);
      if(!r.basis.some(b=>/\w[\w/-]*\.(?:ts|md):\d/.test(b)&&/Đề xuất.*targetMs=/.test(b)))out.basisErrors.push(`${r.id}: thiếu căn cứ số đề xuất file:dòng`);
    }
    try{const c=calculateTakes(r,list.assumptions);for(const k of ['hitsPerTake','takes'])if(c[k]!==r[k])out.calculationErrors.push(`${r.id}: ${k}`);}catch(e){out.calculationErrors.push(e.message);}
  }
  if(!same(calculateTotals(list.rows),list.totals))out.calculationErrors.push('totals');
  for(const k of ['td-1c','a2-days'])if(list.sourceCommits?.[k]!==src.commits[k])out.sourceCommitErrors.push(`${k}: nguồn đã đổi, cần rà lại căn cứ trước khi cập nhật hash`);
  if(md!==undefined){
    const entries=[...md.matchAll(/^\| `([^`]+)` \| ([^|]+) \| (P[012]) \| (\d+) \|$/gm)];
    const table=entries.map(m=>m[1]);
    for(const r of list.rows){
      const matches=entries.filter(m=>m[1]===r.id);
      if(matches.length!==1||matches[0][2].trim()!==(r.playerName??'—')||matches[0][3]!==r.priority||Number(matches[0][4])!==r.takes)out.markdownErrors.push(`${r.id}: bảng tóm tắt`);
    }
    for(const id of table)if(!list.rows.some(r=>r.id===id))out.markdownErrors.push(`${id}: thừa bảng`);
    const blocks=new Map();
    for(const m of md.matchAll(/^## `([^`]+)`\n([\s\S]*?)(?=^#{1,2} |$(?![\s\S]))/gm)){
      if(blocks.has(m[1]))out.markdownErrors.push(`${m[1]}: trùng block`);
      blocks.set(m[1],m[2].match(/```text\n([\s\S]*?)\n```/)?.[1]);
    }
    for(const r of list.rows)if(blocks.get(r.id)!==r.prompt)out.markdownErrors.push(`${r.id}: prompt khác từng chữ`);
    for(const id of blocks.keys())if(!list.rows.some(r=>r.id===id))out.markdownErrors.push(`${id}: block thừa`);
    const t=list.totals;
    const expected=`**${t.rows} hàng · ${t.takes} lượt dự kiến** (P0 ${t.byPriority.P0}, P1 ${t.byPriority.P1}, P2 ${t.byPriority.P2})`;
    if(md.split('\n').filter(l=>l===expected).length!==1)out.markdownErrors.push('Dòng tổng');
  }
  return out;
}

function main(){
  const src=sources(),list=JSON.parse(read('docs/games/audio/firefly/typing-defense.json'));
  const schema=JSON.parse(read('docs/games/audio/firefly/schema.json'));
  const fired=JSON.parse(read('docs/codex-queue/221/fired-ids.json'));
  const result=checkList(list,schema,fired,src,read('docs/games/audio/firefly/typing-defense.md'));
  const counts=Object.fromEntries(Object.entries(result).map(([k,v])=>[k,v.length]));
  let selftest;
  if(process.argv.includes('--selftest')){
    const missingId=fired.find(f=>f.map1&&f.id!=='key-right').id;
    const tests=[
      ['bỏ hàng map1=true',x=>{x.rows=x.rows.filter(r=>r.id!==missingId);},r=>r.missing.includes(missingId)&&r.map1Errors.some(e=>e.startsWith(missingId+':'))],
      ['thêm id lạ',x=>x.rows.push({...x.rows[0],id:'unknown.injected'}),r=>r.unknown.includes('unknown.injected')],
      ['thêm chữ có dấu',x=>{x.rows[0].prompt+=' á';},r=>r.asciiPromptErrors.includes(list.rows[0].id)]
    ];
    selftest=tests.map(([name,mutate,caught])=>{const x=structuredClone(list);mutate(x);const diagnostics=checkList(x,schema,fired,src);return{name,caught:caught(diagnostics),counts:Object.fromEntries(Object.entries(diagnostics).map(([k,v])=>[k,v.length]))};});
  }
  const longest=[...list.rows].sort((a,b)=>b.prompt.length-a.prompt.length)[0];
  const evidence=JSON.parse(read('docs/codex-queue/221/source-evidence.json'));
  const summary={soundIds:src.codeIds.length,extraIds:src.extraIds,directPlayIds:src.direct,uiIds:src.ui,specIds:Object.keys(src.specs).length,unionIds:new Set([...src.codeIds,...src.extraIds,...fired.map(f=>f.id),...Object.keys(src.specs)]).size,map1Fired:fired.filter(f=>f.map1).length,map1PolicyExceptions:['key-right: mục 6 bắt buộc excluded bộ phím 189–193 dù thực sự phát ở map 1'],rows:list.rows.length,excluded:list.excluded.length,retired:list.retired.length,withSpec:list.rows.filter(r=>r.specCard!==null).length,withoutSpec:list.rows.filter(r=>r.specCard===null).length,groups:evidence.groups.map(({name,ids})=>({name,rows:list.rows.filter(r=>ids.includes(r.id)).length,takes:list.rows.filter(r=>ids.includes(r.id)).reduce((n,r)=>n+r.takes,0)})),totals:list.totals,longestPrompt:{id:longest.id,characters:longest.prompt.length},gongRows:list.rows.filter(r=>/\bgong\b/i.test(r.prompt)).map(r=>r.id),sourceCommits:list.sourceCommits,counts,details:result,...(selftest?{selftest,selftestPassed:selftest.filter(t=>t.caught).length}:{})};
  const ok=Object.values(counts).every(n=>n===0)&&(!selftest||selftest.every(t=>t.caught));
  const lines=[`${ok?'PASS':'FAIL'} · Phiếu 221`, `SOUND_IDS=${summary.soundIds}; extra=${src.extraIds.length}; spec=${summary.specIds}; union=${summary.unionIds}`,`map1Fired=${summary.map1Fired}; rows=${summary.rows}; excluded=${summary.excluded}; retired=${summary.retired}`,`map1PolicyException=key-right (mục 6: bộ phím 189–193)`,...Object.entries(counts).map(([k,v])=>`${k}=${v}`),`takes=${list.totals.takes}; P0=${list.totals.byPriority.P0}; P1=${list.totals.byPriority.P1}; P2=${list.totals.byPriority.P2}`,`withSpec=${summary.withSpec}; withoutSpec=${summary.withoutSpec}`,`longestPrompt=${longest.id}: ${longest.prompt.length} ASCII characters`,...(selftest?[...selftest.map(t=>`${t.caught?'CAUGHT':'MISSED'} ${t.name}`),`selftest=${summary.selftestPassed}/3`]:[]),...(!ok?[JSON.stringify(result,null,2)]:[])].flat().join('\n')+'\n';
  const suffix=selftest?'-selftest':'';
  writeFileSync(resolve(here,`check${suffix}.json`),JSON.stringify({ok,...summary},null,2)+'\n');
  writeFileSync(resolve(here,`check${suffix}.txt`),lines);
  process.stdout.write(lines);
  process.exitCode=ok?0:1;
}
if(process.argv[1]&&pathToFileURL(resolve(process.argv[1])).href===import.meta.url)main();
