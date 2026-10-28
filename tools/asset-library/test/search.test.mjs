import test, { after, mock } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { syncBuiltinESMExports } from 'node:module';
import vm from 'node:vm';
import { performance } from 'node:perf_hooks';

// K1: lõi tìm kiếm không cần ghi ở đâu cả. Bọc callback, sync, promises,
// stream và open có cờ ghi trước khi nạp module cần kiểm.
const writes = [];
const denyWrite = (op, p) => { writes.push({ op, path: String(p) }); throw new Error(`K1: lời gọi ghi ${op} ${p}`); };
for (const name of ['writeFile', 'appendFile', 'mkdir', 'mkdtemp', 'rename', 'copyFile', 'cp', 'symlink', 'link',
  'unlink', 'rm', 'rmdir', 'truncate', 'chmod', 'chown', 'utimes']) {
  for (const key of [name, name + 'Sync']) if (typeof fs[key] === 'function') mock.method(fs, key, (...args) => denyWrite(key, args[0]));
  if (typeof fs.promises[name] === 'function') mock.method(fs.promises, name, (...args) => denyWrite('promises.' + name, args[0]));
}
for (const [object, key] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
  const original = object[key];
  mock.method(object, key, function (p, flags, ...rest) {
    const write = typeof flags === 'number'
      ? flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_APPEND | fs.constants.O_TRUNC)
      : /[wa+]/u.test(flags);
    if (write) denyWrite(key, p);
    return original.call(this, p, flags, ...rest);
  });
}
mock.method(fs, 'createWriteStream', p => denyWrite('createWriteStream', p));
syncBuiltinESMExports();
after(() => { mock.restoreAll(); syncBuiltinESMExports(); });

const { STOP, WEIGHTS, normalize, unaccent, tokenize, createSearch, search } = await import('../lib/search.mjs');
const read = rel => fs.readFileSync(new URL(rel, import.meta.url), 'utf8');
const json = rel => JSON.parse(read(rel));
const taxonomy = json('../../../library/taxonomy.json');
const small = json('./fixtures/catalog-small.json');
const index = createSearch(small, { taxonomy });
const uids = rows => rows.map(row => row.card.uid);
const includes = (rows, uid) => uids(rows).includes(uid);
const herb = small.cards[0];
const make = (overrides = {}) => ({ uid: 'test:plain', type: 'image', status: 'unscored', files: [], ...overrides });
const one = (card, query, filters = {}) => search([make(card)], query, filters, { taxonomy });
const freeze = value => { if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); } return value; };

test('Chuẩn hóa dấu Việt, đ, camelCase, dấu phân tách và đúng STOP của tripo-match', () => {
  assert.equal(unaccent('ĐÁ Chòi'), 'da choi');
  assert.equal(normalize('impactWood_light+old.Model/Front-v2'), 'impact wood light old model front v2');
  assert.deepEqual(tokenize('Đá_đá+chòi.glb / 3d model PNG alpha flat front back left stylized fantasy cartoon with the of a an cua va o 123'), ['da', 'choi']);
  const source = read('../../tripo-match/match.mjs');
  const original = [...source.match(/const STOP = new Set\(\[([\s\S]*?)\]\)/u)[1].matchAll(/'([^']+)'/gu)].map(m => m[1]);
  assert.deepEqual(STOP, original);
  assert.deepEqual(WEIGHTS, { name: 5, aliases: 4, subkind: 3, kind: 3, tags: 2, text: 1 });
});

test('Đồng nghĩa hai chiều, cụm nhiều từ, không gộp từ liên quan thành đồng nghĩa', () => {
  for (const [a, b] of [['hut', 'chòi'], ['chòi', 'choi'], ['jetty', 'cầu tàu'], ['jetty', 'cau tau'], ['rock', 'stones'], ['wood', 'timber']]) {
    assert.deepEqual(index.search(a), index.search(b), `${a} = ${b}`);
  }
  assert.equal(one({ name: 'house' }, 'hut')[0].score, 2.5);
  assert.equal(one({ name: 'hut' }, 'house')[0].score, 2.5);
  assert.equal(one({ name: 'knock' }, 'click')[0].score, 2.5);
  assert.equal(one({ name: 'wood' }, 'gõ').length, 0);
  assert.equal(one({ name: 'wood' }, 'gỗ')[0].score, 5);
  assert.equal(one({ name: 'click' }, 'gõ')[0].score, 5);
  assert.equal(one({ name: 'tau' }, 'jetty').length, 0);
  assert.equal(one({ name: 'tree' }, 'rock').length, 0);
});

