import assert from "node:assert/strict";
import { Readable } from "node:stream";
import { mkdtemp, rm, mkdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { resolve } from "node:path";
import test from "node:test";
import { readSharedOverview } from "./shared-overview.mjs";
import { ADMIN_PERMISSION_CATALOG, createLocalAdminActor } from "./admin-security.mjs";

const root = resolve(import.meta.dirname, "..");
const UNAVAILABLE = {
  present: null,
  missing: { error: "space-typing-not-checked-out" },
  failed: { error: "space-typing-unavailable" },
};

// Exercise the real server request listener without binding a network socket.
// space: "present" (this checkout), "missing" (no Space dir) or "failed" (contracts present, start-up throws).
async function startServer(t, space) {
  const dir = await mkdtemp(resolve(tmpdir(), "admin-shared-ia-"));
  const spaceDir = {
    present: resolve(root, "games/space-typing"),
    missing: resolve(dir, "absent-space"),
    failed: resolve(dir, "broken-space"),
  }[space];
  if (space === "failed") {
    await mkdir(resolve(spaceDir, "contracts"), { recursive: true });
    await writeFile(resolve(spaceDir, "contracts/space-typing-admin.v1.json"), "{ half-written");
  }
  const env = {
    TYPING_GAME_ADMIN_PORT: "0", TYPING_GAME_ADMIN_DATA_DIR: dir,
    TYPING_GAME_ADMIN_TOKEN: "shared-ia-test", TYPING_GAME_ADMIN_ROLE: "super-admin",
    TYPING_GAME_ADMIN_PERMISSION_OVERRIDES: "",
    TYPING_GAME_ADMIN_SPACE_DIR: spaceDir,
  };
  const previous = Object.fromEntries(Object.keys(env).map((key) => [key, process.env[key]]));
  Object.assign(process.env, env);
  t.after(async () => {
    for (const [key, value] of Object.entries(previous)) {
      if (value === undefined) delete process.env[key]; else process.env[key] = value;
    }
    await rm(dir, { recursive: true, force: true });
  });
  // Start-up logs go to console.warn (missing) or console.error (failed); capture them for the assertions.
  const logs = { warn: t.mock.method(console, "warn", () => {}), error: t.mock.method(console, "error", () => {}) };
  const { server } = await import(`./server.mjs?shared-ia=${space}`);
  const get = (path, auth = true) => new Promise((done) => {
    const request = Readable.from([]);
    request.method = "GET";
    request.url = path;
    request.headers = auth ? { "x-typing-game-admin-token": "shared-ia-test" } : {};
    const response = {
      writeHead(status) { this.status = status; },
      end(value) { done({ status: this.status, data: JSON.parse(value) }); },
    };
    server.emit("request", request, response);
  });
  return { get, logs };
}

for (const space of ["present", "missing", "failed"]) {
  test(`shared Admin and Media V2 run with Space ${space}`, { timeout: 20000 }, async (t) => {
    const { get, logs } = await startServer(t, space);
    const available = space === "present";
    const spaceStatus = { present: "available", missing: "not-checked-out", failed: "failed" }[space];
    for (const path of ["/api/admin/shared/status", "/api/admin/shared/overview", "/api/admin/shared/learning-content/catalog", "/api/admin/shared/actor", "/api/admin/space-typing/media/assets"]) {
      assert.equal((await get(path, false)).status, 401, `${path} requires a token`);
    }
    assert.deepEqual(await get("/api/admin/shared/status"), { status: 200, data: { spaceAvailable: available, spaceStatus } });
    const overview = await get("/api/admin/shared/overview");
    assert.equal(overview.status, 200);
    assert.equal(overview.data.spaceAvailable, available);
    assert.equal(overview.data.spaceStatus, spaceStatus);
    assert.equal(overview.data.consumers.length, 4);
    assert.equal(overview.data.consumersError, null);
    assert.deepEqual(overview.data.consumers.map((row) => row.readsTypingFeel), [false, false, false, false]);
    const content = await get("/api/admin/shared/learning-content/catalog");
    assert.equal(content.status, 200);
    assert.ok(content.data.canonicalTotals.vocabulary > 0);
    assert.deepEqual(await get("/api/admin/space-typing/typing-content/catalog"), content, "Old content API is a shared alias, including without Space");
    const actor = await get("/api/admin/shared/actor");
    assert.equal(actor.status, 200);
    assert.ok(actor.data.permissions.includes("shared.publish"));
    for (const path of ["/api/admin/space-typing/contract", "/api/admin/space-typing/state", "/api/admin/space-typing/actor", "/api/runtime/space-typing/ships", "/api/runtime/space-typing/equipment"]) {
      const result = await get(path);
      assert.equal(result.status, available ? 200 : 503, path);
      if (!available) assert.deepEqual(result.data, UNAVAILABLE[space], path);
    }
    const media = await get("/api/admin/space-typing/media/assets");
    assert.equal(media.status, 200);
    // A missing media ID is still handled by Media V2, not the Space availability guard.
    assert.equal((await get("/api/runtime/space-typing/media/assets/unknown", false)).status, 404);
    if (!available) assert.deepEqual((await get("/api/runtime/space-typing/unknown", false)).data, UNAVAILABLE[space]);
    // Only a real start-up failure is an error with its stack; a missing checkout is a warning.
    const startupErrors = logs.error.mock.calls.filter((call) => String(call.arguments[0]).includes("Space Typing failed to start"));
    assert.equal(startupErrors.length, space === "failed" ? 1 : 0);
    if (space === "failed") assert.match(String(startupErrors[0].arguments[1]), /SyntaxError[\s\S]*\n\s+at /, "the stack is logged");
    const notCheckedOut = logs.warn.mock.calls.filter((call) => String(call.arguments[0]).includes("Space Typing is not checked out"));
    assert.equal(notCheckedOut.length, space === "missing" ? 1 : 0);
  });
}

async function overviewRoot(t) {
  const dir = await mkdtemp(resolve(tmpdir(), "admin-overview-"));
  t.after(() => rm(dir, { recursive: true, force: true }));
  await mkdir(resolve(dir, "admin/typing-feel"), { recursive: true });
  await mkdir(resolve(dir, "typing-feel/public/v1/keys"), { recursive: true });
  const write = (path, text) => writeFile(resolve(dir, path), text);
  return { dir, write };
}
const MANIFEST = "typing-feel/public/v1/keys/keys-manifest.json";
const CONSUMERS = "admin/typing-feel/consumers.json";

test("shared overview reads an optional imported catalogue", async (t) => {
  const { dir, write } = await overviewRoot(t);
  await write(CONSUMERS, "[]");
  assert.equal((await readSharedOverview({ rootDir: dir, spaceAvailable: false })).catalogue, null);
  await write(MANIFEST, JSON.stringify({ schema: "typing-feel/catalogue-3", revision: "fixture-r1", profiles: [{ id: "a" }, { id: "b" }] }));
  assert.deepEqual((await readSharedOverview({ rootDir: dir, spaceAvailable: true })).catalogue, { status: "imported", revision: "fixture-r1", setCount: 2 });
});

test("an invalid catalogue is data, not a failure: consumers and Space status still come back", async (t) => {
  const { dir, write } = await overviewRoot(t);
  await write(CONSUMERS, JSON.stringify([{ id: "survival", name: "Last Line", host: "survival.typing-game.local", readsTypingFeel: false }]));
  for (const manifest of ['{ "revision": "half-writ', JSON.stringify({ revision: "r1", profiles: "not-a-list" })]) {
    await write(MANIFEST, manifest);
    const overview = await readSharedOverview({ rootDir: dir, spaceAvailable: true, spaceStatus: "available" });
    assert.equal(overview.catalogue.status, "invalid");
    assert.equal(typeof overview.catalogue.message, "string");
    assert.ok(overview.catalogue.message.length > 0);
    assert.equal(overview.consumers.length, 1);
    assert.equal(overview.consumersError, null);
    assert.equal(overview.spaceAvailable, true);
    assert.equal(overview.spaceStatus, "available");
  }
});

test("a missing or invalid consumers.json is reported, the rest of the overview still comes back", async (t) => {
  const { dir, write } = await overviewRoot(t);
  await write(MANIFEST, JSON.stringify({ revision: "r2", profiles: [{ id: "a" }] }));
  const missing = await readSharedOverview({ rootDir: dir, spaceAvailable: false, spaceStatus: "failed" });
  assert.deepEqual(missing.consumers, []);
  assert.equal(missing.consumersError.status, "missing");
  assert.deepEqual(missing.catalogue, { status: "imported", revision: "r2", setCount: 1 });
  assert.equal(missing.spaceAvailable, false);
  assert.equal(missing.spaceStatus, "failed");
  for (const text of ["{ not json", JSON.stringify({ games: [] })]) {
    await write(CONSUMERS, text);
    const invalid = await readSharedOverview({ rootDir: dir, spaceAvailable: false });
    assert.deepEqual(invalid.consumers, []);
    assert.equal(invalid.consumersError.status, "invalid");
    assert.equal(invalid.spaceStatus, "not-checked-out");
  }
});

test("shared.publish is dangerous and distinct from Space publishing", () => {
  assert.equal(ADMIN_PERMISSION_CATALOG.find((entry) => entry.id === "shared.publish").dangerous, true);
  assert.ok(createLocalAdminActor({ role: "super-admin" }).permissions.includes("shared.publish"));
  assert.ok(createLocalAdminActor({ role: "publisher" }).permissions.includes("shared.publish"));
  assert.ok(!createLocalAdminActor({ role: "editor", permissionOverrideText: "+config.publish" }).permissions.includes("shared.publish"));
});
