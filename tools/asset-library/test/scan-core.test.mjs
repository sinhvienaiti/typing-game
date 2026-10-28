import test from 'node:test';
import assert from 'node:assert/strict';
import * as fs from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { deflateSync } from 'node:zlib';
import { scan, main, inspectImage, pathAllowed, REPO_ROOT } from '../scan.mjs';

const DATE = '2026-10-28T12:00:00.000Z';
const sources = JSON.parse(await fs.readFile(path.join(REPO_ROOT, 'library/sources.json'), 'utf8'));
const md5 = data => createHash('md5').update(data).digest('hex');
const sha256 = data => createHash('sha256').update(data).digest('hex');
const target = 'games/dragon-hold/art-src/houses/herb-hut.png';

function crc32(data) {
  let crc = 0xffffffff;
  for (const byte of data) {
    crc ^= byte;
    for (let i = 0; i < 8; i++) crc = (crc >>> 1) ^ ((crc & 1) ? 0xedb88320 : 0);
  }
  return (crc ^ 0xffffffff) >>> 0;
}
function chunk(type, bytes) {
  const result = Buffer.alloc(bytes.length + 12);
  result.writeUInt32BE(bytes.length);
  result.write(type, 4);
  bytes.copy(result, 8);
  result.writeUInt32BE(crc32(result.subarray(4, -4)), result.length - 4);
  return result;
}
function png(color = 6, transparent = false) {
  const header = Buffer.alloc(13);
  header.writeUInt32BE(1); header.writeUInt32BE(1, 4); header[8] = 8; header[9] = color;
  return Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), chunk('IHDR', header),
    ...(transparent ? [chunk('tRNS', Buffer.from([0, 0, 0, 0, 0, 0]))] : []),
    chunk('IDAT', deflateSync(Buffer.alloc(color === 6 ? 5 : 4))), chunk('IEND', Buffer.alloc(0))]);
}
function glb() {
  const geometry = Buffer.alloc(36);
  [0, 0, 0, 2, 0, 0, 0, 3, 4].forEach((n, i) => geometry.writeFloatLE(n, i * 4));
  const json = JSON.stringify({ asset: { version: '2.0' }, scene: 0, scenes: [{ nodes: [0] }],
    nodes: [{ mesh: 0 }], meshes: [{ primitives: [{ attributes: { POSITION: 0 } }] }],
    buffers: [{ byteLength: 36 }], bufferViews: [{ buffer: 0, byteLength: 36 }],
    accessors: [{ bufferView: 0, componentType: 5126, count: 3, type: 'VEC3', min: [0, 0, 0], max: [2, 3, 4] }] });
  const body = Buffer.from(json.padEnd(Math.ceil(Buffer.byteLength(json) / 4) * 4, ' '));
  const result = Buffer.alloc(28 + body.length + geometry.length);
  result.writeUInt32LE(0x46546c67); result.writeUInt32LE(2, 4); result.writeUInt32LE(result.length, 8);
  result.writeUInt32LE(body.length, 12); result.writeUInt32LE(0x4e4f534a, 16); body.copy(result, 20);
  result.writeUInt32LE(geometry.length, 20 + body.length); result.writeUInt32LE(0x004e4942, 24 + body.length);
  geometry.copy(result, 28 + body.length);
  return result;
}

async function put(root, p, data) {
  await fs.mkdir(path.dirname(path.join(root, p)), { recursive: true });
  await fs.writeFile(path.join(root, p), data);
}
async function fixture(t) {
  const root = await fs.mkdtemp(path.join(tmpdir(), 'al05-scan-'));
  t.after(async () => {
    async function writable(dir) {
      await fs.chmod(dir, 0o700);
      for (const item of await fs.readdir(dir, { withFileTypes: true })) {
        if (item.isDirectory()) await writable(path.join(dir, item.name));
      }
    }
    await writable(root);
    await fs.rm(root, { recursive: true, force: true });
  });
  await put(root, 'library/sources.json', JSON.stringify(sources));
  for (const [p, data] of [
    [target, png()], ['games/dragon-hold/art-src/houses/herb-hut.tripo.png', png(2)],
    ['games/dragon-hold/art-src/houses/herb-hut.prompt.txt', 'Mẫu thử'],
    ['games/dragon-hold/art-src/houses/herb-hut.rejected-056.png', png()],
    ['games/dragon-hold/art-src/3d/houses/herb-hut.glb', glb()],
    ['games/typing-defense/art-src/scenery/meadow/reed-v1.png', png()],
    ['games/typing-defense/art-src/scenery/meadow/reed-v2.png', png()],
    ['games/space-typing/art-src/ships/ship-01-scout-2d.png', png()],
    ['games/space-typing/art-src/3d/ships/ship-01-scout.glb', glb()],
    ['games/space-typing/public/assets/pilot.png', png()],
    ['games/dragon-hold/art-src/houses/broken.glb', 'GLB lỗi'],
    ['games/dragon-hold/art-src/houses/hut.unlisted.png', png()],
    ['games/dragon-hold/art-src/houses/not-image.png', 'PNG lỗi'],
    ['games/dragon-hold/art-src/tmp/ignored.png', png()],
    ['games/dragon-hold/art-src/dist/ignored.png', png()],
    ['games/dragon-hold/art-src/houses/skip.ogg', 'Không quét âm'],
  ]) await put(root, p, data);
  await put(root, 'games/space-typing/art-src/3d/SOURCES.json', JSON.stringify({ files: {
    'ships/ship-01-scout.glb': { image: 'art-src/ships/ship-01-scout-2d.png' },
  } }));
  return root;
}

