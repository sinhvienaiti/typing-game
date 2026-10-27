// Builds the media sets by walking the disk and subtracting `git ls-files`:
// originals and runtime per game (games[] in media.config.json, each with its
// own lock and Drive folder), private shared. .gitignore plays no part: an
// ignored, untracked runtime GLB is still media that only exists on this machine.
import { existsSync, readFileSync } from 'node:fs';
import { lstat, readdir } from 'node:fs/promises';
import path from 'node:path';
import { matchesAny } from './glob.mjs';
import { trackedFiles } from './git.mjs';
import { hashEntries } from './hash.mjs';
import { isSafeRelativePath, LockError, readLockFile } from './lock.mjs';

export const CONFIG_FILE = 'media/media.config.json';

const GAME_ID = /^[a-z0-9][a-z0-9-]*$/;

/**
 * games[]: one entry per game repo, each with its own lock and Drive folder
 * (repo/<dir>). A config with the older single `game` block still loads.
 */
function normalizeGames(config) {
  const list = Array.isArray(config.games) ? config.games : config.game ? [config.game] : [];
  if (!list.length) throw new Error(`${CONFIG_FILE}: cần mảng games[]`);
  const ids = new Set();
  const dirs = new Set();
  return list.map((entry, index) => {
    const id = entry?.id ?? path.posix.basename(entry?.dir ?? '');
    const where = `${CONFIG_FILE}: games[${index}]`;
    if (!GAME_ID.test(id)) throw new Error(`${where}: id không hợp lệ (${id})`);
    if (!isSafeRelativePath(entry.dir ?? '')) throw new Error(`${where}: dir không hợp lệ`);
    if (!isSafeRelativePath(entry.lock ?? '')) throw new Error(`${where}: lock không hợp lệ`);
    if (ids.has(id) || dirs.has(entry.dir)) throw new Error(`${where}: trùng id hoặc dir (${id})`);
    ids.add(id);
    dirs.add(entry.dir);
    return { ...entry, id };
  });
}

export function loadConfig(root) {
  const file = path.join(root, CONFIG_FILE);
  const config = JSON.parse(readFileSync(file, 'utf8'));
  if (config.version !== 1) throw new Error(`${CONFIG_FILE}: version không hỗ trợ`);
  config.games = normalizeGames(config);
  delete config.game;
  return config;
}

/** The game entry for an id (or the entry itself). */
export function findGame(config, game) {
  if (game && typeof game === 'object') return game;
  const found = config.games.find((entry) => entry.id === game);
  if (!found) throw new Error(`Không có game ${game} trong ${CONFIG_FILE}`);
  return found;
}

/** A copy of ctx that works on one game (null: the private set only). */
export function withGame(ctx, game) {
  return { ...ctx, game: game === null ? null : findGame(ctx.config, game) };
}

/** Name of a game's lock copy in Drive's _locks/<stamp>/ (Space: space-typing.media.md5). */
export function lockCopyName(game) {
  return `${game.id}.media.md5`;
}

/**
 * Games whose folder exists on this machine. A missing folder (game not
 * created yet, submodule not checked out) is skipped with a notice, once per run.
 */
export function presentGames(ctx) {
  // Shared by every withGame() copy of ctx, so the notice prints once.
  ctx.present ??= {};
  if (ctx.present.games) return ctx.present.games;
  const games = [];
  for (const game of ctx.config.games) {
    if (existsSync(path.join(ctx.root, game.dir))) { games.push(game); continue; }
    ctx.out.write(`Bỏ qua ${game.dir}: chưa có thư mục này trên máy (game chưa tạo, hoặc chạy git submodule update --init ${game.dir}).\n`);
  }
  ctx.present.games = games;
  return games;
}

/**
 * Where each set lives: its lock, the base its lock paths are relative to, and
 * its Drive folder. originals and runtime belong to one game; private is shared.
 */
