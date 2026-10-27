import { describe, expect, it } from "vitest";
import { fmix32, fnv1a32, hash32, type HashPart } from "./hash";

describe("map hash32", () => {
  const goldens: { parts: HashPart[]; expected: number }[] = [
    { parts: [], expected: 2872998923 },
    { parts: [0], expected: 3758500711 },
    { parts: [1], expected: 2798434716 },
    { parts: [-1], expected: 3872971898 },
    { parts: [""], expected: 1404927536 },
    { parts: ["vegetation"], expected: 3618500123 },
    { parts: ["Thác Bạc"], expected: 2036913320 },
  ];
  it.each(goldens)("matches golden $parts: $expected", ({ parts, expected }) => {
    expect(hash32(...parts)).toBe(expected);
  });

  it.each([
    ["", 0x811c9dc5],
    ["a", 0xe40c292c],
    ["foobar", 0xbf9cf968],
  ] as const)("matches the public FNV-1a vector %j", (text, expected) => {
    expect(fnv1a32(new TextEncoder().encode(text))).toBe(expected);
  });

  it.each([[0, 0], [1, 0x514e28b7]])("matches fmix32(%i)", (input, expected) => {
    expect(fmix32(input!)).toBe(expected);
  });

  it("matches the encoded numeric and Vietnamese debugging vectors", () => {
    const numeric = [0x01, 0x01, 0x00, 0x00, 0x00];
    const vietnamese = [0x02, 0x0b, 0x00, 0x00, 0x00, 0x54, 0x68, 0xc3, 0xa1, 0x63, 0x20, 0x42, 0xe1, 0xba, 0xa1, 0x63];
    expect(fnv1a32(numeric)).toBe(0x1b95c75d);
    expect(fmix32(fnv1a32(numeric))).toBe(hash32(1));
    expect(fnv1a32(vietnamese)).toBe(0xc55e45d6);
    expect(fmix32(fnv1a32(vietnamese))).toBe(hash32("Thác Bạc"));
  });

  it("preserves intentional word equivalence and separates types and string boundaries", () => {
    expect(hash32(-1)).toBe(hash32(4294967295));
    expect(hash32("1")).not.toBe(hash32(1));
    expect(hash32("ab", "c")).not.toBe(hash32("a", "bc"));
    expect(hash32("Thác Bạc")).not.toBe(hash32("Thác Bạc".normalize("NFD")));
    expect(hash32(-2147483648)).toBe(hash32(2147483648));
  });

  it.each([1.5, 4294967296, -2147483649, NaN, Infinity, -Infinity])("rejects invalid number %s", (value) => {
    expect(() => hash32(value)).toThrow(RangeError);
  });

  it.each([true, null, undefined, {}, []])("rejects non-number/string part %j", (value) => {
    expect(() => hash32(value as never)).toThrow(TypeError);
  });
});
