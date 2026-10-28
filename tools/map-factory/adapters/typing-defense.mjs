import '../lib/ts-hook.mjs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { exactCm, extractTree, gameRepo, gameplayHash, resolveCommit } from './extract.mjs';

export const ADAPTER = 'typing-defense@1';
export const GAME = 'typing-defense';
export const PIN = '10ce627ff4e1c91f29e808cb658c086f51bd97d6';

export async function load(dir) {
  const moduleAt = file => import(pathToFileURL(path.join(dir, file)).href);
  const [{ SLICE_1A }, { BUILD, TREE, RALLY }, { groundLanes }] = await Promise.all([
    moduleAt('src/content/slice-1a.ts'),
    moduleAt('src/content/rules.ts'),
    moduleAt('src/sim/lanes.ts'),
  ]);
  return { SLICE_1A, BUILD, TREE, RALLY, groundLanes };
}

export function toGameplay({ SLICE_1A, BUILD, TREE, RALLY, groundLanes }, sha) {
  const map = SLICE_1A.map;
  const point = (p, what) => p.map((m, i) => exactCm(m, `${what}[${i}]`));
  const points = (ps, what) => ps.map((p, i) => point(p, `${what}[${i}]`));
  const rects = (rs, what) => rs.map((r, i) => Object.fromEntries(
    ['x0', 'x1', 'z0', 'z1'].map(k => [k, exactCm(r[k], `${what}[${i}].${k}`)]),
  ));
  const footprintCm = Object.fromEntries(Object.entries(BUILD.footprintR).map(
    ([size, m]) => [size, exactCm(m, `BUILD.footprintR.${size}`)],
  ));
  const footprint = kind => {
    const building = SLICE_1A.buildings.find(b => b.id === kind);
    if (!building || !Object.hasOwn(footprintCm, building.footprint)) {
      throw new Error(`Missing building footprint: ${kind}`);
    }
    return building.footprint;
  };
  const extract = {
    format: 'map-gameplay/0', adapter: ADAPTER, game: GAME,
    map: SLICE_1A.id, contentMapId: map.id, commit: sha, unit: 'cm',
    field: { halfCm: exactCm(map.halfM, 'halfM'), buildHalfCm: exactCm(map.buildHalfM, 'buildHalfM') },
    rules: {
      roadHalfCm: exactCm(map.roadHalfM, 'roadHalfM'),
      roadClearCm: exactCm(BUILD.roadClearM, 'BUILD.roadClearM'),
      keepClearCm: exactCm(BUILD.keepClearM, 'BUILD.keepClearM'),
      gapCm: exactCm(BUILD.gapM, 'BUILD.gapM'),
      snapCm: exactCm(BUILD.snapM, 'BUILD.snapM'),
      nodeSnapCm: exactCm(BUILD.nodeSnapM, 'BUILD.nodeSnapM'),
      treeRadiusCm: exactCm(TREE.radiusM, 'TREE.radiusM'), footprintCm,
      rallyRadiusCm: exactCm(RALLY.radiusM, 'RALLY.radiusM'),
      rallyRoadMaxCm: exactCm(RALLY.roadMaxM, 'RALLY.roadMaxM'),
    },
    gate: point(map.gate, 'gate'),
    keep: { at: point(map.keep, 'keep'), footprintCm: footprintCm[footprint('keep')] },
    routeKnots: map.routes.map((route, i) => points(route, `routes[${i}]`)),
    routes: groundLanes(map.routes).map(lane => ({
      lengthCm: Math.round(lane.length * 100) + 0,
      points: Array.from(lane.xs, (x, i) => [Math.round(x * 100) + 0, Math.round(lane.zs[i] * 100) + 0]),
    })),
    fly: { points: points(map.flyRoute, 'flyRoute'), heightCm: exactCm(map.flyHeightM, 'flyHeightM') },
    water: rects(map.water, 'water'), bridges: rects(map.bridges, 'bridges'),
    nodes: map.nodes.map((n, i) => ({ at: point([n.x, n.z], `nodes[${i}]`), richness: n.richness })),
    trees: points(map.trees, 'trees'),
    preset: map.preset.map(([kind, x, z], i) => {
      const size = footprint(kind);
      return { kind, at: point([x, z], `preset[${i}]`), footprint: size, footprintCm: footprintCm[size] };
    }),
  };
  extract.hash = gameplayHash(extract);
  return extract;
}

export async function extract(rev = PIN) {
  const repo = gameRepo(GAME);
  const sha = resolveCommit(repo, rev);
  const mods = await load(extractTree(GAME, repo, sha));
  return { extract: toGameplay(mods, sha), mods };
}
