// Drive-side helpers: the remote must exist and be pinned to its folder before
// anything else touches it; lock copies live in _locks/<stamp>/.
import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { formatLock, parseLock } from './lock.mjs';
import { installHint, rcloneOk, rcloneVersion, remoteConfig, runRclone, versionAtLeast } from './rclone.mjs';
import { assertLockKeys } from './sets.mjs';
import { MediaError } from './ui.mjs';

export const LOCK_COPY_NAMES = { game: 'space-typing.media.md5', private: 'private.md5' };
// Which set rules a Drive lock copy's keys must follow (see lockKeyProblem).
const LOCK_COPY_KINDS = { [LOCK_COPY_NAMES.game]: 'game', [LOCK_COPY_NAMES.private]: 'private' };
const STAMP = /^\d{4}-\d{2}-\d{2}_\d{6}Z$/;
// Test backends: an alias or local remote pointing at a temp folder.
const TEST_TYPES = new Set(['alias', 'local']);

export function tempDir(prefix = 'media-') {
  return mkdtempSync(path.join(tmpdir(), prefix));
}

export async function ensureRclone(ctx) {
  const version = await rcloneVersion(ctx);
  if (!version) throw new MediaError(`Chưa có rclone. ${installHint()}`);
  if (!versionAtLeast(version, ctx.config.rcloneMinVersion)) {
    throw new MediaError(`rclone ${version.join('.')} quá cũ (cần ${ctx.config.rcloneMinVersion} trở lên). ${installHint()}`);
  }
  return version;
}

/** The remote is configured, and a Drive remote is pinned to its own folder (root_folder_id). */
export async function ensureRemote(ctx) {
  await ensureRclone(ctx);
  const remote = ctx.config.remote;
  const config = await remoteConfig(ctx, remote);
  if (!config) {
    throw new MediaError(`Máy này chưa kết nối Google Drive (remote "${remote}"). Chạy pnpm media:setup trong terminal của bạn (không chạy qua AI).`);
  }
  if (config.type === 'drive') {
    if (!config.root_folder_id) {
      throw new MediaError(`Remote "${remote}" chưa được khoá vào thư mục ${ctx.config.driveFolder}. Chạy lại pnpm media:setup.`);
    }
  } else if (!TEST_TYPES.has(config.type)) {
    throw new MediaError(`Remote "${remote}" có kiểu ${config.type}; kho media chỉ dùng Google Drive.`);
  }
  return { remote, type: config.type, isDrive: config.type === 'drive' };
}

export function driveFlags(info) {
  return info.isDrive ? ['--fast-list', '--drive-stop-on-upload-limit'] : [];
}

export function listingFlags(info) {
  return info.isDrive ? ['--fast-list'] : [];
}

/**
 * Lists _locks/<stamp>/<name>. Returns { byName: { [name]: stamps oldest first },
 * maxStamp } where maxStamp is the newest stamp of any copy (for the clock check).
 */
export async function listLockCopies(ctx, info) {
  const byName = Object.fromEntries(Object.values(LOCK_COPY_NAMES).map((name) => [name, []]));
  let maxStamp = null;
  if (!(await remoteTopFolders(ctx, info)).has('_locks')) return { byName, maxStamp };
  const listing = await rcloneOk(ctx, ['lsf', '-R', '--files-only', `${info.remote}:_locks`, ...listingFlags(info)]);
  for (const line of listing.stdout.split('\n')) {
    const [stamp, name, extra] = line.trim().split('/');
    if (extra !== undefined || !STAMP.test(stamp ?? '') || !byName[name]) continue;
    byName[name].push(stamp);
    if (!maxStamp || stamp > maxStamp) maxStamp = stamp;
  }
  for (const stamps of Object.values(byName)) stamps.sort();
  return { byName, maxStamp };
}

/**
 * Downloads the given copies ([{ stamp, name }]) in one rclone call. Returns
 * Map("stamp/name" -> entries). Every key must stay inside its set.
 */
export async function downloadLockCopies(ctx, info, items) {
  const result = new Map();
  if (!items.length) return result;
  const wanted = items.map(({ stamp, name }) => `${stamp}/${name}`);
  const dir = tempDir('media-locks-');
  try {
    const listFile = path.join(dir, 'files.txt');
    writeFileSync(listFile, `${wanted.join('\n')}\n`);
    const target = path.join(dir, 'locks');
    await rcloneOk(ctx, ['copy', `${info.remote}:_locks`, target, '--files-from-raw', listFile, ...listingFlags(info)]);
    for (const { stamp, name } of items) {
      const file = path.join(target, stamp, name);
      if (!existsSync(file)) continue;
      const label = `Drive _locks/${stamp}/${name}`;
      result.set(`${stamp}/${name}`, assertLockKeys(ctx.config, LOCK_COPY_KINDS[name], parseLock(readFileSync(file, 'utf8'), label), label));
    }
    return result;
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

/**
 * Downloads lock copies from _locks/<stamp>/: every version for names in
 * `all` (history), only the newest for names in `latest`.
 * Returns { [name]: [{ stamp, entries }] } sorted oldest first.
 */
export async function fetchLockCopies(ctx, info, { all = [], latest = [] } = {}, listing = null) {
  const names = [...new Set([...all, ...latest])];
  const result = Object.fromEntries(names.map((name) => [name, []]));
  if (!names.length) return result;
  const { byName } = listing ?? await listLockCopies(ctx, info);
  const items = [];
  for (const name of names) {
    const stamps = byName[name] ?? [];
    for (const stamp of all.includes(name) ? stamps : stamps.slice(-1)) items.push({ stamp, name });
  }
  const copies = await downloadLockCopies(ctx, info, items);
  for (const { stamp, name } of items) {
    const entries = copies.get(`${stamp}/${name}`);
    if (entries) result[name].push({ stamp, entries });
  }
  return result;
}

/** Copies the lock files to _locks/<stamp>/ so Drive describes itself without Git. */
export async function uploadLockCopies(ctx, info, stamp, copies) {
  const entries = Object.entries(copies).filter(([, lock]) => lock);
  if (!entries.length) return;
  const dir = tempDir('media-lockcopy-');
  try {
    for (const [name, lock] of entries) writeFileSync(path.join(dir, name), formatLock(lock));
    await rcloneOk(ctx, ['copy', dir, `${info.remote}:_locks/${stamp}`]);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

/** Top-level folders inside the pinned Drive folder (repo, private, _locks, _replaced). */
export async function remoteTopFolders(ctx, info) {
  if (info.topFolders) return info.topFolders;
  const result = await rcloneOk(ctx, ['lsf', `${info.remote}:`, '--dirs-only', '--max-depth', '1']);
  info.topFolders = new Set(result.stdout.split('\n').map((line) => line.trim().replace(/\/$/, '')).filter(Boolean));
  return info.topFolders;
}

/** True when the Drive folder for a set base exists (repo/games/space-typing, private). */
export async function remoteHas(ctx, info, remoteBase) {
  return (await remoteTopFolders(ctx, info)).has(remoteBase.split('/')[0]);
}

export async function driveAbout(ctx, info) {
  const result = await runRclone(ctx, ['about', `${info.remote}:`, '--json']);
  if (result.code !== 0) return null;
  try { return JSON.parse(result.stdout); }
  catch { return null; }
}
