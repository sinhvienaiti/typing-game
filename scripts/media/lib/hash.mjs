// md5 (the lock and Drive's server-side hash) plus sha256 (the ?v= of runtime
// manifests) in one read. Cached in .cache/media-hash.json by size + mtime.
import { createHash } from 'node:crypto';
import { createReadStream, existsSync, readFileSync } from 'node:fs';
import { writeFileAtomic } from './lock.mjs';

export function hashFile(file) {
  return new Promise((resolve, reject) => {
    const md5 = createHash('md5');
    const sha256 = createHash('sha256');
    const stream = createReadStream(file);
    stream.on('data', (chunk) => { md5.update(chunk); sha256.update(chunk); });
    stream.on('error', reject);
    stream.on('end', () => resolve({ md5: md5.digest('hex'), sha256: sha256.digest('hex') }));
  });
}

export class HashCache {
  constructor(file) {
    this.file = file;
    this.files = Object.create(null);
    this.dirty = false;
    if (file && existsSync(file)) {
      try {
        const data = JSON.parse(readFileSync(file, 'utf8'));
        if (data?.version === 1 && data.files && typeof data.files === 'object') {
          this.files = Object.assign(Object.create(null), data.files);
        }
      } catch {
        // A broken cache only costs a re-hash.
      }
    }
  }

  get(key, size, mtimeMs) {
    const hit = this.files[key];
    if (!hit || hit[0] !== size || hit[1] !== mtimeMs) return null;
    return { md5: hit[2], sha256: hit[3] };
  }

  set(key, size, mtimeMs, hashes) {
    this.files[key] = [size, mtimeMs, hashes.md5, hashes.sha256];
    this.dirty = true;
  }

  save() {
    if (!this.file || !this.dirty) return;
    writeFileAtomic(this.file, `${JSON.stringify({ version: 1, files: this.files })}\n`);
    this.dirty = false;
  }
}

/**
 * Fills entry.md5 / entry.sha256 for entries { key, abs, size, mtimeMs }.
 * Entries without a cache key (restores outside the repo) are hashed every time.
 */
export async function hashEntries(entries, cache, { concurrency = 4, onSlow } = {}) {
  const todo = [];
  for (const entry of entries) {
    if (entry.md5) continue;
    const hit = entry.cacheKey && cache ? cache.get(entry.cacheKey, entry.size, entry.mtimeMs) : null;
    if (hit) Object.assign(entry, hit);
    else todo.push(entry);
  }
  if (!todo.length) return 0;
  const bytes = todo.reduce((sum, entry) => sum + entry.size, 0);
  if (onSlow && bytes > 200e6) onSlow(todo.length, bytes);
  let next = 0;
  const worker = async () => {
    while (next < todo.length) {
      const entry = todo[next];
      next += 1;
      const hashes = await hashFile(entry.abs);
      Object.assign(entry, hashes);
      if (entry.cacheKey && cache) cache.set(entry.cacheKey, entry.size, entry.mtimeMs, hashes);
    }
  };
  await Promise.all(Array.from({ length: Math.min(concurrency, todo.length) }, worker));
  cache?.save();
  return todo.length;
}
