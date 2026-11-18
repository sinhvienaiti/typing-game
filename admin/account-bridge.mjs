import { ADMIN_PERMISSIONS, requireAdminPermission, runAuthorizedAdminMutation } from "./admin-security.mjs";

/**
 * Players & Live-ops bridge: /api/admin/space-typing/accounts/* → the Space
 * Typing online API (games/space-typing/cloud: Cloudflare Worker + D1 +
 * Durable Objects; locally `pnpm account:local` on 127.0.0.1:3016) at
 * /internal/admin/*. This server owns who may do what (role permissions)
 * and writes the Admin audit entry; the account service keeps its own
 * audit table with the same actor.
 *
 * Each route has its own permission (ROUTES below); anything else is 404.
 * players.read never reveals save files, reset links or the email outbox.
 */
const PREFIX = "/api/admin/space-typing/accounts";

export function createAccountAdminHttpHandler({
  auditLog,
  onAuditError = () => undefined,
  baseUrl = process.env.ACCOUNT_SERVICE_URL || "http://127.0.0.1:3016",
  token = process.env.ACCOUNT_ADMIN_TOKEN || "local-account-admin",
  fetchImpl = fetch,
  /** True when this Admin still runs on the default or a short TYPING_GAME_ADMIN_TOKEN. */
  adminTokenWeak = false,
} = {}) {
  // Real player data (a deployed Worker) needs a strong Admin token: with
  // the default one, anyone who reaches this Admin could ban players,
  // restore saves or read reset links. Local development is unaffected.
  const remote = !/^https?:\/\/(127\.0\.0\.1|localhost|\[::1\])(:\d+)?(\/|$)/i.test(baseUrl);
  const blockedReason = !remote
    ? null
    : adminTokenWeak
      ? "This Admin manages a deployed Worker but still uses a weak TYPING_GAME_ADMIN_TOKEN. Set a random token of 24+ characters (openssl rand -base64 32) and restart Admin."
      : token === "local-account-admin"
        ? "Set ACCOUNT_ADMIN_TOKEN to the Worker's ADMIN_TOKEN secret before managing a deployed Worker."
        : null;
  async function forward(method, path, search, actor, body) {
    let response;
    try {
      response = await fetchImpl(baseUrl + "/internal/admin" + path + search, {
        method,
        headers: {
          "content-type": "application/json",
          "x-account-admin-token": token,
          "x-admin-actor": `${actor.actorDisplayName ?? actor.actorId ?? "admin"} (${actor.role ?? "?"})`,
        },
        body: body === undefined ? undefined : JSON.stringify(body),
        signal: AbortSignal.timeout(10_000),
      });
    } catch {
      return {
        status: 503,
        payload: {
          error: "account-service-offline",
          message: "Online API is not running. Start it with: pnpm --dir games/space-typing account:local",
        },
      };
    }
    const text = await response.text();
    let payload;
    try {
      payload = text ? JSON.parse(text) : {};
    } catch {
      payload = { error: "bad-response", message: text.slice(0, 200) };
    }
    return { status: response.status, payload };
  }

  async function readBody(request) {
    const chunks = [];
    let size = 0;
    for await (const chunk of request) {
      size += chunk.length;
      if (size > 64 * 1024) throw Object.assign(new Error("Request body too large."), { status: 413 });
      chunks.push(chunk);
    }
    if (size === 0) return {};
    return JSON.parse(Buffer.concat(chunks).toString("utf8"));
  }

  /** Every allowed route with its permission; anything else is 404. */
  const ID = "[0-9a-f-]{36}";
  const ROUTES = [
    ["GET", /^\/stats$/, ADMIN_PERMISSIONS.PLAYERS_READ],
    ["GET", /^\/players$/, ADMIN_PERMISSIONS.PLAYERS_READ],
    ["GET", new RegExp(`^/players/${ID}$`), ADMIN_PERMISSIONS.PLAYERS_READ],
    ["GET", new RegExp(`^/players/${ID}/save$`), ADMIN_PERMISSIONS.PLAYERS_SAVE],
    ["POST", new RegExp(`^/players/${ID}/(ban|unban|sessions/revoke)$`), ADMIN_PERMISSIONS.PLAYERS_MODERATE],
    ["POST", new RegExp(`^/players/${ID}/mute$`), ADMIN_PERMISSIONS.CHAT_MODERATE],
    ["GET", /^\/chat\/recent$/, ADMIN_PERMISSIONS.CHAT_MODERATE],
    ["POST", /^\/chat\/delete$/, ADMIN_PERMISSIONS.CHAT_MODERATE],
    ["GET", /^\/chat\/reports$/, ADMIN_PERMISSIONS.CHAT_MODERATE],
    ["POST", /^\/chat\/reports\/\d+\/resolve$/, ADMIN_PERMISSIONS.CHAT_MODERATE],
    ["POST", /^\/chat\/announce$/, ADMIN_PERMISSIONS.LIVEOPS_MAIL],
    ["POST", new RegExp(`^/players/${ID}/save/restore$`), ADMIN_PERMISSIONS.PLAYERS_SAVE],
    // Server wallet correction (signed amounts, Warp, a reason); same trust level as restoring a save.
    ["POST", new RegExp(`^/players/${ID}/wallet$`), ADMIN_PERMISSIONS.PLAYERS_SAVE],
    ["POST", new RegExp(`^/players/${ID}/password-reset-link$`), ADMIN_PERMISSIONS.PLAYERS_CREDENTIALS],
    ["POST", new RegExp(`^/players/${ID}/mail$`), ADMIN_PERMISSIONS.LIVEOPS_MAIL],
    ["GET", /^\/mail$/, ADMIN_PERMISSIONS.PLAYERS_READ],
    ["POST", /^\/mail$/, ADMIN_PERMISSIONS.LIVEOPS_MAIL],
    ["POST", new RegExp(`^/mail/${ID}/revoke$`), ADMIN_PERMISSIONS.LIVEOPS_MAIL],
    ["GET", /^\/gift-codes$/, ADMIN_PERMISSIONS.PLAYERS_READ],
    ["POST", /^\/gift-codes$/, ADMIN_PERMISSIONS.LIVEOPS_MAIL],
    ["POST", new RegExp(`^/gift-codes/${ID}/disable$`), ADMIN_PERMISSIONS.LIVEOPS_MAIL],
    // Emails carry verification and reset links.
    ["GET", /^\/outbox$/, ADMIN_PERMISSIONS.PLAYERS_CREDENTIALS],
    ["GET", /^\/audit$/, ADMIN_PERMISSIONS.AUDIT_READ],
    // Player feedback and bug reports; a reply is a plain in-game letter (no reward).
    ["GET", /^\/feedback$/, ADMIN_PERMISSIONS.FEEDBACK_READ],
    ["POST", new RegExp(`^/feedback/${ID}/(status|reply)$`), ADMIN_PERMISSIONS.FEEDBACK_MANAGE],
    // Deletes only expired sessions, links and rate-limit rows (the daily cron runs the same).
    ["POST", /^\/maintenance$/, ADMIN_PERMISSIONS.PLAYERS_MODERATE],
  ];

  function permissionFor(method, path) {
    return ROUTES.find(([routeMethod, pattern]) => routeMethod === method && pattern.test(path))?.[2] ?? null;
  }

  /** Returns true when the request was handled. */
  return async function handleAccountAdminRequest({ request, response, url, actor }) {
    if (!url.pathname.startsWith(PREFIX + "/") && url.pathname !== PREFIX) return false;
    const path = url.pathname.slice(PREFIX.length) || "/";
    const method = request.method || "GET";
    const send = (status, payload) => {
      const data = JSON.stringify(payload);
      response.writeHead(status, { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", "content-length": Buffer.byteLength(data) });
      response.end(data);
    };
    const permission = permissionFor(method, path);
    if (permission === null) {
      send(404, { error: "not-found", message: "Unknown accounts endpoint." });
      return true;
    }
    if (blockedReason !== null) {
      send(403, { error: "weak-admin-token", message: blockedReason });
      return true;
    }
    if (method === "GET") {
      requireAdminPermission(actor, permission);
      const result = await forward("GET", path, url.search, actor);
      send(result.status, result.payload);
      return true;
    }
    let body;
    try {
      body = await readBody(request);
    } catch (error) {
      send(error?.status === 413 ? 413 : 400, { error: "bad-request", message: error?.status === 413 ? "Request body too large." : "Request body must be valid JSON." });
      return true;
    }
    const segments = path.split("/").filter(Boolean);
    const result = await runAuthorizedAdminMutation({
      actor,
      permission,
      auditLog,
      onAuditError,
      action: "accounts." + segments.filter((part) => !/^[0-9a-f-]{36}$/.test(part)).join("."),
      domain: "accounts",
      entityType: segments[0] ?? null,
      entityId: segments[1] ?? null,
      // Never copy reward text or codes into the change scope verbatim beyond what support needs.
      changeScope: { reason: typeof body.reason === "string" ? body.reason.slice(0, 120) : null, title: typeof body.title === "string" ? body.title.slice(0, 120) : null },
      operation: async () => {
        const forwarded = await forward("POST", path, "", actor, body);
        if (forwarded.status >= 400) {
          const error = new Error(forwarded.payload?.message || "Account service refused the request.");
          error.status = forwarded.status;
          error.payload = forwarded.payload;
          throw error;
        }
        return forwarded;
      },
    }).catch((error) => {
      if (error?.payload) return { status: error.status, payload: error.payload };
      throw error;
    });
    send(result.status, result.payload);
    return true;
  };
}
