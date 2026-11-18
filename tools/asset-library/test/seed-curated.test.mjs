import test, { after, mock } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { syncBuiltinESMExports } from 'node:module';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = fs.mkdtempSync(path.join(os.tmpdir(), 'al11-'));
const repoRoot = fileURLToPath(new URL('../../../', import.meta.url));
const writes = [];
const inside = p => { const r = path.relative(root, path.resolve(p instanceof URL ? fileURLToPath(p) : String(p))); return !r.startsWith('..') && !path.isAbsolute(r); };
const check = (op, p) => { assert.ok(inside(p), `K1: ghi ngoài cây tạm (${op})`); writes.push({ op, p: String(p) }); };
const mutations = ['writeFile', 'appendFile', 'mkdir', 'mkdtemp', 'rename', 'copyFile', 'cp', 'symlink', 'link', 'unlink', 'rm', 'rmdir', 'truncate', 'chmod', 'chown', 'utimes'];
for (const op of mutations) for (const [owner, key] of [[fs, op], [fs, op + 'Sync'], [fs.promises, op]]) {
  if (typeof owner[key] !== 'function') continue;
  const original = owner[key];
  mock.method(owner, key, function (...args) {
    check(key, ['copyFile', 'cp', 'symlink', 'link'].includes(op) ? args[1] : args[0]);
    if (op === 'rename') check(key, args[1]);
    return original.apply(this, args);
  });
}
for (const [owner, key] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
  const original = owner[key];
  mock.method(owner, key, function (p, flags, ...args) {
    if (typeof flags === 'number' ? flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_APPEND | fs.constants.O_TRUNC) : /[wa+]/u.test(flags)) check(key, p);
    return original.call(this, p, flags, ...args);
  });
}
const stream = fs.createWriteStream;
mock.method(fs, 'createWriteStream', function (p, ...args) { check('createWriteStream', p); return stream.call(this, p, ...args); });
syncBuiltinESMExports();
after(() => { console.log(`K1: ${writes.length} lời gọi ghi, đều dưới cây tạm; 0 ghi repo thật`); fs.rmSync(root, { recursive: true, force: true }); mock.restoreAll(); syncBuiltinESMExports(); });

const { seedCurated, prepareSeeds, loadInputs, FILES, privateInventory, leaks } = await import('../seed-curated.mjs');
const { createSearch } = await import('../lib/search.mjs');
const read = rel => fs.readFileSync(path.join(repoRoot, rel), 'utf8');
const taxonomy = JSON.parse(read('library/taxonomy.json'));
const inventory = { names: [], md5s: new Set(), paths: new Set() };
const card = (id, extra = {}) => ({ uid: 'typing-defense:landmarks/' + id, origin: 'typing-defense', status: 'unscored', type: 'model3d',
  files: [{ path: `games/typing-defense/art-src/3d/landmarks/${id}.glb`, role: 'glb-original', md5: 'a'.repeat(32) }], ...extra });
const facts = { schema: 'asset-library-doc-facts/1', byId: {}, byPath: {} };
const inputs = cards => ({ catalog: { cards }, facts, taxonomy, inventory });
function fixture(name) { const dir = path.join(root, name); fs.mkdirSync(path.join(dir, 'library/curated'), { recursive: true }); return dir; }

test('Tên ưu tiên NAMES_EN, phần Anh 3D_IMPORT rồi dịch mồi; alias có/không dấu và Tripo', () => {
  const d = inputs([card('choi-canh-doi'), card('cau-tau', { name: 'Jetty Import', nameSource: '3D_IMPORT_2026-10-28.md' }),
    card('nha-rai-da', { name: 'Stone Hut', nameSource: 'NAMES_EN', nameVi: 'Nhà rải đá', provenance: { tripoFile: 'thatched+hut+3d+model.glb', prompt: 'SECRET PROMPT CONTENT' } })]);
  const rows = prepareSeeds(d).candidates.map(c => c.row);
  assert.equal(rows.find(r => r.uid.endsWith('choi-canh-doi')).name, 'Hilltop Watch Hut');
  assert.equal(rows.find(r => r.uid.endsWith('cau-tau')).nameSource, '3D_IMPORT_2026-10-28.md');
  const hut = rows.find(r => r.uid.endsWith('nha-rai-da'));
  assert.equal(hut.nameSource, 'NAMES_EN');
  for (const alias of ['Nhà rải đá', 'Nha rai da', 'nha-rai-da', 'thatched hut 3d model']) assert.ok(hut.aliases.includes(alias));
  assert.ok(!JSON.stringify(rows).includes('SECRET PROMPT')); assert.ok(!JSON.stringify(rows).includes('"prompt"'));
  for (const r of rows) { assert.equal(r.name.normalize('NFD').replace(/\p{M}/gu, ''), r.name); assert.equal(r.quality, null); assert.deepEqual(r.canonical, {}); }
});

