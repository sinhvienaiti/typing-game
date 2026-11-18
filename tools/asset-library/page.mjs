import * as fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { REPO_ROOT, main, safeInfo } from './find.mjs';
import { loadCards, loadThumbIndex } from './thumbs.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
// Danh sách cấm, áp dụng trước khi đọc nguồn và trước khi xuất dữ liệu.
const DENY = /immortality-cultivation|tu-tien|tu_tien|monkeytype/iu;
const OUTPUTS = ['library/out/catalog.html', 'library/out/catalog.data.js'];
const NETWORK = /https?:\/\/[^\s<>"']*/giu;
const AUDIO = /\.(?:ogg|opus|wav|mp3|m4a|aac|flac|aiff?)$/iu;
const pick = (object, keys) => Object.fromEntries(keys.filter(k => object?.[k] != null).map(k => [k, object[k]]));

// Không nhúng sổ tải nguồn (có URL), sourceRows trùng lặp hay metadata GLB thừa.
// Giữ các trường mà search.mjs dùng, kể cả đường dẫn file ẩn.
function fileView(file) {
  const view = pick(file, ['path', 'role', 'md5', 'sha256', 'bytes', 'local', 'onDrive', 'hidden',
    'status', 'canonical', 'variant', 'tier', 'image', 'audio', 'location', 'copyOf', 'master']);
  if (file.glb) view.glb = pick(file.glb, ['bounds', 'triangles', 'clips', 'animations', 'skinned', 'sockets']);
  return view;
}

function clean(value) {
  if (typeof value === 'string') return DENY.test(value) ? undefined : value.replace(NETWORK, '[nguồn ngoài mạng]');
  if (Array.isArray(value)) return value.map(clean).filter(v => v !== undefined);
  if (value && typeof value === 'object') return Object.fromEntries(Object.entries(value)
    .filter(([key]) => !DENY.test(key)).map(([key, v]) => [key, clean(v)]).filter(([, v]) => v !== undefined));
  return value;
}

// Chỉ tạo URL local từ file đã kiểm từng tổ tiên; không theo symlink.
export async function localHref(rel, { repoRoot, home = os.homedir(), io = fs }) {
  if (typeof rel !== 'string' || DENY.test(rel)) return null;
  const external = rel.startsWith('~/AudioLab/');
  const root = external ? home : repoRoot;
  const source = external ? rel.slice(2) : rel;
  try {
    if (!(await safeInfo(root, source, io))?.isFile()) return null;
    return path.relative(path.join(repoRoot, 'library/out'), path.join(root, source)).split(path.sep)
      .map(part => encodeURIComponent(part).replace(/'/gu, '%27')).join('/');
  } catch (error) {
    if (['EACCES', 'EPERM', 'ENOENT', 'ENOTDIR'].includes(error.code) || /symlink|bị chặn/u.test(error.message)) return null;
    throw error;
  }
}

export async function pageCards({ repoRoot = REPO_ROOT, io = fs, home = os.homedir() } = {}) {
  const cards = await loadCards({ repoRoot, io });
  // Dùng nguyên các dòng AL-12; không dịch hoặc suy đoán lại tên/loại.
  if (await safeInfo(repoRoot, 'library/curated', io)) {
    const rows = new Map();
    for (const name of (await io.readdir(path.join(repoRoot, 'library/curated'))).sort()) {
      if (!name.endsWith('.jsonl') || DENY.test(name)) continue;
      const rel = `library/curated/${name}`;
      if (!(await safeInfo(repoRoot, rel, io))?.isFile()) continue;
      for (const line of (await io.readFile(path.join(repoRoot, rel), 'utf8')).split(/\r?\n/u).filter(Boolean)) {
        const row = JSON.parse(line);
        if (typeof row.uid === 'string' && !DENY.test(row.uid)) rows.set(row.uid, row);
      }
    }
    for (const card of cards) {
      const row = rows.get(card.uid);
      if (row) for (const key of ['name', 'nameSource', 'nameVi', 'aliases', 'kind', 'subkind', 'tags',
        'biome', 'style', 'reuseNotes', 'quality', 'reviewed']) if (row[key] !== undefined) card[key] = row[key];
    }
  }
  const warnings = [], thumbIndex = await loadThumbIndex({ repoRoot, io });
  const thumbs = new Map(thumbIndex.thumbnails.map(row => [row.uid, row.thumb]));
  const result = [];
  for (const card of cards) {
    const view = pick(card, ['uid', 'short', 'name', 'nameVi', 'meaning', 'aliases', 'description', 'path', 'type',
      'origin', 'kind', 'subkind', 'tags', 'biome', 'style', 'quality', 'status', 'pipeline', 'hidden',
      'model', 'licence', 'audio', 'usedBy', 'canonical', 'reuseNotes', 'reviewed', 'similar']);
    view.files = card.files.filter(f => typeof f.path === 'string' && !DENY.test(f.path)).map(fileView);
    view.copies = (card.copies ?? []).filter(f => !DENY.test(f.path ?? '')).map(fileView);
    view.provenance = pick(card.provenance, ['prompt', 'tripoFile', 'description']);
    const thumb = thumbs.get(card.uid);
    if (thumb && /^library\/\.thumbs\/(?:[a-f0-9]{32}\.webp|[a-f0-9]{64}\.wave\.png)$/u.test(thumb)) {
      view.thumb = await localHref(thumb, { repoRoot, home, io });
      if (!view.thumb) warnings.push(`Ảnh nhỏ không còn trên máy: ${card.uid}`);
    }
    const prompt = card.provenance?.prompt ?? card.files.find(f => f.role === 'prompt')?.path;
    if (typeof prompt === 'string' && !DENY.test(prompt)) {
      const href = await localHref(prompt, { repoRoot, home, io });
      if (href) {
        const absolute = prompt.startsWith('~/AudioLab/') ? path.join(home, prompt.slice(2)) : path.join(repoRoot, prompt);
        try { view.promptPreview = [...await io.readFile(absolute, 'utf8')].slice(0, 300).join(''); }
        catch (error) { warnings.push(`Không đọc được prompt ${card.uid}: ${error.code ?? error.message}`); }
      }
    }
    for (const file of view.files) if (AUDIO.test(file.path) && file.local !== false) {
      file.href = await localHref(file.path, { repoRoot, home, io });
    }
    result.push(clean(view));
  }
  return { cards: result, warnings };
}

export async function buildPage({ repoRoot = REPO_ROOT, io = fs, home = os.homedir(), stdout = process.stdout } = {}) {
  const { cards, warnings } = await pageCards({ repoRoot, io, home });
  const catalog = JSON.parse(await io.readFile(path.join(repoRoot, 'library/out/catalog.json'), 'utf8'));
  const taxonomy = clean(JSON.parse(await io.readFile(path.join(repoRoot, 'library/taxonomy.json'), 'utf8')));
  // Gỡ duy nhất từ khóa export. Nội dung lõi còn lại giống từng byte với AL-09.
  const core = (await io.readFile(path.join(HERE, 'lib/search.mjs'), 'utf8')).replace(/^export /gmu, '');
  const [shell, css, app] = await Promise.all(['index.html', 'style.css', 'app.js']
    .map(name => io.readFile(path.join(HERE, 'page', name), 'utf8')));
  const data = { schema: 'asset-library/1', scannedAt: catalog.scannedAt, cards, taxonomy };
  const serialize = value => JSON.stringify(value).replace(/</gu, '\\u003c').replace(/\u2028/gu, '\\u2028').replace(/\u2029/gu, '\\u2029');
  const js = `window.CATALOG = ${serialize(data)};\n`;
  // IIFE cho search tránh trùng tên helper của phần giao diện; classic script chạy file://.
  const script = `/* SEARCH_CORE_BEGIN */\n(function () {\n${core}\nwindow.CatalogSearch = { createSearch, search };\n})();\n/* SEARCH_CORE_END */`;
  const html = shell.replace('/* PAGE_STYLE */', () => css).replace('/* PAGE_SEARCH */', () => script)
    .replace('/* PAGE_APP */', () => app);
  const htmlBytes = Buffer.byteLength(html), dataBytes = Buffer.byteLength(js);
  if (htmlBytes > 200_000 || htmlBytes + dataBytes > 8_000_000) throw new Error(`Trang vượt trần: ${htmlBytes} + ${dataBytes} byte`);
  if (/https?:\/\//iu.test(html + js) || DENY.test(js)) throw new Error('Trang chứa URL mạng hoặc nội dung bị cấm');
  // Không mkdir, rename, sao chép hay sửa nguồn. Chặn cả symlink ở đầu ra trước khi ghi.
  for (const rel of OUTPUTS) {
    const info = await safeInfo(repoRoot, rel, io);
    if (info && !info.isFile()) throw new Error(`Đầu ra không phải file thường: ${rel}`);
  }
  await io.writeFile(path.join(repoRoot, OUTPUTS[1]), js);
  await io.writeFile(path.join(repoRoot, OUTPUTS[0]), html);
  const result = { cards: cards.length, thumbnails: cards.filter(c => c.thumb).length,
    prompts: cards.filter(c => c.promptPreview).length, htmlBytes, dataBytes, totalBytes: htmlBytes + dataBytes, warnings };
  stdout.write(`Trang: ${result.cards} thẻ; ${result.thumbnails} ảnh nhỏ; ${result.prompts} đoạn prompt.\n`);
  stdout.write(`HTML ${htmlBytes} byte; dữ liệu ${dataBytes} byte; tổng ${result.totalBytes} byte.\n`);
  for (const warning of warnings) stdout.write(`Cảnh báo: ${warning}\n`);
  return result;
}

export async function runPage(argv = [], options = {}) {
  if (argv.length) throw new Error('Cách dùng: pnpm lib:page');
  await buildPage(options);
  return 0;
}
main(import.meta.url, runPage);
