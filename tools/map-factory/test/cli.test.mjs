import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { REPO_ROOT, FIXTURE_DIR } from '../adapters/extract.mjs';
import { KITS_DIR, REGISTRY_OUT_DIR, loadKits, checkKit, loadGameplays } from '../lib/spec-context.mjs';

const cli = path.join(REPO_ROOT, 'tools/map-factory/cli.mjs');
const root = path.join(REPO_ROOT, 'tools/map-factory');
const cache = path.join(root, '.cache/cli-test');
const readJson = file => JSON.parse(readFileSync(file, 'utf8'));
const digest = file => createHash('sha256').update(readFileSync(file)).digest('hex');
const run = (...args) => spawnSync(process.execPath, [cli, ...args], { cwd: REPO_ROOT, encoding: 'utf8' });
const samples = [
  ['typing-defense/w1-silverfall', 'd304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16', '4c60f45b2eaaf8d8b56124eb0ffad60102510f4dacfd8d033a52a60b2da799a0'],
  ['dragon-hold/L2-cau', 'e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83', '2d4620366e5942352f8eee34a7e2dc853b8746e85bdfbea1964dee0f43e26030'],
];
const badCases = [
  [
    "fractional-number",
    "not-integer",
    "/layers/water/streams/0/wobbleCm",
    "193be3e3f5a1f460009efd4e1353c3dce9cccc7e8f4fb267354e6397e61630dd"
  ],
  [
    "density-over-1000",
    "permille-range",
    "/layers/vegetation/groves/densityPermille",
    "3b9eb49201b8dd62b3f65da14f9f9381ab3bb6fd18a1518dd96e4cbfef39e39a"
  ],
  [
    "unknown-proto",
    "proto-unknown",
    "/layers/vegetation/groves/mix/pine-giant",
    "559d3eda596ff2551cdb07096c53c467dfa5a10ffb769228966e145348fc1254"
  ],
  [
    "gameplay-hash-mismatch",
    "gameplay-hash-mismatch",
    "/gameplay/hash",
    "7436981da69c115b957d741b40c57016481a3125b6fe6282a67645596d689090"
  ],
  [
    "bad-pin-id",
    "pin-id-format",
    "/pins/0/keep",
    "c8cd22b18ae7389ccf38846a7cfb4facdc23694f3411001024415dc5ad48705b"
  ],
  [
    "missing-budget",
    "budget-missing",
    "/budget",
    "a099fd032dae6ad16b6df644cb4e1f45532a5e13de1820eb08da7498fc45346e"
  ],
  [
    "odd-cell",
    "cell-not-even",
    "/extent/cellCm",
    "ab61bbfd7da596abdc38bdc433cfade00f8d6a6850ba1ccd304e9173569355ea"
  ]
];


for (const [name, hash] of samples) {
  test(`CLI validates ${name} and repeats identical bytes`, () => {
    const dir = path.join(root, 'maps', name);
    const first = run('validate', dir);
    const second = run('validate', dir);
    assert.equal(first.status, 0, first.stderr);
    assert.equal(second.status, 0, second.stderr);
    assert.equal(first.stderr, '');
    assert.equal(second.stderr, '');
    assert.equal(first.stdout, `ok ${hash}\n`);
    assert.equal(first.stdout, second.stdout);
  });
}

for (const [name, code, pointer] of badCases) {
  test(`CLI reports exactly one error for ${name}`, () => {
    const dir = path.join(root, 'test/fixtures/bad-spec', name);
    const result = run('validate', dir);
    assert.equal(result.status, 1, result.stderr);
    assert.equal(result.stderr, '');
    assert.equal(result.stdout, `error ${code} ${JSON.stringify(pointer)}\n`);
  });
}

test('CLI reports spec-json for a malformed file', () => {
  const dir = path.join(cache, 'broken-json');
  mkdirSync(dir, { recursive: true });
  writeFileSync(path.join(dir, 'map.spec.json'), '{');
  const result = run('validate', dir);
  assert.equal(result.status, 1, result.stderr);
  assert.equal(result.stdout, 'error spec-json ""\n');
  assert.equal(result.stderr, '');
});

const sampleDir = path.join(root, 'maps/typing-defense/w1-silverfall');
for (const args of [[], ['validate'], ['validate', sampleDir, 'extra'], ['build', sampleDir], ['check', sampleDir], ['validate', 'tools/map-factory/test/fixtures']]) {
  test(`CLI rejects arguments ${JSON.stringify(args)}`, () => {
    const result = run(...args);
    assert.equal(result.status, 2, result.stderr);
    assert.equal(result.stdout, '');
    assert.notEqual(result.stderr, '');
    if (args[0] === 'build' || args[0] === 'check') assert.match(result.stderr, /not implemented in map-spec\/0 \(ticket 032\)/);
    else if (args.length !== 2) assert.match(result.stderr, /Usage:/);
  });
}

