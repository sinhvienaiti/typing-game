// Shared flags for the model tools, with Space Typing as the default game.
//   --root <game dir>          default games/space-typing
//   --out <public models dir>  default <root>/public/assets/<id>/models
//   --url-base </assets/<id>/models/>  default from the game folder name
//   --art-src <dir>            default <root>/art-src
// Relative paths resolve against the current directory (pnpm: the parent repo).
import { existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

export const REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
export const DEFAULT_GAME = 'games/space-typing';

export class UsageError extends Error {}

const SHARED = { root: 'string', out: 'string', 'url-base': 'string', 'art-src': 'string', help: 'boolean' };

/**
 * Parses --name value, --name=value and boolean --name. spec adds tool flags:
 * 'string' (once), 'boolean', or 'list' (comma-separated, repeatable).
 * Fails closed: unknown flags, missing values and positionals are errors.
 */
export function parseFlags(argv, spec = {}) {
  const types = { ...SHARED, ...spec };
  const args = [...argv];
  if (args[0] === '--') args.shift(); // pnpm 11 passes a literal "--" through
  const options = {};
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === '-h') { options.help = true; continue; }
    if (!arg.startsWith('--') || arg === '--') throw new UsageError(`Unexpected argument: ${arg}`);
    const eq = arg.indexOf('=');
    const name = eq === -1 ? arg.slice(2) : arg.slice(2, eq);
    const type = Object.hasOwn(types, name) ? types[name] : undefined;
    if (!type) throw new UsageError(`Unknown option: --${name}`);
    if (type === 'boolean') {
      if (eq !== -1) throw new UsageError(`--${name} takes no value`);
      options[name] = true;
      continue;
    }
    let value;
    if (eq !== -1) value = arg.slice(eq + 1);
    else {
      value = args[index + 1];
      if (value === undefined || value.startsWith('--')) throw new UsageError(`Missing value for --${name}`);
      index += 1;
    }
    if (value === '') throw new UsageError(`Missing value for --${name}`);
    if (type === 'list') {
      options[name] = [...(options[name] ?? []), ...value.split(',').map((item) => item.trim()).filter(Boolean)];
    } else {
      if (Object.hasOwn(options, name)) throw new UsageError(`--${name} given twice`);
      options[name] = value;
    }
  }
  return options;
}

/** Path for log lines: relative inside the current directory, absolute outside it. */
export function displayPath(file, cwd = process.cwd()) {
  const rel = path.relative(cwd, file);
  return rel && !rel.startsWith('..') && !path.isAbsolute(rel) ? rel.split(path.sep).join('/') : file;
}

/** "/assets/x/models/" -> "/assets/x/models": absolute URL path, no query, no dot segments. */
export function normalizeUrlBase(value) {
  if (typeof value !== 'string' || !value.startsWith('/') || /[?#\\\s]/.test(value)) {
    throw new UsageError(`--url-base must be an absolute URL path such as /assets/<id>/models/ (got ${value})`);
  }
  const trimmed = value.replace(/\/+$/, '');
  const parts = trimmed.split('/').slice(1);
  if (!parts.length || parts.some((part) => !part || part === '.' || part === '..')) {
    throw new UsageError(`--url-base must be an absolute URL path such as /assets/<id>/models/ (got ${value})`);
  }
  return trimmed;
}

/** The game the tool works on. Defaults reproduce Space Typing's own scripts. */
export function resolveGame(options = {}, cwd = process.cwd()) {
  const root = options.root ? path.resolve(cwd, options.root) : path.join(REPO_ROOT, DEFAULT_GAME);
  const id = path.basename(root);
  return {
    root,
    id,
    out: options.out ? path.resolve(cwd, options.out) : path.join(root, 'public/assets', id, 'models'),
    urlBase: normalizeUrlBase(options['url-base'] ?? `/assets/${id}/models/`),
    artSrc: options['art-src'] ? path.resolve(cwd, options['art-src']) : path.join(root, 'art-src'),
  };
}

/** Public URL of one tier: <base>/<kind>/<id>/<id>.<tier>.glb?v=<hash>. */
export function tierUrl(urlBase, kind, id, tier, hash) {
  return `${urlBase}/${kind}/${id}/${id}.${tier}.glb?v=${hash}`;
}

export function urlPath(url) {
  return url.split('?')[0];
}

/** Path of a URL below urlBase ("heroes/x/x.high.glb"), or null when it lies elsewhere. */
export function relativeToBase(url, urlBase) {
  const file = urlPath(url);
  if (!file.startsWith(`${urlBase}/`)) return null;
  const rel = file.slice(urlBase.length + 1);
  return rel.split('/').every((part) => part && part !== '.' && part !== '..') ? rel : null;
}

/** Moves a URL from one base to another; the ?v= query is kept. */
export function rebaseUrl(url, fromBase, toBase) {
  const rel = relativeToBase(url, fromBase);
  if (rel === null) throw new Error(`URL ${url} is not under ${fromBase}`);
  const query = url.includes('?') ? url.slice(url.indexOf('?')) : '';
  return `${toBase}/${rel}${query}`;
}

/** Base of a tier URL: everything before <kind>/<id>/<file>. */
export function inferUrlBase(url) {
  const parts = urlPath(url).split('/');
  if (parts.length < 5) throw new Error(`Cannot tell the model base of ${url}`);
  return normalizeUrlBase(parts.slice(0, -3).join('/'));
}

/**
 * Loads a build dependency (gltf-transform, sharp, meshoptimizer) from the
 * game's own node_modules, else from Space Typing's, so the parent repo needs no install.
 */
export async function importDependency(specifier, root) {
  const bases = [...new Set([root, path.join(REPO_ROOT, DEFAULT_GAME), REPO_ROOT])];
  for (const base of bases) {
    let resolved;
    try { resolved = createRequire(path.join(base, 'package.json')).resolve(specifier); } catch { continue; }
    return import(pathToFileURL(resolved).href);
  }
  throw new Error(`${specifier} is not installed in ${bases.join(' or ')}: run pnpm install in the game folder`);
}

/** Model contracts of the game (TypeScript, loaded by Node's type stripping). */
export async function loadContracts(root, explicit) {
  const candidates = explicit ? [explicit] : ['src/render3d/model-contracts.ts', 'src/kit/three/model-contracts.ts'];
  for (const candidate of candidates) {
    const file = path.resolve(root, candidate);
    if (!explicit && !existsSync(file)) continue;
    const module = await import(pathToFileURL(file).href);
    if (!module.MODEL_CONTRACTS) throw new Error(`${file} exports no MODEL_CONTRACTS`);
    return { file, ...module };
  }
  throw new Error(`No model contracts in ${root} (${candidates.join(', ')}); pass --contracts <file>`);
}
