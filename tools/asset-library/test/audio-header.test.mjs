import test, { after, mock } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { tmpdir, homedir } from 'node:os';
import { join, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';
import { performance } from 'node:perf_hooks';
import { audioHeader } from '../lib/audio-header.mjs';

const started = performance.now();
const root = fileURLToPath(new URL('../../../', import.meta.url));
const temporary = fs.mkdtempSync(join(tmpdir(), 'al04-audio-'));
const packagePath = join(root, 'package.json');
const dependenciesBefore = JSON.parse(fs.readFileSync(packagePath)).dependencies;
const writes = [];
const writableFds = new Set();
let fixtureBytes = 0;
let fixtureCount = 0;
const inside = (folder, path) => {
  const rel = relative(folder, resolve(path instanceof URL ? fileURLToPath(path) : String(path)));
  return rel === '' || (!rel.startsWith('..' + sep) && rel !== '..' && !rel.startsWith(sep));
};

// K1: bọc fs thật, gồm API callback, Sync, promises và open có cờ ghi.
// Mã sản xuất và bộ sinh fixture đều đi qua lớp này, không chỉ một mock truyền riêng.
const mutators = ['writeFile', 'appendFile', 'mkdir', 'rename', 'copyFile', 'cp', 'symlink',
  'link', 'unlink', 'rm', 'rmdir', 'truncate', 'chmod', 'chown', 'utimes', 'mkdtemp'];
function guard(path, operation) {
  assert.ok(inside(temporary, path), `K1: cấm ${operation} ngoài thư mục test: ${path}`);
  writes.push(operation);
}
for (const name of mutators) for (const suffix of ['', 'Sync']) {
  const key = name + suffix;
  if (typeof fs[key] !== 'function') continue;
  const original = fs[key];
  mock.method(fs, key, function (...args) {
    guard(args[0], key);
    if (['rename', 'copyFile', 'cp', 'symlink', 'link'].includes(name)) guard(args[1], key);
    return original.apply(this, args);
  });
}
for (const name of mutators) {
  if (typeof fs.promises[name] !== 'function') continue;
  const original = fs.promises[name];
  mock.method(fs.promises, name, function (...args) {
    guard(args[0], `promises.${name}`);
    if (['rename', 'copyFile', 'cp', 'symlink', 'link'].includes(name)) guard(args[1], name);
    return original.apply(this, args);
  });
}
for (const [object, key] of [[fs, 'open'], [fs, 'openSync'], [fs.promises, 'open']]) {
  const original = object[key];
  mock.method(object, key, function (path, flags, ...args) {
    const writing = typeof flags === 'number'
      ? !!(flags & (fs.constants.O_WRONLY | fs.constants.O_RDWR | fs.constants.O_CREAT | fs.constants.O_TRUNC | fs.constants.O_APPEND))
      : /[wa+]/u.test(flags);
    if (writing) guard(path, key);
    const result = original.call(this, path, flags, ...args);
    if (writing && key === 'openSync') writableFds.add(result);
    return result;
  });
}
for (const key of ['write', 'writeSync', 'writev', 'writevSync', 'ftruncate', 'ftruncateSync']) {
  const original = fs[key];
  mock.method(fs, key, function (fd, ...args) {
    assert.ok(writableFds.has(fd), `K1: ${key} cần fd ghi đã kiểm đường dẫn trong cây tạm`);
    writes.push(key);
    return original.call(this, fd, ...args);
  });
}
const originalClose = fs.closeSync;
mock.method(fs, 'closeSync', function (fd) {
  writableFds.delete(fd);
  return originalClose.call(this, fd);
});
const originalStream = fs.createWriteStream;
mock.method(fs, 'createWriteStream', function (path, ...args) {
  guard(path, 'createWriteStream');
  return originalStream.call(this, path, ...args);
});
after(() => {
  // Chỉ dọn đúng cây tạm do test này tạo; mọi fixture là vài KB, không lưu media vào repo.
  fs.rmSync(temporary, { recursive: true });
  mock.restoreAll();
});

function fixture(buffer, name = 'sample.bin') {
  fixtureBytes += buffer.length;
  fixtureCount++;
  const path = join(temporary, `${fixtureCount}-${name}`);
  fs.writeFileSync(path, buffer);
  return path;
}
function check(buffer, expected) {
  const path = fixture(buffer);
  const before = writes.length;
  const actual = audioHeader(path);
  assert.equal(writes.length, before, 'Parser không gọi API ghi');
  assert.deepEqual(actual, { ...expected, bytes: buffer.length });
  assert.deepEqual(audioHeader(buffer), actual, 'Buffer và file cho cùng kết quả');
  return path;
}
function chunk(kind, body, be = false) {
  const h = Buffer.alloc(8);
  h.write(kind);
  h[be ? 'writeUInt32BE' : 'writeUInt32LE'](body.length, 4);
  return Buffer.concat([h, body, Buffer.alloc(body.length & 1)]);
}
function wave({ float = false, extensible = false, be = false, dataFirst = false } = {}) {
  const rate = 48000;
  const channels = 2;
  const bits = float ? 32 : 16;
  const fmt = Buffer.alloc(extensible ? 40 : 16);
  const u16 = (n, offset) => fmt[be ? 'writeUInt16BE' : 'writeUInt16LE'](n, offset);
  const u32 = (n, offset) => fmt[be ? 'writeUInt32BE' : 'writeUInt32LE'](n, offset);
  const align = bits / 8 * channels;
  u16(extensible ? 0xfffe : float ? 3 : 1, 0);
  u16(channels, 2); u32(rate, 4); u32(rate * align, 8); u16(align, 12); u16(bits, 14);
  if (extensible) {
    u16(22, 16); u16(bits, 18); u32(3, 20); u16(float ? 3 : 1, 24);
    Buffer.from('00001000800000aa00389b71', 'hex').copy(fmt, 28);
  }
  const f = chunk('fmt ', fmt, be);
  const d = chunk('data', Buffer.alloc(48 * align), be);
  const body = Buffer.concat([Buffer.from('WAVE'), chunk('JUNK', Buffer.from('odd'), be), ...(dataFirst ? [d, f] : [f, d])]);
  return chunk(be ? 'RIFX' : 'RIFF', body, be);
}
function oggPage(body, { serial = 7, granule = 0n, flags = 0, laces, sequence = 0 } = {}) {
  laces ??= [...Array(Math.floor(body.length / 255)).fill(255), body.length % 255];
  const head = Buffer.alloc(27);
  head.write('OggS'); head[5] = flags; head.writeBigUInt64LE(granule, 6);
  head.writeUInt32LE(serial, 14); head.writeUInt32LE(sequence, 18); head[26] = laces.length;
  // Không giải mã âm và không kiểm CRC: fixture chỉ chứa cấu trúc cần đọc metadata.
  return Buffer.concat([head, Buffer.from(laces), body]);
}
function vorbisHead(length = 30) {
  const head = Buffer.alloc(length);
  head.write('\x01vorbis', 'latin1'); head[11] = 1; head.writeUInt32LE(44100, 12);
  head[28] = 0x76; head[29] = 1;
  return head;
}
function opusHead() {
  const b = Buffer.alloc(19);
  b.write('OpusHead'); b[8] = 1; b[9] = 2; b.writeUInt16LE(312, 10);
  b.writeUInt32LE(24000, 12); // Không nhầm input rate với clock 48 kHz.
  return b;
}
function mpegFrame({ version = 3, layer = 3, bitrate = 9, rate = 0, mono = false, pad = 0, crc = false } = {}) {
  const sampleRate = [44100, 48000, 32000][rate] / (version === 3 ? 1 : version === 2 ? 2 : 4);
  const kbps = layer === 1 ? [0, 32, 64, 96, 128, 160, 192, 224, 256, 288][bitrate]
    : version === 3 ? [0, 32, 40, 48, 56, 64, 80, 96, 112, 128][bitrate]
      : [0, 8, 16, 24, 32, 40, 48, 56, 64, 80][bitrate];
  const size = layer === 1 ? (Math.floor(12000 * kbps / sampleRate) + pad) * 4
    : Math.floor((version === 3 ? 144000 : 72000) * kbps / sampleRate) + pad;
  const b = Buffer.alloc(size);
  b[0] = 255; b[1] = 224 | (version << 3) | ((4 - layer) << 1) | (crc ? 0 : 1);
  b[2] = (bitrate << 4) | (rate << 2) | (pad << 1); b[3] = mono ? 192 : 0;
  return b;
}
function atom(kind, body, wide = false) {
  const h = Buffer.alloc(wide ? 16 : 8);
  h.writeUInt32BE(wide ? 1 : h.length + body.length); h.write(kind, 4);
  if (wide) h.writeBigUInt64BE(BigInt(h.length + body.length), 8);
  return Buffer.concat([h, body]);
}
function movie({ version = 0, wide = false, codec = 'mp4a' } = {}) {
  const mvhd = Buffer.alloc(version ? 32 : 20);
  mvhd[0] = version; mvhd.writeUInt32BE(1000, version ? 20 : 12);
  if (version) mvhd.writeBigUInt64BE(1234n, 24); else mvhd.writeUInt32BE(1234, 16);
  const entry = Buffer.alloc(28); entry.writeUInt16BE(2, 16); entry.writeUInt32BE(48000 * 65536, 24);
  const prefix = Buffer.alloc(8); prefix.writeUInt32BE(1, 4);
  const hdlr = Buffer.alloc(12); hdlr.write('soun', 8);
  const stsd = atom('stsd', Buffer.concat([prefix, atom(codec, entry)]));
  const trak = atom('trak', atom('mdia', Buffer.concat([atom('hdlr', hdlr), atom('minf', atom('stbl', stsd))])));
  return Buffer.concat([atom('ftyp', Buffer.from('M4A \0\0\0\0')), atom('mdat', Buffer.alloc(12)),
    atom('moov', Buffer.concat([atom('mvhd', mvhd), trak]), wide)]);
}

test('K1 · chặn ghi ngoài cây tạm; parser chỉ đọc và đóng fd khi lỗi', async t => {
  const forbidden = join(root, 'tools/asset-library/lib/audio-header.mjs');
  assert.throws(() => fs.writeFileSync(forbidden, ''), /K1/u);
  assert.throws(() => fs.appendFileSync(forbidden, ''), /K1/u);
  assert.throws(() => fs.mkdirSync(join(root, 'library')), /K1/u);
  assert.throws(() => fs.openSync(forbidden, 'r+'), /K1/u);
  assert.throws(() => fs.openSync(forbidden, fs.constants.O_RDWR), /K1/u);
  assert.throws(() => fs.promises.writeFile(forbidden, ''), /K1/u);
  const broken = fixture(Buffer.from('OggS'), 'broken.ogg');
  const close = mock.method(fs, 'closeSync');
  const before = close.mock.callCount();
  assert.throws(() => audioHeader(broken), /không hợp lệ/u);
  assert.equal(close.mock.callCount(), before + 1);
  t.diagnostic('fs callback/Sync/promises, open cờ ghi, fd/stream được bọc; 0 lần parser gọi ghi');
});

test('WAV · PCM, float, extensible, RIFX, chunk lẻ và data trước fmt', () => {
  for (const float of [false, true]) for (const extensible of [false, true]) for (const be of [false, true]) {
    check(wave({ float, extensible, be, dataFirst: extensible }), {
      codec: `pcm_${float ? 'f32' : 's16'}${be ? 'be' : 'le'}`, sampleRate: 48000, channels: 2, durationMs: 1,
    });
  }
  const bad = wave(); bad.writeUInt32LE(0x7fffffff, 16);
  assert.throws(() => audioHeader(bad), /cắt ngắn/u);
});

test('Ogg · Vorbis lấy granule cuối, Opus trừ pre-skip, packet qua nhiều trang', () => {
  check(Buffer.concat([oggPage(vorbisHead(), { flags: 2 }),
    oggPage(Buffer.from([0]), { granule: 441n, flags: 4, sequence: 1 })]), {
    codec: 'vorbis', sampleRate: 44100, channels: 1, durationMs: 10,
  });
  check(Buffer.concat([oggPage(opusHead(), { flags: 2 }),
    oggPage(Buffer.from([0]), { granule: 48312n, flags: 4, sequence: 1 })]), {
    codec: 'opus', sampleRate: 48000, channels: 2, durationMs: 1000,
  });
  const h = vorbisHead(300);
  check(Buffer.concat([oggPage(h.subarray(0, 255), { laces: [255], granule: 0xffffffffffffffffn, flags: 2 }),
    oggPage(h.subarray(255), { flags: 1, sequence: 1 }),
    oggPage(Buffer.from([0]), { granule: 88200n, sequence: 2 }),
    oggPage(Buffer.from([0]), { granule: 0xffffffffffffffffn, sequence: 3 })]), {
    codec: 'vorbis', sampleRate: 44100, channels: 1, durationMs: 2000,
  });
  const multiplex = Buffer.concat([oggPage(Buffer.from('other'), { serial: 8 }),
    oggPage(vorbisHead()), oggPage(Buffer.from([0]), { granule: 44100n }),
    oggPage(Buffer.from([0]), { serial: 8, granule: 999999n })]);
  assert.equal(audioHeader(multiplex).durationMs, 1000, 'Không lấy granule của stream khác');
  assert.throws(() => audioHeader(oggPage(opusHead(), { granule: 100n })), /granule/u);
  assert.throws(() => audioHeader(multiplex.subarray(0, multiplex.length - 1)), /cắt ngắn/u);
});

test('MP3 · Xing/Info, VBRI, ID3, quét VBR/CBR, MPEG-2/2.5 và CRC', () => {
  for (const crc of [false, true]) for (const kind of ['Xing', 'Info', 'VBRI']) {
    const first = mpegFrame({ crc });
    if (kind === 'VBRI') { first.write(kind, 36); first.writeUInt32BE(100, 50); }
    else { const x = 36 + (crc ? 2 : 0); first.write(kind, x); first.writeUInt32BE(1, x + 4); first.writeUInt32BE(100, x + 8); }
    check(Buffer.concat([first, mpegFrame()]), {
      codec: 'mp3', sampleRate: 44100, channels: 2, durationMs: Math.round(100 * 1152 / 44100 * 1000),
    });
  }
  for (const version of [3, 2, 0]) {
    const sampleRate = 44100 / (version === 3 ? 1 : version === 2 ? 2 : 4);
    const id3 = Buffer.alloc(10); id3.write('ID3'); id3[3] = 4; id3[5] = 16; id3[9] = 7;
    const data = Buffer.concat([id3, Buffer.alloc(17), mpegFrame({ version, mono: true }),
      mpegFrame({ version, mono: true, bitrate: 5, pad: 1 }), Buffer.from('TAG'), Buffer.alloc(125)]);
    check(data, { codec: 'mp3', sampleRate, channels: 1,
      durationMs: Math.round((version === 3 ? 1152 : 576) * 2 / sampleRate * 1000) });
  }
  check(Buffer.concat([mpegFrame(), mpegFrame({ pad: 1 }), mpegFrame()]), {
    codec: 'mp3', sampleRate: 44100, channels: 2, durationMs: Math.round(3 * 1152 / 44100 * 1000),
  });
  const gapless = mpegFrame();
  gapless.write('Xing', 36); gapless.writeUInt32BE(15, 40); gapless.writeUInt32BE(31, 44);
  gapless.write('LAME3.99r', 156);
  Buffer.from([0x24, 0x06, 0x04]).copy(gapless, 177); // delay 576, padding 1540.
  check(Buffer.concat([gapless, mpegFrame()]), {
    codec: 'mp3', sampleRate: 44100, channels: 2, durationMs: 762,
  });
  assert.throws(() => audioHeader(Buffer.from('ID3\x04\0\0\xff\0\0\0', 'latin1')), /ID3/u);
});

test('M4A · mvhd v0/v1, moov sau mdat, atom 64-bit và sample entry AAC/ALAC', () => {
  for (const version of [0, 1]) for (const wide of [false, true]) for (const codec of ['mp4a', 'alac']) {
    check(movie({ version, wide, codec }), {
      codec: codec === 'mp4a' ? 'aac' : 'alac', sampleRate: 48000, channels: 2, durationMs: 1234,
    });
  }
  const bad = movie(); bad.writeUInt32BE(0x7fffffff, 0);
  assert.throws(() => audioHeader(bad), /atom/u);
});

test('File rỗng, định dạng lạ, đầu file bị cắt: báo lỗi thay vì metadata giả', () => {
  for (const b of [Buffer.alloc(0), Buffer.from('not audio'), Buffer.from('RIFF'), Buffer.from('OggS'),
    Buffer.from([255, 251, 144, 0]), movie().subarray(0, 33), wave().subarray(0, 21)]) {
    assert.throws(() => audioHeader(b), /không hợp lệ/u);
  }
});

test('Đọc theo cửa sổ: WAV/M4A bỏ qua payload lớn, không nạp cả file', () => {
  const wav = wave();
  const data = wav.indexOf('data');
  const size = 32 * 1024 * 1024;
  // File ảo; không ghi 32 MB xuống đĩa.
  wav.writeUInt32LE(size - 8, 4); wav.writeUInt32LE(size - data - 8, data + 4);
  let virtualSize = size;
  let segments = [{ start: 0, buffer: wav }];
  let totalRead = 0;
  let closed = 0;
  const virtualFs = {
    openSync: (_path, flags) => { assert.equal(flags, 'r'); return 8; },
    fstatSync: () => ({ size: virtualSize }),
    readSync: (_fd, target, offset, length, position) => {
      totalRead += length;
      target.fill(0, offset, offset + length);
      for (const segment of segments) {
        const from = Math.max(position, segment.start);
        const end = Math.min(position + length, segment.start + segment.buffer.length);
        if (from < end) segment.buffer.copy(target, offset + from - position, from - segment.start, end - segment.start);
      }
      return length;
    },
    closeSync: () => { closed++; },
  };
  assert.equal(audioHeader('virtual.wav', { fs: virtualFs }).bytes, size);
  assert.equal(closed, 1);
  assert.ok(totalRead <= 65536, `${totalRead} byte đọc`);
  const original = movie();
  const tail = original.subarray(original.indexOf('moov') - 4);
  const front = Buffer.concat([original.subarray(0, 16), Buffer.alloc(8)]);
  front.writeUInt32BE(size - 16, 16); front.write('mdat', 20);
  virtualSize = size + tail.length;
  segments = [{ start: 0, buffer: front }, { start: size, buffer: tail }];
  totalRead = 0;
  assert.deepEqual(audioHeader('virtual.m4a', { fs: virtualFs }), {
    codec: 'aac', sampleRate: 48000, channels: 2, durationMs: 1234, bytes: virtualSize,
  });
  assert.equal(closed, 2);
  assert.ok(totalRead < 70000, `${totalRead} byte đọc, bỏ qua 32 MB mdat`);
});

function seededShuffle(rows, initial) {
  let seed = initial;
  const result = [...rows].sort((a, b) => a.file < b.file ? -1 : a.file > b.file ? 1 : 0);
  for (let i = result.length - 1; i > 0; i--) {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    const j = seed % (i + 1);
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

test('1 · AudioLab: 60 mẫu cố định, 30 Kenney + 30 VCSL khớp index', t => {
  const base = join(homedir(), 'AudioLab/libraries');
  let index;
  try { index = JSON.parse(fs.readFileSync(join(base, 'index.json'))); } catch (error) {
    if (!['ENOENT', 'EACCES', 'EPERM'].includes(error.code)) throw error;
    return t.skip(`Không đọc được ~/AudioLab/libraries/index.json (${error.code}); Claude chạy lại phần thật khi duyệt`);
  }
  const seed = 20261028; // Ngày giao phiếu, độc lập với thứ tự index.
  const rows = ['kenney', 'vcsl'].flatMap(library => {
    const available = index.files.filter(row => row.library === library);
    assert.ok(available.length >= 30, `${library} phải có ít nhất 30 mẫu`);
    return seededShuffle(available, seed).slice(0, 30);
  });
  let maxError = 0;
  const codecs = {};
  for (const row of rows) {
    assert.match(row.file, /^(kenney|vcsl)\//u);
    const path = join(base, row.file);
    assert.ok(inside(base, path));
    let actual;
    try { actual = audioHeader(path); } catch (error) {
      if (!['ENOENT', 'EACCES', 'EPERM'].includes(error.code)) throw error;
      return t.skip(`Không đọc được mẫu AudioLab (${error.code}); Claude chạy lại phần thật khi duyệt`);
    }
    assert.equal(actual.sampleRate, row.sample_rate, row.file);
    assert.equal(actual.channels, row.channels, row.file);
    assert.equal(actual.bytes, row.bytes, row.file);
    const error = Math.abs(actual.durationMs - row.duration * 1000);
    maxError = Math.max(error, maxError);
    codecs[actual.codec] = (codecs[actual.codec] ?? 0) + 1;
    assert.ok(error <= Math.max(5, row.duration * 10), `${row.file}: lệch ${error} ms`);
  }
  assert.equal(rows.length, 60);
  t.diagnostic(`seed=${seed}; 60/60 (Kenney 30, VCSL 30); lệch tối đa ${maxError.toFixed(3)} ms; ${JSON.stringify(codecs)}`);
});

function probe(path) {
  return new Promise((resolveProbe, reject) => {
    const child = spawn('/opt/homebrew/bin/ffprobe', ['-v', 'error', '-select_streams', 'a:0',
      '-show_entries', 'stream=codec_name,sample_rate,channels,duration:format=duration', '-of', 'json', path],
    { stdio: ['ignore', 'pipe', 'pipe'] });
    let output = '';
    let errors = '';
    child.stdout.on('data', data => { output += data; });
    child.stderr.on('data', data => { errors += data; });
    child.on('error', reject);
    child.on('close', code => {
      if (code !== 0) return reject(new Error(`ffprobe ${path}: ${errors}`));
      try { resolveProbe(JSON.parse(output)); } catch (error) { reject(error); }
    });
  });
}

test('2 · Space: đủ 116 file, đối chiếu ffprobe trong 10 ms; click.ogg = 10 ms', async t => {
  const files = ['games/space-typing/public/assets/audio', 'games/space-typing/src/assets/audio/ui']
    .flatMap(folder => fs.readdirSync(join(root, folder), { recursive: true, withFileTypes: true })
      .filter(entry => entry.isFile() && /\.(wav|ogg|opus|mp3|m4a)$/iu.test(entry.name))
      .map(entry => join(entry.parentPath, entry.name))).sort();
  assert.equal(files.length, 116, 'Không bỏ sót file âm trong hai cây của Space');
  const click = audioHeader(join(root, 'games/space-typing/src/assets/audio/ui/click.ogg'));
  assert.deepEqual({ ...click, bytes: undefined }, {
    codec: 'vorbis', sampleRate: 44100, channels: 1, durationMs: 10, bytes: undefined,
  });
  try { fs.accessSync('/opt/homebrew/bin/ffprobe', fs.constants.X_OK); } catch (error) {
    return t.skip(`Thiếu ffprobe tại /opt/homebrew/bin/ffprobe (${error.code}); Claude chạy lại khi duyệt`);
  }
  let cursor = 0;
  let checked = 0;
  let maxError = 0;
  let worst = '';
  const codecs = {};
  const parsingStart = performance.now();
  const headers = files.map(path => audioHeader(path));
  const parsingMs = performance.now() - parsingStart;
  await Promise.all(Array.from({ length: 8 }, async () => {
    while (cursor < files.length) {
      const i = cursor++;
      const path = files[i];
      const expected = await probe(path);
      const stream = expected.streams[0];
      const actual = headers[i];
      assert.equal(actual.codec, stream.codec_name, path);
      assert.equal(actual.sampleRate, Number(stream.sample_rate), path);
      assert.equal(actual.channels, stream.channels, path);
      const expectedMs = Number(stream.duration ?? expected.format.duration) * 1000;
      const error = Math.abs(actual.durationMs - expectedMs);
      if (error > maxError) { maxError = error; worst = relative(root, path); }
      assert.ok(error <= 10, `${path}: ${actual.durationMs} ms so với ffprobe ${expectedMs} ms, lệch ${error} ms`);
      codecs[actual.codec] = (codecs[actual.codec] ?? 0) + 1;
      checked++;
    }
  }));
  t.diagnostic(`116/116; ${JSON.stringify(codecs)}; lệch tối đa ${maxError.toFixed(3)} ms (${worst}); đọc Node ${parsingMs.toFixed(1)} ms`);
  t.diagnostic('click.ogg: vorbis, 44100 Hz, 1 kênh, 10 ms');
  assert.equal(checked, 116);
});

test('3 · Cả lượt dưới 5 giây; dependencies không đổi; fixture dưới 50 KB', t => {
  assert.deepEqual(JSON.parse(fs.readFileSync(packagePath)).dependencies, dependenciesBefore);
  assert.ok(fixtureBytes < 50000, `${fixtureBytes} byte fixture`);
  const elapsed = performance.now() - started;
  assert.ok(elapsed < 5000, `Cả lượt ${elapsed.toFixed(1)} ms, phải < 5000 ms`);
  t.diagnostic(`${elapsed.toFixed(1)} ms; ${fixtureCount} fixture, ${fixtureBytes} byte; dependencies không đổi`);
});
