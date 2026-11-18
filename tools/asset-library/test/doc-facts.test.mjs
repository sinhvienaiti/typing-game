import test from 'node:test';
import assert from 'node:assert/strict';
import * as fs from 'node:fs/promises';
import path from 'node:path';
import { tmpdir } from 'node:os';
import { spawnSync } from 'node:child_process';
import { DOCUMENTS, REPO_ROOT, markdownRows, readDocFacts, writeDocFacts, mergeDocFacts } from '../doc-facts.mjs';
import { scan } from '../scan.mjs';

const table = (headers, rows) => [headers, headers.map(() => '---'), ...rows].map(r => '| ' + r.join(' | ') + ' |').join('\n');
const pngPath = 'games/dragon-hold/art-src/houses/herb-hut.png';
const glbPath = 'games/dragon-hold/art-src/3d/houses/herb-hut.glb';
async function put(root, rel, text) {
  await fs.mkdir(path.dirname(path.join(root, rel)), { recursive: true });
  await fs.writeFile(path.join(root, rel), text);
}
async function fixture(t) {
  const root = await fs.mkdtemp(path.join(tmpdir(), 'al07-docs-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  await put(root, DOCUMENTS[0], '# Rồng Giữ Ải\n' + table(
    ['id trong mã', 'Tên Việt hiện tại', 'Tên tiếng Anh đề xuất', 'Nghĩa Việt ngắn (cho lần đầu)'],
    [['`herb-hut`', 'Lều Thuốc Nam', 'Herb Hut', 'lều thảo dược'],
      ['`hero; banner`', 'Cờ', 'Banner', 'cờ hiệu']]));
  await put(root, DOCUMENTS[1], table(['Game', 'Mã · id', 'Tên', 'Ô ảnh Tripo · đường dẫn ảnh 2D', 'Face limit', 'Rig', 'Nơi lưu GLB gốc'],
    [['Rồng Giữ Ải', 'H1 · `herb-hut`', 'Nhà Thuốc Lá', `Image = \`${pngPath}\``, '10000', 'Không rig', `\`${glbPath}\``],
      ['Lời Gọi', '02-VS/V55 · `nha-rai-da`', 'Nhà Rái Đá', '`games/typing-defense/art-src/landmarks/nha-rai-da.png`', '8000', 'Không rig', '`games/typing-defense/art-src/3d/landmarks/nha-rai-da.glb`']]));
  await put(root, DOCUMENTS[2], table(['Game', 'Mã model', 'Thư mục Tripo', 'File Tripo', 'Tam giác', 'Đích', 'Độ tin'],
    [['Rồng Giữ Ải', '`rong_herb-hut`', 'face 10000 - không rig - 1 ảnh', '`fantasy+cottage+3d+model.glb`', '9.858', `\`${glbPath}\``, '0,98'],
      ['Rồng Giữ Ải', '`rong_herb-hut`', 'face 10000 - không rig - 1 ảnh', '`spare+cottage.glb`', '9000', '`games/dragon-hold/art-src/tripo-spares/herb-hut.alt.glb`', '0,97'],
      ['Tuyến Cuối', '`tuyencuoi_rainbow-scout`', 'face 5000 - không rig - 1 ảnh', '`crystal+insect.glb`', '4500', '`games/space-typing/art-src/3d/enemies/rainbow-tank.glb`', '0.75']]));
  await put(root, DOCUMENTS[3], table(['Mã model', 'Tên (Việt / Anh)', 'Thư mục Tripo', 'File Tripo', 'Tam giác', 'Đích', 'Độ tin', 'Điểm', 'Mức'],
    [['`loigoi_choi-canh-doi`', 'Chòi canh / Watch Hut', 'face 8000 - không rig - 1 ảnh', '`thatched+hut+3d+model (2).glb`', '7733', '`games/typing-defense/art-src/3d/landmarks/choi-canh-doi.glb`', '0,98', '9', 'Đạt'],
      ['`loigoi_nha-rai-da`', 'Nhà Rái Đá', 'face 8000 - không rig - 1 ảnh', '`thatched+hut+3d+model (1).glb`', '7289', '`games/typing-defense/art-src/3d/landmarks/nha-rai-da.glb`', '0,97', '8,5 (8 và 9)', 'Tạm chấp nhận']])
    + '\n\n' + table(['Mã', 'Lỗi không sửa rẻ', 'Mức cần'], [['V55 Nhà Rái Đá', 'Cửa bị nhòe', 'P2']]));
  await put(root, DOCUMENTS[4], '# Lời Gọi\n' + table(['Mã', 'File', 'Điểm', 'Mức cần'],
    [['V55 Nhà Rái Đá', '[nhà](../../games/typing-defense/art-src/3d/landmarks/nha-rai-da.glb)', '8,5', 'P3']]));
  await put(root, DOCUMENTS[5], '# Rồng Giữ Ải\n' + table(['Mã', 'Nội dung', 'Trạng thái', 'Ảnh'],
    [['H1', 'Lều Thuốc Nam `herb-hut`', 'Đạt 9,5', `[Herb Hut](../../${pngPath})`]]));
  await put(root, 'typing-game-handoff-2026-10-25/tripo-upload-dot3/INDEX.md', '# Rồng Giữ Ải\n' + table(
    ['Thư mục', 'Ảnh', 'Món', 'Cỡ thật trong game'],
    [['face 2000 - không rig - 1 ảnh', '`rong_wooden-jetty.png`', 'Wooden Jetty (cầu tàu gỗ nhỏ)', 'dài 4 m']]));
  await put(root, pngPath, 'ảnh mẫu');
  return root;
}