test('kits contain the exact v0 proto lists and all model tiers', () => {
  const { kits, problems } = loadKits();
  assert.deepEqual(problems, []);
  assert.deepEqual(kits.map(({ kit, game, protos }) => [kit, game, protos.length]), [
    ['meadow@1', 'typing-defense', 18], ['pine-river@1', 'dragon-hold', 12],
  ]);
  const meadow = readJson(path.join(KITS_DIR, 'meadow.json'));
  assert.ok(Object.values(meadow.protos).every(proto => proto.asset === null));
  const pine = readJson(path.join(KITS_DIR, 'pine-river.json'));
  const assets = readJson(path.join(REGISTRY_OUT_DIR, 'assets.dragon-hold.json')).assets;
  for (const proto of Object.values(pine.protos)) for (const tier of ['high', 'medium']) {
    assert.ok(assets.some(asset => asset.source === 'runtime' && asset.id === `${proto.asset}.${tier}`));
  }
  assert.deepEqual(checkKit('pine-river.json', pine, assets), []);
  const altered = structuredClone(pine);
  altered.protos['pine-tall'].asset = 'm0b/props/pine-river-pine-giant/pine-river-pine-giant';
  assert.equal(checkKit('pine-river.json', altered, assets).length, 1);
  assert.ok(checkKit('river.json', pine, assets).length > 0);
  assert.ok(checkKit('pine-river.json', { ...pine, format: 'map-kit/1' }, assets).length > 0);
  assert.ok(checkKit('pine-river.json', { ...pine, protos: {} }, assets).length > 0);
});

test('checkKit rejects invalid structures and counts missing tiers once per proto', () => {
  const kit = { format: 'map-kit/0', kit: 'test@1', game: 'test', protos: { pine: { asset: 'pine' } } };
  for (const assets of [[], [{ source: 'runtime', id: 'pine.high' }], [{ source: 'original', id: 'pine.high' }, { source: 'runtime', id: 'pine.medium' }]]) {
    const problems = checkKit('test.json', kit, assets);
    assert.equal(problems.length, 1);
    assert.match(problems[0], /test.json/);
  }
  for (const protos of [null, [], { Pine: { asset: null } }, { pine: { asset: 5 } }, { pine: { asset: null, extra: true } }, { pine: {} }]) {
    assert.ok(checkKit('test.json', { ...kit, protos }, []).length > 0);
  }
  assert.ok(checkKit('test.json', kit, null).length > 0);
  assert.ok(checkKit('test.json', { ...kit, game: '../test' }, []).length > 0);
  assert.ok(checkKit('test.json', { ...kit, kit: 'Test@1' }, []).length > 0);
  assert.ok(checkKit('test.json', null, []).length > 0);
});

test('gameplay fixtures match all pinned reference fields and detect content tampering', () => {
  const { gameplays, problems } = loadGameplays();
  assert.deepEqual(problems, []);
  assert.deepEqual(gameplays, [
    { game: 'dragon-hold', map: 'L2-cau', adapter: 'dragon-hold@1', commit: '83da970eacbf85ea64da89f62a4d1b6622bc5c7b', hash: 'c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a' },
    { game: 'typing-defense', map: 'w1-silverfall', adapter: 'typing-defense@1', commit: '10ce627ff4e1c91f29e808cb658c086f51bd97d6', hash: '7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23' },
  ]);
  const dir = path.join(cache, 'gameplay');
  mkdirSync(dir, { recursive: true });
  const dragon = readJson(path.join(FIXTURE_DIR, 'dragon-hold.L2-cau.json'));
  assert.equal(dragon.dais.radiusCm, 400);
  dragon.dais.radiusCm = 401;
  writeFileSync(path.join(dir, 'dragon-hold.L2-cau.json'), JSON.stringify(dragon));
  const altered = loadGameplays(dir);
  assert.equal(altered.problems.length, 1);
  assert.deepEqual(altered.gameplays, []);
});

test('context loaders return read, parse, registry and duplicate errors without throwing', () => {
  assert.equal(loadGameplays(path.join(cache, 'absent-gameplay')).problems.length, 1);
  assert.equal(loadKits(path.join(cache, 'absent-kits')).problems.length, 1);
  const broken = path.join(cache, 'broken-context');
  mkdirSync(broken, { recursive: true });
  writeFileSync(path.join(broken, 'broken.json'), '{');
  assert.equal(loadGameplays(broken).problems.length, 1);
  assert.equal(loadKits(broken).problems.length, 1);
  const kitsDir = path.join(cache, 'duplicate-kits');
  const registryDir = path.join(cache, 'registries');
  mkdirSync(kitsDir, { recursive: true });
  mkdirSync(registryDir, { recursive: true });
  const meadow = readFileSync(path.join(KITS_DIR, 'meadow.json'));
  writeFileSync(path.join(kitsDir, 'meadow.json'), meadow);
  writeFileSync(path.join(kitsDir, 'duplicate.json'), meadow);
  writeFileSync(path.join(registryDir, 'assets.typing-defense.json'), '{"assets":[]}');
  assert.ok(loadKits(kitsDir, registryDir).problems.some(problem => problem.includes('duplicate kit meadow@1')));
  const missing = loadKits(kitsDir, path.join(cache, 'absent-registry'));
  assert.ok(missing.problems.some(problem => problem.includes('assets.typing-defense.json')));
});

test('all eleven spec and kit files match the ticket byte hashes', () => {
  for (const [name, , hash] of samples) assert.equal(digest(path.join(root, 'maps', name, 'map.spec.json')), hash);
  for (const [name, , , hash] of badCases) assert.equal(digest(path.join(root, 'test/fixtures/bad-spec', name, 'map.spec.json')), hash);
  assert.equal(digest(path.join(KITS_DIR, 'meadow.json')), 'ffe6a5eac17e103509f29e90615bc31e57e551c9a7f8177a644ab6dca8b954da');
  assert.equal(digest(path.join(KITS_DIR, 'pine-river.json')), 'f8e574c5e4abc773ec3204f912af218d05f24ce13257773db974e9d8bc0ee73a');
});
