// Kiểm tra bằng chính WASM Basis đi kèm bộ mã hoá, không cần trình duyệt hay GPU.
// node inspect.mjs <file.ktx2> [--rgba <level-0.rgba>]
import { readFile, writeFile } from 'node:fs/promises';
import { parseArgs } from 'node:util';
import BASIS from './node_modules/ktx2-encoder/dist/basis/basis_encoder.js';
import { read } from 'ktx-parse';

try {
  const { values, positionals } = parseArgs({ allowPositionals: true,
    options: { rgba: { type: 'string' } } });
  if (positionals.length !== 1) throw new Error('cần một file .ktx2');
  const raw = new Uint8Array(await readFile(positionals[0]));
  const parsed = read(raw);
  const basis = await BASIS();
  basis.initializeBasis();
  const file = new basis.KTX2File(raw);
  try {
    if (!file.isValid() || !file.startTranscoding()) throw new Error('KTX2 không giải mã được');
    const width = file.getWidth(), height = file.getHeight(), levels = file.getLevels();
    if (values.rgba) {
      const rgba32 = 13; // Basis transcoder_texture_format::cTFRGBA32
      const decoded = new Uint8Array(file.getImageTranscodedSizeInBytes(0, 0, 0, rgba32));
      if (decoded.length !== width * height * 4
          || !file.transcodeImage(decoded, 0, 0, 0, rgba32, 0, -1, -1))
        throw new Error('không giải mã được RGBA mức 0');
      await writeFile(values.rgba, decoded);
    }
    console.log(JSON.stringify({ file: positionals[0], width, height, levels,
      uastc: file.isUASTC(), transfer: file.getDFDTransferFunc(),
      supercompression: parsed.supercompressionScheme, bytes: raw.length,
      levelBytes: parsed.levels.map(level => level.uncompressedByteLength) }));
  } finally {
    file.close();
    file.delete();
  }
} catch (error) {
  console.error(String(error));
  process.exitCode = 1;
}
