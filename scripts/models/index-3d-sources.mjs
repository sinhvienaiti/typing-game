#!/usr/bin/env node
/**
 * pnpm models:index [--root <game>] [--art-src <dir>] [--out <SOURCES.json>] [--preset <file>]
 *
 * Copy of games/space-typing/scripts/models/index-3d-sources.mjs for any game.
 * Rewrites <art-src>/3d/SOURCES.json from the files on disk: each owner GLB's
 * md5 and size, the 2D image it mirrors, the build entries that read it, and
 * the 2D images whose own model is not made yet (built from a placeholder).
 * The recorded history and the list of originals missing from this machine
 * are kept. With no flags it writes exactly what Space's script writes.
 *
 * Rule: art-src/<path>/<name>.png -> art-src/3d/<path>/<name>.glb.
 * Ships: art-src/ships/ship-NN-<id>-2d.png -> art-src/3d/ships/ship-NN-<id>.glb
 * (Vanguard's image is art-src/ships/vanguard-top-hd.png). skills/ and items/
 * hold Text to 3D models that have no 2D image.
 * Readers come from the preset (default <root>/scripts/models/presets/campaign3d-models.json)
 * and, when the game has one, its ship catalog (<root>/scripts/ships/ship-sources.mjs).
 */
import { createHash } from 'node:crypto';
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { mkdir, rename, writeFile } from 'node:fs/promises';
import { dirname, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { DEFAULT_GAME, displayPath, parseFlags, REPO_ROOT, resolveGame, UsageError } from './lib/options.mjs';

const TEXT_TO_3D = ['skills/', 'items/'];
const toPosix = (value) => value.split(sep).join('/');

export const FLAGS = { preset: 'string' };

/** The 2D image a model under art-src/3d mirrors (null for Text to 3D models). */
export function mirrorImage(file, artSrc = 'art-src') {
  if (TEXT_TO_3D.some((folder) => file.startsWith(folder))) return null;
  if (file === 'ships/ship-01-vanguard.glb') return artSrc + '/ships/vanguard-top-hd.png';
  if (file.startsWith('ships/')) return artSrc + '/' + file.replace(/\.glb$/, '-2d.png');
  return artSrc + '/' + file.replace(/\.glb$/, '.png');
}

/** Build entries that read each file: the preset, the ship catalog and the G01 packagers. */
export function readers(preset, shipCatalog = []) {
  const used = {};
  const add = (file, who) => (used[file] ??= []).push(who);
  for (const [key, value] of Object.entries(preset.models ?? {})) {
    add(value.source, key);
    if (value.placeholder) add(value.placeholder, key + ' (placeholder)');
  }
  for (const visual of shipCatalog) {
    const numbered = visual.rawModelSources.find((name) => /^ship-\d\d-/.test(name));
    if (numbered) add('ships/' + numbered, 'ships/' + visual.id);
  }
  for (const who of ['bosses/tyrant-g01', 'bosses/3d/tyrant-g01 (prepare-boss-3d)', 'bosses/auriel-hero (--hero-clips)']) add('bosses/tyrant-g01.glb', who);
  return used;
}

/** Command written into SOURCES.json "rule": Space keeps its own script's command. */
export function regenerateCommand(game) {
  const isDefault = game.root === join(REPO_ROOT, DEFAULT_GAME) && game.artSrc === join(game.root, 'art-src');
  if (isDefault) return 'node scripts/models/index-3d-sources.mjs';
  const artSrc = game.artSrc === join(game.root, 'art-src') ? '' : ' --art-src ' + toPosix(relative(REPO_ROOT, game.artSrc));
  return 'pnpm models:index --root ' + toPosix(relative(REPO_ROOT, game.root)) + artSrc;
}

export async function loadShipCatalog(root) {
  const file = join(root, 'scripts/ships/ship-sources.mjs');
  if (!existsSync(file)) return [];
  return (await import(pathToFileURL(file).href)).SHIP_VISUAL_CATALOG ?? [];
}

export function indexSources({ root, artSrc, preset, shipCatalog = [], regenerate = 'node scripts/models/index-3d-sources.mjs' }) {
  const tree = join(artSrc, '3d');
  const prefix = toPosix(relative(root, artSrc)) || '.';
  const previous = existsSync(join(tree, 'SOURCES.json')) ? JSON.parse(readFileSync(join(tree, 'SOURCES.json'), 'utf8')) : {};
  const used = readers(preset, shipCatalog);
  const glbs = existsSync(tree) ? readdirSync(tree, { recursive: true, withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith('.glb'))
    .map((entry) => toPosix(relative(tree, join(entry.parentPath ?? entry.path, entry.name)))).sort() : [];
  const files = {};
  const noImage = [];
  for (const file of glbs) {
    const bytes = readFileSync(join(tree, file));
    const image = mirrorImage(file, prefix);
    if (image !== null && !existsSync(join(root, image))) noImage.push(file);
    files[file] = {
      md5: createHash('md5').update(bytes).digest('hex'),
      bytes: statSync(join(tree, file)).size,
      image: image !== null && existsSync(join(root, image)) ? image : null,
      usedBy: used[file] ?? [],
      ...(previous.files?.[file]?.downloadedAs ? { downloadedAs: previous.files[file].downloadedAs } : {}),
    };
  }
  const notMadeYet = {};
  for (const [file, value] of Object.entries(previous.notMadeYet ?? {})) if (!files[file]) notMadeYet[file] = value;
  for (const [key, value] of Object.entries(preset.models ?? {})) {
    if (!value.placeholder || files[value.source]) continue;
    notMadeYet[value.source] = { image: mirrorImage(value.source, prefix), standIn: value.placeholder, usedBy: used[value.source] ?? [key] };
  }
  const out = {
    version: 1,
    rule: 'art-src/<path>/<name>.png -> art-src/3d/<path>/<name>.glb (ships: art-src/ships/ship-NN-<id>-2d.png -> art-src/3d/ships/ship-NN-<id>.glb; skills/ and items/ hold Text to 3D models with no 2D image). Owner originals from Tripo/Meshy, never edited; pipelines read them and write processed copies elsewhere. Regenerate: ' + regenerate,
    files,
    notMadeYet: Object.fromEntries(Object.entries(notMadeYet).sort(([a], [b]) => a.localeCompare(b))),
    noOriginalOnThisMachine: previous.noOriginalOnThisMachine ?? {},
    history: previous.history ?? {},
  };
  return { out, noImage };
}

/** Flags -> everything indexSources needs (preset and ship catalog loaded). */
export async function indexOptions(flags, cwd = process.cwd()) {
  const game = resolveGame(flags, cwd);
  if (flags['url-base']) throw new UsageError('--url-base is for models:prepare');
  const outFile = flags.out ? resolve(cwd, flags.out) : join(game.artSrc, '3d/SOURCES.json');
  if (!outFile.endsWith('.json')) throw new UsageError('--out for models:index is the SOURCES.json file to write');
  const presetFile = flags.preset ? resolve(cwd, flags.preset) : join(game.root, 'scripts/models/presets/campaign3d-models.json');
  if (flags.preset && !existsSync(presetFile)) throw new UsageError('--preset: no file ' + presetFile);
  const preset = existsSync(presetFile) ? JSON.parse(readFileSync(presetFile, 'utf8')) : { models: {} };
  return { ...game, outFile, preset, shipCatalog: await loadShipCatalog(game.root), regenerate: regenerateCommand(game) };
}

export const USAGE = `pnpm models:index [--root <game>] [--art-src <dir>] [--out <SOURCES.json>] [--preset <file>]
Defaults: games/space-typing, <root>/art-src, <art-src>/3d/SOURCES.json, <root>/scripts/models/presets/campaign3d-models.json.`;

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const flags = parseFlags(process.argv.slice(2), FLAGS);
    if (flags.help) console.log(USAGE);
    else {
      const options = await indexOptions(flags);
      const { out, noImage } = indexSources(options);
      await mkdir(dirname(options.outFile), { recursive: true });
      const temporary = options.outFile + '.tmp-' + process.pid;
      await writeFile(temporary, JSON.stringify(out, null, 1) + '\n');
      await rename(temporary, options.outFile);
      const where = displayPath(options.outFile);
      const unused = Object.values(out.files).filter((value) => value.usedBy.length === 0).length;
      console.log(where + ': ' + Object.keys(out.files).length + ' models, ' + Object.keys(out.notMadeYet).length + ' not made yet, ' + unused + ' read by no build');
      for (const file of noImage) console.log('WARN ' + file + ': no 2D image at ' + mirrorImage(file, toPosix(relative(options.root, options.artSrc))) + ' (name it after its 2D art)');
      if (noImage.length) process.exitCode = 1;
    }
  } catch (error) {
    console.error((error instanceof UsageError ? 'Usage: ' : '') + error.message);
    process.exitCode = error instanceof UsageError ? 2 : 1;
  }
}
