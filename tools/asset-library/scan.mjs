import * as fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { imageHeader, inspectGlb } from '../map-factory/registry/scan-assets.mjs';
import { groupFiles } from './lib/grammar.mjs';
import { load, kindFor, styleFor } from './lib/taxonomy.mjs';
import { createHashCache } from './lib/hash-cache.mjs';

export const REPO_ROOT = fileURLToPath(new URL('../../', import.meta.url));
export const GAMES = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing'];
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const IMAGE = /\.(?:png|jpe?g|webp|avif|gif|svg|tga)$/iu;
const beneath = (p, base) => p === base || p.startsWith(base + '/');
const relative = p => typeof p === 'string' && p.length > 0 && !path.isAbsolute(p)
  && !/[\\\0\r\n:]/u.test(p) && p.split('/').every(part => part && part !== '.' && part !== '..');
// Danh sách cấm cố định vẫn có hiệu lực khi cấu hình bị sửa nhầm.
const DENY = /(?:^|\/)(?:immortality-cultivation|tu-tien|tu_tien|monkeytype)(?:\/|$)|(?:^|\/)TU_TIEN_[^/]*|tu-tien/iu;

export function pathAllowed(p, sources) {
  return relative(p) && !DENY.test(p)
    && ![...(sources.deny ?? []), ...(sources.ignore ?? [])].some(glob => path.matchesGlob(p, glob));
}

// Không dùng walkFiles của Map Factory: hàm đó chủ ý đi theo symlink.
// Kiểm từng thành phần cả với đường cấu hình và sidecar, tránh symlink ở tổ tiên.
async function safeInfo(repoRoot, rel, io) {
  let current = repoRoot;
  let info;
  for (const part of rel.split('/')) {
    current = path.join(current, part);
    info = await io.lstat(current);
    if (info.isSymbolicLink()) return null;
  }
  return info;
}

async function readJson(repoRoot, rel, io, allowed, warnings, optional = true) {
  if (!allowed(rel)) return {};
  try {
    if (!(await safeInfo(repoRoot, rel, io))?.isFile()) return {};
    return JSON.parse(await io.readFile(path.join(repoRoot, rel), 'utf8'));
  } catch (error) {
    if (optional && error.code === 'ENOENT') return {};
    if (error.code === 'ENOENT') { warnings.push(`${rel}: ENOENT — file đã biến mất`); return {}; }
    throw error;
  }
}

async function walk(repoRoot, rel, io, allowed, warnings, found, optional = false) {
  if (!allowed(rel)) return;
  try {
    const info = await safeInfo(repoRoot, rel, io);
    if (!info) return;
    if (info.isDirectory()) {
      for (const name of (await io.readdir(path.join(repoRoot, rel))).sort(cmp)) {
        await walk(repoRoot, `${rel}/${name}`, io, allowed, warnings, found);
      }
    } else if (info.isFile()) found.add(rel);
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
    if (!optional) warnings.push(`${rel}: ENOENT — file đã biến mất khi đi cây`);
  }
}

function pngAlpha(data) {
  if (data.length < 33) throw new Error('IHDR PNG bị cắt');
  const color = data[25];
  if (color === 4 || color === 6) return true;
  for (let offset = 8; offset + 12 <= data.length;) {
    const length = data.readUInt32BE(offset);
    if (offset + 12 + length > data.length) throw new Error('Chunk PNG bị cắt');
    const type = data.toString('ascii', offset + 4, offset + 8);
    if (type === 'tRNS') return true;
    if (type === 'IDAT' || type === 'IEND') break;
    offset += length + 12;
  }
  return false;
}

