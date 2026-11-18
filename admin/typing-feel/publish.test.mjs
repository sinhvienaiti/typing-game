// node --test admin/typing-feel/publish.test.mjs
// Draft → Validate → Publish → Rollback of the Typing Feel store against a
// synthetic catalogue r1 in a temp folder (docs/games/TYPING_FEEL_SERVICE.md §3.12, §8.1).
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { cp, mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { loadContract } from "../../typing-feel/tools/import-staging.mjs";
import { AdminConflictError, AdminValidationError } from "../store.mjs";
import { TypingFeelExportError, catalogueProblems } from "./export.mjs";
import { activeConfig, addBundleSet, makeTypingFeelFixture, readCatalogue, sameSnapshot, setRow, snapshot } from "./fixture.mjs";
import { TypingFeelValidationError } from "./policy.mjs";

const ROOT = resolve(fileURLToPath(new URL("../..", import.meta.url)));
const KIT_AUDIO = join(ROOT, "shared/game-kit/feedback/typing-fx/audio.ts");
const READER = fileURLToPath(new URL("./kit-reader/read-catalogues.mjs", import.meta.url));
const REGISTER = fileURLToPath(new URL("./kit-reader/register.mjs", import.meta.url));
const contract = loadContract();

/** Reads exported folders with the kit's own loadKeyboardCatalog and keyboardFiles. */
function readWithKit(publicDirs) {
  const result = spawnSync(process.execPath, ["--experimental-transform-types", "--no-warnings", "--import", REGISTER, READER, KIT_AUDIO, ...publicDirs], { encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr);
  return JSON.parse(result.stdout);
}

/** Moves set `id` one step up inside its family (swaps orders with its upper neighbour). */
function moveUp(config, id) {
  const set = config.keyboard.sets.find((entry) => entry.id === id);
  const above = config.keyboard.sets.filter((entry) => entry.family === set.family && entry.order < set.order).sort((a, b) => b.order - a.order)[0];
  [set.order, above.order] = [above.order, set.order];
}

test("reorder, hide, default and effects round-trip through draft, validate and publish", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  // Fixture families: Deep (deep, deep-amber), Bright Clack (bright-clack, raindrop-tile).
  moveUp(config, "deep-amber");
  config.keyboard.sets.find((set) => set.id === "raindrop-tile").enabled = false;
  config.keyboard.defaultSet = "deep";
  config.effects.defaults = { style: "rune", intensity: "high", size: "huge", volume: 0.6 };
  const draft = await fx.service.saveDraft({ baseRevision: seed, config, message: "Owner review", author: "owner" });
  assert.deepEqual((await fx.store.getRevision(draft.revision)).config, config, "the draft keeps the config as saved");
  assert.equal((await readCatalogue(fx.publicDir)).includes('"revision": "r1"'), true, "a draft changes nothing the games read");

  const validation = await fx.service.validate(draft.revision);
  assert.equal(validation.valid, true, validation.problems.join("\n"));
  assert.equal(validation.publishable, true);
  assert.deepEqual(validation.changeScope.hidden, ["raindrop-tile"]);
  assert.deepEqual(validation.changeScope.reordered.sort(), ["deep", "deep-amber"]);
  assert.deepEqual(validation.changeScope.defaultChanged, { from: "bright-clack", to: "deep" });
  assert.deepEqual(validation.changeScope.effectsChanged.map((entry) => entry.field), ["style", "intensity", "size", "volume"]);
  assert.equal(validation.changeScope.affects, "all games");
  assert.deepEqual(validation.plan.created, [], "no set sound changed, so no folder is written");

  const result = await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  assert.equal(result.state.activeRevision, draft.revision);
  const catalogue = JSON.parse(await readCatalogue(fx.publicDir));
  assert.equal(catalogue.revision, draft.revision);
  assert.equal(catalogue.default, "deep");
  assert.deepEqual(catalogue.effects, { style: "rune", intensity: "high", size: "huge", volume: 0.6 });
  assert.deepEqual(catalogue.profiles.map((profile) => [profile.id, profile.order]), [["deep-amber", 0], ["deep", 1], ["bright-clack", 2]]);
  assert.deepEqual(catalogueProblems(catalogue, contract), []);
  const health = JSON.parse(await readFile(join(fx.publicDir, "v1/health.json"), "utf8"));
  assert.equal(health.revision, draft.revision);
  assert.match(health.build, /^data-[0-9a-f]{12}$/);

  // Show it again in a second draft: it comes back at its family place.
  const next = structuredClone(config);
  next.keyboard.sets.find((set) => set.id === "raindrop-tile").enabled = true;
  const second = await fx.service.saveDraft({ baseRevision: draft.revision, config: next });
  await fx.service.publish({ revision: second.revision, expectedActiveRevision: draft.revision });
  assert.deepEqual(JSON.parse(await readCatalogue(fx.publicDir)).profiles.map((profile) => profile.id), ["deep-amber", "deep", "bright-clack", "raindrop-tile"]);
});

test("publish with a stale expectedActiveRevision is refused and writes nothing", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.defaultSet = "deep";
  const first = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: first.revision, expectedActiveRevision: seed });
  const second = await fx.service.saveDraft({ baseRevision: first.revision, config: { ...config, effects: { defaults: { ...config.effects.defaults, style: "smash" } } } });
  const before = await snapshot(fx.publicDir);
  await assert.rejects(fx.service.publish({ revision: second.revision, expectedActiveRevision: seed }), AdminConflictError);
  // A draft based on an older revision is refused even with the right expected revision.
  const stale = await fx.service.saveDraft({ baseRevision: seed, config });
  await assert.rejects(fx.service.publish({ revision: stale.revision, expectedActiveRevision: first.revision }), AdminConflictError);
  assert.ok(sameSnapshot(before, await snapshot(fx.publicDir)), "nothing under public/ changed");
  assert.equal((await fx.store.getState()).activeRevision, first.revision);
  assert.equal(await fx.store.getPublication(second.revision), null, "no publication record is left behind");
});

