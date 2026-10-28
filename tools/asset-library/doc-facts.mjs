import * as fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

export const REPO_ROOT = fileURLToPath(new URL('../../', import.meta.url));
export const DOCUMENTS = ['NAMES_EN.md', '3D_REQUESTS.md', '3D_IMPORT_2026-10-26.md',
  '3D_IMPORT_2026-10-28.md', 'ART_REPLACE_LATER.md', 'IMAGE_AUDIT_2026-10-25.md']
  .map(name => `docs/games/${name}`);
const HANDOFF = 'typing-game-handoff-2026-10-25';
const GAMES = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing'];
const PREFIX = { rong: 'dragon-hold', loigoi: 'typing-defense', tuyencuoi: 'typing-survival' };
// Danh sách cấm áp dụng cả nội dung bảng, đường dẫn tương đối và đích symlink.
const DENY = /immortality-cultivation|tu-tien|tu_tien|Tu Tiên|Tu Tien|monkeytype/iu;
const clean = s => (s ?? '').replace(/<br\s*\/?\s*>/giu, '; ').replace(/\[([^\]]+)\]\([^\n]*?\)/gu, '$1')
  .replace(/[`*]/gu, '').trim();
const unique = a => [...new Set(a.filter(Boolean))];
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const numeric = s => {
  const token = clean(s).match(/\d+(?:[.,]\d+)?/u)?.[0];
  return token === undefined ? undefined : Number(token.replace(',', '.'));
};
const integer = s => {
  const token = clean(s).match(/\d[\d., ]*/u)?.[0];
  return token === undefined ? undefined : Number(token.replace(/[., ]/gu, ''));
};
const levelOf = s => /Tạm chấp nhận/iu.test(s) ? 'provisional' : /(?:^|\s)Đạt(?:\s|$)/iu.test(s) ? 'pass' : undefined;
const gameOf = s => GAMES.find(g => s.includes(g)) ?? (/Rồng Giữ Ải/iu.test(s) ? 'dragon-hold'
  : /Lời Gọi/iu.test(s) ? 'typing-defense' : /Tuyến Cuối/iu.test(s) ? 'typing-survival'
    : /Space(?: Typing)?/iu.test(s) ? 'space-typing' : undefined);
const permitted = p => typeof p === 'string' && !DENY.test(p) && !path.isAbsolute(p)
  && !/[\\\0\r\n:]/u.test(p) && p.split('/').every(part => part && part !== '.' && part !== '..');
const cells = line => line.trim().replace(/^\||\|$/gu, '').split(/(?<!\\)\|/u).map(c => c.trim().replace(/\\\|/gu, '|'));
const separator = row => row.length > 0 && row.every(c => /^:?-{3,}:?$/u.test(c));

/** Đếm toàn bộ dòng thân bảng, kể cả bảng tóm tắt; không nhận header làm fact. */
export function markdownRows(text, file) {
  const lines = text.split(/\r?\n/u), rows = [];
  let headers, game = file.endsWith('/3D_IMPORT_2026-10-28.md') ? 'typing-defense' : undefined;
  let excluded = false, excludedDepth = 0;
  const stats = { file, pipeRows: 0, headers: 0, separators: 0, rows: 0, excluded: 0, facts: 0 };
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^#{1,6}\s/u.test(line)) {
      const depth = line.match(/^#+/u)[0].length;
      if (excluded && depth <= excludedDepth) excluded = false;
      if (DENY.test(line)) { excluded = true; excludedDepth = depth; }
      game = gameOf(line) ?? game;
    }
    if (!/^\|/u.test(line)) { headers = undefined; continue; }
    if (/^\| /u.test(line)) stats.pipeRows++;
    const row = cells(line);
    if (separator(row)) { stats.separators++; continue; }
    if (lines[i + 1]?.startsWith('|') && separator(cells(lines[i + 1]))) {
      headers = row.map(clean); stats.headers++; continue;
    }
    if (!headers) continue;
    stats.rows++;
    if (excluded || DENY.test(line)) { stats.excluded++; continue; }
    rows.push({ file, line: i + 1, evidence: `${file}:${i + 1}`, game,
      cells: Object.fromEntries(headers.map((h, j) => [h, row[j] ?? ''])) });
  }
  return { rows, stats };
}

// Kiểm từng tổ tiên: không đi theo symlink và không mở file thuộc danh sách cấm.
async function safeStat(root, rel, io) {
  if (!permitted(rel)) return null;
  let current = root, info;
  try {
    for (const part of rel.split('/')) {
      current = path.join(current, part);
      info = await io.lstat(current);
      if (info.isSymbolicLink()) return null;
    }
    return info;
  } catch (error) {
    if (error.code === 'ENOENT' || error.code === 'ENOTDIR') return null;
    throw error;
  }
}

function fileTokens(cell) {
  const tokens = [];
  let rest = cell.replace(/\[[^\]]*\]\((<[^>]+>|(?:[^()\n]|\([^()\n]*\))*)\)/gu, (_, target) => {
    tokens.push(target.replace(/^<|>$/gu, '')); return '';
  });
  rest = rest.replace(/`([^`]+)`/gu, (_, token) => { tokens.push(token); return ''; });
  // Một số bảng ghi đường dẫn không bọc backtick.
  tokens.push(...(rest.match(/(?:games\/|\.\.\/|[\w-]+\/)[^\s;<>]*\.(?:png|jpe?g|webp|glb|gltf|md)/giu) ?? []));
  return unique(tokens.filter(t => /\.(?:png|jpe?g|webp|glb|gltf|md)(?:#.*)?$/iu.test(t)));
}

function resolveFile(token, row, game, directory = '') {
  let raw;
  try { raw = decodeURI(token.split('#')[0]); } catch { return null; }
  if (DENY.test(raw) || /^(?:[a-z]+:|\/|\\)/iu.test(raw)) return null;
  let rel;
  if (raw.startsWith('games/') || raw.startsWith(`${HANDOFF}/`)) rel = raw;
  else if (raw.startsWith('../') || raw.startsWith('./')) rel = path.posix.normalize(path.posix.join(path.posix.dirname(row.file), raw));
  else if (row.file.startsWith(`${HANDOFF}/`)) rel = path.posix.join(path.posix.dirname(row.file), directory, raw);
  else if (game) rel = `games/${game}/art-src/${/\.gl[bt]f?$/iu.test(raw) ? '3d/' : ''}${raw.replace(/^art-src\//u, '')}`;
  return permitted(rel) ? rel : null;
}

function identity(raw) {
  const value = clean(raw).replace(/\.(?:png|glb)$/iu, '');
  const prefixed = value.match(/(?:^|\s)(rong|loigoi|tuyencuoi)_([^\s;]+)/u);
  if (prefixed) return { game: PREFIX[prefixed[1]], id: prefixed[2] };
  const code = raw.match(/`([^`]+)`/u)?.[1];
  return { id: code && !/[\r\n/]/u.test(code) ? code : undefined };
}

function fileReferences(row, game, directory) {
  const refs = [];
  for (const [column, cell] of Object.entries(row.cells)) {
    if (!/File|Đích|Ảnh|ảnh|Đường dẫn|đường dẫn|GLB gốc/u.test(column) || column === 'File Tripo') continue;
    for (const token of fileTokens(cell)) {
      const resolved = resolveFile(token, row, game, directory);
      if (resolved) refs.push({ path: resolved, column, evidence: row.evidence });
    }
  }
  return refs;
}

function factFrom(row) {
  const c = row.cells, entries = Object.entries(c);
  const pick = pattern => entries.find(([h]) => pattern.test(h))?.[1] ?? '';
  const rawId = pick(/^(?:id trong mã|Mã model|Mã · id)$/u);
  const ident = identity(rawId);
  let game = ident.game ?? gameOf(pick(/^Game$/u)) ?? row.game;
  const directory = clean(pick(/^(?:Thư mục Tripo|Thư mục)$/u));
  const pathColumns = fileReferences(row, game, directory);
  const paths = pathColumns.map(ref => ref.path);
  // INDEX: tên file có tiền tố xác định game và id, kể cả khi tiêu đề thiếu game.
  const indexId = identity(pick(/^Ảnh$/u));
  game = ident.game ?? indexId.game ?? game ?? paths.map(gameOf).find(Boolean);
  const id = ident.id ?? indexId.id ?? paths.map(p => /games\/[\w-]+\/(.+)\.[^.]+$/u.exec(p)?.[1])
    .find(Boolean)?.split('/').at(-1);
  if (!game || !id || DENY.test(id)) return null;
  const fact = { game, id, paths: unique(paths), aliases: [], evidence: [row.evidence], confidence: 'document',
    quality: { evidence: [row.evidence] }, provenance: {} };
  const isNames = row.file.endsWith('/NAMES_EN.md');
  if (isNames) {
    fact.name = clean(c['Tên tiếng Anh đề xuất']);
    fact.nameVi = clean(c['Tên Việt hiện tại']);
    fact.meaning = clean(pick(/^Nghĩa Việt/u));
    fact.nameSource = 'NAMES_EN';
  } else {
    const names = clean(pick(/^(?:Tên \(Việt \/ Anh\)|Tên|Nội dung|Món)$/u));
    if (c['Tên (Việt / Anh)']) {
      const [vi, en] = names.split(/\s+\/\s+/u);
      fact.nameVi = vi;
      if (en) { fact.name = en; fact.nameSource = path.posix.basename(row.file); }
    } else if (c.Món) {
      const match = names.match(/^(.+?)\s+\(([^()]*)\)$/u);
      if (match) { fact.name = match[1]; fact.nameVi = match[2]; fact.nameSource = 'INDEX'; }
    } else if (names && !/[`]/u.test(pick(/^Nội dung$/u))) fact.nameVi = names;
  }
  const code = clean(pick(/^Mã$/u));
  fact.aliases = unique([fact.nameVi, fact.meaning, clean(rawId), code, id]);
  const tripo = clean(c['File Tripo']);
  if (tripo) {
    fact.provenance.tripoFile = tripo;
    fact.aliases.push(tripo.replace(/\+/gu, ' ').replace(/\.glb$/iu, ''));
  }
  const triangles = integer(c['Tam giác']);
  if (triangles !== undefined) fact.triangles = triangles;
  const faceLimit = integer(c['Face limit'] ?? directory.match(/face\s+(\d+)/iu)?.[1]);
  if (faceLimit !== undefined) fact.provenance.faceLimit = faceLimit;
  const rig = clean(c.Rig ?? directory.match(/face\s+\d+\s*-\s*(.*?)\s*-\s*\d+\s*[aả]nh/iu)?.[1]);
  if (rig) fact.provenance.rig = rig;
  const confidence = numeric(c['Độ tin']);
  if (confidence !== undefined) { fact.provenance.matchConfidence = confidence; fact.confidence = confidence; }
  const need = pick(/^Mức cần$/u).match(/P[123]/u)?.[0];
  if (need) fact.quality.need = need;
  const score = numeric(c['Điểm'] ?? '');
  const is3d = Boolean(tripo) || paths.some(p => /\.glb$/iu.test(p));
  if (score !== undefined) fact.quality[is3d ? 'score3d' : 'score2d'] = score;
  const status = clean(c['Mức'] ?? c['Trạng thái'] ?? c['Điểm / mức']);
  const level = levelOf(status);
  if (level) fact.quality[is3d ? 'level3d' : 'level2d'] = level;
  const scoredStatus = status.match(/(?:Đạt|Tạm chấp nhận)\s+(\d+(?:[.,]\d+)?)/iu);
  if (scoredStatus && !tripo) fact.quality.score2d = numeric(scoredStatus[1]);
  if (row.file.endsWith('/ART_REPLACE_LATER.md')) fact.quality[is3d ? 'level3d' : 'level2d'] = 'provisional';
  fact.pathColumns = pathColumns;
  return fact;
}

function mergeFact(target, source) {
  // Nguồn được xử lý theo thứ tự ưu tiên tăng dần, tên NAMES_EN luôn thắng.
  for (const key of ['name', 'nameVi', 'meaning', 'nameSource', 'triangles', 'confidence']) {
    if (source[key] !== undefined && (!['name', 'nameVi', 'meaning', 'nameSource'].includes(key) || target.nameSource !== 'NAMES_EN')
      && !(key === 'confidence' && typeof target.confidence === 'number' && typeof source.confidence !== 'number')) target[key] = source[key];
  }
  for (const key of ['paths', 'aliases', 'evidence']) target[key] = unique([...(target[key] ?? []), ...source[key]]);
  target.provenance = { ...target.provenance, ...source.provenance };
  target.quality = { ...target.quality, ...source.quality, evidence: unique([...(target.quality?.evidence ?? []), ...source.quality.evidence]) };
  const level = target.quality.level3d ?? target.quality.level2d;
  if (level) target.quality.level = level;
  return target;
}

/** Chỉ đọc tài liệu trong whitelist và lstat đường dẫn được tài liệu nhắc đến. */
export async function readDocFacts({ repoRoot = REPO_ROOT, io = fs } = {}) {
  const files = [...DOCUMENTS], warnings = [], documents = [], facts = [], references = [], pending = [];
  if ((await safeStat(repoRoot, HANDOFF, io))?.isDirectory()) {
    for (const name of (await io.readdir(path.join(repoRoot, HANDOFF))).sort(cmp)) {
      if (/^tripo-upload[^/]*$/u.test(name) && !DENY.test(name)) files.push(`${HANDOFF}/${name}/INDEX.md`);
    }
  }
  for (const file of files) {
    if (!(await safeStat(repoRoot, file, io))?.isFile()) { warnings.push(`${file}: không có tài liệu thường, bỏ qua`); continue; }
    const parsed = markdownRows(await io.readFile(path.join(repoRoot, file), 'utf8'), file);
    for (const row of parsed.rows) {
      const fact = factFrom(row);
      if (!fact) {
        references.push(...fileReferences(row, gameOf(row.cells.Game ?? '') ?? row.game,
          clean(row.cells['Thư mục Tripo'] ?? row.cells['Thư mục'])));
        if (/P[123]/u.test(row.cells['Mức cần'] ?? '')) pending.push(row);
        continue;
      }
      const { pathColumns, ...fields } = fact;
      facts.push(fields); parsed.stats.facts++;
      references.push(...pathColumns);
    }
    documents.push(parsed.stats);
  }
  // Bảng việc thay sau chỉ ghi V62/K17: nối bằng mã duyệt của 3D_REQUESTS,
  // chỉ nhận khi mã có đúng một id trong cùng game.
  const approvalCodes = new Map();
  for (const fact of facts.filter(f => f.evidence[0].startsWith(`${DOCUMENTS[1]}:`))) for (const alias of fact.aliases) {
    for (const match of alias.matchAll(/(?:^|[\s/])([A-Z]+\d+(?:-[A-Z0-9]+)?)(?=\s|$)/gu)) {
      const key = `${fact.game}:${match[1]}`;
      if (!approvalCodes.has(key)) approvalCodes.set(key, new Set());
      approvalCodes.get(key).add(fact.id);
    }
  }
  for (const row of pending) {
    const code = clean(row.cells.Mã).match(/^([A-Z]+\d+(?:-[A-Z0-9]+)?)(?=\s|$)/u)?.[1];
    const ids = approvalCodes.get(`${row.game}:${code}`);
    if (ids?.size !== 1) continue;
    facts.push({ game: row.game, id: [...ids][0], paths: [], aliases: [clean(row.cells.Mã)],
      evidence: [row.evidence], quality: { need: row.cells['Mức cần'].match(/P[123]/u)[0], evidence: [row.evidence] }, provenance: {} });
    documents.find(doc => doc.file === row.file).facts++;
  }
  // Đợt nhập mới nhất chốt chất lượng 3D; audit chốt điểm 2D; tên đứng cuối.
  const sourceRank = f => f.evidence[0].includes('NAMES_EN.md:') ? 60 : f.evidence[0].includes('3D_IMPORT_2026-10-28.md:') ? 50
    : f.evidence[0].includes('IMAGE_AUDIT') ? 40 : f.evidence[0].includes('ART_REPLACE_LATER') ? 30
      : f.evidence[0].includes('3D_IMPORT') ? 20 : 10;
  const rank = f => sourceRank(f) - (f.paths.some(p => p.includes('/tripo-spares/')) ? 0.5 : 0);
  facts.sort((a, b) => rank(a) - rank(b));
  const byId = {}, byPath = {};
  for (const fact of facts) {
    const key = `${fact.game}:${fact.id}`;
    byId[key] = mergeFact(byId[key] ?? { game: fact.game, id: fact.id }, fact);
    for (const p of fact.paths) byPath[p] = mergeFact(byPath[p] ?? { game: fact.game, id: fact.id }, fact);
  }
  const missing = [];
  for (const ref of references) {
    ref.exists = Boolean((await safeStat(repoRoot, ref.path, io))?.isFile());
    if (!ref.exists && !missing.includes(ref.path)) missing.push(ref.path);
  }
  return { schema: 'asset-library-doc-facts/1', documents, byId, byPath, references,
    missing: missing.sort(cmp), warnings };
}

/** Sau nối sổ: tài liệu thắng dữ liệu mồi, tuyển chọn vẫn có ưu tiên cao nhất. */
export function mergeDocFacts(cards, data, { curated = [] } = {}) {
  if (data.schema !== 'asset-library-doc-facts/1') return cards;
  const idCounts = new Map();
  for (const card of cards) {
    const key = card.origin + ':' + card.uid.split('/').at(-1).split(':').at(-1);
    idCounts.set(key, (idCounts.get(key) ?? 0) + 1);
  }
  for (const card of cards) {
    const key = card.origin + ':' + card.uid.split('/').at(-1).split(':').at(-1);
    const specific = unique([...(card.files ?? []), ...(card.copies ?? [])].map(f => f.path))
      .map(p => data.byPath?.[p]).filter(Boolean);
    const general = idCounts.get(key) === 1 ? data.byId?.[key] : undefined;
    const found = general ? [general, ...specific] : specific;
    if (!found.length) continue;
    if (found.some(f => DENY.test(JSON.stringify(f)))) continue;
    const fact = found.reduce((acc, f) => mergeFact(acc, f), {});
    const override = Object.assign({}, ...curated.filter(row => row && typeof row.uid === 'string'
      && (row.md5s === undefined || Array.isArray(row.md5s)) && !DENY.test(JSON.stringify(row))
      && (row.uid === card.uid || card.formerUids?.includes(row.uid))));
    if (fact.name && !Object.hasOwn(override, 'name')) { card.name = fact.name; card.nameSource = fact.nameSource; }
    card.aliases = unique([...(card.aliases ?? []), ...fact.aliases]);
    card.quality = { ...fact.quality, ...override.quality,
      evidence: unique([...fact.quality.evidence, ...(override.quality?.evidence ?? [])]) };
    card.provenance = { ...fact.provenance, ...card.provenance };
    if (fact.meaning && !Object.hasOwn(override, 'meaning')) card.meaning = fact.meaning;
    if (fact.nameVi && !Object.hasOwn(override, 'nameVi')) card.nameVi = fact.nameVi;
    if (fact.triangles !== undefined) card.model = { ...card.model, triangles: { original: fact.triangles, ...card.model?.triangles } };
    if (!Object.hasOwn(override, 'status') && card.status === 'unscored' && fact.quality.level) card.status = fact.quality.level;
  }
  return cards;
}

/** Chỉ ghi một file đầu ra; không ghi gì trong nguồn. */
export async function writeDocFacts(options = {}) {
  const { repoRoot = REPO_ROOT, io = fs } = options;
  const output = 'library/out/doc-facts.json';
  // Từ chối cả thư mục đầu ra bị thay bằng symlink.
  for (const rel of ['library', 'library/out', output]) {
    try { if ((await io.lstat(path.join(repoRoot, rel))).isSymbolicLink()) throw new Error(`Từ chối symlink đầu ra: ${rel}`); }
    catch (error) { if (error.code !== 'ENOENT') throw error; }
  }
  const data = await readDocFacts(options);
  await io.mkdir(path.join(repoRoot, 'library/out'), { recursive: true });
  await io.writeFile(path.join(repoRoot, output), JSON.stringify(data, null, 2) + '\n');
  return data;
}

export async function main(args = process.argv.slice(2), options = {}) {
  if (args.length) throw new Error('doc-facts.mjs không nhận cờ; chỉ ghi library/out/doc-facts.json');
  const data = await writeDocFacts(options);
  for (const doc of data.documents) console.log(`${doc.file}: ${doc.rows} dòng thân bảng; ${doc.facts} fact; ${doc.excluded} dòng bị chặn`);
  console.log(`${Object.keys(data.byId).length} game+id; ${Object.keys(data.byPath).length} đường dẫn; missing[]: ${data.missing.length}`);
  for (const p of data.missing) console.log(`MISSING ${p}`);
  for (const warning of data.warnings) console.log(`CẢNH BÁO ${warning}`);
  return data;
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
