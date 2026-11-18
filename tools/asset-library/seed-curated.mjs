import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { mergeDocFacts, markdownRows } from './doc-facts.mjs';

export const REPO_ROOT = fileURLToPath(new URL('../../', import.meta.url));
export const FILES = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing', 'audio-libraries'];
const GAMES = FILES.slice(0, 4);
const VISIBLE = new Set(['shipped', 'pass', 'provisional', 'unscored']);
// Danh sách cấm: kiểm cả nội dung trước khi sinh dòng công khai.
const DENY = /immortality-cultivation|tu-tien|tu_tien|monkeytype/iu;
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
export const unaccent = s => s.normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/gu, 'd').replace(/Đ/gu, 'D');
const words = s => unaccent(String(s)).replace(/([a-z])([A-Z])/gu, '$1 $2').toLowerCase().replace(/[^a-z0-9]+/gu, ' ').trim();
const unique = a => [...new Set(a.filter(x => typeof x === 'string' && x.trim()).map(x => x.trim()))].sort(cmp);
const title = s => s.replace(/\b[a-z]/gu, c => c.toUpperCase());
const clean = s => String(s ?? '').replace(/[`*]/gu, '').replace(/<br\s*\/?\s*>/giu, ' ').trim();

// Chỉ dịch mồi; không suy tên từ prompt hoặc lấy chú thích Tripo làm tên thật.
const TRANSLATIONS = {
  'choi canh doi': 'Hilltop Watch Hut', 'nha rai da': 'Stone Hut', 'cau tau': 'Wooden Jetty',
  'cau go': 'Wooden Bridge', 'cau do': 'Red Bridge', 'cau tre': 'Bamboo Bridge',
  'hai dang': 'Lighthouse', 'goc da rong': 'Hollow Banyan Stump', 'da ke': 'Stone Ledge',
  're vom': 'Root Arch', 'thac ho sut': 'Sinkhole Waterfall', 'them da trang': 'White Stone Steps',
  'vach thac bac': 'Silver Waterfall Cliff', 'cuong thi': 'Hopping Zombie', 'ma da': 'Water Ghost',
  'mam go': 'Sapling', 'tat phuong': 'Fire Bird', 'thuong luong': 'Water Serpent',
  'chuon chuon tre': 'Bamboo Dragonfly', 'dai bang tinh': 'Eagle Spirit',
  'linh giao dai': 'Long Spearman', 'linh giao': 'Spearman', 'linh khien': 'Shield Bearer',
  'go lan': 'Rolling Log', 'rao tre': 'Bamboo Fence', 'giao dai': 'Long Spear',
  'khien dong': 'Bronze Shield', 'en bao': 'Storm Swallow', 'than tien': 'Divine Arrow',
  'coi lon': 'Heavy Mortar', 'vac lua': 'Fire Cannon', 'bac thang': 'Terrace',
  'chuong trau': 'Buffalo Pen', 'ham sau': 'Deep Shaft', 'lo duc tien': 'Coin Foundry',
  'tram cuu thuong': 'Aid Station', 'vuon thao duoc': 'Herb Garden', 'xuong cua': 'Sawmill',
  'xuong rao': 'Fence Workshop', 'but loi': 'Thunder Brush', 'muc bang': 'Ice Ink',
  'phong an': 'Seal', 'vang am': 'Echo', 'ao ca': 'Fish Pond', 'nuong': 'Field',
  'heo': 'Pig', 'trau': 'Buffalo', 'tre': 'Bamboo', 'ruin xl': 'Extra Large Ruin', 'ruin l': 'Large Ruin',
  'ruin m': 'Medium Ruin', 'ruin s': 'Small Ruin'
};
export function translate(stem) {
  let value = words(stem).replace(/^(?:ship|g)\s*\d+\s*/u, '');
  for (const [vi, en] of Object.entries(TRANSLATIONS).sort((a, b) => b[0].length - a[0].length)) {
    value = value.replace(new RegExp(`\\b${vi}\\b`, 'gu'), en);
  }
  return title(value || 'Asset');
}

async function safeFile(root, rel, io, optional = false) {
  if (DENY.test(rel) || path.isAbsolute(rel) || rel.split('/').some(p => !p || p === '..' || p === '.')) throw new Error('Đường dẫn đọc bị chặn');
  let current = root;
  try {
    for (const part of rel.split('/')) {
      current = path.join(current, part);
      if ((await io.lstat(current)).isSymbolicLink()) throw new Error(`Không đọc qua symlink: ${rel}`);
    }
    return await io.readFile(current, 'utf8');
  } catch (e) { if (optional && e.code === 'ENOENT') return null; throw e; }
}

/** Chỉ đọc tên, md5 riêng tư để chặn rò; không in tên riêng tư ra log. */
export async function privateInventory({ repoRoot = REPO_ROOT, io = fs } = {}) {
  const text = await safeFile(repoRoot, 'media/private.md5', io, true);
  const names = new Set(), md5s = new Set(), paths = new Set();
  for (const line of (text ?? '').split(/\r?\n/u)) {
    const m = line.match(/^([a-f\d]{32}) [ *](.+)$/iu);
    if (m) { md5s.add(m[1].toLowerCase()); paths.add(m[2]); names.add(path.posix.basename(m[2]).replace(/\.[^.]+$/u, '')); }
  }
  const rel = 'games/space-typing/art-src/Dota-Sounds';
  async function walk(p) {
    try {
      let current = repoRoot;
      for (const part of p.split('/')) { current = path.join(current, part); if ((await io.lstat(current)).isSymbolicLink()) return; }
      for (const item of await io.readdir(current, { withFileTypes: true })) {
        if (item.isDirectory()) await walk(p + '/' + item.name);
        else if (item.isFile()) { paths.add(p + '/' + item.name); names.add(item.name.replace(/\.[^.]+$/u, '')); }
      }
    } catch (e) { if (e.code !== 'ENOENT') throw e; }
  }
  await walk(rel);
  return { names: [...names].filter(Boolean), md5s, paths, hasPrivateLock: text !== null };
}
export function leaks(text, inventory) {
  return inventory.names.some(name => text.includes(name));
}
function restricted(card, inventory) {
  return DENY.test(JSON.stringify(card)) || card.private || card.notForRelease || card.hidden
    || card.licence?.private || card.licence?.notForRelease || card.status === 'private'
    || [...(card.files ?? []), ...(card.copies ?? [])].some(f =>
      f.private || f.notForRelease || f.onDrive === 'private' || inventory.md5s.has(f.md5)
      || inventory.paths.has(f.path) || /(?:^|\/)(?:Dota-Sounds|shared\/music)(?:\/|$)/u.test(f.path ?? ''));
}
function folderRule(card, taxonomy) {
  const [game, original] = card.uid.split(':');
  const rel = original.replace(/^src\/assets\//u, '').replace(/^public\/assets\/[^/]+\/(?:models\/)?/u, '');
  const folders = taxonomy.folderMap[game] ?? {};
  const folder = Object.keys(folders).filter(p => rel === p || rel.startsWith(p + '/')).sort((a, b) => b.length - a.length)[0];
  const fallback = /^(?:guides|heroes)\//u.test(rel) ? { kind: 'character' }
    : /^skills\//u.test(rel) ? { kind: 'vfx' }
      : /^backgrounds\/|^docs\/art-requests\/defense-maps\//u.test(rel) ? { kind: 'backdrop' }
        : /(?:^|\/)icons\//u.test(rel) ? { kind: 'ui' } : {};
  const rule = folders[folder] ?? fallback;
  const stem = rel.split('/').at(-1).replace(rule.hyphenVariants ? /-v\d+$/u : /$^/u, '');
  const local = stem.replace(/^g\d{2}-/u, '');
  const prefix = Object.keys(rule.itemPrefixes ?? {}).filter(p => local === p || local.startsWith(p + '-')).sort((a, b) => b.length - a.length)[0];
  return { ...rule, ...(rule.perItem ? rule.items?.[stem] ?? rule.itemPrefixes?.[prefix] : {}) };
}
function vocabulary(text, card, taxonomy) {
  const normalized = ' ' + words(text) + ' ';
  const literal = ' ' + text.normalize('NFC').replace(/([a-z])([A-Z])/gu, '$1 $2').toLowerCase().replace(/[^\p{L}0-9]+/gu, ' ').trim() + ' ';
  const tokens = new Set(normalized.trim().split(' '));
  for (const token of [...tokens]) {
    if (token.endsWith('s')) tokens.add(token.slice(0, -1));
    if (token === 'enemies') tokens.add('enemy');
  }
  for (const group of taxonomy.synonyms) if (group.some(alias => {
    const key = words(alias);
    // Các chữ Việt mơ hồ chỉ dịch trong phạm vi đã khai, không gõ -> gỗ.
    if (['cau', 'da'].includes(key)) return false;
    if (alias === 'go') return literal.includes(' gỗ ');
    const exact = alias.normalize('NFC').toLowerCase().replace(/[-_]+/gu, ' ');
    return literal.includes(' ' + exact + ' ');
  })) tokens.add(group[0]);
  for (const [vi, scope] of Object.entries(taxonomy.viTokens ?? {})) {
    if (tokens.has(vi) && scope.folders.some(f => card.uid.includes(f.replace(/\/$/u, '')))) tokens.add(scope.word);
  }
  return taxonomy.tags.filter(tag => tokens.has(tag) || normalized.includes(' ' + tag + ' ')).sort(cmp);
}

/** Dùng lại AL-07/08; dữ liệu đầu vào được sao chép, không sửa catalog của người gọi. */
export function prepareSeeds({ catalog, audio = { cards: [] }, facts, taxonomy, notes = new Map(), inventory = { names: [], md5s: new Set(), paths: new Set() } }) {
  const cards = [...new Map([...catalog.cards, ...audio.cards].map(c => [c.uid, structuredClone(c)])).values()];
  mergeDocFacts(cards, facts);
  const candidates = [], skipped = { hidden: 0, restricted: 0, unsupported: 0 };
  for (const card of cards.sort((a, b) => cmp(a.uid, b.uid))) {
    if (restricted(card, inventory)) { skipped.restricted++; continue; }
    if (!VISIBLE.has(card.status)) { skipped.hidden++; continue; }
    const target = GAMES.includes(card.origin) ? card.origin
      : (card.files ?? []).some(f => f.path?.startsWith('~/AudioLab/libraries/')) ? 'audio-libraries' : null;
    if (!target || !card.uid.startsWith(card.origin + ':')) { skipped.unsupported++; continue; }
    const stem = card.uid.split('/').at(-1).split(':').at(-1);
    const source = card.nameSource;
    const documented = card.name && (source === 'NAMES_EN' || /^3D_IMPORT_/u.test(source ?? ''));
    const name = documented ? unaccent(clean(card.name)) : translate(stem);
    const rawAliases = [card.nameVi, card.meaning, ...(card.aliases ?? []), stem, words(stem),
      clean(card.provenance?.tripoFile ?? card.provenance?.downloadedAs).replace(/\.[^.]+$/u, '').replace(/\+/gu, ' ')];
    const aliases = unique(rawAliases.flatMap(s => s ? [s, unaccent(s)] : []));
    const rule = folderRule(card, taxonomy);
    const kind = rule.kind ?? card.kind ?? null;
    const text = [name, ...aliases, ...(notes.get(card.uid) ?? []), card.uid.split(':')[1]].join(' ');
    const tags = vocabulary(text, card, taxonomy);
    const subkind = rule.subkind ?? card.subkind ?? null;
    // Nhãn loại/con là bằng chứng từ folderMap, không bù nhãn vật liệu tùy ý.
    const classifiedTags = unique([...tags, ...[kind, subkind].filter(t => taxonomy.tags.includes(t))]);
    const row = { uid: card.uid, md5s: unique((card.files ?? []).filter(f => f.role !== 'rejected').map(f => f.md5)),
      name, nameSource: documented ? source : 'seed-translation', aliases, kind, subkind, tags: classifiedTags,
      biome: rule.biomes ?? card.biome ?? [], style: rule.style ?? card.style ?? taxonomy.gameStyles[card.origin] ?? 'neutral',
      canonical: {}, reuseNotes: null, quality: null, reviewed: null };
    if (rule.private || rule.notForRelease || leaks(JSON.stringify(row), inventory)) { skipped.restricted++; continue; }
    const confidence = source === 'NAMES_EN' ? 1 : documented ? 0.9 : TRANSLATIONS[words(stem)] ? 0.75
      : /(?:^|\s)(?:dong|sam|se|tieu|tro|phay|gach|lam|moc|tinh)(?:\s|$)/u.test(words(stem)) ? 0.25
        : /[^\x00-\x7f]/u.test(card.nameVi ?? '') ? 0.4 : 0.55;
    candidates.push({ target, row, type: card.type, confidence });
  }
  return { candidates, skipped };
}

export async function loadInputs({ repoRoot = REPO_ROOT, io = fs } = {}) {
  const json = async (rel, optional = false) => JSON.parse(await safeFile(repoRoot, rel, io, optional) ?? '{"cards":[]}');
  const [catalog, audio, facts, taxonomy, inventory] = await Promise.all([
    json('library/out/catalog.json'), json('library/out/audio-catalog.json', true), json('library/out/doc-facts.json'),
    json('library/taxonomy.json'), privateInventory({ repoRoot, io })]);
  const notes = new Map();
  // AL-07 đã nối đường dẫn; chỉ đọc thêm ghi chú của hai tài liệu đã biết.
  const docs = new Map();
  for (const file of ['docs/games/3D_IMPORT_2026-10-26.md', 'docs/games/3D_IMPORT_2026-10-28.md']) {
    const text = await safeFile(repoRoot, file, io, true);
    if (text) for (const row of markdownRows(text, file).rows) docs.set(row.evidence, Object.entries(row.cells)
      .filter(([h]) => /Vấn đề|Sửa khi dựng|Ghi chú|Tên/u.test(h)).map(([, s]) => clean(s)).join(' '));
  }
  for (const card of catalog.cards) {
    const key = card.origin + ':' + card.uid.split('/').at(-1).split(':').at(-1);
    const found = [facts.byId?.[key], ...(card.files ?? []).map(f => facts.byPath?.[f.path])].filter(Boolean);
    notes.set(card.uid, unique(found.flatMap(f => (f.evidence ?? []).map(e => docs.get(e)))));
  }
  return { catalog, audio, facts, taxonomy, notes, inventory };
}

/** Ghi đúng năm file cố định; dòng cũ giữ nguyên byte, kể cả CRLF và khoảng trắng. */
export async function seedCurated({ repoRoot = REPO_ROOT, io = fs, inputs, dryRun = false } = {}) {
  repoRoot = path.resolve(repoRoot);
  const data = inputs ?? await loadInputs({ repoRoot, io });
  const result = prepareSeeds(data);
  const plans = [], rows = [], seen = new Set();
  for (const target of FILES) {
    const rel = `library/curated/${target}.jsonl`;
    const previous = await safeFile(repoRoot, rel, io, true) ?? '';
    if (DENY.test(previous) || leaks(previous, data.inventory)) throw new Error(`Chặn rò trong file đã có: ${rel}`);
    const records = [];
    for (const raw of previous.match(/[^\n]*\n|[^\n]+$/gu) ?? []) {
      if (!raw.trim()) throw new Error(`Dòng trống trong ${rel}; cần người duyệt sửa`);
      const row = JSON.parse(raw);
      if (typeof row.uid !== 'string' || seen.has(row.uid)) throw new Error(`Uid thiếu hoặc trùng trong ${rel}`);
      seen.add(row.uid); rows.push(row); records.push({ uid: row.uid, raw });
    }
    const additions = result.candidates.filter(c => c.target === target && !seen.has(c.row.uid));
    for (const { row } of additions) { seen.add(row.uid); rows.push(row); records.push({ uid: row.uid, raw: JSON.stringify(row) + '\n' }); }
    if (!additions.length) continue;
    records.sort((a, b) => cmp(a.uid, b.uid));
    if (records.slice(0, -1).some(r => !r.raw.endsWith('\n'))) throw new Error(`${rel}: dòng cũ thiếu xuống dòng; giữ nguyên, cần người duyệt sửa`);
    plans.push({ rel, previous, text: records.map(r => r.raw).join(''), added: additions.length });
  }
  if (!dryRun && plans.length) {
    // Kiểm lại toàn bộ tổ tiên trước mọi lần ghi; không theo symlink.
    const dir = path.join(repoRoot, 'library/curated');
    for (const rel of ['library', 'library/curated']) {
      try { if ((await io.lstat(path.join(repoRoot, rel))).isSymbolicLink()) throw new Error('Thư mục tuyển chọn là symlink'); }
      catch (e) { if (e.code !== 'ENOENT' || rel === 'library') throw e; }
    }
    await io.mkdir(dir, { recursive: true });
    for (const plan of plans) {
      if ((await safeFile(repoRoot, plan.rel, io, true) ?? '') !== plan.previous) {
        throw new Error(`${plan.rel}: file vừa được làn khác sửa; giữ nguyên và chạy lại`);
      }
      await io.writeFile(path.join(repoRoot, plan.rel), plan.text, 'utf8');
    }
  }
  const visible = result.candidates.length;
  const named = result.candidates.filter(c => c.row.name && c.row.kind).length;
  const models = result.candidates.filter(c => c.type === 'model3d');
  const tagged = models.filter(c => c.row.tags.length >= 2).length;
  return { added: plans.reduce((n, p) => n + p.added, 0), changedFiles: plans.length, files: plans.map(({ rel, added }) => ({ rel, added })),
    visible, named, namedPercent: visible ? 100 * named / visible : 100,
    models: models.length, tagged, taggedPercent: models.length ? 100 * tagged / models.length : 100,
    skipped: result.skipped, lowestConfidence: result.candidates.sort((a, b) => a.confidence - b.confidence || cmp(a.row.uid, b.row.uid))
      .slice(0, 50).map(c => ({ uid: c.row.uid, name: c.row.name, confidence: c.confidence, nameSource: c.row.nameSource })), rows };
}
export async function main(args = process.argv.slice(2), options = {}) {
  if (args.some(a => a !== '--dry-run')) throw new Error('Chỉ nhận --dry-run');
  const { rows, ...result } = await seedCurated({ ...options, dryRun: args.includes('--dry-run') });
  console.log(JSON.stringify(result, null, 2));
  return result;
}
if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(e => { console.error(e.message); process.exitCode = 1; });
}
