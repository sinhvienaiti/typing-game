import nodeFs from 'node:fs';

const invalid = message => { throw new Error(`Đầu file âm thanh không hợp lệ: ${message}`); };
const text = (buffer, start = 0, end = buffer.length) => buffer.toString('latin1', start, end);

// Bộ đệm cửa sổ: không nạp cả bản nhạc; WAV/M4A bỏ qua thẳng các khối dữ liệu.
function reader(size, read) {
  let window = Buffer.alloc(0);
  let start = 0;
  return {
    size,
    get(offset, length) {
      if (!Number.isSafeInteger(offset) || !Number.isSafeInteger(length)
        || offset < 0 || length < 0 || offset + length > size) invalid('khối bị cắt ngắn');
      if (offset < start || offset + length > start + window.length) {
        start = offset;
        window = read(offset, Math.min(size - offset, Math.max(65536, length)));
      }
      return window.subarray(offset - start, offset - start + length);
    },
  };
}

function wav(r) {
  const head = r.get(0, 12);
  if (text(head, 8, 12) !== 'WAVE') invalid('RIFF không phải WAVE');
  const be = text(head, 0, 4) === 'RIFX';
  const u16 = (b, p) => be ? b.readUInt16BE(p) : b.readUInt16LE(p);
  const u32 = (b, p) => be ? b.readUInt32BE(p) : b.readUInt32LE(p);
  const end = Math.min(r.size, u32(head, 4) + 8);
  let format;
  let dataBytes = 0;
  let hasData = false;
  for (let p = 12; p + 8 <= end;) {
    const h = r.get(p, 8);
    const kind = text(h, 0, 4);
    const size = u32(h, 4);
    if (p + 8 + size > end) invalid('chunk WAV bị cắt ngắn');
    if (kind === 'fmt ') {
      if (size < 16) invalid('fmt WAV thiếu trường');
      const b = r.get(p + 8, Math.min(size, 40));
      let tag = u16(b, 0);
      if (tag === 0xfffe) {
        if (size < 40 || u16(b, 16) < 22) invalid('WAVE_FORMAT_EXTENSIBLE bị cắt ngắn');
        tag = u16(b, 24);
      }
      const channels = u16(b, 2);
      const sampleRate = u32(b, 4);
      const blockAlign = u16(b, 12);
      const bits = u16(b, 14);
      if (![1, 3].includes(tag)) invalid(`WAV codec ${tag} chưa hỗ trợ`);
      if (!channels || !sampleRate || !blockAlign || !bits) invalid('fmt WAV bằng 0');
      const endian = be ? 'be' : 'le';
      const codec = tag === 3 ? `pcm_f${bits}${endian}` : bits === 8 ? 'pcm_u8' : `pcm_s${bits}${endian}`;
      format = { codec, channels, sampleRate, blockAlign };
    } else if (kind === 'data') {
      dataBytes += size;
      hasData = true;
    }
    p += 8 + size + (size & 1);
  }
  if (!format || !hasData) invalid('WAV thiếu fmt hoặc data');
  const { blockAlign, ...result } = format;
  return { ...result, durationMs: dataBytes / blockAlign / format.sampleRate * 1000 };
}

