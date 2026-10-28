import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join, matchesGlob } from 'node:path';
import { spawnSync } from 'node:child_process';
import { load, resolve, related, kindFor, styleFor } from '../lib/taxonomy.mjs';

const root = fileURLToPath(new URL('../../../', import.meta.url));
const read = path => readFileSync(join(root, path), 'utf8');
const data = load();
const games = ['dragon-hold', 'typing-defense', 'typing-survival', 'space-typing'];
const sorted = value => Array.isArray(value) ? value.map(sorted)
  : value && typeof value === 'object'
    ? Object.fromEntries(Object.keys(value).sort().map(key => [key, sorted(value[key])])) : value;
const key = word => word.normalize('NFC').toLowerCase().trim().replace(/[\s_-]+/gu, ' ');
const ignored = name => name.startsWith('.') || name === '_review'
  || name.startsWith('review-vs') || name === '_from-downloads' || name === 'tmp';

test('1 · Đi thật các thư mục: mỗi thư mục có dòng ánh xạ riêng', t => {
  let count = 0;
  const visited = [];
  function directories(path, optional = false) {
    try {
      return readdirSync(join(root, path), { withFileTypes: true })
        .filter(entry => entry.isDirectory() && !ignored(entry.name)).map(entry => entry.name).sort();
    } catch (error) {
      if (optional && error.code === 'ENOENT') {
        t.diagnostic(`Bỏ qua gốc chưa tồn tại: ${path}`);
        return [];
      }
      throw error;
    }
  }
  function inspect(game, physical, logical, optional = false) {
    for (const name of directories(physical, optional)) {
      const mapped = logical ? `${logical}/${name}` : name;
      assert.ok(Object.hasOwn(data.folderMap[game], mapped), `Chưa ánh xạ: ${physical}/${name} → ${mapped}`);
      assert.ok(kindFor(game, mapped), mapped);
      visited.push(`${physical}/${name}`);
      count++;
    }
  }
  for (const game of games) {
    inspect(game, `games/${game}/art-src`, '');
    inspect(game, `games/${game}/art-src/3d`, '', true);
  }
  const split = {
    'dragon-hold': ['props', 'models', '2d'],
    'typing-defense': ['scenery', 'models'],
    'space-typing': ['models', 'expansion-v2', 'td', 'td/scenery'],
  };
  for (const [game, parents] of Object.entries(split)) {
    for (const parent of parents) inspect(game, `games/${game}/art-src/${parent}`, parent);
  }
  inspect('dragon-hold', 'games/dragon-hold/art-src/3d/props', 'props');
  for (const path of ['public/assets/audio', 'public/assets/audio/duel',
    'public/assets/audio/sfx', 'public/assets/audio/music', 'src/assets/audio']) {
    inspect('space-typing', `games/space-typing/${path}`, path);
  }
  for (const path of visited) t.diagnostic(`Đã đi: ${path}`);
  t.diagnostic(`Tổng thư mục được kiểm: ${count}`);
  assert.ok(count > 0);
});

test('2 · Nhóm đồng nghĩa không trùng; giữ từ vựng tripo-match với các tách nghĩa có chủ ý', t => {
  const seen = new Map();
  for (const group of data.synonyms) {
    for (const word of group) {
      assert.ok(!seen.has(key(word)), `Trùng: ${word} (${seen.get(key(word))}, ${group[0]})`);
      seen.set(key(word), group[0]);
    }
  }
  // Chỉ đọc dạng chữ; không import hay chạy CLI tripo-match.
  const literal = read('tools/tripo-match/match.mjs').match(/export const SYNONYMS = (\[[\s\S]*?\]);/u)?.[1];
  assert.ok(literal, 'Không tìm thấy bảng SYNONYMS');
  const original = JSON.parse(literal.replaceAll("'", '"').replace(/,\s*\]/gu, ']'));
  for (const group of original) {
    for (const word of group) {
      if (word === 'cau' || word === 'da') assert.ok(Object.hasOwn(data.viTokens, word));
      else assert.ok(seen.has(key(word)), `Thiếu alias gốc: ${word}`);
    }
  }
  assert.equal(Object.isFrozen(data.folderMap), true);
  assert.throws(() => { data.tags.push('changed'); }, TypeError);
  assert.throws(() => load({ fs: { readFileSync: () => JSON.stringify({
    ...data, synonyms: [['hut', 'chòi'], ['house', 'chòi']],
  }) } }), /bị trùng/u);
  t.diagnostic(`${data.synonyms.length} nhóm, ${seen.size} từ duy nhất`);
});

