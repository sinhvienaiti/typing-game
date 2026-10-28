import test from 'node:test';
import assert from 'node:assert/strict';
import * as fs from 'node:fs/promises';
import { constants } from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { generateThumbs, loadCards, loadThumbIndex, runProcess, runThumbs, waveGain, WAVE_DRAW, MIN_FREE, MAX_FILE, MAX_TOTAL } from '../thumbs.mjs';

const hash = (data, algorithm = 'md5') => createHash(algorithm).update(data).digest('hex');
const fakeWebp = Buffer.concat([Buffer.from('RIFF'), Buffer.alloc(4), Buffer.from('WEBPVP8 '), Buffer.alloc(16)]);
const fakePng = Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), Buffer.alloc(30)]);
const mutations = ['writeFile', 'appendFile', 'mkdir', 'mkdtemp', 'unlink', 'rm', 'rmdir', 'truncate', 'chmod', 'utimes'];
const card = (uid, file, type = 'image', extra = {}) => ({ uid, type, status: 'unscored', files: [file], ...extra });
const image = (p, md5 = hash(p)) => ({ path: p, role: 'concept', md5, local: true });
const model = (p, md5 = hash(p)) => ({ path: p, role: 'glb-original', md5, local: true });

// K1: mọi API ghi (kể cả API công cụ hiện chưa dùng) đều qua hàng rào này.
function guardedIo(root, writes) {
  const cache = path.join(root, 'library/.thumbs');
  const check = value => {
    const p = path.resolve(value instanceof URL ? fileURLToPath(value) : value);
    assert.ok(p === cache || p.startsWith(cache + path.sep), `K1: ghi ngoài .thumbs: ${p}`);
    writes.push(p);
  };
  const io = { ...fs };
  for (const name of mutations) io[name] = (p, ...args) => { check(p); return fs[name](p, ...args); };
  for (const name of ['rename', 'link']) io[name] = (from, to, ...args) => {
    check(from); check(to); return fs[name](from, to, ...args);
  };
  for (const name of ['copyFile', 'symlink']) io[name] = (from, to, ...args) => {
    check(to); return fs[name](from, to, ...args);
  };
  io.open = (p, flags, ...args) => {
    if (typeof flags === 'number'
      ? flags & (constants.O_WRONLY | constants.O_RDWR | constants.O_CREAT | constants.O_TRUNC | constants.O_APPEND)
      : /[wa+]/u.test(flags)) check(p);
    return fs.open(p, flags, ...args);
  };
  return io;
}

async function fixture(t) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'al13-thumbs-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  const writes = [], calls = [];
  let output = '';
  const io = guardedIo(root, writes);
  io.statfs = async () => ({ bavail: BigInt(MIN_FREE), bsize: 2n });
  const options = { repoRoot: root, home: root, io, stdout: { write: s => { output += s; } },
    magick: 'fake-magick', ffmpeg: 'fake-ffmpeg', blender: 'fake-blender' };
  options.exec = async (command, args, opts) => {
    calls.push({ command, args, opts });
    if (args.includes('-version') || args.includes('--python-expr')) return Buffer.from('available');
    if (command === 'fake-blender') {
      const target = args.at(-1);
      await io.writeFile(target, fakePng, { flag: 'wx' });
      return Buffer.alloc(0);
    }
    if (command === 'fake-ffmpeg' && args.includes('null')) return Buffer.from('frame:0\nlavfi.astats.Overall.Peak_level=-31.500000\n');
    if (command === 'fake-ffmpeg' || args.at(-1) === 'png:-') return fakePng;
    return fakeWebp;
  };
  async function put(rel, bytes = 'source') {
    const target = path.join(root, rel);
    await fs.mkdir(path.dirname(target), { recursive: true });
    await fs.writeFile(target, bytes);
    return target;
  }
  async function run(cards) { return generateThumbs({ ...options, cards }); }
  return { root, options, io, calls, writes, put, run, output: () => output };
}

