import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {createRequire} from 'node:module';
import vm from 'node:vm';
const root=path.resolve('games/.wt-ts-codex'),dir=path.resolve('docs/codex-queue/130');
const ts=createRequire(path.join(root,'package.json'))('typescript');
const read=(file,before)=>before?execFileSync('git',['-C',root,'show','HEAD:'+file],{encoding:'utf8'}):fs.readFileSync(path.join(root,file),'utf8');
function definitions(file,before,names) {
 const source=ts.createSourceFile(file,read(file,before),ts.ScriptTarget.Latest,true);
 return source.statements.flatMap(node=>{
  if(ts.isFunctionDeclaration(node)&&names.includes(node.name?.text))return [node.getText(source)];
  if(ts.isVariableStatement(node))return node.declarationList.declarations.filter(d=>names.includes(d.name.getText(source))).map(d=>'const '+d.getText(source)+';');
  return [];
 }).join('\n');
}
function menu(before,started,level,mode,tier) {
 const context=vm.createContext({started,level,world:{phase:'won'},chosen:{pilot:'vanguard',tier},pilot:'vanguard',tier,settings:{mode,sfxVolume:0.8,musicVolume:0.5,screenShake:true,pronunciationEnabled:true,paceAdapt:true},shakeAllowed:true,motionPreference:()=> 'system',CHAPTER_1: before? [{index:1,name:'Ca trực đầu'},{index:2,name:'Săn Pack Leader'},{index:3,name:'Vách nứt'},{index:4,name:'Khiên sáng'}]:[{index:1,name:'First Shift'},{index:2,name:'Hunt Pack Leader'},{index:3,name:'Rift Wall'},{index:4,name:'Shield Glow'}],STAGE_S0:{seconds:120}});
 const code=definitions('src/app/main.ts',before,['TIER_NAMES','PILOT_NAMES','MOTION_NAMES','percent','onOff','nextRun','items'])+'\n'+definitions('src/content/balance.ts',before,['MODE_SPECS']);
 vm.runInContext(ts.transpileModule(code,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.None}}).outputText,context);
 return which=>vm.runInContext('items('+JSON.stringify(which)+')',context);
}
const rows=[];
for(const started of [false,true])for(const level of [{id:'s0',index:0},{id:'c1-s1',index:1},{id:'c1-s2',index:2},{id:'c1-s3',index:3},{id:'c1-s4',index:4}])for(const mode of ['relax','balanced','challenge'])for(const tier of ['low','medium','high','ultra']){
 const old=menu(true,started,level,mode,tier),now=menu(false,started,level,mode,tier);
 for(const screen of ['title','settings','armory','profile','pause','end']){
  const a=old(screen),b=now(screen);
  for(let i=0;i<a.length;i++)for(const field of ['label','note','value']){
   const before=a[i][field],after=b[i][field];
   if(typeof before==='string'&&typeof after==='string'&&before!==after)rows.push({screen,id:a[i].id,field,before,after,old:[...before].length,new:[...after].length,ratio:[...after].length/[...before].length});
  }
 }
}
const unique=[...new Map(rows.map(r=>[r.screen+'|'+r.id+'|'+r.field+'|'+r.before+'|'+r.after,r])).values()];
const over=unique.filter(r=>r.ratio>1.2);
fs.writeFileSync(path.join(dir,'lengths.json'),JSON.stringify({cases:rows.length,unique:unique.length,over,rows:unique},null,2)+'\n');
console.log(JSON.stringify({cases:rows.length,unique:unique.length,over},null,2));
