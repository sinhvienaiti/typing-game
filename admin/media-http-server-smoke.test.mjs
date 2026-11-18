import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createServer as createNetServer } from "node:net";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const token = "media-v2-http-smoke";

async function freePort() {
  const probe = createNetServer();
  await new Promise((ok, fail) => { probe.once("error", fail); probe.listen(0, "127.0.0.1", ok); });
  const address = probe.address();
  if (address === null || typeof address === "string") throw new Error("Could not allocate port");
  const port = address.port;
  await new Promise((ok, fail) => probe.close((error) => error ? fail(error) : ok()));
  return port;
}

async function waitForAdmin(base, child, stderr) {
  for (let index = 0; index < 120; index += 1) {
    if (child.exitCode !== null) throw new Error(`Admin exited (${child.exitCode}): ${stderr()}`);
    try {
      const response = await fetch(`${base}/api/admin/space-typing/state`, { headers: { "x-typing-game-admin-token": token } });
      if (response.ok) return;
    } catch {}
    await new Promise((resolveWait) => setTimeout(resolveWait, 50));
  }
  throw new Error(`Timed out waiting for Admin: ${stderr()}`);
}

function startAdmin(dataDir, port) {
  let stderr = "";
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
  child.stderr.on("data", (chunk) => { stderr += chunk; });
  return { child, stderr: () => stderr };
}

async function stopAdmin(child) {
  if (child.exitCode === null) child.kill("SIGTERM");
  await new Promise((resolveWait) => {
    if (child.exitCode !== null) return resolveWait();
    child.once("exit", resolveWait);
    setTimeout(resolveWait, 1000).unref();
  });
}

async function jsonRequest(base, path, { method = "GET", headers = {}, body, auth = true, expectedStatus = 200 } = {}) {
  const response = await fetch(`${base}${path}`, {
    method,
    headers: {
      accept: "application/json",
      ...(auth ? { "x-typing-game-admin-token": token } : {}),
      ...headers,
    },
    ...(body === undefined ? {} : { body }),
  });
  const payload = await response.json().catch(() => ({}));
  assert.equal(response.status, expectedStatus, `${method} ${path}: ${JSON.stringify(payload)}`);
  return payload;
}

test("Media V2 real Admin server bootstraps references, persists uploads and never mutates gameplay on upload", async (t) => {
  const dataDir = await mkdtemp(join(tmpdir(), "typing-game-media-http-server-"));
  t.after(() => rm(dataDir, { recursive: true, force: true }));

  let port = await freePort();
  let base = `http://127.0.0.1:${port}`;
  let running = startAdmin(dataDir, port);
  t.after(() => stopAdmin(running.child));
  await waitForAdmin(base, running.child, running.stderr);

  await jsonRequest(base, "/api/admin/space-typing/media/assets", { auth: false, expectedStatus: 401 });

  const beforeState = await jsonRequest(base, "/api/admin/space-typing/state");
  const bootstrapped = await jsonRequest(base, "/api/admin/space-typing/media/assets?includeArchived=true");
  assert.ok(bootstrapped.assets.some((asset) => asset.assetId === "runtime.ship-model.vanguard"));
  assert.ok(bootstrapped.assets.some((asset) => asset.kind === "music"));
  assert.ok(bootstrapped.assets.some((asset) => asset.kind === "sfx"));

  const uploadResponse = await fetch(`${base}/api/admin/space-typing/media/assets`, {
    method: "POST",
    headers: {
      "x-typing-game-admin-token": token,
      "x-media-kind": "image",
      "x-media-title": "A3.1 Smoke Portrait",
      "x-media-file-name": "smoke.png",
      "x-media-tags": "smoke,ships",
      "content-type": "image/png",
    },
    body: Buffer.from("a3.1-media-smoke-v1"),
  });
  assert.equal(uploadResponse.status, 201);
  const uploaded = await uploadResponse.json();
  assert.equal(uploaded.version.provenance, "admin-upload");

  const afterUploadState = await jsonRequest(base, "/api/admin/space-typing/state");
  assert.equal(afterUploadState.state.activeRevision, beforeState.state.activeRevision, "Media upload must not publish or mutate gameplay revision state");
  assert.equal(afterUploadState.state.generation, beforeState.state.generation, "Media upload must not advance gameplay generation");

  const blobResponse = await fetch(`${base}/api/admin/space-typing/media/blobs/${encodeURIComponent(uploaded.version.assetVersionId)}/primary`, {
    headers: { "x-typing-game-admin-token": token },
  });
  assert.equal(blobResponse.status, 200);
  assert.match(blobResponse.headers.get("cache-control") ?? "", /immutable/);
  assert.equal(Buffer.from(await blobResponse.arrayBuffer()).toString("utf8"), "a3.1-media-smoke-v1");

  const archived = await jsonRequest(base, `/api/admin/space-typing/media/assets/${encodeURIComponent(uploaded.asset.assetId)}/archive`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ archived: true }),
  });
  assert.equal(archived.lifecycle, "archived");
  const visible = await jsonRequest(base, "/api/admin/space-typing/media/assets");
  assert.ok(!visible.assets.some((asset) => asset.assetId === uploaded.asset.assetId));

  const audit = await jsonRequest(base, "/api/admin/space-typing/audit?limit=50");
  assert.ok(audit.events.some((event) => event.action === "media.asset.create" && event.result === "success"));
  assert.ok(audit.events.some((event) => event.action === "media.asset.archive" && event.result === "success"));

  const assetCountBeforeRestart = bootstrapped.assets.length + 1;
  await stopAdmin(running.child);
  port = await freePort();
  base = `http://127.0.0.1:${port}`;
  running = startAdmin(dataDir, port);
  await waitForAdmin(base, running.child, running.stderr);

  const afterRestart = await jsonRequest(base, "/api/admin/space-typing/media/assets?includeArchived=true");
  assert.equal(afterRestart.assets.length, assetCountBeforeRestart, "Restart bootstrap must reuse existing runtime versions instead of duplicating them");
  const persisted = afterRestart.assets.find((asset) => asset.assetId === uploaded.asset.assetId);
  assert.equal(persisted?.lifecycle, "archived", "Admin-owned asset metadata/blob must persist across restart");

  const afterRestartState = await jsonRequest(base, "/api/admin/space-typing/state");
  assert.equal(afterRestartState.state.activeRevision, beforeState.state.activeRevision);
  assert.equal(afterRestartState.state.generation, beforeState.state.generation);
});