export function setDefinitions(config, game = null) {
  const definitions = {
    private: { name: 'private', game: null, lockFile: config.privateLock, lockBase: '', remoteBase: 'private', backup: true, confirmReplace: true, inGameLock: false },
  };
  if (!game) return definitions;
  const dir = game.dir;
  const gameLock = `${dir}/${game.lock}`;
  return {
    originals: { name: 'originals', game, lockFile: gameLock, lockBase: dir, remoteBase: `repo/${dir}`, backup: true, confirmReplace: true, inGameLock: true },
    runtime: { name: 'runtime', game, lockFile: gameLock, lockBase: dir, remoteBase: `repo/${dir}`, backup: false, confirmReplace: false, inGameLock: true },
    ...definitions,
  };
}

/** Which set a line of the game lock belongs to (its paths are relative to the game folder). */
export function gameLockSetOf(config, key) {
  return key === config.sets.originals.root || key.startsWith(`${config.sets.originals.root}/`) ? 'originals' : 'runtime';
}

export function toKey(definition, rel) {
  return definition.lockBase ? rel.slice(definition.lockBase.length + 1) : rel;
}

export function toRel(definition, key) {
  return definition.lockBase ? `${definition.lockBase}/${key}` : key;
}

function under(rel, folder) {
  return rel === folder || rel.startsWith(`${folder}/`);
}

async function walk(root, startRel, { skipDir, isJunk, onUnsafe }) {
  const files = [];
  const visit = async (rel) => {
    let entries;
    try { entries = await readdir(path.join(root, rel), { withFileTypes: true }); }
    catch (error) {
      if (error.code === 'ENOENT' || error.code === 'ENOTDIR') return;
      throw error;
    }
    for (const entry of entries) {
      const childRel = `${rel}/${entry.name}`;
      // Junk first: a WSL `x.png:Zone.Identifier` is skipped quietly, not reported as unsafe.
      if (entry.isFile() && isJunk?.(childRel)) continue;
      if (!isSafeRelativePath(childRel)) { onUnsafe?.(childRel); continue; }
      if (entry.isSymbolicLink()) continue;
      if (entry.isDirectory()) {
        if (!skipDir?.(childRel)) await visit(childRel);
      } else if (entry.isFile()) {
        files.push(childRel);
      }
    }
  };
  await visit(startRel);
  return files;
}

async function statEntry(root, rel) {
  const stats = await lstat(path.join(root, rel));
  return { rel, abs: path.join(root, rel), size: stats.size, mtimeMs: stats.mtimeMs, cacheKey: rel };
}

export function readSources(root, game) {
  const file = game.sources ? path.join(root, game.dir, game.sources) : null;
  if (!file || !existsSync(file)) return { files: {}, noOriginalOnThisMachine: {} };
  const data = JSON.parse(readFileSync(file, 'utf8'));
  return { files: data.files ?? {}, noOriginalOnThisMachine: data.noOriginalOnThisMachine ?? {} };
}

/** Model ids ("heroes/draconis") whose originals are lost, from SOURCES.json. */
export function lostOriginalIds(sources) {
  return Object.keys(sources.noOriginalOnThisMachine)
    .flatMap((key) => key.split(','))
    .map((id) => id.trim())
    .filter((id) => /^[a-z0-9-]+\/[a-z0-9-]+$/.test(id));
}

/**
 * Scans the requested sets. Returns { sets: { name: entry[] }, notes }.
 * Entries: { set, rel (repo path), key (lock path), abs, size, mtimeMs }.
 * models/raw files are hashed here, to drop only exact copies of art-src/3d.
 * options.gameLock: the game lock to look for art-src/3d twins in (default: the file).
 */
