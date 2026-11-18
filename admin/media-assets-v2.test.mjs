import assert from "node:assert/strict";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { MediaAssetError, MediaAssetStore } from "./media-assets-v2.mjs";

function sequenceUuid() {
  let value = 0;
  return () => `id-${++value}`;
}

async function withStore(run) {
  const rootDir = await mkdtemp(join(tmpdir(), "space-admin-media-v2-"));
  let tick = 0;
  const store = new MediaAssetStore({
    rootDir,
    uuid: sequenceUuid(),
    now: () => new Date(Date.UTC(2026, 9, 13, 0, 0, tick++)),
  });
  try {
    await store.initialize();
    await run({ store, rootDir });
  } finally {
    await rm(rootDir, { recursive: true, force: true });
  }
}

test("Admin upload replacement creates immutable versions and cache-safe URLs", async () => {
  await withStore(async ({ store }) => {
    const first = await store.createUploadAsset({
      kind: "image",
      title: "Vanguard Portrait",
      filename: "vanguard.png",
      mimeType: "image/png",
      buffer: Buffer.from("first-image"),
      actorId: "designer",
      tags: ["Ships", "ships"],
    });

    assert.equal(first.asset.assetId, "media.id-1");
    assert.equal(first.version.assetVersionId, "media-version.id-2");
    assert.equal(first.version.provenance, "admin-upload");
    assert.equal(first.version.components[0].storageClass, "admin-blob");
    assert.deepEqual(first.asset.tags, ["ships"]);

    const firstResolved = await store.resolveComponent(first.version.assetVersionId);
    assert.match(firstResolved.runtimeUrl, /^\/api\/admin\/space-typing\/media\/blobs\/media-version\.id-2\/primary\?v=[a-f0-9]{16}$/);
    assert.equal((await readFile(firstResolved.absolutePath)).toString("utf8"), "first-image");

    const second = await store.createUploadVersion({
      assetId: first.asset.assetId,
      filename: "vanguard-v2.png",
      mimeType: "image/png",
      buffer: Buffer.from("second-image"),
      actorId: "designer",
    });

    assert.equal(second.version.assetVersionId, "media-version.id-3");
    assert.notEqual(second.version.contentFingerprint, first.version.contentFingerprint);
    assert.equal((await store.getAsset(first.asset.assetId)).currentVersionId, second.version.assetVersionId);
    assert.equal((await store.getVersion(first.version.assetVersionId)).contentFingerprint, first.version.contentFingerprint);
    assert.equal((await store.listVersions(first.asset.assetId)).length, 2);

    const secondResolved = await store.resolveComponent(second.version.assetVersionId);
    assert.notEqual(secondResolved.runtimeUrl, firstResolved.runtimeUrl);
    assert.equal((await readFile(firstResolved.absolutePath)).toString("utf8"), "first-image", "replacement must not overwrite old bytes");
  });
});

test("references preserve historical versions and fail closed on hard delete", async () => {
  await withStore(async ({ store }) => {
    const first = await store.createUploadAsset({
      kind: "sfx",
      title: "Laser",
      filename: "laser.ogg",
      mimeType: "audio/ogg",
      buffer: Buffer.from("laser-v1"),
    });
    const second = await store.createUploadVersion({
      assetId: first.asset.assetId,
      filename: "laser-v2.ogg",
      mimeType: "audio/ogg",
      buffer: Buffer.from("laser-v2"),
    });

    const reference = await store.addReference({
      assetId: first.asset.assetId,
      assetVersionId: first.version.assetVersionId,
      domain: "content.ships",
      entityType: "ship",
      entityId: "vanguard",
      field: "shotSfxAssetVersionId",
      revisionId: "published-r1",
      actorId: "designer",
    });
    const duplicate = await store.addReference({
      assetId: first.asset.assetId,
      assetVersionId: first.version.assetVersionId,
      domain: "content.ships",
      entityType: "ship",
      entityId: "vanguard",
      field: "shotSfxAssetVersionId",
      revisionId: "published-r1",
      actorId: "designer",
    });
    assert.equal(duplicate.referenceId, reference.referenceId, "usedBy admission must be idempotent");

    await assert.rejects(
      () => store.hardDeleteVersion(first.version.assetVersionId),
      (error) => error instanceof MediaAssetError && /referenced/.test(error.message),
    );
    await assert.rejects(
      () => store.hardDeleteVersion(second.version.assetVersionId),
      (error) => error instanceof MediaAssetError && /current/.test(error.message),
    );

    await store.removeReference(reference.referenceId);
    const deleted = await store.hardDeleteVersion(first.version.assetVersionId);
    assert.equal(deleted.assetVersionId, first.version.assetVersionId);
    await assert.rejects(() => store.getVersion(first.version.assetVersionId), /Unknown asset version/);
    assert.equal((await store.getVersion(second.version.assetVersionId)).assetId, first.asset.assetId);
  });
});

