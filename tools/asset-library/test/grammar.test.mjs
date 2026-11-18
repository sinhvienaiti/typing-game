import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { parsePath, groupFiles } from '../lib/grammar.mjs';

const root = fileURLToPath(new URL('../../../', import.meta.url));
const read = path => readFileSync(join(root, path), 'utf8');
const json = path => JSON.parse(read(path));
let taxonomy;
try { taxonomy = json('library/taxonomy.json'); } catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
const defenseCtx = taxonomy ? { game: 'typing-defense', taxonomy } : { hyphenVariants: ['scenery/**'] };
const herbPaths = read('tools/asset-library/test/fixtures/grammar/herb-hut.txt').trim().split('\n')
  .map(path => path.replace(/^games\/dragon-hold\/art-src\//u, ''));
const herbCtx = {
  sources: json('games/dragon-hold/art-src/3d/SOURCES.json'),
  preset: json('games/dragon-hold/scripts/models/presets/dragon-hold-m0b.json'),
};
const tally = files => files.reduce((counts, { role }) => ({ ...counts, [role]: (counts[role] ?? 0) + 1 }), {});
const row = (path, expected, ctx) => {
  const actual = parsePath(path, ctx);
  for (const [key, value] of Object.entries(expected)) assert.deepEqual(actual[key], value, `${path} · ${key}`);
};
function namesIn(game) {
  const base = join(root, 'games', game, 'art-src');
  // Không đi theo symlink, không đọc nội dung media hay stat từng file.
  function walk(folder, prefix = '') {
    return readdirSync(folder, { withFileTypes: true }).flatMap(entry => {
      const path = prefix + entry.name;
      if (entry.isDirectory()) return walk(join(folder, entry.name), path + '/');
      return entry.isFile() ? [path] : [];
    });
  }
  return walk(base).sort();
}

test('1 · Herb Hut: fixture thật 32 tên, một stem và đúng từng vai trò', t => {
  const actual = namesIn('dragon-hold').filter(path => /herb-hut/iu.test(path));
  assert.equal(herbPaths.length, 32);
  assert.deepEqual(actual, [...herbPaths].sort(), 'Fixture phải khớp danh sách tên thật');
  const cards = groupFiles(herbPaths, herbCtx);
  assert.equal(cards.length, 1);
  assert.equal(cards[0].stem, 'houses/herb-hut');
  const expected = {
    concept: 1, 'tripo-source': 1, 'glb-original': 1, 'glb-processed': 1,
    icon: 1, 'icon-256': 1, 'icon-64': 1, rejected: 9, prompt: 14, report: 2,
  };
  assert.deepEqual(tally(cards[0].files), expected);
  for (const path of herbPaths) assert.equal(parsePath(path, herbCtx).stem, 'houses/herb-hut', path);
  t.diagnostic(`32 tên → ${cards.length} stem houses/herb-hut; ${JSON.stringify(expected)}`);
});

test('2 · Nháp dấu chấm khác biến thể dấu nối; tổ hợp bamboo-clump-v1.v1', t => {
  row('scenery/meadow/bamboo-clump-v1.v1.png', {
    stem: 'scenery/meadow/bamboo-clump', role: 'draft', variant: 'a',
  }, defenseCtx);
  for (const ending of ['v1', 'v27', 'try2']) {
    row(`houses/hut.${ending}.tripo.alpha.png`, { stem: 'houses/hut', role: 'draft', variant: null });
  }
  row('scenery/meadow/bamboo-clump-v2.png', { stem: 'scenery/meadow/bamboo-clump', role: 'concept', variant: 'b' }, defenseCtx);
  row('buildings/barracks-v2.png', { stem: 'buildings/barracks-v2', role: 'concept', variant: null }, defenseCtx);
  row('scenery-other/bamboo-v1.png', { stem: 'scenery-other/bamboo-v1', variant: null }, { hyphenVariants: ['scenery/**'] });
  row('scenery/disabled/bamboo-v1.png', { variant: null }, {
    game: 'sample', taxonomy: { folderMap: { sample: { scenery: { hyphenVariants: true }, 'scenery/disabled': { hyphenVariants: false } } } },
  });
  row('art-src/3d/scenery/meadow/bamboo-clump-v1.glb', { stem: 'scenery/meadow/bamboo-clump', variant: 'a', role: 'glb-original' }, defenseCtx);
  row('scenery/bamboo-v27.png', { variant: 'aa' }, { hyphenVariants: true });
  row('scenery/bamboo-v0.png', { stem: 'scenery/bamboo-v0', variant: null }, { hyphenVariants: true });
  t.diagnostic(taxonomy ? 'Dùng cờ hyphenVariants từ taxonomy.json đã có' : 'Không có taxonomy.json: dùng cờ thư mục giả');
});

test('Sidecar giữ prompt, mã phiếu và stem qua mọi thứ tự hậu tố', () => {
  for (const suffix of ['tripo.rejected-012c', 'rejected-012c.tripo', 'tripo.v1.rejected-012c.alpha']) {
    row(`houses/herb-hut.${suffix}.png`, { stem: 'houses/herb-hut', role: 'rejected', ticket: '012c' });
    row(`houses/herb-hut.${suffix}.prompt.txt`, { stem: 'houses/herb-hut', role: 'prompt', ticket: '012c' });
  }
  row('houses/herb-hut.png.prompt.txt', { stem: 'houses/herb-hut', role: 'prompt' });
  row('icons/normalized/herb-hut.rejected-012.64.prompt.txt', {
    stem: 'houses/herb-hut', role: 'prompt', ticket: '012', size: 64,
  }, herbCtx);
});

test('Tripo, multiview và tám hậu tố phái sinh', () => {
  row('houses/hut.tripo.png', { stem: 'houses/hut', role: 'tripo-source' });
  for (const view of ['front', 'back', 'left']) for (const extra of ['', '.alpha', '.flat']) {
    row(`houses/hut_${view}${extra}.png`, { stem: 'houses/hut', role: 'multiview', view });
  }
  for (const suffix of ['alpha', 'flat', 'padded', 'seamless', 'trim', 'crop', 'coal', 'fix']) {
    row(`ground/moss.${suffix}.png`, { stem: 'ground/moss', role: 'derivative' });
  }
  row('ground/moss.alpha.flat.trim.png', { stem: 'ground/moss', role: 'derivative' });
  row('houses/hut_front.tripo.alpha.prompt.txt', { stem: 'houses/hut', role: 'prompt', view: 'front' });
  // Ngữ pháp không tự đổi draft thành copy khi chưa có md5 (thuộc AL-06).
  row('props/wooden-jetty.try1.png', { stem: 'props/wooden-jetty', role: 'draft' });
});

test('Tripo spares: alt, r2, old, raw-download và r2-rejected', () => {
  for (const suffix of ['alt', 'r2', 'raw-download-2410']) {
    row(`tripo-spares/barracks.${suffix}.glb`, { stem: 'buildings/barracks', role: 'glb-spare' }, { stems: ['buildings/barracks'] });
  }
  row('tripo-spares/barracks-old.thatched-hut.glb', { stem: 'tripo-spares/barracks', role: 'glb-spare' });
  row('tripo-spares/barracks.r2-rejected.glb', { stem: 'tripo-spares/barracks', role: 'rejected', ticket: null });
  row('tripo-spares/barracks.r2-rejected.prompt.txt', { stem: 'tripo-spares/barracks', role: 'prompt' });
  row('props/bridge-old.png', { stem: 'props/bridge-old', role: 'concept' });
  row('3d/buildings/barracks.alt.glb', { stem: 'buildings/barracks.alt', role: 'glb-original' });
});

test('2 · Âm Kenney, VCSL: giữ số 0 đầu và gom đúng một bộ', t => {
  const click = groupFiles(Array.from({ length: 5 }, (_, i) => `click_00${i + 1}.ogg`));
  assert.equal(click.length, 1);
  assert.equal(click[0].stem, 'click');
  assert.deepEqual(click[0].files.map(file => file.variant), ['001', '002', '003', '004', '005']);
  assert.ok(click[0].files.every(file => file.role === 'variant'));
  const impacts = groupFiles(Array.from({ length: 5 }, (_, i) => `impactWood_light_00${i}.wav`));
  assert.equal(impacts.length, 1);
  assert.equal(impacts[0].stem, 'impactWood_light');
  assert.deepEqual(impacts[0].files.map(file => file.variant), ['000', '001', '002', '003', '004']);
  row('wood_click_f_rr1.wav', { stem: 'wood_click_f', role: 'variant', variant: 'rr1' });
  row('audio/select-1.ogg', { stem: 'audio/select', role: 'variant', variant: '1' });
  row('click1.mp3', { stem: 'click', role: 'variant', variant: '1' });
  row('click.wav', { stem: 'click', role: 'variant', variant: null });
  row('ui/click1.png', { stem: 'ui/click1', role: 'concept', variant: null });
  row('kits/barracks-1.png', { stem: 'kits/barracks-1', variant: null });
  t.diagnostic('click: 1 stem, 5 biến thể 001–005; impactWood_light: 1 stem, 5 biến thể 000–004; wood_click_f: rr1');
});

test('GLB đã xử lý và runtime nối qua preset, kể cả thư mục lặp id', () => {
  row('models/props/herb-hut.glb', { stem: 'houses/herb-hut', role: 'glb-processed' }, herbCtx);
  row('models/props/unmapped.glb', { stem: 'models/props/unmapped', role: 'glb-processed' }, herbCtx);
  for (const tier of ['high', 'medium']) for (const extra of ['', 'herb-hut/']) {
    row(`public/assets/dragon-hold/models/m0b/props/${extra}herb-hut.${tier}.glb`, {
      stem: 'houses/herb-hut', role: `runtime-${tier}`, tier,
    }, herbCtx);
  }
  row('models/props/herb-hut.glb', { stem: 'houses/herb-hut' }, { sources: herbCtx.sources });
  row('models/props/herb-hut.glb', { stem: 'new/herb-hut' }, {
    sources: herbCtx.sources, preset: { models: { 'props/herb-hut': { source: 'new/herb-hut.glb' } } },
  });
});

test('Space: chỉ trường image mới cho phép nối -2d; cả prompt và derivative', () => {
  const ctx = { sources: { files: { 'ships/ship-01-scout.glb': { image: 'art-src/ships/ship-01-scout-2d.png' } } } };
  for (const suffix of ['png', 'alpha.png', 'prompt.txt', 'tripo.prompt.txt']) {
    row(`ships/ship-01-scout-2d.${suffix}`, { stem: 'ships/ship-01-scout' }, ctx);
  }
  row('3d/ships/ship-01-scout.glb', { stem: 'ships/ship-01-scout', role: 'glb-original' }, ctx);
  row('ships/ship-01-scout-2d.png', { stem: 'ships/ship-01-scout-2d' });
  row('ships/other-2d.png', { stem: 'ships/other-2d' }, ctx);
});

test('Icon nối theo id duy nhất; id mơ hồ giữ thẻ riêng, links ghi đè tường minh', () => {
  const paths = ['houses/hut.png', '3d/houses/hut.glb', 'ui/icons/hut.prompt.txt', 'ui/icons/hut.png', 'icons/normalized/hut.64.png'];
  const cards = groupFiles(paths);
  assert.equal(cards.length, 1);
  assert.equal(cards[0].stem, 'houses/hut');
  const ambiguous = groupFiles([...paths, 'props/hut.png']);
  assert.equal(ambiguous.find(card => card.files.some(file => file.path === 'ui/icons/hut.png')).stem, 'ui/icons/hut');
  const ctx = { stems: ['houses/hut', 'props/hut'], links: { 'ui/icons/hut': 'houses/hut' } };
  row('ui/icons/hut.png', { stem: 'houses/hut', role: 'icon' }, ctx);
  row('icons/normalized/hut.256.png', { stem: 'icons/normalized/hut', role: 'icon-256', size: 256 }, ctx);
  row('icons/normalized/hut.128.png', { role: 'unknown', size: null });
  row('props/hut.64.png', { role: 'unknown', size: null });
});

test('Báo cáo, vùng review và unknown được giữ đúng vai trò', () => {
  for (const folder of ['_review', 'review-vs-buildings', '_from-downloads']) {
    row(`${folder}/hut.tripo.rejected-012.prompt.txt`, { role: 'review', ticket: '012' });
    row(`${folder}/run.py`, { role: 'review' });
  }
  row('README-models.md', { role: 'report' });
  for (const folder of ['.reports', '.campaign3d-model-cache']) {
    row(`models/${folder}/props__herb-hut.json`, { stem: 'houses/herb-hut', role: 'report' }, herbCtx);
  }
  row('models/.reports/enemies__wolf.rig.json', { stem: 'models/enemies/wolf', role: 'report' });
  for (const name of ['vs-buildings-run', 'vs-characters-run', 'vs-buildings-005b', 'vs-buildings-005b-continuation']) {
    row(`${name}.json`, { role: 'report' });
  }
  for (const path of ['other/file.bin', 'settings.json', 'notes.txt', 'scene.blend', 'vs-characters-config.json',
    'houses/hut.unlisted.png', 'review-vother/hut.json']) row(path, { role: 'unknown' });
});

test('Dữ liệu bất biến, đầu ra ổn định và đủ bảy trường; đường không hợp lệ bị từ chối', () => {
  function freeze(value) {
    if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); }
    return value;
  }
  const ctx = freeze(structuredClone(herbCtx));
  const paths = Object.freeze([...herbPaths]);
  assert.deepEqual(groupFiles(paths, ctx), groupFiles([...paths].reverse(), ctx));
  assert.deepEqual(groupFiles([...paths, paths[0]], ctx), groupFiles(paths, ctx));
  assert.deepEqual(groupFiles([], ctx), []);
  assert.deepEqual(parsePath('art-src\\houses\\hut.png'), {
    stem: 'houses/hut', role: 'concept', variant: null, ticket: null, size: null, view: null, tier: null,
  });
  for (const path of ['', '/houses/hut.png', 'D:\\typing-game\\hut.png', '../hut.png',
    'houses/../hut.png', 'houses//hut.png', './hut.png', 'hut.png\0', null]) {
    assert.throws(() => parsePath(path), TypeError, String(path));
  }
});

