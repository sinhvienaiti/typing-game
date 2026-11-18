// node --test admin/typing-feel/http.test.mjs
// Typing Feel routes: reads for every Admin role, drafts with config.draft,
// Publish and Rollback with shared.publish only, audit under domain
// "typing-feel", and the no-token preview of a checked revision (§3.12, §3.13).
import assert from "node:assert/strict";
import { writeFile } from "node:fs/promises";
import { join } from "node:path";
import { Readable } from "node:stream";
import test from "node:test";
import { createLocalAdminActor } from "../admin-security.mjs";
import { activeConfig, makeTypingFeelFixture, readCatalogue, tempDir } from "./fixture.mjs";
import { createTypingFeelHttpHandler, createTypingFeelRuntimeHandler } from "./http.mjs";
import { resolveTypingFeelLocations } from "./locations.mjs";
import { startTypingFeel } from "./setup.mjs";

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

  json() {
    return JSON.parse(this.body.toString("utf8"));
  }
}

function makeRequest(method, path, body) {
  const bytes = body === undefined ? Buffer.alloc(0) : Buffer.from(JSON.stringify(body));
  const request = Readable.from(bytes.length ? [bytes] : []);
  request.method = method;
  request.headers = { "content-type": "application/json" };
  return { request, response: new MockResponse(), url: new URL(path, "http://127.0.0.1:3199") };
}

const ROLES = {
  viewer: createLocalAdminActor({ actorId: "viewer", role: "viewer" }),
  editor: createLocalAdminActor({ actorId: "editor", role: "editor" }),
  publisher: createLocalAdminActor({ actorId: "publisher", role: "publisher" }),
  spacePublisher: createLocalAdminActor({ actorId: "space-publisher", role: "publisher", permissionOverrideText: "-shared.publish" }),
  owner: createLocalAdminActor({ actorId: "owner", role: "super-admin" }),
};

async function harness(t, options) {
  const fx = await makeTypingFeelFixture(t, options);
  const typingFeel = { status: "available", service: fx.service, message: null, startup: null };
  const admin = createTypingFeelHttpHandler({ typingFeel, auditLog: fx.auditLog });
  const runtime = createTypingFeelRuntimeHandler({ typingFeel });
  const call = async (actor, method, path, body) => {
    const exchange = makeRequest(method, `/api/admin/shared/typing-feel${path}`, body);
    assert.equal(await admin({ ...exchange, actor }), true, `${method} ${path} is handled`);
    return { status: exchange.response.status, data: exchange.response.json() };
  };
  const get = async (method, path) => {
    const exchange = makeRequest(method, path);
    const handled = await runtime(exchange);
    return { handled, status: exchange.response.status, headers: exchange.response.headers, body: exchange.response.body };
  };
  return { fx, typingFeel, admin, call, get };
}