test('K1: hình + GLB liên kết + âm chỉ ghi .thumbs; lượt hai 0 lần ghi, 0 subprocess', async t => {
  const f = await fixture(t);
  const p = 'games/dragon-hold/art-src/houses/herb-hut.png';
  const g = 'games/dragon-hold/art-src/3d/houses/herb-hut.glb';
  const wav1 = '~/AudioLab/libraries/cc0/click-1.wav', wav2 = '~/AudioLab/libraries/cc0/click-2.wav';
  await f.put(p); await f.put(g); await f.put(wav1.slice(2)); await f.put(wav2.slice(2));
  const img = image(p), glb = model(g);
  const cards = [card('dragon-hold:houses/herb-hut', img, 'image', { name: 'Herb Hut' }),
    card('dragon-hold:model', glb, 'model3d', { files: [glb, img] }),
    card('cc0:click', null, 'audio', { files: [
      { path: wav2, role: 'variant', variant: '2', sha256: hash('two', 'sha256') },
      { path: wav1, role: 'variant', variant: '1', sha256: hash('one', 'sha256') },
    ] })];
  const first = await f.run(cards);
  assert.equal(first.covered, 3); assert.equal(first.created, 2); assert.equal(first.reused, 1);
  assert.equal(first.blenderRenders, 0); assert.equal(first.missing.length, 0);
  assert.ok(first.maxBytes <= MAX_FILE); assert.ok(first.totalBytes <= MAX_TOTAL);
  assert.equal(first.thumbnails[2].source, wav1);
  // Âm nhỏ được đo đỉnh rồi đưa về −1 dBFS trước khi vẽ: −31,5 dB → +30,5 dB.
  assert.ok(f.calls.find(c => c.command === 'fake-ffmpeg' && c.args.includes('-filter_complex')).args
    .includes(`aformat=channel_layouts=mono,volume=30.50dB,${WAVE_DRAW}`));
  assert.equal(waveGain('Peak_level=-inf\n'), 0); assert.equal(waveGain('Peak_level=-80\n'), 40);
  assert.equal(waveGain('Peak_level=-12\nPeak_level=-0.2\n'), 0);
  const index = await fs.readFile(path.join(f.root, 'library/.thumbs/index.json'));
  f.calls.length = 0; f.writes.length = 0;
  const second = await f.run(cards);
  assert.equal(second.created, 0); assert.equal(second.reused, 3);
  assert.deepEqual(f.calls, []); assert.deepEqual(f.writes, []);
  assert.deepEqual(await fs.readFile(path.join(f.root, 'library/.thumbs/index.json')), index);
  assert.match(f.output(), /File lớn nhất: \d+ byte; tổng: \d+ byte/u);
});

test('ổ còn dưới 20 GiB: dừng trước mọi ghi, đọc nguồn và chạy công cụ', async t => {
  const f = await fixture(t);
  f.io.statfs = async () => ({ bavail: BigInt(MIN_FREE - 1), bsize: 1n });
  f.io.readFile = () => { throw new Error('Không được đọc nguồn'); };
  const result = await f.run([card('test:image', image('missing.png'))]);
  assert.equal(result.stopped, true); assert.equal(result.created, 0);
  assert.match(f.output(), /Dừng:.*cần ít nhất 20 GiB/u);
  assert.deepEqual(f.writes, []); assert.deepEqual(f.calls, []);
  assert.deepEqual(await fs.readdir(f.root), []);
  assert.equal(await runThumbs([], f.options), 1);
});

test('dung lượng giảm giữa lượt: không tạo file kế tiếp hoặc index', async t => {
  const f = await fixture(t); let n = 0;
  f.io.statfs = async () => ({ bavail: BigInt(++n <= 2 ? MIN_FREE : 0), bsize: 1n });
  await f.put('a.png'); await f.put('b.png');
  const result = await f.run([card('a', image('a.png')), card('b', image('b.png'))]);
  assert.equal(result.stopped, true); assert.equal(result.created, 1);
  assert.deepEqual(await fs.readdir(path.join(f.root, 'library/.thumbs')), [hash('a.png') + '.webp']);
});

