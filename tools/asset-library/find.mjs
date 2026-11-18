import * as fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createSearch } from './lib/search.mjs';

export const REPO_ROOT = fileURLToPath(new URL('../../', import.meta.url));
const GAMES = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing'];
// Danh sách cấm áp dụng cả đường dẫn trong mục lục và đích symlink.
const DENY = /immortality-cultivation|tu-tien|tu_tien|monkeytype/iu;
const HIDDEN = new Set(['draft', 'rejected', 'review', 'prompt', 'report', 'glb-spare', 'unknown']);
const FILTERS = ['type', 'kind', 'sub', 'tag', 'biome', 'style', 'game', 'used-by', 'status', 'pipeline',
  'min-score', 'max-tris', 'has', 'drive', 'limit'];
const BOOLEAN = new Set(['all', 'requested', 'json', 'help']);
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;

export function parseArgs(argv, values, flags) {
  const options = {}, positional = [];
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--') { positional.push(...argv.slice(i + 1)); break; }
    if (!arg.startsWith('-')) { positional.push(arg); continue; }
    const [key, ...parts] = arg.replace(/^--/u, '').split('=');
    if (flags.includes(key)) {
      if (parts.length) throw new Error(`Cờ --${key} không nhận giá trị`);
      options[key] = true;
    } else if (values.includes(key)) {
      const value = parts.length ? parts.join('=') : argv[++i];
      if (!value || value.startsWith('--')) throw new Error(`Thiếu giá trị cho --${key}`);
      if (['min-score', 'max-tris', 'limit', 'variant'].includes(key)) {
        if (options[key] !== undefined) throw new Error(`Chỉ nhận một --${key}`);
        options[key] = value;
      } else options[key] = options[key] === undefined ? value : [...[options[key]].flat(), value];
    } else throw new Error(`Tùy chọn không hỗ trợ: ${arg}`);
  }
  return { options, positional };
}

export async function loadCatalog({ repoRoot = REPO_ROOT, io = fs } = {}) {
  let catalog;
  try { catalog = JSON.parse(await io.readFile(path.join(repoRoot, 'library/out/catalog.json'), 'utf8')); }
  catch (error) {
    if (error.code === 'ENOENT') throw new Error('Chưa có mục lục; chạy pnpm lib:scan');
    throw error;
  }
  if (catalog.schema !== 'asset-library/1' || !Array.isArray(catalog.cards) ||
    catalog.cards.some(card => typeof card.uid !== 'string' || !Array.isArray(card.files))) {
    throw new Error('Mục lục không đúng lược đồ asset-library/1');
  }
  return catalog;
}

// Chỉ lstat từng tổ tiên; không đi qua symlink tới game đang dừng hay ngoài repo.
export async function safeInfo(repoRoot, rel, io = fs) {
  if (typeof rel !== 'string' || DENY.test(rel) || path.isAbsolute(rel) || /[\\\0\r\n:]/u.test(rel) ||
    rel.split('/').some(p => !p || p === '.' || p === '..')) throw new Error(`Đường dẫn bị chặn: ${rel}`);
  let current = repoRoot, info;
  try {
    for (const part of rel.split('/')) {
      current = path.join(current, part);
      info = await io.lstat(current);
      if (info.isSymbolicLink()) throw new Error(`Không đi theo symlink: ${rel}`);
    }
    return info;
  } catch (error) {
    if (error.code === 'ENOENT' || error.code === 'ENOTDIR') return null;
    throw error;
  }
}

export async function staleWarnings(catalog, { repoRoot = REPO_ROOT, io = fs } = {}) {
  const scanned = Date.parse(catalog.scannedAt);
  if (!Number.isFinite(scanned)) return ['Mục lục thiếu scannedAt hợp lệ; chạy pnpm lib:scan'];
  const newer = [];
  async function inspect(rel, recurse = false) {
    let info;
    try { info = await safeInfo(repoRoot, rel, io); }
    catch (error) { if (/symlink/u.test(error.message)) return; throw error; }
    if (!info) return;
    if (info.isFile() && (!recurse || path.basename(rel) === 'manifest.json') && info.mtimeMs > scanned) newer.push(rel);
    if (recurse && info.isDirectory()) {
      let names;
      try { names = await io.readdir(path.join(repoRoot, rel)); }
      catch (error) { if (error.code === 'ENOENT' || error.code === 'ENOTDIR') return; throw error; }
      for (const name of names.sort(cmp)) {
        if (DENY.test(name)) continue;
        await inspect(`${rel}/${name}`, true);
      }
    }
  }
  for (const game of GAMES) {
    await inspect(`games/${game}/media.md5`);
    await inspect(`games/${game}/art-src/3d/SOURCES.json`);
    await inspect(`games/${game}/public/assets/${game}/models`, true);
  }
  return newer.map(rel => `Mục lục cũ hơn ${rel}; chạy pnpm lib:scan`);
}

