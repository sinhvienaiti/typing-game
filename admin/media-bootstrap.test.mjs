import assert from "node:assert/strict";
import { mkdir, mkdtemp, readFile, readdir, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { bootstrapMediaReferences } from "./media-bootstrap.mjs";
import { MediaAssetStore } from "./media-assets-v2.mjs";

function sequenceUuid() {
  let value = 0;
  return () => `bootstrap-${++value}`;
}

async function writeFixture(path, value) {
  await mkdir(join(path, ".."), { recursive: true });
  await writeFile(path, value);
}

async function createFixture() {
  const root = await mkdtemp(join(tmpdir(), "space-admin-media-bootstrap-"));
  const adminRoot = join(root, "admin-data");
  const childRoot = join(root, "space-typing");

  await writeFixture(join(childRoot, "src/audio/world-music-catalog.json"), JSON.stringify({
    schemaVersion: 1,
    tracks: [
      {
        id: "aurora-serenade",
        title: "Aurora Serenade",
        playback: {
          kind: "stems",
          calm: [{ src: "/assets/audio/music/songs/aurora-serenade/calm.ogg?v=1111111111111111" }],
          intense: [{ src: "/assets/audio/music/songs/aurora-serenade/intense.ogg?v=2222222222222222" }],
        },
        metadata: { mood: "calm" },
      },
      {
        id: "legacy-upload",
        title: "Legacy Upload",
        playback: { kind: "file", src: "/assets/audio/music/uploads/legacy-upload.ogg?v=3333333333333333" },
        metadata: { provenance: "local-admin-upload" },
      },
    ],
  }));

  await writeFixture(join(childRoot, "public/assets/space-typing/ships/3d/manifest.json"), JSON.stringify({ ships: ["vanguard"] }));
  await writeFixture(join(childRoot, "public/assets/space-typing/ships/3d/vanguard/color.webp"), Buffer.from("ship-color-v1"));
  await writeFixture(join(childRoot, "public/assets/space-typing/ships/3d/vanguard/emissive.webp"), Buffer.from("ship-emissive-v1"));
  await writeFixture(join(childRoot, "public/assets/space-typing/ships/3d/vanguard/height.bin"), Buffer.from("ship-height-v1"));
  await writeFixture(join(childRoot, "public/assets/space-typing/ships/3d/vanguard/model.json"), JSON.stringify({ version: 1 }));

  await writeFixture(join(childRoot, "public/assets/audio/sfx/combat/laser.ogg"), Buffer.from("laser-sfx"));
  await writeFixture(join(childRoot, "public/assets/audio/sfx/ui/click.wav"), Buffer.from("click-sfx"));
  await writeFixture(join(childRoot, "public/assets/audio/sfx/README.txt"), "not an audio asset");

  const store = new MediaAssetStore({
    rootDir: adminRoot,
    uuid: sequenceUuid(),
    now: () => new Date("2026-10-13T00:00:00.000Z"),
  });
  await store.initialize();
  return { root, adminRoot, childRoot, store };
}

test("runtime Music, ship bundles and SFX bootstrap as reference-only assets idempotently", async () => {
  const fixture = await createFixture();
  try {
    const first = await bootstrapMediaReferences({ store: fixture.store, childRoot: fixture.childRoot });
    assert.deepEqual(first.music, { created: 2, reused: 0, skipped: 0 });
    assert.deepEqual(first.shipModels, { created: 1, reused: 0, skipped: 0 });
    assert.deepEqual(first.sfx, { created: 2, reused: 0, skipped: 1 });
    assert.deepEqual(first.totals, { created: 5, reused: 0, skipped: 1 });

    const assets = await fixture.store.listAssets({ includeArchived: true });
    assert.equal(assets.length, 5);
    assert.equal((await readdir(join(fixture.adminRoot, "media-v2/blobs"))).length, 0, "reference bootstrap must not copy runtime binaries into Admin blob storage");

    const builtInMusic = await fixture.store.getAsset("runtime.music.aurora-serenade");
    const builtInVersion = await fixture.store.getVersion(builtInMusic.currentVersionId);
    assert.equal(builtInVersion.provenance, "code-owned");
    assert.deepEqual(builtInVersion.components.map((component) => component.role), ["calm-1", "intense-1"]);
    assert.equal(builtInVersion.components[0].storageClass, "runtime-reference");

    const legacyMusic = await fixture.store.getAsset("runtime.music.legacy-upload");
    const legacyVersion = await fixture.store.getVersion(legacyMusic.currentVersionId);
    assert.equal(legacyVersion.provenance, "external-reference", "legacy local-admin-upload bytes must not be misrepresented as Media V2 admin blobs");
    assert.equal(legacyVersion.source.owner, "legacy-music-admin");

    const ship = await fixture.store.getAsset("runtime.ship-model.vanguard");
    const shipVersion = await fixture.store.getVersion(ship.currentVersionId);
    assert.equal(shipVersion.provenance, "generated-runtime");
    assert.deepEqual(shipVersion.components.map((component) => component.role), ["color", "emissive", "height", "model"]);
    for (const component of shipVersion.components) {
      assert.match(component.sha256, /^[a-f0-9]{64}$/);
      assert.ok(component.byteSize > 0);
      assert.equal(component.storageClass, "runtime-reference");
    }

    const second = await bootstrapMediaReferences({ store: fixture.store, childRoot: fixture.childRoot });
    assert.deepEqual(second.totals, { created: 0, reused: 5, skipped: 1 });
    assert.equal((await fixture.store.listVersions("runtime.ship-model.vanguard")).length, 1);
  } finally {
    await rm(fixture.root, { recursive: true, force: true });
  }
});

test("generated ship bundle byte changes create a new immutable reference version", async () => {
  const fixture = await createFixture();
  try {
    await bootstrapMediaReferences({ store: fixture.store, childRoot: fixture.childRoot });
    const before = await fixture.store.getAsset("runtime.ship-model.vanguard");

    await writeFile(join(fixture.childRoot, "public/assets/space-typing/ships/3d/vanguard/model.json"), JSON.stringify({ version: 2 }));
    const changed = await bootstrapMediaReferences({ store: fixture.store, childRoot: fixture.childRoot });

    assert.deepEqual(changed.music, { created: 0, reused: 2, skipped: 0 });
    assert.deepEqual(changed.shipModels, { created: 1, reused: 0, skipped: 0 });
    assert.deepEqual(changed.sfx, { created: 0, reused: 2, skipped: 1 });
    const versions = await fixture.store.listVersions("runtime.ship-model.vanguard");
    assert.equal(versions.length, 2);
    assert.notEqual((await fixture.store.getAsset("runtime.ship-model.vanguard")).currentVersionId, before.currentVersionId);
    assert.notEqual(versions[0].contentFingerprint, versions[1].contentFingerprint);
    assert.equal((await readdir(join(fixture.adminRoot, "media-v2/blobs"))).length, 0);
  } finally {
    await rm(fixture.root, { recursive: true, force: true });
  }
});

test("incomplete generated ship bundles are skipped rather than fabricated", async () => {
  const fixture = await createFixture();
  try {
    await writeFile(join(fixture.childRoot, "public/assets/space-typing/ships/3d/manifest.json"), JSON.stringify({ ships: ["missing-ship"] }));
    const result = await bootstrapMediaReferences({ store: fixture.store, childRoot: fixture.childRoot });
    assert.deepEqual(result.shipModels, { created: 0, reused: 0, skipped: 1 });
    await assert.rejects(() => fixture.store.getAsset("runtime.ship-model.missing-ship"), /Unknown asset/);
  } finally {
    await rm(fixture.root, { recursive: true, force: true });
  }
});

test("pinned Space Typing runtime tree bootstraps without binary copies or duplicate versions", async () => {
  const adminRoot = await mkdtemp(join(tmpdir(), "space-admin-media-runtime-smoke-"));
  const childRoot = fileURLToPath(new URL("../games/space-typing/", import.meta.url));
  const store = new MediaAssetStore({
    rootDir: adminRoot,
    uuid: sequenceUuid(),
    now: () => new Date("2026-10-13T00:00:00.000Z"),
  });
  try {
    await store.initialize();
    const shipManifest = JSON.parse(await readFile(join(childRoot, "public/assets/space-typing/ships/3d/manifest.json"), "utf8"));
    const first = await bootstrapMediaReferences({ store, childRoot, actorId: "ci-runtime-bootstrap" });

    assert.ok(first.music.created > 0, "Pinned child Music catalog must yield reference assets.");
    assert.equal(first.shipModels.created, shipManifest.ships.length, "Every pinned ship3D manifest entry must have a complete generated bundle.");
    assert.ok(first.sfx.created > 0, "Pinned child SFX tree must yield code-owned reference assets.");
    assert.equal((await readdir(join(adminRoot, "media-v2/blobs"))).length, 0, "Runtime smoke bootstrap must remain metadata/reference-only.");

    const assets = await store.listAssets({ includeArchived: true });
    assert.equal(assets.length, first.totals.created, "Every created bootstrap admission must remain present in the registry.");

    const second = await bootstrapMediaReferences({ store, childRoot, actorId: "ci-runtime-bootstrap" });
    assert.equal(second.totals.created, 0, "Second bootstrap over unchanged pinned child must not create versions.");
    assert.equal(second.totals.reused, first.totals.created, "Second bootstrap must reuse every previously created runtime asset version.");
    assert.equal((await store.listAssets({ includeArchived: true })).length, assets.length);
  } finally {
    await rm(adminRoot, { recursive: true, force: true });
  }
});
