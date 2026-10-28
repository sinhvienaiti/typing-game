import test from 'node:test';
import assert from 'node:assert/strict';
import * as fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { constants } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { runFind, REPO_ROOT } from '../find.mjs';
import { runShow, resolveCard, copyCommand } from '../show.mjs';
import { runPlay, runProcess } from '../play.mjs';

const readJson = async p => JSON.parse(await fs.readFile(p, 'utf8'));
const sample = await readJson(new URL('./fixtures/catalog-small.json', import.meta.url));
const taxonomy = await readJson(new URL('../../../library/taxonomy.json', import.meta.url));
const scannedAt = '2026-10-28T00:00:00.000Z';
const catalog = { ...sample, scannedAt };
const writes = [];

// K1: mọi API ghi của công cụ phải ở cây tạm mà chính test tạo.
// Chặn cả API chưa dùng để hồi quy không âm thầm ghi vào repo hoặc nguồn.
function guardedIo(root, readOnly = false) {
  const check = p => {
    const resolved = path.resolve(p instanceof URL ? fileURLToPath(p) : p);
    assert.ok(!readOnly && resolved.startsWith(root + path.sep), `K1: chặn ghi ${resolved}`);
    writes.push(resolved);
  };
  const io = { ...fs };
  for (const name of ['writeFile', 'appendFile', 'mkdir', 'mkdtemp', 'unlink', 'rm', 'rmdir', 'truncate', 'chmod', 'utimes']) {
    io[name] = (p, ...args) => { check(p); return fs[name](p, ...args); };
  }
  for (const name of ['rename', 'link']) io[name] = (from, to, ...args) => { check(from); check(to); return fs[name](from, to, ...args); };
  for (const name of ['copyFile', 'symlink']) io[name] = (from, to, ...args) => { check(to); return fs[name](from, to, ...args); };
  io.open = (p, flags, ...args) => {
    if (typeof flags === 'number' ? Boolean(flags & (constants.O_WRONLY | constants.O_RDWR | constants.O_CREAT | constants.O_TRUNC | constants.O_APPEND)) : /[wa+]/u.test(flags)) check(p);
    return fs.open(p, flags, ...args);
  };
  return io;
}

async function fixture(t, data = catalog) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'asset-library-cli-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  await fs.mkdir(path.join(root, 'library/out'), { recursive: true });
  await fs.writeFile(path.join(root, 'library/out/catalog.json'), JSON.stringify(data));
  await fs.writeFile(path.join(root, 'library/taxonomy.json'), JSON.stringify(taxonomy));
  return { root, io: guardedIo(root) };
}

async function invoke(run, args, ctx = {}) {
  let out = '', err = '';
  const code = await run(args, { ...ctx, stdout: { write: s => { out += s; } }, stderr: { write: s => { err += s; } } });
  return { code, out, err };
}

function assertCard(card) {
  assert.equal(typeof card.uid, 'string');
  assert.ok(['image', 'model3d', 'audio', 'music'].includes(card.type));
  assert.ok(Array.isArray(card.files));
  for (const file of card.files) {
    assert.equal(typeof file.path, 'string');
    assert.equal(typeof file.role, 'string');
  }
}

