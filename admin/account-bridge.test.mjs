import assert from "node:assert/strict";
import test from "node:test";
import { createAccountAdminHttpHandler } from "./account-bridge.mjs";
import { createLocalAdminActor, isWeakAdminToken, sameAdminToken } from "./admin-security.mjs";

function call(handler, method, path) {
  return new Promise((resolve, reject) => {
    const response = {
      status: 0,
      writeHead(status) { this.status = status; },
      end(data) { resolve({ status: this.status, body: JSON.parse(data) }); },
    };
    const request = { method, headers: {}, async *[Symbol.asyncIterator]() {} };
    handler({ request, response, url: new URL("http://admin" + path), actor: createLocalAdminActor() }).catch(reject);
  });
}

test("admin tokens compare in constant time and weak ones are flagged", () => {
  assert.equal(sameAdminToken("abc", "abc"), true);
  assert.equal(sameAdminToken("abc", "abd"), false);
  assert.equal(sameAdminToken(undefined, "abc"), false);
  assert.equal(isWeakAdminToken("local-dev"), true);
  assert.equal(isWeakAdminToken("short"), true);
  assert.equal(isWeakAdminToken("x".repeat(32)), false);
});

function post(handler, path, body, actor) {
  return new Promise((resolve, reject) => {
    const response = {
      status: 0,
      writeHead(status) { this.status = status; },
      end(data) { resolve({ status: this.status, body: JSON.parse(data) }); },
    };
    const request = { method: "POST", headers: {}, async *[Symbol.asyncIterator]() { yield Buffer.from(JSON.stringify(body)); } };
    handler({ request, response, url: new URL("http://admin" + path), actor }).catch(reject);
  });
}

test("server wallet corrections need players.save and reach the Worker with their reason", async () => {
  const forwarded = [];
  const fetchImpl = async (url, init) => {
    forwarded.push({ url, body: JSON.parse(init.body) });
    return new Response(JSON.stringify({ balances: { credits: 5 } }), { status: 200 });
  };
  const handler = createAccountAdminHttpHandler({ baseUrl: "http://127.0.0.1:3016", fetchImpl, auditLog: { record: async () => {} } });
  const id = "00000000-0000-4000-8000-000000000001";
  const path = `/api/admin/space-typing/accounts/players/${id}/wallet`;
  const body = { deltas: { credits: 5 }, reason: "compensation" };
  await assert.rejects(post(handler, path, body, createLocalAdminActor({ role: "liveops" })));
  assert.equal(forwarded.length, 0);
  const done = await post(handler, path, body, createLocalAdminActor({ role: "support" }));
  assert.equal(done.status, 200);
  assert.deepEqual(forwarded, [{ url: `http://127.0.0.1:3016/internal/admin/players/${id}/wallet`, body }]);
});

test("a deployed Worker is refused while Admin runs on a weak token", async () => {
  let forwarded = 0;
  const fetchImpl = async () => { forwarded += 1; return new Response("{}"); };
  const remoteWeak = createAccountAdminHttpHandler({ baseUrl: "https://space-typing-api.example.workers.dev", token: "worker-secret", adminTokenWeak: true, fetchImpl });
  const blocked = await call(remoteWeak, "GET", "/api/admin/space-typing/accounts/players?q=a");
  assert.equal(blocked.status, 403);
  assert.equal(blocked.body.error, "weak-admin-token");
  const remoteDefault = createAccountAdminHttpHandler({ baseUrl: "https://space-typing-api.example.workers.dev", adminTokenWeak: false, fetchImpl });
  assert.equal((await call(remoteDefault, "GET", "/api/admin/space-typing/accounts/players?q=a")).status, 403);
  assert.equal(forwarded, 0);
  const local = createAccountAdminHttpHandler({ baseUrl: "http://127.0.0.1:3016", adminTokenWeak: true, fetchImpl });
  assert.equal((await call(local, "GET", "/api/admin/space-typing/accounts/players?q=a")).status, 200);
  assert.equal(forwarded, 1);
});
