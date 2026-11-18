import { readFile, readdir, realpath, stat, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { inspectGlb } from '../map-factory/registry/scan-assets.mjs';

const execFileAsync = promisify(execFile);
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const md5 = bytes => createHash('md5').update(bytes).digest('hex');
export const CONFIG = Object.freeze({
  minimumFaces: 3000, faceLow: 0.55, faceHigh: 1.02, faceTarget: 0.95,
  faceReward: 35, faceSlope: 35, facePenalty: 45,
  shapeWeight: 25, shapeScale: 0.4, nameWeight: 60,
});

// General vocabulary only; never associate a Tripo filename with a model id.
export const SYNONYMS = [
  ['wolf', 'soi'], ['bridge', 'cau'], ['bamboo', 'tre'], ['feather', 'long'],
  ['scaffold', 'gian'], ['axe', 'riu'], ['hat', 'helmet', 'mu', 'non'],
  ['cliff', 'vach'], ['waterfall', 'thac'], ['wood', 'wooden', 'go'],
  ['rock', 'rocks', 'rocky', 'stone', 'stones', 'da'], ['moss', 'mossy', 'reu'],
  ['bush', 'shrub', 'bui'], ['blossom', 'flower', 'flowering', 'hoa'],
  ['pine', 'evergreen', 'thong'], ['tree', 'cay'], ['pig', 'piggy', 'heo'],
  ['buffalo', 'trau'], ['bird', 'chim'], ['insect', 'bug'], ['wasp', 'ong'],
  ['ant', 'kien'], ['hut', 'cottage', 'house', 'nha', 'leu'],
  ['spike', 'spikes', 'chong'], ['club', 'chuy', 'gay'], ['hammer', 'mallet', 'bua'],
  ['shield', 'khien'], ['bow', 'crossbow', 'cung', 'no'], ['arrow', 'arrows', 'ten'],
  ['hair', 'hairstyle', 'toc'], ['bandana', 'headband', 'khan'],
  ['mustache', 'moustache', 'ria'], ['book', 'sach'], ['fan', 'quat'],
  ['goggles', 'kinh'], ['pickaxe', 'cuoc'], ['basket', 'gio'],
  ['leaf', 'leafy', 'la'], ['water', 'nuoc'], ['gold', 'golden', 'yellow', 'vang'],
  ['purple', 'violet', 'tim'], ['blue', 'xanh'], ['red', 'do'],
  ['white', 'trang'], ['black', 'den'], ['brown', 'nau'],
];
const ALIASES = new Map(SYNONYMS.flatMap(group => group.map(word => [word, group[0]])));
const STOP = new Set(['3d', 'model', 'glb', 'png', 'alpha', 'flat', 'front', 'back', 'left',
  'stylized', 'fantasy', 'cartoon', 'with', 'the', 'of', 'a', 'an', 'cua', 'va', 'o']);

export function unaccent(text) {
  return text.toLowerCase().normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd');
}

export function tokenize(text) {
  const words = unaccent(text).replace(/\bbang[\s-]+do\b/g, 'bandana')
    .replace(/\bpinecone\b/g, 'pine cone');
  return [...new Set(words.split(/[^a-z0-9]+/).filter(word =>
    word && !STOP.has(word) && !/^\d+$/.test(word)).map(word => ALIASES.get(word) ?? word))];
}

export function scoreFace(triangles, faceLimit, config = CONFIG) {
  if (!(triangles > 0) || !(faceLimit > 0)) throw new Error('Tam giác và face phải dương');
  const effectiveLimit = Math.max(faceLimit, config.minimumFaces);
  const ratio = triangles / effectiveLimit;
  const inBand = ratio >= config.faceLow && ratio <= config.faceHigh;
  const distance = Math.abs(Math.log(ratio / config.faceTarget));
  return { score: (inBand ? config.faceReward : -config.facePenalty) - config.faceSlope * distance,
    ratio, rawRatio: triangles / faceLimit, effectiveLimit, inBand };
}

export function scoreShape(glbRatio, imageRatio, config = CONFIG) {
  if (!(glbRatio > 0) || !(imageRatio > 0) || !Number.isFinite(glbRatio) || !Number.isFinite(imageRatio)) {
    return { score: 0, logRatio: null, missing: true };
  }
  const logRatio = Math.log(glbRatio / imageRatio);
  return { score: config.shapeWeight * Math.exp(-Math.abs(logRatio) / config.shapeScale), logRatio, missing: false };
}

export function scoreName(filename, description, config = CONFIG) {
  const query = tokenize(filename.replace(/\.glb$/i, ''));
  const words = new Set(tokenize(description));
  const matched = query.filter(word => words.has(word));
  // Material alone is weak evidence; a named object is stronger.
  const weight = word => word === 'wood' ? 0.3 : 1;
  const totalWeight = query.reduce((sum, word) => sum + weight(word), 0);
  return { score: totalWeight ? config.nameWeight * matched.reduce((sum, word) => sum + weight(word), 0) / totalWeight : 0,
    query, matched };
}

export function parseImageName(filename) {
  const match = /^([a-z0-9]+)_(.+?)(?:_(front|back|left))?(?:\.(alpha|flat))?\.png$/i.exec(filename);
  return match ? { id: `${match[1]}_${match[2]}`, game: match[1], view: match[3]?.toLowerCase() ?? 'single', variant: match[4] ?? null } : null;
}

export function parseIndex(markdown) {
  const result = new Map();
  for (const line of markdown.split(/\r?\n/)) {
    const bullet = /^\s*-\s+`([a-z0-9]+_[^`]+)`\s*:\s*(.+)/i.exec(line);
    if (bullet) result.set(bullet[1], bullet[2].split(/\s*·\s*(?:Lời Gọi|Rồng Giữ Ải|Tuyến Cuối)/)[0]);
    if (line.startsWith('|')) {
      const cells = line.split('|').slice(1, -1).map(cell => cell.trim());
      const basename = cells[0]?.replace(/`/g, '').split('/').at(-1)?.replace(/_\*\.png$/, '_front.png');
      const parsed = basename && parseImageName(basename);
      if (parsed) result.set(parsed.id, cells[1] ?? '');
    }
  }
  return result;
}

