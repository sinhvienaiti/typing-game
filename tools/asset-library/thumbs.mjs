import * as fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createHash } from 'node:crypto';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { REPO_ROOT, main, safeInfo } from './find.mjs';

export const MIN_FREE = 20 * 1024 ** 3;
export const MAX_FILE = 40_000;
export const MAX_TOTAL = 150_000_000;
export const MAX_RENDERS = 150;
const SCRIPT = fileURLToPath(new URL('./blender/thumb.py', import.meta.url));
const IMAGE = /\.(?:png|jpe?g|webp|avif|gif|svg|tga)$/iu;
const AUDIO = /\.(?:ogg|opus|wav|mp3|m4a|aac|flac|aiff?)$/iu;
const HIDDEN = new Set(['draft', 'rejected', 'review', 'requested']);
const HIDDEN_ROLES = new Set(['draft', 'rejected', 'review', 'report', 'prompt', 'glb-spare', 'unknown']);
// Danh sách cấm: kiểm trước mọi lstat/read và cả dữ liệu xuất.
const DENY = /immortality-cultivation|tu-tien|tu_tien|monkeytype/iu;
const GAMES = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing'];
const compare = (a, b) => String(a).localeCompare(String(b), 'en', { numeric: true });
const shown = f => !f.hidden && !HIDDEN_ROLES.has(f.role) && !HIDDEN.has(f.status);
export const visibleCard = c => !c.hidden && !HIDDEN.has(c.status) && !DENY.test(c.uid);
const hash = (algorithm, bytes) => createHash(algorithm).update(bytes).digest('hex');

// Mọi đầu ra subprocess nằm trong RAM; riêng Blender ghi đúng một ảnh ở .thumbs.
export function runProcess(command, args, { input, env = process.env } = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { shell: false, stdio: ['pipe', 'pipe', 'pipe'], env });
    const chunks = [];
    let size = 0, detail = '';
    child.stdout.on('data', chunk => {
      size += chunk.length;
      if (size > 16 * 1024 ** 2) child.kill();
      else chunks.push(chunk);
    });
    child.stderr.on('data', chunk => { detail = (detail + chunk).slice(-2000); });
    child.stdin.on('error', () => {});
    child.on('error', reject);
    child.on('close', (code, signal) => code === 0 && size <= 16 * 1024 ** 2
      ? resolve(Buffer.concat(chunks))
      : reject(new Error(`${path.basename(command)} thoát ${code ?? signal}: ${detail.trim()}`)));
    child.stdin.end(input);
  });
}

async function json(root, rel, io, optional = false) {
  const info = await safeInfo(root, rel, io);
  if (!info && optional) return null;
  if (!info?.isFile()) throw new Error(`Không có file: ${rel}`);
  return JSON.parse(await io.readFile(path.join(root, rel), 'utf8'));
}

// Đọc AL-12 trực tiếp: không yêu cầu quét lại, không sửa tên hay loại đã duyệt.
export async function loadCards({ repoRoot = REPO_ROOT, io = fs } = {}) {
  const catalogs = [await json(repoRoot, 'library/out/catalog.json', io),
    await json(repoRoot, 'library/out/audio-catalog.json', io, true)].filter(Boolean);
  const rows = new Map();
  if (await safeInfo(repoRoot, 'library/curated', io)) {
    for (const name of (await io.readdir(path.join(repoRoot, 'library/curated'))).sort(compare)) {
      if (!name.endsWith('.jsonl') || DENY.test(name)) continue;
      const rel = `library/curated/${name}`;
      if (!(await safeInfo(repoRoot, rel, io))?.isFile()) continue;
      for (const line of (await io.readFile(path.join(repoRoot, rel), 'utf8')).split(/\r?\n/u).filter(Boolean)) {
        const row = JSON.parse(line);
        if (!DENY.test(row.uid)) rows.set(row.uid, row);
      }
    }
  }
  const cards = new Map();
  for (const catalog of catalogs) {
    if (!['asset-library/1', 'asset-library-audio/1'].includes(catalog.schema) || !Array.isArray(catalog.cards)) throw new Error('Sai lược đồ mục lục');
    for (const card of catalog.cards) {
      if (typeof card.uid !== 'string' || !Array.isArray(card.files)) throw new Error('Thẻ thiếu uid/files');
      if (DENY.test(card.uid)) continue;
      const row = rows.get(card.uid);
      const copy = { ...card, files: card.files.filter(f => !DENY.test(f.path)) };
      if (row) {
        for (const key of ['name', 'kind', 'subkind', 'reviewed']) if (row[key] !== undefined) copy[key] = row[key];
        copy.canonical = { ...card.canonical, ...row.canonical };
      }
      cards.set(card.uid, copy);
    }
  }
  return [...cards.values()].sort((a, b) => compare(a.uid, b.uid));
}