test('find --json giữ lược đồ asset-library/1 và thẻ gốc; toàn bộ bộ lọc AL-09', async t => {
  const { root, io } = await fixture(t);
  const result = await invoke(runFind, ['hut', '--type', '3d', '--json'], { repoRoot: root, io });
  assert.equal(result.code, 0);
  const data = JSON.parse(result.out);
  assert.equal(data.schema, 'asset-library/1');
  assert.equal(data.scannedAt, scannedAt);
  assert.equal(data.cards.length, 4);
  for (const card of data.cards) { assertCard(card); assert.deepEqual(card, catalog.cards.find(c => c.uid === card.uid)); }
  const filters = ['--type=3d', '--kind', 'building', '--sub', 'hut', '--tag', 'wood', '--tag', 'thatch',
    '--biome', 'pine-forest', '--style', 'mythic-forest', '--game', 'dragon-hold', '--used-by', 'typing-defense',
    '--status', 'shipped', '--pipeline', 'runtime', '--min-score', '9', '--max-tris', '5000', '--has', 'clips',
    '--has', 'rig', '--drive', 'no', '--limit', '1', '--json'];
  assert.deepEqual(JSON.parse((await invoke(runFind, filters, { repoRoot: root, io })).out).cards.map(c => c.uid), ['dragon-hold:houses/herb-hut']);
  const empty = await invoke(runFind, ['zzzzzz', '--json'], { repoRoot: root, io });
  assert.deepEqual(JSON.parse(empty.out).cards, []);
});

test('find dạng bảng có đủ cột, runtime r, dấu phẩy, tổng và limit; cổng all/requested', async t => {
  const { root, io } = await fixture(t);
  const result = await invoke(runFind, ['hut', '--type', '3d', '--limit', '2'], { repoRoot: root, io });
  for (const value of ['uid', 'tên', 'loại/con', 'game', 'tam giác', 'chất lượng', 'Drive', '4.400 r', '(2 trên 4']) assert.ok(result.out.includes(value), value);
  const all = JSON.parse((await invoke(runFind, ['hut', '--all', '--requested', '--json'], { repoRoot: root, io })).out);
  for (const uid of ['test:rejected', 'test:draft', 'test:requested']) assert.ok(all.cards.some(c => c.uid === uid));
  const zero = await invoke(runFind, ['--limit', '0', '--json'], { repoRoot: root, io });
  assert.deepEqual(JSON.parse(zero.out).cards, []);
});

test('show mã ngắn mở đúng thẻ; --all giữ nguyên thẻ, mặc định ẩn chi tiết; lệnh copy dùng uid đầy đủ', async t => {
  const { root, io } = await fixture(t);
  const result = await invoke(runShow, ['dragon-hold:herb-hut', '--json'], { repoRoot: root, io });
  assert.equal(result.code, 0);
  const card = JSON.parse(result.out);
  assertCard(card);
  assert.equal(card.uid, 'dragon-hold:houses/herb-hut');
  assert.equal(card.files.length, 3);
  assert.ok(card.files.every(f => !f.hidden));
  const all = JSON.parse((await invoke(runShow, ['dragon-hold:herb-hut', '--all', '--json'], { repoRoot: root, io })).out);
  assert.deepEqual(all, catalog.cards[0]);
  const text = (await invoke(runShow, ['dragon-hold:herb-hut'], { repoRoot: root, io })).out;
  assert.ok(text.includes('pnpm lib:copy dragon-hold:houses/herb-hut --to <game>'));
  for (const value of ['vai trò', 'glb-original', 'runtime-high', 'Ẩn 2 file', 'provenance', 'usedBy']) assert.ok(text.includes(value));
  assert.ok(copyCommand({ uid: "kenney:pack/odd' name" }).includes("'kenney:pack/odd'\"'\"' name'"));
});

test('show: uid chính xác thắng mã ngắn; mã ngắn trùng hoặc không tồn tại báo lỗi rõ', () => {
  const cards = { cards: [{ uid: 'game:a/hut' }, { uid: 'game:b/hut' }, { uid: 'other:hut' }] };
  assert.equal(resolveCard(cards, 'game:a/hut').uid, 'game:a/hut');
  assert.throws(() => resolveCard(cards, 'game:hut'), /không duy nhất.*game:hut\ngame:a\/hut\ngame:b\/hut/u);
  assert.equal(resolveCard(cards, 'other:hut').uid, 'other:hut');
  assert.throws(() => resolveCard(cards, 'missing:hut'), /Không tìm thấy/u);
});