test('3 · Tìm tiếng Việt, tiếng Anh và quan hệ đối xứng', () => {
  for (const word of ['hut', 'chòi', 'choi', 'lều', 'leu', '  CHÒI ', 'chòi']) assert.equal(resolve(word), 'hut');
  assert.equal(resolve('nhà'), 'house');
  assert.equal(resolve('nha'), 'house');
  for (const word of ['jetty', 'pier', 'cầu tàu', 'cau-tau', 'cau_tau']) assert.equal(resolve(word), 'jetty');
  assert.equal(resolve('gõ'), 'click');
  assert.equal(resolve('gỗ'), 'wood');
  assert.equal(resolve('go'), 'wood');
  assert.equal(related('hut', 'house'), true);
  assert.equal(related('nhà', 'chòi'), true);
  assert.equal(related('dock', 'bridge'), true);
  assert.equal(related('click', 'knock'), true);
  assert.equal(related('hut', 'tree'), false);
  assert.equal(resolve('không có từ này'), null);
  assert.equal(resolve(null), null);
  assert.equal(resolve('constructor'), null);
  assert.equal(related('?', '?'), false);
});

test('4 · cau và da chỉ có nghĩa trong phạm vi thư mục cho phép', () => {
  for (const folder of ['typing-defense:landmarks', 'typing-defense:landmarks/',
    'typing-defense:art-src/landmarks', 'typing-defense:art-src/3d/landmarks/cau-go']) {
    assert.equal(resolve('cau', { folder }), 'bridge', folder);
  }
  for (const folder of [undefined, 'landmarks', 'typing-defense:landmarks-other',
    'dragon-hold:landmarks', 'typing-defense:scenery', 'typing-defense:landmarks/../props']) {
    assert.equal(resolve('cau', { folder }), null, String(folder));
  }
  for (const folder of ['scenery/', 'landmarks/', 'typing-defense:scenery/coast',
    'space-typing:art-src/td/scenery/meadow', 'typing-defense:3d/landmarks']) {
    assert.equal(resolve('da', { folder }), 'stone', folder);
  }
  for (const folder of [undefined, 'props', 'not-scenery/rock', 'typing-defense:houses']) {
    assert.equal(resolve('da', { folder }), null, String(folder));
  }
  assert.equal(resolve('đá'), 'stone');
});

test('5 · Đủ 9 họ và mọi nhóm âm AudioLab, chỉ đọc Python như văn bản', t => {
  const python = read('tools/audio-lab/specs/taxonomy.py');
  for (const [name, map, expected] of [['FAMILIES', data.audioFamilyMap, 9], ['CATEGORIES', data.audioCategoryMap, 16]]) {
    const block = python.match(new RegExp(`^${name}:[^\\n]*= \\{\\n([\\s\\S]*?)^\\}`, 'm'))?.[1];
    assert.ok(block, `Không tìm thấy ${name}`);
    const keys = [...block.matchAll(/^    "([^"]+)":/gmu)].map(match => match[1]);
    assert.ok(keys.length >= expected);
    for (const id of keys) assert.ok(Object.hasOwn(data.kinds.audio, map[id]), `Chưa ánh xạ ${name}.${id}`);
    assert.deepEqual(Object.keys(map).sort(), keys.sort());
    t.diagnostic(`${name}: ${keys.length}/${keys.length} có ánh xạ`);
  }
});

