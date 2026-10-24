import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Readable } from "node:stream";
import test from "node:test";
import { AdminAuthorizationError, LocalAdminAuditLog, createLocalAdminActor } from "./admin-security.mjs";
import { MediaAssetStore } from "./media-assets-v2.mjs";
import { createMediaV2HttpHandler } from "./media-http.mjs";

class MockResponse {
  constructor() {
    this.status = null;
    this.headers = {};
    this.chunks = [];
  }

  writeHead(status, headers = {}) {
    this.status = status;
    this.headers = Object.fromEntries(Object.entries(headers).map(([key, value]) => [key.toLowerCase(), value]));
  }

  end(value) {
    if (value !== undefined) this.chunks.push(Buffer.isBuffer(value) ? value : Buffer.from(String(value)));
  }

  buffer() {
    return Buffer.concat(this.chunks);
  }

  json() {
    return JSON.parse(this.buffer().toString("utf8"));
  }
}

function request(method, path, { headers = {}, body = Buffer.alloc(0) } = {}) {
  const stream = Readable.from(body.length ? [body] : []);
  stream.method = method;
  stream.headers = Object.fromEntries(Object.entries(headers).map(([key, value]) => [key.toLowerCase(), value]));
  return {
    request: stream,
    response: new MockResponse(),
    url: new URL(path, "http://127.0.0.1:3199"),
  };
}

async function fixture(run) {
  const rootDir = await mkdtemp(join(tmpdir(), "space-admin-media-http-"));
  const store = new MediaAssetStore({ rootDir });
  const auditLog = new LocalAdminAuditLog({ rootDir });
  await store.initialize();
  const handler = createMediaV2HttpHandler({ store, auditLog });
  const actor = createLocalAdminActor({ actorId: "media-manager", displayName: "Media Manager", requestId: "req-media-test" });
  try {
    await run({ rootDir, store, auditLog, handler, actor });
  } finally {
    await rm(rootDir, { recursive: true, force: true });
  }
}

async function call(handler, actor, method, path, options) {
  const context = request(method, path, options);
  const handled = await handler({ ...context, actor });
  assert.equal(handled, true);
  return context.response;
}

test("Media HTTP creates immutable assets, lists them and serves exact Admin blobs", async () => {
  await fixture(async ({ handler, actor, auditLog }) => {
    const create = await call(handler, actor, "POST", "/api/admin/space-typing/media/assets", {
      headers: {
        "x-media-kind": "image",
        "x-media-title": "Vanguard Portrait",
        "x-media-file-name": "vanguard.png",
        "x-media-tags": "ships, portrait",
        "content-type": "image/png",
      },
      body: Buffer.from("portrait-v1"),
    });
    assert.equal(create.status, 201);
    const created = create.json();
    assert.equal(created.asset.title, "Vanguard Portrait");
    assert.equal(created.version.provenance, "admin-upload");

    const list = await call(handler, actor, "GET", "/api/admin/space-typing/media/assets?kind=image&q=vanguard");
    assert.equal(list.status, 200);
    assert.equal(list.json().assets.length, 1);

    const detail = await call(handler, actor, "GET", `/api/admin/space-typing/media/assets/${encodeURIComponent(created.asset.assetId)}`);
    assert.equal(detail.status, 200);
    assert.equal(detail.json().versions.length, 1);
    assert.equal(detail.json().references.length, 0);

    const blob = await call(handler, actor, "GET", `/api/admin/space-typing/media/blobs/${encodeURIComponent(created.version.assetVersionId)}/primary`);
    assert.equal(blob.status, 200);
    assert.equal(blob.headers["content-type"], "image/png");
    assert.match(blob.headers["cache-control"], /immutable/);
    assert.equal(blob.buffer().toString("utf8"), "portrait-v1");

    const events = await auditLog.list({ limit: 10 });
    assert.equal(events.filter((event) => event.action === "media.asset.create" && event.result === "attempt").length, 1);
    assert.equal(events.filter((event) => event.action === "media.asset.create" && event.result === "success").length, 1);
    const success = events.find((event) => event.action === "media.asset.create" && event.result === "success");
    assert.equal(success.entityId, created.asset.assetId);
    assert.equal(success.changeScope.assetVersionId, created.version.assetVersionId);
    assert.equal(success.changeScope.changesGameplay, false);
  });
});

test("Media HTTP replacement creates a new version without mutating the old blob", async () => {
  await fixture(async ({ handler, actor }) => {
    const first = (await call(handler, actor, "POST", "/api/admin/space-typing/media/assets", {
      headers: {
        "x-media-kind": "sfx",
        "x-media-title": "Laser",
        "x-media-file-name": "laser-v1.ogg",
        "content-type": "audio/ogg",
      },
      body: Buffer.from("laser-v1"),
    })).json();

    const secondResponse = await call(handler, actor, "POST", `/api/admin/space-typing/media/assets/${encodeURIComponent(first.asset.assetId)}/versions`, {
      headers: {
        "x-media-file-name": "laser-v2.ogg",
        "content-type": "audio/ogg",
      },
      body: Buffer.from("laser-v2"),
    });
    assert.equal(secondResponse.status, 201);
    const second = secondResponse.json();
    assert.notEqual(second.version.assetVersionId, first.version.assetVersionId);

    const oldBlob = await call(handler, actor, "GET", `/api/admin/space-typing/media/blobs/${encodeURIComponent(first.version.assetVersionId)}/primary`);
    const newBlob = await call(handler, actor, "GET", `/api/admin/space-typing/media/blobs/${encodeURIComponent(second.version.assetVersionId)}/primary`);
    assert.equal(oldBlob.buffer().toString("utf8"), "laser-v1");
    assert.equal(newBlob.buffer().toString("utf8"), "laser-v2");

    const versions = await call(handler, actor, "GET", `/api/admin/space-typing/media/assets/${encodeURIComponent(first.asset.assetId)}/versions`);
    assert.equal(versions.json().versions.length, 2);
  });
});