test("the publication record is written only once the revision is live; a stop in between is repaired at start-up", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  // A draft that retires an id: a record for it would reserve deep-amber for ever.
  const retire = structuredClone(config);
  retire.keyboard.sets = retire.keyboard.sets.filter((set) => set.id !== "deep-amber");
  retire.keyboard.retiredIds = ["deep-amber"];
  const draft = await fx.service.saveDraft({ baseRevision: seed, config: retire });
  const publish = fx.store.publish.bind(fx.store);
  const recordAtSwitch = [];
  fx.store.publish = async (input) => {
    recordAtSwitch.push(await fx.store.getPublication(input.revision));
    throw new Error("stopped before the state switch");
  };
  await assert.rejects(fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed }), /stopped before the state switch/);
  assert.deepEqual(recordAtSwitch, [null], "no record exists before the switch");
  assert.equal(await fx.store.getPublication(draft.revision), null);
  assert.deepEqual(await fx.store.reservedRetiredIds(), [], "an id is reserved only by a revision that went live");
  assert.equal((await fx.store.getState()).activeRevision, seed);

  // A stop after the switch but before the record and the rename: start-up writes the record and exports.
  fx.store.publish = publish;
  const writePublication = fx.store.writePublication.bind(fx.store);
  fx.store.writePublication = async () => {
    throw new Error("stopped after the state switch");
  };
  const before = await readCatalogue(fx.publicDir);
  await assert.rejects(fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed }), /stopped after the state switch/);
  fx.store.writePublication = writePublication;
  assert.equal((await fx.store.getState()).activeRevision, draft.revision);
  assert.equal(await readCatalogue(fx.publicDir), before, "the games still read the old catalogue");
  assert.ok(!(await readdir(join(fx.publicDir, "v1/keys"))).some((name) => name.endsWith(".tmp")), "the temporary catalogue is removed");
  const startup = await fx.service.syncOnStartup();
  assert.equal(startup.status, "re-exported");
  assert.equal(startup.recordWritten, true);
  assert.equal(JSON.parse(await readCatalogue(fx.publicDir)).revision, draft.revision);
  assert.equal((await fx.store.getPublication(draft.revision)).catalogueRevision, draft.revision);
  assert.deepEqual(await fx.store.reservedRetiredIds(), ["deep-amber"]);
});

