import test, { after, mock } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { scanAudio, main, parseAttribution } from '../scan-audio.mjs';
import { scan } from '../scan.mjs';

const repo = fileURLToPath(new URL('../../../', import.meta.url));
// macOS có /var → /private/var; chuẩn hóa cây test trước khi kiểm symlink.
const temporary = fs.realpathSync(fs.mkdtempSync(path.join(os.tmpdir(), 'al08-audio-')));
const inside = (base, p) => { const r = path.relative(base, path.resolve(String(p))); return r === '' || (!r.startsWith('..' + path.sep) && r !== '..' && !path.isAbsolute(r)); };
const writes = [], reads = [];
let liveOutput = false;
const denied = /immortality-cultivation|tu[-_]tien|TU_TIEN_|(?:^|\/)monkeytype(?:\/|$)/iu;
const mutators = ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'cp', 'symlink', 'link', 'unlink', 'rm', 'rmdir', 'truncate', 'chmod', 'chown', 'utimes', 'mkdtemp'];
function guard(p, op) {
  assert.ok(inside(temporary, p) || (liveOutput && inside(path.join(repo, 'library/out'), p)), `K1: ghi ngoài phạm vi: ${op} ${p}`);
  writes.push({ op, path: String(p) });
}
for (const name of mutators) {
  for (const key of [name, name + 'Sync']) if (typeof fs[key] === 'function') {
    const original = fs[key];
    mock.method(fs, key, function (...args) {
      guard(args[0], key);
      if (['rename', 'copyFile', 'cp', 'symlink', 'link'].includes(name)) guard(args[1], key);
      return original.apply(this, args);
    });
  }
  if (typeof fs.promises[name] === 'function') {
    const original = fs.promises[name];
    mock.method(fs.promises, name, function (...args) {
      guard(args[0], `promises.${name}`);
      if (['rename', 'copyFile', 'cp', 'symlink', 'link'].includes(name)) guard(args[1], name);
      return original.apply(this, args);
    });
  }
}
for (const [object, key] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
  const original = object[key];
  mock.method(object, key, function (p, flags, ...args) {
    if (typeof flags === 'number' ? flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_APPEND | fs.constants.O_TRUNC) : /[wa+]/u.test(flags)) guard(p, key);
    else {
      assert.ok(!denied.test(String(p)), 'Không mở vùng cấm');
      assert.ok(!String(p).includes('/AudioLab/libraries/') || !/\.(?:ogg|wav|mp3|m4a)$/u.test(String(p)), 'Không mở lại media AudioLab libraries');
      reads.push(String(p));
    }
    return original.call(this, p, flags, ...args);
  });
}
const originalStream = fs.createWriteStream;
mock.method(fs, 'createWriteStream', function (p, ...args) { guard(p, 'createWriteStream'); return originalStream.call(this, p, ...args); });
// Dùng cùng lớp bọc promises cho cả scanner lẫn lệnh CLI/tích hợp.
const io = new Proxy(fs.promises, { get(target, key) {
  const method = target[key];
  if (typeof method !== 'function') return method;
  return (...args) => {
    if (['readFile', 'lstat', 'readdir'].includes(key)) {
      assert.ok(!denied.test(String(args[0])), `Không đọc vùng cấm: ${args[0]}`);
      if (key === 'readFile') {
        assert.ok(!String(args[0]).includes('/AudioLab/libraries/') || !/\.(?:ogg|wav|mp3|m4a)$/u.test(String(args[0])), 'Không băm lại thư viện AudioLab');
        reads.push(String(args[0]));
      }
    }
    return method.apply(target, args);
  };
} });
after(() => { fs.rmSync(temporary, { recursive: true }); mock.restoreAll(); });

