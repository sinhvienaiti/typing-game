import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { performance } from "node:perf_hooks";
import { describe, expect, it } from "vitest";
import { edtSquared } from "./edt";
import { makeMask, rasterDisc, rasterPolyline, rasterRect, type RasterGrid, type RasterPoint } from "./raster";

// These test-only field builders do not define the future L1 runtime API.
interface DragonFixture {
  hash: string;
  terrain: { sizeCm: number };
  lanes: { points: RasterPoint[]; halfWidthCm: number }[];
  river: { points: RasterPoint[]; widthsCm: number[] };
  dais: { at: RasterPoint; radiusCm: number };
  slots: { at: RasterPoint }[];
}

interface DefenseFixture {
  hash: string;
  field: { halfCm: number };
  routes: { points: RasterPoint[] }[];
  water: { x0: number; z0: number; x1: number; z1: number }[];
  keep: { at: RasterPoint };
  trees: RasterPoint[];
  preset: { at: RasterPoint; footprintCm: number }[];
  nodes: { at: RasterPoint }[];
  rules: { roadHalfCm: number; keepClearCm: number; treeRadiusCm: number; footprintCm: { L: number } };
}

const dragonName = "dragon-hold.L2-cau.json";
const defenseName = "typing-defense.w1-silverfall.json";
const dragonGrid: RasterGrid = { originX: -7200, originZ: -7200, cellCm: 50, w: 288, h: 288 };
const defenseGrid: RasterGrid = { originX: -4800, originZ: -4800, cellCm: 50, w: 192, h: 192 };
const digest = (bytes: Uint8Array): string => createHash("sha256").update(bytes).digest("hex");

function loadFixture<T extends { hash: string }>(name: string, fileSha: string, gameplayHash: string): T {
  const bytes = readFileSync(new URL(`../../../tools/map-factory/test/fixtures/gameplay/${name}`, import.meta.url));
  expect(digest(bytes), `${name}: chạy lại phiếu 028 (sha256 của file)`).toBe(fileSha);
  const fixture = JSON.parse(bytes.toString("utf8")) as T;
  expect(fixture.hash, `${name}: chạy lại phiếu 028 (hash lớp chơi)`).toBe(gameplayHash);
  return fixture;
}

const loadDragon = (): DragonFixture => loadFixture<DragonFixture>(dragonName,
  "ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37",
  "c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a");
const loadDefense = (): DefenseFixture => loadFixture<DefenseFixture>(defenseName,
  "71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428",
  "7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23");

type Field = { name: string; mask: Uint8Array; squared: Int32Array };
type Painter = readonly [string, (mask: Uint8Array) => void];

function buildFields(grid: RasterGrid, painters: readonly Painter[]): Field[] {
  return painters.map(([name, paint]) => {
    const mask = makeMask(grid);
    paint(mask);
    return { name, mask, squared: edtSquared(mask, grid.w, grid.h) };
  });
}

function dragonPainters(data: DragonFixture): Painter[] {
  const grid = dragonGrid;
  return [
    ["lanes", (mask) => {
      for (const lane of data.lanes) rasterPolyline(grid, mask, lane.points, lane.halfWidthCm);
    }],
    ["river", (mask) => {
      for (let k = 0; k < data.river.points.length - 1; k += 1) {
        rasterPolyline(grid, mask, [data.river.points[k]!, data.river.points[k + 1]!],
          Math.floor((data.river.widthsCm[k]! + data.river.widthsCm[k + 1]!) / 4));
      }
    }],
    ["dais", (mask) => rasterDisc(grid, mask, ...data.dais.at, data.dais.radiusCm)],
    ["slots", (mask) => {
      for (const slot of data.slots) rasterDisc(grid, mask, ...slot.at, 150);
    }],
  ];
}

function defensePainters(data: DefenseFixture): Painter[] {
  const grid = defenseGrid;
  return [
    ["roads", (mask) => {
      for (const route of data.routes) rasterPolyline(grid, mask, route.points, data.rules.roadHalfCm);
    }],
    ["water", (mask) => {
      for (const rect of data.water) rasterRect(grid, mask, rect.x0, rect.z0, rect.x1, rect.z1);
    }],
    ["keep", (mask) => rasterDisc(grid, mask, ...data.keep.at, data.rules.keepClearCm)],
    ["blockers", (mask) => {
      for (const at of data.trees) rasterDisc(grid, mask, ...at, data.rules.treeRadiusCm);
      for (const house of data.preset) rasterDisc(grid, mask, ...house.at, house.footprintCm);
      for (const node of data.nodes) rasterDisc(grid, mask, ...node.at, data.rules.footprintCm.L);
    }],
  ];
}