export function inspectImage(data, extension) {
  // SVG là ảnh vector có sẵn; Map Factory chưa nhận định dạng này.
  if (extension === '.svg') {
    const svg = data.toString('utf8').match(/<svg\b[^>]*>/iu)?.[0];
    if (!svg) throw new Error('Thiếu phần tử SVG');
    const dimension = name => {
      const value = svg.match(new RegExp(`\\b${name}\\s*=\\s*["'](\\d+(?:\\.\\d+)?)(?:px)?["']`, 'iu'));
      return value ? Number(value[1]) : null;
    };
    const box = svg.match(/\bviewBox\s*=\s*["']([^"']+)["']/iu)?.[1].trim().split(/[\s,]+/u).map(Number);
    return { w: dimension('width') ?? (box?.length === 4 ? box[2] : null),
      h: dimension('height') ?? (box?.length === 4 ? box[3] : null), alpha: true };
  }
  const header = imageHeader(data);
  let alpha = false;
  if (header.format === 'png') alpha = pngAlpha(data);
  if (header.format === 'webp') {
    for (let offset = 12; offset + 8 <= data.length;) {
      const type = data.toString('ascii', offset, offset + 4);
      const length = data.readUInt32LE(offset + 4), start = offset + 8;
      if (start + length > data.length) throw new Error('Chunk WebP bị cắt');
      if (type === 'VP8X' && length >= 10) { alpha = Boolean(data[start] & 0x10); break; }
      if (type === 'VP8L' && length >= 5) { alpha = Boolean(data.readUInt32LE(start + 1) & 0x10000000); break; }
      if (type === 'ALPH') alpha = true;
      offset = start + length + length % 2;
    }
  }
  return { w: header.width, h: header.height, alpha };
}

function glbFields(row) {
  return Object.fromEntries(['bounds', 'longestAxis', 'triangles', 'meshes', 'primitives',
    'meshInstances', 'primitiveInstances', 'materials', 'skinned', 'animations', 'extensions',
    'needsDecompression', 'warnings'].filter(key => row[key] !== undefined).map(key => [key, row[key]]));
}

function folderRule(taxonomy, game, stem) {
  const folders = taxonomy.folderMap[game] ?? {};
  const folder = Object.keys(folders).filter(p => beneath(stem, p)).sort((a, b) => b.length - a.length)[0];
  const rule = folders[folder] ?? {};
  return { ...rule, ...(rule.items?.[stem.split('/').at(-1)] ?? {}) };
}

function report(catalog, stats) {
  const files = catalog.cards.flatMap(card => card.files);
  const roles = {};
  for (const file of files) roles[file.role] = (roles[file.role] ?? 0) + 1;
  const unknown = files.filter(file => file.role === 'unknown');
  return `# Báo cáo quét lõi 2D và 3D\n\nQuét lúc: ${catalog.scannedAt}\n\n`
    + `Số thẻ: **${catalog.cards.length}**. Số file: **${files.length}**.\n\n`
    + '| Vai trò | Số file |\n|---|---:|\n'
    + Object.keys(roles).sort(cmp).map(role => `| ${role} | ${roles[role]} |`).join('\n')
    + `\n\nUnknown: **${unknown.length}** (${files.length ? (100 * unknown.length / files.length).toFixed(4) : '0.0000'}%).\n\n`
    + unknown.map(file => `- ${file.path}`).join('\n')
    + '\n\n## GLB gốc theo game\n\n'
    + GAMES.map(game => `- ${game}: ${catalog.cards.filter(card => card.origin === game).flatMap(card => card.files).filter(file => file.role === 'glb-original').length}`).join('\n')
    + `\n\n## Bộ đệm\n\nTrúng cache: ${stats.hash.hit}; mồi media: ${stats.hash.seeded}; băm mới: ${stats.hash.hashed}; byte băm: ${stats.hash.bytesHashed}; dùng sổ GLB: ${stats.registry}; đọc GLB: ${stats.inspected}.\n\n`
    + `## Cảnh báo (${catalog.warnings.length})\n\n`
    + (catalog.warnings.length ? catalog.warnings.map(w => `- ${w}`).join('\n') : 'Không có.') + '\n';
}

