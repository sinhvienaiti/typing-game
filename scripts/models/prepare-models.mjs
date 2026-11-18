#!/usr/bin/env node
/**
 * pnpm models:prepare [--root <game>] [--out <dir>] [--url-base <path>] [--art-src <dir>]
 *                     [--only <kind>/<id>[,…]] [--force] [--contracts <file>]
 *                     [--manifest-only] [--import <manifest.json> --only <keys> [--tiers high,medium]]
 *                     [--generated-at <ISO time>]
 *
 * Copy of games/space-typing/scripts/models/prepare-models.ts for any game.
 * With no flags it does exactly what Space's script does:
 *   <art-src>/models/<kind>/<id>.glb (+ <art-src>/3d/bosses/tyrant-g01.glb, packaged as authored)
 * →
 *   <out>/<kind>/<id>/<id>.{high,medium}.glb and <out>/manifest.json,
 *   URLs <url-base>/<kind>/<id>/<id>.<tier>.glb?v=<sha256 prefix>.
 *
 * Each tier: dedup, prune, weld, resample animation, textures resized to the
 * tier's limit and re-encoded as WebP, geometry quantized and compressed with
 * meshopt. The Medium tier is simplified when the model is over its triangle
 * budget. Validation follows the game's model contracts (src/render3d/
 * model-contracts.ts or src/kit/three/model-contracts.ts); a model missing a
 * required socket or clip is reported and skipped unless --force.
 *
 * --manifest-only: no packaging; re-hash every listed tier and rewrite the manifest.
 * --import: copy packaged tiers listed in another game's manifest (Draconis
 *   for Dragonhold), rewriting their URLs to --url-base. No Blender, no contracts.
 * --generated-at: fixed manifest time, for reproducible output and comparisons.
 */
import { createHash } from 'node:crypto';
import { existsSync } from 'node:fs';
import { mkdir, readdir, readFile, rename, stat, writeFile } from 'node:fs/promises';
import { basename, dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  displayPath, importDependency, inferUrlBase, loadContracts, parseFlags, relativeToBase, resolveGame, tierUrl, UsageError,
} from './lib/options.mjs';

const TIERS = ['high', 'medium'];

export const FLAGS = {
  only: 'list', force: 'boolean', contracts: 'string', 'manifest-only': 'boolean', import: 'string', tiers: 'list', 'generated-at': 'string',
};

const sha = (bytes) => createHash('sha256').update(bytes).digest('hex').slice(0, 10);

export function modelKey(kind, id) {
  return kind + '/' + id;
}

/** Turns parsed flags into prepareModels options (paths resolved, modes checked). */
export function modelOptions(flags, cwd = process.cwd()) {
  const game = resolveGame(flags, cwd);
  const only = flags.only ?? [];
  if (flags['manifest-only'] && flags.import) throw new UsageError('--manifest-only and --import do not go together');
  if (flags.import && !only.length) throw new UsageError('--import needs --only <kind>/<id>[,…]');
  if (flags.tiers && !flags.import) throw new UsageError('--tiers only goes with --import');
  for (const tier of flags.tiers ?? []) if (!TIERS.includes(tier)) throw new UsageError(`--tiers: ${tier} (use ${TIERS.join(', ')})`);
  if (flags['generated-at'] !== undefined && Number.isNaN(Date.parse(flags['generated-at']))) throw new UsageError('--generated-at needs an ISO time');
  for (const key of only) if (!/^[a-z0-9-]+\/[a-z0-9][a-z0-9-]*$/.test(key)) throw new UsageError(`--only: ${key} is not <kind>/<id>`);
  return {
    ...game,
    only,
    force: Boolean(flags.force),
    contracts: flags.contracts ? resolve(cwd, flags.contracts) : undefined,
    manifestOnly: Boolean(flags['manifest-only']),
    importFrom: flags.import ? resolve(cwd, flags.import) : undefined,
    tiers: flags.tiers,
    generatedAt: flags['generated-at'],
  };
}

