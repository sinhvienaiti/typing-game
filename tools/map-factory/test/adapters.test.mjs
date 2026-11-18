import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdirSync, readFileSync } from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import * as td from '../adapters/typing-defense.mjs';
import * as dragon from '../adapters/dragon-hold.mjs';
import { CACHE_DIR, FIXTURE_DIR, REPO_ROOT, canonicalJson, exactCm, fixtureText, gameRepo, gameplayHash, gitStatus } from '../adapters/extract.mjs';

const TD_HASH = '7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23';
const DRAGON_HASH = 'c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a';
const CLI = path.join(REPO_ROOT, 'tools/map-factory/adapters/extract.mjs');
const run = (...args) => execFileSync(process.execPath, [CLI, ...args], {
  cwd: REPO_ROOT, maxBuffer: 64 * 1024 * 1024, stdio: ['ignore', 'pipe', 'pipe'],
});
const fixture = (game, map) => readFileSync(path.join(FIXTURE_DIR, `${game}.${map}.json`));

// Independent golden geometry from ticket 028, not derived from the fixture.
const TD_TREES = [[-2100,-4400],[-1750,-4450],[-1450,-4250],[-2000,-4050],[-1650,-3950],[-1900,-3700],[-150,-4400],[250,-4450],[600,-4400],[950,-4300],[500,-4100],[1250,-4100],[-2900,-3500],[-2850,-3050],[-2950,-2600],[-2800,-2150],[-3150,-3250],[-1950,-3100],[-2000,-2700],[-1850,-2300],[-1650,-2900],[-1950,-1900],[3300,-4300],[3700,-4400],[4100,-4200],[3500,-3900],[3900,-3750],[4300,-3800],[4250,-3350],[1500,3600],[1800,3950],[1600,4350],[2000,3500],[1950,4300],[2250,3950],[1350,3150]];
const TD_PRESET = [
  {at:[-800,1200],footprint:'S',footprintCm:200,kind:'archer'},
  {at:[700,1200],footprint:'M',footprintCm:230,kind:'cannon'},
  {at:[300,1800],footprint:'M',footprintCm:230,kind:'barracks'},
  {at:[2600,-3000],footprint:'L',footprintCm:270,kind:'gold-mine'},
  {at:[-1700,4000],footprint:'L',footprintCm:270,kind:'farm'},
];
const DRAGON_GOLDEN = {
  adapter:'dragon-hold@1', commit:'83da970eacbf85ea64da89f62a4d1b6622bc5c7b',
  dais:{at:[0,0],guideAt:[-260,200],heroHoverCm:250,radiusCm:400},
  format:'map-gameplay/0', game:'dragon-hold', hash:DRAGON_HASH,
  lanes:[
    {bridges:[{fromCm:1050,halfWidthCm:170,toCm:1840}],fords:[],halfWidthCm:150,id:'cau',points:[[850,-2900],[500,-2250],[220,-1540],[120,-1000],[40,-600]]},
    {bridges:[],fords:[{fromCm:690,toCm:1400}],halfWidthCm:130,id:'suoi',points:[[-3000,700],[-2400,420],[-1800,140],[-1200,100],[-600,40]]},
  ],
  map:'L2-cau',
  river:{bankCm:40,depthCm:120,points:[[7000,-3300],[3800,-2500],[2400,-2100],[1200,-1750],[100,-1550],[-800,-1350],[-1450,-850],[-1850,-100],[-2300,700],[-3000,1500],[-3800,2200],[-7000,4000]],shallows:[{at:[-2050,260],radiusCm:350}],widthsCm:[800,750,700,650,600,550,500,450,400,400,400,400]},
  sky:[{altitudeCm:300,id:'troi',points:[[3050,-850],[2000,-700],[730,-180]]}],
  slots:[
    {at:[660,-2548],atCm:400,id:'cau-t1',kind:'trap',lane:'cau'},
    {at:[404,-2006],atCm:1000,id:'cau-t2',kind:'trap',lane:'cau'},
    {at:[211,-1492],atCm:1550,id:'cau-t3',kind:'trap',lane:'cau'},
    {at:[95,-873],atCm:2180,id:'cau-t4',kind:'trap',lane:'cau'},
    {at:[441,-2100],atCm:900,id:'cau-b1',kind:'block',lane:'cau'},
    {at:[147,-1148],atCm:1900,id:'cau-b2',kind:'block',lane:'cau'},
    {at:[-2502,467],atCm:550,id:'suoi-t1',kind:'trap',lane:'suoi'},
    {at:[-1575,125],atCm:1550,id:'suoi-t2',kind:'trap',lane:'suoi'},
    {at:[-977,78],atCm:2150,id:'suoi-t3',kind:'trap',lane:'suoi'},
    {at:[-1525,122],atCm:1600,id:'suoi-b1',kind:'block',lane:'suoi'},
    {at:[-1026,83],atCm:2100,id:'suoi-b2',kind:'block',lane:'suoi'},
    {at:[-550,-650],id:'h-nw',kind:'house',ring:'inner'},
    {at:[650,-500],id:'h-ne',kind:'house',ring:'inner'},
    {at:[550,600],id:'h-se',kind:'house',ring:'inner'},
    {at:[-500,650],id:'h-sw',kind:'house',ring:'inner'},
    {at:[950,-1100],id:'h-e',kind:'house',ring:'outer'},
    {at:[-1400,650],id:'h-w',kind:'house',ring:'outer'},
  ],
  terrain:{kit:'pine-river',playRadiusCm:3200,reliefCm:160,seed:20261023,sizeCm:14400}, unit:'cm',
};

