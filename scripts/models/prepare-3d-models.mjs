#!/usr/bin/env node
/**
 * pnpm models:blender [--root <game>] [--out <dir>] [--url-base <path>]
 *                     [--preset <file>] [--only <key>[,…]] [--kind <kind>] [--kinds <a,b>]
 *                     [--contracts <file>] [--blender <bin>] [--preview <dir>] [--dry-run] [--force] [--no-package]
 *
 * Copy of games/space-typing/scripts/models/prepare-campaign3d-models.mjs for
 * any game: Tripo/Meshy GLBs in <root>/art-src/3d go through the Blender helper
 * (blender/space_typing_model_tools.py, same file as Space's) with the
 * orientation and budget in the preset, then through prepare-models.mjs with
 * the same --root/--out/--url-base, into the game's model manifest.
 *
 * Preset (default <root>/scripts/models/presets/campaign3d-models.json):
 *   { "version": 1, "contracts"?: "<file under root>", "kinds"?: ["<kind>", …],
 *     "models": { "<kind>/<id>": { "source": "<path under art-src/3d>.glb",
 *     "placeholder"?, "rotate"?, "nose"?, "facing"?, "triangles", "autoEmissive"?, "reviewed",
 *     "static"?: { … }, "reference"?: "<picture under art-src>" } } }
 * "contracts" and "kinds" are defaults for --contracts and --kinds.
 * An entry with "static" (props, buildings, projectiles, worn or held items:
 * no rig, no clip) goes through blender/static_model_tools.py instead, with
 * "static" as its spec (orientation, size, pivot, colour, FX_ sockets; see
 * that file) and "triangles" as its decimation target. Its colour is matched
 * to "reference", else to the 2D picture SOURCES.json lists for the source.
 * It writes a report to <root>/art-src/models/.reports/<kind>__<id>.json and,
 * with --preview <dir>, before/after/top/front renders.
 * An entry whose own model is not made yet builds from its placeholder; a new
 * or changed source waits for review (REVIEW) until --force. Blender writes
 * <root>/art-src/models/<kind>/<id>.glb, so --art-src is not supported here.
 */
import { createHash } from 'node:crypto';
import { constants, existsSync } from 'node:fs';
import { access, mkdir, readdir, readFile, rename, writeFile } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { dirname, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadContracts, parseFlags, resolveGame, UsageError } from './lib/options.mjs';

const HERE = dirname(fileURLToPath(import.meta.url));
export const HELPER = join(HERE, 'blender/space_typing_model_tools.py');
export const STATIC_HELPER = join(HERE, 'blender/static_model_tools.py');
export const PACKAGER = join(HERE, 'prepare-models.mjs');
export const DEFAULT_KINDS = ['enemies', 'bosses', 'skills', 'items'];
const NOSES = ['+X', '-X', '+Y', '-Y'];
// Kinds the Blender helper accepts (its --kind choices).
const HELPER_KINDS = ['ships', 'enemies', 'bosses', 'skills', 'items', 'heroes', 'guides'];
const sha = (value) => createHash('sha256').update(value).digest('hex');
const fileHash = async (path) => sha(await readFile(path));

export const FLAGS = {
  preset: 'string', only: 'list', kind: 'string', kinds: 'list', contracts: 'string', blender: 'string', preview: 'string',
  'dry-run': 'boolean', force: 'boolean', 'no-package': 'boolean',
};