export async function findSources(artSrc, kinds, only = []) {
  const found = new Map();
  for (const legacy of [{ kind: 'bosses', id: 'tyrant-g01', path: join(artSrc, '3d/bosses/tyrant-g01.glb') }]) {
    if (kinds.includes(legacy.kind) && existsSync(legacy.path)) found.set(modelKey(legacy.kind, legacy.id), legacy);
  }
  for (const kind of kinds) {
    const dir = join(artSrc, 'models', kind);
    if (!existsSync(dir)) continue;
    for (const file of await readdir(dir)) {
      if (!file.toLowerCase().endsWith('.glb')) continue;
      const id = basename(file, '.glb').toLowerCase();
      if (!/^[a-z0-9][a-z0-9-]*$/.test(id)) {
        console.warn('skip ' + kind + '/' + file + ': use lower-case letters, digits and dashes');
        continue;
      }
      found.set(modelKey(kind, id), { kind, id, path: join(dir, file) });
    }
  }
  return [...found.values()].filter((source) => only.length === 0 || only.includes(modelKey(source.kind, source.id)));
}

export function countTriangles(document) {
  let total = 0;
  for (const mesh of document.getRoot().listMeshes()) {
    for (const primitive of mesh.listPrimitives()) {
      const indices = primitive.getIndices();
      const position = primitive.getAttribute('POSITION');
      if (primitive.getMode() !== 4) continue; // TRIANGLES only
      total += Math.floor((indices?.getCount() ?? position?.getCount() ?? 0) / 3);
    }
  }
  return total;
}

function socketNames(document) {
  return document.getRoot().listNodes().map((node) => node.getName()).filter((name) => name.startsWith('FX_'));
}

function clipNames(document) {
  return document.getRoot().listAnimations().map((animation) => animation.getName());
}

export function validationProblems(contracts, kind, document) {
  const contract = contracts.MODEL_CONTRACTS[kind];
  const triangles = countTriangles(document);
  return [
    ...contracts.missingSockets(contract, socketNames(document)).map((name) => 'missing socket ' + name),
    ...contracts.missingClips(contract, clipNames(document)).map((name) => 'missing clip containing ' + name),
    ...(triangles < contract.triangles.min ? ['only ' + triangles + ' triangles (min ' + contract.triangles.min + ')'] : []),
  ];
}

export async function previousManifest(outDir) {
  let text;
  try {
    text = await readFile(join(outDir, 'manifest.json'), 'utf8');
  } catch (error) {
    if (error.code === 'ENOENT') return { version: 1, generatedAt: '', models: {} };
    throw error;
  }
  try {
    const raw = JSON.parse(text);
    if (raw.version === 1 && raw.models !== null && typeof raw.models === 'object' && !Array.isArray(raw.models)) return raw;
  } catch { /* Report the corrupt existing file without replacing it. */ }
  throw new Error('Existing model manifest is invalid; restore or repair ' + join(outDir, 'manifest.json') + ' before preparing models');
}

async function writeAtomic(path, value) {
  await mkdir(dirname(path), { recursive: true });
  const temporary = path + '.tmp-' + process.pid;
  await writeFile(temporary, value);
  await rename(temporary, path);
}

/**
 * Copies packaged tiers listed in another manifest into outDir and records them
 * under urlBase. The source base is read from each URL, so any game's manifest works.
 */
export async function importModels({ importFrom, only, tiers, outDir, urlBase, manifest, log = console.log }) {
  const source = JSON.parse(await readFile(importFrom, 'utf8'));
  const sourceDir = dirname(importFrom);
  for (const key of only) {
    const entry = source.models?.[key];
    if (!entry) throw new Error(key + ' is not in ' + importFrom);
    const copy = { ...structuredClone(entry), tiers: {} };
    for (const tier of tiers ?? Object.keys(entry.tiers ?? {})) {
      const info = entry.tiers?.[tier];
      if (!info) throw new Error(key + ' has no ' + tier + ' tier in ' + importFrom);
      const rel = relativeToBase(info.url, inferUrlBase(info.url));
      const bytes = await readFile(join(sourceDir, rel));
      const hash = sha(bytes);
      const expected = /[?&]v=([0-9a-f]+)/.exec(info.url)?.[1];
      if (expected && !hash.startsWith(expected)) log('  WARN ' + key + ' ' + tier + ': file differs from its manifest ?v=' + expected);
      await writeAtomic(join(outDir, rel), bytes);
      copy.tiers[tier] = { url: urlBase + '/' + rel + '?v=' + hash, bytes: bytes.byteLength };
      log('  ' + tier.padEnd(6) + ' ← ' + rel + ' (' + (bytes.byteLength / 1048576).toFixed(2) + ' MB)');
    }
    manifest.models[key] = copy;
    log('import ' + key + ' → ' + urlBase + '/');
  }
}

