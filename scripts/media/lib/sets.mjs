// Builds the three media sets by walking the disk and subtracting
// `git ls-files`. .gitignore plays no part: an ignored, untracked runtime GLB
// is still media that only exists on this machine.
import { existsSync, readFileSync } from 'node:fs';
import { lstat, readdir } from 'node:fs/promises';
import path from 'node:path';
import { matchesAny } from './glob.mjs';
import { trackedFiles } from './git.mjs';
import { hashEntries } from './hash.mjs';
import { isSafeRelativePath, LockError, readLockFile } from './lock.mjs';

export const CONFIG_FILE = 'media/media.config.json';

export function loadConfig(root) {
  const file = path.join(root, CONFIG_FILE);
  const config = JSON.parse(readFileSync(file, 'utf8'));
  if (config.version !== 1) throw new Error(`${CONFIG_FILE}: version không hỗ trợ`);
  return config;
}

/** Where each set lives: its lock, the base its lock paths are relative to, and its Drive folder. */
export function setDefinitions(config) {
  const game = config.game.dir;
  const gameLock = `${game}/${config.game.lock}`;
  return {
    originals: { name: 'originals', lockFile: gameLock, lockBase: game, remoteBase: `repo/${game}`, backup: true, confirmReplace: true, inGameLock: true },
    runtime: { name: 'runtime', lockFile: gameLock, lockBase: game, remoteBase: `repo/${game}`, backup: false, confirmReplace: false, inGameLock: true },
    private: { name: 'private', lockFile: config.privateLock, lockBase: '', remoteBase: 'private', backup: true, confirmReplace: true, inGameLock: false },
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

export function readSources(root, config) {
  const file = path.join(root, config.game.dir, config.game.sources);
  if (!existsSync(file)) return { files: {}, noOriginalOnThisMachine: {} };
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
  const definitions = setDefinitions(config);
  const game = config.game.dir;
  const gameAbs = path.join(root, game);
  const notes = { rawDuplicates: [], rawKept: [], modelsKept: [], lostOriginals: [], unsafe: [] };
  const sets = Object.fromEntries(names.map((name) => [name, []]));
  if (!existsSync(gameAbs)) throw new Error(`Không thấy ${game}. Chạy: git submodule update --init ${game}`);

  const tracked = new Set(trackedFiles(root));
  for (const file of trackedFiles(gameAbs)) tracked.add(`${game}/${file}`);
  const junk = (rel) => matchesAny(path.posix.basename(rel), config.junk);
  const walkOptions = { isJunk: junk, onUnsafe: (rel) => notes.unsafe.push(rel) };
  const privateRoots = config.sets.private.roots;
  const isPrivate = (rel) => privateRoots.some((folder) => under(rel, folder));
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
      const sources = readSources(root, config);
      const listedMd5 = new Set(Object.values(sources.files).map((item) => item.md5));
      const twinPrefix = `${artRoot}/3d/`;
      const listedBytes = new Set(Object.values(sources.files).map((item) => item.bytes));
      const raw = await Promise.all(rawCandidates.map((rel) => statEntry(root, rel)));
      const sizedLikeListed = raw.filter((entry) => listedBytes.has(entry.size));
      const rawSizes = new Set(sizedLikeListed.map((entry) => entry.size));
      const localTwins = sets.originals.filter((entry) => entry.key.startsWith(twinPrefix) && rawSizes.has(entry.size));
      await hashEntries([...sizedLikeListed, ...localTwins], ctx.cache, { onSlow: ctx.onSlowHash });
      const twinMd5 = new Set(localTwins.map((entry) => entry.md5));
      const gameLock = options.gameLock !== undefined ? options.gameLock : readGameLock(root, config);
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
    const modelsDir = `${game}/${config.game.modelsDir}`;
    const seen = new Set(sets.runtime.map((entry) => entry.rel));
    for (const id of lostOriginalIds(readSources(root, config))) {
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

function readGameLock(root, config) {
  return readLockFile(path.join(root, config.game.dir, config.game.lock), `${config.game.dir}/${config.game.lock}`);
}

/**
 * Why a lock line may not be used, or null. Locks come from a public repo and
 * from Drive: each key must stay inside its own set, so a pull can never write
 * to .git, scripts or any other non-media path. kind: 'game' or 'private'.
 */
export function lockKeyProblem(config, kind, key) {
  const parts = key.split('/');
  if (parts.includes('.git')) return 'thư mục .git';
  const privateRoots = config.sets.private.roots;
  if (kind === 'private') return privateRoots.some((folder) => under(key, folder)) ? null : 'ngoài các thư mục private';
  if (privateRoots.some((folder) => under(`${config.game.dir}/${key}`, folder))) return 'thuộc nhóm private';
  if (gameLockSetOf(config, key) === 'originals') return null;
  const extensions = new Set(config.mediaExtensions.map((ext) => `.${ext.toLowerCase()}`));
  if (!extensions.has(path.posix.extname(key).toLowerCase())) return 'không phải file media';
  for (let index = 1; index < parts.length; index += 1) {
    if (matchesAny(parts.slice(0, index).join('/'), config.sets.runtime.skipDirs)) return 'thư mục không thuộc runtime';
  }
  return null;
}

/** Throws a LockError naming the lines that fall outside their set. */
export function assertLockKeys(config, kind, entries, label) {
  if (!entries) return entries;
  const bad = [];
  for (const key of entries.keys()) {
    const problem = lockKeyProblem(config, kind, key);
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
