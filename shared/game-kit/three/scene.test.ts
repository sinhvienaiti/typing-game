// Source: new for the kit: the CPU side of the 3D helpers (hero rig, particles, helpers), no WebGL
import * as THREE from "three";
import { describe, expect, it } from "vitest";
import { HERO_CLIPS, Hero } from "./hero";
import { ParticlePool, Ribbon } from "./particles";
import { STAGE_TIERS } from "./stage";
import { approach, clamp, damp, emitCount, rand, randomUnit } from "./util";

const seeded = (seed: number) => () => ((seed = (Math.imul(seed, 48271) + 7) >>> 0) / 4294967296);

/** A small rig: a body mesh, two wing bones, a socket, and the clips a game names. */
function rig(clipNames: readonly string[]): { model: THREE.Group; clips: THREE.AnimationClip[] } {
  const model = new THREE.Group();
  const body = new THREE.Mesh(new THREE.BoxGeometry(4, 1, 2), new THREE.MeshStandardMaterial({ emissiveIntensity: 0.5 }));
  model.add(body);
  const root = new THREE.Bone();
  root.name = "root";
  for (const x of [-2, 2]) {
    const wing = new THREE.Bone();
    wing.name = x < 0 ? "wing_l" : "wing_r";
    wing.position.set(x, 0.3, 0);
    root.add(wing);
  }
  model.add(root);
  const core = new THREE.Object3D();
  core.name = "FX_CORE";
  model.add(core);
  const clips = clipNames.map((name) => new THREE.AnimationClip(name, 1, [new THREE.NumberKeyframeTrack("root.position[y]", [0, 1], [0, 0.1])]));
  return { model, clips };
}

describe("hero", () => {
  it("fits the rig, finds its sockets and wing tips, and plays the clips it has", () => {
    const { model, clips } = rig(["Idle_Hover", "Hero_Fly", "Hero_Hit", "Hero_Spit_Big", "Hero_Spit"]);
    const hero = new Hero(model, clips, { tipsPerSide: 1, trail: 8, fitSize: 2 });
    expect(hero.span).toBeCloseTo(2, 5);
    expect(hero.sockets.core?.name).toBe("FX_CORE");
    // One tip a side (turned half round to fly away from the camera, the left wing is on the right).
    expect(hero.tips.map((tip) => tip.name).sort()).toEqual(["wing_l", "wing_r"]);
    expect(hero.ribbons).toHaveLength(2);
    expect(hero.has("hit") && hero.has("spit") && !hero.has("cast")).toBe(true);
    expect(hero.play("hit")).toBeCloseTo(1, 5);
    expect(hero.play("spitBig")).toBeCloseTo(1 / 1.2, 5);
    expect(hero.play("cast")).toBe(0);
    hero.locomotion = "fly";
    for (let k = 0; k < 30; k += 1) hero.update(1 / 60, k / 60, 0);
    expect(hero.flyWeight()).toBeGreaterThan(0.5);
    hero.dispose();
  });

  it("takes a game's own clip names", () => {
    const { model, clips } = rig(["Dragon_Idle", "Dragon_Roar"]);
    expect(HERO_CLIPS.idle).toContain("Idle_Hover");
    const hero = new Hero(model, clips, { tipsPerSide: 1, trail: 4, clips: { idle: ["Dragon_Idle"], burst: ["Dragon_Roar"] } });
    expect(hero.has("burst")).toBe(true);
    expect(hero.play("burst")).toBeCloseTo(1, 5);
    hero.dispose();
  });
});

describe("particles", () => {
  it("a pool spawns, ages and frees its sprites; a full pool reuses the oldest", () => {
    const pool = new ParticlePool(4, new THREE.Texture(), true, seeded(1));
    const at = new THREE.Vector3();
    const up = new THREE.Vector3(0, 1, 0);
    for (let k = 0; k < 6; k += 1) pool.spawn(at, up, new THREE.Color("#ff8040"), 0.5, k < 3 ? 0.2 : 1);
    pool.update(0.1);
    expect(pool.count).toBe(4);
    pool.update(0.5);
    expect(pool.count).toBe(3);
    pool.clear();
    expect(pool.count).toBe(0);
    pool.dispose();
  });

  it("a ribbon follows its head", () => {
    const ribbon = new Ribbon(6, new THREE.Color("#5fe3ff"), 0.05);
    ribbon.reset(new THREE.Vector3());
    const eye = new THREE.Vector3(0, 0, 10);
    for (let k = 1; k <= 6; k += 1) ribbon.update(new THREE.Vector3(k, 0, 0), 1 / 60, 0, eye, 1);
    const position = ribbon.mesh.geometry.getAttribute("position");
    expect((position.getX(0) + position.getX(1)) / 2).toBeCloseTo(6, 5);
    ribbon.dispose();
  });
});

describe("helpers and tiers", () => {
  it("clamp, damp, approach, and draws from the source given", () => {
    expect(clamp(5, 0, 1)).toBe(1);
    expect(damp(0, 10, 1e9, 1)).toBeCloseTo(10, 6);
    expect(approach(0, 1, 0.3)).toBeCloseTo(0.3);
    expect(approach(1, 0, 2)).toBe(0);
    expect(rand(2, 4, () => 0.5)).toBe(3);
    expect(emitCount(30, 0.05, () => 0.99)).toBe(1);
    expect(emitCount(30, 0.05, () => 0)).toBe(2);
    expect(randomUnit(new THREE.Vector3(), seeded(4)).length()).toBeCloseTo(1, 6);
  });

  it("low and medium never bloom; high and ultra do", () => {
    expect([STAGE_TIERS.low.bloom, STAGE_TIERS.medium.bloom, STAGE_TIERS.high.bloom, STAGE_TIERS.ultra.bloom]).toEqual([false, false, true, true]);
    expect(STAGE_TIERS.medium.dpr).toBe(1);
  });
});
