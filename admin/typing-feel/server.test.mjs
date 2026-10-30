// node --test admin/typing-feel/server.test.mjs
// Typing Feel through admin/server.mjs's real request listener (no socket),
// with Space Typing not checked out: token check, the start-up re-export of a
// stale catalogue, Draft → Validate → Publish → Rollback over HTTP and the
// no-token preview (docs/games/TYPING_FEEL_SERVICE.md §3.3, §3.12, §8.1).
import assert from "node:assert/strict";
import { readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { Readable } from "node:stream";
import test from "node:test";
import { activeConfig, makeTypingFeelFixture, readCatalogue } from "./fixture.mjs";

const TOKEN = "typing-feel-server-test";

async function startServer(t, fx, role = "super-admin") {
  const env = {
    TYPING_GAME_ADMIN_PORT: "0",
    TYPING_GAME_ADMIN_TOKEN: TOKEN,
    TYPING_GAME_ADMIN_ROLE: role,
    TYPING_GAME_ADMIN_PERMISSION_OVERRIDES: "",
    TYPING_GAME_ADMIN_SPACE_DIR: join(fx.base, "no-space-checkout"),
    TYPING_GAME_ADMIN_DATA_DIR: fx.dataDir,
    TYPING_GAME_ADMIN_SHARED_DIR: fx.sharedDir,
    TYPING_FEEL_PUBLIC_DIR: fx.publicDir,
  };
  const previous = Object.fromEntries(Object.keys(env).map((key) => [key, process.env[key]]));
  Object.assign(process.env, env);
  t.after(() => {
    for (const [key, value] of Object.entries(previous)) {
      if (value === undefined) delete process.env[key];
      else process.env[key] = value;
    }
  });
  const logs = { warn: t.mock.method(console, "warn", () => {}), log: t.mock.method(console, "log", () => {}), error: t.mock.method(console, "error", () => {}) };
  const { server } = await import(`../server.mjs?typing-feel=${role}-${Date.now()}`);
  const call = (method, path, { body, auth = true, host } = {}) => new Promise((done) => {
    const bytes = body === undefined ? [] : [Buffer.from(JSON.stringify(body))];
    const request = Readable.from(bytes);
    request.method = method;
    request.url = path;
    request.headers = { "content-type": "application/json", ...(auth ? { "x-typing-game-admin-token": TOKEN } : {}), ...(host ? { host } : {}) };
    const chunks = [];
    const response = {
      writeHead(status, headers = {}) {
        this.status = status;
        this.headers = Object.fromEntries(Object.entries(headers).map(([key, value]) => [key.toLowerCase(), value]));
      },
      end(value) {
        if (value !== undefined) chunks.push(Buffer.isBuffer(value) ? value : Buffer.from(String(value)));
        const raw = Buffer.concat(chunks);
        let data = null;
        try {
          data = JSON.parse(raw.toString("utf8"));
        } catch { /* audio */ }
        done({ status: this.status, headers: this.headers, raw, data });
      },
    };
    server.emit("request", request, response);
  });
  return { call, logs };
}

test("Typing Feel runs through the Admin server without Space Typing", { timeout: 20000 }, async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const r1 = await readCatalogue(fx.publicDir);
  const { revision: seed, config } = await activeConfig(fx.store);

  // The server last stopped between the store switch and the rename: the store says D, the disk still says r1.
  config.keyboard.defaultSet = "deep";
  const before = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: before.revision, expectedActiveRevision: seed });
  const published = await readCatalogue(fx.publicDir);
  await writeFile(join(fx.publicDir, "v1/keys/keys-manifest.json"), r1);

  const { call, logs } = await startServer(t, fx);
  assert.equal(await readCatalogue(fx.publicDir), published, "start-up re-exported the active revision");
  assert.ok(logs.log.mock.calls.some((entry) => /Typing Feel: re-exported/.test(String(entry.arguments[0]))));

  for (const path of ["/api/admin/shared/typing-feel/state", "/api/admin/shared/typing-feel/draft"]) {
    assert.equal((await call("GET", path, { auth: false })).status, 401, `${path} needs the token`);
  }
  assert.equal((await call("POST", "/api/admin/shared/typing-feel/publish", { auth: false, body: { revision: before.revision, expectedActiveRevision: seed } })).status, 401);
  const state = await call("GET", "/api/admin/shared/typing-feel/state");
  assert.equal(state.status, 200);
  assert.equal(state.data.state.activeRevision, before.revision);
  assert.equal(state.data.startup.status, "re-exported");
  assert.equal(state.data.local.matchesActive, true);
  assert.equal((await call("GET", "/api/admin/shared/status")).data.spaceAvailable, false);
  assert.equal((await call("GET", "/api/admin/space-typing/state")).status, 503, "Space routes are off, Typing Feel is not");

  // Draft → Review → Publish → Rollback over HTTP.
  const next = structuredClone(config);
  next.keyboard.sets.find((set) => set.id === "raindrop-tile").enabled = false;
  next.effects.defaults.intensity = "low";
  const draft = await call("POST", "/api/admin/shared/typing-feel/revisions", { body: { baseRevision: before.revision, config: next, message: "Hide Raindrop Tile" } });
  assert.equal(draft.status, 201, JSON.stringify(draft.data));
  const review = await call("POST", "/api/admin/shared/typing-feel/validate-revision", { body: { revision: draft.data.revision } });
  assert.equal(review.data.valid, true);
  assert.deepEqual(review.data.changeScope.hidden, ["raindrop-tile"]);
  const preview = await call("GET", `${review.data.previewBase}keys-manifest.json`, { auth: false });
  assert.equal(preview.status, 200, "the preview needs no token");
  assert.ok(!preview.data.profiles.some((profile) => profile.id === "raindrop-tile"));
  const audio = await call("GET", `${review.data.previewBase}${preview.data.profiles[0].preview}`, { auth: false });
  assert.equal(audio.status, 200);
  assert.equal(audio.headers["content-type"], "audio/ogg");

  const publish = await call("POST", "/api/admin/shared/typing-feel/publish", { body: { revision: draft.data.revision, expectedActiveRevision: before.revision } });
  assert.equal(publish.status, 200, JSON.stringify(publish.data));
  const live = JSON.parse(await readCatalogue(fx.publicDir));
  assert.equal(live.revision, draft.data.revision);
  assert.equal(live.effects.intensity, "low");
  const again = await call("POST", "/api/admin/shared/typing-feel/publish", { body: { revision: draft.data.revision, expectedActiveRevision: before.revision } });
  assert.equal(again.status, 409, "a second Publish of the same draft is a conflict");
  const rollback = await call("POST", "/api/admin/shared/typing-feel/rollback", { body: { targetRevision: before.revision, expectedActiveRevision: draft.data.revision } });
  assert.equal(rollback.status, 200);
  assert.equal(await readCatalogue(fx.publicDir), published, "Rollback restores the previous catalogue bytes");

  const history = await call("GET", "/api/admin/shared/typing-feel/history");
  assert.deepEqual(history.data.events.filter((event) => event.result === "success").map((event) => event.action).sort(), ["typing-feel.publish", "typing-feel.revision.create", "typing-feel.rollback"]);
  const audit = JSON.parse((await readFile(join(fx.dataDir, "audit/events.jsonl"), "utf8")).trim().split("\n").at(-1));
  assert.equal(audit.domain, "typing-feel", "Typing Feel uses the shared audit log under its own domain");
  const status = await call("GET", "/api/admin/shared/typing-feel/export/status");
  assert.equal(status.data.local.revision, before.revision, "the local row reads the catalogue after the rollback");
  assert.equal(status.data.git.status, "outside-repository", "a temp published folder is not in Git");
  assert.equal(status.data.online.status, "not-configured");
});

