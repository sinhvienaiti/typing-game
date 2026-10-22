// Model tools: flags, defaults, URL rewriting, manifest import/regeneration,
// SOURCES.json indexing and the Blender plan. No Blender, no network.
// Run: pnpm models:test
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import test from 'node:test';
import {
  displayPath, inferUrlBase, normalizeUrlBase, parseFlags, rebaseUrl, relativeToBase, REPO_ROOT, resolveGame, tierUrl, UsageError,
} from '../lib/options.mjs';
import { FLAGS as PREPARE_FLAGS, importModels, modelOptions, prepareModels, writeManifest } from '../prepare-models.mjs';
import { indexOptions, indexSources, mirrorImage, readers, regenerateCommand } from '../index-3d-sources.mjs';
import { blenderOptions, FLAGS as BLENDER_FLAGS, HELPER, PACKAGER, prepare3DModels, validatePreset } from '../prepare-3d-models.mjs';

const SPACE = path.join(REPO_ROOT, 'games/space-typing');
const SPACE_BASE = '/assets/space-typing/models';
const sha10 = (value) => createHash('sha256').update(value).digest('hex').slice(0, 10);

function scratch(t, prefix = 'models-') {
  const dir = mkdtempSync(path.join(tmpdir(), prefix));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  return dir;
}

function put(root, rel, content) {
  const file = path.join(root, rel);
  mkdirSync(path.dirname(file), { recursive: true });
  writeFileSync(file, content);
  return file;
}

const CONTRACTS = {
  file: path.join(SPACE, 'src/render3d/model-contracts.ts'),
  MODEL_CONTRACTS: {
    enemies: { requiredSockets: ['FX_CORE'], triangles: { min: 800, max: 7000 } },
    units: { requiredSockets: [], triangles: { min: 500, max: 9000 } },
    heroes: { requiredSockets: ['FX_CORE'], triangles: { min: 8000, max: 30000 } },
  },
};

test('flags: --name value, --name=value, lists, booleans; everything else fails closed', () => {
  assert.deepEqual(parseFlags(['--', '--root', 'games/dragon-hold', '--url-base=/assets/dragon-hold/models/'], PREPARE_FLAGS),
    { root: 'games/dragon-hold', 'url-base': '/assets/dragon-hold/models/' });
  assert.deepEqual(parseFlags(['--only', 'heroes/a,guides/b', '--only=units/c', '--force'], PREPARE_FLAGS),
    { only: ['heroes/a', 'guides/b', 'units/c'], force: true });
  assert.deepEqual(parseFlags(['-h']), { help: true });
  for (const argv of [['--bogus'], ['extra'], ['--root'], ['--root', '--out', 'x'], ['--root', 'a', '--root', 'b'], ['--force=1'], ['--out='], ['--only', 'x']]) {
    assert.throws(() => parseFlags(argv, argv.includes('--force=1') ? PREPARE_FLAGS : {}), UsageError, argv.join(' '));
  }
});

test('defaults reproduce Space Typing; --root alone derives the other paths from the folder name', () => {
  assert.deepEqual(resolveGame({}), {
    root: SPACE, id: 'space-typing', out: path.join(SPACE, 'public/assets/space-typing/models'), urlBase: SPACE_BASE, artSrc: path.join(SPACE, 'art-src'),
  });
  const dragon = resolveGame({ root: 'games/dragon-hold' }, REPO_ROOT);
  assert.equal(dragon.id, 'dragon-hold');
  assert.equal(dragon.out, path.join(REPO_ROOT, 'games/dragon-hold/public/assets/dragon-hold/models'));
  assert.equal(dragon.urlBase, '/assets/dragon-hold/models');
  assert.equal(dragon.artSrc, path.join(REPO_ROOT, 'games/dragon-hold/art-src'));
  const explicit = resolveGame({ root: 'g', out: 'o', 'url-base': '/x/y/', 'art-src': 'a' }, '/work');
  assert.deepEqual(explicit, { root: '/work/g', id: 'g', out: '/work/o', urlBase: '/x/y', artSrc: '/work/a' });
  assert.equal(displayPath('/work/a/b', '/work'), 'a/b');
  assert.equal(displayPath('/elsewhere/b', '/work'), '/elsewhere/b');
});

