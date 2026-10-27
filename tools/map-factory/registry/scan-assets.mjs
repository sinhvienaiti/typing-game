import { readFile, readdir, realpath, stat, mkdir, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

export const REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
export const GAMES = ['dragon-hold', 'typing-defense', 'space-typing'];
const IDENTITY = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1];
const CREATURES = new Set(['enemies', 'bosses', 'heroes', 'guides', 'units', 'generals', 'animals', 'workers', 'helpers']);
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const slash = p => p.split(path.sep).join('/');
const md5 = data => createHash('md5').update(data).digest('hex');
const finiteVector = (v, n) => Array.isArray(v) && v.length === n && v.every(Number.isFinite);

// Follows symlinks; a cycle is refused only within the current branch, so valid aliases stay.
export async function walkFiles(root, ancestors = new Set()) {
  const resolved = await realpath(root);
  if (ancestors.has(resolved)) throw new Error(`Chu kỳ symlink: ${root}`);
  const next = new Set([...ancestors, resolved]);
  const result = [];
  for (const name of (await readdir(root)).sort(cmp)) {
    const file = path.join(root, name);
    const info = await stat(file);
    if (info.isDirectory()) result.push(...await walkFiles(file, next));
    else if (info.isFile()) result.push(file);
  }
  return result;
}

export function parseGlb(data) {
  if (data.length < 20 || data.readUInt32LE(0) !== 0x46546c67) throw new Error('Header GLB không hợp lệ');
  if (data.readUInt32LE(4) !== 2) throw new Error('Chỉ hỗ trợ GLB phiên bản 2');
  if (data.readUInt32LE(8) !== data.length) throw new Error('Độ dài GLB không khớp header');
  let json;
  let bin = Buffer.alloc(0);
  for (let offset = 12; offset < data.length;) {
    if (offset + 8 > data.length) throw new Error('Header chunk bị cắt');
    const length = data.readUInt32LE(offset);
    const type = data.readUInt32LE(offset + 4);
    const start = offset + 8;
    if (length % 4 || start + length > data.length) throw new Error('Độ dài chunk không hợp lệ');
    if (offset === 12 && type !== 0x4e4f534a) throw new Error('Chunk đầu phải là JSON');
    if (type === 0x4e4f534a) {
      if (json) throw new Error('GLB có nhiều chunk JSON');
      json = JSON.parse(data.toString('utf8', start, start + length).trim());
    } else if (type === 0x004e4942) bin = data.subarray(start, start + length);
    offset = start + length;
  }
  if (!json || json.asset?.version !== '2.0') throw new Error('Thiếu JSON glTF 2.0');
  return { json, bin };
}

function multiply(a, b) {
  return Array.from({ length: 16 }, (_, i) => {
    const row = i % 4, col = Math.floor(i / 4);
    return [0, 1, 2, 3].reduce((sum, k) => sum + a[k * 4 + row] * b[col * 4 + k], 0);
  });
}

function nodeMatrix(node) {
  if (node.matrix) {
    if (!finiteVector(node.matrix, 16)) throw new Error('Ma trận node không hợp lệ');
    return node.matrix;
  }
  const t = node.translation ?? [0, 0, 0], s = node.scale ?? [1, 1, 1], q = node.rotation ?? [0, 0, 0, 1];
  if (!finiteVector(t, 3) || !finiteVector(s, 3) || !finiteVector(q, 4)) throw new Error('TRS không hợp lệ');
  const [x, y, z, w] = q, [sx, sy, sz] = s;
  return [
    (1 - 2 * (y * y + z * z)) * sx, 2 * (x * y + z * w) * sx, 2 * (x * z - y * w) * sx, 0,
    2 * (x * y - z * w) * sy, (1 - 2 * (x * x + z * z)) * sy, 2 * (y * z + x * w) * sy, 0,
    2 * (x * z + y * w) * sz, 2 * (y * z - x * w) * sz, (1 - 2 * (x * x + y * y)) * sz, 0,
    ...t, 1,
  ];
}

function normalize(value, accessor) {
  if (!accessor.normalized) return value;
  switch (accessor.componentType) {
    case 5120: return Math.max(value / 127, -1);
    case 5121: return value / 255;
    case 5122: return Math.max(value / 32767, -1);
    case 5123: return value / 65535;
    default: throw new Error('Kiểu component chuẩn hóa không hợp lệ');
  }
}

