import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { parseArgs, planPrune, applyPlan, printPlan, main, targetRefusal } from '../prune.mjs';

const NOW = Date.now();
const OLD = new Date(NOW - 120 * 60_000);
const md5 = file => createHash('md5').update(fs.readFileSync(file)).digest('hex');

function fixture(t) {
  const base = fs.realpathSync(fs.mkdtempSync(path.join(os.tmpdir(), 'capture-prune-')));
  t.after(() => fs.rmSync(base, { recursive: true, force: true }));
  const repoRoot = path.join(base, 'repo');
  const target = path.join(repoRoot, 'games/x/tmp/run');
  fs.mkdirSync(target, { recursive: true });
  function put(relative, content = relative) {
    const file = path.join(repoRoot, relative);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, content);
    fs.utimesSync(file, OLD, OLD);
    return file;
  }
  function plan(args = [target]) {
    return planPrune(parseArgs(args), { repoRoot, now: NOW });
  }
  return { base, repoRoot, target, put, plan };
}

test('chạy thử: chỉ ảnh thô; giữ tên, thư mục compare và mọi loại file khác', t => {
  const f = fixture(t);
  for (const name of ['frame.PNG', 'frame.jpg', 'frame.JpEg', 'nested/frame.WEBP',
    'Sheet.PNG', 'my-CONTACT.jpg', 'pre-Compare.jpeg', 'compare-old/raw.png',
    'nested/CompareA/raw.jpg', 'stats.json', 'notes.md', 'frame.gif']) f.put(`games/x/tmp/run/${name}`);
  const before = fs.readdirSync(f.target, { recursive: true });
  const result = f.plan();
  assert.deepEqual(result.files.map(file => file.relative), ['frame.JpEg', 'frame.PNG', 'frame.jpg', 'nested/frame.WEBP']);
  assert.equal(result.kept.length, 5);
  assert.equal(result.bytes, result.files.reduce((sum, file) => sum + fs.statSync(file.path).size, 0));
  const lines = [];
  printPlan(result, line => lines.push(line));
  assert(lines.some(line => line.startsWith(`${f.target}/nested\t1\t`)));
  assert(!lines.some(line => line.includes('Sheet.PNG')));
  assert.deepEqual(fs.readdirSync(f.target, { recursive: true }), before);
});

test('Markdown: tmp/... và games/x/tmp/..., mọi gốc mặc định, ảnh khác cùng basename vẫn xóa', t => {
  const f = fixture(t);
  for (const name of ['linked.png', 'full.jpg', 'nested.webp', 'root.JPEG', 'other/linked.png']) f.put(`games/x/tmp/run/${name}`);
  f.put('docs/a.md', '[ảnh](tmp/run/linked.png)\n<img src="games/x/tmp/run/full.jpg">');
  f.put('games/x/docs/sub/b.MD', '`tmp/run/nested.webp`');
  f.put('games/x/NOTES.md', 'games/x/tmp/run/root.JPEG');
  const result = f.plan();
  assert.deepEqual(result.files.map(file => file.relative), ['other/linked.png']);
  assert.equal(result.kept.length, 4);
  assert(result.kept.every(file => file.reasons.includes('document-reference')));
});

test('--docs nhận nhiều gốc/file, ghi đè mặc định, không theo symlink tài liệu', t => {
  const f = fixture(t);
  for (const name of ['one.png', 'two.jpg', 'default.png', 'symlink.png']) f.put(`games/x/tmp/run/${name}`);
  f.put('docs/a.md', 'tmp/run/default.png');
  const one = f.put('references/a.md', 'tmp/run/one.png');
  const two = f.put('references2/nested/a.md', 'tmp/run/two.jpg');
  const hidden = f.put('hidden/a.md', 'tmp/run/symlink.png');
  fs.symlinkSync(hidden, path.join(path.dirname(one), 'link.md'));
  const result = f.plan([f.target, '--docs', path.dirname(one), two]);
  assert.deepEqual(result.files.map(file => file.relative), ['default.png', 'symlink.png']);
  assert.deepEqual(result.kept.map(file => file.relative), ['one.png', 'two.jpg']);
  assert.throws(() => f.plan([f.target, '--docs', path.join(f.base, 'missing')]), /ENOENT/);
});

