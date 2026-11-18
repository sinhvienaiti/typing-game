import { createRequire } from 'node:module';
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve, relative, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const report = dirname(fileURLToPath(import.meta.url));
const root = resolve(report, '../../../games/.wt-td-codex');
const require = createRequire(resolve(root, 'package.json'));
const ts = require('typescript');
const broad = /[À-ỹđĐ]/u;
const vietnamese = /[ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯư\u1ea0-\u1ef9]/u;
const current = [], baseline = [], comments = [];
function files(path) {
  return readdirSync(path, { withFileTypes: true }).flatMap(e => {
    const p = resolve(path, e.name);
    return e.isDirectory() ? files(p) : /\.(?:ts|css|html)$/.test(p) ? [p] : [];
  });
}
function scan(file, text, output, withComments = false) {
  if (file.endsWith('.ts')) {
    const source = ts.createSourceFile(file, text, ts.ScriptTarget.Latest, true);
    const foundComments = new Set();
    const visit = node => {
      if (ts.isStringLiteralLike(node) || ts.isTemplateHead(node) || ts.isTemplateMiddle(node) || ts.isTemplateTail(node)) {
        output.push({ file, line: source.getLineAndCharacterOfPosition(node.getStart(source)).line + 1, text: node.text, kind: ts.SyntaxKind[node.kind] });
      }
      if (withComments) {
        const add = (pos, end) => {
          const value = text.slice(pos, end);
          if (!foundComments.has(pos) && vietnamese.test(value.normalize('NFC'))) {
            foundComments.add(pos);
            comments.push({ file, line: source.getLineAndCharacterOfPosition(pos).line + 1, text: value });
          }
        };
        ts.forEachLeadingCommentRange(text, node.pos, add);
        ts.forEachTrailingCommentRange(text, node.end, add);
      }
      ts.forEachChild(node, visit);
    };
    visit(source);
  } else if (file.endsWith('.css')) {
    const code = text.replace(/\/\*[\s\S]*?\*\//g, value => value.replace(/[^\n]/g, ' '));
    for (const match of code.matchAll(/"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/g)) {
      output.push({ file, line: code.slice(0, match.index).split('\n').length, text: match[0].slice(1, -1), kind: 'CSSString' });
    }
  } else {
    const code = text.replace(/<!--[\s\S]*?-->/g, value => value.replace(/[^\n]/g, ' '));
    for (const match of code.matchAll(/(?:\b(?:lang|aria-label|title)="([^"]*)")|(?:>([^<>]+)<)/g)) {
      const value = match[1] ?? match[2];
      if (value.trim()) output.push({ file, line: code.slice(0, match.index).split('\n').length, text: value, kind: match[1] === undefined ? 'HTMLText' : 'HTMLAttribute' });
    }
  }
}
for (const path of [...files(resolve(root, 'src')), ...files(resolve(root, 'tests')).filter(p => !p.includes('/golden/')), resolve(root, 'index.html')]) {
  const file = relative(root, path);
  scan(file, readFileSync(path, 'utf8'), current, file.startsWith('src/'));
  try { scan(file, execFileSync('git', ['-C', root, 'show', 'HEAD:' + file], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }), baseline); } catch {}
}
const sourceBefore = JSON.parse(readFileSync(resolve(report, 'literals-before.json'), 'utf8'));
const originals = baseline.filter(x => !x.file.endsWith('.ts') || !sourceBefore.some(y => y.file === x.file));
originals.push(...sourceBefore);
writeFileSync(resolve(report, 'inventory.json'), JSON.stringify({ current, baseline: originals, comments }, null, 2) + '\n');
const remaining = current.filter(x => x.file.startsWith('src/') && !x.file.startsWith('src/kit/') && vietnamese.test(x.text.normalize('NFC')));
console.log(JSON.stringify({ baselineLiterals: originals.length, currentLiterals: current.length, broadMatches: current.filter(x => broad.test(x.text)).length, remainingOutsideKit: remaining }, null, 2));