function accessorRange(accessor) {
  if (!finiteVector(accessor?.min, 3) || !finiteVector(accessor?.max, 3)) return null;
  const min = accessor.min.map(v => normalize(v, accessor));
  const max = accessor.max.map(v => normalize(v, accessor));
  if (min.some((v, i) => v > max[i])) throw new Error('POSITION min lớn hơn max');
  return { min, max };
}

function readScalarTimes(json, bin, accessor) {
  if (accessor.sparse) throw new Error('Thời gian animation sparse chưa có min/max');
  const view = json.bufferViews?.[accessor.bufferView];
  if (!view || (view.buffer ?? 0) !== 0 || view.extensions?.EXT_meshopt_compression) {
    throw new Error('Thời gian animation nén hoặc ở buffer ngoài chưa có min/max');
  }
  if (accessor.type !== 'SCALAR' || accessor.componentType !== 5126) throw new Error('Thời gian animation phải là FLOAT SCALAR');
  const stride = view.byteStride ?? 4;
  const offset = (view.byteOffset ?? 0) + (accessor.byteOffset ?? 0);
  let min = Infinity, max = -Infinity;
  for (let i = 0; i < accessor.count; i++) {
    const at = offset + i * stride;
    if (at + 4 > bin.length || at + 4 > (view.byteOffset ?? 0) + view.byteLength) throw new Error('Accessor thời gian vượt buffer');
    const v = bin.readFloatLE(at);
    if (!Number.isFinite(v)) throw new Error('Thời gian animation không hữu hạn');
    min = Math.min(min, v); max = Math.max(max, v);
  }
  return [min, max];
}

export function inspectGlb(data) {
  const { json, bin } = parseGlb(data);
  const min = [Infinity, Infinity, Infinity], max = [-Infinity, -Infinity, -Infinity];
  const needsDecompression = [], warnings = [];
  let triangles = 0, meshInstances = 0, primitiveInstances = 0, hasBounds = false;
  const visit = (index, parent, ancestors = new Set()) => {
    if (ancestors.has(index)) throw new Error(`Chu kỳ node ${index}`);
    const node = json.nodes?.[index];
    if (!node) throw new Error(`Không tìm thấy node ${index}`);
    const world = multiply(parent, nodeMatrix(node));
    if (node.mesh !== undefined) {
      const mesh = json.meshes?.[node.mesh];
      if (!mesh) throw new Error(`Không tìm thấy mesh ${node.mesh}`);
      meshInstances++;
      for (const primitive of mesh.primitives ?? []) {
        primitiveInstances++;
        const position = json.accessors?.[primitive.attributes?.POSITION];
        if (!position) throw new Error('Primitive thiếu accessor POSITION');
        const elements = primitive.indices === undefined ? position : json.accessors?.[primitive.indices];
        if (!Number.isSafeInteger(elements?.count) || elements.count < 0) throw new Error('Accessor count không hợp lệ');
        const mode = primitive.mode ?? 4;
        if (mode === 4) {
          if (elements.count % 3) throw new Error('TRIANGLES count không chia hết cho 3');
          triangles += elements.count / 3;
        } else if (mode === 5 || mode === 6) triangles += Math.max(0, elements.count - 2);
        const range = accessorRange(position);
        if (!range) {
          needsDecompression.push(`node ${index}, mesh ${node.mesh}, POSITION ${primitive.attributes.POSITION}: thiếu min/max`);
          continue;
        }
        hasBounds = true;
        for (let corner = 0; corner < 8; corner++) {
          const p = range.min.map((v, axis) => corner & (1 << axis) ? range.max[axis] : v);
          for (let axis = 0; axis < 3; axis++) {
            const value = world[axis] * p[0] + world[4 + axis] * p[1] + world[8 + axis] * p[2] + world[12 + axis];
            if (!Number.isFinite(value)) throw new Error('Bounds không hữu hạn');
            min[axis] = Math.min(min[axis], value); max[axis] = Math.max(max[axis], value);
          }
        }
      }
    }
    for (const child of node.children ?? []) visit(child, world, new Set([...ancestors, index]));
  };
  if (!json.scenes?.[0]) throw new Error('Không có scene 0');
  for (const node of json.scenes[0].nodes ?? []) visit(node, IDENTITY);
  const size = max.map((v, i) => v - min[i]);
  const bounds = hasBounds && !needsDecompression.length ? { min, max, size, footprint: [size[0], size[2]], height: size[1] } : null;
  if ((json.scene ?? 0) !== 0) warnings.push('default-scene-is-not-zero');
  const animations = (json.animations ?? []).map((animation, index) => {
    let start = Infinity, end = -Infinity, incomplete = false;
    for (const sampler of animation.samplers ?? []) {
      const accessor = json.accessors?.[sampler.input];
      if (!accessor) throw new Error(`Animation ${index} thiếu input accessor`);
      let range;
      if (finiteVector(accessor.min, 1) && finiteVector(accessor.max, 1)) range = [accessor.min[0], accessor.max[0]];
      else {
        try { range = readScalarTimes(json, bin, accessor); }
        catch (error) { incomplete = true; needsDecompression.push(`animation ${index}: ${error.message}`); continue; }
      }
      start = Math.min(start, range[0]); end = Math.max(end, range[1]);
    }
    if (!Number.isFinite(start) || !Number.isFinite(end)) start = end = 0;
    return { name: animation.name ?? `animation-${index}`, duration: incomplete ? null : end - start, start, end };
  });
  const extensions = new Set([...(json.extensionsUsed ?? []), ...(json.extensionsRequired ?? [])]);
  const collect = value => {
    if (!value || typeof value !== 'object') return;
    for (const [key, child] of Object.entries(value)) {
      if (key === 'extensions') for (const name of Object.keys(child ?? {})) extensions.add(name);
      if (key !== 'extras') collect(child);
    }
  };
  collect(json);
  return {
    bounds, longestAxis: bounds ? ['X', 'Y', 'Z'][size.indexOf(Math.max(...size))] : null,
    triangles, meshes: (json.meshes ?? []).length,
    primitives: (json.meshes ?? []).reduce((sum, mesh) => sum + (mesh.primitives ?? []).length, 0),
    meshInstances, primitiveInstances, materials: (json.materials ?? []).length,
    skinned: (json.skins ?? []).length > 0, animations,
    extensions: [...extensions].sort(cmp), needsDecompression, warnings,
  };
}