test('--min-age-min giữ mới, mốc biên và mtime tương lai; nhiều lý do giữ được ghi đủ', t => {
  const f = fixture(t);
  for (const name of ['old.png', 'new.png', 'edge.png', 'future.png', 'sheet.png']) f.put(`games/x/tmp/run/${name}`);
  for (const [name, offset] of [['new.png', -60_000], ['edge.png', -30 * 60_000], ['future.png', 60_000], ['sheet.png', 0]]) {
    const date = new Date(NOW + offset);
    fs.utimesSync(path.join(f.target, name), date, date);
  }
  const result = f.plan();
  assert.deepEqual(result.files.map(file => file.relative), ['old.png']);
  assert.equal(result.kept.filter(file => file.reasons.includes('too-new')).length, 4);
  assert.deepEqual(result.kept.find(file => file.relative === 'sheet.png').reasons, ['name', 'too-new']);
  const zero = f.plan([f.target, '--min-age-min', '0']);
  assert(zero.files.some(file => file.relative === 'new.png'));
});

test('từ chối theo realpath: thiếu tmp, đường dẫn bảo vệ, ngoài gốc và tiền tố giả', t => {
  const f = fixture(t);
  const realRoot = fs.realpathSync(f.repoRoot);
  const wt = path.join(f.base, 'typing-game-wt');
  // Kiểm thuần cho đường dẫn không /tmp/ vì os.tmpdir() trên Linux đã chứa /tmp/.
  assert.equal(targetRefusal('/repo/games/x/captures', '/repo', '/typing-game-wt'), 'not-tmp');
  assert.equal(targetRefusal('/repo/tmp-copy', '/repo', '/typing-game-wt'), 'not-tmp');
  assert.equal(targetRefusal('/Users/owner/htdocs/repo/games/x/tmp', '/Users/owner/htdocs/repo', '/Users/owner/htdocs/typing-game-wt'), null);
  assert.equal(targetRefusal(realRoot + '-other/tmp/run', realRoot, wt), 'outside-roots');
  for (const name of ['art-src', 'public', 'docs', 'typing-game-handoff', 'immortality-cultivation']) {
    const dir = path.join(f.repoRoot, 'games/x', name, 'tmp');
    fs.mkdirSync(dir, { recursive: true });
    const result = f.plan([dir]);
    assert.equal(result.targets.length, 0);
    assert.equal(result.files.length, 0);
    assert.equal(result.refused[0].reason, 'protected-path');
  }
  const outside = path.join(f.base, 'outside/tmp');
  fs.mkdirSync(outside, { recursive: true });
  assert.equal(f.plan([outside]).refused[0].reason, 'outside-roots');
  if (!realRoot.includes('/tmp/')) assert.equal(f.plan([f.repoRoot]).refused[0].reason, 'not-tmp');
  assert.equal(main([outside], { repoRoot: f.repoRoot, write() {} }), 2);
  assert.equal(main([outside, f.target], { repoRoot: f.repoRoot, write() {} }), 0);
});

test('chấp nhận ../typing-game-wt, đường dẫn trùng/chồng không xóa hai lần', t => {
  const f = fixture(t);
  const dir = path.join(f.base, 'typing-game-wt/lane/games/x/tmp');
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, 'raw.png');
  fs.writeFileSync(file, 'raw'); fs.utimesSync(file, OLD, OLD);
  f.put('games/x/tmp/run/nested/raw.png');
  const result = f.plan([f.target, f.target, path.join(f.target, 'nested'), dir]);
  assert.equal(result.files.length, 2);
  assert.equal(new Set(result.files.map(file => file.path)).size, 2);
});

