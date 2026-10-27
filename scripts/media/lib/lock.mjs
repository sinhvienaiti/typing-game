// Lock files: md5sum format ("<md5>  <path>"), one line per file, sorted,
// POSIX paths, LF endings. A line means the bytes are verified on Drive.
import { existsSync, mkdirSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const LINE = /^([0-9a-f]{32}) [ *](.+)$/;
const CONFLICT = /^(<<<<<<<|=======|>>>>>>>|\|\|\|\|\|\|\|)/;

export class LockError extends Error {}

/**
 * Portable relative path: no backslash, no absolute path, no empty/./.. segment,
 * no control character, and none of the characters Windows forbids in a name
 * (`<>:"|?*`; a WSL `x.png:Zone.Identifier` stream would otherwise slip in).
 */
export function isSafeRelativePath(value) {
  return typeof value === 'string' && value.length > 0
    && !value.startsWith('/') && !/[\\<>:"|?*\u0000-\u001f]/.test(value)
    && value.split('/').every((part) => part && part !== '.' && part !== '..');
}

export function parseLock(text, label = 'media.md5') {
  const entries = new Map();
  const lines = text.split('\n');
  lines.forEach((raw, index) => {
    const line = raw.replace(/\r$/, '');
    if (!line.trim()) return;
    if (CONFLICT.test(line)) {
      throw new LockError(`${label}: còn dấu xung đột merge ở dòng ${index + 1}. Sửa xung đột (giữ cả hai phía) rồi chạy lại.`);
    }
    const match = LINE.exec(line);
    if (!match) throw new LockError(`${label}: dòng ${index + 1} sai định dạng md5sum: ${line.slice(0, 80)}`);
    const [, md5, file] = match;
    if (!isSafeRelativePath(file)) throw new LockError(`${label}: đường dẫn không hợp lệ ở dòng ${index + 1}: ${file}`);
    const previous = entries.get(file);
    if (previous && previous !== md5) {
      throw new LockError(`${label}: có 2 dòng khác md5 cho cùng file ${file}. Giữ một dòng (bản trên Drive: pnpm media:check --remote).`);
    }
    entries.set(file, md5);
  });
  return entries;
}

function compareCodeUnits(left, right) {
  if (left === right) return 0;
  return left < right ? -1 : 1;
}

export function formatLock(entries) {
  return [...entries.keys()].sort(compareCodeUnits).map((file) => {
    const md5 = entries.get(file);
    if (!/^[0-9a-f]{32}$/.test(md5)) throw new LockError(`md5 không hợp lệ cho ${file}`);
    if (!isSafeRelativePath(file)) throw new LockError(`đường dẫn không hợp lệ: ${file}`);
    return `${md5}  ${file}\n`;
  }).join('');
}

export function readLockFile(file, label = path.basename(file)) {
  if (!existsSync(file)) return null;
  return parseLock(readFileSync(file, 'utf8'), label);
}

export function writeFileAtomic(file, content) {
  mkdirSync(path.dirname(file), { recursive: true });
  const temporary = `${file}.${process.pid}.tmp`;
  writeFileSync(temporary, content);
  renameSync(temporary, file);
}

export function writeLockFile(file, entries) {
  writeFileAtomic(file, formatLock(entries));
}

export function sameEntries(left, right) {
  if ((left?.size ?? 0) !== (right?.size ?? 0)) return false;
  for (const [file, md5] of left ?? []) if (right.get(file) !== md5) return false;
  return true;
}

/** Every md5 a path has had: from `git log -p` of a lock, or from several lock texts. */
export function parseLockHistory(patchText) {
  const history = new Map();
  for (const raw of patchText.split('\n')) {
    const line = raw.replace(/\r$/, '');
    if (line.startsWith('+++') || line.startsWith('---')) continue;
    const sign = line[0];
    if (sign !== '+' && sign !== '-' && sign !== ' ') continue;
    const match = LINE.exec(line.slice(1));
    if (!match) continue;
    addHistory(history, match[2], match[1]);
  }
  return history;
}

export function addHistory(history, file, md5) {
  if (!history.has(file)) history.set(file, new Set());
  history.get(file).add(md5);
}

export function mergeHistory(target, entries) {
  for (const [file, md5] of entries ?? []) addHistory(target, file, md5);
  return target;
}
