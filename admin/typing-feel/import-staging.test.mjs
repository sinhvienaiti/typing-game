// node --test admin/typing-feel/import-staging.test.mjs
// The one-off seed (§3.5, §4.2 G1 note, §6.3 step 4): every published set becomes
// a Media V2 reference version that keeps its folder, and the seed's export is
// the published catalogue byte for byte. Temp folders only; the real r1 check
// runs on a copy and only reads typing-feel/public and the Audio Lab staging.
import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { cp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import { join, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { loadContract } from "../../typing-feel/tools/import-staging.mjs";
import { MediaAssetStore } from "../media-assets-v2.mjs";
import { buildCatalogue, catalogueProblems, describeConfigSets } from "./export.mjs";
import { activeConfig, addBundleSet, makeTypingFeelFixture, readCatalogue, sameSnapshot, setRow, snapshot, tempDir } from "./fixture.mjs";
import { LEGACY_NOTE, RESTORED_FAMILY_ID, SeedImportError, importTypingFeelSeed, main, setAssetId } from "./import-staging.mjs";
import { TypingFeelService } from "./service.mjs";
import { TypingFeelRevisionStore } from "./store.mjs";

const ROOT = resolve(fileURLToPath(new URL("../..", import.meta.url)));
const REAL_PUBLIC = join(ROOT, "typing-feel/public");
const REAL_STAGING = join(homedir(), "AudioLab/review/staging/keys-firefly");
const contract = loadContract();

function capture() {
  let text = "";
  return { write: (chunk) => { text += chunk; }, get text() { return text; } };
}

test("the seed registers every set as a reference version that keeps its published folder", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const state = await fx.store.getState();
  assert.equal(state.activeRevision, "seed-v1");
  const seed = await fx.store.getRevision("seed-v1");
  assert.equal(seed.author, "typing-feel-seed");
  assert.match(seed.message, /^Typing Feel seed: catalogue r1/);
  assert.deepEqual(await fx.store.getPublication("seed-v1"), { schema: "typing-feel-publication/1", revision: "seed-v1", catalogueRevision: "r1", publishedAt: "2026-10-30T18:04:19Z", builtAt: "2026-10-30T18:04:19Z" });
  const catalogue = JSON.parse(await readCatalogue(fx.publicDir));
  const { config } = seed;
  assert.equal(config.schema, "typing-feel-admin/1");
  assert.equal(config.keyboard.defaultSet, "bright-clack");
  assert.deepEqual(config.keyboard.retiredIds, []);
  assert.deepEqual(config.effects.defaults, catalogue.effects);
  assert.deepEqual(config.keyboard.families, catalogue.families);
  for (const profile of catalogue.profiles) {
    const set = config.keyboard.sets.find((entry) => entry.id === profile.id);
    assert.equal(set.name, profile.name);
    assert.equal(set.family, profile.familyId);
    assert.equal(set.status, "published");
    assert.equal(set.ownerScore, null, "no owner score is invented");
    const version = await fx.mediaStore.getVersion(set.assetVersionId);
    assert.equal(version.assetId, setAssetId(profile.id));
    assert.equal(version.provenance, "generated-runtime");
    const folder = profile.manifest.replace(/\/keys-manifest\.json$/, "");
    for (const component of version.components) {
      assert.equal(component.storageClass, "runtime-reference");
      assert.ok(component.runtimeUrl.startsWith(`/v1/keys/${folder}/`), `${profile.id}/${component.role} keeps ${folder}`);
      assert.match(component.sha256, /^[0-9a-f]{64}$/);
    }
    assert.equal(version.components.filter((component) => component.role.startsWith("key-")).length, profile.keys);
    const asset = await fx.mediaStore.getAsset(version.assetId);
    assert.ok(asset.tags.includes("typing-feel") && asset.tags.includes("keyboard-set"));
    if (profile.ownerPick) {
      assert.equal(set.note, profile.note);
      assert.equal(version.source.note, profile.note);
      assert.equal(set.labels, undefined);
    } else {
      assert.deepEqual(set.labels, ["legacy-218"]);
      assert.equal(version.source.note, LEGACY_NOTE);
      assert.ok(asset.tags.includes("legacy-218"));
    }
    const references = await fx.mediaStore.listReferences({ assetVersionId: set.assetVersionId });
    assert.deepEqual(references.map((reference) => [reference.domain, reference.entityId, reference.field, reference.revisionId]), [["typing-feel.keyboard", profile.id, "assetVersionId", "seed-v1"]]);
  }
});

test("running the seed import twice changes nothing", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const before = { data: await snapshot(fx.dataDir), shared: await snapshot(fx.sharedDir), public: await snapshot(fx.publicDir) };
  const again = await fx.runSeed();
  assert.equal(again.changed, false);
  assert.equal(again.versionsCreated, 0);
  assert.equal(again.referencesCreated, 0);
  assert.equal(again.revisionWritten, false);
  assert.ok(sameSnapshot(before.data, await snapshot(fx.dataDir)), "Media V2 registry unchanged");
  assert.ok(sameSnapshot(before.shared, await snapshot(fx.sharedDir)), "Typing Feel store unchanged");
  assert.ok(sameSnapshot(before.public, await snapshot(fx.publicDir)), "published folder unchanged");
});

