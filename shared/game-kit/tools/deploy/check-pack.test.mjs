import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import {
  appendFileSync, closeSync, ftruncateSync, mkdirSync, mkdtempSync,
  openSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync,
} from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';
import { checkPack } from './check-pack.mjs';

const gameId = 'dragon-hold';
const cli = fileURLToPath(new URL('./check-pack.mjs', import.meta.url));
const js = 'assets/index-abc123.js';
const modelRoot = `assets/${gameId}/models`;
const modelManifest = `${modelRoot}/manifest.json`;
const high = `${modelRoot}/dragon.high.glb`;
const medium = `${modelRoot}/dragon.medium.glb`;
const hash = (bytes) => createHash('sha256').update(bytes).digest('hex');

function put(dir, path, bytes) {
  const target = join(dir, path);
  mkdirSync(dirname(target), { recursive: true });
  writeFileSync(target, bytes);
}

function fixture(t) {
  const dir = mkdtempSync(join(tmpdir(), 'check-pack-111-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  put(dir, 'index.html', '<script src="/assets/index-abc123.js"></script>');
  put(dir, js, 'console.log("ready");');
  put(dir, 'vocabulary/index.json', JSON.stringify({ levels: [{ file: 'levels/001.json' }] }));
  put(dir, 'vocabulary/levels/001.json', '[{"word":"river"}]\n');
  put(dir, 'vocabulary/ATTRIBUTION.md', 'Nguồn từ vựng thử nghiệm.\n');
  const files = Object.fromEntries(['index.json', 'levels/001.json', 'ATTRIBUTION.md']
    .map((path) => [path, hash(readFileSync(join(dir, 'vocabulary', path)))]));
  put(dir, 'vocabulary/vocab-manifest.json', JSON.stringify({ version: 1, files }));
  put(dir, modelManifest, JSON.stringify({ models: { dragon: { tiers: {
    high: { url: `/${high}?v=123#mesh` },
    medium: { url: './dragon.medium.glb?v=456' },
  } } } }));
  put(dir, high, 'glTF-high');
  put(dir, medium, 'glTF-medium');
  return dir;
}

function result(dir, budgets) {
  return checkPack(dir, { gameId, budgets });
}

function hasCode(dir, code, budgets) {
  const checked = result(dir, budgets);
  assert.equal(checked.ok, false);
  const problems = checked.problems.filter((problem) => problem.code === code);
  assert.ok(problems.length > 0, `Expected ${code}: ${JSON.stringify(checked)}`);
  for (const problem of problems) {
    assert.equal(typeof problem.path, 'string');
    assert.equal(typeof problem.detail, 'string');
    assert.ok(problem.detail.length > 0);
  }
  return problems;
}

test('clean package passes every gate and reports exact file and byte totals', (t) => {
  const dir = fixture(t);
  const totals = { files: 0, bytes: 0 };
  function count(path) {
    for (const item of readdirSync(path, { withFileTypes: true })) {
      const next = join(path, item.name);
      if (item.isDirectory()) count(next);
      else { totals.files++; totals.bytes += statSync(next).size; }
    }
  }
  count(dir);
  assert.deepEqual(result(dir), {
    ok: true, problems: [], report: {
      ...totals, localHost: 0, vocabularyNotShipped: { count: 0, examples: [] }, external: [],
    },
  });
});

test('file-too-big rejects a sparse 26 MiB file', (t) => {
  const dir = fixture(t);
  const fd = openSync(join(dir, 'large.glb'), 'w');
  try { ftruncateSync(fd, 26 * 1024 * 1024); } finally { closeSync(fd); }
  assert.equal(hasCode(dir, 'file-too-big')[0].path, 'large.glb');
});

test('file-too-big accepts exactly 25 MiB', (t) => {
  const dir = fixture(t);
  const fd = openSync(join(dir, 'limit.glb'), 'w');
  try { ftruncateSync(fd, 25 * 1024 * 1024); } finally { closeSync(fd); }
  assert.equal(result(dir).ok, true);
});

test('too-many-files accepts 19,999 and rejects exactly 20,000 files', (t) => {
  const dir = fixture(t);
  const initial = result(dir).report.files;
  for (let i = initial; i < 19_999; i++) put(dir, `small/${i}`, '');
  assert.equal(result(dir).ok, true);
  put(dir, 'small/last', '');
  assert.equal(result(dir).report.files, 20_000);
  hasCode(dir, 'too-many-files');
});

test('budgets override file bytes and the exclusive file count limit', (t) => {
  const dir = fixture(t);
  hasCode(dir, 'file-too-big', { maxFileBytes: 1 });
  const count = result(dir).report.files;
  hasCode(dir, 'too-many-files', { maxFiles: count });
  assert.equal(result(dir, { maxFiles: count + 1 }).ok, true);
});

for (const path of ['art-src/x.png', 'nested/local-assets/x.png',
  'shared/music/track.ogg', 'nested/Dota-Sounds/attack.wav', '.DS_Store', 'assets/.DS_Store']) {
  test(`private-media rejects ${path}`, (t) => {
    const dir = fixture(t);
    put(dir, path, 'private');
    assert.equal(hasCode(dir, 'private-media')[0].path, path);
  });
}

test('private-media accepts similar public path names', (t) => {
  const dir = fixture(t);
  for (const path of ['art-src-public/x.png', 'not-local-assets/x.png',
    'shared/musical/x.ogg', 'Dota-Sounds-public/x.wav', 'DS_Store.txt']) put(dir, path, 'ok');
  assert.equal(result(dir).ok, true);
});

for (const ext of ['html', 'js', 'css', 'json']) {
  test(`foreign-asset rejects another game in .${ext}`, (t) => {
    const dir = fixture(t);
    put(dir, `foreign.${ext}`, '"/assets/space-typing/models/ship.glb"');
    hasCode(dir, 'foreign-asset');
  });
}

test('foreign-asset rejects every known foreign id', (t) => {
  const dir = fixture(t);
  for (const id of ['space-typing', 'typing-defense', 'typing-survival', 'immortality-cultivation']) {
    put(dir, js, `"/assets/${id}/models/manifest.json"`);
    hasCode(dir, 'foreign-asset');
  }
});

test('foreign-asset accepts own assets, Vite hashes and unknown namespaces', (t) => {
  const dir = fixture(t);
  put(dir, js, `"/assets/${gameId}/x.png"; "/assets/index-abc123.js"; "/assets/custom/x.png"`);
  assert.equal(result(dir).ok, true);
});

test('foreign-asset only scans the specified text extensions', (t) => {
  const dir = fixture(t);
  put(dir, 'example.glb', '"/assets/space-typing/models/example.glb"');
  assert.equal(result(dir).ok, true);
});

test('local-host rejects the root and game subdomains and omits them from external', (t) => {
  const dir = fixture(t);
  put(dir, js, '"https://typing-game.local"; "https://dh.typing-game.local/x"');
  hasCode(dir, 'local-host');
  assert.equal(result(dir).report.localHost, 2);
  assert.deepEqual(result(dir).report.external, []);
});

test('local-host API allows local hosts and counts every occurrence across text files', (t) => {
  const dir = fixture(t);
  put(dir, js, '"https://typing-game.local"; "https://dh.typing-game.local/x"');
  put(dir, 'style.css', '/* https://TYPING-GAME.LOCAL */');
  const checked = checkPack(dir, { gameId, allowLocalHost: true });
  assert.equal(checked.ok, true);
  assert.deepEqual(checked.problems, []);
  assert.equal(checked.report.localHost, 3);
  assert.deepEqual(checked.report.external, []);
  assert.equal(result(dir).ok, false);
  assert.equal(result(dir).report.localHost, 3);
});

test('local-host accepts a production host', (t) => {
  const dir = fixture(t);
  put(dir, js, '"https://play.example.org/"');
  assert.equal(result(dir).ok, true);
});

for (const prefix of ['assets', 'vocabulary', 'shared']) {
  for (const quote of ['"', "'"]) {
    test(`parent-path rejects ${quote}../${prefix}/`, (t) => {
      const dir = fixture(t);
      put(dir, js, `${quote}../${prefix}/file${quote}`);
      hasCode(dir, 'parent-path');
    });
  }
}

test('parent-path accepts package root and manifest-relative model paths', (t) => {
  const dir = fixture(t);
  put(dir, js, '"/assets/index-abc123.js"; "/vocabulary/index.json"; "./shared/x"');
  assert.equal(result(dir).ok, true);
});

test('missing-vocabulary rejects a missing index level', (t) => {
  const dir = fixture(t);
  rmSync(join(dir, 'vocabulary/levels/001.json'));
  assert.ok(hasCode(dir, 'missing-vocabulary').some((p) => p.detail.includes('levels/001.json')));
});

test('missing-vocabulary rejects a one-byte content change', (t) => {
  const dir = fixture(t);
  const path = join(dir, 'vocabulary/levels/001.json');
  const bytes = readFileSync(path);
  bytes[bytes.indexOf('r')] = 'l'.charCodeAt(0);
  writeFileSync(path, bytes);
  assert.ok(hasCode(dir, 'missing-vocabulary').some((p) => p.detail.includes('sha256')));
});

test('missing-vocabulary accepts matching sha256 files', (t) => {
  assert.equal(result(fixture(t)).ok, true);
});

function threeLevelVocabulary(t) {
  const dir = fixture(t);
  const levels = Array.from({ length: 100 }, (_, i) => ({
    file: `levels/${String(i + 1).padStart(3, '0')}.json`,
  }));
  put(dir, 'vocabulary/index.json', JSON.stringify({ levels }));
  put(dir, 'vocabulary/levels/002.json', '[{"word":"forest"}]\n');
  put(dir, 'vocabulary/levels/003.json', '[{"word":"mountain"}]\n');
  const paths = ['index.json', 'ATTRIBUTION.md', ...levels.slice(0, 3).map((level) => level.file)];
  const files = Object.fromEntries(paths.map((path) => [
    path, hash(readFileSync(join(dir, 'vocabulary', path))),
  ]));
  put(dir, 'vocabulary/vocab-manifest.json', JSON.stringify({ version: 1, files }));
  return dir;
}

test('missing-vocabulary accepts a 3 level manifest with a 100 level pinned index', (t) => {
  const checked = result(threeLevelVocabulary(t));
  assert.equal(checked.ok, true, JSON.stringify(checked.problems));
  assert.deepEqual(checked.problems, []);
  assert.deepEqual(checked.report.vocabularyNotShipped, {
    count: 97,
    examples: ['levels/004.json', 'levels/005.json', 'levels/006.json',
      'levels/007.json', 'levels/008.json'],
  });
});

test('missing-vocabulary only reports unshipped files absent from the manifest', (t) => {
  const dir = threeLevelVocabulary(t);
  put(dir, 'vocabulary/levels/004.json', '[{"word":"lake"}]\n');
  rmSync(join(dir, 'vocabulary/levels/003.json'));
  const checked = result(dir);
  assert.equal(checked.ok, false);
  assert.deepEqual(checked.problems.map((p) => p.code), ['missing-vocabulary']);
  assert.equal(checked.problems[0].path, 'vocabulary/vocab-manifest.json');
  assert.match(checked.problems[0].detail, /levels\/003\.json/);
  assert.deepEqual(checked.report.vocabularyNotShipped, {
    count: 96,
    examples: ['levels/005.json', 'levels/006.json', 'levels/007.json',
      'levels/008.json', 'levels/009.json'],
  });
});

test('missing-vocabulary rejects a missing manifest level even when absent from the index', (t) => {
  const dir = fixture(t);
  const path = 'vocabulary/vocab-manifest.json';
  const manifest = JSON.parse(readFileSync(join(dir, path), 'utf8'));
  manifest.files['levels/002.json'] = hash('required level');
  put(dir, path, JSON.stringify(manifest));
  const problems = hasCode(dir, 'missing-vocabulary');
  assert.equal(problems[0].path, path);
  assert.match(problems[0].detail, /levels\/002\.json/);
});

test('missing-vocabulary still checks index levels without a hash manifest', (t) => {
  const dir = fixture(t);
  rmSync(join(dir, 'vocabulary/vocab-manifest.json'));
  assert.equal(result(dir).ok, true);
  rmSync(join(dir, 'vocabulary/levels/001.json'));
  hasCode(dir, 'missing-vocabulary');
});

test('missing-vocabulary checks manifest entries even without an index', (t) => {
  const dir = fixture(t);
  rmSync(join(dir, 'vocabulary/index.json'));
  hasCode(dir, 'missing-vocabulary');
});

test('missing-vocabulary rejects malformed JSON and invalid manifest shapes', (t) => {
  const dir = fixture(t);
  for (const value of ['{', 'null', '{"levels":{}}', '{"levels":[{}]}']) {
    put(dir, 'vocabulary/index.json', value);
    hasCode(dir, 'missing-vocabulary');
  }
  for (const value of ['{', 'null', '{"files":[]}', '{"files":{"levels/001.json":"bad"}}']) {
    put(dir, 'vocabulary/vocab-manifest.json', value);
    hasCode(dir, 'missing-vocabulary');
  }
});

test('missing-attribution rejects a missing attribution file', (t) => {
  const dir = fixture(t);
  rmSync(join(dir, 'vocabulary/ATTRIBUTION.md'));
  hasCode(dir, 'missing-attribution');
});

test('missing-attribution accepts attribution or an absent vocabulary directory', (t) => {
  const dir = fixture(t);
  assert.equal(result(dir).ok, true);
  rmSync(join(dir, 'vocabulary'), { recursive: true });
  assert.equal(result(dir).ok, true);
});

test('missing-attribution rejects an empty vocabulary directory', (t) => {
  const dir = fixture(t);
  rmSync(join(dir, 'vocabulary'), { recursive: true });
  mkdirSync(join(dir, 'vocabulary'));
  hasCode(dir, 'missing-attribution');
});

for (const path of [high, medium]) {
  test(`missing-model rejects absent ${path}`, (t) => {
    const dir = fixture(t);
    rmSync(join(dir, path));
    hasCode(dir, 'missing-model');
  });
}

test('missing-model accepts absolute and relative URLs with query and fragment', (t) => {
  assert.equal(result(fixture(t)).ok, true);
});

test('missing-model finds nested manifests and percent-encoded relative filenames', (t) => {
  const dir = fixture(t);
  put(dir, `${modelRoot}/nested/dragon high.glb`, 'glTF');
  put(dir, `${modelRoot}/nested/manifest.json`, JSON.stringify({ models: { x: {
    tiers: { high: { url: './dragon%20high.glb?v=1#scene' } },
  } } }));
  assert.equal(result(dir).ok, true);
  rmSync(join(dir, `${modelRoot}/nested/dragon high.glb`));
  hasCode(dir, 'missing-model');
});

test('missing-model reports external model URLs without treating them as local missing files', (t) => {
  const dir = fixture(t);
  put(dir, modelManifest, JSON.stringify({ models: { x: {
    tiers: { high: { url: 'https://cdn.example.org/model.glb' } },
  } } }));
  assert.equal(result(dir).ok, true);
  assert.deepEqual(result(dir).report.external, [{ host: 'cdn.example.org', count: 1 }]);
});

test('missing-model ignores unrelated manifests without models', (t) => {
  const dir = fixture(t);
  put(dir, `${modelRoot}/metadata/manifest.json`, '{"version":1}');
  assert.equal(result(dir).ok, true);
});

test('missing-model rejects malformed models manifests and unusable URLs', (t) => {
  const dir = fixture(t);
  for (const value of ['{', '{"models":null}', '{"models":{"x":{"tiers":{"high":{"url":42}}}}}',
    '{"models":{"x":{"tiers":{"high":{"url":"../../../../outside.glb"}}}}}']) {
    put(dir, modelManifest, value);
    hasCode(dir, 'missing-model');
  }
});

test('external groups both protocols by host and counts occurrences across files', (t) => {
  const dir = fixture(t);
  put(dir, js, '"https://cdn.example.org/a"; "http://cdn.example.org/b"; "https://z.example.org/c"');
  put(dir, 'style.css', '/* https://cdn.example.org/d */');
  assert.deepEqual(result(dir).report.external, [
    { host: 'cdn.example.org', count: 3 }, { host: 'z.example.org', count: 1 },
  ]);
  assert.equal(result(dir).ok, true);
});

test('external excludes SVG/XML namespace host www.w3.org', (t) => {
  const dir = fixture(t);
  put(dir, js, '"http://www.w3.org/2000/svg"; "http://www.w3.org/XML/1998/namespace"');
  assert.equal(result(dir).ok, true);
  assert.deepEqual(result(dir).report.external, []);
});

test('API rejects invalid game ids, invalid budgets and nonexistent package directories', (t) => {
  const dir = fixture(t);
  assert.throws(() => checkPack(dir, { gameId: 'unknown' }));
  assert.throws(() => checkPack(dir, { gameId, budgets: { maxFiles: 0 } }));
  assert.throws(() => checkPack(dir, { gameId, budgets: { maxFileBytes: NaN } }));
  assert.throws(() => result(join(dir, 'missing')));
});

function run(args) {
  const child = spawnSync(process.execPath, [cli, ...args], { encoding: 'utf8' });
  assert.ifError(child.error);
  return child;
}

test('CLI --allow-local-host allows the demo host while the default still rejects it', (t) => {
  const dir = fixture(t);
  put(dir, js, '"https://typing-game.local"; "https://typing-game.local/portal"');
  const args = [dir, '--game', gameId, '--json'];
  const allowed = run([...args, '--allow-local-host']);
  assert.equal(allowed.status, 0);
  assert.equal(allowed.stderr, '');
  assert.equal(JSON.parse(allowed.stdout).ok, true);
  assert.equal(JSON.parse(allowed.stdout).report.localHost, 2);
  assert.deepEqual(JSON.parse(allowed.stdout), checkPack(dir, { gameId, allowLocalHost: true }));
  assert.equal(run([dir, '--allow-local-host', '--game', gameId]).status, 0);
  const rejected = run(args);
  assert.equal(rejected.status, 1);
  assert.equal(JSON.parse(rejected.stdout).report.localHost, 2);
  assert.deepEqual(JSON.parse(rejected.stdout).problems.map((p) => p.code), ['local-host']);
});

test('CLI --allow-local-host still rejects other package errors', (t) => {
  const dir = fixture(t);
  put(dir, js, '"https://typing-game.local"; "/assets/space-typing/model.glb"');
  const child = run([dir, '--game', gameId, '--allow-local-host', '--json']);
  assert.equal(child.status, 1);
  const checked = JSON.parse(child.stdout);
  assert.equal(checked.report.localHost, 1);
  assert.deepEqual(checked.problems.map((p) => p.code), ['foreign-asset']);
});

test('CLI exits 0 with JSON for a clean package and 1 with one line per problem', (t) => {
  const dir = fixture(t);
  let child = run([dir, '--game', gameId, '--json']);
  assert.equal(child.status, 0);
  assert.deepEqual(JSON.parse(child.stdout), result(dir));
  assert.equal(child.stderr, '');
  assert.equal(run([dir, '--game', gameId]).stdout, '');
  appendFileSync(join(dir, js), '\n"/assets/space-typing/x"; "https://dh.typing-game.local"');
  child = run([dir, '--game', gameId]);
  assert.equal(child.status, 1);
  assert.equal(child.stdout.trim().split('\n').length, result(dir).problems.length);
  assert.match(child.stdout, /foreign-asset/);
  assert.match(child.stdout, /local-host/);
  child = run([dir, '--game', gameId, '--json']);
  assert.equal(child.status, 1);
  assert.equal(JSON.parse(child.stdout).ok, false);
});

test('CLI exits 2 for missing, unknown, duplicate or unusable arguments', (t) => {
  const dir = fixture(t);
  for (const args of [[], [dir], [dir, '--game'], [dir, '--game', 'unknown'],
    [dir, '--game', gameId, '--wat'], [dir, '--game', gameId, 'extra'],
    [dir, '--game', gameId, '--game', gameId], [dir, '--game', gameId, '--json', '--json'],
    [dir, '--game', gameId, '--allow-local-host', '--allow-local-host'],
    [join(dir, 'missing'), '--game', gameId], [join(dir, js), '--game', gameId]]) {
    const child = run(args);
    assert.equal(child.status, 2, JSON.stringify(args));
    assert.ok(child.stderr.length > 0);
  }
});