test('Markdown: nhiều bảng, cột chứa dấu | thoát, bằng chứng đúng dòng', () => {
  const text = '# Rồng Giữ Ải\n' + table(['Mã', 'Tên'], [['A', 'Một \\| hai']])
    + '\n\n## Ghi chú\n' + table(['Mã', 'Tên'], [['B', 'Ba']]);
  const { rows, stats } = markdownRows(text, 'sample.md');
  assert.equal(stats.rows, 2);
  assert.equal(stats.headers, 2);
  assert.equal(stats.separators, 2);
  assert.equal(rows[0].cells.Tên, 'Một | hai');
  assert.equal(rows[0].evidence, 'sample.md:4');
  assert.equal(rows[1].game, 'dragon-hold');
});

test('Cây mẫu: tên, nghĩa, điểm tách 2D/3D, tiền tố, face/rig, độ tin, INDEX và missing', async t => {
  const root = await fixture(t);
  const data = await readDocFacts({ repoRoot: root });
  const herb = data.byId['dragon-hold:herb-hut'];
  assert.equal(herb.name, 'Herb Hut');
  assert.equal(herb.nameVi, 'Lều Thuốc Nam');
  assert.equal(herb.meaning, 'lều thảo dược');
  assert.equal(herb.quality.score2d, 9.5);
  assert.equal(herb.triangles, 9858);
  assert.equal(herb.provenance.faceLimit, 10000);
  assert.equal(herb.provenance.rig, 'không rig');
  assert.equal(herb.confidence, 0.98);
  assert.equal(herb.provenance.tripoFile, 'fantasy+cottage+3d+model.glb');
  assert.equal(data.byPath['games/dragon-hold/art-src/tripo-spares/herb-hut.alt.glb'].provenance.tripoFile, 'spare+cottage.glb');
  assert.ok(herb.quality.evidence.includes(`${DOCUMENTS[5]}:4`));
  assert.ok(data.byId['dragon-hold:hero; banner']);
  assert.equal(data.byId['typing-defense:choi-canh-doi'].quality.score3d, 9);
  assert.equal(data.byId['typing-defense:choi-canh-doi'].quality.level, 'pass');
  assert.equal(data.byId['typing-defense:nha-rai-da'].quality.score3d, 8.5);
  assert.equal(data.byId['typing-defense:nha-rai-da'].quality.need, 'P2');
  assert.equal(data.byId['typing-defense:nha-rai-da'].quality.level, 'provisional');
  assert.ok(data.byId['typing-survival:rainbow-scout']);
  assert.equal(data.byId['dragon-hold:wooden-jetty'].name, 'Wooden Jetty');
  assert.ok(data.byPath[pngPath]);
  assert.ok(!data.missing.includes(pngPath));
  assert.ok(data.missing.includes(glbPath));
  assert.ok(data.missing.includes('typing-game-handoff-2026-10-25/tripo-upload-dot3/face 2000 - không rig - 1 ảnh/rong_wooden-jetty.png'));
  assert.ok(data.references.every(ref => ref.exists || data.missing.includes(ref.path)));
});