test('folderMap/perItem quyết định kind/subkind/biome/style; nhãn lấy cả ghi chú, không lấy prompt', () => {
  const c = card('cau-tau', { provenance: { prompt: 'laser plasma' } });
  const d = inputs([c]); d.notes = new Map([[c.uid, ['wood thatch stilts lookout']]]);
  const r = prepareSeeds(d).candidates[0].row;
  assert.equal(r.kind, 'structure'); assert.equal(r.subkind, 'jetty');
  assert.equal(r.style, 'viet-village');
  for (const t of ['wood', 'thatch', 'stilts', 'lookout']) assert.ok(r.tags.includes(t));
  assert.ok(!r.tags.includes('laser')); assert.ok(!r.tags.includes('plasma'));
  const pine = { ...c, uid: 'dragon-hold:props/pine-river/bridge-old', origin: 'dragon-hold' };
  const p = prepareSeeds(inputs([pine])).candidates[0].row;
  assert.deepEqual(p.biome, ['pine-forest', 'river']); assert.equal(p.kind, 'structure'); assert.equal(p.subkind, 'bridge');
  const ambiguous = inputs([card('anonymous')]);
  ambiguous.notes = new Map([[ambiguous.catalog.cards[0].uid, ['Sạch ở góc nhìn; có gỗ, không có dữ kiện khác.']]]);
  const a = prepareSeeds(ambiguous).candidates[0].row;
  assert.ok(a.tags.includes('wood')); assert.ok(!a.tags.includes('book')); assert.ok(!a.tags.includes('click'));
  const kit = prepareSeeds(inputs([{ ...card('barracks-kit-l2'), uid: 'typing-defense:kits/barracks-kit-l2',
    aliases: ['wooden hut'], name: 'Barracks', nameSource: 'NAMES_EN' }])).candidates[0].row;
  assert.equal(kit.subkind, 'kit-part');
});

test('Chặn private/notForRelease ở thẻ, licence, file, bản sao và md5; ẩn draft/review/rejected/requested', () => {
  const variants = [{ private: true }, { notForRelease: true }, { licence: { private: true } }, { licence: { notForRelease: true } },
    ...['private', 'draft', 'review', 'rejected', 'requested'].map(status => ({ status })), { hidden: true },
    { copies: [{ path: 'private/path', onDrive: 'private' }] }, { files: [{ path: 'games/space-typing/art-src/Dota-Sounds/a.wav' }] }];
  assert.equal(prepareSeeds(inputs(variants.map((extra, i) => card(`bad-${i}`, extra)))).candidates.length, 0);
  const d = inputs([card('safe')]); d.inventory = { ...inventory, md5s: new Set(['a'.repeat(32)]) };
  assert.equal(prepareSeeds(d).candidates.length, 0);
  d.inventory = { ...inventory, names: ['safe'] }; assert.equal(prepareSeeds(d).candidates.length, 0);
});

test('Dòng reviewed lẫn chưa reviewed giữ từng byte khi thêm và sắp; lần hai 0 ghi', async () => {
  const dir = fixture('preserve'); const file = path.join(dir, 'library/curated/typing-defense.jsonl');
  const reviewed = '{ "uid" : "typing-defense:landmarks/cau-go", "name":"Owner Name", "reviewed":"claude-2026-10-29" }\r\n';
  const unreviewed = '{"uid":"typing-defense:landmarks/nha-rai-da","name":"Keep This","reviewed":null}\n';
  fs.writeFileSync(file, reviewed + unreviewed);
  const d = inputs([card('cau-go'), card('nha-rai-da'), card('cau-tau')]);
  const r = await seedCurated({ repoRoot: dir, inputs: d }); assert.equal(r.added, 1);
  const before = fs.readFileSync(file); assert.ok(before.includes(Buffer.from(reviewed))); assert.ok(before.includes(Buffer.from(unreviewed)));
  const rows = before.toString().trim().split('\n').map(JSON.parse); assert.deepEqual(rows.map(r => r.uid), rows.map(r => r.uid).sort());
  const count = writes.length; const again = await seedCurated({ repoRoot: dir, inputs: d });
  assert.equal(again.added, 0); assert.equal(again.changedFiles, 0); assert.equal(writes.length, count); assert.deepEqual(fs.readFileSync(file), before);
});