test("archive/unarchive uses media.delete permission but never hard-deletes versions", async () => {
  await fixture(async ({ handler, actor, store }) => {
    const created = (await call(handler, actor, "POST", "/api/admin/space-typing/media/assets", {
      headers: {
        "x-media-kind": "music",
        "x-media-title": "Boss Theme",
        "x-media-file-name": "boss.ogg",
        "content-type": "audio/ogg",
      },
      body: Buffer.from("boss-theme"),
    })).json();

    const archive = await call(handler, actor, "POST", `/api/admin/space-typing/media/assets/${encodeURIComponent(created.asset.assetId)}/archive`, {
      headers: { "content-type": "application/json" },
      body: Buffer.from(JSON.stringify({ archived: true })),
    });
    assert.equal(archive.status, 200);
    assert.equal(archive.json().lifecycle, "archived");

    assert.equal((await call(handler, actor, "GET", "/api/admin/space-typing/media/assets")).json().assets.length, 0);
    assert.equal((await call(handler, actor, "GET", "/api/admin/space-typing/media/assets?includeArchived=true")).json().assets.length, 1);
    assert.equal((await store.getVersion(created.version.assetVersionId)).assetId, created.asset.assetId);

    const deleteRoute = await call(handler, actor, "DELETE", `/api/admin/space-typing/media/versions/${encodeURIComponent(created.version.assetVersionId)}`);
    assert.equal(deleteRoute.status, 404, "normal Media HTTP surface must not expose hard delete");
    assert.equal((await store.getVersion(created.version.assetVersionId)).assetId, created.asset.assetId);

    const unarchive = await call(handler, actor, "POST", `/api/admin/space-typing/media/assets/${encodeURIComponent(created.asset.assetId)}/archive`, {
      headers: { "content-type": "application/json" },
      body: Buffer.from(JSON.stringify({ archived: false })),
    });
    assert.equal(unarchive.json().lifecycle, "active");
  });
});

test("reference-only components return canonical-runtime guidance instead of being proxied as Admin blobs", async () => {
  await fixture(async ({ handler, actor, store }) => {
    const registered = await store.registerReferenceAsset({
      assetId: "runtime.ship-model.vanguard",
      kind: "model",
      title: "Vanguard Model",
      provenance: "generated-runtime",
      components: [{
        role: "model",
        mimeType: "application/json",
        format: "json",
        storageClass: "runtime-reference",
        runtimeUrl: "/assets/space-typing/ships/3d/vanguard/model.json",
      }],
      source: { owner: "space-typing", generator: "pnpm ship3d:prepare" },
    });

    const response = await call(handler, actor, "GET", `/api/admin/space-typing/media/blobs/${encodeURIComponent(registered.version.assetVersionId)}/model`);
    assert.equal(response.status, 409);
    assert.equal(response.json().error, "reference-only");
  });
});

test("Media write permission fails closed and records denied audit", async () => {
  await fixture(async ({ handler, auditLog }) => {
    const actor = Object.freeze({
      actorId: "viewer",
      actorDisplayName: "Viewer",
      authMethod: "test",
      role: "viewer",
      requestId: "req-denied",
      permissions: [],
    });
    const context = request("POST", "/api/admin/space-typing/media/assets", {
      headers: {
        "x-media-kind": "image",
        "x-media-title": "Denied",
        "x-media-file-name": "denied.png",
        "content-type": "image/png",
      },
      body: Buffer.from("denied"),
    });

    await assert.rejects(
      () => handler({ ...context, actor }),
      (error) => error instanceof AdminAuthorizationError && error.permission === "media.upload",
    );
    const events = await auditLog.list({ limit: 10 });
    assert.equal(events[0].result, "denied");
    assert.equal(events[0].action, "media.asset.create");
  });
});

test("Media HTTP serializes concurrent uploads so registry admissions are not lost", async () => {
  await fixture(async ({ handler, actor, store }) => {
    await Promise.all(Array.from({ length: 8 }, (_, index) => call(handler, actor, "POST", "/api/admin/space-typing/media/assets", {
      headers: {
        "x-media-kind": "image",
        "x-media-title": `Image ${index + 1}`,
        "x-media-file-name": `image-${index + 1}.png`,
        "content-type": "image/png",
      },
      body: Buffer.from(`image-${index + 1}`),
    })));
    assert.equal((await store.listAssets()).length, 8);
  });
});