test('GLB chỉ render khi không có ảnh; giới hạn 150 lần/lượt; cùng md5 dùng chung', async t => {
  const f = await fixture(t), cards = [];
  for (let i = 0; i < 151; i++) {
    const p = `models/${i}.glb`; await f.put(p);
    cards.push(card(`model:${i}`, model(p), 'model3d'));
  }
  cards.push(card('model:duplicate', model('models/0.glb'), 'model3d'));
  const result = await f.run(cards);
  assert.equal(result.blenderRenders, 150); assert.equal(result.created, 150);
  assert.equal(result.covered, 151); assert.equal(result.missing.length, 1);
  assert.match(result.missing[0].reason, /trần 150/u);
  const renders = f.calls.filter(c => c.command === 'fake-blender' && c.args.includes('-P'));
  assert.equal(renders.length, 150);
  for (const call of renders) {
    assert.ok(call.args.includes('-b'));
    assert.match(call.args.at(-1), /library\/\.thumbs\/[a-f0-9]{32}\.webp$/u);
  }
  assert.match(f.output(), /Blender 150\/150/u);
});

test('SOURCES.usedBy và preset.source nối ảnh nguồn, canonical curated thắng hero', async t => {
  const f = await fixture(t);
  const p = 'games/typing-defense/art-src/buildings/hut.png';
  const alt = 'games/typing-defense/art-src/buildings/hut-v2.png';
  const g = 'games/typing-defense/art-src/models/props/hut.glb';
  await f.put(p); await f.put(alt); await f.put(g);
  await f.put('games/typing-defense/art-src/3d/SOURCES.json', JSON.stringify({ files: {
    'buildings/hut.glb': { image: 'art-src/buildings/hut.png', usedBy: ['props/hut'] },
  } }));
  const result = await f.run([card('test:model', model(g), 'model3d'),
    card('test:image', image(p), 'image', { hero: p, canonical: { concept: alt }, files: [image(p), image(alt)] })]);
  assert.equal(result.blenderRenders, 0); assert.equal(result.covered, 2);
  assert.equal(result.thumbnails[0].source, alt); assert.equal(result.thumbnails[1].source, alt);
  await f.put('games/typing-defense/scripts/models/presets/static.json', JSON.stringify({ models: {
    'other/hut': { source: 'buildings/hut.glb' },
  } }));
  const runtime = 'games/typing-defense/public/assets/typing-defense/models/other/hut/hut.high.glb';
  await f.put(runtime);
  const next = await f.run([card('test:runtime', { ...model(runtime), role: 'runtime-high' }, 'model3d')]);
  assert.equal(next.blenderRenders, 0); assert.equal(next.thumbnails[0].source, p);
  const sameKey = 'games/typing-defense/art-src/models/buildings/hut.glb';
  await f.put(sameKey);
  const mirror = await f.run([card('test:mirror', model(sameKey), 'model3d')]);
  assert.equal(mirror.blenderRenders, 0); assert.equal(mirror.thumbnails[0].source, p);
});

test('dùng ảnh liên kết theo md5 của thẻ khác; không render khi ảnh liên kết vắng', async t => {
  const f = await fixture(t), p = 'source.png'; await f.put(p); await f.put('source.glb'); await f.put('copy.glb');
  const shared = hash('shared');
  const result = await f.run([
    card('source', null, 'model3d', { files: [model('source.glb', shared), image(p)] }),
    card('copy', model('copy.glb', shared), 'model3d'),
    card('absent', null, 'model3d', { files: [model('source.glb'), image('absent.png')] }),
  ]);
  assert.equal(result.covered, 2); assert.equal(result.created, 1); assert.equal(result.blenderRenders, 0);
  assert.match(result.missing[0].reason, /Ảnh nguồn liên kết không có/u);
});

test('thiếu công cụ/quyền AudioLab: báo rõ, không thay biến thể đầu, không tạo ảnh giả', async t => {
  const f = await fixture(t); await f.put('image.png'); await f.put('a.glb'); await f.put('second.wav');
  f.options.exec = async command => { throw new Error(`ENOENT ${command}`); };
  const result = await f.run([card('image', image('image.png')), card('model', model('a.glb'), 'model3d'),
    card('audio', null, 'audio', { files: [
      { path: '~/AudioLab/libraries/no-access/first.wav', variant: 1, sha256: hash('one', 'sha256') },
      { path: 'second.wav', variant: 2, sha256: hash('two', 'sha256') },
    ] })]);
  assert.equal(result.created, 0); assert.equal(result.missing.length, 3);
  assert.match(f.output(), /Bỏ qua fake-magick: ENOENT/u);
  assert.match(f.output(), /first.wav/u);
});

