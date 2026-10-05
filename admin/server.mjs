import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { RevisionStore, AdminConflictError, AdminValidationError } from "./store.mjs";
import { createDefaultSpaceTypingConfig } from "./default-config.mjs";
import { runWorldMusicPreview, WorldMusicPreviewError } from "./world-music-preview.mjs";
import {
  QaSessionNotFoundError,
  QaSessionStore,
  QaSessionValidationError,
} from "./qa-sessions.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contractPath = resolve(root, "../games/space-typing/contracts/space-typing-admin.v1.json");
const contract = JSON.parse(await readFile(contractPath, "utf8"));
const store = new RevisionStore({
  rootDir: process.env.TYPING_GAME_ADMIN_DATA_DIR || resolve(root, "../.local/admin/space-typing"),
  contract,
});
await store.initialize(createDefaultSpaceTypingConfig(contract));
const qaSessions = new QaSessionStore();

const host = "127.0.0.1";
const port = Number.parseInt(process.env.TYPING_GAME_ADMIN_PORT || "3199", 10);
const token = process.env.TYPING_GAME_ADMIN_TOKEN || "local-dev";

function json(response, status, body) {
  const data = JSON.stringify(body);
  response.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "content-length": Buffer.byteLength(data),
  });
  response.end(data);
}

async function body(request) {
  const chunks = [];
  let size = 0;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > 1024 * 1024) throw new AdminValidationError("Request body too large.");
    chunks.push(chunk);
  }
  if (chunks.length === 0) return {};
  try {
    return JSON.parse(Buffer.concat(chunks).toString("utf8"));
  } catch {
    throw new AdminValidationError("Request body must be valid JSON.");
  }
}

function authorized(request) {
  return request.headers["x-typing-game-admin-token"] === token;
}

const QA_CONSUME_PATH = "/api/admin/space-typing/qa/consume";
const QA_REVOKE_PATTERN = /^\/api\/admin\/space-typing\/qa\/sessions\/([^/]+)\/revoke$/;

const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url || "/", `http://${host}:${port}`);
    if (!url.pathname.startsWith("/api/admin/")) {
      json(response, 404, { error: "not-found" });
      return;
    }

    // Capability exchange is intentionally the only unauthenticated Admin-service
    // endpoint. It still requires an unguessable bearer bound to runtime session
    // and environment; the Admin token is never exposed to the game process.
    if (request.method === "POST" && url.pathname === QA_CONSUME_PATH) {
      const capability = qaSessions.consume(await body(request));
      json(response, 200, capability);
      return;
    }

    if (!authorized(request)) {
      json(response, 401, { error: "unauthorized" });
      return;
    }

    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/contract") {
      json(response, 200, contract);
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/state") {
      const state = await store.getState();
      const active = await store.getActiveRevision();
      const history = await store.listRevisions();
      json(response, 200, { state, active, history });
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/runtime") {
      json(response, 200, {
        activeRevision: (await store.getState()).activeRevision,
        config: await store.getRuntimeConfig(),
      });
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/qa/sessions") {
      json(response, 200, { sessions: qaSessions.list() });
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/qa/sessions") {
      const issued = qaSessions.issue(await body(request), "admin:local");
      json(response, 201, issued);
      return;
    }
    const qaRevokeMatch = request.method === "POST" ? url.pathname.match(QA_REVOKE_PATTERN) : null;
    if (qaRevokeMatch) {
      json(response, 200, qaSessions.revoke(decodeURIComponent(qaRevokeMatch[1])));
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/world-music/preview") {
      const input = await body(request);
      const activeConfig = await store.getRuntimeConfig();
      const publishedPolicy = input.publishedPolicy ?? activeConfig.worldMusic?.publishedPolicy;
      const preview = await runWorldMusicPreview({
        rootDir: root,
        contract,
        publishedPolicy,
        musicMode: input.musicMode ?? "map",
      });
      json(response, 200, preview);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {
      const input = await body(request);
      store.validateConfig(input.config);
      const publishedPolicy = input.config?.worldMusic?.publishedPolicy;
      if (publishedPolicy !== undefined) {
        await runWorldMusicPreview({
          rootDir: root,
          contract,
          publishedPolicy,
          musicMode: "map",
        });
      }
      const revision = await store.createRevision(input);
      json(response, 201, revision);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/publish") {
      const input = await body(request);
      const state = await store.publish(input);
      json(response, 200, state);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/rollback") {
      const input = await body(request);
      const state = await store.rollback(input);
      json(response, 200, state);
      return;
    }

    json(response, 404, { error: "not-found" });
  } catch (error) {
    if (error instanceof AdminConflictError) {
      json(response, 409, { error: "conflict", message: error.message });
      return;
    }
    if (error instanceof AdminValidationError || error instanceof QaSessionValidationError) {
      json(response, 400, { error: "validation", message: error.message });
      return;
    }
    if (error instanceof QaSessionNotFoundError) {
      json(response, 404, { error: "qa-session-unavailable", message: error.message });
      return;
    }
    if (error instanceof WorldMusicPreviewError) {
      json(response, 502, { error: "preview-error", message: error.message });
      return;
    }
    console.error(error);
    json(response, 500, { error: "internal-error" });
  }
});

server.listen(port, host, () => {
  console.log(`Space Typing Admin service: http://${host}:${port}`);
  if (token === "local-dev") {
    console.log("Admin auth token: local-dev (local development default)");
  }
});