test('url base: absolute path, trailing slash optional, no query or dot segments', () => {
  assert.equal(normalizeUrlBase('/assets/dragon-hold/models/'), '/assets/dragon-hold/models');
  assert.equal(normalizeUrlBase('/assets/dragon-hold/models'), '/assets/dragon-hold/models');
  for (const bad of ['assets/x', '/', '//', '/a/../b', '/a/./b', '/a?x=1', '/a#b', '/a b', '/a\\b', 'http://x/a', '/a//b']) {
    assert.throws(() => normalizeUrlBase(bad), UsageError, bad);
  }
});

test('url rewriting: tier URLs, rebasing between games, inferring a base', () => {
  assert.equal(tierUrl('/assets/dragon-hold/models', 'heroes', 'draconis-v2', 'high', 'abc'), '/assets/dragon-hold/models/heroes/draconis-v2/draconis-v2.high.glb?v=abc');
  const url = `${SPACE_BASE}/heroes/draconis-v2/draconis-v2.high.glb?v=a08a065796`;
  assert.equal(relativeToBase(url, SPACE_BASE), 'heroes/draconis-v2/draconis-v2.high.glb');
  assert.equal(relativeToBase(url, '/assets/dragon-hold/models'), null);
  assert.equal(relativeToBase(`${SPACE_BASE}/../x.glb`, SPACE_BASE), null, 'no escape from the base');
  assert.equal(relativeToBase('/assets/space-typing/models-old/a/b/c.glb', SPACE_BASE), null, 'prefix must end at a slash');
  assert.equal(rebaseUrl(url, SPACE_BASE, '/assets/dragon-hold/models'), '/assets/dragon-hold/models/heroes/draconis-v2/draconis-v2.high.glb?v=a08a065796');
  assert.throws(() => rebaseUrl('/other/a/b/c.glb', SPACE_BASE, '/x'), /not under/);
  assert.equal(inferUrlBase(url), SPACE_BASE);
  assert.throws(() => inferUrlBase('/a/b.glb'), /Cannot tell/);
});

test('prepare options: modes that do not go together are refused', () => {
  const parse = (...argv) => modelOptions(parseFlags(argv, PREPARE_FLAGS), REPO_ROOT);
  assert.equal(parse().urlBase, SPACE_BASE);
  assert.throws(() => parse('--import', 'm.json'), /--import needs --only/);
  assert.throws(() => parse('--tiers', 'high'), /--tiers only goes with --import/);
  assert.throws(() => parse('--manifest-only', '--import', 'm.json', '--only', 'a/b'), /do not go together/);
  assert.throws(() => parse('--import', 'm.json', '--only', 'a/b', '--tiers', 'low'), /--tiers/);
  assert.throws(() => parse('--generated-at', 'yesterday'), /ISO/);
  assert.throws(() => parse('--only', 'draconis'), /<kind>\/<id>/);
  const imported = parse('--root', 'games/dragon-hold', '--import', 'games/space-typing/public/assets/space-typing/models/manifest.json',
    '--only', 'heroes/draconis-v3', '--tiers', 'medium');
  assert.equal(imported.importFrom, path.join(SPACE, 'public/assets/space-typing/models/manifest.json'));
  assert.deepEqual(imported.tiers, ['medium']);
  assert.equal(imported.urlBase, '/assets/dragon-hold/models');
});