export async function scanSets(ctx, names, options = {}) {
  const { root, config } = ctx;
  const gameEntry = ctx.game ?? null;
  const definitions = setDefinitions(config, gameEntry);
  const game = gameEntry?.dir;
  const notes = { rawDuplicates: [], rawKept: [], modelsKept: [], lostOriginals: [], unsafe: [] };
  const sets = Object.fromEntries(names.map((name) => [name, []]));
  const gameNames = names.filter((name) => name !== 'private');
  if (gameNames.length && !gameEntry) throw new Error(`Nhóm ${gameNames.join(', ')} cần biết game nào (ctx.game).`);
  if (gameEntry && !existsSync(path.join(root, game))) throw new Error(`Không thấy ${game}. Chạy: git submodule update --init ${game}`);

  const privateRoots = config.sets.private.roots;
  const isPrivate = (rel) => privateRoots.some((folder) => under(rel, folder));
  // Git's own list, from the parent and from each game repo the scan reads.
  const tracked = new Set(trackedFiles(root));
  const repos = new Set(gameEntry ? [gameEntry] : []);
  if (names.includes('private')) {
    for (const other of presentGames(ctx)) if (privateRoots.some((folder) => under(folder, other.dir))) repos.add(other);
  }
  for (const repo of repos) for (const file of trackedFiles(path.join(root, repo.dir))) tracked.add(`${repo.dir}/${file}`);
  const junk = (rel) => matchesAny(path.posix.basename(rel), config.junk);
  const walkOptions = { isJunk: junk, onUnsafe: (rel) => notes.unsafe.push(rel) };
  const add = async (name, rel) => {
    const entry = await statEntry(root, rel);
    entry.set = name;
    entry.key = toKey(definitions[name], rel);
    sets[name].push(entry);
    return entry;
  };

  if (names.includes('originals')) {
    const { root: artRoot, exclude, duplicateOf3d } = config.sets.originals;
    const base = `${game}/${artRoot}`;
    const rawCandidates = [];
    for (const rel of await walk(root, base, { ...walkOptions, skipDir: isPrivate })) {
      const inner = rel.slice(base.length + 1);
      if (junk(rel) || tracked.has(rel) || isPrivate(rel) || matchesAny(inner, exclude)) continue;
      if (duplicateOf3d && under(inner, duplicateOf3d)) { rawCandidates.push(rel); continue; }
      const entry = await add('originals', rel);
      if (inner.startsWith('models/')) notes.modelsKept.push(entry);
    }
    if (rawCandidates.length) {
      // A models/raw file is dropped only when its bytes are listed in SOURCES.json AND a
      // twin under art-src/3d is backed up: on this machine (pushed with originals) or
      // already in the game lock (verified on Drive). Otherwise it is kept and listed.
      const sources = readSources(root, gameEntry);
      const listedMd5 = new Set(Object.values(sources.files).map((item) => item.md5));
      const twinPrefix = `${artRoot}/3d/`;
      const listedBytes = new Set(Object.values(sources.files).map((item) => item.bytes));
      const raw = await Promise.all(rawCandidates.map((rel) => statEntry(root, rel)));
      const sizedLikeListed = raw.filter((entry) => listedBytes.has(entry.size));
      const rawSizes = new Set(sizedLikeListed.map((entry) => entry.size));
      const localTwins = sets.originals.filter((entry) => entry.key.startsWith(twinPrefix) && rawSizes.has(entry.size));
      await hashEntries([...sizedLikeListed, ...localTwins], ctx.cache, { onSlow: ctx.onSlowHash });
      const twinMd5 = new Set(localTwins.map((entry) => entry.md5));
      const gameLock = options.gameLock !== undefined ? options.gameLock : readGameLock(root, gameEntry);
      for (const [key, md5] of gameLock ?? []) if (key.startsWith(twinPrefix)) twinMd5.add(md5);
      for (const entry of raw) {
        if (listedMd5.has(entry.md5) && twinMd5.has(entry.md5)) { notes.rawDuplicates.push(entry); continue; }
        entry.set = 'originals';
        entry.key = toKey(definitions.originals, entry.rel);
        sets.originals.push(entry);
        notes.rawKept.push(entry);
        notes.modelsKept.push(entry);
      }
    }
  }

  if (names.includes('runtime')) {
    const { skipDirs } = config.sets.runtime;
    const extensions = new Set(config.mediaExtensions.map((ext) => `.${ext.toLowerCase()}`));
    const skipDir = (rel) => isPrivate(rel) || matchesAny(rel.slice(game.length + 1), skipDirs);
    for (const rel of await walk(root, game, { ...walkOptions, skipDir })) {
      if (!extensions.has(path.posix.extname(rel).toLowerCase())) continue;
      if (junk(rel) || tracked.has(rel) || isPrivate(rel)) continue;
      await add('runtime', rel);
    }
    // Tracked runtime copies whose originals are lost: Git is their only other copy.
    const modelsDir = gameEntry.modelsDir ? `${game}/${gameEntry.modelsDir}` : null;
    const seen = new Set(sets.runtime.map((item) => item.rel));
    for (const id of modelsDir ? lostOriginalIds(readSources(root, gameEntry)) : []) {
      const folder = `${modelsDir}/${id}`;
      const inFolder = (file) => file.startsWith(`${folder}/`) && extensions.has(path.posix.extname(file).toLowerCase());
      for (const rel of [...tracked].filter(inFolder).sort()) {
        if (seen.has(rel) || !existsSync(path.join(root, rel))) continue;
        seen.add(rel);
        notes.lostOriginals.push(await add('runtime', rel));
      }
    }
  }

  if (names.includes('private')) {
    const { exclude } = config.sets.private;
    for (const folder of privateRoots) {
      for (const rel of await walk(root, folder, walkOptions)) {
        if (junk(rel) || tracked.has(rel) || exclude.includes(rel)) continue;
        await add('private', rel);
      }
    }
  }

  for (const name of names) sets[name].sort((left, right) => (left.key < right.key ? -1 : left.key > right.key ? 1 : 0));
  return { sets, notes };
}

