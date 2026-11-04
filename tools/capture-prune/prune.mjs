import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const IMAGE = /\.(png|jpe?g|webp)$/i;
// So theo thành phần thư mục: “htdocs” trên Mac không phải thư mục “docs”.
const FORBIDDEN = /(?:^|\/)(?:art-src|public|docs|typing-game-handoff|immortality-cultivation)(?:[\/_-]|$)/i;
const DEFAULT_ROOT = fileURLToPath(new URL('../../', import.meta.url));
const posix = value => value.split(path.sep).join('/');
const inside = (root, file) => file === root || file.startsWith(root + path.sep);
const message = error => `${error.code ?? 'ERROR'}: ${error.message}`;

export function targetRefusal(real, repoRoot, worktreeRoot, reviewRoot = null) {
  const inReview = reviewRoot && inside(reviewRoot, real);
  if (inReview && !inside(path.join(reviewRoot, 'captures'), real)) return 'review-not-captures';
  if (FORBIDDEN.test(posix(real))) return 'protected-path';
  if (inReview) return null;
  if (!/(\/tmp\/|\/tmp$)/.test(posix(real))) return 'not-tmp';
  if (!inside(repoRoot, real) && !inside(worktreeRoot, real)) return 'outside-roots';
  return null;
}

export function parseArgs(args) {
  const result = { targets: [], docs: null, apply: false, minAgeMin: 30, json: null, reviewRoot: null };
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === '--apply') result.apply = true;
    else if (arg === '--help' || arg === '-h') result.help = true;
    else if (arg === '--docs') {
      result.docs ??= [];
      const start = i;
      while (i + 1 < args.length && !args[i + 1].startsWith('--')) result.docs.push(args[++i]);
      if (i === start) throw new Error('--docs cần ít nhất một đường dẫn.');
    } else if (arg === '--min-age-min' || arg === '--json' || arg === '--review-root') {
      const value = args[++i];
      if (!value || value.startsWith('--')) throw new Error(`${arg} thiếu giá trị.`);
      if (arg === '--json') result.json = value;
      else if (arg === '--review-root') result.reviewRoot = value;
      else {
        result.minAgeMin = Number(value);
        if (!Number.isFinite(result.minAgeMin) || result.minAgeMin < 0) {
          throw new Error('--min-age-min phải là số hữu hạn không âm.');
        }
      }
    } else if (arg.startsWith('-')) throw new Error(`Tùy chọn không hợp lệ: ${arg}`);
    else result.targets.push(arg);
  }
  if (!result.help && !result.targets.length) throw new Error('Cần ít nhất một thư mục đích.');
  return result;
}

function defaultDocs(repoRoot, reviewRoot = null) {
  const roots = [path.join(repoRoot, 'docs')];
  if (reviewRoot) roots.push(path.join(reviewRoot, 'README.md'));
  const games = path.join(repoRoot, 'games');
  if (!fs.existsSync(games)) return roots;
  for (const game of fs.readdirSync(games, { withFileTypes: true })) {
    // Tu Tiên's docs count too since 04/11: its captures moved to the review folder and can be pruned there.
    if (!game.isDirectory()) continue;
    const dir = path.join(games, game.name);
    roots.push(path.join(dir, 'docs'));
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      if (entry.isFile() && /\.md$/i.test(entry.name)) roots.push(path.join(dir, entry.name));
    }
  }
  return roots;
}

