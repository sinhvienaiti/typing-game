import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { GAMES, REPO_ROOT, imageHeader, inspectGlb, matchOriginal, parseGlb, walkFiles } from '../scan-assets.mjs';

// Fixtures live in memory only; no media is made or changed on disk.
function glb(json, bin = Buffer.alloc(0)) {
  const encoded = Buffer.from(JSON.stringify({ asset: { version: '2.0' }, ...json }));
  const padded = Buffer.alloc(Math.ceil(encoded.length / 4) * 4, 0x20);
  encoded.copy(padded);
  const binary = Buffer.alloc(Math.ceil(bin.length / 4) * 4);
  bin.copy(binary);
  const out = Buffer.alloc(20 + padded.length + (binary.length ? 8 + binary.length : 0));
  out.writeUInt32LE(0x46546c67, 0); out.writeUInt32LE(2, 4); out.writeUInt32LE(out.length, 8);
  out.writeUInt32LE(padded.length, 12); out.writeUInt32LE(0x4e4f534a, 16); padded.copy(out, 20);
  if (binary.length) {
    const at = 20 + padded.length;
    out.writeUInt32LE(binary.length, at); out.writeUInt32LE(0x004e4942, at + 4); binary.copy(out, at + 8);
  }
  return out;
}

function triangle() {
  return {
    scenes: [{ nodes: [0] }], scene: 0, nodes: [{ mesh: 0, scale: [2, 2, 2] }],
    meshes: [{ primitives: [{ attributes: { POSITION: 0 } }] }],
    accessors: [{ type: 'VEC3', componentType: 5126, count: 3, min: [0, 0, 0], max: [1, 1, 0] }],
  };
}

test('GLB trong RAM: một tam giác, node scale 2', () => {
  const binary = Buffer.alloc(36);
  [0, 0, 0, 1, 0, 0, 0, 1, 0].forEach((v, i) => binary.writeFloatLE(v, i * 4));
  const j = triangle();
  j.buffers = [{ byteLength: 36 }]; j.bufferViews = [{ buffer: 0, byteLength: 36 }]; j.accessors[0].bufferView = 0;
  const model = inspectGlb(glb(j, binary));
  assert.deepEqual(model.bounds, { min: [0, 0, 0], max: [2, 2, 0], size: [2, 2, 0], footprint: [2, 0], height: 2 });
  assert.equal(model.triangles, 1);
});

test('Ma trận cha, TRS con, quay 90 độ, scale âm và 8 góc hộp', () => {
  const j = triangle();
  j.accessors[0].max = [1, 2, 3];
  j.nodes = [
    { matrix: [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 10, 20, 30, 1], children: [1] },
    { mesh: 0, translation: [1, 2, 3], rotation: [0, 0, Math.SQRT1_2, Math.SQRT1_2], scale: [-2, 3, 4] },
  ];
  const b = inspectGlb(glb(j)).bounds;
  for (const [actual, expected] of [[b.min, [5, 20, 33]], [b.max, [11, 22, 45]], [b.size, [6, 2, 12]]]) {
    actual.forEach((v, i) => assert.ok(Math.abs(v - expected[i]) < 1e-10));
  }
});

test('POSITION số nguyên chuẩn hóa phải đổi min/max trước transform', () => {
  const j = triangle();
  Object.assign(j.accessors[0], { componentType: 5122, normalized: true, min: [-32768, 0, -16384], max: [32767, 32767, 16384] });
  const a = inspectGlb(glb(j));
  assert.deepEqual(a.bounds.min, [-2, 0, -32768 / 32767]);
  assert.deepEqual(a.bounds.max, [2, 2, 32768 / 32767]);
});

test('Mesh dùng chung tính theo node trong scene 0, bỏ node của scene khác', () => {
  const j = triangle();
  j.nodes.push({ mesh: 0, translation: [4, 0, 0] }, { mesh: 0, translation: [100, 0, 0] });
  j.scenes = [{ nodes: [0, 1] }, { nodes: [2] }]; j.scene = 1;
  const a = inspectGlb(glb(j));
  assert.equal(a.triangles, 2); assert.equal(a.meshInstances, 2); assert.equal(a.meshes, 1);
  assert.deepEqual(a.bounds.max, [5, 2, 0]);
  assert.ok(a.warnings.includes('default-scene-is-not-zero'));
});

