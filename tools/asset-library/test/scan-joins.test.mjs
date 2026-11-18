import test from 'node:test';
import assert from 'node:assert/strict';
import * as fs from 'node:fs/promises';
import path from 'node:path';
import { tmpdir } from 'node:os';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { scan, main, REPO_ROOT } from '../scan.mjs';
import { parseMd5 } from '../lib/joins.mjs';

const DATE = '2026-10-28T06:00:00.000Z';
const sources = JSON.parse(await fs.readFile(path.join(REPO_ROOT, 'library/sources.json'), 'utf8'));
const hash = data => createHash('md5').update(data).digest('hex');
const png = tag => Buffer.concat([Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jR4sAAAAASUVORK5CYII=', 'base64'), Buffer.from(tag)]);
const pick = (catalog, uid) => {
  const card = catalog.cards.find(card => card.uid === uid);
  assert.ok(card, `Thiếu ${uid}`);
  return card;
};

async function put(root, rel, data) {
  await fs.mkdir(path.dirname(path.join(root, rel)), { recursive: true });
  await fs.writeFile(path.join(root, rel), data);
}

async function fixture(t) {
  const root = await fs.mkdtemp(path.join(tmpdir(), 'al06-joins-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  const tracked = [];
  const metadata = async (rel, data, inGit = true) => {
    await put(root, rel, typeof data === 'string' ? data : JSON.stringify(data));
    if (inGit) tracked.push(rel);
  };
  await metadata('library/sources.json', sources);
  const files = new Map();
  const asset = async (rel, tag = rel) => {
    const data = /\.png$/u.test(rel) ? png(tag) : Buffer.from(tag);
    await put(root, rel, data);
    files.set(rel, hash(data));
    return hash(data);
  };
  const dragon = 'games/dragon-hold/';
  const herb = dragon + 'art-src/houses/herb-hut';
  await asset(herb + '.png');
  await asset(herb + '.tripo.png');
  for (const size of [64, 256]) await asset(`${dragon}art-src/icons/normalized/herb-hut.${size}.png`);
  await asset(dragon + 'art-src/ui/icons/herb-hut.png');
  await asset(dragon + 'art-src/3d/houses/herb-hut.glb');
  await asset(dragon + 'art-src/models/props/herb-hut.glb');
  const manifest = {
    models: { 'props/herb-hut': { tiers: {
      high: { url: '/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.high.glb?v=abc' },
      medium: { url: '/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.medium.glb?v=def' },
    } } },
  };
  for (const tier of ['high', 'medium']) await asset(`${dragon}public/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.${tier}.glb`);
  const promptPaths = [herb, herb + '.tripo', dragon + 'art-src/ui/icons/herb-hut',
    ...[64, 256].map(size => `${dragon}art-src/icons/normalized/herb-hut.${size}`)];
  for (const base of [herb + '.tripo', ...[64, 256].map(size => `${dragon}art-src/icons/normalized/herb-hut.${size}`)]) {
    for (const ticket of ['012', '012b', '012c']) {
      await asset(`${base}.rejected-${ticket}.png`);
      promptPaths.push(`${base}.rejected-${ticket}`);
    }
  }
  for (const base of promptPaths) await asset(base + '.prompt.txt');
  for (const dir of ['.reports', '.campaign3d-model-cache']) await asset(`${dragon}art-src/models/${dir}/props__herb-hut.json`);
  const jetty = dragon + 'art-src/props/pine-river/wooden-jetty';
  await asset(jetty + '.png', 'jetty');
  await asset(jetty + '.try1.png', 'jetty');
  await asset(jetty + '.v2.png', 'jetty-other');
  await asset('typing-game-handoff-2026-10-25/tripo-upload-dot3/face 4000/rong_wooden-jetty.png', 'jetty');
  await asset('typing-game-handoff-2026-10-25/tripo-upload-dot3/new-item.png', 'new');
  const space = 'games/space-typing/';
  const shipHash = await asset(space + 'art-src/3d/ships/scout.glb', 'scout');
  await asset(space + 'art-src/ships/scout-2d.png');
  await asset(space + 'art-src/models/raw/scout.glb', 'scout');
  await asset(space + 'art-src/models/raw/unmatched.glb', 'orphan');
  const spaceManifest = { models: {} };
  for (const id of ['draconis-v2', 'draconis-v3', 'draconis-v4']) {
    const kind = id.endsWith('v4') ? 'guides' : 'heroes';
    const tiers = {};
    for (const tier of ['high', 'medium']) {
      const suffix = `public/assets/space-typing/models/${kind}/${id}/${id}.${tier}.glb`;
      await asset(space + suffix, `${id}-${tier}`);
      await asset(dragon + suffix.replaceAll('space-typing', 'dragon-hold'), `${id}-${tier}`);
      tiers[tier] = { url: suffix.slice('public'.length) };
    }
    spaceManifest.models[`${kind}/${id}`] = { tiers };
  }
  await metadata(space + 'art-src/3d/SOURCES.json', { files: {
    'ships/scout.glb': { image: 'art-src/ships/scout-2d.png', md5: shipHash, downloadedAs: ['scout download.glb'], usedBy: ['ships/scout-runtime'] },
  }, notMadeYet: { 'enemies/next.glb': { image: 'art-src/enemies/next.png', standIn: 'ships/scout.glb', usedBy: ['enemies/next'] } } });
  await metadata(space + 'public/assets/space-typing/models/manifest.json', spaceManifest);
  const originalHash = files.get(dragon + 'art-src/3d/houses/herb-hut.glb');
  await metadata(dragon + 'art-src/3d/SOURCES.json', { files: {
    'houses/herb-hut.glb': { image: 'art-src/houses/herb-hut.png', md5: originalHash, usedBy: ['props/old-key'], downloadedAs: ['hut download.glb'] },
  } });
  await metadata(dragon + 'scripts/models/presets/dragon-hold-m0b.json', { models: { 'props/herb-hut': { source: 'houses/herb-hut.glb' } } });
  // Chưa có trong Git: full được dùng, --locks-only phải bỏ qua.
  await metadata(dragon + 'public/assets/dragon-hold/models/m0b/manifest.json', manifest, false);
  for (const game of ['dragon-hold', 'space-typing']) {
    const prefix = `games/${game}/`;
    await metadata(prefix + 'media.md5', [...files].filter(([p]) => p.startsWith(prefix))
      .map(([p, md5]) => `${md5}  ${p.slice(prefix.length)}`).join('\n') + '\n');
  }
  await metadata('media/private.md5', `${files.get(dragon + 'art-src/ui/icons/herb-hut.png')}  ${dragon}art-src/ui/icons/herb-hut.png\n`, false);
  return { root, tracked, metadata, asset, files, dragon, herb, jetty };
}

test('Herb Hut: nối preset thắng usedBy; 9 vai trò hiện; 9 rejected, 14 prompt, 2 report', async t => {
  const f = await fixture(t);
  const { catalog } = await scan({ repoRoot: f.root, scanDate: DATE });
  const card = pick(catalog, 'dragon-hold:houses/herb-hut');
  assert.equal(card.files.filter(file => !file.hidden).length, 9);
  assert.deepEqual(card.hiddenFiles, { prompt: 14, rejected: 9, report: 2 });
  assert.equal(card.rejectedMd5.length, 9);
  assert.equal(Object.keys(card.canonical).length, 11);
  assert.ok(card.files.filter(file => !file.hidden).every(file => file.canonical));
  assert.equal(card.canonical.prompt, f.herb + '.prompt.txt');
  assert.equal(card.files.filter(file => file.role === 'prompt' && file.canonical).length, 1);
  assert.equal(card.pipeline, 'runtime');
  assert.equal(card.status, 'private');
  assert.equal(card.files.find(file => file.role === 'icon').onDrive, 'private');
  assert.ok(card.files.filter(file => file.role !== 'icon').every(file => file.onDrive === 'yes'));
  assert.equal(card.usedBy.find(row => row.shipped).manifestKey, 'props/herb-hut');
  assert.deepEqual(card.provenance.downloadedAs, ['hut download.glb']);
  t.diagnostic('9 hiện; hiddenFiles rejected=9, prompt=14, report=2; canonical=11 (gồm prompt, report); md5 loại=9');
});

test('md5: same-folder, draft khác byte, handoff trùng/nháp; raw không làm chính; 6 Draconis copyOf Space', async t => {
  const f = await fixture(t);
  await f.asset(f.jetty + '.v3.png', 'jetty');
  const rejectedCopy = 'typing-game-handoff-2026-10-25/tripo-upload-dot3/rejected-hut.png';
  await put(f.root, rejectedCopy, await fs.readFile(path.join(f.root, f.herb + '.tripo.rejected-012.png')));
  const { catalog } = await scan({ repoRoot: f.root, scanDate: DATE });
  const jetty = pick(catalog, 'dragon-hold:props/pine-river/wooden-jetty');
  assert.equal(jetty.pipeline, 'tripo-requested');
  assert.ok(jetty.copies.some(row => row.location === 'same-folder' && row.path.endsWith('.try1.png')));
  assert.ok(jetty.copies.some(row => row.location === 'same-folder' && row.path.endsWith('.v3.png')));
  assert.ok(jetty.copies.some(row => row.location === 'handoff' && row.path.endsWith('rong_wooden-jetty.png')));
  assert.ok(jetty.files.some(row => row.role === 'draft' && row.path.endsWith('.v2.png')));
  assert.equal(pick(catalog, 'handoff:tripo-upload-dot3/new-item').status, 'draft');
  const herb = pick(catalog, 'dragon-hold:houses/herb-hut');
  const rejected = herb.copies.find(file => file.path === rejectedCopy);
  assert.ok(rejected);
  assert.ok(herb.rejectedMd5.includes(rejected.md5));
  assert.ok(!catalog.cards.some(card => card.uid === 'handoff:tripo-upload-dot3/rejected-hut'));
  assert.equal(catalog.cards.flatMap(card => card.files).filter(file => file.path.includes('/models/raw/')).length, 0);
  const scout = pick(catalog, 'space-typing:ships/scout');
  assert.ok(scout.copies.some(file => file.location === 'models-raw'));
  assert.ok(scout.files.some(file => file.path.endsWith('scout-2d.png')));
  const draconis = catalog.cards.filter(card => card.origin === 'dragon-hold').flatMap(card => card.files).filter(file => file.path.includes('/draconis-'));
  assert.equal(draconis.length, 6);
  assert.ok(draconis.every(file => file.copyOf?.startsWith('space-typing:')));
  const next = pick(catalog, 'space-typing:enemies/next');
  assert.equal(next.status, 'requested');
  assert.equal(next.pipeline, 'tripo-requested');
  assert.equal(next.provenance.notMadeYet.standIn, 'ships/scout.glb');
  assert.ok(!next.files.some(file => file.path.endsWith('.glb')));
  t.diagnostic('same-folder=2; handoff trùng=2 (gồm bản loại), nháp=1; raw chính=0; Draconis copyOf Space=6');
});

test('onDrive có đủ yes, changed, no và private; lock giữ nguyên dấu cách', async t => {
  const f = await fixture(t);
  await f.asset(f.herb + '.png', 'đã sửa');
  await f.asset(f.dragon + 'art-src/houses/new house.png', 'chưa khóa');
  const { catalog } = await scan({ repoRoot: f.root, scanDate: DATE });
  const files = catalog.cards.flatMap(card => card.files);
  assert.equal(files.find(file => file.path === f.herb + '.png').onDrive, 'changed');
  assert.equal(files.find(file => file.path.endsWith('/new house.png')).onDrive, 'no');
  assert.equal(files.find(file => file.path === f.herb + '.tripo.png').onDrive, 'yes');
  assert.equal(files.find(file => file.role === 'icon').onDrive, 'private');
  const parsed = parseMd5('a'.repeat(32) + '  art-src/a b.png\n' + 'b'.repeat(32) + '  ../escape.png\n', 'games/dragon-hold/', p => !p.includes('..'));
  assert.deepEqual([...parsed.keys()], ['games/dragon-hold/art-src/a b.png']);
});

test('Tuyển chọn theo md5 sau đổi tên: giữ uid mới, formerUids cũ và trường thủ công thắng', async t => {
  const f = await fixture(t);
  const data = png('renamed');
  const oldPath = path.join(f.root, f.dragon + 'art-src/houses/old-name.png');
  await put(f.root, f.dragon + 'art-src/houses/old-name.png', data);
  await f.metadata('library/curated/dragon-hold.jsonl', [
    JSON.stringify({ uid: 'dragon-hold:houses/old-name', md5s: [hash(data)], name: 'Renamed Hut', kind: 'structure', status: 'pass', reviewed: 'owner', aliases: ['lều mới'] }),
    JSON.stringify({ uid: 'dragon-hold:props/pine-river/wooden-jetty', md5s: ['0'.repeat(32)], name: 'Wooden Jetty', status: 'pass' }),
  ].join('\n'));
  await fs.rename(oldPath, path.join(f.root, f.dragon + 'art-src/houses/renamed.png'));
  const { catalog } = await scan({ repoRoot: f.root, scanDate: DATE });
  const card = pick(catalog, 'dragon-hold:houses/renamed');
  assert.deepEqual(card.formerUids, ['dragon-hold:houses/old-name']);
  assert.equal(card.name, 'Renamed Hut');
  assert.equal(card.kind, 'structure');
  assert.equal(card.status, 'pass');
  assert.equal(card.reviewed, 'owner');
  assert.equal(pick(catalog, 'dragon-hold:props/pine-river/wooden-jetty').name, 'Wooden Jetty');
  t.diagnostic('Đổi tên: md5 gắn đúng 1 dòng; formerUids=[dragon-hold:houses/old-name]; 5 trường thủ công được giữ');
});

test('Canonical tuyển chọn thắng mặc định; uid chính xác thắng md5, md5 mơ hồ được cảnh báo', async t => {
  const f = await fixture(t);
  const selected = f.dragon + 'art-src/houses/herb-hut.webp';
  await put(f.root, selected, 'ảnh webp mẫu');
  const common = png('common');
  await put(f.root, f.dragon + 'art-src/houses/same-a.png', common);
  await put(f.root, f.dragon + 'art-src/houses/same-b.png', common);
  await f.metadata('library/curated/dragon-hold.jsonl', [
    JSON.stringify({ uid: 'dragon-hold:houses/herb-hut', md5s: [hash(common)], name: 'Herb Hut', canonical: { concept: selected } }),
    JSON.stringify({ uid: 'dragon-hold:houses/missing', md5s: [hash(common)], name: 'Ambiguous' }),
  ].join('\n'));
  const { catalog } = await scan({ repoRoot: f.root, scanDate: DATE });
  const card = pick(catalog, 'dragon-hold:houses/herb-hut');
  assert.equal(card.canonical.concept, selected);
  assert.equal(card.files.filter(file => file.role === 'concept' && file.canonical).length, 1);
  assert.equal(card.hero, selected);
  assert.ok(catalog.warnings.some(row => row.includes('khớp nhiều thẻ')));
  assert.ok(!catalog.cards.some(card => card.name === 'Ambiguous'));
});

test('--locks-only: chỉ metadata Git, không đọc/stat media, local=false và không sửa cache AL-05/media', async t => {
  const f = await fixture(t);
  await f.metadata('scripts/models/presets/dragon-hold-extra.json', { game: 'dragon-hold', models: { 'props/extra': { source: 'houses/extra.glb' } } });
  await put(f.root, 'library/.cache/hash.json', '{"files":{},"sentinel":1}');
  const oldCache = await fs.readFile(path.join(f.root, 'library/.cache/hash.json'));
  const reads = [];
  const io = new Proxy(fs, { get(object, key) {
    if (!['readFile', 'lstat'].includes(key)) return object[key];
    return async (file, ...args) => {
      const rel = path.relative(f.root, file).split(path.sep).join('/');
      assert.ok(!/\.(png|glb|webp|prompt\.txt)$/u.test(rel), 'Đọc/stat media: ' + rel);
      assert.ok(!rel.includes('/.cache/') && !rel.includes('media-hash.json'), 'Đọc cache trong locks-only');
      reads.push(rel);
      return object[key](file, ...args);
    };
  } });
  const { catalog, stats } = await main(['--locks-only', '--scan-date', DATE], { repoRoot: f.root, io, hooks: { trackedFiles: f.tracked } });
  assert.ok(catalog.cards.flatMap(card => card.files).every(file => file.local === false));
  assert.equal(stats.hash.hashed, 0);
  assert.equal(stats.inspected, 0);
  assert.ok(!reads.includes(f.dragon + 'public/assets/dragon-hold/models/m0b/manifest.json'));
  assert.equal(pick(catalog, 'dragon-hold:houses/extra').status, 'requested');
  assert.notEqual(pick(catalog, 'dragon-hold:houses/herb-hut').pipeline, undefined);
  assert.ok(!catalog.cards.some(card => card.origin === 'handoff'));
  assert.deepEqual(await fs.readFile(path.join(f.root, 'library/.cache/hash.json')), oldCache);
  t.diagnostic(`${catalog.cards.length} thẻ từ metadata Git; đọc/stat media=0; băm=0; đọc GLB=0; local=true=0`);
});

test('Thiếu media vẫn dựng thẻ từ lock và SOURCES; hai lượt cùng ngày giống từng byte', async t => {
  const f = await fixture(t);
  await fs.unlink(path.join(f.root, f.herb + '.png'));
  await scan({ repoRoot: f.root, scanDate: DATE });
  const first = await fs.readFile(path.join(f.root, 'library/out/catalog.json'));
  const result = await scan({ repoRoot: f.root, scanDate: DATE });
  const file = pick(result.catalog, 'dragon-hold:houses/herb-hut').files.find(file => file.path === f.herb + '.png');
  assert.equal(file.local, false);
  assert.equal(file.onDrive, 'yes');
  assert.deepEqual(await fs.readFile(path.join(f.root, 'library/out/catalog.json')), first);
  t.diagnostic(`Catalog ổn định ${first.length} byte; 1 ảnh vắng local=false, onDrive=yes`);
});

test('K3: chặn vùng cấm và symlink ở preset, manifest, handoff, lock, tuyển chọn trước khi đọc', async t => {
  const f = await fixture(t);
  const excluded = sources.deny.find(p => p.startsWith('games/') && !p.includes('monkeytype'));
  const deniedName = excluded.split('/').at(-1);
  const outer = path.join(f.root, 'outside');
  await fs.mkdir(outer);
  await fs.writeFile(path.join(outer, 'secret.png'), png('secret'));
  const handoff = path.join(f.root, 'typing-game-handoff-2026-10-25');
  await fs.symlink(outer, path.join(handoff, 'linked-dir'));
  await fs.symlink(path.join(outer, 'secret.png'), path.join(handoff, 'linked.png'));
  await put(f.root, `typing-game-handoff-2026-10-25/${deniedName}/secret.png`, png('denied'));
  const preset = path.join(f.root, f.dragon + 'scripts/models/presets/linked.json');
  await fs.symlink(path.join(outer, 'secret.png'), preset);
  const manifest = f.dragon + 'public/assets/dragon-hold/models/linked/manifest.json';
  await fs.mkdir(path.dirname(path.join(f.root, manifest)), { recursive: true });
  await fs.symlink(path.join(outer, 'secret.png'), path.join(f.root, manifest));
  await f.metadata('library/curated/dragon-hold.jsonl', JSON.stringify({ uid: 'dragon-hold:houses/herb-hut', name: deniedName }));
  await fs.appendFile(path.join(f.root, f.dragon + 'media.md5'), `${'a'.repeat(32)}  ../../${excluded}/secret.png\n`);
  const reads = [];
  const io = new Proxy(fs, { get(object, key) {
    if (key !== 'readFile') return object[key];
    return async (file, ...args) => { reads.push(path.relative(f.root, file)); return object[key](file, ...args); };
  } });
  await scan({ repoRoot: f.root, io, scanDate: DATE });
  assert.ok(!reads.some(p => p.includes('secret') || p.includes('linked') || p.includes(deniedName)));
  for (const name of await fs.readdir(path.join(f.root, 'library/out'))) {
    const text = await fs.readFile(path.join(f.root, 'library/out', name), 'utf8');
    assert.ok(!text.includes(deniedName));
    assert.ok(!text.includes('tu-tien'));
    assert.ok(!text.includes('secret.png'));
  }
  t.diagnostic('Đọc vùng cấm/symlink=0; rò tên cấm trong toàn bộ out/=0');
});

test('K1: bọc fs toàn cục; full và locks-only chỉ ghi library/out (kể cả cache)', async t => {
  const f = await fixture(t);
  const script = `
    import fs from 'node:fs';
    import path from 'node:path';
    import assert from 'node:assert/strict';
    import { syncBuiltinESMExports } from 'node:module';
    const root = ${JSON.stringify(f.root)};
    let writes = 0;
    const check = (operation, file) => {
      const rel = path.relative(root, file).split(path.sep).join('/');
      assert.ok(rel === 'library/out' || rel.startsWith('library/out/'), operation + ' ngoài phạm vi: ' + rel);
      writes++;
    };
    for (const name of ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'symlink', 'unlink', 'rm', 'rmdir',
      'write', 'writev', 'truncate', 'ftruncate', 'link', 'mkdtemp', 'chmod', 'chown', 'utimes']) {
      for (const key of [name, name + 'Sync']) if (typeof fs[key] === 'function') {
        const original = fs[key]; fs[key] = function(file, ...args) { check(name, file); return original.call(this, file, ...args); };
      }
      if (typeof fs.promises[name] === 'function') {
        const original = fs.promises[name]; fs.promises[name] = function(file, ...args) { check(name, file); return original.call(this, file, ...args); };
      }
    }
    fs.createWriteStream = () => { throw new Error('Không được mở luồng ghi'); };
    for (const [object, name] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
      const original = object[name]; object[name] = function(file, flags, ...args) {
        const writing = typeof flags === 'number' ? Boolean(flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_TRUNC | fs.constants.O_APPEND)) : /[wa+]/u.test(flags ?? 'r');
        assert.equal(writing, false, 'Mở file để ghi: ' + file);
        return original.call(this, file, flags, ...args);
      };
    }
    syncBuiltinESMExports();
    const { scan } = await import(${JSON.stringify(new URL('../scan.mjs', import.meta.url).href)});
    await scan({ repoRoot: root, scanDate: ${JSON.stringify(DATE)} });
    await scan({ repoRoot: root, locksOnly: true, scanDate: ${JSON.stringify(DATE)}, hooks: { trackedFiles: ${JSON.stringify(f.tracked)} } });
    assert.equal(writes, 8);
    console.log('K1: ' + writes + ' lời gọi ghi, tất cả dưới library/out; ngoài phạm vi=0');
  `;
  const child = spawnSync(process.execPath, ['--input-type=module', '-e', script], { encoding: 'utf8', timeout: 30_000 });
  assert.equal(child.status, 0, child.stdout + child.stderr);
  t.diagnostic(child.stdout.trim());
});
