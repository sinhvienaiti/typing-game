// RGBA đầu vào có hàng trên cùng trước; texture nén lật Y để khớp vxCell của lab.
import { readFile, writeFile } from 'node:fs/promises';
import { parseArgs } from 'node:util';
import { encodeToKTX2 } from 'ktx2-encoder';
import { read } from 'ktx-parse';

try {
  const { values: v } = parseArgs({ options: Object.fromEntries(
    ['raw', 'width', 'height', 'out', 'codec', 'transfer', 'uastc-level', 'etc1s-quality']
      .map(name => [name, { type: 'string' }])) });
  const width = Number(v.width), height = Number(v.height);
  const raw = new Uint8Array(await readFile(v.raw));
  if (!Number.isInteger(width) || !Number.isInteger(height) || width < 1 || height < 1
      || raw.length !== width * height * 4) throw new Error('kích thước RGBA không hợp lệ');
  if (!['uastc', 'etc1s'].includes(v.codec) || !['srgb', 'linear'].includes(v.transfer))
    throw new Error('codec hoặc transfer không hợp lệ');
  const isUASTC = v.codec === 'uastc', srgb = v.transfer === 'srgb';
  const started = performance.now();
  const result = await encodeToKTX2(raw, {
    isUASTC, isYFlip: true, generateMipmap: true, isKTX2File: true, enableDebug: false,
    imageDecoder: async () => ({ width, height, data: raw }),
    ...(isUASTC ? { uastcLDRQualityLevel: Number(v['uastc-level'] ?? 2), needSupercompression: true }
      : { qualityLevel: Number(v['etc1s-quality'] ?? 150), compressionLevel: 2 }),
    isSetKTX2SRGBTransferFunc: srgb, isPerceptual: srgb, ...(!srgb ? { isNormalMap: true } : {}),
  });
  await writeFile(v.out, result);
  const file = read(new Uint8Array(await readFile(v.out)));
  const dfd = file.dataFormatDescriptor[0];
  console.log(JSON.stringify({ width: file.pixelWidth, height: file.pixelHeight,
    levels: file.levels.length, supercompression: file.supercompressionScheme,
    transfer: dfd.transferFunction, colorModel: dfd.colorModel,
    bytes: result.length, encodeMs: performance.now() - started }));
} catch (error) {
  console.error(String(error));
  process.exitCode = 1;
}