test("a viewer reads Typing Feel but cannot publish to all games", { timeout: 20000 }, async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { call } = await startServer(t, fx, "viewer");
  const state = await call("GET", "/api/admin/shared/typing-feel/state");
  assert.equal(state.status, 200);
  assert.deepEqual(state.data.permissions, { draft: false, publish: false, rollback: false });
  const { revision, config } = await activeConfig(fx.store);
  assert.equal((await call("POST", "/api/admin/shared/typing-feel/revisions", { body: { baseRevision: revision, config } })).status, 403);
  const draft = await fx.service.saveDraft({ baseRevision: revision, config: { ...config, keyboard: { ...config.keyboard, defaultSet: "deep" } } });
  const refused = await call("POST", "/api/admin/shared/typing-feel/publish", { body: { revision: draft.revision, expectedActiveRevision: revision } });
  assert.equal(refused.status, 403);
  assert.equal(refused.data.permission, "shared.publish");
  assert.equal(JSON.parse(await readCatalogue(fx.publicDir)).revision, "r1");
});

test("Admin routes answer only local host names (a DNS-rebinding page sends its own)", { timeout: 20000 }, async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { revision, config } = await activeConfig(fx.store);
  const draft = await fx.service.saveDraft({ baseRevision: revision, config: { ...config, keyboard: { ...config.keyboard, defaultSet: "deep" } } });
  const { call } = await startServer(t, fx);
  for (const host of ["evil.example:3199", "attacker.test", "192.168.1.20:3199"]) {
    const refused = await call("POST", "/api/admin/shared/typing-feel/publish", { host, body: { revision: draft.revision, expectedActiveRevision: revision } });
    assert.equal(refused.status, 403, host);
    assert.equal(refused.data.error, "forbidden-host");
    assert.equal((await call("GET", "/api/runtime/typing-feel/preview/seed-v1/keys/keys-manifest.json", { host, auth: false })).status, 403, host);
  }
  assert.equal(JSON.parse(await readCatalogue(fx.publicDir)).revision, "r1", "nothing was published");
  for (const host of ["127.0.0.1:3199", "localhost:3100", "[::1]:3199", "typing-game.local", "admin.localhost:3199"]) {
    assert.equal((await call("GET", "/api/admin/shared/typing-feel/state", { host })).status, 200, host);
  }
});
