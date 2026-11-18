import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const root = path.resolve('games/.wt-ts-codex');
const require = createRequire(path.join(root, 'package.json'));
const ts = require('typescript');
const vietnamese = /[À-ỹđĐ]/u;
function files(dir) {
  return fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => e.isDirectory() ? files(path.join(dir,e.name)) : [path.join(dir,e.name)]);
}
const rows = [];
for (const file of files(path.join(root, 'src')).filter(f => /\.[cm]?[jt]sx?$/.test(f))) {
  const source = fs.readFileSync(file, 'utf8');
  const ast = ts.createSourceFile(file, source, ts.ScriptTarget.Latest, true);
  function visit(node) {
    if (ts.isStringLiteral(node) || ts.isNoSubstitutionTemplateLiteral(node) || ts.isTemplateHead(node) || ts.isTemplateMiddle(node) || ts.isTemplateTail(node)) {
      if(vietnamese.test(node.text)) rows.push({file:path.relative(root,file), line:ast.getLineAndCharacterOfPosition(node.getStart(ast)).line+1, start:node.getStart(ast), end:node.end, text:node.text, raw:node.getText(ast), kind:ts.SyntaxKind[node.kind]});
    }
    ts.forEachChild(node,visit);
  }
  visit(ast);
}
const html = fs.readFileSync(path.join(root,'index.html'),'utf8');
html.split('\n').forEach((text,i)=>{if(vietnamese.test(text)) rows.push({file:'index.html',line:i+1,text,raw:text,kind:'HTML'});});
fs.writeFileSync(path.resolve('docs/codex-queue/130', process.argv[2] ?? 'scan-before.json'),JSON.stringify(rows,null,2)+'\n');
console.log('Literal segments:',rows.length,'non-kit:',rows.filter(r=>!r.file.startsWith('src/kit/')).length);