test('3 · Chỉ liệt kê tên thật của hai art-src; unknown không quá 1% và in hết', t => {
  for (const game of ['dragon-hold', 'typing-defense']) {
    const paths = namesIn(game);
    const ctx = { ...defenseCtx, game };
    const parsed = paths.map(path => ({ path, ...parsePath(path, ctx) }));
    const unknown = parsed.filter(file => file.role === 'unknown');
    const percentage = unknown.length / paths.length * 100;
    t.diagnostic(`${game}: ${paths.length} file; unknown ${unknown.length}/${paths.length} = ${percentage.toFixed(4)}%; vai trò ${JSON.stringify(tally(parsed))}`);
    for (const { path } of unknown) t.diagnostic(`unknown ${game}/art-src/${path}`);
    assert.ok(paths.length > 0);
    assert.ok(percentage <= 1, `${game}: unknown ${percentage.toFixed(4)}% > 1%`);
  }
});

test('K1 · Lớp bọc fs chặn ghi khi import; API chạy toàn bộ tên thật với 0 I/O', t => {
  const payload = {
    herbCtx, herbPaths, defenseCtx,
    games: Object.fromEntries(['dragon-hold', 'typing-defense'].map(game => [game, namesIn(game)])),
    cases: ['scenery/meadow/bamboo-clump-v1.v1.png', 'tripo-spares/barracks.r2-rejected.glb',
      'click_001.ogg', 'impactWood_light_000.wav', 'wood_click_f_rr1.wav', 'unknown.json'],
  };
  const moduleUrl = new URL('../lib/grammar.mjs', import.meta.url).href;
  const result = spawnSync(process.execPath, ['--input-type=module', '-e', `
    import fs from 'node:fs';
    import assert from 'node:assert/strict';
    import { syncBuiltinESMExports } from 'node:module';
    const data = JSON.parse(fs.readFileSync(0, 'utf8'));
    let writes = 0;
    let reads = 0;
    let forbidReads = false;
    const stopWrite = name => () => { writes++; throw new Error('Ghi bị chặn: ' + name); };
    for (const name of ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'symlink', 'unlink',
      'rm', 'rmdir', 'write', 'writev', 'truncate', 'ftruncate', 'link', 'mkdtemp', 'chmod', 'chown', 'utimes']) {
      for (const key of [name, name + 'Sync']) if (typeof fs[key] === 'function') fs[key] = stopWrite(key);
      if (typeof fs.promises[name] === 'function') fs.promises[name] = stopWrite('promises.' + name);
    }
    fs.createWriteStream = stopWrite('createWriteStream');
    for (const [object, name] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
      const original = object[name];
      object[name] = function(path, flags, ...args) {
        const writing = typeof flags === 'number'
          ? Boolean(flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_TRUNC | fs.constants.O_APPEND))
          : /[wa+]/u.test(flags ?? 'r');
        if (writing) return stopWrite(name)();
        if (forbidReads) { reads++; throw new Error('Mở đọc bị chặn: ' + name); }
        return original.call(this, path, flags, ...args);
      };
    }
    syncBuiltinESMExports();
    const api = await import(${JSON.stringify(moduleUrl)});
    forbidReads = true;
    for (const name of ['readFile', 'readdir', 'stat', 'lstat', 'access', 'realpath', 'readlink']) {
      for (const key of [name, name + 'Sync']) if (typeof fs[key] === 'function') fs[key] = () => { reads++; throw new Error('Đọc bị chặn: ' + key); };
      if (typeof fs.promises[name] === 'function') fs.promises[name] = () => { reads++; throw new Error('Đọc bị chặn: ' + name); };
    }
    fs.createReadStream = () => { reads++; throw new Error('Luồng đọc bị chặn'); };
    syncBuiltinESMExports();
    for (const [game, paths] of Object.entries(data.games)) {
      const ctx = { ...data.defenseCtx, game };
      for (const path of paths) api.parsePath(path, ctx);
      assert.equal(api.groupFiles(paths, ctx).flatMap(card => card.files).length, paths.length);
    }
    assert.equal(api.groupFiles(data.herbPaths, data.herbCtx).length, 1);
    for (const path of data.cases) api.parsePath(path, data.defenseCtx);
    assert.equal(writes, 0);
    assert.equal(reads, 0);
    console.log('Lời gọi ghi: ' + writes + '; lời gọi đọc trong API: ' + reads);
  `], { cwd: root, encoding: 'utf8', input: JSON.stringify(payload), timeout: 30_000 });
  assert.equal(result.status, 0, `${result.stdout}\n${result.stderr}`);
  assert.match(result.stdout, /Lời gọi ghi: 0; lời gọi đọc trong API: 0/u);
  t.diagnostic(result.stdout.trim());
});
