const fs = require('node:fs');
const path = require('node:path');
const ts = require('../../../games/.wt-dh-codex/node_modules/typescript');
const root = path.resolve(__dirname, '../../../games/.wt-dh-codex');
const vietnamese = /[À-ÃÈ-ÊÌ-ÍÒ-ÕÙ-ÚÝà-ãè-êì-íò-õù-úýĂăĐđĨĩŨũƠơƯưẠ-ỹ]/;
function walk(dir) { return fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => e.isDirectory() ? walk(path.join(dir,e.name)) : [path.join(dir,e.name)]); }
const entries=[];
for (const abs of walk(path.join(root,'src')).filter(p=>/\.(ts|tsx|js|mjs)$/.test(p))) {
 const file=path.relative(root,abs); const text=fs.readFileSync(abs,'utf8');
 const ast=ts.createSourceFile(file,text,ts.ScriptTarget.Latest,true);
 function visit(node) {
  if (ts.isStringLiteral(node)||ts.isNoSubstitutionTemplateLiteral(node)||ts.isTemplateExpression(node)) {
   const raw=node.getText(ast);
   if(vietnamese.test(raw)) entries.push({file,line:ast.getLineAndCharacterOfPosition(node.getStart(ast)).line+1,start:node.getStart(ast),end:node.end,raw});
   if(ts.isTemplateExpression(node)) { for(const span of node.templateSpans) visit(span.expression); return; }
  }
  ts.forEachChild(node,visit);
 }
 visit(ast);
}
if(process.argv.includes('--save')) fs.writeFileSync(path.join(__dirname,'before.json'),JSON.stringify(entries,null,2)+'\n');
else process.stdout.write(JSON.stringify(entries,null,2)+'\n');