test("the seed's export equals catalogue r1: catalogue, health and set manifests", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const r1 = await readCatalogue(fx.publicDir);
  const r1Health = await readFile(join(fx.publicDir, "v1/health.json"), "utf8");
  const sets = await snapshot(join(fx.publicDir, "v1/keys/sets"));

  // Export into a copy whose catalogue and health are gone.
  const copy = join(fx.base, "export-copy");
  await cp(fx.publicDir, copy, { recursive: true });
  await rm(join(copy, "v1/keys/keys-manifest.json"));
  await rm(join(copy, "v1/health.json"));
  const service = new TypingFeelService({ store: fx.store, mediaStore: fx.mediaStore, publicDir: copy });
  const result = await service.syncOnStartup();
  assert.equal(result.status, "re-exported");
  assert.deepEqual(result.folders.created, [], "seed folders are reused, never rewritten");
  assert.equal(await readCatalogue(copy), r1, "catalogue byte-identical (same revision r1 and publishedAt)");
  assert.equal(await readFile(join(copy, "v1/health.json"), "utf8"), r1Health);
  assert.ok(sameSnapshot(sets, await snapshot(join(copy, "v1/keys/sets"))), "set manifests and audio byte-identical");

  // Under any other identity the catalogue differs only in revision and publishedAt.
  const { config } = await activeConfig(fx.store);
  const { described, problems } = await describeConfigSets({ config, mediaStore: fx.mediaStore, publicDir: fx.publicDir, contract });
  assert.deepEqual(problems, []);
  const other = buildCatalogue({ config, described, catalogueRevision: "r-20261101000000-abcdef012345", publishedAt: "2026-11-01T00:00:00Z", contract });
  const strip = ({ revision, publishedAt, ...rest }) => rest;
  assert.deepEqual(strip(other.catalogue), strip(JSON.parse(r1)));
  assert.deepEqual(catalogueProblems(other.catalogue, contract), []);
});

test("restore rebuilds the store from the published catalogue alone and reuses the Media versions", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const lost = new TypingFeelRevisionStore({ rootDir: join(fx.base, "shared-lost") });
  const restored = await importTypingFeelSeed({ publicDir: fx.publicDir, restore: true, mediaStore: fx.mediaStore, store: lost });
  assert.equal(restored.revision, "restored-r1");
  assert.equal(restored.versionsCreated, 0, "same files, same fingerprints: the existing reference versions");
  assert.equal(restored.referencesCreated, 4, "references name the restored revision");
  const seed = (await fx.store.getRevision("seed-v1")).config;
  assert.deepEqual((await lost.getRevision("restored-r1")).config, seed, "the restored config equals the seed");
  assert.match((await lost.getRevision("restored-r1")).message, /never published are not recoverable/);
  const service = new TypingFeelService({ store: lost, mediaStore: fx.mediaStore, publicDir: fx.publicDir });
  assert.equal((await service.syncOnStartup()).status, "in-sync");
});