export function imageHeader(data) {
  if (data.length >= 24 && data.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]))) {
    return { format: 'png', width: data.readUInt32BE(16), height: data.readUInt32BE(20) };
  }
  if (data.length >= 12 && data.subarray(0, 12).equals(Buffer.from([171, 75, 84, 88, 32, 50, 48, 187, 13, 10, 26, 10]))) {
    return { format: 'ktx2', width: null, height: null };
  }
  if (data.length >= 2 && data[0] === 0xff && data[1] === 0xd8) {
    let offset = 2;
    const sof = new Set([0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf]);
    while (offset < data.length) {
      if (data[offset++] !== 0xff) throw new Error('Marker JPEG không hợp lệ');
      while (data[offset] === 0xff) offset++;
      const marker = data[offset++];
      if (marker === 0xda || marker === 0xd9) break;
      if (marker === 0x01 || (marker >= 0xd0 && marker <= 0xd8)) continue;
      if (offset + 2 > data.length) break;
      const length = data.readUInt16BE(offset);
      if (length < 2 || offset + length > data.length) throw new Error('Segment JPEG bị cắt');
      if (sof.has(marker) && length >= 8) return { format: 'jpeg', width: data.readUInt16BE(offset + 5), height: data.readUInt16BE(offset + 3) };
      offset += length;
    }
    throw new Error('Không tìm thấy kích thước JPEG');
  }
  if (data.length >= 12 && data.toString('ascii', 0, 4) === 'RIFF' && data.toString('ascii', 8, 12) === 'WEBP') {
    for (let offset = 12; offset + 8 <= data.length;) {
      const type = data.toString('ascii', offset, offset + 4), length = data.readUInt32LE(offset + 4), start = offset + 8;
      if (start + length > data.length) throw new Error('Chunk WebP bị cắt');
      if (type === 'VP8X' && length >= 10) return { format: 'webp', width: 1 + data.readUIntLE(start + 4, 3), height: 1 + data.readUIntLE(start + 7, 3) };
      if (type === 'VP8 ' && length >= 10 && data.toString('hex', start + 3, start + 6) === '9d012a') {
        return { format: 'webp', width: data.readUInt16LE(start + 6) & 0x3fff, height: data.readUInt16LE(start + 8) & 0x3fff };
      }
      if (type === 'VP8L' && length >= 5 && data[start] === 0x2f) {
        const bits = data.readUInt32LE(start + 1);
        return { format: 'webp', width: (bits & 0x3fff) + 1, height: ((bits >>> 14) & 0x3fff) + 1 };
      }
      offset = start + length + (length % 2);
    }
    throw new Error('Không tìm thấy kích thước WebP');
  }
  throw new Error('Header ảnh chưa hỗ trợ hoặc bị cắt');
}