test('1. Typing Defense pinned gameplay and exact lane samples', async t => {
  const { extract: e, mods } = await td.extract();
  assert.equal(e.trees.length, 36);
  assert.deepEqual(e.trees, TD_TREES);
  assert.equal(e.preset.length, 5);
  assert.deepEqual(e.preset, TD_PRESET);
  assert.deepEqual(e.rules, {
    footprintCm:{S:200,M:230,L:270,XL:350}, gapCm:100, keepClearCm:1100,
    nodeSnapCm:150, rallyRadiusCm:1200, rallyRoadMaxCm:300, roadClearCm:190,
    roadHalfCm:190, snapCm:25, treeRadiusCm:150,
  });
  assert.equal(mods.TREE.radiusM, 1.5);
  assert.deepEqual([mods.BUILD.roadClearM, mods.BUILD.keepClearM, mods.BUILD.gapM], [1.9,11,1]);
  assert.deepEqual(e.water, [{x0:-2550,x1:-2250,z0:-4800,z1:4800}]);
  assert.deepEqual(e.bridges, [{x0:-2550,x1:-2250,z0:-1550,z1:-1250},{x0:-2550,x1:-2250,z0:2450,z1:2750}]);
  assert.deepEqual(e.nodes, [{at:[2600,-3000],richness:3},{at:[-1200,3200],richness:1},{at:[-3400,800],richness:2}]);
  assert.equal(e.routes.length, 2);
  assert.deepEqual(e.routes.map(r => r.points.length), [476,459]);
  assert.deepEqual(e.routes.map(r => r.lengthCm), [11880,11472]);
  const lanes = mods.groundLanes(mods.SLICE_1A.map.routes);
  let maxDeviation = 0;
  for (const [r, route] of e.routes.entries()) {
    assert.deepEqual(route.points.slice(0,3), [[-1000,-4600],[-983,-4582],[-966,-4564]]);
    assert.deepEqual(route.points.slice(-3), [[29,3959],[14,3979],[0,4000]]);
    assert.equal(route.points.length, lanes[r].xs.length);
    for (const [i, [x,z]] of route.points.entries()) {
      const dx = Math.abs(x - lanes[r].xs[i] * 100);
      const dz = Math.abs(z - lanes[r].zs[i] * 100);
      assert.ok(dx <= 1 && dz <= 1, `route ${r}, sample ${i}`);
      maxDeviation = Math.max(maxDeviation, dx, dz);
    }
  }
  assert.ok(maxDeviation <= 0.5);
  t.diagnostic(`Maximum lane deviation: ${maxDeviation} cm; trees=36, preset=5`);
  assert.deepEqual(JSON.parse(fixtureText(e)), e);
});

test('2. Dragon Hold pinned gameplay and integer conversion counts', async t => {
  const { extract: e, stats, mods } = await dragon.extract();
  assert.deepEqual(e, DRAGON_GOLDEN);
  assert.equal(fixtureText(e), fixtureText(DRAGON_GOLDEN));
  assert.deepEqual(stats, {laneValues:37,checked:132,notDivisible:0});
  assert.equal(e.slots.length, 17);
  for (const [kind, count] of [['trap',7],['block',4],['house',6]]) {
    assert.equal(e.slots.filter(s => s.kind === kind).length, count);
  }
  assert.deepEqual(mods.STAGE_M0.lanes, ['cau','suoi','troi']);
  t.diagnostic(`laneValues=${stats.laneValues}, checked=${stats.checked}, notDivisible=${stats.notDivisible}; lane slots=11, house slots=6`);
});

test('3. Golden hashes across pinned and comparison commits', async t => {
  const cases = [
    [td, td.PIN, TD_HASH, td.PIN, false],
    [td, '10ce627^', TD_HASH, '84d0ac116b396df2b341ed4330461653a05fd8b2', true],
    [dragon, dragon.PIN, DRAGON_HASH, dragon.PIN, false],
    [dragon, '3f3390d', DRAGON_HASH, '3f3390d6bddf404a2dee508c80973181bd31795f', true],
  ];
  for (const [adapter, rev, hash, commit, optional] of cases) {
    await t.test(`${adapter.GAME} ${rev}`, async st => {
      if (optional) {
        const repo = gameRepo(adapter.GAME);
        try {
          execFileSync('git', ['-C',repo,'rev-parse','--verify','--quiet','--end-of-options',`${rev}^{commit}`], {stdio:'pipe'});
        } catch (error) {
          if (typeof error.status !== 'number' || error.status === 0) throw error;
          st.skip(`${rev} is not in ${repo}`);
          return;
        }
      }
      const { extract: e } = await adapter.extract(rev);
      assert.equal(e.hash, hash);
      assert.equal(e.commit, commit);
      assert.equal(gameplayHash(e), hash);
      st.diagnostic(`${adapter.GAME} ${e.commit}: ${e.hash}`);
    });
  }
});