const allowedOutputs = ['library/.cache/hash.json', 'library/out/catalog.json', 'library/out/scan-report.md'];
function guardedIo(root, writes, reads = []) {
  return new Proxy(fs, { get(object, name) {
    const original = object[name];
    if (typeof original !== 'function') return original;
    return async (file, ...args) => {
      const rel = path.relative(root, file).split(path.sep).join('/');
      if (['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'symlink', 'unlink', 'rm', 'open'].includes(name)) {
        const permitted = name === 'mkdir' ? ['library/out', 'library/.cache'].includes(rel)
          : name === 'writeFile' && allowedOutputs.includes(rel);
        assert.ok(permitted, `Ghi ngoài phạm vi: ${name} ${rel}`);
        writes.push([name, rel]);
      }
      if (name === 'readFile') reads.push(rel);
      return original(file, ...args);
    };
  } });
}

test('K1 · Cây nguồn chmod a-w, lớp bọc fs: chỉ ghi 3 sản phẩm; gom ảnh và GLB', async t => {
  const root = await fixture(t);
  async function readonly(dir) {
    for (const item of await fs.readdir(dir, { withFileTypes: true })) {
      const file = path.join(dir, item.name);
      if (item.isDirectory()) await readonly(file);
      else await fs.chmod(file, 0o444);
    }
    await fs.chmod(dir, 0o555);
  }
  await readonly(path.join(root, 'games'));
  const writes = [], reads = [];
  const { catalog, stats } = await scan({ repoRoot: root, scanDate: DATE, io: guardedIo(root, writes, reads) });
  assert.equal(catalog.schema, 'asset-library/1');
  assert.deepEqual(catalog.cards.map(c => c.uid), catalog.cards.map(c => c.uid).sort());
  const hut = catalog.cards.find(c => c.uid === 'dragon-hold:houses/herb-hut');
  assert.equal(hut.kind, 'building'); assert.equal(hut.style, 'mythic-forest');
  assert.equal(hut.type, 'model3d'); assert.equal(hut.files.length, 5);
  assert.deepEqual(hut.files.find(f => f.path === target).image, { w: 1, h: 1, alpha: true });
  assert.equal(hut.files.find(f => f.role === 'glb-original').glb.triangles, 1);
  assert.deepEqual(hut.files.find(f => f.role === 'glb-original').glb.bounds.size, [2, 3, 4]);
  const reed = catalog.cards.find(c => c.uid === 'typing-defense:scenery/meadow/reed');
  assert.deepEqual(reed.files.map(f => f.variant), ['a', 'b']);
  assert.deepEqual(reed.biome, ['meadow']);
  assert.equal(catalog.cards.find(c => c.uid === 'space-typing:ships/ship-01-scout').files.length, 2);
  assert.ok(catalog.cards.some(c => c.uid === 'space-typing:public/assets/pilot'));
  assert.ok(catalog.cards.some(c => c.files.some(f => f.role === 'unknown')));
  assert.ok(catalog.warnings.some(w => w.includes('broken.glb')));
  assert.ok(catalog.warnings.some(w => w.includes('not-image.png')));
  assert.ok(catalog.warnings.some(w => w.includes('Unknown vượt ngưỡng')));
  assert.ok(catalog.cards.every(c => c.files.every(f => f.local && f.md5.length === 32 && f.sha256.length === 64)));
  assert.ok(!reads.some(p => p.endsWith('.ogg') || p.includes('/tmp/') || p.includes('/dist/')));
  assert.equal(new Set(writes.filter(([name]) => name === 'writeFile').map(([, p]) => p)).size, 3);
  assert.equal(stats.hash.hashed, catalog.cards.flatMap(c => c.files).length);
  t.diagnostic(`Cây a-w: ${catalog.cards.length} thẻ, ${stats.hash.hashed} file; ${writes.length} lời gọi ghi, đúng 3 file sản phẩm`);
});

test('2 · Cùng --scan-date giống từng byte; lượt ấm không đọc/băm lại media', async t => {
  const root = await fixture(t);
  await main(['--scan-date', DATE], { repoRoot: root });
  const first = await fs.readFile(path.join(root, 'library/out/catalog.json'));
  const cache = await fs.readFile(path.join(root, 'library/.cache/hash.json'));
  const reads = [];
  const start = performance.now();
  const result = await main(['--scan-date', DATE], { repoRoot: root, io: guardedIo(root, [], reads) });
  assert.deepEqual(await fs.readFile(path.join(root, 'library/out/catalog.json')), first);
  assert.deepEqual(await fs.readFile(path.join(root, 'library/.cache/hash.json')), cache);
  assert.equal(result.stats.hash.hashed, 0); assert.equal(result.stats.inspected, 0);
  assert.equal(reads.filter(p => IMAGE.test(p) || p.endsWith('.glb') || p.endsWith('.prompt.txt')).length, 0);
  t.diagnostic(`Catalog giống ${first.length} byte; lượt ấm ${(performance.now() - start).toFixed(1)} ms; băm 0 file`);
});
const IMAGE = /\.(png|jpg|webp|svg)$/u;

test('3 · File biến mất qua móc test: CLI kết thúc 0, cảnh báo ENOENT', async t => {
  const root = await fixture(t);
  const script = `
    import { unlink } from 'node:fs/promises';
    import path from 'node:path';
    import { main } from ${JSON.stringify(new URL('../scan.mjs', import.meta.url).href)};
    let removed = false;
    const result = await main(['--scan-date', ${JSON.stringify(DATE)}], {
      repoRoot: ${JSON.stringify(root)}, hooks: { async beforeFile(file) {
        if (file === ${JSON.stringify(target)} && !removed) {
          await unlink(path.join(${JSON.stringify(root)}, file)); removed = true;
        }
      } }
    });
    if (!result.catalog.warnings.some(w => w.includes('ENOENT'))) process.exitCode = 9;
  `;
  const child = spawnSync(process.execPath, ['--input-type=module', '-e', script], { encoding: 'utf8', timeout: 30_000 });
  assert.equal(child.status, 0, child.stdout + child.stderr);
  const catalog = JSON.parse(await fs.readFile(path.join(root, 'library/out/catalog.json')));
  assert.ok(catalog.warnings.some(w => w.includes(target) && w.includes('ENOENT')));
  assert.ok(!catalog.cards.flatMap(c => c.files).some(f => f.path === target));
  t.diagnostic('Xóa 1 file giữa lúc đi: ENOENT thành cảnh báo, mã thoát 0');
});

test('Cache media chỉ đọc: size và mtime phải cùng khớp; đổi file chỉ băm lại file đó', async t => {
  const root = await fixture(t);
  const original = await fs.readFile(path.join(root, target));
  const info = await fs.stat(path.join(root, target));
  const second = 'games/dragon-hold/art-src/houses/herb-hut.tripo.png';
  const secondInfo = await fs.stat(path.join(root, second));
  const third = 'games/typing-defense/art-src/scenery/meadow/reed-v1.png';
  const thirdInfo = await fs.stat(path.join(root, third));
  const seed = { version: 1, files: {
    [target]: [info.size, info.mtimeMs, md5(original), sha256(original)],
    [second]: [secondInfo.size, secondInfo.mtimeMs - 1, 'a'.repeat(32), 'b'.repeat(64)],
    [third]: [thirdInfo.size + 1, thirdInfo.mtimeMs, 'c'.repeat(32), 'd'.repeat(64)],
  } };
  await put(root, '.cache/media-hash.json', JSON.stringify(seed));
  const seedBefore = await fs.readFile(path.join(root, '.cache/media-hash.json'));
  const first = await scan({ repoRoot: root, scanDate: DATE });
  assert.equal(first.stats.hash.seeded, 1);
  assert.equal(first.catalog.cards.flatMap(c => c.files).find(f => f.path === second).md5, md5(png(2)));
  await fs.writeFile(path.join(root, target), png(2, true));
  const warm = await scan({ repoRoot: root, scanDate: DATE });
  assert.equal(warm.stats.hash.hashed, 1); assert.equal(warm.stats.hash.seeded, 0);
  assert.deepEqual(await fs.readFile(path.join(root, '.cache/media-hash.json')), seedBefore);
  assert.equal(warm.catalog.cards.flatMap(c => c.files).find(f => f.path === target).md5, md5(png(2, true)));
  t.diagnostic('Mồi đúng 1 file; mtime lệch bị từ chối; file thay đổi: băm lại đúng 1; cache media nguyên byte');
});

test('GLB: sổ Map Factory chỉ thắng khi md5 khớp; md5 lệch dùng inspectGlb', async t => {
  const root = await fixture(t);
  const original = 'games/dragon-hold/art-src/3d/houses/herb-hut.glb';
  const space = 'games/space-typing/art-src/3d/ships/ship-01-scout.glb';
  await put(root, 'tools/map-factory/registry/out/assets.dragon-hold.json', JSON.stringify({ assets: [
    { file: original, md5: md5(glb()), triangles: 99, bounds: { height: 7 }, skinned: false, animations: [] },
  ] }));
  await put(root, 'tools/map-factory/registry/out/assets.space-typing.json', JSON.stringify({ assets: [
    { file: space, md5: '0'.repeat(32), triangles: 9999, errors: [] },
  ] }));
  const { catalog, stats } = await scan({ repoRoot: root, scanDate: DATE });
  const files = catalog.cards.flatMap(c => c.files);
  assert.equal(files.find(f => f.path === original).glb.triangles, 99);
  assert.equal(files.find(f => f.path === space).glb.triangles, 1);
  assert.equal(stats.registry, 1); assert.equal(stats.inspected, 1);
  t.diagnostic('1 GLB md5 khớp dùng sổ; 1 GLB md5 lệch đọc thật: 1 tam giác');
});

test('K3 · Chặn trước khi đọc: deny, ignore, symlink thư mục/file/tổ tiên; --game', async t => {
  const root = await fixture(t);
  const excluded = sources.deny.find(p => p.startsWith('games/') && !p.includes('monkeytype'));
  const custom = structuredClone(sources);
  custom.deny.push('games/dragon-hold/art-src/blocked', 'games/dragon-hold/art-src/blocked/**');
  custom.roots.push({ game: 'dragon-hold', path: excluded });
  custom.roots.push({ game: 'dragon-hold', path: '../outside' });
  await put(root, 'library/sources.json', JSON.stringify(custom));
  await put(root, 'games/dragon-hold/art-src/blocked/secret.png', png());
  const outside = path.join(root, 'outside');
  await fs.mkdir(outside); await fs.writeFile(path.join(outside, 'secret.png'), png());
  await fs.symlink(outside, path.join(root, 'games/dragon-hold/art-src/linked-dir'));
  await fs.symlink(path.join(outside, 'secret.png'), path.join(root, 'games/dragon-hold/art-src/linked.png'));
  await fs.mkdir(path.join(root, 'games/dragon-hold/src'), { recursive: true });
  await fs.symlink(outside, path.join(root, 'games/dragon-hold/src/assets'));
  const reads = [];
  const io = guardedIo(root, [], reads);
  const result = await main(['--game', 'dragon-hold', '--scan-date', DATE], { repoRoot: root, io });
  assert.ok(result.catalog.cards.every(c => c.origin === 'dragon-hold'));
  assert.ok(!reads.some(p => /blocked|linked|outside/u.test(p)));
  for (const output of allowedOutputs) {
    const raw = await fs.readFile(path.join(root, output), 'utf8');
    assert.ok(!raw.includes(excluded.split('/').at(-1)));
    assert.ok(!raw.includes('tu-tien'));
    assert.ok(!raw.includes('secret.png'));
  }
  for (const p of [excluded, excluded + '/image.png', 'games/monkeytype', '../outside', '/absolute', 'games/dragon-hold/art-src/tmp']) {
    assert.equal(pathAllowed(p, custom), false, p);
  }
  await assert.rejects(main(['--game', 'unknown'], { repoRoot: root }), /không được phép/u);
  await assert.rejects(main(['--scan-date', 'not-a-date'], { repoRoot: root }), /ISO/u);
  await assert.rejects(main(['--oops'], { repoRoot: root }), /Cờ/u);
  t.diagnostic('0 lần đọc vùng deny/ignore/symlink; --game chỉ xuất đúng game; 3 file ra không rò vùng cấm');
});

test('Ảnh: PNG alpha/tRNS, JPEG, WebP VP8X/VP8L và SVG', () => {
  assert.equal(inspectImage(png(), '.png').alpha, true);
  assert.equal(inspectImage(png(2), '.png').alpha, false);
  assert.equal(inspectImage(png(2, true), '.png').alpha, true);
  const jpeg = Buffer.from([255, 216, 255, 192, 0, 8, 8, 0, 7, 0, 9, 0]);
  assert.deepEqual(inspectImage(jpeg, '.jpg'), { w: 9, h: 7, alpha: false });
  function webp(type, bytes) {
    const data = Buffer.alloc(20 + bytes.length);
    data.write('RIFF'); data.writeUInt32LE(data.length - 8, 4); data.write('WEBP', 8);
    data.write(type, 12); data.writeUInt32LE(bytes.length, 16); bytes.copy(data, 20); return data;
  }
  const vp8x = Buffer.alloc(10); vp8x[0] = 0x10; vp8x.writeUIntLE(2, 4, 3); vp8x.writeUIntLE(4, 7, 3);
  assert.deepEqual(inspectImage(webp('VP8X', vp8x), '.webp'), { w: 3, h: 5, alpha: true });
  const vp8l = Buffer.alloc(5); vp8l[0] = 0x2f; vp8l.writeUInt32LE(0x10000000, 1);
  assert.deepEqual(inspectImage(webp('VP8L', vp8l), '.webp'), { w: 1, h: 1, alpha: true });
  assert.deepEqual(inspectImage(Buffer.from('<svg viewBox="0 0 24 32"></svg>'), '.svg'), { w: 24, h: 32, alpha: true });
});

test('K1 · Bọc fs toàn cục, kể cả import Map Factory: mọi lần ghi đúng phạm vi', async t => {
  const root = await fixture(t);
  const script = `
    import fs from 'node:fs';
    import path from 'node:path';
    import assert from 'node:assert/strict';
    import { syncBuiltinESMExports } from 'node:module';
    const root = ${JSON.stringify(root)};
    const allowed = ${JSON.stringify(allowedOutputs)};
    let writes = 0;
    const check = (name, file) => {
      const rel = path.relative(root, file).split(path.sep).join('/');
      assert.ok(name === 'mkdir' ? ['library/out','library/.cache'].includes(rel)
        : name === 'writeFile' && allowed.includes(rel), 'Ghi ngoài phạm vi: ' + name + ' ' + rel);
      writes++;
    };
    for (const name of ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'symlink', 'unlink', 'rm',
      'rmdir', 'write', 'writev', 'truncate', 'ftruncate', 'link', 'mkdtemp', 'chmod', 'chown', 'utimes']) {
      for (const key of [name, name + 'Sync']) if (typeof fs[key] === 'function') {
        const original = fs[key]; fs[key] = function(file, ...args) { check(name, file); return original.call(this, file, ...args); };
      }
      if (typeof fs.promises[name] === 'function') {
        const original = fs.promises[name]; fs.promises[name] = function(file, ...args) { check(name, file); return original.call(this, file, ...args); };
      }
    }
    fs.createWriteStream = () => { throw new Error('Không được mở luồng ghi'); };
    for (const [object, name] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
      const original = object[name]; object[name] = function(file, flags, ...args) {
        const writing = typeof flags === 'number' ? Boolean(flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_TRUNC | fs.constants.O_APPEND)) : /[wa+]/u.test(flags ?? 'r');
        assert.equal(writing, false, 'Mở file để ghi: ' + file);
        return original.call(this, file, flags, ...args);
      };
    }
    syncBuiltinESMExports();
    const { scan } = await import(${JSON.stringify(new URL('../scan.mjs', import.meta.url).href)});
    await scan({ repoRoot: root, scanDate: ${JSON.stringify(DATE)} });
    assert.equal(writes, 5);
    console.log('K1: ' + writes + ' lời gọi ghi, chỉ 3 file sản phẩm và 2 mkdir được phép');
  `;
  const child = spawnSync(process.execPath, ['--input-type=module', '-e', script], { encoding: 'utf8', timeout: 30_000 });
  assert.equal(child.status, 0, child.stdout + child.stderr);
  t.diagnostic(child.stdout.trim());
});
