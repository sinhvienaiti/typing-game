// Local state shared by status, check and push: scanned sets, their hashes,
// the locks and the plan for each set.
import path from 'node:path';
import { lockHistory } from './git.mjs';
import { hashEntries } from './hash.mjs';
import { readLockFile } from './lock.mjs';
import { classify } from './plan.mjs';
import { assertLockKeys, gameLockSetOf, scanSets, setDefinitions } from './sets.mjs';

export function lockForSet(config, definition, gameLock, privateLock) {
  if (!definition.inGameLock) return new Map(privateLock ?? []);
  return new Map([...(gameLock ?? [])].filter(([key]) => gameLockSetOf(config, key) === definition.name));
}

export function readLocks(ctx) {
  const definitions = setDefinitions(ctx.config);
  const gameLockFile = path.join(ctx.root, definitions.originals.lockFile);
  const privateLockFile = path.join(ctx.root, definitions.private.lockFile);
  const gameLabel = `${ctx.config.game.dir}/${ctx.config.game.lock}`;
  return {
    gameLockFile,
    privateLockFile,
    gameLock: assertLockKeys(ctx.config, 'game', readLockFile(gameLockFile, gameLabel), gameLabel),
    privateLock: assertLockKeys(ctx.config, 'private', readLockFile(privateLockFile, definitions.private.lockFile), definitions.private.lockFile),
  };
}

/**
 * options.gameLock / options.privateLock replace the files on disk (push uses
 * Drive's private lock); options.privateHistory adds the Drive lock history.
 */
export async function loadState(ctx, names, options = {}) {
  const definitions = setDefinitions(ctx.config);
  const locks = readLocks(ctx);
  const gameLock = options.gameLock ?? locks.gameLock;
  const { sets, notes } = await scanSets(ctx, names, { gameLock });
  await hashEntries(Object.values(sets).flat(), ctx.cache, { onSlow: ctx.onSlowHash });
  const privateLock = options.privateLock ?? locks.privateLock;
  const gameHistory = lockHistory(path.join(ctx.root, ctx.config.game.dir), ctx.config.game.lock);
  const privateHistory = options.privateHistory ?? new Map();
  const perSet = {};
  for (const name of names) {
    const definition = definitions[name];
    const local = new Map(sets[name].map((entry) => [entry.key, entry]));
    const lock = lockForSet(ctx.config, definition, gameLock, privateLock);
    const history = definition.inGameLock ? gameHistory : privateHistory;
    perSet[name] = { definition, local, lock, history, plan: classify({ local, lock, history }) };
  }
  return {
    definitions,
    sets,
    notes,
    perSet,
    gameLock: gameLock ?? new Map(),
    privateLock: privateLock ?? new Map(),
    gameLockExists: Boolean(gameLock),
    privateLockExists: Boolean(privateLock),
    gameLockFile: locks.gameLockFile,
    privateLockFile: locks.privateLockFile,
  };
}

export function selectedSets(options) {
  return options.only?.length ? options.only : ['originals', 'runtime', 'private'];
}