test('TRIANGLES, STRIP, FAN và LINES; indexed và non-indexed', () => {
  const j = triangle();
  j.accessors.push({ type: 'SCALAR', componentType: 5123, count: 6 });
  j.meshes[0].primitives = [
    { attributes: { POSITION: 0 }, indices: 1, mode: 4 },
    { attributes: { POSITION: 0 }, indices: 1, mode: 5 },
    { attributes: { POSITION: 0 }, mode: 6 },
    { attributes: { POSITION: 0 }, mode: 1 },
  ];
  assert.equal(inspectGlb(glb(j)).triangles, 2 + 4 + 1);
});

test('Thiếu POSITION min/max: bounds null, không công bố hộp thiếu một phần', () => {
  const j = triangle();
  j.accessors.push({ ...j.accessors[0], min: undefined });
  j.meshes[0].primitives.push({ attributes: { POSITION: 1 } });
  const a = inspectGlb(glb(j));
  assert.equal(a.bounds, null); assert.equal(a.longestAxis, null);
  assert.equal(a.needsDecompression.length, 1); assert.equal(a.triangles, 2);
});

test('Animation: hợp khoảng thời gian nhiều sampler, đọc FLOAT BIN khi thiếu min/max', () => {
  const j = triangle();
  const bin = Buffer.alloc(12); [0.5, 1.5, 3].forEach((v, i) => bin.writeFloatLE(v, i * 4));
  j.buffers = [{ byteLength: 12 }]; j.bufferViews = [{ buffer: 0, byteLength: 12 }];
  j.accessors.push({ type: 'SCALAR', componentType: 5126, count: 3, bufferView: 0 });
  j.accessors.push({ type: 'SCALAR', componentType: 5126, count: 2, min: [1], max: [4] });
  j.animations = [{ name: 'Idle', samplers: [{ input: 1 }, { input: 2 }] }];
  assert.deepEqual(inspectGlb(glb(j, bin)).animations, [{ name: 'Idle', duration: 3.5, start: 0.5, end: 4 }]);
});

test('GLB hỏng header, chunk hoặc chu kỳ node phải báo lỗi', () => {
  const data = glb(triangle()); data.writeUInt32LE(1, 8);
  assert.throws(() => parseGlb(data), /Độ dài GLB/);
  const j = triangle(); j.nodes[0].children = [0];
  assert.throws(() => inspectGlb(glb(j)), /Chu kỳ node/);
  assert.throws(() => parseGlb(Buffer.alloc(12)), /Header GLB/);
});

test('Header ảnh PNG, JPEG baseline/progressive, WebP VP8/VP8L/VP8X, KTX2', () => {
  const png = Buffer.alloc(24); Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]).copy(png);
  png.writeUInt32BE(640, 16); png.writeUInt32BE(480, 20);
  assert.deepEqual(imageHeader(png), { format: 'png', width: 640, height: 480 });
  for (const marker of [0xc0, 0xc2]) {
    const jpeg = Buffer.from([0xff, 0xd8, 0xff, marker, 0, 8, 8, 1, 224, 2, 128, 1]);
    assert.deepEqual(imageHeader(jpeg), { format: 'jpeg', width: 640, height: 480 });
  }
  const webp = (type, payload) => {
    const b = Buffer.alloc(20 + payload.length + payload.length % 2);
    b.write('RIFF'); b.writeUInt32LE(b.length - 8, 4); b.write('WEBP', 8); b.write(type, 12);
    b.writeUInt32LE(payload.length, 16); payload.copy(b, 20); return b;
  };
  const vp8 = Buffer.alloc(10); Buffer.from([0x9d, 1, 0x2a]).copy(vp8, 3); vp8.writeUInt16LE(640, 6); vp8.writeUInt16LE(480, 8);
  const vp8l = Buffer.alloc(5); vp8l[0] = 0x2f; vp8l.writeUInt32LE(639 | (479 << 14), 1);
  const vp8x = Buffer.alloc(10); vp8x.writeUIntLE(639, 4, 3); vp8x.writeUIntLE(479, 7, 3);
  for (const [type, payload] of [['VP8 ', vp8], ['VP8L', vp8l], ['VP8X', vp8x]]) {
    assert.deepEqual(imageHeader(webp(type, payload)), { format: 'webp', width: 640, height: 480 });
  }
  assert.deepEqual(imageHeader(Buffer.from([171, 75, 84, 88, 32, 50, 48, 187, 13, 10, 26, 10])), { format: 'ktx2', width: null, height: null });
  assert.throws(() => imageHeader(Buffer.alloc(3)), /Header ảnh/);
});

