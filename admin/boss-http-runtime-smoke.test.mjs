import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createServer as createNetServer } from "node:net";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const token = "boss-http-smoke";

async function freePort() {
  const probe = createNetServer();
  await new Promise((resolveListen, reject) => {
    probe.once("error", reject);
    probe.listen(0, "127.0.0.1", resolveListen);
  });
  const address = probe.address();
  if (address === null || typeof address === "string") throw new Error("Could not allocate an ephemeral port.");
  const port = address.port;
  await new Promise((resolveClose, reject) => probe.close((error) => error ? reject(error) : resolveClose()));
  return port;
}

async function request(baseUrl, path, { method = "GET", body, auth = true } = {}) {
  const response = await fetch(`${baseUrl}${path}`, {
    method,
    headers: {
      accept: "application/json",
      ...(body === undefined ? {} : { "content-type": "application/json" }),
      ...(auth ? { "x-typing-game-admin-token": token } : {}),
    },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
  const payload = await response.json().catch(() => ({}));
  assert.ok(response.ok, `${method} ${path} failed (${response.status}): ${JSON.stringify(payload)}`);
  return payload;
}

async function waitForAdmin(baseUrl, child, stderr) {
  for (let attempt = 0; attempt < 80; attempt += 1) {
    if (child.exitCode !== null) throw new Error(`Admin server exited before startup (${child.exitCode}): ${stderr()}`);
    try {
      const response = await fetch(`${baseUrl}/api/admin/space-typing/state`, {
        headers: { "x-typing-game-admin-token": token },
      });
      if (response.ok) return;
    } catch {
      // Server socket is not listening yet.
    }
    await new Promise((resolveWait) => setTimeout(resolveWait, 50));
  }
  throw new Error(`Timed out waiting for Admin server: ${stderr()}`);
}

test("B06.5 HTTP Draft -> Validate -> Publish -> child preview -> Runtime -> Rollback smoke", async (t) => {
  const dataDir = await mkdtemp(join(tmpdir(), "typing-game-boss-http-"));
  const port = await freePort();
  const baseUrl = `http://127.0.0.1:${port}`;
  let serverStderr = "";
  const child = spawn(process.execPath, ["admin/server.mjs"], {
    cwd: root,
    env: {
      ...process.env,
      TYPING_GAME_ADMIN_DATA_DIR: dataDir,
      TYPING_GAME_ADMIN_PORT: String(port),
      TYPING_GAME_ADMIN_TOKEN: token,
    },
    stdio: ["ignore", "pipe", "pipe"],
  });
  child.stderr.setEncoding("utf8");
  child.stderr.on("data", (chunk) => { serverStderr += chunk; });
  t.after(async () => {
    if (child.exitCode === null) child.kill("SIGTERM");
    await new Promise((resolveExit) => {
      if (child.exitCode !== null) return resolveExit();
      child.once("exit", resolveExit);
      setTimeout(resolveExit, 1000).unref();
    });
    await rm(dataDir, { recursive: true, force: true });
  });

  await waitForAdmin(baseUrl, child, () => serverStderr);

  const initial = await request(baseUrl, "/api/admin/space-typing/state");
  const seedRevision = initial.active.revision;
  const seedRuntime = await request(baseUrl, "/api/runtime/space-typing/bosses", { auth: false });
  assert.equal(seedRuntime.activeRevision, seedRevision);
  assert.equal(seedRuntime.applyBoundary, "new-session");
  assert.deepEqual(seedRuntime.policy.bosses, {});

  const config = structuredClone(initial.active.config);
  config.content = {
    ...(config.content ?? {}),
    bosses: {
      configRevision: "bosses-http-smoke-v1",
      bosses: {
        "tyrant-g01": {
          name: "Aurora Regent",
          title: "Sovereign of the Runtime Gate",
        },
      },
    },
  };

  const previewBeforeDraft = await request(baseUrl, "/api/admin/space-typing/bosses/preview", {
    method: "POST",
    body: { policy: config.content.bosses },
  });
  assert.equal(previewBeforeDraft.configRevision, "bosses-http-smoke-v1");
  assert.equal(previewBeforeDraft.bosses.find((boss) => boss.id === "tyrant-g01")?.name, "Aurora Regent");

  const draft = await request(baseUrl, "/api/admin/space-typing/revisions", {
    method: "POST",
    body: {
      baseRevision: seedRevision,
      config,
      message: "B06.5 HTTP Boss smoke draft",
    },
  });

  const runtimeBeforePublish = await request(baseUrl, "/api/runtime/space-typing/bosses", { auth: false });
  assert.equal(runtimeBeforePublish.activeRevision, seedRevision, "Draft must not affect runtime before Publish.");
  assert.deepEqual(runtimeBeforePublish.policy.bosses, {});

  const validation = await request(baseUrl, "/api/admin/space-typing/validate-revision", {
    method: "POST",
    body: { revision: draft.revision },
  });
  assert.equal(validation.valid, true);
  assert.equal(validation.publishable, true);

  await request(baseUrl, "/api/admin/space-typing/publish", {
    method: "POST",
    body: { revision: draft.revision, expectedActiveRevision: seedRevision },
  });

  const publishedRuntime = await request(baseUrl, "/api/runtime/space-typing/bosses", { auth: false });
  assert.equal(publishedRuntime.activeRevision, draft.revision);
  assert.equal(publishedRuntime.applyBoundary, "new-session");
  assert.equal(publishedRuntime.policy.configRevision, "bosses-http-smoke-v1");
  assert.equal(publishedRuntime.policy.bosses["tyrant-g01"].name, "Aurora Regent");
  assert.equal(publishedRuntime.policy.bosses["tyrant-g01"].title, "Sovereign of the Runtime Gate");

  const childPreview = await request(baseUrl, "/api/admin/space-typing/bosses/preview", {
    method: "POST",
    body: { policy: publishedRuntime.policy },
  });
  const consumed = childPreview.bosses.find((boss) => boss.id === "tyrant-g01");
  assert.equal(childPreview.configRevision, "bosses-http-smoke-v1");
  assert.equal(consumed?.name, "Aurora Regent", "Pinned child preview must consume the published Boss policy.");
  assert.equal(consumed?.title, "Sovereign of the Runtime Gate");
  assert.equal(consumed?.overridden, true);

  await request(baseUrl, "/api/admin/space-typing/rollback", {
    method: "POST",
    body: { targetRevision: seedRevision, expectedActiveRevision: draft.revision },
  });

  const rolledBackRuntime = await request(baseUrl, "/api/runtime/space-typing/bosses", { auth: false });
  assert.equal(rolledBackRuntime.activeRevision, seedRevision);
  assert.deepEqual(rolledBackRuntime.policy.bosses, {});
});