function dataUri(uri) {
  const match = /^data:([^,]*),(.*)$/s.exec(uri);
  if (!match) throw new Error('Data URI không hợp lệ');
  return match[1].endsWith(';base64') ? Buffer.from(match[2], 'base64') : Buffer.from(decodeURIComponent(match[2]));
}

async function localUri(uri, file, repoRoot) {
  if (/^[a-z][a-z\d+.-]*:/i.test(uri) || uri.startsWith('//')) throw new Error('Không đọc URI mạng hoặc URI tuyệt đối');
  const target = path.resolve(path.dirname(file), decodeURIComponent(uri));
  const resolved = await realpath(target), root = await realpath(repoRoot);
  if (!resolved.startsWith(root + path.sep)) throw new Error('URI ngoài repo');
  return readFile(resolved);
}

async function texturesOf(data, file, repoRoot) {
  const { json, bin } = parseGlb(data);
  const images = [];
  for (const [index, image] of (json.images ?? []).entries()) {
    let bytes;
    if (image.uri) bytes = image.uri.startsWith('data:') ? dataUri(image.uri) : await localUri(image.uri, file, repoRoot);
    else {
      const view = json.bufferViews?.[image.bufferView];
      if (!view) throw new Error(`Ảnh ${index} thiếu bufferView`);
      if (view.extensions?.EXT_meshopt_compression) throw new Error(`Ảnh ${index} dùng bufferView meshopt`);
      const buffer = json.buffers?.[view.buffer ?? 0];
      const source = buffer?.uri ? (buffer.uri.startsWith('data:') ? dataUri(buffer.uri) : await localUri(buffer.uri, file, repoRoot)) : bin;
      const start = view.byteOffset ?? 0;
      if (start + view.byteLength > source.length) throw new Error(`Ảnh ${index} vượt buffer`);
      bytes = source.subarray(start, start + view.byteLength);
    }
    images.push({ index, name: image.name ?? null, mimeType: image.mimeType ?? null, bytes: bytes.length, ...imageHeader(bytes) });
  }
  return { count: images.length, textureObjects: (json.textures ?? []).length, images };
}

export function inferTags(id) {
  const words = new Set(id.toLowerCase().split(/[^a-z0-9]+/));
  const vocabulary = ['tree', 'pine', 'rock', 'bush', 'bridge', 'house', 'tower', 'fence', 'hut', 'log', 'stump', 'stone', 'river', 'wall', 'gate', 'farm', 'keep', 'mine', 'cart', 'chest', 'shield', 'spear', 'cannon', 'archer', 'wolf', 'boar', 'ant', 'wasp', 'dragon', 'ship'];
  const tags = vocabulary.filter(tag => words.has(tag));
  if (words.has('stones')) tags.push('stone');
  if (words.has('hut')) tags.push('house');
  if (words.has('pine') && !words.has('river') && !words.has('bomb')) tags.push('tree');
  return [...new Set(tags)].sort(cmp);
}

function canonicalId(relative) {
  const parts = relative.replace(/\.glb$/i, '').replace(/\.(high|medium|low)$/i, '').split('/');
  if (parts.at(-1) === parts.at(-2)) parts.pop();
  if (parts[0] === 'm0b') parts.shift();
  return parts.join('/');
}