test('6 · Từ vựng đủ loại, đủ nhãn, nhỏ hơn 60 KB và tuần tự hóa ổn định từng byte', t => {
  assert.deepEqual(Object.keys(data.kinds.visual).sort(),
    'building structure nature prop character creature vehicle weapon projectile item trap vfx ui ground backdrop motion'.split(' ').sort());
  assert.deepEqual(Object.keys(data.kinds.audio).sort(),
    'ui typing reward shot impact explosion death creature voice ambience music stinger foley movement'.split(' ').sort());
  for (const group of Object.values(data.kinds)) for (const row of Object.values(group)) {
    assert.ok(row.label.length > 0);
    assert.ok(Object.keys(row.subkinds).length > 0);
    for (const label of Object.values(row.subkinds)) assert.ok(label.length > 0);
  }
  assert.ok(data.tags.length >= 120);
  assert.equal(new Set(data.tags).size, data.tags.length);
  assert.ok(data.tags.every(tag => /^[a-z][a-z0-9-]*$/u.test(tag)));
  const scanner = read('tools/map-factory/registry/scan-assets.mjs');
  const literal = scanner.match(/function inferTags\([^)]*\)[\s\S]*?const vocabulary = (\[[^;]+\]);/u)?.[1];
  assert.ok(literal, 'Không tìm thấy inferTags.vocabulary');
  const vocabulary = JSON.parse(literal.replaceAll("'", '"'));
  for (const word of vocabulary) assert.ok(data.tags.includes(word), `Thiếu nhãn inferTags: ${word}`);
  const raw = read('library/taxonomy.json');
  const bytes = Buffer.byteLength(raw);
  assert.ok(bytes <= 60_000, `${bytes} vượt 60 KB`);
  const serialized = JSON.stringify(sorted(JSON.parse(raw)), null, 2) + '\n';
  assert.equal(serialized, raw);
  assert.equal(JSON.stringify(sorted(JSON.parse(serialized)), null, 2) + '\n', raw);
  t.diagnostic(`16 loại hình/3D, 14 loại âm; ${data.tags.length} nhãn; ${vocabulary.length}/${vocabulary.length} inferTags; ${bytes} byte; tuần tự hóa bằng từng byte`);
});