function fieldBytes(grid: RasterGrid, fields: readonly Field[]): Buffer {
  const parts = fields.map((field) => {
    const name = Buffer.from(field.name, "utf8");
    const bytes = Buffer.alloc(name.length + 9 + field.squared.length * 4);
    name.copy(bytes);
    bytes[name.length] = 0;
    bytes.writeUInt32LE(grid.w, name.length + 1);
    bytes.writeUInt32LE(grid.h, name.length + 5);
    for (let k = 0; k < field.squared.length; k += 1) bytes.writeInt32LE(field.squared[k]!, name.length + 9 + k * 4);
    return bytes;
  });
  return Buffer.concat(parts);
}

function assertFields(name: string, fields: readonly Field[], golden: readonly (readonly [string, number, number])[]): void {
  expect(fields.map((field) => field.name)).toEqual(golden.map(([field]) => field));
  for (let k = 0; k < fields.length; k += 1) {
    const field = fields[k]!;
    const count = field.mask.reduce((sum, value) => sum + Number(value === 1), 0);
    const max = field.squared.reduce((best, value) => Math.max(best, value), 0);
    console.info(`field ${name} ${field.name} mask=${count} max=${max}`);
    expect([field.name, count, max], `${name}: ${field.name}`).toEqual(golden[k]);
  }
}

describe("sample field sets from ticket 028 fixtures", () => {
  it("matches golden Dragon bytes, counts and maxima twice", () => {
    const data = loadDragon();
    expect(data.terrain.sizeCm).toBe(dragonGrid.w * dragonGrid.cellCm);
    const painters = dragonPainters(data);
    const fields = buildFields(dragonGrid, painters);
    assertFields(dragonName, fields, [
      ["lanes", 613, 43573], ["river", 3794, 38597], ["dais", 208, 38088], ["slots", 445, 33800],
    ]);
    const bytes = fieldBytes(dragonGrid, fields);
    console.info(`field-set ${dragonName} ${digest(bytes)} ${bytes.length}`);
    expect(bytes.length).toBe(1327159);
    expect(digest(bytes)).toBe("ca039deb73b5dc47e0a90ba7cd354719fed12419de77c7602a44e04cae2542b4");
    expect(fieldBytes(dragonGrid, buildFields(dragonGrid, painters)).equals(bytes)).toBe(true);
  });

  it("matches golden Defense bytes, counts and maxima twice", () => {
    const data = loadDefense();
    expect(data.field.halfCm * 2).toBe(defenseGrid.w * defenseGrid.cellCm);
    const painters = defensePainters(data);
    const fields = buildFields(defenseGrid, painters);
    assertFields(defenseName, fields, [
      ["roads", 2632, 8689], ["water", 1152, 19881], ["keep", 1402, 31705], ["blockers", 1692, 5941],
    ]);
    const bytes = fieldBytes(defenseGrid, fields);
    console.info(`field-set ${defenseName} ${digest(bytes)} ${bytes.length}`);
    expect(bytes.length).toBe(589882);
    expect(digest(bytes)).toBe("885278a7f3e1547fee5d7c0c04fde305d54cec8c4cc6cf35f6717c2090f30507");
    expect(fieldBytes(defenseGrid, buildFields(defenseGrid, painters)).equals(bytes)).toBe(true);
  });

  it("builds four Dragon fields in a median of at most 250 ms", () => {
    const painters = dragonPainters(loadDragon());
    buildFields(dragonGrid, painters);
    const times: number[] = [];
    for (let run = 0; run < 5; run += 1) {
      const start = performance.now();
      buildFields(dragonGrid, painters);
      times.push(performance.now() - start);
    }
    const median = [...times].sort((a, b) => a - b)[2]!;
    console.info(`field-timing ${dragonName} median=${median.toFixed(3)}ms samples=${times.map((n) => n.toFixed(3)).join(",")}ms`);
    // Diagnose a missed M4 target without weakening the algorithmic guard.
    if (median > 60) {
      const masks = painters.map(([, paint]) => {
        const mask = makeMask(dragonGrid);
        return { mask, paint };
      });
      const start = performance.now();
      for (const { mask, paint } of masks) paint(mask);
      const painted = performance.now();
      for (const { mask } of masks) edtSquared(mask, dragonGrid.w, dragonGrid.h);
      console.info(`field-timing breakdown raster=${(painted - start).toFixed(3)}ms edt=${(performance.now() - painted).toFixed(3)}ms`);
    }
    expect(median).toBeLessThanOrEqual(250);
  });
});