test('import: tiers are copied from another game and their URLs rewritten to this game', async (t) => {
  const dir = scratch(t);
  const from = path.join(dir, 'space/models');
  const out = path.join(dir, 'dragon/models');
  const high = 'draconis v2 high bytes';
  const medium = 'draconis v3 medium bytes';
  put(from, 'heroes/draconis-v2/draconis-v2.high.glb', high);
  put(from, 'heroes/draconis-v2/draconis-v2.medium.glb', 'v2 medium');
  put(from, 'heroes/draconis-v3/draconis-v3.medium.glb', medium);
  put(from, 'heroes/draconis-v3/draconis-v3.high.glb', 'v3 high');
  const entry = (id, hashes) => ({ kind: 'heroes', id, tiers: Object.fromEntries(Object.entries(hashes).map(([tier, v]) => [tier, { url: `${SPACE_BASE}/heroes/${id}/${id}.${tier}.glb?v=${v}`, bytes: 1 }])), triangles: 9000, sockets: ['FX_CORE'], clips: ['Hero_Fly'], size: [1, 2, 3] });
  put(from, 'manifest.json', JSON.stringify({ version: 1, generatedAt: 'x', models: {
    'heroes/draconis-v2': entry('draconis-v2', { high: sha10(high), medium: sha10('v2 medium') }),
    'heroes/draconis-v3': entry('draconis-v3', { high: sha10('v3 high'), medium: 'deadbeef00' }),
  } }));
  const lines = [];
  const manifest = { version: 1, generatedAt: '', models: {} };
  await importModels({ importFrom: path.join(from, 'manifest.json'), only: ['heroes/draconis-v2'], outDir: out, urlBase: '/assets/dragon-hold/models', manifest, log: (line) => lines.push(line) });
  await importModels({ importFrom: path.join(from, 'manifest.json'), only: ['heroes/draconis-v3'], tiers: ['medium'], outDir: out, urlBase: '/assets/dragon-hold/models', manifest, log: (line) => lines.push(line) });
  assert.equal(readFileSync(path.join(out, 'heroes/draconis-v2/draconis-v2.high.glb'), 'utf8'), high);
  assert.equal(existsSync(path.join(out, 'heroes/draconis-v3/draconis-v3.high.glb')), false, 'only the asked tier');
  assert.deepEqual(manifest.models['heroes/draconis-v3'].tiers, { medium: { url: `/assets/dragon-hold/models/heroes/draconis-v3/draconis-v3.medium.glb?v=${sha10(medium)}`, bytes: medium.length } });
  assert.equal(manifest.models['heroes/draconis-v2'].tiers.high.url, `/assets/dragon-hold/models/heroes/draconis-v2/draconis-v2.high.glb?v=${sha10(high)}`);
  assert.deepEqual(Object.keys(manifest.models['heroes/draconis-v2']), ['kind', 'id', 'tiers', 'triangles', 'sockets', 'clips', 'size'], 'entry shape kept');
  assert.ok(lines.some((line) => /WARN heroes\/draconis-v3 medium/.test(line)), 'a stale ?v= in the source manifest is reported');
  await assert.rejects(importModels({ importFrom: path.join(from, 'manifest.json'), only: ['heroes/nope'], outDir: out, urlBase: '/x', manifest, log() {} }), /not in/);
  await assert.rejects(importModels({ importFrom: path.join(from, 'manifest.json'), only: ['heroes/draconis-v3'], tiers: ['low'], outDir: out, urlBase: '/x', manifest, log() {} }), /no low tier/);

  // The whole command: import, then the manifest is written sorted with fixed time.
  const { manifest: written } = await prepareModels({ ...modelOptions({ root: path.join(dir, 'dragon'), out, 'url-base': '/assets/dragon-hold/models/',
    import: path.join(from, 'manifest.json'), only: ['heroes/draconis-v2'], 'generated-at': '2026-10-23T00:00:00.000Z' }, dir), log() {} });
  assert.deepEqual(Object.keys(written.models), ['heroes/draconis-v2']);
  const text = readFileSync(path.join(out, 'manifest.json'), 'utf8');
  assert.match(text, /"generatedAt": "2026-10-23T00:00:00.000Z"/);
  assert.doesNotMatch(text, /space-typing/);
});

test('manifest regeneration: re-versions every tier, refuses URLs outside the base, and is reproducible', async (t) => {
  const dir = scratch(t);
  const out = path.join(dir, 'models');
  put(out, 'units/warden/warden.high.glb', 'warden high v2');
  const manifest = () => ({ version: 1, generatedAt: '', models: {
    'units/warden': { kind: 'units', id: 'warden', tiers: {
      high: { url: '/assets/dragon-hold/models/units/warden/warden.high.glb?v=old', bytes: 1 },
      medium: { url: '/assets/dragon-hold/models/units/warden/warden.medium.glb?v=keep', bytes: 7 },
    }, triangles: 1, sockets: [], clips: [], size: [1, 1, 1] },
  } });
  const at = '2026-10-23T01:02:03.000Z';
  const first = await writeManifest({ outDir: out, urlBase: '/assets/dragon-hold/models', manifest: manifest(), generatedAt: at });
  assert.equal(first.models['units/warden'].tiers.high.url, `/assets/dragon-hold/models/units/warden/warden.high.glb?v=${sha10('warden high v2')}`);
  assert.equal(first.models['units/warden'].tiers.medium.url, '/assets/dragon-hold/models/units/warden/warden.medium.glb?v=keep', 'missing file: URL kept');
  const bytes = readFileSync(path.join(out, 'manifest.json'));
  await writeManifest({ outDir: out, urlBase: '/assets/dragon-hold/models', manifest: manifest(), generatedAt: at });
  assert.deepEqual(readFileSync(path.join(out, 'manifest.json')), bytes, 'same input, same bytes');
  await assert.rejects(writeManifest({ outDir: out, urlBase: SPACE_BASE, manifest: manifest(), generatedAt: at }), /Unexpected model URL/);
});