test('báo cũ qua stderr cho media.md5, SOURCES và manifest model lồng; stdout JSON vẫn hợp lệ', async t => {
  const { root, io } = await fixture(t);
  const newer = ['games/dragon-hold/media.md5', 'games/typing-defense/art-src/3d/SOURCES.json',
    'games/dragon-hold/public/assets/dragon-hold/models/m0b/manifest.json'];
  const old = 'games/space-typing/media.md5';
  for (const rel of [...newer, old]) {
    const file = path.join(root, rel);
    await fs.mkdir(path.dirname(file), { recursive: true });
    await fs.writeFile(file, '{}');
    const date = new Date(Date.parse(scannedAt) + (rel === old ? -10000 : 10000));
    await fs.utimes(file, date, date);
  }
  const result = await invoke(runFind, ['hut', '--json'], { repoRoot: root, io });
  JSON.parse(result.out);
  assert.equal(result.code, 0);
  assert.equal(result.err.split('\n').filter(Boolean).length, 3);
  for (const rel of newer) assert.ok(result.err.includes(`Mục lục cũ hơn ${rel}; chạy pnpm lib:scan`));
  assert.ok(!result.err.includes(old));
});

test('báo cũ không đọc qua symlink; thư mục nguồn thiếu không gây lỗi', async t => {
  const { root, io } = await fixture(t);
  await fs.mkdir(path.join(root, 'games'), { recursive: true });
  await fs.symlink(path.join(root, 'private-target'), path.join(root, 'games/dragon-hold'));
  const observed = [];
  const guarded = { ...io, lstat: p => { observed.push(p); return io.lstat(p); } };
  const result = await invoke(runFind, ['hut', '--json'], { repoRoot: root, io: guarded });
  assert.equal(result.code, 0);
  assert.equal(result.err, '');
  assert.ok(!observed.some(p => p.includes('private-target') || p.includes('dragon-hold/media.md5')));
});

async function audioFixture(t) {
  const data = { schema: 'asset-library/1', scannedAt, cards: [{ uid: 'kenney:pack/wood', short: 'kenney:wood', type: 'audio', status: 'pass',
    files: [2, 1].map(n => ({ role: 'variant', variant: String(n), local: true, path: `audio/wood ${n}.ogg` })) }] };
  const ctx = await fixture(t, data);
  await fs.mkdir(path.join(ctx.root, 'audio'));
  for (const file of data.cards[0].files) await fs.writeFile(path.join(ctx.root, file.path), 'fake opus');
  return ctx;
}

test('afplay giả lỗi → ffmpeg giả tạo WAV trong cache tạm → afplay giả phát WAV; --variant 2', async t => {
  const { root, io } = await audioFixture(t);
  const bin = path.join(root, 'bin');
  await fs.mkdir(bin);
  const log = path.join(root, 'calls.jsonl');
  for (const command of ['afplay', 'ffmpeg']) {
    const executable = path.join(bin, command);
    const script = `#!${process.execPath}\n` +
      `const fs = require('node:fs'); const path = require('node:path');\n` +
      `const args = process.argv.slice(2); fs.appendFileSync(${JSON.stringify(log)}, JSON.stringify({command:${JSON.stringify(command)},args})+'\\n');\n` +
      (command === 'afplay' ? `process.exit(args[0].endsWith('.wav') && fs.existsSync(args[0]) ? 0 : 7);\n`
        : `const out=args.at(-1); if (!out.startsWith(${JSON.stringify(root + path.sep)})) process.exit(9); fs.writeFileSync(out, 'RIFF fake WAV');\n`);
    await fs.writeFile(executable, script, { mode: 0o755 });
  }
  const calls = [];
  const exec = async (command, args) => {
    calls.push({ command, args });
    // Gọi chương trình giả thật, không thay PATH chung và không mở thiết bị âm thanh.
    await runProcess(path.join(bin, command), args);
  };
  const result = await invoke(runPlay, ['kenney:wood', '--variant', '2'], { repoRoot: root, io, exec });
  assert.equal(result.code, 0);
  assert.match(result.err, /giải mã WAV/u);
  assert.deepEqual(calls.map(c => c.command), ['afplay', 'ffmpeg', 'afplay']);
  assert.equal(calls[0].args[0], path.join(root, 'audio/wood 2.ogg'));
  const wav = calls[2].args[0];
  assert.equal(path.dirname(wav), path.join(root, 'library/.cache/play'));
  assert.ok(wav.endsWith('.wav'));
  assert.equal(calls[1].args.at(-1), wav);
  assert.equal(calls[1].args[calls[1].args.indexOf('-i') + 1], calls[0].args[0]);
  assert.ok(calls[1].args.includes('-nostdin') && calls[1].args.includes('-n'));
  assert.deepEqual((await fs.readFile(log, 'utf8')).trim().split('\n').map(JSON.parse), calls);
  assert.equal(await fs.readFile(wav, 'utf8'), 'RIFF fake WAV');
  assert.equal(await fs.readFile(calls[0].args[0], 'utf8'), 'fake opus');
  t.diagnostic('3 lần chạy chương trình giả; 1 WAV dưới os.tmpdir(); 0 lần ghi cache thật, 0 lần phát âm thật.');
});

