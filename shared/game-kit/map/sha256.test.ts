import { createHash } from "node:crypto";
import { describe, expect, it } from "vitest";
import { RngStream } from "../platform/rng";
import { hash32 } from "./hash";
import { sha256Hex } from "./sha256";

const utf8 = new TextEncoder();
const reference = (bytes: Uint8Array): string => createHash("sha256").update(bytes).digest("hex");

describe("sha256Hex", () => {
  it.each([
    ["empty", "", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"],
    ["abc", "abc", "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    ["two blocks", "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq", "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1"],
    ["million a", "a".repeat(1000000), "cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0"],
  ])("matches FIPS vector %s", (_name, input, expected) => {
    expect(sha256Hex(utf8.encode(input!))).toBe(expected);
  });

  it.each([55, 56, 57, 63, 64, 65, 119, 120, 128])("matches node:crypto at %i bytes", (length) => {
    const bytes = Uint8Array.from({ length }, (_, i) => (i * 37 + 11) & 255);
    expect(sha256Hex(bytes)).toBe(reference(bytes));
  });

  it("matches node:crypto for 200 seeded byte sequences", () => {
    for (let k = 0; k < 200; k += 1) {
      const rng = new RngStream(hash32("sha256", k));
      const bytes = Uint8Array.from({ length: rng.int(0, 1000) }, () => rng.int(0, 255));
      expect(sha256Hex(bytes), `sequence ${k}, length ${bytes.length}`).toBe(reference(bytes));
    }
    console.info("sha256 seeded sequences: 200");
  });

  it("hashes only the bytes of a subarray", () => {
    const bytes = Uint8Array.from([255, 97, 98, 99, 255]).subarray(1, 4);
    expect(sha256Hex(bytes)).toBe(reference(bytes));
  });

  it("rejects a length above the supported maximum before reading bytes", () => {
    const oversized = new Proxy(new Uint8Array(), { get: (_target, key) => key === "length" ? 0x100000000 : undefined });
    expect(() => sha256Hex(oversized)).toThrow(RangeError);
  });
});