export function validatePreset(key, value, { contracts, kinds = DEFAULT_KINDS }) {
  const [kind, id] = key.split('/');
  if (!kinds.includes(kind) || !/^[a-z0-9][a-z0-9-]*$/.test(id ?? '')) throw new Error(key + ': key must be <' + kinds.join('|') + '>/<id>');
  const safe = (path) => typeof path === 'string' && path.endsWith('.glb') && !path.includes('..') && !path.startsWith('/');
  if (!safe(value?.source)) throw new Error(key + ': source must be a .glb path under art-src/3d');
  if (value.placeholder != null && (!safe(value.placeholder) || value.placeholder === value.source)) throw new Error(key + ': placeholder must be another .glb path under art-src/3d');
  if (value.rotate != null && (!Array.isArray(value.rotate) || value.rotate.length !== 9 || !value.rotate.every(Number.isFinite))) throw new Error(key + ': rotate must be nine numbers');
  if (value.nose != null && !NOSES.includes(value.nose)) throw new Error(key + ': nose must be one of ' + NOSES.join(', '));
  if (value.facing != null && !['+Y', '-Y'].includes(value.facing)) throw new Error(key + ': facing must be +Y or -Y');
  const { min, max } = contracts.MODEL_CONTRACTS[kind].triangles;
  if (!Number.isInteger(value.triangles) || value.triangles < min || value.triangles > max) throw new Error(key + ': triangles must be an integer in ' + min + '–' + max);
  if (!Number.isFinite(value.autoEmissive ?? 0) || (value.autoEmissive ?? 0) < 0 || (value.autoEmissive ?? 0) > 1) throw new Error(key + ': autoEmissive must be in [0, 1]');
  if (typeof value.reviewed !== 'boolean') throw new Error(key + ': reviewed must be true or false');
  if (value.static != null && (typeof value.static !== 'object' || Array.isArray(value.static))) throw new Error(key + ': static must be an object (the static helper spec)');
  if (value.reference != null && (typeof value.reference !== 'string' || !/\.(png|jpe?g|webp)$/i.test(value.reference) || value.reference.includes('..') || value.reference.startsWith('/'))) {
    throw new Error(key + ': reference must be a picture path under art-src');
  }
  return { kind, id, ...value, nose: value.nose ?? '+Y', facing: value.facing ?? '+Y', autoEmissive: value.autoEmissive ?? 0 };
}

/** The file an entry builds from: its own model, else its placeholder while that is missing (null: neither). */
export function resolveSource(sourceRoot, entry) {
  const own = join(sourceRoot, entry.source);
  if (existsSync(own)) return { path: own, placeholder: false };
  const stand = entry.placeholder ? join(sourceRoot, entry.placeholder) : null;
  return stand !== null && existsSync(stand) ? { path: stand, placeholder: true } : null;
}

/** Content, not paths: moving or renaming a source costs no rebuild. */
export function cacheSignature(value, sourceHash, shared, packaged) {
  const { source, placeholder, note, ...numbers } = value;
  return sha(JSON.stringify({ version: 2, source: sourceHash, entry: numbers, ...shared, package: packaged }));
}

/** Static helper command: no rig, no clip; the spec carries the decimation target. */
export function staticArguments(entry, input, { output, report, reference, preview }) {
  const args = ['--background', '--factory-startup', '--python-exit-code', '1', '--python', STATIC_HELPER, '--',
    '--input', input, '--output', output, '--id', entry.kind + '/' + entry.id,
    '--spec', JSON.stringify({ ...entry.static, triangles: entry.triangles })];
  if (report) args.push('--report', report);
  if (reference) args.push('--reference', reference);
  if (preview) args.push('--preview', preview);
  return args;
}

/** The 2D picture a static entry's colour is matched to: its own "reference", else SOURCES.json's image. */
export function referencePicture(options, entry, sources) {
  if (entry.reference) return join(options.artSrc, entry.reference);
  const image = sources?.files?.[entry.source]?.image;
  return typeof image === 'string' && !image.includes('..') ? join(options.root, image) : null;
}

export function blenderArguments(root, entry, input) {
  const args = ['--background', '--factory-startup', '--python-exit-code', '1', '--python', HELPER, '--',
    '--input', input, '--kind', entry.kind, '--id', entry.id, '--project', root,
    '--nose=' + entry.nose, '--facing=' + entry.facing, '--tris', String(entry.triangles), '--auto-emissive', String(entry.autoEmissive)];
  // Inline form: a leading "-1" would otherwise parse as an option.
  if (entry.rotate) args.push('--rotate=' + entry.rotate.join(','));
  return args;
}

/** Packager command for one model, with the same game flags. */
export function packagerArguments(options, key) {
  const args = ['--root', options.root, '--out', options.out, '--url-base', options.urlBase + '/', '--only', key];
  if (options.contracts) args.push('--contracts', options.contracts);
  return [PACKAGER, ...args];
}