test("the seed refuses, with nothing changed, on a store that moved on or on missing files", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision, config } = await activeConfig(fx.store);
  config.keyboard.defaultSet = "deep";
  const draft = await fx.service.saveDraft({ baseRevision: revision, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: revision });
  const before = await snapshot(fx.sharedDir);
  await assert.rejects(importTypingFeelSeed({ publicDir: fx.publicDir, restore: true, mediaStore: fx.mediaStore, store: fx.store }), (error) => error instanceof SeedImportError && /only runs on an empty store/.test(error.message));
  assert.ok(sameSnapshot(before, await snapshot(fx.sharedDir)));

  const empty = await makeTypingFeelFixture(t, { seed: false });
  const catalogue = JSON.parse(await readCatalogue(empty.publicDir));
  await rm(join(empty.publicDir, "v1/keys", catalogue.profiles[1].preview));
  const registry = await readFile(join(empty.dataDir, "media-v2/registry.json"));
  await assert.rejects(empty.runSeed(), (error) => error instanceof SeedImportError && /preview\.ogg is missing \(run pnpm media:pull\)/.test(error.message));
  assert.equal(await empty.store.isInitialized(), false);
  assert.ok(registry.equals(await readFile(join(empty.dataDir, "media-v2/registry.json"))), "no Media version was registered");

  // A field outside the v1 contract, or bytes the Admin would not write again: refused before writing.
  const extra = await makeTypingFeelFixture(t, { seed: false });
  const parsed = JSON.parse(await readCatalogue(extra.publicDir));
  parsed.profiles[0].extra = true;
  await writeFile(join(extra.publicDir, "v1/keys/keys-manifest.json"), `${JSON.stringify(parsed, null, 2)}\n`);
  await assert.rejects(extra.runSeed(), (error) => error instanceof SeedImportError && /breaks the v1 contract: profiles\[0\]\.extra/.test(error.message));
  const reformatted = await makeTypingFeelFixture(t, { seed: false });
  const text = await readCatalogue(reformatted.publicDir);
  await writeFile(join(reformatted.publicDir, "v1/keys/keys-manifest.json"), `${JSON.stringify(JSON.parse(text), null, 1)}\n`);
  await assert.rejects(reformatted.runSeed(), (error) => error instanceof SeedImportError && /would differ from the published keys-manifest\.json/.test(error.message));
  for (const fixture of [extra, reformatted]) assert.equal(await fixture.store.isInitialized(), false);
});

