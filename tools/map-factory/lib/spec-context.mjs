import { readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { REPO_ROOT, FIXTURE_DIR, gameplayHash } from '../adapters/extract.mjs';

export const KITS_DIR = path.join(REPO_ROOT, 'tools/map-factory/registry/kits');
export const REGISTRY_OUT_DIR = path.join(REPO_ROOT, 'tools/map-factory/registry/out');

const KEBAB = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const KIT = /^([a-z0-9]+(?:-[a-z0-9]+)*)@[1-9][0-9]*$/;
const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const readJson = file => JSON.parse(readFileSync(file, 'utf8'));

function jsonFiles(dir, problems) {
  try {
    return readdirSync(dir).filter(name => name.endsWith('.json')).sort();
  } catch (error) {
    problems.push(`${dir}: ${error.message}`);
    return [];
  }
}

export function loadGameplays(dir = FIXTURE_DIR) {
  const gameplays = [];
  const problems = [];
  for (const name of jsonFiles(dir, problems)) {
    const file = path.join(dir, name);
    try {
      const extract = readJson(file);
      if (gameplayHash(extract) !== extract.hash) {
        problems.push(`${file}: gameplay hash does not match fixture content`);
        continue;
      }
      const { game, map, adapter, commit, hash } = extract;
      gameplays.push({ game, map, adapter, commit, hash });
    } catch (error) {
      problems.push(`${file}: ${error.message}`);
    }
  }
  return { gameplays, problems };
}

/** Validate the v0 kit name list against the two runtime model tiers. */
export function checkKit(fileName, kit, assets) {
  const problems = [];
  const problem = reason => problems.push(`${fileName}: ${reason}`);
  if (!object(kit)) {
    problem('kit must be an object');
    return problems;
  }
  if (kit.format !== 'map-kit/0') problem('format must be map-kit/0');
  const match = typeof kit.kit === 'string' ? KIT.exec(kit.kit) : null;
  if (!match || fileName !== `${match[1]}.json`) problem('kit name must match KIT and its file name');
  if (typeof kit.game !== 'string' || !KEBAB.test(kit.game)) problem('game must match KEBAB');
  if (!Array.isArray(assets)) problem('model registry is missing or invalid');
  if (!object(kit.protos) || Object.keys(kit.protos).length === 0) {
    problem('protos must be a nonempty object');
    return problems;
  }
  const runtimeIds = new Set(Array.isArray(assets)
    ? assets.filter(asset => object(asset) && asset.source === 'runtime').map(asset => asset.id)
    : []);
  for (const [name, proto] of Object.entries(kit.protos)) {
    if (!KEBAB.test(name)) problem(`proto ${JSON.stringify(name)} must match KEBAB`);
    if (!object(proto) || Object.keys(proto).length !== 1 || !Object.hasOwn(proto, 'asset')
        || (proto.asset !== null && typeof proto.asset !== 'string')) {
      problem(`proto ${JSON.stringify(name)} must contain only asset (string or null)`);
      continue;
    }
    if (typeof proto.asset === 'string'
        && (!runtimeIds.has(`${proto.asset}.high`) || !runtimeIds.has(`${proto.asset}.medium`))) {
      problem(`proto ${JSON.stringify(name)} requires high and medium runtime assets: ${proto.asset}`);
    }
  }
  return problems;
}

export function loadKits(dir = KITS_DIR, registryDir = REGISTRY_OUT_DIR) {
  const kits = [];
  const problems = [];
  const seen = new Set();
  const registries = new Map();
  for (const name of jsonFiles(dir, problems)) {
    const file = path.join(dir, name);
    try {
      const kit = readJson(file);
      let assets = null;
      if (object(kit) && typeof kit.game === 'string' && KEBAB.test(kit.game)) {
        if (!registries.has(kit.game)) {
          const registryFile = path.join(registryDir, `assets.${kit.game}.json`);
          try {
            const registry = readJson(registryFile);
            if (!Array.isArray(registry?.assets)) throw new TypeError('assets must be an array');
            registries.set(kit.game, registry.assets);
          } catch (error) {
            problems.push(`${registryFile}: ${error.message}`);
            registries.set(kit.game, null);
          }
        }
        assets = registries.get(kit.game);
      }
      const kitProblems = checkKit(name, kit, assets);
      if (object(kit) && typeof kit.kit === 'string') {
        if (seen.has(kit.kit)) kitProblems.push(`${file}: duplicate kit ${kit.kit}`);
        seen.add(kit.kit);
      }
      problems.push(...kitProblems);
      if (kitProblems.length === 0) kits.push({ kit: kit.kit, game: kit.game, protos: Object.keys(kit.protos) });
    } catch (error) {
      problems.push(`${file}: ${error.message}`);
    }
  }
  return { kits, problems };
}