export async function findBlender(explicit, env = process.env) {
  const candidates = [explicit, env.BLENDER_BIN,
    '/Applications/Blender.app/Contents/MacOS/Blender',
    ...(env.PATH ?? '').split(':').filter(Boolean).map((dir) => join(dir, process.platform === 'win32' ? 'blender.exe' : 'blender'))].filter(Boolean);
  for (const candidate of candidates) {
    try { await access(candidate, constants.X_OK); return candidate; } catch { /* Try next installation. */ }
  }
  throw new Error('Blender CLI not found. Set BLENDER_BIN or pass --blender /path/to/blender; raw sources and existing game models were kept.');
}

export function runCommand(command, args, options = {}) {
  return new Promise((resolveRun, reject) => {
    const child = spawn(command, args, { cwd: options.cwd, stdio: 'inherit', shell: false });
    child.on('error', reject);
    child.on('close', (code, signal) => (code === 0 ? resolveRun() : reject(new Error(command + ' exited ' + (signal ?? code)))));
  });
}

async function readJson(path, fallback = null) {
  try { return JSON.parse(await readFile(path, 'utf8')); } catch (error) { if (error.code === 'ENOENT') return fallback; throw error; }
}

async function writeJsonAtomic(path, value) {
  await mkdir(dirname(path), { recursive: true });
  const temporary = path + '.tmp-' + process.pid;
  await writeFile(temporary, JSON.stringify(value, null, 2) + '\n');
  await rename(temporary, path);
}

async function sourceFiles(sourceRoot) {
  if (!existsSync(sourceRoot)) return [];
  const entries = await readdir(sourceRoot, { recursive: true, withFileTypes: true });
  return entries.filter((entry) => entry.isFile() && entry.name.endsWith('.glb'))
    .map((entry) => relative(sourceRoot, join(entry.parentPath ?? entry.path, entry.name)).split(sep).join('/')).sort();
}

function runtimePaths(options, kind, id) {
  return ['high', 'medium'].map((tier) => join(options.out, kind, id, id + '.' + tier + '.glb'));
}

async function validRuntimeEntry(options, contracts, kind, id) {
  const entry = (await readJson(join(options.out, 'manifest.json')))?.models?.[kind + '/' + id];
  if (!entry || contracts.MODEL_CONTRACTS[kind].requiredSockets.some((socket) => !entry.sockets?.includes(socket))) return false;
  return ['high', 'medium'].every((tier) => entry.tiers?.[tier]?.url?.split('?')[0] === options.urlBase + '/' + kind + '/' + id + '/' + id + '.' + tier + '.glb')
    && runtimePaths(options, kind, id).every(existsSync);
}

/** Flags -> options. Blender writes into <root>/art-src, so a custom --art-src is refused. */
export function blenderOptions(flags, cwd = process.cwd()) {
  const game = resolveGame(flags, cwd);
  if (game.artSrc !== join(game.root, 'art-src')) throw new UsageError('models:blender works on <root>/art-src (the Blender helper writes there); drop --art-src');
  return {
    ...game,
    presetFile: flags.preset ? resolve(cwd, flags.preset) : join(game.root, 'scripts/models/presets/campaign3d-models.json'),
    only: flags.only?.length ? flags.only : null,
    kind: flags.kind,
    kinds: flags.kinds,
    contracts: flags.contracts ? resolve(cwd, flags.contracts) : undefined,
    blender: flags.blender,
    preview: flags.preview ? resolve(cwd, flags.preview) : undefined,
    dryRun: Boolean(flags['dry-run']),
    force: Boolean(flags.force),
    noPackage: Boolean(flags['no-package']),
  };
}