function ogg(r) {
  const streams = new Map();
  let selected;
  for (let p = 0; p < r.size;) {
    const h = r.get(p, 27);
    if (text(h, 0, 4) !== 'OggS' || h[4] !== 0) invalid('trang Ogg');
    const serial = h.readUInt32LE(14);
    const laces = r.get(p + 27, h[26]);
    const length = laces.reduce((sum, n) => sum + n, 0);
    const body = p + 27 + laces.length;
    if (body + length > r.size) invalid('trang Ogg bị cắt ngắn');
    let stream = streams.get(serial);
    if (!stream) {
      stream = { pieces: [], packetBytes: 0, identified: false, granule: null };
      streams.set(serial, stream);
    }
    // Chỉ ghép packet nhận dạng đầu tiên, kể cả khi packet trải qua nhiều trang.
    if (!stream.identified) {
      let offset = body;
      for (const n of laces) {
        stream.packetBytes += n;
        if (stream.packetBytes > 65536) invalid('packet nhận dạng Ogg quá lớn');
        stream.pieces.push(r.get(offset, n));
        offset += n;
        if (n < 255) {
          const b = Buffer.concat(stream.pieces);
          stream.identified = true;
          stream.pieces = [];
          if (b.length >= 30 && b[0] === 1 && text(b, 1, 7) === 'vorbis') {
            stream.audio = { codec: 'vorbis', channels: b[11], sampleRate: b.readUInt32LE(12) };
            stream.preSkip = 0;
          } else if (b.length >= 19 && text(b, 0, 8) === 'OpusHead') {
            // Granule Opus luôn đếm ở 48 kHz; input sample rate chỉ là gợi ý.
            stream.audio = { codec: 'opus', channels: b[9], sampleRate: 48000 };
            stream.preSkip = b.readUInt16LE(10);
          }
          if (stream.audio && !selected) selected = stream;
          break;
        }
      }
    }
    const granule = h.readBigUInt64LE(6);
    if (granule !== 0xffffffffffffffffn) stream.granule = granule;
    p = body + length;
  }
  if (!selected?.audio.sampleRate || !selected.audio.channels || selected.granule === null) invalid('Ogg thiếu nhận dạng hoặc granule');
  const samples = selected.granule - BigInt(selected.preSkip);
  if (samples < 0n || samples > BigInt(Number.MAX_SAFE_INTEGER)) invalid('granule Ogg ngoài miền');
  return { ...selected.audio, durationMs: Number(samples) / selected.audio.sampleRate * 1000 };
}

const BITRATES = {
  v1: [null, [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448],
    [0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384],
    [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320]],
  v2: [null, [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256],
    [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],
    [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160]],
};
function frame(b) {
  if (b[0] !== 255 || (b[1] & 224) !== 224) return null;
  const version = (b[1] >> 3) & 3;
  const layer = 4 - ((b[1] >> 1) & 3);
  const rateIndex = (b[2] >> 2) & 3;
  const bitrateIndex = b[2] >> 4;
  if (version === 1 || layer === 4 || rateIndex === 3 || bitrateIndex === 0 || bitrateIndex === 15) return null;
  const sampleRate = [44100, 48000, 32000][rateIndex] / (version === 3 ? 1 : version === 2 ? 2 : 4);
  const bitrate = BITRATES[version === 3 ? 'v1' : 'v2'][layer][bitrateIndex] * 1000;
  const samples = layer === 1 ? 384 : layer === 3 && version !== 3 ? 576 : 1152;
  const pad = (b[2] >> 1) & 1;
  const length = layer === 1 ? (Math.floor(12 * bitrate / sampleRate) + pad) * 4
    : Math.floor((layer === 3 && version !== 3 ? 72 : 144) * bitrate / sampleRate) + pad;
  return { version, layer, sampleRate, samples, length, channels: b[3] >> 6 === 3 ? 1 : 2, crc: !(b[1] & 1) };
}