function readReferences(roots, optional) {
  const refs = new Set();
  const seen = new Set();
  function visit(file) {
    let stat;
    try { stat = fs.lstatSync(file); }
    catch (error) { if (optional && error.code === 'ENOENT') return; throw error; }
    if (stat.isSymbolicLink()) return;
    if (stat.isDirectory()) {
      for (const name of fs.readdirSync(file).sort()) visit(path.join(file, name));
    } else if (stat.isFile() && /\.md$/i.test(file) && !seen.has(file)) {
      seen.add(file);
      const text = fs.readFileSync(file, 'utf8');
      // Quét riêng để tmp/ trong tiền tố không nuốt mất tham chiếu captures/ phía sau.
      for (const pattern of [/tmp\/[^\s)`"'<>]+\.(?:png|jpe?g|webp)/gi, /captures\/[^\s)`"'<>]+\.(?:png|jpe?g|webp)/gi]) {
        for (const match of text.matchAll(pattern)) refs.add(match[0]);
      }
    }
  }
  roots.forEach(visit);
  return refs;
}

function referenced(real, refs, repoRoot, reviewRoot, areas) {
  let relatives = [posix(path.relative(repoRoot, real))];
  if (reviewRoot && inside(path.join(reviewRoot, 'captures'), real)) {
    const captureRef = posix(path.relative(reviewRoot, real));
    if (refs.has(captureRef)) return true;
    const [, area, ...rest] = captureRef.split('/');
    const mapping = areas[area];
    if (!Array.isArray(mapping)) return false;
    const [gameDir, legacyPrefix] = mapping;
    if (typeof gameDir !== 'string' || typeof legacyPrefix !== 'string') return false;
    const legacyRef = legacyPrefix + rest.join('/');
    relatives = [legacyRef, `${gameDir}/${legacyRef}`];
  }
  // Regex bắt đầu ở tmp/, kể cả khi Markdown ghi games/x/tmp/ảnh.png.
  for (const relative of relatives) {
    for (let index = relative.indexOf('tmp/'); index !== -1; index = relative.indexOf('tmp/', index + 1)) {
      if (refs.has(relative.slice(index))) return true;
    }
  }
  return false;
}

function identity(stat) {
  return { dev: stat.dev, ino: stat.ino, size: stat.size, mtimeMs: stat.mtimeMs, ctimeMs: stat.ctimeMs };
}

export function planPrune(options, { repoRoot = DEFAULT_ROOT, now = Date.now() } = {}) {
  repoRoot = fs.realpathSync(repoRoot);
  let worktreeRoot = path.resolve(repoRoot, '../typing-game-wt');
  if (fs.existsSync(worktreeRoot)) worktreeRoot = fs.realpathSync(worktreeRoot);
  let reviewRoot = options.reviewRoot ?? path.resolve(repoRoot, '..', path.basename(repoRoot) + '-review');
  reviewRoot = options.reviewRoot != null || fs.existsSync(reviewRoot) ? fs.realpathSync(reviewRoot) : null;
  const config = reviewRoot && path.join(reviewRoot, 'review.config.json');
  const areas = config && fs.existsSync(config) ? JSON.parse(fs.readFileSync(config, 'utf8')).areas ?? {} : {};
  const refs = readReferences(options.docs === null ? defaultDocs(repoRoot, reviewRoot) : options.docs.map(p => path.resolve(p)), options.docs === null);
  const result = { targets: [], files: [], kept: [], bytes: 0, refused: [] };
  const seenFiles = new Set();
  const refuse = (file, reason) => result.refused.push({ path: file, reason });
  const cutoff = now - options.minAgeMin * 60_000;

  function walk(dir, target) {
    for (const name of fs.readdirSync(dir).sort()) {
      const file = path.join(dir, name);
      let stat, real;
      try {
        stat = fs.lstatSync(file);
        if (stat.isSymbolicLink()) {
          let outside = false;
          try { outside = !inside(target, fs.realpathSync(file)); } catch { /* Liên kết gãy cũng bỏ qua. */ }
          refuse(file, outside ? 'outside-target' : 'symlink');
          continue;
        }
        real = fs.realpathSync(file);
      } catch (error) { refuse(file, message(error)); continue; }
      if (!inside(target, real)) { refuse(file, 'outside-target'); continue; }
      if (stat.isDirectory()) {
        if (FORBIDDEN.test(posix(real))) { refuse(file, 'protected-path'); continue; }
        walk(file, target);
      } else if (stat.isFile() && IMAGE.test(name) && !seenFiles.has(real)) {
        seenFiles.add(real);
        const relative = posix(path.relative(target, real));
        const reasons = [];
        if (/sheet|contact|compare/i.test(name)) reasons.push('name');
        if (posix(path.dirname(real)).split('/').some(part => /^compare/i.test(part))) reasons.push('compare-directory');
        if (referenced(real, refs, repoRoot, reviewRoot, areas)) reasons.push('document-reference');
        if (stat.mtimeMs >= cutoff) reasons.push('too-new');
        const entry = { target, path: real, relative, bytes: stat.size };
        if (reasons.length) result.kept.push({ ...entry, reasons });
        else {
          result.files.push({ ...entry, identity: identity(stat) });
          result.bytes += stat.size;
        }
      }
    }
  }
  for (const input of options.targets) {
    const absolute = path.resolve(input);
    try {
      const stat = fs.lstatSync(absolute);
      if (stat.isSymbolicLink()) { refuse(absolute, 'symlink'); continue; }
      if (!stat.isDirectory()) { refuse(absolute, 'not-directory'); continue; }
      const real = fs.realpathSync(absolute);
      const reason = targetRefusal(real, repoRoot, worktreeRoot, reviewRoot);
      if (reason) { refuse(absolute, reason); continue; }
      if (result.targets.includes(real)) continue;
      result.targets.push(real);
      walk(real, real);
    } catch (error) { refuse(absolute, message(error)); }
  }
  return result;
}

export function printPlan(result, write = line => process.stdout.write(line + '\n')) {
  write('Danh sách ảnh thô sẽ xóa (byte):');
  for (const file of result.files) write(`${file.path}\t${file.bytes}`);
  write('\nThư mục / nhóm cấp 1\tSố file\tMB (1 MB = 1.000.000 byte)');
  for (const target of result.targets) {
    const groups = new Map();
    const files = result.files.filter(file => file.target === target);
    for (const file of files) {
      const group = file.relative.includes('/') ? file.relative.split('/')[0] : '.';
      const sum = groups.get(group) ?? { count: 0, bytes: 0 };
      sum.count++; sum.bytes += file.bytes; groups.set(group, sum);
    }
    for (const [group, sum] of groups) write(`${target}/${group}\t${sum.count}\t${(sum.bytes / 1e6).toFixed(3)}`);
    write(`${target} [cộng]\t${files.length}\t${(files.reduce((n, f) => n + f.bytes, 0) / 1e6).toFixed(3)}`);
  }
  write(`Tổng: ${result.files.length} file, ${(result.bytes / 1e6).toFixed(3)} MB; giữ ${result.kept.length} ảnh, từ chối ${result.refused.length} mục.`);
  for (const item of result.refused) write(`Từ chối: ${item.path}\t${item.reason}`);
}

function unchanged(file) {
  const stat = fs.lstatSync(file.path);
  if (!stat.isFile() || stat.isSymbolicLink() || fs.realpathSync(file.target) !== file.target) return false;
  // Không đi qua một thư mục cha vừa bị thay thành symlink, kể cả symlink trỏ vào trong.
  for (let dir = path.dirname(file.path); inside(file.target, dir); dir = path.dirname(dir)) {
    if (fs.lstatSync(dir).isSymbolicLink()) return false;
    if (dir === file.target) break;
  }
  if (fs.realpathSync(file.path) !== file.path || !inside(file.target, file.path)) return false;
  return Object.entries(file.identity).every(([key, value]) => stat[key] === value);
}

export function applyPlan(result, { now = new Date() } = {}) {
  const pad = n => String(n).padStart(2, '0');
  const stamp = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}-${pad(now.getHours())}${pad(now.getMinutes())}`;
  const deleted = [];
  const logs = [];
  let failed = false;
  for (const target of result.targets) {
    const files = result.files.filter(file => file.target === target);
    if (!files.length) continue;
    let fd;
    const log = path.join(target, `.pruned-${stamp}.txt`);
    try {
      if (fs.realpathSync(target) !== target || fs.lstatSync(target).isSymbolicLink()) throw new Error('Đích đã đổi.');
      // Giữ chỗ độc quyền trước khi xóa; không ghi đè nhật ký cùng phút hoặc symlink.
      fd = fs.openSync(log, 'wx');
      logs.push(log);
      for (const file of files) {
        try {
          if (!unchanged(file)) throw new Error('File đã đổi từ lúc lập danh sách.');
          fs.unlinkSync(file.path);
          deleted.push(file.path);
          fs.writeSync(fd, `${file.relative}\t${file.bytes}\n`);
        } catch (error) {
          failed = true;
          result.refused.push({ path: file.path, reason: message(error) });
        }
      }
    } catch (error) {
      failed = true;
      result.refused.push({ path: target, reason: message(error) });
    } finally { if (fd !== undefined) fs.closeSync(fd); }
  }
  result.deleted = deleted;
  result.logs = logs;
  return failed ? 1 : 0;
}

export function main(args, context = {}) {
  const options = parseArgs(args);
  const write = context.write ?? (line => process.stdout.write(line + '\n'));
  if (options.help) {
    write('node tools/capture-prune/prune.mjs <thư mục>... [--apply] [--min-age-min 30] [--review-root <thư mục>] [--docs <gốc tài liệu>...] [--json <file>]');
    return 0;
  }
  const result = planPrune(options, context);
  printPlan(result, write);
  let jsonFd;
  // Mở đầu ra trước --apply để lỗi đường dẫn/ghi đè không xảy ra sau khi đã xóa ảnh.
  if (options.json) {
    const output = path.resolve(options.json);
    if (!/\.json$/i.test(output)) throw new Error('--json cần file có đuôi .json.');
    fs.mkdirSync(path.dirname(output), { recursive: true });
    const realOutput = path.join(fs.realpathSync(path.dirname(output)), path.basename(output));
    if (result.targets.some(target => inside(target, realOutput))) throw new Error('--json phải nằm ngoài các thư mục đích.');
    try { jsonFd = fs.openSync(output, 'wx'); }
    catch (error) {
      if (error.code !== 'EEXIST') throw error;
      const previous = fs.lstatSync(output);
      if (!previous.isFile() || previous.isSymbolicLink() || previous.nlink !== 1) throw new Error('Đầu ra JSON phải là file thường, không liên kết.');
      jsonFd = fs.openSync(output, fs.constants.O_WRONLY | fs.constants.O_NOFOLLOW);
      const opened = fs.fstatSync(jsonFd);
      if (opened.dev !== previous.dev || opened.ino !== previous.ino || opened.nlink !== 1) {
        fs.closeSync(jsonFd); throw new Error('Đầu ra JSON đã đổi.');
      }
      fs.ftruncateSync(jsonFd, 0);
    }
  }
  let code = result.targets.length ? 0 : 2;
  try {
    if (options.apply && result.targets.length) {
      const start = result.refused.length;
      code = applyPlan(result);
      write(`Đã xóa ${result.deleted.length}/${result.files.length} file; nhật ký: ${result.logs.join(', ') || '(không có)'}.`);
      for (const item of result.refused.slice(start)) write(`Từ chối: ${item.path}\t${item.reason}`);
    }
    if (jsonFd !== undefined) fs.writeFileSync(jsonFd, JSON.stringify(result, null, 2) + '\n');
  } finally { if (jsonFd !== undefined) fs.closeSync(jsonFd); }
  return code;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { process.exitCode = main(process.argv.slice(2)); }
  catch (error) { process.stderr.write(message(error) + '\n'); process.exitCode = 1; }
}
