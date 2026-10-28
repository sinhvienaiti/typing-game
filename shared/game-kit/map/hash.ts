export type HashPart = number | string;

const encoder = new TextEncoder();
const FNV_OFFSET = 0x811c9dc5;
const FNV_PRIME = 0x01000193;

/** Plain FNV-1a over bytes, without the MurmurHash3 finaliser. */
export function fnv1a32(bytes: ArrayLike<number>): number {
  let h = FNV_OFFSET;
  for (let index = 0; index < bytes.length; index += 1) {
    h = Math.imul(h ^ bytes[index]!, FNV_PRIME);
  }
  return h >>> 0;
}

/** MurmurHash3 finaliser, returning an unsigned 32-bit word. */
export function fmix32(h: number): number {
  h ^= h >>> 16;
  h = Math.imul(h, 0x85ebca6b);
  h ^= h >>> 13;
  h = Math.imul(h, 0xc2b2ae35);
  h ^= h >>> 16;
  return h >>> 0;
}

/**
 * Hash typed, length-delimited parts as UTF-8 and little-endian 32-bit words.
 * Signed and unsigned forms of the same word intentionally hash alike:
 * hash32(-1) === hash32(4294967295). Type tags distinguish "1" from 1;
 * string lengths distinguish ("ab", "c") from ("a", "bc").
 * Strings retain their original Unicode form, without normalisation.
 */
export function hash32(...parts: readonly HashPart[]): number {
  let h = FNV_OFFSET;
  const byte = (value: number): void => {
    h = Math.imul(h ^ value, FNV_PRIME);
  };
  const word = (value: number): void => {
    byte(value & 0xff);
    byte((value >>> 8) & 0xff);
    byte((value >>> 16) & 0xff);
    byte(value >>> 24);
  };

  for (const part of parts) {
    if (typeof part === "number") {
      if (!Number.isInteger(part) || part < -2147483648 || part > 4294967295) {
        throw new RangeError("Hash numbers must be integers in [-2147483648, 4294967295]");
      }
      byte(0x01);
      word(part >>> 0);
    } else if (typeof part === "string") {
      const bytes = encoder.encode(part);
      byte(0x02);
      word(bytes.length);
      for (const value of bytes) byte(value);
    } else {
      throw new TypeError("Hash parts must be numbers or strings");
    }
  }
  return fmix32(h);
}