test('K3 và K1: chặn đường cấm, traversal, symlink nguồn và symlink cache', async t => {
  const f = await fixture(t); await f.put('ok.png');
  // Danh sách cấm trong test, không đọc cây thật.
  const banned = 'games/immortality-cultivation/image.png';
  const originalLstat = f.io.lstat;
  f.io.lstat = (p, ...args) => {
    assert.ok(!String(p).includes('immortality-cultivation'), 'Không được lstat đường cấm');
    return originalLstat(p, ...args);
  };
  await fs.symlink(path.join(f.root, 'ok.png'), path.join(f.root, 'link.png'));
  const result = await f.run([
    card('hidden', image('ok.png'), 'image', { status: 'draft' }),
    card('immortality-cultivation:paused', image(banned)),
    card('bad-source', image(banned)), card('traversal', image('../outside.png')),
    card('symlink', image('link.png')), card('ok', image('ok.png')),
  ]);
  assert.equal(result.visible, 4); assert.equal(result.covered, 1);
  const index = await fs.readFile(path.join(f.root, 'library/.thumbs/index.json'), 'utf8');
  assert.doesNotMatch(index, /immortality-cultivation|tu-tien/u);
  const other = await fixture(t);
  await fs.mkdir(path.join(other.root, 'library'));
  await fs.symlink(f.root, path.join(other.root, 'library/.thumbs'));
  await assert.rejects(other.run([]), /symlink/u);
});

test('cache quá cỡ/hỏng không bị ghi đè; tổng cache cũ cũng tính vào trần', async t => {
  const f = await fixture(t); await f.put('a.png');
  await f.put(`library/.thumbs/${hash('a.png')}.webp`, Buffer.alloc(MAX_FILE + 1));
  const before = await fs.readFile(path.join(f.root, `library/.thumbs/${hash('a.png')}.webp`));
  await assert.rejects(f.run([card('a', image('a.png'))]), /40 KB/u);
  assert.deepEqual(await fs.readFile(path.join(f.root, `library/.thumbs/${hash('a.png')}.webp`)), before);
  const other = await fixture(t);
  await other.put('library/.thumbs/' + hash('old') + '.webp', fakeWebp);
  const stat = other.io.lstat;
  other.io.lstat = async (p, ...args) => {
    const info = await stat(p, ...args);
    if (String(p).endsWith('.webp')) return { ...info, isFile: () => true, isSymbolicLink: () => false, size: MAX_TOTAL + 1 };
    return info;
  };
  await assert.rejects(other.run([]), /150 MB/u);
});

test('đọc đúng AL-12, gộp âm không trùng uid, không sửa catalog hay curated', async t => {
  const f = await fixture(t);
  const before = { schema: 'asset-library/1', cards: [card('a', image('a.png'), 'image', { name: 'Old' })] };
  await f.put('library/out/catalog.json', JSON.stringify(before));
  await f.put('library/out/audio-catalog.json', JSON.stringify({ schema: 'asset-library-audio/1', cards: [card('sound', null, 'audio', { files: [] })] }));
  const row = { uid: 'a', name: 'Reviewed Hut', kind: 'building', subkind: 'hut', reviewed: 'claude-2026-10-28', canonical: { concept: 'v2.png' } };
  await f.put('library/curated/game.jsonl', JSON.stringify(row) + '\n');
  const loaded = await loadCards(f.options);
  assert.equal(loaded.length, 2); assert.equal(loaded[0].name, row.name);
  assert.equal(loaded[0].kind, row.kind); assert.deepEqual(loaded[0].canonical, row.canonical);
  assert.deepEqual(f.writes, []);
  assert.deepEqual(JSON.parse(await fs.readFile(path.join(f.root, 'library/out/catalog.json'))), before);
});