test('play thành công trực tiếp không tạo cache; lỗi ffmpeg/lần afplay hai được truyền ra', async t => {
  const { root, io } = await audioFixture(t);
  const calls = [];
  await invoke(runPlay, ['kenney:wood'], { repoRoot: root, io, exec: async (command, args) => { calls.push({ command, args }); } });
  assert.equal(calls.length, 1);
  assert.match(calls[0].args[0], /wood 1\.ogg$/u);
  await assert.rejects(fs.stat(path.join(root, 'library/.cache')), { code: 'ENOENT' });
  for (const failure of ['ffmpeg', 'afplay-wav']) {
    let count = 0;
    await assert.rejects(invoke(runPlay, ['kenney:wood'], { repoRoot: root, io, exec: async command => {
      count++;
      if (count === 1 || (failure === 'ffmpeg' ? command === 'ffmpeg' : count === 3)) throw new Error(`fake ${failure}`);
    } }), new RegExp(`fake ${failure}`, 'u'));
    assert.equal(count, failure === 'ffmpeg' ? 2 : 3);
  }
});

test('play kiểm loại, số thứ tự, nguồn thiếu và đường dẫn thoát cây trước khi chạy tiến trình', async t => {
  const { root, io } = await audioFixture(t);
  const exec = async () => { assert.fail('Không được gọi tiến trình'); };
  for (const n of ['0', '-1', '1.5', 'NaN', '3']) await assert.rejects(invoke(runPlay, ['kenney:wood', '--variant', n], { repoRoot: root, io, exec }));
  await fs.writeFile(path.join(root, 'library/out/catalog.json'), JSON.stringify(catalog));
  await assert.rejects(invoke(runPlay, ['dragon-hold:herb-hut'], { repoRoot: root, io, exec }), /không phải âm thanh/u);
  for (const p of ['../outside.ogg', '/outside.ogg', 'missing.ogg']) {
    const data = { ...catalog, cards: [{ uid: 'test:audio', type: 'audio', files: [{ role: 'variant', path: p }] }] };
    await fs.writeFile(path.join(root, 'library/out/catalog.json'), JSON.stringify(data));
    await assert.rejects(invoke(runPlay, ['test:audio'], { repoRoot: root, io, exec }));
  }
});

