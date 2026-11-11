const encoder = new TextEncoder();

/**
 * Compute a deterministic 2-hex-digit bucket ("00".."ff") using UTF-8 FNV-1a + avalanche mix.
 * Pure JS and synchronous so scripts, Node tests, and browser bundles share the exact hash.
 */
export function indexBucketHex(id) {
  const bytes = encoder.encode(String(id ?? ""));
  let h = 0x811c9dc5;
  for (let i = 0; i < bytes.length; i++) {
    h ^= bytes[i];
    h = Math.imul(h, 0x01000193);
  }
  h ^= h >>> 16;
  h = Math.imul(h, 0x85ebca6b);
  h ^= h >>> 13;
  h = Math.imul(h, 0xc2b2ae35);
  h ^= h >>> 16;
  return (h & 0xff).toString(16).padStart(2, "0");
}