test('Gộp thẻ: tuyển chọn thắng tài liệu, giữ shipped, số đo thật và không nối nhầm id mơ hồ', async t => {
  const data = await readDocFacts({ repoRoot: await fixture(t) });
  const card = { uid: 'dragon-hold:houses/herb-hut', origin: 'dragon-hold', status: 'shipped',
    files: [{ path: pngPath }], name: 'Tên mồi', provenance: { ticket: '016' },
    model: { triangles: { original: 9000, high: 5000 } } };
  mergeDocFacts([card], data);
  assert.equal(card.name, 'Herb Hut');
  assert.equal(card.status, 'shipped');
  assert.equal(card.provenance.ticket, '016');
  assert.equal(card.model.triangles.original, 9000);
  const row = { uid: card.uid, name: 'Herb Hut duyệt', status: 'unscored', quality: { score2d: 10 }, provenance: { rig: 'Rig tay' } };
  Object.assign(card, row);
  mergeDocFacts([card], data, { curated: [row] });
  assert.equal(card.name, row.name);
  assert.equal(card.status, 'unscored');
  assert.equal(card.quality.score2d, 10);
  assert.equal(card.provenance.rig, 'Rig tay');
  const renamed = { ...card, uid: 'dragon-hold:houses/new-name', formerUids: [row.uid] };
  mergeDocFacts([renamed], data, { curated: [row] });
  assert.equal(renamed.name, row.name);
  const twins = ['a', 'b'].map(folder => ({ uid: `dragon-hold:${folder}/herb-hut`, origin: 'dragon-hold', files: [], status: 'unscored' }));
  mergeDocFacts(twins, data);
  assert.ok(twins.every(c => c.name === undefined));
});

test('scan.mjs đọc doc-facts.json sau AL-06; tuyển chọn khớp md5 sau đổi tên vẫn thắng', async t => {
  const root = await fixture(t);
  await writeDocFacts({ repoRoot: root });
  const sources = JSON.parse(await fs.readFile(path.join(REPO_ROOT, 'library/sources.json'), 'utf8'));
  await put(root, 'library/sources.json', JSON.stringify(sources));
  const md5 = 'a'.repeat(32);
  const lock = 'games/dragon-hold/media.md5';
  await put(root, lock, `${md5}  art-src/houses/herb-hut.png\n`);
  const curated = { uid: 'dragon-hold:houses/old-hut', md5s: [md5], name: 'Owner Hut', status: 'unscored', quality: { score2d: 10 } };
  const blocked = { uid: 'dragon-hold:houses/herb-hut', name: 'Tên bị chặn', quality: { evidence: [['tu', 'tien'].join('-')] } };
  await put(root, 'library/curated/dragon-hold.jsonl', JSON.stringify(curated) + '\n' + JSON.stringify(blocked) + '\n');
  const { catalog } = await scan({ repoRoot: root, game: 'dragon-hold', locksOnly: true,
    hooks: { trackedFiles: [lock] }, scanDate: '2026-10-28T06:00:00.000Z' });
  const card = catalog.cards.find(c => c.uid === 'dragon-hold:houses/herb-hut');
  assert.ok(card);
  assert.deepEqual(card.formerUids, [curated.uid]);
  assert.equal(card.name, curated.name);
  assert.equal(card.status, curated.status);
  assert.equal(card.quality.score2d, 10);
  assert.equal(card.provenance.tripoFile, 'fantasy+cottage+3d+model.glb');
  assert.ok(!JSON.stringify(catalog).includes(['tu', 'tien'].join('-')));
});