function readGameLock(root, game) {
  return readLockFile(path.join(root, game.dir, game.lock), `${game.dir}/${game.lock}`);
}

/**
 * Why a lock line may not be used, or null. Locks come from a public repo and
 * from Drive: each key must stay inside its own set, so a pull can never write
 * to .git, scripts or any other non-media path. kind: 'game' (keys relative
 * to that game's folder) or 'private'.
 */
export function lockKeyProblem(config, kind, key, game = null) {
  const parts = key.split('/');
  if (parts.includes('.git')) return 'thư mục .git';
  const privateRoots = config.sets.private.roots;
  if (kind === 'private') return privateRoots.some((folder) => under(key, folder)) ? null : 'ngoài các thư mục private';
  if (!game) throw new Error('lockKeyProblem: danh sách của game cần biết game nào');
  if (privateRoots.some((folder) => under(`${game.dir}/${key}`, folder))) return 'thuộc nhóm private';
  if (gameLockSetOf(config, key) === 'originals') return null;
  const extensions = new Set(config.mediaExtensions.map((ext) => `.${ext.toLowerCase()}`));
  if (!extensions.has(path.posix.extname(key).toLowerCase())) return 'không phải file media';
  for (let index = 1; index < parts.length; index += 1) {
    if (matchesAny(parts.slice(0, index).join('/'), config.sets.runtime.skipDirs)) return 'thư mục không thuộc runtime';
  }
  return null;
}

/** Throws a LockError naming the lines that fall outside their set. */
export function assertLockKeys(config, kind, entries, label, game = null) {
  if (!entries) return entries;
  const bad = [];
  for (const key of entries.keys()) {
    const problem = lockKeyProblem(config, kind, key, game);
    if (problem) bad.push(`${key} (${problem})`);
  }
  if (bad.length) {
    throw new LockError(`${label}: ${bad.length} dòng nằm ngoài nhóm của nó, không dùng danh sách này:\n    ${bad.slice(0, 10).join('\n    ')}`);
  }
  return entries;
}

/** Folder summary for the dry run: "art-src/3d/enemies  114 file  1,2 GB". */
export function folderSummary(entries, depth = 3) {
  const groups = new Map();
  for (const entry of entries) {
    const parts = entry.key.split('/');
    const folder = parts.slice(0, Math.min(depth, parts.length - 1)).join('/') || '.';
    const group = groups.get(folder) ?? { folder, count: 0, bytes: 0 };
    group.count += 1;
    group.bytes += entry.size;
    groups.set(folder, group);
  }
  return [...groups.values()].sort((left, right) => (left.folder < right.folder ? -1 : 1));
}