export function parseEnglishNames(markdown) {
  const result = new Map();
  let game;
  for (const line of markdown.split(/\r?\n/)) {
    if (line.startsWith('## ')) game = line.includes('games/dragon-hold') ? 'rong'
      : line.includes('games/typing-defense') ? 'loigoi' : line.includes('games/typing-survival') ? 'tuyencuoi' : null;
    if (!game || !line.startsWith('|')) continue;
    const cells = line.split('|').slice(1, -1).map(cell => cell.trim());
    const id = /^`([a-z0-9-]+)`$/.exec(cells[0] ?? '')?.[1];
    if (id && cells[2] && cells[2] !== '—') result.set(`${game}_${id}`, cells[2]);
  }
  return result;
}

export function rankCandidates(glb, candidates, config = CONFIG) {
  return candidates.map(candidate => {
    const face = scoreFace(glb.triangles, candidate.faceLimit, config);
    const shape = scoreShape(glb.ratio, candidate.ratio, config);
    const name = scoreName(glb.file, [candidate.id.split('_').slice(1).join('_'), candidate.englishName, candidate.label].filter(Boolean).join(' '), config);
    return { id: candidate.id, image: candidate.image, score: face.score + shape.score + name.score, face, shape, name };
  }).sort((a, b) => b.score - a.score || cmp(a.id, b.id));
}

// Highest remaining pair first; preserve the original rankings and all their scores.
export function greedyMatch(rows) {
  const edges = rows.flatMap((row, index) => row.ranking.map(candidate => ({ index, file: row.file, candidate })));
  edges.sort((a, b) => b.candidate.score - a.candidate.score || cmp(a.file, b.file) || cmp(a.candidate.id, b.candidate.id) || a.index - b.index);
  const used = new Set(), assigned = new Set(), result = rows.map(() => null);
  for (const { index, candidate } of edges) {
    if (assigned.has(index) || used.has(candidate.id)) continue;
    result[index] = candidate;
    assigned.add(index); used.add(candidate.id);
  }
  return result;
}

async function entries(directory, missingOK = false) {
  try { return (await readdir(directory, { withFileTypes: true })).sort((a, b) => cmp(a.name, b.name)); }
  catch (error) { if (missingOK && error.code === 'ENOENT') return []; throw error; }
}

async function glbFiles(directory) {
  const files = [];
  for (const entry of await entries(directory, true)) {
    const target = path.join(directory, entry.name);
    // Do not follow directory symlinks outside the requested tree.
    if (entry.isDirectory()) files.push(...await glbFiles(target));
    else if (entry.isFile() && /\.glb$/i.test(entry.name)) files.push(target);
  }
  return files;
}

export async function imageSize(file) {
  const { stdout } = await execFileAsync('/opt/homebrew/bin/magick',
    [file, '-fuzz', '15%', '-trim', '-format', '%w %h', 'info:'], { timeout: 30000, maxBuffer: 65536 });
  const values = stdout.trim().split(/\s+/).map(Number);
  if (values.length !== 2 || !values.every(v => Number.isFinite(v) && v > 0)) throw new Error(`Cỡ ảnh không hợp lệ: ${file}`);
  return { width: values[0], height: values[1], ratio: values[0] / values[1] };
}