test("a restore after a lost .local keeps every id that has a set folder: hidden rows or retired, never reusable", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  // Draft A: re-format raindrop-tile (a second folder for its id) and add a new set "fresh-pick".
  const reformatted = await addBundleSet(fx.mediaStore, { id: "raindrop-tile", name: "Raindrop Tile", salt: "-v2" });
  const fresh = await addBundleSet(fx.mediaStore, { id: "fresh-pick", name: "Fresh Pick" });
  const a = structuredClone(config);
  Object.assign(a.keyboard.sets.find((set) => set.id === "raindrop-tile"), { assetVersionId: reformatted.assetVersionId, ownerScore: 9 });
  a.keyboard.sets.push(setRow(fresh, { id: "fresh-pick", name: "Fresh Pick", family: "deep", order: 5 }));
  const draftA = await fx.service.saveDraft({ baseRevision: seed, config: a });
  await fx.service.publish({ revision: draftA.revision, expectedActiveRevision: seed });
  // Draft B: retire raindrop-tile (two folders) and deep-amber (one folder), hide fresh-pick.
  const b = structuredClone(a);
  b.keyboard.sets = b.keyboard.sets.filter((set) => set.id !== "raindrop-tile" && set.id !== "deep-amber");
  b.keyboard.retiredIds = ["deep-amber", "raindrop-tile"];
  b.keyboard.sets.find((set) => set.id === "fresh-pick").enabled = false;
  const draftB = await fx.service.saveDraft({ baseRevision: draftA.revision, config: b });
  await fx.service.publish({ revision: draftB.revision, expectedActiveRevision: draftA.revision });
  assert.deepEqual(await fx.store.reservedRetiredIds(), ["deep-amber", "raindrop-tile"]);
  const published = await readCatalogue(fx.publicDir);
  assert.deepEqual(JSON.parse(published).profiles.map((profile) => profile.id), ["deep", "bright-clack"]);

  // A stray folder too small to be a set (by hand, never by the Admin): its id is retired, not shown again.
  const stray = join(fx.publicDir, "v1/keys/sets/stray-set/abcdefabcdef");
  await mkdir(stray, { recursive: true });
  const strayManifest = { schema: "typing-feel/set-1", id: "stray-set", name: "Stray", licence: "test", recipe: "natural-v1", files: [{ file: "key-01.ogg", set: "key", durationMs: 300 }, { file: "space-01.ogg", set: "space", durationMs: 500 }], preview: "preview.ogg" };
  await writeFile(join(stray, "keys-manifest.json"), `${JSON.stringify(strayManifest, null, 2)}\n`);
  for (const name of ["key-01.ogg", "space-01.ogg", "preview.ogg"]) await writeFile(join(stray, name), `OggS ${name}`);

  // .local is lost: no Media registry, no Typing Feel store. Restore from the published folder alone.
  const dataDir = join(fx.base, "data-lost");
  const sharedDir = join(fx.base, "shared-lost");
  const out = capture();
  const err = capture();
  const code = await main(["--restore", "--public", fx.publicDir, "--data", dataDir, "--shared", sharedDir], { out, err, env: {}, root: ROOT });
  assert.equal(code, 0, err.text);
  assert.match(out.text, /kept as hidden rows in family Restored: deep-amber, fresh-pick/);
  assert.match(out.text, /retired \(the id is never used again\): raindrop-tile, because it has 2 set folders/);
  assert.match(out.text, /retired \(the id is never used again\): stray-set, because sets\/stray-set\/abcdefabcdef\/ cannot be registered: it holds 1 keys and 1 spaces, fewer than the 10 and 3/);
  const mediaStore = new MediaAssetStore({ rootDir: dataDir });
  const store = new TypingFeelRevisionStore({ rootDir: sharedDir });
  const restored = await store.getActiveRevision();
  assert.equal(restored.revision, `restored-${draftB.revision}`);
  const keyboard = restored.config.keyboard;
  assert.deepEqual(keyboard.retiredIds, ["raindrop-tile", "stray-set"]);
  assert.deepEqual(keyboard.families.at(-1), { id: RESTORED_FAMILY_ID, name: "Restored", order: 2 });
  const row = (id) => keyboard.sets.find((set) => set.id === id);
  assert.deepEqual([row("deep-amber").enabled, row("deep-amber").family, row("deep-amber").status, row("deep-amber").labels], [false, RESTORED_FAMILY_ID, "published", ["legacy-218"]], "a 218-batch set was published");
  assert.deepEqual([row("fresh-pick").enabled, row("fresh-pick").status, row("fresh-pick").name], [false, "provisional", "Fresh Pick"], "any other set's status was not recorded");
  assert.match(row("fresh-pick").note, /^Restored hidden from sets\/fresh-pick\/[0-9a-f]{12}\//);
  assert.deepEqual(await store.reservedRetiredIds(), ["raindrop-tile", "stray-set"]);
  // The hidden rows keep their own sound: the folder that was published under the id.
  const freshVersion = await mediaStore.getVersion(row("fresh-pick").assetVersionId);
  assert.ok(freshVersion.components.every((component) => component.runtimeUrl.startsWith(`/v1/keys/sets/fresh-pick/${fresh.contentFingerprint.slice(0, 12)}/`)));
  // The export of the restored revision is still the published catalogue.
  const service = new TypingFeelService({ store, mediaStore, publicDir: fx.publicDir });
  assert.equal((await service.syncOnStartup()).status, "in-sync");
  assert.equal(await readCatalogue(fx.publicDir), published);

  // No id that was used can take another sound: a new row under a retired or hidden id is refused.
  const other = await addBundleSet(mediaStore, { id: "raindrop-tile", salt: "-other" });
  for (const id of ["raindrop-tile", "deep-amber"]) {
    const reuse = structuredClone(restored.config);
    reuse.keyboard.sets.push(setRow(other, { id, family: "deep", order: 7 }));
    await assert.rejects(service.saveDraft({ baseRevision: restored.revision, config: reuse }), /retired; a retired id is never used again|is listed twice/, id);
  }
  // A hidden row can be shown again with the sound it had.
  const show = structuredClone(restored.config);
  Object.assign(show.keyboard.sets.find((set) => set.id === "deep-amber"), { enabled: true, family: "deep", order: 9 });
  const shown = await service.saveDraft({ baseRevision: restored.revision, config: show });
  assert.equal((await service.validate(shown.revision)).valid, true);
});

