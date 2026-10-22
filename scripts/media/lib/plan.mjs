// Compares the files on disk with a lock. Pure functions, so the rules for
// stale copies and renames are unit-tested without a disk or a network.
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';

/**
 * local: Map(key -> entry with md5); lock: Map(key -> md5) of this set only;
 * history: Map(key -> Set(md5)) of every md5 the key ever had in the lock.
 * - added: on disk, not in the lock, and never in it with these bytes.
 * - removedElsewhere: on disk, not in the lock, but the lock once listed this
 *   path with exactly these bytes and then dropped it (a rename or --forget,
 *   here or on another machine). Never uploaded again, never a rename target,
 *   unless push gets --readd.
 * - changed: md5 differs and was never in the lock: a real edit on this machine.
 * - stale: md5 differs but matches an older lock entry: Drive has a newer copy.
 * - missing: in the lock, not on disk.
 * - renames: a missing entry whose md5 equals an added file.
 */
export function classify({ local, lock, history = new Map() }) {
  const result = { unchanged: [], added: [], removedElsewhere: [], changed: [], stale: [], missing: [], renames: [] };
  for (const [key, entry] of local) {
    const locked = lock.get(key);
    if (!locked) {
      if (history.get(key)?.has(entry.md5)) result.removedElsewhere.push(key);
      else result.added.push(key);
    } else if (locked === entry.md5) result.unchanged.push(key);
    else if (history.get(key)?.has(entry.md5)) result.stale.push(key);
    else result.changed.push(key);
  }
  for (const key of lock.keys()) if (!local.has(key)) result.missing.push(key);
  result.missing.sort();
  result.added.sort();
  result.removedElsewhere.sort();

  const addedByMd5 = new Map();
  for (const key of result.added) {
    const md5 = local.get(key).md5;
    if (!addedByMd5.has(md5)) addedByMd5.set(md5, []);
    addedByMd5.get(md5).push(key);
  }
  const renamedTo = new Set();
  const stillMissing = [];
  for (const key of result.missing) {
    const candidates = addedByMd5.get(lock.get(key));
    const target = candidates?.find((candidate) => !renamedTo.has(candidate));
    if (target) {
      renamedTo.add(target);
      result.renames.push({ from: key, to: target });
    } else {
      stillMissing.push(key);
    }
  }
  result.missing = stillMissing;
  result.added = result.added.filter((key) => !renamedTo.has(key));
  return result;
}

/**
 * Quota rule: refuse when Drive's free space is below the upload plus the reserve.
 * about: `rclone about --json` (null when it failed). status:
 * - ok / low: free is known (from `free`, else total - used - other);
 * - unlimited: rclone answered but Drive reports no limit (Workspace pooled or
 *   unlimited storage): nothing to compare, push goes on with a warning;
 * - unknown: rclone about failed: push refuses.
 * For Drive, rclone's `used` already includes the trash, so it is not subtracted twice.
 */
export function quotaCheck(about, uploadBytes, reserveBytes) {
  const need = uploadBytes + reserveBytes;
  if (!about || typeof about !== 'object') return { status: 'unknown', free: null, need };
  const number = (value) => (typeof value === 'number' && Number.isFinite(value) ? value : null);
  let free = number(about.free);
  if (free === null && number(about.total) !== null && number(about.used) !== null) {
    free = about.total - about.used - (number(about.other) ?? 0);
  }
  if (free === null) return { status: 'unlimited', free: null, need };
  return { status: free < need ? 'low' : 'ok', free, need };
}

function stripQuery(url) {
  return url.split('?')[0];
}

/**
 * Runtime files the game asks for (relative to the game folder), each with the
 * ?v= hash prefix it expects: models/manifest.json tiers and ships/3d model.json.
 */
export function runtimeReferences(gameRoot, gameConfig) {
  const references = [];
  const manifestFile = gameConfig.modelsManifest ? path.join(gameRoot, gameConfig.modelsManifest) : null;
  if (manifestFile && existsSync(manifestFile)) {
    const manifest = JSON.parse(readFileSync(manifestFile, 'utf8'));
    for (const [id, model] of Object.entries(manifest.models ?? {})) {
      for (const [tier, info] of Object.entries(model.tiers ?? {})) {
        if (typeof info?.url !== 'string' || !info.url.startsWith('/')) continue;
        const version = /[?&]v=([0-9a-f]+)/.exec(info.url)?.[1] ?? null;
        references.push({ key: `public${stripQuery(info.url)}`, version, from: `models/manifest.json ${id} ${tier}` });
      }
    }
  }
  const shipsDir = gameConfig.ships3dDir ? path.join(gameRoot, gameConfig.ships3dDir) : null;
  if (shipsDir && existsSync(shipsDir)) {
    for (const entry of readdirSync(shipsDir, { withFileTypes: true })) {
      const modelFile = path.join(shipsDir, entry.name, 'model.json');
      if (!entry.isDirectory() || !existsSync(modelFile)) continue;
      const model = JSON.parse(readFileSync(modelFile, 'utf8'));
      for (const field of ['color', 'emissive', 'height']) {
        if (typeof model[field] !== 'string') continue;
        const version = /[?&]v=([0-9a-f]+)/.exec(model[field])?.[1] ?? null;
        references.push({
          key: `${gameConfig.ships3dDir}/${entry.name}/${stripQuery(model[field])}`,
          version,
          from: `ships/3d/${entry.name}/model.json ${field}`,
        });
      }
    }
  }
  return references;
}

/** Lock entries in folders the manifests own; only these may be forgotten automatically. */
export function isManifestOwned(key, gameConfig) {
  return [gameConfig.modelsDir, gameConfig.ships3dDir].some((dir) => Boolean(dir) && key.startsWith(`${dir}/`));
}