test('dry-run không ghi; symlink tổ tiên hoặc file đích bị chặn; JSON trùng uid bị chặn', async () => {
  const dir = fixture('safety'); const d = inputs([card('cau-tau')]);
  let n = writes.length; assert.equal((await seedCurated({ repoRoot: dir, inputs: d, dryRun: true })).added, 1); assert.equal(writes.length, n);
  const file = path.join(dir, 'library/curated/typing-defense.jsonl'); fs.symlinkSync(path.join(dir, 'other'), file);
  await assert.rejects(seedCurated({ repoRoot: dir, inputs: d }), /symlink/u); fs.unlinkSync(file);
  const line = JSON.stringify({ uid: d.catalog.cards[0].uid }) + '\n'; fs.writeFileSync(file, line + line);
  await assert.rejects(seedCurated({ repoRoot: dir, inputs: d }), /trùng/u);
});

test('Làn khác vừa duyệt sau khi đọc kế hoạch: dừng và giữ byte mới', async () => {
  const dir = fixture('concurrent'); const file = path.join(dir, 'library/curated/typing-defense.jsonl');
  fs.writeFileSync(file, '{"uid":"typing-defense:landmarks/cau-go","reviewed":null}\n');
  const reviewed = '{ "uid":"typing-defense:landmarks/cau-go", "reviewed":"claude-new", "name":"Keep" }\r\n';
  let reads = 0;
  const io = { ...fs.promises, async readFile(p, ...args) {
    if (p === file && ++reads === 2) fs.writeFileSync(file, reviewed);
    return fs.promises.readFile(p, ...args);
  } };
  await assert.rejects(seedCurated({ repoRoot: dir, io, inputs: inputs([card('cau-tau')]) }), /làn khác/u);
  assert.equal(fs.readFileSync(file, 'utf8'), reviewed);
});

const real = await loadInputs();
const prepared = prepareSeeds(real);
test('Dữ liệu thật: >=95% tên/loại, >=80% model >=2 nhãn; không dấu Việt, nhãn thuộc từ vựng', async () => {
  const r = await seedCurated({ inputs: real, dryRun: true });
  console.log(`Thật: ${r.named}/${r.visible} tên+loại (${r.namedPercent.toFixed(2)}%); ${r.tagged}/${r.models} model ≥2 nhãn (${r.taggedPercent.toFixed(2)}%)`);
  assert.ok(r.namedPercent >= 95); assert.ok(r.taggedPercent >= 80);
  for (const { row } of prepared.candidates) {
    assert.ok(!/[À-ỹĐđ]/u.test(row.name), row.uid);
    assert.ok(row.tags.every(t => taxonomy.tags.includes(t)), row.uid);
    assert.ok(!Object.hasOwn(row, 'prompt')); assert.equal(row.reviewed, null);
  }
});

test('Chặn rò thật: private.md5 và mọi tên file Dota không vào curated/taxonomy/sources', async t => {
  const inv = await privateInventory();
  if (!inv.hasPrivateLock) t.diagnostic('BỎ QUA phần private.md5: không có file trên máy; vẫn kiểm tên Dota');
  const dir = path.join(repoRoot, 'library/curated');
  const texts = ['library/taxonomy.json', 'library/sources.json'].map(read);
  if (fs.existsSync(dir)) for (const name of fs.readdirSync(dir)) if (name.endsWith('.jsonl')) texts.push(fs.readFileSync(path.join(dir, name), 'utf8'));
  texts.push(...prepared.candidates.map(c => JSON.stringify(c.row)));
  assert.ok(texts.every(s => !leaks(s, inv)), 'Tên file riêng tư đã rò vào dữ liệu công khai');
  t.diagnostic(`Kiểm ${inv.names.length} tên riêng tư, ${texts.length} khối văn bản; không in tên riêng tư`);
});

// pnpm lib:scan chạy thật, mọi ghi out được chuyển sang os.tmpdir().
// Không đổi scanner của AL-06 hoặc mở quyền ghi out trong repo.
const guardSource = `
import fs from 'node:fs'; import path from 'node:path'; import {syncBuiltinESMExports} from 'node:module'; import {fileURLToPath} from 'node:url';
const root=process.env.AL11_TEMP, repo=process.env.AL11_REPO; let count=0;
function guard(p){const s=path.resolve(p instanceof URL?fileURLToPath(p):String(p));const rel=path.relative(root,s);if(rel.startsWith('..')||path.isAbsolute(rel))throw Error('K1 child: ghi ngoài cây tạm');count++;return s;}
function dest(p){const s=path.resolve(p instanceof URL?fileURLToPath(p):String(p));const out=path.join(repo,'library/out');return guard(s===out||s.startsWith(out+path.sep)?path.join(root,'scan-out',path.relative(out,s)):s);}
for(const name of ${JSON.stringify(mutations)})for(const [obj,key]of [[fs,name],[fs,name+'Sync'],[fs.promises,name]]){const original=obj[key];if(typeof original!=='function')continue;obj[key]=function(...args){const dual=['rename','copyFile','cp','symlink','link'].includes(name);if(dual){args[1]=dest(args[1]);if(name==='rename')args[0]=dest(args[0]);}else args[0]=dest(args[0]);return original.apply(this,args);};}
for(const [obj,key]of [[fs,'open'],[fs,'openSync'],[fs.promises,'open']]){const original=obj[key];obj[key]=function(p,flags,...rest){if(typeof flags==='number'?flags&(fs.constants.O_WRONLY|fs.constants.O_RDWR|fs.constants.O_CREAT|fs.constants.O_TRUNC|fs.constants.O_APPEND):/[wa+]/.test(flags))p=dest(p);return original.call(this,p,flags,...rest);};}
const stream=fs.createWriteStream;fs.createWriteStream=function(p,...args){return stream.call(this,dest(p),...args);};syncBuiltinESMExports();process.on('exit',()=>console.log('K1 child: '+count+' ghi chỉ vào cây tạm'));
`;