test('Vùng cấm, traversal, symlink và thư mục handoff không thuộc whitelist không được đọc', async t => {
  const root = await fixture(t);
  const denied = ['immortality', 'cultivation'].join('-');
  const bad = ['tu', 'tien'].join('-');
  await fs.appendFile(path.join(root, DOCUMENTS[1]), '\n\n## Tu Tiên\n' + table(['Mã · id', 'Nơi lưu GLB gốc'],
    [['`secret`', `\`games/${denied}/art-src/3d/secret.glb\``]]) + '\n\n## Lời Gọi\n'
    + table(['Mã · id', 'Nơi lưu GLB gốc'], [['`escape`', '`../../../../secret.glb`']]));
  await put(root, `docs/games/${bad}/secret.md`, 'không được đọc');
  await put(root, 'typing-game-handoff-2026-10-25/unrelated/INDEX.md', 'không được đọc');
  await put(root, 'outside/secret.md', 'không được đọc');
  await fs.mkdir(path.join(root, 'typing-game-handoff-2026-10-25/tripo-upload-linked'), { recursive: true });
  await fs.symlink(path.join(root, 'outside/secret.md'), path.join(root, 'typing-game-handoff-2026-10-25/tripo-upload-linked/INDEX.md'));
  const reads = [];
  const io = { ...fs, readFile: async (file, ...args) => { reads.push(path.relative(root, file)); return fs.readFile(file, ...args); } };
  const data = await writeDocFacts({ repoRoot: root, io });
  assert.ok(reads.every(p => DOCUMENTS.includes(p) || p.endsWith('tripo-upload-dot3/INDEX.md')));
  assert.ok(!JSON.stringify(data).includes(denied));
  assert.ok(!JSON.stringify(data).includes(bad));
  assert.ok(!data.missing.some(p => p.startsWith('..')));
  assert.equal(data.documents.find(d => d.file === DOCUMENTS[1]).excluded, 1);
  // Không được ghi xuyên symlink đầu ra, kể cả symlink trỏ vào thư mục tạm khác.
  const output = path.join(root, 'library/out/doc-facts.json');
  await fs.unlink(output);
  await fs.symlink(path.join(root, 'outside/secret.md'), output);
  await assert.rejects(writeDocFacts({ repoRoot: root }), /symlink/iu);
  t.diagnostic(`Đọc nguồn: ${reads.length}; đọc vùng cấm/symlink=0; rò tên cấm=0`);
});

test('K1: bọc fs toàn cục, mọi API ghi chỉ được vào doc-facts.json hoặc thư mục tạm của test', async t => {
  const root = await fixture(t);
  const script = `
    import fs from 'node:fs';
    import path from 'node:path';
    import assert from 'node:assert/strict';
    import { syncBuiltinESMExports } from 'node:module';
    const root = ${JSON.stringify(root)};
    const repo = ${JSON.stringify(REPO_ROOT)};
    let writes = 0;
    const guard = (name, file) => {
      const absolute = path.resolve(file);
      assert.ok(absolute.startsWith(root + path.sep) || absolute === path.join(repo, 'library/out')
        || absolute === path.join(repo, 'library/out/doc-facts.json'), name + ' ngoài phạm vi: ' + absolute);
      writes++;
    };
    for (const name of ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'symlink', 'unlink', 'rm', 'rmdir',
      'write', 'writev', 'truncate', 'ftruncate', 'link', 'mkdtemp', 'chmod', 'chown', 'utimes']) {
      for (const [object, key] of [[fs, name], [fs, name + 'Sync'], [fs.promises, name]]) if (typeof object[key] === 'function') {
        const original = object[key]; object[key] = function(file, ...args) {
          guard(name, file);
          if (['rename', 'copyFile', 'symlink', 'link'].includes(name)) guard(name + ' đích', args[0]);
          return original.call(this, file, ...args);
        };
      }
    }
    fs.createWriteStream = () => { throw new Error('Không được mở luồng ghi'); };
    for (const [object, key] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
      const original = object[key]; object[key] = function(file, flags, ...args) {
        const writing = typeof flags === 'number' ? Boolean(flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_TRUNC | fs.constants.O_APPEND)) : /[wa+]/u.test(flags ?? 'r');
        assert.equal(writing, false, 'open để ghi bị chặn: ' + file);
        return original.call(this, file, flags, ...args);
      };
    }
    syncBuiltinESMExports();
    const { writeDocFacts, readDocFacts } = await import(${JSON.stringify(new URL('../doc-facts.mjs', import.meta.url).href)});
    await writeDocFacts({ repoRoot: root });
    const afterFixture = writes;
    const data = await readDocFacts({ repoRoot: repo });
    assert.equal(writes, afterFixture);
    assert.ok(Object.keys(data.byId).length > 100);
    console.log('K1: ' + writes + ' lời gọi ghi trong cây tạm; đọc repo thật: 0 ghi; ngoài phạm vi: 0');
  `;
  const child = spawnSync(process.execPath, ['--input-type=module', '-e', script], { encoding: 'utf8', timeout: 30000 });
  assert.equal(child.status, 0, child.stdout + child.stderr);
  t.diagnostic(child.stdout.trim());
});

