import * as fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';

const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const valid = row => row && /^[a-f0-9]{32}$/u.test(row.md5)
  && /^[a-f0-9]{64}$/u.test(row.sha256);
const matches = (row, info) => valid(row) && row.size === info.size && row.mtimeMs === info.mtimeMs;

async function readJson(io, file) {
  try { return JSON.parse(await io.readFile(file, 'utf8')); }
  catch (error) { if (error.code === 'ENOENT') return {}; throw error; }
}

/** Cache riêng; cache media chỉ được đọc, không sao chép các mục chưa quét. */
export async function createHashCache({ repoRoot, io = fs, allowPath = () => true }) {
  const file = path.join(repoRoot, 'library/.cache/hash.json');
  const own = await readJson(io, file);
  const seed = await readJson(io, path.join(repoRoot, '.cache/media-hash.json'));
  const files = Object.create(null);
  // Giữ cache các game khác khi chạy --game, vẫn lọc danh sách cấm.
  for (const [key, row] of Object.entries(own.files ?? {})) {
    if (allowPath(key) && valid(row)) files[key] = row;
  }
  const stats = { hit: 0, seeded: 0, hashed: 0, bytesHashed: 0 };
  return {
    stats,
    async get(key, info) {
      if (!allowPath(key)) throw new Error('Đường dẫn băm không được phép');
      let row = files[key];
      let data;
      if (matches(row, info)) stats.hit++;
      else {
        const source = seed.files?.[key];
        const seeded = Array.isArray(source)
          ? { size: source[0], mtimeMs: source[1], md5: source[2], sha256: source[3] } : null;
        if (matches(seeded, info)) { row = seeded; stats.seeded++; }
        else {
          data = await io.readFile(path.join(repoRoot, key));
          row = { size: info.size, mtimeMs: info.mtimeMs,
            md5: createHash('md5').update(data).digest('hex'),
            sha256: createHash('sha256').update(data).digest('hex') };
          stats.hashed++;
          stats.bytesHashed += data.length;
        }
        files[key] = row;
      }
      return { row, data: async () => data ??= await io.readFile(path.join(repoRoot, key)) };
    },
    async save() {
      await io.mkdir(path.dirname(file), { recursive: true });
      await io.writeFile(file, JSON.stringify({ version: 1,
        files: Object.fromEntries(Object.keys(files).sort(cmp).map(key => [key, files[key]])),
      }, null, 2) + '\n');
    },
    forget(key) { delete files[key]; },
  };
}