test("a seed rerun on a lost Media registry refuses before writing anything", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  await rm(join(fx.dataDir, "media-v2"), { recursive: true });
  const mediaStore = new MediaAssetStore({ rootDir: fx.dataDir });
  await mediaStore.initialize();
  const registry = join(fx.dataDir, "media-v2/registry.json");
  const before = { registry: await readFile(registry), shared: await snapshot(fx.sharedDir), public: await snapshot(fx.publicDir) };
  await assert.rejects(
    importTypingFeelSeed({ publicDir: fx.publicDir, stagingDir: fx.staging, mediaStore, store: fx.store }),
    (error) => error instanceof SeedImportError && /does not hold 4 of the versions seed-v1 names/.test(error.message) && /Nothing was changed/.test(error.message) && /--restore/.test(error.message),
  );
  assert.ok(before.registry.equals(await readFile(registry)), "no Media version was registered");
  assert.ok(sameSnapshot(before.shared, await snapshot(fx.sharedDir)));
  assert.ok(sameSnapshot(before.public, await snapshot(fx.publicDir)));
  // The start-up check names the same way out.
  const service = new TypingFeelService({ store: fx.store, mediaStore, publicDir: fx.publicDir });
  const startup = await service.syncOnStartup();
  assert.equal(startup.status, "error");
  assert.match(startup.problems.at(-1), /registry .* was reset or lost, move the Typing Feel store folder .* aside, run node admin\/typing-feel\/import-staging\.mjs --restore/);
});

test("the command line checks its arguments and keeps the three locations together", async (t) => {
  const fx = await makeTypingFeelFixture(t, { seed: false });
  const run = async (argv, env = {}) => {
    const out = capture();
    const err = capture();
    const code = await main(argv, { out, err, env, root: ROOT });
    return { code, out: out.text, err: err.text };
  };
  assert.equal((await run(["--restore", fx.staging, "--public", fx.publicDir])).code, 2);
  assert.equal((await run([fx.staging])).code, 2, "--public is required");
  const partial = await run([fx.staging, "--public", fx.publicDir]);
  assert.equal(partial.code, 2, "a temp public folder with the real Admin data folders is refused");
  assert.match(partial.err, /together or none of them/);
  const dirs = ["--data", fx.dataDir, "--shared", fx.sharedDir];
  const first = await run([fx.staging, "--public", fx.publicDir, ...dirs]);
  assert.equal(first.code, 0, first.err);
  assert.match(first.out, /seed-v1 \(catalogue r1\): 4 sets in 2 families, 3 legacy-218, 1 owner picks/);
  const second = await run([fx.staging, "--public", fx.publicDir, ...dirs]);
  assert.equal(second.code, 0);
  assert.match(second.out, /nothing changed/);
});

test("today's catalogue r1 (a copy) round-trips through the seed byte for byte", async (t) => {
  const catalogueFile = join(REAL_PUBLIC, "v1/keys/keys-manifest.json");
  if (!existsSync(catalogueFile)) return t.skip("typing-feel/public has no catalogue in this checkout");
  const catalogue = JSON.parse(await readFile(catalogueFile, "utf8"));
  const firstPreview = join(REAL_PUBLIC, "v1/keys", catalogue.profiles[0].preview);
  if (!existsSync(firstPreview)) return t.skip("the Typing Feel sound files are not pulled (pnpm media:pull)");
  const dir = await tempDir(t, "typing-feel-real-r1-");
  const publicDir = join(dir, "public");
  await cp(REAL_PUBLIC, publicDir, { recursive: true });
  const original = await snapshot(publicDir);
  const mediaStore = new MediaAssetStore({ rootDir: join(dir, "data") });
  await mediaStore.initialize();
  const store = new TypingFeelRevisionStore({ rootDir: join(dir, "shared") });
  const staging = existsSync(join(REAL_STAGING, "keys-manifest.json")) ? REAL_STAGING : null;
  const result = await importTypingFeelSeed({ publicDir, stagingDir: staging, restore: staging === null, mediaStore, store });
  assert.equal(result.sets, catalogue.profiles.length);
  assert.equal(result.legacy, catalogue.profiles.filter((profile) => (profile.labels ?? []).includes("legacy-218")).length);
  assert.deepEqual(result.warnings, []);
  const service = new TypingFeelService({ store, mediaStore, publicDir });
  assert.equal((await service.syncOnStartup()).status, "in-sync", "the seed's export is the catalogue on disk");
  await rm(join(publicDir, "v1/keys/keys-manifest.json"));
  await rm(join(publicDir, "v1/health.json"));
  assert.equal((await service.syncOnStartup()).status, "re-exported");
  assert.ok(sameSnapshot(original, await snapshot(publicDir)), "every file of r1 is byte-identical after the export");
});