const hash = b => createHash('sha256').update(b).digest('hex');
const md5 = b => createHash('md5').update(b).digest('hex');
function wav(value) {
  const b = Buffer.alloc(244, value); b.write('RIFF'); b.writeUInt32LE(236, 4); b.write('WAVEfmt ', 8);
  b.writeUInt32LE(16, 16); b.writeUInt16LE(1, 20); b.writeUInt16LE(1, 22); b.writeUInt32LE(1000, 24);
  b.writeUInt32LE(2000, 28); b.writeUInt16LE(2, 32); b.writeUInt16LE(16, 34); b.write('data', 36); b.writeUInt32LE(200, 40); return b;
}
function write(root, rel, value) { const p = path.join(root, rel); fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, value); }
function fixture(name) {
  const root = path.join(temporary, name), lab = path.join(root, 'AudioLab');
  for (const file of ['sources.json', 'taxonomy.json', 'licences.json']) write(root, 'library/' + file, fs.readFileSync(path.join(repo, 'library', file)));
  const a = wav(1), b = wav(2), confirm = wav(3), force = wav(4);
  const files = [a, b, confirm, force].map((buffer, i) => ({ file: 'kenney/interface-sounds/Audio/' + ['click_001.ogg', 'click_002.ogg', 'confirmation_001.ogg', 'forceField_000.ogg'][i], library: 'kenney', family: 'phim-ui/click', key: 'click', licence: 'CC0-1.0', sha256: hash(buffer), bytes: buffer.length, duration: 0.1, sample_rate: 1000, channels: 1, format: 'WAV', subtype: 'PCM_16' }));
  // Cây mẫu chỉ có index, không tạo media bên ngoài: kiểm việc chỉ đọc siêu dữ liệu.
  write(lab, 'libraries/index.json', JSON.stringify({ files }));
  write(lab, 'libraries/SOURCES.jsonl', JSON.stringify({ path: 'kenney/interface-sounds', author: 'Kenney', licence: 'CC0-1.0', commercial_ok: true, ai_input_allowed: false, attribution_required: false, url: 'https://example.invalid/pack' }) + '\n');
  const prefix = 'games/space-typing/';
  write(root, prefix + 'src/assets/audio/ui/click.ogg', b);
  for (const rel of ['public/assets/audio/sfx/kenney/confirm.ogg', 'src/assets/audio/ui/confirm.ogg']) write(root, prefix + rel, confirm);
  for (const rel of ['public/assets/audio/sfx/kenney/force-field.ogg', 'src/assets/audio/ui/deploy.ogg']) write(root, prefix + rel, force);
  write(root, prefix + 'public/assets/audio/duel/war/gun-a.ogg', a);
  write(root, prefix + 'public/assets/audio/unknown-001.ogg', wav(8));
  write(root, prefix + 'public/assets/audio/unknown-002.ogg', wav(9));
  write(root, prefix + 'public/assets/audio/ATTRIBUTION.md', '## Menu / UI SFX — Kenney\n| File | Source file |\n| `click.ogg` | Interface `click_002.ogg` |\n## Duel war SFX — Freesound (CC0)\n| `gun-a.ogg` | Sci Fi Gun Shot.wav (#317136) | Bird_man | https://freesound.org/people/Bird_man/sounds/317136/ |\n');
  write(root, prefix + 'src/audio/Sfx.ts', 'const bank = import.meta.glob<string>("../assets/audio/ui/*.ogg", { eager: true });\nthis.uiFile("click", .2);\nconst url = "/assets/audio/duel/war/gun-a.ogg";\n// const ignored = "/assets/audio/unknown-001.ogg";\n');
  write(root, prefix + 'art-src/Dota-Sounds/private.wav', a);
  write(root, 'shared/music/album/song.mp3', b);
  write(root, 'media/private.md5', `${md5(b)}  shared/music/album/song.mp3\n${md5(a)}  ${prefix}art-src/Dota-Sounds/private.wav\n`);
  write(root, prefix + 'media.md5', `${md5(b)}  src/assets/audio/ui/click.ogg\n`);
  write(root, 'tools/audio-lab/build/legacy-audio.json', JSON.stringify({ 'space-typing': { files: { 'src/assets/audio/ui/click.ogg': hash(b) } } }));
  write(lab, 'work/run/manifest.fragment.json', JSON.stringify({ sounds: { 'ui.demo': { files: ['sfx/ui/demo-1.ogg'], durationMs: [100], family: 'phim-ui', loop: false } } }));
  write(lab, 'work/run/SOURCES.json', JSON.stringify({ 'sfx/ui/demo-1.ogg': { id: 'ui.demo', family: 'phim-ui', game: 'space-typing', sha256: hash(a), durationMs: 100, sampleRate: 1000, channels: 1 } }));
  write(lab, 'work/run/sfx/ui/demo-1.ogg', a);
  write(lab, 'work/incomplete/manifest.fragment.json', '{"sounds":{"incomplete":{"files":["bad.ogg"]}}}');
  write(lab, 'work/orphan/masters/orphan.wav', a);
  return { root, lab };
}
const click = result => result.cards.find(c => c.uid === 'kenney:interface-sounds/Audio/click');