export async function runMatch({ upload, glb }, { measureImage = imageSize } = {}) {
  upload = path.resolve(upload);
  const uploadEntries = await entries(upload);
  if (!glb) {
    // macOS may store the directory name in decomposed Unicode (NFD).
    const names = uploadEntries.filter(e => e.isDirectory() && e.name.normalize('NFC') === '_GLB tải về');
    if (names.length > 1) throw new Error('Nhiều thư mục GLB trùng tên sau chuẩn hóa Unicode');
    glb = path.join(upload, names[0]?.name ?? '_GLB tải về');
  }
  glb = path.resolve(glb);
  const labels = parseIndex(await readFile(path.join(upload, 'INDEX.md'), 'utf8'));
  let englishNames = new Map();
  const warnings = [];
  try { englishNames = parseEnglishNames(await readFile(path.join(ROOT, 'docs/games/NAMES_EN.md'), 'utf8')); }
  catch (error) { if (error.code !== 'ENOENT') throw error; warnings.push('Không có NAMES_EN.md; chỉ dùng id và INDEX.md'); }
  const groups = new Map();
  for (const folder of uploadEntries) {
    const faceLimit = /^face\s+(\d+)\s*-/i.exec(folder.name)?.[1];
    if (!folder.isDirectory() || !faceLimit) continue;
    for (const entry of await entries(path.join(upload, folder.name))) {
      const parsed = entry.isFile() && parseImageName(entry.name);
      if (!parsed) continue;
      const key = parsed.id;
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push({ ...parsed, faceLimit: Number(faceLimit), file: path.join(upload, folder.name, entry.name) });
    }
  }
  const files = await glbFiles(glb);
  const candidates = [], rows = [], hashes = new Map();
  // Snapshot every source view, even though only one front/single view is measured.
  const allMedia = [...groups.values()].flat().map(i => i.file).concat(files).sort(cmp);
  for (const file of allMedia) hashes.set(file, md5(await readFile(file)));
  try {
    for (const [id, images] of [...groups].sort(([a], [b]) => cmp(a, b))) {
      const priorities = { front: 0, single: 1, left: 2, back: 3 };
      images.sort((a, b) => priorities[a.view] - priorities[b.view] || cmp(a.file, b.file));
      const source = images[0];
      if (new Set(images.map(i => i.faceLimit)).size > 1) throw new Error(`Model ${id} có nhiều face limit`);
      let size = { width: null, height: null, ratio: null };
      // No ImageMagick needed when there are no GLBs to rank.
      if (files.length) {
        try { size = await measureImage(source.file); }
        catch (error) { warnings.push(`${id}: không đo được ảnh: ${error.message}`); }
      }
      candidates.push({ id, faceLimit: source.faceLimit, label: labels.get(id) ?? '', englishName: englishNames.get(id) ?? '',
        image: path.relative(upload, source.file), images: images.map(i => path.relative(upload, i.file)), ...size });
    }
    for (const file of files) {
      try {
        const data = await readFile(file);
        if (md5(data) !== hashes.get(file)) throw new Error('MD5 thay đổi trước khi đọc GLB');
        const info = inspectGlb(data);
        const ratio = info.bounds?.size[1] > 0 ? Math.max(info.bounds.size[0], info.bounds.size[2]) / info.bounds.size[1] : null;
        const row = { file: path.relative(glb, file), triangles: info.triangles, bounds: info.bounds, ratio,
          warnings: [...info.warnings, ...info.needsDecompression], error: null };
        row.ranking = rankCandidates(row, candidates);
        rows.push(row);
      } catch (error) {
        rows.push({ file: path.relative(glb, file), triangles: null, ratio: null, error: error.message, ranking: [] });
      }
    }
  } finally {
    const changed = [];
    for (const [file, before] of hashes) {
      try { if (md5(await readFile(file)) !== before) changed.push(file); }
      catch { changed.push(file); }
    }
    if (changed.length) throw new Error(`MD5 media thay đổi: ${changed.join(', ')}`);
  }
  const assigned = greedyMatch(rows);
  return { schemaVersion: 1, upload, glb, config: CONFIG, candidates,
    rows: rows.map(({ ranking, ...row }, i) => ({ ...row, top3: ranking.slice(0, 3), assigned: assigned[i] })),
    warnings, mediaIntegrity: { algorithm: 'md5', filesChecked: hashes.size, changed: [],
      files: [...hashes].map(([file, hash]) => ({ file, before: hash, after: hash })) } };
}