async function packageSources({ root, artSrc, outDir, urlBase, only, force, contracts: contractsFile, manifest }) {
  const contracts = await loadContracts(root, contractsFile);
  const kinds = Object.keys(contracts.MODEL_CONTRACTS);
  const sources = await findSources(artSrc, kinds, only);
  if (sources.length === 0) {
    console.log('No model sources. Put Blender exports in ' + relative(root, join(artSrc, 'models')) + '/<kind>/<id>.glb (kinds: ' + kinds.join(', ') + ').');
    return null;
  }
  const { NodeIO } = await importDependency('@gltf-transform/core', root);
  const { ALL_EXTENSIONS } = await importDependency('@gltf-transform/extensions', root);
  const { cloneDocument, dedup, getBounds, meshopt, prune, resample, simplify, textureCompress, weld } = await importDependency('@gltf-transform/functions', root);
  const { MeshoptDecoder, MeshoptEncoder, MeshoptSimplifier } = await importDependency('meshoptimizer', root);
  const sharp = (await importDependency('sharp', root)).default;
  await MeshoptDecoder.ready;
  await MeshoptEncoder.ready;
  await MeshoptSimplifier.ready;
  const io = new NodeIO()
    .registerExtensions(ALL_EXTENSIONS)
    .registerDependencies({ 'meshopt.decoder': MeshoptDecoder, 'meshopt.encoder': MeshoptEncoder });

  let failures = 0;
  for (const source of sources) {
    const key = modelKey(source.kind, source.id);
    try {
      const contract = contracts.MODEL_CONTRACTS[source.kind];
      const document = await io.read(source.path);
      const triangles = countTriangles(document);
      const sockets = socketNames(document);
      const clips = clipNames(document);
      const problems = validationProblems(contracts, source.kind, document);
      const notes = triangles > contract.triangles.max
        ? ['' + triangles + ' triangles (budget ' + contract.triangles.max + '); Medium tier will be simplified']
        : [];
      const sourceBytes = (await stat(source.path)).size;
      console.log('\n' + key + '  ←  ' + source.path.replace(root + '/', ''));
      console.log('  ' + triangles.toLocaleString() + ' tris · ' + (sourceBytes / 1048576).toFixed(2) + ' MB · sockets: ' + (sockets.join(', ') || 'none') + ' · clips: ' + (clips.join(', ') || 'none'));
      for (const note of notes) console.log('  note: ' + note);
      if (problems.length > 0) {
        for (const problem of problems) console.log('  ERROR: ' + problem);
        if (!force) {
          failures += 1;
          console.log('  skipped (fix the export, or rerun with --force)');
          continue;
        }
      }

      // Sockets are empty leaf nodes: pruning must keep them.
      const keep = prune({ keepLeaves: true, keepExtras: true });
      await document.transform(dedup(), keep, weld(), resample());
      const bounds = getBounds(document.getRoot().listScenes()[0]);
      const size = [0, 1, 2].map((axis) => Number((bounds.max[axis] - bounds.min[axis]).toFixed(4)));

      const entry = { kind: source.kind, id: source.id, tiers: {}, triangles, sockets, clips, size };
      const pending = [];
      for (const tier of TIERS) {
        const copy = cloneDocument(document);
        const limit = contract.textureMax[tier];
        const steps = [
          textureCompress({ encoder: sharp, targetFormat: 'webp', resize: [limit, limit], quality: tier === 'high' ? 90 : 84 }),
        ];
        if (tier === 'medium' && triangles > contract.triangles.max) {
          steps.push(simplify({ simplifier: MeshoptSimplifier, ratio: contract.triangles.max / triangles, error: 0.002 }));
        }
        steps.push(meshopt({ encoder: MeshoptEncoder, level: 'medium', cleanup: false }), prune({ keepLeaves: true, keepExtras: true }));
        await copy.transform(...steps);
        const kept = socketNames(copy);
        const lost = sockets.filter((name) => !kept.includes(name));
        if (lost.length > 0) throw new Error(key + ' ' + tier + ': optimisation removed sockets ' + lost.join(', '));
        const bytes = await io.writeBinary(copy);
        pending.push({ file: join(outDir, source.kind, source.id, source.id + '.' + tier + '.glb'), bytes });
        entry.tiers[tier] = { url: tierUrl(urlBase, source.kind, source.id, tier, sha(bytes)), bytes: bytes.byteLength };
        console.log('  ' + tier.padEnd(6) + ' → ' + (bytes.byteLength / 1048576).toFixed(2) + ' MB (textures ≤ ' + limit + ' px)');
      }
      // Finish both tier transforms before replacing a previous working model.
      for (const { file, bytes } of pending) await writeAtomic(file, bytes);
      manifest.models[key] = entry;
    } catch (error) {
      failures += 1;
      console.error('FAIL ' + key + ': ' + (error instanceof Error ? error.message : String(error)) + '; previous manifest entry kept');
    }
  }
  return failures;
}