test("two concurrent publishes: exactly one passes", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  const a = await fx.service.saveDraft({ baseRevision: seed, config: { ...config, keyboard: { ...config.keyboard, defaultSet: "deep" } } });
  const b = await fx.service.saveDraft({ baseRevision: seed, config: { ...config, keyboard: { ...config.keyboard, defaultSet: "deep-amber" } } });
  const results = await Promise.allSettled([
    fx.service.publish({ revision: a.revision, expectedActiveRevision: seed }),
    fx.service.publish({ revision: b.revision, expectedActiveRevision: seed }),
  ]);
  assert.equal(results.filter((entry) => entry.status === "fulfilled").length, 1);
  const refused = results.find((entry) => entry.status === "rejected");
  assert.ok(refused.reason instanceof AdminConflictError, String(refused.reason));
  const winner = results[0].status === "fulfilled" ? a : b;
  const state = await fx.store.getState();
  assert.equal(state.activeRevision, winner.revision);
  assert.equal(state.generation, 2);
  assert.equal(JSON.parse(await readCatalogue(fx.publicDir)).revision, winner.revision, "the catalogue on disk is the one that passed");
});

test("rollback restores the previous catalogue and health bytes", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  const r1Catalogue = await readCatalogue(fx.publicDir);
  const r1Health = await readFile(join(fx.publicDir, "v1/health.json"), "utf8");
  config.keyboard.sets.find((set) => set.id === "deep").name = "Deep Velvet II";
  config.keyboard.defaultSet = "deep";
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  const draftCatalogue = await readCatalogue(fx.publicDir);
  assert.notEqual(draftCatalogue, r1Catalogue);

  await assert.rejects(fx.service.rollback({ targetRevision: seed, expectedActiveRevision: seed }), AdminConflictError);
  await assert.rejects(fx.service.rollback({ targetRevision: draft.revision, expectedActiveRevision: draft.revision }), AdminValidationError, "the active revision is not its own ancestor");
  const result = await fx.service.rollback({ targetRevision: seed, expectedActiveRevision: draft.revision });
  assert.equal(result.state.activeRevision, seed);
  assert.equal(await readCatalogue(fx.publicDir), r1Catalogue, "catalogue bytes are r1's again");
  assert.equal(await readFile(join(fx.publicDir, "v1/health.json"), "utf8"), r1Health, "health bytes are r1's again");

  // The rolled-back revision can be published again, with its first publish time.
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  assert.equal(await readCatalogue(fx.publicDir), draftCatalogue);
});

test("a new Admin set gets a new content-addressed folder; existing folders are never overwritten", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  const version = await addBundleSet(fx.mediaStore, { id: "hail-stone", name: "Hail Stone" });
  config.keyboard.sets.push(setRow(version, { id: "hail-stone", name: "Hail Stone", family: "deep", order: 9 }));
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  const folder = `sets/hail-stone/${version.contentFingerprint.slice(0, 12)}`;
  assert.deepEqual((await fx.service.validate(draft.revision)).plan.created, [folder]);

  // Something already sits at that URL with other bytes: an error, never a rewrite.
  const target = join(fx.publicDir, "v1/keys", folder);
  await mkdir(target, { recursive: true });
  await writeFile(join(target, "key-01.ogg"), "not the Media V2 bytes");
  const before = await readCatalogue(fx.publicDir);
  await assert.rejects(fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed }), (error) => error instanceof TypingFeelExportError && /never overwritten/.test(error.message));
  assert.equal(await readFile(join(target, "key-01.ogg"), "utf8"), "not the Media V2 bytes", "the existing file is left alone");
  assert.equal(await readCatalogue(fx.publicDir), before);
  assert.equal((await fx.store.getState()).activeRevision, seed);

  await rm(target, { recursive: true });
  const result = await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  assert.deepEqual(result.folders.created, [folder]);
  for (const component of version.components.filter((entry) => entry.role !== "report")) {
    const name = component.role === "manifest" ? "keys-manifest.json" : `${component.role}.ogg`;
    const bytes = await readFile(join(target, name));
    assert.equal(bytes.length, component.byteSize, name);
  }
  assert.ok(!existsSync(join(target, "report.ogg")) && !existsSync(join(target, "report.json")), "the report stays in the Admin");
  const catalogue = JSON.parse(await readCatalogue(fx.publicDir));
  const row = catalogue.profiles.find((profile) => profile.id === "hail-stone");
  assert.equal(row.status, "provisional");
  assert.equal(row.manifest, `${folder}/keys-manifest.json`);
  assert.deepEqual(catalogueProblems(catalogue, contract), []);

  // A seed folder whose audio was changed by hand is refused on the next publish.
  const deep = catalogue.profiles.find((profile) => profile.id === "deep");
  await writeFile(join(fx.publicDir, "v1/keys", deep.preview), "tampered");
  const next = await fx.service.saveDraft({ baseRevision: draft.revision, config: { ...config, effects: { defaults: { ...config.effects.defaults, style: "minimal" } } } });
  await assert.rejects(fx.service.publish({ revision: next.revision, expectedActiveRevision: draft.revision }), (error) => error instanceof TypingFeelExportError && /preview\.ogg differs/.test(error.message));
});