test('index: mirror rule, readers and SOURCES.json for a game without Space\'s ship catalog', async (t) => {
  assert.equal(mirrorImage('enemies/frost-healer.glb'), 'art-src/enemies/frost-healer.png');
  assert.equal(mirrorImage('ships/ship-02-razorwing.glb'), 'art-src/ships/ship-02-razorwing-2d.png');
  assert.equal(mirrorImage('ships/ship-01-vanguard.glb'), 'art-src/ships/vanguard-top-hd.png');
  assert.equal(mirrorImage('skills/dragon-fireball.glb'), null);
  assert.equal(mirrorImage('units/warden.glb', 'art'), 'art/units/warden.png');
  assert.deepEqual(readers({ models: { 'units/a': { source: 'units/a.glb', placeholder: 'units/b.glb' } } }, [{ id: 'razor', rawModelSources: ['ship-02-razor.glb'] }]), {
    'units/a.glb': ['units/a'], 'units/b.glb': ['units/a (placeholder)'], 'ships/ship-02-razor.glb': ['ships/razor'],
    'bosses/tyrant-g01.glb': ['bosses/tyrant-g01', 'bosses/3d/tyrant-g01 (prepare-boss-3d)', 'bosses/auriel-hero (--hero-clips)'],
  });
  assert.equal(regenerateCommand(resolveGame({})), 'node scripts/models/index-3d-sources.mjs', 'Space keeps its own rule text');
  assert.equal(regenerateCommand(resolveGame({ root: 'games/dragon-hold' }, REPO_ROOT)), 'pnpm models:index --root games/dragon-hold');

  const root = path.join(scratch(t), 'dragon-hold');
  put(root, 'art-src/3d/units/warden.glb', 'warden');
  put(root, 'art-src/units/warden.png', 'png');
  put(root, 'art-src/3d/units/no-art.glb', 'no art');
  put(root, 'art-src/3d/SOURCES.json', JSON.stringify({ noOriginalOnThisMachine: { 'heroes/draconis-v2': 'runtime copy only' }, history: { a: 1 } }));
  put(root, 'scripts/models/presets/campaign3d-models.json', JSON.stringify({ version: 1, models: {
    'units/warden': { source: 'units/warden.glb' }, 'units/scout': { source: 'units/scout.glb', placeholder: 'units/warden.glb' },
  } }));
  const options = await indexOptions({ root }, '/');
  assert.equal(options.outFile, path.join(root, 'art-src/3d/SOURCES.json'));
  assert.deepEqual(options.shipCatalog, []);
  const { out, noImage } = indexSources(options);
  assert.deepEqual(Object.keys(out.files), ['units/no-art.glb', 'units/warden.glb']);
  assert.deepEqual(out.files['units/warden.glb'], { md5: createHash('md5').update('warden').digest('hex'), bytes: 6, image: 'art-src/units/warden.png', usedBy: ['units/warden', 'units/scout (placeholder)'] });
  assert.deepEqual(noImage, ['units/no-art.glb']);
  assert.deepEqual(out.notMadeYet, { 'units/scout.glb': { image: 'art-src/units/scout.png', standIn: 'units/warden.glb', usedBy: ['units/scout'] } });
  assert.deepEqual(out.noOriginalOnThisMachine, { 'heroes/draconis-v2': 'runtime copy only' });
  assert.match(out.rule, /Regenerate: pnpm models:index --root /);
  await assert.rejects(indexOptions({ root, out: path.join(root, 'x.txt') }), /SOURCES\.json/);
  await assert.rejects(indexOptions({ root, 'url-base': '/a/' }), /models:prepare/);
});