test('bảng nối lớn chia phần dưới 40 KB; đọc lại đủ thẻ, lượt hai không ghi gì', async t => {
  const f = await fixture(t); await f.put('image.png');
  const cards = Array.from({ length: 300 }, (_, i) => card(`model:${i}`, image('image.png'), 'image', { name: 'Reviewed Hut ' + i }));
  const first = await f.run(cards);
  const root = JSON.parse(await fs.readFile(path.join(f.root, 'library/.thumbs/index.json')));
  assert.ok(root.parts.length > 1);
  assert.deepEqual((await loadThumbIndex(f.options)).thumbnails, JSON.parse(JSON.stringify(first.thumbnails)));
  for (const name of await fs.readdir(path.join(f.root, 'library/.thumbs'))) {
    assert.ok((await fs.stat(path.join(f.root, 'library/.thumbs', name))).size <= MAX_FILE);
  }
  f.writes.length = 0;
  assert.equal((await f.run(cards)).created, 0); assert.deepEqual(f.writes, []);
  // Bảng nối đổi (thêm thẻ): phần cũ không còn được trỏ tới bị dọn, không tích rác.
  await f.run([card('model:new', image('image.png'), 'image', { name: 'Reviewed Hut new' }), ...cards]);
  const parts = JSON.parse(await fs.readFile(path.join(f.root, 'library/.thumbs/index.json'))).parts;
  const onDisk = (await fs.readdir(path.join(f.root, 'library/.thumbs'))).filter(n => n.startsWith('index-'));
  assert.deepEqual(onDisk.sort(), [...parts].sort());
  assert.ok(root.parts.some(n => !parts.includes(n)), 'phải có ít nhất một phần cũ bị thay');
});

test('ImageMagick + ffmpeg thật: cạnh dài 256, PNG một biến thể, mỗi file ≤40 KB, lượt hai tạo 0', async t => {
  const f = await fixture(t), magick = '/opt/homebrew/bin/magick';
  try { await runProcess(magick, ['-version']); await runProcess('ffmpeg', ['-version']); }
  catch (error) { t.skip(`Bỏ qua phần thật: thiếu magick/ffmpeg: ${error.message}`); return; }
  // Alpha nhiều chi tiết: kiểm cả giới hạn cỡ cho sprite, không chỉ ảnh RGB.
  const raw = await runProcess(magick, ['-size', '900x500', 'plasma:fractal', '-alpha', 'set',
    '-channel', 'A', '+noise', 'Random', '+channel', 'png:-']);
  await f.put('source.png', raw);
  const wav = await runProcess('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-f', 'lavfi', '-i',
    'sine=frequency=600:duration=0.2', '-f', 'wav', 'pipe:1']);
  await f.put('AudioLab/libraries/test/first.wav', wav);
  const cards = [card('image', image('source.png', hash(raw))), card('sound', {
    path: '~/AudioLab/libraries/test/first.wav', role: 'variant', variant: 1, sha256: hash(wav, 'sha256'),
  }, 'audio')];
  const options = { ...f.options, cards, exec: runProcess, magick, ffmpeg: 'ffmpeg' };
  const first = await generateThumbs(options);
  assert.equal(first.missing.length, 0, JSON.stringify(first.missing));
  assert.equal(first.covered, 2); assert.equal(first.created, 2);
  assert.ok(first.maxBytes <= MAX_FILE); assert.ok(first.totalBytes <= MAX_TOTAL);
  const dimensions = (await runProcess(magick, [path.join(f.root, first.thumbnails[0].thumb), '-format', '%w %h', 'info:'])).toString().split(' ').map(Number);
  assert.equal(Math.max(...dimensions), 256);
  const second = await generateThumbs(options);
  assert.equal(second.created, 0); assert.equal(second.reused, 2);
  // Chuỗi VFX động mở đầu bằng khung trống: lấy khung giữa (đỏ), không lấy khung 0 (trong suốt).
  const anim = await runProcess(magick, ['-size', '300x200', 'xc:none', 'xc:red', 'xc:none', '-loop', '0', 'webp:-']);
  await f.put('vfx/burst.webp', anim);
  const motion = await generateThumbs({ ...options, cards: [card('vfx', image('vfx/burst.webp', hash(anim)))] });
  assert.equal(motion.created, 1, JSON.stringify(motion.missing));
  // -alpha extract: ảnh đục (WebP bỏ kênh alpha) ra 1, khung 0 trong suốt ra 0.
  const alpha = Number((await runProcess(magick, [path.join(f.root, motion.thumbnails[0].thumb),
    '-alpha', 'extract', '-format', '%[fx:mean]', 'info:'])).toString());
  assert.ok(alpha > 0.9, `khung giữa phải hiện, alpha trung bình ${alpha}`);
  t.diagnostic(`K1/K4 thật: 2/2 thẻ; lớn nhất ${first.maxBytes} byte; tổng ${first.totalBytes} byte; lượt hai 0 file; Blender 0/150.`);
});

