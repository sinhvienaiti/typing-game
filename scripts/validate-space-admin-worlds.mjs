import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const root=new URL("../",import.meta.url);
const [router,worlds,stages,server,contract,map]=await Promise.all([
  readFile(new URL("portal/src/admin/space-typing-phase-b.ts",root),"utf8"),
  readFile(new URL("portal/src/admin/space-typing-worlds-phase-b.ts",root),"utf8"),
  readFile(new URL("portal/src/admin/space-typing-stages-phase-b.ts",root),"utf8"),
  readFile(new URL("admin/server.mjs",root),"utf8"),
  readFile(new URL("portal/src/admin/contracts/space-typing-admin.v1.json",root),"utf8").then(JSON.parse),
  readFile(new URL("admin/space-typing-phase-b-map.v1.json",root),"utf8").then(JSON.parse),
]);

const screen=map.screens.find((entry)=>entry.route==="/admin/space-typing/stages");
assert.equal(screen?.persistence,"immutable-revision-store");
assert.equal(screen?.applyBoundary,"new-session");
assert.match(router,/renderPhaseBWorlds/);
assert.match(router,/\$\{BASE\}\/stages/);
assert.match(router,/\$\{BASE\}\/worlds-stages/);
assert.equal(contract.worlds.count,50);
assert.deepEqual(contract.worlds.authorableFields,["enemyRoster"]);
assert.deepEqual(contract.worlds.structuralFields,["id","galaxy","stageStart","stageEnd","enemyFamilies"]);
assert.match(worlds,/B06\.6/);
assert.match(worlds,/enemyRoster/);
assert.match(worlds,/\/api\/admin\/space-typing\/worlds\/preview/);
assert.match(worlds,/Admin Phase B · B06\.6 World roster draft/);
assert.match(worlds,/api\.createRevision/);
assert.doesNotMatch(worlds,/api\.publish/);
assert.match(worlds,/Reload this screen before saving to avoid overwriting newer published changes/);
assert.match(stages,/enemyBudget/);
assert.match(stages,/eliteChance/);
assert.match(stages,/modifierSlots/);
assert.match(server,/\/api\/runtime\/space-typing\/worlds/);
assert.match(server,/\/api\/admin\/space-typing\/worlds\/preview/);
console.log("Space Typing B06.6 Worlds + Stages UI/runtime mapping: PASS");
