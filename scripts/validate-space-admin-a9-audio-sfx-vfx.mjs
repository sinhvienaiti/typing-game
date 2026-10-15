import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
// A9 ownership re-audit: b75cec6..dcba99b changes only the bounded Test Lab
// direct-launch bootstrap, registry wiring and focused unit coverage.
// Audio/SFX/VFX ownership, contracts, production sample/music sources and write
// boundaries asserted below are unchanged.
const A9_SFX_AUDITED_CHILD_SHA = "dcba99b60523f671076bda497f126824ad01797c";

const [
  sfxContract,
  childCatalog,
  sampleBank,
  childPackageSource,
  page,
  router,
  command,
  phaseMapSource,
  musicPage,
  musicModel,
  vfxWrapper,
  vfxLegacy,
] = await Promise.all([
  readFile(resolve(childRoot, "contracts/space-typing-admin-sfx.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "src/audio/admin-sfx-catalog.ts"), "utf8"),
  readFile(resolve(childRoot, "src/audio/sample-bank.ts"), "utf8"),
  readFile(resolve(childRoot, "package.json"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-sfx-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-command.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-music-library-phase-b.ts"), "utf8"),
  readFile(resolve(childRoot, "src/audio/world-music-model.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-vfx-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-vfx-phase-b-legacy.ts"), "utf8"),
]);
const childPackage = JSON.parse(childPackageSource);
const phaseMap = JSON.parse(phaseMapSource);
const vfxPage = `${vfxWrapper}\n${vfxLegacy}`;
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, A9_SFX_AUDITED_CHILD_SHA, `A9 SFX audit is stale: audited=${A9_SFX_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Audio/SFX/VFX before changing this SHA.`);
assert.equal(sfxContract.contractRevision, "space-typing-admin-sfx-v1");
assert.equal(sfxContract.capability, "sfx.read");
assert.equal(sfxContract.route.path, "/admin/space-typing/sfx");
assert.equal(sfxContract.sfx.mode, "runtime-backed-readonly");
assert.equal(sfxContract.sfx.runtimeOwner, "SampleSfxBank + SAMPLE_SFX");
assert.equal(sfxContract.sfx.eventBinding, "SampleSfxId");
assert.equal(sfxContract.sfx.writeCapability, false);
assert.equal(sfxContract.sfx.adminPreviewWriteCapability, false);
assert.equal(sfxContract.sfx.previewCapability, true);
assert.equal(sfxContract.sfx.previewMutation, false);
assert.equal(sfxContract.sfx.applyBoundary, "none");
assert.deepEqual(sfxContract.sfx.authorableFields, []);
for (const fakeField of ["cooldown", "priority", "enabled", "gain override", "source override"]) {
  assert.ok(sfxContract.sfx.unsupportedAdminMockFields.includes(fakeField), `SFX fake-field boundary missing: ${fakeField}`);
}

assert.match(sampleBank, /export const SAMPLE_SFX/);
assert.match(sampleBank, /export type SampleSfxId/);
assert.match(childCatalog, /createAdminSfxCatalog/);
assert.match(childCatalog, /Object\.keys\(SAMPLE_SFX\)/);
assert.match(childCatalog, /eventBinding:\s*id/);
assert.match(childCatalog, /authorable:\s*false/);
assert.match(childCatalog, /mutation:\s*false/);
assert.equal(childPackage.scripts?.["sfx:audit"], "node --import tsx scripts/audit-admin-sfx.ts");
assert.equal(childPackage.scripts?.["sfx:admin-preview"], "tsx scripts/admin/sfx-runtime-preview.ts");

assert.match(page, /createAdminSfxCatalog/);
assert.match(page, /\.\.\/\.\.\/\.\.\/games\/space-typing\/src\/audio\/admin-sfx-catalog/);
assert.match(page, /RUNTIME-BACKED · READ ONLY/);
assert.match(page, /TEST PLAYBACK/);
assert.match(page, /NO FAKE SFX POLICY/);
assert.match(page, /Runtime Gain/);
assert.match(page, /Pool/);
assert.match(page, /entry\.eventBinding/);
assert.match(page, /new Audio\(productionSampleUrl/);
assert.match(page, /source\.startsWith\("\/assets\/audio\/"\)/);
assert.match(page, /\/games\.json/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|method:\s*["'](?:POST|PUT|PATCH|DELETE)["']/);

assert.match(router, /renderPhaseBSfx/);
assert.match(router, /\$\{BASE\}\/sfx`\) return decorated\(path, renderPhaseBSfx\(\)\)/);
assert.match(router, /attachProductionPreviewClassification\(screen, path\)/);
assert.match(router, /attachRoleAwareActionGates\(screen\)/);
assert.match(command, /\["SFX",\s*`\$\{BASE\}\/sfx`,\s*"Media"\]/);

const sfxMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/sfx");
assert.ok(sfxMap, "A9 SFX Phase B map row is required");
assert.equal(sfxMap.domain, "audio.sfx");
assert.equal(sfxMap.persistence, "child-code-owned-sample-bank");
assert.equal(sfxMap.applyBoundary, "none");
assert.equal(sfxMap.status, "phase-b-ui-wired-runtime-backed-readonly-preview");

// A9 Music: catalog source/duration/loop are visible and Test Playback uses the
// exact production asset. Context and Enabled are owned by World Music policy,
// so Music Library must not invent duplicate authoring controls for them.
assert.match(musicModel, /export type CatalogTrack/);
assert.match(musicModel, /loop:\s*boolean/);
assert.match(musicModel, /disabledTrackIds\?: readonly string\[\]/);
assert.match(musicModel, /stages\?: Readonly<Record<string, WorldMusicPolicyEntry>>/);
assert.match(musicModel, /worlds\?: Readonly<Record<string, WorldMusicPolicyEntry>>/);
assert.match(musicModel, /galaxies\?: Readonly<Record<string, WorldMusicPolicyEntry>>/);
assert.match(musicPage, /Music Library/);
assert.match(musicPage, /\/api\/admin\/space-typing\/music\/library/);
assert.match(musicPage, /TEST PLAYBACK/);
assert.match(musicPage, /<th>Source<\/th>/);
assert.match(musicPage, /<th>Duration<\/th>/);
assert.match(musicPage, /<th>Loop<\/th>/);
assert.match(musicPage, /\/games\.json/);
assert.match(musicPage, /source\.startsWith\("\/assets\/audio\/music\/"\)/);
assert.match(musicPage, /new Audio\(productionMusicUrl/);
assert.match(musicPage, /audio\.loop = track\.loop === true/);
assert.match(musicPage, /Context assignments and enabled\/disabled policy remain under World \/ Stage Music/);
assert.doesNotMatch(musicPage, /trimGain[^\n]*(?:Volume|volume)/);
assert.doesNotMatch(musicPage, /createRevision|\/publish|\/revisions/);

assert.match(vfxPage, /space-typing-vfx-phase-b-legacy/);
assert.match(vfxPage, /createCombatVfxProductionPreviewPanel/);
assert.match(vfxPage, /RUNTIME-BACKED · READ ONLY/);
assert.match(vfxPage, /NO FAKE VFX PROFILE/);
assert.doesNotMatch(vfxPage, /createRevision|\/publish|\/revisions/);

console.log(`Space Typing Admin A9 Audio/SFX/VFX boundary: PASS (${childHead.slice(0, 12)} · Music + SFX production asset Test Playback; VFX production preview wrapper retains code-owned read-only tuning boundary).`);