test("owner score gate, provisional default and removed ids are refused at draft time", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  const version = await addBundleSet(fx.mediaStore, { id: "pebble-rain" });
  const unscored = structuredClone(config);
  unscored.keyboard.sets.push(setRow(version, { id: "pebble-rain", family: "deep", order: 5, status: "published" }));
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: unscored }), (error) => error instanceof TypingFeelValidationError && /owner score of 9/.test(error.message));
  const scored = structuredClone(config);
  scored.keyboard.sets.push(setRow(version, { id: "pebble-rain", family: "deep", order: 5, status: "published", ownerScore: 9, note: null }));
  await fx.service.saveDraft({ baseRevision: seed, config: scored });

  const provisionalDefault = structuredClone(config);
  provisionalDefault.keyboard.sets.push(setRow(version, { id: "pebble-rain", family: "deep", order: 5 }));
  provisionalDefault.keyboard.defaultSet = "pebble-rain";
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: provisionalDefault }), /provisional set cannot be the default/);

  const hiddenDefault = structuredClone(config);
  hiddenDefault.keyboard.sets.find((set) => set.id === "bright-clack").enabled = false;
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: hiddenDefault }), /hidden; the default must be shown/);

  const dropped = structuredClone(config);
  dropped.keyboard.sets = dropped.keyboard.sets.filter((set) => set.id !== "deep-amber");
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: dropped }), /removed; hide it or retire it/);

  const archived = await addBundleSet(fx.mediaStore, { id: "old-rain" });
  await fx.mediaStore.archiveAsset(archived.assetId, { archived: true });
  const fromArchive = structuredClone(config);
  fromArchive.keyboard.sets.push(setRow(archived, { id: "old-rain", family: "deep", order: 6 }));
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: fromArchive }), /archived/);

  const untagged = await addBundleSet(fx.mediaStore, { id: "loose", tags: ["typing-feel"] });
  const wrongTags = structuredClone(config);
  wrongTags.keyboard.sets.push(setRow(untagged, { id: "loose", family: "deep", order: 7 }));
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: wrongTags }), /keyboard-set/);

  const thin = await addBundleSet(fx.mediaStore, { id: "thin", keys: 9 });
  const tooFew = structuredClone(config);
  tooFew.keyboard.sets.push(setRow(thin, { id: "thin", family: "deep", order: 8 }));
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: tooFew }), /9 keys and 3 spaces/);
});

test("a retired id is reserved forever, also after a rollback", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  const retire = structuredClone(config);
  retire.keyboard.sets = retire.keyboard.sets.filter((set) => set.id !== "deep-amber");
  retire.keyboard.retiredIds = ["deep-amber"];
  const retired = await fx.service.saveDraft({ baseRevision: seed, config: retire });
  await fx.service.publish({ revision: retired.revision, expectedActiveRevision: seed });
  assert.ok(!JSON.parse(await readCatalogue(fx.publicDir)).profiles.some((profile) => profile.id === "deep-amber"), "a retired set leaves the catalogue");
  assert.deepEqual(await fx.store.reservedRetiredIds(), ["deep-amber"]);

  const newSound = await addBundleSet(fx.mediaStore, { id: "deep-amber", salt: "-other" });
  const reuse = structuredClone(retire);
  reuse.keyboard.sets.push(setRow(newSound, { id: "deep-amber", family: "deep", order: 3 }));
  await assert.rejects(fx.service.saveDraft({ baseRevision: retired.revision, config: reuse }), /retired; a retired id is never used again/);
  const unretire = structuredClone(retire);
  unretire.keyboard.retiredIds = [];
  await assert.rejects(fx.service.saveDraft({ baseRevision: retired.revision, config: unretire }), /must stay retired/);

  // Rolling back brings the old sound back under its id; a new sound under that id stays refused.
  await fx.service.rollback({ targetRevision: seed, expectedActiveRevision: retired.revision });
  const afterRollback = structuredClone(config);
  afterRollback.keyboard.sets.find((set) => set.id === "deep-amber").assetVersionId = newSound.assetVersionId;
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: afterRollback }), /was retired in a published revision/);
  // The same old sound may stay under its id.
  await fx.service.saveDraft({ baseRevision: seed, config });
});