test('play mở AudioLab qua home được truyền vào; chặn symlink nguồn và symlink cache trước khi ghi', async t => {
  const { root, io } = await audioFixture(t);
  const home = path.join(root, 'home');
  const external = path.join(home, 'AudioLab/libraries/example/click.ogg');
  await fs.mkdir(path.dirname(external), { recursive: true });
  await fs.writeFile(external, 'fake audio');
  const data = { ...catalog, cards: [{ uid: 'test:external', type: 'audio', files: [
    { role: 'variant', path: '~/AudioLab/libraries/example/click.ogg' },
  ] }] };
  await fs.writeFile(path.join(root, 'library/out/catalog.json'), JSON.stringify(data));
  const calls = [];
  await invoke(runPlay, ['test:external'], { repoRoot: root, io, home, exec: async (name, args) => { calls.push({ name, args }); } });
  assert.deepEqual(calls, [{ name: 'afplay', args: [external] }]);
  const link = path.join(root, 'audio/link.ogg');
  await fs.symlink(external, link);
  data.cards[0].files[0].path = 'audio/link.ogg';
  await fs.writeFile(path.join(root, 'library/out/catalog.json'), JSON.stringify(data));
  await assert.rejects(invoke(runPlay, ['test:external'], { repoRoot: root, io, exec: async () => { assert.fail('Nguồn symlink'); } }), /symlink/u);
  data.cards[0].files[0].path = 'audio/wood 1.ogg';
  await fs.writeFile(path.join(root, 'library/out/catalog.json'), JSON.stringify(data));
  await fs.symlink(home, path.join(root, 'library/.cache'));
  const before = writes.length;
  let count = 0;
  await assert.rejects(invoke(runPlay, ['test:external'], { repoRoot: root, io, exec: async () => {
    count++; throw new Error('afplay giả lỗi');
  } }), /symlink/u);
  assert.equal(count, 1);
  assert.equal(writes.length, before);
});

test('tùy chọn sai, catalog sai/thiếu và mã thiếu không âm thầm thành công; --help không đọc file', async t => {
  const { root, io } = await fixture(t);
  for (const args of [['--typo'], ['--type'], ['--all=false'], ['--limit', '-1'], ['--limit', '1.2'], ['--has', 'unknown']]) {
    await assert.rejects(invoke(runFind, args, { repoRoot: root, io }));
  }
  for (const run of [runShow, runPlay]) await assert.rejects(invoke(run, [], { repoRoot: root, io }));
  await fs.writeFile(path.join(root, 'library/out/catalog.json'), '{"schema":"wrong","cards":[]}');
  await assert.rejects(invoke(runFind, [], { repoRoot: root, io }), /lược đồ/u);
  const missingRoot = path.join(root, 'missing');
  await assert.rejects(invoke(runShow, ['test:id'], { repoRoot: missingRoot, io }), /pnpm lib:scan/u);
  for (const run of [runFind, runShow, runPlay]) assert.equal((await invoke(run, ['--help'], { repoRoot: missingRoot, io })).code, 0);
});

test('K1: find/show mục lục thật chỉ đọc; các entrypoint CLI chạy thật và lỗi có exit 1', async t => {
  const io = guardedIo(REPO_ROOT, true);
  const find = await invoke(runFind, ['hut', '--type', '3d', '--json'], { io });
  assert.equal(find.code, 0);
  assert.ok(JSON.parse(find.out).cards.some(c => c.uid === 'dragon-hold:houses/herb-hut'));
  const show = await invoke(runShow, ['dragon-hold:herb-hut', '--json'], { io });
  assert.equal(JSON.parse(show.out).uid, 'dragon-hold:houses/herb-hut');
  for (const name of ['find', 'show', 'play']) {
    const file = fileURLToPath(new URL(`../${name}.mjs`, import.meta.url));
    assert.match(execFileSync(process.execPath, [file, '--help'], { encoding: 'utf8' }), /Cách dùng/u);
    assert.throws(() => execFileSync(process.execPath, [file, '--unknown'], { stdio: 'pipe' }), error => {
      assert.equal(error.status, 1); assert.match(error.stderr.toString(), /Lỗi: Tùy chọn không hỗ trợ/u); return true;
    });
  }
  t.diagnostic(`K1: ${writes.length} lời gọi ghi được bọc, tất cả trong cây tạm của test; find/show thật 0 lời gọi ghi.`);
});