test('4. Changing one tree in memory changes only trees and hash', async t => {
  const { extract: original, mods } = await td.extract();
  const SLICE_1A = structuredClone(mods.SLICE_1A);
  SLICE_1A.map.trees[7][0] += 0.01;
  const changed = td.toGameplay({...mods, SLICE_1A}, original.commit);
  assert.deepEqual(original.trees[7], [250,-4450]);
  assert.deepEqual(changed.trees[7], [251,-4450]);
  assert.equal(original.hash, TD_HASH);
  assert.notEqual(changed.hash, TD_HASH);
  const { trees: originalTrees, hash: originalHash, ...originalRest } = original;
  const { trees: changedTrees, hash: changedHash, ...changedRest } = changed;
  assert.deepEqual(changedRest, originalRest);
  assert.deepEqual(changedTrees.filter((_,i) => i !== 7), originalTrees.filter((_,i) => i !== 7));
  t.diagnostic(`Tree 7: [250,-4450] -> [251,-4450]; hash=${changedHash}`);
});

test('5. Separate CLI processes produce identical bytes and fixtures', () => {
  for (const [game, map] of [[td.GAME,'w1-silverfall'],[dragon.GAME,'L2-cau']]) {
    const first = run(game);
    const second = run(game);
    assert.deepEqual(first, second);
    assert.deepEqual(first, fixture(game,map));
  }
  assert.deepEqual(run('all'), Buffer.concat([fixture(td.GAME,'w1-silverfall'),fixture(dragon.GAME,'L2-cau')]));
});

test('6. Extraction preserves game repository status', t => {
  for (const game of [td.GAME, dragon.GAME]) {
    const repo = gameRepo(game);
    let stable = false;
    for (let attempt = 1; attempt <= 3; attempt += 1) {
      const before = gitStatus(repo);
      run(game);
      const after = gitStatus(repo);
      if (before === after) {
        stable = true;
        t.diagnostic(`${game}: status unchanged on attempt ${attempt}; ${JSON.stringify(after)}`);
        break;
      }
      const lines = s => new Set(s.split('\n').filter(Boolean));
      const a = lines(before);
      const b = lines(after);
      t.diagnostic(`${game} attempt ${attempt}: removed=${JSON.stringify([...a].filter(l => !b.has(l)))}; added=${JSON.stringify([...b].filter(l => !a.has(l)))}`);
    }
    assert.ok(stable, `${game}: no stable status comparison in three attempts`);
  }
});

test('7. Empty directories cannot masquerade as game repositories', async () => {
  const emptyGames = path.join(CACHE_DIR, 'empty-games');
  mkdirSync(path.join(emptyGames, dragon.GAME), { recursive:true });
  const previous = process.env.MAP_FACTORY_GAMES_DIR;
  try {
    process.env.MAP_FACTORY_GAMES_DIR = emptyGames;
    assert.throws(() => gameRepo(dragon.GAME), /not a separate game repository/);
    await assert.rejects(dragon.extract(), /not a separate game repository/);
  } finally {
    if (previous === undefined) delete process.env.MAP_FACTORY_GAMES_DIR;
    else process.env.MAP_FACTORY_GAMES_DIR = previous;
  }
});

test('8. Canonical JSON sorts keys, normalizes zero and rejects invalid values', () => {
  assert.equal(canonicalJson({z:[true,false,null,'text'],a:{b:2,a:1}}), '{"a":{"a":1,"b":2},"z":[true,false,null,"text"]}');
  assert.equal(canonicalJson({'\uE000':1,'😀':2}), '{"😀":2,"\uE000":1}');
  assert.equal(canonicalJson(-0), '0');
  assert.equal(canonicalJson({x:-0}), '{"x":0}');
  for (const value of [1.5,NaN,undefined,Infinity,Number.MAX_SAFE_INTEGER+1,{x:undefined},[undefined]]) {
    assert.throws(() => canonicalJson(value), TypeError);
  }
  assert.equal(exactCm(2.51, 'tree'), 251);
  assert.ok(Object.is(exactCm(-0, 'zero'), 0));
  assert.throws(() => exactCm(1.001, 'bad distance'), /bad distance/);
});

test('CLI rejects invalid arguments without changing fixtures', () => {
  const files = [fixture(td.GAME,'w1-silverfall'),fixture(dragon.GAME,'L2-cau')];
  for (const args of [[],['unknown'],['all','HEAD'],['all','HEAD','--write'],
    [td.GAME,'HEAD','--write'],[dragon.GAME,'HEAD','--write'],
    [td.GAME,'HEAD','extra'],[td.GAME,'--write','--write'],[td.GAME,'--unknown']]) {
    assert.throws(() => run(...args), error => error.status === 2);
  }
  assert.deepEqual([fixture(td.GAME,'w1-silverfall'),fixture(dragon.GAME,'L2-cau')], files);
});