/** Injectable command runner keeps the workflow testable without Blender. */
export async function prepare3DModels(options) {
  const log = options.log ?? console.log;
  const execute = options.runCommand ?? runCommand;
  const sourceRoot = join(options.artSrc, '3d');
  const preset = await readJson(options.presetFile);
  if (preset?.version !== 1 || !preset.models || typeof preset.models !== 'object') throw new Error('Invalid preset file: ' + options.presetFile);
  // The preset may name the game's contracts and kinds; flags win.
  if (preset.contracts != null && (typeof preset.contracts !== 'string' || preset.contracts.includes('..'))) throw new Error('Preset contracts must be a path under the game root');
  if (preset.kinds != null && (!Array.isArray(preset.kinds) || !preset.kinds.every((kind) => typeof kind === 'string'))) throw new Error('Preset kinds must be a list of kinds');
  options = { ...options, contracts: options.contracts ?? (preset.contracts ? join(options.root, preset.contracts) : undefined) };
  const contracts = options.contractsModule ?? await loadContracts(options.root, options.contracts);
  const kinds = options.kinds ?? preset.kinds ?? DEFAULT_KINDS;
  const allStatic = (kind) => {
    const entries = Object.entries(preset.models).filter(([key]) => key.startsWith(kind + '/'));
    return entries.length > 0 && entries.every(([, value]) => value?.static != null);
  };
  for (const kind of kinds) {
    if (!contracts.MODEL_CONTRACTS[kind]) throw new Error('--kinds: ' + kind + ' has no model contract in ' + contracts.file);
    if (!HELPER_KINDS.includes(kind) && !allStatic(kind)) throw new Error('--kinds: the Blender helper does not handle ' + kind + ' (only "static" entries can use it)');
  }
  if (options.kind && !kinds.includes(options.kind)) throw new Error('--kind must be one of ' + kinds.join(', '));
  const only = options.only ? new Set(options.only) : null;
  if (only) for (const key of only) if (!preset.models[key]) throw new Error('Unknown preset key: ' + key);
  const keys = Object.keys(preset.models).filter((key) => (!only || only.has(key)) && (!options.kind || key.startsWith(options.kind + '/')));
  const staticHash = await fileHash(STATIC_HELPER);
  const sources = await readJson(join(sourceRoot, 'SOURCES.json'));
  const shared = {
    helperHash: await fileHash(HELPER),
    packagerHash: await fileHash(PACKAGER),
    contractsHash: await fileHash(contracts.file),
    dependencyHash: existsSync(join(options.root, 'pnpm-lock.yaml')) ? await fileHash(join(options.root, 'pnpm-lock.yaml')) : null,
  };
  const results = [];
  let blender = null;
  for (const key of keys) {
    try {
      const entry = validatePreset(key, preset.models[key], { contracts, kinds });
      const source = resolveSource(sourceRoot, entry);
      if (source === null) { results.push({ key, status: 'missing' }); log('MISSING ' + key + ': ' + join(sourceRoot, entry.source)); continue; }
      const cacheFile = join(options.artSrc, 'models/.campaign3d-model-cache', entry.kind + '__' + entry.id + '.json');
      const cache = await readJson(cacheFile);
      if (source.placeholder && !options.force && typeof cache?.source === 'string' && cache.source.endsWith(join('art-src/3d', entry.source))) {
        results.push({ key, status: 'missing' }); log('MISSING ' + key + ': its own model ' + entry.source + ' was built before and is gone; the built model is kept (--force builds the placeholder)'); continue;
      }
      if (!source.placeholder && entry.placeholder && !options.force) {
        results.push({ key, status: 'review' }); log('REVIEW ' + key + ': its own model ' + entry.source + ' is in; check its orientation (rotate, facing), then drop "placeholder" from ' + options.presetFile + ' (or rerun with --force)'); continue;
      }
      const sourceHash = await fileHash(source.path);
      if (!options.force && typeof cache?.sourceHash === 'string' && cache.sourceHash !== sourceHash && cache.source === source.path) {
        results.push({ key, status: 'review' }); log('REVIEW ' + key + ': ' + (source.placeholder ? entry.placeholder : entry.source) + ' changed since its last build; check its orientation, then rerun with --force --only=' + key); continue;
      }
      if (source.placeholder) log('NOTE ' + key + ': its own model ' + entry.source + ' is not made yet; building from the placeholder ' + entry.placeholder);
      if (!entry.reviewed) log('NOTE ' + key + ': orientation not yet marked reviewed in ' + options.presetFile);
      const processed = join(options.artSrc, 'models', entry.kind, entry.id + '.glb');
      const outputs = [processed, ...(!options.noPackage ? runtimePaths(options, entry.kind, entry.id) : [])];
      const reference = entry.static ? referencePicture(options, entry, sources) : null;
      const usable = reference !== null && existsSync(reference) ? reference : null;
      if (entry.static && reference !== null && usable === null) log('NOTE ' + key + ': reference picture ' + reference + ' is missing; colour matching is skipped');
      const signature = cacheSignature(preset.models[key], sourceHash,
        entry.static ? { ...shared, helperHash: staticHash, referenceHash: usable ? await fileHash(usable) : null } : shared, !options.noPackage);
      let cached = !options.force && cache?.signature === signature && (options.noPackage || await validRuntimeEntry(options, contracts, entry.kind, entry.id));
      if (cached) for (const path of outputs) {
        if (!existsSync(path) || await fileHash(path) !== cache.outputs?.[path]) { cached = false; break; }
      }
      if (cached) { results.push({ key, status: 'cached' }); log('CACHED ' + key); continue; }
      const args = entry.static
        ? staticArguments(entry, source.path, {
          output: processed, reference: usable, preview: options.preview,
          report: join(options.artSrc, 'models/.reports', entry.kind + '__' + entry.id + '.json'),
        })
        : blenderArguments(options.root, entry, source.path);
      if (options.dryRun) {
        results.push({ key, status: 'planned', args, packager: options.noPackage ? null : packagerArguments(options, key) });
        log('PLAN ' + key + ': ' + entry.triangles + ' triangles, ' + (entry.static ? 'static' : 'nose ' + entry.nose + ', facing ' + entry.facing)); continue;
      }
      blender ??= await findBlender(options.blender);
      await execute(blender, args, { cwd: options.root });
      if (!existsSync(processed)) throw new Error('Blender did not write ' + processed);
      if (!options.noPackage) {
        await execute(process.execPath, packagerArguments(options, key), { cwd: options.root });
        if (!await validRuntimeEntry(options, contracts, entry.kind, entry.id)) throw new Error('Packager did not produce a complete model manifest entry');
      }
      const hashes = {};
      for (const path of outputs) hashes[path] = await fileHash(path);
      await writeJsonAtomic(cacheFile, { version: 2, signature, source: source.path, sourceHash, outputs: hashes });
      results.push({ key, status: 'pass' }); log('PASS ' + key);
    } catch (error) {
      results.push({ key, status: 'failed', detail: error.message }); log('FAIL ' + key + ': ' + error.message);
    }
  }
  // A new file nothing reads would otherwise pass silently; ships and tyrant-g01 have their own pipelines.
  const read = new Set(Object.values(preset.models).flatMap((value) => [value.source, value.placeholder].filter(Boolean)));
  const known = new Set(Object.keys((await readJson(join(sourceRoot, 'SOURCES.json')))?.files ?? {}));
  if (!only && !options.kind) for (const file of await sourceFiles(sourceRoot)) {
    if (read.has(file) || known.has(file) || file.startsWith('ships/') || file === 'bosses/tyrant-g01.glb') continue;
    results.push({ key: file, status: 'unread' }); log('UNREAD art-src/3d/' + file + ': no preset entry reads it; add one to ' + options.presetFile);
  }
  const failures = results.filter((result) => ['failed', 'missing', 'review'].includes(result.status)).length;
  const counts = results.reduce((all, result) => ({ ...all, [result.status]: (all[result.status] ?? 0) + 1 }), {});
  log('3D models (' + options.id + '): ' + (Object.entries(counts).map(([status, count]) => status + ' ' + count).join(', ') || 'nothing to do'));
  return { results, failures };
}

export const USAGE = `pnpm models:blender [--root <game>] [--out <dir>] [--url-base </assets/<id>/models/>] [--preset <file>]
    [--only <key>[,…]] [--kind <kind>] [--kinds <a,b>] [--contracts <file>] [--blender <bin>] [--preview <dir>] [--dry-run] [--force] [--no-package]`;

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const flags = parseFlags(process.argv.slice(2), FLAGS);
    if (flags.help) console.log(USAGE);
    else {
      const { failures } = await prepare3DModels(blenderOptions(flags));
      if (failures) process.exitCode = 1;
    }
  } catch (error) {
    console.error((error instanceof UsageError ? 'Usage: ' : '') + error.message);
    process.exitCode = error instanceof UsageError ? 2 : 1;
  }
}