test('viTokens chỉ dịch chữ không dấu trong phạm vi thư mục, không khớp chuỗi con', () => {
  const cards = [
    make({ uid: 'typing-defense:landmarks/cau-go', name: 'Cau' }),
    make({ uid: 'typing-defense:landmarks/stone-object', name: 'Da' }),
    make({ uid: 'typing-defense:scenery/meadow/object', name: 'Da' }),
    make({ uid: 'typing-defense:enemies/object', name: 'Da Cau' }),
    make({ uid: 'typing-defense:scenery-fake/object', name: 'Da Cau' }),
    make({ uid: 'dragon-hold:landmarks/cau-object', name: 'Cau' }),
    make({ uid: 'typing-defense:enemies/accented', name: 'Đá' }),
  ];
  const scoped = createSearch(cards, { taxonomy });
  assert.deepEqual(uids(scoped.search('bridge')), ['typing-defense:landmarks/cau-go']);
  assert.deepEqual(new Set(uids(scoped.search('stone'))), new Set([
    'typing-defense:landmarks/stone-object', 'typing-defense:scenery/meadow/object', 'typing-defense:enemies/accented',
  ]));
  assert.ok(!includes(scoped.search('stone'), 'typing-defense:enemies/object'));
});

test('Điểm từng trường, nửa điểm liên quan, không nhân điểm do lặp alias hay nhiều từ', () => {
  for (const [field, weight] of Object.entries(WEIGHTS)) {
    const card = field === 'text' ? { description: 'needle' } : { [field]: field === 'aliases' || field === 'tags' ? ['needle'] : 'needle' };
    assert.equal(one(card, 'needle')[0].score, weight, field);
  }
  assert.equal(one({ name: 'needle', aliases: ['needle', 'needle'], subkind: 'needle', kind: 'needle', tags: ['needle'], provenance: { tripoFile: 'needle.glb' } }, 'needle')[0].score, 18);
  assert.equal(one({ name: 'needle pin', aliases: ['needle', 'pin'] }, 'needle pin needle')[0].score, 9);
  assert.equal(one({ name: 'house', aliases: ['house'], subkind: 'house', kind: 'house', tags: ['house'], description: 'house' }, 'hut')[0].score, 9);
  assert.equal(one({ name: 'needle', aliases: ['unknown'] }, 'unknown')[0].score, 4);
  assert.equal(one({ name: 'needle', description: 'needle' }, 'unmatched').length, 0);
  assert.equal(one({ uid: 'test:impactWood_light' }, 'wood')[0].score, 6);
  assert.equal(index.search('obsolete needle').length, 0, 'Không dùng đường dẫn file bị loại để tính điểm');
});

test('Cộng shipped/pass một lần, runtime 0,5 và provisional trừ 0,5', () => {
  for (const [status, bonus] of [['unscored', 0], ['shipped', 1], ['pass', 1], ['provisional', -0.5]]) {
    assert.equal(one({ name: 'needle', status, quality: { level: 'pass' } }, 'needle')[0].score, 5 + bonus);
    assert.equal(one({ name: 'needle', status, pipeline: 'runtime' }, 'needle')[0].score, 5.5 + bonus);
  }
  assert.equal(one({ name: 'needle', files: [{ role: 'runtime-medium', path: 'plain.glb' }] }, 'needle')[0].score, 5.5);
});

test('Ẩn draft/rejected/review/hidden/work; all vẫn không tự mở requested; private xem được', () => {
  for (const filters of [{}, { all: true }, { requested: true }, { all: true, requested: true }]) {
    const result = index.search('', filters);
    assert.equal(includes(result, 'test:requested'), Boolean(filters.requested));
    for (const name of ['draft', 'rejected', 'review', 'hidden', 'work']) assert.equal(includes(result, `test:${name}`), Boolean(filters.all));
    assert.ok(includes(result, 'test:private'));
  }
  assert.equal(index.search('', { status: 'rejected' }).length, 0);
  assert.deepEqual(uids(index.search('', { status: 'rejected', all: true })), ['test:rejected']);
  assert.equal(index.search('', { status: 'requested', all: true }).length, 0);
});