test('Bảng ATTRIBUTION giữ file nguồn Kenney và số, tác giả, URL Freesound', () => {
  const rows = parseAttribution(fs.readFileSync(path.join(repo, 'games/space-typing/public/assets/audio/ATTRIBUTION.md'), 'utf8'));
  assert.equal(rows.size, 41);
  assert.equal(rows.get('src/assets/audio/ui/click.ogg').sourceFile, 'Interface click_002.ogg');
  assert.deepEqual(Object.fromEntries(['soundId', 'author', 'url'].map(k => [k, rows.get('public/assets/audio/duel/war/gun-a.ogg')[k]])), { soundId: '317136', author: 'Bird_man', url: 'https://freesound.org/people/Bird_man/sounds/317136/' });
});

test('Cây mẫu: gom biến thể, master ngoài repo, bản sao, giấy phép, dùng mã và nháp', async t => {
  const { root, lab } = fixture('core');
  const before = writes.length;
  const r = await scanAudio({ repoRoot: root, audioLabRoot: lab, io });
  assert.equal(writes.length, before, 'scanAudio không ghi bất kỳ file nào');
  assert.equal(r.stats.spaceFiles, 8); assert.equal(r.stats.externalFiles, 4); assert.equal(r.stats.kenneyCopies, 6);
  const c = click(r);
  assert.equal(c.kind, 'ui'); assert.ok(c.aliases.includes('phim-ui/click')); assert.equal(c.audio.variants, 2);
  assert.equal(c.copies.find(f => f.path.endsWith('/click.ogg')).variant, '002');
  assert.equal(c.copies.find(f => f.path.endsWith('/click.ogg')).onDrive, 'yes');
  assert.ok(c.files.filter(f => f.role !== 'copy').every(f => f.onDrive === 'external'));
  assert.equal(c.licence.aiInputAllowed, false, 'Chặn AI từ ledger thắng mặc định CC0');
  assert.ok(c.usedBy.some(r => r.ref.endsWith('Sfx.ts:1') && r.confidence === 'folder'));
  assert.ok(c.usedBy.some(r => r.ref.endsWith('Sfx.ts:2') && r.confidence === 'path'));
  assert.ok(c.usedBy.some(r => r.ref.endsWith('Sfx.ts:3') && r.confidence === 'path'));
  const unknown = r.cards.find(c => c.uid.endsWith('public/assets/audio/unknown'));
  assert.equal(unknown.files.length, 2); assert.equal(unknown.licence.id, 'unknown'); assert.equal(unknown.usedBy.length, 0);
  assert.equal(r.duplicates.length, 2);
  assert.equal(r.stats.dotaFiles, 1); assert.equal(r.stats.privateMusic, 1);
  assert.ok(r.cards.filter(c => c.private).every(c => c.licence.private && c.licence.notForRelease && c.files[0].audio.durationMs === 100));
  assert.equal(r.stats.workRuns, 1); assert.equal(r.stats.hiddenWorkCards, 1); assert.equal(r.cards.filter(c => c.status === 'draft').length, 0);
  const complete = await scanAudio({ repoRoot: root, audioLabRoot: lab, io, all: true });
  const draft = complete.cards.find(c => c.status === 'draft');
  assert.equal(draft.kind, 'ui'); assert.equal(draft.hidden, true); assert.equal(draft.files[0].sourceRow.id, 'ui.demo');
  assert.equal(draft.files[0].audio.codec, 'pcm_s16le'); assert.equal(complete.stats.hiddenWorkCards, 0);
  const locked = await scanAudio({ repoRoot: root, audioLabRoot: lab, io, locksOnly: true });
  assert.equal(locked.stats.spaceFiles, 1); assert.equal(click(locked).copies[0].local, false);
  assert.equal(locked.stats.privateMusic, 1); assert.equal(locked.stats.dotaFiles, 1);
  assert.equal(locked.stats.workCards, 0);
  t.diagnostic(`K1 đọc cây mẫu: 0 ghi; ${r.stats.externalFiles} file ngoài chỉ đọc index; ${r.stats.spaceFiles} file Space; 2 nhóm trùng.`);
});