// AL-14 đọc bảng nối bằng hàm này; cả các phần metadata đều dưới 40 KB.
export async function loadThumbIndex({ repoRoot = REPO_ROOT, io = fs } = {}) {
  const index = await json(repoRoot, 'library/.thumbs/index.json', io);
  if (index.schema !== 'asset-library-thumbs/1') throw new Error('Sai lược đồ ảnh nhỏ');
  if (Array.isArray(index.thumbnails)) return index;
  const thumbnails = [];
  for (const name of index.parts ?? []) {
    if (!/^index-[a-f0-9]{64}\.json$/u.test(name)) throw new Error('Phần metadata ảnh nhỏ không hợp lệ');
    const part = await json(repoRoot, `library/.thumbs/${name}`, io);
    thumbnails.push(...part.thumbnails);
  }
  return { schema: index.schema, thumbnails };
}

function images(card) {
  const preferred = [card.canonical?.concept, card.canonical?.['tripo-source'], card.hero, card.canonical?.icon];
  const rank = f => {
    const i = preferred.indexOf(f.path);
    const role = ['concept', 'tripo-source', 'icon', 'icon-256', 'derivative'].indexOf(f.role);
    return i >= 0 ? i : 10 + (role < 0 ? 5 : role);
  };
  return card.files.filter(f => shown(f) && IMAGE.test(f.path)).sort((a, b) => rank(a) - rank(b) || compare(a.path, b.path));
}

// Liên kết có chứng cứ: md5 GLB chung, khóa đầy đủ SOURCES, usedBy/preset.source.
// Không đoán theo tên ngắn vì hai vật khác nhau có thể trùng tên.
async function linkedImages(cards, root, io) {
  const byHash = new Map(), byPath = new Map();
  for (const c of cards.filter(visibleCard)) {
    const image = images(c)[0];
    if (!image) continue;
    for (const f of c.files.filter(f => shown(f) && /\.glb$/iu.test(f.path))) {
      if (f.md5) byHash.set(f.md5, image);
      byPath.set(f.path, image);
    }
  }
  for (const game of GAMES) {
    const prefix = `games/${game}/`;
    const sources = await json(root, `${prefix}art-src/3d/SOURCES.json`, io, true);
    const sourceImages = new Map();
    for (const [key, row] of Object.entries(sources?.files ?? {})) {
      if (typeof row.image !== 'string' || DENY.test(key + row.image)) continue;
      const rel = prefix + row.image;
      const owner = cards.find(c => visibleCard(c) && c.files.some(f => f.path === rel && shown(f)));
      const image = (owner && images(owner)[0]) ?? { path: rel, role: 'concept' };
      sourceImages.set(key, image);
      byPath.set(`${prefix}art-src/3d/${key}`, image);
      // Cùng quy ước target(key) của AL-06: thiếu preset thì giữ đầy đủ key.
      byPath.set(`${prefix}art-src/models/${key}`, image);
      const stem = key.replace(/\.glb$/iu, '');
      const base = stem.split('/').at(-1);
      byPath.set(`${prefix}public/assets/${game}/models/${stem}/${base}.high.glb`, image);
      byPath.set(`${prefix}public/assets/${game}/models/${stem}/${base}.medium.glb`, image);
      for (const used of row.usedBy ?? []) if (typeof used === 'string' && !DENY.test(used)) {
        byPath.set(`${prefix}art-src/models/${used}.glb`, image);
      }
    }
    for (const dir of [`${prefix}scripts/models/presets`, 'scripts/models/presets']) {
      if (!(await safeInfo(root, dir, io))?.isDirectory()) continue;
      for (const name of (await io.readdir(path.join(root, dir))).sort(compare)) {
        if (!name.endsWith('.json') || DENY.test(name)) continue;
        if (dir === 'scripts/models/presets' && !name.includes(game) && !(game === 'space-typing' && name.startsWith('campaign3d'))) continue;
        const preset = await json(root, `${dir}/${name}`, io);
        for (const [key, row] of Object.entries(preset.models ?? {})) {
          const image = sourceImages.get(row.source);
          if (!image || DENY.test(key)) continue;
          byPath.set(`${prefix}art-src/models/${key}.glb`, image);
          byPath.set(`${prefix}public/assets/${game}/models/${key}/${key.split('/').at(-1)}.high.glb`, image);
          byPath.set(`${prefix}public/assets/${game}/models/${key}/${key.split('/').at(-1)}.medium.glb`, image);
        }
      }
    }
  }
  return { byHash, byPath };
}

