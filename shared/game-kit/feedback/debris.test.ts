// Source: new for the kit: the shards' life by profile (Sinh Tồn S0 checked them in the browser only)
import * as THREE from "three";
import { describe, expect, it } from "vitest";
import { Debris } from "./debris";
import { DRAGON, SHIP } from "./profiles";

const seeded = (seed: number) => () => ((seed = (Math.imul(seed, 48271) + 7) >>> 0) / 4294967296);
const run = (debris: Debris, seconds: number) => {
  for (let k = 0; k < Math.round(seconds * 60); k += 1) debris.update(1 / 60);
};

describe("debris", () => {
  it("throws shards along the blow; they settle on the floor and lie there the profile's rest time, then fade", () => {
    const a = new THREE.Color("#ff8040");
    const b = new THREE.Color("#ffd0a0");
    const dragon = new Debris(32, { profile: DRAGON, random: seeded(3) });
    dragon.burst(0, 1, 0, 1, 0, 6, 4, a, b);
    expect(dragon.live).toBe(6);
    run(dragon, 2);
    const at = new THREE.Vector3();
    for (let i = 0; i < 6; i += 1) {
      dragon.position(i, at);
      expect(at.y).toBeCloseTo(0.04, 3);
      expect(at.x).toBeGreaterThan(0);
    }
    run(dragon, 3.9);
    expect(dragon.live).toBe(6);
    run(dragon, 0.9);
    expect(dragon.live).toBe(0);
    expect(dragon.mesh.count).toBe(0);
    // Ship shards lie 8 s.
    const ship = new Debris(32, { profile: SHIP, random: seeded(3) });
    ship.burst(0, 1, 0, 1, 0, 6, 4, a, b);
    run(ship, 6.8);
    expect(ship.live).toBe(6);
    run(ship, 2);
    expect(ship.live).toBe(0);
  });

  it("a full pool makes room with its oldest shard; a seeded burst lands the same way twice", () => {
    const color = new THREE.Color("#ffffff");
    const pool = new Debris(4, { random: seeded(9) });
    pool.burst(0, 1, 0, 0, 1, 6, 3, color, color);
    expect(pool.live).toBe(4);
    const twin = new Debris(4, { random: seeded(9) });
    twin.burst(0, 1, 0, 0, 1, 6, 3, color, color);
    run(pool, 1);
    run(twin, 1);
    const p = new THREE.Vector3();
    const q = new THREE.Vector3();
    for (let i = 0; i < 4; i += 1) expect(pool.position(i, p).equals(twin.position(i, q))).toBe(true);
    pool.dispose();
    twin.dispose();
  });
});
