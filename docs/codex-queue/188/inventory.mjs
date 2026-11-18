// Kiểm kê chỉ đọc; chỉ ghi bằng chứng vào thư mục phiếu 188. Không chạy build.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { createHash } from 'node:crypto';
const root = process.cwd(), out = path.join(root, 'docs/codex-queue/188');
const ts = createRequire(path.join(root, 'games/dragon-hold/package.json'))('typescript');
const rel = p => path.relative(root,p);
const hash = p => createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read = p => fs.readFileSync(p, 'utf8');
const bases = ['games/dragon-hold','games/typing-defense','games/typing-survival','shared/game-kit'];
function lockData(file) {
  const lines = read(file).split('\n'), result = {dependencies:{}, devDependencies:{}, snapshots:{}};
  let top='', section='', name='', snapshot='', depSection='';
  for(const line of lines) {
    if(/^\S.*:$/.test(line)) top=line.slice(0,-1);
    if(top==='importers') {
      const s=line.match(/^    (dependencies|devDependencies):$/); if(s)section=s[1];
      const n=line.match(/^      (.+):$/);if(n)name=n[1].replace(/^['"]|['"]$/g,'');
      const v=line.match(/^        version: (.+)$/);if(v && section)result[section][name]=v[1].replace(/^['"]|['"]$/g,'');
    }
    if(top==='snapshots') {
      const n=line.match(/^  (\S.*):(?: \{\})?$/);if(n){snapshot=n[1].replace(/^['"]|['"]$/g,'');result.snapshots[snapshot]={};depSection='';}
      const s=line.match(/^    (\w+):$/);if(s)depSection=s[1];
      const d=line.match(/^      (.+): (.+)$/);if(d && ['dependencies','optionalDependencies'].includes(depSection))result.snapshots[snapshot][d[1].replace(/^['"]|['"]$/g,'')]=d[2].replace(/^['"]|['"]$/g,'');
    }
  } return result;
}
function walk(dir) {
  return fs.readdirSync(dir,{withFileTypes:true}).filter(d=>!['node_modules','.git','tmp','dist','tests'].includes(d.name)).flatMap(d=>d.isDirectory()?walk(path.join(dir,d.name)):[path.join(dir,d.name)]);
}
function imports(file) {
  const text=read(file), list=[];
  if(file.endsWith('.css')) {for(const m of text.matchAll(/@import\s+(?:url\()?['"]([^'"]+)['"]/g))list.push({spec:m[1],line:text.slice(0,m.index).split('\n').length});return list;}
  if(!/\.[cm]?[jt]sx?$/.test(file))return list;
  const ast=ts.createSourceFile(file,text,ts.ScriptTarget.Latest,true);
  function visit(n) {
    if((ts.isImportDeclaration(n)||ts.isExportDeclaration(n)) && n.moduleSpecifier && !n.importClause?.isTypeOnly && !n.isTypeOnly) {
      const clause=n.importClause;
      const onlyTypes=clause && !clause.name && clause.namedBindings && ts.isNamedImports(clause.namedBindings) && clause.namedBindings.elements.length && clause.namedBindings.elements.every(e=>e.isTypeOnly);
      if(!onlyTypes)list.push({spec:n.moduleSpecifier.text,line:ast.getLineAndCharacterOfPosition(n.getStart()).line+1});
    }
    if(ts.isCallExpression(n) && n.expression.kind===ts.SyntaxKind.ImportKeyword)list.push({spec:ts.isStringLiteral(n.arguments[0])?n.arguments[0].text:null,line:ast.getLineAndCharacterOfPosition(n.getStart()).line+1});
    ts.forEachChild(n,visit);
  } visit(ast);return list;
}
function graph(entries,base) {
  const seen=new Set(), external=[],unresolved=[];
  function visit(f) {
    if(seen.has(f))return;seen.add(f);
    for(const item of imports(f)) {
      const {spec}=item;
      if(!spec){unresolved.push({file:rel(f),...item});continue;}
      if(!spec.startsWith('.')){external.push({file:rel(f),...item});continue;}
      const stem=path.resolve(path.dirname(f),spec);
      const resolved=[stem,stem+'.ts',stem+'.js',stem+'.css',path.join(stem,'index.ts')].find(p=>fs.existsSync(p)&&fs.statSync(p).isFile());
      if(resolved)visit(resolved);else unresolved.push({file:rel(f),...item});
    }
  } entries.forEach(visit);
  return {files:[...seen].map(rel).sort(),external,unresolved};
}
const audit=[];
for(const base of bases) {
  const dir=path.join(root,base), manifest=JSON.parse(read(path.join(dir,'package.json'))), lock=lockData(path.join(dir,'pnpm-lock.yaml'));
  const records=[],done=new Set();
  function pkg(name,version,kind,parent) {
    const key=name+'@'+version;if(done.has(key))return;done.add(key);
    let moduleDir=path.join(dir,'node_modules',name);
    if(!fs.existsSync(moduleDir)) {
      const store=path.join(dir,'node_modules/.pnpm');
      const match=fs.readdirSync(store).find(n=>n.startsWith(name.replace('/','+')+'@'+version+'') && fs.existsSync(path.join(store,n,'node_modules',name)));
      if(match)moduleDir=path.join(store,match,'node_modules',name);
    }
    if(!fs.existsSync(moduleDir)) {records.push({name,version,kind,parent,missing:true});return;}
    const json=JSON.parse(read(path.join(moduleDir,'package.json')));
    const notices=fs.readdirSync(moduleDir).filter(n=>/^(licen[cs]e|copying|notice)/i.test(n)&&fs.statSync(path.join(moduleDir,n)).isFile()).map(n=>({path:rel(path.join(moduleDir,n)),sha256:hash(path.join(moduleDir,n)),text:read(path.join(moduleDir,n))}));
    records.push({name,version:version.split('(')[0],installedVersion:json.version,kind,parent,license:json.license,repository:json.repository,dependencies:json.dependencies??{},packageJson:rel(path.join(moduleDir,'package.json')),packageJsonSha256:hash(path.join(moduleDir,'package.json')),notices});
    for(const [dep,v] of Object.entries(lock.snapshots[key]??{}))pkg(dep,v,'transitive',key);
  }
  for(const [name,version] of Object.entries(lock.dependencies))pkg(name,version,'dependency',base);
  if(base==='shared/game-kit')pkg('three',lock.devDependencies.three,'devDependency-runtime',base);
  for(const [name,version] of Object.entries(lock.devDependencies)) {
    const d=path.join(dir,'node_modules',name,'package.json');
    records.push({name,version:version.split('(')[0],kind:'devDependency',installedVersion:fs.existsSync(d)?JSON.parse(read(d)).version:null});
  }
  const sourceRoot=base==='shared/game-kit'?dir:path.join(dir,'src');
  const allFiles=walk(sourceRoot).filter(f=>!f.includes('/node_modules/')&&!f.includes('/.git/')&&!f.includes('/tests/')&&!/\.test\.[cm]?[jt]s$/.test(f)&&/\.(ts|js|mjs|css)$/.test(f));
  const entries=base==='shared/game-kit'?allFiles.filter(f=>!f.includes('/tools/')&&!/config\.[cm]?[jt]s$/.test(f)&&!f.endsWith('/verify-kit.mjs')):[path.join(dir,base.endsWith('typing-survival')?'src/app/main.ts':'src/main.ts')];
  const runtime=graph(entries,dir);
  const threeEntries=[...new Set(runtime.external.map(i=>i.spec).filter(s=>s==='three'||s?.startsWith('three/')))];
  const vendorGraph=threeEntries.length?graph(threeEntries.map(s=>path.join(dir,'node_modules/three',s==='three'?'build/three.module.js':s.slice(6))),dir):{files:[],external:[],unresolved:[]};
  const vendorNotices=vendorGraph.files.flatMap(f=>read(path.join(root,f)).split('\n').flatMap((line,i)=>/copyright|license|SPDX/i.test(line)?[{file:f,line:i+1,text:line.slice(0,500)}]:[]));
  const allExternal=allFiles.flatMap(f=>imports(f).filter(i=>i.spec&&!i.spec.startsWith('.')).map(i=>({file:rel(f),...i})));
  const hashes=Object.fromEntries(['package.json','pnpm-lock.yaml'].map(f=>[base+'/'+f,hash(path.join(dir,f))]));
  audit.push({base,manifest,lock,records,runtime,allExternal,vendorGraph,vendorNotices,hashes});
}
fs.writeFileSync(path.join(out,'inventory.json'),JSON.stringify(audit,null,2)+'\n');
console.log(JSON.stringify(audit.map(a=>({base:a.base,packages:a.records.map(({name,version,kind,license,installedVersion,missing})=>({name,version,kind,license,installedVersion,missing})),runtimeFiles:a.runtime.files.length,runtimeExternal:[...new Set(a.runtime.external.map(x=>x.spec))],unresolved:a.runtime.unresolved})),null,2));
