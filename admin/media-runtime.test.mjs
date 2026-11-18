import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { MediaAssetStore } from "./media-assets-v2.mjs";
import {
  MEDIA_RUNTIME_BASE,
  MediaRuntimeError,
  resolveExactRuntimeMediaVersion,
} from "./media-runtime.mjs";

async function withStore(run) {
  const rootDir = await mkdtemp(join(tmpdir(), "space-typing-media-runtime-"));
  const store = new MediaAssetStore({ rootDir });
  await store.initialize();
  try {
    await run(store);
  } finally {
    await rm(rootDir, { recursive: true, force: true });
  }
}

test("runtime media resolution pins the requested immutable version even after current advances", async () => {
  await withStore(async (store) => {
    const first = await store.createUploadAsset({
      kind: "image",
      title: "Vanguard Hull",
      filename: "vanguard-a.webp",
      mimeType: "image/webp",
      buffer: Buffer.from("version-a"),
    });
    const second = await store.createUploadVersion({
      assetId: first.asset.assetId,
      filename: "vanguard-b.webp",
      mimeType: "image/webp",
      buffer: Buffer.from("version-b"),
      makeCurrent: true,
    });

    const resolvedA = await resolveExactRuntimeMediaVersion(store, first.version.assetVersionId);
    const resolvedB = await resolveExactRuntimeMediaVersion(store, second.version.assetVersionId);
    const currentAsset = await store.getAsset(first.asset.assetId);

    assert.equal(currentAsset.currentVersionId, second.version.assetVersionId);
    assert.equal(resolvedA.assetVersionId, first.version.assetVersionId);
    assert.notEqual(resolvedA.assetVersionId, resolvedB.assetVersionId);
    assert.match(
      resolvedA.components[0].runtimeUrl,
      new RegExp(`^${MEDIA_RUNTIME_BASE.replaceAll("/", "\\/")}\\/blobs\\/`),
    );
    assert.notEqual(resolvedA.components[0].runtimeUrl, resolvedB.components[0].runtimeUrl);
  });
});

test("runtime media resolution exposes generated same-origin runtime references without raw source paths", async () => {
  await withStore(async (store) => {
    const registered = await store.registerReferenceAsset({
      assetId: "runtime.ship-model.vanguard",
      kind: "model",
      title: "Vanguard 3D Ship",
      provenance: "generated-runtime",
      components: [
        {
          role: "model",
          mimeType: "application/json",
          format: "json",
          storageClass: "runtime-reference",
          runtimeUrl: "/assets/space-typing/ships/3d/vanguard/model.json",
        },
        {
          role: "height",
          mimeType: "application/octet-stream",
          format: "bin",
          storageClass: "runtime-reference",
          runtimeUrl: "/assets/space-typing/ships/3d/vanguard/height.bin",
        },
      ],
      source: {
        owner: "space-typing",
        sourcePath: "art-src/ships/vanguard-top-hd.png",
      },
    });

    const resolved = await resolveExactRuntimeMediaVersion(store, registered.version.assetVersionId);
    assert.equal(resolved.kind, "model");
    assert.equal(resolved.provenance, "generated-runtime");
    assert.deepEqual(
      resolved.components.map((component) => component.runtimeUrl),
      [
        "/assets/space-typing/ships/3d/vanguard/height.bin",
        "/assets/space-typing/ships/3d/vanguard/model.json",
      ],
    );
    assert.equal("source" in resolved, false);
    assert.equal("sourcePath" in resolved.components[0], false);
  });
});

test("runtime media resolution fails closed for non-runtime and cross-origin components", async () => {
  await withStore(async (store) => {
    const sourceOnly = await store.registerReferenceAsset({
      assetId: "runtime.source-only.asset",
      kind: "data",
      title: "Source Only",
      provenance: "code-owned",
      components: [{
        role: "primary",
        mimeType: "application/json",
        storageClass: "source-reference",
        sourcePath: "private/source.json",
      }],
    });
    await assert.rejects(
      () => resolveExactRuntimeMediaVersion(store, sourceOnly.version.assetVersionId),
      (error) => error instanceof MediaRuntimeError && error.code === "unsupported-runtime-component",
    );

    const external = await store.registerReferenceAsset({
      assetId: "runtime.external.asset",
      kind: "image",
      title: "External",
      provenance: "external-reference",
      components: [{
        role: "primary",
        mimeType: "image/webp",
        storageClass: "external-reference",
        runtimeUrl: "https://example.invalid/external.webp",
      }],
    });
    await assert.rejects(
      () => resolveExactRuntimeMediaVersion(store, external.version.assetVersionId),
      (error) => error instanceof MediaRuntimeError && error.code === "unsupported-runtime-component",
    );
  });
});

test("runtime media resolution never accepts a current/latest alias", async () => {
  await withStore(async (store) => {
    await assert.rejects(
      () => resolveExactRuntimeMediaVersion(store, "current"),
      (error) => error instanceof MediaRuntimeError && error.code === "unknown-version",
    );
    await assert.rejects(
      () => resolveExactRuntimeMediaVersion(store, "latest"),
      (error) => error instanceof MediaRuntimeError && error.code === "unknown-version",
    );
  });
});