test("start-up re-exports a stale catalogue and re-adds missing Media references", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const r1 = await readCatalogue(fx.publicDir);
  assert.equal((await fx.service.syncOnStartup()).status, "in-sync");
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.defaultSet = "deep";
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  const published = await readCatalogue(fx.publicDir);

  // A stop between the store switch and the rename: the old catalogue is still on disk.
  await writeFile(join(fx.publicDir, "v1/keys/keys-manifest.json"), r1);
  const registry = JSON.parse(await readFile(join(fx.dataDir, "media-v2/registry.json"), "utf8"));
  const dropped = Object.values(registry.references).filter((reference) => reference.revisionId === draft.revision);
  for (const reference of dropped) delete registry.references[reference.referenceId];
  await writeFile(join(fx.dataDir, "media-v2/registry.json"), `${JSON.stringify(registry, null, 2)}\n`);

  const result = await fx.service.syncOnStartup();
  assert.equal(result.status, "re-exported");
  assert.equal(result.previousCatalogueRevision, "r1");
  assert.equal(result.referencesCreated, dropped.length);
  assert.equal(await readCatalogue(fx.publicDir), published);
  const again = await fx.service.syncOnStartup();
  assert.equal(again.status, "in-sync");
  assert.equal(again.referencesCreated, 0);
});

test("every exported revision passes the contract and loads in the kit's own reader", async (t) => {
  if (!existsSync(KIT_AUDIO)) return t.skip("shared/game-kit is not in this checkout");
  const fx = await makeTypingFeelFixture(t);
  const copies = [];
  const keep = async (name) => {
    const copy = join(fx.base, `export-${name}`);
    await cp(fx.publicDir, copy, { recursive: true });
    copies.push(copy);
    assert.deepEqual(catalogueProblems(JSON.parse(await readCatalogue(copy)), contract), [], name);
  };
  await keep("seed");
  const { revision: seed, config } = await activeConfig(fx.store);
  const version = await addBundleSet(fx.mediaStore, { id: "hail-stone", name: "Hail Stone", keys: 12, spaces: 4 });
  moveUp(config, "raindrop-tile");
  config.keyboard.sets.find((set) => set.id === "deep").enabled = false;
  config.keyboard.sets.push(setRow(version, { id: "hail-stone", name: "Hail Stone", family: "bright-clack", order: 2, status: "published", ownerScore: 9.5, note: null }));
  config.keyboard.defaultSet = "hail-stone";
  config.effects.defaults.volume = 0.5;
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  await keep("draft");
  await fx.service.rollback({ targetRevision: seed, expectedActiveRevision: draft.revision });
  await keep("rollback");

  const [first, second, third] = readWithKit(copies);
  for (const read of [first, second, third]) {
    assert.equal(read.state, "ready");
    assert.equal(read.options[0], "off");
    for (const set of read.sets) {
      assert.ok(set.keys >= 10 && set.spaces >= 3, `${set.id} has its files`);
      assert.match(set.firstKey, /^https:\/\/feel\.test\/v1\/keys\/sets\/[a-z0-9-]+\/[0-9a-f]{12}\/key-01\.ogg$/);
    }
  }
  assert.equal(first.revision, "r1");
  assert.equal(first.defaultId, "bright-clack");
  assert.deepEqual(first.options, ["off", "deep", "deep-amber", "bright-clack", "raindrop-tile"]);
  assert.equal(second.revision, draft.revision);
  assert.equal(second.defaultId, "hail-stone");
  assert.equal(second.effects.volume, 0.5);
  assert.deepEqual(second.options, ["off", "deep-amber", "raindrop-tile", "bright-clack", "hail-stone"]);
  assert.deepEqual(second.sets.find((set) => set.id === "hail-stone").keys, 12);
  assert.deepEqual(third, { ...first, publicDir: third.publicDir });
});