export const visibleFiles = (card, all = false) => card.files.filter(f => all || (!f.hidden && !HIDDEN.has(f.role) && !HIDDEN.has(f.status)));
export const cardName = card => card.name || card.uid.split(':').at(-1).split('/').at(-1)
  .replace(/[-_]+/gu, ' ').replace(/\b\p{L}/gu, c => c.toUpperCase());
export const number = value => typeof value === 'number' ? value.toLocaleString('vi-VN') : '—';
export const driveLabel = value => ({ yes: 'có', no: 'chưa', changed: 'đã đổi', private: 'riêng tư', external: 'ngoài repo' })[value] ?? '—';
export function triangleLabel(card) {
  const t = card.model?.triangles;
  if (typeof t === 'number') return number(t);
  const files = visibleFiles(card).slice().sort((a, b) => {
    const rank = f => f.role === 'runtime-high' ? 0 : f.role === 'runtime-medium' ? 1 : f.role === 'glb-original' ? 2 : 3;
    return rank(a) - rank(b);
  });
  const runtime = card.pipeline === 'runtime' || files.some(f => /^runtime-/u.test(f.role));
  if (runtime && (t?.high ?? t?.medium) !== undefined) return `${number(t.high ?? t.medium)} r`;
  const file = files.find(f => typeof f.glb?.triangles === 'number');
  if (file && /^runtime-/u.test(file.role)) return `${number(file.glb.triangles)} r`;
  return number(t?.original ?? file?.glb.triangles);
}
export function qualityLabel(card) {
  const q = card.quality ?? {};
  const level = ({ shipped: 'đã ship', pass: 'đạt', provisional: 'tạm', unscored: 'chưa chấm',
    requested: 'mới xin', draft: 'nháp', rejected: 'bị loại', review: 'đang duyệt', private: 'riêng tư' })[card.status] ?? card.status ?? 'chưa chấm';
  const score = card.type === 'model3d' ? q.score3d : card.type === 'image' ? q.score2d : q.score;
  return `${score === undefined ? '' : `${card.type === 'model3d' ? '3D' : card.type === 'image' ? '2D' : 'Âm'} ${number(score)} `}${level}`;
}
export function table(headers, rows) {
  const clean = v => String(v ?? '—').replace(/[\r\n\t\x1b]/gu, ' ');
  const data = [headers, ...rows].map(row => row.map(clean));
  const widths = headers.map((_, i) => Math.max(...data.map(row => [...row[i]].length)));
  return data.map(row => row.map((cell, i) => cell + ' '.repeat(widths[i] - [...cell].length)).join('  ').trimEnd()).join('\n');
}

export async function runFind(argv = [], { repoRoot = REPO_ROOT, io = fs, stdout = process.stdout, stderr = process.stderr } = {}) {
  const { options, positional } = parseArgs(argv, FILTERS, [...BOOLEAN]);
  if (options.help) {
    stdout.write(`Cách dùng: pnpm lib:find [từ khóa] [--${FILTERS.join(' <giá trị>] [--')} <giá trị>] [--all] [--requested] [--json]\n`);
    return 0;
  }
  const catalog = await loadCatalog({ repoRoot, io });
  const taxonomy = JSON.parse(await io.readFile(path.join(repoRoot, 'library/taxonomy.json'), 'utf8'));
  const index = createSearch(catalog, { taxonomy });
  const { limit = 20, ...filters } = options;
  const rows = index.search(positional.join(' '), filters);
  // Lõi chịu trách nhiệm kiểm cả limit, kể cả trường hợp không có kết quả.
  index.search('', { limit });
  for (const warning of await staleWarnings(catalog, { repoRoot, io })) stderr.write(`Cảnh báo: ${warning}\n`);
  const cards = rows.slice(0, Number(limit)).map(row => row.card);
  if (options.json) stdout.write(JSON.stringify({ schema: catalog.schema, scannedAt: catalog.scannedAt, cards }, null, 2) + '\n');
  else {
    const games = { 'dragon-hold': 'Rồng', 'typing-defense': 'Lời Gọi', 'typing-survival': 'Tuyến Cuối', 'space-typing': 'Space' };
    stdout.write(table(['#', 'uid', 'tên', 'loại/con', 'game', 'tam giác', 'chất lượng', 'Drive'], cards.map((card, i) => [
      i + 1, card.uid, cardName(card), [card.kind, card.subkind].filter(Boolean).join('/'), games[card.origin] ?? card.origin,
      triangleLabel(card), qualityLabel(card), [...new Set(visibleFiles(card).map(f => driveLabel(f.onDrive)))].join(', ') || '—',
    ])) + `\n(${cards.length} trên ${rows.length}; --all hiện thêm bản dự phòng và bản loại, --requested hiện món mới xin)\n`);
  }
  return 0;
}

export function main(moduleUrl, run) {
  if (process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === moduleUrl) {
    run(process.argv.slice(2)).then(code => { process.exitCode = code; }).catch(error => {
      process.stderr.write(`Lỗi: ${error.message}\n`); process.exitCode = 1;
    });
  }
}
main(import.meta.url, runFind);