test('Đủ bộ lọc §5.2, AND giữa trục, tag/biome/has và used-by lặp', () => {
  const filters = { type: '3d', kind: 'building', sub: 'hut', tag: ['wood', 'thatch'], biome: ['pine-forest', 'river'],
    style: 'mythic-forest', game: 'dragon-hold', 'used-by': ['dragon-hold', 'typing-defense'], status: 'shipped', pipeline: 'runtime',
    'min-score': 9, 'max-tris': 5000, has: ['glb', 'runtime', 'clips', 'rig', 'prompt', 'icon'], drive: 'no', json: true, limit: 1 };
  assert.deepEqual(uids(index.search('', filters)), [herb.uid]);
  for (const key of ['type', 'kind', 'sub', 'tag', 'biome', 'style', 'game', 'used-by', 'status', 'pipeline', 'drive']) {
    assert.equal(index.search('', { ...filters, [key]: 'missing' }).length, 0, key);
  }
  assert.deepEqual(index.search('', { type: '3d' }), index.search('', { type: 'model3d' }));
  assert.deepEqual(index.search('', { usedBy: 'typing-defense', subkind: 'hut', minScore: 9, maxTris: 5000 }), index.search('', { 'used-by': 'typing-defense', sub: 'hut', 'min-score': 9, 'max-tris': 5000 }));
  assert.deepEqual(index.search('', { '--type': '3d', '--limit': '0' }), []);
  assert.equal(index.search('', { type: 'music' })[0].card.uid, 'test:private');
  assert.equal(index.search('', { type: 'audio', 'min-score': 4 })[0].card.uid, 'kenney:impact-sounds/Audio/impactWood_light');
  assert.ok(!includes(index.search('', { 'min-score': 9 }), 'typing-defense:landmarks/nha-rai-da'), '3D dùng score3d, không mượn điểm 2D');
  assert.equal(one({}, '', { 'min-score': 0 }).length, 0, 'Thiếu điểm không coi là 0');
  assert.equal(one({}, '', { 'max-tris': 10000 }).length, 0, 'Thiếu số đo không coi là 0');
  assert.equal(one({ model: { triangles: { original: 7000 } } }, '', { 'max-tris': 5000 }).length, 0);
  assert.equal(one({ files: [{ role: 'runtime-medium', glb: { triangles: 2000 } }, { role: 'runtime-high', glb: { triangles: 6000 } }] }, '', { 'max-tris': 5000 }).length, 0, 'Không mượn bậc medium để vượt trần của high');
  assert.equal(one({ files: [{ role: 'glb-original', path: 'plain.glb', glb: { triangles: 200, skinned: true, clips: ['idle'] } }] }, '', { 'max-tris': 500, has: ['glb', 'clips', 'rig'] }).length, 1);
  for (const has of ['glb', 'runtime', 'clips', 'rig', 'prompt', 'icon']) assert.equal(one({}, '', { has }).length, 0, has);
  assert.equal(one({ files: [{ path: 'plain.glb', role: 'rejected', onDrive: 'no' }] }, '', { has: 'glb' }).length, 0);
  assert.equal(one({ files: [{ path: 'plain.glb', role: 'rejected', onDrive: 'no' }] }, '', { drive: 'no' }).length, 0);
});

test('Bộ lọc sai báo lỗi rõ ràng thay vì trả sai kết quả âm thầm', () => {
  for (const filters of [{ typo: 'a' }, { limit: -1 }, { limit: 1.1 }, { limit: null }, { limit: '' }, { minScore: NaN }, { maxTris: Infinity }, { maxTris: true }, { all: 'false' }, { requested: 'true' }, { has: 'animation' }]) {
    assert.throws(() => index.search('', filters));
  }
  assert.throws(() => createSearch(small), /taxonomy/u);
  assert.throws(() => createSearch({}, { taxonomy }), /Catalog/u);
});

test('Không đổi dữ liệu đầu vào; hòa điểm theo phân loại hợp từ vựng rồi uid', () => {
  const data = freeze(structuredClone(small)), tax = freeze(structuredClone(taxonomy));
  const before = JSON.stringify(data), engine = createSearch(data, { taxonomy: tax });
  assert.strictEqual(engine.search('herb')[0].card, data.cards[0]);
  engine.search('', { all: true, requested: true, limit: 2 });
  assert.equal(JSON.stringify(data), before);
  const cards = [make({ uid: 'test:z', name: 'needle', kind: 'building', subkind: 'hut' }), make({ uid: 'test:a', name: 'needle' }), make({ uid: 'test:y', name: 'needle', kind: 'building', subkind: 'hut' })];
  assert.deepEqual(uids(search(cards, 'needle', {}, { taxonomy })), ['test:y', 'test:z', 'test:a']);
  assert.deepEqual(search([], '', {}, { taxonomy }), []);
});