test('blender: preset checks, a dry run plans Blender and the packager with the same game flags', async (t) => {
  const root = path.join(scratch(t), 'dragon-hold');
  assert.throws(() => blenderOptions({ root, 'art-src': path.join(root, 'elsewhere') }), /drop --art-src/);
  assert.deepEqual(parseFlags(['--kinds', 'units,enemies', '--dry-run'], BLENDER_FLAGS), { kinds: ['units', 'enemies'], 'dry-run': true });
  const base = { source: 'enemies/warden.glb', triangles: 6000, reviewed: true };
  assert.equal(validatePreset('enemies/warden', base, { contracts: CONTRACTS, kinds: ['enemies'] }).nose, '+Y');
  assert.throws(() => validatePreset('heroes/warden', { ...base, triangles: 9000 }, { contracts: CONTRACTS }), /key must be/, 'Space\'s four kinds by default');
  assert.throws(() => validatePreset('enemies/warden', { ...base, source: '../x.glb' }, { contracts: CONTRACTS, kinds: ['enemies'] }), /source/);
  assert.throws(() => validatePreset('enemies/warden', { ...base, triangles: 100 }, { contracts: CONTRACTS, kinds: ['enemies'] }), /triangles/);

  put(root, 'art-src/3d/enemies/warden.glb', 'tripo warden');
  put(root, 'art-src/3d/enemies/stray.glb', 'nobody reads me');
  put(root, 'scripts/models/presets/campaign3d-models.json', JSON.stringify({ version: 1, models: {
    'enemies/warden': { ...base, rotate: [-1, 0, 0, 0, -1, 0, 0, 0, 1] }, 'enemies/missing': { ...base, source: 'enemies/missing.glb' },
  } }));
  const lines = [];
  const options = { ...blenderOptions({ root, kinds: ['enemies'], 'dry-run': true }), contractsModule: CONTRACTS, log: (line) => lines.push(line) };
  const { results, failures } = await prepare3DModels(options);
  assert.equal(failures, 1, 'the missing source counts');
  const planned = results.find((result) => result.key === 'enemies/warden');
  assert.equal(planned.status, 'planned');
  assert.equal(planned.args[planned.args.indexOf('--python') + 1], HELPER);
  assert.equal(planned.args[planned.args.indexOf('--project') + 1], root);
  assert.ok(planned.args.includes('--rotate=-1,0,0,0,-1,0,0,0,1'));
  assert.deepEqual(planned.packager, [PACKAGER, '--root', root, '--out', path.join(root, 'public/assets/dragon-hold/models'),
    '--url-base', '/assets/dragon-hold/models/', '--only', 'enemies/warden']);
  assert.ok(lines.some((line) => line.startsWith('UNREAD art-src/3d/enemies/stray.glb')));
  assert.ok(lines.some((line) => line.startsWith('MISSING enemies/missing')));
  await assert.rejects(prepare3DModels({ ...options, kinds: ['ponies'] }), /no model contract/);
  await assert.rejects(prepare3DModels({ ...options, kinds: ['units'] }), /Blender helper does not handle units/, 'a contract alone is not enough');
  assert.equal(readFileSync(HELPER, 'utf8'), readFileSync(path.join(SPACE, 'scripts/models/blender/space_typing_model_tools.py'), 'utf8'),
    'the Blender helper is the same file as Space\'s');
});

test('CLI: bad flags exit 2 before doing anything; --help exits 0', () => {
  for (const script of ['prepare-models.mjs', 'index-3d-sources.mjs', 'prepare-3d-models.mjs']) {
    const file = path.join(REPO_ROOT, 'scripts/models', script);
    const bad = spawnSync(process.execPath, [file, '--bogus'], { encoding: 'utf8' });
    assert.equal(bad.status, 2, `${script}: ${bad.stderr}`);
    assert.match(bad.stderr, /Unknown option: --bogus/);
    const help = spawnSync(process.execPath, [file, '--help'], { encoding: 'utf8' });
    assert.equal(help.status, 0, help.stderr);
    assert.match(help.stdout, /--root/);
  }
});