test('Nối nguồn: ưu tiên usedBy, id, rồi tên duy nhất; từ chối tên mơ hồ', () => {
  assert.deepEqual(matchOriginal('bosses/alias', ['bosses/raw'], { 'bosses/raw.glb': { usedBy: ['bosses/alias'] } }), { id: 'bosses/raw', match: 'SOURCES.usedBy' });
  assert.deepEqual(matchOriginal('props/pine-river-log', ['props/pine-river/log'], {}), { id: 'props/pine-river/log', match: 'unique-filename-id' });
  assert.deepEqual(matchOriginal('props/herb-hut', ['houses/herb-hut'], {}), { id: 'houses/herb-hut', match: 'unique-filename-id' });
  assert.equal(matchOriginal('props/missing', ['houses/log', 'props/log-other'], {}), null);
  assert.equal(matchOriginal('props/log', ['houses/log', 'trees/log'], {}), null);
  assert.deepEqual(matchOriginal('bosses/later', ['bosses/stand-in'], {}, {
    notMadeYet: { 'bosses/later.glb': { standIn: 'bosses/stand-in.glb' } },
  }), { id: 'bosses/stand-in', match: 'SOURCES.notMadeYet.standIn', requested: 'bosses/later.glb', reference: { standIn: 'bosses/stand-in.glb' } });
  assert.deepEqual(matchOriginal('bosses/alias', ['bosses/raw'], {}, {
    noOriginalOnThisMachine: { 'bosses/alias': 'Built from art-src/3d/bosses/raw.glb.' },
  }), { id: 'bosses/raw', match: 'SOURCES.note-path', reference: 'Built from art-src/3d/bosses/raw.glb.' });
});

// A second counter reads the chunks and every index in BIN itself, without
// parseGlb, accessor.count or inspectGlb, to count each primitive's elements.
function countFromBinary(data) {
  let json, bin;
  for (let cursor = 12; cursor < data.length;) {
    const size = data.readUInt32LE(cursor), type = data.toString('ascii', cursor + 4, cursor + 8);
    const chunk = data.subarray(cursor + 8, cursor + 8 + size);
    if (type === 'JSON') json = JSON.parse(chunk.toString());
    if (type === 'BIN\0') bin = chunk;
    cursor += size + 8;
  }
  const pending = [...json.scenes[0].nodes], meshUses = new Map();
  while (pending.length) {
    const n = json.nodes[pending.shift()]; pending.push(...n.children ?? []);
    if (n.mesh !== undefined) meshUses.set(n.mesh, (meshUses.get(n.mesh) ?? 0) + 1);
  }
  let total = 0;
  for (const [meshIndex, uses] of meshUses) for (const p of json.meshes[meshIndex].primitives) {
    assert.equal(p.mode ?? 4, 4);
    const a = json.accessors[p.indices]; assert.ok(a); assert.equal(a.byteOffset ?? 0, 0);
    const view = json.bufferViews[a.bufferView];
    assert.equal(view.buffer ?? 0, 0); assert.ok(!view.extensions?.EXT_meshopt_compression);
    const width = { 5121: 1, 5123: 2, 5125: 4 }[a.componentType]; assert.ok(width); assert.ok(!view.byteStride);
    assert.equal(view.byteLength % (width * 3), 0);
    let triangles = 0;
    for (let cursor = view.byteOffset ?? 0; cursor < (view.byteOffset ?? 0) + view.byteLength; cursor += width * 3) {
      // Reads all three indices and checks they really point into POSITION.
      for (let i = 0; i < 3; i++) assert.ok(bin.readUIntLE(cursor + i * width, width) < json.accessors[p.attributes.POSITION].count);
      triangles++;
    }
    total += triangles * uses;
  }
  return total;
}

