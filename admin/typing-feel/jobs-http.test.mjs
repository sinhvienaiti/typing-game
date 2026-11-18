// node --test admin/typing-feel/jobs-http.test.mjs
// Add sound set routes (docs/games/TYPING_FEEL_SERVICE.md §3.8, §3.12, §3.13):
// capabilities and job reads for every role; the upload check, Format, Accept and
// Discard only with shared.publish; the token check of server.mjs in front of all
// of them; job files by one checked name; audit under domain "typing-feel".
import assert from "node:assert/strict";
import { join } from "node:path";
import { Readable } from "node:stream";
import test from "node:test";
import { createLocalAdminActor } from "../admin-security.mjs";
import { FAKE_NATURAL_TOOL as FAKE_TOOL, fakeWav, makeTypingFeelFixture } from "./fixture.mjs";
import { JOB_PERMISSIONS, createTypingFeelHttpHandler } from "./http.mjs";
import { SOURCE_TAGS, TypingFeelJobs } from "./jobs.mjs";

const quiet = { log() {}, warn() {}, error() {} };

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

  get body() {
    return Buffer.concat(this.chunks);
  }
}

const ROLES = {
  viewer: createLocalAdminActor({ actorId: "viewer", role: "viewer" }),
  editor: createLocalAdminActor({ actorId: "editor", role: "editor" }),
  publisher: createLocalAdminActor({ actorId: "publisher", role: "publisher" }),
  spacePublisher: createLocalAdminActor({ actorId: "space-publisher", role: "publisher", permissionOverrideText: "-shared.publish" }),
  owner: createLocalAdminActor({ actorId: "owner", role: "super-admin" }),
};

async function harness(t) {
  const fx = await makeTypingFeelFixture(t);
  const tool = { command: process.execPath, args: [FAKE_TOOL], cwd: fx.base, env: { PATH: process.env.PATH, FAKE_NATURAL_MODE: "ok", FAKE_NATURAL_LOG: join(fx.base, "runs.jsonl") } };
  const jobs = new TypingFeelJobs({ store: fx.store, service: fx.service, mediaStore: fx.mediaStore, tool, machine: async () => ({ ready: true, venv: true, ffmpeg: true, problems: [] }), logger: quiet });
  const typingFeel = { status: "available", service: fx.service, jobs, message: null, startup: null };
  const admin = createTypingFeelHttpHandler({ typingFeel, auditLog: fx.auditLog });
  const call = async (actor, method, path, body) => {
    const bytes = body === undefined ? [] : [Buffer.from(JSON.stringify(body))];
    const request = Readable.from(bytes);
    request.method = method;
    request.headers = { "content-type": "application/json" };
    const response = new MockResponse();
    assert.equal(await admin({ request, response, url: new URL(`/api/admin/shared/typing-feel${path}`, "http://127.0.0.1:3199"), actor }), true, `${method} ${path} is handled`);
    let data = null;
    try {
      data = JSON.parse(response.body.toString("utf8"));
    } catch {
      data = null;
    }
    return { status: response.status, headers: response.headers, body: response.body, data };
  };
  const upload = async (name = "raindrop.wav", tags = SOURCE_TAGS) => (await fx.mediaStore.createUploadAsset({ kind: "audio", title: name, filename: name, mimeType: "audio/wav", buffer: fakeWav(name), tags })).version;
  return { fx, jobs, typingFeel, call, upload };
}