async function sourceInfo(file, root, home, io) {
  if (!file || typeof file.path !== 'string' || DENY.test(file.path) || file.local === false) return null;
  const external = file.path.startsWith('~/AudioLab/');
  const base = external ? home : root;
  const rel = external ? file.path.slice(2) : file.path;
  const info = await safeInfo(base, rel, io);
  return info?.isFile() ? path.join(base, rel) : null;
}

export const WAVE_DRAW = 'showwavespic=s=256x96:colors=0x63c7df:scale=sqrt:filter=peak';
// Gom 65.536 mẫu/khung để dòng in ra ít (~1 dòng/1,5 s), file dài vẫn dưới trần stdout 16 MB.
const PEAK_PROBE = 'asetnsamples=n=65536:p=0,astats=metadata=1:reset=0:measure_perchannel=none:measure_overall=Peak_level,'
  + 'ametadata=mode=print:key=lavfi.astats.Overall.Peak_level:file=-';
// Dòng cuối của astats cộng dồn là đỉnh cả file; im lặng (-inf) hay không đọc được thì không khuếch đại.
export function waveGain(output) {
  const peak = Number([...String(output).matchAll(/Peak_level=(\S+)/gu)].at(-1)?.[1]);
  return Number.isFinite(peak) ? Math.min(40, Math.max(0, -1 - peak)) : 0;
}

const webp = bytes => bytes.length >= 16 && bytes.toString('ascii', 0, 4) === 'RIFF' && bytes.toString('ascii', 8, 12) === 'WEBP';
const png = bytes => bytes.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]));
// Chuỗi VFX động (WebP/GIF 12 khung) thường mở đầu bằng khung gần trống: 8/13 chuỗi
// combat-vfx ra chấm nhỏ ở khung 0. Lấy khung giữa sau -coalesce (khung delta thành khung đủ).
async function frameArgs(source, magick, exec) {
  if (!/\.(?:webp|gif)$/iu.test(source)) return [`${source}[0]`];
  const frames = Number.parseInt(String(await exec(magick, ['identify', '-format', '%n\n', source])), 10);
  if (!(frames > 1)) return [`${source}[0]`];
  return [source, '-coalesce', '(', '-clone', String(Math.floor(frames / 2)), ')', '-delete', '0--2'];
}

async function encodeWebp(input, magick, exec) {
  for (const quality of [78, 60, 42, 24, 12]) {
    const bytes = await exec(magick, [...input, '-auto-orient', '-strip', '-resize', '256x256',
      '-define', 'webp:alpha-quality=80',
      '-quality', String(quality), 'webp:-']);
    if (!webp(bytes)) throw new Error('WebP không hợp lệ');
    if (bytes.length <= MAX_FILE) return bytes;
  }
  throw new Error(`WebP quá ${MAX_FILE} byte`);
}

/** Kết quả trả về và index.json đều dùng thumb tương đối từ gốc repo.
 * Trang catalog dùng ../.thumbs/<hash> khi nằm trong library/out/.
 * Không sửa catalog.json: AL-13 chỉ có quyền ghi library/.thumbs.
 */