test('không theo symlink thư mục hoặc file; symlink ra ngoài ghi refused', t => {
  const f = fixture(t);
  const outside = path.join(f.base, 'outside');
  fs.mkdirSync(outside);
  fs.writeFileSync(path.join(outside, 'secret.png'), 'unchanged');
  const raw = f.put('games/x/tmp/run/raw.png');
  fs.symlinkSync(outside, path.join(f.target, 'linked-dir'));
  fs.symlinkSync(path.join(outside, 'secret.png'), path.join(f.target, 'external.png'));
  fs.symlinkSync(raw, path.join(f.target, 'internal.png'));
  fs.symlinkSync(path.join(f.base, 'missing'), path.join(f.target, 'broken.png'));
  const result = f.plan();
  assert.deepEqual(result.files.map(file => file.relative), ['raw.png']);
  assert.equal(result.refused.length, 4);
  assert.equal(result.refused.find(item => item.path.endsWith('/linked-dir')).reason, 'outside-target');
  assert.equal(result.refused.find(item => item.path.endsWith('/external.png')).reason, 'outside-target');
  assert.equal(f.plan([path.join(f.target, 'linked-dir')]).targets.length, 0);
  assert.equal(fs.readFileSync(path.join(outside, 'secret.png'), 'utf8'), 'unchanged');
});

test('--apply chỉ xóa danh sách tính được; nhật ký đúng và MD5 mọi file giữ nguyên', t => {
  const f = fixture(t);
  const raw = ['raw.PNG', 'nested/raw.jpeg'].map(name => f.put(`games/x/tmp/run/${name}`));
  const keep = ['sheet.png', 'contact.jpg', 'compare.webp', 'Compare-set/raw.png', 'linked.png', 'new.png', 'stats.json', 'notes.md']
    .map(name => f.put(`games/x/tmp/run/${name}`));
  const doc = f.put('docs/report.md', 'tmp/run/linked.png');
  fs.utimesSync(path.join(f.target, 'new.png'), new Date(), new Date());
  const hashes = [...keep, doc].map(file => [file, md5(file)]);
  const json = path.join(f.base, 'result.json');
  assert.equal(main([f.target, '--apply', '--json', json], { repoRoot: f.repoRoot, now: NOW, write() {} }), 0);
  const result = JSON.parse(fs.readFileSync(json, 'utf8'));
  assert.deepEqual([...result.deleted].sort(), [...raw].sort());
  assert.equal(result.logs.length, 1);
  assert.match(path.basename(result.logs[0]), /^\.pruned-\d{8}-\d{4}\.txt$/);
  const log = fs.readFileSync(result.logs[0], 'utf8');
  for (const file of result.files) assert(log.includes(`${file.relative}\t${file.bytes}\n`));
  assert.equal(log.trimEnd().split('\n').length, raw.length);
  assert(raw.every(file => !fs.existsSync(file)));
  for (const [file, hash] of hashes) assert.equal(md5(file), hash);
  assert(result.kept.every(file => Array.isArray(file.reasons) && file.reasons.length));
});

test('không xóa file sửa, mới thêm hoặc thay symlink sau khi tính danh sách', t => {
  const f = fixture(t);
  const changed = f.put('games/x/tmp/run/changed.png');
  const replaced = f.put('games/x/tmp/run/replaced.png');
  const result = f.plan();
  const fresh = f.put('games/x/tmp/run/added.png');
  fs.writeFileSync(changed, 'new content');
  fs.unlinkSync(replaced);
  fs.symlinkSync(changed, replaced);
  assert.equal(applyPlan(result), 1);
  assert.deepEqual(result.deleted, []);
  assert(fs.existsSync(fresh));
  assert.equal(fs.readFileSync(changed, 'utf8'), 'new content');
  assert(fs.lstatSync(replaced).isSymbolicLink());
});