test('pnpm lib:scan được bọc fs trên nguồn thật; mọi câu tìm vàng đạt', { timeout: 180000 }, async t => {
  const guard = path.join(root, 'guard.mjs'); fs.writeFileSync(guard, guardSource);
  const output = await new Promise((resolve, reject) => {
    const child = spawn('pnpm', ['lib:scan'], { cwd: repoRoot, env: { ...process.env, AL11_TEMP: root, AL11_REPO: repoRoot,
      NODE_OPTIONS: `--import=${guard}`, COREPACK_ENABLE_NETWORK: '0', GIT_OPTIONAL_LOCKS: '0' }, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '', stderr = ''; child.stdout.on('data', d => stdout += d); child.stderr.on('data', d => stderr += d);
    const timer = setTimeout(() => { child.kill('SIGTERM'); reject(new Error('Quét quá 170 giây')); }, 170000);
    child.on('error', e => { clearTimeout(timer); reject(e); }); child.on('exit', code => { clearTimeout(timer); code === 0 ? resolve(stdout) : reject(new Error(`Quét exit ${code}: ${stderr.slice(-2000)} ${stdout.slice(-2000)}`)); });
  });
  t.diagnostic(output.trim());
  const catalog = JSON.parse(fs.readFileSync(path.join(root, 'scan-out/catalog.json'), 'utf8'));
  const current = prepareSeeds({ ...real, catalog, audio: { cards: [] } });
  const seedSnapshot = await seedCurated({ repoRoot: fixture('current-scan'), inputs: { ...real, catalog, audio: { cards: [] } } });
  assert.equal(seedSnapshot.added, current.candidates.length, 'Mỗi thẻ trong ảnh chụp lần quét mới sinh đúng một dòng');
  const stored = new Map(FILES.flatMap(name => JSON.parse('[' + read(`library/curated/${name}.jsonl`).trim().split('\n').join(',') + ']')).map(r => [r.uid, r]));
  const covered = current.candidates.filter(c => stored.has(c.row.uid));
  // Media của làn khác vẫn tăng trong lúc test; kiểm cổng 95% trên bản thật,
  // còn tính một-thẻ-một-dòng kiểm tuyệt đối trên ảnh chụp vừa quét trong cây tạm.
  assert.ok(covered.length / current.candidates.length >= 0.95, 'Độ phủ dòng thật dưới 95%');
  const named = covered.filter(c => { const row = stored.get(c.row.uid); return row.name && row.kind; });
  const models = covered.filter(c => c.type === 'model3d');
  const tagged = models.filter(c => stored.get(c.row.uid).tags.length >= 2);
  assert.ok(named.length / covered.length >= 0.95); assert.ok(tagged.length / models.length >= 0.8);
  t.diagnostic(`Sau quét mới: ${covered.length}/${current.candidates.length} thẻ có dòng; ${named.length} tên+loại; ${tagged.length}/${models.length} model ≥2 nhãn`);
  t.diagnostic(`Ảnh chụp tạm: ${seedSnapshot.added}/${current.candidates.length} dòng; cảnh báo chưa nối curated: ${catalog.warnings.filter(w => w.includes('dòng tuyển chọn không còn thẻ')).length}`);
  const index = createSearch(catalog, { taxonomy });
  for (const q of JSON.parse(read('library/test/queries.json'))) {
    const rows = index.search(q.query, { ...q.filters, limit: q.topN });
    const uids = rows.map(r => r.card.uid);
    for (const uid of q.mustInclude) assert.ok(uids.includes(uid), `${q.query}: thiếu ${uid}; ${uids.join(', ')}`);
    t.diagnostic(`${q.query}: ${q.mustInclude.length} uid bắt buộc đạt trong top ${q.topN}`);
  }
  const serialized = JSON.stringify(catalog); assert.ok(!/immortality-cultivation|tu-tien/u.test(serialized));
});
