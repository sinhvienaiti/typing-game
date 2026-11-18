// node --test admin/media-write-lock.test.mjs
// The Media V2 registry write lock is process-wide (every MediaAssetStore on the
// same folder shares it) and re-entrant; bundle versions are immutable
// multi-component Admin uploads (docs/games/TYPING_FEEL_SERVICE.md §3.6).
import assert from "node:assert/strict";
import { spawn, spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { mkdtemp, readFile, readdir, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { MediaAssetError, MediaAssetStore, acquireRegistryFileLock } from "./media-assets-v2.mjs";

const MEDIA_MODULE = fileURLToPath(new URL("./media-assets-v2.mjs", import.meta.url));

async function folder(t) {
  const rootDir = await mkdtemp(join(tmpdir(), "media-write-lock-"));
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  return rootDir;
}

const bundle = (id, salt = "") => [
  { role: "manifest", filename: "keys-manifest.json", mimeType: "application/json", buffer: Buffer.from(`{"id":"${id}"}\n`) },
  { role: "preview", filename: "preview.ogg", mimeType: "audio/ogg", buffer: Buffer.from(`preview ${id}${salt}`) },
  { role: "key-01", filename: "key-01.ogg", mimeType: "audio/ogg", buffer: Buffer.from(`key ${id}${salt}`), durationSeconds: 0.45 },
  { role: "space-01", filename: "space-01.ogg", mimeType: "audio/ogg", buffer: Buffer.from(`space ${id}${salt}`), durationSeconds: 0.535 },
];

test("two stores on one folder share the write lock: concurrent admissions are never lost", async (t) => {
  const rootDir = await folder(t);
  const upload = new MediaAssetStore({ rootDir });
  const typingFeel = new MediaAssetStore({ rootDir });
  await upload.initialize();
  const reference = await typingFeel.registerReferenceAsset({
    assetId: "typing-feel.keyboard-set.deep", kind: "audio", title: "Deep Velvet", provenance: "generated-runtime",
    tags: ["typing-feel", "keyboard-set"],
    components: [{ role: "preview", mimeType: "audio/ogg", storageClass: "runtime-reference", runtimeUrl: "/v1/keys/sets/deep/1ebcd392567a/preview.ogg" }],
  });
  const work = [];
  for (let index = 0; index < 8; index += 1) {
    work.push(upload.createUploadAsset({ kind: "audio", title: `Upload ${index}`, filename: `take-${index}.wav`, mimeType: "audio/wav", buffer: Buffer.from(`wav ${index}`) }));
    work.push(typingFeel.addReference({ assetId: reference.asset.assetId, assetVersionId: reference.version.assetVersionId, domain: "typing-feel.keyboard", entityType: "keyboard-set", entityId: "deep", field: "assetVersionId", revisionId: `r-${index}` }));
    work.push(typingFeel.createUploadBundleAsset({ kind: "audio", title: `Bundle ${index}`, tags: ["typing-feel", "keyboard-set"], components: bundle(`set-${index}`) }));
  }
  await Promise.all(work);
  const registry = JSON.parse(await readFile(join(rootDir, "media-v2/registry.json"), "utf8"));
  assert.equal(Object.keys(registry.assets).length, 17);
  assert.equal(Object.keys(registry.versions).length, 17);
  assert.equal(Object.keys(registry.references).length, 8);
});

test("the lock is re-entrant: grouped writes inside withWriteLock do not deadlock", async (t) => {
  const store = new MediaAssetStore({ rootDir: await folder(t) });
  await store.initialize();
  const order = [];
  const outer = store.withWriteLock(async () => {
    const created = await store.createUploadBundleAsset({ kind: "audio", title: "Grouped", components: bundle("grouped") });
    order.push("bundle");
    await store.addReferences([{ assetId: created.asset.assetId, assetVersionId: created.version.assetVersionId, domain: "d", entityType: "e", entityId: "x", field: "f" }]);
    order.push("references");
    return created;
  });
  const waiting = store.createUploadAsset({ kind: "audio", title: "After", filename: "after.wav", mimeType: "audio/wav", buffer: Buffer.from("after") }).then(() => order.push("after"));
  await Promise.all([outer, waiting]);
  assert.deepEqual(order, ["bundle", "references", "after"], "a write from outside waits for the whole group");
});

test("a bundle version is immutable, content-addressed and fingerprinted over every component", async (t) => {
  const rootDir = await folder(t);
  const store = new MediaAssetStore({ rootDir });
  await store.initialize();
  const source = { generator: "typing-feel natural-v1 (test)", sourcePath: "media-version.wav-source", license: "Adobe Firefly", note: "{\"amount\":0.6}" };
  const first = await store.createUploadBundleAsset({ kind: "audio", title: "Raindrop Tile", tags: ["typing-feel", "keyboard-set"], components: bundle("raindrop"), source });
  assert.equal(first.version.provenance, "admin-upload");
  assert.deepEqual(first.version.components.map((component) => component.role), ["key-01", "manifest", "preview", "space-01"]);
  assert.equal(first.version.source.owner, "admin-media-v2");
  assert.equal(first.version.source.note, source.note);
  for (const component of first.version.components) {
    assert.equal(component.storageClass, "admin-blob");
    assert.ok(existsSync(join(rootDir, "media-v2", component.storageKey)));
  }
  assert.equal(first.version.components.find((component) => component.role === "key-01").durationSeconds, 0.45);
  assert.equal(first.version.components.find((component) => component.role === "manifest").format, "json");

  const same = await store.createUploadBundleVersion({ assetId: first.asset.assetId, components: bundle("raindrop"), source });
  assert.notEqual(same.version.assetVersionId, first.version.assetVersionId, "every Accept is its own version");
  assert.equal(same.version.contentFingerprint, first.version.contentFingerprint, "same bytes and source, same fingerprint (same fp12 folder)");
  const other = await store.createUploadBundleVersion({ assetId: first.asset.assetId, components: bundle("raindrop", "-v2"), source });
  assert.notEqual(other.version.contentFingerprint, first.version.contentFingerprint);
  assert.equal((await store.getAsset(first.asset.assetId)).currentVersionId, other.version.assetVersionId);
  assert.deepEqual((await store.getVersion(first.version.assetVersionId)).components, first.version.components, "older versions are untouched");

  const blobs = (await readdir(join(rootDir, "media-v2/blobs"))).length;
  const registry = await readFile(join(rootDir, "media-v2/registry.json"));
  await assert.rejects(store.createUploadBundleVersion({ assetId: first.asset.assetId, components: [...bundle("raindrop", "-x"), bundle("raindrop")[0]] }), (error) => error instanceof MediaAssetError && /Duplicate component role: manifest/.test(error.message));
  await assert.rejects(store.createUploadBundleVersion({ assetId: first.asset.assetId, components: [{ role: "Bad Role", mimeType: "audio/ogg", buffer: Buffer.from("x") }] }), /Invalid component role/);
  await assert.rejects(store.createUploadBundleVersion({ assetId: first.asset.assetId, components: [] }), /must not be empty/);
  await assert.rejects(store.createUploadBundleAsset({ kind: "audio", title: "Empty", components: [{ role: "preview", mimeType: "audio/ogg", buffer: Buffer.alloc(0) }] }), /must contain bytes/);
  assert.equal((await readdir(join(rootDir, "media-v2/blobs"))).length, blobs, "a refused bundle writes no blob");
  assert.ok(registry.equals(await readFile(join(rootDir, "media-v2/registry.json"))), "a refused bundle leaves the registry as it was");
});

test("addReferences admits a batch with one write and is idempotent", async (t) => {
  const rootDir = await folder(t);
  const store = new MediaAssetStore({ rootDir });
  await store.initialize();
  const created = await store.createUploadBundleAsset({ kind: "audio", title: "Set", components: bundle("set") });
  const inputs = ["a", "b", "c"].map((entityId) => ({ assetId: created.asset.assetId, assetVersionId: created.version.assetVersionId, domain: "typing-feel.keyboard", entityType: "keyboard-set", entityId, field: "assetVersionId", revisionId: "r1" }));
  const first = await store.addReferences(inputs, { actorId: "owner" });
  assert.equal(first.created, 3);
  assert.ok(first.references.every((reference) => reference.createdBy === "owner"));
  const before = await readFile(join(rootDir, "media-v2/registry.json"));
  const again = await store.addReferences(inputs);
  assert.equal(again.created, 0);
  assert.deepEqual(again.references.map((reference) => reference.referenceId), first.references.map((reference) => reference.referenceId));
  assert.ok(before.equals(await readFile(join(rootDir, "media-v2/registry.json"))), "nothing new, nothing written");
  await assert.rejects(store.addReferences([{ ...inputs[0], assetVersionId: "media-version.unknown" }]), /pair is invalid/);
  await assert.rejects(store.hardDeleteVersion(created.version.assetVersionId), /is referenced and cannot be hard-deleted/);
});

test("two processes on one registry (the Admin service and the import command) never lose a write", { timeout: 60000 }, async (t) => {
  const rootDir = await folder(t);
  const store = new MediaAssetStore({ rootDir });
  await store.initialize();
  const count = 60;
  // Both processes start writing at the same moment: the child loads, says ready, waits for go.
  const script = `
    const { MediaAssetStore } = await import(${JSON.stringify(MEDIA_MODULE)});
    const store = new MediaAssetStore({ rootDir: ${JSON.stringify(rootDir)} });
    process.stdout.write("ready\\n");
    await new Promise((resolve) => process.stdin.once("data", resolve));
    for (let index = 0; index < ${count}; index += 1) await store.createUploadAsset({ kind: "audio", title: "Child " + index, filename: "c" + index + ".wav", mimeType: "audio/wav", buffer: Buffer.from("child " + index) });
    process.exit(0);
  `;
  const child = spawn(process.execPath, ["--input-type=module", "-e", script], { stdio: ["pipe", "pipe", "pipe"] });
  let stderr = "";
  child.stderr.on("data", (chunk) => { stderr += chunk; });
  const exited = new Promise((done) => child.on("exit", done));
  await new Promise((resolve) => child.stdout.once("data", resolve));
  child.stdin.write("go\n");
  for (let index = 0; index < count; index += 1) await store.createUploadAsset({ kind: "audio", title: `Parent ${index}`, filename: `p${index}.wav`, mimeType: "audio/wav", buffer: Buffer.from(`parent ${index}`) });
  assert.equal(await exited, 0, stderr);
  const titles = (await store.listAssets()).map((asset) => asset.title);
  assert.equal(titles.length, 2 * count, "every admission of both processes is in registry.json");
  assert.ok(!existsSync(`${store.registryPath}.lock`), "the lock file is gone once both are done");
});

test("the registry lock waits for a live holder and breaks one left by a process that is gone", { timeout: 30000 }, async (t) => {
  const rootDir = await folder(t);
  const store = new MediaAssetStore({ rootDir });
  await store.initialize();
  const lockPath = `${store.registryPath}.lock`;

  // A holder that is gone (its pid no longer runs): broken at once.
  const gone = spawnSync(process.execPath, ["-e", ""]).pid;
  await writeFile(lockPath, JSON.stringify({ pid: gone, at: new Date().toISOString() }));
  await store.createUploadAsset({ kind: "audio", title: "After a dead holder", filename: "a.wav", mimeType: "audio/wav", buffer: Buffer.from("a") });
  assert.ok(!existsSync(lockPath));

  // A live holder (another process): the write waits until it lets go.
  const holder = spawn(process.execPath, ["-e", "setTimeout(() => {}, 20000)"], { stdio: "ignore" });
  t.after(() => holder.kill());
  await writeFile(lockPath, JSON.stringify({ pid: holder.pid, at: new Date().toISOString() }));
  let done = false;
  const waiting = store.createUploadAsset({ kind: "audio", title: "After a live holder", filename: "b.wav", mimeType: "audio/wav", buffer: Buffer.from("b") }).then(() => { done = true; });
  await new Promise((resolve) => setTimeout(resolve, 200));
  assert.equal(done, false, "the write waits while the holder runs");
  await rm(lockPath);
  await waiting;
  assert.equal((await store.listAssets()).length, 2);

  // A live holder that never lets go: a clear error after the wait, and the registry is untouched.
  await writeFile(lockPath, JSON.stringify({ pid: holder.pid, at: new Date().toISOString() }));
  await assert.rejects(acquireRegistryFileLock(store.registryPath, { waitMs: 100 }), (error) => error instanceof MediaAssetError && /Media registry is busy: process \d+ holds/.test(error.message));
  await rm(lockPath);
});