test('Phân loại từng món, đường gương 3D, âm Space và phong cách', () => {
  const cases = [
    ['dragon-hold', 'art-src/houses/herb-hut.png', 'building'],
    ['dragon-hold', 'art-src/3d/props/pine-river/bridge-old.glb', 'structure'],
    ['dragon-hold', 'props/pine-river/wooden-jetty.tripo.png', 'structure'],
    ['dragon-hold', 'props/pine-river/rail-fence.png', 'prop'],
    ['dragon-hold', 'props/pine-river/reed-clump.png', 'nature'],
    ['typing-defense', '3d/landmarks/choi-canh-doi.glb', 'building'],
    ['typing-defense', 'landmarks/nha-rai-da.png', 'building'],
    ['typing-defense', 'landmarks/cau-tau.png', 'structure'],
    ['typing-defense', 'landmarks/vach-thac-bac.png', 'nature'],
    ['typing-defense', 'scenery/meadow/almond-tree-v2.png', 'nature'],
    ['space-typing', 'g01/g01-atlas-rocks.png', 'prop'],
    ['space-typing', 'g01/g01-glow-a.png', 'vfx'],
    ['space-typing', 'g01/g01-plate.png', 'backdrop'],
    ['space-typing', 'td/enemies/cuong-thi.png', 'creature'],
    ['space-typing', 'public/assets/audio/duel/war/railgun.ogg', 'shot'],
    ['space-typing', 'public/assets/audio/duel/war/explosion-a.ogg', 'explosion'],
    ['space-typing', 'public/assets/audio/dragon/roar.mp3', 'creature'],
    ['space-typing', 'public/assets/audio/sfx/kenney/crystal-hit.ogg', 'impact'],
    ['space-typing', 'public/assets/audio/announcer-base.wav', 'voice'],
    ['space-typing', 'src/assets/audio/ui/reward-big.ogg', 'reward'],
  ];
  for (const [game, path, expected] of cases) assert.equal(kindFor(game, path), expected, `${game}:${path}`);
  for (const path of ['../houses/x.png', '/art-src/houses/x.png', 'houses/../../x', 'houses-other/a.png', 'unknown/x.png']) {
    assert.equal(kindFor('dragon-hold', path), null, path);
  }
  assert.equal(kindFor('unknown', 'houses/x.png'), null);
  assert.equal(kindFor('toString', 'houses/x.png'), null);
  for (const [game, style] of Object.entries(data.gameStyles)) assert.equal(styleFor(game), style);
  assert.equal(styleFor('unknown'), null);
  assert.equal(data.folderMap['space-typing'].td.style, 'viet-village');
  for (const biome of ['coast', 'meadow', 'rainforest', 'shared']) {
    const row = data.folderMap['typing-defense'][`scenery/${biome}`];
    assert.equal(row.hyphenVariants, true);
    assert.deepEqual(row.biomes, [biome === 'shared' ? 'any' : biome]);
  }
  assert.equal(Object.keys(data.folderMap['typing-defense'].landmarks.items).length, 12);
  for (const [game, folders] of Object.entries(data.folderMap)) for (const [folder, row] of Object.entries(folders)) {
    const kinds = data.kinds[row.media === 'audio' ? 'audio' : 'visual'];
    assert.ok(Object.hasOwn(kinds, row.kind), `${game}:${folder}`);
    for (const item of Object.values(row.items ?? {})) {
      assert.ok(Object.hasOwn(kinds, item.kind));
      if (item.subkind) assert.ok(Object.hasOwn(kinds[item.kind].subkinds, item.subkind));
    }
  }
});

test('Nguồn quét, chặn vùng cấm và quyền giấy phép', () => {
  const sources = JSON.parse(read('library/sources.json'));
  const licences = JSON.parse(read('library/licences.json'));
  assert.equal(sources.roots.length, 16);
  for (const game of games) for (const part of ['art-src', 'public', 'src/assets']) {
    assert.ok(sources.roots.some(row => row.game === game && row.path === `games/${game}/${part}`));
  }
  for (const [path, mode] of [['~/AudioLab/libraries', 'catalog'], ['~/AudioLab/work', 'draft'],
    ['shared/music', 'private'], ['typing-game-handoff-2026-10-25', 'copies-only']]) {
    assert.equal(sources.roots.find(row => row.path === path)?.mode, mode);
  }
  // Chỉ dựng đường mẫu từ danh sách cấm; tuyệt đối không truy cập các đường này.
  const excludedGame = sources.deny.find(path => path.startsWith('games/') && !path.includes('monkeytype'));
  const excludedRoot = excludedGame.replace(/\/\*\*$/u, '');
  for (const path of [excludedRoot, `${excludedRoot}/asset.png`, 'games/monkeytype',
    'games/monkeytype/src/main.js',
    `typing-game-handoff-2026-10-25/copy/${excludedRoot.slice('games/'.length)}`,
    `typing-game-handoff-2026-10-25/copy/${excludedRoot.slice('games/'.length)}/asset.png`]) {
    assert.ok(sources.deny.some(glob => matchesGlob(path, glob)), path);
  }
  for (const path of ['tmp', 'a/tmp', '.wt-demo', 'a/dist', '.visual', '.media-tmp',
    'node_modules', 'library/browse', 'library/browse.new']) {
    for (const candidate of [path, `${path}/x`]) {
      assert.ok(sources.ignore.some(glob => matchesGlob(candidate, glob)), candidate);
    }
  }
  assert.deepEqual(Object.keys(licences).sort(), ['owner-tripo', 'owner-ai-2d', 'cc0-1.0', 'cc-by-4.0',
    'stability-community', 'repo-synth', 'unknown', 'private-producer', 'private-valve'].sort());
  for (const licence of Object.values(licences)) {
    for (const flag of ['commercialOk', 'aiInputAllowed', 'private', 'notForRelease']) assert.equal(typeof licence[flag], 'boolean');
    assert.ok(licence.attribution === null || typeof licence.attribution === 'string');
  }
  for (const id of ['unknown', 'private-producer', 'private-valve']) {
    assert.equal(licences[id].commercialOk, false);
    assert.equal(licences[id].aiInputAllowed, false);
    assert.equal(licences[id].notForRelease, true);
  }
  assert.ok(licences['cc-by-4.0'].attribution);
  const dota = data.folderMap['space-typing']['Dota-Sounds'];
  assert.equal(dota.private, true);
  assert.equal(dota.notForRelease, true);
  assert.equal(dota.licence, 'private-valve');
  assert.equal(read('library/.gitignore'), 'out/\n.thumbs/\n.cache/\nbrowse/\nbrowse.new/\nprivate/\n');
});