/** Chỉ ghi ba sản phẩm AL-05. io và hooks phục vụ cây mẫu/test biến mất giữa lượt. */
export async function scan({ repoRoot = REPO_ROOT, game, scanDate = new Date().toISOString(),
  io = fs, hooks = {} } = {}) {
  if (game !== undefined && !GAMES.includes(game)) throw new Error(`Game không được phép: ${game}`);
  if (typeof scanDate !== 'string' || !/^\d{4}-\d\d-\d\dT/u.test(scanDate) || !Number.isFinite(Date.parse(scanDate))) {
    throw new Error('--scan-date cần ngày ISO hợp lệ');
  }
  repoRoot = path.resolve(repoRoot);
  const warnings = [];
  const sources = JSON.parse(await io.readFile(path.join(repoRoot, 'library/sources.json'), 'utf8'));
  const taxonomy = load();
  const allowed = p => pathAllowed(p, sources);
  const cache = await createHashCache({ repoRoot, io, allowPath: p => allowed(p)
    && GAMES.some(id => beneath(p, `games/${id}`)) });
  const stats = { hash: cache.stats, registry: 0, inspected: 0 };
  const cards = [];
  for (const id of GAMES.filter(id => !game || id === game)) {
    const found = new Set();
    for (const root of sources.roots) {
      if (root.game !== id || !['art-src', 'public', 'src/assets'].some(p => root.path === `games/${id}/${p}`)) continue;
      await walk(repoRoot, root.path, io, allowed, warnings, found, true);
    }
    const prefix = `games/${id}/`;
    const logical = p => p.slice(prefix.length).replace(/^art-src\//u, '');
    const physical = new Map();
    for (const p of [...found].sort(cmp)) {
      if (IMAGE.test(p) || /\.glb$/iu.test(p) || /\.prompt\.txt$/iu.test(p)
        || /(?:^|\/)README[^/]*\.md$/iu.test(p)
        || /\/(?:\.reports|\.campaign3d-model-cache)\/[^/]+\.json$/iu.test(p)
        || /\/vs-(?:buildings|characters)-(?:run|\d+[a-z]?(?:-continuation)?)\.json$/u.test(p)) physical.set(logical(p), p);
    }
    const source = await readJson(repoRoot, `${prefix}art-src/3d/SOURCES.json`, io, allowed, warnings);
    // AL-05 dùng liên kết image; nối preset/manifest, lock và tuyển chọn ở AL-06.
    const sourceFiles = Object.fromEntries(Object.entries(source.files ?? {}).filter(([p, row]) =>
      allowed(`${prefix}art-src/3d/${p}`) && (!row.image || allowed(`${prefix}${row.image.startsWith('art-src/') ? row.image : 'art-src/' + row.image}`))));
    const registry = await readJson(repoRoot, `tools/map-factory/registry/out/assets.${id}.json`, io, allowed, warnings);
    const registryByFile = new Map((registry.assets ?? []).map(row => [row.file, row]));
    for (const group of groupFiles(physical.keys(), { game: id, taxonomy, sources: { files: sourceFiles } })) {
      if (!allowed(`${prefix}art-src/${group.stem}`)) continue;
      const files = [];
      for (const parsed of group.files) {
        const p = physical.get(parsed.path);
        await hooks.beforeFile?.(p);
        try {
          const info = await safeInfo(repoRoot, p, io);
          if (!info?.isFile()) { warnings.push(`${p}: không còn là file thường`); continue; }
          const cached = await cache.get(p, info);
          const row = cached.row;
          const { path: _, ...metadata } = parsed;
          const file = { ...metadata, path: p, md5: row.md5, sha256: row.sha256, bytes: info.size, local: true };
          if (IMAGE.test(p)) {
            if (!row.image && !row.imageError) {
              try { row.image = inspectImage(await cached.data(), path.extname(p).toLowerCase()); }
              catch (error) { if (error.code === 'ENOENT') throw error; row.imageError = error.message; }
            }
            file.image = row.image ?? { w: null, h: null, alpha: null };
            if (row.imageError) warnings.push(`${p}: ${row.imageError}`);
          } else if (/\.glb$/iu.test(p)) {
            const registered = registryByFile.get(p);
            if (registered?.md5 === row.md5 && !registered.errors?.length) {
              file.glb = glbFields(registered); stats.registry++;
            } else {
              if (!row.glb && !row.glbError) {
                try { row.glb = inspectGlb(await cached.data()); stats.inspected++; }
                catch (error) { if (error.code === 'ENOENT') throw error; row.glbError = error.message; }
              }
              file.glb = row.glb ?? null;
              if (row.glbError) warnings.push(`${p}: ${row.glbError}`);
            }
            for (const warning of [...(file.glb?.warnings ?? []), ...(file.glb?.needsDecompression ?? [])]) warnings.push(`${p}: ${warning}`);
          }
          const after = await safeInfo(repoRoot, p, io);
          if (!after?.isFile() || after.size !== info.size || after.mtimeMs !== info.mtimeMs) {
            cache.forget(p); warnings.push(`${p}: file đã đổi trong lúc quét; bỏ qua lượt này`); continue;
          }
          files.push(file);
        } catch (error) {
          if (error.code !== 'ENOENT') throw error;
          cache.forget(p); warnings.push(`${p}: ENOENT — file đã biến mất khi đọc`);
        }
      }
      if (!files.length) continue;
      const rule = folderRule(taxonomy, id, group.stem);
      cards.push({ uid: `${id}:${group.stem}`, short: `${id}:${group.stem.split('/').at(-1)}`,
        type: files.some(file => /\.glb$/iu.test(file.path)) ? 'model3d' : 'image',
        origin: id, kind: kindFor(id, group.stem), subkind: rule.subkind ?? null,
        style: rule.style ?? styleFor(id), biome: rule.biomes ?? [], files });
    }
  }
  cards.sort((a, b) => cmp(a.uid, b.uid));
  const allFiles = cards.flatMap(card => card.files);
  const unknownCount = allFiles.filter(file => file.role === 'unknown').length;
  if (unknownCount > allFiles.length * 0.01) {
    warnings.push(`Unknown vượt ngưỡng thiết kế 1%: ${unknownCount}/${allFiles.length} (${(100 * unknownCount / allFiles.length).toFixed(4)}%); cần duyệt ngữ pháp tên file`);
  }
  const catalog = { schema: 'asset-library/1', scannedAt: scanDate, cards,
    warnings: [...new Set(warnings)].sort(cmp) };
  await cache.save();
  await io.mkdir(path.join(repoRoot, 'library/out'), { recursive: true });
  await io.writeFile(path.join(repoRoot, 'library/out/catalog.json'), JSON.stringify(catalog, null, 2) + '\n');
  await io.writeFile(path.join(repoRoot, 'library/out/scan-report.md'), report(catalog, stats));
  return { catalog, stats };
}

export async function main(args = process.argv.slice(2), options = {}) {
  const parsed = {};
  for (let i = 0; i < args.length; i++) {
    const key = { '--game': 'game', '--scan-date': 'scanDate' }[args[i]];
    if (!key || !args[i + 1] || args[i + 1].startsWith('--')) throw new Error(`Cờ không hợp lệ: ${args[i]}`);
    parsed[key] = args[++i];
  }
  const start = performance.now();
  const result = await scan({ ...options, ...parsed });
  console.log(`${result.catalog.cards.length} thẻ; ${result.catalog.cards.flatMap(c => c.files).length} file; ${result.catalog.warnings.length} cảnh báo; ${((performance.now() - start) / 1000).toFixed(3)} giây`);
  console.log(JSON.stringify(result.stats));
  return result;
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