function triangleGlb() {
  const geometry = Buffer.alloc(36);
  [0, 0, 0, 2, 0, 0, 0, 3, 1].forEach((n, i) => geometry.writeFloatLE(n, i * 4));
  const json = JSON.stringify({ asset: { version: '2.0' }, scene: 0, scenes: [{ nodes: [0] }], nodes: [{ mesh: 0 }],
    meshes: [{ primitives: [{ attributes: { POSITION: 0 } }] }], buffers: [{ byteLength: 36 }],
    bufferViews: [{ buffer: 0, byteLength: 36 }], accessors: [{ bufferView: 0, componentType: 5126, count: 3,
      type: 'VEC3', min: [0, 0, 0], max: [2, 3, 1] }] });
  const body = Buffer.from(json.padEnd(Math.ceil(Buffer.byteLength(json) / 4) * 4, ' '));
  const glb = Buffer.alloc(28 + body.length + geometry.length);
  glb.writeUInt32LE(0x46546c67); glb.writeUInt32LE(2, 4); glb.writeUInt32LE(glb.length, 8);
  glb.writeUInt32LE(body.length, 12); glb.writeUInt32LE(0x4e4f534a, 16); body.copy(glb, 20);
  glb.writeUInt32LE(geometry.length, 20 + body.length); glb.writeUInt32LE(0x004e4942, 24 + body.length);
  geometry.copy(glb, 28 + body.length); return glb;
}

test('Blender headless thật: 3/4, nền trong; bỏ qua rõ lý do nếu không chạy được', async t => {
  const f = await fixture(t), blender = '/Applications/Blender.app/Contents/MacOS/Blender';
  try {
    await runProcess(blender, ['--disable-crash-handler', '--disable-abort-handler', '-b', '--factory-startup',
      '--disable-autoexec', '--python-expr', 'print("AL13_READY")']);
    await runProcess('/opt/homebrew/bin/magick', ['-version']);
  } catch (error) { t.skip(`Bỏ qua Blender/magick thật: ${error.message}`); return; }
  const raw = triangleGlb(); await f.put('triangle.glb', raw);
  const result = await generateThumbs({ ...f.options, exec: runProcess, blender, magick: '/opt/homebrew/bin/magick',
    cards: [card('model', model('triangle.glb', hash(raw)), 'model3d')] });
  assert.equal(result.covered, 1, JSON.stringify(result.missing)); assert.equal(result.blenderRenders, 1);
  const info = (await runProcess('/opt/homebrew/bin/magick', [path.join(f.root, result.thumbnails[0].thumb),
    '-format', '%w %h %[opaque]', 'info:'])).toString();
  assert.match(info, /^256 256 False$/u);
  // Khung vừa hình chiếu thật (chừa 5% mỗi bên): vật chiếm ≥ 200/256 px theo cạnh dài.
  const trim = (await runProcess('/opt/homebrew/bin/magick', [path.join(f.root, result.thumbnails[0].thumb),
    '-format', '%@', 'info:'])).toString().split(/[x+]/u).map(Number);
  assert.ok(Math.max(trim[0], trim[1]) >= 200, `vật chỉ chiếm ${trim[0]}x${trim[1]} px`);
  assert.ok(result.maxBytes <= MAX_FILE);
});