test("reads for every role; the upload check, Format, Accept and Discard need shared.publish", async (t) => {
  const { fx, jobs, call, upload } = await harness(t);
  assert.deepEqual({ ...JOB_PERMISSIONS }, { check: "shared.publish", format: "shared.publish", accept: "shared.publish", discard: "shared.publish", upload: "media.upload", draft: "config.draft" });
  for (const actor of Object.values(ROLES)) {
    const capabilities = await call(actor, "GET", "/capabilities");
    assert.equal(capabilities.status, 200, actor.actorId);
    assert.deepEqual(capabilities.data.recipes, ["natural-v1"]);
    assert.equal(capabilities.data.upload.maxBytes, 50 * 1024 * 1024);
    assert.equal(capabilities.data.publishedOwnerScore, 9);
    assert.equal(capabilities.data.permissions.format, actor.permissions.includes("shared.publish"));
    assert.equal(capabilities.data.permissions.upload, actor.permissions.includes("media.upload"));
    assert.equal((await call(actor, "GET", "/jobs")).status, 200);
  }
  const source = await upload();
  for (const actor of [ROLES.viewer, ROLES.editor, ROLES.spacePublisher]) {
    assert.equal((await call(actor, "POST", "/sources/check", { sourceAssetVersionId: source.assetVersionId })).status, 403, `${actor.actorId} check`);
    const refused = await call(actor, "POST", "/jobs", { sourceAssetVersionId: source.assetVersionId, recipe: "natural-v1" });
    assert.equal(refused.status, 403, `${actor.actorId} Format`);
    assert.equal(refused.data.permission, "shared.publish");
  }
  assert.equal((await jobs.list()).jobs.length, 0, "a refused Format leaves no job");

  const checked = await call(ROLES.publisher, "POST", "/sources/check", { sourceAssetVersionId: source.assetVersionId });
  assert.equal(checked.status, 200);
  assert.equal(checked.data.ok, true);
  assert.equal(checked.data.source.tapsUsable, 17);
  assert.equal(checked.data.source.file, "raindrop.wav");

  const started = await call(ROLES.owner, "POST", "/jobs", { sourceAssetVersionId: source.assetVersionId, recipe: "natural-v1", setId: "rain-http", name: "Rain HTTP", family: "deep" });
  assert.equal(started.status, 202);
  const { jobId } = started.data;
  assert.match(jobId, /^j\d{8}-\d{6}-[0-9a-f]{6}$/);
  await jobs.whenIdle();
  const read = await call(ROLES.viewer, "GET", `/jobs/${jobId}`);
  assert.equal(read.status, 200);
  assert.equal(read.data.job.status, "succeeded");
  assert.equal(read.data.report.counts.key, 12);
  assert.equal(read.data.filesBase, `/api/admin/shared/typing-feel/jobs/${jobId}/files/`);
  assert.equal(read.data.timeoutSeconds, 180);

  const preview = await call(ROLES.viewer, "GET", `/jobs/${jobId}/files/preview.ogg`);
  assert.equal(preview.status, 200);
  assert.equal(preview.headers["content-type"], "audio/ogg");
  assert.equal(preview.headers["x-content-type-options"], "nosniff");
  assert.match(preview.body.toString("utf8"), /^OggS fake rain-http preview\.ogg/);
  assert.equal((await call(ROLES.viewer, "GET", `/jobs/${jobId}/files/natural.mp3`)).headers["content-type"], "audio/mpeg");
  for (const bad of ["..%2Fjob.json", "job.json", "%2E%2E", "source.wav", "evil.sh", "%ZZ"]) assert.equal((await call(ROLES.viewer, "GET", `/jobs/${jobId}/files/${bad}`)).status, 404, bad);
  for (const path of ["/jobs/..%2F..%2Fstate.json", "/jobs/j20261031-000000-abcdef", `/jobs/${jobId}/files/a/b`, `/jobs/${jobId}/nope`]) assert.equal((await call(ROLES.viewer, "GET", path)).status, 404, path);

  const accept = { setId: "rain-http", name: "Rain HTTP", family: "deep", ownerScore: 9 };
  for (const actor of [ROLES.viewer, ROLES.editor, ROLES.spacePublisher]) {
    assert.equal((await call(actor, "POST", `/jobs/${jobId}/accept`, accept)).status, 403, `${actor.actorId} Accept`);
    assert.equal((await call(actor, "POST", `/jobs/${jobId}/discard`, {})).status, 403, `${actor.actorId} Discard`);
  }
  const bad = await call(ROLES.owner, "POST", `/jobs/${jobId}/accept`, { ...accept, ownerScore: 8 });
  assert.equal(bad.status, 400);
  assert.match(bad.data.message, /needs a reason/);
  const accepted = await call(ROLES.owner, "POST", `/jobs/${jobId}/accept`, accept);
  assert.equal(accepted.status, 201);
  assert.equal(accepted.data.row.id, "rain-http");
  assert.equal(accepted.data.row.status, "published");
  assert.equal(accepted.data.job.status, "accepted");
  assert.equal((await call(ROLES.owner, "POST", `/jobs/${jobId}/accept`, accept)).status, 409);
  assert.equal((await call(ROLES.owner, "POST", `/jobs/${jobId}/discard`, {})).status, 409);
  assert.equal((await call(ROLES.viewer, "GET", `/jobs/${jobId}/files/key-01.ogg`)).status, 200, "an accepted job still plays, from Media V2");

  // Audit: one domain, the job actions named apart from Space and from Publish.
  const events = (await fx.auditLog.list({ limit: 200 })).filter((event) => event.domain === "typing-feel");
  const success = (action) => events.filter((event) => event.action === action && event.result === "success");
  assert.equal(success("typing-feel.job.format").length, 1);
  assert.equal(success("typing-feel.job.format")[0].entityId, jobId);
  assert.equal(success("typing-feel.job.accept").length, 1);
  assert.equal(success("typing-feel.job.accept")[0].changeScope.assetVersionId, accepted.data.version.assetVersionId);
  assert.ok(events.some((event) => event.action === "typing-feel.job.format" && event.result === "denied" && event.actor.actorId === "editor"));
});

test("bad Format and Accept input answers 400 or 404 with one clear line; Discard drops a job", async (t) => {
  const { call, upload, jobs, typingFeel } = await harness(t);
  const source = await upload();
  const recipe = await call(ROLES.owner, "POST", "/jobs", { sourceAssetVersionId: source.assetVersionId, recipe: "firefly-218" });
  assert.equal(recipe.status, 400);
  assert.match(recipe.data.message, /offers natural-v1 only/);
  assert.equal((await call(ROLES.owner, "POST", "/jobs", { sourceAssetVersionId: "media-version.missing" })).status, 404);
  const untagged = await upload("loop.wav", ["typing-feel"]);
  const tag = await call(ROLES.owner, "POST", "/sources/check", { sourceAssetVersionId: untagged.assetVersionId });
  assert.equal(tag.status, 400);
  assert.match(tag.data.message, /keyboard-source/);
  const live = await call(ROLES.owner, "POST", "/jobs", { sourceAssetVersionId: source.assetVersionId, setId: "raindrop-tile" });
  assert.equal(live.status, 400);
  assert.match(live.data.message, /already a live set/);
  const malformed = await call(ROLES.owner, "POST", "/jobs", "not an object");
  assert.equal(malformed.status, 400);

  const started = await call(ROLES.owner, "POST", "/jobs", { sourceAssetVersionId: source.assetVersionId });
  await jobs.whenIdle();
  const discarded = await call(ROLES.owner, "POST", `/jobs/${started.data.jobId}/discard`, {});
  assert.equal(discarded.status, 200);
  assert.equal(discarded.data.job.status, "discarded");
  assert.equal((await call(ROLES.viewer, "GET", `/jobs/${started.data.jobId}/files/preview.ogg`)).status, 404, "a discarded job's files are gone");

  typingFeel.jobs = null;
  assert.equal((await call(ROLES.owner, "GET", "/capabilities")).status, 503);
});
