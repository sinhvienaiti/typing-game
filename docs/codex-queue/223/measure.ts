/** DH-08 one-off runner. Outputs stay in tmp/codex-223. No source mutation. */
import {writeFileSync,readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {BOTS,BOT_NAMES,M0_BOTS,type BotSpec} from '../../scripts/balance/bot';
import {CDP_TIMING,CdpTypist,findBot,measureRun,percentile,type HumanWave} from '../../scripts/balance/human';
import {STAGE_M0} from '../../src/content/data/stages';
import {PRESSURE} from '../../src/content/rules';
import {pacedStage} from '../../scripts/balance/variants';
import {summarize} from '../../scripts/balance/report';
const args=process.argv.slice(2),arg=(n:string,f:string)=>args.find(s=>s.startsWith('--'+n+'='))?.slice(n.length+3)??f;
const out=arg('out','measurement'),bots=arg('bots','b35,b35cdp,b35human').split(','),single=args.includes('--single');
const bases=single?[Number(arg('seed','1'))]:[20261023,21261026],seeds=single?1:20;
const pace=Number(arg('pace','1')),pressure=Number(arg('pressure','1000'));
(PRESSURE.difficultyPm as {normal:number}).normal=pressure;
const uptime=execFileSync('uptime',{encoding:'utf8'}).trim(),started=performance.now();
let deck: Awaited<ReturnType<typeof pinnedDeck>> | undefined;
async function pinnedDeck(){
 const {createLearningClient}=await import('../../src/app/learning');
 const original=globalThis.fetch;
 globalThis.fetch=(async(url:unknown)=>({ok:true,json:async()=>JSON.parse(readFileSync('public/'+String(url).replace(/^\//,''),'utf8'))})) as typeof fetch;
 const client=createLearningClient({vocabLevel:1,excludeMature:false,bridge:{dispose(){},lookup:async()=>{throw Error('offline')}} as never,storage:{readJson:()=>null,writeJson:()=>true},every:()=>()=>{}});
 try{return await client.buildDeck(STAGE_M0);}finally{client.dispose();globalThis.fetch=original;}
}
if(args.includes('--pinned'))deck=await pinnedDeck();
const results:Record<string,unknown>={};
for(const name of bots){
 const measured=[];const botStart=performance.now();
 for(const base of bases)for(let i=0;i<seeds;i++){
  const seed=base+i; let custom:CdpTypist|undefined;
  const original=findBot(name)!;
  const spec:BotSpec=name==='b35cdp'?{...original,typist:rng=>(custom=new CdpTypist(rng))}:original;
  const exposure:Record<number,{lateWordTicks:number;standingNoWordTicks:number}>={};
  const {run,waves}=measureRun(spec,{seed,difficulty:'normal',stage:pacedStage(STAGE_M0,pace),...(deck?{deck}:{}),onTick:(w)=>{
   if(w.phase!=='wave')return;
   const row=exposure[w.wave]??={lateWordTicks:0,standingNoWordTicks:0};
   const grace=Math.round(w.pace.graceTicks*PRESSURE.graceX10/10);
   for(const e of w.enemies.list)if(e.alive&&e.x*e.x+e.z*e.z<=26*60000*26*60000){const word=e.word>=0?w.words.live[e.word]:null;if(word&&w.tick-word.bornTick>grace)row.lateWordTicks++;else if(!word&&['blocked','attack','hold'].includes(e.mode))row.standingNoWordTicks++;}
  }});
  measured.push({seed,base,run,waves,exposure,...(custom?{cdp:{sent:custom.sent,planSent:custom.planSent,rejected:custom.rejected,pauses:custom.pauses}}:{})});
 }
 const runs=measured.map(m=>m.run),flat=measured.flatMap(m=>m.waves);
 const q=(values:number[])=>({p50:percentile(values,.5),p90:percentile(values,.9)});
 const byWave=Array.from({length:10},(_,i)=>{const rows=flat.filter(w=>w.wave===i+1);return{wave:i+1,n:rows.length,hpStart:q(rows.map(w=>w.hpStart)),hpMin:q(rows.map(w=>w.hpMin)),wordsCompleted:q(rows.map(w=>w.wordsCompleted)),letters:q(rows.map(w=>w.letters)),lettersPerMinute:q(rows.map(w=>w.lettersPerMinute)),hpDrop:q(rows.map(w=>w.hpDrop)),heroDamage:q(rows.map(w=>w.heroDamage)),reaction:q(rows.flatMap(w=>w.reaction.samples)),nearest:q(rows.flatMap(w=>w.nearestPct===null?[]:[w.nearestPct]))};});
 results[name]={seconds:(performance.now()-botStart)/1000,summary:summarize(name,runs,STAGE_M0,'balanced'),sets:bases.map(base=>{const rr=measured.filter(m=>m.base===base).map(m=>m.run);return{base,n:rr.length,winPct:rr.filter(r=>r.result==='victory').length*100/rr.length};}),winPct:runs.filter(r=>r.result==='victory').length*100/runs.length,hpDrop:q(flat.map(w=>w.hpDrop)),heroDamage:q(flat.map(w=>w.heroDamage)),byWave,runs:measured};
}
writeFileSync('tmp/codex-223/'+out+'.json',JSON.stringify({uptime,jobs:1,cdpTiming:CDP_TIMING,seeds,bases,bots,mode:'balanced',pace,pressureNormal:pressure,pinned:!!deck,seconds:(performance.now()-started)/1000,results},null,2)+'\n');
writeFileSync('../../docs/codex-queue/223/bots-after.txt',JSON.stringify({BOT_NAMES,M0_BOTS,keys:Object.keys(BOTS)},null,2)+'\n');
console.log(JSON.stringify({out,seconds:(performance.now()-started)/1000,bots:Object.entries(results).map(([name,v])=>({name,...Object.fromEntries(Object.entries(v as object).filter(([k])=>['winPct','hpDrop','heroDamage'].includes(k)))}))},null,2));