test('không xóa qua thư mục cha bị thay symlink; nhật ký cùng phút không ghi đè', t => {
  const f = fixture(t);
  f.put('games/x/tmp/run/nested/raw.png');
  const result = f.plan();
  const nested = path.join(f.target, 'nested');
  const moved = path.join(f.target, 'moved');
  fs.renameSync(nested, moved);
  fs.symlinkSync(moved, nested);
  const now = new Date(2026, 0, 2, 3, 4);
  assert.equal(applyPlan(result, { now }), 1);
  assert(fs.existsSync(path.join(moved, 'raw.png')));
  const log = path.join(f.target, '.pruned-20260102-0304.txt');
  assert.equal(fs.readFileSync(log, 'utf8'), '');
  const next = f.plan();
  assert.equal(applyPlan(next, { now }), 1);
  assert(fs.existsSync(path.join(moved, 'raw.png')));
  assert.equal(fs.readFileSync(log, 'utf8'), '');
});

test('JSON chạy thử đủ trường, chạy lại được; không ghi vào ảnh, đích hay symlink', t => {
  const f = fixture(t);
  const file = f.put('games/x/tmp/run/raw.png');
  const hash = md5(file);
  const json = path.join(f.base, 'out/result.json');
  assert.equal(main([f.target, '--json', json], { repoRoot: f.repoRoot, now: NOW, write() {} }), 0);
  const result = JSON.parse(fs.readFileSync(json, 'utf8'));
  for (const key of ['targets', 'files', 'kept', 'bytes', 'refused']) assert(Object.hasOwn(result, key));
  assert.equal(result.files.length, 1);
  assert.equal(md5(file), hash);
  const oldJson = md5(json);
  assert.equal(main([f.target, '--json', json], { repoRoot: f.repoRoot, now: NOW, write() {} }), 0);
  assert.equal(md5(json), oldJson);
  assert.throws(() => main([f.target, '--apply', '--json', file], { repoRoot: f.repoRoot, write() {} }), /đuôi .json/);
  const stats = f.put('games/x/tmp/run/stats.json', 'keep');
  assert.throws(() => main([f.target, '--apply', '--json', stats], { repoRoot: f.repoRoot, write() {} }), /ngoài/);
  const link = path.join(f.base, 'link.json');
  fs.symlinkSync(json, link);
  assert.throws(() => main([f.target, '--apply', '--json', link], { repoRoot: f.repoRoot, write() {} }), /không liên kết/);
  const hardlink = path.join(f.base, 'hardlink.json');
  fs.linkSync(json, hardlink);
  assert.throws(() => main([f.target, '--apply', '--json', hardlink], { repoRoot: f.repoRoot, write() {} }), /không liên kết/);
  assert.equal(md5(json), oldJson);
  assert.equal(md5(file), hash);
  assert.equal(fs.readFileSync(stats, 'utf8'), 'keep');
});

test('CLI help, lỗi đối số và mã thoát khi mọi đích bị từ chối', t => {
  const f = fixture(t);
  for (const args of [[], ['x', '--min-age-min', '-1'], ['x', '--min-age-min', 'Infinity'], ['x', '--min-age-min', 'no'], ['x', '--docs'], ['x', '--json'], ['x', '--unknown']]) {
    assert.throws(() => parseArgs(args));
  }
  const script = fileURLToPath(new URL('../prune.mjs', import.meta.url));
  const help = spawnSync(process.execPath, [script, '--help'], { encoding: 'utf8' });
  assert.equal(help.status, 0);
  assert.match(help.stdout, /--apply/);
  const denied = spawnSync(process.execPath, [script, f.target, '--docs', f.repoRoot], { encoding: 'utf8' });
  assert.equal(denied.status, 2);
  assert.match(denied.stdout, /Từ chối/);
  const invalid = spawnSync(process.execPath, [script, '--min-age-min', '-1'], { encoding: 'utf8' });
  assert.equal(invalid.status, 1);
});