export function parseAnswers(markdown) {
  return markdown.split(/\r?\n/).filter(line => line.startsWith('|')).flatMap(line => {
    const cells = line.split('|').slice(1, -1).map(cell => cell.trim().replace(/`/g, ''));
    return /\.glb$/i.test(cells[3] ?? '') && /^[a-z0-9]+_/.test(cells[1] ?? '')
      ? [{ file: cells[3], id: cells[1], triangles: Number(cells[4]) }] : [];
  });
}

// Evaluation is separate from scoring: answers can never influence suggestions.
export function evaluate(result, answers) {
  const expected = new Map(answers.map(a => [a.file, a]));
  const details = result.rows.filter(row => expected.has(row.file)).map(row => {
    const answer = expected.get(row.file);
    return { file: row.file, expected: answer.id, top1: row.top3[0]?.id ?? null,
      top3: row.top3.map(c => c.id), assigned: row.assigned?.id ?? null,
      top1Correct: row.top3[0]?.id === answer.id, top3Correct: row.top3.some(c => c.id === answer.id),
      assignedCorrect: row.assigned?.id === answer.id, trianglesMatch: row.triangles === answer.triangles };
  });
  const count = key => details.filter(row => row[key]).length;
  return { total: details.length, top1: count('top1Correct'), top3: count('top3Correct'), assigned: count('assignedCorrect'),
    missingFiles: answers.filter(a => !result.rows.some(row => row.file === a.file)).map(a => a.file),
    unlabelledFiles: result.rows.filter(row => !expected.has(row.file)).map(row => row.file), details };
}

const cell = value => String(value).replace(/\|/g, '\\|').replace(/[\r\n]/g, ' ');
const number = value => Number.isFinite(value) ? value.toFixed(2) : '—';
const describe = c => c ? `${cell(c.id)}: ${number(c.score)} (face ${number(c.face.score)}; hình ${number(c.shape.score)}; chữ ${number(c.name.score)})` : '—';
export function markdown(result) {
  const lines = [`${result.rows.length} GLB · ${result.candidates.length} model ứng viên`, '',
    '| File GLB | Tam giác | Rộng : cao | Ứng viên 1 | Ứng viên 2 | Ứng viên 3 | Ghép một-một |',
    '|---|---:|---:|---|---|---|---|'];
  for (const row of result.rows) lines.push(`| ${cell(row.file)} | ${row.triangles ?? '—'} | ${number(row.ratio)} | ${describe(row.top3[0])} | ${describe(row.top3[1])} | ${describe(row.top3[2])} | ${describe(row.assigned)}${row.error ? `; LỖI: ${cell(row.error)}` : ''} |`);
  lines.push('', `MD5: ${result.mediaIntegrity.filesChecked} file không đổi. Điểm là gợi ý, cần duyệt bằng mắt.`);
  for (const warning of result.warnings) lines.push(`- ${cell(warning)}`);
  for (const row of result.rows) for (const warning of row.warnings ?? []) lines.push(`- ${cell(row.file)}: ${cell(warning)}`);
  return lines.join('\n');
}

export function parseOptions(args) {
  const result = {};
  for (let i = 0; i < args.length; i++) {
    if (!['--upload', '--glb', '--out'].includes(args[i]) || !args[i + 1] || args[i + 1].startsWith('--')) throw new Error('Cú pháp: --upload <thư mục> [--glb <thư mục>] [--out <file.json>]');
    const key = args[i].slice(2);
    if (result[key]) throw new Error(`Cờ lặp: ${args[i]}`);
    result[key] = args[++i];
  }
  if (!result.upload) throw new Error('Thiếu --upload');
  return result;
}

export async function validateOutput(out, upload, glb) {
  const target = path.resolve(out);
  if (!/\.json$/i.test(target)) throw new Error('--out phải là file .json mới');
  // Resolve parents before checking containment, including symlink aliases.
  const resolved = path.join(await realpath(path.dirname(target)), path.basename(target));
  const within = (file, directory) => file === directory || file.startsWith(directory + path.sep);
  for (const directory of [upload, glb, path.join(ROOT, 'games'), path.join(ROOT, 'typing-game-handoff-2026-10-25')].filter(Boolean)) {
    let root;
    try { root = await realpath(directory); }
    catch (error) { if (error.code !== 'ENOENT') throw error; root = path.resolve(directory); }
    if (within(resolved, root)) throw new Error('Không ghi JSON trong cây media/games/upload/GLB');
  }
  try { await stat(target); throw new Error('--out đã tồn tại; không ghi đè'); }
  catch (error) { if (error.code !== 'ENOENT') throw error; }
  return resolved;
}

export async function main(args = process.argv.slice(2)) {
  const options = parseOptions(args);
  const out = options.out ? await validateOutput(options.out, options.upload, options.glb) : null;
  const result = await runMatch(options);
  if (out) await writeFile(out, JSON.stringify(result, null, 2) + '\n', { flag: 'wx' });
  console.log(markdown(result));
  if (result.rows.some(row => row.error)) process.exitCode = 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