test('Repo thật: grep độc lập, 148 tên, đủ bảng nhập, bốn ca mẫu và mọi đường dẫn File/Đích được kiểm', async t => {
  const data = await readDocFacts();
  for (const doc of data.documents) {
    const file = path.join(REPO_ROOT, doc.file);
    const result = spawnSync('grep', ['-c', '^| ', file], { encoding: 'utf8' });
    assert.equal(result.status, 0, result.stderr);
    // Header = dòng ngay trước dòng kẻ; dòng kẻ có thể có hoặc không có dấu cách.
    const lines = (await fs.readFile(file, 'utf8')).split(/\r?\n/u);
    const rule = l => /^\|\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$/u.test(l ?? '');
    const headers = lines.filter((l, i) => /^\| /u.test(l) && rule(lines[i + 1])).length;
    const separatorsWithSpace = lines.filter(l => /^\| /u.test(l) && rule(l)).length;
    const expected = Number(result.stdout.trim()) - headers - separatorsWithSpace;
    assert.equal(doc.rows, expected, doc.file);
    t.diagnostic(`${doc.file}: grep=${result.stdout.trim()}, header=${headers}, kẻ có cách=${separatorsWithSpace}, dòng=${doc.rows}, fact=${doc.facts}, chặn=${doc.excluded}`);
  }
  assert.equal(data.documents.find(d => d.file === DOCUMENTS[0]).facts, 148);
  assert.ok(data.documents.find(d => d.file === DOCUMENTS[2]).facts >= 55);
  assert.ok(data.documents.find(d => d.file === DOCUMENTS[3]).facts >= 86);
  const hut = data.byId['typing-defense:choi-canh-doi'];
  assert.equal(hut.quality.score3d, 9);
  assert.equal(hut.quality.level, 'pass');
  assert.equal(hut.provenance.tripoFile, 'thatched+hut+3d+model (2).glb');
  assert.equal(hut.triangles, 7733);
  const rai = data.byId['typing-defense:nha-rai-da'];
  assert.equal(rai.quality.score3d, 8.5);
  assert.equal(rai.quality.level, 'provisional');
  assert.equal(data.byId['typing-defense:barracks-kit-l2'].provenance.tripoFile, 'wooden+hut+3d+model.glb');
  const herb = data.byId['dragon-hold:herb-hut'];
  assert.equal(herb.name, 'Herb Hut');
  assert.equal(herb.quality.score2d, 9.5);
  assert.ok(herb.quality.evidence.includes(`${DOCUMENTS[5]}:42`));
  assert.equal(herb.provenance.tripoFile, 'fantasy+cottage+3d+model.glb');
  // Tách đường dẫn bằng cách độc lập cho chính hai cột bắt buộc.
  let checked = 0;
  for (const doc of data.documents) {
    for (const row of markdownRows(await fs.readFile(path.join(REPO_ROOT, doc.file), 'utf8'), doc.file).rows) {
      for (const [column, value] of Object.entries(row.cells)) {
        if (column !== 'File' && column !== 'Đích') continue;
        const targets = [...value.matchAll(/\]\(([^)]+)\)|`([^`]+)`/gu)].map(m => m[1] ?? m[2]);
        for (const target of targets) {
          let rel = target;
          if (target.startsWith('../')) rel = path.posix.normalize(path.posix.join(path.posix.dirname(doc.file), target));
          else if (!target.startsWith('games/')) rel = `games/${row.game}/art-src/3d/${target}`;
          const ref = data.references.find(ref => ref.evidence === row.evidence && ref.column === column && ref.path === rel);
          assert.ok(ref, `Chưa kiểm ${row.evidence} ${column}: ${rel}`);
          assert.ok(ref.exists || data.missing.includes(rel));
          checked++;
        }
      }
    }
  }
  assert.ok(checked >= 200);
  for (const ref of data.references) {
    if (!ref.exists) assert.ok(data.missing.includes(ref.path));
  }
  t.diagnostic(`File/Đích: ${checked} đường dẫn; toàn bộ tham chiếu=${data.references.length}; missing[]=${data.missing.length}`);
  for (const p of data.missing) t.diagnostic(`MISSING ${p}`);
});