test('K1 · API chạy với lớp bọc fs: 0 lời gọi ghi', t => {
  const moduleUrl = new URL('../lib/taxonomy.mjs', import.meta.url).href;
  const result = spawnSync(process.execPath, ['--input-type=module', '-e', `
    import fs from 'node:fs';
    import { syncBuiltinESMExports } from 'node:module';
    let writes = 0;
    const stop = name => () => { writes++; throw new Error('Lời gọi ghi bị chặn: ' + name); };
    const mutations = ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'symlink',
      'unlink', 'rm', 'rmdir', 'write', 'writev', 'truncate', 'ftruncate', 'link', 'mkdtemp',
      'chmod', 'chown', 'utimes'];
    for (const name of mutations) {
      for (const method of [name, name + 'Sync']) if (typeof fs[method] === 'function') fs[method] = stop(method);
      if (typeof fs.promises[name] === 'function') fs.promises[name] = stop('promises.' + name);
    }
    fs.createWriteStream = stop('createWriteStream');
    for (const [object, name] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
      const original = object[name];
      object[name] = function(path, flags, ...args) {
        const writing = typeof flags === 'number'
          ? Boolean(flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_TRUNC | fs.constants.O_APPEND))
          : /[wa+]/u.test(flags ?? 'r');
        if (writing) return stop(name)();
        return original.call(this, path, flags, ...args);
      };
    }
    syncBuiltinESMExports();
    const api = await import(${JSON.stringify(moduleUrl)});
    const data = api.load({ fs });
    for (const group of data.synonyms) for (const word of group) api.resolve(word);
    for (const [token, row] of Object.entries(data.viTokens)) {
      api.resolve(token);
      for (const folder of row.folders) api.resolve(token, { folder });
    }
    for (const [a,b] of data.related) { api.related(a,b); api.related(b,a); }
    for (const [game, folders] of Object.entries(data.folderMap)) {
      api.styleFor(game);
      for (const [folder, rule] of Object.entries(folders)) {
        api.kindFor(game, folder + '/example.png');
        for (const id of Object.keys(rule.items ?? {})) api.kindFor(game, folder + '/' + id + '.glb');
      }
    }
    if (writes !== 0) throw new Error('Có lời gọi ghi');
    console.log('Lời gọi ghi: ' + writes);
  `], { cwd: root, encoding: 'utf8' });
  assert.equal(result.status, 0, `${result.stdout}\n${result.stderr}`);
  assert.match(result.stdout, /Lời gọi ghi: 0/u);
  t.diagnostic(result.stdout.trim());
});