test("reads work for every role; drafts need config.draft; Publish and Rollback need shared.publish", async (t) => {
  const { fx, call } = await harness(t);
  for (const actor of Object.values(ROLES)) {
    for (const path of ["/state", "/draft", "/history", "/library", "/export/status"]) {
      const result = await call(actor, "GET", path);
      assert.equal(result.status, 200, `${actor.actorId} GET ${path}`);
    }
  }
  const viewerState = (await call(ROLES.viewer, "GET", "/state")).data;
  assert.deepEqual(viewerState.permissions, { draft: false, publish: false, rollback: false });
  assert.deepEqual(viewerState.requiredPermissions, { draft: "config.draft", publish: "shared.publish", rollback: "shared.publish" });
  assert.equal(viewerState.active.revision, "seed-v1");
  assert.equal(viewerState.local.matchesActive, true);
  // The pages offer exactly the contract's lists (§3.10), so a page can never pick what the checks refuse.
  const contract = fx.store.contract;
  assert.deepEqual(viewerState.options.effects, { styles: contract.effects.styles, intensities: contract.effects.intensities, sizes: contract.effects.sizes, volume: contract.effects.volume, defaults: contract.effects.defaults });
  assert.deepEqual(viewerState.options.statuses, contract.statuses);
  assert.deepEqual(viewerState.options.labels, Object.keys(contract.labels));
  assert.equal(viewerState.options.idPattern, contract.id.pattern);
  assert.equal(viewerState.options.publishedOwnerScore, 9);
  assert.equal((await call(ROLES.viewer, "GET", "/history")).data.events, null, "audit events need audit.read");

  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.defaultSet = "deep";
  const draftBody = { baseRevision: seed, config, message: "Default: Deep" };
  const denied = await call(ROLES.viewer, "POST", "/revisions", draftBody);
  assert.equal(denied.status, 403);
  assert.equal(denied.data.permission, "config.draft");
  const created = await call(ROLES.editor, "POST", "/revisions", draftBody);
  assert.equal(created.status, 201);
  const revision = created.data.revision;
  assert.equal((await call(ROLES.editor, "GET", "/draft")).data.draft.revision, revision);

  const review = await call(ROLES.viewer, "POST", "/validate-revision", { revision });
  assert.equal(review.status, 200);
  assert.equal(review.data.valid, true);
  assert.equal(review.data.changeScope.affects, "all games");
  assert.deepEqual(review.data.changeScope.defaultChanged, { from: "bright-clack", to: "deep" });
  assert.equal((await call(ROLES.viewer, "POST", "/change-scope", { revision })).data.defaultChanged.to, "deep");

  const before = await readCatalogue(fx.publicDir);
  for (const actor of [ROLES.viewer, ROLES.editor, ROLES.spacePublisher]) {
    const refused = await call(actor, "POST", "/publish", { revision, expectedActiveRevision: seed });
    assert.equal(refused.status, 403, `${actor.actorId} cannot publish to all games`);
    assert.equal(refused.data.permission, "shared.publish");
  }
  assert.equal(await readCatalogue(fx.publicDir), before, "refused publishes change nothing");
  const stale = await call(ROLES.publisher, "POST", "/publish", { revision, expectedActiveRevision: "r-old" });
  assert.equal(stale.status, 409);
  const published = await call(ROLES.publisher, "POST", "/publish", { revision, expectedActiveRevision: seed });
  assert.equal(published.status, 200, JSON.stringify(published.data));
  assert.equal(published.data.state.activeRevision, revision);
  assert.equal(JSON.parse(await readCatalogue(fx.publicDir)).default, "deep");

  // Any role can read what a Rollback would change; it writes nothing.
  const rollbackScope = await call(ROLES.viewer, "POST", "/rollback-change-scope", { targetRevision: seed });
  assert.equal(rollbackScope.status, 200);
  assert.equal(rollbackScope.data.affects, "all games");
  assert.deepEqual(rollbackScope.data.defaultChanged, { from: "deep", to: "bright-clack" });
  assert.equal((await call(ROLES.viewer, "POST", "/rollback-change-scope", {})).status, 400);
  assert.equal((await call(ROLES.viewer, "POST", "/rollback-change-scope", { targetRevision: "r-missing" })).status, 404);
  for (const actor of [ROLES.editor, ROLES.spacePublisher]) {
    assert.equal((await call(actor, "POST", "/rollback", { targetRevision: seed, expectedActiveRevision: revision })).status, 403);
  }
  const rolledBack = await call(ROLES.publisher, "POST", "/rollback", { targetRevision: seed, expectedActiveRevision: revision });
  assert.equal(rolledBack.status, 200);
  assert.equal(await readCatalogue(fx.publicDir), before);

  const events = (await call(ROLES.owner, "GET", "/history")).data.events;
  const summary = events.map((event) => `${event.action}:${event.result}:${event.actor.actorId}`);
  assert.ok(summary.includes("typing-feel.revision.create:denied:viewer"));
  assert.ok(summary.includes("typing-feel.revision.create:success:editor"));
  assert.ok(summary.includes("typing-feel.publish:denied:space-publisher"));
  assert.ok(summary.includes("typing-feel.publish:success:publisher"));
  assert.ok(summary.includes("typing-feel.rollback:success:publisher"));
  assert.ok(events.every((event) => event.domain === "typing-feel"));
  const publishEvent = events.find((event) => event.action === "typing-feel.publish" && event.result === "success");
  assert.equal(publishEvent.changeScope.affects, "all games");
});