const originals = [
  ['dragon-hold', 'enemies/moss-grunt.glb', 5708],
  ['dragon-hold', 'enemies/blight-wolf.glb', 5637],
  ['dragon-hold', 'generals/moss-banner.glb', 8382],
  ['dragon-hold', 'houses/herb-hut.glb', 9858],
  ['typing-defense', 'buildings/keep.glb', 18962],
  ['space-typing', 'ships/ship-01-vanguard.glb', 21193],
];
for (const [game, relative, known] of originals) test(`${game}/${relative}: đếm BIN độc lập và số đối chiếu`, async () => {
  const data = await readFile(path.join(REPO_ROOT, 'games', game, 'art-src/3d', relative));
  const independent = countFromBinary(data);
  assert.equal(independent, known); assert.equal(inspectGlb(data).triangles, independent);
});

for (const game of GAMES) test(`${game}: sổ đủ trường, đủ GLB và md5 trước/sau`, async () => {
  const registry = JSON.parse(await readFile(path.join(REPO_ROOT, 'tools/map-factory/registry/out', `assets.${game}.json`), 'utf8'));
  assert.equal(registry.errors.length, 0); assert.equal(registry.needsDecompression.length, 0);
  assert.equal(registry.mediaIntegrity.changed.length, 0);
  const files = [];
  for (const directory of [`public/assets/${game}/models`, 'art-src/3d']) {
    files.push(...(await walkFiles(path.join(REPO_ROOT, 'games', game, directory))).filter(f => /\.glb$/i.test(f)));
  }
  assert.deepEqual(registry.assets.map(a => a.file).sort(), files.map(f => path.relative(REPO_ROOT, f).split(path.sep).join('/')).sort());
  assert.equal(registry.statistics.total, files.length);
  const manifestDocuments = new Map();
  const keys = ['id', 'game', 'file', 'bytes', 'category', 'tags', 'tagsSource', 'bounds', 'longestAxis', 'triangles', 'meshes', 'primitives', 'materials', 'textures', 'skinned', 'animations', 'extensions', 'source', 'licence', 'manifest'];
  for (const asset of registry.assets) {
    for (const key of keys) assert.ok(Object.hasOwn(asset, key), `${asset.file}: thiếu ${key}`);
    assert.equal(asset.tagsSource, 'auto'); assert.equal(asset.game, game);
    assert.ok(['runtime', 'original'].includes(asset.source));
    assert.ok(['owner-tripo', 'space-library', 'unknown'].includes(asset.licence));
    assert.ok(asset.bounds?.size.every(Number.isFinite)); assert.ok(Number.isInteger(asset.triangles));
    assert.equal(asset.textures.count, asset.textures.images.length);
    for (const image of asset.textures.images) {
      assert.ok(['png', 'jpeg', 'webp', 'ktx2'].includes(image.format));
      if (image.format !== 'ktx2') { assert.ok(image.width > 0); assert.ok(image.height > 0); }
    }
    assert.equal(asset.md5, asset.md5After);
    const data = await readFile(path.join(REPO_ROOT, asset.file));
    assert.equal(asset.bytes, data.length);
    const current = createHash('md5').update(data).digest('hex');
    assert.equal(asset.md5, current, asset.file);
    if (asset.manifestFile) {
      if (!manifestDocuments.has(asset.manifestFile)) manifestDocuments.set(asset.manifestFile,
        JSON.parse(await readFile(path.join(REPO_ROOT, asset.manifestFile), 'utf8')));
      assert.deepEqual(asset.manifest, manifestDocuments.get(asset.manifestFile).models[asset.manifestKey]);
    }
    if (asset.original) {
      const original = registry.assets.find(a => a.file === asset.original.file);
      assert.ok(original); assert.equal(asset.original.md5, original.md5);
    }
    if (asset.source === 'original') assert.equal(asset.licence, 'owner-tripo');
    if (asset.source === 'runtime' && game === 'space-typing') assert.equal(asset.licence, 'space-library');
  }
});