test("Accept stores a bundle through the queue; Publish references the set and its source WAV; archiving later breaks nothing", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const wav = await fx.mediaStore.createUploadAsset({ kind: "audio", title: "raindrop.wav", filename: "raindrop.wav", mimeType: "audio/wav", buffer: Buffer.from("RIFF fake wav"), tags: ["typing-feel", "keyboard-source"] });
  const template = await addBundleSet(fx.mediaStore, { id: "tile-rain" });
  const components = [];
  for (const component of template.components) {
    const bytes = await readFile(join(fx.dataDir, "media-v2", component.storageKey));
    components.push({ role: component.role, filename: component.role === "manifest" || component.role === "report" ? `${component.role}.json` : `${component.role}.ogg`, mimeType: component.mimeType, buffer: bytes, durationSeconds: component.durationSeconds });
  }
  const accepted = await fx.service.acceptSetBundle({ title: "Tile Rain", components, source: { generator: "typing-feel natural-v1 (test)", sourcePath: wav.version.assetVersionId, license: "Adobe Firefly" } });
  assert.deepEqual((await fx.mediaStore.getAsset(accepted.asset.assetId)).tags, ["keyboard-set", "typing-feel"]);
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets.push(setRow(accepted.version, { id: "tile-rain", family: "deep", order: 4 }));
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  const sourceReferences = await fx.mediaStore.listReferences({ assetVersionId: wav.version.assetVersionId });
  assert.deepEqual(sourceReferences.map((reference) => [reference.domain, reference.entityId, reference.field, reference.revisionId]), [["typing-feel.source", "tile-rain", "sourceAssetVersionId", draft.revision]]);
  await assert.rejects(fx.mediaStore.hardDeleteVersion(wav.version.assetVersionId), /referenced/);

  // Archiving the set's asset in the Media Library afterwards does not break start-up or a rollback back to it.
  await fx.mediaStore.archiveAsset(accepted.asset.assetId, { archived: true });
  assert.equal((await fx.service.syncOnStartup()).status, "in-sync");
  await fx.service.rollback({ targetRevision: seed, expectedActiveRevision: draft.revision });
  // Publishing it again adds the set anew: an archived asset is refused until it is restored.
  await assert.rejects(fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed }), /is archived; restore it before using it/);
  await fx.mediaStore.archiveAsset(accepted.asset.assetId, { archived: false });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  assert.ok(JSON.parse(await readCatalogue(fx.publicDir)).profiles.some((profile) => profile.id === "tile-rain"));
});

test("start-up removes only the leftovers an interrupted export of its own wrote", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const keys = join(fx.publicDir, "v1/keys");
  const leftovers = [
    join(keys, "keys-manifest.json.4242.0f8fad5b-d9cb-469f-a165-70867728950e.tmp"),
    join(fx.publicDir, "v1/health.json.4242.7c9e6679-7425-40de-944b-e07fc1f90ae7.tmp"),
  ];
  for (const file of leftovers) await writeFile(file, "{}");
  await mkdir(join(keys, "sets/deep/.incoming-0123456789ab-4242-1a2b3c4d"), { recursive: true });
  const foreign = [join(keys, "keys-manifest.json.4242.tmp"), join(keys, "notes.txt")];
  for (const file of foreign) await writeFile(file, "keep");
  await mkdir(join(keys, "sets/deep/.incoming-0123456789ab-4242"), { recursive: true });

  const result = await fx.service.syncOnStartup();
  assert.equal(result.status, "in-sync");
  assert.deepEqual(result.leftovers.sort(), ["v1/health.json.4242.7c9e6679-7425-40de-944b-e07fc1f90ae7.tmp", "v1/keys/keys-manifest.json.4242.0f8fad5b-d9cb-469f-a165-70867728950e.tmp", "v1/keys/sets/deep/.incoming-0123456789ab-4242-1a2b3c4d"]);
  for (const file of leftovers) assert.equal(existsSync(file), false);
  for (const file of foreign) assert.equal(existsSync(file), true, "files another tool wrote are left alone");
  assert.equal(existsSync(join(keys, "sets/deep/.incoming-0123456789ab-4242")), true, "a feel:import folder is not ours");
});