function mp3(r) {
  let p = 0;
  if (r.size >= 10 && text(r.get(0, 3)) === 'ID3') {
    const b = r.get(0, 10);
    if ([...b.subarray(6)].some(n => n & 128)) invalid('kích thước ID3 synchsafe');
    p = 10 + b[6] * 2097152 + b[7] * 16384 + b[8] * 128 + b[9];
    if (b[3] === 4 && (b[5] & 16)) p += 10;
    if (p > r.size) invalid('ID3 bị cắt ngắn');
  }
  let first;
  // Không chấp nhận sync giả: kiểm cả header kế tiếp nếu còn một frame đầy đủ.
  for (; p + 4 <= r.size; p++) {
    const f = frame(r.get(p, 4));
    if (!f || p + f.length > r.size) continue;
    const next = p + f.length;
    if (next + 4 <= r.size && !frame(r.get(next, 4))
      && text(r.get(next, Math.min(3, r.size - next))) !== 'TAG') continue;
    first = f;
    break;
  }
  if (!first) invalid('không tìm thấy frame MPEG');
  const info = { codec: first.layer === 3 ? 'mp3' : `mp${first.layer}`, sampleRate: first.sampleRate, channels: first.channels };
  const b = r.get(p, first.length);
  const side = first.version === 3 ? (first.channels === 1 ? 17 : 32) : (first.channels === 1 ? 9 : 17);
  const x = 4 + (first.crc ? 2 : 0) + side;
  if (first.layer === 3 && x + 12 <= b.length && ['Xing', 'Info'].includes(text(b, x, x + 4))
    && (b.readUInt32BE(x + 4) & 1)) {
    const count = b.readUInt32BE(x + 8);
    if (!count) invalid('Xing có 0 frame');
    const flags = b.readUInt32BE(x + 4);
    const encoder = x + 12 + (flags & 2 ? 4 : 0) + (flags & 4 ? 100 : 0) + (flags & 8 ? 4 : 0);
    let samples = count * first.samples;
    // Xing đếm cả encoder delay/padding. LAME/Lavc lưu hai số 12-bit
    // để lấy đúng số mẫu phát ra, tương ứng duration của ffprobe hiện hành.
    if (encoder + 24 <= b.length && /^(LAME|Lavc|Lavf)/u.test(text(b, encoder, encoder + 4))) {
      const delay = b[encoder + 21] * 16 + (b[encoder + 22] >> 4);
      const padding = (b[encoder + 22] & 15) * 256 + b[encoder + 23];
      if (delay + padding > samples) invalid('LAME delay/padding ngoài miền');
      samples -= delay + padding;
    }
    return { ...info, durationMs: samples / first.sampleRate * 1000 };
  }
  if (first.layer === 3 && b.length >= 54 && text(b, 36, 40) === 'VBRI') {
    const count = b.readUInt32BE(50);
    if (!count) invalid('VBRI có 0 frame');
    return { ...info, durationMs: count * first.samples / first.sampleRate * 1000 };
  }
  let seconds = 0;
  while (p + 4 <= r.size) {
    const f = frame(r.get(p, 4));
    if (!f) break; // ID3v1/APE phía cuối không phải âm thanh.
    if (p + f.length > r.size) invalid('frame MPEG bị cắt ngắn');
    seconds += f.samples / f.sampleRate;
    p += f.length;
  }
  return { ...info, durationMs: seconds * 1000 };
}