test('Chặn symlink nguồn, đường index thoát gốc, vùng cấm và output symlink', async () => {
  const { root, lab } = fixture('blocked');
  const outside = path.join(temporary, 'outside'); fs.mkdirSync(outside);
  write(outside, 'secret.ogg', wav(6));
  fs.symlinkSync(outside, path.join(root, 'games/space-typing/public/assets/audio/linked'));
  const indexFile = path.join(lab, 'libraries/index.json');
  const index = JSON.parse(fs.readFileSync(indexFile));
  const deniedPaths = ['../escape.wav', '/absolute.wav', 'kenney/../../escape.wav', 'kenney/tu-tien/audio.wav', 'games/immortality-cultivation/audio.wav', 'games/monkeytype/audio.wav'];
  for (const file of deniedPaths) index.files.push({ ...index.files[0], file });
  fs.writeFileSync(indexFile, JSON.stringify(index));
  const r = await scanAudio({ repoRoot: root, audioLabRoot: lab, io });
  assert.equal(r.stats.externalFiles, 4); assert.equal(r.stats.spaceFiles, 8);
  assert.ok(!denied.test(JSON.stringify(r))); assert.ok(!JSON.stringify(r).includes('secret.ogg'));
  fs.symlinkSync(outside, path.join(root, 'library/out'));
  await assert.rejects(main([], { repoRoot: root, audioLabRoot: lab, io }), /symlink/u);
  assert.deepEqual(fs.readdirSync(outside), ['secret.ogg']);
});

test('K1 CLI và tích hợp scan chỉ ghi library/out trong cây test', async t => {
  const { root, lab } = fixture('cli');
  let before = writes.length;
  await main(['--all'], { repoRoot: root, audioLabRoot: lab, io });
  const output = JSON.parse(fs.readFileSync(path.join(root, 'library/out/audio-catalog.json')));
  assert.equal(output.schema, 'asset-library-audio/1'); assert.ok(output.cards.some(c => c.status === 'draft'));
  const cliWrites = writes.slice(before);
  assert.equal(cliWrites.length, 2); assert.ok(cliWrites.every(w => inside(path.join(root, 'library/out'), w.path)));
  // Kho ngoài được thay bằng nguồn vắng trong test tích hợp để giữ test độc lập máy.
  const integratedIo = new Proxy(io, { get(target, key) { if (['lstat', 'readFile', 'readdir'].includes(key)) return (...args) => {
    if (String(args[0]).includes('/AudioLab') && !inside(temporary, args[0])) { const e = new Error('Nguồn ngoài bị tắt trong test tích hợp'); e.code = 'ENOENT'; return Promise.reject(e); }
    return target[key](...args);
  }; return target[key]; } });
  before = writes.length;
  const integrated = await scan({ repoRoot: root, game: 'space-typing', io: integratedIo });
  assert.equal(integrated.stats.audio.spaceFiles, 8);
  assert.ok(integrated.catalog.cards.some(c => c.type === 'audio'));
  assert.ok(integrated.catalog.warnings.some(w => w.startsWith('Âm trùng byte')));
  assert.ok(writes.slice(before).every(w => inside(path.join(root, 'library/out'), w.path)));
  t.diagnostic(`K1 CLI: ${cliWrites.length} lời gọi ghi; tích hợp: ${writes.length - before}; 0 ngoài library/out.`);
});