/** Re-hashes every listed tier (retained ones too), sorts and writes the manifest. */
export async function writeManifest({ outDir, urlBase, manifest, generatedAt }) {
  // Version retained entries too when --only is used: every stable filename must invalidate old caches.
  for (const entry of Object.values(manifest.models)) for (const tier of Object.values(entry.tiers)) {
    const path = tier.url.split('?')[0];
    const rel = relativeToBase(path, urlBase);
    if (rel === null) throw new Error('Unexpected model URL: ' + path + ' (not under --url-base ' + urlBase + '/)');
    let bytes;
    try {
      bytes = await readFile(join(outDir, rel));
    } catch {
      console.warn('WARN missing retained model tier ' + path + '; manifest URL retained, other models can still be prepared');
      continue;
    }
    tier.url = path + '?v=' + sha(bytes);
    tier.bytes = bytes.byteLength;
  }
  manifest.generatedAt = generatedAt ?? new Date().toISOString();
  manifest.models = Object.fromEntries(Object.entries(manifest.models).sort(([a], [b]) => a.localeCompare(b)));
  await writeAtomic(join(outDir, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
  return manifest;
}

export async function prepareModels(options) {
  const { root, out: outDir, urlBase } = options;
  const manifest = await previousManifest(outDir);
  let failures = 0;
  if (options.importFrom) {
    await importModels({ ...options, outDir, manifest });
  } else if (!options.manifestOnly) {
    const result = await packageSources({ ...options, outDir, manifest });
    if (result === null) return { failures: 0, manifest };
    failures = result;
  }
  await writeManifest({ outDir, urlBase, manifest, generatedAt: options.generatedAt });
  console.log('\nmanifest: ' + Object.keys(manifest.models).length + ' models → ' + displayPath(join(outDir, 'manifest.json')) + ' (URLs ' + urlBase + '/…, game ' + displayPath(root) + ')');
  if (failures > 0) console.log(failures + ' model(s) skipped; see ERROR lines above.');
  return { failures, manifest };
}

export const USAGE = `pnpm models:prepare [--root <game>] [--out <dir>] [--url-base </assets/<id>/models/>] [--art-src <dir>]
    [--only <kind>/<id>[,…]] [--force] [--contracts <file>] [--manifest-only] [--generated-at <ISO>]
    [--import <other manifest.json> --only <keys> [--tiers high,medium]]
Defaults: games/space-typing, <root>/public/assets/<id>/models, /assets/<id>/models/, <root>/art-src.`;

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const flags = parseFlags(process.argv.slice(2), FLAGS);
    if (flags.help) console.log(USAGE);
    else {
      const { failures } = await prepareModels(modelOptions(flags));
      if (failures > 0) process.exitCode = 1;
    }
  } catch (error) {
    console.error((error instanceof UsageError ? 'Usage: ' : '') + error.message);
    if (error instanceof UsageError) console.error(USAGE);
    process.exitCode = error instanceof UsageError ? 2 : 1;
  }
}