function atoms(r, start, end) {
  const result = [];
  for (let p = start; p < end;) {
    const h = r.get(p, 8);
    let size = h.readUInt32BE(0);
    let header = 8;
    if (size === 1) {
      const wide = r.get(p + 8, 8).readBigUInt64BE();
      if (wide > BigInt(Number.MAX_SAFE_INTEGER)) invalid('atom quá lớn');
      size = Number(wide);
      header = 16;
    } else if (size === 0) size = end - p;
    if (size < header || p + size > end) invalid('atom MP4 bị cắt ngắn');
    result.push({ type: text(h, 4, 8), start: p + header, end: p + size });
    p += size;
  }
  return result;
}
function m4a(r) {
  const children = atom => atoms(r, atom.start, atom.end);
  const moov = atoms(r, 0, r.size).find(a => a.type === 'moov');
  if (!moov) invalid('M4A thiếu moov');
  const movie = children(moov);
  const mvhd = movie.find(a => a.type === 'mvhd');
  if (!mvhd) invalid('M4A thiếu mvhd');
  const version = r.get(mvhd.start, 1)[0];
  if (version > 1 || mvhd.end - mvhd.start < (version ? 32 : 20)) invalid('mvhd bị cắt ngắn');
  const b = r.get(mvhd.start, version ? 32 : 20);
  const scale = b.readUInt32BE(version ? 20 : 12);
  const ticks = version ? Number(b.readBigUInt64BE(24)) : b.readUInt32BE(16);
  if (!scale || !Number.isSafeInteger(ticks)) invalid('thời gian mvhd');
  for (const trak of movie.filter(a => a.type === 'trak')) {
    const mdia = children(trak).find(a => a.type === 'mdia');
    if (!mdia) continue;
    const media = children(mdia);
    const hdlr = media.find(a => a.type === 'hdlr');
    if (!hdlr || hdlr.end - hdlr.start < 12 || text(r.get(hdlr.start + 8, 4)) !== 'soun') continue;
    const minf = media.find(a => a.type === 'minf');
    const stbl = minf && children(minf).find(a => a.type === 'stbl');
    const stsd = stbl && children(stbl).find(a => a.type === 'stsd');
    if (!stsd || stsd.end - stsd.start < 8) continue;
    const entry = atoms(r, stsd.start + 8, stsd.end)[0];
    if (!entry || entry.end - entry.start < 28) invalid('sample entry âm thanh');
    const sample = r.get(entry.start, 28);
    const channels = sample.readUInt16BE(16);
    const sampleRate = sample.readUInt32BE(24) / 65536;
    if (!channels || !sampleRate) invalid('sample rate/kênh M4A bằng 0');
    return { codec: entry.type === 'mp4a' ? 'aac' : entry.type, sampleRate, channels, durationMs: ticks / scale * 1000 };
  }
  invalid('M4A thiếu track âm thanh');
}

/**
 * Đọc đồng bộ đường dẫn/URL file hoặc Buffer; chỉ mở file với cờ r.
 * Trả {codec, sampleRate, channels, durationMs, bytes}, làm tròn tới mili giây.
 * Codec theo tên ffprobe (pcm_s16le, pcm_f32le, vorbis, opus, mp3, aac…).
 * Ném lỗi khi định dạng không hỗ trợ hoặc đầu file hỏng; không gọi công cụ ngoài.
 * options.fs cho phép bên gọi/test bọc quyền I/O bằng cùng giao diện node:fs.
 */
export function audioHeader(input, { fs = nodeFs } = {}) {
  let fd;
  try {
    let r;
    if (Buffer.isBuffer(input)) {
      r = reader(input.length, (offset, length) => input.subarray(offset, offset + length));
    } else {
      fd = fs.openSync(input, 'r');
      const size = fs.fstatSync(fd).size;
      r = reader(size, (offset, length) => {
        const b = Buffer.allocUnsafe(length);
        let done = 0;
        while (done < length) {
          const n = fs.readSync(fd, b, done, length - done, offset + done);
          if (!n) invalid('file bị cắt ngắn trong lúc đọc');
          done += n;
        }
        return b;
      });
    }
    const magic = text(r.get(0, Math.min(12, r.size)));
    let result;
    if (/^(RIFF|RIFX)/u.test(magic)) result = wav(r);
    else if (magic.startsWith('OggS')) result = ogg(r);
    else if (['ftyp', 'moov', 'mdat', 'free', 'wide'].includes(magic.slice(4, 8))) result = m4a(r);
    else if (magic.startsWith('ID3') || (r.size >= 4 && frame(r.get(0, 4)))) result = mp3(r);
    else invalid('định dạng chưa hỗ trợ');
    if (!Number.isFinite(result.durationMs) || result.durationMs < 0) invalid('độ dài ngoài miền');
    return { ...result, durationMs: Math.round(result.durationMs), bytes: r.size };
  } finally {
    if (fd !== undefined) fs.closeSync(fd);
  }
}

export default audioHeader;
