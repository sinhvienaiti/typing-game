// pnpm media:pull: download only the files the lock lists and this machine
// lacks. Never overwrites or deletes a local file: --update-stale first moves
// a stale copy to .media-old/<stamp>/. Downloads land in .media-tmp/<stamp>/
// and only a file whose md5 matches the lock is moved into place.
import { existsSync, mkdirSync, readFileSync, renameSync, rmdirSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';
import { lockHistory } from '../lib/git.mjs';
import { hashEntries } from '../lib/hash.mjs';
import { mergeHistory, sameEntries, writeLockFile } from '../lib/lock.mjs';
import { runRclone, TRANSFER_FLAGS } from '../lib/rclone.mjs';
import { ensureRemote, fetchLockCopies, listingFlags, PRIVATE_LOCK_COPY, tempDir } from '../lib/remote.mjs';
import { lockCopyName, presentGames, setDefinitions, toRel, withGame } from '../lib/sets.mjs';
import { gameSetNames, lockForSet, readGameLock, readLocks, selectedSets } from '../lib/state.mjs';
import { fmtBytes, fmtCount, MediaError, printList, runStamp } from '../lib/ui.mjs';

function resolveTarget(ctx, value) {
  const expanded = value === '~' ? homedir() : value.startsWith('~/') ? path.join(homedir(), value.slice(2)) : value;
  const target = path.resolve(ctx.root, expanded);
  const relative = path.relative(ctx.root, target);
  if (!relative || (!relative.startsWith('..') && !path.isAbsolute(relative))) {
    throw new MediaError(`--to phải là thư mục ngoài repo (ví dụ ~/media-restore-test), không phải ${value}`);
  }
  return target;
}

export function isWsl(env = process.env) {
  if (env.WSL_DISTRO_NAME) return true;
  try { return /microsoft/i.test(readFileSync('/proc/version', 'utf8')); }
  catch { return false; }
}

async function remoteSizes(ctx, info, remoteBase, keys) {
  const dir = tempDir('media-size-');
  try {
    const listFile = path.join(dir, 'files.txt');
    writeFileSync(listFile, `${keys.join('\n')}\n`);
    const result = await runRclone(ctx, ['size', `${info.remote}:${remoteBase}`, '--files-from-raw', listFile, '--json', ...listingFlags(info)]);
    if (result.code !== 0) return null;
    return JSON.parse(result.stdout);
  } catch {
    return null;
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

/** Downloads into a staging folder (destBase), never into the repo itself. */
async function copyDown(ctx, info, remoteBase, destBase, keys) {
  const dir = tempDir('media-pull-');
  try {
    const listFile = path.join(dir, 'files.txt');
    writeFileSync(listFile, `${keys.join('\n')}\n`);
    mkdirSync(destBase, { recursive: true });
    const args = ['copy', `${info.remote}:${remoteBase}`, destBase, '--files-from-raw', listFile, '--ignore-existing',
      ...TRANSFER_FLAGS, ...listingFlags(info)];
    return (await runRclone(ctx, args, { capture: false })).code;
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

export async function pull(ctx, options) {
  const names = selectedSets(options);
  const target = options.to ? resolveTarget(ctx, options.to) : null;
  const destRoot = target ?? ctx.root;
  if (target && options['update-stale']) throw new MediaError('--update-stale chỉ dùng cho repo, không dùng với --to.');
  const gameSets = gameSetNames(names);
  const games = gameSets.length ? presentGames(ctx) : [];
  const info = await ensureRemote(ctx);

  const local = readLocks(withGame(ctx, null));
  const gameLocks = games.map((game) => ({ game, ...readGameLock(ctx, game) }));
  const copies = await fetchLockCopies(ctx, info, {
    latest: gameLocks.filter((item) => !item.entries).map((item) => lockCopyName(item.game)),
    all: names.includes('private') ? [PRIVATE_LOCK_COPY] : [],
  });
  for (const item of gameLocks) {
    if (item.entries) continue;
    item.entries = copies[lockCopyName(item.game)]?.at(-1)?.entries ?? null;
    if (item.entries) ctx.out.write(`Máy này chưa có ${item.label} (chưa git pull?): dùng bản sao mới nhất trên Drive.\n`);
    else ctx.out.write(`Chưa có ${item.label}: chưa ai đẩy originals/runtime lên Drive.\n`);
  }
  const privateVersions = copies[PRIVATE_LOCK_COPY] ?? [];
  const privateLock = privateVersions.at(-1)?.entries ?? local.privateLock;
  if (names.includes('private') && !target && privateVersions.length && !sameEntries(privateLock, local.privateLock ?? new Map())) {
    writeLockFile(local.privateLockFile, privateLock);
  }
  const privateHistory = mergeHistory(new Map(), local.privateLock);
  for (const version of privateVersions) mergeHistory(privateHistory, version.entries);

  // Every (lock, set) pair to restore: each game's sets, then the private set.
  const sources = gameLocks.map(({ game, entries }) => ({
    game, gameLock: entries, names: gameSets, history: lockHistory(path.join(ctx.root, game.dir), game.lock),
  }));
  if (names.includes('private')) sources.push({ game: null, gameLock: null, names: ['private'], history: privateHistory });

  // What each locked file looks like in the destination.
  const plan = [];
  for (const source of sources) for (const name of source.names) {
    const definition = setDefinitions(ctx.config, source.game)[name];
    const lock = lockForSet(ctx.config, definition, source.gameLock, privateLock);
    for (const [key, md5] of lock) {
      const rel = toRel(definition, key);
      const abs = path.join(destRoot, rel);
      const item = { name, definition, history: source.history, key, rel, abs, md5, state: 'missing' };
      if (existsSync(abs)) {
        const stats = statSync(abs);
        Object.assign(item, { size: stats.size, mtimeMs: stats.mtimeMs, cacheKey: target ? null : rel, md5: undefined, expected: md5 });
        item.state = 'present';
      } else {
        item.expected = md5;
      }
      plan.push(item);
    }
  }
  const present = plan.filter((item) => item.state === 'present');
  await hashEntries(present, target ? null : ctx.cache, { onSlow: ctx.onSlowHash });
  const stale = [];
  const edited = [];
  for (const item of present) {
    if (item.md5 === item.expected) { item.state = 'ok'; continue; }
    if (item.history.get(item.key)?.has(item.md5)) { item.state = 'stale'; stale.push(item); }
    else { item.state = 'edited'; edited.push(item); }
  }

  const stamp = runStamp(ctx.now?.() ?? new Date());
  if (stale.length && options['update-stale']) {
    const oldRoot = path.join(ctx.root, ctx.config.oldDir, stamp);
    for (const item of stale) {
      const destination = path.join(oldRoot, item.rel);
      mkdirSync(path.dirname(destination), { recursive: true });
      renameSync(item.abs, destination);
      item.state = 'missing';
    }
    ctx.out.write(`Đã chuyển ${fmtCount(stale.length)} file cũ vào ${ctx.config.oldDir}/${stamp}/ (không xoá), sẽ tải bản mới.\n`);
  } else if (stale.length) {
    printList(ctx, `${fmtCount(stale.length)} file ở máy này cũ hơn bản trên Drive (giữ nguyên). Lấy bản mới: pnpm media:pull --update-stale`, stale.map((item) => item.rel), { limit: 10 });
  }
  if (edited.length) {
    printList(ctx, `${fmtCount(edited.length)} file ở máy này khác danh sách và chưa từng lên Drive (giữ nguyên). Nếu là bản sửa: pnpm media:push`, edited.map((item) => item.rel), { limit: 10 });
  }

  const missing = plan.filter((item) => item.state === 'missing');
  const groups = new Map();
  for (const item of missing) {
    const key = item.definition.remoteBase;
    const group = groups.get(key) ?? { remoteBase: key, lockBase: item.definition.lockBase, items: [] };
    group.items.push(item);
    groups.set(key, group);
  }
  let failedCopy = false;
  const stagingRoot = path.join(destRoot, '.media-tmp', stamp);
  if (missing.length) {
    let bytes = 0;
    for (const group of groups.values()) {
      const size = await remoteSizes(ctx, info, group.remoteBase, group.items.map((item) => item.key));
      bytes += size?.bytes ?? 0;
    }
    ctx.out.write(`Đang tải ${fmtCount(missing.length)} file (${fmtBytes(bytes)}) từ Google Drive…\n`);
    for (const group of groups.values()) {
      const code = await copyDown(ctx, info, group.remoteBase, path.join(stagingRoot, group.lockBase), group.items.map((item) => item.key));
      if (code !== 0) failedCopy = true;
    }
  }

  // Verify what arrived in the staging folder; only matching files go into place.
  const staged = [];
  for (const item of missing) {
    const file = path.join(stagingRoot, item.rel);
    if (!existsSync(file)) continue;
    const stats = statSync(file);
    staged.push(Object.assign(item, { staged: file, abs: file, size: stats.size, mtimeMs: stats.mtimeMs, cacheKey: null, md5: undefined }));
  }
  await hashEntries(staged, null, { onSlow: ctx.onSlowHash });
  const placed = [];
  const bad = [];
  const occupied = [];
  const mismatchRoot = path.join(destRoot, ctx.config.oldDir, stamp, 'mismatch');
  for (const item of staged) {
    item.abs = path.join(destRoot, item.rel);
    if (item.md5 !== item.expected) {
      const destination = path.join(mismatchRoot, item.rel);
      mkdirSync(path.dirname(destination), { recursive: true });
      renameSync(item.staged, destination);
      bad.push(item);
    } else if (existsSync(item.abs)) {
      occupied.push(item); // appeared while downloading: never overwritten
    } else {
      mkdirSync(path.dirname(item.abs), { recursive: true });
      renameSync(item.staged, item.abs);
      if (!target) {
        const stats = statSync(item.abs);
        ctx.cache.set(item.rel, stats.size, stats.mtimeMs, { md5: item.md5, sha256: item.sha256 });
      }
      placed.push(item);
    }
  }
  if (!target) ctx.cache.save();
  rmSync(stagingRoot, { recursive: true, force: true });
  try { rmdirSync(path.dirname(stagingRoot)); } catch { /* other runs still staging, or not empty */ }
  const notArrived = missing.filter((item) => !item.staged);
  const okCount = plan.filter((item) => item.state === 'ok').length + placed.length;

  if (!target && placed.length) {
    ctx.out.write(`Đã tải ${fmtCount(placed.length)} file.\n`);
    const rebuilt = games.filter((game) => game.pulledStamp && placed.some((item) => item.rel.startsWith(`${game.dir}/`)));
    for (const game of rebuilt) {
      // Pulled files keep Drive's older modification times; this stamp makes ./play.sh rebuild.
      writeFileSync(path.join(ctx.root, game.dir, game.pulledStamp), `${new Date().toISOString()}\n`);
      ctx.out.write(`./play.sh sẽ build lại ${game.title ?? game.id}.\n`);
    }
    if (rebuilt.length && isWsl(ctx.env)) ctx.out.write('WSL: nếu Vite đang chạy, khởi động lại để thấy file mới trong public/.\n');
    if (placed.some((item) => item.rel.startsWith('shared/music/'))) {
      ctx.out.write('Nhạc mới: ./dev.sh và ./play.sh tự chạy pnpm music:index (hoặc chạy tay).\n');
    }
  }
  printList(ctx, `✗ ${fmtCount(bad.length)} file tải về khác md5 trong danh sách: không đặt vào chỗ, đã chuyển vào ${path.relative(destRoot, mismatchRoot)}/ để kiểm tra. Chạy pnpm media:check --remote.`,
    bad.map((item) => item.rel), { limit: 20 });
  printList(ctx, `✗ ${fmtCount(notArrived.length)} file không tải được (có thể chưa có trên Drive):`, notArrived.map((item) => item.rel), { limit: 20 });
  printList(ctx, `! ${fmtCount(occupied.length)} file vừa xuất hiện ở máy này trong lúc tải: giữ bản ở máy, bỏ bản tải về.`, occupied.map((item) => item.rel), { limit: 20 });
  const total = plan.length;
  ctx.out.write(`${target ? `Khôi phục vào ${target}: ` : ''}Khớp ${fmtCount(okCount)}/${fmtCount(total)} file trong danh sách md5.\n`);
  if (!missing.length && !stale.length && !edited.length) ctx.out.write('Không thiếu file nào.\n');
  return bad.length || notArrived.length || occupied.length || failedCopy ? 1 : 0;
}