export function matchOriginal(runtimeId, originals, sourceFiles, sourceIndex = {}) {
  const used = originals.filter(id => (sourceFiles[`${id}.glb`]?.usedBy ?? []).includes(runtimeId));
  if (used.length) return used.length === 1 ? { id: used[0], match: 'SOURCES.usedBy' } : null;
  if (originals.includes(runtimeId)) return { id: runtimeId, match: 'same-id' };
  const substitutes = Object.entries(sourceIndex.notMadeYet ?? {}).filter(([file, entry]) =>
    file.replace(/\.glb$/i, '') === runtimeId || (entry.usedBy ?? []).includes(runtimeId));
  if (substitutes.length === 1) {
    const [requested, record] = substitutes[0], id = record.standIn?.replace(/\.glb$/i, '');
    if (originals.includes(id)) return { id, match: 'SOURCES.notMadeYet.standIn', requested, reference: record };
  }
  // Only a GLB path written in this id's own note counts; no guessing from similar names.
  for (const [ids, note] of Object.entries(sourceIndex.noOriginalOnThisMachine ?? {})) {
    if (!ids.split(/,\s*/).includes(runtimeId) || typeof note !== 'string') continue;
    const explicit = [...note.matchAll(/art-src\/3d\/([a-zA-Z0-9_./-]+)\.glb/g)].map(m => m[1]).filter(id => originals.includes(id));
    if (new Set(explicit).size === 1) return { id: explicit[0], match: 'SOURCES.note-path', reference: note };
  }
  const leaf = runtimeId.split('/').at(-1);
  const flattened = originals.filter(id => id.split('/').slice(1).join('-').replace(/^ship-\d+-/, '') === leaf);
  return flattened.length === 1 ? { id: flattened[0], match: 'unique-filename-id' } : null;
}

