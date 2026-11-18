import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Readable } from "node:stream";
import test from "node:test";
import { LocalAdminAuditLog, createLocalAdminActor } from "./admin-security.mjs";
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

  json() {
    return JSON.parse(Buffer.concat(this.chunks).toString("utf8"));
  }
}

function context(method, path, { headers = {}, body = Buffer.alloc(0) } = {}) {
  const request = Readable.from(body.length ? [body] : []);
  request.method = method;
  request.headers = Object.fromEntries(Object.entries(headers).map(([key, value]) => [key.toLowerCase(), value]));
  return {
    request,
    response: new MockResponse(),
    url: new URL(path, "http://127.0.0.1:3199"),
  };
}

async function call(handler, actor, method, path, options) {
  const value = context(method, path, options);
  assert.equal(await handler({ ...value, actor }), true);
  return value.response;
}

test("runtime-owned Media V2 assets reject replacement and archive mutations", async () => {
  const rootDir = await mkdtemp(join(tmpdir(), "space-admin-media-owner-"));
  try {
    const store = new MediaAssetStore({ rootDir });
    const auditLog = new LocalAdminAuditLog({ rootDir });
    await store.initialize();
    const registered = await store.registerReferenceAsset({
      assetId: "runtime.ship-model.vanguard",
      kind: "model",
      title: "Vanguard 3D Ship",
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
    const actor = createLocalAdminActor({ actorId: "media-manager", displayName: "Media Manager", requestId: "req-owner-boundary" });
    const handler = createMediaV2HttpHandler({ store, auditLog });

    const replace = await call(
      handler,
      actor,
      "POST",
      "/api/admin/space-typing/media/assets/runtime.ship-model.vanguard/versions",
      {
        headers: {
          "x-media-file-name": "replacement.json",
          "x-media-role": "model",
          "content-type": "application/json",
        },
        body: Buffer.from('{"replacement":true}'),
      },
    );
    assert.equal(replace.status, 409);
    assert.equal(replace.json().error, "read-only-owner");

    const archive = await call(
      handler,
      actor,
      "POST",
      "/api/admin/space-typing/media/assets/runtime.ship-model.vanguard/archive",
      {
        headers: { "content-type": "application/json" },
        body: Buffer.from(JSON.stringify({ archived: true })),
      },
    );
    assert.equal(archive.status, 409);
    assert.equal(archive.json().error, "read-only-owner");

    const asset = await store.getAsset("runtime.ship-model.vanguard");
    assert.equal(asset.lifecycle, "active");
    assert.equal(asset.currentVersionId, registered.version.assetVersionId);
    assert.equal((await store.listVersions(asset.assetId)).length, 1, "read-only ownership rejection must not create a shadow Admin version");

    const deniedOwnerMutations = (await auditLog.list({ limit: 20 }))
      .filter((event) => event.action === "media.asset.version.create" || event.action === "media.asset.archive");
    assert.equal(deniedOwnerMutations.length, 0, "ownership checks happen before mutation/audit workflow because no mutation is admissible");
  } finally {
    await rm(rootDir, { recursive: true, force: true });
  }
});