test('Nhúng cùng mã vào trang: không Node/import/fs, kết quả giống hệt trong VM trống', () => {
  const source = read('../lib/search.mjs');
  assert.doesNotMatch(source, /\bimport\s*(?:[({*]|['"]|[\w]+\s+from)|\brequire\s*\(|\b(?:process|Buffer|document|window|fetch)\b|node:|\bfs\./u);
  // page.mjs có thể bỏ export rồi nhúng inline; không mô phỏng browser hay mở server.
  const context = vm.createContext({});
  vm.runInContext(source.replace(/^export /gmu, '') + '\nglobalThis.engine = { createSearch, normalize, tokenize };', context);
  const browser = context.engine.createSearch(structuredClone(small), { taxonomy: structuredClone(taxonomy) });
  for (const query of ['chòi', 'wood click', 'cầu tàu', 'rock', '']) {
    for (const filters of [{}, { type: '3d' }, { all: true, requested: true, limit: 5 }]) {
      assert.equal(JSON.stringify(browser.search(query, filters)), JSON.stringify(index.search(query, filters)));
    }
  }
});

let real;
async function realCatalog() {
  if (real) return real;
  const catalog = json('../../../library/out/catalog.json');
  const facts = json('../../../library/out/doc-facts.json');
  const audio = json('../../../library/out/audio-catalog.json');
  // AL-07/08 đã có đầu ra riêng nhưng catalog cũ chưa quét lại. Dùng đúng hàm
  // nối AL-07, gộp âm AL-08 trong RAM, không chạy scanner hay ghi library/out.
  const { mergeDocFacts } = await import('../doc-facts.mjs');
  mergeDocFacts(catalog.cards, facts);
  const cards = [...new Map([...catalog.cards, ...audio.cards].map(card => [card.uid, card])).values()];
  const start = performance.now();
  const engine = createSearch(cards, { taxonomy });
  real = { cards, engine, indexMs: performance.now() - start, queries: json('../../../library/test/queries.json'),
    baseCount: catalog.cards.length, audioCount: audio.cards.length };
  return real;
}

test('Mục lục thật: câu tìm vàng, chòi = choi, bản loại chỉ hiện khi all', async t => {
  const { engine, cards, queries, baseCount, audioCount, indexMs } = await realCatalog();
  t.diagnostic(`Catalog thật: ${baseCount} thẻ hình/3D + ${audioCount} thẻ âm; ${cards.length} uid duy nhất; tạo index ${indexMs.toFixed(2)} ms; 0 lần ghi.`);
  for (const entry of queries) await t.test(`${entry.query} ${JSON.stringify(entry.filters)} top ${entry.topN}`, () => {
    assert.deepEqual(Object.keys(entry).sort(), ['filters', 'mustInclude', 'query', 'topN']);
    assert.ok(Number.isInteger(entry.topN) && entry.topN > 0 && entry.mustInclude.length > 0);
    const rows = engine.search(entry.query, { ...entry.filters, limit: entry.topN });
    for (const uid of entry.mustInclude) assert.ok(includes(rows, uid), `${uid} không có trong ${JSON.stringify(uids(rows))}`);
    t.diagnostic(`${entry.query}: ${rows.map((r, i) => `${i + 1}. ${r.card.uid} (${r.score})`).join('; ')}`);
  });
  assert.deepEqual(engine.search('chòi'), engine.search('choi'));
  assert.deepEqual(engine.search('chòi', { type: '3d' }), engine.search('choi', { type: '3d' }));
  const hidden = cards.filter(c => ['draft', 'review', 'rejected'].includes(c.status));
  const visible = engine.search('');
  assert.ok(hidden.length > 0);
  assert.ok(visible.every(r => !['draft', 'review', 'rejected', 'requested'].includes(r.card.status)));
  const all = engine.search('', { all: true });
  for (const card of hidden) assert.ok(includes(all, card.uid));
  assert.ok(all.every(r => r.card.status !== 'requested'));
  t.diagnostic(`Ẩn mặc định: ${hidden.length} thẻ (${cards.filter(c => c.status === 'rejected').length} rejected); all mở đủ; requested vẫn có cổng riêng.`);
});

test('p95 dưới 300 ms trên mục lục thật, cả tìm ấm và tạo index + tìm lạnh', async t => {
  const { cards, engine, queries } = await realCatalog();
  const percentile = values => values.slice().sort((a, b) => a - b)[Math.ceil(values.length * .95) - 1];
  const warm = [], cold = [];
  for (let i = 0; i < 14; i++) engine.search(queries[i % queries.length].query, queries[i % queries.length].filters);
  for (let i = 0; i < 140; i++) {
    const q = queries[i % queries.length], start = performance.now();
    engine.search(q.query, q.filters); warm.push(performance.now() - start);
  }
  for (let i = 0; i < 21; i++) {
    const q = queries[i % queries.length], start = performance.now();
    search(cards, q.query, q.filters, { taxonomy }); cold.push(performance.now() - start);
  }
  const warm95 = percentile(warm), cold95 = percentile(cold);
  t.diagnostic(`${cards.length} thẻ thật: p95 ấm ${warm95.toFixed(2)} ms / ${warm.length} lượt; p95 lạnh (tạo index + tìm) ${cold95.toFixed(2)} ms / ${cold.length} lượt.`);
  assert.ok(warm95 < 300, `p95 ấm ${warm95} ms`);
  assert.ok(cold95 < 300, `p95 lạnh ${cold95} ms`);
});

test('K1: mọi lượt trên cây mẫu, VM và mục lục thật có 0 lời gọi ghi', t => {
  assert.deepEqual(writes, []);
  t.diagnostic('K1: 0 lời gọi ghi; không tạo hay dọn file tạm.');
});