test("generated multi-component bundles bootstrap idempotently without copying ownership", async () => {
  await withStore(async ({ store }) => {
    const bundle = {
      assetId: "runtime.ship-model.vanguard",
      kind: "model",
      title: "Vanguard 3D Ship",
      provenance: "generated-runtime",
      actorId: "bootstrap",
      tags: ["ship", "3d"],
      source: {
        owner: "space-typing",
        generator: "pnpm ship3d:prepare",
        sourcePath: "art-src/ships/vanguard-top-hd.png",
      },
      components: [
        { role: "color", mimeType: "image/webp", format: "webp", storageClass: "runtime-reference", runtimeUrl: "/assets/space-typing/ships/3d/vanguard/color.webp" },
        { role: "emissive", mimeType: "image/webp", format: "webp", storageClass: "runtime-reference", runtimeUrl: "/assets/space-typing/ships/3d/vanguard/emissive.webp" },
        { role: "height", mimeType: "application/octet-stream", format: "bin", storageClass: "runtime-reference", runtimeUrl: "/assets/space-typing/ships/3d/vanguard/height.bin" },
        { role: "model", mimeType: "application/json", format: "json", storageClass: "runtime-reference", runtimeUrl: "/assets/space-typing/ships/3d/vanguard/model.json" },
      ],
    };

    const first = await store.registerReferenceAsset(bundle);
    assert.equal(first.created, true);
    assert.equal(first.version.components.length, 4);
    assert.equal(first.version.provenance, "generated-runtime");

    const repeated = await store.registerReferenceAsset(bundle);
    assert.equal(repeated.created, false);
    assert.equal(repeated.version.assetVersionId, first.version.assetVersionId);
    assert.equal((await store.listVersions(bundle.assetId)).length, 1);

    const changed = await store.registerReferenceAsset({
      ...bundle,
      components: bundle.components.map((component) => component.role === "model"
        ? { ...component, runtimeUrl: "/assets/space-typing/ships/3d/vanguard/model.v2.json" }
        : component),
    });
    assert.equal(changed.created, true);
    assert.notEqual(changed.version.assetVersionId, first.version.assetVersionId);
    assert.equal((await store.listVersions(bundle.assetId)).length, 2);
    assert.equal((await store.getAsset(bundle.assetId)).currentVersionId, changed.version.assetVersionId);

    await assert.rejects(
      () => store.hardDeleteVersion(first.version.assetVersionId),
      (error) => error instanceof MediaAssetError && /Only unreferenced Admin-upload/.test(error.message),
      "generated runtime files must never become deletable just because they are indexed",
    );
  });
});

test("archive hides an asset from normal lists without breaking exact-version resolution", async () => {
  await withStore(async ({ store }) => {
    const created = await store.createUploadAsset({
      kind: "music",
      title: "Boss Theme",
      filename: "boss.ogg",
      mimeType: "audio/ogg",
      buffer: Buffer.from("boss-theme"),
    });
    await store.archiveAsset(created.asset.assetId, { actorId: "media-manager" });
    assert.equal((await store.listAssets()).length, 0);
    assert.equal((await store.listAssets({ includeArchived: true }))[0].lifecycle, "archived");
    assert.equal((await store.getVersion(created.version.assetVersionId)).assetId, created.asset.assetId);
    assert.equal((await store.resolveComponent(created.version.assetVersionId)).assetVersionId, created.version.assetVersionId);

    await store.archiveAsset(created.asset.assetId, { actorId: "media-manager", archived: false });
    assert.equal((await store.listAssets()).length, 1);
  });
});

test("reference admission rejects mismatched asset/version pairs", async () => {
  await withStore(async ({ store }) => {
    const a = await store.createUploadAsset({ kind: "image", title: "A", filename: "a.png", mimeType: "image/png", buffer: Buffer.from("a") });
    const b = await store.createUploadAsset({ kind: "image", title: "B", filename: "b.png", mimeType: "image/png", buffer: Buffer.from("b") });
    await assert.rejects(
      () => store.addReference({
        assetId: a.asset.assetId,
        assetVersionId: b.version.assetVersionId,
        domain: "shop",
        entityType: "product",
        entityId: "p1",
        field: "imageAssetVersionId",
      }),
      (error) => error instanceof MediaAssetError && /pair is invalid/.test(error.message),
    );
  });
});
