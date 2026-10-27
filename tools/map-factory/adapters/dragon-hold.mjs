import '../lib/ts-hook.mjs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { extractTree, gameRepo, gameplayHash, resolveCommit } from './extract.mjs';

export const ADAPTER = 'dragon-hold@1';
export const GAME = 'dragon-hold';
export const PIN = '83da970eacbf85ea64da89f62a4d1b6622bc5c7b';

export async function load(dir) {
  const moduleAt = file => import(pathToFileURL(path.join(dir, file)).href);
  const [{ MAP_L2_CAU }, { STAGE_M0 }, { compileLanes }, { mToU, U_PER_M }] = await Promise.all([
    moduleAt('src/content/data/maps.ts'), moduleAt('src/content/data/stages.ts'),
    moduleAt('src/sim/lanes.ts'), moduleAt('src/sim/fixed.ts'),
  ]);
  return { MAP_L2_CAU, STAGE_M0, compileLanes, mToU, U_PER_M };
}

export function toGameplay({ MAP_L2_CAU: map, STAGE_M0, compileLanes, mToU, U_PER_M }, sha) {
  if (U_PER_M !== 60000) throw new Error(`Expected U_PER_M === 60000, got ${U_PER_M}`);
  const ids = [...map.lanes, ...map.sky].map(lane => lane.id);
  if (JSON.stringify(ids) !== JSON.stringify(STAGE_M0.lanes)) {
    throw new Error('Map lane IDs do not match STAGE_M0.lanes');
  }
  const stats = { laneValues: 0, checked: 0, notDivisible: 0 };
  const uToCm = (u, what) => {
    stats.checked += 1;
    if (u % 600 !== 0) {
      stats.notDivisible += 1;
      throw new Error(`${what} is not divisible by 600 u: ${u}`);
    }
    return u / 600 + 0;
  };
  const cm = (m, what) => uToCm(mToU(m), what);
  const point = (p, what) => p.map((m, i) => cm(m, `${what}[${i}]`));
  // Check both width and altitude for every runtime lane, including zero values.
  const runtime = compileLanes(map, ids).map(lane => ({
    id: lane.id, sky: lane.sky,
    points: lane.xs.map((x, i) => [uToCm(x, `${lane.id}.xs[${i}]`), uToCm(lane.zs[i], `${lane.id}.zs[${i}]`)]),
    halfWidthCm: uToCm(lane.halfWidth, `${lane.id}.halfWidth`),
    altitudeCm: uToCm(lane.altitude, `${lane.id}.altitude`),
    bridges: lane.bridges.map((b, i) => ({
      fromCm: uToCm(b.from, `${lane.id}.bridges[${i}].from`),
      toCm: uToCm(b.to, `${lane.id}.bridges[${i}].to`),
      halfWidthCm: uToCm(b.halfWidth, `${lane.id}.bridges[${i}].halfWidth`),
    })),
    fords: lane.fords.map((f, i) => ({
      fromCm: uToCm(f.from, `${lane.id}.fords[${i}].from`),
      toCm: uToCm(f.to, `${lane.id}.fords[${i}].to`),
    })),
  }));
  stats.laneValues = stats.checked;
  const extract = {
    format: 'map-gameplay/0', adapter: ADAPTER, game: GAME, map: map.id, commit: sha, unit: 'cm',
    dais: {
      at: point(map.dais.center, 'dais.center'), radiusCm: cm(map.dais.radiusM, 'dais.radiusM'),
      heroHoverCm: cm(map.dais.heroHoverM, 'dais.heroHoverM'), guideAt: point(map.dais.guideAt, 'dais.guideAt'),
    },
    lanes: runtime.filter(l => !l.sky).map(({ id, halfWidthCm, points, bridges, fords }) => ({ id, halfWidthCm, points, bridges, fords })),
    sky: runtime.filter(l => l.sky).map(({ id, altitudeCm, points }) => ({ id, altitudeCm, points })),
    slots: map.slots.map((s, i) => {
      const at = point(s.pos, `slots[${i}].pos`);
      return s.kind === 'house'
        ? { id: s.id, kind: s.kind, ring: s.ring, at }
        : { id: s.id, kind: s.kind, lane: s.lane, atCm: cm(s.atM, `slots[${i}].atM`), at };
    }),
    river: {
      points: map.river.points.map((p, i) => point(p, `river.points[${i}]`)),
      widthsCm: map.river.widthsM.map((m, i) => cm(m, `river.widthsM[${i}]`)),
      depthCm: cm(map.river.depthM, 'river.depthM'), bankCm: cm(map.river.bankM, 'river.bankM'),
      shallows: map.river.shallows.map((s, i) => ({ at: point(s.center, `shallows[${i}].center`), radiusCm: cm(s.radiusM, `shallows[${i}].radiusM`) })),
    },
    terrain: {
      seed: map.terrain.seed, sizeCm: cm(map.terrain.sizeM, 'terrain.sizeM'),
      playRadiusCm: cm(map.terrain.playRadiusM, 'terrain.playRadiusM'),
      reliefCm: cm(map.terrain.reliefM, 'terrain.reliefM'), kit: map.terrain.kit,
    },
  };
  extract.hash = gameplayHash(extract);
  return { extract, stats };
}

export async function extract(rev = PIN) {
  const repo = gameRepo(GAME);
  const sha = resolveCommit(repo, rev);
  const mods = await load(extractTree(GAME, repo, sha));
  return { ...toGameplay(mods, sha), mods };
}
