import nodeFs from 'node:fs';
import * as fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createHash } from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { audioHeader } from './lib/audio-header.mjs';

export const REPO_ROOT = fileURLToPath(new URL('../../', import.meta.url));
const GAMES = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing'];
// Danh sách cấm áp trước lstat/readdir/readFile, cả với dữ liệu từ index và ledger.
const DENY = /immortality-cultivation|tu[-_]tien|TU_TIEN_|(?:^|\/)monkeytype(?:\/|$)/iu;
const AUDIO = /\.(?:wav|ogg|mp3|m4a|opus)$/iu;
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const valid = p => typeof p === 'string' && p.length > 0 && !path.isAbsolute(p)
  && !/[\\\0\r\n:]/u.test(p) && p.split('/').every(s => s && s !== '.' && s !== '..') && !DENY.test(p);
const stem = p => p.replace(/\.[^/.]+$/u, '');
const variantOf = p => stem(p).match(/[_-](\d+)$/u)?.[1] ?? null;
const familyStem = p => stem(p).replace(/[_-]\d+$/u, '');
const clean = row => !DENY.test(JSON.stringify(row));
const missing = e => ['ENOENT', 'EACCES', 'EPERM'].includes(e.code);

/** Bảng nguồn Space: giữ số Freesound, tác giả, URL, tên file nguồn và dòng chứng cứ. */
export function parseAttribution(text = '') {
  const rows = new Map();
  let section = '';
  for (const [i, line] of text.split(/\r?\n/u).entries()) {
    if (line.startsWith('## ')) section = line.slice(3);
    if (!line.startsWith('|')) continue;
    const cells = line.split('|').slice(1, -1).map(c => c.trim().replaceAll('`', ''));
    if (!AUDIO.test(cells[0] ?? '')) continue;
    let prefix;
    if (section.includes('Menu / UI')) prefix = 'src/assets/audio/ui/';
    else if (section.includes('Boss SFX')) prefix = 'public/assets/audio/sfx/kenney/';
    else if (section.includes('Duel war')) prefix = 'public/assets/audio/duel/war/';
    else if (section.includes('dragon SFX')) prefix = 'public/assets/audio/dragon/';
    if (!prefix) continue;
    const source = { section, sourceFile: cells[1], evidence: `games/space-typing/public/assets/audio/ATTRIBUTION.md:${i + 1}` };
    if (cells[3]) Object.assign(source, { soundId: cells[1].match(/#(\d+)/u)?.[1], author: cells[2], url: cells[3] });
    else Object.assign(source, { author: 'Kenney', url: `https://kenney.nl/assets/${section.includes('Boss') && cells[1].startsWith('Impact') ? 'impact-sounds' : cells[1].startsWith('Interface') ? 'interface-sounds' : 'sci-fi-sounds'}` });
    rows.set(prefix + cells[0], source);
  }
  return rows;
}

function card(uid, origin, family, file, licence, extra = {}) {
  const [kind = 'audio', subkind = null] = (family || 'audio').split('/');
  return { uid, short: `${origin}:${uid.split('/').at(-1).split(':').at(-1)}`, origin,
    type: kind === 'music' ? 'music' : 'audio', name: uid.split('/').at(-1), nameSource: 'path',
    kind, subkind, aliases: [], tags: [], biome: [], style: 'neutral', status: 'unscored',
    quality: { level: 'unscored' }, licence, provenance: {}, usedBy: [], copies: [], files: [file], warnings: [], ...extra };
}
function summarize(c) {
  c.files.sort((a, b) => cmp(a.path, b.path));
  const variants = c.files.filter(f => f.role !== 'copy');
  const common = key => variants.every(f => f.audio?.[key] === variants[0]?.audio?.[key]) ? variants[0]?.audio?.[key] ?? null : null;
  c.audio = { variants: variants.length, durationMs: variants.map(f => f.audio?.durationMs ?? null),
    sampleRate: common('sampleRate'), channels: common('channels'), codec: common('codec'), loop: c.audio?.loop ?? false };
  if (c.status !== 'draft' && c.usedBy.length) {
    c.status = 'shipped';
    if (c.licence.id !== 'unknown' && !c.licence.private) c.quality = { level: 'pass', rule: 'Đã dùng trong mã; giấy phép giữ theo nguồn.' };
  }
  c.usedBy.sort((a, b) => cmp(a.ref, b.ref) || cmp(a.copyPath, b.copyPath));
}

/** Chỉ đọc nguồn. Dùng index AudioLab, không mở/băm lại media thư viện ngoài. */
export async function scanAudio({ repoRoot = REPO_ROOT, audioLabRoot = path.join(os.homedir(), 'AudioLab'),
  io = fs, headerFs = nodeFs, all = false, game, locksOnly = false } = {}) {
  if (game !== undefined && !GAMES.includes(game)) throw new Error('Game không được phép');
  repoRoot = path.resolve(repoRoot);
  audioLabRoot = path.resolve(audioLabRoot);
  const warnings = [], cards = [], byHash = new Map(), spaceFiles = [], duplicates = [];
  const stats = { externalFiles: 0, externalMediaReads: 0, spaceFiles: 0, kenneyCopies: 0,
    dotaFiles: 0, privateMusic: 0, workRuns: 0, workCards: 0, hiddenWorkCards: 0, sourceFiles: 0 };
  let sources = {};
  sources = await json(repoRoot, 'library/sources.json');
  const taxonomy = await json(repoRoot, 'library/taxonomy.json');
  const licences = await json(repoRoot, 'library/licences.json');
  function allowed(rel) {
    return valid(rel) && ![...(sources.deny ?? []), ...(sources.ignore ?? [])].some(glob => path.matchesGlob(rel, glob));
  }
  async function info(base, rel) {
    if (!allowed(rel)) return null;
    let p = path.parse(base).root, stat;
    // Kiểm cả gốc cấu hình để không đi theo liên kết ở tổ tiên.
    for (const part of path.resolve(base).split(path.sep).filter(Boolean)) {
      p = path.join(p, part);
      stat = await io.lstat(p);
      if (stat.isSymbolicLink()) return null;
    }
    p = base;
    for (const part of rel.split('/')) {
      p = path.join(p, part); stat = await io.lstat(p);
      if (stat.isSymbolicLink()) return null;
    }
    return stat;
  }
  async function text(base, rel, warn = false) {
    try { return (await info(base, rel))?.isFile() ? await io.readFile(path.join(base, rel), 'utf8') : null; }
    catch (e) { if (!missing(e)) throw e; if (warn) warnings.push(`${base === repoRoot ? rel : '~/AudioLab/' + rel}: ${e.code} — bỏ qua nguồn không đọc được`); return null; }
  }
  async function json(base, rel, warn = false) {
    const value = await text(base, rel, warn);
    if (!value) return {};
    try { return JSON.parse(value); } catch { warnings.push(`${rel}: JSON không hợp lệ`); return {}; }
  }
  async function walk(base, rel, visit) {
    if (!allowed(rel)) return;
    try {
      const stat = await info(base, rel);
      if (stat?.isDirectory()) {
        for (const name of (await io.readdir(path.join(base, rel))).sort(cmp)) await walk(base, `${rel}/${name}`, visit);
      } else if (stat?.isFile()) await visit(rel, stat);
    } catch (e) { if (!missing(e)) throw e; warnings.push(`${base === repoRoot ? rel : '~/AudioLab/' + rel}: ${e.code} — bỏ qua`); }
  }
  function licence(id, ledger) {
    const result = { id: id?.toLowerCase() ?? 'unknown', ...(licences[id?.toLowerCase()] ?? licences.unknown ?? { commercialOk: false, aiInputAllowed: false, notForRelease: true, private: false }) };
    if (ledger) {
      result.ledger = '~/AudioLab/libraries/SOURCES.jsonl';
      if (ledger.commercial_ok !== undefined) result.commercialOk = ledger.commercial_ok;
      if (ledger.ai_input_allowed !== undefined) result.aiInputAllowed = ledger.ai_input_allowed;
      if (ledger.attribution_required) result.attribution = ledger.attribution_text || `${ledger.author} — ${ledger.page || ledger.url}`;
    }
    return result;
  }
  function family(value) {
    const [head, ...tail] = (value || 'audio').split('/');
    return [taxonomy.audioFamilyMap?.[head] ?? head, ...tail].join('/');
  }
  function register(c, f) {
    if (!f.sha256) return;
    if (!byHash.has(f.sha256)) byHash.set(f.sha256, { card: c, file: f });
  }
  // Giữ nguyên dòng SOURCES trong provenance; chỉ đọc hồ sơ nguồn.
  const index = await json(audioLabRoot, 'libraries/index.json', true);
  const ledger = [];
  for (const line of (await text(audioLabRoot, 'libraries/SOURCES.jsonl', true) ?? '').split(/\r?\n/u).filter(Boolean)) {
    try { const row = JSON.parse(line); if (clean(row) && valid(row.path)) ledger.push(row); }
    catch { warnings.push('libraries/SOURCES.jsonl: dòng JSON không hợp lệ'); }
  }
  const externalCards = new Map();
  for (const row of index.files ?? []) {
    if (!allowed(row.file) || !AUDIO.test(row.file) || !clean(row) || !/^[a-f\d]{64}$/iu.test(row.sha256 ?? '')) continue;
    const parts = row.file.split('/'), origin = parts.shift();
    const uid = `${origin}:${familyStem(parts.join('/'))}`;
    const source = ledger.filter(l => row.file.startsWith(l.path + '/')).sort((a, b) => b.path.length - a.path.length)[0];
    const codec = ({ VORBIS: 'vorbis', OPUS: 'opus', PCM_16: 'pcm_s16le', PCM_24: 'pcm_s24le', FLOAT: 'pcm_f32le' })[row.subtype] ?? row.format?.toLowerCase() ?? null;
    const f = { path: `~/AudioLab/libraries/${row.file}`, role: 'variant', variant: variantOf(row.file),
      sha256: row.sha256.toLowerCase(), bytes: row.bytes, onDrive: 'external',
      audio: { durationMs: Math.round(row.duration * 1000), sampleRate: row.sample_rate, channels: row.channels, codec } };
    let c = externalCards.get(uid);
    if (!c) {
      c = card(uid, origin, family(row.family), f, licence(source?.licence ?? row.licence, source),
        { tags: row.tags ?? [], aliases: [row.key, row.family].filter(Boolean), provenance: { licenceRow: source ?? null }, sourceRows: [] });
      cards.push(c); externalCards.set(uid, c);
    } else c.files.push(f);
    c.sourceRows.push(row);
    register(c, f); stats.externalFiles++;
  }
  const attr = parseAttribution(await text(repoRoot, 'games/space-typing/public/assets/audio/ATTRIBUTION.md') ?? '');
  const privateRows = new Map();
  for (const line of (await text(repoRoot, 'media/private.md5', true) ?? '').split(/\r?\n/u)) {
    const m = line.match(/^([a-f\d]{32}) [ *](.+)$/iu);
    if (m && allowed(m[2])) privateRows.set(m[2], m[1].toLowerCase());
  }
  const spaceLock = new Map();
  for (const line of (await text(repoRoot, 'games/space-typing/media.md5') ?? '').split(/\r?\n/u)) {
    const m = line.match(/^([a-f\d]{32}) [ *](.+)$/iu);
    if (m && valid(m[2])) spaceLock.set('games/space-typing/' + m[2], m[1]);
  }
  const gameCards = new Map();
  async function addSpace(p, stat, frozenHash) {
    let f;
    if (locksOnly) f = { path: p, role: 'variant', variant: variantOf(p), sha256: frozenHash ?? null, md5: spaceLock.get(p) ?? null, bytes: null, local: false, onDrive: spaceLock.has(p) ? 'yes' : 'no' };
    else {
      const data = await io.readFile(path.join(repoRoot, p));
      f = { path: p, role: 'variant', variant: variantOf(p), sha256: createHash('sha256').update(data).digest('hex'),
        md5: createHash('md5').update(data).digest('hex'), bytes: stat.size, local: true };
      f.onDrive = privateRows.has(p) ? 'private' : spaceLock.has(p) ? spaceLock.get(p) === f.md5 ? 'yes' : 'changed' : 'no';
      try { f.audio = audioHeader(data); } catch (e) { warnings.push(`${p}: ${e.message}`); }
    }
    const rel = p.slice('games/space-typing/'.length);
    const attribution = attr.get(rel);
    if (attribution) f.sourceRow = attribution;
    const isPrivate = privateRows.has(p);
    const match = isPrivate ? null : byHash.get(f.sha256);
    if (match) {
      const c = match.card;
      f.role = 'copy'; f.variant = match.file.variant; f.copyOf = match.file.path;
      c.files.push(f); c.copies.push({ ...f, location: 'game' });
      if (c.origin === 'kenney') stats.kenneyCopies++;
    } else {
      const uid = `space-typing:${familyStem(rel)}`;
      let c = gameCards.get(uid);
      if (!c) {
        let sourceLicence = 'unknown';
        if (attribution || rel.includes('/sfx/kenney/')) sourceLicence = 'cc0-1.0';
        else if (/\/music\/songs\//u.test(rel)) sourceLicence = 'repo-synth';
        else if (/\/(?:music\/(?:sector|pulse|urgent)|stingers\/victory)\.ogg$/u.test(rel)) sourceLicence = 'cc0-1.0';
        const audioKind = /\/music\//u.test(rel) ? 'music' : /\/ui\//u.test(rel) ? 'ui' : /\/ambient\//u.test(rel) ? 'ambience' : 'audio';
        c = card(uid, 'space-typing', audioKind, f, licence(isPrivate ? 'private-producer' : sourceLicence), { provenance: attribution ?? {} });
        if (!attribution && sourceLicence === 'unknown') c.warnings.push('Chưa có nguồn từng file trong ATTRIBUTION.md.');
        cards.push(c); gameCards.set(uid, c);
      } else c.files.push(f);
      register(c, f);
    }
    spaceFiles.push(f); stats.spaceFiles++;
  }
  if (!game || game === 'space-typing') {
    if (locksOnly) {
      const legacy = (await json(repoRoot, 'tools/audio-lab/build/legacy-audio.json'))['space-typing']?.files ?? {};
      const paths = new Set([...Object.keys(legacy).map(p => 'games/space-typing/' + p), ...spaceLock.keys()]);
      for (const p of [...paths].sort(cmp)) if (allowed(p) && AUDIO.test(p) && /\/(?:public\/assets|src\/assets)\/audio\//u.test(p)) await addSpace(p, null, legacy[p.slice(19)]);
    } else for (const dir of ['public/assets/audio', 'src/assets/audio']) {
      await walk(repoRoot, 'games/space-typing/' + dir, async (p, stat) => { if (AUDIO.test(p)) await addSpace(p, stat); });
    }
    // Dota: luôn riêng tư kể cả khi private.md5 chưa hiện diện trên máy mới.
    const dota = 'games/space-typing/art-src/Dota-Sounds';
    const addPrivate = async (p, stat, music) => {
      const f = { path: p, role: 'variant', variant: null, md5: privateRows.get(p) ?? null,
        bytes: stat?.size ?? null, local: !!stat, onDrive: 'private' };
      if (stat) try { f.audio = audioHeader(path.join(repoRoot, p), { fs: headerFs }); } catch (e) { warnings.push(`${p}: ${e.message}`); }
      const uid = music ? 'music:' + stem(p.slice('shared/music/'.length)) : 'space-typing:' + stem(p.slice(19));
      cards.push(card(uid, music ? 'private-music' : 'space-typing', music ? 'music' : 'audio', f,
        licence(music ? 'private-producer' : 'private-valve'), { private: true, notForRelease: true }));
      stats[music ? 'privateMusic' : 'dotaFiles']++;
    };
    if (locksOnly) {
      for (const p of privateRows.keys()) if (AUDIO.test(p) && (p.startsWith(dota + '/') || p.startsWith('shared/music/'))) await addPrivate(p, null, p.startsWith('shared/music/'));
    } else {
      await walk(repoRoot, dota, async (p, stat) => { if (AUDIO.test(p)) await addPrivate(p, stat, false); });
      for (const p of privateRows.keys()) if (p.startsWith('shared/music/') && AUDIO.test(p)) {
        let stat;
        try { stat = await info(repoRoot, p); } catch (e) { if (!missing(e)) throw e; warnings.push(`${p}: ${e.code} — chỉ có trong lock riêng tư`); }
        await addPrivate(p, stat, true);
      }
    }
  }
  const hashes = new Map();
  for (const f of spaceFiles) if (f.sha256) { if (!hashes.has(f.sha256)) hashes.set(f.sha256, []); hashes.get(f.sha256).push(f.path); }
  for (const [sha256, paths] of hashes) if (paths.length > 1) duplicates.push({ sha256, paths: paths.sort(cmp) });
  // Chỉ lượt có cả hai hồ sơ mới tạo thẻ nháp, không quét mọi master rời rạc.
  const manifests = [];
  if (!locksOnly) await walk(audioLabRoot, 'work', async p => { if (p.endsWith('/manifest.fragment.json')) manifests.push(p); });
  for (const manifest of manifests) {
    const run = path.posix.dirname(manifest), sourcePath = run + '/SOURCES.json';
    const sourceText = await text(audioLabRoot, sourcePath);
    if (!sourceText) continue;
    let source;
    try { source = JSON.parse(sourceText); } catch { warnings.push(`${sourcePath}: JSON không hợp lệ`); continue; }
    const fragment = await json(audioLabRoot, manifest);
    stats.workRuns++;
    for (const [id, sound] of Object.entries(fragment.sounds ?? {})) {
      if (DENY.test(id) || !Array.isArray(sound.files)) continue;
      let c;
      for (const [i, file] of sound.files.entries()) {
        if (!valid(file) || !AUDIO.test(file)) continue;
        const sourceRow = source[file];
        if (!sourceRow || !clean(sourceRow) || (game && sourceRow.game !== game)) continue;
        const p = `${run}/${file}`;
        let stat;
        try { stat = await info(audioLabRoot, p); } catch (e) { if (!missing(e)) throw e; }
        const f = { path: `~/AudioLab/${p}`, role: 'variant', variant: variantOf(file), local: !!stat,
          bytes: stat?.size ?? null, sha256: sourceRow.sha256 ?? null, onDrive: 'external', sourceRow,
          audio: { durationMs: sourceRow.durationMs ?? sound.durationMs?.[i] ?? null,
            sampleRate: sourceRow.sampleRate ?? null, channels: sourceRow.channels ?? null, codec: sourceRow.codec ?? null } };
        if (stat) try { f.audio = audioHeader(path.join(audioLabRoot, p), { fs: headerFs }); } catch (e) { warnings.push(`~/AudioLab/${p}: ${e.message}`); }
        if (!c) {
          c = card(`audiolab:${run}/${id}`, 'audiolab', family(sourceRow.family ?? sound.family ?? 'audio'), f, licence('unknown'),
            { status: 'draft', hidden: true, aliases: [sourceRow.family, sound.family].filter(Boolean), audio: { loop: sound.loop ?? false }, provenance: { manifest: `~/AudioLab/${manifest}`, sources: `~/AudioLab/${sourcePath}` } });
          cards.push(c); stats.workCards++;
        } else c.files.push(f);
      }
    }
  }
  await collectUsage();
  for (const c of cards) summarize(c);
  stats.hiddenWorkCards = all ? 0 : stats.workCards;
  return { cards: cards.filter(c => all || c.status !== 'draft').sort((a, b) => cmp(a.uid, b.uid)), stats,
    duplicates: duplicates.sort((a, b) => cmp(a.paths[0], b.paths[0])), warnings: [...new Set(warnings)].sort(cmp) };

  async function collectUsage() {
    const byPath = new Map(cards.flatMap(c => c.files.filter(f => !f.path.startsWith('~/')).map(f => [f.path, { c, f }])));
    function use(p, code, line, confidence, glob) {
      const entry = byPath.get(p);
      if (!entry) return;
      const row = { game: code.split('/')[1], ref: `${code}:${line}`, copyPath: p, variant: entry.f.variant, shipped: true, confidence, ...(glob ? { glob } : {}) };
      if (!entry.c.usedBy.some(r => r.ref === row.ref && r.copyPath === p && r.confidence === confidence)) entry.c.usedBy.push(row);
    }
    for (const id of GAMES.filter(id => !game || game === id)) await walk(repoRoot, `games/${id}/src`, async code => {
      if (!/\.(?:[cm]?[jt]sx?|vue|svelte)$/u.test(code)) return;
      const raw = await text(repoRoot, code);
      if (raw === null) return;
      stats.sourceFiles++;
      // Bỏ bình luận nhưng giữ vị trí xuống dòng và các chuỗi nguyên vẹn.
      const source = raw.replace(/(["'`])(?:\\[\s\S]|(?!\1)[^\\])*?\1|\/\*[\s\S]*?\*\/|\/\/[^\n]*/gu,
        token => token.startsWith('/') ? token.replace(/[^\n]/gu, ' ') : token);
      const strings = [...source.matchAll(/(["'`])((?:\\.|(?!\1)[^\\])*?)\1/gu)].map(m => ({ value: m[2], index: m.index, line: source.slice(0, m.index).split('\n').length }));
      const globs = [];
      for (const str of strings) {
        const before = source.slice(Math.max(0, str.index - 160), str.index);
        if (!/import\.meta\.glob(?:<[^;\n]+?>)?\(\s*(?:\[\s*)?$/u.test(before)) continue;
        const pattern = path.posix.normalize(path.posix.join(path.posix.dirname(code), str.value));
        if (!allowed(pattern)) continue;
        globs.push({ pattern, ...str });
        for (const p of byPath.keys()) if (path.matchesGlob(p, pattern)) use(p, code, str.line, 'folder', str.value);
      }
      for (const str of strings) {
        if (str.value.includes('*')) continue;
        let p;
        const value = str.value.split(/[?#]/u)[0];
        if (value.startsWith('.')) p = path.posix.normalize(path.posix.join(path.posix.dirname(code), value));
        else if (value.startsWith('/assets/')) p = `games/${id}/public${value}`;
        if (p && allowed(p)) use(p, code, str.line, 'path');
        if (AUDIO.test(value) && !value.startsWith('/') && value.includes('/') && valid(value)) {
          for (const target of byPath.keys()) if (target.startsWith(`games/${id}/`) && target.endsWith('/' + value)) use(target, code, str.line, 'path');
        }
        // uiFile tra tên ngắn trong glob UI của chính module này.
        if (/\buiFile\(\s*$/u.test(source.slice(Math.max(0, str.index - 25), str.index))) {
          for (const glob of globs) for (const target of byPath.keys()) {
            if (stem(path.posix.basename(target)) === value && path.matchesGlob(target, glob.pattern)) use(target, code, str.line, 'path');
          }
        }
      }
    });
  }
}

/** CLI autonome AL-08: exactement deux écritures, toutes deux sous library/out. */
export async function main(args = process.argv.slice(2), options = {}) {
  const parsed = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--all') parsed.all = true;
    else if (args[i] === '--locks-only') parsed.locksOnly = true;
    else if (args[i] === '--game' && args[i + 1]) parsed.game = args[++i];
    else throw new Error(`Cờ không hợp lệ: ${args[i]}`);
  }
  const result = await scanAudio({ ...options, ...parsed });
  const io = options.io ?? fs, root = path.resolve(options.repoRoot ?? REPO_ROOT);
  const out = path.join(root, 'library/out');
  // Chặn output có symlink trước mọi lần ghi, không đi theo đích liên kết.
  let current = path.parse(out).root;
  for (const part of out.split(path.sep).filter(Boolean)) {
    current = path.join(current, part);
    try { if ((await io.lstat(current)).isSymbolicLink()) throw new Error('Đường output có symlink'); }
    catch (e) { if (e.code !== 'ENOENT') throw e; }
  }
  try { if ((await io.lstat(path.join(out, 'audio-catalog.json'))).isSymbolicLink()) throw new Error('File output có symlink'); }
  catch (e) { if (e.code !== 'ENOENT') throw e; }
  await io.mkdir(out, { recursive: true });
  await io.writeFile(path.join(out, 'audio-catalog.json'), JSON.stringify({ schema: 'asset-library-audio/1', ...result }, null, 2) + '\n');
  console.log(JSON.stringify({ cards: result.cards.length, ...result.stats, duplicateGroups: result.duplicates.length, warnings: result.warnings.length }));
  return result;
}
if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(e => { console.error(e.message); process.exitCode = 1; });
}