export async function generateThumbs({ repoRoot = REPO_ROOT, io = fs, exec = runProcess,
  stdout = process.stdout, home = os.homedir(), cards: supplied,
  magick = process.env.ART_MAGICK || '/opt/homebrew/bin/magick', ffmpeg = 'ffmpeg',
  blender = '/Applications/Blender.app/Contents/MacOS/Blender' } = {}) {
  const result = { schema: 'asset-library-thumbs/1', created: 0, reused: 0, blenderRenders: 0,
    visible: 0, covered: 0, maxBytes: 0, totalBytes: 0, thumbnails: [], missing: [], warnings: [] };
  const cache = path.join(repoRoot, 'library/.thumbs');
  async function cacheSize(allowIndexMigration = false) {
    let total = 0, max = 0;
    if (await safeInfo(repoRoot, 'library/.thumbs', io)) {
      for (const name of await io.readdir(cache)) {
        if (!/^(?:[a-f0-9]{32}\.webp|[a-f0-9]{64}\.wave\.png|index(?:-[a-f0-9]{64})?\.json)$/u.test(name)) continue;
        const info = await safeInfo(repoRoot, `library/.thumbs/${name}`, io);
        if (!info?.isFile()) throw new Error(`Cache không phải file thường: ${name}`);
        total += info.size;
        if (!(allowIndexMigration && name === 'index.json')) max = Math.max(max, info.size);
      }
    }
    if (max > MAX_FILE || total > MAX_TOTAL) throw new Error('Cache vượt giới hạn 40 KB/file hoặc 150 MB tổng');
    return { total, max };
  }
  async function diskOK() {
    const stat = await io.statfs(repoRoot, { bigint: true });
    const free = BigInt(stat.bavail) * BigInt(stat.bsize);
    if (free >= BigInt(MIN_FREE)) return true;
    result.stopped = true;
    stdout.write(`Dừng: còn ${Number(free / 1024n ** 2n)} MiB trống, cần ít nhất 20 GiB; không tạo thêm file.\n`);
    return false;
  }
  // Kiểm trước cả mkdir, đọc nguồn, thăm dò công cụ và ghi index.
  if (!await diskOK()) return result;
  // Tính cả cache của lượt trước trước khi cấp thêm dung lượng.
  let cacheBytes = (await cacheSize(true)).total;
  const cards = supplied ?? await loadCards({ repoRoot, io });
  const visible = cards.filter(visibleCard);
  result.visible = visible.length;
  const links = await linkedImages(cards, repoRoot, io);
  const availability = new Map(), done = new Map();
  async function available(tool, args) {
    if (!availability.has(tool)) {
      try { await exec(tool, args); availability.set(tool, true); }
      catch (error) {
        availability.set(tool, false);
        result.warnings.push(`Bỏ qua ${path.basename(tool)}: ${error.message}`);
      }
    }
    return availability.get(tool);
  }
  async function existing(name) {
    const info = await safeInfo(repoRoot, `library/.thumbs/${name}`, io);
    if (!info) return false;
    if (!info.isFile()) throw new Error(`Cache không phải file thường: ${name}`);
    const bytes = await io.readFile(path.join(cache, name));
    if (bytes.length > MAX_FILE || !(name.endsWith('.webp') ? webp(bytes) : png(bytes))) {
      throw new Error(`Cache hỏng hoặc quá ${MAX_FILE} byte: ${name}`);
    }
    return true;
  }
  for (const card of visible) {
    try {
      const isAudio = ['audio', 'music'].includes(card.type);
      const models = card.files.filter(f => shown(f) && /\.glb$/iu.test(f.path))
        .sort((a, b) => (a.role === 'glb-original' ? -1 : b.role === 'glb-original' ? 1 : 0) || compare(a.path, b.path));
      let file, kind;
      if (isAudio) {
        // Tuyệt đối không chuyển sang biến thể thứ hai khi biến thể đầu vắng mặt.
        file = card.files.filter(f => shown(f) && AUDIO.test(f.path)).sort((a, b) =>
          compare(a.variant ?? a.path, b.variant ?? b.path) || compare(a.path, b.path))[0];
        kind = 'wave';
      } else {
        const candidates = [...images(card), ...models.flatMap(f => [links.byPath.get(f.path), links.byHash.get(f.md5)]).filter(Boolean)];
        for (const candidate of candidates) if (await sourceInfo(candidate, repoRoot, home, io)) { file = candidate; break; }
        if (file) kind = 'image';
        else if (candidates.length) throw new Error('Ảnh nguồn liên kết không có trên máy; không render thay bằng GLB');
        else { file = models[0]; kind = 'blender'; }
      }
      if (!file) throw new Error('Không có file nguồn phù hợp');
      let key = isAudio ? file.sha256 : file.md5;
      let source;
      if (!(isAudio ? /^[a-f0-9]{64}$/u : /^[a-f0-9]{32}$/u).test(key ?? '')) {
        source = await sourceInfo(file, repoRoot, home, io);
        if (!source) throw new Error('Không đọc được file nguồn để băm');
        key = hash(isAudio ? 'sha256' : 'md5', await io.readFile(source));
      }
      const name = `${key}${isAudio ? '.wave.png' : '.webp'}`;
      const entry = { uid: card.uid, name: card.name, kind: card.kind, subkind: card.subkind,
        thumb: `library/.thumbs/${name}`, source: file.path, method: kind };
      if (done.has(name) || await existing(name)) {
        result.reused++;
      } else {
        source ??= await sourceInfo(file, repoRoot, home, io);
        if (!source) throw new Error(`File chưa có trên máy hoặc không đọc được: ${file.path}`);
        if (!await diskOK()) break;
        if (kind === 'blender' && result.blenderRenders >= MAX_RENDERS) throw new Error('Đã chạm trần 150 lần render Blender');
        if (kind === 'blender' && cacheBytes + MAX_FILE > MAX_TOTAL) throw new Error('Không đủ ngân sách 150 MB để render GLB');
        if (!await available(magick, ['-version'])) throw new Error('Không dùng được magick');
        if (kind === 'wave' && !await available(ffmpeg, ['-version'])) throw new Error('Không dùng được ffmpeg');
        if (kind === 'blender' && !await available(blender,
          ['--disable-crash-handler', '--disable-abort-handler', '-b', '--factory-startup', '--disable-autoexec', '--python-expr', 'print("AL13_READY")'])) {
          throw new Error('Không dùng được Blender headless');
        }
        await io.mkdir(cache, { recursive: true });
        let bytes;
        if (kind === 'image') bytes = await encodeWebp(await frameArgs(source, magick, exec), magick, exec);
        else if (kind === 'wave') {
          // Lớp velocity mềm (VSCO2, đỉnh −30…−40 dB) vẽ ra vạch phẳng: đo đỉnh trước,
          // đưa về −1 dBFS (tối đa +40 dB) rồi vẽ theo đỉnh từng cột thay vì trung bình.
          const gain = waveGain(await exec(ffmpeg, ['-nostdin', '-hide_banner', '-loglevel', 'error', '-i', source,
            '-af', `aformat=channel_layouts=mono,${PEAK_PROBE}`, '-threads', '1', '-f', 'null', '-']));
          const raw = await exec(ffmpeg, ['-nostdin', '-hide_banner', '-loglevel', 'error', '-i', source,
            '-filter_complex', `aformat=channel_layouts=mono,volume=${gain.toFixed(2)}dB,${WAVE_DRAW}`,
            '-frames:v', '1', '-threads', '1', '-f', 'image2pipe', '-vcodec', 'png', 'pipe:1']);
          bytes = await exec(magick, ['png:-', '-strip', '-define', 'png:compression-level=9', 'png:-'], { input: raw });
          if (!png(bytes) || bytes.length > MAX_FILE) throw new Error(`Dạng sóng quá ${MAX_FILE} byte hoặc PNG không hợp lệ`);
        } else {
          result.blenderRenders++;
          // Blender ghi PNG vào đúng tên cache; magick thay bằng WebP ngay sau đó.
          // Nếu tiến trình bị ngắt, lượt sau báo cache hỏng thay vì tái dùng ảnh sai.
          const output = path.join(cache, name);
          await exec(blender, ['--disable-crash-handler', '--disable-abort-handler', '-b', '--factory-startup',
            '--disable-autoexec', '-P', SCRIPT, '--', source, output]);
          bytes = await encodeWebp([output], magick, exec);
        }
        if (cacheBytes + bytes.length > MAX_TOTAL) throw new Error('Ảnh nhỏ vượt tổng 150 MB');
        await io.writeFile(path.join(cache, name), bytes, { flag: kind === 'blender' ? 'w' : 'wx' });
        cacheBytes += bytes.length;
        result.created++;
      }
      const size = done.get(name) ?? (await io.stat(path.join(cache, name))).size;
      if (!done.has(name)) { result.totalBytes += size; result.maxBytes = Math.max(result.maxBytes, size); }
      done.set(name, size);
      result.thumbnails.push(entry);
      result.covered++;
    } catch (error) {
      result.missing.push({ uid: card.uid, reason: error.message });
    }
  }
  // Kiểm cả cache cũ, không tự xóa ảnh (chỉ dọn phần index mồ côi) và không xuất metadata nguồn riêng tư.
  if (!result.stopped) {
    const encode = thumbnails => JSON.stringify({ schema: result.schema, thumbnails }, null, 2) + '\n';
    const files = new Map();
    let index = encode(result.thumbnails);
    if (Buffer.byteLength(index) > MAX_FILE) {
      const parts = [];
      let rows = [];
      const flush = () => {
        const content = encode(rows), name = `index-${hash('sha256', content)}.json`;
        files.set(name, content); parts.push(name); rows = [];
      };
      for (const entry of result.thumbnails) {
        if (Buffer.byteLength(encode([...rows, entry])) > MAX_FILE && rows.length) flush();
        rows.push(entry);
      }
      if (rows.length) flush();
      index = JSON.stringify({ schema: result.schema, parts }, null, 2) + '\n';
    }
    files.set('index.json', index);
    const changes = [];
    let plannedBytes = cacheBytes;
    for (const [name, content] of files) {
      const bytes = Buffer.byteLength(content);
      if (bytes > MAX_FILE) throw new Error('Metadata ảnh nhỏ vượt 40 KB/file');
      const old = await safeInfo(repoRoot, `library/.thumbs/${name}`, io)
        ? await io.readFile(path.join(cache, name), 'utf8') : null;
      if (old === content) continue;
      plannedBytes += bytes - (old === null ? 0 : Buffer.byteLength(old));
      changes.push({ name, content, old });
    }
    if (plannedBytes > MAX_TOTAL) throw new Error('Ảnh nhỏ và metadata vượt tổng 150 MB');
    if (changes.length) await io.mkdir(cache, { recursive: true });
    for (const { name, content, old } of changes) {
      await io.writeFile(path.join(cache, name), content, { flag: old === null ? 'wx' : 'w' });
    }
    // Phần index theo hash nội dung: bảng nối đổi thì phần cũ thành rác (lượt duyệt 28/10
    // thêm 34 phần mới, 34 phần cũ ở lại). Chỉ xóa phần index-<sha256>.json không còn được trỏ tới.
    if (await safeInfo(repoRoot, 'library/.thumbs', io)) {
      for (const name of await io.readdir(cache)) {
        if (/^index-[a-f0-9]{64}\.json$/u.test(name) && !files.has(name)) await io.unlink(path.join(cache, name));
      }
    }
  }
  const sizes = await cacheSize();
  result.totalBytes = sizes.total; result.maxBytes = sizes.max;
  stdout.write(`Ảnh nhỏ: ${result.covered}/${result.visible} thẻ; tạo ${result.created}; dùng lại ${result.reused}; Blender ${result.blenderRenders}/${MAX_RENDERS}.\n`);
  stdout.write(`File lớn nhất: ${result.maxBytes} byte; tổng: ${result.totalBytes} byte (trần ${MAX_FILE} / ${MAX_TOTAL}).\n`);
  for (const warning of result.warnings) stdout.write(`${warning}\n`);
  for (const item of result.missing) stdout.write(`Thiếu ${item.uid}: ${item.reason}\n`);
  return result;
}

export async function runThumbs(argv = [], options = {}) {
  if (argv.length) throw new Error('Cách dùng: node tools/asset-library/thumbs.mjs');
  const result = await generateThumbs(options);
  return result.stopped || result.missing.length ? 1 : 0;
}
main(import.meta.url, runThumbs);