let real;
test('K1 và sáu kiểm thật: Space, Kenney, byte trùng, riêng tư, nháp, usedBy', async t => {
  const lab = path.join(os.homedir(), 'AudioLab');
  let hasLab = true;
  try { fs.accessSync(path.join(lab, 'libraries/index.json'), fs.constants.R_OK); }
  catch (e) { hasLab = false; t.diagnostic(`BỎ QUA đối chiếu AudioLab thật: ${e.code}; Claude cần chạy lại khi đọc được ~/AudioLab.`); }
  const before = writes.length;
  real = await scanAudio({ io });
  assert.equal(writes.length, before, 'K1: quét thật có 0 lời gọi ghi');
  assert.equal(real.stats.spaceFiles, 116);
  const space = real.cards.flatMap(c => c.files).filter(f => /^games\/space-typing\/(?:public\/assets|src\/assets)\/audio\//u.test(f.path));
  assert.equal(new Set(space.map(f => f.path)).size, 116);
  assert.ok(space.every(f => f.audio?.durationMs >= 0));
  assert.equal(real.duplicates.length, 2);
  assert.ok(real.duplicates.some(d => d.paths.every(p => p.endsWith('/confirm.ogg'))));
  assert.ok(real.duplicates.some(d => d.paths.some(p => p.endsWith('/sfx/kenney/force-field.ogg')) && d.paths.some(p => p.endsWith('/ui/deploy.ogg'))));
  assert.equal(real.stats.dotaFiles, 15); assert.equal(real.stats.privateMusic, 193);
  const dota = real.cards.filter(c => c.files.some(f => f.path.includes('/Dota-Sounds/')));
  const music = real.cards.filter(c => c.origin === 'private-music');
  assert.equal(dota.flatMap(c => c.files).length, 15); assert.equal(music.flatMap(c => c.files).length, 193);
  assert.ok([...dota, ...music].every(c => c.licence.private && c.licence.notForRelease && c.files.every(f => f.onDrive === 'private' && f.audio)));
  assert.equal(real.cards.filter(c => c.status === 'draft' || c.uid.startsWith('audiolab:work/')).length, 0);
  assert.ok(!denied.test(JSON.stringify(real)), 'K3: không có chuỗi vùng cấm trong output');
  if (hasLab) {
    assert.equal(real.stats.externalFiles, 1859); assert.equal(real.stats.kenneyCopies, 29);
    const c = click(real); assert.ok(c);
    assert.equal(c.files.filter(f => f.role !== 'copy').length, 5);
    const copy = c.copies.find(f => f.path === 'games/space-typing/src/assets/audio/ui/click.ogg');
    assert.equal(copy.variant, '002'); assert.ok(copy.copyOf.endsWith('click_002.ogg'));
    assert.ok(c.usedBy.some(r => r.ref === 'games/space-typing/src/audio/Sfx.ts:36' && r.confidence === 'folder'));
    assert.ok(c.usedBy.some(r => r.ref === 'games/space-typing/src/audio/Sfx.ts:672'));
    assert.equal(real.stats.externalMediaReads, 0);
  }
  t.diagnostic(JSON.stringify({ ...real.stats, duplicateGroups: real.duplicates.length, warnings: real.warnings.length, realScanWrites: writes.length - before }));
});

test('Sinh JSON thật dưới lớp bọc K1, chỉ library/out', async t => {
  liveOutput = true;
  const before = writes.length;
  try { await main([], { io }); } finally { liveOutput = false; }
  const actual = writes.slice(before);
  assert.equal(actual.length, 2); assert.ok(actual.every(w => inside(path.join(repo, 'library/out'), w.path)));
  t.diagnostic(`K1 sinh thật: ${actual.length} lời gọi ghi (mkdir, writeFile); 0 ngoài library/out. K3: 0 chuỗi vùng cấm.`);
});