export async function scanGame(game, repoRoot = REPO_ROOT) {
  if (!GAMES.includes(game)) throw new Error(`Game ngoài phạm vi: ${game}`);
  const root = path.join(repoRoot, 'games', game);
  const runtimeRoot = path.join(root, 'public/assets', game, 'models'), originalRoot = path.join(root, 'art-src/3d');
  const errors = [], inventories = [];
  for (const [source, directory] of [['runtime', runtimeRoot], ['original', originalRoot]]) {
    try {
      const files = await walkFiles(directory);
      inventories.push({ source, directory, files });
    } catch (error) { errors.push({ file: slash(path.relative(repoRoot, directory)), error: error.message }); }
  }
  const originals = inventories.find(i => i.source === 'original')?.files.filter(f => /\.glb$/i.test(f)) ?? [];
  let sourceIndex = {}, sourceFiles = {};
  const sourcesFile = path.join(originalRoot, 'SOURCES.json');
  try { sourceIndex = JSON.parse(await readFile(sourcesFile, 'utf8')); sourceFiles = sourceIndex.files ?? {}; }
  catch (error) { errors.push({ file: slash(path.relative(repoRoot, sourcesFile)), error: error.message }); }
  const manifests = new Map();
  for (const file of inventories.find(i => i.source === 'runtime')?.files.filter(f => /manifest[^/]*\.json$/i.test(path.basename(f))) ?? []) {
    try {
      const document = JSON.parse(await readFile(file, 'utf8'));
      for (const [key, entry] of Object.entries(document.models ?? {})) {
        for (const [tier, value] of Object.entries(entry.tiers ?? {})) {
          const url = decodeURIComponent((value.url ?? '').split(/[?#]/)[0]);
          const target = url.startsWith('/assets/') ? path.join(root, 'public', url) : path.resolve(path.dirname(file), url);
          if (!value.url) continue;
          if (manifests.has(target)) throw new Error(`Nhiều mục manifest trỏ tới ${target}`);
          manifests.set(target, { entry, key, tier, file: slash(path.relative(repoRoot, file)) });
        }
      }
    } catch (error) { errors.push({ file: slash(path.relative(repoRoot, file)), error: error.message }); }
  }
  const originalIds = originals.map(f => slash(path.relative(originalRoot, f)).replace(/\.glb$/i, ''));
  const assets = [], before = new Map();
  // md5 of every GLB before any metadata is read for this game.
  for (const { files } of inventories) for (const file of files.filter(f => /\.glb$/i.test(f))) {
    try { before.set(file, md5(await readFile(file))); }
    catch (error) { errors.push({ file: slash(path.relative(repoRoot, file)), error: error.message }); }
  }
  for (const { source, directory, files } of inventories) for (const file of files.filter(f => /\.glb$/i.test(f))) {
    const relative = slash(path.relative(directory, file)), id = relative.replace(/\.glb$/i, '');
    const manifest = manifests.get(file);
    const canonical = manifest?.key ?? canonicalId(relative);
    const category = id.split('/')[0], categoryHint = manifest?.entry.kind ?? canonical.split('/')[0];
    const original = source === 'runtime' ? matchOriginal(canonical, originalIds, sourceFiles, sourceIndex) : null;
    const originalFile = original ? path.join(originalRoot, `${original.id}.glb`) : null;
    const entry = {
      id, game, file: slash(path.relative(repoRoot, file)), source, bytes: null,
      category, categoryHint, tags: inferTags(id), tagsSource: 'auto',
      bounds: null, upAxis: '+Y', longestAxis: null, triangles: null, meshes: null, primitives: null,
      meshInstances: null, primitiveInstances: null, materials: null, textures: null,
      skinned: null, animations: [], extensions: [],
      licence: source === 'original' || original ? 'owner-tripo' : game === 'space-typing' ? 'space-library' : 'unknown',
      original: original ? {
        file: slash(path.relative(repoRoot, originalFile)), md5: before.get(originalFile) ?? null, match: original.match,
        sourceRecord: sourceFiles[`${original.id}.glb`] ?? null,
        requested: original.requested ?? null, reference: original.reference ?? null,
      } : null,
      sourceRecord: source === 'original' ? sourceFiles[`${id}.glb`] ?? null : null,
      sourcesFile: source === 'original' || original ? slash(path.relative(repoRoot, sourcesFile)) : null,
      manifest: manifest?.entry ?? null, manifestFile: manifest?.file ?? null, manifestKey: manifest?.key ?? null, tier: manifest?.tier ?? null,
      md5: before.get(file) ?? null, md5After: null, needsDecompression: [], warnings: [], errors: [],
    };
    if (source === 'runtime' && game === 'space-typing') entry.licence = 'space-library';
    try {
      const data = await readFile(file);
      entry.bytes = data.length;
      if (md5(data) !== entry.md5) throw new Error('GLB thay đổi sau ảnh chụp md5 đầu');
      Object.assign(entry, inspectGlb(data));
      entry.textures = await texturesOf(data, file, repoRoot);
      if (entry.bounds?.height > 30) entry.warnings.push('height-above-30m');
      if (entry.bounds?.height < 0.05) entry.warnings.push('height-below-0.05m');
      if (CREATURES.has(categoryHint) && entry.longestAxis && entry.longestAxis !== 'Y') entry.warnings.push('creature-longest-axis-not-Y');
      if (entry.sourceRecord?.md5 && entry.sourceRecord.md5 !== entry.md5) entry.warnings.push('SOURCES-md5-mismatch');
      if (source === 'runtime' && !original) entry.warnings.push('original-not-found');
    } catch (error) {
      entry.errors.push(error.message);
      errors.push({ file: entry.file, error: error.message });
    }
    assets.push(entry);
  }
  const changed = [];
  for (const asset of assets) {
    try {
      asset.md5After = md5(await readFile(path.join(repoRoot, asset.file)));
      if (asset.md5 !== asset.md5After) changed.push(asset.file);
    } catch (error) { changed.push(asset.file); errors.push({ file: asset.file, error: error.message }); }
  }
  for (const file of changed) errors.push({ file, error: 'MD5 trước/sau không khớp' });
  assets.sort((a, b) => cmp(a.source, b.source) || cmp(a.id, b.id));
  const needsDecompression = assets.filter(a => a.needsDecompression.length).map(a => ({ file: a.file, reasons: a.needsDecompression }));
  return {
    schemaVersion: 1, game, units: 'metres', upAxis: '+Y', sceneIndex: 0,
    statistics: { total: assets.length, runtime: assets.filter(a => a.source === 'runtime').length, original: originals.length, errors: errors.length, needsDecompression: needsDecompression.length },
    mediaIntegrity: { algorithm: 'md5', filesChecked: assets.length, changed },
    errors, needsDecompression, assets,
  };
}

async function main() {
  const out = path.join(REPO_ROOT, 'tools/map-factory/registry/out');
  await mkdir(out, { recursive: true });
  let total = 0, errors = 0, pending = 0;
  for (const game of GAMES) {
    const registry = await scanGame(game);
    await writeFile(path.join(out, `assets.${game}.json`), JSON.stringify(registry, null, 2) + '\n');
    const s = registry.statistics;
    console.log(`${game}: ${s.total} GLB (${s.runtime} runtime + ${s.original} original), ${s.errors} lỗi, ${s.needsDecompression} cần giải nén; md5 ${registry.mediaIntegrity.filesChecked - registry.mediaIntegrity.changed.length}/${s.total} không đổi`);
    total += s.total; errors += s.errors; pending += s.needsDecompression;
  }
  console.log(`Tổng: ${total} GLB, ${errors} lỗi, ${pending} cần giải nén.`);
  if (errors) process.exitCode = 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error); process.exitCode = 1; });
}