test("bad drafts, unknown revisions and an unimported store answer with clear errors", async (t) => {
  const { fx, call } = await harness(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets[0].id = "Not An Id";
  const invalid = await call(ROLES.owner, "POST", "/revisions", { baseRevision: seed, config });
  assert.equal(invalid.status, 400);
  assert.equal(invalid.data.error, "validation");
  assert.ok(invalid.data.problems.some((problem) => /must match/.test(problem)));
  assert.equal((await call(ROLES.owner, "GET", "/revisions/r-missing")).status, 404);
  const malformed = await call(ROLES.owner, "GET", "/revisions/%E0%A4%A");
  assert.deepEqual([malformed.status, malformed.data.error], [400, "validation"], "a malformed percent-encoding is a bad request, not a 500");
  assert.equal((await call(ROLES.owner, "POST", "/validate-revision", { revision: "r-missing" })).status, 404);
  assert.equal((await call(ROLES.owner, "GET", "/nothing-here")).status, 404);

  const empty = await harness(t, { seed: false });
  const state = await empty.call(ROLES.owner, "GET", "/state");
  assert.equal(state.data.initialized, false);
  assert.match(state.data.setup.importCommand, /import-staging\.mjs/);
  const refused = await empty.call(ROLES.owner, "POST", "/revisions", { baseRevision: "seed-v1", config });
  assert.equal(refused.status, 409);
  assert.equal(refused.data.error, "typing-feel-not-imported");

  const off = createTypingFeelHttpHandler({ typingFeel: { status: "unavailable", service: null, message: "Typing Feel is off." }, auditLog: fx.auditLog });
  const exchange = makeRequest("GET", "/api/admin/shared/typing-feel/state");
  await off({ ...exchange, actor: ROLES.owner });
  assert.equal(exchange.response.status, 503);
  assert.equal(exchange.response.json().message, "Typing Feel is off.");
  const other = makeRequest("GET", "/api/admin/shared/overview");
  assert.equal(await off({ ...other, actor: ROLES.owner }), false, "other shared routes are not this handler's");
});

test("the no-token preview serves only the files of a checked revision", async (t) => {
  const { fx, call, get } = await harness(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets.find((set) => set.id === "deep").enabled = false;
  const draft = (await call(ROLES.owner, "POST", "/revisions", { baseRevision: seed, config })).data.revision;
  const base = `/api/runtime/typing-feel/preview/${draft}/keys/`;
  const catalogue = await get("GET", `${base}keys-manifest.json`);
  assert.equal(catalogue.status, 200);
  assert.match(catalogue.headers["content-type"], /^application\/json/);
  assert.equal(catalogue.headers["x-content-type-options"], "nosniff");
  const parsed = JSON.parse(catalogue.body.toString("utf8"));
  assert.equal(parsed.revision, draft);
  assert.ok(!parsed.profiles.some((profile) => profile.id === "deep"), "the preview is the draft's export");
  const raindrop = parsed.profiles.find((profile) => profile.id === "raindrop-tile");
  const preview = await get("GET", `${base}${raindrop.preview}`);
  assert.equal(preview.status, 200);
  assert.equal(preview.headers["content-type"], "audio/ogg");
  assert.equal(preview.body.toString("utf8"), "OggS fake raindrop-tile/preview.ogg\n");
  assert.equal((await get("HEAD", `${base}${raindrop.manifest}`)).status, 200);

  // Plain ../ segments never reach the handler: the URL parser resolves them first.
  for (const path of [`${base}sets/raindrop-tile/000000000000/preview.ogg`, `${base}sets/raindrop-tile/..%2F..%2Fkeys-manifest.json`, `${base}index.html`, "/api/runtime/typing-feel/preview/", "/api/runtime/typing-feel/lab/index.html"]) {
    const missing = await get("GET", path);
    assert.equal(missing.status, 404, path);
    assert.match(missing.headers["content-type"], /^application\/json/, "a missing file is a 404, never an HTML page");
  }
  assert.equal((await get("GET", "/api/runtime/typing-feel/preview/r-missing/keys/keys-manifest.json")).status, 404);
  assert.equal((await get("POST", `${base}keys-manifest.json`)).status, 405);

  // The published copy of any set file, hidden sets too, for the Media Library's player.
  const deepFolder = JSON.parse(await readCatalogue(fx.publicDir)).profiles.find((profile) => profile.id === "deep").preview;
  const published = await get("GET", `/api/runtime/typing-feel/published/keys/${deepFolder}`);
  assert.equal(published.status, 200);
  assert.equal(published.headers["content-type"], "audio/ogg");
  assert.equal(published.body.toString("utf8"), "OggS fake deep/preview.ogg\n");
  for (const path of ["/api/runtime/typing-feel/published/keys/keys-manifest.json", "/api/runtime/typing-feel/published/keys/sets/deep/000000000000/preview.ogg", "/api/runtime/typing-feel/published/keys/sets/deep/..%2F..%2F..%2Fhealth.json"]) {
    assert.equal((await get("GET", path)).status, 404, path);
  }
  assert.equal((await get("GET", "/api/runtime/space-typing/media/assets")).handled, false, "other runtime routes are not this handler's");
});

test("start-up keeps Typing Feel off unless the three locations are moved together", async (t) => {
  const root = await tempDir(t);
  const quiet = { log() {}, warn() {}, error() {} };
  const partial = resolveTypingFeelLocations({ root, env: { TYPING_GAME_ADMIN_DATA_DIR: `${root}/data` } });
  assert.equal(partial.available, false);
  assert.match(partial.reason, /together or none/);
  assert.equal(resolveTypingFeelLocations({ root, env: {} }).mode, "default");

  const fx = await makeTypingFeelFixture(t);
  const env = { TYPING_GAME_ADMIN_DATA_DIR: fx.dataDir, TYPING_GAME_ADMIN_SHARED_DIR: fx.sharedDir, TYPING_FEEL_PUBLIC_DIR: fx.publicDir };
  const started = await startTypingFeel({ root, env, mediaStore: fx.mediaStore, auditLog: fx.auditLog, logger: quiet });
  assert.equal(started.typingFeel.status, "available");
  assert.equal(started.typingFeel.startup.status, "in-sync");
  const off = await startTypingFeel({ root, env: { TYPING_GAME_ADMIN_DATA_DIR: fx.dataDir }, mediaStore: fx.mediaStore, auditLog: fx.auditLog, logger: quiet });
  assert.equal(off.typingFeel.status, "unavailable");
  assert.equal(off.typingFeel.service, null);
  const empty = await startTypingFeel({ root, env: { ...env, TYPING_GAME_ADMIN_SHARED_DIR: `${fx.base}/shared-empty` }, mediaStore: fx.mediaStore, auditLog: fx.auditLog, logger: quiet });
  assert.equal(empty.typingFeel.status, "not-initialized");

  // A start-up that throws (here an unreadable state.json) leaves Typing Feel off with the reason, not editable.
  await writeFile(join(fx.sharedDir, "state.json"), "{ torn");
  const failed = await startTypingFeel({ root, env, mediaStore: fx.mediaStore, auditLog: fx.auditLog, logger: quiet });
  assert.equal(failed.typingFeel.status, "failed");
  assert.equal(failed.typingFeel.service, null);
  const exchange = makeRequest("GET", "/api/admin/shared/typing-feel/state");
  await failed.handleTypingFeelRequest({ ...exchange, actor: ROLES.owner });
  assert.equal(exchange.response.status, 503);
  assert.match(exchange.response.json().message, /^Typing Feel failed to start: .+ Fix it, then restart the Admin service\.$/);
});

test("state and history send History rows without configs; the draft waiting skips drafts older than the live revision", async (t) => {
  const { fx, call } = await harness(t);
  const { revision: seed, config } = await activeConfig(fx.store);
  const old = structuredClone(config);
  old.keyboard.defaultSet = "deep";
  const abandoned = (await call(ROLES.owner, "POST", "/revisions", { baseRevision: seed, config: old })).data.revision;
  const live = structuredClone(config);
  live.effects.defaults.style = "rune";
  const published = (await call(ROLES.owner, "POST", "/revisions", { baseRevision: seed, config: live })).data.revision;
  await call(ROLES.owner, "POST", "/publish", { revision: published, expectedActiveRevision: seed });
  await call(ROLES.owner, "POST", "/rollback", { targetRevision: seed, expectedActiveRevision: published });

  const state = (await call(ROLES.owner, "GET", "/state")).data;
  assert.ok(state.history.every((entry) => !("config" in entry)), "History rows come without configs");
  assert.ok(state.active.config && state.active.revision === seed, "the live revision comes whole");
  const row = (id) => state.history.find((entry) => entry.revision === id);
  assert.equal(row(abandoned).publishable, true, "the old draft sits on the live revision again");
  assert.equal(state.draft, null, "but it was saved before the rollback, so it is not the draft waiting");
  assert.ok((await call(ROLES.owner, "GET", "/history")).data.history.every((entry) => !("config" in entry)));
  assert.deepEqual((await call(ROLES.owner, "GET", `/revisions/${abandoned}`)).data.config, old, "one revision is read whole on demand");

  const fresh = (await call(ROLES.owner, "POST", "/revisions", { baseRevision: seed, config: old })).data.revision;
  const after = (await call(ROLES.owner, "GET", "/state")).data;
  assert.equal(after.draft.revision, fresh, "a draft saved after the rollback is the draft waiting");
  assert.deepEqual(after.draft.config, old);
});
